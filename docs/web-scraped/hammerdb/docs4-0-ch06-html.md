# Source: https://www.hammerdb.com/docs4.0/ch06.html

Title: Chapter 6. Transactions

URL Source: https://www.hammerdb.com/docs4.0/ch06.html

Markdown Content:
HammerDB includes a Transaction Counter that logs into the target database and samples the transaction rate displaying it in graph format to view the TPM of a test in real time. Note that the TPM value is displayed as opposed to the NOPM value as TPM is selected from a database in-memory table and therefore sampling does not impact the test being measured. NOPM on the other hand is sampled from the schema itself and is therefore only measured at the start and end of the test to minimize the impact of testing upon performance. To configure the Transaction Counter select the Transactions tree-view. If Virtual Users are running the Transaction Counter Options can be selected from the menu.

**Figure 6.1.Transaction Counter Options**

![Image 1: Transaction Counter Options](https://www.hammerdb.com/docs4.0/resources/ch6-1.PNG)
