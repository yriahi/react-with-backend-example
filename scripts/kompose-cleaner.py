import os
import sys
import yaml

def clean_annotations(metadata):
    """Remove kompose.cmd and kompose.version from annotations."""
    if metadata and "annotations" in metadata:
        annotations = metadata["annotations"]
        if "kompose.cmd" in annotations or "kompose.version" in annotations:
            annotations.pop("kompose.cmd", None)
            annotations.pop("kompose.version", None)
            if not annotations:  # If annotations is empty, remove it
                metadata.pop("annotations", None)

def rename_kompose_service(obj):
    """Rename io.kompose.service to app in labels, selectors, and matchLabels."""
    if "labels" in obj:
        labels = obj["labels"]
        if "io.kompose.service" in labels:
            labels["app"] = labels.pop("io.kompose.service")
    
    if "selector" in obj:
        selector = obj["selector"]
        if "io.kompose.service" in selector:
            selector["app"] = selector.pop("io.kompose.service")
    
    if "matchLabels" in obj:
        match_labels = obj["matchLabels"]
        if "io.kompose.service" in match_labels:
            match_labels["app"] = match_labels.pop("io.kompose.service")

def process_yaml(file_path):
    with open(file_path, 'r') as f:
        try:
            yaml_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error loading YAML file {file_path}: {e}")
            return

    if yaml_data:
        updated = False

        # Clean annotations at top-level metadata
        if "metadata" in yaml_data:
            clean_annotations(yaml_data["metadata"])
            updated = True

        # Rename io.kompose.service in metadata.labels and spec.selector
        if "metadata" in yaml_data:
            rename_kompose_service(yaml_data["metadata"])
            updated = True

        # Process spec (including template.metadata if present)
        if "spec" in yaml_data:
            spec = yaml_data["spec"]

            # Clean annotations inside template.metadata if it exists
            if "template" in spec and "metadata" in spec["template"]:
                clean_annotations(spec["template"]["metadata"])
                updated = True

            # Rename io.kompose.service in selectors and matchLabels
            if "selector" in spec:
                rename_kompose_service(spec["selector"])
                updated = True

            # Handle spec.template.selector, spec.template.metadata.labels and matchLabels
            if "template" in spec:
                template = spec["template"]
                if "metadata" in template:
                    rename_kompose_service(template["metadata"])

                if "spec" in template and "selector" in template["spec"]:
                    rename_kompose_service(template["spec"]["selector"])
                updated = True

        # If updates were made, write changes back to the file
        if updated:
            with open(file_path, 'w') as f:
                yaml.dump(yaml_data, f, default_flow_style=False)
            print(f"Updated file: {file_path}")

def process_directory(target_dir):
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                file_path = os.path.join(root, file)
                process_yaml(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <target_directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    if not os.path.isdir(target_directory):
        print(f"Error: {target_directory} is not a valid directory")
        sys.exit(1)

    process_directory(target_directory)
