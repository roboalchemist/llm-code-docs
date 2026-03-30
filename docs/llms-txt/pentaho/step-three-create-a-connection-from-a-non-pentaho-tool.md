# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/connect-to-the-pentaho-data-service-from-a-non-pentaho-tool/step-three-create-a-connection-from-a-non-pentaho-tool.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/connect-to-the-pentaho-data-service-from-a-non-pentaho-tool/step-three-create-a-connection-from-a-non-pentaho-tool.md

# Step 3: Create a connection from a non-Pentaho tool

Once the driver is installed, you will need to create the connection to the Pentaho Data Service. For many tools, you can connect by specifying a connection object. Review the connection details and options in [Connect to the Pentaho Data Service from a Pentaho tool](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/connect-to-the-pentaho-data-service-from-a-pentaho-tool).

You will probably also need the following JDBC driver class parameter and its value:

* **JDBC Driver Class**

  *org.pentaho.di.trans.dataservice.jdbc.ThinDriver*

The JDBC connection string uses the following format:

```
jdbc:pdi://<Pentaho Server Hostname:Port>/kettle?option=value&option=value

```

The following example shows how you might format a connection string:

```
jdbc:pdi://localhost:8080/kettle?webappname=pentaho
```

The **webappname** is required if the data service is running on the Pentaho Server.
