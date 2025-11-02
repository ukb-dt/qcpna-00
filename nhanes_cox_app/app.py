from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import traceback

app = Flask(__name__)

try:
    model_data = joblib.load('cox_model.joblib')
    cph = model_data['model']
    feature_cols = model_data['feature_cols']
    feature_means = model_data['feature_means']
    use_real_model = True
    print("✓ SEROTONIN MODE: Real model loaded")
except:
    use_real_model = False
    print("⚡ DOPAMINE MODE: Using simulated curves")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_curve', methods=['POST'])
def generate_curve():
    try:
        data = request.json
        age = float(data['age'])
        sex = data['sex']
        race = int(data['race'])
        dm = 1 if data['dm'] == 'Yes' else 0
        htn = 1 if data['htn'] == 'Yes' else 0
        sbp = float(data['sbp'])
        uacr = float(data['uacr'])
        egfr = float(data['egfr'])
        bmi = float(data['bmi'])
        smoking = 1 if data['smoking'] == 'Yes' else 0
        
        times = np.linspace(0, 360, 121)
        
        if use_real_model:
            base_profile = {
                'age': age, 'dm': dm, 'htn': htn, 'sbp': sbp,
                'uacr': uacr, 'egfr': egfr, 'bmi': bmi,
                'smoking': smoking, 'antihtn': 0
            }
            
            for col in [c for c in feature_cols if c.startswith('sex_')]:
                base_profile[col] = 0
            if sex == 'Female':
                base_profile['sex_2.0'] = 1
                
            for col in [c for c in feature_cols if c.startswith('race_')]:
                base_profile[col] = 0
            if race != 3:
                race_col = f'race_{race}.0'
                if race_col in feature_cols:
                    base_profile[race_col] = 1
            
            for col in feature_cols:
                if col not in base_profile:
                    base_profile[col] = feature_means.get(col, 0)
            
            patient_df = pd.DataFrame([base_profile])[feature_cols]
            survival_no = cph.predict_survival_function(patient_df, times=times)
            cum_inc_no = 1 - survival_no.values.flatten()
            
            base_profile['antihtn'] = 1
            patient_df_yes = pd.DataFrame([base_profile])[feature_cols]
            survival_yes = cph.predict_survival_function(patient_df_yes, times=times)
            cum_inc_yes = 1 - survival_yes.values.flatten()
            
            model_info = "Real NHANES 1999-2018"
        else:
            baseline_hazard = 0.01
            treatment_effect = -0.3
            age_effect = (age - 60) * 0.02
            dm_effect = dm * 0.4
            htn_effect = htn * 0.3
            
            total_hazard_no = baseline_hazard * np.exp(age_effect + dm_effect + htn_effect)
            total_hazard_yes = total_hazard_no * np.exp(treatment_effect)
            times_years = times / 12
            
            shape = 1.5
            scale_no = 1 / (total_hazard_no ** (1/shape))
            scale_yes = 1 / (total_hazard_yes ** (1/shape))
            
            cum_inc_no = 1 - np.exp(-(times_years / scale_no) ** shape)
            cum_inc_yes = 1 - np.exp(-(times_years / scale_yes) ** shape)
            model_info = "Simulated"
        
        return jsonify({
            'times': (times / 12).tolist(),
            'cum_inc_no': cum_inc_no.tolist(),
            'cum_inc_yes': cum_inc_yes.tolist(),
            'model_type': 'real' if use_real_model else 'simulated',
            'model_info': model_info
        })
        
    except Exception as e:
        print(f"Error: {traceback.format_exc()}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("NHANES Cox App - Visit: http://127.0.0.1:5000")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5001)
 