----
-- phpLiteAdmin database dump (http://www.phpliteadmin.org/)
-- phpLiteAdmin version: 1.9.7.1
-- Exported: 12:46am on May 21, 2017 (EEST)
-- database file: ./Hash_POS
----
BEGIN TRANSACTION;

----
-- Drop table for items
----
DROP TABLE IF EXISTS "items";

----
-- Table structure for items
----
CREATE TABLE 'items' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT NOT NULL, 'number' INTEGER NOT NULL, 'label' TEXT, 'warehouse_id' INTEGER, 'category_id' INTEGER, 'from_customer_id' INTEGER, 'description' TEXT, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for items, a total of 0 rows
----

----
-- Drop table for warehouses
----
DROP TABLE IF EXISTS "warehouses";

----
-- Table structure for warehouses
----
CREATE TABLE 'warehouses' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT NOT NULL, 'description' TEXT, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for warehouses, a total of 0 rows
----

----
-- Drop table for categories
----
DROP TABLE IF EXISTS "categories";

----
-- Table structure for categories
----
CREATE TABLE 'categories' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT NOT NULL, 'description' TEXT, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for categories, a total of 0 rows
----

----
-- Drop table for attributes
----
DROP TABLE IF EXISTS "attributes";

----
-- Table structure for attributes
----
CREATE TABLE 'attributes' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'name' TEXT NOT NULL, 'description' TEXT, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for attributes, a total of 0 rows
----

----
-- Drop table for item_category
----
DROP TABLE IF EXISTS "item_category";

----
-- Table structure for item_category
----
CREATE TABLE 'item_category' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'item_id' INTEGER NOT NULL, 'category_id' INTEGER NOT NULL, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for item_category, a total of 0 rows
----

----
-- Drop table for item_warehouse
----
DROP TABLE IF EXISTS "item_warehouse";

----
-- Table structure for item_warehouse
----
CREATE TABLE 'item_warehouse' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'item_id' INTEGER NOT NULL, 'warehouse_id' INTEGER NOT NULL, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for item_warehouse, a total of 0 rows
----

----
-- Drop table for item_attr
----
DROP TABLE IF EXISTS "item_attr";

----
-- Table structure for item_attr
----
CREATE TABLE 'item_attr' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'item_id' INTEGER NOT NULL, 'attribute_id' INTEGER NOT NULL, 'value' TEXT, 'created_at'  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP  );

----
-- Data dump for item_attr, a total of 0 rows
----

----
-- Drop table for users
----
DROP TABLE IF EXISTS "users";

----
-- Table structure for users
----
CREATE TABLE 'users' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'first_name' TEXT, 'last_name' TEXT, 'username' TEXT NOT NULL, 'password' TEXT NOT NULL, 'privilege_id' INTEGER NOT NULL, 'email' TEXT, 'description' TEXT, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for users, a total of 0 rows
----

----
-- Drop table for privileges
----
DROP TABLE IF EXISTS "privileges";

----
-- Table structure for privileges
----
CREATE TABLE 'privileges' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'role_name' REAL NOT NULL, 'description' TEXT, 'created_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);

----
-- Data dump for privileges, a total of 0 rows
----
COMMIT;
