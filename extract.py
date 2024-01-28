import os
import json
from github import Github


org_name = 'Scytale-exercise'

g = Github()
org = g.get_organization(org_name)
repositories = org.get_repos()



def get_repo_data(repo):
    repo_data ={"org": repo.full_name,
                "name":repo.name ,
                "id": repo.id, 
                "login":repo.owner.login}
    prs = []

    for pull_request in repo.get_pulls(state='all'):
        pull_request_info = {
            'title': pull_request.title,
            'number': pull_request.number,
            'state': pull_request.state,
            'created_at': str(pull_request.created_at),
            'updated_at': str(pull_request.updated_at),
        }
        prs.append(pull_request_info)
    
    repo_data["pull_requests"]=prs
    
    return repo_data

def save_repo_data(org_name, repo_name, pull_requests_data):
    org_folder = f"{org_name}"
    repo_folder = f"{org_name}/{repo_name}"

    if not os.path.exists(org_folder):
        os.makedirs(org_folder)

    if not os.path.exists(repo_folder):
        os.makedirs(repo_folder)

    file_path = f"{repo_folder}/data.json"
    with open(file_path, 'w') as json_file:
        json.dump(pull_requests_data, json_file, indent=4)



for repo in repositories:
    repo_name = repo.name
    pull_requests_data = get_repo_data(repo)
    save_repo_data(org_name, repo_name, pull_requests_data)