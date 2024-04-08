import json
import os
import subprocess
import sys


def read_json(licenses_file):
    try:
        with open(licenses_file, "r") as f:
            licenses_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{licenses_file}' not found.")
    return licenses_data


def create_and_push_repo(folder_name, folder_path):
    """
    Creates a new repository on GitHub for the folder and pushes the content.

    Args:
        folder_name: Path to the folder containing the website files.
        remote_url: URL of the corresponding remote repository on GitHub.
    """
    os.chdir(folder_path)
    command = ["gh", "repo", "create",
               f'raffaello-templates/{folder_name}', '--private',]
    try:
        process = subprocess.run(command, check=True)
        print(f'🤖 {process=}')
        print(f"Pushed '{folder_name}' to remote repository.")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error creating repository for '{folder_name}': {e}")
        return False


def commit_and_push(folder_name, folder_path):
    try:
        # Change directory to the folder
        os.chdir(folder_path)

        # Initialize Git repository (assuming it doesn't exist)
        subprocess.run(["git", "init"], check=True)

        # Add all files to staging area
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes with a message
        commit_message = f"🚀 Initial commit for {folder_name}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        subprocess.run(["git", "branch", "-M", "main"], check=True)

        subprocess.run(["git", "remote", "add","origin",f"https://github.com/raffaello-templates/{folder_name}.git"], check=True)
        # Push changes to remote repository
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print(f"Committed and pushed initial content for '{folder_name}'.")

    except subprocess.CalledProcessError as e:
        print(f"Error committing or pushing for '{folder_name}': {e}")


def main(license):
    base_path = "/Users/lifen/Templates/Websites/MIT/"
    data = read_json(f'{license}.json')

    projects = data[f'{license}']
    repos = ['adex', 'agen-bootstrap', 'grilli',
             'Funel-Application-Landing-Page', 'Agency-website','airspace-bootstrap','aviato-bootstrap']
    for folder_name in projects:
        if folder_name not in repos:
            folder_path = os.path.join(base_path, folder_name)
            print(f'🗂 {folder_path=}')
            if os.path.isdir(folder_path):
                repo_created = create_and_push_repo(
                    folder_name=folder_name, folder_path=folder_path)
                if repo_created:
                    committed = commit_and_push(
                        folder_name=folder_name, folder_path=folder_path)
                    if committed:
                        print(f'✅ Pushed commit to {folder_name}.git')
                # exit()


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        license = args[1]
        main(license)
