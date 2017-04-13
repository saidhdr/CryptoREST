from distutils.util import strtobool
from datetime import datetime
from datetime import timedelta
import sys


class LogFileStructMapper:
    date = 0
    time = 1
    mac_address = 2
    client_known = 3
    ip_address = 4
    ip_internal = 5
    ip_known = 6
    user_id = 7
    user_known = 8
    success = 9


class IpType:
    internal = 'internal'
    external = 'external'
    known = 'known'


class MyMethods:
    def __init__(self):
        self.matchedLogs = []
        self.matchedLogsPrevious = []
        self.logFileLines = []
        self.logFileLines = [line.rstrip('\n') for line in open('static/dummyLog.txt', 'r')]


    def hellowWorld(self):
        return "hello, world from class"


    def getLatestLog(self):
        result = []    
        self.logFileLines = [line.rstrip('\n') for line in open('static/dummyLog.txt', 'r')]
        result.extend(self.logFileLines)
        return result


    def clearMatchedLogs(self,keepOldValues = True):
        if keepOldValues == True:
            self.matchedLogsPrevious.clear()
            self.matchedLogsPrevious.extend(self.matchedLogs)
        self.matchedLogs.clear()


    def findIpAddresses(self,ipAddress):
        result = []
        for line in self.logFileLines:
            lineSplitted = line.split()
            if lineSplitted[LogFileStructMapper.ip_address] == ipAddress:
                result.append(line)
                self.matchedLogs.append(line)
        return result


    def isIpTypeOf(self,ipAddress, ipType):
        result = []
        for line in self.logFileLines:
            lineSplitted = line.split()
            if IpType.internal == ipType:
                if (
                        lineSplitted[LogFileStructMapper.ip_address] == ipAddress and
                        strtobool(lineSplitted[LogFileStructMapper.ip_internal]) == True
                    ):    
                    return True
            elif IpType.external == ipType:
                if (
                        lineSplitted[LogFileStructMapper.ip_address] == ipAddress and 
                        strtobool(lineSplitted[LogFileStructMapper.ip_internal]) == False
                    ):    
                    return True
            else:
                if (
                        lineSplitted[LogFileStructMapper.ip_address] == ipAddress and 
                        strtobool(lineSplitted[LogFileStructMapper.ip_known]) == True
                    ):    
                    return True
        return False


    def isUserKnown(self,userId):
        result = []
        for line in self.logFileLines:
            lineSplitted = line.split()
            if lineSplitted[LogFileStructMapper.user_id] == userId:
                return strtobool(lineSplitted[LogFileStructMapper.user_known]) == True
        return False


    def isClientKnown(self,macAddress):
        result = []
        for line in self.logFileLines:
            lineSplitted = line.split()
            if lineSplitted[LogFileStructMapper.mac_address] == macAddress:
                return strtobool(lineSplitted[LogFileStructMapper.client_known]) == True
        return False


    def getLastSuccessfulLoginDate(self,userId):
        result = []
        for line in self.logFileLines:
            lineSplitted = line.split()
            if (
                lineSplitted[LogFileStructMapper.user_id] == userId and
                strtobool(lineSplitted[LogFileStructMapper.success]) == True
                ):
                result.append(line)
        if len(result) > 1:
            result.sort(key = lambda d: (datetime.strptime(d.split()[0], "%Y%m%d"), datetime.strptime(d.split()[1], "%H:%M:%S")), reverse = True)
        return result


    def getLastFailedLoginDate(self,userId):
        result = []
        for line in self.logFileLines:
            lineSplitted = line.split()
            if (
                lineSplitted[LogFileStructMapper.user_id] == userId and
                strtobool(lineSplitted[LogFileStructMapper.success]) == False
                ):
                result.append(line)
        if len(result) > 1:
            result.sort(key = lambda d: (datetime.strptime(d.split()[0], "%Y%m%d"), datetime.strptime(d.split()[1], "%H:%M:%S")), reverse = True)
        return result


    def getFailedLoginCountLastWeek(self):
        result = []
        today = datetime.today()
        week_ago = today - timedelta(days=7) 
        for line in self.logFileLines:
            lineSplitted = line.split()
            logDate = datetime.strptime(lineSplitted[LogFileStructMapper.date],"%Y%m%d")
            if (
                strtobool(lineSplitted[LogFileStructMapper.success]) == False and
                week_ago <= logDate <= today
                ):
                result.append(line)
        if len(result) > 1:
            result.sort(key = lambda d: (datetime.strptime(d.split()[0], "%Y%m%d"), datetime.strptime(d.split()[1], "%H:%M:%S")), reverse = True)
        return result

    
    def insertNewLog(self,newLog):
        f = open('static/dummyLog.txt', 'a')
        f.write("\n"+newLog)
        f.close()

    def cleanUpMess(self):
        #this is just a dirty trick to cleanup
        with open('static/tempFile.txt', "w"):
            pass

        s = set()
        print(s)
        with open('static/tempFile.txt', 'w') as out:
            for line in open('static/dummyLog.txt'):
                if line not in s:
                    out.write(line)
                    s.add(line)

        with open('static/dummyLog.txt', "w"):
            pass
        
        with open("static/dummyLog.txt") as f:
            with open("static/dummyLog.txt", "w") as f1:
                for line in f:
                    if "ROW" in line:
                        f1.write(line) 
