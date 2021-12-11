import os
import datetime
import json

class Logs:
    def __init__(self, name:str="logs.log"):
        self.name=name
        self.initialize()

    def initialize(self):
        if not os.path.exists(self.name):
            with open(self.name, "w") as f:
                pass
            

    def log(self, content, priority="root"):
        with open(self.name, "r") as f:
            bLogs = f.read()

        with open(self.name, "w") as f:
            f.write(bLogs + priority + ": " + str(datetime.datetime.now()) +": "+ content + "\n")

class JSONSaver:
    def __init__(self, name:str="keys.json"):
        self.name=name
        self.initialize()

    def initialize(self):
        if not os.path.exists(self.name):
            with open(self.name, "w") as f:
                f.write("{}")

    def save(self, content:dict):

        with open(self.name, "w") as f:
            f.write(json.dumps(content))