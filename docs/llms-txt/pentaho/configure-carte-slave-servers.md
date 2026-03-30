# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-dynamic-carte-cluster/configure-carte-slave-servers.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/configure-a-dynamic-carte-cluster/configure-carte-slave-servers.md

# Configure Carte slave servers

Follow the directions below to set up static Carte slave servers.

1. Follow the process to configure the Carte master server (see above).
2. Make sure the master server is running.
3. Copy over any required JDBC drivers from your development instances of PDI to the Carte instances.
4. In the`/pentaho/design-tools/` directory, create a `carte-slave-config.xml` configuration file using the following example as a template:

   ```xml
   <slave_config>
   <!-- the masters node defines one or more load balancing Carte instances that will manage this slave -->
       <masters>
   		<slaveserver>
   			<name>Master</name>
   			<hostname>yourhostname</hostname>
   			<port>9000</port>
   <!-- uncomment the next line if you want the DI Server to act as the load balancer -->
   <!--	    <webAppName>pentaho</webAppName> -->
   			<username>cluster</username>
   			<password>cluster</password>
   			<master>Y</master>
   		</slaveserver>
   	</masters>
   	<report_to_masters>Y</report_to_masters>
   <!-- the slaveserver node contains information about this Carte slave instance -->
       <slaveserver>
           <name>SlaveOne</name>
           <hostname>yourhostname</hostname>
           <port>9001</port>
           <username>cluster</username>
           <password>cluster</password>
           <master>N</master>
       </slaveserver>
   </slave_config>
   ```

   **Note:** The slaveserver \<name> must be unique among all Carte instances in the cluster.
5. If you want a slave server to use the same kettle properties as the master server, add the \<get\_properties\_from\_master> and \<override\_existing\_properties> tags between the \<slaveserver> and \</slaveserver> tags for the slave server. Put the name of the master server between the \<get\_properties\_from\_master> and \</get\_properties\_from\_master> tags. Here is an example.

   ```xml
   <!-- the slaveserver node contains information about this Carte slave instance -->
       <slaveserver>
           <name>SlaveOne</name>
           <hostname>yourhostname</hostname>
           <port>9001</port>
           <username>cluster</username>
           <password>cluster</password>
           <master>N</master>
           <get_properties_from_master>Master</get_properties_from_master>
           <override_existing_properties>Y</override_existing_properties>
       </slaveserver>
   ```
6. Save and close the file.
7. Run the Carte script with the `carte-slave-config.xml` parameter. Note that if you placed the `carte-slave-config.xml` file in a different directory than the Carte script, you will need to add the path to the file to the command.

   ```xml
   ./carte.sh carte-slave-config.xml
   ```
8. If you will be executing content stored in a Pentaho Repository, copy the `repositories.xml` file from the `.kettle` directory on your workstation to the same location on your Carte slave. Without this file, the Carte slave will be unable to connect to the Pentaho Repository to retrieve PDI content.
9. Stop, then start the master and slave servers.
10. Stop, then start the Pentaho Server.
11. Ensure that the Carte service is running as intended. If you want to start this slave server every time the operating system boots, create a startup or init script to run Carte at boot time.

**Note:** Note: The following are features of Carte:

* The PDI Server and Carte keep track of the age of an object in transformations and jobs.
* Objects are purged when the maximum specified age is reached.
* Objects are only purged when the servers are idle.
* Purge verification occurs every 20 seconds.
