#!/bin/bash

source ~/.pyenv/versions/prusament/bin/activate
cd "$(dirname "$0")"
python main.py notify -u
python main.py save
