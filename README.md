# GCP IAM Brute

**GCP IAM Brute** is a tool that leverages the `testIamPermissions` feature in Google Cloud Platform (GCP) to perform fuzz testing for different permissions within GCP.

## Overview

This tool is designed to explore and test the IAM (Identity and Access Management) permissions of roles in a Google Cloud project. By utilizing the `testIamPermissions` API endpoint, it fuzzes various permissions to identify potential security vulnerabilities or misconfigurations.

## How it Works

1. **Role Definition Files:**
   - GCP IAM Brute processes JSON files containing role definitions.
   - Each file represents a role and includes the list of permissions (`includedPermissions`).

2. **`testIamPermissions` API Endpoint:**
   - The tool constructs a request payload with the extracted permissions for each role.
   - It sends a request to the `testIamPermissions` API endpoint for the specified GCP project.

3. **Response Analysis:**
   - The tool examines the API response to identify successful permissions and potential issues.
   - If a response indicates a problem or if permissions are empty, the role is flagged for further investigation.

## Usage

To use GCP IAM Brute, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/hac01/gcp-iam-brute.git
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Run the tool
   ```bash
   python gcp-iam-brute.py --access-token YOUR_GCP_API_ACCESS_TOKEN --project-id YOUR_GCP_PROJECT_ID --service-account-email YOUR_SERVICE_ACCOUNT_EMAIL

# Disclaimer

This tool should be used responsibly and only on systems that you have permission to test. Always follow ethical hacking principles and comply with applicable laws and regulations.

# Credits

The role definitions used in this project were sourced from [iam-dataset](https://github.com/iann0036/iam-dataset/tree/main) by [iann0036](https://github.com/iann0036). 

We appreciate their work in providing a valuable collection of IAM (Identity and Access Management) roles. Please check out their repository for more details.
