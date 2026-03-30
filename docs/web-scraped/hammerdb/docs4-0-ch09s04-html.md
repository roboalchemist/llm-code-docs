# Source: https://www.hammerdb.com/docs4.0/ch09s04.html

Title: 4. Building the Schema

URL Source: https://www.hammerdb.com/docs4.0/ch09s04.html

Markdown Content:
Run the buildschema command and the build will commence without prompting using your configuration and if successful report the status at the end of the build. Note that exactly as the GUI the build is multithreaded with Virtual Users running simultaneously.

hhammerdb>buildschema
Script cleared
Building 10 Warehouses with 5 Virtual Users, 4 active + 1 Monitor VU(dict value mssqls_num_vu is set to 4)
Ready to create a 10 Warehouse MS SQL Server TPROC-C schema
in host (LOCAL)\SQLDEVELOP in database TPCC?
Enter yes or no: replied yes
Vuser 1 created - WAIT IDLE
Vuser 2 created - WAIT IDLE
Vuser 3 created - WAIT IDLE
Vuser 4 created - WAIT IDLE
Vuser 5 created - WAIT IDLE
Vuser 1:RUNNING
Vuser 1:Monitor Thread
Vuser 1:CREATING TPCC SCHEMA
Vuser 1:CHECKING IF DATABASE tpcc EXISTS
Vuser 1:CREATING DATABASE tpcc
Vuser 1:CREATING TPCC TABLES
Vuser 1:Loading Item
Vuser 2:RUNNING
Vuser 2:Worker Thread
Vuser 2:Waiting for Monitor Thread...
Vuser 2:Loading 2 Warehouses start:1 end:2
Vuser 2:Start:Thu Oct 22 17:56:27 BST 2020
Vuser 2:Loading Warehouse
Vuser 2:Loading Stock Wid=1
Vuser 3:RUNNING
Vuser 3:Worker Thread
Vuser 3:Waiting for Monitor Thread...
Vuser 3:Loading 2 Warehouses start:3 end:4
Vuser 3:Start:Thu Oct 22 17:56:27 BST 2020
Vuser 3:Loading Warehouse
Vuser 3:Loading Stock Wid=3
Vuser 4:RUNNING
Vuser 4:Worker Thread
Vuser 4:Waiting for Monitor Thread...
Vuser 4:Loading 2 Warehouses start:5 end:6
Vuser 4:Start:Thu Oct 22 17:56:28 BST 2020
Vuser 4:Loading Warehouse
Vuser 4:Loading Stock Wid=5
Vuser 5:RUNNING
Vuser 5:Worker Thread
Vuser 5:Waiting for Monitor Thread...
Vuser 5:Loading 2 Warehouses start:7 end:10
Vuser 5:Start:Thu Oct 22 17:56:28 BST 2020
Vuser 5:Loading Warehouse
Vuser 5:Loading Stock Wid=7

.....

Vuser 5:Loading Orders for D=10 W=10
Vuser 5:...1000
Vuser 5:...2000
Vuser 5:...3000
Vuser 5:Orders Done
Vuser 5:End:Thu Oct 22 18:02:45 BST 2020
Vuser 5:FINISHED SUCCESS
Vuser 1:Workers: 0 Active 4 Done
Vuser 1:CREATING TPCC INDEXES
Vuser 1:CREATING TPCC STORED PROCEDURES
Vuser 1:UPDATING SCHEMA STATISTICS
Vuser 1:TPCC SCHEMA COMPLETE
Vuser 1:FINISHED SUCCESS
ALL VIRTUAL USERS COMPLETE

hammerdb>

The vustatus command can confirm the status of each Virtual User.

hammerdb>vustatus
1 = FINISH SUCCESS
2 = FINISH SUCCESS
3 = FINISH SUCCESS
4 = FINISH SUCCESS
5 = FINISH SUCCESS
When the build is complete destroy the Virtual Users and confirm the status.

hammerdb>vudestroy
Destroying Virtual Users
Virtual Users Destroyed

hammerdb>vustatus
No Virtual Users found
