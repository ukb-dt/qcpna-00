{% raw %}
<!-- Drop this anywhere in your README.md or page HTML -->
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$','$$'], ['\\[','\\]']],
      processEscapes: true
    },
    options: {
      skipHtmlTags: ['script','noscript','style','textarea','pre','code']
    }
  };
</script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
{% endraw %}


# 🧩 NHANES Cox App — Field Prototype v0.2

> **System-builder’s log.**
> A survival model explorer as a living signal test.  
> Flask → Render → Response → Reflection.  
> Proof of signaling, proof of concept, proof of coherence.

This app — *ukb-app-00* — is the first live circuit: a working flask-based model environment that turns data into visible survival dynamics, then back into cognition via interface.  
Running on [Render](https://ukb-app-00.onrender.com), it behaves like a **signaling organism**: spun up, responsive, metabolic, idling when inactive.

---

## ⚙️ The Field Phases (Pentad Table)

| **Phase** | **Physics / Ontology** | **Engineering / Implementation** | **Grammar / Syntax** | **Prosody / Dynamics (Rates)** | **Metaphysics / Epistemology** |
|------------|------------------------|----------------------------------|-----------------------|--------------------------------|--------------------------------|
| **1. Electromagnetic** | Energy fields, charge differentials, latent potential | Server instance, Python runtime, ports open | Primitives — imports, constants | Power input, latency, spin-up | Being-as-field — conditions for expression |
| **2. Mechanical** | Structure, motion, force, constraint | Container orchestration, Flask routes, request/response | Syntax — order, indentation, binding | Load, throughput, friction | Form-as-function — articulation of pattern |
| **3. Signaling** | Transmission, coupling, interference, noise | JSON endpoints, render templates, API calls | Semantics — subject/predicate relations | Frequency, delay, signal/noise ratio | Communication-as-being — coherence across parts |
| **4. Metabolic** | Transformation, flow, feedback, homeostasis | Model computation, joblib load, inference cycles | Pragmatics — context, action, response | Throughput, regeneration, efficiency | Systemic value — balancing work and waste |
| **5. Cognitive** | Emergence, anticipation, intentionality | Monitoring, adaptation, self-reflection, UX layer | Meta-grammar — recursion, inference | Reflex latency, learning rate | Knowing-as-energy — awareness of its own rates |

Each row is a **rate domain**.  
Each column a **plane of articulation**.  
Together they define the *operational calculus* of a living system — software as metabolism.

Excellent — here’s the insert I recommend, ready to drop right below your **Pentad Table** in the README:

---

### ⚛️ The Rate Calculus — System Dynamics in Five Motions

$$
(E, x) \rightarrow E(t \mid x) + \epsilon \rightarrow 
\frac{dE_x}{dt} \rightarrow 
\frac{d^2E_x}{dt^2} \rightarrow 
\int E_x \, dt + \epsilon_x + C_x
$$


| **Operator**            | **Interpretation**                                    | **System Domain**   |
| ----------------------- | ----------------------------------------------------- | ------------------- |
| $E(t \mid x)$         | Conditional expectation — potential energy in context | **Electromagnetic** |
| $\frac{dE_x}{dt}$     | Rate of change — motion, work, force                  | **Mechanical**      |
| $\frac{d^2E_x}{dt^2}$ | Acceleration — resonance, oscillation, feedback       | **Signaling**       |
| $\int E_x , dt$       | Accumulation — metabolism, integration of flow        | **Metabolic**       |
| $\epsilon_x + C_x$    | Perturbation and constant — adaptation, awareness     | **Cognitive**       |

Each derivative and integral defines a *temporal interface* between modes of being.
Render’s own behavior — spinning up, serving, idling — traces the same rhythm:
energy → expression → feedback → restoration → reflection.

## 🧠 The Prototype (Signaling Layer)

**Mode:** DOPAMINE → SEROTONIN  
- *Dopamine Mode:* Simulated curves, synthetic hazard.
- *Serotonin Mode:* Real NHANES 1999–2018 model (`cox_model.joblib`).

**Architecture Flow**
```

user → Flask UI → JSON POST → model.eval() → JSON return → Plot

````

If the model is absent, a simulation engine generates synthetic risk curves.  
If the model is present, it computes real survival trajectories.  
In both cases, a message passes, energy transfers, and cognition occurs.

---

## 🧪 Run Protocol

Local test:
```bash
git clone https://github.com/ukb-dt/ukb-app-00.git
cd ukb-app-00/nhanes_cox_app
pip install -r ../requirements.txt
python app.py
````

Render deploy (`render.yaml`):

```yaml
services:
  - type: web
    name: ukb-app-00
    env: python
    pythonVersion: 3.10.14
    buildCommand: pip install -r requirements.txt
    startCommand: python nhanes_cox_app/app.py
```

Visit: **[ukb-app-00.onrender.com](https://ukb-app-00.onrender.com)**
→ responds within 50–60s if cold (Render free-tier idle spin-up).

---

## 🌱 Next Iteration

| Layer           | Target               | Function                                  |
| --------------- | -------------------- | ----------------------------------------- |
| Signaling       | `/ping` endpoint     | Health-check JSON: `{ "status": "ok" }`   |
| Metabolic       | Model energy monitor | Track inference time / power draw         |
| Cognitive       | UI reflection        | Show real vs. simulated feedback visually |
| Mechanical      | CI/CD refinement     | Auto-deploy on commit                     |
| Electromagnetic | Instance upgrade     | Remove cold start delay                   |

---

## 🜂 Meta-Reflection

This repo is a *living organism in miniature*.
Every successful deployment closes a loop between energy, structure, signal, metabolism, and cognition.
It is both a Flask app and an epistemic experiment — an embodied question:

> *Can code metabolize?*
> *Can a system learn to know its own rates?*

That’s the core inquiry — and the calculus continues.

---

*v0.2 — November 2025*
**Mode:** Signaling ↔ Metabolic transition
**Author:** Ukubona LLC

 
