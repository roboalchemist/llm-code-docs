# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page/ael-logging-cp/configuring-ael-logging/modify-the-logback.xml-file.md

# Modify the XML file

The `logback.xml` file controls the size and number of the log files. Perform the following steps to modify the `logback.xml` file:

1. 1. Log on to the cluster and stop the AEL daemon.
2. 2. Navigate to the `design-tools/data-integration/adaptive-execution/config` directory and open the `logback.xml` file.
3. 3. Edit the following settings:
   4. **maxFileSize**

      The rotation file size. The maximum size of each log file is 10MB (default).
   5. **minIndex and maxIndex**

      The number of log files in use. The maximum number of log files is 10 (default). The minimum number of log files is 0.
4. 5. Save and close the file.
5. Restart the AEL daemon.

See the **Administer Pentaho Data Integration and Analytics** document for more information about the AEL daemon.
