from distutils.util import strtobool


class MyMethods:
    def __init__(self):
        self.logFileLines = []
        self.logFileLines = [line.rstrip('\n') for line in open('static/dummyLog.txt', 'r')]

 
    def hellowWorld(self):
        return "hello, world from class"

    def getLatestLog(self):
        result = []    
        self.logFileLines = [line.rstrip('\n') for line in open('static/dummyLog.txt', 'r')]
        result.extend(self.logFileLines)
        
        return result