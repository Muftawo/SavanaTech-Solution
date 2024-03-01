# GitMerica

Review insights from your organiztion's Github acticity, gain a deep understanding on repositries, member activity and languages.


# Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up Virtual Environment](#setting-up-virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Running the Project](#running-the-project)


## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) (version 3.11 recommended)
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Muftawo/GitMetrica.git
    cd GitMetrica
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

The solution to the project has 3 python files `extract.py` , `transform.py` and `main.py`

1. `extract.py` pulls all repos from the organization github in addition with all pull request and saves the reulting data as a JSON. run the following to extract all repo data form github orgnization

2. `transform.py` reads all the the saved json data apply the need transformations per the description and saves the reuslting dataframe to as a parquet file. run this to apply the needed transformation and save the parquet file.


3. '`main.py` is the primary application file, it imports from the extract and transform modules and run the entire application.
    ```
    $ python main.py
    ```



