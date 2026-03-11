# Source: https://www.hammerdb.com/docs4.0/ch10s03.html

Title: 3. Retrieving Output

URL Source: https://www.hammerdb.com/docs4.0/ch10s03.html

Markdown Content:
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
