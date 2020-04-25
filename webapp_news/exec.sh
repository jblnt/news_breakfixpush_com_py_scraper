#!/bin/bash


source /home/jules/scripts/webapp_news/venv/bin/activate
python3 /home/jules/scripts/webapp_news/kaieteurnews.py > ~/log1.txt
python3 /home/jules/scripts/webapp_news/stabroeknews.py > ~/log2.txt
