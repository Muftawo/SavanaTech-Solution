import logging
from github import Github
from src.extract import Extract
from src.transform import transformer


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main() -> None:

    org_name = "Scytale-exercise"

    g = Github()
    org = g.get_organization(org_name)

    # paginated list
    repositories = org.get_repos()

    logging.info("Begin data extraction...")
    for repo in repositories:
        repo_name = repo.name
        repository_data = Extract.get_repo_data(repo)
        Extract.save_repo_data(org_name, repo_name, repository_data)
    logging.info(f"Data extracted form {repositories.totalCount} repos")
    logging.info("Extraction completed !!")

    logging.info("Begin Trasnformation...")
    transformer()
    logging.info("Transformation Done.")


if __name__ == "__main__":
    main()
