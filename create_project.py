import json
import os
import subprocess

def create_folders(folders, base_path="."):
    for folder in folders:
        folder_path = os.path.join(base_path, folder["name"])
        os.makedirs(folder_path, exist_ok=True)
        
        if "subfolders" in folder:
            create_folders(folder["subfolders"], folder_path)

def create_files(files):
    for file in files:
        with open(file["name"], "w") as f:
            f.write(file["content"])

def run_commands(commands):
    for command in commands:
        print(f"Executing: {command['description']}")
        subprocess.run(command["command"], shell=True, check=True)

def create_project_from_json(json_file):
    with open(json_file, "r") as f:
        project_data = json.load(f)

    create_folders(project_data["folders"])
    create_files(project_data["files"])
    run_commands(project_data["commands"])

if __name__ == "__main__":
    json_file = "example_project.json"  # Replace this with the path to your JSON file
    create_project_from_json(json_file)
