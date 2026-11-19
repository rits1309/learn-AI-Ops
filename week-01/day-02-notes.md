# Day 2: Python for Data Analysis — NumPy & Pandas for DevOps Metrics

- **Level:** Beginner to Intermediate
- **Duration:** 2 hours
- **Language:** Python
- **Goal:** AI + DevOps / MLOps Engineer

---

## 1. Objectives
- Understand why Data Analysis tools (**NumPy** and **Pandas**) are foundational for MLOps and AIOps.
- Learn NumPy vectorization and how it speeds up metric processing compared to pure Python loops.
- Calculate essential DevOps operational statistics (Mean, Standard Deviation, and Latency Percentiles: $p50$, $p95$, $p99$).
- Master Pandas **Series** and **DataFrames** to filter, aggregate, and inspect multi-node server telemetry.
- Connect data preprocessing to **AWS CloudWatch Metric Streams** and **SageMaker Feature Store**.

---

## 2. Why DevOps & MLOps Engineers Need NumPy and Pandas

In traditional DevOps, scripts frequently parse text files or JSON using basic loops:
```python
# Pure Python: Slow on millions of log entries
high_cpu = []
for entry in logs:
    if entry["cpu"] > 80:
        high_cpu.append(entry)
```

In **AIOps and MLOps**, production systems generate millions of data points every minute:
- **CloudWatch / Datadog / Prometheus** time-series metrics.
- Distributed tracing data and latency measurements.
- Training datasets for predictive auto-scaling.

| Challenge | Pure Python | NumPy & Pandas |
| :--- | :--- | :--- |
| **Execution Speed** | Interpreted, slow loop execution | Written in C/Fortran, vectorized SIMD instructions |
| **Memory Efficiency** | High overhead per Python object pointer | Contiguous memory buffers, compact memory footprint |
| **Data Alignment** | Manual dictionary parsing and indexing | Automatic index alignment, handles missing values (`NaN`) |
| **ML Readiness** | Requires custom format conversions | Directly fed into Scikit-learn, PyTorch, and SageMaker |

---

## 3. NumPy Fundamentals for Infrastructure Engineers

NumPy (`Numerical Python`) provides the $N$-dimensional array object (`ndarray`).

### A. Vectorization vs Loops
Instead of iterating through every server metric one by one, vectorized operations apply calculations to the entire array simultaneously:

```python
import numpy as np

# Memory in Megabytes
memory_mb = np.array([1024, 2048, 4096, 8192, 16384])

# Vectorized conversion to Gigabytes (no for-loop required!)
memory_gb = memory_mb / 1024
# Result: array([ 1.,  2.,  4.,  8., 16.])
```

### B. DevOps Metric Percentiles ($p50$, $p90$, $p95$, $p99$)
In site reliability engineering (SRE), average latency can hide critical outages (the "flaw of averages"). Percentiles measure tail latency experienced by real users:

- **$p50$ (Median):** 50% of requests are faster than this value.
- **$p95$:** 95% of requests meet this threshold (SLA target).
- **$p99$:** The worst 1% of transactions (critical for identifying edge-case bottlenecks).

```python
latencies = np.array([25, 30, 28, 35, 42, 110, 450, 29, 31, 850])

p50 = np.percentile(latencies, 50)  # 33.0 ms
p95 = np.percentile(latencies, 95)  # 670.0 ms
p99 = np.percentile(latencies, 99)  # 833.1 ms
```

---

## 4. Pandas for Telemetry & Cluster Data Analysis

Pandas introduces two primary data structures:
1. **Series:** A 1-dimensional labeled array (e.g., a single column of CPU metrics).
2. **DataFrame:** A 2-dimensional labeled tabular structure (rows = timestamps/nodes, columns = metrics).

### Key DataFrame Operations for DevOps:

```python
import pandas as pd

# Creating a Telemetry DataFrame
data = {
    "instance_id": ["i-01", "i-02", "i-03", "i-04"],
    "region": ["us-east-1", "us-east-1", "eu-west-1", "us-west-2"],
    "cpu_pct": [45.2, 88.5, 92.1, 31.0],
    "memory_pct": [60.0, 78.4, 85.0, 42.1],
    "status": ["healthy", "warning", "critical", "healthy"]
}

df = pd.DataFrame(data)

# 1. Filtering High-Load Instances
stressed = df[df["cpu_pct"] > 80]

# 2. Aggregating by Region
regional_avg = df.groupby("region")[["cpu_pct", "memory_pct"]].mean()

# 3. Adding Calculated Operational Metrics
df["resource_pressure"] = (df["cpu_pct"] + df["memory_pct"]) / 2
```

---

## 5. How This Fits into AWS & MLOps Architecture

```
┌────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│ AWS CloudWatch Metrics │ ───> │ Amazon S3 (Data Lake)   │ ───> │ Amazon SageMaker        │
│ & EKS Container Logs   │      │ (Parquet / CSV files)   │      │ Processing Job (Pandas) │
└────────────────────────┘      └─────────────────────────┘      └─────────────────────────┘
                                                                              │
                                                                              ▼
                                                                 ┌─────────────────────────┐
                                                                 │ Clean Feature Matrices  │
                                                                 │ for Anomaly Detection   │
                                                                 └─────────────────────────┘
```

1. **Amazon CloudWatch Metric Streams:** Continuously streams infrastructure metrics to **Amazon S3** in near real-time.
2. **AWS Glue / Amazon Athena:** Catalogs and queries the S3 telemetry data.
3. **Amazon SageMaker Processing:** Runs containerized Python scripts leveraging NumPy and Pandas to clean, normalize, and construct features for predictive autoscaling models.

---

## 6. Practical Lab Summary

- **Core Exercise:** `week-01/day2.py`
  - Utilizes 2D NumPy arrays `[CPU, Memory]` across server fleets.
  - Slices feature columns using array index notation (`servers[:, 0]`, `servers[:, 1]`).
  - Computes fleet statistics (`np.mean`, `np.max`).
  - Identifies servers violating thresholds using boolean masks and `np.where(high_cpu)[0] + 1`.
- **Extended Telemetry Lab:** `week-01/day2_numpy_pandas_devops.py`
  - Uses **NumPy** to calculate SLA latency percentiles ($p50, p90, p95, p99$).
  - Uses **Pandas** to calculate error rates, filter unhealthy EC2 instances, and group resource consumption by AWS region.
  - Generates an incident triage report for DevOps alerts.

---

## 7. Knowledge Check (Self-Quiz)

1. **Why is NumPy preferred over pure Python lists for processing telemetry arrays?**
   - *Answer:* NumPy stores data in contiguous memory blocks and uses compiled C-level vectorized operations, avoiding slow Python pointer lookups and loops.
2. **Which metric percentile represents the latency experienced by the slowest 1% of users?**
   - *Answer:* The $p99$ percentile.
3. **In Pandas, which function is used to calculate statistical aggregates (e.g. average CPU) grouped by a category like AWS region?**
   - *Answer:* `.groupby()`, e.g., `df.groupby("region")["cpu_pct"].mean()`.
4. **How do you filter a DataFrame `df` to include only servers with CPU utilization above 85%?**
   - *Answer:* `df[df["cpu_pct"] > 85]`.

---

## 8. Checklist Completed
- [x] Understand why NumPy & Pandas are essential for AIOps and MLOps.
- [x] Master NumPy vectorization vs standard Python loops.
- [x] Compute $p50$, $p95$, and $p99$ latency percentiles for SLA tracking.
- [x] Perform boolean indexing, filtering, and `.groupby()` operations in Pandas.
- [x] Run `week-01/day2_numpy_pandas_devops.py` and inspect cluster report.
- [x] Push Day 2 notes and lab to GitHub.
