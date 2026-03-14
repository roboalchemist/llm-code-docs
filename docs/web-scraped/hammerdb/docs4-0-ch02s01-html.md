# Source: https://www.hammerdb.com/docs4.0/ch02s01.html

Title: 1. Building the Schema

URL Source: https://www.hammerdb.com/docs4.0/ch02s01.html

Markdown Content:
**Figure 2.1.Benchmark Options**

![Image 1: Benchmark Options](https://www.hammerdb.com/docs4.0/resources/ch2-1.PNG)

Click on the Benchmark tree view, under TPROC-C select TPROC-C Schema Build Options to display the TPROC-C Schema Options window. Within this window enter the connection details of your database software. These options will vary depending on the database chosen. Select a number of warehouses, 10 is good for a first test and set the Virtual Users to build schema to the number of CPU cores on your system. Click OK.

**Figure 2.2.Build Options**

![Image 2: Build Options](https://www.hammerdb.com/docs4.0/resources/ch2-2.PNG)

.

Double-click on Build in the tree view and you will receive a prompt on the settings chosen to build the schema. Click Yes.

**Figure 2.3.Create Schema**

![Image 3: Create Schema](https://www.hammerdb.com/docs4.0/resources/ch2-3.PNG)

Observe that HammerDB begins to build the schema with multiple users.

**Figure 2.4.Building Schema**

![Image 4: Building Schema](https://www.hammerdb.com/docs4.0/resources/ch2-4.PNG)

Wait until the schema build completes and then click on the red button, tagged with Destroy Virtual Users.

**Figure 2.5.Schema build complete**

![Image 5: Schema build complete](https://www.hammerdb.com/docs4.0/resources/ch2-5.PNG)

Within the tree-view Select Driver Script Options. Leave the settings at Test Driver Script and click OK
