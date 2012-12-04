import json

from scrapy.conf import settings
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class OnderwijsinspectiePipeline(object):
    def __init__(self):
        self.organisations = []
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def process_item(self, item, spider):
        self.organisations.append(dict(item))

        return item

    def spider_closed(self, spider):
        with open('%s/%s.json' % (settings['EXPORT_DIRECTORY'],
            settings['EDUCATION_SECTOR']), 'w') as f:
            json.dump(self.organisations, f, indent=4, separators=(',', ': '))
