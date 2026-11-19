# Day 1: Introduction to AI, ML, Deep Learning & Generative AI

- **Level:** Beginner
- **Duration:** 2 hours
- **Language:** Python
- **Goal:** AI + DevOps / MLOps Engineer

---

## 1. Objectives
- Understand the core concepts of **AI**, **Machine Learning (ML)**, **Deep Learning (DL)**, and **Generative AI (GenAI)**.
- Understand how these technologies relate to one another hierarchically.
- Explore real-world DevOps & AWS use cases for AI.
- Set up the local Python learning environment.
- Run your first infrastructure metric analysis lab.

---

## 2. What is Artificial Intelligence (AI)?
Artificial Intelligence is a broad branch of computer science that enables machines to execute tasks that typically require human intelligence, such as reasoning, problem-solving, perception, and natural language understanding.

### Real-World DevOps Comparison: Traditional vs AI-Assisted Monitoring

| Feature | Traditional DevOps Monitoring | AI-Assisted DevOps / AIOps |
| :--- | :--- | :--- |
| **Trigger** | Hardcoded static threshold (e.g., CPU > 90%) | Dynamic baseline & multi-signal anomaly detection |
| **Context** | Single isolated metric alert (CloudWatch alarm) | Correlates CPU, memory, error logs, and recent deployments |
| **Response** | Engineer investigates root cause manually | System suggests root cause & recommends remediation |
| **Advantage** | Predictable, simple rules | Reduces alert fatigue, prevents downtime proactively |

---

## 3. Technology Hierarchy: AI vs ML vs DL vs GenAI

```
┌─────────────────────────────────────────────────────────┐
│ Artificial Intelligence (AI)                            │
│  Machines simulating intelligent behavior & logic       │
│  ┌───────────────────────────────────────────────────┐  │
│  │ Machine Learning (ML)                             │  │
│  │  Algorithms that learn patterns from data         │  │
│  │  ┌─────────────────────────────────────────────┐  │  │
│  │  │ Deep Learning (DL)                          │  │  │
│  │  │  Multi-layer neural networks                │  │  │
│  │  │  ┌───────────────────────────────────────┐  │  │  │
│  │  │  │ Generative AI (GenAI)                 │  │  │  │
│  │  │  │  Models generating text, code, images │  │  │  │
│  │  │  └───────────────────────────────────────┘  │  │  │
│  │  └─────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

| Technology | Definition | DevOps / Cloud Example |
| :--- | :--- | :--- |
| **Artificial Intelligence (AI)** | Machines performing intelligent tasks | Chatbots, expert diagnostic systems |
| **Machine Learning (ML)** | Statistical algorithms learning patterns from historical data | Predicting server failure or autoscaling demand |
| **Deep Learning (DL)** | ML using multi-layered artificial neural networks | Anomaly detection across complex unstructured log streams |
| **Generative AI** | Models producing new synthetic content (text, code, images) | Automated Terraform script generation, PR summaries |

---

## 4. The Three Types of Machine Learning

### A. Supervised Learning
- **Concept:** Trained on **labeled data** (input feature $X \rightarrow$ target label $y$).
- **DevOps Example:** Classifying server health status:
  - Input: `[CPU: 95%, Memory: 90%]` $\rightarrow$ Target: `"High Load"`
  - Input: `[CPU: 25%, Memory: 35%]` $\rightarrow$ Target: `"Normal"`
- **DevOps Use Case:** Predictive autoscaling, disk failure prediction.

### B. Unsupervised Learning
- **Concept:** Given **unlabeled data**, discovers hidden clusters, patterns, or outliers on its own.
- **DevOps Example:** Grouping EC2 instances with similar traffic patterns or flagging an IP address displaying abnormal request spikes.
- **DevOps Use Case:** Anomaly detection in network traffic and system logs.

### C. Reinforcement Learning (RL)
- **Concept:** An **agent** interacts with an environment, taking actions and receiving **rewards or penalties** to learn an optimal policy.
- **DevOps Example:** An auto-scaler dynamically testing scaling boundaries to minimize cloud cost while keeping latency under SLA.
- **DevOps Use Case:** Dynamic cluster capacity optimization and autonomous self-healing networks.

---

## 5. How AI Fits into AWS DevOps & MLOps

| AWS Service | Role in AI & MLOps |
| :--- | :--- |
| **Amazon S3** | Durable storage for training datasets, raw logs, and model artifacts |
| **Amazon SageMaker AI** | End-to-end ML lifecycle (data prep, training, tuning, hosting endpoints, monitoring) |
| **Amazon Bedrock** | Serverless access to foundation models (Claude, Llama, Titan) via unified APIs |
| **AWS Lambda** | Event-driven serverless compute to invoke models or parse telemetry |
| **Amazon EKS** | Managed Kubernetes cluster for running containerized AI/ML microservices |
| **Amazon ECR** | Container registry storing Docker images for ML training and inference |
| **Amazon CloudWatch** | Real-time monitoring, metrics collection, and alerting for models & infra |
| **AWS IAM** | Granular least-privilege access control for AI workloads and data buckets |
| **AWS Step Functions** | Serverless orchestration of multi-step ML pipelines and CI/CD gates |

> **Key Distinction:**
> - **SageMaker AI** is used for building, training, and operationalizing custom ML models.
> - **Amazon Bedrock** is used for integrating foundation models and building GenAI applications without training from scratch.

---

## 6. Practical Lab Summary

- **File:** `week-01/day1_infra_monitoring.py`
- **Goal:** Analyze simulated CPU and memory telemetry data with Python.
- **Key Takeaway:** Static if/else thresholds represent **traditional rule-based automation**. In upcoming sessions, we replace manual thresholds with **machine learning models** capable of learning multivariate patterns and detecting drift automatically.

---

## 7. Knowledge Check (Self-Quiz)

1. **Which technology is a subset of Machine Learning?**
   - *Answer:* Deep Learning.
2. **Which AWS service allows you to build applications using foundation models without managing model training?**
   - *Answer:* Amazon Bedrock.
3. **Which type of Machine Learning learns from labeled dataset examples?**
   - *Answer:* Supervised Learning.
4. **Is a manual `if average_cpu > 80:` condition considered a Machine Learning model?**
   - *Answer:* No, that is deterministic rule-based programming.

---

## 8. Checklist Completed
- [x] Understand AI, ML, Deep Learning, and Generative AI distinctions.
- [x] Understand Supervised, Unsupervised, and Reinforcement Learning with DevOps applications.
- [x] Map AWS AI/ML services to DevOps workflows.
- [x] Configure Python virtual environment and install core data science libraries.
- [x] Implement and execute infrastructure metrics Python script.
- [x] Save Day 1 notes and push to GitHub repository.
