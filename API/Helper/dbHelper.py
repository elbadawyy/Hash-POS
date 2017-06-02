#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
import ConfigParser
import sqlite3
from sqlite3 import Error
import os
from abc import ABCMeta, abstractmethod

class dbHelper:
	
	@staticmethod
	def importDbVars():
		global dBDir
		global dBName
		global cwd
		
		cwd = os.getcwd()
		config = ConfigParser.ConfigParser()
		#Some Validations Goes Here To Check The Configration File
		config.read('../../Config/DB.conf')
		dBDir = config.get('DataBaseConfig', 'DataBaseDirPath')
		dBName = config.get('DataBaseConfig', 'DataBaseName')

	@staticmethod
	def addEntry(table, field_tuple, value_tuple):
		dbHelper.importDbVars()
		
		os.chdir(dBDir)
		try:
			conn = sqlite3.connect(dBName)
		except Error as e:
			print(e)

		field_tuple=str(field_tuple)
		value_tuple=str(value_tuple)
		print 'Connection Succeed With {}'.format(dBName)

		query="INSERT INTO "+table+" "+field_tuple+" VALUES "+value_tuple+""
		conn.execute(query)
		conn.commit()
		conn.close()
		os.chdir(cwd)

	@staticmethod
	def modEntry(table ,id , field, value):
		dbHelper.importDbVars()
		os.chdir(dBDir)
		try:
			conn = sqlite3.connect(dBName)
		except Error as e:
			print(e)
		id=str(id)
		print 'Connection Succeed With {}'.format(dBName)
		query="UPDATE "+table+" SET "+field+" = '"+value+"' WHERE id ='"+id+"'"
		conn.execute(query)
		conn.commit()
		conn.close()
<<<<<<< HEAD

=======
		os.chdir(cwd)
		
>>>>>>> 234adc3120195f9d5656fea2c95acdf342ad6ce0
	@staticmethod
	def delEntry(table, id):
		dbHelper.importDbVars()
		cwd = os.getcwd()
		os.chdir(dBDir)
		try:
			conn = sqlite3.connect(dBName)
		except Error as e:
			print(e)
		print 'Connection Succeed With {}'.format(dBName)
		id=str(id)
		query="DELETE FROM "+table+" WHERE (id = '"+id+"')"	
		conn.execute(query)
		conn.commit()
		conn.close()
		os.chdir(cwd)

	@staticmethod
	def resolvNameToID(table, name):
		dbHelper.importDbVars()
		
		os.chdir(dBDir)
		try:
			conn = sqlite3.connect(dBName)
		except Error as e:
			print(e)
		print 'Connection Succeed With {}'.format(dBName)
		query = "SELECT id FROM "+table+" WHERE name = '"+name+"'"
		cur = conn.cursor()
		cur.execute(query)
		conn.commit()
		os.chdir(cwd)
		id = cur.fetchone()
		for i in id:
			id = i

		return id


class Table:

	__metaclass__ = ABCMeta
	table=""
	field_tuple=()

	def add(self, value_tuple):

		errcode="" 
		if not(value_tuple) or not (value_tuple[0]) or(type(value_tuple) is not tuple) or (len(self.field_tuple) != len(value_tuple)):
			errcode="255"
			return errcode
		dbHelper.addEntry(self.table, self.field_tuple,value_tuple)
		errcode="0"
		return errcode

	def modify(self, id, field, value):
		errcode=""
		id=int(id) 
		if not (id) or(type(id) is not int) or (id < 0) or not (field) or(type(field) is not str) or not (value):
			errcode="255"
			return errcode
		dbHelper.modEntry(self.table ,id, field, value)
		errcode="0"
		return errcode

	def delete(self, id):
		errcode=""
		id=int(id) 
		if not(id) or (id < 0) or(type(id) is not int):
			errcode="255"
			return errcode
		dbHelper.delEntry(self.table, id)
		errcode="0"
		return errcode

	@abstractmethod    
	def retTableName(self):
		pass
