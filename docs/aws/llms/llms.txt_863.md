# Source: https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/llms.txt

# Wickr Enterprise Automated Install Guide

- [What is Wickr Enterprise?](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/what-is-wickr-enterprise.html)
- [Getting started](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/getting-started.html)
- [Connecting to Kubernetes](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/connecting.html)
- [Installing Wickr Enterprise](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/installing.html)
- [Post installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/post-installation.html)
- [Context values](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/context-values.html)
- [Destroying resources](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/destroying-resources.html)
- [Troubleshooting](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/doc-history.html)

## [Custom installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/custom-installation.html)

- [Requirements](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/requirements.html): Before you start to install Wickr Enterprise, verify that the following requirements are met.
- [Architecture](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/architecture.html): Recommended Production Architecture
- [Installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/installation.html)
- [Ingress settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/ingress-settings.html): Ingress Controller
- [Database Settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/database-settings.html): Wickr Enterprise requires a MySQL 8.0 database.
- [S3 File storage](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/s3-file-storage.html): Wickr Enterprise requires an S3 compatible storage service.
- [Persistent volume claim settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/persistent-volume-claim-settings.html): Wickr Enterprise requires Persistent Volume Claims to store stateful data.
- [TLS certificate settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/tls-certificate-settings.html): Upload a PEM certificate and private key for terminating TLS.
- [Calling settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/calling-settings.html)
- [Calling ingress settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/calling-ingress-settings.html): Wickr supports a calling ingress setting, allowing a client to connect to any calling node within the cluster and have the call route to the correct calling server.
- [Kubernetes cluster autoscaler (optional)](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/kubernetes-cluster-autoscaler.html): Kubernetes Cluster Autoscaler is an optional configuration value for the Wickr Enterprise installation.
- [Backups](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/backups.html): Wickr Enterprise utilizes Velero for Backup purposes.
- [Airgap installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/airgap-installation.html): Wickr Enterprise and KOTS both support deployment into a fully airgapped Kubernetes cluster.
- [Security settings](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/security-settings.html): AWS Wickr Enterprise provides configuration settings to enforce an enhanced security context for your deployment.
- [FAQ](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/faq.html): Q: My deployment fails with the following error in helm stderr:


## [Embedded cluster installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/embedded-cluster-overview.html)

- [Getting started](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/getting-started-enterprise-embedded.html): To begin using the Wickr Enterprise embedded cluster option, contact support to receive a license.
- [Requirements](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/embedded-cluster-requirements.html): Before you start to install Wickr Enterprise embedded cluster, verify that the following requirements are met.
- [Standard installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/standard-installation.html): Once you have the download instructions, download the Wickr Enterprise bundle to the destination machine and unpack it.
- [Multi-Node installation](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/multi-node-installation.html): Wickr Enterprise Embedded Cluster Multi-Node installations provide an option for Embedded Cluster users to separate the Wickr Calling and Wickr Messaging workloads on to different physical machines.
- [KOTS admin console configuration](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/kots-admin-console-config.html): The KOTS admin console initially uses a self-signed certificate, which you'll need to allow as an exception in your browser.
- [Additional installation requirements](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/common-installation-requirements.html): IP Hostname Installations
- [Troubleshooting embedded cluster installations](https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/troubleshooting-installation.html): All instances of these troubleshooting steps assume you have shell access to the instance running the Wickr Embedded Cluster installation and have run the ./wickr-enterprise-ha shell command to be able to interact with the Kubernetes installation directly.
