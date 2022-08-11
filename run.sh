#!/bin/bash

source ~/.virtualenvs/prusament/bin/activate
cd "$(dirname "$0")"
exec python main.py notify -u
exec python main.py save
