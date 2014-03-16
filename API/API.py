#!/usr/bin/env python
#Python API
#2/10/2014
#CS492

import sqlite3
import sys
import socket
	
#Initialize/Create SQL lite Database with TrainLab Setup
conn=sqlite3.connect('Train.db')

#Initialize Possible User DB
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='USER'"
if not conn.execute(tb_exists).fetchone():
	conn.execute('''CREATE TABLE USER
		(NUMBER INT PRIMARY KEY		NOT NULL,
		USERNAME TEXT	NOT NULL,
		PASSWORD TEXT	NOT NULL);''')
	print "User Table Created"

#Initialize Trains DB
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='TRAIN'"
if not conn.execute(tb_exists).fetchone():
	conn.execute('''CREATE TABLE TRAIN
		(NUMBER INT PRIMARY KEY     NOT NULL,
		SPEED         INT,
		LOCATION      INT,
		LIGHTS        INT,
		NOISE         INT,
		LOCK          INT);''')
	print "Train Table Created"

#Initialize Turnouts DB
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='TURNOUT'"
if not conn.execute(tb_exists).fetchone():
	conn.execute('''CREATE TABLE TURNOUT
		(NUMBER INT PRIMARY KEY     NOT NULL,
		STATUS	INT,
		LOCK   INT);''')
	print "Turnout Table Created"

#Authentication KEY
#KEY = ...... whatever we get from socket communication

#Constant Train Numbers
TrainNum = [420, 123, 411]

#Train array to hold Train objects
TrainObj = [] * 3

#Turnout array
TurnoutObj = [] * 23


class Train(object):
	number = 0
	speed = 0
	locked = 0
	noise = 0
	lights = 0
	location = 0
	direction = 0
    #The class "constructor" - It's actually an initializer 
	def __init__(self, number, speed, location, lights, noise, lock):
		self.number = number
		self.speed = speed
		self.location = location
		self.lights = lights
		self.noise = noise
		self.lock = lock
	def requestSpeed(self, KEY, ID, NUM):
		self.speed = send(KEY + "[TSPD|" + str(ID) + "|SPEED]")
		conn.execute('''UPDATE TRAIN SET SPEED = ? WHERE NUMBER = ?''', (self.speed, NUM))
		conn.commit()	
	def requestLocation(self, KEY, ID, NUM):
		self.location = send(KEY + "[TLOC|" + str(ID) + "|SECT#]")
		conn.execute('''UPDATE TRAIN SET LOCATION = ? WHERE NUMBER = ?''', (self.location, NUM))
		conn.commit()	
	def requestLock(self, KEY, ID, NUM):
		self.lock = send(KEY + "[TLCK|" + str(ID) + "|STATE]")
		conn.execute('''UPDATE TRAIN SET LOCK = ? WHERE NUMBER = ?''', (self.lock, NUM))
		conn.commit()	
	def setNoise(self, KEY, ID, NUM, Change):
		self.noise = send(KEY + "[SND|" + str(ID) + "|" + Change + "]")
		conn.execute('''UPDATE TRAIN SET NOISE = ? WHERE NUMBER = ?''', (self.noise, NUM))
		conn.commit()
	

class Turnout(object):
	number = 0
	status = 0
	lock = 0

    # The class "constructor" - It's actually an initializer 
	def __init__(self, number, status, lock):
		self.number = number
		self.status = status
		self.lock = lock     

	def make_turnout(self, number, status, locked):
		Turnout = Turnout(number, status, lock)
		return Turnout
		
	def requestLock(self, KEY, NUM):
		self.lock = send(KEY + "[TOLK|" + str(NUM) + "|STATE]")
		conn.execute('''UPDATE TURNOUT SET LOCK = ? WHERE NUMBER = ?''', (self.lock, NUM))
		conn.commit()
	
	def requestStatus(self, KEY, NUM):
		self.status = send(KEY + "[TURN|" + str(NUM) + "|STATE]")
		conn.execute('''UPDATE TURNOUT SET STATUS = ? WHERE NUMBER = ?''', (self.status, NUM))
		conn.commit()

#Port For Train Communication
Port = 54321
#Not sure if TrainLab start server or API
#IP Address for Train Lab
#Host = "140.160.136.227"

Host = "74.125.0.0"
#Last part in each socket message to mark endswith
End = ".Done"

#Function to send Data through Socket with end marker then receive response
def send(data):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((Host,Port))
	try :
		s.sendall(data+End)
	except socket.error:
		#Send failed
		print 'Send failed'
		sys.exit()
	Info = s.recv(64)
	s.close()
	return Info
	
def update():
	#Continue listening for more train info until closed
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	while True:
		s.connect((Host,Port))
		s.recv(1024)
		break
	s.close()
	return

def main():

	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print 'Socket created'
	except socket.error, msg:
		print 'Failed to create socket.'
		sys.exit();	
		
	#connect to Train Host
	s.connect((Host,Port))
	print 'Socket Connected to ' + host + ' on ip ' + remote_ip
	
	#Send message that we are connected
	s.send('Initialized')
	#Wait for confirmation
	Key = s.recv(1024)
	print Key
	s.close();
	
	
	#initialize setup for trains on start
	for i in range (0, 2):
		Num = TrainNum[i]
		TrainObj.append(Train(Num, 0, 0, 0, 0, 0))
		TrainObj[i].requestLock(Key, Num, i)
		#No method for requesting noise Train.requestNoise(TrainNum[i])
		#No Method for reuesting light Train.requestLights(TrainNum[i])
		TrainObj[i].requestLocation(Key, Num, i)
		TrainObj[i].requestSpeed(Key, Num, i)
	#initialize the 23 turnouts
	for i in range (0, 22):	
		TurnoutObj.append(Train())
		TurnoutObj[i].createTO(i, 0, 0)
		TurnoutObj[i].requestStatus(Key, i)
		TurnoutObj[i].requestLock(Key, i)
	
	return
	
		
if __name__ == '__main__':
    main()


