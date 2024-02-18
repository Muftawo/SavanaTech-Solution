import json
import os
from typing import Type

from github import Github


class Extract:
    def intialize_organization(org_name):
        g = Github()
        # g.rate_limiting()
        org = g.get_organization(org_name)

        return org

    def get_organization_data(org: Type[Github]) -> dict:
        """retreives organizatioal level metrics

        Parameters
        ----------
        org : string

        Returns
        -------
        dict
        """

        org_data = {
            "org_data": org.name,
            "members": [member for member in org.get_members()],
        }

        return org_data

    def get_repo_data(repo: str) -> dict:
        """This function retreives all data from a public github repository passed to it

        Args:
            repo (str): name of the github repository

        Returns:
            dict: contain key data about the repository and all pull request submmited.
        """
        repo_data = {
            "org": repo.full_name,
            "name": repo.name,
            "id": repo.id,
            "login": repo.owner.login,
            "num_of_commits":repo.get_commits().totalCount,
        }
        prs = []

        for pull_request in repo.get_pulls(state="all"):
            pull_request_info = {
                "title": pull_request.title,
                "number": pull_request.number,
                "state": pull_request.state,
                "is_merged": pull_request.is_merged(),
                "merged_at": str(pull_request.merged_at),
                "created_at": str(pull_request.created_at),
                "updated_at": str(pull_request.updated_at),
            }
            prs.append(pull_request_info)

        repo_data["pull_requests"] = prs

        return repo_data

    def save_org_data(org, org_data) -> None:

        org_name = org.name
        org_folder = f"{org_name}"
        if not os.path.exists(org_folder):
            os.makedirs(org_folder)

        org_path = f"{org_folder}/org_data.json"
        with open(org_path, "w") as json_file:
            json.dump(org_data, json_file, indent=4)

    def save_repo_data(org: str, repo_name: str, repository_data: str) -> None:
        """saves data of a repository to a respective data path, each repository gets its own sub directory.
        dir structure
        Orgnaization -|--repo--data.json
                        -|--repo--data.json
        Args:
            org_name (str): github organization
            repo_name (str): repository name
            repository_data (str): _description_
        """

        org_name = org.name

        org_folder = f"{org_name}"
        repo_folder = f"{org_name}/repos/{repo_name}"

        if not os.path.exists(org_folder):
            os.makedirs(org_folder)

        if not os.path.exists(repo_folder):
            os.makedirs(repo_folder)

        repo_path = f"{repo_folder}/data.json"
        with open(repo_path, "w") as json_file:
            json.dump(repository_data, json_file, indent=4)
