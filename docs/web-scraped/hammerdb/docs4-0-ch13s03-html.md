# Source: https://www.hammerdb.com/docs4.0/ch13s03.html

Title: 3. Generate the template database

URL Source: https://www.hammerdb.com/docs4.0/ch13s03.html

Markdown Content:
Generating a template database is exceptionally straightforward. From the HammerDB documentation follow the steps for Build a Schema and create the smallest size database such as Scale Factor 1 for TPROC-H. This database can then be used as a template to capture the DDL. Note that if you stop the database creation after the tables are created but before all of the data is loaded objects such as indexes will not have been created and will not therefore be included in generated DDL, this may or may not be an issue for the type of schema you are intending to build, for example for a column store such as Amazon Redshift, indexes are not a requirement.

### [](https://www.hammerdb.com/docs4.0/ch13s03.html)3.1.Capture and run the table creation DDL

All of the mainstream databases supported with HammerDB enable DDL capture. This can be done as follows for each database. Note that at this stage you have the option to modify the DDL for your needs such as for partitioning or column orientation.

#### [](https://www.hammerdb.com/docs4.0/ch13s03.html)3.1.1.Oracle

As the user owning the template database at a sqlplus prompt run a GET_DDL SQL statement as follows, noting that you need to set the long and pagesize values correctly to view all of the output.

SQL>select DBMS_METADATA.GET_DDL('TABLE','ORDERS') from dual;
This produces a Create Table statement such as follows:

CREATE TABLE "TPCH"."ORDERS"                                                 
("O_ORDERDATE" DATE,                                         
"O_ORDERKEY" NUMBER NOT NULL ENABLE,                            
"O_CUSTKEY" NUMBER NOT NULL ENABLE,                            
"O_ORDERPRIORITY" CHAR(15),                                   
"O_SHIPPRIORITY" NUMBER,                                      
"O_CLERK" CHAR(15),                                           
"O_ORDERSTATUS" CHAR(1),                                       
"O_TOTALPRICE" NUMBER,              
"O_COMMENT" VARCHAR2(79),
 CONSTRAINT "ORDERS_PK" PRIMARY KEY ("O_ORDERKEY")
);

Joining these files together can then be run against the database to create the schema of empty tables:

sqlplus tpch/tpch
SQL*Plus: Release 12.1.0.2.0 Production
Copyright (c) 1982, 2014, Oracle.  All rights reserved.
Connected to:
Oracle Database 12c Enterprise Edition Release 12.1.0.2.0
SQL> @tpch_tables.sql
Table created.
Table created.
Table created.
Table created.
Table created.
Table created.
Table created.
Table created.
SQL>

#### [](https://www.hammerdb.com/docs4.0/ch13s03.html)3.1.2.SQL Server

Within SQL Server Management Studio right click your chosen table, select “Script Table as” followed by “CREATE To” and choose your destination for the DDL. This produces DDL to create your table such as follows. Create a single file containing all of your DDL statements and click on Execute (F5) under SQL Server Management Studio.

**Figure 13.12.SQL Server Create Table**

![Image 1: SQL Server Create Table](https://www.hammerdb.com/docs4.0/resources/ch10-12.png)

#### [](https://www.hammerdb.com/docs4.0/ch13s03.html)3.1.3.Db2

For Db2 use the db2look command, this can generate the DDL for all objects within a schema with one command.

db2look -d TPCH -a -e -x -o tpchcreate.sql
-- Generate statistics for all creators 
-- Creating DDL for table(s)
-- Output is sent to file: tpchcreate.sql
-- Binding package automatically ... 
-- Bind is successful
-- Binding package automatically ... 
-- Bind is successful
------------------------------------------------
-- DDL Statements for Table "DB2INST1"."ORDERS"
------------------------------------------------

The output file will contain output as follows:

CREATE TABLE "DB2INST1"."ORDERS"  (
  "O_ORDERKEY" INTEGER NOT NULL , 
  "O_CUSTKEY" INTEGER NOT NULL , 
  "O_ORDERSTATUS" CHAR(1 OCTETS) NOT NULL , 
  "O_TOTALPRICE" DOUBLE NOT NULL , 
  "O_ORDERDATE" DATE NOT NULL , 
  "O_ORDERPRIORITY" CHAR(15 OCTETS) NOT NULL , 
  "O_CLERK" CHAR(15 OCTETS) NOT NULL , 
  "O_SHIPPRIORITY" INTEGER , 
  "O_COMMENT" VARCHAR(79 OCTETS) NOT NULL )   
 IN "USERSPACE1"  
 ORGANIZE BY ROW; 

Run the file as follows:

db2 -tvf tpchcreate.sql
CONNECT TO TPCH

   Database Connection Information

 Database server        = DB2/LINUXX8664 11.1.0
 SQL authorization ID   = DB2INST1
 Local database alias   = TPCH2

CREATE SCHEMA "DB2INST1"
DB20000I  The SQL command completed successfully.

CREATE TABLE "DB2INST1"."ORDERS"  ( "O_ORDERKEY" INTEGER NOT NULL , "O_CUSTKEY" INTEGER NOT NULL , "O_ORDERSTATUS" CHAR(1 OCTETS) NOT NULL , "O_TOTALPRICE" DOUBLE NOT NULL , "O_ORDERDATE" DATE NOT NULL , "O_ORDERPRIORITY" CHAR(15 OCTETS) NOT NULL , "O_CLERK" CHAR(15 OCTETS) NOT NULL , "O_SHIPPRIORITY" INTEGER , "O_COMMENT" VARCHAR(79 OCTETS) NOT NULL ) IN "USERSPACE1" ORGANIZE BY ROW
DB20000I  The SQL command completed successfully.

#### [](https://www.hammerdb.com/docs4.0/ch13s03.html)3.1.4.MySQL

For MySQL use the show create table command. Be aware that if foreign keys are defined at this stage they will significantly impact load performance.

mysql> use tpch;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+----------------+
| Tables_in_tpch |
+----------------+
| CUSTOMER       |
| LINEITEM       |
| NATION         |
| ORDERS         |
| PART           |
| PARTSUPP       |
| REGION         |
| SUPPLIER       |
+----------------+
8 rows in set (0.00 sec)

mysql> show create table SUPPLIER;

CREATE TABLE `SUPPLIER` (
  `S_SUPPKEY` int(11) NOT NULL,
  `S_NATIONKEY` int(11) DEFAULT NULL,
  `S_COMMENT` varchar(102) CHARACTER SET latin1 COLLATE latin1_bin DEFAULT NULL,
  `S_NAME` char(25) CHARACTER SET latin1 COLLATE latin1_bin DEFAULT NULL,
  `S_ADDRESS` varchar(40) CHARACTER SET latin1 COLLATE latin1_bin DEFAULT NULL,
  `S_PHONE` char(15) CHARACTER SET latin1 COLLATE latin1_bin DEFAULT NULL,
  `S_ACCTBAL` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`S_SUPPKEY`),
  KEY `SUPPLIER_FK1` (`S_NATIONKEY`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

Create a file containing all of the table creation statements and run as follows:

sql> use tpch
Database changed
mysql> source /home/mysql/TPCHDATA/createtpch.sql
Query OK, 0 rows affected (0.08 sec)
Query OK, 0 rows affected (0.07 sec)
Query OK, 0 rows affected (0.05 sec)
Query OK, 0 rows affected (0.05 sec)
Query OK, 0 rows affected (0.05 sec)
Query OK, 0 rows affected (0.06 sec)
Query OK, 0 rows affected (0.05 sec)
Query OK, 0 rows affected (0.05 sec)
mysql>

#### [](https://www.hammerdb.com/docs4.0/ch13s03.html)3.1.5.PostgreSQL/Amazon Redshift

To create the DLL for PostgreSQL or Amazon Redshift (note you can create a template local PostgreSQL database and the DDL is 100% compatible to create a database in Redshift) use the pg_dump command as follows:

pg_dump -U postgres -h localhost tpch -t table_name --schema-only -f table.sql
On Linux systems you can use the bash shell to generate the DDL for all tables with one command, for example:

for sys in customer lineitem nation orders part partsupp region supplier; do pg_dump -U postgres -h localhost tpch -t $sys --schema-only -f $sys.sql; done
This generates a series of files containing the required DDL as follows:

CREATE TABLE customer (
    c_custkey numeric NOT NULL,
    c_mktsegment character(10),
    c_nationkey numeric,
    c_name character varying(25),
    c_address character varying(40),
    c_phone character(15),
    c_acctbal numeric,
    c_comment character varying(118)
);

Run the files as follows under PostgreSQL or Redshift to create the desired tables. The following example create the schema on PostgreSQL

psql -d tpch -f pgtpchtables.sql
and the following on Redshift

bash-4.2$ psql -h tpch-instance.xxxxxxxxxxxx.eu-west-1.redshift.amazonaws.com -U postgres -d tpch -p 5439 -f pgtpchtables.sql
Password for user postgres: 
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
-bash-4.2$ psql -h tpch-instance.xxxxxxxxxxxx.eu-west-1.redshift.amazonaws.com -U postgres -d tpch -p 5439
Password for user postgres: 
psql (9.2.15, server 8.0.2)
WARNING: psql version 9.2, server version 8.0.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

tpch=# \d
          List of relations
 schema |   name   | type  |  owner   
--------+----------+-------+----------
 public | customer | table | postgres
 public | lineitem | table | postgres
 public | nation   | table | postgres
 public | orders   | table | postgres
 public | part     | table | postgres
 public | partsupp | table | postgres
 public | region   | table | postgres
 public | supplier | table | postgres
(8 rows)
