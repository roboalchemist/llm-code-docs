# Source: https://www.hammerdb.com/docs4.0/ch06s03.html

Title: 3. Db2 Transaction Counter

URL Source: https://www.hammerdb.com/docs4.0/ch06s03.html

Markdown Content:
For Db2 the connection parameters are the same as the schema options. The refresh rate determines the sampling interval.

**Figure 6.4.Db2 TX Counter Options**

![Image 1: Db2 TX Counter Options](https://www.hammerdb.com/docs4.0/resources/ch6-4.PNG)

The following SQL is used to sample the transaction rate.

select total_app_commits + total_app_rollbacks from sysibmadm.mon_db_summary
