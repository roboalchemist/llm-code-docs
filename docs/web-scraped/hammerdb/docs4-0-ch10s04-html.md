# Source: https://www.hammerdb.com/docs4.0/ch10s04.html

Title: 4. Running Jobs

URL Source: https://www.hammerdb.com/docs4.0/ch10s04.html

Markdown Content:
The following script run in the same shows how this can be extended so that an external script can interact with the web service and run a build and then a test successively. Note that wait_to_complete procedures can properly sleep using the after command without activity and without affecting the progress of the jobs as the driving script is run in one interpreter and the web service in another.

set UserDefaultDir [ file dirname [ info script ] ]
::tcl::tm::path add "$UserDefaultDir/modules"
package require rest
package require huddle

proc wait_for_run_to_complete { runjob } {
global complete
set res [rest::get http://localhost:8080/vucomplete "" ]
set complete [ lindex [rest::format_json $res] 1]
if {!$complete} {
#sleep for 20 seconds and recheck
after 20000 
wait_for_run_to_complete $runjob
	} else {
set res [rest::get http://localhost:8080/vudestroy "" ]
puts "Test Complete"
set jobid [ lindex [ split [ lindex [ lindex [ lindex [rest::format_json $runjob ] 1 ] 1 ] 3 ] \= ] 1 ]
set res [rest::get http://localhost:8080/jobs?jobid=$jobid&result "" ]
puts "Test result: $res"
  }
}

proc wait_for_build_to_complete {} {
global complete
set res [rest::get http://localhost:8080/vucomplete "" ]
set complete [ lindex [rest::format_json $res] 1]
if {!$complete} {
#sleep for 20 seconds and recheck
after 20000 
wait_for_build_to_complete 
	} else {
set res [rest::get http://localhost:8080/vudestroy "" ]
puts "Build Complete"
set complete false
  }
}

proc run_test {} {
puts "Setting Db values"
set body { "db": "ora" }
    set res [ rest::post http://localhost:8080/dbset $body ] 
set body { "bm": "TPC-C" }
    set res [ rest::post http://localhost:8080/dbset $body ] 
puts "Setting Vusers"
set body { "vu": "5" }
    set res [ rest::post http://localhost:8080/vuset $body ] 
puts $res
puts "Setting Dict Values"
set body { "dict": "connection", "key": "system_password", "value": "oracle" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "connection", "key": "instance", "value": "VULPDB1" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "tpcc_pass", "value": "oracle" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "ora_driver", "value": "timed" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "rampup", "value": "1" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "duration", "value": "2" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "checkpoint", "value": "false" }
    set res [rest::post http://localhost:8080/diset $body ]
puts "Config"
set res [rest::get http://localhost:8080/dict "" ]
puts $res
puts "Clearscript"
    set res [rest::post http://localhost:8080/clearscript "" ]
puts $res
puts "Loadscript"
    set res [rest::post http://localhost:8080/loadscript "" ]
puts $res
puts "Create VU"
 set res [rest::post http://localhost:8080/vucreate "" ]
puts $res
puts "Run VU"
 set res [rest::post http://localhost:8080/vurun "" ]
puts $res
wait_for_run_to_complete $res
}

proc run_build {} {
puts "running build"
set body { "db": "ora" }
    set res [ rest::post http://localhost:8080/dbset $body ] 
set body { "bm": "TPC-C" }
    set res [ rest::post http://localhost:8080/dbset $body ] 
puts "Setting Dict Values"
set body { "dict": "connection", "key": "system_password", "value": "oracle" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "connection", "key": "instance", "value": "VULPDB1" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "count_ware", "value": "10" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "tpcc_pass", "value": "oracle" }
    set res [rest::post http://localhost:8080/diset $body ]
set body { "dict": "tpcc", "key": "num_vu", "value": "5" }
    set res [rest::post http://localhost:8080/diset $body ]
puts "Starting Schema Build"
    set res [rest::post http://localhost:8080/buildschema "" ]
puts $res
wait_for_build_to_complete
	}
#Run build followed by run test
run_build
run_test

An example of the output running the script is shown.

./bin/tclsh8.6 
% source buildrun_tpcc.tcl
running build
Setting Dict Values
Starting Schema Build
{"success": {"message": "Building 10 Warehouses with 6 Virtual Users, 5 active + 1 Monitor VU(dict value num_vu is set to 5): JOBID=5D1F4CA858CE03E213431323"}}
Build Complete
Setting Db values
Setting Vusers
{"success": {"message": "Virtual users set to 5"}}
Setting Dict Values
Config
{
  "connection": {
    "system_user": "system",
    "system_password": "oracle",
    "instance": "VULPDB1",
    "rac": "0"
  },
  "tpcc": {
    "count_ware": "10",
    "num_vu": "5",
    "tpcc_user": "tpcc",
    "tpcc_pass": "oracle",
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
    "ora_driver": "timed",
    "rampup": "1",
    "duration": "2",
    "allwarehouse": "false",
    "timeprofile": "false"
  }
}
Clearscript
{"success": {"message": "Script cleared"}}
Loadscript
{"success": {"message": "script loaded"}}
Create VU
{"success": {"message": "6 Virtual Users Created with Monitor VU"}}
Run VU
{"success": {"message": "Running Virtual Users: JOBID=5D1F4FF558CE03E223730313"}}
Test Complete
Test result: [
  "5D1F4FF558CE03E223730313",
  "TEST RESULT : System achieved 0 Oracle TPM at 27975 NOPM"
]
%
