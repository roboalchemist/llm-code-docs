# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/about-carte-clusters.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/about-carte-clusters.md

# About Carte Clusters

You can set up an individual instance of Carte to operate as a standalone execution engine for a job or transformation. In the PDI client (Spoon) you can define one or more Carte servers and send jobs and transformations to them. If you want to improve PDI performance for resource-intensive transformations and jobs, use Carte cluster.

**Note:** You can cluster the Pentaho Server to provide failover support. If you decide to use the Pentaho Server, you must enable the proxy trusting filter as explained in [Schedule Jobs to Run on a Remote Carte Server](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/schedule-jobs-to-run-on-a-remote-carte-server), then set up your dynamic Carte slaves and define the Pentaho Server as the master.

There are two types of Carte clusters. Static Carte cluster has a fixed schema that specifies one master node and two or more slave nodes. In a static cluster, you specify the nodes in a cluster at design-time, before you run the transformation or job.

Static clusters are a good choice for smaller environments where you don't have a lot of machines (virtual or real) to use for PDI transformations. Dynamic clusters work well if nodes are added or removed often, such as in a cloud computing environment. Dynamic clustering is also more appropriate in environments where transformation performance is extremely important, or if there can potentially be multiple concurrent transformation executions.

A Dynamic Carte cluster has a schema that specifies one master node and a varying number of slave nodes. Unlike a static cluster, slave nodes are not known until runtime. Instead, you register the slave nodes, then at runtime, PDI monitors the slave nodes every 30 seconds to see if it is available to perform transformation and job processing tasks.
