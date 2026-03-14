# Source: https://documentation.wazuh.com/current/user-manual/wazuh-server-cluster/index.md

<!-- Copyright (C) 2015, Wazuh, Inc. -->

# Wazuh server cluster

The Wazuh server cluster is made up of multiple Wazuh server nodes in a distributed environment. This deployment strategy helps to provide horizontal scalability and improved performance. In an environment with many endpoints to monitor, you can combine this deployment strategy with a [network load balancer](agent-connections.md#connecting-with-load-balancer) to distribute the Wazuh agent connection load effectively across multiple nodes. This approach enables the Wazuh server to manage a large number of Wazuh agents more efficiently and ensure high availability.

> ##### Content
> 
> * [Architecture overview](architecture-overview.md)
> * [Types of nodes in a Wazuh server cluster](types-of-nodes.md)
> * [How the Wazuh server cluster works](how-server-cluster-works.md)
> * [Wazuh cluster nodes configuration](cluster-nodes-configuration.md)
> * [Data synchronization](data-synchronization.md)
> * [Certificates deployment](certificates-deployment.md)
> * [Adding new Wazuh server nodes](adding-new-server-nodes/index.md)
>   * [Certificates creation](adding-new-server-nodes/certificates-creation.md)
>   * [Configuring existing components to connect with the new node](adding-new-server-nodes/configuration-to-connect-with-new-node.md)
>   * [Wazuh server node(s) installation](adding-new-server-nodes/server-nodes-installation.md)
>   * [Testing the cluster](adding-new-server-nodes/testing-the-cluster.md)
> * [Agent connections](agent-connections.md)
> * [Load balancers](load-balancers.md)
