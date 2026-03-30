# Source: https://www.hammerdb.com/docs4.0/ch09s03.html

Title: 3. Configure Schema Build

URL Source: https://www.hammerdb.com/docs4.0/ch09s03.html

Markdown Content:
Use the dbset command to choose a database and benchmark. For the database the database prefix shown in the XML configuration is used. IIf an incorrect database is selected the available values are prompted.

hammerdb>dbset db orac
Unknown prefix orac, choose one from ora mssqls db2 mysql pg
When a valid option is chosen the database is set.

hammerdb>dbset db mssqls
Database set to MSSQLServer
The print command can be used to confirm the chosen database and available options.

hammerdb>print db
Database MSSQLServer set.
To change do: dbset db prefix, one of:
Oracle = ora MSSQLServer = mssqls Db2 = db2 MySQL = mysql PostgreSQL = pg 
Similarly the workload is also selected from the available configuration also prompting if an incorrect value is chosen. When a correct value is chosen the selection is confirmed. For backward compatibility with existing scripts TPROC-C and TPC-C and TPROC-H and TPC-H are interchangeable.

hammerdb>dbset bm TPROC-H
Benchmark set to TPROC-H for MSSQLServer

hammerdb>dbset bm TPC-C
Benchmark set to TPC-C for MSSQLServer

hammerdb>print bm
Benchmark set to TPC-C
After the database and workload is selected the print dict command lists all of the available configuration variables for that database.

hammerdb>print dict
Dictionary Settings for MSSQLServer
connection {
 mssqls_server         = (local)
 mssqls_linux_server   = localhost
 mssqls_tcp            = false
 mssqls_port           = 1433
 mssqls_azure          = false
 mssqls_authentication = windows
 mssqls_linux_authent  = sql
 mssqls_odbc_driver    = ODBC Driver 17 for SQL Server
 mssqls_linux_odbc     = ODBC Driver 17 for SQL Server
 mssqls_uid            = sa
 mssqls_pass           = admin
}
tpcc       {
 mssqls_count_ware       = 1
 mssqls_num_vu           = 1
 mssqls_dbase            = tpcc
 mssqls_imdb             = false
 mssqls_bucket           = 1
 mssqls_durability       = SCHEMA_AND_DATA
 mssqls_total_iterations = 1000000
 mssqls_raiseerror       = false
 mssqls_keyandthink      = false
 mssqls_checkpoint       = false
 mssqls_driver           = test
 mssqls_rampup           = 2
 mssqls_duration         = 5
 mssqls_allwarehouse     = false
 mssqls_timeprofile      = false
 mssqls_async_scale      = false
 mssqls_async_client     = 10
 mssqls_async_verbose    = false
 mssqls_async_delay      = 1000
 mssqls_connect_pool     = false
}

Use the diset command to change these values for example for the number of warehouses to build.

hammerdb>diset tpcc mssqls_count_ware 10
Changed tpcc:mssqls_count_ware from 1 to 10 for MSSQLServer
and the number of virtual users to build them.

hammerdb>diset tpcc mssqls_num_vu 4
Changed tpcc:mssqls_num_vu from 1 to 4 for MSSQLServer
If the dict value to be set has a special character using curly brackets around the value will prevent the interpretation of the special character.

hammerdb>diset connection mssqls_server {(local)\SQLDEVELOP}
Changed connection:mssqls_server from (local) to (local)\SQLDEVELOP for MSSQLServer
print dict will show the changed values.

hammerdb>print dict
Dictionary Settings for MSSQLServer
connection {
 mssqls_server         = (local)\SQLDEVELOP
 mssqls_linux_server   = localhost
 mssqls_tcp            = false
 mssqls_port           = 1433
 mssqls_azure          = false
 mssqls_authentication = windows
 mssqls_linux_authent  = sql
 mssqls_odbc_driver    = ODBC Driver 17 for SQL Server
 mssqls_linux_odbc     = ODBC Driver 17 for SQL Server
 mssqls_uid            = sa
 mssqls_pass           = admin
}
tpcc       {
 mssqls_count_ware       = 10
 mssqls_num_vu           = 4
 mssqls_dbase            = tpcc
 mssqls_imdb             = false
 mssqls_bucket           = 1
 mssqls_durability       = SCHEMA_AND_DATA
 mssqls_total_iterations = 1000000
 mssqls_raiseerror       = false
 mssqls_keyandthink      = false
 mssqls_checkpoint       = false
 mssqls_driver           = test
 mssqls_rampup           = 2
 mssqls_duration         = 5
 mssqls_allwarehouse     = false
 mssqls_timeprofile      = false
 mssqls_async_scale      = false
 mssqls_async_client     = 10
 mssqls_async_verbose    = false
 mssqls_async_delay      = 1000
 mssqls_connect_pool     = false
}
