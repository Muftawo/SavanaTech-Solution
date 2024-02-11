from github import Github
from src.extract import Extract
from src.transform import transformer


def main()-> None:
        
    org_name = 'Scytale-exercise'

    g = Github()
    org = g.get_organization(org_name)
    repositories = org.get_repos()




    for repo in repositories:
        repo_name = repo.name
        repository_data = Extract.get_repo_data(repo)
        Extract.save_repo_data(org_name, repo_name, repository_data)
        
        
    transformer()
    
if __name__ == "__main__":
    main()