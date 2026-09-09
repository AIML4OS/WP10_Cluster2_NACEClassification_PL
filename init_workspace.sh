#!/bin/bash

#Script for workspace initialisation 


# Get repository name from the Git repository configured by Onyxia
export MY_REPO="$(basename "${GIT_REPOSITORY%.git}")"

echo "Repository: $MY_REPO"

mkdir -p /home/onyxia/work/TESTOWY