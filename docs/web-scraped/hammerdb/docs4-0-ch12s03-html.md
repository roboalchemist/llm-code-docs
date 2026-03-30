# Source: https://www.hammerdb.com/docs4.0/ch12s03.html

Title: 3. Configuring Schema Build Options

URL Source: https://www.hammerdb.com/docs4.0/ch12s03.html

Markdown Content:
To create the analytic test schema based on the TPROC-H you will need to select which benchmark and database you wish to use by choosing select benchmark from under the Options menu or under the benchmark tree-view. The initial settings are determined by the values in your XML configuration files. The following example shows the selection of SQL Server however the process is the same for all databases.

**Figure 12.2.Benchmark Options**

![Image 1: Benchmark Options](https://www.hammerdb.com/docs4.0/resources/ch13-2.PNG)

To create the TPROC-H schema select the TPROC-H schema options menu tab from the benchmark tree-view or the options menu. This menu will change dynamically according to your chosen database.

**Figure 12.3.TPROC-H Schema Build Options**

![Image 2: TPROC-H Schema Build Options](https://www.hammerdb.com/docs4.0/resources/ch13-3.PNG)

If selected from the Options menu the schema options window is divided into two sections. The “Build Options” section details the general login information and where the schema will be built and the “Driver Options” for the Driver Script to run after the schema is built. If selected from the benchmark tree-view only the “Build Options” are shown and these are the only options of importance at this stage. Note that in any circumstance you do not have to rebuild the schema every time you change the “Driver Options”, once the schema has been built only the “Driver Options” may need to be modified. For the “Build Options” fill in the values according to the database where the schema will be built as follows.

### [](https://www.hammerdb.com/docs4.0/ch12s03.html)3.1.Oracle Schema Build Options

**Figure 12.4.Oracle TPROC-H Build Options**

![Image 3: Oracle TPROC-H Build Options](https://www.hammerdb.com/docs4.0/resources/ch13-4.PNG)

**Table 12.1.Oracle Build Options**

| Option | Description |
| --- | --- |
| Oracle Service Name | The Oracle Service Name is the service name that your load generation server will use to connect to the database running on the SUT database server. |
| System User | The “system” user or a user with system level privileges |
| System User Password | The system user password is the password for the “system” user you entered during database creation. The system user already exists in all Oracle databases and has the necessary permissions to create the TPROC-H user. |
| TPROC-H User | The TPROC-H user is the name of a user to be created that will own the TPROC-H schema. This user can have any name you choose but must not already exist and adhere to the standard rules for naming Oracle users. You may if you wish run the schema creation multiple times and have multiple TPROC-H schemas created with ownership under a different user you create each time. |
| TPROC-H User Password | The TPROC-H user password is the password to be used for the TPROC-H user you create and must adhere to the standard rules for Oracle user password. You will need to remember the TPROC-H user name and password for running the TPROC-H driver script after the schema is built. |
| TPROC-H Default Tablespace | The TPROC-H default tablespace is the tablespace that will be the default for the TPROC-H user and therefore the tablespace to be used for the schema creation. The tablespace must have sufficient free space for the schema to be created. |
| TPROC-H Temporary Tablespace | The TPROC-H temporary tablespace is the temporary tablespace that already exists in the database to be used by the TPROC-H User. |
| TimesTen Database Compatible | When selected this option means that the Oracle Service Name should be a TimesTen Data Source Name and will grey out non-compatible options. |
| Scale Factor | The Scale Factor is selected by a radio button with a choice of scale factors of 1,10,30,100,300 and 1000 corresponding to 1GB, 10GB, 30GB,100GB and 1000GB respectively, larger schema sizes can also be created with the datagen option. Note that the required space will be larger than these values due to the indexes required. |
| Virtual Users to Build Schema | The Virtual Users to Build Schema is the number of Virtual Users to be created on the Load Generation Server that will complete your multi-threaded schema build. You should set this value to the number of cores on your Load Generation Server or SUT if HammerDB is running there. |

### [](https://www.hammerdb.com/docs4.0/ch12s03.html)3.2.SQL Server Schema Build Options

**Figure 12.5.SQL Server Build Options**

![Image 4: SQL Server Build Options](https://www.hammerdb.com/docs4.0/resources/ch13-5.PNG)

**Table 12.2.SQL Server Build Options**

| Option | Description |
| --- | --- |
| SQL Server | The Microsoft SQL Server is the host name or host name and instance where the TPROC-H database will be created. |
| TCP | Use the TCP Protocol |
| SQL Server Port | When TCP is enabled, the SQL Server Port is the network port that your load generation server will use to connect to the database running on the SUT database server. In most cases this will be the default port of 1433 and will not need to be changed. |
| Azure | Include the Database name in the connect string typical of Azure connections. To successfully build the schema this database must be created and empty. |
| SQL Server ODBC Driver | The Microsoft SQL ODBC Driver is the ODBC driver you will use to connect to the SQL Server database. To view which drivers are available on Windows view the ODBC Data Source Administrator Tool. |
| Authentication | When installing SQL Server on Windows you will have configured SQL Server for Windows or Windows and SQL Server Authentication. On Linux you will be using SQL Server Authentication. If you specify Windows Authentication then SQL Server will use a trusted connection to your SQL Server using your Windows credentials without requiring a username and password. If SQL Server Authentication is specified and SQL Authentication is enabled on your SQL Server then you will be able connect by specifying a username and password that you have already configured on your SQL Server. |
| SQL Server User ID | The SQL Server User ID is the User ID of a user that you have already created on your SQL Server. |
| SQL Server User Password | The SQL Server User Password is the Password configured on the SQL Server for the User ID you have specified. Note that when configuring the password on the SQL Server there is a checkbox that when selected enforces more complex rules for passwords or if unchecked enables a simple password such as “admin”. |
| SQL Server TPCH Database | The SQL Server Database is the name of the Database to be created on the SQL Server to contain the schema. If this database does not already exist then HammerDB will create it, if the database does already exist and the database is empty then HammerDB will use this existing database. Therefore if you wish to create a particular layout or schema then pre-creating the database and using this database is an advanced method to use this configuration. |
| MAXDOP | The MAXDOP setting defines the maximum degree of parallelism to be set as a default on the schema objects. |
| Clustered Columnstore | This option selects the database to be created with in-memory clustered columnstore indexes. |
| Scale Factor | The Scale Factor is selected by a radio button with a choice of scale factors of 1,10,30,100,300 and 1000 corresponding to 1GB, 10GB, 30GB,100GB and 1000GB respectively, larger schema sizes can also be created with the datagen option. Note that the required space will be larger than these values due to the indexes required. |
| Virtual Users to Build Schema | The Virtual Users to Build Schema is the number of Virtual Users to be created on the Load Generation Server that will complete your multi-threaded schema build. You should set this value to the number of cores on your Load Generation Server or SUT if HammerDB is running there. |

### [](https://www.hammerdb.com/docs4.0/ch12s03.html)3.3.Db2 Schema Build Options

**Figure 12.6.Db2 Build Options**

![Image 5: Db2 Build Options](https://www.hammerdb.com/docs4.0/resources/ch13-6.PNG)

**Table 12.3.Db2 Build Options**

| Option | Description |
| --- | --- |
| Db2 User | The name of the operating system user to connect to the DB2 database for example db2inst1. |
| Db2 Password | The password for the operating system DB2 user by default “ibmdb2” |
| Db2 Database | The name of the Db2 database that you have already created, for example “tpcc” |
| Db2 Default Tablespace | The name of the existing tablespace where tables should be located if a specific tablespace has not been defined for that table in the tablespace list. The default is “USERSPACE1”. |
| Db2 Organize By | The Organize by option is selected by a radio button and determines an optional organize by clause to be specified when creating the tables. The database version must be able to accept the option chosen and therefore the recommended choice is NONE to accept the defaults. When the setting DB2_WORKLOAD is set to analytics for example the default is configuration is for columnar storage. If for example this parameter is set you can then choose ROW configuration even when DB2_WORKLOAD is set to analytics to create row organized tables. The DATE option is mutually exclusive to the column store option however creates a ROW organized table that is organized by date which can accelerate some queries when row organized. |
| Scale Factor | The Scale Factor is selected by a radio button with a choice of scale factors of 1,10,30,100,300 and 1000 corresponding to 1GB, 10GB, 30GB,100GB and 1000GB respectively, larger schema sizes can also be created with the datagen option. Note that the required space will be larger than these values due to the indexes required. |
| Virtual Users to Build Schema | The Virtual Users to Build Schema is the number of Virtual Users to be created on the Load Generation Server that will complete your multi-threaded schema build. You should set this value to the number of cores on your Load Generation Server or SUT if HammerDB is running there. |

### [](https://www.hammerdb.com/docs4.0/ch12s03.html)3.4.MySQL Schema Build Options

**Figure 12.7.MySQL Build Options**

![Image 6: MySQL Build Options](https://www.hammerdb.com/docs4.0/resources/ch13-8.PNG)

**Table 12.4.MySQL Build Options**

| Option | Description |
| --- | --- |
| MySQL Host | The MySQL Host Name is the host name of the SUT database server. |
| MySQL Port | The MySQL Port is the network port on the SUT database server. In most cases this will be the default port of 3306. |
| MySQL User | The MySQL User is the user which has permission to create a database and you previously granted access to from the load generation server. The root user already exists in all MySQL databases and has the necessary permissions to create the TPROC-H database. |
| MySQL User Password | The MySQL user password is the password for the user defined as the MySQL User. You will need to remember the MySQL user name and password for running the TPROC-H driver script after the database is built. |
| MySQL Database | The MySQL Database is the database that will be created containing the TPROC-H schema creation. There must have sufficient free space for the database to be created. |
| Data Warehouse Storage Engine | Use the "show engine" command to display available storage engines and select a storage engine that supports analytics. For MariaDB columnstore specify. "Columnstore" |
| Scale Factor | The Scale Factor is selected by a radio button with a choice of scale factors of 1,10,30,100,300 and 1000 corresponding to 1GB, 10GB, 30GB,100GB and 1000GB respectively, larger schema sizes can also be created with the datagen option. Note that the required space will be larger than these values due to the indexes required. |
| Virtual Users to Build Schema | The Virtual Users to Build Schema is the number of Virtual Users to be created on the Load Generation Server that will complete your multi-threaded schema build. You should set this value to the number of cores on your Load Generation Server or SUT if HammerDB is running there. |

### [](https://www.hammerdb.com/docs4.0/ch12s03.html)3.5.PostgreSQL Schema Build Options

**Figure 12.8.PostgreSQL Build Options**

![Image 7: PostgreSQL Build Options](https://www.hammerdb.com/docs4.0/resources/ch13-7.PNG)

**Table 12.5.PostgreSQL Build Options**

| Option | Description |
| --- | --- |
| PostgreSQL Host | The host name of the SUT running PostgreSQL. |
| PostgreSQL Port | The port of the PostgreSQL service. By default this will be 5432 for a standard PostgreSQL installation or 5444 for EnterpriseDB. |
| PostgreSQL Superuser | The PostgreSQL Superuser is a user with sufficient privileges to create both new users (roles) and databases to enable the creation of the test schema. |
| PostgreSQL Superuser Password | The PostgreSQL Superuser Password is the password for the PostgreSQL superuser which will have been defined during installation. If you have forgotten the password it can be reset from a psql prompt that has logged in from a trusted connection therefore requiring no password using postgres=# alter role postgres password ‘postgres’; |
| PostgreSQL Default Database | The PostgreSQL default databases is the database to specify for the superuser connection. Typically this will be postgres for a standard PostgreSQL installation or edb for EnterpriseDB. |
| PostgreSQL User | The PostgreSQL User is the user (role) that will be created that owns the database containing the TPROC-H schema. |
| PostgreSQL User Password | The PostgreSQL User Password is the password that will be specified for the PostgreSQL user when it is created. |
| PostgreSQL Database | The PostgreSQL Database is the database that will be created and owned by the PostgreSQL User that contains the TPROC-H schema. |
| Greenplum Database Compatible | Choosing Greenplum Database Compatible creates a schema with Greenplum Database Options. Building the schema by inserting into Greenplum is not recommended and instead a bulk load of data created with the datagen option should be used. |
| Greenplum Compressed Columns | Becomes active when Greenplum Database Compatible is selected and configures the columns in a compressed format. |
| Scale Factor | The Scale Factor is selected by a radio button with a choice of scale factors of 1,10,30,100,300 and 1000 corresponding to 1GB, 10GB, 30GB,100GB and 1000GB respectively, larger schema sizes can also be created with the datagen option. Note that the required space will be larger than these values due to the indexes required. |
| Virtual Users to Build Schema | The Virtual Users to Build Schema is the number of Virtual Users to be created on the Load Generation Server that will complete your multi-threaded schema build. You should set this value to the number of cores on your Load Generation Server or SUT if HammerDB is running there. |
