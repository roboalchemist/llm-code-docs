# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/change-jetty-server-parameters.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/carte-cluster-configuration/change-jetty-server-parameters.md

# Change Jetty Server Parameters

Carte runs on a Jetty server. You do not need to do anything to configure the Jetty server for Carte to work. But if you want to make changes to the default connection parameters, complete the steps in one of the subsections that follow.

| Jetty Server Parameters | Definition                                                                                                                                |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| acceptors               | The number of thread dedicated to accepting incoming connections. The number of acceptors should be below or equal to the number of CPUs. |
| acceptQueueSize         | Number of connection requests that can be queued up before the operating system starts to send rejections.                                |
| lowResourcesMaxIdleTime | This allows the server to rapidly close idle connections in order to gracefully handle high load situations.                              |

**Note:** If you want to learn more about these options, check out the Jetty documentation here: <http://wiki.eclipse.org/Jetty/Howto/Configure_Connectors#Configuration_Options>. For more information about a high load setup read this article: <https://wiki.eclipse.org/Jetty/Howto/High_Load>.
