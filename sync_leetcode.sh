#!/bin/bash

# ---- CONFIG ----
REPO_URL="https://github.com/AhteshamAlvi/Leetcode_Solutions.git"

# ---- CHECK glsync ----
if ! command -v glsync &> /dev/null
then
    echo "Error: glsync is not installed or not in PATH"
    exit 1
fi

# ---- CHECK GIT ----
if ! command -v git &> /dev/null
then
    echo "Error: git is not installed"
    exit 1
fi

# ---- CHECK REPO EXISTS ----
echo "Checking if repo exists..."
if ! git ls-remote "$REPO_URL" &> /dev/null
then
    echo "Error: Repo does not exist or is not accessible:"
    echo "$REPO_URL"
    exit 1
fi

# ---- GET COOKIE ----
echo "Paste your LeetCode cookie:"
read -r LC_COOKIE

if [ -z "$LC_COOKIE" ]; then
    echo "Error: Cookie cannot be empty"
    exit 1
fi

# ---- RUN GLSYNC ----
echo "Running glsync..."
glsync -lc-cookie="$LC_COOKIE" -repo-url="$REPO_URL"

echo "Done."
