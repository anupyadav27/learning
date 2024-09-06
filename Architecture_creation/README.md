
# Kubernetes Architecture Visualization Tool

This tool helps visualize the architecture of a Kubernetes cluster by collecting, processing, and visualizing data about the nodes, services, and pods within the cluster. It also includes the option to generate both HTML and PNG visualizations.

## Stages

### 1. Data Collection (`data_collection.py`)
This script collects data from your Kubernetes cluster, including information about nodes, services, and pods. The data is saved in a JSON file (`k8s_data.json`) for further processing.

### 2. Data Processing (`data_processing.py`)
This script loads the collected data, processes it to verify its structure, and prepares it for visualization. It prints out the nodes, services, and pods to confirm that the data was collected correctly.

### 3. Visualization

#### HTML Visualization (`visualization_html.py`)
This script generates an HTML file (`k8s_architecture_filtered.html`) that embeds an SVG representation of the Kubernetes architecture, showing the relationships between nodes, services, and pods. System namespaces such as `kube-system`, `kube-public`, and `kube-node-lease` are excluded, and only user-generated pods and services within the `default` namespace are included.

#### PNG Visualization (`visualization_png.py`)
This script generates a PNG image (`k8s_architecture_filtered.png`) of the Kubernetes architecture. The same filtering logic is applied as in the HTML visualization.

## How to Run

### Prerequisites
- Python 3.6+
- The following Python packages must be installed:
  - `kubernetes`
  - `graphviz`
  
  You can install them using pip:
  ```bash
  pip install kubernetes graphviz
  ```

- Graphviz must be installed on your system. You can download it from [Graphviz download page](https://graphviz.org/download/) and make sure it is added to your system's `PATH`.

### Running the Tool

You can run the tool in one of two ways:

1. **Step-by-Step Execution:**
   - Run each of the scripts in order:
     ```bash
     python data_collection.py
     python data_processing.py
     python visualization_html.py
     python visualization_png.py
     ```

2. **Using the Consolidated Script:**
   - Run the consolidated script (`run_all_consolidated.py`) to execute all stages in sequence:
     ```bash
     python run_all_consolidated.py
     ```

This will automatically collect data, process it, and generate both the HTML and PNG architecture diagrams.

### Output
- **Data File**: `k8s_data.json` - Contains the raw data collected from the Kubernetes cluster.
- **HTML Diagram**: `k8s_architecture_filtered.html` - The visual representation of the Kubernetes architecture in HTML format.
- **PNG Diagram**: `k8s_architecture_filtered.png` - The visual representation of the Kubernetes architecture in PNG format.

## Troubleshooting

- **ModuleNotFoundError**: If you encounter a `ModuleNotFoundError` for `kubernetes` or `graphviz`, ensure that the required packages are installed and that Graphviz is correctly added to your system's `PATH`.
- **ExecutableNotFound**: If Graphviz is not recognized, ensure it is installed and added to your system's `PATH`.

## Enhancements

The current implementation is basic and may not fully capture complex relationships or provide the most aesthetic visualizations. Consider improving the tool by:
- Grouping nodes by type or namespace.
- Adding more context or details to the visualization.
- Using a more advanced visualization tool if needed.
