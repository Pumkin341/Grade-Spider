import customtkinter as ctk
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import json

from scrapy.crawler import CrawlerRunner
from note.spiders.notespider import NotespiderSpider
from app.gradesFrame import GradesFrame

from time import sleep

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.titleLabel = ctk.CTkLabel(self, text="Login", font=("Fira Code", 30), text_color = '#2fa572')
        self.titleLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=60, sticky="nsew")

        self.nameLabel = ctk.CTkLabel(self, text="Name", font=("Fira Code", 16))
        self.nameLabel.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.nameEntry = ctk.CTkEntry(self, font=("Fira Code", 16))
        self.nameEntry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        
        self.passwordLabel = ctk.CTkLabel(self, text="Password", font=("Fira Code", 16))
        self.passwordLabel.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        
        self.passwordEntry = ctk.CTkEntry(self, font=("Fira Code", 16), show="*") 
        self.passwordEntry.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        
        self.setFormButton = ctk.CTkButton(self, text="Get Grades", font=("Fira Code", 16), corner_radius=20, border_color='#225c31', border_width=3, command=self.start_spider )
        self.setFormButton.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.errorLabel = ctk.CTkLabel(self, text="", font=("Fira Code", 16), text_color = '#ff0000')
        self.errorLabel.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.usersLabel = ctk.CTkLabel(self, text="Users", font=("Fira Code", 16))
        self.usersLabel.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        rownr = 6
        self.userButtons = [] 
        if open("data/users.json").read() != "[]":
            users = json.loads(open("data/users.json").read())
            
            for idx, user in enumerate(users):
                self.userButtons.append(ctk.CTkButton(self, text=user["username"], font=("Fira Code", 16), corner_radius=20, border_color='#225c31', border_width=3, command=lambda idx=idx: self.set_user(idx)))
                self.userButtons[-1].grid(row=rownr+1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
                rownr += 1
        else:
            self.nouserLabel = ctk.CTkLabel(self, text="No users found", font=("Fira Code", 16), text_color = '#2fa572')
            self.nouserLabel.grid(row=rownr+1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def set_user(self, index):
        self.nameEntry.delete(0, "end")
        self.passwordEntry.delete(0, "end")
        
        users = json.loads(open("data/users.json").read())
        self.nameEntry.insert(0, users[index]["username"])
        self.passwordEntry.insert(0, users[index]["password"])
  
    def crawl(self, formdata, callback):
        NotespiderSpider.formdata = formdata
        process = CrawlerProcess(get_project_settings())
        process.crawl(NotespiderSpider)
        process.start()
        process.join()
        callback(self.master.gradesFrame)

    def load_grades(self, gradesFrame):
        GradesFrame.load_grades(gradesFrame)
        
    def start_spider(self):
        username = self.nameEntry.get()
        password = self.passwordEntry.get()

        if username == "" or password == "":
            self.errorLabel.configure(text="Please fill in all fields")
            return

        users = json.loads(open("data/users.json").read())
        exists = False
        for user in users:
            if user["username"] == username:
                exists = True
        if exists == False:
            users.append({"username": username, "password": password})
            json.dump(users, open("data/users.json", "w"))
        
        self.errorLabel.configure(text="")
        
        self.crawl({"username": username, "password": password}, self.load_grades)
    
    
        
    



        
        
        