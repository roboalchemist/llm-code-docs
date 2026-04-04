# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/server/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/dce/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/server/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/dce/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/server/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/dce/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/server/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/before-you-start.md

# Before you start

### Installation requirements <a href="#installation-requirements" id="installation-requirements"></a>

* The SonarQube Server Helm chart comes with default values for [CPU and memory requests and limits](https://artifacthub.io/packages/helm/sonarqube/sonarqube#cpu-and-memory-settings). Depending on your system, you may have to adjust them.
* See the [Helm chart documentation](https://artifacthub.io/packages/helm/sonarqube/sonarqube) for information about the supported Kubernetes and OpenShift versions.

### Production use case <a href="#prod-use-case" id="prod-use-case"></a>

In a production use case:

* Ensure that the SonarQube Server Helm chart runs in a full restricted namespace (see [#ensuring-restricted-level](https://docs.sonarsource.com/sonarqube-server/server-installation/customizing-helm-chart#ensuring-restricted-level "mention")).
* Use your own Ingress controllers.\
  Ingress controllers are critical Kubernetes components, we advise users to install their own.
* Use your own database.

For more information, see the [production use case guidelines](https://artifacthub.io/packages/helm/sonarqube/sonarqube#production-use-case) in the Helm chart documentation, which we strongly recommend following.

{% hint style="danger" %}
The PostgreSQL data dependency was removed in SonarQube Server 2026.1. If you used PostgreSQL for testing purposes, you can rely on the H2 database by default. For production, migrate your data to a standalone database prior to the SonarQube Server 2026.1 update. See the[ Helm chart](https://artifacthub.io/packages/helm/sonarqube/sonarqube#upgrade) documentation for more details.
{% endhint %}

### Known limitations <a href="#known-limitations" id="known-limitations"></a>

As SonarQube Server is intended to be run anywhere, there are some drawbacks that are currently known when operating in Kubernetes. This list is not comprehensive, but something to keep in mind and points for us to improve on.

#### Readiness and startup delays <a href="#readiness-and-startup-delays" id="readiness-and-startup-delays"></a>

When persistence is disabled, SonarQube Server startup takes significantly longer as the Elasticsearch indexes need to be rebuilt. As this delay depends on the amount of data in your SonarQube Server instance, the values for the startup/readiness and liveness probes need to be adjusted to your environment. We also recommend looking at the default limits for the SonarQube Server deployment, as the amount of CPU available to SonarQube Server also impacts the startup time.

#### Problems with Azure Fileshare PVC <a href="#problems-with-azure-fileshare-pvc" id="problems-with-azure-fileshare-pvc"></a>

Currently, there is a known limitation when working with AKS due to the way Azure Fileshare uses NTFS, which cannot handle the file system permissions and properties that SonarQube Server relies on. We recommend using another storage class for persistence on AKS.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [installation-overview](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installation-overview "mention")
* [customizing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/customizing-helm-chart "mention")
* [installing-helm-chart](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installing-helm-chart "mention")
* [set-up-monitoring](https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring "mention")
* Installing Data Center Edition on Kubernetes: [on-kubernetes-or-openshift](https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift "mention")
