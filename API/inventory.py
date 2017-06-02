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
	field_tuple=('name', 'quantity', 'barcode', 'warehouse_id', 'category_id', 'from_customer_id', 'description')

	def retTableName(self):
		return "items"

class Item_Attr(Table):
	table="item_attr"
	field_tuple=('item_id', 'attribute_id', 'value')

	def retTableName(self):
		return "item_attr"

class Item_Cat(Table):
	table="item_category"
	field_tuple=('item_id', 'category_id')

	def retTableName(self):
		return "item_attr"

#cat = Category()
#cat.add(('Materials', 'Meta Description'))
#attr = Attribute()
#attr.add(('Size', 'Products sizes will be defined by this attribute'))
#attr.add(('Weight', 'Products weights will be defined by this attribute'))
#id = dbHelper.resolvNameToID('items', 'mars')
#cat.modify(id, 'description', 'Wearable things')
#dbHelper.listFieldVals('attributes', 'name')
#ic = Item_Cat()
#ic.add(('5', '2'))
#ia = Item_Attr()
#ia.add(('5', '1', 'Black'))
