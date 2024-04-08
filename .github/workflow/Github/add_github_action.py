import json
import os
import subprocess
import sys
# Constants
BASE_PATH = "/Users/lifen/Templates/Websites/MIT/"
DIAGRAM_YML_PATH = '/Users/lifen/Projects/lifeninc/Bots/Tools/Github'
FOLDERS = [
"Funel-Application-Landing-Page",
"Greatly-The-Multipurpose-HTML5-Template",
# "Stellar",
# "adex",
# "agen-bootstrap",
# "airspace-bootstrap",
# "aviato-bootstrap",
# "bingo-bootstrap",
# "blue-pro-bootstrap",
# "business-porto-1",
# "classimax-bootstrap",
# "constra-bootstrap",
# "corona-free-dark-bootstrap-admin-template",
# "craftsols",
# "educenter-bootstrap",
# "fame-bootstrap",
# "focus-bootstrap",
# "grilli",
# "gymfit-bootstrap",
# "kross-bootstrap",
# "medic-bootstrap",
# "megakit-bootstrap",
# "myPortfolio",
# "newsbit-bootstrap",
# "novena-bootstrap",
# "orbitor-bootstrap",
# "parsa-bootstrap",
# "phantom-bootstrap",
# "promodise-bootstrap",
# "rappo-bootstrap",
# "restaurant-bootstrap",
# "sigma",
# "sulfer-bootstrap",
# "thomson-bootstrap",
# "vex-bootstrap",
# "webdavit",
]

def run_command(command):
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e} {command=}")
        return False

def make_directory(path, directory_name):
    directory_path = os.path.join(path, directory_name)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    return directory_path

def copy_diagram_yml(path):
    command = ["cp", "-rf", DIAGRAM_YML_PATH, path]
    return run_command(command)

def commit_and_push(folder_path, folder_name):
    try:
        os.chdir(folder_path)
        subprocess.run(["git", "add", "."], check=True)
        commit_message = f"🤖 Added Github Action for Repo Hero for {folder_name}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print(f'Committed and pushed initial content for "{folder_name}".')
    except subprocess.CalledProcessError as e:
        print(f'Error committing or pushing for "{folder_name}": {e}')

def main():
    for folder in FOLDERS:
        print(f'Processing folder: {folder}')
        folder_path = os.path.join(BASE_PATH, folder)
        github_path = make_directory(folder_path, ".github")
        workflow_path = make_directory(github_path, "workflow")

        if copy_diagram_yml(workflow_path):
            print(f"✅ Copied diagram.yml to {workflow_path}")
            commit_and_push(workflow_path, folder)
        else:
            print(f"❌ Error copying diagram.yml to {workflow_path}")

if __name__ == "__main__":
    main()