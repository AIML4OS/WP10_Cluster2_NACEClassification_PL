# Using Scraping and RAG to Predict NACE Categories
## Introduction

This project is built using:
1. **Python** - versin 3.14.2
2. **ChromaDB** - vector database for storing embeddings
3. **Transformers** - library for working with LLMs
4. **Playwright** - library for scraping dynamic web pages

---

# Step 1 – Scraping data

## Goal
- Get comapanys description to predict NACE (in Poland PKD) category 

---

# Step 2 Summarize the scrapped data
## Goal
- Generate short, high-quality descriptions that improve RAG retrieval and LLM performance.

---

# Step 3 - RAG 
## Goal 
- Predict the NACE category using all three data sources.

---

# Example code in Onyxia

You can test our example code on Onyxia. Click the button below to launch Onyxia with the Visual Studio Code service and our repository already loaded.

<a href="https://datalab.sspcloud.fr/launcher/ide/vscode-python?name=example_code_PL&version=2.5.7&s3=default&resources.requests.cpu=«25900m»&resources.requests.memory=«171Gi»&resources.limits.cpu=«30000m»&resources.limits.memory=«200Gi»&git.repository=«https%3A%2F%2Fgithub.com%2FAIML4OS%2FWP10_Cluster2_NACEClassification_PL.git»&git.branch=«example_code»&autoLaunch=true" target="_blank" rel="noopener" data-original-href="https://datalab.sspcloud.fr/launcher/ide/vscode-python?name=example_code_PL&version=2.5.7&s3=default&resources.requests.cpu=«25900m»&resources.requests.memory=«171Gi»&resources.limits.cpu=«30000m»&resources.limits.memory=«200Gi»&git.repository=«https%3A%2F%2Fgithub.com%2FAIML4OS%2FWP10_Cluster2_NACEClassification_PL.git»&git.branch=«example_code»&autoLaunch=true"><img src="https://custom-icon-badges.demolab.com/badge/SSP%20Cloud-Launch_with_VSCode-blue?logo=vsc&amp;logoColor=white" alt="Onyxia"></a>

## How to set enviorment

1. Open a new terminal and navigate to the repository directory:

    `cd WP10_Cluster2_NACEClassification_PL/`

2. Run command:

    `uv sync`

3. Next open Command Palette and change Python interpreter:

    *ctr+schift+p  or f1*

    *Python: Select Interpreter > Enter interpreter path > /home/onyxia/work/WP10-CLuster_2-example_code/.venv/bin/python*

4. Open Jupyter notebook file and change kernel:

    *change kernel  -> Select another kernel > Python enviorments > .venv*
