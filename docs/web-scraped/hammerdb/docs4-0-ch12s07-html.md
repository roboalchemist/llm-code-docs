# Source: https://www.hammerdb.com/docs4.0/ch12s07.html

Title: 7. Configure Virtual Users

URL Source: https://www.hammerdb.com/docs4.0/ch12s07.html

Markdown Content:
| Option | Description |
| --- | --- |
| Virtual Users | The number of Virtual Users to create. Note that when running a Timed Workload HammerDB will automatically create an additional Virtual User to monitor the workload. |
| User Delay(ms) | User Delay(ms) defines the time to wait a Virtual User will wait behind the previous Virtual User before starting its test, this is to prevent a login storm with all Virtual Users attempting to login at the same time. |
| Repeat Delay(ms) | Repeat Delay(ms) is the time that each Virtual User will wait before running its next Iteration of the Driver Script. For TPROC-H this is an external loop before running another query set, however should not be more than 1 when the refresh function is enabled. |
| Iterations | Iterations is the number of times that the Driver Script is run in its entirety. |
| Show Output | Show Output will report Virtual User Output to the Virtual User Output Window, For TPROC-H tests this should be enabled. |
| Log Output to Temp | When enabled this appends all Virtual User Output to a text file in an available temp directory named hammerdb.log |
| Use Unique Log Name | Use a unique identifier for the Log Name. |
| No Log Buffer | By default text log output is buffered in memory before being written, this option writes the log output immediately. |
| Log Timestamps | Add an additional line of output with a timestamp every time that the log is written to. |
