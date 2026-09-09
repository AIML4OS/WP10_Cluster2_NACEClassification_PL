#!/bin/bash

#Script for workspace initialisation 


# Get repository name from the Git repository configured by Onyxia
export MY_REPO="$(basename "${GIT_REPOSITORY%.git}")"

echo "Repository: $MY_REPO"

cd $MY_REPO

cd example_code

mkdir -p TESTOWY
