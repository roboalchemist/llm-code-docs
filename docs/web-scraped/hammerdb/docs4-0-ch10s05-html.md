# Source: https://www.hammerdb.com/docs4.0/ch10s05.html

Title: 5. Query Job Output

URL Source: https://www.hammerdb.com/docs4.0/ch10s05.html

Markdown Content:
Note that no output is seen directly in the script and no output recorded to a logfile. Instead the output is stored as a job by the web service. For example the following script would retrieve the output for the run job.

set UserDefaultDir [ file dirname [ info script ] ]
::tcl::tm::path add "$UserDefaultDir/modules"
package require rest
package require huddle
    set res [rest::get http://localhost:8080/jobs?jobid=5D1F4FF558CE03E223730313 "" ]
puts "JSON format"
puts $res

With the output as follows.

% source joboutput.tcl
JSON format
[
  "0",
  "Vuser 1:RUNNING",
  "1",
  "Beginning rampup time of 1 minutes",
  "0",
  "Vuser 2:RUNNING",
  "2",
  "Processing 1000000 transactions with output suppressed...",
  "0",
  "Vuser 3:RUNNING",
  "3",
  "Processing 1000000 transactions with output suppressed...",
  "0",
  "Vuser 4:RUNNING",
  "4",
  "Processing 1000000 transactions with output suppressed...",
  "0",
  "Vuser 5:RUNNING",
  "5",
  "Processing 1000000 transactions with output suppressed...",
  "0",
  "Vuser 6:RUNNING",
  "6",
  "Processing 1000000 transactions with output suppressed...",
  "1",
  "Rampup 1 minutes complete ...",
  "1",
  "Rampup complete, Taking start AWR snapshot.",
  "1",
  "Start Snapshot 298 taken at 05 JUL 2019 14:20 of instance VULCDB1 (1) of database VULCDB1 (1846545596)",
  "1",
  "Timing test period of 2 in minutes",
  "1",
  "1  ...,",
  "1",
  "2  ...,",
  "1",
  "Test complete, Taking end AWR snapshot.",
  "1",
  "End Snapshot 298 taken at 05 JUL 2019 14:20 of instance VULCDB1 (1) of database VULCDB1 (1846545596)",
  "1",
  "Test complete: view report from SNAPID  298 to 298",
  "1",
  "5 Active Virtual Users configured",
  "1",
  "TEST RESULT : System achieved 0 Oracle TPM at 27975 NOPM",
  "0",
  "Vuser 2:FINISHED SUCCESS",
  "0",
  "Vuser 1:FINISHED SUCCESS",
  "0",
  "Vuser 6:FINISHED SUCCESS",
  "0",
  "Vuser 5:FINISHED SUCCESS",
  "0",
  "Vuser 3:FINISHED SUCCESS",
  "0",
  "Vuser 4:FINISHED SUCCESS",
  "0",
  "ALL VIRTUAL USERS COMPLETE"
]

The dumpdb command can be used to dump all of the SQLite database to the web service console for debugging and the killws command cause the web service terminate.
