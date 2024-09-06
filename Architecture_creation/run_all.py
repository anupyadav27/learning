
import subprocess

# Run data collection
print("Running data collection...")
subprocess.run(['python', 'data_collection.py'])

# Run data processing
print("Running data processing...")
subprocess.run(['python', 'data_processing.py'])

# Run visualization for HTML
print("Running HTML visualization...")
subprocess.run(['python', 'visualization_html.py'])

# Run visualization for PNG
print("Running PNG visualization...")
subprocess.run(['python', 'visualization_png.py'])

print("All stages completed.")
