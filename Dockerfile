FROM python:3.8-buster

WORKDIR /scraper-py

COPY ./webscript_scraper .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main_scraper.py" ]