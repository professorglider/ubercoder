import json
import os
import sys

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

def main(json_file):
    with open(json_file, "r") as f:
        project_data = json.load(f)

    os.makedirs(project_data["project_name"], exist_ok=True)
    os.chdir(project_data["project_name"])

    create_folders(project_data["folders"])
    create_files(project_data["files"])

    if "env_file" in project_data:
        with open(project_data["env_file"]["name"], "w") as f:
            f.write(project_data["env_file"]["content"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_project.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    main(json_file)
