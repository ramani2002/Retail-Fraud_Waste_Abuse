import os

# Define the folder structure
folder_structure = {
    "fraud_detection": {
        "data": {
            "raw": {},
            "processed": {},
            "external": {},
            "interim": {},
            "sample": {}
        },
        "notebooks": {
            "EDA.ipynb": "",
            "model_comparison.ipynb": ""
        },
        "src": {
            "__init__.py": "",
            "data": {
                "data_loader.py": "",
                "data_preprocessing.py": "",
                "feature_engineering.py": ""
            },
            "models": {
                "model.py": "",
                "model_selection.py": "",
                "predictions.py": ""
            },
            "utils": {
                "visualization.py": "",
                "metrics.py": ""
            },
            "config.py": ""
        },
        "tests": {
            "test_data_loader.py": "",
            "test_model.py": "",
            "test_utils.py": ""
        },
        "requirements.txt": "",
        "README.md": "",
        "main.py": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)  # Create directories
            create_structure(path, content)    # Recurse into subdirectories
        else:
            with open(path, 'w') as f:         # Create files
                f.write(content)

# Create the folder structure in the current directory
create_structure(".", folder_structure)

print("Folder structure created successfully.")