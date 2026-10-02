import json
class Subject:
    def __init__(self):
        try:
            file=open('subjects.json','r')
            self.subjects=json.load(file)
            file.close()
        except FileNotFoundError:
            self.subjects=[]
    def save_subjects(self):
        file = open("subjects.json", "w")
        json.dump(self.subjects, file)
        file.close()
    def add_subject(self,name):
        self.subjects.append(name)
        self.save_subjects()
    def get_subject(self):
        return self.subjects
    def update_subject(self,p_subject,n_subject):
        for s in self.subjects:
            if p_subject==s:
                i=self.subjects.index(p_subject)
                self.subjects[i]=n_subject
                self.save_subjects()
                return True
        else:
            return False   
    def delete_subject(self,subject):
                for s in self.subjects:
                    if subject==s:
                        i=self.subjects.index(subject)
                        self.subjects.remove(self.subjects[i])
                        self.save_subjects()
                        return True
                else:
                    return False  


