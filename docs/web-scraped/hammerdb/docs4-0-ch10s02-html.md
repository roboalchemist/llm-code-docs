# Source: https://www.hammerdb.com/docs4.0/ch10s02.html

Title: 2. Starting the Web Service and Help Screen

URL Source: https://www.hammerdb.com/docs4.0/ch10s02.html

Markdown Content:
On starting the Web service with the hammerdbws command HammerDB will listen on the specified port for HTTP requests.

[oracle@vulture HammerDB-4.0]$ ./hammerdbws 
HammerDB Web Service v4.0
Copyright (C) 2003-2020 Steve Shaw
Type "help" for a list of commands
The xml is well-formed, applying configuration
Initialized new SQLite in-memory database
Starting HammerDB Web Service on port 8080
Listening for HTTP requests on TCP port 8080

Navigating to the configured port without further argument will return the help screen.

HammerDB Web Service

See the HammerDB Web Service Environment
HAMMERDB REST/HTTP API

GET db: Show the configured database.
get http://localhost:8080/print?db / get http://localhost:8080/db
{
"ora": "Oracle",
"mssqls": "MSSQLServer",
"db2": "Db2",
"mysql": "MySQL",
"pg": "PostgreSQL",
"redis": "Redis"
}

GET bm: Show the configured benchmark.
get http://localhost:8080/print?bm / get http://localhost:8080/bm
{"benchmark": "TPC-C"}

GET dict: Show the dictionary for the current database ie all active variables.
get http://localhost:8080/print?dict /  http://localhost:8080/dict
{
"connection": {
"system_user": "system",
"system_password": "manager",
"instance": "oracle",
"rac": "0"
},
"tpcc": {
"count_ware": "1",
"num_vu": "1",
"tpcc_user": "tpcc",
"tpcc_pass": "tpcc",
"tpcc_def_tab": "tpcctab",
"tpcc_ol_tab": "tpcctab",
"tpcc_def_temp": "temp",
"partition": "false",
"hash_clusters": "false",
"tpcc_tt_compat": "false",
"total_iterations": "1000000",
"raiseerror": "false",
"keyandthink": "false",
"checkpoint": "false",
"ora_driver": "test",
"rampup": "2",
"duration": "5",
"allwarehouse": "false",
"timeprofile": "false"
}
}

 
GET script: Show the loaded script.
get http://localhost:8080/print?script / http://localhost:8080/script
{"script": "#!/usr/local/bin/tclsh8.6
#TIMED AWR SNAPSHOT DRIVER SCRIPT##################################
#THIS SCRIPT TO BE RUN WITH VIRTUAL USER OUTPUT ENABLED
#EDITABLE OPTIONS##################################################
set library Oratcl ;# Oracle OCI Library
set total_iterations 1000000 ;# Number of transactions before logging off
set RAISEERROR \"false\" ;# Exit script on Oracle error (true or false)
set KEYANDTHINK \"false\" ;# Time for user thinking and keying (true or false)
set CHECKPOINT \"false\" ;# Perform Oracle checkpoint when complete (true or false)
set rampup 2;  # Rampup time in minutes before first snapshot is taken
set duration 5;  # Duration in minutes before second AWR snapshot is taken
set mode \"Local\" ;# HammerDB operational mode
set timesten \"false\" ;# Database is TimesTen
set systemconnect system/manager@oracle ;# Oracle connect string for system user
set connect tpcc/new_password@oracle ;# Oracle connect string for tpc-c user
#EDITABLE OPTIONS##################################################
#LOAD LIBRARIES AND MODULES …. 
"}

 
GET vuconf: Show the virtual user configuration.
get http://localhost:8080/print?vuconf / http://localhost:8080/vuconf
{
"Virtual Users": "1",
"User Delay(ms)": "500",
"Repeat Delay(ms)": "500",
"Iterations": "1",
"Show Output": "1",
"Log Output": "0",
"Unique Log Name": "0",
"No Log Buffer": "0",
"Log Timestamps": "0"
}

 
GET vucreate: Create the virtual users. Equivalent to the Virtual User Create option in the graphical interface. Use vucreated to see the number created, vustatus to see the status and vucomplete to see whether all active virtual users have finished the workload. A script must be loaded before virtual users can be created.
get http://localhost:8080/vucreate
{"success": {"message": "4 Virtual Users Created"}}

 
GET vucreated: Show the number of virtual users created.
get http://localhost:8080/print?vucreated / get http://localhost:8080/vucreated
{"Virtual Users created": "10"}

 
GET vustatus: Show the status of virtual users, status will be "WAIT IDLE" for virtual users that are created but not running a workload,"RUNNING" for virtual users that are running a workload, "FINISH SUCCESS" for virtual users that completed successfully or "FINISH FAILED" for virtual users that encountered an error.
get http://localhost:8080/print?vustatus / get http://localhost:8080/vustatus
{"Virtual User status": "1 {WAIT IDLE} 2 {WAIT IDLE} 3 {WAIT IDLE} 4 {WAIT IDLE} 5 {WAIT IDLE} 6 {WAIT IDLE} 7 {WAIT IDLE} 8 {WAIT IDLE} 9 {WAIT IDLE} 10 {WAIT IDLE}"}

 
GET datagen: Show the datagen configuration
get http://localhost:8080/print?datagen /  get http://localhost:8080/datagen
{
"schema": "TPC-C",
"database": "Oracle",
"warehouses": "1",
"vu": "1",
"directory": "/tmp\""
}

 
GET vucomplete: Show if virtual users have completed. returns "true" or "false" depending on whether all virtual users that started a workload have completed regardless of whether the status was "FINISH SUCCESS" or "FINISH FAILED".
get http://localhost:8080/vucomplete
{"Virtual Users complete": "true"}

 
GET vudestroy: Destroy the virtual users. Equivalent to the Destroy Virtual Users button in the graphical interface that replaces the Create Virtual Users button after virtual user creation.
get http://localhost:8080/vudestroy
{"success": {"message": "vudestroy success"}}

 
GET loadscript: Load the script for the database and benchmark set with dbset and the dictionary variables set with diset. Use print?script to see the script that is loaded. Equivalent to loading a Driver Script in the Script Editor window in the graphical interface. Driver script must be set to timed for the script to be loaded. Test scripts should be run in the GUI environment.  
get http://localhost:8080/loadscript
{"success": {"message": "script loaded"}}

 
GET clearscript: Clears the script. Equivalent to the "Clear the Screen" button in the graphical interface.
get http://localhost:8080/clearscript
{"success": {"message": "Script cleared"}}

 
GET vurun: Send the loaded script to the created virtual users for execution. Equivalent to the Run command in the graphical interface. Creates a job id associated with all output. 
get http://localhost:8080/vurun
{"success": {"message": "Running Virtual Users: JOBID=5CEFBFE658A103E253238363"}}

GET datagenrun: Run Data Generation. Equivalent to the Generate option in the graphical interface. Not supported in web service. Generate data using GUI or CLI. 

GET buildschema: Runs the schema build for the database and benchmark selected with dbset and variables selected with diset. Equivalent to the Build command in the graphical interface. Creates a job id associated with all output. 
get http://localhost:8080/buildschema
{"success": {"message": "Building 6 Warehouses with 4 Virtual Users, 3 active + 1 Monitor VU(dict value num_vu is set to 3): JOBID=5CEFA68458A103E273433333"}}

GET jobs: Show the job ids, output, status and results of jobs created by buildschema and vurun. Job output is equivalent to the output viewed in the graphical interface or command line.
GET http://localhost:8080/jobs: Show all job ids
get http://localhost:8080/jobs
[
"5CEE889958A003E203838313",
"5CEFA68458A103E273433333"
]
GET http://localhost:8080/jobs?jobid=TEXT: Show output for the specified job id.
get http://localhost:8080/jobs?jobid=5CEFA68458A103E273433333
[
"0",
"Ready to create a 6 Warehouse Oracle TPC-C schema
in database VULPDB1 under user TPCC in tablespace TPCCTAB?",
"0",
"Vuser 1:RUNNING",
"1",
"Monitor Thread",
"1",
"CREATING TPCC SCHEMA",
...
"1",
"TPCC SCHEMA COMPLETE",
"0",
"Vuser 1:FINISHED SUCCESS",
"0",
"ALL VIRTUAL USERS COMPLETE"
]
GET http://localhost:8080/jobs?jobid=TEXT&vu=INTEGER: Show output for the specified job id and virtual user.
get http://localhost:8080/jobs?jobid=5CEFA68458A103E273433333&vu=1
[
"1",
"Monitor Thread",
"1",
"CREATING TPCC SCHEMA",
"1",
"CREATING USER tpcc",
"1",
"CREATING TPCC TABLES",
"1",
"Loading Item",
"1",
"Loading Items - 50000",
"1",
"Loading Items - 100000",
"1",
"Item done",
"1",
"Monitoring Workers...",
"1",
"Workers: 3 Active 0 Done"
]
GET http://localhost:8080/jobs?jobid=TEXT&status: Show status for the specified job id. Equivalent to virtual user 0.
get http://localhost:8080/jobs?jobid=5CEFA68458A103E273433333&status
[
"0",
"Ready to create a 6 Warehouse Oracle TPC-C schema
in database VULPDB1 under user TPCC in tablespace TPCCTAB?",
"0",
"Vuser 1:RUNNING",
"0",
"Vuser 2:RUNNING",
"0",
"Vuser 3:RUNNING",
"0",
"Vuser 4:RUNNING",
"0",
"Vuser 4:FINISHED SUCCESS",
"0",
"Vuser 3:FINISHED SUCCESS",
"0",
"Vuser 2:FINISHED SUCCESS",
"0",
"Vuser 1:FINISHED SUCCESS",
"0",
"ALL VIRTUAL USERS COMPLETE"
]
GET http://localhost:8080/jobs?jobid=TEXT&result: Show the test result for the specified job id. If job is not a test job such as build job then no result will be reported. 
get http://localhost:8080/jobs?jobid=5CEFA68458A103E273433333&result
[
"5CEFA68458A103E273433333",
"Jobid has no test result"
]
GET http://localhost:8080/jobs?jobid=TEXT&delete: Delete all output for the specified jobid.
get http://localhost:8080/jobs?jobid=5CEFA68458A103E273433333&delete
{"success": {"message": "Deleted Jobid 5CEFA68458A103E273433333"}} 

GET killws: Terminates the webservice and reports message to the console.
get http://localhost:8080/killws
Shutting down HammerDB Web Service

POST dbset: Usage: dbset [db|bm] value. Sets the database (db) or benchmark (bm). Equivalent to the Benchmark Menu in the graphical interface. Database value is set by the database prefix in the XML configuration.
set body { "db": "ora" }
rest::post http://localhost:8080/dbset $body

POST diset: Usage: diset dict key value. Set the dictionary variables for the current database. Equivalent to the Schema Build and Driver Options windows in the graphical interface. Use print?dict to see what these variables are and diset to change.
set body { "dict": "tpcc", "key": "rampup", "value": "0" }
rest::post http://localhost:8080/diset $body
set body { "dict": "tpcc", "key": "duration", "value": "1" }
rest::post http://localhost:8080/diset $body

POST vuset: Usage: vuset [vu|delay|repeat|iterations|showoutput|logtotemp|unique|nobuff|timestamps]. Configure the virtual user options. Equivalent to the Virtual User Options window in the graphical interface.
set body { "vu": "4" }
rest::post http://localhost:8080/vuset $body

POST customscript: Load an external script. Equivalent to the "Open Existing File" button in the graphical interface. Script must be converted to JSON format before post as shown in the example:
set customscript "testscript.tcl"
set _ED(file) $customscript
if {$_ED(file) == ""} {return}
if {![file readable $_ED(file)]} {
puts "File [$_ED(file)] is not readable."
return
}
if {[catch "open \"$_ED(file)\" r" fd]} {
puts "Error while opening $_ED(file): [$fd]"
} else {
set _ED(package) "[read $fd]"
close $fd
}
set huddleobj [ huddle compile {string} "$_ED(package)" ]
set jsonobj [ huddle jsondump $huddleobj ]
set body [ subst { {"script": $jsonobj}} ]
set res [ rest::post http://localhost:8080/customscript $body ] 

POST dgset: Usage: dgset [vu|ware|directory]. Set the Datagen options. Equivalent to the Datagen Options dialog in the graphical interface.
set body { "directory": "/home/oracle" }
rest::post http://localhost:8080/dgset $body 

DEBUG
GET dumpdb: Dumps output of the SQLite database to the console.
GET http://localhost:8080/dumpdb
***************DEBUG***************
5CEE889958A003E203838313 0 {Ready to create a 6 Warehouse Oracle TPC-C schema
in database VULPDB1 under user TPCC in tablespace TPCCTAB?} 5CEE889958A003E203838313 0 {Vuser 1:RUNNING} 5CEE889958A003E203838313 1 {Monitor Thread} 5CEE889958A003E203838313 1 {CREATING TPCC SCHEMA} 5CEE889958A003E203838313 0 {Vuser 2:RUNNING} 5CEE889958A003E203838313 2 {Worker Thread} 5CEE889958A003E203838313 2 {Waiting for Monitor Thread...} 5CEE889958A003E203838313 1 {Error: ORA-12541: TNS:no listener} 5CEE889958A003E203838313 0 {Vuser 1:FINISHED FAILED} 5CEE889958A003E203838313 0 {Vuser 3:RUNNING} 5CEE889958A003E203838313 3 {Worker Thread} 5CEE889958A003E203838313 3 {Waiting for Monitor Thread...} 5CEE889958A003E203838313 0 {Vuser 4:RUNNING} 5CEE889958A003E203838313 4 {Worker Thread} 5CEE889958A003E203838313 4 {Waiting for Monitor Thread...} 5CEE889958A003E203838313 2 {Monitor failed to notify ready state} 5CEE889958A003E203838313 0 {Vuser 2:FINISHED SUCCESS} 5CEE889958A003E203838313 3 {Monitor failed to notify ready state} 5CEE889958A003E203838313 0 {Vuser 3:FINISHED SUCCESS} 5CEE889958A003E203838313 4 {Monitor failed to notify ready state} 5CEE889958A003E203838313 0 {Vuser 4:FINISHED SUCCESS} 5CEE889958A003E203838313 0 {ALL VIRTUAL USERS COMPLETE}
***************DEBUG***************

As an example the following script shows printing the output of print commands in both JSON and text format.

set UserDefaultDir [ file dirname [ info script ] ]
::tcl::tm::path add "$UserDefaultDir/modules"
package require rest
package require huddle
puts "TEST DIRECT PRINT COMMANDS"
puts "--------------------------------------------------------"
foreach i {db bm dict script vuconf vucreated vustatus datagen}  {
puts "Printing output for $i and converting JSON to text"
    set res [rest::get http://localhost:8080/$i "" ]
puts "JSON format"
puts $res
puts "TEXT format"
    set res [rest::format_json $res]
    puts $res
}
puts "--------------------------------------------------------"
puts "PRINT COMMANDS COMPLETE"
puts "--------------------------------------------------------"

Once the Web Service is running in another port, run the TCL shell as follows and run the script above, the output is shown as follows.

$ ./bin/tclsh8.6 
% source restchk.tcl
TEST DIRECT PRINT COMMANDS
--------------------------------------------------------
Printing output for db and converting JSON to text
JSON format
{
  "ora": "Oracle",
  "mssqls": "MSSQLServer",
  "db2": "Db2",
  "mysql": "MySQL",
  "pg": "PostgreSQL",
  "redis": "Redis"
}
TEXT format
ora Oracle mssqls MSSQLServer db2 Db2 mysql MySQL pg PostgreSQL redis Redis
Printing output for bm and converting JSON to text
JSON format
{"benchmark": "TPC-C"}
TEXT format
benchmark TPC-C
Printing output for dict and converting JSON to text
JSON format
{
  "connection": {
    "system_user": "system",
    "system_password": "manager",
    "instance": "oracle",
    "rac": "0"
  },
  "tpcc": {
    "count_ware": "1",
    "num_vu": "1",
    "tpcc_user": "tpcc",
    "tpcc_pass": "tpcc",
    "tpcc_def_tab": "tpcctab",
    "tpcc_ol_tab": "tpcctab",
    "tpcc_def_temp": "temp",
    "partition": "false",
    "hash_clusters": "false",
    "tpcc_tt_compat": "false",
    "total_iterations": "1000000",
    "raiseerror": "false",
    "keyandthink": "false",
    "checkpoint": "false",
    "ora_driver": "test",
    "rampup": "2",
    "duration": "5",
    "allwarehouse": "false",
    "timeprofile": "false"
  }
}
TEXT format
connection {system_user system system_password manager instance oracle rac 0} tpcc {count_ware 1 num_vu 1 tpcc_user tpcc tpcc_pass tpcc tpcc_def_tab tpcctab tpcc_ol_tab tpcctab tpcc_def_temp temp partition false hash_clusters false tpcc_tt_compat false total_iterations 1000000 raiseerror false keyandthink false checkpoint false ora_driver test rampup 2 duration 5 allwarehouse false timeprofile false}
Printing output for script and converting JSON to text
JSON format
{"error": {"message": "No Script loaded: load with loadscript"}}
TEXT format
error {message {No Script loaded: load with loadscript}}
Printing output for vuconf and converting JSON to text
JSON format
{
  "Virtual Users": "1",
  "User Delay(ms)": "500",
  "Repeat Delay(ms)": "500",
  "Iterations": "1",
  "Show Output": "1",
  "Log Output": "0",
  "Unique Log Name": "0",
  "No Log Buffer": "0",
  "Log Timestamps": "0"
}
TEXT format
{Virtual Users} 1 {User Delay(ms)} 500 {Repeat Delay(ms)} 500 Iterations 1 {Show Output} 1 {Log Output} 0 {Unique Log Name} 0 {No Log Buffer} 0 {Log Timestamps} 0
Printing output for vucreated and converting JSON to text
JSON format
{"Virtual Users created": "0"}
TEXT format
{Virtual Users created} 0
Printing output for vustatus and converting JSON to text
JSON format
{"Virtual User status": "No Virtual Users found"}
TEXT format
{Virtual User status} {No Virtual Users found}
Printing output for datagen and converting JSON to text
JSON format
{
  "schema": "TPC-C",
  "database": "Oracle",
  "warehouses": "1",
  "vu": "1",
  "directory": "\/tmp\""
}
TEXT format
schema TPC-C database Oracle warehouses 1 vu 1 directory /tmp\"
--------------------------------------------------------
PRINT COMMANDS COMPLETE
--------------------------------------------------------
%
