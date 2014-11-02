# -*- coding: utf-8 -*-

# Scrapy settings for histdata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'histdata'

SPIDER_MODULES = ['histdata.spiders']
NEWSPIDER_MODULE = 'histdata.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; CrOS x86_64 6415.2.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2202.5 Safari/537.36'

DOWNLOAD_DELAY = 1.0
