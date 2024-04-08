import os
import subprocess


def upload_to_surge(folder_path, desired_domain):
    """
    Uploads a folder to surge.sh and attempts to update the domain (not guaranteed).

    Args:
        folder_path: Path to the folder containing the website files.
        desired_domain: The desired domain name for the deployment.
    """
    os.chdir(folder_path)
    print(f'{folder_path=}')

    try:
        # Step 1: Run surge interactively to capture prompts (domain selection)
        # process = subprocess.Popen(["surge"], stdin=subprocess.PIPE,
        #                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        surge = subprocess.run(["surge", "./", f"{desired_domain}"], check=True)
        print(f'✅ {surge=}')
        # Send "Enter" key to confirm project path (Step 1 in your example)
        # x = process.stdin.write(b"\n")
        # print(f'{x}')

        # Assuming desired_domain is a single word without spaces
        # Send the desired domain name followed by an "Enter" key
        # y=process.stdin.write(f"{desired_domain}\n".encode())
        # print(f'{y}')
        # stdout, stderr = process.communicate()
        # print(stdout.decode())  # Print surge output for debugging (optional)

        # Check if deployment was successful (assuming success message in stdout)
        # if "Successfully deployed project" in stdout.decode():
            # print(f"Pushed '{folder_path}' to surge.")
            # Step 2: Update domain (This part might not be reliable)
            # Ideally, surge.sh should offer a programmatic way to set the domain.
            # This section attempts to update the domain name in the surge output,
            # but it's not guaranteed to work and might require further exploration.
        #     domain_line = next(
        #         (line for line in stdout.decode().splitlines() if "Domain:" in line), None)
        #     if domain_line:
        #         # Extract current domain and replace with desired domain (modify if needed)
        #         current_domain = domain_line.split(": ")[-1]
        #         updated_output = stdout.decode().replace(current_domain, desired_domain)
        #         print(f"** Note: Domain update attempted (might not be successful).")
        #         print(updated_output)
        #     else:
        #         print(f"** Unable to locate domain information in surge output.")
        # else:
        #     print(f"Error deploying '{folder_path}': {stderr.decode()}")

    except subprocess.CalledProcessError as e:
        print(f"Error uploading to surge: {e}")


def main():
    projects = {
                "sigma": "/Users/lifen/Templates/Websites/MIT/sigma",
                "sulfer-bootstrap": "/Users/lifen/Templates/Websites/MIT/sulfer-bootstrap",
                "thomson-bootstrap": "/Users/lifen/Templates/Websites/MIT/thomson-bootstrap",
                "vex-bootstrap": "/Users/lifen/Templates/Websites/MIT/vex-bootstrap",
                "webdavit": "/Users/lifen/Templates/Websites/MIT/webdavit", 
                }

    for folder_name, folder_path in projects.items():
        # Modify domain pattern as needed
        desired_domain = f"{folder_name}-template.surge.sh"
        upload_to_surge(folder_path, desired_domain)


if __name__ == "__main__":
    main()
