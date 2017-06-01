import sys
from Helper.dbHelper import *

class Warehouse(Table):

	table="warehouses"
	field_tuple=('name', 'description')

	def retTableName(self):
		return 'warehouses'

class Category(Table):

	table="categories"
	field_tuple=('name', 'description')

	def retTableName(self):
		return 'categories'

class Attribute(Table):

	table="attributes"
	field_tuple=('name', 'description')

	def retTableName(self):
		return 'attributes'

class Item(Table):
	table="items"
	field_tuple=('name', 'number', 'label', 'warehouse_id', 'category_id', 'from_customer_id', 'description')

	def retTableName(self):
		return "items"

#cat = Category()
#cat.add(('Materials', 'Meta Description'))
#id = dbHelper.resolvNameToID('categories', 'Clothes')
#cat.modify(id, 'description', 'Wearable skins, furs and plants')

