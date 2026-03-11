# Source: https://www.hammerdb.com/docs4.0/ch09s08.html

Title: 8. CLI Scripting

URL Source: https://www.hammerdb.com/docs4.0/ch09s08.html

Markdown Content:
The CLI enables a powerful automated test environment through scripting in the TCL language. A recommended updated guide to TCL is "The Tcl Programming Language: A Comprehensive Guide by Ashok P. Nadkarni (ISBN: 9781548679644)"

The following example shows an automated test script for a Microsoft SQL Server database that has previously been created. In this example the script runs a timed tests for a duration of a minute for 1, 2 and 4 Virtual Users in a similar manner to autopilot functionality with a timer set to run for 2 minutes. Note that from HammerDB v4.0 the runtimer command is included. The timer is set to a period of time for the test to run, however if vucomplete is set to true during the test it will also return.

#!/usr/bin/tclsh
puts "SETTING CONFIGURATION"
dbset db mssqls
diset tpcc mssqls_driver timed
diset tpcc mssqls_rampup 0
diset tpcc mssqls_duration 1
vuset logtotemp 1
loadscript
puts "SEQUENCE STARTED"
foreach z { 1 2 4 } {
puts "$z VU TEST"
vuset vu $z
vucreate
vurun
runtimer 120
vudestroy
after 5000
}
puts "TEST SEQUENCE COMPLETE"
Run the hammerdbcli command and at the prompt type source and the name of the script. The following output is produced without further intervention whilst also writing the output to the logfile.

HammerDB CLI v4.0
Copyright (C) 2003-2020 Steve Shaw
Type "help" for a list of commands
The xml is well-formed, applying configuration
hammerdb>source cliexample.tcl
SETTING CONFIGURATION
Database set to MSSQLServer
Clearing Script, reload script to activate new setting
Script cleared
Changed tpcc:mssqls_driver from test to timed for MSSQLServer
Changed tpcc:mssqls_rampup from 2 to 0 for MSSQLServer
Changed tpcc:mssqls_duration from 5 to 1 for MSSQLServer
Script loaded, Type "print script" to view
SEQUENCE STARTED
1 VU TEST
Vuser 1 created MONITOR - WAIT IDLE
Vuser 2 created - WAIT IDLE
Logging activated
to C:/Users/Hdb/AppData/Local/Temp/hammerdb.log
2 Virtual Users Created with Monitor VU
Vuser 1:RUNNING
Vuser 1:Beginning rampup time of 0 minutes
Vuser 1:Rampup complete, Taking start Transaction Count.
Vuser 1:Timing test period of 1 in minutes
Vuser 2:RUNNING
Vuser 2:Processing 1000000 transactions with output suppressed...
Vuser 1:1 ...,
Vuser 1:Test complete, Taking end Transaction Count.
Timer: 1 minutes elapsed
Vuser 1:1 Active Virtual Users configured
Vuser 1:TEST RESULT : System achieved 35576 NOPM from 81705 SQL Server TPM
Vuser 1:FINISHED SUCCESS
Vuser 2:FINISHED SUCCESS
ALL VIRTUAL USERS COMPLETE
runtimer returned after 61 seconds
vudestroy success
2 VU TEST
Vuser 1 created MONITOR - WAIT IDLE
Vuser 2 created - WAIT IDLE
Vuser 3 created - WAIT IDLE
Logging activated
to C:/Users/Hdb/AppData/Local/Temp/hammerdb.log
3 Virtual Users Created with Monitor VU
Vuser 1:RUNNING
Vuser 1:Beginning rampup time of 0 minutes
Vuser 1:Rampup complete, Taking start Transaction Count.
Vuser 1:Timing test period of 1 in minutes
Vuser 2:RUNNING
Vuser 2:Processing 1000000 transactions with output suppressed...
Vuser 3:RUNNING
Vuser 3:Processing 1000000 transactions with output suppressed...
Vuser 1:1 ...,
Vuser 1:Test complete, Taking end Transaction Count.
Vuser 1:2 Active Virtual Users configured
Vuser 1:TEST RESULT : System achieved 60364 NOPM from 138633 SQL Server TPM
Timer: 1 minutes elapsed
Vuser 1:FINISHED SUCCESS
Vuser 2:FINISHED SUCCESS
Vuser 3:FINISHED SUCCESS
ALL VIRTUAL USERS COMPLETE
runtimer returned after 60 seconds
vudestroy success
4 VU TEST
Vuser 1 created MONITOR - WAIT IDLE
Vuser 2 created - WAIT IDLE
Vuser 3 created - WAIT IDLE
Vuser 4 created - WAIT IDLE
Vuser 5 created - WAIT IDLE
Logging activated
to C:/Users/Hdb/AppData/Local/Temp/hammerdb.log
5 Virtual Users Created with Monitor VU
Vuser 1:RUNNING
Vuser 1:Beginning rampup time of 0 minutes
Vuser 1:Rampup complete, Taking start Transaction Count.
Vuser 1:Timing test period of 1 in minutes
Vuser 2:RUNNING
Vuser 2:Processing 1000000 transactions with output suppressed...
Vuser 3:RUNNING
Vuser 3:Processing 1000000 transactions with output suppressed...
Vuser 4:RUNNING
Vuser 4:Processing 1000000 transactions with output suppressed...
Vuser 5:RUNNING
Vuser 5:Processing 1000000 transactions with output suppressed...
Vuser 1:1 ...,
Vuser 1:Test complete, Taking end Transaction Count.
Vuser 1:4 Active Virtual Users configured
Vuser 1:TEST RESULT : System achieved 103055 NOPM from 236412 SQL Server TPM
Vuser 1:FINISHED SUCCESS
Vuser 2:FINISHED SUCCESS
Vuser 4:FINISHED SUCCESS
Vuser 5:FINISHED SUCCESS
Vuser 3:FINISHED SUCCESS
ALL VIRTUAL USERS COMPLETE
runtimer returned after 59 seconds
vudestroy success
TEST SEQUENCE COMPLETE

hammerdb>
It is a common requirement to also want to drive HammerDB CLI scripts from an external scripting tool. For this reason HammerDB v4.0 also includes the command waittocomplete. This can be seen as complementary to runtimer, whereas runtimer will run in the main thread for a specified period of time, waittocomplete will wait for an indeterminate period of time until vucomplete is set to true. Therefore waittocomplete is particularly beneficial for schema builds which may take different periods of time but is complete when all Virtual Users have finished their task. An example automated build is shown.

#!/bin/tclsh
dbset db mssqls
diset tpcc mssqls_count_ware 10
diset tpcc mssqls_num_vu 4
diset connection mssqls_server {(local)\SQLDEVELOP}
vuset logtotemp 1
print dict
buildschema
waittocomplete
The HammerDB CLI will accept the argument auto to run a specified script automatically.

hammerdbcli.bat auto autorunbuild.tcl
Using this approach it is possible to build complex test scenarios automating both build and test functionality.
