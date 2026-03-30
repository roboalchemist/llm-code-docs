# Source: https://www.hammerdb.com/docs4.0/ch05s02.html

Title: 2. Autopilot Troubleshooting

URL Source: https://www.hammerdb.com/docs4.0/ch05s02.html

Markdown Content:
The most Frequent Autopilot Configuration Error is caused by configuring the Autopilot Time Interval to be less than the combined rampup and duration time of the test that is running. When viewed from the concept of a "Virtual DBA" this User has been instructed to press the Stop button before the test has ended, consequently a warning is produced and no output results are reported. To resolve this issue ensure that the time interval is set long enough to allow the configured tests to complete inside this interval.

**Figure 5.7.Autopilot Error**

![Image 1: Autopilot Error](https://www.hammerdb.com/docs4.0/resources/ch5-7.PNG)
