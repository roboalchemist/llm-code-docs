# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/pentaho-data-integration-performance-tips/limit-in-memory-log-output.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/pentaho-data-integration-performance-tips/limit-in-memory-log-output.md

# Limit in-memory log output

PDI logs data about transformations and jobs according to default parameters that control how many lines are allowed in the log and how long the oldest line should stay in memory before it is released. Obviously the more lines that are recorded and the longer they are kept, the more heap space is consumed by them. If you are experiencing memory shortages or slow performance in your PDI content, you can address the problem by modifying in-memory logging.

In Spoon, the following parameters control logging:

* **KETTLE\_MAX\_LOG\_SIZE\_IN\_LINES**

  the maximum number of log lines that are kept internally by Kettle. Setting this to 0 (the default) forces PDI to keep all rows.
* **KETTLE\_MAX\_LOG\_TIMEOUT\_IN\_MINUTES**

  the maximum age (in minutes) that a log line should be kept internally by PDI. Setting this to 0 (the default) keeps all rows indefinitely.
* **KETTLE\_MAX\_JOB\_TRACKER\_SIZE**

  the maximum number of job trackers kept in memory. Default value is: 1000.
* **KETTLE\_MAX\_JOB\_ENTRIES\_LOGGED**

  the maximum number of job entry results kept in memory for logging purposes. Default value is: 1000.
* **KETTLE\_MAX\_LOGGING\_REGISTRY\_SIZE**

  the maximum number of logging registry entries kept in memory for logging purposes. Default value is: 1000.

The equivalent parameters to the first two variables, which can be set on each KTR or KJB individually using Kitchen or Pan, are:

* maxloglines
* maxlogtimeout

Set these values to the lowest non-zero values that your operations can tolerate. If you are using logging for any purpose, you must balance between tolerable performance and necessary functionality.
