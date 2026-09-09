#!/bin/bash

#Script for workspace initialisation 


# Get repository name from the Git repository configured by Onyxia
export MY_REPO="$(basename "${GIT_REPOSITORY%.git}")"

echo "Repository: $MY_REPO"

cd $MY_REPO

cd example_code

uv sync
echo $? >> plik.txt

mkdir -p TESTOWY

echo "$$MY_REPO" >> plik.txt
ls -la >> plik.txt


cd ..

# Set VSCode's default interpreter path
mkdir -p .vscode
echo "{ \"python.defaultInterpreterPath\": \"./$MY_REPO/example_code/.venv/bin/python\" }" >> .vscode/settings.json