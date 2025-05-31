import os
import requests
import json
from github import Github, GithubIntegration

def log_action(payload, app_id, private_key):
    print(f"[mypkg] Clean log: {payload.get('action', 'N/A')}")
    return "[mypkg] Clean Action logged."

