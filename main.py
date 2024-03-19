from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from note.spiders.notespider import NotespiderSpider
import json

import customtkinter as ctk
from app.loginFrame import LoginFrame
from app.gradesFrame import GradesFrame


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Grades")
        height = 800
        width = 1200
        x = self.winfo_screenwidth() // 2 - width // 2
        y = self.winfo_screenheight() // 2 - height // 2
        self.geometry("{}x{}+{}+{}".format(width, height, x, y))
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.loginFrame = LoginFrame(self)
        self.loginFrame.grid(row=0, column=0, padx=20, pady=20, sticky = "nsew")
        
        self.gradesFrame = GradesFrame(self)
        self.gradesFrame.grid(row=0, column=1, columnspan = 2, padx=20, pady=20, sticky = "nsew")

if __name__ == "__main__":

    app = App()
    app.mainloop()
