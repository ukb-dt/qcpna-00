# 1. Install Python packages (one time)
cd nhanes_cox_app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Start the Flask app (DOPAMINE - instant UI)
python app.py
# → Visit http://127.0.0.0:5001

# 3. In SEPARATE terminal: Build the model (SEROTONIN - real data)
# python build_model.py
# → Takes 10-30 min, downloads data, trains model