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

# Render the diagram to an SVG file
svg_filename = 'k8s_architecture_filtered'
dot.render(svg_filename, format='svg', view=False)

# Create an HTML file that embeds the SVG
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kubernetes Architecture</title>
</head>
<body>
    <h1>Kubernetes Architecture Diagram (Filtered)</h1>
    <div>
        <embed src="{svg_filename}.svg" type="image/svg+xml" width="100%" height="800px"/>
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open('k8s_architecture_filtered.html', 'w') as f:
    f.write(html_content)

print("Filtered architecture diagram generated as 'k8s_architecture_filtered.html'. You can open this file in your browser to view the architecture.")
