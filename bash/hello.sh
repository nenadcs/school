#!/usr/bin/env bash
set -euo pipefail

read -p "Hello, what is your name? " name
read -p "Your name is $name. Is that correct? (y/n) " resp
if [[ $resp == "y" ]]; then
    echo "Cool! Nice to meet you, $name"
elif [[ $resp == "n" ]]; then
    echo "Well, fuck you then!"
    exit 1
fi

read -p "What file do you want to read? " path
cat "$path"
