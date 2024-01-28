# SavanaTech-Solution

This repo contains the solution to [Scytale-excersis](https://github.com/Scytale-exercise/scytale-repo2/blob/main/README.md)



# Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up Virtual Environment](#setting-up-virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Running the Project](#running-the-project)
- [Additional Notes](#additional-notes)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) (version 3.11 recommended)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Set up and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  
    ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Setting Up Virtual Environment

Activate the virtual environment before running the project:

```bash
source .venv/bin/activate 

```
## Running the Project 

The solution to the project was split in to 2 python files `extract.py` and `transform.py`

1. `extract.py` pulls all repos from the organization github in addition with all pull request and saves the reulting data as a JSON.

2. `transform.py` reads all the the saved json data apply the need transformations per the description and saves the reuslting dataframe to as a parquet file.


## Additional Notes
For repos with no merged PRs, merged at is recorded as -1. 


