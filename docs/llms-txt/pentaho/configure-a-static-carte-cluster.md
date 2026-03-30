# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-static-carte-cluster.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-static-carte-cluster.md

# Configure a static Carte cluster

Follow the directions below to set up static Carte slave servers:

1. Copy over any required JDBC drivers and PDI plugins from your development instances of PDI to the Carte instances.
2. Run the Carte script with an IP address, hostname, or domain name of this server, and the port number you want it to be available on.

   ```
   ./carte.sh 127.0.0.1 8081
   ```
3. If you will be executing content stored in a Pentaho Repository, copy the`repositories.xml` file from the .kettle directory on your workstation to the same location on your Carte slave. Without this file, the Carte slave will be unable to connect to the Pentaho Repository to retrieve content.
4. Ensure that the Carte service is running as intended, accessible from your primary PDI development machines, and that it can run your jobs and transformations.
5. To start this slave server every time the operating system boots, create a startup or init script to run Carte at boot time with the same options you tested with.

   Pentaho Server Considerations

   **Note:** Any action done through the Carte server embedded in the Pentaho Server is controlled through the`/pentaho/server/pentaho-server/pentaho-solutions/system/kettle/slave-server-config.xml`file. To make modifications to `slave-server-config.xml`, you must stop the Pentaho Server.
