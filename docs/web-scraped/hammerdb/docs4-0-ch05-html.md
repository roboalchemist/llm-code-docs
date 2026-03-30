# Source: https://www.hammerdb.com/docs4.0/ch05.html

Title: Chapter 5. Autopilot for Automated Testing

URL Source: https://www.hammerdb.com/docs4.0/ch05.html

Markdown Content:
To automate this process of repeated tests HammerDB provides the autopilot feature that enables you to configure a single test to be repeated by a different numbers of virtual users a number of times. Conceptually autopilot is best understood as having instructed a virtual DBA to manually repeat the test you have configured a number of times at a pre-determined time interval. That virtual DBA will then run the tests by ‘virtually’ pressing exactly the same buttons on the HammerDB interface that you would press as if running the test manually yourself. It is important to understand this concept as the most frequent user errors in using autopilot are as a result of not following this approach. Before running autopilot you should ensure that you have run a number of tests manually and your system is in an optimal configuration for running tests up to your planned maximum Virtual User count. For example you should enable enough space to schema growth throughout all of the tests you plan to run.
