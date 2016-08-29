# Using Scrapy to scrape, then process and present some data


## Required system prerequisites:

The following system packages will be required in order to get Scrapy and Lxml to work.

```
sudo apt-get update

sudo apt-get install python-dev python3-dev libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

## Set up your virtualenv with Python 3.4 or 3.5

Assuming virtualenv is already installed on your system.
Set up a virtual environment for this project ...
```
eg. mkvirtualenv -p /usr/bin/python3.4 -a <path to project> <virtualenv name>
```

Once this has been done, activate your virtualenv and run

```
pip install scrapy
```

## Running the scraper

To begin scraping, run as follows ... giving path to output file
```
python run_ripe_fruit_scraper.py <path to json dump file>
```

For usage help, run ...
python run_ripe_fruit_scraper.py -h
```
usage: run_ripe_fruit_scraper.py [-h] json_file

Program scrapes data about fruits from a grocery site.

positional arguments:
  json_file   json scraped data output file.

optional arguments:
  -h, --help  show this help message and exit
```
