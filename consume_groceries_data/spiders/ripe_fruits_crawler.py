# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from consume_groceries_data.items import ConsumeGroceriesDataItem


class RipeFruits(CrawlSpider):
    """ The spider class defines attributes that tell it where to start scraping
    and how deep to follow links within the given list of allowed domains.

    It also defines a parse method telling it how to handle scraped data.
    """

    name = 'ripefruits'
    allowed_domains = ['hiring-tests.s3-website-eu-west-1.amazonaws.com']
    start_urls = [
        'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/'
        '2015_Developer_Scrape/5_products.html'
    ]
    custom_settings = {
        'BOT_NAME': 'ripe_fruit_scraper',
        'DEPTH_LEVEL': 2,
        'DOWNLOAD_DELAY': 1,
        'REDIRECT_ENABLED': True,
    }
    rules = [
        Rule(
            LinkExtractor(allow=['2015_Developer_Scrape/']),
            callback='parse_item',
            follow=True
        )
    ]

    def parse_item(self, response):
        """ Parses the response data, extracting and loading it into an
        instance of the items container.
        """
        # only extracts content from the links followed on the starting url,
        # but not the actual starting page
        if response.url not in RipeFruits.start_urls:
            title = response.xpath('//title/text()').extract()[0]
            description = response.xpath(
                '//meta[@name="description"]/@content').extract()[0]
            unit_price = response.xpath(
                '//div[@class="pricing"]/p[@class="pricePerUnit"]/text()'
            ).extract()[0].strip()

            item = ConsumeGroceriesDataItem()
            item['title'] = title
            item['description'] = description
            item['unit_price'] = unit_price.strip('£')
            yield item
