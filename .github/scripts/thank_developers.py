import requests

repo_owner = "hegdepavankumar"
repo_name = "VMware-Workstation-Pro-17-Licence-Keys"

# Get the list of stargazers
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/stargazers"
response = requests.get(url)
stargazers = response.json()

# Thank each stargazer
for stargazer in stargazers:
    username = stargazer["login"]
    print(f"Thank you, @{username}, for starring the repo! 🌟 We appreciate your support.")

