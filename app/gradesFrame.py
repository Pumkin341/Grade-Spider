import customtkinter as ctk
import json

class GradesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
        with open('data/grades.json') as file:
            if file.read() == "":
                self.gradesLabel = ctk.CTkLabel(self, text="No grades found", font=("Fira Code", 16), text_color = '#2fa572')
                self.gradesLabel.grid(row=0, column=0, padx=11, pady=5, sticky="w")
                return
            else:
                file.close()
                self.load_grades()
                
    def load_grades(self):
        row = 0    
        data = json.load(open('data/grades.json'))
        for discipline in data:
            
            discipline['Discipline'] = discipline['Discipline'].replace('Äƒ', 'a').replace('Å£', 't').replace('ÅŸ', 's').replace('È›', 't').replace('Å£', 't')
                    
            self.disciplineHeaderLabel = ctk.CTkLabel(self, text=f"{discipline['Discipline']}", font=("Fira Code", 16), text_color = '#2fa572')
            self.disciplineHeaderLabel.grid(row=row, column=0, padx=11, pady=5, sticky="w", columnspan=3)
            
            self.yearLabel = ctk.CTkLabel(self, text=f"Year: {discipline['Year']}", font=("Fira Code", 11))
            self.yearLabel.grid(row=row+1, column=0, padx=5, pady=5, sticky = "w")
            
            self.semesterLabel = ctk.CTkLabel(self, text=f"Semester: {discipline['Semester']}", font=("Fira Code", 11))
            self.semesterLabel.grid(row=row+1, column=1, padx=5, pady=5,sticky="w")
            
            self.typeLabel = ctk.CTkLabel(self, text=f"Exam Type: {discipline['Examination Type']}", font=("Fira Code", 11))
            self.typeLabel.grid(row=row+1, column=2, padx=5, pady=5,sticky="w")
            
            for rownr, i in enumerate(discipline['Teachers']):
                self.teachersLabel = ctk.CTkLabel(self, text=f"{i}: {discipline['Teachers'][i].replace('Äƒ', 'a').replace('Å£', 't').replace('ÅŸ', 's').replace('Ã®', 'i').replace('È™', 't')}", font=("Fira Code", 11))
                self.teachersLabel.grid(row=row+rownr+2, column=0, padx=5, pady=5, sticky='w')
            
            self.creditsLabel = ctk.CTkLabel(self, text=f"Credits: {discipline['Credits']}", font=("Fira Code", 11))
            self.creditsLabel.grid(row=row+2, column=1, padx=5, pady=5, sticky='w')
            
            self.gradeLabel = ctk.CTkLabel(self, text=f"Grade: {discipline['Final Grade']}", font=("Fira Code", 11))
            self.gradeLabel.grid(row=row+2, column=2, padx=5, pady=5, sticky='w')
            
            row += 4
        

        

