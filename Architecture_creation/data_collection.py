
from kubernetes import client, config

# Load the Kubernetes configuration
config.load_kube_config()
v1 = client.CoreV1Api()

# Get nodes
nodes = v1.list_node()

# Get services
services = v1.list_service_for_all_namespaces()

# Get pods
pods = v1.list_pod_for_all_namespaces()

# Collect the relevant information
node_info = [node.metadata.name for node in nodes.items]
service_info = [(svc.metadata.namespace, svc.metadata.name) for svc in services.items]
pod_info = [(pod.metadata.namespace, pod.metadata.name, pod.status.pod_ip) for pod in pods.items]

# Save the data to a file for processing
import json
with open('k8s_data.json', 'w') as f:
    json.dump({
        "nodes": node_info,
        "services": service_info,
        "pods": pod_info
    }, f)

print("Data collection complete. Data saved to k8s_data.json.")
