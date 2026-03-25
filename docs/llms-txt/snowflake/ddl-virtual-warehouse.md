# Source: https://docs.snowflake.com/en/sql-reference/ddl-virtual-warehouse.md

# Warehouse & resource monitor DDL

A virtual warehouse is a cluster of compute resources. A warehouse is needed to execute certain types of SQL statements because it provides resources such as CPU, memory, and local storage.

Resource monitors can be used to control credit usage for warehouses. A resource monitor specifies a monthly credit quota, one or more credit usage thresholds, and actions to perform when the thresholds are
reached. Each resource monitor can be associated with one or more warehouses.

## Virtual warehouses

* [CREATE WAREHOUSE](sql/create-warehouse.md)
* [ALTER WAREHOUSE](sql/alter-warehouse.md)
* [DESCRIBE WAREHOUSE](sql/desc-warehouse.md)
* [DROP WAREHOUSE](sql/drop-warehouse.md)
* [USE WAREHOUSE](sql/use-warehouse.md)
* [SHOW WAREHOUSES](sql/show-warehouses.md)

## Resource monitors

* [CREATE RESOURCE MONITOR](sql/create-resource-monitor.md)
* [ALTER RESOURCE MONITOR](sql/alter-resource-monitor.md)
* [DROP RESOURCE MONITOR](sql/drop-resource-monitor.md)
* [SHOW RESOURCE MONITORS](sql/show-resource-monitors.md)
