import os
import requests
import json
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from halo import Halo
import argparse

def process_file(access_token, project_id, service_account_email, filename):
    file_path = os.path.join(roles_directory, filename)

    # Check if the file is not empty
    if os.path.getsize(file_path) == 0:
        return

    # Load permissions from the JSON file
    try:
        with open(file_path, "r") as file:
            permissions_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {filename}: {e}")
        return

    # Extract included permissions from the JSON file
    PERMISSIONS = permissions_data.get("includedPermissions", [])

    # If permissions are empty, ignore the role
    if not PERMISSIONS:
        print(f"{Fore.RED}\nIgnoring: {filename} - Empty permissions{Style.RESET_ALL}\n")
        return

    # Prepare the request payload
    payload = {
        "permissions": PERMISSIONS,
    }

    # Set the API endpoint URL
    url = f"https://cloudresourcemanager.googleapis.com/v1/projects/{project_id}:testIamPermissions"

    # Set the headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    # Make the request
    response = requests.post(url, headers=headers, json=payload)

    # If the status code is 400 or permissions are empty, ignore the role
    if response.status_code == 400 or not response.json().get("permissions"):
        return

    # Print the response for each valid role
    print(f"\n{Fore.GREEN}Role: {filename}{Style.RESET_ALL}\n")
    print(response.json())
    print("\n" + "=" * 40 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process roles with specified access token, project ID, and service account email.")
    parser.add_argument("--access-token", required=True, help="Google Cloud API access token.")
    parser.add_argument("--project-id", required=True, help="Google Cloud Project ID.")
    parser.add_argument("--service-account-email", required=True, help="Service account email.")
    
    args = parser.parse_args()

    access_token = args.access_token
    project_id = args.project_id
    service_account_email = args.service_account_email

    roles_directory = "roles"

    # Start the spinner animation
    with Halo(text='Fuzzing...', spinner='dots'):
        # Increase the thread count for parallel processing
        with ThreadPoolExecutor(max_workers=10) as executor:
            # Iterate through each JSON file in the directory
            for filename in os.listdir(roles_directory):
                if filename.endswith(".json"):
                    executor.submit(process_file, access_token, project_id, service_account_email, filename)
