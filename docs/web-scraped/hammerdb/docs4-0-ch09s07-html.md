# Source: https://www.hammerdb.com/docs4.0/ch09s07.html

Title: 7. Run the workload

URL Source: https://www.hammerdb.com/docs4.0/ch09s07.html

Markdown Content:
To begin the workload type vurun.

hammerdb>vurun
Vuser 1:RUNNING
Vuser 1:Beginning rampup time of 1 minutes
Vuser 2:RUNNING
Vuser 2:Processing 1000000 transactions with output suppressed...
Vuser 3:RUNNING
Vuser 3:Processing 1000000 transactions with output suppressed...
Vuser 4:RUNNING
Vuser 4:Processing 1000000 transactions with output suppressed...
Vuser 5:RUNNING
Vuser 5:Processing 1000000 transactions with output suppressed...
The vustatus command can confirm the change in status.

hammerdb>vustatus

1 = RUNNING
2 = RUNNING
3 = RUNNING
4 = RUNNING
5 = RUNNING
The vucomplete command returns a boolean value to confirm whether an entire workload is still running or finished.

hammerdb>vucomplete
false
The test runs as per the configuration and reports the result at the end and the Virtual User status. Note that when complete the vucomplete command can confirm this.

hammerdb>Vuser 1:Rampup 1 minutes complete ...
Vuser 1:Rampup complete, Taking start Transaction Count.
Vuser 1:Timing test period of 3 in minutes
Vuser 1:1 ...,
Vuser 1:2 ...,
Vuser 1:3 ...,
Vuser 1:Test complete, Taking end Transaction Count.
Vuser 1:4 Active Virtual Users configured
Vuser 1:TEST RESULT : System achieved 101005 NOPM from 232149 SQL Server TPM
Vuser 1:FINISHED SUCCESS
Vuser 5:FINISHED SUCCESS
Vuser 4:FINISHED SUCCESS
Vuser 3:FINISHED SUCCESS
Vuser 2:FINISHED SUCCESS
ALL VIRTUAL USERS COMPLETE

hammerdb>vucomplete
true
hammerdb>
To complete the test type vudestroy.

hammerdb>vudestroy
Destroying Virtual Users
Virtual Users Destroyed

and clear the script.

hammerdb>clearscript
Script cleared
