#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import json
from decimal import Decimal

from consume_groceries_data.spiders.ripe_fruits_crawler import RipeFruits


def crawl(json_data_dump):
    """ Runs the spider for the class RipeFruits, which has its starting url
     and scraping rules defined.

     It also generates a json dump file of the scraped data.
    """
    # erases any existing content in the dump file
    with open(json_data_dump, 'w') as fh:
        pass
    crawler = RipeFruits()
    os.system('scrapy crawl {0} -o {1}'.format(crawler.name, json_data_dump))


def update_json_with_total_unit_prices(json_data_file):
    """ Reads the json data and sums the unit prices for each json item,
    and then appends that total to the json object and writes it back to the
    dump file.
    """
    # read json data
    if os.path.isfile(json_data_file):
        with open(json_data_file, 'r') as fh:
            json_data = json.load(fh)

    # tally up unit prices
    total_unit_prices = 0
    for json_str in json_data:
        total_unit_prices += Decimal(json_str.get('unit_price'))

    # overwrite dump file with updated json data
    json_data.append({'total': '{}'.format(total_unit_prices)})
    with open(json_data_file, 'w') as fh:
        json.dump(json_data, fh, sort_keys=True, indent=4)


def arg_parser():
    """ Processes command line argument(s)
    """
    parser = argparse.ArgumentParser(
        description='Program scrapes data about fruits from a grocery site.')
    parser.add_argument(
        'json_file', action="store", type=str,
        help='location of json formatted scraped data output file.')
    return vars(parser.parse_args())


if __name__ == '__main__':
    args = arg_parser()
    data_file = args['json_file']
    crawl(data_file)
    update_json_with_total_unit_prices(data_file)

