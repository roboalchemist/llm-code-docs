# Source: https://www.hammerdb.com/docs4.0/ch08.html

Title: Chapter 8. Remote Primary and Replica Modes

URL Source: https://www.hammerdb.com/docs4.0/ch08.html

Markdown Content:
HammerDB allows for multiple instances of the HammerDB program to run in Primary and Replica modes. Running with multiple modes enables the additional instances to be controlled by a single master instance either on the same load testing server or across the network. This functionality can be particularly applicable when testing Virtualized environments and the desire is to test multiple databases running in virtualized guests at the same time. Similarly this functionality is useful for clustered databases with multiple instances such as Oracle Real Application Clusters and wishing to partition a load precisely across servers. HammerDB Remote Modes are entirely operating system independent and therefore an instance of HammerDB running on Windows can be Primary to one or more instances running on Linux and vice versa. Additionally there is no requirement for the workload to be the same and therefore it would be possible to connect multiple instances of HammerDB running on Windows and Linux simultaneously testing SQL Server, Oracle, MySQL and PostrgreSQL workloads in a virtualized environment. In the bottom right hand corner of the interface the status bar shows the mode that HammerDB is running in. By default this will be Local Mode.

**Figure 8.1.Mode**

![Image 1: Mode](https://www.hammerdb.com/docs4.0/resources/ch11-1.PNG)
