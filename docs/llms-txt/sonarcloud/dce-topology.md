# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/dce-topology.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/dce-topology.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/dce-topology.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/dce-topology.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/dce-topology.md

# DCE topology

As a DCE subscriber, Sonar will assist with the setup and configuration of your cluster. Get in touch with your account manager to receive appropriate onboarding resources.

The DCE consists of:

* Application nodes responsible for handling web requests from users (Web process) and handling analysis reports (Compute Engine process). You can add application nodes to increase computing capabilities.
* Search nodes that host the Elasticsearch process that will store data indices. The search nodes build an Elasticsearch cluster. Unicast discovery is used in this cluster.
* A reverse proxy / load balancer to load balance traffic between the two application nodes. The installing organization must supply this hardware or software component.
* PostgreSQL, Oracle, or Microsoft SQL Server database server. This software must be supplied by the installing organization.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/RTRoF8FqhdTiuZy0qUr2/sonarqube-data-center-edition-topology_Q0043.png" alt="DCE consists of application nodes, search nodes, database. A reverse proxy / load balancer is used to load balance the traffic between application nodes."><figcaption></figcaption></figure>

We recommend having one machine for each node to be resilient to failures. To maintain an even higher level of availability, each of your three search nodes can be located in a separate availability zone *within the same region*.

For more information about the SonarQube Server processes (Sonar, Web, Compute Engine, and Elasticsearch), see [server-components-overview](https://docs.sonarsource.com/sonarqube-server/server-installation/server-components-overview "mention").

### Default topology <a href="#default-topology" id="default-topology"></a>

The default topology of the Data Center Edition corresponds to the minimum topology and comprises:

* Two application nodes.
* Three search nodes.

With this topology, one application node and one search node can be lost without impacting users. Below is a diagram of the default topology.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/jogE753tkpRsnlyeNuCB/3555755a63635e0fdb9e75a54f4cd5b3df280216.png" alt="Default topology diagram of SonarQube Server installed as a cluster"><figcaption></figcaption></figure>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [installation-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/installation-requirements "mention")
* [pre-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/pre-installation "mention")
* [from-zip-file](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/from-zip-file "mention")
* [on-kubernetes-or-openshift](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift "mention")
* **Configuring network security features:**
  * [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/securing-behind-proxy "mention")
  * [elasticsearch-security-features](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/elasticsearch-security-features "mention")
  * [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/network-rules "mention")
* [starting-stopping-cluster](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster "mention")
