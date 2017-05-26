#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
import sys


sys.path.insert(0, '../Helper')

from dbHelper import *

class Warehouse:
	#def __init__(self):
	#	dbHelper.connectDb()
	#	
	def addWarehouse(self, warehouseName='', desc=''):
		
 
		msg=""
		if(warehouseName==''):
			msg="error msg Warehouse Name not found !!!"
			return msg
		
		dbHelper.addWarehouseInDb(warehouseName,desc)
		print "success Adding"
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

	def modWarehouse():
	  print "" 
	def delWarehouse():
		print " " 
	def mvToWarehouse():
		print " " 
	  
	  
	def modAmount():
		print " "
		
mainWare = Warehouse()
mainWare.addWarehouse("DumpWareHouse","DumpDescription")