# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/continuous-scale-axis.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/continuous-scale-axis.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer/continuous-scale-axis.md

# Continuous scale axis

Line, Area, and Scatter charts provide the number and time dimensions on a continuous scale axis. The continuous axis is helpful for identifying trends that occur over a period of time, such as financial growth, real estate sales, or test scores.

For a level of a time hierarchy to be plotted on a continuous scale, the level must be able to provide start date times for its members. You can use either of these methods to provide the start date times:

* Base the level directly on a date-related database column and set the level's key column data type to: **Date**, **Timestamp**, or **Time**.
* Use the level to provide start date times for its members by specifying the **AnalyzerDateFormat** annotation.

**Note:** Prior to Pentaho version 8.1, line and area visualizations used a discrete axis, where the data points display evenly spaced across the axis. To revert to the discrete axis behavior and preserve chart compatibility with earlier versions, you must change the web client configuration file, as explained in the **Install Pentaho Data Integration and Analytics** document.
