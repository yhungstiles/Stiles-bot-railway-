#!/bin/bash

# Install playwright with browser dependencies
python3 -m playwright install --with-deps

# Start your bot
python3 main.py