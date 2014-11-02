import scrapy
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst, Identity
import urllib2

class HistDataItem(scrapy.Item):
    url = scrapy.Field(
        input_processor=MapCompose(urllib2.unquote),
        output_processor=TakeFirst(),
    )
    tk = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst(),
    )
    date = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst(),
    )
    datemonth = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst(),
    )
    platform = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst(),
    )
    timeframe = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst(),
    )
    fxpair = scrapy.Field(
        input_processor=Identity(),
        output_processor=TakeFirst(),
    )
