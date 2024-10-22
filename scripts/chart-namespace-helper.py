import os
import argparse


def add_namespace_to_yaml_files(target_dir):
    # Loop through all files in the target directory
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # Process only .yaml files
            if file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                # If it's values.yaml, check and update it
                if file == "values.yaml":
                    add_namespace_to_values(file_path)
                else:
                    modify_file(file_path)


def modify_file(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check if 'namespace: {{ .Values.namespace }}' is already present
    if any('namespace: {{ .Values.namespace }}' in line for line in lines):
        print(f"'namespace: {{ .Values.namespace }}' already exists in {file_path}, skipping.")
        return

    # Look for the 'metadata:' line and add the namespace after it
    modified_lines = []
    namespace_added = False
    for line in lines:
        modified_lines.append(line)
        if 'metadata:' in line and not namespace_added:
            # Add the namespace line right after 'metadata:' if it's not already there
            modified_lines.append('  namespace: {{ .Values.namespace }}\n')
            namespace_added = True

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

    print(f"Modified: {file_path}")


def add_namespace_to_values(values_file_path):
    # Read the content of values.yaml
    with open(values_file_path, 'r') as file:
        lines = file.readlines()

    # Check if 'namespace:' is already defined in values.yaml
    namespace_defined = any('namespace:' in line for line in lines)

    # If 'namespace:' is missing, append it with a default value
    if not namespace_defined:
        with open(values_file_path, 'a') as file:
            file.write('namespace: default\n')
        print(f"Added 'namespace: default' to {values_file_path}")
    else:
        print(f"'namespace' already defined in {values_file_path}, skipping.")


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Add namespace to YAML files in the specified directory.")
    parser.add_argument("target_directory", help="The target directory containing YAML files.")

    args = parser.parse_args()

    target_directory = args.target_directory

    # Verify the provided directory exists
    if os.path.isdir(target_directory):
        add_namespace_to_yaml_files(target_directory)
    else:
        print(f"{target_directory} is not a valid directory.")
