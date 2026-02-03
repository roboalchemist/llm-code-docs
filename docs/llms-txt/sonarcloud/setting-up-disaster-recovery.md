# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery.md

# Setting up disaster recovery

To explain the disaster recovery setup in SonarQube Server’s Data Center Edition (DCE) deployed on Kubernetes, we use the example of a system deployed on Azure Kubernetes Service (AKS). But the overall concept can be adapted to Google Cloud Platform (GCP) or Amazon Web Services (AWS) with a few modifications.

For the setup explained in this section, you need a basic understanding of Azure Cloud Services.

{% hint style="info" %}
A forced Elasticsearch reindex is required after a failover event of the Kubernetes cluster hosting the SonarQube DCE server.
{% endhint %}

{% content-ref url="setting-up-disaster-recovery/architecture-example" %}
[architecture-example](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example)
{% endcontent-ref %}

{% content-ref url="setting-up-disaster-recovery/deploy-databases" %}
[deploy-databases](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases)
{% endcontent-ref %}

{% content-ref url="setting-up-disaster-recovery/set-up-clusters-on-aks" %}
[set-up-clusters-on-aks](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks)
{% endcontent-ref %}

{% content-ref url="setting-up-disaster-recovery/configure-azure-front-door" %}
[configure-azure-front-door](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door)
{% endcontent-ref %}

{% content-ref url="setting-up-disaster-recovery/test-failover-scenarios" %}
[test-failover-scenarios](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios)
{% endcontent-ref %}
