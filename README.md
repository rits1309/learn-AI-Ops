# 🚀 AI + DevOps / MLOps Hands-on Engineering Journey

Welcome to the **AI + DevOps / MLOps** practical learning journey! This repository documents daily concepts, hands-on Python labs, AWS architectures, MLOps pipelines, and infrastructure automation experiments.

---

## 🎯 Career Target
**AI + DevOps / MLOps Engineer** — Bridging scalable cloud infrastructure, CI/CD automation, and production machine learning model lifecycles.

---

## 📅 Curriculum Roadmap & Progress

| Week | Day | Focus Area | Status | Code & Notes |
| :--- | :--- | :--- | :---: | :--- |
| **Week 1** | **Day 1** | **Introduction to AI, ML, Deep Learning & AWS Services** | ✅ Done | [Notes](week-01/day-01-notes.md) \| [Lab Code](week-01/day1_infra_monitoring.py) |
| **Week 1** | **Day 2** | **Python for Data Analysis (NumPy & Pandas for DevOps metrics)** | ✅ Done | [Notes](week-01/day-02-notes.md) \| [Lab Code](week-01/day2.py) \| [Extended Lab](week-01/day2_numpy_pandas_devops.py) |
| **Week 1** | **Day 3** | Data Visualization (Matplotlib & Seaborn for server telemetry) | ⏳ Up Next | Coming soon |
| **Week 1** | **Day 4** | Supervised Learning: Linear Regression for Capacity Planning | ⏳ Upcoming | Coming soon |
| **Week 1** | **Day 5** | Classification Models for Server Incident Triage | ⏳ Upcoming | Coming soon |
| **Week 1** | **Day 6** | Unsupervised Learning: Anomaly Detection on Cloud Logs | ⏳ Upcoming | Coming soon |
| **Week 1** | **Day 7** | Week 1 Capstone: End-to-End Metric Predictor Pipeline | ⏳ Upcoming | Coming soon |

---

## 📁 Repository Structure

```text
learn-AI-Ops/
├── .gitignore                      # Python and virtual environment exclusions
├── README.md                       # Roadmap, setup guide, and progress tracker
├── requirements.txt                # Core Python libraries
└── week-01/                        # Week 1: AI/ML Fundamentals & Applied Python
    ├── day-01-notes.md             # Theoretical notes, comparisons & quiz
    ├── day1_infra_monitoring.py    # Metric aggregation & rule-based monitoring lab
    ├── day-02-notes.md             # NumPy & Pandas fundamentals, SLA percentiles
    ├── day2.py                     # NumPy 2D server fleet analysis lab
    └── day2_numpy_pandas_devops.py # Multi-node cluster telemetry analysis lab
```

---

## 🛠️ Environment Setup (Windows PowerShell)

### 1. Clone the Repository
```powershell
git clone https://github.com/rits1309/learn-AI-Ops.git
cd learn-AI-Ops
```

### 2. Create & Activate Virtual Environment
```powershell
python -m venv ai-env

# If execution policy blocks script execution:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\ai-env\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run Day 1 Lab
```powershell
python week-01/day1_infra_monitoring.py
```

---

## 🧠 Day 1 Highlights
- **Concept Hierarchy:** AI $\supset$ Machine Learning $\supset$ Deep Learning $\supset$ Generative AI.
- **ML Paradigms:** Supervised (labeled telemetry), Unsupervised (anomaly clustering), Reinforcement (autonomous scaling).
- **AWS Ecosystem:** Mapping Amazon SageMaker AI (model lifecycle), Amazon Bedrock (foundation models), EKS, S3, and CloudWatch.
- **Hands-on Experiment:** Developed a Python baseline to analyze infrastructure CPU and memory averages vs static threshold alert limits.

---

## 👤 Author
- **GitHub:** [@rits1309](https://github.com/rits1309)
