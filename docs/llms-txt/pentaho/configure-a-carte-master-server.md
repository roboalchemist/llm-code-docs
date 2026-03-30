# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-dynamic-carte-cluster/configure-a-carte-master-server.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-dynamic-carte-cluster/configure-a-carte-master-server.md

# Configure a Carte Master Server

Follow the process below to configure the Carte Master Server.

1. Copy over any required JDBC drivers from your development instances of PDI to the Carte instances.
2. Create a carte-master-config.xml configuration file using the following example as a template:

   ```xml
   <slave_config>
   <!-- on a master server, the slaveserver node contains information about this Carte instance -->
       <slaveserver>
           <name>Master</name>
           <hostname>yourhostname</hostname>
           <port>9001</port>
           <username>cluster</username>
           <password>cluster</password>
           <master>Y</master>
       </slaveserver>
   </slave_config>
   ```

   **Note:** The \<name> of the Master server must be unique among all Carte instances in the cluster.
3. Run the Carte script with the `carte-slave-config.xml` parameter. Note that if you placed the `carte-slave-config.xml` file in a different directory than the Carte script, you will need to add the path to the file to the command.

   ```
   ./carte.sh carte-master-config.xml
   ```
4. Ensure that the Carte service is running as intended.
5. To start this master server every time the operating system boots, create a startup or init script to run Carte at boot time.

You now have a Carte master server to use in a dynamic cluster. Next, configure the Carte slave servers.
