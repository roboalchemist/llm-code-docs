# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/monitor-a-pentaho-data-service.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/monitor-a-pentaho-data-service.md

# Monitor a Pentaho Data Service

To monitor a data service, type one of the following commands into your browser:

* **List Names of Data Services on the Pentaho Server**

  ```
  http://<*Pentaho Server Host:Port*>/pentaho/kettle/listServices
  ```
* **List Status of Data Services on the Pentaho Server**

  ```
  http://<*Pentaho Server Host:Port*>/pentaho/kettle/status
  ```

Replace the `<*Pentaho Server Host:Port*>` of the Pentaho Server with the host name or IP address and the port of the Pentaho Server running the data service. You will need to have access to the Pentaho Server and be authenticated to run these commands.
