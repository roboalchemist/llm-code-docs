# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/starting-stopping-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/starting-stopping-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/starting-stopping-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/starting-stopping-cluster.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster.md

# Starting and stopping cluster

{% hint style="info" %}
There is no way to perform actions on the cluster from a central app - all operations must be done manually on each node of the cluster.
{% endhint %}

### Start the cluster <a href="#start-cluster" id="start-cluster"></a>

To start a cluster, you need to follow these steps in order:

1. Start the search nodes.
2. Start the application nodes.

### Stop the cluster <a href="#stop-cluster" id="stop-cluster"></a>

To stop a cluster, you need to follow these steps in order:

1. Stop the application nodes.
2. Stop the search nodes.

### Start or stop a node <a href="#start-stop-node" id="start-stop-node"></a>

You can start or stop a single node in the same way as starting and stopping an instance using a single server. By default, it’s a graceful shutdown where no new analysis report processing can start, but the tasks in progress are allowed to finish.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [dce-topology](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/dce-topology "mention")
* [installation-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/installation-requirements "mention")
* [pre-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/pre-installation "mention")
* [from-zip-file](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/from-zip-file "mention")
* [on-kubernetes-or-openshift](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift "mention")
* **Configuring network security features:**
  * [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/securing-behind-proxy "mention")
  * [elasticsearch-security-features](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/elasticsearch-security-features "mention")
  * [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/network-rules "mention")
