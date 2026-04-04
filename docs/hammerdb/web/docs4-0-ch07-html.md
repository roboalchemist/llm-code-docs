# Source: https://www.hammerdb.com/docs4.0/ch07.html

Title: Chapter 7. CPU and Database Metrics

URL Source: https://www.hammerdb.com/docs4.0/ch07.html

Markdown Content:
By default HammerDB metrics displays the CPU utilisation per core across the target system. HammerDB has also introduced a database metrics display initially for the Oracle Database. HammerDB Metrics uses an agent and display configuration meaning that the agent must be installed on the SUT. This can be accomplished by installing HammerDB on the SUT as well as the server. On Linux the sysstat package must be pre-installed where the agent is running.

$ mpstat -V
sysstat version 11.5.7
(C) Sebastien Godard (sysstat <at> orange.fr
On Windows a version of mpstat is included with HammerDB.
