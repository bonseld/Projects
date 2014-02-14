#Python API
#2/10/2014
#CS492

import sqlite3
import sys

#Initialize/Create SQL lite Database with TrainLab Setup

conn = sqlite3.connect('Train.db')

#Initialize Trains DB Status'
conn.execute('''CREATE TABLE TRAIN
       (NUMBER INT PRIMARY KEY     NOT NULL,
       SPEED         INT,
       LOCATION      INT,
       LIGHTS        INT,
       NOISE         INT,
       LOCK          INT);''')

#Initialize Turnouts DB Status' 
conn.execute('''CREATE TABLE TURNOUT
       (NUMBER INT PRIMARY KEY     NOT NULL,
	LOCK   INT);''')
	
#Initialize Sections DB Status'   
conn.execute('''CREATE TABLE SECTION
       (NUMBER INT PRIMARY KEY     NOT NULL,
	LOCK   INT);''')


#Constant Train Numbers
TrainNum = [420, 300, 200]

#Train array to hold Train objects
TrainObj = []

#Turnout array
TurnoutObj = []

#Section array
SectionObj = []


class Train(object):
	number = 0
	speed = 0
	locked = 0
	noise = 0
	lights = 0
	location = 0
	direction = 0
	
        # The class "constructor" - It's actually an initializer 
    	def __init__(self, number, speed, location, lights, noise, locked):
		self.number = number
    		self.speed = speed
    		self.location = location
    		self.lights = lights
		self.noise = noise
		self.locked = locked
        
	def make_train(number, speed, location, lights, noise, lock):
    		Train = Train(number, speed, location, lights, noise, lock)
    		return Train	

	
class Turnout(object):
	number = 0
	status = 0
	locked = 0
	
        # The class "constructor" - It's actually an initializer 
    	def __init__(self, number, status, locked):
		self.number = number
		self.status = status
		self.locked = locked      

	def make_turnout(number, status, locked):
    		Turnout = Turnout(number, status, locked)
    		return Turnout
	
	
class Section(object):
	number = 0
	status = 0

        #The class "constructor" - It's actually an initializer 
	def __init__(self, number, status):
		self.number = number
		self.status =  status
        

	def make_section(number, status):
    		Section = Section(number, status)
    		return Section
	

#initialize setup for trains on start
for i in range (0, 2):
	lock = reqTrain.Lock(TrainNum[i])
	noise = reqTrain.Noise(TrainNum[i])
	light = reqTrain.Lights(TrainNum[i])
	loc = reqTrain.Location(TrainNum[i])
	spd = reqTrain.Speed(TrainNum[i])
	TrainObj.append(Train(TrainNum[i], spd, loc, light, noise, lock))

#initialize the 23 turnouts
for i in range (0, 22):	
	TurnoutObj.append(Turnout( i, reqTurn.stat(i), reqTurn.lock(i)))

#initialize the 104 sections
for i in range (0, 103):	
	SectionObj.append(Section( i, reqSec.stat(i)))

##### Create Functions for Requests for Train/Turnout/Section based on Protocol ######

#[TLOC|TRAIN_ID|SECT#]		protocol for location
#[TSPD|TRAIN_ID|SPEED]		protocol for speed	
#[TLCK|TRAIN_ID|STATE]		protocol for lock

#[TURN|TO#|STATE]		protocol for status
#[TOLK|TO#|STATE]		protocol for lock

##### Decide when to store in SQL Databases and retrieve data from them     ######
##### After initialization step should be only sending messages for changes ######
##### To database and then retrieving current information from them         ######
	
	
	
	
	
	
	
	
	
	
	
	
	
