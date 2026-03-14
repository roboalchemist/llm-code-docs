# Source: https://www.hammerdb.com/docs4.0/ch13s02.html

Title: 2. Generate the Dataset with the CLI

URL Source: https://www.hammerdb.com/docs4.0/ch13s02.html

Markdown Content:
Data Generation can also be run from the command line. As shown the dbset command is used to specify the database and benchmark to generate data for.

./hammerdbcli 
HammerDB CLI v4.0
Copyright (C) 2003-2020 Steve Shaw
Type "help" for a list of commands
The xml is well-formed, applying configuration
hammerdb>print datagen
Data Generation set to build a TPC-C schema for Oracle with 1 warehouses with 1 virtual users in /tmp

hammerdb>dbset bm TPROC-H
Benchmark set to TPROC-H for Oracle

hammerdb>print datagen
Data Generation set to build a TPC-H schema for Oracle with 1 scale factor with 1 virtual users in /tmp

hammerdb>dbset bm TPROC-C
Benchmark set to TPROC-C for Oracle

hammerdb>print datagen
Data Generation set to build a TPC-C schema for Oracle with 1 warehouses with 1 virtual users in /tmp
and the Data Generation options set with the command dgset:

hammerdb>dgset warehouse 10

hammerdb>dgset vu 8
Set virtual users to 8 for data generation

hammerdb>dgset directory "/tmp/TPCCDATA"

hammerdb>print datagen
Data Generation set to build a TPC-C schema for Oracle with 10 warehouses with 8 virtual users in /tmp/TPCCDATA
The data is then created using the command datagenrun.

hammerdb>datagenrun
Ready to generate the data for a 10 Warehouse Oracle TPC-C schema
in directory /tmp/TPCCDATA ?
Enter yes or no: replied yes
Vuser 1 created - WAIT IDLE
Vuser 2 created - WAIT IDLE
Vuser 3 created - WAIT IDLE
Vuser 4 created - WAIT IDLE
Vuser 5 created - WAIT IDLE
Vuser 6 created - WAIT IDLE
Vuser 7 created - WAIT IDLE
Vuser 8 created - WAIT IDLE
Vuser 9 created - WAIT IDLE
RUNNING - TPC-C generation
Vuser 1:RUNNING
Vuser 1:Monitor Thread
Vuser 1:Opened File /tmp/TPCCDATA/item_1.tbl
Vuser 1:Generating Item
Vuser 2:RUNNING
Vuser 2:Worker Thread
Vuser 2:Waiting for Monitor Thread...
Vuser 2:Generating 2 Warehouses start:1 end:2
Vuser 2:Start:Mon Apr 09 16:21:36 BST 2018
Vuser 2:Opened File /tmp/TPCCDATA/warehouse_1.tbl
Vuser 2:Opened File /tmp/TPCCDATA/stock_1.tbl
Vuser 2:Opened File /tmp/TPCCDATA/district_1.tbl
Vuser 2:Opened File /tmp/TPCCDATA/customer_1.tbl
Vuser 2:Opened File /tmp/TPCCDATA/history_1.tbl
Vuser 2:Opened File /tmp/TPCCDATA/orders_1.tbl
Vuser 2:Opened File /tmp/TPCCDATA/new_order_1.tbl
Vuser 2:Opened File /tmp/TPCCDATA/order_line_1.tbl
Vuser 2:Generating Warehouse
Vuser 2:Generating Stock Wid=1

...
