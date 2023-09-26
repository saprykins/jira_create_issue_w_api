# DID WORK

import requests
import json

# Set your Jira server URL and API endpoint
jira_url = "https://rsvp5507.atlassian.net"
api_endpoint = "/rest/api/2/issue/"

# Set your Jira username and API token or password
username = "r*"
api_token = "A*"  # Use an API token or password for authentication


# Set the project key where you want to create the issue
project_key = "TC"

# Define the issue data
issue_data = {
    "fields": {
        "project": {"key": project_key},
        "summary": "Application 51",
        "description": "",
        "issuetype": {"name": "Appli"},  # Change the issue type as needed
    }
}

# Create headers with authentication
headers = {
    "Content-Type": "application/json",
}
auth = (username, api_token)

# Make the API request to create the issue
response = requests.post(
    f"{jira_url}{api_endpoint}",
    headers=headers,
    auth=auth,
    data=json.dumps(issue_data),
)

# Check the response status
if response.status_code == 201:
    print("Issue created successfully!")
    issue_data = response.json()
    issue_key = issue_data["key"]
    print(f"Issue Key: {issue_key}")

    # Create subtasks
    subtask_data = [
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "0.010 - Discovery done",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "0.020 - Assessment is done",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "0.030 - Target design is done",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "0.040 - Target validated",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "1.010 - Prerequisites are gathered",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "1.020 - ?Integration?",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "1.030 - Migration plan is prepared",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "1.040 - Pre-migration tests done",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "2.010 - Non-prod migration done",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "2.020 - Pre-prod migration done",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "2.030 - Application tested",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "2.040 - Prod migration done",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
                {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "3.010 - UAT tests done (after migration)",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "3.020 - Cutover Completed",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "4.010 - Warranty phase / Hypercare periode",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        },
        {
            "fields": {
                "project": {"key": project_key},
                "parent": {"key": issue_key},
                "summary": "4.020 - Decommission completed",
                "issuetype": {"name": "Subtask"},  # Change the issue type as needed
            }
        }
    ]

    for subtask in subtask_data:
        subtask_response = requests.post(
            f"{jira_url}{api_endpoint}",
            headers=headers,
            auth=auth,
            data=json.dumps(subtask),
        )
        if subtask_response.status_code == 201:
            print(f"Subtask created successfully!")
        else:
            print(f"Failed to create subtask. Status code: {subtask_response.status_code}")
            print(subtask_response.text)

else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.text)
