# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page/ael-logging-cp/activating-ael-logging.md

# Activating AEL logging

AEL logging is installed and activated by default. To deactivate AEL logging, you will need to modify the `application.properties` file as described in the following instructions. Verify that you have the appropriate permissions to read, write, and execute commands in the following directories in the instructions.

1. Log on to the cluster and stop the AEL daemon.
2. Navigate to the `design-tools/data-integration/adaptive-execution/config` directory and open the `application.properties` file.
3. Locate the following line of code: `logging.config=./config/logback.xml`
4. Add comment tags for this line of code.
5. Save and close the file.
6. Restart the AEL daemon.

See the **Administer Pentaho Data Integration and Analytics** document for more information about the AEL daemon.
