from graphviz import Digraph
import json

# Load the processed data
with open('k8s_data.json', 'r') as f:
    architecture_data = json.load(f)

dot = Digraph(comment='Kubernetes Architecture')
dot.attr(rankdir='LR', size='10')

# Define system namespaces to exclude
system_namespaces = {'kube-system', 'kube-public', 'kube-node-lease'}

# Filter services and pods based on namespace and pod name within the default namespace
for ns, svc in architecture_data['services']:
    if ns not in system_namespaces:
        dot.node(svc, f'{ns}/{svc}', shape='ellipse', style='filled', color='lightgreen')

for ns, pod, ip in architecture_data['pods']:
    if ns not in system_namespaces and not (ns == 'default' and pod.startswith('kube')):
        dot.node(pod, f'{ns}/{pod} (IP: {ip})', shape='circle', style='filled', color='lightcoral')
        dot.edge(pod, ip, label='has IP')

# Render the diagram to a PNG file
png_filename = 'k8s_architecture_filtered'
dot.render(png_filename, format='png', view=False)

print(f"Filtered architecture diagram generated as '{png_filename}.png'.")
