import scrapy
from histdata.items import HistDataItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.loader import ItemLoader
import itertools
import urllib2

class DecodeLinkExtractor(LinkExtractor):
    def extract_links(self, response):
        links = super(DecodeLinkExtractor, self).extract_links(response)
        for link in links:
            link.url = urllib2.unquote(link.url).replace('=','')
        return links
class NoFollowLinkExtractor(LinkExtractor):
    def extract_links(self, response):
        return [i for i in super(NoFollowLinkExtractor, self).extract_links(response) if not i.nofollow]

class HistDataSpider(CrawlSpider):
    name = "histdata"
    allowed_domains = ["histdata.com"]
    start_urls = [
        "http://www.histdata.com/download-free-forex-historical-data/?/ascii/tick-data-quotes/eurgbp/2013"
    ]

    rules = (
        Rule(DecodeLinkExtractor(allow=('download-free-forex-historical-data/\?/ascii/tick-data-quotes/.*/[0-9]+/[0-9]+', )), callback='parse_item'),
        Rule(DecodeLinkExtractor(allow=('download-free-forex-historical-data/\?/ascii/tick-data-quotes/', )))
    )

    def parse_item(self, response):
        parser = ItemLoader(item=HistDataItem())
        parser.add_value('url', response.url) 
        fields = ['tk', 'date', 'datemonth', 'platform', 'timeframe', 'fxpair']
        for field in fields:
            parser.add_value(field, getValue('#'+field, response))
        item = parser.load_item()
        formdata = dict(zip(fields, [item['tk'], item['date'], item['datemonth'], item['platform'], item['timeframe'], item['fxpair']]))
        request = scrapy.FormRequest.from_response(response, formnumber=0, formdata=formdata, callback=getData)
        return request


def getValue(selector, response):
    return list(itertools.chain(*[i.xpath('@value').extract() for i in response.css(selector)]))

def getData(response):
    filename = response.headers['Content-Disposition'].split('=')[-1]
    with open(filename, "wb") as f:
        f.write(response.body)

