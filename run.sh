#!/bin/bash

cd "$(dirname "$0")"
source .venv/bin/activate
python main.py notify -u
python main.py save
