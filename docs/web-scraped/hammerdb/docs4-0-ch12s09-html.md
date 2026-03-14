# Source: https://www.hammerdb.com/docs4.0/ch12s09.html

Title: 9. Run a Power Test

URL Source: https://www.hammerdb.com/docs4.0/ch12s09.html

Markdown Content:
Many test environments are sufficient with running single Virtual User tests. With available parallel and column store configurations this test is sufficient to stress an entire system. Nevertheless a component of the TPROC-H test is the refresh function and the refresh function should be run either side of the Power Test. To enable this functionality HammerDB has a special power test mode, whereby if refresh_on is set to true as shown and only one virtual user is configured then HammerDB will run a Power Test. Note that once you selected refresh_on for a single Virtual User in Power Test Mode the value of update_sets will be set to 1 and the value of trickle_refresh set to 0 and the value of REFRESH_VERBOSE set to false, all these values will be set automatically to ensure optimal running of the Power Test.

**Figure 12.25.Power Test Options**

![Image 1: Power Test Options](https://www.hammerdb.com/docs4.0/resources/ch13-26.PNG)

When loaded note that the refresh_on option is set in the script. You should also ensure that the scale factor setting matches the setting for your schema.

**Figure 12.26.TPROC-H refresh on**

![Image 2: TPROC-H refresh on](https://www.hammerdb.com/docs4.0/resources/ch13-28.PNG)

With these settings run the Virtual User and it will run a New Sales Refresh, single Virtual User Query Set and Old Sales Refresh in order as required by a Power Test.

**Figure 12.27.Power Test**

![Image 3: Power Test](https://www.hammerdb.com/docs4.0/resources/ch13-27.PNG)

HammerDB will report when the Power Test is complete.

**Figure 12.28.Power Test Complete**

![Image 4: Power Test Complete](https://www.hammerdb.com/docs4.0/resources/ch13-29.PNG)

and you can collect the refresh and query times from the log.

Hammerdb Log @ Fri Oct 23 15:41:39 BST 2020
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
Vuser 1:New Sales refresh
Vuser 1:New Sales refresh complete in 54.15 seconds
Vuser 1:Completed 1 update set(s)
Vuser 1:Executing Query 14 (1 of 22)
Vuser 1:query 14 completed in 7.868 seconds
Vuser 1:Executing Query 2 (2 of 22)
Vuser 1:query 2 completed in 0.334 seconds
Vuser 1:Executing Query 9 (3 of 22)
Vuser 1:query 9 completed in 21.87 seconds
Vuser 1:Executing Query 20 (4 of 22)
Vuser 1:query 20 completed in 0.816 seconds
Vuser 1:Executing Query 6 (5 of 22)
Vuser 1:query 6 completed in 0.926 seconds
Vuser 1:Executing Query 17 (6 of 22)
Vuser 1:query 17 completed in 1.299 seconds
Vuser 1:Executing Query 18 (7 of 22)
Vuser 1:query 18 completed in 19.289 seconds
Vuser 1:Executing Query 8 (8 of 22)
Vuser 1:query 8 completed in 4.232 seconds
Vuser 1:Executing Query 21 (9 of 22)
Vuser 1:query 21 completed in 59.815 seconds
Vuser 1:Executing Query 13 (10 of 22)
Vuser 1:query 13 completed in 13.889 seconds
Vuser 1:Executing Query 3 (11 of 22)
Vuser 1:query 3 completed in 5.773 seconds
Vuser 1:Executing Query 22 (12 of 22)
Vuser 1:query 22 completed in 0.928 seconds
Vuser 1:Executing Query 16 (13 of 22)
Vuser 1:query 16 completed in 0.792 seconds
Vuser 1:Executing Query 4 (14 of 22)
Vuser 1:query 4 completed in 19.258 seconds
Vuser 1:Executing Query 11 (15 of 22)
Vuser 1:query 11 completed in 0.497 seconds
Vuser 1:Executing Query 15 (16 of 22)
Vuser 1:query 15 completed in 9.436 seconds
Vuser 1:Executing Query 1 (17 of 22)
Vuser 1:query 1 completed in 16.067 seconds
Vuser 1:Executing Query 10 (18 of 22)
Vuser 1:query 10 completed in 22.284 seconds
Vuser 1:Executing Query 19 (19 of 22)
Vuser 1:query 19 completed in 19.648 seconds
Vuser 1:Executing Query 5 (20 of 22)
Vuser 1:query 5 completed in 18.98 seconds
Vuser 1:Executing Query 7 (21 of 22)
Vuser 1:query 7 completed in 6.089 seconds
Vuser 1:Executing Query 12 (22 of 22)
Vuser 1:query 12 completed in 12.512 seconds
Vuser 1:Completed 1 query set(s) in 263 seconds
Vuser 1:Geometric mean of query times returning rows (22) is 5.43452
Vuser 1:Old Sales refresh
Vuser 1:Old Sales refresh complete in 16.016 seconds
Vuser 1:Completed 1 update set(s)
Be aware that some databases are considerably better at running the refresh functions than others and also that once the power test has been run it is necessary to restore the database from backup before running the refresh function again. If you fail to do so you will receive a constraint violation error. This is expected behaviour.

Error in Virtual User 1: 23000 2627 {[Microsoft][ODBC Driver 13 for SQL Server][SQL Server]
Violation of PRIMARY KEY constraint 'orders_pk'. 
Cannot insert duplicate key in object 'dbo.orders'. The duplicate key value is (9).}
