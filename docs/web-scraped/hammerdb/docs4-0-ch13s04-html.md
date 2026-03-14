# Source: https://www.hammerdb.com/docs4.0/ch13s04.html

Title: 4. Run the bulk data load

URL Source: https://www.hammerdb.com/docs4.0/ch13s04.html

Markdown Content:
With the schemas created you can proceed to bulk load the data you have created without the overhead of features such as logging associated with inserts. This section details example methods by which data can be bulk loaded. Note that some of these databases support multiple different methods to bulk load data and this section gives examples using either the most straightforward or widely available tools, therefore additional methods may exists to load your data.

### [](https://www.hammerdb.com/docs4.0/ch13s04.html)4.1.Oracle

SQL*Loader is the default method for loading Oracle with external data. SQL*Loader has the advantage of flexibility in being adaptable to loading data in many different formats. To use SQL*Loader firstly create a control file. The following example shows a control file for the ORDERS table from the TPCH schema. Firstly note that the control can accept wildcard characters and therefore multiple files can be loaded with one command. Also note how the DATE format has been specified.

more sqlldr-orders.ctl
load data
infile '/home/oracle/TPCCDATA/orders_*.tbl'
into table orders
fields terminated by "|"
(O_ID,O_W_ID,O_D_ID,O_C_ID,O_CARRIER_ID,O_OL_CNT,O_ALL_LOCAL,O_ENTRY_D DATE "YYY
YMMDDHH24MISS")

A further different date formatting example can be seen for the LINEITEM table in the TPCH schema.

more sqlldr-lineitem.ctl
load data
infile '/home/oracle/TPCHDATA/lineitem_*.tbl'
into table lineitem
fields terminated by "|"
(L_SHIPDATE DATE "yyyy-mon-dd",L_ORDERKEY,L_DISCOUNT ,L_EXTENDEDPRICE,L_SUPPKEY,L_QUANTITY,L_RETURNFLAG,L_PARTKEY,L_LINESTATUS,L_TAX,L_COMMITDATE DATE "yyyy-mon-dd", L_RECEIPTDATE DATE "yyyy-mon-dd",L_SHIPMODE, L_LINENUMBER, L_SHIPINSTRUCT, L_COMMENT)

Now run SQL*Loader specifying the control file and username and password.

sqlldr tpch/tpch control=/home/oracle/sqlldr-orders.ctl direct=true

### [](https://www.hammerdb.com/docs4.0/ch13s04.html)4.2.SQL Server

For SQL Server use a bulk insert state as follows. SQL Server does not recognize wildcard characters for bulk insert however is adaptable in recognizing both NULLS and various date formats by default.

BULK INSERT customer FROM 'C:\TEMP\TPCHDATA\customer_1.tbl' WITH (TABLOCK, DATAFILETYPE='char', CODEPAGE='raw', FIELDTERMINATOR = '|')
Run the bulk insert commands via SQL Server Management studio.

**Figure 13.13.SQL Server Bulk Insert**

![Image 1: SQL Server Bulk Insert](https://www.hammerdb.com/docs4.0/resources/ch10-13.png)

### [](https://www.hammerdb.com/docs4.0/ch13s04.html)4.3.Db2

For DB2 firstly connect to your database and then use the db2 load command. The delimiter is specified by 0x7c as the ASCII character for vertical bar as the delimiter used.

$ db2 connect to tpch

Database Connection Information

Database server        = DB2/LINUXX8664 11.1.0
SQL authorization ID   = DB2INST1
Local database alias   = TPCH

db2 load from /home/db2inst1/TPCHDATA/nation_1.tbl of DEL MODIFIED BY DELPRIORITYCHAR COLDEL0x7c insert INTO nation

This command is easy to script in Linux environments to load all available files:

$ for sys in `ls -1 customer_*.tbl`; do db2 load from /home/db2inst1/TPCHDATA/$sys of DEL MODIFIED BY DELPRIORITYCHAR COLDEL0x7c insert INTO customer; done

Where a date is specified the dateformat must be given as follows:

db2 load from /home/db2inst1/TPCHDATA/lineitem_1.tbl of DEL MODIFIED BY DELPRIORITYCHAR COLDEL0x7c DATEFORMAT=\"YYYY-MMM-DD\" insert INTO lineitem
As with Oracle and SQL Server Db2 automatically recognises NULL values in the data.

### [](https://www.hammerdb.com/docs4.0/ch13s04.html)4.4.MySQL

Bulk loading is done in MySQL using the load data infile command. This can be done as follows:

mysql> load data infile '/home/mysql/TPCHDATA/supplier_1.tbl' INTO table SUPPLIER fields terminated by '|';
Load data infile does not offer enable a method by which different date formats can be specified however this can be achieved by specifying an additional SET command as shown for the LINEITEM table:

load data infile '/home/mysql/TPCHDATA/lineitem_1.tbl' INTO table LINEITEM fields terminated by '|'
(@dt1, L_ORDERKEY, L_DISCOUNT, L_EXTENDEDPRICE, L_SUPPKEY, L_QUANTITY, L_RETURNFLAG, L_PARTKEY, L_LINESTATUS, L_TAX, @dt2, @dt3, L_SHIPMODE, L_LINENUMBER, L_SHIPINSTRUCT, L_COMMENT)
set L_SHIPDATE = STR_TO_DATE(@dt1, '%Y-%b-%d'),L_COMMITDATE = STR_TO_DATE(@dt2, '%Y-%b-%d'),L_RECEIPTDATE = STR_TO_DATE(@dt3, '%Y-%b-%d');

and a SET command as follows shown for the ORDERS table:

load data infile '/home/mysql/TPCHDATA/orders_1.tbl' INTO table ORDERS fields terminated by '|'
(@dt1, O_ORDERKEY, O_CUSTKEY, O_ORDERPRIORITY, O_SHIPPRIORITY, O_CLERK, O_ORDERSTATUS, O_TOTALPRICE, O_COMMENT)
set O_ORDERDATE = STR_TO_DATE(@dt1, '%Y-%b-%d');

Add these commands to a file:

load data infile '/home/mysql/TPCHDATA/customer_1.tbl' INTO table CUSTOMER fields terminated by '|';
load data infile '/home/mysql/TPCHDATA/customer_2.tbl' INTO table CUSTOMER fields terminated by '|';
load data infile '/home/mysql/TPCHDATA/customer_3.tbl' INTO table CUSTOMER fields terminated by '|';
load data infile '/home/mysql/TPCHDATA/customer_4.tbl' INTO table CUSTOMER fields terminated by '|';
load data infile '/home/mysql/TPCHDATA/customer_5.tbl' INTO table CUSTOMER fields terminated by '|';
load data infile '/home/mysql/TPCHDATA/customer_6.tbl' INTO table CUSTOMER fields terminated by '|';

and run as follows:

mysql> source /home/mysql/TPCHDATA/loadfiles.sql
Query OK, 150000 rows affected (0.74 sec)
Records: 150000  Deleted: 0  Skipped: 0  Warnings: 0

Query OK, 150000 rows affected (1.56 sec)
Records: 150000  Deleted: 0  Skipped: 0  Warnings: 0

For the MySQL TPROC-C schema NULLS are not automatically recognised and a SET command is required as follows for the ORDER_LINE and ORDERS table:

load data infile '/home/mysql/TPCCDATA/order_line_1.tbl' INTO table order_line fields terminated by '|'
(ol_w_id, ol_d_id, ol_o_id, ol_number, ol_i_id, @dt1, ol_amount, ol_supply_w_id, ol_quantity, ol_dist_info)
set ol_delivery_d = nullif(@dt1,'');

load data infile '/home/mysql/TPCCDATA/orders_1.tbl' INTO table orders fields terminated by '|'
(o_id, o_w_id, o_d_id, o_c_id, @id1, o_ol_cnt, o_all_local, o_entry_d)
set o_carrier_id = nullif(@id1,'');

### [](https://www.hammerdb.com/docs4.0/ch13s04.html)4.5.PostgreSQL/Amazon Redshift

Both PostgreSQL and Amazon Redshift use the copy command to bulk load data, however Redshift has additional requirements to load the data into the cloud. For PostgreSQL make a file with the copy commands for all tables for example:

\copy customer from '/home/postgres/TPCHDATA/customer_1.tbl' WITH DELIMITER AS '|';
\copy customer from '/home/postgres/TPCHDATA/customer_2.tbl' WITH DELIMITER AS '|';
\copy customer from '/home/postgres/TPCHDATA/customer_3.tbl' WITH DELIMITER AS '|';
\copy customer from '/home/postgres/TPCHDATA/customer_4.tbl' WITH DELIMITER AS '|';
\copy customer from '/home/postgres/TPCHDATA/customer_5.tbl' WITH DELIMITER AS '|';
\copy customer from '/home/postgres/TPCHDATA/customer_6.tbl' WITH DELIMITER AS '|';
\copy customer from '/home/postgres/TPCHDATA/customer_7.tbl' WITH DELIMITER AS '|';
\copy customer from '/home/postgres/TPCHDATA/customer_8.tbl' WITH DELIMITER AS '|';

And run the script to copy the files

psql -U postgres -d tpch -f TPCHCOPY.sql
With PostgreSQL additional lines are required to handle NULL value for the TPROC-C schema as follows:

\copy order_line from '/home/postgres/TPCCDATA/order_line_1.tbl' WITH NULL AS '' DELIMITER AS '|';
\copy orders from '/home/postgres/TPCCDATA/orders_1.tbl' WITH NULL AS '' DELIMITER AS '|';

For Amazon Redshift firstly upload the generated files to an Amazon S3 bucket. As noted previously Amazon S3 is one of the databases that supports loading from a compressed file and therefore you may wish to convert the files to a compressed format such as gzip before uploading.

**Figure 13.14.Upload to S3**

![Image 2: Upload to S3](https://www.hammerdb.com/docs4.0/resources/ch10-14.png)

Under the AWS IAM Console create a user for uploading and under security credentials create and download an access key. Note that the access keys have been removed from the image.

**Figure 13.15.Postgres User Access Keys**

![Image 3: Postgres User Access Keys](https://www.hammerdb.com/docs4.0/resources/ch10-15.png)

Finally give the postgres user permission to access Amazon S3.

**Figure 13.16.S3 Permissions**

![Image 4: S3 Permissions](https://www.hammerdb.com/docs4.0/resources/ch10-16.png)

Now connect to Redshift using the PostgreSQL command line tool and run the copy command specifying the location of the S3 bucket and the CREDENTIALs option where the XXX characters are replaced by the access key and secure access key you created previously.

-bash-4.2$ psql -h tpch-instance.xxxxxxxxxxxx.eu-west-1.redshift.amazonaws.com -U postgres -d tpch -p 5439
Password for user postgres: 
psql (9.2.15, server 8.0.2)
WARNING: psql version 9.2, server version 8.0.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

tpch=# copy region from 's3://s3bucket/load/region_1.tbl' CREDENTIALS 'aws_access_key_id=XXXXXXXXXXXXXXXXXXXX;aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' delimiter '|';
INFO:  Load into table 'region' completed, 5 record(s) loaded successfully.
COPY

Note that if you specify part of the filename Redshift will upload all of the files with the same prefix.

copy customer from 's3://s3bucket/load/customer_' CREDENTIALS 'aws_access_key_id=XXXXXXXXXXXXXXXXXXXX;aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' delimiter '|';
INFO:  Load into table 'customer' completed, 150000 record(s) loaded successfully.

For NULL values and date and time formats you can specify the formats for load as follows:

tpch=# copy orders from 's3://s3bucket/load/orders_' CREDENTIALS 'aws_access_key_id=XXXXXXXXXXXXXXXXXXXX;aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' emptyasnull blanksasnull delimiter '|' timeformat 'YYYY-MON-DD HH:MI:SS';
INFO:  Load into table 'orders' completed, 1500000 record(s) loaded successfully.
COPY

Note that as a column store Redshift does not require the additional indexes or constraints of a traditional row store format.
