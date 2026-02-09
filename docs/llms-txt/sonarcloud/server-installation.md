# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation.md

# Server installation and setup

- [Introduction](/sonarqube-server/server-installation/introduction.md): This section explains how to install and setup your SonarQube Server.
- [Server components](/sonarqube-server/server-installation/server-components-overview.md): Overview of Java processes run by SonarQube Server and of SonarQube Server database.
- [Installing database](/sonarqube-server/server-installation/installing-the-database.md): Install the SonarQube Server database according to the database engine used: MicrosoftSQL Server, Oracle, PostgreSQL.
- [Server host requirements](/sonarqube-server/server-installation/server-host-requirements.md): This section describes the requirements and recommendations for a machine running SonarQube Server.
- [Pre-installation steps](/sonarqube-server/server-installation/pre-installation.md): The pre-installation steps depend on your operating system.
- [On Linux systems](/sonarqube-server/server-installation/pre-installation/linux.md): Pre-installation steps on SonarQube Server host for the Developer and Enterprise Editions on Linux systems.
- [On Unix-based systems](/sonarqube-server/server-installation/pre-installation/unix.md): Pre-installation steps on SonarQube Server host for the Developer and Enterprise Editions on Unix systems.
- [On macOS systems](/sonarqube-server/server-installation/pre-installation/macos.md): Pre-installation steps on SonarQube Server host for the Developer and Enterprise Editions on macOS systems.
- [Defining a JWT token](/sonarqube-server/server-installation/pre-installation/jwt-token.md): Optional pre-installation step to keep user sessions alive during startup.
- [From ZIP file](/sonarqube-server/server-installation/from-zip-file.md): Installing SonarQube Server Developer or Enterprise Edition from the ZIP file.
- [Installation overview](/sonarqube-server/server-installation/from-zip-file/overview.md): Main steps for installing SonarQube Server from the ZIP file.
- [Basic installation](/sonarqube-server/server-installation/from-zip-file/basic-installation.md): How to install SonarQube Server Developer or Enterprise edition from the ZIP file and perform the basic setup.
- [Advanced setup](/sonarqube-server/server-installation/from-zip-file/advanced-setup.md): Advanced setup when installing SonarQube Server from the ZIP file.
- [Starting / stopping server](/sonarqube-server/server-installation/from-zip-file/starting-stopping-server.md): How to start or stop the server in case of a ZIP installation
- [From the ZIP file](/sonarqube-server/server-installation/from-zip-file/starting-stopping-server/from-zip-file.md): Starting SonarQube Server from the ZIP file
- [Running as a service](/sonarqube-server/server-installation/from-zip-file/starting-stopping-server/running-as-a-service.md): How to install and start SonarQube Server as a service in case of a ZIP installation. The operation depends on your operating system.
- [From Docker image](/sonarqube-server/server-installation/from-docker-image.md): Installing SonarQube Server Developer or Enterprise Edition from the Docker image.
- [Installation overview](/sonarqube-server/server-installation/from-docker-image/installation-overview.md): Main steps for installing SonarQube Server from the Docker image.
- [Prepare the Docker installation](/sonarqube-server/server-installation/from-docker-image/prepare-installation.md): How to prepare the installation of SonarQube Server Developer or Enterprise edition from the Docker image.
- [Set up and start your container](/sonarqube-server/server-installation/from-docker-image/set-up-and-start-container.md): How to set up and start your SonarQube Server container with the Developer or Enterprise edition.
- [Advanced setup](/sonarqube-server/server-installation/from-docker-image/advanced-setup.md): Advanced setup when installing SonarQube Server from the Docker image.
- [Installing on Kubernetes or OpenShift](/sonarqube-server/server-installation/on-kubernetes-or-openshift.md): Installing SonarQube Server Developer or Enterprise Edition on Kubernetes or Openshift.
- [Installation overview](/sonarqube-server/server-installation/on-kubernetes-or-openshift/installation-overview.md): Main steps for installing SonarQube Server on Kubernetes or Openshift.
- [Before you start](/sonarqube-server/server-installation/on-kubernetes-or-openshift/before-you-start.md): Requirements and known limitations of a SonarQube Server deployment on Kubernetes or OpenShift.
- [Customizing Helm chart](/sonarqube-server/server-installation/on-kubernetes-or-openshift/customizing-helm-chart.md): How to perform the most important SonarQube Helm chart customization when working with SonarQube Server.
- [Installing Helm chart](/sonarqube-server/server-installation/on-kubernetes-or-openshift/installing-helm-chart.md): How to install the Helm chart for SonarQube Server’s Developer or Enterprise Edition.
- [Setting up monitoring](/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring.md): Setting up monitoring on a Kubernetes deployment of SonarQube Server.
- [Introduction](/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/introduction.md): If you deploy SonarQube Server on Kubernetes, Prometheus metrics can be collected.
- [Setting up with Prometheus server](/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus.md): This article describes how to use SonarQube’s core integration with Prometheus to collect Prometheus metrics in a Kubernetes deployment.
- [Setting up with Datadog](/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/datadog.md): In case of a Kubernetes deployment, you can use Datadog to collect the metrics provided through the SonarQube Server’s Web API (Openmetrics format).
- [List of Prometheus metrics](/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics.md): List of the SonarQube Server metrics exposed by Prometheus.
- [Encrypting sensitive data](/sonarqube-server/server-installation/on-kubernetes-or-openshift/encrypting-helm-chart-sensitive-data.md): Encrypting sensitive Sonar properties.
- [Network security](/sonarqube-server/server-installation/network-security.md): Enhancing the network security.
- [Securing behind a proxy](/sonarqube-server/server-installation/network-security/securing-behind-proxy.md): Securing SonarQube Server behind a proxy.
- [Network rules](/sonarqube-server/server-installation/network-security/network-rules.md): Defining network rules to enhance the security.
- [Data Center Edition](/sonarqube-server/server-installation/data-center-edition.md): Installing SonarQube Server's Data Center Edition.
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
- [Setting system properties](/sonarqube-server/server-installation/system-properties.md): The system properties are the properties used by SonarQube at startup and not stored in the database.
- [Configuration methods](/sonarqube-server/server-installation/system-properties/configuration-methods.md): The system properties are the properties used by SonarQube at startup and not stored in the database. They can be configured using different methods.
- [List of properties common to all editions](/sonarqube-server/server-installation/system-properties/common-properties.md): This page lists the configurable system properties that are common to all SonarQube editions.
- [List of DCE-specific properties](/sonarqube-server/server-installation/system-properties/dce-specific.md): This page lists the configurable system properties that are specific to the Data Center Edition.
- [Installing plugins](/sonarqube-server/server-installation/plugins.md): Installing plugins for SonarQube Server.
- [Plugin version matrix](/sonarqube-server/server-installation/plugins/plugin-version-matrix.md): This table describes the version of each plugin that is compatible with each version of SonarQube Server.
- [Installing a plugin](/sonarqube-server/server-installation/plugins/install-a-plugin.md): Learn how to install or uninstall a plugin in SonarQube Server.
- [Reference architectures](/sonarqube-server/server-installation/reference-architectures.md): This section describes the architecture of a SonarQube Server instance for different contexts.
- [Up to 10 M LOC](/sonarqube-server/server-installation/reference-architectures/up-to-10m-loc.md): This page describes the architecture of a SonarQube Server instance that will support up to 10 million lines of code under normal usage patterns in a non-high availability setup.
- [Up to 50 M LOC](/sonarqube-server/server-installation/reference-architectures/up-to-50m-loc.md): This architecture describes the setup of a SonarQube Server Enterprise Editon instance that will support up to 50 million lines of code.
