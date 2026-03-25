# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/create-a-cluster-schema.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/create-a-cluster-schema.md

# Create a cluster schema

Clustering allows transformations and transformation steps to be executed in parallel on more than one Carte server. The clustering schema defines which slave servers you want to assign to the cluster and a variety of clustered execution options.

Begin by selecting the **Kettle cluster schemas** node in the PDI client **Explorer View**. Right-click and select **New** to open the Clustering Schema dialog box.

| Option                      | Description                                                                                                                                                                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Schema name                 | The name of the clustering schema                                                                                                                                                                                                                                                  |
| Port                        | <p>Specify the port from which to start numbering ports for the slave servers. Each additional clustered step executing on a slave server will consume an additional port.</p><p>To avoid networking problems, make sure no other networking protocols are in the same range .</p> |
| Sockets buffer size         | The internal buffer size to use                                                                                                                                                                                                                                                    |
| Sockets flush interval rows | The number of rows after which the internal buffer is sent completely over the network and emptied.                                                                                                                                                                                |
| Sockets data compressed?    | When enabled, all data is compressed using the Gzip compression algorithm to minimize network traffic                                                                                                                                                                              |
| Dynamic cluster             | If checked, a master Carte server will perform failover operations, and you must define the master as a slave server in the field below. If unchecked, the PDI client will act as the master server, and you must define the available Carte slaves in the field below.            |
| Slave Servers               | A list of the servers to be used in the cluster. You must have one master server and any number of slave servers. To add servers to the cluster, click **Select slave servers** to select from the list of available slave servers.                                                |
