#!/bin/bash

source ~/.virtualenvs/prusament/bin/activate
cd "$(dirname "$0")"
python main.py notify -u
python main.py save
