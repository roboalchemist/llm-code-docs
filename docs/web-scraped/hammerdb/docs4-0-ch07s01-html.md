# Source: https://www.hammerdb.com/docs4.0/ch07s01.html

Title: 1. Start the Agent

URL Source: https://www.hammerdb.com/docs4.0/ch07s01.html

Markdown Content:
To start the agent on Linux run the agent program locally in the agent directory.

$./agent 
Initializing HammerDB Metric Agent 4.0
HammerDB Metric Agent active @ id 20376 hostname CRANE (Ctrl-C to Exit)
On Windows double-click on agent.bat in the agent directory.

**Figure 7.1.agent.bat**

![Image 1: agent.bat](https://www.hammerdb.com/docs4.0/resources/ch7-1.PNG)

On both Windows and Linux your Firewall configuration should permit communication between the hosts where the agent and the display are running, for example on Windows you may see the following security alert as the agent will open a port for communication, access needs to be permitted to enable communication.

**Figure 7.2.Security Alert**

![Image 2: Security Alert](https://www.hammerdb.com/docs4.0/resources/ch7-2.PNG)

A window will open indicating the id that the agent is listening on. Pressing Ctrl-C or closing the window will close the agent.

**Figure 7.3.Windows agent**

![Image 3: Windows agent](https://www.hammerdb.com/docs4.0/resources/ch7-3.PNG)
