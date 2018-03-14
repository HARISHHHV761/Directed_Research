#Author: Harish Holenarsipura Viswanatha
#Date: 12/06/2017

import mysql.connector
import threading
import time
import MySQLdb
from mysql.connector import Error
import logging
import configparser
import ConfigParser
import argparse
from collections import OrderedDict
from threading import Thread, Lock

#Configuration file to read the information
parser = ConfigParser.RawConfigParser()
parser.read("/home/pi/Desktop/iotsc-master/dashboard/config.cnf")

#Change host IP network and the client information 
host="192.168.0.15"
user="client2"
password="client2"
database="client2"

mutex = Lock()

#List of table to store the changes in the configuration setting for each client in the server
trigger_table=['trigger_dashboard','trigger_IMSCBroker','trigger_GrafanaBroker','trigger_id','trigger_sensor1','trigger_sensor2','trigger_sensor3','trigger_sensor4','trigger_sensor5','trigger_sensor6','trigger_sensor7','trigger_sensor8','trigger_sensor9','trigger_sensor10','trigger_sensor11']

class BasicConfig:
    def __init__(self, host, user, password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database =database
 
    def read_db(self):
        conn = MySQLdb.connect(self.host,self.user,self.password ,self.database)
        cursor = conn.cursor()
        try:
            for table in trigger_table:
                entry=("SELECT * FROM %s" % table )
                result=cursor.execute(entry)
                table_name=table.split('_')
                trans=1
                name=table_name[1]
                output=[]
                j=0
                k=0
                if result:
                    section = OrderedDict(parser.items(name))
                    for row in cursor:
                        if k==0:
                            last=row[len(row)-1]
                        if (trans==last):
                            output=[]    
                        for i in row:
                            output.append(i)                           
                        k=k+1            
                    for key,value in section.iteritems():
                        parser.set(name,key,output[j])
                        #print output[j]
                        #print key,value
                        with open("/home/pi/Desktop/iotsc-master/dashboard/config.cnf", 'wb') as configfile:
                            parser.write(configfile)
                        j=j+1
                else:
                    continue
        except:
            cursor.execute(entry)
            print "ignore the exception"   


