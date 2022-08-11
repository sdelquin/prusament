#!/bin/bash

source ~/.virtualenvs/prusament/bin/activate
cd "$(dirname "$0")"
git pull
pip install -r requirements.txt
