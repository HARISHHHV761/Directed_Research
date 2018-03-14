#Author: Harish Holenarsipura Viswanatha
#Date: 12/06/2017
# Use this script if wanted to create the tables and add values to it.
# Functions provided to create tables, update entries and alter table information.
from __future__ import print_function
import MySQLdb
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

TABLES = {}
TABLES['dashboard'] = (
    "CREATE TABLE dashboard ("
    " url varchar(20) NOT NULL,"
    " iotsc_port int(11) NOT NULL,"
    " access_token int(11) NOT NULL,"
    " topic_telemetry varchar(30) NOT NULL,"
    " topic_attributes varchar(30) NOT NULL,"
    ") ENGINE=InnoDB")

TABLES['IMSCBroker'] = (
    "CREATE TABLE IMSCBroker("
    " i3_url varchar(30) NOT NULL,"
    " i3_port int(11) NOT NULL,"
    " i3_topic varchar(30) NOT NULL,"
    " i3_user_name varchar(30) NOT NULL,"
    " i3_password varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['GrafanaBroker'] = (
    "CREATE TABLE GrafanaBroker ("
    " eclipse_url varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['id'] = (
    "CREATE TABLE id ("
    " myid int(11) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor1'] = (
    "CREATE TABLE sensor1 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port int(11) NOT NULL,"
    " sampling int(11) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor2'] = (
    "CREATE TABLE sensor2 ("
    " id varchar(14) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor3'] = (
    "CREATE TABLE sensor3 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor4'] = (
    "CREATE TABLE sensor4 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(30) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor5'] = (
    "CREATE TABLE sensor5 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(30) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor6'] = (
    "CREATE TABLE sensor6 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor7'] = (
    "CREATE TABLE sensor7 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor8'] = (
    "CREATE TABLE sensor8 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"

    ") ENGINE=InnoDB")

TABLES['sensor9'] = (

    "CREATE TABLE sensor9 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor10'] = (
    "CREATE TABLE sensor10 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['sensor11'] = (
    "CREATE TABLE sensor11 ("
    " id varchar(30) NOT NULL,"
    " type varchar(30) NOT NULL,"
    " bus ENUM('analog','digital','i2c'),"
    " port  int(11) NOT NULL,"
    " sampling int(14) NOT NULL,"
    " telemetry varchar(30) NOT NULL"
    ") ENGINE=InnoDB")



ADD_dashboard = (
    "INSERT INTO dashboard "
    "(url,iotsc_port,access_token,topic_telemetry,topic_attributes)"
    "VALUES(%s,%s,%s,%s,%s)")

ADD_IMSCBroker = (
    "INSERT INTO IMSCBroker "
    "(i3_url,i3_port,i3_topic,i3_user_name,i3_password)"
    "VALUES(%s,%s,%s,%s,%s)")

ADD_GrafanaBroker =(
    "INSERT INTO GrafanaBroker "
    "eclipse_url"
    "VALUES('%s')")

ADD_id = (
    "INSERT INTO id "
    "(myid)"
    "VALUES(%s)")

ADD_sensor1 = (
    "INSERT INTO sensor1 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor2 = (
    "INSERT INTO sensor2 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor3 = (
    "INSERT INTO sensor3 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor4 = (
    "INSERT INTO sensor4 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor5 = (
    "INSERT INTO sensor5 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor6 = (
    "INSERT INTO sensor6 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor7 = (
    "INSERT INTO sensor7 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor8 = (
    "INSERT INTO sensor8 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor9  = (
    "INSERT INTO sensor9 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor10 = (
    "INSERT INTO sensor10 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

ADD_sensor11 = (
    "INSERT INTO sensor11 "
    "(id,type,bus,port,sampling,telemetry)"
    "VALUES(%s,%s,%s,%s,%s,%s)")

id=9003
eclipse='eclipse.usc.edu'

data_dashboard=('neptune.usc.edu',2883,'xJispNqriF2A7OEopFgH','v1/devices/me/telemetry','v1/devices/me/attributes')
data_IMSCBroker=('imscspark3.usc.edu',1880,'USC/UPC/sensor2','iottestbed','j7B764')
data_id=("INSERT INTO id(myid) VALUES (%s)" % id)
data_GrafanaBroker=("INSERT INTO GrafanaBroker(eclipse_url) VALUES (%s)" % eclipse)
data_sensor1=('dht_temp','sensor','digital',2,1000,'temperature')
data_sensor2=('dht_hum','sensor','digital',2,1000,'humidity')
data_sensor3=('temp_interior','sensor','analog',0,1000,'temperature_interior')
data_sensor4=('light_digital','sensor','i2c',1,1000,'light')
data_sensor5=('pir','sensor','digital',3,100,'pir')
data_sensor6=('vibration','sensor','analog',1,100,'vibration')
data_sensor7=('sound','sensor','analog',2,100,'Sound')
data_sensor8=('gas_mq2','sensor','analog',2,5000,'gas_mq2')
data_sensor9=('gas_mq3','sensor','analog',2,5000,'gas_mq3')
data_sensor10=('gas_mq5','sensor','analog',3,5000,'gas_mq5')
data_sensor11=('gas_mq9','sensor','analog',4,5000,'gas_mq9')



class Config:
    def __init__(self, host, user, password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database =database

    def createtable(self):
        db=mysql.connector.connect(user= self.user,password=self.password,host=self.host,database=self.database)
        cursor = db.cursor()
        for name, ddl in TABLES.iteritems():
            try:
                print("Creating table {}: ".format(name))
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

            cursor.close()
            db.close()
    def inserttable(self):
        db=mysql.connector.connect(user= self.user,password=self.password,host=self.host,database=self.database)
        cursor = db.cursor()
        try:
            cursor.execute(ADD_dashboard, data_dashboard)
            cursor.execute(ADD_IMSCBroker, data_IMSCBroker)
            cursor.execute(data_id)
            cursor.execute(data_GrafanaBroker)
            cursor.execute(ADD_sensor1, data_sensor1)
            cursor.execute(ADD_sensor2, data_sensor2)
            cursor.execute(ADD_sensor3, data_sensor3)
            cursor.execute(ADD_sensor4, data_sensor4)
            cursor.execute(ADD_sensor5, data_sensor5)
            cursor.execute(ADD_sensor6, data_sensor6)
            cursor.execute(ADD_sensor7, data_sensor7)
            cursor.execute(ADD_sensor8, data_sensor8)
            cursor.execute(ADD_sensor9, data_sensor9)
            cursor.execute(ADD_sensor10, data_sensor10)
            cursor.execute(ADD_sensor11, data_sensor11)
            db.commit()
            print("Added SUccessfully")
        except:
            print "Entries already created, not possible to add duplicate entry"
                    
        cursor.close()
        db.close()
            

    def update_table(self,Table_Name,Name,ID):
        db = MySQLdb.connect(self.host, self.user, self.password, self.database)
        args = (Name, ID)
        sql = "UPDATE %s SET ID='%d' WHERE Name='%s'" %(Table_Name,ID,Name)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print('Table updated succesfully')
        
    def alter_table(self,Table_Name,column_name):
        db = MySQLdb.connect(self.host, self.user, self.password, self.database)
        args = (Name, ID)
        sql = "ALTER TABLE %s ADD %s int(11) NOT NULL" %(Table_Name,column_name)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print('Table altered succesfully')        
            
            	
config1=Config(host,user,password,database)
#config1.createtable()
#config1.inserttable()
#config1.update_table("Pi2","IOTSC-client1",10)
