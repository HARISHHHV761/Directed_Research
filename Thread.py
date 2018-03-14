#Author: Harish Holenarsipura Viswanatha
#Date: 12/06/2017
#Run parallel to the main thread and updates the configuration file.
import mysql.connector
import threading
import time
import MySQLdb
from mysql.connector import Error
import logging
import argparse
import ConfigParser
from collections import OrderedDict
from threading import Thread, Lock
#from BasicConfig import read_db
from MySQL import BasicConfig


#COnfiguration file to read the information
parser = ConfigParser.RawConfigParser()
#parser.read("/home/pi/Desktop/iotsc-master/dashboard/config.cnf")
sensors = {}

#Change host IP network 
host="10.120.62.3"
user="client2"
password="client2"
database="client2"

mutex = Lock()

#List of table to store the changes in the configuration setting for each client in the server
trigger_table=['trigger_dashboard','trigger_IMSCBroker','trigger_GrafanaBroker','trigger_id','trigger_sensor1','trigger_sensor2','trigger_sensor3','trigger_sensor4','trigger_sensor5','trigger_sensor6','trigger_sensor7','trigger_sensor8','trigger_sensor9','trigger_sensor10','trigger_sensor11']
       
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        while self.counter:
            myThread.modify_config(self.name)
            parser.read("/home/pi/Desktop/iotsc-master/dashboard/config.cnf")
            for section in parser.sections():
                if section.startswith('sensor'):
                    l = [str(settings.get(section, 'telemetry')),
                    str(settings.get(section, 'type')),
                    str(settings.get(section, 'bus')),
                    int(settings.get(section, 'port')),
                    int(settings.get(section, 'sampling'))]
                    sensors[str(settings.get(section, 'id'))] = l
                    #self.counter-=1
            time.sleep(10)
        print "Exiting " + self.name
        
    @staticmethod
    def modify_config(threadName):
        mutex.acquire()
        try:
            config1.read_db() 
            print "%s: %s" % (threadName, time.ctime(time.time()))
        finally:
            mutex.release()
            
config1=BasicConfig(host,user,password,database)                       


