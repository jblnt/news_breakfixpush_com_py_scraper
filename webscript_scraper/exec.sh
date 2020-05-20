#!/bin/bash

source /home/jules/webscript_scraper/env/bin/activate
python3 /home/jules/webscript_scraper/main_scraper.py > ~/scraper.log 2>&1

