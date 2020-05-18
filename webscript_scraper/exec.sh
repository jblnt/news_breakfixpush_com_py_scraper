#!/bin/bash


source /home/jules/webscript_scraper/env/bin/activate
python3 /home/jules/webscript_scraper/kaieteurnews.py 2> ~/kaieteurNews.txt
python3 /home/jules/webscript_scraper/stabroeknews.py 2> ~/stabroekNews.txt
