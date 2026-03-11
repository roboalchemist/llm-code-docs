# Source: https://www.hammerdb.com/docs4.0/ch06s05.html

Title: 5. PostgreSQL Transaction Counter

URL Source: https://www.hammerdb.com/docs4.0/ch06s05.html

Markdown Content:
For PostgreSQL the connection parameters are the same as the schema options. The refresh rate determines the sampling interval.

**Figure 6.6.PostgreSQL TX Counter Options**

![Image 1: PostgreSQL TX Counter Options](https://www.hammerdb.com/docs4.0/resources/ch6-6.PNG)

The following SQL is used to sample the transaction rate.

select sum(xact_commit + xact_rollback) from pg_stat_database
