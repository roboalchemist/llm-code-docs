# Source: https://www.hammerdb.com/docs4.0/ch06s06.html

Title: 6. Running the Transaction Counter

URL Source: https://www.hammerdb.com/docs4.0/ch06s06.html

Markdown Content:
During a test, select the start transaction counter button.

**Figure 6.7.Start Transaction Counter**

![Image 1: Start Transaction Counter](https://www.hammerdb.com/docs4.0/resources/ch6-8.PNG)

On starting the transaction counter will begin sampling the transaction data.

**Figure 6.8.Transaction Counter Starting**

![Image 2: Transaction Counter Starting](https://www.hammerdb.com/docs4.0/resources/ch6-9.PNG)

The transaction counter will be displayed and continually sample and display the transaction rate during the test. It is important to note that the transaction rate is sampled with the SQL detailed above for the database selected and therefore all transactions on the database are sampled whether from HammerDB or another application running at the same time. Similarly if 2 or more instances of HammerDB are run against the same database at the same time, the cumulative transaction is sampled.

**Figure 6.9.Transaction Counter Running**

![Image 3: Transaction Counter Running](https://www.hammerdb.com/docs4.0/resources/ch6-10.PNG)

While active the Transaction Counter Window can be dragged out of the main HammerDB display to be displayed in an standalone window by selecting and dragging the notebook tab. To return to the main display close the window and it will be re-embedded in the main interface.

**Figure 6.10.Transaction Counter standalone.**

![Image 4: Transaction Counter standalone.](https://www.hammerdb.com/docs4.0/resources/ch6-11.PNG)
