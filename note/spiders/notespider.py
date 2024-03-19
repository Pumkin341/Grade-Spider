import scrapy
from scrapy.http.request import json_request
import json


class NotespiderSpider(scrapy.Spider):
    name = "notespider"
    allowed_domains = ["portal.univ-ovidius.ro"]
        
    formdata = {}
    url = "https://portal.univ-ovidius.ro/backend/commons/user/login"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36' 
    }
    
    custom_settings = {
        'FEEDS': {
            'data/grades.json': {'format': 'json', 'overwrite': True},
        }
    }

    def start_requests(self):
        yield scrapy.FormRequest(
            url=self.url,
            formdata=self.formdata,
            callback=self.parse_login_response,
            headers=self.headers
        )

    def parse_login_response(self, response):
        date = json.loads(response.body)
        
        with open('data/date.json', 'w') as file:
            json.dump(date, file)
            
        self.headers['cookie'] = response.headers['Set-Cookie']
        
        for year in date['_students'][0]['_contexts']:    
            for ids in year['_studentYearDisciplines']:
                yield scrapy.Request(
                    url = f'https://portal.univ-ovidius.ro/backend/portal/information/scholarSituation/{ids["_id"]}',
                    callback = self.parse_grade,
                    headers = self.headers
                    
                )
        
    def parse_grade(self, response):
        
        grade = json.loads(response.body)
        yield {
            'Discipline' : grade['_name'],
            'Year' : grade['_code'],
            'Semester' : grade['_semester_number'],
            'Teachers' : grade['didactic_activities'],
            'Credits' : grade['_number_of_credits'],
            'Examination Type' : grade['_examination_form'],
            'Final Grade' : grade['_final_grade']
        }
       