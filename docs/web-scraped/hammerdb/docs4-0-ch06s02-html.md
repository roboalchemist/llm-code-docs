# Source: https://www.hammerdb.com/docs4.0/ch06s02.html

Title: 2. SQL Server Transaction Counter

URL Source: https://www.hammerdb.com/docs4.0/ch06s02.html

Markdown Content:
For SQL Server the connection parameters are the same as the schema options. The refresh rate determines the sampling interval.

**Figure 6.3.SQL Server TX Counter Options**

![Image 1: SQL Server TX Counter Options](https://www.hammerdb.com/docs4.0/resources/ch6-3.PNG)

The following SQL is used to sample the transaction rate displaying the same value as can be seen in the Activity Monitor in SSMS.

select cntr_value from sys.dm_os_performance_counters where counter_name = 'Batch Requests/sec'
