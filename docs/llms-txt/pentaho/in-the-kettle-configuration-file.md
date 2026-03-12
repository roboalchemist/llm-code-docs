# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/change-jetty-server-parameters/in-the-kettle-configuration-file.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/change-jetty-server-parameters/in-the-kettle-configuration-file.md

# In the Kettle Configuration file

To change the Jetty server parameters in the `kettle.properties` file, configure the following parameters to the numeric value you want. See [Set Kettle Variables](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables) if you need more information on how to do this.

| Kettle Variable in kettle.properties       | Jetty Server Parameter  |
| ------------------------------------------ | ----------------------- |
| KETTLE\_CARTE\_JETTY\_ACCEPTORS            | acceptors               |
| KETTLE\_CARTE\_JETTY\_ACCEPT\_QUEUE\_SIZE  | acceptQueueSize         |
| KETTLE\_CARTE\_JETTY\_RES\_MAX\_IDLE\_TIME | lowResourcesMaxIdleTime |
