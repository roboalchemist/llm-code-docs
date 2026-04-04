# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/data-center-edition.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition.md

# Data Center Edition

- [Introduction](/sonarqube-server/server-installation/data-center-edition/introduction.md): Content of the Data Center Edition (DCE) installation section.
- [DCE topology](/sonarqube-server/server-installation/data-center-edition/dce-topology.md): The Data Center Edition (DCE) allows SonarQube Server to run in a clustered configuration to make it resilient to failures.
- [Installation requirements](/sonarqube-server/server-installation/data-center-edition/installation-requirements.md): General requirements, recommendations, and limitations for SonarQube Server’s cluster. Additional requirements specific to an installation type may be mentioned in the respective installation section.
- [Pre-installation steps](/sonarqube-server/server-installation/data-center-edition/pre-installation.md): Steps to perform before installing Data Center Edition (DCE).
- [Installing from ZIP file](/sonarqube-server/server-installation/data-center-edition/from-zip-file.md): Installing SonarQube Server's Data Center Edition (DCE) form the ZIP file.
- [Installing on Kubernetes or Openshift](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift.md): Installating SonarQube Server's Data Center Edition on Kubernetes or Openshift.
- [Installation overview](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/overview.md): Your entry point to deploy the Data Center Edition (DCE) on Kubernetes or OpenShift.
- [Before you start](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/before-you-start.md): This page describes the requirements and known limitations of a SonarQube Server’s Data Center Edition (DCE) deployment on Kubernetes or Openshift.
- [Customizing the DCE Helm chart](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/customizing-helm-chart.md): How to perform the most important customization of the Helm chart for SonarQube Server’s Data Center Edition (DCE).
- [Setting up autoscaling](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-autoscaling.md): With Kubernetes’ Horizontal Pod Autoscaling (HPA), you can automatically scale your SonarQube Server out and in, resolving any performance issues you may have.
- [Setting up disaster recovery](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery.md): How to set up a disaster recovery for SonarQube Server’s Data Center Edition (DCE) deployed on Kubernetes.
- [Disaster recovery architecture example with Azure resources](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/architecture-example.md): Example of disaster recovery architecture used for SonarQube Server’s Data Center Edition (DCE) deployed on Kubernetes.
- [Step 1: Deploy the primary and replica databases](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/deploy-databases.md): The first step of the disaster recovery setup for the Data Center Edition (DCE) deployed on Kubernetes consists in deploying the primary and replica databases.
- [Step 2: Set up the primary and replica clusters on AKS](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/set-up-clusters-on-aks.md): The second step of the disaster recovery setup for the Data Center Edition (DCE) on Kubernetes consists in setting up the primary and replica clusters.
- [Step 3: Configure the Azure Front Door](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/configure-azure-front-door.md): The third step of the disaster recovery setup for the Data Center Edition (DCE) deployed on Kubernetes consists in configuring the Azure Front Door.
- [Step 4: Test failover scenarios](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/setting-up-disaster-recovery/test-failover-scenarios.md): How to test the failover of the Data Center Edition (DCE) deployed on Kubernetes.
- [Installing the DCE Helm chart](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-helm-repo.md): SonarQube Data Center Edition (DCE) can be installed from a customized SonarQube Server Helm chart.
- [Installing from Google Cloud Platform](/sonarqube-server/server-installation/data-center-edition/on-kubernetes-or-openshift/installing-from-gcp.md): SonarQube Data Center Edition (DCE) can be deployed on Kubernetes through the Google Marketplace.
- [Network security](/sonarqube-server/server-installation/data-center-edition/network-security.md): Enhancing network security for your Data Center Edition.
- [Securing behind a proxy](/sonarqube-server/server-installation/data-center-edition/network-security/securing-behind-proxy.md): It is recommended to run SonarQube behind a proxy, if it should be accessible from outside.
- [Elasticsearch security features](/sonarqube-server/server-installation/data-center-edition/network-security/elasticsearch-security-features.md): How to to set up Elasticsearch security features.
- [Network rules](/sonarqube-server/server-installation/data-center-edition/network-security/network-rules.md): Defining network rules to enhance the security.
- [Starting and stopping cluster](/sonarqube-server/server-installation/data-center-edition/starting-stopping-cluster.md): How to start and stop your Data Center Edition's cluster.
