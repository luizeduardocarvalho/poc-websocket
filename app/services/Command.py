from services.Data import DataController
from datetime import datetime

class Command:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        
class CommandService:
    @staticmethod
    def pushCommand(name):
        command = Command(name, datetime.now())
        DataController.insertCommand(command)
        print("- [INFO] - comando salvo.")
        DataController.printCommand()

    @staticmethod
    def getCommands():
        rows = DataController.getCommands()
        commandLine = []
        for row in rows:
            commandLine.append(row)
        return commandLine