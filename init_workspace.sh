#!/bin/bash

#Script for workspace initialisation 


# Get repository name from the Git repository configured by Onyxia
export MY_REPO="$(basename "${GIT_REPOSITORY%.git}")"

echo "Repository: $MY_REPO"

cd $MY_REPO

cd example_code

uv sync

cd Summary
curl -L -o Bielik-1.5B-v3.0-Instruct.Q8_0.gguf "https://huggingface.co/speakleash/Bielik-1.5B-v3.0-Instruct-GGUF/resolve/main/Bielik-1.5B-v3.0-Instruct.Q8_0.gguf?download=true"

echo $? >> plik.txt

mkdir -p TESTOWY

echo "$MY_REPO" >> plik.txt
ls -la >> plik.txt

