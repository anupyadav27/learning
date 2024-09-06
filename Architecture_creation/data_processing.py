
import json

# Load the collected data
with open('k8s_data.json', 'r') as f:
    architecture_data = json.load(f)

# For now, just print the data to verify it's correct
print("Nodes:")
for node in architecture_data['nodes']:
    print(f" - {node}")

print("Services:")
for ns, svc in architecture_data['services']:
    print(f" - {ns}/{svc}")

print("Pods:")
for ns, pod, ip in architecture_data['pods']:
    print(f" - {ns}/{pod} (IP: {ip})")

# Process data if needed (e.g., mapping pods to services or nodes)
# For simplicity, we'll assume the data is fine as is
