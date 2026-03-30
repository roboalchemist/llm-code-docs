# Source: https://www.hammerdb.com/docs4.0/ch06s04.html

Title: 4. MySQL Transaction Counter

URL Source: https://www.hammerdb.com/docs4.0/ch06s04.html

Markdown Content:
For MySQL the connection parameters are the same as the schema options. The refresh rate determines the sampling interval.

**Figure 6.5.MySQL TX Counter Options**

![Image 1: MySQL TX Counter Options](https://www.hammerdb.com/docs4.0/resources/ch6-5.PNG)

The following SQL is used to sample the transaction rate.

show global status where Variable_name = 'Com_commit' or Variable_name =  'Com_rollback'
Note that Com_commit is used instead of the handler_commit value used in previous releases of HammerDB as a result of MySQL Bug #52453 handler_commit is incremented for InnoDB SELECT queries.
