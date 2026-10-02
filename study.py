import json
class Study:
    def __init__(self):
        try:
            file=open("study.json",'r')
            self.tracker=json.load(file)
            file.close()
        except:
            self.tracker=[]
    def savefile(self):
        file=open('study.json','w')
        json.dump(self.tracker,file)
        file.close()
    def add_tracker(self,sbj,hr,date):
        self.tracker.append({"subject":sbj,"hours":hr,"date":date})
        self.savefile()
    def get_tracker(self):
        return self.tracker 
    def update(self,p_s,n_s):
        for record in self.tracker:
            if record['subject']==p_s:
                record['subject']=n_s
                self.savefile()
                return True
        else:
            return False  
    def delete(self,s):
        for record in self.tracker:
            if record['subject']==s:
                self.tracker.remove(record)
                self.savefile()
                return True 
        else:
            return False
