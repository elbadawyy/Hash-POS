#! /usr/bin/python2.7
# -*- coding: utf-8 -*- 

import ConfigParser
import sqlite3
from sqlite3 import Error
import os
from abc import ABCMeta, abstractmethod

curr_dir = os.path.dirname(os.path.realpath(__file__))
api_dir = os.path.abspath(os.path.join(curr_dir, '..'))
root_dir = os.path.abspath(os.path.join(api_dir, '..'))
config_dir = os.path.abspath(os.path.join(root_dir, 'Config'))
config_file = os.path.abspath(os.path.join(config_dir, 'DB.conf'))

class API:
	
	@staticmethod
	def importDBVars():
		global db_dir
		global db_name
		config = ConfigParser.ConfigParser()
		#Some Validations Goes Here To Check The Configration File
		config.read(config_file)
		db_dir = config.get('DataBaseConfig', 'DataBaseDirPath')
		db_name = config.get('DataBaseConfig', 'DataBaseName')

	@staticmethod
	def addEntry(table, field_tuple, value_tuple):
		API.importDBVars()
		
		os.chdir(db_dir)
		try:
			conn = sqlite3.connect(db_name)
		except Error as e:
			print(e)

		field_tuple=str(field_tuple)
		value_tuple=str(value_tuple)
		print 'Connection Succeed With {}'.format(db_name)

		query="INSERT INTO "+table+" "+field_tuple+" VALUES "+value_tuple+""
		conn.execute(query)
		conn.commit()
		conn.close()

	@staticmethod
	def modEntry(table ,id , field, value):
		API.importDBVars()
		os.chdir(db_dir)
		try:
			conn = sqlite3.connect(db_name)
		except Error as e:
			print(e)
		id=str(id)
		print 'Connection Succeed With {}'.format(db_name)
		query="UPDATE "+table+" SET "+field+" = '"+value+"' WHERE id ='"+id+"'"
		conn.execute(query)
		conn.commit()
		conn.close()
		
	@staticmethod
	def delEntry(table, id):
		API.importDBVars()
		os.chdir(db_dir)
		try:
			conn = sqlite3.connect(db_name)
		except Error as e:
			print(e)
		print 'Connection Succeed With {}'.format(db_name)
		id=str(id)
		query="DELETE FROM "+table+" WHERE (id = '"+id+"')"	
		conn.execute(query)
		conn.commit()
		conn.close()

	@staticmethod
	def resolvNameToID(table, name):
		API.importDBVars()
		
		os.chdir(db_dir)
		try:
			conn = sqlite3.connect(db_name)
		except Error as e:
			print(e)
		print 'Connection Succeed With {}'.format(db_name)
		query = "SELECT id FROM "+table+" WHERE name = '"+name+"'"
		cur = conn.cursor()
		cur.execute(query)
		conn.commit()
		id = cur.fetchone()
		for i in id:
			id = i

		return id
		conn.close()

	@staticmethod
	def listFieldVals(table, field):
		API.importDBVars()

		os.chdir(db_dir)
		try:
			conn = sqlite3.connect(db_name)
		except Error as e:
			print(e)
		print 'Connection Succeed With {}'.format(db_name)
		query = "SELECT "+field+" FROM "+table+""
		cur = conn.cursor()
		cur.execute(query)
		conn.commit()
		id = cur.fetchall()
		res=[]
		for i in id:
                        res.append(i[0])
		return res
		conn.close()
	
class Table:

	__metaclass__ = ABCMeta
	table=""
	field_tuple=()

	def add(self, value_tuple):

		errcode="" 
		if not(value_tuple) or not (value_tuple[0]) or(type(value_tuple) is not tuple) or (len(self.field_tuple) != len(value_tuple)):
			errcode="255"
			return errcode
		API.addEntry(self.table, self.field_tuple,value_tuple)
		errcode="0"
		return errcode

	def modify(self, id, field, value):
		errcode=""
		id=int(id) 
		if not (id) or(type(id) is not int) or (id < 0) or not (field) or(type(field) is not str) or not (value):
			errcode="255"
			return errcode
		API.modEntry(self.table ,id, field, value)
		errcode="0"
		return errcode

	def delete(self, id):
		errcode=""
		id=int(id) 
		if not(id) or (id < 0) or(type(id) is not int):
			errcode="255"
			return errcode
		API.delEntry(self.table, id)
		errcode="0"
		return errcode

	@abstractmethod    
	def retTableName(self):
		pass
