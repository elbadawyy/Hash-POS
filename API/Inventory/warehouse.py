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
			msg="Error: msg Warehouse Name not found !!!"
			return msg
		
		dbHelper.addWarehouseInDb(warehouseName,desc)
		msg="Success Adding"
		return msg
		
		
		

		
		

	def modWarehouse(self,WarehouseId="0", newWarehouseName="", newDesc=""): 
		msg=""
		if(WarehouseId=="0") or (newDesc==""):
			msg="Error: WarehouseId or newDesc not found !!!"
			return msg
		
		dbHelper.modWarehouseInDb(WarehouseId,newWarehouseName,newDesc)
		msg="Success Modifing"
		return msg
	  
	  
	  
	def delWarehouse(self,WarehouseId="0"):
		msg=""
		if(WarehouseId==''):
			msg="Error: msg Warehouse Id not found !!!"
			return msg
		
		dbHelper.delWarehouseFrmDb(WarehouseId)
		msg="Success Deleting"
		return msg
	
	

		
mainWare = Warehouse()
addWarehouse("mainWarehous", "desc"):
modWarehouse("4", "newname", "newDesc")
mainWare.delWarehouse("4")