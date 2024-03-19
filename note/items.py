# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    year = scrapy.Field()
    discipline = scrapy.Field()
    semester = scrapy.Field()
    teachers = scrapy.Field()
    creditss = scrapy.Field()
    examination_type = scrapy.Field()
    final_grade = scrapy.Field()

