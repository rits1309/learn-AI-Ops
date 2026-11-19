
# Day 1: AI + DevOps learning

# Infrastructure monitoring dataset

cpu_usage = [20, 35, 45, 70, 95, 98]
memory_usage = [30, 40, 50, 65, 90, 95]

# Calculate average CPU usage
average_cpu = sum(cpu_usage) / len(cpu_usage)

# Calculate average memory usage
average_memory = sum(memory_usage) / len(memory_usage)

print("Average CPU:", average_cpu)
print("Average Memory:", average_memory)

# Basic rule-based analysis
if average_cpu > 80:
    print("Warning: High CPU usage detected")
else:
    print("CPU usage is normal")
