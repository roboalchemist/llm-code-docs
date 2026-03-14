# Source: https://www.hammerdb.com/docs4.0/ch04s04.html

Title: 4. Creating the Schema

URL Source: https://www.hammerdb.com/docs4.0/ch04s04.html

Markdown Content:
When you have completed your Build Options click OK to store the values you have entered. To begin the schema creation select Build from the tree-view.

**Figure 4.9.Build**

![Image 1: Build](https://www.hammerdb.com/docs4.0/resources/ch4-10.PNG)

On clicking this button a dialog box is shown

**Figure 4.10.Create Schema**

![Image 2: Create Schema](https://www.hammerdb.com/docs4.0/resources/ch4-11.PNG)

When you click Yes HammerDB will login to your chosen database a monitor virtual user and depending on the database create the user with the password you have chosen. It will then log out and log in again as your chosen user, create the tables and then load the item table data before waiting and monitoring the other virtual users. The worker virtual users will wait for the monitor virtual user to complete its initial work. Subsequently the worker virtual users will create and insert the data for their assigned warehouses. There are no intermediate data files or manual builds required, HammerDB will both create and load your requested data dynamically. Data is inserted in a batch format for optimal network performance.

**Figure 4.11.Schema Build Start**

![Image 3: Schema Build Start](https://www.hammerdb.com/docs4.0/resources/ch4-12.PNG)

When the worker virtual users are complete the monitor virtual users will depending on the database create the indexes, stored procedures and gather the statistics. When the schema build is complete Virtual User 1 will display the message SCHEMA COMPLETE and all virtual users will show an end timestamp and that they completed their action successfully. If this is not the case then then build did not complete successfully, the schema is not valid for testing and should therefore be deleted and reinstalled.

**Figure 4.12.Schema complete**

![Image 4: Schema complete](https://www.hammerdb.com/docs4.0/resources/ch4-13.PNG)

### [](https://www.hammerdb.com/docs4.0/ch04s04.html)4.1.Deleting or Verifying the Oracle Schema

If you have made a mistake simply close the application and run the following SQL to undo the user you have created.

SQL>drop user tpcc cascade;
Note that if Hash Clusters were used it will first be necessary to re-enable the table locks as follows before deleting the schema.

ALTER TABLE WAREHOUSE DISABLE TABLE LOCK;
ALTER TABLE DISTRICT DISABLE TABLE LOCK;
ALTER TABLE CUSTOMER DISABLE TABLE LOCK;
ALTER TABLE ITEM DISABLE TABLE LOCK;
ALTER TABLE STOCK DISABLE TABLE LOCK;
ALTER TABLE ORDERS DISABLE TABLE LOCK;
ALTER TABLE NEW_ORDER DISABLE TABLE LOCK;
ALTER TABLE ORDER_LINE DISABLE TABLE LOCK;
ALTER TABLE HISTORY DISABLE TABLE LOCK;
When you have created your schema you can verify the contents with SQL*PLUS or your favourite admin tool as the newly created user.

SQL> select tname, tabtype from tab;

TNAME                          TABTYPE
------------------------------ -------
HISTORY                          TABLE
CUSTOMER                         TABLE
DISTRICT                         TABLE
ITEM                             TABLE
WAREHOUSE                        TABLE
STOCK                            TABLE
NEW_ORDER                        TABLE
ORDERS                           TABLE
ORDER_LINE                       TABLE

9 rows selected.

SQL> select * from warehouse;

      W_ID      W_YTD      W_TAX W_NAME     W_STREET_1
---------- ---------- ---------- ---------- --------------------
W_STREET_2           W_CITY               W_ W_ZIP
-------------------- -------------------- -- ---------
         1  773095764        .11 4R0mUe     rM8f7zFYdx
JyiNY5zg1gQNBDO      v2973cRoiFSJ0z       OF 374311111

SQL> select index_name, index_type from ind;

INDEX_NAME                     INDEX_TYPE
------------------------------ ---------------------------
IORDL                          IOT - TOP
ORDERS_I1                      NORMAL
ORDERS_I2                      NORMAL
INORD                          IOT - TOP
STOCK_I1                       NORMAL
WAREHOUSE_I1                   NORMAL
ITEM_I1                        NORMAL
DISTRICT_I1                    NORMAL
CUSTOMER_I1                    NORMAL
CUSTOMER_I2                    NORMAL

10 rows selected.

SQL>

SQL> select object_name from user_procedures;

OBJECT_NAME
------------------------------
NEWORD
DELIVERY
PAYMENT
OSTAT
SLEV

SQL> select sum(bytes)/1024/1024 as MB from user_segments;
        MB
----------
   838.125

### [](https://www.hammerdb.com/docs4.0/ch04s04.html)4.2.Deleting or Verifying the SQL Server Schema and In-memory Schema

If you have made a mistake simply close the application and in SQL Server Management Studio right-click the database and choose Delete. Select the Close existing connections checkbox and click OK. When you have created your schema you can verify the contents with the SQL Server Management Studio or SQL Connection, for example:

C:\Users>sqlcmd -S (local)\SQLDEVELOP -E -Q "use tpcc; select name from sys.tables"
Changed database context to 'tpcc'.
name
---------------------------------------------------------------------------
CUSTOMER
DISTRICT
HISTORY
ITEM
NEW_ORDER
ORDERS
ORDER_LINE
STOCK
WAREHOUSE
(9 rows affected)

C:\Users>sqlcmd -S (local)\SQLDEVELOP -E -Q "use tpcc; select * from wareh
ouse where w_id = 1"
Changed database context to 'tpcc'.
w_id        w_ytd                 w_tax        w_name     w_street_1           w
_street_2           w_city               w_state w_zip     padding
          1          3000000.0000        .1000 s21C90Ft   pd1mYv9GlqyIww      u
6sOhAB9HF7iOZpM     llz9x35NhpVcrJc47Wy  VL      182111111 xxxxxxxxxxxxxxxxxxxxx(....)
(1 rows affected)

When an In-memory schema has been created under SSMS right click the created database and select reports followed memory usage by memory optimized objects, this produces a report such as follows for a 10 warehouse configuration. As with an on-disk schema a rough estimate of 100MB per warehouse can be used for the space required. In particular note that SQL Server Express has a particularly small memory allocation of 252MB and can be used for tests on 1 warehouse only for a short period of time before this limit will be reached. The error reported in the log will be as follows:

Could not perform the operation because the database has reached its quota for in-memory tables.

**Figure 4.13.SQL Server in-Memory**

![Image 5: SQL Server in-Memory](https://www.hammerdb.com/docs4.0/resources/ch4-22.png)

Additionally after schema creation and during testing monitor bucket usage as follows:

use imoltp 
SELECT  
    QUOTENAME(SCHEMA_NAME(t.schema_id)) + N'.' + QUOTENAME(OBJECT_NAME(h.object_id)) as [table],   
    i.name                   as [index],   
    h.total_bucket_count,  
    h.empty_bucket_count,  
      
    FLOOR((  
      CAST(h.empty_bucket_count as float) /  
        h.total_bucket_count) * 100)  
                             as [empty_bucket_percent],  
    h.avg_chain_length,   
    h.max_chain_length  
  FROM  
         sys.dm_db_xtp_hash_index_stats  as h   
    JOIN sys.indexes                     as i  
            ON h.object_id = i.object_id  
           AND h.index_id  = i.index_id  
    JOIN sys.memory_optimized_tables_internal_attributes ia ON h.xtp_object_id=ia.xtp_object_id
    JOIN sys.tables t on h.object_id=t.object_id
  WHERE ia.type=1
  ORDER BY [table], [index];

This script produces a report as follows where the empty_bucket_percent should indicate a good level of free space and the max_chain_length is not too long.

**Figure 4.14.In-memory report**

![Image 6: In-memory report](https://www.hammerdb.com/docs4.0/resources/ch4-23.png)

### [](https://www.hammerdb.com/docs4.0/ch04s04.html)4.3.Deleting or Verifying the Db2 Schema

If you have made a mistake simply close the application and run the following SQL to undo the user you have created.

db2inst1 ~]$ db2 drop database tpcc
DB20000I  The DROP DATABASE command completed successfully.

To browse the Db2 schema do the following.

[db2inst1 ~]$ db2 connect to tpcc

   Database Connection Information

 Database server        = DB2/LINUXX8664 10.5.5
 SQL authorization ID   = DB2INST1
 Local database alias   = TPCC

[db2inst1 ~]$ db2
(c) Copyright IBM Corporation 1993,2007
Command Line Processor for DB2 Client 10.5.5

db2 =>  select * from warehouse fetch first 10 rows only

W_NAME     W_STREET_1           W_STREET_2           W_CITY               W_STATE W_ZIP     W_TAX                    W_YTD          W_ID       
---------- -------------------- -------------------- -------------------- ------- --------- ------------------------ -------------- -----------
5SuPObQR4  FCPEw6PzfOCdp5DHDq7e d9lOkysRKPyPtqB      G0Nt9PuUyR8qZxCOXms0 9Y      546011111            +1.70000E-001     3000000.00           1
QP75kKTagb sOaOeFYpGjc5lvA8BW   f6HbFCH2S6mh         cCPt1emu6hFjobgOqeP  TT      533211111            +1.50000E-001     3000000.00           2
Hu3QQhR    KwwcMmuWbpoiQRM      9MaTxygtYX4Dz        NFSkHHdHyEChXclP4iqA cE      919511111            +1.60000E-001     3000000.00           3
aqN3Df     PAJg6lOtk7r          XxWjB1HMQhOlJ        jknxafMFlirG8pUpntm  mG      217211111            +1.80000E-001     3000000.00           4
zZBreP     gCMDTWuJUHh          AG0vp9mbvGh          t7dDHFKFhd72WKP      xa      342611111            +1.30000E-001     3000000.00           5
bleOmY     pzPzlBidlwneHdMkq    dmZvxDxmrL4WdQNg     jC2DTpxGc1g1LQlk5P8n bt      980911111            +1.50000E-001     3000000.00           6
BFmMdkLUUK joucFFovxwZWcdsBPZ   IBjiEBzqn7dtuU       8FNwUX40bJ56Iwh      gC      751911111            +1.00000E-001     3000000.00           7
xWY9EugeeD t5dK0z1bQWwEuMGMnb59 sYEzAdgb9FeuX        K7PkSQHSno0NSHEet4xr 1Q      270611111            +1.70000E-001     3000000.00           8
5XtsHe1kw  uNJGs1Y1lQnYLAX      qvOfjMIqml5kHzm      C3iX14JTbnCyoRVR     ai      203011111            +2.00000E-001     3000000.00           9
t89Pm591   CKjgdxmZ5AgvZ        LqyRXzAoFUO          2O0j38eGPNMXFb       XU      372011111            +1.40000E-001     3000000.00          10

  10 record(s) selected.

db2 => 

### [](https://www.hammerdb.com/docs4.0/ch04s04.html)4.4.Deleting or Verifying the MySQL Schema

If you have made a mistake simply close the application and run the following SQL to undo the database you have created.

SQL>drop database tpcc;
you can verify the contents with SQL or your favourite admin tool as the newly created user.

mysql> use tpcc;
Database changed
mysql> show tables;
+----------------+
| Tables_in_tpcc |
+----------------+
| customer       |
| district       |
| history        |
| item           |
| new_order      |
| order_line     |
| orders         |
| stock          |
| warehouse      |
+----------------+
9 rows in set (0.00 sec)

mysql> select * from warehouse limit 1 \G
*************************** 1. row ***************************
      w_id: 1
     w_ytd: 3000000.00
     w_tax: 0.1300
    w_name: mBr6dkgK
w_street_1: FH0SO5CUEREo
w_street_2: cBcStSxKcIIs4IAUUsJy
    w_city: FKaak9ZBgtJr3Tr6gESW
   w_state: Tt
     w_zip: 432611111
1 row in set (0.00 sec)

mysql> show indexes from warehouse \G
*************************** 1. row ***************************
        Table: warehouse
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: w_id
    Collation: A
  Cardinality: 10
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
1 row in set (0.00 sec)

mysql> select routine_name from information_schema.routines where routine_schema
 = 'TPCC';
+--------------+
| routine_name |
+--------------+
| DELIVERY     |
| NEWORD       |
| OSTAT        |
| PAYMENT      |
| SLEV         |
+--------------+
5 rows in set (0.03 sec)

### [](https://www.hammerdb.com/docs4.0/ch04s04.html)4.5.Deleting or Verifying the PostgreSQL Schema

If you have made a mistake simply close the application and run the following SQL to undo the user you have created.

postgres=# drop database tpcc;
postgres=# drop role tpcc;

You can browse the created schema, for example:

-bash-4.1$ ./bin/psql -d tpcc
Password: 
psql.bin (9.3.4.10)
Type "help" for help.

tpcc=# select relname, n_tup_ins - n_tup_del as rowcount from pg_stat_user_tables;
  relname   | rowcount 
------------+----------
 orders     |   300000
 district   |      100
 stock      |  1000000
 warehouse  |       10
 history    |   300000
 new_order  |    90000
 item       |   100000
 order_line |  3001170
 customer   |   300000
(9 rows)
