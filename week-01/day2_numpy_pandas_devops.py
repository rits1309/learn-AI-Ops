"""
Day 2: AI + DevOps / MLOps Learning Lab
Topic: Infrastructure Telemetry Analysis using NumPy and Pandas
"""

import numpy as np
import pandas as pd


def run_devops_data_analysis():
    print("============================================================")
    print("🚀 Day 2 Lab: Telemetry Analysis with NumPy & Pandas")
    print("============================================================\n")

    # ------------------------------------------------------------
    # Part 1: NumPy Vectorization & SLA Latency Percentiles
    # ------------------------------------------------------------
    print("[1] Processing API Gateway Latency with NumPy...")
    # Raw API response latencies in milliseconds
    latencies = np.array([24.2, 28.5, 31.0, 35.8, 42.1, 88.0, 142.5, 29.1, 
                          33.4, 27.9, 39.0, 48.2, 210.4, 520.1, 31.2, 26.8])

    # Vectorized conversion: milliseconds to seconds
    latencies_sec = latencies / 1000.0

    # Calculate statistical percentiles for SLA compliance
    p50 = np.percentile(latencies, 50)
    p90 = np.percentile(latencies, 90)
    p95 = np.percentile(latencies, 95)
    p99 = np.percentile(latencies, 99)

    print(f"    Total Recorded Requests : {len(latencies)}")
    print(f"    Median Latency (p50)   : {p50:.2f} ms")
    print(f"    90th Percentile (p90)  : {p90:.2f} ms")
    print(f"    95th Percentile (p95)  : {p95:.2f} ms (Target SLA: < 150 ms)")
    print(f"    99th Percentile (p99)  : {p99:.2f} ms (Tail Latency)")

    if p95 > 150:
        print("    ⚠️  [ALERT] p95 latency breached SLA target!")
    else:
        print("    ✅  [PASS] p95 latency meets SLA standards.")

    print("\n------------------------------------------------------------")

    # ------------------------------------------------------------
    # Part 2: Multi-Node Cluster Telemetry with Pandas
    # ------------------------------------------------------------
    print("[2] Analyzing AWS EC2 Fleet Telemetry with Pandas...\n")

    raw_cluster_data = {
        "instance_id": ["i-0a1b2c3d01", "i-0a1b2c3d02", "i-0a1b2c3d03", 
                        "i-0a1b2c3d04", "i-0a1b2c3d05", "i-0a1b2c3d06"],
        "region": ["us-east-1", "us-east-1", "us-west-2", 
                   "us-west-2", "eu-central-1", "eu-central-1"],
        "instance_type": ["c5.xlarge", "c5.xlarge", "m5.large", 
                          "m5.large", "r5.xlarge", "r5.xlarge"],
        "cpu_utilization": [42.5, 94.2, 88.7, 35.1, 78.4, 91.0],
        "memory_utilization": [55.0, 89.1, 72.3, 40.0, 82.5, 96.4],
        "requests_total": [12500, 18900, 14200, 9800, 16100, 19400],
        "failed_requests": [12, 450, 210, 8, 35, 780]
    }

    df = pd.DataFrame(raw_cluster_data)

    # Calculate Error Rate percentage using vectorized operations
    df["error_rate_pct"] = (df["failed_requests"] / df["requests_total"]) * 100

    # Display full DataFrame
    print("Cluster Snapshot:")
    print(df[["instance_id", "region", "cpu_utilization", "memory_utilization", "error_rate_pct"]].to_string(index=False))

    # ------------------------------------------------------------
    # Part 3: Filtering & Triage of High-Risk Nodes
    # ------------------------------------------------------------
    print("\n[3] Automated Incident Triage (Filtering High-Risk Nodes):")
    critical_condition = (df["cpu_utilization"] > 85) | (df["error_rate_pct"] > 1.0)
    critical_nodes = df[critical_condition]

    if not critical_nodes.empty:
        print("    🚨 Nodes Requiring Immediate Auto-Scaling / Triage:")
        for _, node in critical_nodes.iterrows():
            print(f"       - {node['instance_id']} ({node['region']}) | "
                  f"CPU: {node['cpu_utilization']}% | Error Rate: {node['error_rate_pct']:.2f}%")
    else:
        print("    All instances are within nominal limits.")

    # ------------------------------------------------------------
    # Part 4: Regional Resource Grouping
    # ------------------------------------------------------------
    print("\n[4] Regional Aggregations (Average Utilization):")
    regional_summary = df.groupby("region")[["cpu_utilization", "memory_utilization", "error_rate_pct"]].mean()
    print(regional_summary.round(2))

    print("\n============================================================")
    print("✅ Day 2 Analysis Complete: Ready for Data Visualization (Day 3)")
    print("============================================================")


if __name__ == "__main__":
    run_devops_data_analysis()
