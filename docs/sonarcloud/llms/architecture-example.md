# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example.md

# Disaster recovery architecture example with Azure resources

In the disaster recovery architecture example described below, Azure Kubernetes Service (AKS) is used, but the overall concept can be adapted to Google Cloud Platform (GCP) or Amazon Web Services (AWS) with a few modifications.

For this architecture example, you need the Azure subscription.

### Architecture overview <a href="#overview" id="overview"></a>

In our setup example, the disaster architecture consists of:

* Azure Front Door.
* Two AKS clusters (with two ingresses): your SonarQube primary and replica clusters.
* Azure Database for PostgreSQL flexible server with geo-replication and a writer endpoint.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/70a1gXco42mleutuyXOl/sonarqube-data-center-edition-disaster-recovery-architecture.png" alt="The disaster recovery architecture example consists of and Azure Front Door, two AKS clusters (with two ingresses), an Azure Database for PostgreSQL"><figcaption></figcaption></figure>

{% hint style="warning" %}
The architecture presented here represents an Active-Cold Standby configuration as SonarQube Server currently does not support access to a database in read-only format for Active/Standby or Active/Active configurations.
{% endhint %}

### Disaster recovery mechanism <a href="#mechanism" id="mechanism"></a>

Azure Front Door provides a mechanism for global traffic routing and failover, which can be used in conjunction with DNS to ensure high availability:

* An endpoint is used for an origin group consisting of the two ingresses from your SonarQube primary and replica clusters.
* Priority routing is used to ensure high availability by directing traffic to your primary cluster (highest priority). If the primary cluster is unavailable, traffic automatically fails over to the replica cluster.
* An alert can be set up for your origin group that triggers whenever your primary cluster health goes under a specific threshold. The alert can optionally send an email to the SonarQube Server Administrator or start an automation runbook to perform additional actions. For example, the runbook powers on the replica cluster site in case of an outage of the primary cluster site.

The database failover process is entirely automated by the Azure Database for PostgreSQL flexible server.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [deploy-databases](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases "mention")
* [set-up-clusters-on-aks](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks "mention")
* [configure-azure-front-door](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door "mention")
* [test-failover-scenarios](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios "mention")
