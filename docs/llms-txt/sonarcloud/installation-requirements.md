# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/installation-requirements.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/installation-requirements.md

# Installation requirements

As a Data Center Edition subscriber, Sonar will assist with the setup and configuration of your cluster. Get in touch with your account manager to receive appropriate onboarding resources.

### Limitations <a href="#limitations" id="limitations"></a>

See [#limitations](https://docs.sonarsource.com/sonarqube-server/server-host-requirements#limitations "mention").

### Cluster nodes <a href="#network" id="network"></a>

You need a minimum of five servers (two application nodes and three search nodes) to form a SonarQube Server application cluster. Servers can be virtual machines; it is not necessary to use physical machines. You can also add application nodes to increase computing capabilities.

We recommend having one machine for each node to be resilient to failures. To maintain an even higher level of availability, each of your three search nodes can be located in a separate availability zone *within the same region*.

The operating system requirements for servers are available on the [server-host-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements "mention") page.

All application nodes should be identical in terms of hardware and software. Similarly, all search nodes should be identical to each other. Application and search nodes, however, can differ from one another. Generally, search nodes are configured with more CPU and RAM than application nodes.

Search nodes can be located in different availability zones, but they must be in the same region. In this case, each search node should be located in a separate availability zone to maintain availability in the event of a failure in one zone. SSDs perform significantly better than HDDs for these nodes.

#### Example machines <a href="#example-machines" id="example-machines"></a>

Here are the machines we used to perform our validation with a 200M issues database. You can use this as a minimum recommendation to build your cluster.

* App Node made of [Amazon EC2 general purpose xlarge](https://aws.amazon.com/ec2/instance-types/): 4 vCPUs, 16GB RAM
* Search Node made of [Amazon EC2 general purpose 2xlarge](https://aws.amazon.com/ec2/instance-types/): 8 vCPUs, 32GB RAM - 16GB allocated to Elasticsearch. SSDs perform significantly better than HDDs for these nodes.

### Docker containers <a href="#docker-containers" id="docker-containers"></a>

In case you install your SonarQube Server from the Docker images:

* Sonar recommends running the database, application, and search containers in different Docker hosts for production workloads. You should install on a single Docker host only for test purposes.
* All containers should be in the same network. This includes search and application nodes. For the best performance, it is advised to check for low latency between the database and the cluster nodes.
* The limits of each container depend on the workload that each container has. A good starting point would be:
  * cpus: 0.5
  * mem\_limit: 4096M\
    4Gb mem\_limit should is the minimal value for Elasticsearch.
  * mem\_reservation: 1024M

### Database server <a href="#database-server" id="database-server"></a>

Supported database systems are available on the [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention") page.

### TCP networks <a href="#tcp-networks" id="tcp-networks"></a>

There are three TCP networks to configure:

* the network of application nodes that relies on Hazelcast.
* the network used for Elasticsearch internal communication between search nodes (`es` properties).
* the network between application nodes and search nodes (`search` properties).

[Hazelcast](https://hazelcast.org/) is used to manage the communication between the cluster’s application nodes. You don’t need to install it yourself, it’s provided out of the box.

### Load balancer <a href="#load-balancer" id="load-balancer"></a>

The installing organization must supply the load balancer.

Sonar does not provide specific recommendations for reverse proxy / load balancer or solution-specific configuration. The general requirements are:

* Ability to balance HTTP requests (load) between the application nodes configured in the cluster.
* If terminating HTTPS, meets the requirements set out in [Operating the server](https://app.gitbook.com/s/I10pmJWeVVXYITlQJllp/setup-and-upgrade/operating-the-server "mention").
* No requirement to preserve or sticky sessions; this is handled by the built-in JWT mechanism.
* Ability to check for node health for routing.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [dce-topology](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/dce-topology "mention")
* [pre-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/pre-installation "mention")
* [from-zip-file](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/from-zip-file "mention")
* [on-kubernetes-or-openshift](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift "mention")
* **Configuring network security features:**
  * [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/securing-behind-proxy "mention")
  * [elasticsearch-security-features](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/elasticsearch-security-features "mention")
  * [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/network-rules "mention")
* [starting-stopping-cluster](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster "mention")
* [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention")
