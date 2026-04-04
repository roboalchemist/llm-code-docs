# Source: https://www.hammerdb.com/docs4.0/ch08s03.html

Title: 3. Primary Distribution

URL Source: https://www.hammerdb.com/docs4.0/ch08s03.html

Markdown Content:
The Primary Distribution button in the edit menu now becomes active to distribute scripts across instances.

**Figure 8.8.Primary Distribution**

![Image 1: Primary Distribution](https://www.hammerdb.com/docs4.0/resources/ch11-8.PNG)

Pressing this button enables the distribution of the contents of the Script Editor to all connected instances.

Distributing to 18424 osprey ...Primary Distribution Succeeded
The TPROC-C timed driver scripts reference the operating Mode and when loaded will set the parameter "mode" to the operating Mode running on that system.

If loaded locally a script will show the Mode that the instance of HammerDB is running in which by default will be "Local".

set mode "Local" ;# HammerDB operational mode
Once the Mode is set to "Primary" when the script is loaded on the Primary it will show the correct mode.

set mode "Primary" ;# HammerDB operational mode
When distributed from the Primary to the Replica the Replica will change the mode to the correct setting.

set mode "Replica" ;# HammerDB operational mode
Once a Replica is connected to a Primary all actions that are taken on the Primary will be replicated on the Replica. All of your workload choices of creating and running and closing down virtual users will be replicated automatically on the connected Replicas enabling control and simultaneous timing from a central point. This enables workloads to be directed to different database instances simultaneously. When operating in Replica Mode the Monitor Virtual User on that instance of HammerDB will not capture any performance data and report that "No snapshots are taken", the Replica will only run the active Virtual Users. Note that running a schema creation with multiple connected instances is not supported.

**Figure 8.9.Operating in Replica Mode**

![Image 2: Operating in Replica Mode](https://www.hammerdb.com/docs4.0/resources/ch11-9.PNG)

When the workload is complete the Primary will terminate the Virtual Users on the Replicas meaning that running in Remote Mode configurations is compatible with Autopilot.

**Figure 8.10.Replica Mode terminated**

![Image 3: Replica Mode terminated](https://www.hammerdb.com/docs4.0/resources/ch11-10.PNG)

If it is wished to capture the performance metrics on the Replica as well as the Primary the operational mode can be manually changed to "Local". In this case the Replicas will capture performance data from the databases instances that they are connected to.

set mode "Local" ;# HammerDB operational mode
To disable Remote Modes select Local Mode on the Primary on confirmation all connected instances will return to Local Mode.

Remote modes functionality in the CLI can be accessed using the switchmode command with the GUI and CLI being interchangeable and therefore a number of CLI Replicas can be connected to a GUI Primary if desired.
