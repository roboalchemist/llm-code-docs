# Source: https://www.hammerdb.com/docs4.0/ch02s03.html

Title: 3. Run a Timed Workload

URL Source: https://www.hammerdb.com/docs4.0/ch02s03.html

Markdown Content:
the Test script is to check connectivity and diagnose performance and configuration errors. It is the Timed Workload that should be used to conduct performance tests. Under Driver Options select Timed Driver Script and click OK, the Timed Driver Script is now loaded.

**Figure 2.11.Driver Options**

![Image 1: Driver Options](https://www.hammerdb.com/docs4.0/resources/ch2-11.PNG)

Verify the Virtual User Options.

**Figure 2.12.Virtual Users**

![Image 2: Virtual Users](https://www.hammerdb.com/docs4.0/resources/ch2-12.PNG)

Click create Virtual User and observe that for Timed workloads an additional Virtual User has been created. This Virtual User does not run the workload but provides the timing and monitoring functionality.

**Figure 2.13.Virtual User and Monitor Created**

![Image 3: Virtual User and Monitor Created](https://www.hammerdb.com/docs4.0/resources/ch2-13.PNG)

Click Run, the workload will begin but this time without the Virtual User output being written to the screen. The Monitor Virtual User will provide information on Timing as the workload progresses.

**Figure 2.14.Timed Workload Running**

![Image 4: Timed Workload Running](https://www.hammerdb.com/docs4.0/resources/ch2-14.PNG)

On completion observe that the Monitor Virtual User reports a value for NOPM and a value for TPM. NOPM stands for New Orders per Minute and is extracted from the database schema and is therefore database independent meaning it is valid to compare between different databases. TPM is the transactions per minute and is a unique value to how each database processes transactions. NOPM is the key performance metric however TPM is the metric that correlates with database performance tools measurement of transactions per second or minute and can therefore be used by database engineers for deeper analysis of database performance.

**Figure 2.15.Test Result**

![Image 5: Test Result](https://www.hammerdb.com/docs4.0/resources/ch2-15.PNG)
