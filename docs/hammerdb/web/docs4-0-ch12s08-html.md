# Source: https://www.hammerdb.com/docs4.0/ch12s08.html

Title: 8. Run a Single Virtual User Test

URL Source: https://www.hammerdb.com/docs4.0/ch12s08.html

Markdown Content:
Check that your scale_factor in the Driver Script is the same as the schema you are running the test against. You can also set the Degree of Parallelism/MAXDOP directly in the script.

**Figure 12.22.Modified Options**

![Image 1: Modified Options](https://www.hammerdb.com/docs4.0/resources/ch13-24.PNG)

Double-click on create Virtual User followed by Run. This will proceed to run a single Virtual User with one Query Set.

**Figure 12.23.Run a single Virtual User Test**

![Image 2: Run a single Virtual User Test](https://www.hammerdb.com/docs4.0/resources/ch13-23.PNG)

When complete the Virtual User will show the query set time as well as the geometric mean of queries that returned rows including a count of those queries that returned rows.

**Figure 12.24.Single Virtual User Complete**

![Image 3: Single Virtual User Complete](https://www.hammerdb.com/docs4.0/resources/ch13-25.PNG)

And the log will show the Query times. Note how the queries are run in a pre-determined random order.

Hammerdb Log @ Fri Oct 23 15:31:59 BST 2020
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
Vuser 1:Executing Query 14 (1 of 22)
Vuser 1:query 14 completed in 7.301 seconds
Vuser 1:Executing Query 2 (2 of 22)
Vuser 1:query 2 completed in 0.952 seconds
Vuser 1:Executing Query 9 (3 of 22)
Vuser 1:query 9 completed in 24.457 seconds
Vuser 1:Executing Query 20 (4 of 22)
Vuser 1:query 20 completed in 1.249 seconds
Vuser 1:Executing Query 6 (5 of 22)
Vuser 1:query 6 completed in 1.978 seconds
Vuser 1:Executing Query 17 (6 of 22)
Vuser 1:query 17 completed in 1.079 seconds
Vuser 1:Executing Query 18 (7 of 22)
Vuser 1:query 18 completed in 19.45 seconds
Vuser 1:Executing Query 8 (8 of 22)
Vuser 1:query 8 completed in 11.962 seconds
Vuser 1:Executing Query 21 (9 of 22)
Vuser 1:query 21 completed in 58.399 seconds
Vuser 1:Executing Query 13 (10 of 22)
Vuser 1:query 13 completed in 17.475 seconds
Vuser 1:Executing Query 3 (11 of 22)
Vuser 1:query 3 completed in 4.463 seconds
Vuser 1:Executing Query 22 (12 of 22)
Vuser 1:query 22 completed in 2.39 seconds
Vuser 1:Executing Query 16 (13 of 22)
Vuser 1:query 16 completed in 1.152 seconds
Vuser 1:Executing Query 4 (14 of 22)
Vuser 1:query 4 completed in 19.246 seconds
Vuser 1:Executing Query 11 (15 of 22)
Vuser 1:query 11 completed in 2.593 seconds
Vuser 1:Executing Query 15 (16 of 22)
Vuser 1:query 15 completed in 2.253 seconds
Vuser 1:Executing Query 1 (17 of 22)
Vuser 1:query 1 completed in 19.213 seconds
Vuser 1:Executing Query 10 (18 of 22)
Vuser 1:query 10 completed in 21.596 seconds
Vuser 1:Executing Query 19 (19 of 22)
Vuser 1:query 19 completed in 20.239 seconds
Vuser 1:Executing Query 5 (20 of 22)
Vuser 1:query 5 completed in 19.305 seconds
Vuser 1:Executing Query 7 (21 of 22)
Vuser 1:query 7 completed in 6.117 seconds
Vuser 1:Executing Query 12 (22 of 22)
Vuser 1:query 12 completed in 15.223 seconds
Vuser 1:Completed 1 query set(s) in 278 seconds
Vuser 1:Geometric mean of query times returning rows (22) is 6.82555

### [](https://www.hammerdb.com/docs4.0/ch12s08.html)8.1.Changing the Query Order

For a single virtual User test you may wish to change the query order. This query order is predetermined in the common modules. However you can redefine this function by copying and pasting the ordered_set function and modifying the order. The following example is sufficient for the single Virtual User

rename ordered_set ordered_set_orig
proc ordered_set { myposition } {
if { $myposition > 40 } { set myposition [ expr $myposition % 40 ] }
        set o_s(0)  { 14 2 9 20 6 17 18 8 21 13 3 22 16 4 11 15 1 10 19 5 7 12 }
        return $o_s($myposition)
}
and then you can change the query order as follows:

set o_s(0)  { 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 }
If your database has issues with particular queries being long running you can also remove queries this way that you do not wish to run.
