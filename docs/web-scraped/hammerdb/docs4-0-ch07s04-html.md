# Source: https://www.hammerdb.com/docs4.0/ch07s04.html

Title: 4. Oracle Database Metrics

URL Source: https://www.hammerdb.com/docs4.0/ch07s04.html

Markdown Content:
When the Oracle Database is selected on both Windows and Linux an additional option is available to connect to the Oracle Database and display detailed performance metrics.

**Figure 7.11.Oracle Metrics Options**

![Image 1: Oracle Metrics Options](https://www.hammerdb.com/docs4.0/resources/ch7-11.PNG)

When the metrics button is pressed HammerDB connects to the database and displays graphical information from the Active Session History detailing wait events. By default in embedded mode the Oracle Database Metrics will display the Active Session History Graph. For detailed Oracle Database Metrics the Notebook tab should be dragged out and expanded to display in a separate window.

**Figure 7.12.Oracle Metrics Display Linux**

![Image 2: Oracle Metrics Display Linux](https://www.hammerdb.com/docs4.0/resources/ch7-12.png)

When display in a separate window, it is possible to make a selection from the window and display the wait events related to that period of time. When the SQL_ID is selected the buttons then enable the detailed viewing of SQL text, the explain plan, IO statistics and SQL statistics related to that SQL.

**Figure 7.13.Oracle Metrics Display Windows**

![Image 3: Oracle Metrics Display Windows](https://www.hammerdb.com/docs4.0/resources/ch7-13.png)

When an event is selected the analysis shows details related to that particular event.

**Figure 7.14.Oracle Metrics Event**

![Image 4: Oracle Metrics Event](https://www.hammerdb.com/docs4.0/resources/ch7-14.PNG)

The CPU Metrics button displays the current standard HammerDB CPU Metrics display in an embedded Window and requires the agent running on the database server. The CPU metrics are not recorded as historical data relating to the Active Session History.

**Figure 7.15.Oracle Database CPU Metrics**

![Image 5: Oracle Database CPU Metrics](https://www.hammerdb.com/docs4.0/resources/ch7-15.PNG)
