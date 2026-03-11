# Source: https://www.hammerdb.com/docs4.0/ch05s01.html

Title: 1. Configure and Run Autopilot

URL Source: https://www.hammerdb.com/docs4.0/ch05s01.html

Markdown Content:
| Option | Description |
| --- | --- |
| Autopilot Disabled/Autopilot Enabled | This Autopilot Disabled/Autopilot Enabled Radio buttons give you the option to select whether the Autopilot button is enabled on the main window. |
| Minutes per Test in Virtual User Sequence | The minutes for test duration defines the time interval between which your virtual DBA will create the Virtual Users, stop the test and create the next Virtual Users in the sequence. You should configure this value in relation to the Minutes for Ramup Time and Minutes for Test Duration given in the Timed Test options. For example if the values in the test script are 2 and 5 minutes respectively then 10 minutes for the Autopilot Options is a good value to allow the test to complete before the next test in the sequence is run. If the test overruns the time interval and the Virtual Users are still running the sequence will wait for the Virtual Users to complete before proceeding however note any pending output will be discarded and therefore for example if the TPM and NOPM values have not been reported by the time the test is stopped they will not be reported at all. |
| Virtual User Sequence (Space Separated Values) | The Virtual User Sequence defines the number of Virtual Users to be configured in order for a sequence of tests separated by the Minutes for Test Duration. Note that for a Timed workload the Monitor Virtual User will be added and therefore the sequence defines the number of active worker Virtual Users. Therefore in this example the actual users running the workload will be 1, 2, 4, 8, 12, 16, 20 and 24 however and additional one will be created. |
| Virtual User Options | These values are exactly the same as set when defining the Virtual User Options, you should ensure that Output is enabled and configure preferred logging options. |
