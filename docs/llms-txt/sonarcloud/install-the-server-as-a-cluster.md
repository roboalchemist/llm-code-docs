# Source: https://docs.sonarsource.com/sonarqube-server/8.9/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/install-the-server-as-a-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server-as-a-cluster.md

# Data Center Edition (DCE)

*Running SonarQube Server as a Cluster is only possible with a* [*Data Center Edition*](https://www.sonarsource.com/plans-and-pricing/data-center/)*.* As a DCE subscriber, Sonar will assist with the setup and configuration of your cluster. Get in touch with your account manager to receive appropriate onboarding resources.

The Data Center Edition (DCE) allows SonarQube Server to run in a clustered configuration to make it resilient to failures.

### Overview <a href="#overview" id="overview"></a>

The default configuration for the Data Center Edition comprises five servers, a load balancer, and a database server:

* Two application nodes responsible for handling web requests from users (WebServer process) and handling analysis reports (ComputeEngine process). You can add application nodes to increase computing capabilities.
* Three search nodes that host the Elasticsearch process that will store data indices. SSDs perform significantly better than HDDs for these nodes.
* A reverse proxy / load balancer to load balance traffic between the two application nodes. The installing organization must supply this hardware or software component.
* PostgreSQL, Oracle, or Microsoft SQL Server database server. This software must be supplied by the installing organization.

With this configuration, one application node and one search node can be lost without impacting users. Here is a diagram of the default topology:

<figure><img src="https://3560343708-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4FzELVjsPO4ijRo3jtBV%2Fuploads%2Fgit-blob-99037b15faf389852488e711ff471c04bd1ea757%2F3555755a63635e0fdb9e75a54f4cd5b3df280216.png?alt=media" alt="Diagram of SonarQube installed as a cluster"><figcaption></figcaption></figure>

### Requirements <a href="#requirements" id="requirements"></a>

#### Network <a href="#network" id="network"></a>

You need a minimum of five servers (two application nodes and three search nodes) to form a SonarQube Server application cluster. Servers can be virtual machines; it is not necessary to use physical machines. You can also add application nodes to increase computing capabilities.

The operating system requirements for servers are available on the [server-host](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/installation-requirements/server-host "mention") page.

All application nodes should be identical in terms of hardware and software. Similarly, all search nodes should be identical to each other. Application and search nodes, however, can differ from one another. Generally, search nodes are configured with more CPU and RAM than application nodes.

Search nodes can be located in different availability zones, but they must be in the same region. In this case, each search node should be located in a separate availability zone to maintain availability in the event of a failure in one zone.

**Example machines**

Here are the machines we used to perform our validation with a 200M issues database. You can use this as a minimum recommendation to build your cluster.

* App Node made of [Amazon EC2 general purpose xlarge](https://aws.amazon.com/ec2/instance-types/): 4 vCPUs, 16GB RAM
* Search Node made of [Amazon EC2 general purpose 2xlarge](https://aws.amazon.com/ec2/instance-types/): 8 vCPUs, 32GB RAM - 16GB allocated to Elasticsearch. SSDs perform significantly better than HDDs for these nodes.

#### Database server <a href="#database-server" id="database-server"></a>

Supported database systems are available on the [database-requirements](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/installation-requirements/database-requirements "mention") page.

#### Load balancer <a href="#load-balancer" id="load-balancer"></a>

Sonar does not provide specific recommendations for reverse proxy / load balancer or solution-specific configuration. The general requirements for the Data Center Edition are:

* Ability to balance HTTP requests (load) between the application nodes configured in the cluster.
* If terminating HTTPS, meets the requirements set out in [Operating the server](https://app.gitbook.com/s/I10pmJWeVVXYITlQJllp/setup-and-upgrade/operating-the-server "mention").
* No requirement to preserve or sticky sessions; this is handled by the built-in JWT mechanism.
* Ability to check for node health for routing

#### Example with HAproxy <a href="#example-with-haproxy" id="example-with-haproxy"></a>

```css-79elbk
frontend http-in
    bind *:80
    bind *:443 ssl crt /etc/ssl/private/<server_certificate>
    http-request redirect scheme https unless { ssl_fc }
    default_backend sonarqube_server
backend sonarqube_server
    balance roundrobin
    http-request set-header X-Forwarded-Proto https
    option httpchk GET /api/system/status
    http-check expect rstring UP|DB_MIGRATION_NEEDED|DB_MIGRATION_RUNNING
    default-server check maxconn 200
    server node1 <server_endpoint_1>
    server node2 <server_endpoint_2> 
```

#### License <a href="#license" id="license"></a>

You need a dedicated license to activate the Data Center Edition. If you don’t have one yet, please contact the SonarSource Sales Team.

#### Support <a href="#support" id="support"></a>

Don’t start this journey alone! As a Data Center Edition subscriber, Sonar will assist with the setup and configuration of your cluster. Get in touch with [Sonar Support](https://help.sonarsource.com/) for help.

### Installing SonarQube Server from the ZIP file <a href="#installing-sonarqube-from-the-zip-file" id="installing-sonarqube-from-the-zip-file"></a>

Additional parameters are required to activate clustering capabilities and specialize each node. These parameters are in addition to standard configuration properties used in a single-node configuration.

The **sonar.properties** file on each node will be edited to configure the node’s specialization. A list of all cluster-specific configuration parameters is available in the [configure-and-operate-a-cluster](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/configure-and-operate-a-cluster "mention") documentation.

Prior to configuration, you will need to generate a value for the `sonar.auth.jwtBase64Hs256Secret` property for the application nodes. The value is a HS256 key encoded with base64 and will be the same for both nodes. The following examples illustrate how to generate this value, where `your_secret` and `your_key` are arbitrary strings that can be modified:

**On a Unix system**:

```css-79elbk
echo -n "your_secret" | openssl dgst -sha256 -hmac "your_key" -binary | base64
```

**On a Windows system with PowerShell**:

```css-79elbk
$message = 'your_secret'
$secret = 'your_key'

$hmacsha = New-Object System.Security.Cryptography.HMACSHA256
$hmacsha.key = [Text.Encoding]::ASCII.GetBytes($secret)
$signature = $hmacsha.ComputeHash([Text.Encoding]::ASCII.GetBytes($message))
$signature = [Convert]::ToBase64String($signature)

echo $signature
```

#### Sample Configuration <a href="#sample-configuration" id="sample-configuration"></a>

The following example represents a sample configuration of a SonarQube Server DCE. The example assumes:

* The VMs having IP addresses ip1 and ip2 (server1, server2) are application nodes
* The VMs having IP addresses ip3, ip4, and ip5 (server3, server4 and server5) are search nodes

The configuration to be added to `sonar.properties` for each node is the following. For information about the system properties used, see [#traditional-environment-configuration](https://docs.sonarsource.com/sonarqube-server/2025.1/configure-and-operate-a-cluster#traditional-environment-configuration "mention").

**Application nodes**

server1:

```css-79elbk
...
sonar.cluster.enabled=true
sonar.cluster.node.type=application
sonar.cluster.node.host=ip1
sonar.cluster.node.port=9003
sonar.cluster.node.web.port=4023
sonar.cluster.node.ce.port=4024
sonar.cluster.hosts=ip1,ip2
sonar.cluster.search.hosts=ip3:9001,ip4:9001,ip5:9001
sonar.auth.jwtBase64Hs256Secret=YOURGENERATEDSECRET
...
```

server2

```css-79elbk
...
sonar.cluster.enabled=true
sonar.cluster.node.type=application
sonar.cluster.node.host=ip2
sonar.cluster.node.port=9003
sonar.cluster.node.web.port=4023
sonar.cluster.node.ce.port=4024
sonar.cluster.hosts=ip1,ip2
sonar.cluster.search.hosts=ip3:9001,ip4:9001,ip5:9001
sonar.auth.jwtBase64Hs256Secret=YOURGENERATEDSECRET
...
```

{% hint style="info" %}
The `sonar.cluster.node.web.port` and `sonar.cluster.node.ce.port` system properties are optional. If not used, a dynamic port will be chosen.&#x20;
{% endhint %}

**Search nodes**

server3

```css-79elbk
...
sonar.cluster.enabled=true
sonar.cluster.node.type=search
sonar.cluster.node.search.host=ip3
sonar.cluster.node.search.port=9001
sonar.cluster.node.es.host=ip3
sonar.cluster.node.es.port=9002
sonar.cluster.es.hosts=ip3:9002,ip4:9002,ip5:9002
...
```

server4

```css-79elbk
...
sonar.cluster.enabled=true
sonar.cluster.node.type=search
sonar.cluster.node.search.host=ip4
sonar.cluster.node.search.port=9001
sonar.cluster.node.es.host=ip4
sonar.cluster.node.es.port=9002
sonar.cluster.es.hosts=ip3:9002,ip4:9002,ip5:9002
...
```

server5

```css-79elbk
...
sonar.cluster.enabled=true
sonar.cluster.node.type=search
sonar.cluster.node.search.host=ip5
sonar.cluster.node.search.port=9001
sonar.cluster.node.es.host=ip5
sonar.cluster.node.es.port=9002
sonar.cluster.es.hosts=ip3:9002,ip4:9002,ip5:9002
...
```

#### Sample Installation Process <a href="#sample-installation-process" id="sample-installation-process"></a>

The following is an example of the default SonarQube Server DCE installation process. You need to tailor your installation to the specifics of the target installation environment and the operational requirements of the hosting organization.

**Prepare the cluster environment:**

1. Prepare the cluster environment by setting up the network and provisioning the nodes and load balancer.
2. Follow the [introduction](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/introduction "mention") documentation to configure the database server.

**Prepare a personalized SonarQube Server package:**

1. On a single application node of the cluster, download and install SonarQube Server DCE, following the usual [introduction](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/introduction "mention") documentation.
2. Add cluster-related parameters to `<sonarqubeHome>/conf/sonar.properties`.
3. This is also a good opportunity to install plugins. Download and place a copy of each plugin JAR in \<sonarqubeHome>`/extensions/plugins`. Be sure to check compatibility with your SonarQube Server version using the [plugin-version-matrix](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/plugins/plugin-version-matrix "mention").
4. Zip the directory `<sonarqubeHome>`. This archive is a customized SonarQube Server DCE package that can be copied to other nodes.

**Test configuration on a single node:**

1. On the application node where you created your Zip package, comment out all cluster-related parameters in `<sonarqubeHome>/conf/sonar.properties`.
2. Configure the load balancer to proxy with single application node.
3. Start server and test access through load balancer.
4. Request license from SonarSource Sales Team.
5. After applying license, you will have a full-featured SonarQube Server system operating on a single node.

**Deploy SonarQube package on other nodes:**

1. Unzip SonarQube Server package on the other four nodes.
2. Configure node-specific parameters on all five nodes in `<sonarqubeHome>/conf/sonar.properties` and ensure application node-specific and search node-specific parameters are properly set.
3. Start all search nodes.
4. After all search nodes are running, start all application nodes.
5. Configure the load balancer to proxy with both application nodes.

### Installing SonarQube Server from the Docker image <a href="#install-sonarqube-from-the-docker-image" id="install-sonarqube-from-the-docker-image"></a>

{% hint style="warning" %}
You should install SonarQube Server DCE using Docker compose on a single Docker host only for test purposes. Sonar recommends running the database, application, and search containers in different Docker hosts for production workloads.
{% endhint %}

The general setup with Docker is the same but is shifted to a Docker-specific terminology.

#### Requirements <a href="#requirements" id="requirements"></a>

**Network**

All containers should be in the same network. This includes search and application nodes. For the best performance, it is advised to check for low latency between the database and the cluster nodes.

**Limits**

The limits of each container depend on the workload that each container has. A good starting point would be:

* cpus: 0.5
* mem\_limit: 4096M
* mem\_reservation: 1024M

The 4Gb mem\_limit should not be lower as this is the minimal value for Elasticsearch.

**Scalability**

Application nodes can be scaled using replicas. This is not the case for the Search nodes as Elasticsearch will not become ready. See the [configure-and-operate-a-cluster](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/configure-and-operate-a-cluster "mention") for more information.

**Volumes**

You’ll use the following volumes in your configuration:

* `sonarqube_data` – In the Docker Compose configuration example in the following section, volumes are shared between replicas in the application nodes, so you don’t need a `sonarqube_data` volume on your application nodes. In the search nodes, the `sonarqube_data` volume contains the Elasticsearch data and helps reduce startup time, so we recommend having a `sonarqube_data` volume on each search node.
* `sonarqube_extensions` – For application nodes, we recommend sharing a common `sonarqube_extensions` volume which contains any plugins you install and the Oracle JDBC driver if necessary.
* `sonarqube_logs` – For both application and search nodes, we recommend sharing a common `sonarqube_logs` volume which contains SonarQube Server logs. The volume will be populated with a new folder depending on the container’s hostname and all logs of this container will be put into this folder. This behavior also happens when a custom log path is specified via the [environment-variables](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/environment-variables "mention").

### Next steps <a href="#next-steps" id="next-steps"></a>

Once you’ve completed these steps, check out the [configure-and-operate-a-cluster](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/configure-and-operate-a-cluster "mention") documentation.

### Post-installation steps <a href="#post-installation" id="post-installation"></a>

You can encrypt sensitive properties stored in `<sonarqubeHome>/conf/sonar.properties`. See [encrypting-settings](https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/encrypting-settings "mention").
