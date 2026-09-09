#!/bin/bash

#Script for workspace initialisation 


# Get repository name from the Git repository configured by Onyxia
export MY_REPO="$(basename "${GIT_REPOSITORY%.git}")"

echo "Repository: $MY_REPO"

cd $MY_REPO

cd example_code

# Setup enviorment packages
uv sync

cd ../../

# Set VSCode's default interpreter path
mkdir -p .vscode

cat > .vscode/settings.json <<'EOF'
{
    "python.defaultInterpreterPath": "/home/onyxia/work/WP10_Cluster2_NACEClassification_PL/example_code/.venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "files.exclude": {
        "**/.git": true,
        "**/images": true,
        "**/chapters": true,
        "**/notebooks": true,
        "**/_site": true,
        "**/sspcloud": true,
        "**/styles.css": true,
        "**/export-metadata.lua": true,
        "**/.python-version": true,
        "**/pyproject.toml": true,
        "**/uv.lock": true,
        "**/metadata.json": true,
        "**/_brand.yml": true,
        "**/about.qmd": true,
        "**/.gitignore": true,
        "**/init.sh": true,
        "**/README.md": true,
        "**/index.qmd": true,
        "**/_quarto.yml": true,
        "**/init_workspace.sh": true,
        "**/_extensions": true,
        "**/resources": true,

        "**/example_code": false
    }
}
EOF


# Download Bielki model file
cd $MY_REPO/example_code/Summary
curl -L -o Bielik-1.5B-v3.0-Instruct.Q8_0.gguf "https://huggingface.co/speakleash/Bielik-1.5B-v3.0-Instruct-GGUF/resolve/main/Bielik-1.5B-v3.0-Instruct.Q8_0.gguf?download=true"
