# Source: https://www.hammerdb.com/docs4.0/ch09s06.html

Title: 6. Configure Virtual Users

URL Source: https://www.hammerdb.com/docs4.0/ch09s06.html

Markdown Content:
With the schema built and the driver script loaded the next step in the workflow is to configure the Virtual Users.

The print command can be used to show the number of Virtual Users currently created. As the Virtual Users were destroyed after the build it is reported that none are created.

hammerdb>print vucreated
0 Virtual Users created
The vuset command is used to configure the Virtual User options, for example the number of Virtual Users to create.

hammerdb>vuset vu 4
and to enable logging.

hammerdb>vuset logtotemp 1
print vuconf confirms the configuration.

hammerdb>print vuconf
Virtual Users = 4
User Delay(ms) = 500
Repeat Delay(ms) = 500
Iterations = 1
Show Output = 1
Log Output = 1
Unique Log Name = 0
No Log Buffer = 0
Log Timestamps = 0

Then run vucreate to create the Virtual Users who will be created in an idle state not yet running. Note that when a timed test is selected a Monitor Virtual User is also created as is the case with the graphical interface.

hammerdb>vucreate
Vuser 1 created MONITOR - WAIT IDLE
Vuser 2 created - WAIT IDLE
Vuser 3 created - WAIT IDLE
Vuser 4 created - WAIT IDLE
Vuser 5 created - WAIT IDLE
Logging activated
to C:/Users/Steve/AppData/Local/Temp/hammerdb.log
5 Virtual Users Created with Monitor VU
vustatus can confirm this status.

hammerdb>vustatus
1 = WAIT IDLE
2 = WAIT IDLE
3 = WAIT IDLE
4 = WAIT IDLE
5 = WAIT IDLE
