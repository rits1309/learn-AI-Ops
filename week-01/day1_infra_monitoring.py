"""
Day 1: AI + DevOps Learning Lab
Topic: Infrastructure Monitoring Analysis - Rule-based vs ML Fundamentals
"""

def analyze_infrastructure():
    # Simulated infrastructure metric snapshots (percentages)
    cpu_usage = [20, 35, 45, 70, 95, 98]
    memory_usage = [30, 40, 50, 65, 90, 95]

    # Calculate average CPU usage
    average_cpu = sum(cpu_usage) / len(cpu_usage)

    # Calculate average memory usage
    average_memory = sum(memory_usage) / len(memory_usage)

    print("=== Infrastructure Telemetry Summary ===")
    print(f"Recorded CPU Readings    : {cpu_usage}")
    print(f"Recorded Memory Readings : {memory_usage}")
    print(f"Average CPU              : {average_cpu:.2f}%")
    print(f"Average Memory           : {average_memory:.2f}%")
    print("----------------------------------------")

    # Rule-Based Analysis (Static Threshold)
    threshold = 80.0
    if average_cpu > threshold:
        print(f"[STATUS] WARNING: High CPU usage detected (>{threshold}%)")
    else:
        print("[STATUS] CPU usage is normal")

    print("\n[NOTE] This is rule-based logic. In upcoming labs, we will train")
    print("ML models to detect anomalies and predict spikes from multi-variate data.")

if __name__ == "__main__":
    analyze_infrastructure()
