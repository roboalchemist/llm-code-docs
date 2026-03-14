# Source: https://www.hammerdb.com/docs4.0/ch04s10.html

Title: 10. Create and Run Virtual Users

URL Source: https://www.hammerdb.com/docs4.0/ch04s10.html

Markdown Content:
Double-click Create in the tree-view. The Virtual Users will be created and waiting in an idle status ready to run the Driver Script in the Script Editor Window. If you press Run instead it will both Create and Run the Virtual Users. If you have selected a Timed Workload the additional Virtual User created will be shown as a monitor.

**Figure 4.34.Virtual Users Create**

![Image 1: Virtual Users Create](https://www.hammerdb.com/docs4.0/resources/ch4-19.PNG)

Double-click on Run and the Virtual Users will login to the target database and begin running their workload.

**Figure 4.35.Virtual Users Running**

![Image 2: Virtual Users Running](https://www.hammerdb.com/docs4.0/resources/ch4-20.PNG)

When complete the Monitor Virtual User will report the Test Result, refer to Chapter for the configuration of how the NOPM and TPM values are reported. If logging has been selected these values will also be reported in the log. Where supported additional database side server report information will also be reported.

**Figure 4.36.Virtual Users Complete**

![Image 3: Virtual Users Complete](https://www.hammerdb.com/docs4.0/resources/ch4-21.PNG)

you may choose to run all of your performance tests manually in this way, however generating a performance profile is the key to successful database performance analysis requiring the running of a sequence of tests. Consequently HammerDB enables a way to automate the running of this sequence of tests with the Autopilot Feature.
