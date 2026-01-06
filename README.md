# Neural Config Impact Analyzer

An AI-powered security tool that **predicts cloud security risks before deployment**.

Most tools detect issues *after* deployment.  
This project focuses on **preventative, predictive security**.

---

##  What This Project Does

Given an AWS IAM policy (JSON), the system:

- Parses the configuration
- Builds a graph-based permission model
- Calculates blast radius
- Extracts security features
- Predicts risk using Machine Learning
- Explains *why* the policy is risky
- Suggests a safer, least-privilege policy

All **before deployment**.

---

##  Key Concepts Used

- Cloud Security (AWS IAM)
- Graph-based blast radius analysis
- Explainable AI
- Machine Learning risk prediction
- Preventative security design

---

##  Architecture Flow

IAM Policy → Parser → Graph Model → Feature Extraction  
→ Risk Scoring → ML Prediction → Explanation → Auto-Remediation

---

##  How to Run

Activate virtual environment:
```bash
source venv/bin/activate

Run full analysis:
python src/analyze_policies.py
bash'''
---

##  Output

For each policy, the tool outputs:

Blast radius
Risk score (0–100)
ML predicted risk level
Human-readable explanation
Safer IAM policy (if needed)

## Why This Matters

This project demonstrates how AI can be used to:

Prevent security incidents
Reduce misconfigurations
Improve cloud security posture

