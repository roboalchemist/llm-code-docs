# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/data-center-edition/scaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/data-center-edition/scaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/data-center-edition/scaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/data-center-edition/scaling.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/scaling.md

# Scaling

You have the option of adding application nodes (up to 10 total application nodes) to your cluster to increase computing capabilities. The operation is different depending on the SonarQube Server installation type.

### ZIP installation <a href="#zip-installation" id="zip-installation"></a>

#### Adding an Application Node <a href="#adding-an-application-node" id="adding-an-application-node"></a>

To add an application node:

1. Configure your new application node in sonar.properties. The following is an example of the configuration to be added to `sonar.properties` for a sixth application node (server6, ip6) in a cluster with the default five servers. For information about the system properties used, see [#general](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/dce-specific#general "mention").<br>

   **Server6:**

```css-79elbk
...
sonar.cluster.enabled=true
sonar.cluster.node.type=application
sonar.cluster.node.host=ip6 
sonar.cluster.node.port=9003
sonar.cluster.node.web.port=4023
sonar.cluster.node.ce.port=4024
sonar.cluster.hosts=ip1,ip2,ip6
sonar.cluster.search.hosts=ip3:9001,ip4:9001,ip5:9001
sonar.auth.jwtBase64Hs256Secret=YOURGENERATEDSECRET
...
```

{% hint style="info" %}
In the example:

* The hosts followed by ports are written using the IPv4 notation (e.g. `ip3:9001`). If you use IPv6 addresses, enclose the IP address in square brackets (`[ip3]:9001`).
* The `sonar.cluster.node.web.port` and `sonar.cluster.node.ce.port` system properties are used but are optional. If not used, a dynamic port will be chosen.
  {% endhint %}

2. Update the configuration of the preexisting nodes to include your new node. While you don’t need to restart the cluster after adding a node, you should ensure the configuration is up to date on all of your nodes to avoid issues when you eventually do need to restart.

#### Removing an Application Node <a href="#removing-an-application-node" id="removing-an-application-node"></a>

When you remove an application node, make sure to update the configuration of the remaining nodes. Much like adding a node, while you don’t need to restart the cluster after removing a node, you should ensure the configuration is up to date on all of your nodes to avoid issues when you eventually do need to restart.

### Docker installation <a href="#docker-installation" id="docker-installation"></a>

#### Adding Application Nodes <a href="#adding-application-nodes" id="adding-application-nodes"></a>

If you’re using docker-compose, you can scale the application nodes using the following command:

`docker-compose up -d --scale sonarqube=3`

#### Removing Application Nodes <a href="#removing-application-nodes" id="removing-application-nodes"></a>

You can reduce the number of application nodes with the same command used to add application nodes by lowering the number.

### Kubernetes installation <a href="#kubernetes-installation" id="kubernetes-installation"></a>

With Kubernetes’ Horizontal Pod Autoscaling (HPA), you can automatically scale your SonarQube Server out and in, resolving any performance issues you may have. See [setting-up-autoscaling](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [dce-topology](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/dce-topology "mention")
* [starting-stopping-cluster](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster "mention")
* [monitoring](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/monitoring "mention") your cluster
* [improving-performance](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/improving-performance "mention") of your cluster
* [updating](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition/updating "mention") your cluster
