# Source: https://www.hammerdb.com/docs4.0/ch09s05.html

Title: 5. Configure Driver

URL Source: https://www.hammerdb.com/docs4.0/ch09s05.html

Markdown Content:
Set the type of workload to run. A timed workload with suppressed output is strongly recommended as a test workload will print considerable output to the command prompt.

hammerdb>diset tpcc mssqls_driver timed
Clearing Script, reload script to activate new setting
Script cleared
Changed tpcc:mssqls_driver from test to timed for MSSQLServer
Configure workload settings, in this example the rampup and duration times are set.

hammerdb>diset tpcc mssqls_rampup 1
Changed tpcc:mssqls_rampup from 2 to 1 for MSSQLServer

hammerdb>diset tpcc mssqls_duration 3
Changed tpcc:mssqls_duration from 5 to 3 for MSSQLServer
Confirm the settings with the print dict command.

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
 mssqls_driver           = timed
 mssqls_rampup           = 1
 mssqls_duration         = 3
 mssqls_allwarehouse     = false
 mssqls_timeprofile      = false
 mssqls_async_scale      = false
 mssqls_async_client     = 10
 mssqls_async_verbose    = false
 mssqls_async_delay      = 1000
 mssqls_connect_pool     = false
}
When all the settings have been chosen load the driver script with the loadscript command.

hammerdb>loadscript
Script loaded, Type "print script" to view
The loaded script can be viewed with the print script command. Note that the driver script is exactly the same as the driver script observed in the GUI. There is no difference whatsoever in what is run in the CLI compared to the GUI. If there is a wish to change the script a modified version can be loaded with the customscript command and it is therefore recommended to use the GUI to save a version of the script to modify.

#!/usr/local/bin/tclsh8.6
#EDITABLE OPTIONS##################################################
set library tdbc::odbc ;# SQL Server Library
set version 1.1.1 ;# SQL Server Library Version
set total_iterations 1000000;# Number of transactions before logging off
set RAISEERROR "false" ;# Exit script on SQL Server error (true or false)
set KEYANDTHINK "false" ;# Time for user thinking and keying (true or false)
set CHECKPOINT "false" ;# Perform SQL Server checkpoint when complete (true or false)
set rampup 1;  # Rampup time in minutes before first Transaction Count is taken
set duration 3;  # Duration in minutes before second Transaction Count is taken
set mode "Local" ;# HammerDB operational mode
set authentication "windows";# Authentication Mode (WINDOWS or SQL)
set server {(local)\SQLDEVELOP1};# Microsoft SQL Server Database Server
set port "1433";# Microsoft SQL Server Port 
set odbc_driver {ODBC Driver 17 for SQL Server};# ODBC Driver
set uid "sa";#User ID for SQL Server Authentication
set pwd "admin";#Password for SQL Server Authentication
set tcp "false";#Specify TCP Protocol
set azure "false";#Azure Type Connection
set database "tpcc";# Database containing the TPC Schema
#EDITABLE OPTIONS##################################################
...
