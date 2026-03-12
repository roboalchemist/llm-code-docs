# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/connect-to-the-pentaho-data-service-from-a-non-pentaho-tool.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/connect-to-the-pentaho-data-service-from-a-non-pentaho-tool.md

# Connect to the Pentaho Data Service from a Non-Pentaho tool

A Pentaho Data Service is a virtual table that contains the output of a step in a PDI transformation. You can identify, connect to, and query the Pentaho Data Service from a non-Pentaho tool, like RStudio or SQuirreL. For a [streaming data service](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/creating-a-regular-or-streaming-pentaho-data-service), you must use a JDBC driver from your non-Pentaho tool to access streaming operations.

**Note:** To connect and query the Pentaho Data Service, you need to know the data service name and have permission to run the transformation and to access the Pentaho Server where it is published.

To connect to and run a Pentaho Data Service from a non-Pentaho tool, like SQuirreL or Beaker, you need to install the service driver files, then create a connection to the data service from your tool.

Before you can connect to and run a Pentaho Data Service from a non-Pentaho tool like SQuirreL or Beaker, you need to download the PDI Data Service driver and install it. The driver is bundled with PDI. If you want someone who does not have PDI to connect to your data service, you will need to download the driver and give it to them so that they can install it.
