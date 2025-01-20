from typing import Dict
import requests

def fetch_script_list(repo_url: str) -> Dict[str, str]:
    """Fetch list of Python files from repository API and check for inline metadata."""
    if "github.com" in repo_url:
        api_url = f"https://api.github.com/repos/{repo_url.split('github.com/')[1]}/git/trees/main?recursive=1"
        response = requests.get(api_url)
        response.raise_for_status()
        
        scripts = {}
        for item in response.json()["tree"]:
            if item["path"].endswith(".py"):
                raw_url = f"https://raw.githubusercontent.com/{repo_url.split('github.com/')[1]}/main/{item['path']}"
                content = requests.get(raw_url).text
                if "# /// script" in content and "# ///" in content:
                    name = item["path"].split("/")[-1]
                    scripts[name] = item["path"]  # Only store with .py extension
        return scripts
    
    raise ValueError("Currently only GitHub repositories are supported")