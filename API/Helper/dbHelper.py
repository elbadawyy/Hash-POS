#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
import ConfigParser
import sqlite3
from sqlite3 import Error
import os

class dbHelper:
	
	@staticmethod
	def importDbVars():
		global dBDir
		global dBName
		config = ConfigParser.ConfigParser()
		#Some Validations Gous Here To Check The Configration File
		config.read('../../Config/DB.conf')
		dBDir = config.get('DataBaseConfig', 'DataBaseDirPath')
		dBName = config.get('DataBaseConfig', 'DataBaseName')

	@staticmethod
	def addWarehouseInDb(warehouseName="",desc=""):
		dbHelper.importDbVars()
	
		os.chdir(dBDir)
		
		try:
			conn = sqlite3.connect(dBName)
		except Error as e:
			print(e)
		
		print 'Connection Succeed With {}'.format(dBName)
		query="INSERT INTO warehouses(name,description) VALUES ('"+warehouseName+"','"+desc+"')"
		conn.execute(query)
		conn.commit()