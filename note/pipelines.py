# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NotePipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        
        rawteachers = adapter['Teachers']
        teachers = {}
        for i in rawteachers: 
            teachers.update({i['_name'] : i['_teachers'][0]['_last_name'] + ' ' + i['_teachers'][0]['_first_name']})

        adapter['Teachers'] = teachers
        adapter['Year'] = adapter['Year'].split('.')[2]
        if adapter['Final Grade'] == 0:
            adapter['Final Grade'] = "Not Graded Yet"
        
        return item