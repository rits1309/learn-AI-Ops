
import numpy as np

# Infrastructure monitoring data
# Columns: CPU and Memory

servers = np.array([
    [20, 30],
    [35, 40],
    [45, 50],
    [70, 65],
    [95, 90]
])

# Extract CPU and Memory columns
cpu = servers[:, 0]
memory = servers[:, 1]

print("CPU Utilization:", cpu)
print("Memory Utilization:", memory)
# Calculate average utilization
print("Average CPU:", np.mean(cpu))
print("Average Memory:", np.mean(memory))

# Find maximum utilization
print("Maximum CPU:", np.max(cpu))
print("Maximum Memory:", np.max(memory))

# Detect servers with high CPU
high_cpu = cpu > 80

print("High CPU servers:", high_cpu)

# Find server numbers with high CPU
server_numbers = np.where(high_cpu)[0] + 1

print("Servers requiring investigation:", server_numbers)
