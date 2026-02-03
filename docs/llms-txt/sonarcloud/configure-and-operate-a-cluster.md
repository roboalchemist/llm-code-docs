# Source: https://docs.sonarsource.com/sonarqube-server/8.9/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/configure-and-operate-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/configure-and-operate-a-cluster.md

# Operating the DCE cluster

*High availability and cluster scalability are features of the* [*Data Center Edition*](https://redirect.sonarsource.com/editions/datacenter.html)*.*

Once the SonarQube Server cluster is installed, you have a high availability configuration that allows your SonarQube Server instance to stay up and running even if there is a crash or failure in one of the cluster’s nodes. Your SonarQube Server cluster is also scalable, and you can add application nodes to increase your computing capabilities.

### Start, stop, or update the cluster <a href="#start-stop-or-upgrade-the-cluster" id="start-stop-or-upgrade-the-cluster"></a>

#### Start the Cluster <a href="#start-the-cluster" id="start-the-cluster"></a>

To start a cluster, you need to follow these steps in order:

1. Start the search nodes
2. Start the application nodes

#### Stop the Cluster <a href="#stop-the-cluster" id="stop-the-cluster"></a>

To stop a cluster, you need to follow these steps in order:

1. Stop the application nodes
2. Stop the search nodes

#### Update SonarQube Server <a href="#upgrade-sonarqube-server" id="upgrade-sonarqube-server"></a>

1. Stop the cluster.
2. Update SonarQube Server on all nodes (application part, plugins, JDBC driver if required) following the usual update procedure but without triggering the setup phase. See [update](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/update "mention").
3. Once all nodes have the same binaries: restart the cluster.
4. At this point, only one of the application nodes is up. Try to access `node_ip:port/setup` on each application node, and trigger the setup operation on the one that responds.

### Start or stop a node <a href="#start-or-stop-a-node" id="start-or-stop-a-node"></a>

You can start or stop a single node in the same way as starting and stopping an instance using a single server. By default, it’s a graceful shutdown where no new analysis report processing can start, but the tasks in progress are allowed to finish.

### Install or upgrade a plugin <a href="#install-or-upgrade-a-plugin" id="install-or-upgrade-a-plugin"></a>

1. Stop the application nodes.
2. Install or upgrade the plugin on the application nodes.
   * If upgrading, remove the old version.
   * You don’t need to install plugins on search nodes.
3. Restart the application nodes.

### Scalability <a href="#scalability" id="scalability"></a>

You have the option of adding application nodes (up to 10 total application nodes) to your cluster to increase computing capabilities.

#### Scaling in a Traditional Environment <a href="#scaling-in-a-traditional-environment" id="scaling-in-a-traditional-environment"></a>

**Adding an Application Node**

To add an application node:

1. Configure your new application node in sonar.properties. The following is an example of the configuration to be added to `sonar.properties` for a sixth application node (server6, ip6) in a cluster with the default five servers. For information about the system properties used, see [#traditional-environment-configuration](#traditional-environment-configuration "mention").<br>

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
The `sonar.cluster.node.web.port` and `sonar.cluster.node.ce.port` system properties are optional. If not used, a dynamic port will be chosen.&#x20;
{% endhint %}

2. Update the configuration of the preexisting nodes to include your new node. While you don’t need to restart the cluster after adding a node, you should ensure the configuration is up to date on all of your nodes to avoid issues when you eventually do need to restart.

**Removing an Application Node**

When you remove an application node, make sure to update the configuration of the remaining nodes. Much like adding a node, while you don’t need to restart the cluster after removing a node, you should ensure the configuration is up to date on all of your nodes to avoid issues when you eventually do need to restart.

#### Scaling in a Docker Environment <a href="#scaling-in-a-docker-environment" id="scaling-in-a-docker-environment"></a>

**Adding Application Nodes**

If you’re using docker-compose, you can scale the application nodes using the following command:

`docker-compose up -d --scale sonarqube=3`

**Removing Application Nodes**

You can reduce the number of application nodes with the same command used to add application nodes by lowering the number.

### Monitoring <a href="#monitoring" id="monitoring"></a>

CPU and RAM usage on each node have to be monitored separately with an APM.

In addition, we provide a Web API `api/system/health` you can use to validate that all of the nodes in your cluster are operational.

* GREEN: SonarQube Server is fully operational
* YELLOW: SonarQube Server is usable, but it needs attention in order to be fully operational
* RED: SonarQube Server is not operational

To call it from a monitoring system without having to give admin credentials, it is possible to setup a system passcode. You can configure this through the `sonar.web.systemPasscode` property in `<sonarqubeHome>/conf/sonar.properties` if you’re using a traditional environment or through the corresponding environment variable if you’re using a Docker environment.

#### Cluster Status <a href="#cluster-status" id="cluster-status"></a>

On the System Info page at **Administration > System**, you can check whether your cluster is running safely (green) or has some nodes with problems (orange or red).

#### Maximum Pending Time for Tasks <a href="#maximum-pending-time-for-tasks" id="maximum-pending-time-for-tasks"></a>

On the global Background Tasks page at **Administration > Projects > Background Tasks**, you can see the number of **pending** tasks as well as the maximum **pending time** for the tasks in the queue. This shows the pending time of the oldest background task waiting to be processed. You can use this to evaluate if it might be worth configuring additional Compute Engine workers (Enterprise Edition) or additional nodes (Data Center Edition) to improve SonarQube Server performance.

### Compute engine workers <a href="#compute-engine-workers" id="compute-engine-workers"></a>

If you change the number of compute engine workers in the Sonar Qube Server UI, *you must restart each application node for the change to take effect*; more details about is on the [improving-performance](https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/maintenance/improving-performance "mention") page. You can configure up to 10 workers replicated across each application node. The number of workers is global and cannot be configured at the application node level.

For example, if you set 4 workers in the SonarQube Server UI and you have 2 application nodes, you have configured 8 workers total after you finish restarting all the application nodes (4 workers \* 2 nodes = 8 workers total).

### Project move <a href="#project-move" id="project-move"></a>

When the [project-move](https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/project-move "mention") feature is used in a DC installation:

* Projects are exported on only one of the application nodes
* The archive of the exported projects must be copied to all the applications nodes in the target server

### Configuration details <a href="#configuration-details" id="configuration-details"></a>

There are three TCP networks to configure:

* the network of application nodes that relies on Hazelcast.
* the network used for Elasticsearch internal communication between search nodes (`es` properties).
* the network between application nodes and search nodes (`search` properties).

[Hazelcast](https://hazelcast.org/) is used to manage the communication between the cluster’s application nodes. You don’t need to install it yourself, it’s provided out of the box.

### Docker environment configuration <a href="#docker-environment-configuration" id="docker-environment-configuration"></a>

In a Docker environment, your properties are configured using [environment-variables](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/environment-variables "mention").

### Traditional environment configuration <a href="#traditional-environment-configuration" id="traditional-environment-configuration"></a>

The following properties may be defined in the `<sonarqubeHome>/conf/sonar.properties` file of each node in a cluster. When defining a property that contains a list of hosts (`*.hosts`) the port is not required if the default port was not overridden in the configuration.

{% hint style="warning" %}
Ports can be unintentionally exposed. We recommend only giving external access to the application nodes and to main port (`sonar.web.port`).
{% endhint %}

**All nodes**

|                           |                                                                                                                                                                                                                                                                              |                    |             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------- |
| Property                  | Description                                                                                                                                                                                                                                                                  | Default            | Required    |
| `sonar.cluster.enabled`   | Set to `true` in each node to activate the cluster mode                                                                                                                                                                                                                      | `false`            | yes         |
| `sonar.cluster.name`      | The name of the cluster. **Required if multiple clusters are present on the same network.** For example this prevents mixing Production and Preproduction clusters. This will be the name stored in the Hazelcast cluster and used as the name of the Elasticsearch cluster. | `sonarqube`        | no          |
| `sonar.cluster.node.name` | The name of the node that is used on Elasticsearch and stored in Hazelcast member attribute (NODE\_NAME) for sonar-application                                                                                                                                               | `sonarqube-{UUID}` | <p><br></p> |
| `sonar.cluster.node.type` | Type of node: either `application` or `search`                                                                                                                                                                                                                               | <p><br></p>        | <p><br></p> |

**Application nodes**

<table><thead><tr><th width="265"></th><th></th></tr></thead><tbody><tr><td>Property</td><td>Description</td></tr><tr><td><code>sonar.cluster.hosts</code></td><td>Comma-delimited list of all <strong>application</strong> hosts in the cluster. This value must contain <strong>only application hosts</strong>. Each item in the list must contain the port if the default <code>sonar.cluster.node.port</code> value is not used. Item format is <code>sonar.cluster.node.host</code> or <code>sonar.cluster.node.host:sonar.cluster.node.po</code></td></tr><tr><td><code>sonar.cluster.node.host</code></td><td>IP address of the network card that will be used by Hazelcast to communicate with the members of the cluster.</td></tr><tr><td><code>sonar.cluster.node.port</code></td><td>The Hazelcast port for communication with each application member of the cluster. Default: <code>9003</code></td></tr><tr><td><code>sonar.cluster.node.web.port</code></td><td>The Hazelcast port for communication with the WebServer process. Port must be accessible to all other application nodes. If not specified, a dynamic port will be chosen and all ports must be open among the nodes.</td></tr><tr><td><code>sonar.cluster.node.ce.port</code></td><td>The Hazelcast port for communication with the ComputeEngine process. Port must be accessible to all other application nodes. If not specified, a dynamic port will be chosen and all ports must be open among the nodes.</td></tr><tr><td><code>sonar.cluster.search.hosts</code></td><td>Comma-delimited list of search hosts in the cluster. The list can contain either the host or the host and port, but not both. The item format is <code>sonar.cluster.node.search.host</code> for host only or<code>sonar.cluster.node.search.host:sonar.cluster.node.search.port</code> for host and port.</td></tr><tr><td><code>sonar.auth.jwtBase64Hs256Secret</code></td><td>Required for authentication with multiple web servers. It is used to keep user sessions opened when they are redirected from one web server to another by the load balancer. See <em>$SONARQUBE-HOME/conf/sonar.properties</em>) for details about how to generate this secret key.</td></tr></tbody></table>

**Search nodes**

<table><thead><tr><th width="262"></th><th></th></tr></thead><tbody><tr><td>Property</td><td>Description</td></tr><tr><td><code>sonar.cluster.node.search.host</code></td><td>Elasticsearch host of the current node used for HTTP communication between search and application nodes. IP must be accessible to all application nodes.</td></tr><tr><td><code>sonar.cluster.node.search.port</code></td><td>Elasticsearch port of the current node used for HTTP communication between search and application nodes. Port must be accessible to all application nodes.</td></tr><tr><td><code>sonar.cluster.es.hosts</code></td><td>Comma-delimited list of search hosts in the cluster. The list can contain either the host or the host and port but not both. The item format is <code>sonar.cluster.node.es.host</code> for host only or<code>sonar.cluster.node.es.host:sonar.cluster.node.es.port</code> for host and port.</td></tr><tr><td><code>sonar.cluster.node.es.host</code></td><td>Elasticsearch host of the current node used by Elasticsearch internal communication to form a cluster (TCP transport).</td></tr><tr><td><code>sonar.cluster.node.es.port</code></td><td>Elasticsearch port of the current node used by Elasticsearch internal communication to form a cluster (TCP transport). Port must be accessible to all other search nodes</td></tr><tr><td><code>sonar.search.initialStateTimeout</code></td><td>The timeout for the Elasticsearch nodes to elect a primary node. The default value will be fine in most cases, but in a situation where startup is failing because of a timeout, this may need to be adjusted. The value must be set in the format: <code>{integer}{timeunit}</code>. Valid <code>{timeunit}</code> values are: <code>ms</code> (milliseconds); <code>s</code> (seconds); <code>m</code> (minutes); <code>h</code> (hours); <code>d</code> (days); <code>w</code> (weeks)</td></tr></tbody></table>

#### Elasticsearch authentication <a href="#elasticsearch-authentication" id="elasticsearch-authentication"></a>

{% hint style="info" %}
This configuration is optional. To secure access to your setup, you may want to first limit access to the nodes in your network. Elasticsearch authentication just adds another layer of security.
{% endhint %}

{% hint style="warning" %}
When creating the PKCS#12 container, make sure it is created with an algorithm that is readable by Java 17.
{% endhint %}

For Elasticsearch authentication, the following properties need to be configured on specific nodes:

**Application nodes**

|                                 |                                                                                                                                                                                                                                                      |             |          |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| Property                        | Description                                                                                                                                                                                                                                          | Default     | Required |
| `sonar.cluster.search.password` | Password for Elasticsearch built-in user (elastic) which will be used on the client site. If provided, it enables authentication. If this property is set, `sonar.cluster.search.password` on the search nodes must also be set to exact same value. | <p><br></p> | no       |

**Search nodes**

|                                           |                                                                                                                                                                                                                                                                                                            |             |          |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | -------- |
| Property                                  | Description                                                                                                                                                                                                                                                                                                | Default     | Required |
| `sonar.cluster.search.password`           | Password for Elasticsearch built-in user (elastic) which will be set in ES. If provided, it enables authentication, and the instance will require additional properties to be set. If this property is set, `sonar.cluster.search.password` on the application nodes must also be set to exact same value. | <p><br></p> | no       |
| `sonar.cluster.es.ssl.keystore`           | File path to a keystore in PKCS#12 format. The user running SonarQube Server must have READ permission to that file. Required if password provided.                                                                                                                                                        | <p><br></p> | no       |
| `sonar.cluster.es.ssl.truststore`         | File path to a truststore in PKCS#12 format. The user running SonarQube Server must have READ permission to that file. Required if password provided.                                                                                                                                                      | <p><br></p> | no       |
| `sonar.cluster.es.ssl.keystorePassword`   | Password to the keystore.                                                                                                                                                                                                                                                                                  | <p><br></p> | no       |
| `sonar.cluster.es.ssl.truststorePassword` | Password to the truststore.                                                                                                                                                                                                                                                                                | <p><br></p> | no       |

When you’re using the SonarSource Docker images, the truststore/keystore should be provided as volumes. On Kubernetes, you need to create a new Secret from the truststore/keystore and provide the name to the Helm chart.

#### Elasticsearch TLS encryption over HTTP <a href="#elasticsearch-tls-encryption-over-http" id="elasticsearch-tls-encryption-over-http"></a>

**Prerequisite:** Elasticsearch authentication is enabled.

This configuration is optional. Enabling TLS on the HTTP layer provides additional security to ensure that all communications between application nodes and search nodes are encrypted.

The following properties need to be configured on both application nodes and search nodes:

|                                              |                                                                                                                                                              |             |          |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------- |
| Property                                     | Description                                                                                                                                                  | Default     | Required |
| `sonar.cluster.es.http.ssl.keystore`         | File path to a keystore in PKCS#12 format. The user running SonarQube Server must have READ permission to that file. If provided, it enables TLS encryption. | <p><br></p> | no       |
| `sonar.cluster.es.http.ssl.keystorePassword` | Password to the keystore.                                                                                                                                    | <p><br></p> | no       |

### Secure your network <a href="#secure-your-network" id="secure-your-network"></a>

To further lock down the communication in between the nodes in your SonarQube Server Cluster, you can define the following network rules:

|          |               |             |                                  |         |
| -------- | ------------- | ----------- | -------------------------------- | ------- |
| Protocol | Source        | Destination | Port                             | Default |
| TCP      | Reverse Proxy | App Node    | `sonar.web.port`                 | 9000    |
| TCP      | App Node      | Search Node | `sonar.cluster.node.search.port` | 9001    |
| TCP      | Search Node   | Search Node | `sonar.cluster.node.es.port`     | 9002    |
| TCP      | App Node      | App Node    | `sonar.cluster.node.port`        | 9003    |

You can further segment your network configuration if you specify a frontend, a backend and a search network.

<table><thead><tr><th width="118"></th><th></th><th></th></tr></thead><tbody><tr><td>Network</td><td>Parameter</td><td>Description</td></tr><tr><td>Frontend</td><td><code>sonar.web.host</code></td><td>Frontend HTTP Network</td></tr><tr><td>Backend</td><td><code>sonar.cluster.node.host</code></td><td>Backend App to App Network</td></tr><tr><td>Backend</td><td><code>sonar.cluster.search.hosts</code></td><td>Backend App to Search Network</td></tr><tr><td>Search</td><td><code>sonar.cluster.node.search.host</code></td><td>Backend Search to Search Network</td></tr></tbody></table>

### Limitations <a href="#limitations" id="limitations"></a>

* Cluster downtime is required for SonarQube Server upgrades or plugin installations.
* All application nodes must be stopped when installing, uninstalling, or upgrading a plugin.
* Plugins are not shared, meaning if you install/uninstall/upgrade a given plugin on one application node, you need to perform the same actions on the other application node.
* There is no way to perform actions on the cluster from a central app - all operations must be done manually on each node of the cluster.

### Frequently asked questions <a href="#frequently-asked-questions" id="frequently-asked-questions"></a>

**Does Elasticsearch discover automatically other ES nodes?**

No. Multicast is disabled. All hosts (IP+port) must be listed.

**Can different nodes run on the same machine?**

Yes, but it’s best to have one machine for each node to be resilient to failures. To maintain an even higher level of availability, each of your three search nodes can be located in a separate availability zone *within the same region*.

**Can the members of a cluster be discovered automatically?**

No, all nodes must be configured in `<sonarqubeHome>/conf/sonar.properties`*.*

**My keystore/truststore cannot be read by SonarQube Server**

Make sure that the keystore/truststore in question was generated with an algorithm that is known to Java 17. See [JDK-8267599](https://bugs.openjdk.java.net/browse/JDK-8267599) for reference
