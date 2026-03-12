# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/connect-to-clusters-pdi-only.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/connect-to-clusters-pdi-only.md

# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connect-to-clusters-pdi-only.md

# Connect to clusters (PDI only)

Use the **Clustering** options in the Database Connection dialog box to cluster the database connection and create connections to data partitions in PDI. To create a new connection to a data partition, enter a **Partition ID**, the **Host Name**, the **Port**, the **Database Name**, **User Name**, and **Password** for the connection.

If you have the Pentaho Server configured in a cluster of servers, and use the Data Source Wizard(DSW) in PUC to add a new data source, the new data source will only be seen on the cluster node where the user has a session. For the new data source to be seen by all the cluster nodes, you must disable DSW data source caching. This may cause the loading of the data source list to be slower since the list is not cached.

To disable the cache, navigate to the `server/pentaho-server/pentaho-solutions/system` folder and set the **enableDomainIdCache** value in the `system.properties` file to false.
