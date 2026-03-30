# Stackstate Documentation

Source: https://archivedocs.stackstate.com/llms-full.txt

---

# StackState docs!

**These documentation pages cover all functionality in the StackState product**.

### Get started

Visit the [quick start guide page](https://docs.stackstate.com/get-started/k8s-quick-start-guide).

## Can't find something?

**Search for it!** Use the search bar on the top right. If you believe any documentation is missing, please let us know on the [StackState support site](http://support.stackstate.com/).

## Troubleshooting and support

Any questions? We love to help! Find our support team on the [StackState support site](http://support.stackstate.com/).


# Docs for all StackState products

Select your version of StackState to jump to the associated documentation.

### Kubernetes troubleshooting

Use StackState to troubleshoot your Kubernetes cluster.

🚀 [StackState docs](https://docs.stackstate.com/)

### StackState Self-hosted

Use StackState Self-hosted to observe an extensive set of technologies that originate either in your own data centers or in the cloud.

↗️ [**StackState Self-hosted v5.1 docs**](https://docs.stackstate.com/v/5.1/latest) **- latest self-hosted release!**

↗️ [StackState Self-hosted v5.0 docs](https://docs.stackstate.com/v/5.0/)

↗️ [StackState Self-hosted v4.6 docs](https://docs.stackstate.com/v/4.6/)

### StackState SaaS

Use StackState SaaS to observe cloud technologies, such as Kubernetes and AWS services.

↗️ [StackState SaaS docs](https://docs.stackstate.com/v/stackstate-saas/)

{% hint style="success" %}
🔒 StackState is SOC2/3 certified. [Learn more](https://www.stackstate.com/compliance)
{% endhint %}


# Quick start guide

StackState v6.0

## StackState quick start guides

### Overview

When your StackState SaaS instance has been set up and configured, you will receive an email from StackState with the required login details. This quick start guide will help you get started and get your own data into your StackState SaaS instance.

To integrate your cluster(s) with StackState you can follow one of these guides for your appropriate environment.

* [Amazon EKS](#amazon-eks)
* [Azure AKS](#azure-aks)
* [Google GKE](#google-gke)
* [Kubernetes](#kubernetes)
* [KOPS](#kops)
* [OpenShift](#openshift)
* [Self-hosted](#self-hosted)

***

## Kubernetes

Set up a Kubernetes integration to collect topology, events, logs, change and metrics data from a Kubernetes cluster and make this available in StackState.

#### Supported versions

| Supported Kubernetes Version |
| ---------------------------- |
| Kubernetes 1.30              |
| Kubernetes 1.29              |
| Kubernetes 1.28              |
| Kubernetes 1.27              |
| Kubernetes 1.26              |
| Kubernetes 1.25              |
| Kubernetes 1.24              |
| Kubernetes 1.23              |
| Kubernetes 1.22              |
| Kubernetes 1.21              |

#### Supported runtime

| Supported runtime |
| ----------------- |
| Docker            |
| ContainerD        |
| CRI-O             |

#### Prerequisites for Kubernetes

To set up a StackState Kubernetes integration you need to have:

* An up-and-running Kubernetes Cluster.
* A recent version of Helm 3.
* A user with the permission to `create privileged pods`, `ClusterRoles` and `ClusterRoleBindings`:
  * ClusterRole and ClusterRoleBinding are needed to grant StackState Agents permissions to access the Kubernetes API.
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

#### Set up a Kubernetes integration

{% hint style="warning" %}
Before you begin, check the [prerequisites for Kubernetes](#prerequisites-for-kubernetes).
{% endhint %}

To get data from a Kubernetes cluster into StackState, follow the steps described below:

1. Add the StackState helm repository to the local helm client:

   ```buildoutcfg
   helm repo add stackstate https://helm.stackstate.io
   helm repo update
   ```
2. In the StackState UI, open the main menu by clicking in the top left of the screen and go to `StackPacks` > `Integrations` > `Kubernetes`.
3. Install a new instance of the Kubernetes StackPack:
   * Specify a **Kubernetes Cluster Name**
     * This name will be used to identify the cluster in StackState
   * Click **install**.
4. Deploy the StackState Agent, Cluster Agent, Checks Agent and kube-state-metrics on your Cluster using the helm command provided in the StackState UI after you have installed the StackPack.
   * Once the Agents have been deployed, they will begin collecting data and push this to StackState

{% hint style="warning" %}
When running on a self-hosted air-gapped environment prepare the agent installation first with the [air-gapped instructions](https://archivedocs.stackstate.com/self-hosted-setup/no_internet/agent_install).
{% endhint %}

***

## OpenShift

Set up an OpenShift integration to collect topology, events, logs, change and metrics data from a OpenShift cluster and make this available in StackState.

#### Supported versions

| OpenShift Version | Supported Kubernetes Version | OpenShift End of Support |
| ----------------- | ---------------------------- | ------------------------ |
| OpenShift 4.12    | Kubernetes 1.25              | July 17, 2024            |
| OpenShift 4.11    | Kubernetes 1.24              | February 10, 2024        |
| OpenShift 4.10    | Kubernetes 1.23              | September 10, 2023       |
| OpenShift 4.9     | Kubernetes 1.22              | April 18, 2023           |

#### Supported runtime

| Supported runtime |
| ----------------- |
| Docker            |
| ContainerD        |
| CRI-O             |

#### Prerequisites for OpenShift

To set up a StackState OpenShift integration you need to have:

* An up-and-running OpenShift Cluster.
* A recent version of Helm 3.
* A user with the permission to `create privileged pods`, `ClusterRoles` and `ClusterRoleBindings`:
  * ClusterRole and ClusterRoleBinding are needed to grant StackState Agents permissions to access the Kubernetes API.
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

#### Set up an OpenShift integration

{% hint style="warning" %}
Before you begin, check the [prerequisites for Kubernetes](#prerequisites-for-openshift).
{% endhint %}

To get data from a Kubernetes cluster into StackState, follow the steps described below:

1. Add the StackState helm repository to the local helm client:

   ```buildoutcfg
   helm repo add stackstate https://helm.stackstate.io
   helm repo update
   ```
2. In the StackState UI, open the main menu by clicking in the top left of the screen and go to `StackPacks` > `Integrations` > `Kubernetes`.
3. Install a new instance of the Kubernetes StackPack:
   * Specify a **Kubernetes Cluster Name**
     * This name will be used to identify the cluster in StackState
   * Click **install**.
4. Deploy the StackState Agent, Cluster Agent, Checks Agent and kube-state-metrics on your Cluster using the helm command provided in the StackState UI after you have installed the StackPack.
   * Once the Agents have been deployed, they will begin collecting data and push this to StackState

***

## Amazon EKS

Set up an Amazon EKS integration to collect topology, events, logs, change and metrics data from an Amazon EKS cluster and make this available in StackState.

#### Supported versions

| Kubernetes version | Amazon EKS release | Amazon EKS End of Support | Amazon EKS End of Extended Support |
| ------------------ | ------------------ | ------------------------- | ---------------------------------- |
| 1.30               | May 23, 2024       | July 23, 2025             | July 23, 2026                      |
| 1.29               | January 23, 2024   | March 23, 2025            | March 23, 2026                     |
| 1.28               | September 26, 2023 | November 01, 2024         | November 26, 2025                  |
| 1.27               | May 24, 2023       | July 2024                 | July 24, 2025                      |
| 1.26               | April 11, 2023     | June 2024                 | June 11, 2025                      |
| 1.25               | February 21, 2023  | May 2024                  | May 1, 2025                        |
| 1.24               | November 15, 2022  | January 2024              | January 31, 2025                   |
| 1.23               | August 11, 2022    | October 11, 2023          | October 11, 2024                   |
| 1.22               | April 4, 2022      | June 4, 2023              | September 1, 2024                  |
| 1.21               | July 19, 2021      | February 15, 2023         | July 15, 2024                      |
| 1.20               | May 18, 2021       | November 1, 2022          | N/A                                |
| 1.19               | February 16, 2021  | August 1, 2022            | N/A                                |
| 1.18               | October 13, 2020   | August 15, 2022           | N/A                                |

#### Supported runtime

| Supported runtime |
| ----------------- |
| Docker            |
| ContainerD        |
| CRI-O             |

#### Prerequisites for Amazon EKS

To set up a StackState Amazon EKS integration you need to have:

* An up-and-running Amazon EKS Cluster.
* A recent version of Helm 3.
* A user with the permission to `create privileged pods`, `ClusterRoles` and `ClusterRoleBindings`:
  * ClusterRole and ClusterRoleBinding are needed to grant StackState Agents permissions to access the Kubernetes API.
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

#### Set up a Amazon EKS integration

{% hint style="warning" %}
Before you begin, check the [prerequisites for Kubernetes](#prerequisites-for-amazon-eks).
{% endhint %}

To get data from a Kubernetes cluster into StackState, follow the steps described below:

1. Add the StackState helm repository to the local helm client:

   ```buildoutcfg
   helm repo add stackstate https://helm.stackstate.io
   helm repo update
   ```
2. In the StackState UI, open the main menu by clicking in the top left of the screen and go to `StackPacks` > `Integrations` > `Kubernetes`.
3. Install a new instance of the Kubernetes StackPack:
   * Specify a **Kubernetes Cluster Name**
     * This name will be used to identify the cluster in StackState
   * Click **install**.
4. Deploy the StackState Agent, Cluster Agent, Checks Agent and kube-state-metrics on your Cluster using the helm command provided in the StackState UI after you have installed the StackPack.
   * Once the Agents have been deployed, they will begin collecting data and push this to StackState

***

## Google GKE

Set up a Google GKE integration to collect topology, events, logs, change and metrics data from an Google GKE cluster and make this available in StackState.

#### Supported versions

| Kubernetes Version | Google GKE release | Google GKE End of Support |
| ------------------ | ------------------ | ------------------------- |
| 1.30               | June, 2024         | August 15, 2025           |
| 1.29               | January 25, 2024   | March 21, 2025            |
| 1.28               | December 4, 2023   | February 4, 2025          |
| 1.27               | June 14, 2023      | August 31, 2024           |
| 1.26               | April 14, 2023     | June 30, 2024             |

#### Supported runtime

| Supported runtime |
| ----------------- |
| Docker            |
| ContainerD        |
| CRI-O             |

#### Prerequisites for Google GKE

To set up a StackState Google GKE integration you need to have:

* An up-and-running Google GKE Cluster.
* A recent version of Helm 3.
* A user with the permission to `create privileged pods`, `ClusterRoles` and `ClusterRoleBindings`:
  * ClusterRole and ClusterRoleBinding are needed to grant StackState Agents permissions to access the Kubernetes API.
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

#### Set up a Google GKE integration

{% hint style="warning" %}
Before you begin, check the [prerequisites for Kubernetes](#prerequisites-for-amazon-eks).
{% endhint %}

To get data from a Kubernetes cluster into StackState, follow the steps described below:

1. Add the StackState helm repository to the local helm client:

   ```buildoutcfg
   helm repo add stackstate https://helm.stackstate.io
   helm repo update
   ```
2. In the StackState UI, open the main menu by clicking in the top left of the screen and go to `StackPacks` > `Integrations` > `Kubernetes`.
3. Install a new instance of the Kubernetes StackPack:
   * Specify a **Kubernetes Cluster Name**
     * This name will be used to identify the cluster in StackState
   * Click **install**.
4. Deploy the StackState Agent, Cluster Agent, Checks Agent and kube-state-metrics on your Cluster using the helm command provided in the StackState UI after you have installed the StackPack.
   * Once the Agents have been deployed, they will begin collecting data and push this to StackState

***

## Azure AKS

Set up an Azure AKS integration to collect topology, events, logs, change and metrics data from an Azure AKS cluster and make this available in StackState.

#### Supported versions

| Kubernetes Version | Azure AKS release | Azure AKS End of Support |
| ------------------ | ----------------- | ------------------------ |
| 1.30               | June 2024         | Not known when published |
| 1.29               | March 18, 2024    | Jan 31, 2025             |
| 1.28               | November 7, 2023  | November 30, 2024        |
| 1.27               | August 16, 2023   | July 31, 2024            |

#### Supported runtime

| Supported runtime |
| ----------------- |
| Docker            |
| ContainerD        |
| CRI-O             |

#### Prerequisites for Azure AKS

To set up a StackState Azure AKS integration you need to have:

* An up-and-running Azure AKS Cluster.
* A recent version of Helm 3.
* A user with the permission to `create privileged pods`, `ClusterRoles` and `ClusterRoleBindings`:
  * ClusterRole and ClusterRoleBinding are needed to grant StackState Agents permissions to access the Kubernetes API.
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

#### Set up a Azure AKS integration

{% hint style="warning" %}
Before you begin, check the [prerequisites for Kubernetes](#prerequisites-for-amazon-eks).
{% endhint %}

To get data from a Kubernetes cluster into StackState, follow the steps described below:

1. Add the StackState helm repository to the local helm client:

   ```buildoutcfg
   helm repo add stackstate https://helm.stackstate.io
   helm repo update
   ```
2. In the StackState UI, open the main menu by clicking in the top left of the screen and go to `StackPacks` > `Integrations` > `Kubernetes`.
3. Install a new instance of the Kubernetes StackPack:
   * Specify a **Kubernetes Cluster Name**
     * This name will be used to identify the cluster in StackState
   * Click **install**.
4. Deploy the StackState Agent, Cluster Agent, Checks Agent and kube-state-metrics on your Cluster using the helm command provided in the StackState UI after you have installed the StackPack.
   * Once the Agents have been deployed, they will begin collecting data and push this to StackState

***

## KOPS

Set up a KOPS integration to collect topology, events, logs, change and metrics data from an KOPS cluster and make this available in StackState.

#### Supported versions

| Supported Kubernetes Version |
| ---------------------------- |
| Kubernetes 1.30              |
| Kubernetes 1.29              |
| Kubernetes 1.28              |
| Kubernetes 1.27              |
| Kubernetes 1.26              |
| Kubernetes 1.25              |
| Kubernetes 1.24              |
| Kubernetes 1.23              |
| Kubernetes 1.22              |
| Kubernetes 1.21              |
| Kubernetes 1.20              |
| Kubernetes 1.19              |
| Kubernetes 1.18              |
| Kubernetes 1.17              |
| Kubernetes 1.16              |

#### Supported runtime

| Supported runtime |
| ----------------- |
| Docker            |
| ContainerD        |
| CRI-O             |

#### Prerequisites for KOPS

To set up a StackState KOPS integration you need to have:

* An up-and-running KOPS Cluster.
* A recent version of Helm 3.
* A user with the permission to `create privileged pods`, `ClusterRoles` and `ClusterRoleBindings`:
  * ClusterRole and ClusterRoleBinding are needed to grant StackState Agents permissions to access the Kubernetes API.
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

#### Set up a KOPS integration

{% hint style="warning" %}
Before you begin, check the [prerequisites for Kubernetes](#prerequisites-for-amazon-eks).
{% endhint %}

To get data from a Kubernetes cluster into StackState, follow the steps described below:

1. Add the StackState helm repository to the local helm client:

   ```buildoutcfg
   helm repo add stackstate https://helm.stackstate.io
   helm repo update
   ```
2. In the StackState UI, open the main menu by clicking in the top left of the screen and go to `StackPacks` > `Integrations` > `Kubernetes`.
3. Install a new instance of the Kubernetes StackPack:
   * Specify a **Kubernetes Cluster Name**
     * This name will be used to identify the cluster in StackState
   * Click **install**.
4. Deploy the StackState Agent, Cluster Agent, Checks Agent and kube-state-metrics on your Cluster using the helm command provided in the StackState UI after you have installed the StackPack.
   * Once the Agents have been deployed, they will begin collecting data and push this to StackState

***

## Self-hosted

Set up a Self-hosted integration to collect topology, events, logs, change and metrics data from an Self-hosted cluster and make this available in StackState.

#### Supported versions

| Supported Kubernetes Version |
| ---------------------------- |
| Kubernetes 1.30              |
| Kubernetes 1.29              |
| Kubernetes 1.28              |
| Kubernetes 1.27              |
| Kubernetes 1.26              |
| Kubernetes 1.25              |
| Kubernetes 1.24              |
| Kubernetes 1.23              |
| Kubernetes 1.22              |
| Kubernetes 1.21              |
| Kubernetes 1.20              |
| Kubernetes 1.19              |
| Kubernetes 1.18              |
| Kubernetes 1.17              |
| Kubernetes 1.16              |

#### Supported runtime

| Supported runtime |
| ----------------- |
| Docker            |
| ContainerD        |
| CRI-O             |

#### Prerequisites for Self-hosted

To set up a StackState Self-hosted integration you need to have:

* An up-and-running Self-hosted Cluster.
* A recent version of Helm 3.
* A user with the permission to `create privileged pods`, `ClusterRoles` and `ClusterRoleBindings`:
  * ClusterRole and ClusterRoleBinding are needed to:
    * Grant StackState Agents permissions to access the Kubernetes API
    * Generate a secret for the mutating validation webhook which is part of [request tracing](https://archivedocs.stackstate.com/agent/k8sts-agent-request-tracing)
  * StackState Agents need to run in a privileged pod to be able to gather information on network connections and host information.

#### Set up a self-hosted integration

{% hint style="warning" %}
Before you begin, check the [prerequisites for Kubernetes](#prerequisites-for-amazon-eks).
{% endhint %}

To get data from a Kubernetes cluster into StackState, follow the steps described below:

1. Add the StackState helm repository to the local helm client:

   ```buildoutcfg
   helm repo add stackstate https://helm.stackstate.io
   helm repo update
   ```
2. In the StackState UI, open the main menu by clicking in the top left of the screen and go to `StackPacks` > `Integrations` > `Kubernetes`.
3. Install a new instance of the Kubernetes StackPack:
   * Specify a **Kubernetes Cluster Name**
     * This name will be used to identify the cluster in StackState
   * Click **install**.
4. Deploy the StackState Agent, Cluster Agent, Checks Agent and kube-state-metrics on your Cluster using the helm command provided in the StackState UI after you have installed the StackPack.
   * Once the Agents have been deployed, they will begin collecting data and push this to StackState

***

### What's next?

* [StackState walk-through](https://archivedocs.stackstate.com/get-started/k8s-getting-started)


# StackState walk-through

StackState v6.0

Hi! So, you've integrated your Kubernetes or OpenShift clusters and you are ready to get started.

After setting up your [integration with Kubernetes](https://archivedocs.stackstate.com/get-started/k8s-quick-start-guide), you can go open the Main menu to explore your resources. You can for example start with the Services.

## Explore your Kubernetes resources

![Main menu](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-19fe937807bace4e776906381983b93d930ca9ec%2Fk8s-quick-start-menu.png?alt=media)

This brings you to the service overview which shows all services running in your clusters. If you click any of the other items underneath Kubernetes you will go to the overview page of that type of resource. It will show all resources of that type in all clusters and all namespaces at first.

![Services overview](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-2d3ea34ee6dec527c570f5f1c7d01257df8fd418%2Fk8s-quick-start-services.png?alt=media)

At the right top, you have the option to filter your selection to a certain cluster and/ or namespace to see the resources for which you are responsible.

At the bottom left, you find two inputs.

1. The time-range selector. This selects the time range for all metrics, logs and events you see throughout the product.
2. The topology-time selector. This is used to travel back to a certain moment in time to see the exact state of your systems as observed at that moment in time.

You can for example filter on a certain namespace, in this case, I filter the services down to 'sock-shop' which is a demo application using different microservices written in different programming languages and using different ways of communication to act as a nice example for troubleshooting an issue. If you now click on Topology you will see the topology of the currently selected components (in this case the services of the sock-shop).

![Services topology](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-81c15d963107cc62715ca570af2445ac2e26aefd%2Fk8s-quick-start-service-topology.png?alt=media)

In the topology, you see all resources, in this case services.

* If you click a component (in this case a service) it shows you the details of a service including the most important metrics, in the case of a service, for example, the latency, throughput and error rate. Next to the most important metrics the health of the component is shown and expanded if there is anything going wrong.
* If you click a relation you will see the detail of the relation including all components part of it. In the case of a service map you will see all components involved in the service-to-service communication. If you want to open a component to see all details of that resource (e.g. the details of this service a certain service) you can click on the 'Open Component' button from a selected component (which you then see in the Right Hand Side panel) or you can open the component by clicking on the name of the component in the overview page tab.

![Service overview](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-2440c81ff92c653056456fb50502526eaed599d5%2Fk8s-quick-start-service.png?alt=media)

After opening a Kubernetes resource you will get a Highlight perspective showing you all the highlights of that component.

1. The component meta-data
2. The actions available on the component, in the case of a service, it gives you the ability to show the Status and/ or Configuration information. If you want to see the logs you can open the pods via the related resources which give you access to the Logs.
3. Related resources. This section shows all related resources to this resource in this case 2 other services to which it communicates and 1 pod which backs this services.
4. The monitors sections shows you all monitors applied to this Resource including their state a the selected topology-time.
5. The metrics section shows you all the important metrics for this service. The metrics include the selected telemetry-time interval.
6. A health time-line for a service shows the health of this resource over time.
7. A event time-line showing all events happening on this service over time.

Let's now explore a triggered monitor by clicking on the 'HTTP - 5xx error ratio' one.

![HTTP - 5xx error ratio triggered monitor](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-43737f4415cd4c6dc455deeaa87059d33f84f361%2Fk8s-quick-start-service-5xx-error-triggered-monitor.png?alt=media)


# SUSE Rancher Prime

StackState v6.0

## Introduction

This page describes how to install SUSE Rancher Prime - Observability during the Tech Preview phase on-premise.

SUSE Rancher Prime - Observability, formerly known as StackState can be used for Observability of your Kubernetes clusters and their workloads. During the Tech Preview phase we only offer 2 on-prem installations which can support up-to 50 (non-HA) or up-to 250 (HA) worker Nodes.

The Tech Preview phase is expected is expected to last at least 30 days. After the Tech Preview phase a GA version will be made available for SUSE Rancher Prime customers. There is no guarantee that the Tech Preview will be compatible from a feature or upgrade perspective with the GA version.

The installation of StackState, the SUSE Rancher Observability UI extension and the StackState Agents takes about 30 minutes in total.

## Getting help

To get support, ask any question or provide feedback you can reach us during the tech preview phase on the following email <rancherobservability@suse.com>

## Prerequisites

### License key

A license key for StackState server can be obtained via the SUSE Customer Center and will be shown as "SUSE Rancher Prime - Observability Tech Preview" Registration Code. The license for the tech preview is valid until Oct, 31 2024. Before the end a license will be made available which is valid until the end of your SUSE Rancher Prime subscription.

### Requirements

To install StackState, ensure that the nodes have enough CPU and memory capacity. Below are the specific requirements.

There are different installation options available for StackState. It is possible to install StackState either in a High-Availability (HA) or single instance (non-HA) setup. The non-HA setup is recommended for testing purposes or small environments. For production environments, it is recommended to install StackState in a HA setup.

The HA production setup can support up to 250 Nodes (a Node is counted as<= 4 vCPU and <= 16GB Memory) under observation The Non-HA setup can support up to 50 Nodes under observation.

![Requirements](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-5187b04bb168b0bab51ef3819fe4032e806eb2d5%2Frequirements.png?alt=media)

In the near feature we will have more options with lower resource constraints and for smaller + larger setups.

### The different components

#### StackState Server

This is the on-prem hosted server part of the installation. It contains a set of services to store observability data:

* Topology (StackGraph)
* Metrics (VictoriaMetrics)
* Traces (ClickHouse)
* Logs (ElasticSearch)

Next to this, it contains a set of services for all the observability tasks. e.g. Notifications, State management, Monitoring, etc.

#### StackState Agent

The lightweight StackState agent is installed on your downstream worker nodes. It collects and reports metrics, events, traces and logs, and it provides real-time observability and insights, enabling proactive monitoring and troubleshooting of your IT environment.

The SUSE Rancher Prime version of the Agent also uses eBPF as a lightweight way to monitor all your workloads and their communication. It also decodes the RED (Rate, Errors and Duration) signals for most of the common L7 protocols like TCP, HTTP, TLS, Redis, etc.

#### Rancher Prime - Observability UI extension

This is an UI extension to Rancher Manager that integrates the health signals observed by StackState. It gives direct access to the health of any resource and a link to StackState's UI for further investigation.

### Where to install StackState server

StackState server should be installed in its own downstream cluster intended for Observability. See the below picture for reference.

For StackState to be able to work properly it needs:

* [Kubernetes Persistent Storage](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/create-kubernetes-persistent-storage) to be available in the observability cluster to store metrics, events, etc.
* the observability cluster to support a way to expose StackState on an HTTPS URL to Rancher, StackState users and the StackState agent. This can be done via an Ingress configuration using an ingress controller, alternatively a (cloud) loadbalancer for the StackState services could do this too, for more information see the [Rancher docs](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/kubernetes-resources-setup/load-balancer-and-ingress-controller).

![Architecture](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-975d9319c4e8475a63db930f367865ab54f66617%2Farchitecture.png?alt=media)

### Pre-Installation

Before installing the StackState server a default storage class must be set up in the cluster where the StackState server will be installed:

* **For k3s**: The local-path storage class of type rancher.io/local-path is created by default.
* **For EKS, AKS, GKE** a storage class is set by default
* **For RKE2 Node Drivers**: No storage class is created by default. You will need to create one before installing StackState.
* **RKE1** is not supported to run StackState server.

## Installing StackState

{% hint style="info" %}
**Good to know**

If you created the cluster using Rancher Manager and would like to run the provisioning commands below from a local terminal instead of in the web terminal, just copy or download the kubeconfig from the cluster dashboard, see image below, and paste it (or place the downloaded file) into a file that you can easily find e.g. \~/.kube/config-rancher and set the environment variable KUBECONFIG=$HOME/.kube/config-rancher
{% endhint %}

![Rancher](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-b09c050720dbfa184baa8cf2ba231e625490f282%2Francher_cluster_dashboard.png?alt=media)

After meeting the prerequisites you can proceed with the installation. The installation is NOT YET AVAILABLE from the app store. Instead, you can install StackState via the downstream or upstream kubectl shell of the cluster.

You can now follow the instruction below for a HA or NON-HA setup.

{% hint style="info" %}
Be aware upgrading or downgrading from HA to NON-HA and visa-versa is not yet supported.
{% endhint %}

### Installing a default HA setup for up to 250 Nodes

1. Get the helm chart

{% code title="helm\_repo.sh" lineNumbers="true" %}

```
helm repo add rancher-prime-observability https://helm-rancher-prime.stackstate.io
helm repo update
```

{% endcode %}

2. Command to generate helm chart values file:

{% code title="helm\_template.sh" lineNumbers="true" %}

```
helm template \
    --set license='<licenseKey>' \
    --set baseUrl='<baseURL>' \
    --set pullSecret.username='trial' \
    --set pullSecret.password='trial' \
    prime-observability-values \
    rancher-prime-observability/stackstate-values > values.yaml
```

{% endcode %}

3. Deploy the StackState helm chart with the generated values:

{% code title="helm\_deploy.sh" lineNumbers="true" %}

```
helm upgrade --install \
    --namespace prime-observability \
    --create-namespace \
    --values values.yaml \
    prime-observe \
    rancher-prime-observability/stackstate-k8s
```

{% endcode %}

### Installing a NON-HA setup for up to 50 Nodes

1. Get the helm chart

{% code title="helm\_repo.sh" lineNumbers="true" %}

```
helm repo add rancher-prime-observability https://helm-rancher-prime.stackstate.io
helm repo update
```

{% endcode %}

2. Command to generate helm chart values file:

{% code title="helm\_template.sh" lineNumbers="true" %}

```
helm template \
    --set license='<licenseKey>' \
    --set baseUrl='<baseURL>' \
    --set pullSecret.username='trial' \
    --set pullSecret.password='trial' \
    prime-observability-values \
    rancher-prime-observability/stackstate-values > values.yaml
```

{% endcode %}

The `baseUrl` must be the URL via which StackState will be accessible to Rancher, users, and the StackState agent. The URL must including the scheme, for example `https://stackstate.internal.mycompany.com`. See also [accessing StackState](#accessing-stackstate).

3. Create a second values file for the non-ha setup, named nonha\_values.yaml with the following content:

{% code title="nonha\_values.yaml" lineNumbers="true" %}

```
# This files defines additional Helm values to run StackState on a
# non-high availability production setup. Use this file in combination
# with a regular values.yaml file that contains your API key, etc.
elasticsearch:
  minimumMasterNodes: 1
  replicas: 1

hbase:
  hbase:
    master:
      replicaCount: 1
    regionserver:
      replicaCount: 1
  hdfs:
    datanode:
      replicaCount: 1
    secondarynamenode:
      enabled: false
  tephra:
    replicaCount: 1

kafka:
  replicaCount: 1
  defaultReplicationFactor: 1
  offsetsTopicReplicationFactor: 1
  transactionStateLogReplicationFactor: 1

stackstate:
  components:
    ui:
      replicaCount: 1

victoria-metrics-1:
  enabled: false

zookeeper:
  replicaCount: 1

clickhouse:
  replicaCount: 1
```

{% endcode %}

4. Deploy the StackState helm chart with the generated values, as well as the non-ha configuration values:

{% code title="helm\_deploy.sh" lineNumbers="true" %}

```
helm upgrade --install \
    --namespace prime-observability \
    --create-namespace \
    --values values.yaml \
    --values nonha_values.yaml \
    prime-observe \
    rancher-prime-observability/stackstate-k8s
```

{% endcode %}

## Accessing StackState

The StackState Helm chart has support for creating an Ingress resource to make StackState accessible outside of the cluster. Follow [these instructions](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/ingress) to set that up when you have an ingress controller in the cluster. Make sure that the resulting URL uses TLS with a valid, not self-signed, certificate.

If you prefer to use a load balancer instead of ingress, expose the `prime-observe-stackstate-k8s-router` service. The URL for the loadbalancer needs to use a valid, not self-signed, TLS certificate.

## Installing UI extensions

{% hint style="warning" %}
Currently the UI extension for SUSE Rancher Prime Observability is only supported on the 2.8.x versions for SUSE Rancher Prime, and not on the 2.9.x versions. The 2.9.x version will be released soon.
{% endhint %}

To install UI extensions, enable the UI extensions from the rancher UI

![Install](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fa63bbbda98068c86db47cce43f03dcdf1f83d7f%2Fui_extensions.png?alt=media)

After enabling UI extensions, follow these steps:

1. Navigate to **Local Cluster > Apps > Repositories** and create a new repository. Use the default Helm option and add the **Index URL**: <http://stackvista.github.io/rancher-extension-stackstate>
2. Once it is created, a deployment by the name **ui-plugin-operator** in the namespace **cattle-ui-plugin-system** gets created in the local cluster
3. Navigate to extensions on the rancher UI and under Available section of extensions, we will have the Observability extension available.
4. Install the Observability extension.
5. Once installed, on the left panel of the rancher UI, the *Rancher Prime Observability* section appears.
6. Navigate to the *Rancher Prime Observability* section and select "configurations". In this section, you can add the StackState server details and connect it.
7. Follow the instructions as mentioned in *Obtain a service token* tab and fill in the details.

### Obtain a service token:

1. Log into the StackState instance.
2. From the top left corner, select CLI.
3. Note the API token and install StackState cli on your local machine.
4. Create a service token by running

```
sts service-token create --name rancher-prime-observability --roles stackstate-k8s-troubleshooter
```

## Installing the StackState Agent

There are two ways to install the StackState Agent: via the Rancher UI or directly via helm, as mentioned in the instructions of the StackPack page.

{$ hint style="warning" %} Ensure that the cluster name provided in the StackState UI matches the cluster name in the Rancher UI. {$ endhint %}

### Install the StackState Agent from the Rancher UI:

1. In the StackState UI open the main menu and select StackPacks.
2. Select the Kubernetes StackPack.
3. Click on new instance and provide the cluster name of the downstream cluster which you are adding. Make sure you match the name of the Rancher cluster with the name provided here. Click install. When installation completes the api-key and StackState URL are shown as part of the installation instructions.
4. In a separate tab navigate to the downstream cluster on the Rancher UI on which you want to install the Agent and then go to apps.
5. From the partner charts, select the StackState agent.
6. Provide the requested installation values:
   1. Make sure the cluster name matches the Rancher cluster name.
   2. The api-key and StackState URL from step 3 must be used.
7. The Stackstate agent will now be installed on the downstream cluster.
8. After you install the StackState Agent, the cluster can be seen within the StackState UI as well as the *SUSE Rancher - Observability UI extension*.

### Install the StackState Agent via helm:

1. In the StackState UI open the main menu and select StackPacks.
2. Select the Kubernetes StackPack.
3. Click on new instance and provide the cluster name of the downstream cluster which you are adding. Make sure you match the name of the Rancher cluster with the name provided here. Click install.
4. You will now see the helm command which you need to execute.
5. After you install the StackState Agent, the cluster can be seen within the StackState UI as well as the *SUSE Rancher - Observability UI extension*.

## Single Sign On

To enable Single sign-on with your own authentication provider please [see here](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/authentication_options).

## Frequently asked questions & Observations:

1. Is it mandatory to install a StackState agent before proceeding with adding the UI extension?
   * No this is not mandatory, the UI extension can be installed independent.
2. Is it mandatory to install StackState Server before we proceed with UI extensions?
   * Yes this is not mandatory since you need to provide a StackState endpoint in the configuration
3. Can we install StackState on a local cluster or on a downstream cluster?
   * Both options are possible.
4. To monitor the downstream clusters, should we install the StackState agent from the app store or add a new instance from the StackState UI?
   * Both options are possible depending on users preference.

## Open Issues

1. When you uninstall and reinstall the UI extensions for Observability, we noticed that service token is not deleted and is reused upon reinstallation. Whenever we uninstall the extensions, service token should be removed.
   * This information should be deleted when the UI extensions are uninstalled.
2. After the extensions are installed, the StackState UI opens in the same tab as the Rancher UI.
   * You can use shift-click to open in a new tab, this will become the default behaviour
3. The SUSE Rancher Prime - Observability Extension is only supported on 2.8.x versions and not yet on the 2.9.x version.
   * Support for 2.9.x will be available soon.
4. On RKE(1) The Node Agent does not start process-agent with Ubuntu 20.04.6 LTS worker nodes it fails with a message `failed to create network tracer`
5. Be aware upgrading or downgrading from HA to NON-HA and visa-versa is not yet supported.


# Air-gapped

Suse Rancher Prime

This document provides a step-by-step guide for installing Rancher Prime Observability using Helm charts in an air-gapped environment. The process involves preparing the necessary Docker images and Helm charts on a host with internet access, transferring them to a host within a private network, copying Docker images to a private registry, and then deploying the Helm charts.

## Prerequisites

### On the Local Host (Internet Access)

* **Operating System**: Linux or MacOS
* **Tools Installed**:
  * [Docker](https://www.docker.com/products/docker-desktop/)
  * [Helm cli](https://helm.sh/docs/intro/install/)
  * Scripts for downloading Docker images from the source registry (links will be provided later in this guide).
* **Internet Access**: Required to pull Docker images from Quay.io and Helm charts from ChartMuseum.

### On the Private Network Host

* **Access**: SSH access to the host.
* **Tools Installed**:
  * [Docker](https://www.docker.com/products/docker-desktop/)
  * [Helm cli](https://helm.sh/docs/intro/install/)
  * Scripts for downloading Docker images from the source registry (links will be provided later in this guide).
  * Network access and credentials to upload images to a private Docker registry.
  * A configured Kubeconfig to install the Helm charts on the target clusters.

## Preparing the Docker Images and Helm Charts

Run the following commands on the local host to obtain the required Docker images and Helm charts:

**Adding Helm repositories to the local Helm cache:**

```bash
# Adding the Helm repository for Rancher Prime Observability
helm repo add rancher-prime-observability https://helm-rancher-prime.stackstate.io
helm repo update
```

**Fetching the latest versions of the charts. These commands will download TGZ archives of the charts:**

```bash
# Downloading the chart for Rancher Prime Observability
# The file will be named stackstate-k8s-A.B.C.tgz
helm fetch rancher-prime-observability/stackstate-k8s

# Downloading the helper chart that generates values for Rancher Prime Observability
# The file will be named stackstate-values-L.M.N.tgz
helm fetch rancher-prime-observability/stackstate-values
```

**Downloading the Bash scripts to save Docker images:**

```bash
# o11y-get-images.sh
curl -LO https://raw.githubusercontent.com/StackVista/helm-charts/stackstate-6.x/stable/stackstate-k8s/installation/o11y-get-images.sh
# o11y-save-images.sh
curl -LO https://raw.githubusercontent.com/StackVista/helm-charts/stackstate-6.x/stable/stackstate-k8s/installation/o11y-save-images.sh

# Make the scripts executable
chmod a+x o11y-get-images.sh o11y-save-images.sh
```

**Extracting and Saving Docker Images:**

```bash
# Extract the list of images from the Helm chart and save it to a file.
./o11y-get-images.sh -f stackstate-k8s-A.B.C.tgz > o11y-images.txt
```

{% hint style="info" %}
Replace `stackstate-k8s-A.B.C.tgz` with the actual filename of the chart archive downloaded earlier.\*
{% endhint %}

```bash
# Save Docker images to an archive.
# The script expects the file o11y-images.txt to contain the list of images used by Rancher Prime Observability.
# The Docker images will be saved to o11y-images.tar.gz.
./o11y-save-images.sh -i o11y-images.txt -f o11y-images.tar.gz
```

## Copying the Required Files to the Remote Host

Copy the following files from the local host to the host in the private network:

* o11y-images.txt (List of images required by the Rancher Prime Observability chart)
* o11y-images.tar.gz (An archive with the Rancher Prime Observability's Docker images)
* [o11y-load-images.sh](https://raw.githubusercontent.com/StackVista/helm-charts/stackstate-6.x/stable/stackstate-k8s/installation/o11y-load-images.sh) (Bash script to upload Docker images to a registry)
* Helm charts downloaded earlier:
  * stackstate-k8s-A.B.C.tgz
  * stackstate-values-L.M.N.tgz

## Restoring Docker Images from the Archive to the Private Registry

**Upload the images to the private registry:**

```bash
# Load Docker images from the archive and push them to the private registry.
# Replace <private-registry> with your private registry's URL.
export DST_REGISTRY_USERNAME="..."
export DST_REGISTRY_PASSWORD="..."
./o11y-load-images.sh -d registry.example.com:5043 -i o11y-images.txt -f o11y-images.tar.gz
```

{% hint style="info" %}
If the destination registry doesn't use authentication the environment variables, `DST_REGISTRY_USERNAME` and `DST_REGISTRY_PASSWORD` must not be configured or have to be set to empty values.\*
{% endhint %}

## Installing Rancher Prime Observability

**Custom Helm values**

Installing Rancher Prime Observability Helm charts in an air-gapped environment requires overriding the registries used in Docker image URLs. This can be achieved by customizing Helm values.

Create a private-registry.yaml file with the following content:

```yaml
global:
  imageRegistry: registry.example.com:5043
elasticsearch:
  prometheus-elasticsearch-exporter:
    image:
      repository: registry.example.com:5043/stackstate/elasticsearch-exporter
victoria-metrics-0:
  server:
    image:
      repository: registry.example.com:5043/stackstate/victoria-metrics
victoria-metrics-1:
  server:
    image:
      repository: registry.example.com:5043/stackstate/victoria-metrics
```

This guide follows the [Installing a default HA setup for up to 250 Nodes](https://docs.stackstate.com/get-started/k8s-suse-rancher-prime#installing-a-default-ha-setup-for-up-to-250-nodes) setup, but instead of using publicly available Helm and Docker repositories/registries, it uses pre-downloaded Helm archives and private Docker registries.

**Command to Generate Helm Chart Values File:**

{% code title="helm\_template.sh" lineNumbers="true" %}

```
helm template \
    --set license='<licenseKey>' \
    --set baseUrl='<baseURL>' \
    --set pullSecret.username='trial' \
    --set pullSecret.password='trial' \
    prime-observability-values stackstate-values-L.M.N.tgz\
     > values.yaml
```

{% endcode %}

**Deploying the Rancher Prime Observability Helm Chart:**

{% code title="helm\_deploy.sh" lineNumbers="true" %}

```
helm upgrade --install \
    --namespace prime-observability \
    --create-namespace \
    --values values.yaml \
    --values private-registry.yaml \
    prime-observe \
    stackstate-k8s-A.B.C.tgz
```

{% endcode %}

**Validating the Deployment:**

```bash
kubectl get pod -n prime-observability
```


# Agent Air-gapped

Suse Rancher Prime

This document provides a step-by-step guide for installing the Rancher Prime Observability Agent using Helm charts in an air-gapped environment. The installation process involves preparing the necessary Docker images and Helm chart on a host with internet access, transferring them to a host within a private network, uploading Docker images to a private registry, and deploying the Helm charts.

## Prerequisites

### On the Local Host (Internet Access)

* **Operating System**: Linux or MacOS
* **Tools Installed**:
  * [Docker](https://www.docker.com/products/docker-desktop/)
  * [Helm cli](https://helm.sh/docs/intro/install/)
  * Scripts for downloading Docker images from the source registry (links will be provided later in the guide).
* **Internet Access**: Required to pull Docker images from Quay.io and Helm charts from ChartMuseum.

### On the Private Network Host

* **Access**: SSH access to the host.
* **Tools Installed**:
  * [Docker](https://www.docker.com/products/docker-desktop/)
  * [Helm cli](https://helm.sh/docs/intro/install/)
  * Scripts for downloading Docker images from the source registry (links will be provided later in the guide).
  * Network access and credentials to upload images to a private Docker registry.
  * A configured Kubeconfig to install the Helm charts on the target clusters.

## Preparing the Docker Images and Helm Chart

Run the following commands on the local host to obtain the necessary Docker images and Helm charts:

**Adding Helm Repositories to the Local Helm Cache:**

```bash
# Adding the Helm repository for the Rancher Prime Observability Agent
helm repo add stackstate https://helm.stackstate.io
helm repo update
```

**Fetching the Latest Version of the Chart**

The following command will download a TGZ archive of the chart from the Helm repository:

```bash
# Downloading the chart for the Rancher Prime Observability Agent
# The file will be named stackstate-agent-X.Y.Z.tgz
helm fetch stackstate/stackstate-k8s-agent
```

**Getting the Bash scripts to save Docker images.**

```bash
# o11y-agent-get-images.sh
curl -LO https://raw.githubusercontent.com/StackVista/helm-charts/master/stable/stackstate-k8s-agent/installation/o11y-agent-get-images.sh
# o11y-agent-save-images.sh
curl -LO https://raw.githubusercontent.com/StackVista/helm-charts/master/stable/stackstate-k8s-agent/installation/o11y-agent-save-images.sh

# Make the scripts executable
chmod a+x o11y-agent-get-images.sh o11y-agent-save-images.sh
```

**Extracting and Saving Docker Images**

```bash
# Extract the list of images from the Helm chart and save it to a file.
./o11y-agent-get-images.sh -f stackstate-k8s-agent-X.Y.Z.tgz > o11y-agent-images.txt
```

{% hint style="info" %}
Replace `stackstate-k8s-agent-X.Y.Z.tgz` with the actual filename of the chart archive downloaded earlier.\*
{% endhint %}

```bash
# Save Docker images to an archive.
# The script expects the file o11y-agent-images.txt to contain the list of images used by the Rancher Prime Observability Agent.
# The Docker images will be saved to o11y-agent-images.tar.gz.
./o11y-agent-save-images.sh -i o11y-agent-images.txt -f o11y-agent-images.tar.gz
```

## Copying the Required Files to the Remote Host

The following files have to be copied from the local host to the host in the private network:

* o11y-agent-images.txt (List of images required by the Rancher Prime Observability Agent chart)
* o11y-agent-images.tar.gz (An archive with the Rancher Prime Observability Agent's Docker images)
* [o11y-agent-load-images.sh](https://raw.githubusercontent.com/StackVista/helm-charts/master/stable/stackstate-k8s-agent/installation/o11y-agent-load-images.sh) (Bash script to upload Docker images to a registry)
* Helm charts downloaded earlier:
  * stackstate-k8s-agent-X.Y.Z.tgz

## Restoring Docker Images from the Archive to the Private Registry

**Uploading the images to the private registry:**

```bash
# Load Docker images from the archive and push them to the private registry.
# Replace <private-registry> with your private registry's URL.
export DST_REGISTRY_USERNAME="..."
export DST_REGISTRY_PASSWORD="..."
./o11y-agent-load-images.sh -d registry.example.com:5043 -i o11y-agent-images.txt -f o11y-agent-images.tar.gz
```

{% hint style="info" %}
*Note: if the destination registry doesn't use authentication the environment variables, `DST_REGISTRY_USERNAME` and `DST_REGISTRY_PASSWORD` must not be configured or have to be set to empty values.*
{% endhint %}

## Installing Rancher Prime Observability Agent

The command to install the Rancher Prime Observability Agent has to be received from Rancher Prime Observability UI. Log in to your instance and in the left-side menu choose the `Stackpacks`. Press `ADD NEW INSTANCE` and fill in the name of the cluster. For correct integration with Rancher it has to be the same as the cluster name in the Rancher UI.

![Adding New Agent](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-117b1616849e5aa0b95227af70c81feff3c560fa%2Francher-prime-agent-airgap-01.png?alt=media)

When an instance is added, the UI will provide the instructions how the Helm chart can be deployed. Scroll down to the `Self-hosted` section and copy `helm upgrade ...` command

![Getting Helm Install Command](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-d290b5d56be63ddecdcaba06163ed005cd614313%2Francher-prime-agent-airgap-02.png?alt=media)

The command has to be updated for the air-gapped installation:

* Overriding the image registry with `all.image.registry` value.
* Using the arhive with the Helm chart instead of the Helm repository. `stackstate/stackstate-k8s-agent` -> `./stackstate-k8s-agent-X.Y.Z.tgz`

Run the command to install the Rancher Prime Observability Agent

```bash
helm upgrade --install \
--namespace stackstate \
--create-namespace \
--set-string 'stackstate.apiKey'='<api-key>' \
--set-string 'stackstate.cluster.name'='<cluster-name>' \
--set-string 'stackstate.url'='https://...' \
--set 'nodeAgent.skipKubeletTLSVerify'=true \
--set-string 'all.image.registry'='registry.acme.com:5000' \
--set-string 'global.imageRegistry'='registry.acme.com:5000' \
--set-string 'global.skipSslValidation'=true \
stackstate-k8s-agent ./stackstate-k8s-agent-X.Y.Z.tgz
```

**Validating the Deployment**

```bash
kubectl get pod -n stackstate
```


# What is guided troubleshooting?

StackState v6.0

## Overview

Guided troubleshooting with StackState is a powerful approach to accelerate issue resolution by offering targeted, actionable insights throughout the troubleshooting process. By leveraging advanced algorithms, StackState provides troubleshooting hints, visual assistance, and step-by-step guidance tailored to your specific environment. This not only streamlines the process of identifying and resolving issues but also empowers Site Reliability Engineers (SREs) to better support their development teams.

By utilizing StackState's guided remediation, engineers can ensure consistent, high-quality services, and share their expertise with other team members. Furthermore, our remediation guides can be easily extended or modified to adapt to your unique environment, making them an invaluable tool for maintaining service reliability and performance.

Pre-configured monitors that look at the right things and issue alerts at the right time are enriched with clear hints to enable engineers to remediate the issues. This guidance helps every engineer immediately understand what needs to happen in order to remediate. In addition, after the issue is solved, this information will support the process of a blameless post-mortem to determine what needs to be improved.

## Remediating issues with guided troubleshooting

To remediate quickly StackState has a clear problem report and remediation guide packaged in a single screen. It contains the following items:

1. A brief description to explain the problem to people who are less familiar with what it is.
2. Some facts on this problem such as Health State, triggered time and a reason if present.
3. The supporting metric indicates how the issue evolved over time.
4. Often, issues don’t happen in isolation. Sometimes they cause other issues, or the real problem is caused by a different component. StackState keeps track of how all components are related and warns you about related issues.
5. The remediation guide itself to guide you through the problem resolution step by step.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-e1338cfe311d62a6e92b6e451f5516c6f28e2936%2Fguided-troubleshooting.png?alt=media)

## Using pinned items when troubleshooting

You can keep a remediation guide at hand while troubleshooting by adding it to the **pinned items**. Click on **Add to pinned items** button to pin remediation guide for the current monitor. Now you can follow the step-by-step guidance even when you close the triggered monitor. You can access all pinned remediation guides from the pinned items menu. When you are done troubleshooting just unpin the guide from the menu.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-b584959ae2ebef25dfb9ca6725425343975c456f%2Fk8s-pinned-items.png?alt=media)


# YAML Configuration

StackState v6.0

If a pod is experiencing issues such as crashes, failures to start or misconfigurations, inspecting the YAML configuration can help you identify the root cause. You can see YAML configuration by clicking on **Show configuration** button.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-0f88977a9dc6201d750eaeb3ecd06aaa4c0cd8ce%2Fk8s-configuration.png?alt=media)

This gives the same output as `kubectl describe` command applied for service, pod or other resource.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-9776d2eb1f38417f64c192e568014000f9d79641%2Fk8s-configuration-opened.png?alt=media)


# Changes

StackState v6.0

## See diff from the last deployment

When issues arise after applying changes to your Kubernetes configurations, take a look at the last deployment change.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-3ab45014b7c5c8a81ec28bd4f0218e2d7af2d132%2Fk8s-show-diff.png?alt=media)

Comparing the current configuration with the previous one can help you identify the specific changes that might have caused the problem.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-340ec7876832c9446b8cde8a338f138622dd083c%2Fk8s-show-diff-opened.png?alt=media)


# Logs

StackState v6.0

## Overview

Kubernetes keeps comprehensive logs of cluster activity and application output. Logging provides valuable insight into how containers, nodes and Kubernetes itself is performing. Meticulously logging everything from Pods to ReplicaSets, it allows you to trace problems back to their source.

## Accessing pod logs

Errors and warnings in the logs are indicators of potential problems in your application, containers or the pod itself. To explore logs when on the pod screen click **Show logs** button.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-af3436eb2a9d13075ad1d874881c673c03c5cafc%2Fk8s-logs.png?alt=media)

## Using pod logs

You can use search to look for specific errors or warnings in the logs. Logs can be filtered by a container. You can select a desired time interval logs will be shown for and a refresh interval for how often you would like logs to be updated.

Logs histogram visualizes the number of log lines within a selected time interval and allows you to zoom to a particular interval by clicking and dragging.

Use these options to show or hide additional information for each log line:

* **Show time** to show timestamps
* **Show containers** to show the container name the log line belongs to
* **Wrap lines** to enable wrapping for the long lines
* **Newest first/Oldest first** to switch the log sorting order

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-cb0537abfa272ae3e188e38476aebc4b0f334c93%2Fk8s-logs-opened.png?alt=media)


# Monitors

StackState v6.0

## Overview

StackState has the best practices encoded via monitors. StackState monitors not only monitor metrics, events or logs but can also monitor the topology and meta-data to detect common issues, ensuring compliance and adherence to industry standards. Combining monitors with our unique troubleshooting intelligence, StackState quickly detects issues that are related and advises on how to remediate them. This proactive approach reduces the risk of undetected problems and helps maintain a healthy and robust Kubernetes environment. Monitors are accompanied by remediation guides specific to the resource on which is alerted and the monitored condition to guide our users in their troubleshooting.

## Monitor results

Monitor results are shown in two places:

1. On highlight pages of all resources to immediately see what is going on and how to remediate it.
2. On the right-hand side panel if you select an element in the topology to give you a quick indication of issues for that component.

## Remediation guides

Remediation guides are shown on the Monitor Status drawer which is shown if you open a monitor by clicking on the message on the Highlight perspective of a resource.

## See also

* [Out-of-the-box monitors for Kubernetes](https://archivedocs.stackstate.com/monitors-and-alerts/kubernetes-monitors)


# Out of the box monitors for Kubernetes

StackState v6.0

## Overview

This section describes the out-of-the-box monitors delivered with StackState. Monitors delivered with the product are added constantly. Have a look under the Monitors section in the main menu to find the full list.

## Out of the box Kubernetes monitors

### Available service endpoints

It is important to ensure that your services are available and accessible to users. To monitor this, StackState has set up a check that verifies if a service has at least one endpoint available. Endpoints are network addresses that enable communication between different components in a distributed system, and they need to be available for the service to function properly. If there is an occurrence of zero endpoints available within the last 10 minutes, the monitor will remain deviating, indicating that there may be an issue with the service that needs to be addressed. Allows [Override Monitor arguments](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments)

### Cpu limits resourcequota

Users create resources (pods, services, etc.) in the namespace, and the quota system tracks usage to ensure it does not exceed hard resource limits for Cpu defined in a ResourceQuota. The monitor will alert when the total Cpu limits in the namespace gets to 90% or more of the established by the quota. Each `resourcequota` in the namespace produces a monitor health state.

### Cpu requests resourcequota

Users create resources (pods, services, etc.) in the namespace, and the quota system tracks usage to ensure it does not exceed hard resource requests for Cpu defined in a ResourceQuota. The monitor will alert when the total Cpu requests in the namespace gets to 90% or more of the established by the quota. Each `resourcequota` in the namespace produces a monitor health state.

### Daemonset desired replicas

It is important that the desired number of replicas for a Daemonset is being met. Daemonsets are used to manage a set of pods that need to run on all or a subset of nodes in a cluster, ensuring that a copy of the pod is running on each node that meets the specified criteria. This is useful for tasks such as logging, monitoring, and other cluster-level tasks that need to be executed on every node in the cluster. To monitor this, StackState has set up a check that verifies if the available replicas match the desired number of replicas. This check will only be applied to DaemonSets that have a desired number of replicas greater than zero. - If the number of available replicas is less than the desired number, the monitor will signal a DEVIATING health state, indicating that there may be an issue with the StatefulSet. - If the number of available replicas is zero, the monitor will signal a CRITICAL health state, indicating that the StatefulSet is not functioning at all. To understand the full monitor definition check the details.

### Deployment desired replicas

It is important that the desired number of replicas for a Deployments is being met. Deployments are used to manage the deployment and scaling of a set of identical Pods in a Kubernetes cluster. By ensuring that the desired number of replicas is running and available, Deployments can help maintain the availability and reliability of a Kubernetes application or service. To monitor this, StackState has set up a check that verifies if the available replicas match the desired number of replicas. This check will only be applied to Deployments that have a desired number of replicas greater than zero. - If the number of available replicas is less than the desired number, the monitor will signal a DEVIATING health state, indicating that there may be an issue with the Deployments. - If the number of available replicas is zero, the monitor will signal a CRITICAL health state, indicating that the StatefulSet is not functioning at all. To understand the full monitor definition check the details.

### HTTP - 5xx error ratio

HTTP responses with a status code in the 5xx range indicate server-side errors such as a misconfiguration, overload or internal server errors. To ensure a good user experience, the percentage of 5xx responses should be less than 5% of the total HTTP responses for a Kubernetes (K8s) service.

### HTTP - response time - Q95 is above 3 seconds

It is important to keep an eye on the HTTP response times for a Kubernetes service. StackState monitors the 95th percentile response time, or Q95, which is a statistical measure indicating that 95% of the responses are faster than this time. This is a useful measure for identifying outliers and slow requests that may negatively impact the user experience. If the Q95 response time is above 3 seconds during a specified time window, the monitor will produce a notification indicating a deviating state.

### Kubernetes volume usage trend over 12 hours

It is important to monitor the usage of Persistent Volume Claims (PVCs) in your Kubernetes cluster. PVCs are used to store data that needs to persist beyond the lifetime of a container, and it's crucial to ensure that they have enough space to store the data. To track this, StackState has set up a check that uses linear prediction to forecast the Kubernetes volume usage trend over a 12-hour period. If the trend indicates that the PVCs will run out of space within this time frame, you will receive a notification, allowing you to take action to prevent data loss or downtime.

### Kubernetes volume usage trend over 4 days

It is important to monitor the usage of Persistent Volume Claims (PVCs) in your Kubernetes cluster over time. PVCs are used to store data that needs to persist beyond the lifetime of a container, and it's crucial to ensure that they have enough space to store the data. To track this, StackState set up a check that uses linear prediction to forecast the Kubernetes volume usage trend over a 4-day period. If the trend indicates that the PVCs will run out of space within this time frame, you will receive a notification, allowing you to take action to prevent data loss or downtime.

### Memory limits resourcequota

Users create resources (pods, services, etc.) in the namespace, and the quota system tracks usage to ensure it does not exceed hard resource limits for memory defined in a ResourceQuota. The monitor will alert when the total memory limits in the namespace gets to 90% or more of the established by the quota. Each `resourcequota` in the namespace produces a monitor health state.

### Memory requests resourcequota

Users create resources (pods, services, etc.) in the namespace, and the quota system tracks usage to ensure it does not exceed hard resource requests for memory defined in a ResourceQuota. The monitor will alert when the total memory requests in the namespace gets to 90% or more of the established by the quota. Each `resourcequota` in the namespace produces a monitor health state.

### Node Disk Pressure

Node disk pressure refers to a situation where the disks connected to a node experience excessive strain. While encountering node disk pressure is unlikely due to Kubernetes' built-in preventive measures, it can still occur sporadically. There are two primary reasons why node disk pressure may arise. The first reason relates to Kubernetes failing to clean up unused images. Under normal circumstances, Kubernetes regularly checks for and deletes any images that are not in use. Therefore, this is an uncommon cause of node disk pressure, but it should be acknowledged. The more probable issue involves the accumulation of logs. In Kubernetes, logs are typically saved in two scenarios: when containers are running and when the most recently exited container's logs are retained for troubleshooting purposes. This approach aims to strike a balance between preserving important logs and discarding unnecessary ones over time. However, if a long-running container generates an extensive volume of logs, they may accumulate to the point where they overload the node disk's capacity. To understand the full monitor definition check the details. Allows [Override Monitor arguments](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments)

### Node Memory Pressure

Node memory pressure refers to a situation where the memory resources on a Kubernetes node are excessively strained. While encountering node memory pressure is uncommon due to Kubernetes' built-in resource management mechanisms, it can still occur under specific circumstances. There are two primary reasons why node memory pressure may arise. The first reason is related to misconfigured or insufficient resource requests and limits for containers running on the node. Kubernetes relies on resource requests and limits to allocate and manage resources effectively. If containers are not accurately configured with their memory requirements, they may consume more memory than expected, leading to node memory pressure. The second reason involves the presence of memory-intensive applications or processes. Certain workloads or applications may have higher memory demands, resulting in increased memory utilization on the node. If multiple pods or containers with substantial memory requirements are scheduled on the same node without proper resource allocation, it can cause memory pressure. To mitigate node memory pressure, it is crucial to review and adjust resource requests and limits for containers, ensuring they align with the actual memory needs of the applications. Monitoring and optimizing memory usage within the applications themselves can also help reduce memory consumption. Additionally, consider horizontal pod autoscaling to dynamically scale the number of pods based on memory utilization. Regular monitoring, analysis of memory-related metrics, and proactive allocation of memory resources can help maintain a healthy memory state on Kubernetes nodes. It's essential to understand the specific requirements of your workloads and adjust resource allocation accordingly to prevent memory pressure and ensure optimal performance. Allows [Override Monitor arguments](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments)

### Node PID Pressure

Node PID pressure occurs when the available process identification (PID) resources on a Kubernetes node are excessively strained. The first reason is related to misconfigured or insufficient resource requests and limits for containers running on the node. Kubernetes relies on accurate resource requests and limits to effectively allocate and manage resources. If containers are not configured correctly with their PID requirements, they may consume more PIDs than expected, resulting in node PID pressure. The second reason is the presence of PID-intensive applications or processes. Some workloads or applications have higher demands for process identification, leading to increased PID utilization on the node. If multiple pods or containers with significant PID requirements are scheduled on the same node without proper resource allocation, it can cause PID pressure. To address node PID pressure, it is important to review and adjust resource requests and limits for containers to ensure they align with the actual PID needs of the applications. Monitoring and optimizing PID usage within the applications themselves can also help reduce PID consumption. Additionally, considering horizontal pod autoscaling can dynamically scale the number of pods based on PID utilization. Regular monitoring, analysis of PID-related metrics, and proactive allocation of PID resources are crucial for maintaining a healthy state of PID usage on Kubernetes nodes. It is essential to understand the specific requirements of your workloads and adjust resource allocation accordingly to prevent PID pressure and ensure optimal performance. Allows [Override Monitor arguments](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments)

### Node Readiness

Check if the Node is up and running as expected. Allows [Override Monitor arguments](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments)

### Out of memory for containers

It is important to ensure that the containers running in your Kubernetes cluster have enough memory to function properly. Out-of-memory (OOM) conditions can cause containers to crash or become unresponsive, leading to restarts and potential data loss. To monitor for these conditions, StackState set up a check that detects and reports OOM events in the containers running in the cluster. This check will help you identify any containers that are running out of memory and allow you to take action to prevent issues before they occur. Allows [Override Monitor arguments](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments)

### Pod Ready State

Checks if a Pod that has been scheduled is running and ready to receive traffic within the expected amount of time.

### Pod span duration

Monitors the duration of the server and consumer spans. When the 95th percentile of the duration is greater than the threshold (default 5000ms) the monitor has a Deviating state. This monitor supports overriding settings via [monitor argument overrides](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments).

### Pod span error ratio

Monitors the percentage of the server and consumer spans that have an error status. If the percentage of error spans exceeds the threshold (default 5) the monitor has a Deviating state. This monitor supports overriding settings via [monitor argument overrides](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments).

### Pods in Waiting State

If a pod is within a waiting state and contains a reason of CreateContainerConfigError, CreateContainerError, CrashLoopBackOff, or ImagePullBackOff it will be seen as deviating.

### Replicaset desired replicas

It is important to ensure that the desired number of replicas for your ReplicaSet (and Deployment) is being met. ReplicaSets and Deployments are used to manage the number of replicas of a particular pod in a Kubernetes cluster.

To monitor this, StackState has set up a check that verifies if the available replicas match the desired number of replicas. This check will only be applied to ReplicaSets and Deployments that have a desired number of replicas greater than zero.

* If the number of available replicas is less than the desired number, the monitor will signal a DEVIATING health state, indicating that there may be an issue with the ReplicaSet or Deployment.
* If the number of available replicas is zero, the monitor will signal a CRITICAL health state, indicating that the ReplicaSet or Deployment is not functioning at all.

Additionally, the health state of the ReplicaSet will propagate to the Deployment for more comprehensive monitoring.

### Restarts for containers

It is important to monitor the restarts for each container in a Kubernetes cluster. Containers can restart for a variety of reasons, including issues with the application or the infrastructure. To ensure that the application is running smoothly, StackState has set up a monitor that tracks the number of container restarts over a 10-minute period. If there are more than 3 restarts during this time frame, the container's health state will be set to DEVIATING, indicating that there may be an issue that needs to be investigated.

### Service span duration

Monitors the duration of the server and consumer spans. When the 95th percentile of the duration is greater than the threshold (default 5000ms) the monitor has a Deviating state. This monitor supports overriding settings via [monitor argument overrides](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments).

### Service span error ratio

Percentage of server and consumer spans that are in an error state for a Kubernetes service. This monitor supports overriding settings via [monitor argument overrides](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-override-monitor-arguments).

### Statefulset desired replicas

It is important that the desired number of replicas for a StatefulSet is being met. StatefulSets are used to manage stateful applications and require a specific number of replicas to function properly.

To monitor this, StackState has set up a check that verifies if the available replicas match the desired number of replicas. This check will only be applied to StatefulSets that have a desired number of replicas greater than zero.

* If the number of available replicas is less than the desired number, the monitor will signal a DEVIATING health state, indicating that there may be an issue with the StatefulSet.
* If the number of available replicas is zero, the monitor will signal a CRITICAL health state, indicating that the StatefulSet is not functioning at all.

### Unschedulable Node

If you encounter a "NodeNotSchedulable" event in Kubernetes, it means that the Kubernetes scheduler was unable to place a pod on a specific node due to some constraints or issues with the node. This event occurs when the scheduler cannot find a suitable node to run the pod according to its resource requirements and other constraints.

### Aggregated health state of a Cluster

Cluster doesn't have any health itself. But a cluster is build from few components, some of them are critical to normal operation. The monitor aggregates states of these components:

* all pods in 'kube-system' namespace
* all nodes and then takes the most critical health state.

### Aggregated health state of a DaemonSet

The monitor aggregates states of all children Pods and then returns the most critical health state.

### Aggregated health state of a Deployment

The monitor aggregates states of all children ReplicaSets and then returns the most critical health state. ReplicaSets have the similar Monitor, so eventually this one aggregates health states of all children ReplicaSets and Pods.

### Aggregated health state of a ReplicaSet

The monitor aggregates states of all children Pods and then returns the most critical health state.

### Aggregated health state of a StatefulSet

The monitor aggregates states of all children Pods and then returns the most critical health state.

## See also

* [Monitors](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-monitors)


# Notifications

StackState v6.0

Notifications in StackState are the way to notify third-party applications when a [monitor](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-monitors) in StackState fires. Notifications intergrate with third-party applications like incident management tools (like PagerDuty or Opsgenie), ticketing systems (like JIRA, ServiceNow), or other collaboration platforms (like Slack). Other tools might refer to notifications as alerts.

Notifications are triggered by health state changes of monitors on StackState components. Via the configured notification channels the health, component and monitor information is sent to these external systems.


# Configure notifications

StackState v6.0

To configure a new notification these are the steps:

* [Create a new notification](#create-a-new-notification)
* [Configure when to notify](#configure-when-to-notify)
* [Define where notifications should be sent](#where-to-send-notifications)

## Create a new notification

Open the notifications page via the link in the bottom half of hamburger menu in the StackState UI. This opens an overview of all notifications that are already configured including their status.

You can check if the desired notification already exists. If not create a new one with the "Add new notification" button.

## Configure when to notify

![Adding a new notification](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-26dc01f91ffb9ca841a1e0c5b72adc2c769216ff%2Fnotifications-add-new-notification.png?alt=media)

Configure the notification:

1. Name - Choose a name that's short but still describes what the intent is of this notification. It is for your own reference in the notifications overview.
2. Status - The notification can be disabled temporarily in case it's not yet needed, turns out to be too noisy etc.
3. Notify when - A critical health state always triggers a notification, but optionally also deviating states can be included.
4. Scope - In the example health states for all monitors on pods in the default Kubernetes namespace will be sent. Use the available filters in the [scope](#scopes) section to change this selection.

### Scope

There are 4 possible scope filters. By default a notification will be sent for each critical (and optionally deviating) health state. The filters are used to limit this scope. A health state will only result in a notification when it matches all filters.

* Monitors: Select 1 or more specific monitors. Notifications will only be sent for health states of the selected monitors.
* Monitor tags: Select 1 or more monitor tags. Notifications will only be sent for health states of monitors that have at least one of the selected tags.
* Component types: Select 1 or more component types. Notifications will only be sent for health states of components of the selected types.
* Component tags: Select 1 or more component tags. Notifications will only be sent for health states of components that have at least one of the selected tags.

## Where to send notifications?

StackState can send notifications to different external systems via channels. Supported channels are:

* [Slack](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/channels/slack) - Send notifications to Slack
* [Webhook](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/channels/webhook) - Send notifications to a webhook, the webhook endpoint can translate the StackState payload into any custom third-party API needed
* [Opsgenie](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/channels/opsgenie) - Send notifications to OpsGenie

In general StackState sends two types of messages for notifications:

1. An `open` message when a health state goes to Critical or Deviating. This message can be repeated when there are changes in the health state
2. A `close` message when the health state isn't Critical or Deviating anymore or when for other reasons (the component disappeared, the monitor was removed, etc.) the notification isn't active anymore.


# Notification channels

StackState v6.0


# Slack

StackState v6.0

## Configure Slack notifications

To send notifications to Slack follow these steps:

1. [Connect StackState to your Slack workspace](#connect-slack-workspace)
2. [Select a Slack channel to sent the notifications to](#select-a-slack-channel)
3. [Add and test the channel](#add-and-test-the-channel)

### Connect Slack workspace

Click on the "Choose workspace" button. This will open a Slack webpage where StackState asks for permission to list channels and send messages to Slack channels. Make sure that in the top-right corner you have the desired Slack workspace selected.

Click "Allow" to continue.

### Select a Slack channel

![Select the Slack channel](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c7c6b19a1c78daf6136ce01eb37d5b007a425064%2Fnotifications-slack-channel-configuration.png?alt=media)

Back in StackState you can now select a Slack channel from the list. Select the channel where the notification messages need to be sent.

{% hint style="info" %}
Private channels won't be listed automatically. To select a private channel first invite the StackState bot into the private channel by sending a Slack message in the channel that mentions the bot `@StackState` and selecting "Invite them." Now the channel will become available in the list.
{% endhint %}

## Add and test the channel

Finally click the "Add channel" button. This adds the channel to the list of channels on the right. It will show a "Test" button. Press it to verify that the test message appears in the selected Slack channel.

## Slack messages for notifications

When a notification is opened a new Slack message is created. This message will be updated for changes, usually only when the health state changes. In the thread for the message every change will show up as a message as well. Finally, when the notification is closed the Slack message is updated again (now the bar that shows the health state is grey) and a final message is added to the Slack thread that describes why the notification was closed.

<figure><img src="https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-1277ea4611f4a2d748903725288fcd34cc96f31d%2Fnotifications-slack-message-example.png?alt=media" alt="Slack thread example" width="75%"><figcaption><p>A Slack message with its thread for a closed notification</p></figcaption></figure>

## Related

* [Troubleshooting](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/troubleshooting)


# Teams

StackState v6.0

## Configure Teams notifications

To send notifications to Slack follow these steps:

1. [Create a Power Automate Flow](#create-a-power-automate-flow)
2. [Add and test the channel](#add-and-test-the-channel)

### Create a Power Automate Flow

In Teams, create a new Flow from the "Webhook" template. ![Create Flow from Webhook template](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-921b8397c6134158f10113068cd4d6b11977c09b%2Fnotifications-teams-webhook-template.png?alt=media)

Select the Team and Channel you want the notification pasted to and save the flow.

Edit the flow and click the "When a Teams webhook request is received" box.\
Copy the HTTP URL parameter.

![Select URL from Flow](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fe7e7207c26fafccdf357b0efbec5c26ae72f59b%2Fnotifications-teams-select-url.png?alt=media)

## Add and test the channel

![Configure Teams Channe](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-4dcbdf8bd163bcaaf2ac946bfd16d3777f52e2c8%2Fconfigure-teams-channel.png?alt=media)

Back in StackState you can now use the Webhook URL to create a notification channel.

## Teams messages for notifications

When a notification is opened or closed a new Teams message is created in the channel.

<figure><img src="https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-b0b7d7205baf8cd7c7eaa4880299b6d894b169a8%2Fnotifications-teams-example.png?alt=media" alt="Teams example" width="75%"><figcaption><p>Teams messages for an open and close notification</p></figcaption></figure>

## Related

* [Troubleshooting](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/troubleshooting)


# Webhook

StackState v6.0

Webhooks are custom HTTP callbacks that you define and run. They can take any action needed whenever a notification is opened or closed. For example by creating a ticket in a ticketing system that's not supported natively by StackState. Or by simply writing the notification messages to an S3 bucket for future reference.

The webhook channel sends the notifications data as [JSON over HTTP](#webhook-requests-and-payload).

## Configure a webhook

![Configure a webhook](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-5b99ecd26ec51079b3ddbcad58527d648b0c5c55%2Fnotifications-webhook-channel-configuration.png?alt=media)

To configure a webhook complete the fields:

1. URL - enter the URL of the webhook endpoint. The URL must be percent-encoded if it has special characters.
2. Secret token - a secret token that StackState will include in every request to [validate it](#validate-the-requests)
3. Metadata - add extra key/value pairs that are included in the payload. This can be used when the same endpoint handles multiple StackState webhooks and needs some extra information
4. Enable SSL verification - (default on) enable SSL certificate validation. Only disable when using self-signed certificates or certificate authorities not supported by StackState

Finally select "Add channel". The webhook channel will appear on the right. To test that the webhook works send a test message by clicking the "Test" button.

## Webhook requests and payload

The Webhook channel sends data as HTTP POST requests. The endpoint and payload are documented in an [OpenAPI specification](https://github.com/StackVista/stackstate-openapi/tree/master/spec_webhook).

### Example payload for a notification open request

```
{
    "component": {
        "identifier": "urn:kubernetes:/k8s-demo-cluster:sock-shop:service/catalogue",
        "link": "https://play.stackstate.com/#/components/urn%3Akubernetes%3A%2Fk8s-demo-cluster%3Asock-shop%3Aservice%2Fcatalogue?timeRange=1702624556757_1702646156757&timestamp=1702635356757",
        "name": "catalogue",
        "tags": [
            "app.kubernetes.io/component:catalogue",
            "app.kubernetes.io/instance:sock-shop",
            "app.kubernetes.io/managed-by:Helm",
            "app.kubernetes.io/name:sock-shop",
            "app.kubernetes.io/version:0.3.5",
            "cluster-name:k8s-demo-cluster",
            "cluster-type:kubernetes",
            "component-type:kubernetes-service",
            "domain:business",
            "extra-identifier:catalogue",
            "helm.sh/chart:sock-shop",
            "name:catalogue",
            "namespace:sock-shop",
            "service-type:ClusterIP",
            "stackpack:kubernetes"
        ],
        "type": "service"
    },
    "event": {
        "state": "CRITICAL",
        "title": "HTTP - response time - is above 3.0 seconds",
        "triggeredTimeMs": 1702635356757,
        "type": "open"
    },
    "monitor": {
        "identifier": "urn:stackpack:kubernetes-v2:shared:monitor:kubernetes-v2:http-response-time",
        "link": "https://play.stackstate.com/#/monitors/urn%3Astackpack%3Akubernetes-v2%3Ashared%3Amonitor%3Akubernetes-v2%3Ahttp-response-time",
        "name": "HTTP - response time - is above 3 seconds",
        "tags": []
    },
    "notificationConfiguration": {
        "identifier": "urn:system:default:notification-configuration:testing-2",
        "link": "https://play.stackstate.com/#/notifications/urn%3Asystem%3Adefault%3Anotification-configuration%3Atesting-2",
        "name": "Test Notification"
    },
    "notificationId": "836f628c-1258-4500-b1c7-23884e00f439",
    "metadata": {
        "team": "Team A"
    }
}
```

The sections in the `open` payload are:

1. Component: the StackState component that the notification applies to. This includes the components name, identifier, type, and tags. It also has a link to the StackState UI that will open the component at the time of the health state change
2. Event: the event that triggered this notification. It can either be of type `open` or `close` (see next section). An `open` state means that the monitor is still in a critical (or deviating) state for the specified component. A `close` state means that the monitor was open before but that the issue has been resolved. The state and triggered time are included. Also included is a `title` which is a short description of the problem as provided by the monitor, it is the same title shown in the highlights page of the component, this can be different and more detailed than the monitor name.
3. Monitor: the monitor that triggered the notification. Next to the monitor name, tags and identifier also a link is included. The link will open the monitor in the StackState UI.
4. Notification configuration: The notification configuration for this notification. Includes a name, identifier and link. The link will open the notification configuration in the StackState UI.
5. Notification id: A unique identifier for this notification. See also the [Notification life cycle](#notification-life-cycle)
6. Metadata: It's possible to specify metadata on a webhook channel. The metadata is one-to-one reproduced here as a set of key/value pairs.

### Example payload for a notification close request

```
{
    "component": {
        "identifier": "urn:kubernetes:/gke-demo-dev.gcp.stackstate.io:sock-shop:service/catalogue",
        "link": "https://stac-20533-webhook-channel-management-api.preprod.stackstate.io/#/components/urn%3Akubernetes%3A%2Fgke-demo-dev.gcp.stackstate.io%3Asock-shop%3Aservice%2Fcatalogue?timeRange=1702624556757_1702646156757&timestamp=1702635356757",
        "name": "catalogue",
        "tags": [
            "app.kubernetes.io/component:catalogue",
            "app.kubernetes.io/instance:sock-shop",
            "app.kubernetes.io/managed-by:Helm",
            "app.kubernetes.io/name:sock-shop",
            "app.kubernetes.io/version:0.3.5",
            "cluster-name:gke-demo-dev.gcp.stackstate.io",
            "cluster-type:kubernetes",
            "component-type:kubernetes-service",
            "domain:business",
            "extra-identifier:catalogue",
            "helm.sh/chart:sock-shop",
            "name:catalogue",
            "namespace:sock-shop",
            "service-type:ClusterIP",
            "stackpack:kubernetes"
        ],
        "type": "service"
    },
    "event": {
        "reason": "HealthStateResolved",
        "type": "close"
    },
    "monitor": {
        "identifier": "urn:stackpack:kubernetes-v2:shared:monitor:kubernetes-v2:http-response-time",
        "link": "https://stac-20533-webhook-channel-management-api.preprod.stackstate.io/#/monitors/urn%3Astackpack%3Akubernetes-v2%3Ashared%3Amonitor%3Akubernetes-v2%3Ahttp-response-time",
        "name": "HTTP - response time - is above 3 seconds",
        "tags": []
    },
    "notificationConfiguration": {
        "identifier": "urn:system:default:notification-configuration:testing-2",
        "link": "https://stac-20533-webhook-channel-management-api.preprod.stackstate.io/#/notifications/urn%3Asystem%3Adefault%3Anotification-configuration%3Atesting-2",
        "name": "Test Notification"
    },
    "notificationId": "836f628c-1258-4500-b1c7-23884e00f439",
    "tags": {
        "team": "Team A"
    }
}
```

The sections in the `close` payload are the same as in the `open` payload except for the `event`. The `type` is now `close` and there is only a `reason` field indicating why the notification was closed. The value in this field is an enum, the [OpenAPI specification](https://github.com/StackVista/stackstate-openapi/tree/master/spec_webhook) documents the possible values.

## Notification life cycle

As can be seen from the payload each notification is uniquely identified by its `notificationId`. It's possible, even common, to receive more than one message for the same notification, but they will always be sent according to this life cycle.

A notification is first created when a monitor state changes to deviating or critical (whether deviating is applicable depends on the [notification settings](https://archivedocs.stackstate.com/monitors-and-alerts/configure#configure-when-to-notify)). A message with event type `open` is sent to the webhook.

A notification can be updated when the `state` or the `title` in the event change. Changes to the component and other parts of the message will be included but on their own they won't trigger an update. A notification update also sends a message with event type `open` to the webhook. The message will have the same `notificationId` which can be used to update the data in the external system (instead of creating a new notification).

Finally a notification is closed when the monitor state changes back to a non-critical (or deviating) state. A message with event type `close` is sent to the webhook. This is also the last time that the specific `notificationId` is used.

Note that a notification can be both opened and closed for different reasons than a health state change:

* A tag is added to a component or monitor. This can cause some critical monitor health state to match the selection criteria in a notification configuration and corresponding notifications will be opened.
* For the same reason removal of a tag from a component or monitor can close a notification even though the health state is still critical.
* Changes to the notification configuration itself can also result in many new notifications being opened or closed.

## Validate the requests

The secret token specified in the channel configuration is included in the webhook requests in the `X-StackState-Webhook-Token` header. Your webhook endpoint can check the value to verify the requests is legitimate.

## Retries

The webhook channel will retry requests for a notification until it receives a status 200 OK response (the body in the response is ignored). If the webhook fails to process the message (for example because a database is unreachable right at the time) it can simply respond with a 500 status code. StackState will re-send the same message within a few seconds in the hope that the issue has been resolved now.

If a notification was updated or closed the old message will however be discarded and the new, updated, message will be send and again retried until it succeeds.

## Example webhook

To test how webhooks work you can use this simply Python script that starts an HTTP server and writes the received payload to standard out.

1. Save this Python script as `webhook.py`:

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys

class WebhookHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        notification = json.loads(self.rfile.read(content_len))
        print("Notification received: ", json.dumps(notification, indent = 2))
        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(('', int(sys.argv[1])), WebhookHTTPRequestHandler)
httpd.serve_forever()
```

2. Run the webhook server on an unused port (for example 8000): `python3 webhook.py 8000`
3. Configure the webhook in StackState with the URL for your webhook server `http://webhook.example.com:8000`
4. Click `test` on the webhook channel

{% hint style="info" %}
The URL for your webhook must be accessible by StackState, so a localhost address or a local ip-address won't be enough.
{% endhint %}

The example doesn't authenticate the request, which can be added by verifying the value of the [token header](#validate-the-requests).

Instead of implenting this by hand it's also possible to use the [OpenAPI specification](https://github.com/StackVista/stackstate-openapi/tree/master/spec_webhook) to generate a server implementation in any of the languages supported by the [OpenAPI generators project](https://openapi-generator.tech/).

## Related

* [Troubleshooting](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/troubleshooting)


# Opsgenie

StackState v6.0

## Configure Opsgenie notifications

To send notifications to Slack follow these steps:

1. [Create an integration in OpsGenie](#create-integration)
2. [Create the channel](#create-and-test-the-channel)

### Create integration

In order to integrate StackState with OpsGenie, a global "API key" needs to be created. The responders for a notification can be different for each notification and will be configured in StackState.

In Opsgenie, go to "Settings -> Integrations".

* Click the "Add integration" button
* Search for the "API" integration type.
* Choose a name for this integration, but *do not select an Assignee team*.

When the integration has been created, it will have an "API key".

### Create and test the channel

![Create the channel](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ab2702cb4d5a87d7ff45e7868cd633f2c5ef18ca%2Fnotifications-opsgenie-channel-configuration.png?alt=media)

Select the appropriate region for your OpsGenie account and enter the "API key". Choose responders for the notification; *users*, *teams*, *schedules* and *escalations* are available for this.

Click the "Add channel" button. This adds the channel to the list of channels on the right. It will show a "Test" button. Pressing it will generate a test alert in OpsGenie.

## OpsGenie alerts for notifications

When a notification is opened a new OpsGenie alert is created. This message will be updated for changes, usually only when the health state changes. When the notification is closed the OpsGenie alert is closed again. A note on the alert contains the reason for closing it.

<figure><img src="https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-7e81c21e69521d719c37bc3504dfb14994c59f03%2Fnotifications-opsgenie-alert-example.png?alt=media" alt="Opsgenie alert" width="75%"><figcaption><p>An OpsGenie alert generated by StackState</p></figcaption></figure>

## Related

* [Troubleshooting](https://archivedocs.stackstate.com/monitors-and-alerts/notifications/troubleshooting)


# Troubleshooting

StackState v6.0

When a notification channel fails to send out notifications the notification overview will show an error status. To inspect the errors:

1. Click on the notification
2. The top of the page shows a banner with a summary of the errors
3. Scroll down to the channels, click on the "error" link for the affected channel(s) to open the error details.

## Common errors

### Slack

Slack errors usually contain an error code:

* `token_revoked`, `token_expired` or `missing_scope`: These error codes all indicate a problem with the authorization of StackState to post messages to Slack. To solve these recreate the channel to re-authorize StackState with Slack such that all required permissions are granted.
* For other error codes see [Slack API error codes](https://api.slack.com/automation/cli/errors).

### HTTP

Most channels, specifically the webhook, expect a HTTP response with status 200 OK. Other responses are considered an error. HTTP errors contain a, usually short, message and the status code that was received instead of 200 OK.

Verify that any configured URLs and tokens are correct and, in case of the webhook, that POST requests are handled properly and return a 200 OK response.

### Other

In case the error is of type "Other" StackState is most likely not able to even connect to the external service or webhook. Verify that URL is correct, can be resolved and can be accessed by StackState.


# Customize


# Add a monitor using the CLI

StackState v6.0

## Overview

StackState provides [monitors out of the box](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-monitors), which provide monitoring on common issues that can occur in a Kubernetes cluster. It's also possible to configure custom monitors for the metrics collected by StackState or application metrics ingested [from Prometheus](https://archivedocs.stackstate.com/metrics/advanced-metrics/k8s-prometheus-remote-write).

## Steps

Steps to create a monitor:

1. [Write the outline of the monitor](#write-the-outline-of-the-monitor)
2. [Bind the results of the monitor to the correct component](#bind-the-results-of-the-monitor-to-the-correct-components)
3. [Write the remediation hint](#write-the-remediation-hint)
4. [Create or update the metric binding in StackState](#create-or-update-the-monitor-in-stackstate)
5. [Verify the monitor produces the expected result](#verifying-the-results-of-a-monitor)
6. [Common issues](#common-issues)

As an example the steps will add a monitor for the `Replica counts` of Kubernetes deployments.

## Write the outline of the monitor

Create a new YAML file called `monitor.yaml` and add this YAML template to it to create your own monitor. Open it in your favorite code editor to change it throughout this guide. At the end the StackState CLI will be used to create and update the monitor in StackState.

```
nodes:
- _type: Monitor
  arguments:
    metric:
      query: 
      unit:
      aliasTemplate: 
    comparator: 
    threshold: 
    failureState: 
    urnTemplate:
    titleTemplate: 
  description: 
  function: {{ get "urn:stackpack:common:monitor-function:threshold"  }}
  identifier: urn:custom:monitor:...
  intervalSeconds: 30
  name: 
  remediationHint: 
  status: 
  tags: {}
```

The fields in this template are:

* `_type`: StackState needs to know this is a monitor so, value always needs to be `Monitor`
* `query`: A PromQL query. Use the [metric explorer](https://archivedocs.stackstate.com/metrics/k8sts-explore-metrics) of your StackState instance, <http://your-stackstate-instance/#/metrics>, and use it to construct query for the metric of interest.
* `unit`: The unit of the values in the time series returned by the query or queries, used to render the Y-axis of the chart. See the [supported units](https://archivedocs.stackstate.com/reference/k8sts-chart-units) reference for all units.
* `aliasTemplate`: An alias for time series in the metric chart. This is a template that can substitute labels from the time series using the `${my_label}` placeholder.
* `comparator`: Choose one of LTE/LT/GTE/GT to compare the threshold against the metric. Time series for which `<metric> <comparator> <threshold>` holds true will produce the failure state.
* `threshold`: A numeric threshold to compare against.
* `failureState`: Either "CRITICAL" or "DEVIATING". "CRITICAL" will show as read in StackState and "DEVIATING" as orange, to denote different severity.
* `urnTemplate`: A template to construct the urn of the component a result of the monitor will be [bound to](#bind-the-results-of-the-monitor-to-the-correct-components).
* `titleTemplate`: A title for the result of a monitor. Because multiple monitor results can bind to the same component, it's possible to substitute time series labels using the `${my_label}` placeholder.
* `description`: A description of the monitor.
* `function`: A reference to the monitor function that will execute the monitor. Currently only `{{ get "urn:stackpack:kubernetes-v2:shared:monitor-function:threshold" }}` is supported.
* `identifier`: An identifier of the form `urn:custom:monitor:....` which uniquely identifies the monitor when updating its configuration.
* `intervalSeconds`: The interval at which the monitor executes. For regular real-time metric 30 seconds is advised. For longer-running analytical metric queries a bigger interval is recommended.
* `name`: The name of the monitor
* `remediationHint`: A description of what the user can do when the monitor fails. The format is markdown, with optionally use of handlebars variables to customize the hint based on time series or other data ([more explanation below](#write-the-remediation-hint)).
* `status`: Either `"DISABLED"` or `"ENABLED"`. Determines whether the monitor will run or not.
* `tags`: Add tags to the monitor to help organize them in the monitors overview of your StackState instance, <http://your-StackState-instance/#/monitors>

For example, this could be the start for a monitor which monitors the available replicas of a deployment:

```
nodes:
- _type: Monitor
  arguments:
    metric:
      query: "kubernetes_state_deployment_replicas_available" 
      unit: "short"
      aliasTemplate: "Deployment replicas" 
    comparator: "LTE"
    threshold: 0.0
    failureState: "DEVIATING"
    urnTemplate: 
  description: "Monitor whether a deployment has replicas.  
  function: {{ get "urn:stackpack:kubernetes-v2:shared:monitor-function:threshold"  }}
  identifier: urn:custom:monitor:deployment-has-replicas
  intervalSeconds: 30
  name: Deployment has replicas
  remediationHint: 
  status: "ENABLED"
  tags:
  - "deployments"
```

The `urnTemplate` and `remediationHint` will be filled in the next steps.

## Bind the results of the monitor to the correct components

The results of a monitor need to be bound to components in StackState, to be visible and usable. The result of a monitor is bound to a component using the component `identifiers`. Each component in StackState has one or more identifiers that uniquely identify the component. To bind a result of a monitor to a component, it's required to provide the `urnTemplate`. The `urnTemplate` substitutes the labels in the time series of the monitor result into the template, producing an identifier matching a component. This is best illustrated with the example:

The metric that's used in this example is the `kubernetes_state_deployment_replicas_available` metric. Run the metric in the metric explorer to observe what labels are available on the time series:

![The available replicas in the metric explorer](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fa5bc3332a848916a803cbb5b475d9e0535f2cd9%2Favailable-replicas-metric-inspector.png?alt=media)

In the above table it's shown the metric has labels like `cluster_name`, `namespace` and `deployment`.

Because the metric is observed on deployments, it's most logical to bind the monitor results to deployment components. To do this, it's required to understand how the identifiers for deployments are constructed:

1. In the UI, navigate to the `deployments` view and select a single deployment.
2. Open the `Topology` view, and click the deployment component.
3. When expanding the `Properties` in the right panel of the screen, the identifiers will show after hovering as shown below:

![Finding a component identifier](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-a086aeeb7fb28cb29483cc695e2a215e04da2fc0%2Fcomponent-identifier.png?alt=media)

The identifier is shown as `urn:kubernetes:/preprod-dev.preprod.stackstate.io:calico-system:deployment/calico-typha`. This shows that the identifier is constructed based on the cluster name, namespace and deployment name. Knowing this, it's now possible to construct the `urnTemplate`:

```
  ...
  urnTemplate: "urn:kubernetes:/${cluster_name}:${namespace}:deployment/${deployment}" 
  ...
```

[To verify](#verifying-the-results-of-a-monitor) whether the `urnTemplate` is correct, is explained further below.

## Write the remediation hint

The remediation hint is there to help users find the cause of an issue when a monitor fires. The remediation hint is written in [markdown](https://en.wikipedia.org/wiki/Markdown). It's also possible to use the labels that are on the time series of the monitor result using a handlebars template, as in the following example:

```
  ...
  remediationHint: |-
    To remedy this issue with the deployment {{ labels.deployment }}, consider taking the following steps:
    
    1. Look at the logs of the pods created by the deployment
  ...
```

## Create or update the monitor in StackState

After completing the `monitor.yaml`, use the [StackState CLI](https://archivedocs.stackstate.com/cli/k8sts-cli-sts) to create or update the monitor:

```bash
sts monitor apply -f monitor.yaml
```

Verify whether the monitor produces the expected results, using the steps [below](#verifying-the-results-of-a-monitor).

{% hint style="warning" %}
The identifier is used as the unique key of a monitor. Changing the identifier will create a new monitor instead of updating the existing one.
{% endhint %}

The `sts monitor` command has more options, for example it can list all monitors:

```bash
sts monitor list
```

To delete a monitor use

```bash
sts monitor delete --id <id>
```

To edit a monitor, edit the original of the monitor that was applied, and apply again. Or there is a `sts monitor edit` command to edit the configured monitor in the StackState instance directly:

```bash
sts monitor edit --id <id>
```

The `<id>` in this command isn't the identifier but the number in the `Id` column of the `sts monitor list` output.

## Enable or disable the monitor

A monitor can be enabled or disabled. Enabled means the monitor will produce results, disabled means it will suppress all output. Use the following commands to enable/disable:

```bash
sts monitor enable/disable --id <id>
```

## Verifying the results of a monitor

It's good practice to, after a monitor is made, validate whether it produces the expected result. The following steps can be taken:

### Verify the execution of the monitor

Go to the monitor overview page (<http://your-StackState-instance/#/monitors>) and find your monitor.

1. Verify the `Status` column is in `Enabled` state. If the monitor is in `Disabled` state, [enable it](#enable-or-disable-the-monitor). If the status is in `Error` state, follow the steps below [to debug](#the-monitor-is-showing-an-error-in-the-monitor-status-overview).
2. Verify you see the expected amount of states in the `Clear`/`Deviating`/`Critical` column. If the number of states is significantly lower or higher than the amount of components you meant to monitor, the PromQL query might be giving too many results.

### Verify the binding of the monitor

Observe whether the monitor is producing a result on one of the components that it's meant to monitor for. If the monitor doesn't show up, follow [these steps](#the-result-of-the-monitor-isnt-showing-on-a-component) to remedy.

## Common issues

### The result of the monitor isn't showing on a component

First check if the monitor is actually [producing results](#verify-the-execution-of-the-monitor). If this is the case but the monitor results do not show up on the components, there might be a problem with the binding. First use the following command to verify:

```bash
sts monitor status --id <id>
```

If the output has `Monitor health states with identifier which has no matching topology element (<nr>): ....`, this shows that the `urnTemplate` may not generate an identifier matching the topology. To remedy this [revisit your urnTemplate](#bind-the-results-of-the-monitor-to-the-correct-components).

### The monitor is showing an error in the monitor status overview

Get the status of the monitor through the CLI

```bash
sts monitor status --id <id>
```

The section `Monitor Stream errors:` will show the errors happening on the monitor and offer further help.


# Override monitor arguments

StackState v6.0

## Overview

StackState provides [monitors out of the box](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-monitors), which provide monitoring on common issues that can occur in a Kubernetes cluster. Those monitors work with certain default arguments that suit most of the use cases but sometimes there's need to adapt its behaviour by overriding some of such default arguments like `threshold` or `failureState`. The mechanism to declare the overrides is via kubernetes resource annotations that denote to which monitor and component they should apply. For example we could override the `failureState` for the `Available service endpoints` monitor for a specific service where we want to signal a `CRITICAL` state when it fails rather than the default `DEVIATING`.

## How to

* [Build an override annotation](#build-an-override-annotation)
* [What monitors allow overriding arguments?](#what-monitor-allows-overriding)
* [Build an override for a custom monitor](#build-an-override-for-a-custom-monitor)

As an example the steps will override the arguments for the `Available service endpoints` monitor of Kubernetes HTTP services.

## How to build my annotation

The override annotations keys for StackState monitors follow the following convention:

```
monitor.${owner}.stackstate.io/${monitorShorName}
```

The `owner` property represents who created such a monitor, for the out of the box monitors is `kubernetes-v2`, and the `monitorShorName` property represents the id of the monitor and can be extracted from the `identifier` property of a monitor which can be read from the cli when listing or inspecting monitors

```
sts monitor list

ID              | STATUS  | IDENTIFIER                                                                          | NAME                                        | FUNCTION ID     | TAGS                                                                                  
8051105457030   | ENABLED | urn:stackpack:kubernetes-v2:shared:monitor:kubernetes-v2:service-available-endpoint | Available service endpoints                 | 233276809885571 | [services]         
```

In our example the identifier is `urn:stackpack:kubernetes-v2:shared:monitor:kubernetes-v2:service-available-endpoint` and the `monitorShorName` corresponds to the very last segment as in `service-available-endpoint` therefore the annotation key is:

```bash
monitor.kubernetes-v2.stackstate.io/service-available-endpoint
```

the annotation payload is a JSON object where the following optional arguments can be defined:

* `threshold`: optional.A numeric threshold to compare against.
* `failureState`: optional. Either "CRITICAL" or "DEVIATING". "CRITICAL" will show as read in StackState and "DEVIATING" as orange, to denote different severity.
* `enabled`: optional. Boolean that determines if the monitor would produce a health state for that component.

The full annotation then would look like

```bash
    monitor.kubernetes-v2.stackstate.io/service-available-endpoint: |-
      {
        "threshold": 0.0,
        "failureState": "CRITICAL",
        "enabled": true
      }
```

## What monitors allow overriding arguments?

* [Available service endpoints](https://archivedocs.stackstate.com/kubernetes-monitors#available-service-endpoints)
* [Cpu limits resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#cpu-limits-resourcequota)
* [Cpu requests resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#cpu-requests-resourcequota)
* [Memory limits resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#memory-limits-resourcequota)
* [Memory requests resourcequota](https://archivedocs.stackstate.com/kubernetes-monitors#memory-requests-resourcequota)
* [Node Disk Pressure](https://archivedocs.stackstate.com/kubernetes-monitors#node-disk-pressure)
* [Node Memory Pressure](https://archivedocs.stackstate.com/kubernetes-monitors#node-memory-pressure)
* [Node PID Pressure](https://archivedocs.stackstate.com/kubernetes-monitors#node-pid-pressure)
* [Node Readiness](https://archivedocs.stackstate.com/kubernetes-monitors#node-readiness)
* [Out of memory for containers](https://archivedocs.stackstate.com/kubernetes-monitors#out-of-memory-for-containers)

## Build an override for a custom monitor

Any custom threshold monitor created using the guide at [Add a threshold monitor to components using the CLI](https://archivedocs.stackstate.com/monitors-and-alerts/customize/k8s-add-monitors-cli) is suitable to override arguments, as [the example shows](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-add-monitors-cli#write-the-outline-of-the-monitor) an identifier for a custom monitor is structured as `urn:custom:monitor:{monitorShortName}`and the override annotation key for such an identifier is expected to be

```bash
monitor.custom.stackstate.io/${monitorShortName}
```

The example uses the identifier `urn:custom:monitor:deployment-has-replicas` therefore the annotation key would be

```bash
monitor.custom.stackstate.io/deployment-has-replicas
```

And the full annotation would look like

```bash
    monitor.custom.stackstate.io/deployment-has-replicas: |-
      {
        "threshold": 0.0,
        "failureState": "CRITICAL"
        "enabled": true
      }
```


# Write a remediation guide

StackState v6.0

## Overview

StackState provides [monitors out of the box](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-monitors), which provide monitoring on common issues that can occur in a Kubernetes cluster. These monitors also contain out of the box remediation guides which are meant to guide users in accurately troubleshooting issues. They are created using the best practices and community knowledge. Follow the indications on this page to learn how to write an effective remediation guide yourself.

## Guidelines

* Provide step by step instructions to guide a user into solving the issue detected by the monitor;
* Make sure the instructions are ordered by the most likely cause(s).
* If possible, include links to relevant data and/or resources to speed up the investigation.
* Keep it short and on point:
  * Avoid over explaining - add links to supporting documentation if that's the case;
  * Avoid using a table of contents and similar content blocks;
  * Avoid having a summary of the same content;
* Try to format the guide in a structured way. Use:
  * bullet points
  * numbering
  * short sentences
  * paragraphs
  * inline formatted examples
* If there are open ends (there might be different causes which are still unknown), provide guidance for escalating the issue. E.g. provide the user with a support link/ number, etc.

## Remediation guide example

```
When a Kubernetes container has errors, it can enter into a state called CrashLoopBackOff, where Kubernetes attempts to restart the container to resolve the issue. The container will continue to restart until the problem is resolved.Take the following steps to diagnose the problem:

### Pod Events

Check the pod events to identify any explicit errors or warnings.
1. Go to the "Events" section in the middle of the [Pod highlight page](/#/components/{{ componentUrnForUrl }})
2. Check if there is are events like "BackOff", "FailedScheduling", "FailedAttachVolume" or "OOMKilled" in the Alert Category by clicking on 'Alerts'.
3. You can see the details of the event (click on the event) to give more information about the issue.
4. If the 'Show related event' option is enabled all events of resources related to this resource like a deployment will also show up and can give you a clue if any change on them is causing this issue. You can see this by checking if there is a correlation between the time of a deployment and a change of behaviour seen by the metrics and events of this pod.
For easy correlation you can use 'shift'-'click' to add markers to the different graph, log and event widgets.
    
### Container Logs
Check the container logs for any explicit errors or warnings
Inspect the [Logs](/#/components/{{ componentUrnForUrl }}#logs) of all the containers in this pod.
Search for hints in the logs by:
1.  Looking for changes in logging pattern, by looking at the number of logs per time unit (The histogram bars).
    In many cases the change in pattern will indicate what is going on.
    You can click-drag on the histogram bars to narrow the logs displayed to that time-frame.
2.  Searching for "Error" or "Fatal" in the search bar.
3.  Looking at the logs around the time that the monitor triggered
    
### Recent Changes
Look at the pod age in the "About" section on the [Pod highlight page](/#/components/{{ componentUrnForUrl }}) to identify any recent deployments that might have caused the issue
1. The "Age" is shown in the "About" section on the left side of the screen
2. If the "Age" and the time that the monitor was triggered are in close proximity then take a look at the most recent deployment by clicking on [Show last change](/#/components/{{ componentUrnForUrl }}#lastChange).
```

## Inserting links

The syntax we use is different for "deep links" vs "in-page links". The "deep links" will redirect the user from the current page, whilst the "in-page links" will keep the user on the same page.

### Deep links

To link to any perspective (e.g. "hightlights", "topology", "events", "metrics") of the current resource, use the following syntax:

```
[highlight page](/#/components/{{ componentUrnForUrl }})
```

```
[topology](/#/components/{{ componentUrnForUrl }}/topology)
```

```
[events](/#/components/{{ componentUrnForUrl }}/events)
```

```
[metrics](/#/components/{{ componentUrnForUrl }}/metrics)
```

### In-page links

To link to any additional data (e.g. "show logs", "show last change", "show status", "show configuration") on the current resource, use the following syntax:

```
[logs](/#/components/{{ componentUrnForUrl }}#logs)
```

```
[last change](/#/components/{{ componentUrnForUrl }}#lastChange)
```

```
[status](/#/components/{{ componentUrnForUrl }}#status)
```

```
[configuration](/#/components/{{ componentUrnForUrl }}#configuration)
```


# Explore Metrics

StackState v6.0

You can find the metrics explorer at the bottom of the StackState main menu. Use it to execute any PromQL query and visualize the resulting time series. The query result is shown in a chart for the selected time range and in a table that shows the last value together with the labels for the time series.

![Metrics Explorer](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-427fb0b8a38dbaa9d0abb6c479408dec23db2086%2Fk8s-metrics-explorer.png?alt=media)

## PromQL queries

The query input field has auto-suggestions for metric names, label names and values, and supported PromQL functions. See the Prometheus documentation for a complete [PromQL guide and reference](https://prometheus.io/docs/prometheus/latest/querying/basics/). StackState also adds 2 default parameters that can be used in any query: `${__interval}` and `${__rate_interval}`. They can be used to scale the aggregation interval automatically with the chart resolution ([more details](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-writing-promql-for-charts)).

## See also

* [Writing PromQL queries for representative charts](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-writing-promql-for-charts)
* [PromQL documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/)
* [PromQL operators](https://prometheus.io/docs/prometheus/latest/querying/operators/)
* [PromQL functions](https://prometheus.io/docs/prometheus/latest/querying/functions/)
* [Anatomy of a PromQL Query](https://promlabs.com/blog/2020/06/18/the-anatomy-of-a-promql-query/)
* [Selecting Data in PromQL](https://promlabs.com/blog/2020/07/02/selecting-data-in-promql/)
* [How to join multiple metrics](https://iximiuz.com/en/posts/prometheus-vector-matching/)
* [Aggregation over time](https://iximiuz.com/en/posts/prometheus-functions-agg-over-time/)


# Custom charts


# Adding custom charts to components

StackState v6.0

## Overview

StackState provides already many metric charts by default on most types of components that represent Kubernetes resources. Extra metric charts can be added to any set of components whenever needed. When adding metrics to components there are 2 options:

1. The metrics are already collected by StackState but aren't visualized on a component by default
2. The metrics aren't yet collected by StackState at all and therefore aren't available yet

For option 1 the steps below will instruct you how to create a metric binding which will configure StackState to add a specific metric to a specific set of components.

In case of option 2, first make sure that the metrics are available in StackState, by sending them to StackState using the [Prometheus remote write protocol](https://archivedocs.stackstate.com/metrics/advanced-metrics/k8s-prometheus-remote-write). Only after that continue by adding charts for the metrics to the components.

## Steps

Steps to create a metric binding:

1. [Write the outline of the metric binding](#write-the-outline-of-the-metric-binding)
2. [Write the topology query (STQL) to select the components](#write-the-topology-query)
3. [Write the PromQL query for the desired metric](#write-the-promql-query)
4. [Bind the correct time series to each component](#bind-the-correct-time-series-to-each-component)
5. [Create or update the metric binding in StackState](#create-or-update-the-metric-binding-in-stackstate)

As an example the steps will add a metric binding for the `Replica counts` of Kubernetes deployments. This is just an example, this metric binding already exists in StackState by default.

## Write the outline of the metric binding

Create a new YAML file called `metric-bindings.yaml` and add this YAML template to it to create your own metric binding. Open it in your favorite code editor to change it throughout this guide. At the end the StackState CLI will be used to create and update the metric bindings in StackState.

```
nodes:
- _type: MetricBinding
  chartType: line
  enabled: true
  tags: {}
  unit: 
  name: 
  description: 
  priority: 
  identifier: urn:custom:metric-binding:...
  queries:
    - expression:
      alias:
  scope:
  layout:
    weight:
    layouts:
      - pespective: Metrics
        tab: 
          name: 
          weight:
        section: 
          name:
          weight:
```

The fields in this template are:

* `_type`: StackState needs to know this is a metric binding so, value always needs to be `MetricBinding`
* `chartType`: StackState will support different chart types (`line`, `bar`, etc.), currently only `line` is supported
* `enabled`: Set to `false` to keep the metric binding but not show it to users
* `tags`: Will be used to organize metrics in the user interface, can be left empty using `{}`
* `unit`: The unit of the values in the time series returned by the query or queries, used to render the Y-axis of the chart. See the [supported units](https://archivedocs.stackstate.com/reference/k8sts-chart-units) reference for all units.
* `name`: The name for the metric binding
* `description`: Optional description, displayed on-hover of the name
* `priority`: \[Deprecated] One of `HIGH`, `MEDIUM`, or `LOW`. Main sort order for metrics on a component (in the order they're mentioned here), secondary sort order is the `name`.
* `identifier`: A URN (universal resource identifier), used as the unique identifier of the metric binding. It must start with `urn:custom:metric-binding:`, the remainder is free-format as long as it's unique amongst all metric bindings.
* `queries`: A list of queries to show in the chart for the metric binding (see also the following sections)
* `scope`: The topology scope of the metric binding, a topology query that selects the components on which this metric binding will be shown.
* `layout`: How to groups charts on different perspective views, e.g. on [Metrics perspective](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/perspectives/metrics-perspective.md)

Fill in all the parts already known first (with the deployment replica counts as the example)

```
_type: MetricBinding
chartType: line
enabled: true
tags: {}
unit: short
name: Replica counts
priority: MEDIUM
identifier: urn:custom:metric-binding:my-deployment-replica-counts
queries:
  - expression:
    alias:
scope:
```

The queries and scope section will be filled in the next steps. Note that the unit used is `short`, which will simply render a numeric value. In case you're not sure yet about the unit of the metric, you can leave it open and decide on the correct unit when writing the PromQL query.

## Write the topology query

Use the Explore view of the [Topology perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-topology-perspective), <http://your-stackstate-instance/#/views/explore>, and select the components that need to show the new metric. Both the basic and advanced views can be used to make the selection. The most common fields to select topology on for metric bindings are `type` for the component type and `label` for selecting all the labels. For example for the deployments:

```
type = "deployment" and label = "stackpack:kubernetes"
```

The type filter selects all deployments, while the label filter selects only components created by the Kubernetes stackpack (label name is `stackpack` and label value is `kubernetes`). The latter can also be omitted to get the same result.

Switch to the advanced mode to copy the resulting topology query and put it in the `scope` field of the metric binding.

{% hint style="info" %}
Metric bindings only support the query filters, query functions like `withNeighborsOf` aren't supported and can't be used.
{% endhint %}

## Write the PromQL query

Go to the [metric explorer](https://archivedocs.stackstate.com/metrics/k8sts-explore-metrics) of your StackState instance, <http://your-stackstate-instance/#/metrics>, and use it to query for the metric of interest. The explorer has auto-completion for metrics, labels, label values but also PromQL functions, and operators to help you out. Start with a short time range of, for example, an hour to get the best results.

For the total number of replicas use the `kubernetes_state_deployment_replicas` metric. To make the charts shown for this metric representative for the time series data extend the query to do an aggregation using the `${__interval}` parameter:

```
max_over_time(kubernetes_state_deployment_replicas[${__interval}])
```

In this specific case use `max_over_time` to make sure the chart always shows the highest number of replicas at any given time. For longer time ranges this means that a short dip in replicas won't be shown, to emphasize the lowest number of replicas use `min_over_time` instead.

Copy the query into the `expression` property of the first entry in the `queries` field of the metric binding. Use `Total replicas` as an alias. This is the name that will show in the chart legend.

{% hint style="info" %}
In StackState the size of the metric chart automatically determines the granularity of the metric shown in the chart. PromQL queries can adjusted to make optimal use of this behavior to get a representative chart for the metric. [Writing PromQL for charts](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-writing-promql-for-charts) explains this in detail.
{% endhint %}

## Bind the correct time series to each component

The metric binding with all fields filled in:

```
_type: MetricBinding
chartType: line
enabled: true
tags: {}
unit: short
name: Replica counts
priority: MEDIUM
identifier: urn:custom:metric-binding:my-deployment-replica-counts
queries:
  - expression: max_over_time(kubernetes_state_deployment_replicas[${__interval}])
    alias: Total replicas
scope: type = "deployment" and label = "stackpack:kubernetes"
```

Creating it in StackState and viewing the "Replica count" chart on a deployment component gives an unexpected result. The chart shows the replica counts for all deployments. Logically one would expect only 1 time series: the replica count for this specific deployment.

![The incorrect chart for a single deployment, it shows the replica count for all deployments](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-f8fe19e0fb1fb1e1e21b29c10bed6a4d1145813f%2Fk8s-replica-counts-without-binding.png?alt=media)

To fix this make the PromQL query specific for a component using information from the component. Filter on enough metric labels to select only the specific time series for the component. This is the "binding" of the correct time series to the component. For anyone experienced in making Grafana dashboards this is similar to a dashboard with parameters that are used in queries on the dashboard. Let's change the query in the metric binding to this:

```
max_over_time(kubernetes_state_deployment_replicas{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", deployment="${name}"}[${__interval}])
```

![After adding the parameterized filters the resulting chart looks as expected, only 1 time series for this component](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ef05cde8ee73697761d34653ed20d0318958282a%2Fk8s-replica-counts-with-binding.png?alt=media)

The PromQL query now filters on 3 labels, `cluster_name`, `namespace` and `deployment`. Instead of specifying an actual value for these labels a variable reference to fields of the component is used. In this case the labels `cluster-name` and `namespace` are used, referenced using `${tags.cluster-name}` and `${tags.namespace}`. Further the component name is referenced with `${name}`.

Supported variable references are:

* Any component label, using `${tags.<label-name>}`
* The component name, using `${name}`

![Component Highlights page that shows the labels and component name (both highlighted in red)](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-08521ff3b8c77ec6c7d06aa3dbf810c33a62db84%2Fk8s-carts-highlights.png?alt=media)

{% hint style="info" %}
The cluster name, namespace and a combination of the component type and name are ususally enough for selecting the metrics for a specific component from Kubernetes. These labels, or similar labels, are usually available on most metrics and components.
{% endhint %}

## Create or update the metric binding in StackState

Use the StackState CLI to create the metric binding in StackState. Make sure the `metric-bindings.yaml` is saved and looks like this:

```
nodes:
- _type: MetricBinding
  chartType: line
  enabled: true
  tags: {}
  unit: short
  name: Replica counts
  priority: MEDIUM
  identifier: urn:custom:metric-binding:my-deployment-replica-counts
  queries:
    - expression: max_over_time(kubernetes_state_deployment_replicas{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", deployment="${name}"}[${__interval}])
      alias: Total replicas
  scope: type = "deployment" and label = "stackpack:kubernetes"
```

Use the [StackState CLI](https://archivedocs.stackstate.com/cli/k8sts-cli-sts) to create the metric binding:

```bash
sts settings apply -f metric-bindings.yaml
```

Verify the results in StackState by opening the metrics perspective for a deployment. If you're not happy with the result simply change the metric binding in the YAML file and run the command again to update it. The list of nodes supports adding many metric bindings. Simply add another metric binding entry to the YAML array using the same steps as before.

{% hint style="warning" %}
The identifier is used as the unique key of a metric binding. Changing the identifier will create a new metric binding instead of updating the existing one.
{% endhint %}

The `sts settings` command has more options, for example it can list all metric bindings:

```bash
sts settings list --type MetricBinding
```

Finally to delete a metric binding use

```bash
sts settings delete --ids <id>
```

The `<id>` in this command isn't the identifier but the number in the `Id` column of the `sts settings list` output.

{% hint style="info" %}
The recommended way of working is to store metric bindings (and any other custom resources created in StackState) as YAML files in a Git repository. From there changes can be manually applied or it can be fully automated by using the StackState CLI in a CI/CD system like GitHub actions or GitLab pipelines.
{% endhint %}

## Other options

### More than 1 time series in a chart

{% hint style="info" %}
There is only 1 unit for a metric binding (it gets plotted on the y-axis of the chart). As a result you should only combine queries that produce time series with the same unit in 1 metric binding. Sometimes it might be possible to convert the unit. For example, CPU usage might be reported in milli-cores or cores, milli-cores can be converted to cores by multiplying by 1000 like this `(<original-query>) * 1000`.
{% endhint %}

There are 2 ways to get more than 1 time series in a single metric binding and therefore in a single chart:

1. Write a PromQL query that returns multiple time series for a single component
2. Add more PromQL queries to the metric binding

For the first option an example is given in the [next section](#using-metric-labels-in-aliases). The second option can be useful for comparing related metrics. Some typical use-cases:

* Comparing total replicas vs desired and available
* Resource usage: limits, requests and usage in a single chart

To add more queries to a metric binding simply repeat [steps](#steps) 3. and 4. and add the query as an extra entry in the list of queries. For the deployment replica counts there are several related metrics that can be included in the same chart:

```
nodes:
- _type: MetricBinding
  chartType: line
  enabled: true
  tags: {}
  unit: short
  name: Replica counts
  priority: MEDIUM
  identifier: urn:custom:metric-binding:my-deployment-replica-counts
  queries:
    - expression: max_over_time(kubernetes_state_deployment_replicas{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", deployment="${name}"}[${__interval}])
      alias: Total replicas
    - expression: max_over_time(kubernetes_state_deployment_replicas_available{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}",  deployment="${name}"}[${__interval}])
      alias: Available - ${cluster_name} - ${namespace} - ${deployment}
    - expression: max_over_time(kubernetes_state_deployment_replicas_unavailable{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}",  deployment="${name}"}[${__interval}])
      alias: Unavailable - ${cluster_name} - ${namespace} - ${deployment}
    - expression: min_over_time(kubernetes_state_deployment_replicas_desired{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}",  deployment="${name}"}[${__interval}])
      alias: Desired - ${cluster_name} - ${namespace} - ${deployment}
  scope: type = "deployment" and label = "stackpack:kubernetes"
```

![Metric binding with multiple metrics](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fe1f8ac82023abac7d7a255c1690fbb9a604015d%2Fk8s-replica-counts-multiple-timeseries.png?alt=media)

### Using metric labels in aliases

When a single query returns multiple time series per component, this will show as multiple lines in the chart. But in the legend they will all use the same alias. To be able to see the difference between the different time series the alias can include references to the metric labels using the `${label}` syntax. For example here is a metric binding for the "Container restarts" metric on a pod, note that a pod can have multiple containers:

```
type: MetricBinding
chartType: line
enabled: true
id: -1
identifier: urn:custom:metric-binding:my-pod-restart-count
name: Container restarts
priority: MEDIUM
queries:
- alias: Restarts - ${container}
  expression: max by (cluster_name, namespace, pod_name, container) (kubernetes_state_container_restarts{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"})
scope: (label = "stackpack:kubernetes" and type = "pod")
unit: short
```

Note that the `alias` references the `container` label of the metric. Make sure the label is present on the query result, when the label is missing the `${container}` will be rendered as literal text to help troubleshooting.

### Layouts

Each component can be associated with various technologies or protocols such as k8s, networking, runtime environments (e.g., JVM), protocols (HTTP, AMQP), etc. Consequently, a multitude of different metrics can be displayed for each component. For easier readability, StackState can organize these charts into tabs and sections. To display a chart (`MetricBinding`) within a specific tab or section, you need to configure the layout property. Any MetricsBinding without a specified layout will be displayed in a tab and section named `Other`.

Here is an example configuration:

```
layout:
  weight: 100
  layouts:
    - perspective: Metrics
      tab:
        name: AMQP
        weight: 150
      section:
        name: Performance
        weight: 300
```

Fields:

* `layout.weight` - This represents the weight of the chart within sections. The charts are sorted in ascending order by weight, followed by alphabetical order.
* `layout.layouts` - (array) This allows each chart to be added to multiple views (perspectives).
* `layout.layouts.perspective` - This is the type of perspective to display the chart. Currently, only the `Metrics` perspective is supported.
  * `Metrics` - display on [Metrics perspective](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/stackstate-ui/perspectives/metrics-perspective.md)
* `layout.layouts.tab` - This indicates the tab `name` and its `weight`. Tabs are sorted ascending by weight (the lowest one from all `MetricBinding`), followed by alphabetical order.
* `layout.layouts.section` - This is the section `name` and its `weight`. Sections are sorted alphabetically.


# Writing PromQL queries for representative charts

StackState v6.0

## Guidelines

When StackState shows data in a chart it almost always needs to change the resolution of the stored data to make it fit into the available space for the chart. To get the most representative charts possible follow these guidelines:

* Don't query for the raw metric but always aggregate over time (using `*_over_time` or `rate` functions).
* Use the `${__interval}` parameter as the range for aggregations over time, it will automatically adjust with the resolution of the chart
* Use the `${__rate_interval}` parameter as the range for `rate` aggregations, it will also automatically adjust with the resolution of the chart but takes into account specific behaviors of `rate`.

Applying an aggregation often means that a trade-off is made to emphasize certain patterns in metrics more than others. For example, for large time windows `max_over_time` will show all peaks, but it won't show all troughs. While `min_over_time` does the exact opposite and `avg_over_time` will smooth out both peaks and troughs. To show this behavior, here is an example metric binding using the CPU usage of pods. To try it yourself, copy it to a YAML file and use the [CLI to apply it](https://archivedocs.stackstate.com/metrics/k8s-add-charts#create-or-update-the-metric-binding-in-stackstate) in your own StackState (you can remove it later).

```
nodes:
- _type: MetricBinding
  chartType: line
  enabled: true
  tags: {}
  unit: short
  name: CPU Usage (different aggregations and intervals)
  priority: HIGH
  identifier: urn:custom:metric-binding:pod-cpu-usage-a
  queries:
    - expression: sum(max_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[${__interval}])) by (cluster_name, namespace, pod_name) /1000000000
      alias: max_over_time dynamic interval
    - expression: sum(min_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[${__interval}])) by (cluster_name, namespace, pod_name) /1000000000
      alias: min_over_time dynamic interval
    - expression: sum(avg_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[${__interval}])) by (cluster_name, namespace, pod_name) /1000000000
      alias: avg_over_time dynamic interval
    - expression: sum(last_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[${__interval}])) by (cluster_name, namespace, pod_name) /1000000000
      alias: last_over_time dynamic interval
    - expression: sum(max_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[1m])) by (cluster_name, namespace, pod_name) /1000000000
      alias: max_over_time 1m interval
    - expression: sum(min_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[1m])) by (cluster_name, namespace, pod_name) /1000000000
      alias: min_over_time 1m interval
    - expression: sum(avg_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[1m])) by (cluster_name, namespace, pod_name) /1000000000
      alias: avg_over_time 1m interval
    - expression: sum(last_over_time(container_cpu_usage{cluster_name="${tags.cluster-name}", namespace="${tags.namespace}", pod_name="${name}"}[1m])) by (cluster_name, namespace, pod_name) /1000000000
      alias: last_over_time 1m interval
  scope: (label = "stackpack:kubernetes" and type = "pod")
```

After applying it, open the metrics perspective for a pod in StackState (preferably a pod with some spikes and troughs in CPU usage). Enlarge the chart using the icon in its top-right corner to get a better view. Now you can also change the time window to see what the effects are from the different aggregations (30 minutes vs 24 hours for example).

{% hint style="info" %}
When the metric binding doesn't specify an aggregation StackState will automatically use the `last_over_time` aggregation to reduce the number of data points for a chart. See also [Why is this necessary?](#why) for an explanation.
{% endhint %}

![The chart for this metric binding for the last 30m, there are only a few lines in the chart visible because most time series are on top of each other](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c8099eeacac67e988b40d4a2e3200ac07aa340c5%2Fmetric-aggregation-differences-30m.png?alt=media) ![The same chart, same component and same end time, but now for the last 24h. It shows, sometimes completely, different results for the different aggregations](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-a20578bf1b5d300f2f11921d8a9aaf64ca1aa487%2Fmetric-aggregation-differences-24h.png?alt=media)

## Why is this necessary?

First of all, why should you use an aggregation? It doesn't make sense to retrieve more data points from the metric store than fit in the chart. Therefore StackState automatically determines the step needed between 2 data points to get a good result. For short time windows (for example a chart showing only 1 hour of data) this results in a small step (around 10 seconds). Metrics are often only collected every 30 seconds, so for 10 second steps the same value will repeat for 3 steps before changing to the next value. Zooming out to a 1 week time window, will require a much bigger step (around 1 hour, depending on the exact size of the chart on screen).

When the steps become larger than the resolution of the collected data points, a decision needs to be made on how to summarize the data points of the 1 hour time range into a single value. When an aggregation over time is already specified in the query, it will be used to do that. However, if no aggregation is specified, or when the aggregation interval is smaller than the step, the `last_over_time` aggregation is used, with the `step` size as the interval. The result is that only the last data point for each hour is used to "summarize" the all data points in that hour.

To summarize, when executing a PromQL query for a time range of 1 week with a step of 1 hour this query:

```
container_cpu_usage /1000000000
```

is automatically converted to:

```
last_over_time(container_cpu_usage[1h]) /1000000000
```

Try it for yourself on the [StackState playground](https://play.stackstate.com/#/metrics?promql=last_over_time%28container_cpu_usage%7Bnamespace%3D%22sock-shop%22%2C%20pod_name%3D~%22carts.%2A%22%7D%5B%24%7B__interval%7D%5D%29%20%2F%201000000000\&timeRange=LAST_7_DAYS).

![Last over time](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-25c33a5105eee48462b050b2a4f1e165982bcefa%2Fk8s-metric-queries-for-chart-last-over-time.png?alt=media) ![Max over time with fixed range](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-3005e8d973f404e160fee55cca49deb57b3d0ecc%2Fk8s-metric-queries-for-chart-max-over-time-fixed-range.png?alt=media) ![Max over time with automatic range](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-e9f63d22ee1eaae5b53c7e7a5eca7bd9bf3847c3%2Fk8s-metric-queries-for-chart-max-over-time-interval.png?alt=media)

Often this behavior isn't intended and it's better to decide for yourself what kind of aggregation is needed. Using different aggregation functions it's possible to emphasize certain behavior (at the cost of hiding other behavior). Is it more important to see peaks, troughs, a smooth chart etc.? Then use the `${__interval}` parameter for the range as it's automatically replaced with the `step` size used for the query. The result is that all the data points in the step are used.

![A fixed range, shorter than the data resolution](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-99ad03a9b763833e0b053b14ab7d6e08a627dd9a%2Fk8s-metric-queries-small-range.png?alt=media) ![Automatic range, based on step but with a lower limit](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-59439f844b8c86cc8bd91efb8d56b592f9e2e75a%2Fk8s-metric-queries-interval-for-range.png?alt=media)

The `${__interval}` parameter prevents another issue. When the `step` size and therefore the `${__interval}` value, would shrink to a smaller size than the resolution of the stored metric data this would result in gaps in the chart.

Therefore `${__interval}` will never shrink smaller than the 2\* the default scrape interval (default scrape interval is 30 seconds) of the StackState agent.

Finally the `rate()` function requires at least 2 data points to be in the interval to calculate a rate at all. With less than 2 data points the rate won't have a value. Therefore `${__rate_interval}` is guaranteed to always be at least 4 \* the scrape interval. This guarantees no unexpected gaps or other strange behavior in rate charts, unless data is missing.

There are some excellent blog posts on the internet that explain this in more detail:

* [Step and query range](https://www.robustperception.io/step-and-query_range/)
* [What range should I use with rate()?](https://www.robustperception.io/what-range-should-i-use-with-rate/)
* [Introduction of \_\_rate\_interval in Grafana](https://grafana.com/blog/2020/09/28/new-in-grafana-7.2-__rate_interval-for-prometheus-rate-queries-that-just-work/)

## See also

Some more resources on understanding PromQL queries:

* [Anatomy of a PromQL Query](https://promlabs.com/blog/2020/06/18/the-anatomy-of-a-promql-query/)
* [Selecting Data in PromQL](https://promlabs.com/blog/2020/07/02/selecting-data-in-promql/)
* [How to join multiple metrics](https://iximiuz.com/en/posts/prometheus-vector-matching/)
* [Aggregation over time](https://iximiuz.com/en/posts/prometheus-functions-agg-over-time/)


# Troubleshooting custom charts

StackState v6.0

## Overview

* [The metric chart doesn't show on the Highlights page of a component](#the-metric-chart-doesnt-show-on-the-highlights-page-of-a-component)
* [The metric chart doesn't show on the metrics perspective of a component](#the-metric-chart-doesnt-show-on-the-metrics-perspective-of-a-component)
* [The metric chart on a component remains empty ("no data")](#the-metric-chart-on-a-component-remains-empty-no-data)

## The metric chart doesn't show on the Highlights page of a component

At the moment it is not possible to customize the metric charts that are shown on a components Highlights page. The charts for custom metric bindings will be shown in the Metrics perspective only.

## The metric chart doesn't show on the metrics perspective of a component

The `scope` query on a metric binding is used to determine whether a component shows the metric binding. If a component doesn't show a metric binding check that the topology query in the scope matches the component.

First check that the component indeed has the expected labels and/or component type on the component highlights page, name and type are at the top, the labels are in the "About" section. Make sure there are no spelling mistakes in label names or values.

Check that the scope query has the correct syntax:

1. Open the explore view, via Views in the menu and the blue "Explore" button on the right. Or directly via the URL: `https://<your-stackstate-instance>/#/views/explore`
2. Open the filters and select `switch to STQL`
3. Now copy/paste the query from the scope into the STQL field and run the query

The overview now shows all components that match the query and that will get the chart.

## The metric chart on a component remains empty ("no data")

For the metric chart that has no data while data was expected open the inspector (the icon on the top-right corner of the chart). Toggle the "Show query" button to show the queries.

Make sure the query doesn't contain any of the parameters anymore (i.e. all values like `${tags.cluster-name}` or `${name}`) have been replaced with the values for the component. If some parameters were left behind in the query the labels were not available on this component. So cross-check the names used (in this example `cluster-name`) against the labels available on the component. Also make sure there are no typos in the names.

If all parameters are filled in there may be an issue with the PromQL query. To investigate that copy the PromQL query and open the Metrics explorer (via the main menu of StackState). Paste the query into the metric explorer and run it. This should still give an empty result.

Either the metric doesn't exist, it doesn't have one of the labels or the label does exist but there are no time series matching the value. The fastest method to resolve this is to rewrite the query to only its metric name and run that, if there are results the metric exists (so no typos). The table result can also be used to verify that all the labels that are used exist. Make sure there are no typos here either.

If there are results, but just not for a specific value of a label (for example for the `pod_name` label) the query is ok but there is no time series for this specific metric for this specific component. Things to check in this case:

* Is the data collected for this component (either via the StackState agent or some other means)?
* Is the component even reporting the metric?

How to do this depends on how data collection is configured.


# Advanced Metrics


# Grafana Datasource

Use StackState as a Grafana datasource

StackState can be used as a datasource for Grafana. This will allow to use Grafana as a visualization tool for your StackState data. This is useful if you already have some dashboards which you want to keep using. Because StackState exposes a Prometheus-compatible API, you can use the [Prometheus datasource](https://grafana.com/docs/grafana/latest/datasources/prometheus) in Grafana to connect to StackState. This also makes StackState usable with other Prometheus-compatible solutions.

## Prerequisites

Before you can add StackState as a datasource in Grafana, you need to setup a ServiceToken to authenticate with StackState. StackState recommends to create a dedicated role with permissions for this purpose.

You can do this via the StackState CLI:

```sh
> sts rbac create-subject --subject grafana
✅ Created subject 'grafana'
> sts rbac grant --subject grafana --permission read-metrics
✅ Granted permission 'read-metrics' on 'system' to subject 'grafana'
PERMISSION   | RESOURCE
read-metrics | system
```

This will create a new role in StackState called `grafana` and grant it the `read-metrics` permission. You can then create a ServiceToken for this role:

```sh
> sts service-token create --name grafana --roles grafana
✅ Service token created: svctok-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Learn more about [managing ServiceTokens](https://archivedocs.stackstate.com/security/k8s-service-tokens).

The returned ServiceToken can be used to authenticate with StackState. You can now add StackState as a datasource in Grafana.

## Create a new StackState datasource in Grafana

With the created ServiceToken, you can now add StackState as a datasource in Grafana. To do this, go to the Grafana UI and navigate to the datasource configuration page. Click on the `Add data source` button and select `Prometheus` from the list of datasources.

![Grafana new datasource](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c57861c57cc8b7349f4fe59222ddd54fbc392c46%2Fk8s-grafana-new-datasource.png?alt=media)

On the datasource configuration page, enter the following configuration details:

* **Name**: StackState
* **URL**: `https://<tenant-name>.app.stackstate.io/prometheus`
* **Custom HTTP Headers**
  * **Header**: `X-API-Key`
  * **Value**: `<service-token>`

![Grafana datasource configuration](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fff332231a7accb534fc950f830159fb4cdc39b2%2Fk8s-grafana-datasource.png?alt=media)

Click on the `Save & Test` button to save the datasource. If the configuration is correct, you should see a green `Data source is working` message.


# Prometheus remote\_write

StackState v6.0

When you have your own on-premise or self-hosted Prometheus running where metrics for your environment are aggregated, you can mirror these metrics in StackState. This will allow you to use StackState's powerful topology and correlation features to troubleshoot your Kubernetes environment without having to switch between tools.

To make this possible, StackState exposes the Prometheus `remote_write` protocol as an endpoint. Using this endpoint you can configure your Prometheus instance to send metrics to StackState. The metrics are then automatically ingested, and it will be possible to bind the metrics to the components observed by StackState. The following diagram shows how this works:

![Prometheus Remote Write](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-1c099f1d43f355c80723fb706bdb356ec40ac38e%2Fk8s-prometheus-remotewrite.png?alt=media)

## Prerequisites

To mirror your Prometheus metrics in StackState, you need to lookup the API Key that's used to send in metrics into StackState. The API Key can be found in the description of the installed Kubernetes StackPack in StackState. The following steps show how to find the API Key:

1. Open the StackState UI and navigate to the StackPacks page

   ![StackPacks](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-5a77a6e54ac0a3475c42cc7a820b12acd4178474%2Fk8s-stackpacks.png?alt=media)
2. Find the Kubernetes StackPack and click on it.
3. In the description of the StackPack, you will find the API Key that's used to send in metrics into StackState.

   ![API Key](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-f4f6c4a7f172fbcaefc69e93bfa6284ce379d0f6%2Fk8s-stackpacks-apikey.png?alt=media)

## Configuring your Prometheus instance

To configure your Prometheus instance to send metrics to StackState, you need to add a new remote write endpoint to your Prometheus configuration. This can be done by updating the `remote_write` section in your `prometheus.yml` file. There are 2 variants that you can use for the authentication to the endpoint, either through a header or through basic authentication.

### Header authentication

You can authenticate using the API Key by adding the `sts-api-key` header to the prometheus remote\_write requests. The following example shows how to configure this:

```yaml
remote_write:
- url: https://<tenant>.app.stackstate.io/receiver/prometheus/api/v1/write
  headers:
    sts-api-key: <API Key>
```

### Basic authentication

You can authenticate using basic authentication by adding the `basic_auth` section to the prometheus remote\_write requests. Because the requests to this API are made from a headless service, the username field is set to the static value `apikey`. The following example shows how to configure this:

```yaml
remote_write:
- url: https://<tenant>.app.stackstate.io/receiver/prometheus/api/v1/write
  basic_auth:
    username: apikey
    password: <API Key>
```

## Finishing up

After the configuration changes have been applied to the Prometheus configuration file, Prometheus needs to be restarted. After the restart, Prometheus will start sending metrics to StackState. The metrics will be automatically correlated with the rest of your environment and will be visible in the StackState UI.


# OpenMetrics

StackState v6.0

## Overview

StackState Agent V2 can be configured to retrieve metrics from an OpenMetrics endpoint and push these to StackState.

## Setup

### Installation

The OpenMetrics check is included in the \[Agent V2 StackPack].

### Configuration

To enable the OpenMetrics integration and begin collecting metrics data from an OpenMetrics endpoint, the OpenMetrics check must be configured on StackState Agent V2. The check configuration provides all details required for the Agent to connect to your OpenMetrics endpoint and retrieve the available metrics.

{% tabs %}
{% tab title="Kubernetes, OpenShift" %}

1. Deploy the Agent on your Kubernetes or OpenShift cluster.
2. Add the annotations below when launching a pod that exposes metrics via an OpenMetrics endpoint. Add the following:
   * **\<CONTAINER\_NAME>** - the name of the container that exposes the OpenMetrics. It's possible to process multiple endpoints in a single pod (that's why there is a list in the JSON).
   * **prometheus\_url** - the path (often just `metrics`) and port at which the OpenMetrics endpoint is exposed.
   * **namespace** - all metrics collected here will get this as a dot-separated prefix.
   * **metrics** - use `["*"]` to collect all available metrics. It's also possible to specify a list of metrics to be fetched. This should either be a string representing the metric name or a mapping to rename the metric`<EXPOSED_METRIC>:<SENT_METRIC>`

     ```yaml
     ...
     metadata:
       annotations:
         ad.stackstate.com/<CONTAINER_NAME>.check_names: '["openmetrics"]'
         ad.stackstate.com/<CONTAINER_NAME>.init_configs: '[{}]'
         ad.stackstate.com/<CONTAINER_NAME>.instances: |
           [ 
             {
               "prometheus_url": "http://%%host%%:<METRICS_PORT>/<METRICS_PATH>",
               "namespace": "<METRICS_NAMESPACE>", 
               "metrics": ["*"] 
             } 
           ]
     ...
     # This already exists in the pod spec, the container name needs to match the container that is exposing the openmetrics endpoint
     spec:
       containers:
        - name: <CONTAINER_NAME>
     ...
     ```
3. You can also add optional configuration and filters:
   * **prometheus\_metrics\_prefix** - prefix to add to exposed OpenMetrics metrics.
   * **health\_service\_check** - send a service check `<NAMESPACE>.prometheus.health` reporting the health of the OpenMetrics endpoint. Default `true`.
   * **label\_to\_hostname** - override the hostname with the value of one label.
   * **label\_joins** - target a metric and retrieve it's label via a 1:1 mapping
   * **labels\_mapper** - rename labels. Format is `<LABEL_TO_RENAME>: <NEW_LABEL_NAME>`.
   * **type\_overrides** - override a type in the OpenMetrics the payload or type an untyped metric (these would be ignored by default). Supported `<METRIC_TYPE>` are `gauge`, `count` and `rate`. Format is `<METRIC_NAME>: <METRIC_TYPE>`.
   * **tags** - list of tags to attach to every metric, event and service check emitted by this integration.
   * **send\_histograms\_buckets** - send the histograms bucket. Default `true`.
   * **send\_monotonic\_counter** - set to `true` to convert counters to a rate (note that two runs are required to produce the first result). Set to `false` to send counters as a monotonic counter. Default `true`.
   * **exclude\_labels** - list of labels to be excluded.
   * **prometheus\_timeout** - set a timeout for the OpenMetrics query.
   * **ssl\_cert** - If your OpenMetrics endpoint is secured, enter the path to the certificate and specify the private key in the `ssl_private_key` parameter, or give the path to a file containing both the certificate and the private key.
   * **ssl\_private\_key** - required if the certificate linked in `ssl_cert` doesn't include the private key. Note that the private key to your local certificate must be unencrypted.
   * **ssl\_ca\_cert** - the path to the trusted CA used for generating custom certificates.
   * **extra\_headers** - a list of additional HTTP headers to send in queries to the OpenMetrics endpoint. Can be combined with autodiscovery template variables. For example, `"Authorization: Bearer %%env_TOKEN%%"`.
4. Wait for the Agent to collect data from the OpenMetrics endpoint and send it to StackState.
   {% endtab %}
   {% endtabs %}

## Data collected

### Metrics

By default, all metrics are retrieved from the specified OpenMetrics endpoint. To optimize performance, a maximum of 2000 metrics will be retrieved. If the check is attempting to retrieve more than 2000 metrics, add a `metrics` filter to the [configuration](#configuration) to ensure that all important metrics can be retrieved within the limit.

Retrieved metrics won't automatically be mapped to topology elements but they can be browsed using the [telemetry inspector](https://archivedocs.stackstate.com/metrics/k8sts-explore-metrics) and eventually [added to components via a metric binding](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-add-charts).

### Events

The OpenMetrics integration doesn't retrieve any events data.

### Traces

The OpenMetrics integration doesn't retrieve trace data.


# Explore Logs

StackState v6.0

## Navigate to Logs

You can explore the container logs of any Kubernetes environment that is configured with log shipping through the StackState UI. This can be done by drilling down to `pod` level through any of the provided paradigms (Services, Deployments, Stateful Sets, Daemon Sets, etc.) from the Kubernetes menu on the left

![Kubernetes Paradigms Menu](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6a656a9b73bf6babe65af49fbbadc699e95de16e%2Fk8s-menu.png?alt=media)

For simplicity, and completeness, the example uses the `Pods` paradigm directly, and a pod was chosen that contains multiple containers, as to be able to distinguish between Pod logs and Container logs. The Pod view will have multiple log-related entry points.

## Viewing the Logs

![Kubernetes Pod View](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-bb5b741a3f82088c34e4d0739203e37a9d65e0f1%2Fk8s-pod-view-node-agent.png?alt=media)

To view all the logs associated with this Pod, click on either of the two options circled in red. To filter by log entry type (Errors, Warnings, Other), select one of the items circled in blue. The histogram displaying proportionality between the log entry types is circled in green.

### The Logs Drawer

The Logs Drawer facilitates a visually pleasing experience to navigating log files in a way that enhances the troubleshooting experience.

For simplicity, the example only deals with unfiltered selections (circled in red), which will display all log lines, of all containers, of any log entry type. Selecting either of the two options circled in red opens up the log drawer with no filtering applied:

![Kubernetes Log View No Filters](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-b3813f9be4c03d5a86123f2e67c6cee1ef45d007%2Fk8s-pod-view-log-drawer-no-filter.png?alt=media)

From this point onward, one could start to drill in closer to the problem by applying options to the provided filters (search string match, severity, container, log window interval). Several options are available for sorting and display preference directly below the histogram in the logs drawer.

* Search String Match will take an input search term and filter out any log line that does not contain it.
* Severity options are `Any`, `Error`, `Warning`, and `Other`. Selecting anything but `Any` will exclude all log lines that don't match the selection.
* Container options will include `Any`, and a list of containers in the Pod. Selecting anything but `Any` will restrict output to that produced by the selected container.
* Log Window Interval options will be a date-time picker interface that allows you to specify a `from` and `to` interval. Changing this from the default will exclude all log entries that fall outside the selected period.

As an example, all four can be seen in action below:

![Kubernetes Log View With Filters](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-e9ed6c4b9974ce6d0cb8b4ebb65df940777ed948%2Fk8s-pod-view-log-drawer-with-filters.png?alt=media)

The image above has the following filters applied:

* Search term: `wrong type in json response`
* Severity: `Warning`
* Container: `node-agent`
* Log Window Interval: Between `02:00am` and `03:00am` of the current day.


# Log Shipping

StackState v6.0

## Agent Installation

### Openshift

Third-party log shippers are not readily supported on Openshift, the platform has options for log forwarding, which is used instead of the promtail configuration included in the StackState helm chart. For detailed instructions on how to configure this, refer to the Kubernetes stackpack documentation on your running StackState instance.

### Kubernetes

The StackState k8s Agent helm chart default configuration sets log shipping as enabled via the helm values supplied with the chart:

```yaml
logsAgent:
  # logsAgent.enabled -- Enable / disable k8s pod log collection
  enabled: true
```

The above will ensure that a promtail container is deployed to each node to collect logs and send it to StackState. For deployments where it is not desirable to ship logs to StackState, set the above value to `false`.

### Running Additional Promtail Pods

StackState uses a tuned configuration for log ingestion, and this is usually not in line with auxiliary requirements. It is therefore not possible to run a separate configuration for log ingestion to other destination endpoints, it is instead recommended to run a second promtail pod that deals with these requirements as a separate concern to the promtail that is deployed by the agent helm chart.


# Explore Traces

StackState v6.0

## Viewing Traces

![Pod Menu Traces](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-391c4c95444471ea7f57379f1a09cba5403335fb%2Fk8s-pod-view-menu.png?alt=media)

To view the traces associated with the pod, service, deployment, statefulset or daemonset, click on the "Traces" menu item. This will take you to the [Traces Perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-traces-perspective)


# Health synchronization

StackState v6.0

This section describes the advanced topic of synchronizing custom health data from different monitoring systems to StackState. This topic is mostly interesting for engineers who want to make a custom integration with an existing monitoring system. For out of the box monitors you can look [here](https://archivedocs.stackstate.com/monitors-and-alerts/kubernetes-monitors).

## Overview

Health synchronization adds existing health checks from external monitoring systems to StackState topology elements. Health data is calculated in the external monitoring system using its own data and rules, then automatically synchronized and attached to the associated topology elements in StackState.

## Set up health synchronization

The StackState Receiver API will automatically receive and process all incoming health data. StackState doesn't require additional configuration to enable health synchronization, however, the health data received should match the expected JSON format.

Details on how to ingest health data can be found on the following pages:

* [Ingest health data through the StackState Receiver API](https://archivedocs.stackstate.com/health/send-health-data/send-health-data)

## Health synchronization pipeline

The health synchronization framework works as follows:

* Health data is sent to StackState and ingested via the Receiver API.
* StackState topology elements related to the ingested health checks are identified and bound based on:
  * the topology identifiers obtained during topology synchronization.
  * the `topologyElementIdentifier` from the ingested [health payload](https://archivedocs.stackstate.com/send-health-data/send-health-data#json-health-payload).
* StackState keeps track of changes to both topology elements and health checks to maintain up-to-date information.

![Health synchronization pipeline](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-1427da0d7e0994e2d0b0866930c6fc0e47e6c78a%2Fhealth-sync-pipeline.svg?alt=media)

### Consistency models

StackState health synchronization relies on different consistency models to guarantee that the data sent from an external monitoring system matches with what StackState ingests and shows. The consistency model is specified in the `"health"` property of the [common JSON object](https://archivedocs.stackstate.com/send-health-data/send-health-data#common-json-object) or as an argument in the StackState CLI when health data is sent to StackState. The supported models are: `REPEAT_SNAPSHOTS`, `REPEAT_STATES` and `TRANSACTIONAL_INCREMENTS`.

{% tabs %}
{% tab title="Repeat snapshots model" %}
The `REPEAT_SNAPSHOTS` consistency model works with periodic, full snapshots of all checks in an external monitoring system. StackState keeps track of the checks in each received snapshot and decides if associated external check states need to be created, updated or deleted in StackState. For example, if a check state is no longer present in a snapshot. This model offers full control over which external checks will be deleted as all decisions are inferred from the received snapshots. There is no ambiguity over the external checks that will be present in StackState.

**Use this model when:** The external monitoring system is capable of keeping the state of which elements are present in a determined time window and therefore can communicate how the full snapshot looks like.

**JSON payload:** The [Repeat Snapshots health payload](https://archivedocs.stackstate.com/health/send-health-data/repeat_snapshots) accepts specific properties to specify when a snapshot starts or stops.
{% endtab %}

{% tab title="Repeat States model" %}
The `REPEAT_STATES` consistency model works with periodic checks received from an external monitoring system. StackState keeps track of the checks and decides if associated external checks need to be created or updated in StackState. A configurable expiry mechanism is used to delete external checks that aren't observed anymore. This model offers less control over data than the `REPEAT_SNAPSHOTS` model. As an expiry configuration is used to delete external checks, it might happen that elements are deleted due to barely missing the expiry timeout. This would reflect as external checks disappearing and reappearing in StackState.

**Use this model when:** The external monitoring system isn't capable of collecting all checks in a determined time window. The best effort is just to send the external checks as they're obtained.

**JSON payload:** The [Repeat States health payload](https://archivedocs.stackstate.com/health/send-health-data/repeat_states) accepts specific properties to specify the expiry configuration.
{% endtab %}

{% tab title="Transactional Increments model" %}
The `TRANSACTIONAL_INCREMENTS` consistency model is designed to be used on streaming systems where only incremental changes are communicated to StackState. As there is no repetition of data, data consistency is upheld by ensuring that at-least-once delivery is guaranteed across the entire pipeline. To detect whether any data is missing, StackState requires that both a checkpoint and the previous checkpoint are communicated together with the `check_states`. This model requires strict control across the whole pipeline to guarantee no data loss.

**Use this model when:** The external monitoring system doesn't have access to the total external checks state, but only works on an event based approach.

**JSON payload:** The metadata `repeat_interval` and `expire_interval` aren't relevant for the [Transactional Increments health payload](https://archivedocs.stackstate.com/health/send-health-data/transactional_increments) as there is no predefined periodicity on the data.
{% endtab %}
{% endtabs %}

### Health stream and substream

External monitoring systems send health data to the StackState Receiver in a health stream. Each health stream has at least one substream with health checks.

#### Health stream

The Health stream uniquely identifies the health synchronization and defines the boundaries within which the health check states should be processed together.

#### Substream

Sub streams contain the health check data that are processed by StackState. When working with health data from a distributed external monitoring system, multiple sub streams can be configured, each containing health snapshots from a single location. The data in each substream is semi-independent, but contributes to the health check states of the complete health stream. If a single location is responsible for reporting the health check states of the health stream, you can omit the `sub_stream_id` from the [health payload](https://archivedocs.stackstate.com/send-health-data/send-health-data#json-health-payload). StackState will assume that all the external health checks belong to a single, default substream.

### Repeat Interval

Health synchronization processes the ingested health data per substream. The repeat interval specified in the [health payload](https://archivedocs.stackstate.com/send-health-data/send-health-data#json-health-payload) is the commitment from the external monitoring system to send complete snapshots over and over to keep the data up to date on StackState. This is helpful for StackState to be able to inform the user how up to date the health synchronization is running.

### Expire Interval

The expire interval can be used to configure sub streams in the health synchronization to delete data that isn't sent by the external system anymore. This is helpful in case the source for a substream could be decommissioned and StackState would not hear from it again. Without an expire interval, the previously synchronized data would be left permanently hanging.

### Check State

The health check state is calculated by an external monitoring system and includes all information required to attach it to a topology element. In order to be able to materialize and attach it to a component it requires to attribute the health state to a particular monitor in this case an [ExternalMonitor](#external-monitor).

Once attached to a topology element, the health check state contributes to the element's own health state.

### External Monitor

An external monitor allows to attach the health states to components and to show a remediationHint on the StackState highlight pages. This resource needs to be created via the [StackState CLI](https://archivedocs.stackstate.com/cli/k8sts-cli-sts) or as part of a stackpack. Here is an example of an externa monitor:

```
    {
      "_type": "ExternalMonitor",
      "healthStreamUrn": "urn:health:kubernetes:external-health",
      "description": "Monitored by external tool.",
      "identifier": "urn:custom:external-monitor:heartbeat",
      "name": "External Monitor Heartbeat",
      "remediationHint": "",
      "tags": [
        "heartbeat"
      ]
    }
```

Every `ExternalMonitor` payload has the following details:

* `_type`: StackState needs to know this is a monitor so, value always needs to be `ExternalMonitor`
* `healthStreamUrn`: This field needs to match the `urn` that is sent as part of the [Health Payload](https://archivedocs.stackstate.com/send-health-data/repeat_snapshots#json-property-health).
* `description`: A description of the external monitor.
* `identifier`: An identifier of the form `urn:custom:external-monitor:....` which uniquely identifies the external monitor when updating its configuration.
* `name`: The name of the external monitor
* `remediationHint`: A description of what the user can do when the monitor fails. The format is markdown.
* `tags`: Add tags to the monitor to help organize them in the monitors overview of your StackState instance, <http://your-StackState-instance/#/monitors>

Here is an example of how to create an `External Monitor` using the [StackState CLI](https://archivedocs.stackstate.com/cli/k8sts-cli-sts)

* Create a new YAML file called `externalMonitor.yaml` and add this YAML template to it to create your own external monitor.

```
nodes:
- _type: ExternalMonitor
  healthStreamUrn: urn:health:sourceId:streamId
  description: Monitored by external tool.
  identifier: urn:custom:external-monitor:heartbeat
  name: External Monitor Heartbeat
  remediationHint: |-
    To remedy this issue with the deployment {{ labels.deployment }}, consider taking the following steps:
    
    1. Look at the logs of the pods created by the deployment
  tags:
    - heartbeat
```

* Use the cli to create the external monitor

```bash
sts settings apply -f externalMonitor.yaml 
✅ Applied 1 setting node(s).                                                                                                                                                                                                               

TYPE            | ID              | IDENTIFIER                            | NAME                      
ExternalMonitor | 150031117290020 | urn:custom:external-monitor:heartbeat | External Monitor Heartbeat
```

## See also

* [JSON health payload](https://archivedocs.stackstate.com/send-health-data/send-health-data#json-health-payload)


# Send health data over HTTP

StackState v6.0


# Send health data

StackState

## Overview

StackState can synchronize health information from your own data sources either via HTTP or the [StackState CLI](https://archivedocs.stackstate.com/cli/k8sts-cli-sts).

## StackState Receiver API

The StackState Receiver API accepts topology, metrics, events and health data in a common JSON object. The default location for the receiver API is the `<STACKSTATE_RECEIVER_API_ADDRESS>`, constructed using the `<STACKSTATE_BASE_URL>` and <`STACKSTATE_RECEIVER_API_KEY>`.

{% tabs %}
{% tab title="Kubernetes" %}
The `<STACKSTATE_RECEIVER_API_ADDRESS>` for StackState deployed on Kubernetes or OpenShift is:

```
https://<STACKSTATE_BASE_URL>/receiver/stsAgent/intake?api_key=<STACKSTATE_RECEIVER_API_KEY>
```

The `<STACKSTATE_BASE_URL>` and `<STACKSTATE_RECEIVER_API_KEY>` are set during StackState installation, for details see [Kubernetes install - configuration parameters](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/kubernetes_install#generate-values-yaml).
{% endtab %}

{% tab title="Linux" %}
The `<STACKSTATE_RECEIVER_API_ADDRESS>` for StackState deployed on Linux is:

```
https://<STACKSTATE_BASE_URL>:<STACKSTATE_RECEIVER_PORT>/stsAgent/intake?api_key=<STACKSTATE_RECEIVER_API_KEY>
```

The `<STACKSTATE_BASE_URL>` and `<STACKSTATE_RECEIVER_API_KEY>` are set during StackState installation, for details see [Linux install - configuration parameters](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/install-stackstate/linux/install_stackstate.md#configuration-options-required-during-install).
{% endtab %}
{% endtabs %}

## JSON

### Common JSON object

Topology, telemetry and health data are sent to the receiver API via HTTP POST. There is a common JSON object used for all messages.

```javascript
{
  "collection_timestamp": 1548855554, // the epoch timestamp for the collection
  "events": {}, // used to send events data
  "internalHostname": "localdocker.test", // the host sending this data
  "metrics": [], // used to send metrics data
  "service_checks": [],
  "topologies": [], // used to send topology data
  "health": // used for sending health data
}
```

### JSON health payload

StackState accepts health data based on a chosen [consistency model](https://archivedocs.stackstate.com/health-synchronization#consistency-models). The message that can be sent for each model are described on the pages below:

* [Repeat Snapshots JSON](https://archivedocs.stackstate.com/health/send-health-data/repeat_snapshots)
* [Repeat States JSON](https://archivedocs.stackstate.com/health/send-health-data/repeat_states)
* [Transactional Increments JSON](https://archivedocs.stackstate.com/health/send-health-data/transactional_increments)

## See also

* [Install the StackState CLI](https://archivedocs.stackstate.com/cli/k8sts-cli-sts)


# Repeat Snapshots JSON

StackState v6.0

### Overview

This page describes the exact JSON messages that can be sent for the health synchronization Repeat Snapshots consistency model.

### JSON property: "health"

Health can be sent to the StackState Receiver API using the `"health"` property of the [common JSON object](https://archivedocs.stackstate.com/health/send-health-data#common-json-object).

{% tabs %}
{% tab title="Example health `repeat_snapshots` JSON" %}

```javascript
{
   "apiKey":"<STACKSTATE_RECEIVER_API_KEY>",
   "collection_timestamp":1585818978,
   "internalHostname":"lnx-343242.srv.stackstate.com",
   "health":[
      {
        "consistency_model": "REPEAT_SNAPSHOTS",
        "start_snapshot": {
          "repeat_interval_s": 50
          //"expiry_interval_s": 200 Optional
        },
        "stop_snapshot": {},
        "stream": {
          "urn": "urn:health:sourceId:streamId"
          //"sub_stream_id": "subStreamId" Optional
        },
        "check_states": [
          {
            "checkStateId": "checkStateId1",
            "message": "Server Running out of disk space",
            "health": "Deviating",
            "topologyElementIdentifier": "server-1",
            "name": "Disk Usage"
          },
          {
            "checkStateId": "checkStateId2",
            "message": "Provisioning failed. [Learn more](https://www.any-link.com)",
            "health": "critical",
            "topologyElementIdentifier": "server-2",
            "name": "Health monitor"
          }
        ]
      }
   ]
}
```

{% endtab %}
{% endtabs %}

Every health Repeat Snapshots data payload has the following details:

* **start\_snapshot** - Optional. A start of a snapshot needs to be processed before processing `check_states`. This enables StackState to diff a stream snapshot with the previously received one and delete check states that are no longer present in the snapshot. It carries the following fields as snapshot metadata:
  * **repeat\_interval\_s** - Time in seconds. The frequency with which the external source will send health data to StackState. Max allowed value is 1800 (30 minutes).
  * **expiry\_interval\_s** - Time in seconds. The time to wait after the last update before an external check is deleted by StackState. Required when using sub streams.
* **stop\_snapshot** - Optional. An end of a snapshot will be processed after processing the`check_states`.
* **stream** - Object providing identification regarding which snapshots and `check_states` belong together. It has the following fields:
  * **urn** - Data source and stream ID encoded as a StackState [URN](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/configure/topology/identifiers.md) that matches the following convention: `urn:health:<sourceId>:<streamId>` where `<sourceId>` is the name if the external data source and `<streamId>` is a unique identifier for the health data stream.
  * **sub\_stream\_id** - Optional. Identifier for a subset of the stream health data. When the stream data is distributed and reported by several Agents, this allows snapshot lifecycles per `sub_stream_id`
* **check\_states** - A list of check states. Each check state can have the following fields:
  * **checkStateId** - Identifier for the check state in the external system
  * **message** - Optional. Message to display in StackState UI. Data will be interpreted as markdown allowing to have links to the external system check that generated the external check state.
  * **health** - One of the following StackState Health state values: `Clear`, `Deviating`, `Critical`.
  * **topologyElementIdentifier** - Used to bind the check state to a StackState topology element.
  * **name** - Name of the external check state.

### Send health to StackState

Health can be sent in one JSON message via HTTP POST or using the `stac` CLI command `stac health send`. In the example below, a snapshot containing two check states is sent to StackState from a single external monitoring system.

{% tabs %}
{% tab title="curl" %}

```bash
curl -X POST \
 '<STACKSTATE_RECEIVER_API_ADDRESS>' \
 -H 'Content-Type: application/json' \
 -d '{
  "collection_timestamp": 1548857167,
  "internalHostname": "local.test",
  "health": [
    {
      "consistency_model": "REPEAT_SNAPSHOTS",
      "start_snapshot": {
        "repeat_interval_s": 300
      },
      "stop_snapshot": {},
      "stream": {
        "urn": "urn:health:sourceId:streamId"
      },
      "check_states": [
        {
          "checkStateId": "checkStateId1",
          "message": "Server Running out of disk space",
          "health": "Deviating",
          "topologyElementIdentifier": "server-1",
          "name": "Disk Usage"
        },
        {
          "checkStateId": "checkStateId2",
          "message": "Provisioning failed. [Learn more](https://www.any-link.com)",
          "health": "critical",
          "topologyElementIdentifier": "server-2",
          "name": "Health monitor"
        }
      ]
    }
  ]
}'
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```
stac health send start urn:health:sourceId:streamId \
  --repeat-interval-seconds 300

stac health send check-state urn:health:sourceId:streamId \
  checkStateId1 "Disk Usage" "server-1" deviating \
  --message "Deviating Server Running out of disk space" --consistency-model="REPEAT_SNAPSHOTS"

stac health send check-state urn:health:sourceId:streamId \
  checkStateId2 "Health monitor" "server-2" critical \
  --message "Provisioning failed. [Learn more](https://www.any-link.com)" --consistency-model="REPEAT_SNAPSHOTS"

stac health send stop urn:health:sourceId:streamId
```

{% endtab %}

{% tab title="CLI: sts" %}
The new `sts` CLI doesn't support sending health states. This will only be supported by directly reaching out to the receiver API.
{% endtab %}
{% endtabs %}


# Repeat States JSON

StackState v6.0

### Overview

This page describes the exact JSON messages that can be sent for the health synchronization Repeat States consistency model.

### JSON property: "health"

Health can be sent to the StackState Receiver API using the `"health"` property of the [common JSON object](https://archivedocs.stackstate.com/health/send-health-data#common-json-object).

{% tabs %}
{% tab title="Example health `repeat_states` JSON" %}

```javascript
   "apiKey":"<STACKSTATE_RECEIVER_API_KEY>",
   "collection_timestamp":1585818978,
   "internalHostname":"lnx-343242.srv.stackstate.com",
   "events":{},
   "metrics":[],
   "service_checks":[],
   "health":[
      {
        "consistency_model": "REPEAT_STATES",
        "expiry": {
          "repeat_interval_s": 50,
          "expiry_interval_s": 100
        },
        "stream": {
          "urn": "urn:health:sourceId:streamId"
          //"sub_stream_id": "subStreamId" Optional
        },
        "check_states": [
          {
            "checkStateId": "checkStateId1",
            "message": "Server Running out of disk space",
            "health": "Deviating",
            "topologyElementIdentifier": "server-1",
            "name": "Disk Usage"
          },
          {
            "checkStateId": "checkStateId2",
            "message": "Provisioning failed. [Learn more](https://www.any-link.com)",
            "health": "critical",
            "topologyElementIdentifier": "server-2",
            "name": "Health monitor"
          }
        ]
      }
   ],
   "topologies":[]
```

{% endtab %}
{% endtabs %}

Every health Repeat States data payload has the following details:

* **expiry** - Optional. An expiry update needs to be processed before processing `check_states`. This enables StackState to track how long the external checks should be present in the system if they aren't sent again. It carries the following fields as expiry metadata:
  * **repeat\_interval\_s** - Time in seconds. The frequency with which the external source will send health data to StackState. Max allowed value is 1800 (30 minutes).
  * **expiry\_interval\_s** - Time in seconds. The time to wait after the last update before an external check is deleted by StackState if the external check isn't observed again.
* **stream** - Object providing identification regarding which snapshots and `check_states` belong together. It has the following fields:
  * **urn** - Data source and stream ID encoded as a StackState [URN](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/configure/topology/identifiers.md) that matches the following convention: `urn:health:<sourceId>:<streamId>` where `<sourceId>` is the name if the external data source and `<streamId>` is a unique identifier for the health data stream.
  * **sub\_stream\_id** - Optional. Identifier for a subset of the stream health data. When the stream data is distributed and reported by several agents, this allows snapshot lifecycles per `sub_stream_id`
* **check\_states** - A list of check states. Each check state can have the following fields:
  * **checkStateId** - Identifier for the check state in the external system
  * **message** - Optional. Message to display in StackState UI. Data will be interpreted as markdown allowing to have links to the external system check that generated the external check state.
  * **health** - One of the following StackState Health state values: `Clear`, `Deviating`, `Critical`.
  * **topologyElementIdentifier** - Used to bind the check state to a StackState topology element.
  * **name** - Name of the external check state.

### Send health to StackState

Health can be sent in one JSON message via HTTP POST or using the `stac` CLI command `stac health send`. In the example below, a snapshot containing two check states is sent to StackState from a single external monitoring system.

{% tabs %}
{% tab title="curl" %}

```bash
curl -X POST \
 '<STACKSTATE_RECEIVER_API_ADDRESS>' \
 -H 'Content-Type: application/json' \
 -d '{
  "collection_timestamp": 1548857167,
  "internalHostname": "local.test",
  "health": [
    {
      "consistency_model": "REPEAT_STATES",
      "expiry": {
        "repeat_interval_s": 300,
        "expiry_interval_s": 600
      },
      "stream": {
        "urn": "urn:health:sourceId:streamId"
      },
      "check_states": [
        {
          "checkStateId": "checkStateId1",
          "message": "Server Running out of disk space",
          "health": "Deviating",
          "topologyElementIdentifier": "server-1",
          "name": "Disk Usage"
        },
        {
          "checkStateId": "checkStateId2",
          "message": "Provisioning failed. [Learn more](https://www.any-link.com)",
          "health": "critical",
          "topologyElementIdentifier": "server-2",
          "name": "Health monitor"
        }
      ]
    }
  ]
}'
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```
stac health send expiry urn:health:sourceId:streamId \
  --repeat-interval-seconds 300 \
  --expiry-interval-seconds 600

stac health send check-state urn:health:sourceId:streamId \
  checkStateId1 "Disk Usage" "server-1" deviating \
  --message "Deviating Server Running out of disk space" \
  --consistency-model="REPEAT_STATES"

stac health send check-state urn:health:sourceId:streamId \
  checkStateId2 "Health monitor" "server-2" critical \
  --message "Provisioning failed. [Learn more](https://www.any-link.com)" \
  --consistency-model="REPEAT_STATES"
```

{% endtab %}

{% tab title="CLI: sts" %}
The new `sts` CLI doesn't support sending health states. This is only supported by directly calling out to the receiver API.
{% endtab %}
{% endtabs %}


# Transactional Increments JSON

StackState v6.0

### Overview

This page describes the exact JSON messages that can be sent for the health synchronization Transactional Increments consistency model.

### JSON property: "health"

Health can be sent to the StackState Receiver API using the `"health"` property of the [common JSON object](https://archivedocs.stackstate.com/health/send-health-data#common-json-object).

{% tabs %}
{% tab title="Example health `transactional_increments` JSON" %}

```javascript
   "apiKey":"your api key",
   "collection_timestamp":1585818978,
   "internalHostname":"lnx-343242.srv.stackstate.com",
   "events":{},
   "metrics":[],
   "service_checks":[],
   "health":[
      {
        "consistency_model": "TRANSACTIONAL_INCREMENTS",
        "increment": {
              "checkpoint": {
                  "offset": 5,
                  "batch_index": 102
              },
              "previous_checkpoint": {
                  "offset": 5,
                  "batch_index": 100
              }
        },
        "stream": {
          "urn": "urn:health:sourceId:streamId"
          //"sub_stream_id": "subStreamId" Optional
        },
        "check_states": [
          {
            "checkStateId": "checkStateId1",
            "message": "Server Running out of disk space",
            "health": "Deviating",
            "topologyElementIdentifier": "server-1",
            "name": "Disk Usage"
          },
          {
            "checkStateId": "checkStateId2",
            "message": "Provisioning failed. [Learn more](https://www.any-link.com)",
            "health": "critical",
            "topologyElementIdentifier": "server-2",
            "name": "Health monitor"
          },
          {
            "checkStateId": "checkStateId3",
            "delete": true
          }
        ]
      }
   ],
   "topologies":[]
```

{% endtab %}
{% endtabs %}

Every health Transactional Increments data payload has the following details:

* **increment** - An increment objects needs to be present on every message. This enables StackState to track the complete chain of messages and be able to detect when a retransmission of data, or an unexpected gap in the data is occurring. It carries the following fields as increment metadata:
  * **checkpoint** - Object providing the checkpoint that belongs the `check_states` present in the message, it has two fields:
    * **offset** - The offset asigned to the messages by the streaming pipeline. For example, Kafka offset.
    * **batch\_index** - Optional. When using a single message to accumulate several `check_states` the batch index represents the latest index that's present in the message, allowing to send big batches in separate api calls.
  * **previous\_checkpoint** - Optional. Represents the previously communicated checkpoint, can be empty on the very first transmission on the substream. It allows StackState to keep track if there could be any data missing from upstream.
* **stream** - Object providing identification regarding which snapshots and `check_states` belong together. It has the following fields:
  * **urn** - Data source and stream ID encoded as a StackState [URN](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/configure/topology/identifiers.md) that matches the following convention: `urn:health:<sourceId>:<streamId>` where `<sourceId>` is the name if the external data source and `<streamId>` is a unique identifier for the health data stream.
  * **sub\_stream\_id** - Optional. Identifier for a subset of the stream health data. When the stream data is distributed and reported by several agents, this allows snapshot lifecycles per `sub_stream_id`
* **check\_states** - A list of check states. Each check state can have the following fields:
  * **checkStateId** - Identifier for the check state in the external system
  * **message** - Optional. Message to display in StackState UI. Data will be interpreted as markdown allowing to have links to the external system check that generated the external check state.
  * **health** - One of the following StackState Health state values: `Clear`, `Deviating`, `Critical`.
  * **topologyElementIdentifier** - Used to bind the check state to a StackState topology element.
  * **name** - Name of the external check state.
  * **delete** - Flag that's interpreted as a delete request for the related `checkStateId`. Even if the rest of the fields for the create are present, for example, `name, health, ...` the delete will take precedence.

### Send health to StackState

Health can be sent in one JSON message via HTTP POST. In the example below, a snapshot containing two check states is sent to StackState from a single external monitoring system.

{% tabs %}
{% tab title="curl" %}

```bash
curl -X POST \
 '<STACKSTATE_RECEIVER_API_ADDRESS>' \
 -H 'Content-Type: application/json' \
 -d '{
  "collection_timestamp": 1548857167,
  "internalHostname": "local.test",
  "health": [
    {
      "consistency_model": "TRANSACTIONAL_INCREMENTS",
      "increment": {
            "checkpoint": {
                "offset": 5,
                "batch_index": 102
            },
            "previous_checkpoint": {
                "offset": 5,
                "batch_index": 100
            }
      },
      "stream": {
        "urn": "urn:health:sourceId:streamId"
      },
      "check_states": [
        {
          "checkStateId": "checkStateId1",
          "message": "Server Running out of disk space",
          "health": "Deviating",
          "topologyElementIdentifier": "server-1",
          "name": "Disk Usage"
        },
        {
          "checkStateId": "checkStateId2",
          "message": "Provisioning failed. [Learn more](https://www.any-link.com)",
          "health": "critical",
          "topologyElementIdentifier": "server-2",
          "name": "Health monitor"
        },
        {
          "checkStateId": "checkStateId3",
          "delete": true
        }
      ]
    }
  ]
}'
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

Sending of Transactional increments check\_states isn't available in the CLI, but all the debugging and introspection features can still be used.
{% endtab %}

{% tab title="CLI: sts" %}
Sending of Transactional increments check\_states isn't available in the `sts` CLI.
{% endtab %}
{% endtabs %}


# Debug health synchronization

StackState v6.0

## Overview

The [StackState CLI](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/README.md) can be used to troubleshoot a health synchronization and fix issues that might prevent health data from being correctly ingested and displayed in StackState. This page describes the general troubleshooting steps to take when debugging a health synchronization, as well as the CLI commands used, and a description of the error messages returned.

## General troubleshooting steps

When debugging the health synchronization there are some common verification steps that can be made no matter what the specific issue is:

1. [Verify that the stream exists](#list-streams).
2. If you are using sub streams, [verify that the substream exists](#list-sub-streams). The response will also show the number of check states on the substream. This lets you know if the data is being ingested and processed.
3. Investigate further:
   * **Stream present** - [Check the stream status](#show-stream-status), this will show the metrics latency of the stream and any [errors](#error-messages).
   * **Streams / sub streams present, but there are no check states** - Confirm that the payload sent to the Receiver API adheres to the [health payload specification](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/configure/health/send-health-data.md).
   * **No streams / sub streams are present** - Use the CLI command below to verify that health data sent to the Receiver API is arriving in StackState:

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts topic describe --name sts_health_sync
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
$ stac topic show sts_health_sync
```

{% endtab %}
{% endtabs %}

## Common issues

### Check state not visible on the component

There can be two reasons for a check state not to show on a component in StackState:

* The health check state hasn't been created. Follow the [general troubleshooting steps](#general-troubleshooting-steps) to confirm that the stream / substream has been created and that data is arriving in StackState.
* The health check state was created, but its `topologyElementIdentifier` doesn't match any `identifiers` from the StackState topology. Use the CLI command [show substream status](#show-substream-status) to verify if there are any `Check states with identifier which has no matching topology element`.

### Check state slow to update in StackState

The main reason for this is that the latency of the health synchronization is higher than expected. Use the CLI command [show stream status](#show-stream-status) to confirm the latency of the stream as well as the throughput of messages and specific check operations. It may be necessary to tweak the data sent to the health synchronization, or the frequency with which data is sent.

## Useful CLI commands

### List streams

Returns a list of all current synchronized health streams and the number of sub streams included in each.

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts health list
STREAM URN                                              | STREAM CONSISTENCY MODEL | SUB STREAM COUNT
urn:health:sourceId:streamId                            | REPEAT_SNAPSHOTS         | 1
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
# List streams
$ stac health list-streams

stream urn                                            substream count
--------------------------------------------------  ------------------
urn:health:sourceId:streamId                                         1
```

{% endtab %}
{% endtabs %}

### List sub streams

Returns a list of all sub streams for a given stream URN, together with the number of check states in each.

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts health list -u urn:health:sourceId:streamId
SUB STREAM ID  | CHECK STATE COUNT
subStreamId1   | 1
subStreamId2   | 1
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
# List sub streams
$ stac health list-sub-streams urn:health:sourceId:streamId

substream id                     check state count
------------------------------  -------------------
subStreamId1                                     20
subStreamId2                                     17
```

{% endtab %}
{% endtabs %}

### Show stream status

The stream status command returns the aggregated stream latency and throughput metrics. This is helpful when debugging why a health check takes a long time to land on the expected topology elements. It will help diagnose if the frequency of data sent to StackState should be adjusted. The output includes a section `Errors for non-existing sub streams:` as some errors are only relevant when a substream couldn't be created, for example `StreamMissingSubStream`. Substream errors can be any of the documented [error messages](#error-messages).

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts health status -u urn:health:sourceId:streamId
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
# Show a stream status
$ stac health show urn:health:sourceId:streamId

Aggregate metrics for the stream and all substreams:

metric                             value between now and 300 seconds ago    value between 300 and 600 seconds ago    value between 600 and 900 seconds ago
---------------------------------  ---------------------------------------  ---------------------------------------  ---------------------------------------
latency (Seconds)                  1.102                                    1.102                                    -
messages processed (per second)    0.256                                    0.16                                     -
check states created (per second)  0.10555555555555556                      0.10666666666666667                      -
check states updated (per second)  -                                        -                                        -
check states deleted (per second)  -                                        -                                        -

Errors for non-existing sub streams:

error message                                                                                   error occurrence count
----------------------------------------------------------------------------------------------  ------------------------
Substream `substream with ID `subStreamId2`` not started when receiving snapshot stop                          6
```

{% endtab %}
{% endtabs %}

### Show substream status

The substream status provides useful information to verify that StackState could bind check states sent from an external system to existing topology elements. This information is helpful to debug why a specific check isn't visible on the expected topology element.

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts health status -u urn:health:sourceId:streamId -sub-stream-urn subStreamId3
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
# Show a substream status.
$ stac health show urn:health:sourceId:streamId -s "subStreamId3"

Synchronized check state count: 32
Repeat interval (Seconds): 120
Expiry (Seconds): 240

Synchronization errors:

code    level    message    occurrence count
------  -------  ---------  ------------------

Synchronization metrics:

metric                             value between now and 300 seconds ago    value between 300 and 600 seconds ago    value between 600 and 900 seconds ago
---------------------------------  ---------------------------------------  ---------------------------------------  ---------------------------------------
latency (Seconds)                  0.23                                     0.125                                    0.265
messages processed (per second)    0.256                                    0.2773333333333333                       0.256
check states created (per second)  -                                        -                                        -
check states updated (per second)  -                                        -                                        -
check states deleted (per second)  -
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
A substream status will show the metadata related to the consistency model:

* **Repeat Snapshots** - Show repeat interval and expiry
* **Repeat States** - Show repeat interval and expiry
* **Transactional Increments** - Show checkpoint offset and checkpoint batch index
  {% endhint %}

The substream status can be expanded to include details of matched and unmatched check states using the `-t` command line argument. This is helpful to identify any health states that aren't attached to a topology element. In the example below, `checkStateId2` is listed under `Check states with identifier which has no matching topology element`. This means that it was not possible to match the check state to a topology element with the identifier `server-2`.

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts health status -u urn:health:sourceId:streamId -sub-stream-urn subStreamId3 -t
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
# Show a substream status matched/unmatched check states.
$ stac health show urn:health:sourceId:streamId -s "subStreamId3" -t
# If we configured our stream to not use explicit substreams then a default
# substream can be reached by omitting the optional substreamId parameter as in:
$ stac health show urn:health:sourceId:streamId -t

Check states with identifier matching exactly 1 topology element: 32

Check states with identifier which has no matching topology element:

check state id    topology element identifier
----------------  -----------------------------
checkStateId2     server-2

Check states with identifier which has multiple matching topology elements:

check state id    topology element identifier    number of matched topology elements
----------------  -----------------------------  -------------------------------------
```

{% endtab %}
{% endtabs %}

### Delete a health stream

The `delete` stream functionality is helpful while setting up a health synchronization in StackState. You can use it to experiment, delete the data and start over again clean. You can also delete a stream and drop its data when you are sure that you don't want to keep using it.

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts health delete -u urn:health:sourceId:streamId
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
# Delete a health synchronization stream
$ stac health delete urn:health:sourceId:streamId
```

{% endtab %}
{% endtabs %}

### Clear health stream errors

The `clear-errors` option removes all errors from a health stream. This is helpful while setting up a health synchronization in StackState, or, for the case of the `TRANSACTIONAL_INCREMENTS` consistency model, when some errors can't be removed organically. For example, a request to delete a check state might raise an error if the check state isn't known to StackState. The only way to suppress such an error would be to use the `clear-errors` command.

{% tabs %}
{% tab title="CLI: sts" %}
{% hint style="info" %}
From StackState v5.0, the old `sts` CLI has been renamed to `stac` and there is a new `sts` CLI. The command(s) provided here are for use with the new `sts` CLI.

➡️ [Check which version of the `sts` CLI you are running](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
{% endhint %}

```sh
$ sts health clear-error -u urn:health:sourceId:streamId
```

{% endtab %}

{% tab title="CLI: stac (deprecated)" %}
{% hint style="warning" %}
**From StackState v5.0, the old `sts` CLI is called `stac`. The old CLI is now deprecated.**

The new `sts` CLI replaces the `stac` CLI. It's advised to install the new `sts` CLI and upgrade any installed instance of the old `sts` CLI to `stac`. For details see:

* [Which version of the `sts` CLI am I running?](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md#which-version-of-the-cli-am-i-running)
* [Install the new `sts` CLI and upgrade the old `sts` CLI to `stac`](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-sts.md#install-the-new-sts-cli)
* [Comparison between the CLIs](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/setup/cli/cli-comparison.md)
  {% endhint %}

```sh
# Clear health stream errors
$ stac health clear-errors urn:health:sourceId:streamId

```

{% endtab %}
{% endtabs %}

## Error messages

{% hint style="info" %}
Errors will be closed once the described issue has been remediated.

For example a `SubStreamStopWithoutStart` will be closed once the health synchronization observes a start snapshot message followed by a stop snapshot message.
{% endhint %}

| Error                                  | Description                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **StreamMissingSubStream**             | Raised when the health synchronization receives messages without a previous stream setup message as `start_snapshot` or `expiry`.                                                                                                                                                                                                                  |
| **StreamConsistencyModelMismatch**     | Raised when a message is received that belongs to a different consistency model than that specified when the stream was created.                                                                                                                                                                                                                   |
| **StreamMissingSubStream**             | Raised when the health synchronization receives messages with a previous start snapshot in place.                                                                                                                                                                                                                                                  |
| **SubStreamRepeatIntervalTooHigh**     | Raised when the health synchronization receives a `repeat_interval_s` greater than the configured max of 30 minutes.                                                                                                                                                                                                                               |
| **SubStreamStartWithoutStop**          | Raised when the health synchronization receives a second message to open a snapshot when a previous snapshot was still open.                                                                                                                                                                                                                       |
| **SubStreamCheckStateOutsideSnapshot** | Raised when the health synchronization receives external check states without previously opening a snapshot.                                                                                                                                                                                                                                       |
| **SubStreamStopWithoutStart**          | Raised when the health synchronization receives a stop snapshot message without having started a snapshot at all.                                                                                                                                                                                                                                  |
| **SubStreamMissingStop**               | Raised when the health synchronization doesn't receive a stop snapshot after time out period of two times the `repeat_interval_s` established in the start snapshot message. In this case an automatic stop snapshot will be applied.                                                                                                              |
| **SubStreamExpired**                   | Raised when the health synchronization stops receiving data on a particular substream for longer than the configured `expiry_interval_s`. In this case, the substream will be deleted.                                                                                                                                                             |
| **SubStreamLateData**                  | Raised when the health synchronization doesn't receive a complete snapshot timely based on the established `repeat_interval_s`.                                                                                                                                                                                                                    |
| **SubStreamTransformerError**          | Raised when the health synchronization is unable to interpret the payload sent to the receiver. For example, "Missing required field 'name'" with payload `{"checkStateId":"checkStateId3","health":"deviating","message":"Unable to provision the device. ","topologyElementIdentifier":"server-3"}` and transformation `Default Transformation`. |
| **SubStreamMissingCheckpoint**         | Raised when a Transactional increments substream previously observed a checkpoint, but the received message is missing the `previous_checkpoint`                                                                                                                                                                                                   |
| **SubStreamInvalidCheckpoint**         | Raised when a Transactional increments substream previously observed a checkpoint, but the received message has a `previous_checkpoint` that isn't equivalent to the last observed one.                                                                                                                                                            |
| **SubStreamOutdatedCheckpoint**        | Raised when a Transactional increments substream previously observed a checkpoint, but the received message has a `checkpoint` that precedes the last observed one, meaning that its data that StackState already received.                                                                                                                        |
| **SubStreamUnknownCheckState**         | Raised when deleting a Transactional increments check\_state and the `check_state_id` isn't present on the substream.                                                                                                                                                                                                                              |

## See also

* [Install the StackState CLI](https://archivedocs.stackstate.com/cli/k8sts-cli-sts)


# Kubernetes views

StackState v6.0

## Overview

StackState has deep knowledge of Kubernetes and its components. After installation of the StackState agent in your cluster, it will then automatically detect and visualize the topology of your Kubernetes applications. This includes the Kubernetes resources that make up your application, such as deployments, pods, services, and ingress. It will also automatically detect and visualize the topology of your Kubernetes infrastructure that makes up your cluster, such as nodes, namespaces, and persistent volumes.

StackState has dedicated overviews and highlights pages for the following Kubernetes native resources:

![Kubernetes views](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6a656a9b73bf6babe65af49fbbadc699e95de16e%2Fk8s-menu.png?alt=media)

All other Kubernetes resources are recognized and visualized in the topology views.

## Overview pages

The overview pages provide a high-level overview of specific Kubernetes resources in your environment. These overviews highlight the most important information about the resource, including its health, age, namespace, cluster and more.

![Overview pages](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-a4ef27705721b68a02275b0939af7abce8643fa5%2Fk8s-service-overview.png?alt=media)

From an overview page, you can click on one of the Kubernetes resources to navigate to the highlights page for that resource.

## Highlights pages

The highlights page shows an overview of the most important information about a specific Kubernetes resource. Here you can see the health of the resource, the monitors that are active on the resource, and the events that have occurred on the resource. Also we display the key metrics for the resource.

![Highlights pages](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ebfd5f97b615eedd1e40b884e1e240fd9148e85e%2Fk8s-pod-highlights.png?alt=media)


# Custom views

StackState v6.0

## Overview

Whilst a [kubernetes view](https://archivedocs.stackstate.com/views/k8s-views) acts as a starting point to explore a specific part of your IT landscape, and an [explore view](https://archivedocs.stackstate.com/views/k8s-explore-views) allows you to investigate a subset of a particular view, a **custom view** provides a way for you to get back to any of these views.

In other words, you can create a custom view by saving a [kubernetes view](https://archivedocs.stackstate.com/views/k8s-views) or an [explore view](https://archivedocs.stackstate.com/views/k8s-explore-views) with your own settings (filters, visualization options, view settings, timeline configuration) to bookmark a part of your topology that's of particular interest to you or your team.

{% hint style="info" %}
By default, custom views will be visible to all users, these can be secured by a **StackState administrator** if required.
{% endhint %}

![Custom view](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-1420d43ebe9e280b029788d98585159c37c7cd4f%2Fk8s-custom-view.png?alt=media)

## Handling

All the custom views can be found unde the **Views** entry in the main menu.

If you frequently use a certain custom view, you can add it to the **starred views**. All the starred views are listed directly in the **Views** section of the main menu for quick access - you can recognize the starred views by the yellow star icon next to their name. Add or remove a custom view from the starred views by simply clicking the star icon next to its name.

### Create a view

To create a new custom view, click the **Save view as...** blue button on the top navigation bar when you're on a [kubernetes view](https://archivedocs.stackstate.com/views/k8s-views) or an [explore view](https://archivedocs.stackstate.com/views/k8s-explore-views). To create a new view from a modified custom view, use the dropdown menu next to the button and select **Save view as...**.

![Edit view settings](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-eb4bd04cb76c2540cc00b1fbab8f09c6aabfd19f%2Fk8s-custom-view-edit-settings.png?alt=media)

In the **Save view as** dialog, the following options can be set:

| Field Name                | Description                                                                                                                                                                                                                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| View name                 | The name of the view.                                                                                                                                                                                                                                                                                                                             |
| Description               | A short description for the view. It helps remembering the scope of the view.                                                                                                                                                                                                                                                                     |
| View health state enabled | Whether the view has a health state or not. If this is enable, the view health state is calculated based on the configuration function below.                                                                                                                                                                                                     |
| Configuration function    | When view health state is enabled, you can choose a function that's used to calculate the view health state whenever there are changes in the view. The default choice is **minimum health states** - this function calculates the health state of the view based on the amount of components in **CRITICAL** or **DEVIATING** state in the view. |
| Arguments                 | The required arguments will vary depending on the chosen configuration function, if any.                                                                                                                                                                                                                                                          |
| Identifier                | A unique reference for the view, helpful when you want to reference the view from an exported configuration, such as the exported configuration in a StackPack.                                                                                                                                                                                   |

### Reset a view

When a custom view is created, all the filters, visualization options, view settings and the timeline configuration are saved on the view. If you want to reset the custom view to its original state after you have made some changes to it, use the dropdown menu next to the **Save...** button on the top navigation bar and select **Reset view**.

### Delete or edit a view

{% hint style="info" %}
Note that changes made to a custom view will be applied for all users.
{% endhint %}

A custom view can be edited or deleted from either the **all views** screen, or the **custom view** screen.

1. **All views** screen:
   * Click **Views** in the main menu to open the **all views** screen.
   * Hover over the view you would like to edit or delete.
   * Click the **Edit view settings** or **Delete view** button on the right.
2. **Custom view** screen:
   * Open the view.
   * Open the dropdown menu next to the **Save...** button on the top navigation bar.
   * Click **Edit view settings** or **Delete view**.

## Structure

A custom view has an identical structure to the [kubernetes view](https://archivedocs.stackstate.com/views/k8s-views) or the [explore view](https://archivedocs.stackstate.com/views/k8s-explore-views) it was created from: it has the same [filters](https://archivedocs.stackstate.com/k8s-view-structure#filters) and the same [perspectives](https://archivedocs.stackstate.com/k8s-view-structure#perspectives).


# Component views

StackState v6.0


# Explore views

StackState v6.0

## Overview

In general, the concept of a [view](https://archivedocs.stackstate.com/views/k8s-view-structure) in StackState allows you to monitor an area of your IT landscape that you had previously saved. But, often times when you need to investigate a subset of a particular view, you don't want to lose the scope of that view. This is where the **explore views** come into play.

To keep the scope of a particular view (e.g. `my view`) intact, all the investigative actions applied to a topology element or selection of elements (e.g. components, relations, groups) will automatically open in a temporary explore view, under the view you have started from (e.g. `my view / explore`).

Examples of **investigative actions** that will automatically be opened in an explore view:

* The **+ button** was clicked on a component in the [topology perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-topology-perspective) to show the hidden neighbors of that component
* A **quick action** was executed on a component
* A topology element (component, relation, group) was **double-clicked** in the [topology perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-topology-perspective) to investigate it
* The **'Explore...'** link or button was clicked on a topology element (component, relation, group) to investigate it

{% hint style="success" %}
The investigative actions executed from an existing explore view will **not** open a new explore view - they will change the scope of the explore view you are in.
{% endhint %}

## Handling

When an explore view is automatically created, its original scope is also defined. This is helpful if you want to reset the explore view to its original scope after you have made some changes to it.

Although an explore view is meant to be temporary, it can be saved as a [custom view](https://archivedocs.stackstate.com/views/k8s-custom-views) if you want to monitor it or review it later on.

If you don't want to save an explore view, simply move away from it or go back to the view you started from by using the breadcrumbs on the top navigation bar.

![Explore views](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-2b88ee7617195cc2104fdc700147568b2b3fe09c%2Fk8s-explore-views.png?alt=media)

## Structure

The explore views have an identical structure to the [custom views](https://archivedocs.stackstate.com/views/k8s-custom-views): they have the same [filters](https://archivedocs.stackstate.com/k8s-view-structure#filters) and the same [perspectives](https://archivedocs.stackstate.com/k8s-view-structure#perspectives).

![Explore views structure](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-7ca72f5affa0e8dcd81c09d64923df813254ba1d%2Fk8s-explore-views-structure.png?alt=media)


# View structure

StackState v6.0

## Overview

A view in StackState allows you to monitor and inspect a subset of your IT environment. The structure of a view is tailored towards filtering and visualizing the data in that subset (view) in an efficient way.

### Filters

The **Filters** menu on the top right corner of the view UI allows you to filter the components (topology), events and traces displayed in a view. Once applied, the filters will affect the content of all the perspectives in a view.

* [Filters](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-filters) - Filter the components (topology), events and traces in your view

### Perspectives

The **Perspectives** of a view are displayed as tabs on the top left corner of the view UI and allow you to visualize all the data in a view through different lenses:

* [Overview perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-overview-perspective) or [Highlights perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-highlights-perspective) - depending on the type of view you are in
* [Topology perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-topology-perspective) - the dependency map of the view components
* [Events perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-events-perspective) - all the events happening on the topology
* [Metrics perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-metrics-perspective) - key metrics for the most relevant components
* [Traces perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-traces-perspective) - the tracing information running on the topology

{% hint style="info" %}
**All the perspectives** will update their content based on the [timeline](https://archivedocs.stackstate.com/views/k8sts-timeline-time-travel) configuration.
{% endhint %}

![Overview cards layout](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6fddd5b0f2d8d4dc45641c2360bf605f3cc4c6f6%2Fk8s-overview-perspective-cards-layout.png?alt=media)


# Filters

StackState v6.0

## Overview

The **Filters** menu on the top right corner of the view UI allows you to filter the components (topology) and events displayed in a view. Once applied, the filters will affect the content of all the perspectives in a view.

![View filters](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ec2963d2e6f7266a9c1da03d5fb5763296926948%2Fk8s-filters.png?alt=media)

## Filter topology

Topology filters can be used to select a sub-set of topology components to be shown in any one of the available perspectives. While the events filter is the same for all the view types, the topology filters depend on the type of view you are in. Read more:

* [Topology filters on Kubernetes views](#topology-filters-on-kubernetes-views)
* [Topology filters on other view types](#topology-filters-on-other-view-types)

### Topology filters on Kubernetes views

On the [kubernetes views](https://archivedocs.stackstate.com/views/k8s-views), the topology filters are limited to a small set of basic filters that persist across all the Kubernetes views: `clusters` and / or `namespaces`. The persistent topology filters for Kubernetes views are placed outside the regular `filters` menu in the UI and are not interdependent on each other (e.g. selecting a cluster does **not** automatically update the `namespaces` filter to reflect only the namespaces of that cluster).

![Kubernetes topology filters](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ea0666f3d2e33ea02ce1f55f6d2c3f02b1b04a58%2Fk8s-filters-kube-topology.png?alt=media)

### Topology filters on other view types

For other view types, you can browse your topology using basic or advanced topology filters. Read more about:

* [Basic topology filters](#basic-topology-filters)
* [Advanced topology filters](#advanced-topology-filters)
* [Topology filtering limits](#topology-filtering-limits)

#### Basic topology filters

The main way to filter topology is using the available basic filters. When you set a filter, the open perspective will update to show only the visualization or data for the subset of your topology that matches the filter. Setting multiple filters will narrow down your search further. You can set more than one value for each filter to expand your search

| Filter                                            | Description                                                                                                           |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Layers, Domains, Environments and Component types | Filter by the component details included when components are imported or created.                                     |
| Component health                                  | Only include components with the named health state as reported by the associated health check.                       |
| Component labels                                  | Only include components with a specific label.                                                                        |
| Include components                                | Components named here will be included in the topology **in addition to** the components returned from other filters. |

To filter the topology using basic filters, click the **Filters** menu in the top right corner of the UI and select **Switch to basic** under the **Topology** vertical tab.

![Basic topology filters](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-27417a77a895b3ffa4c78f06c60a560236edf87a%2Fk8s-filters-basic-topology.png?alt=media)

#### Advanced topology filters

You can use the in-built [StackState Query Language (STQL)](https://archivedocs.stackstate.com/reference/k8sts-stql_reference) to build an advanced topology filter that zooms in on a specific area of your topology.

To filter the topology using an STQL query, click the **Filters** menu in the top right corner of the UI and select **Switch to STQL** under the **Topology** vertical tab.

The STQL query example below will return components that match the following conditions:

* In the **Domain** `security check`
* AND has a **Health** state of `Clear` OR `Deviating`
* OR is the **Component** with the name `ai_engine`

```yaml
(domain IN ("security check") AND healthstate IN ("CLEAR", "DEVIATING")) OR name IN ("ai_engine")
```

![Advanced topology filters](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-05ad3e4a59766824410bc0f5941cf40666c90788%2Fk8s-filters-advanced-topology.png?alt=media)

#### Compatibility of basic and advanced filters

You can switch between basic and advanced filtering by selecting **Switch to basic** or **Switch to STQL** under the **Topology** vertical tab in the **Filters** menu.

It's always possible to switch from basic to advanced filtering. The selected basic filters will be converted directly to an STQL query. For simple queries it's also possible to switch from advanced to basic filtering, however, some advanced queries aren't compatible with basic filters.

➡️ [Learn more about the compatibility of basic and advanced topology filters](https://archivedocs.stackstate.com/reference/k8sts-stql_reference#compatibility-basic-and-advanced-filters)

#### Other filters

The advanced filters listed below are compatible with basic filtering, but can't be set or adjusted as a basic filter.

* **withNeighborsOf** - when an advanced filter includes the function [withNeighborsOf](https://archivedocs.stackstate.com/reference/k8sts-stql_reference#withneighborsof), the number of components whose neighbors are queried for is shown in the **Other filters** box. To be compatible with basic filtering, a `withNeighborsOf` function must be joined to other filters using an `OR` operator.
* **identifier** - when an advanced filter selects components by [identifier](https://archivedocs.stackstate.com/reference/k8sts-stql_reference#filters), the number of component identifiers queried is reported in the **Other filters** box. To be compatible with basic filtering, an `identifier` filter must be specified and joined to other filters using the operator `OR identifier IN (...)`.

The **Other filters** box in the basic topology filters lists all these advanced filters and the number of affected components.

{% hint style="info" %}
The **Other filters** box only gives details of advanced filters that have been set and are compatible with basic filtering.
{% endhint %}

#### Topology filtering limits

To optimize performance, a limit is placed on the amount of elements that can be loaded to produce a topology visualization. The filtering limit has a default value of 10000 elements. If a [basic filter](#basic-topology-filters) or [advanced filter query](#advanced-topology-filters) exceeds the filtering limit, a message will be shown on screen and no topology visualization will be displayed.

Note that the filtering limit is applied to the total amount of elements that need to be **loaded** and not the amount of elements that will ultimately be displayed.

In the example below, we first LOAD all neighbors of every component in our topology and then DISPLAY only the ones that belong to the `applications` layer. This would likely fail with a filtering limit error as it requires all components in the topology to be loaded.

```
withNeighborsOf(direction = "both", components = (name = "*"), levels = "15")
   AND layer = "applications"
```

To successfully produce this topology visualization, we would need to either re-write the query to keep the number of components loaded below the configured filtering limit, or increase the filtering limit. By fitering for only components in the `applications` layer, we will DISPLAY the same components as the query above, without first needing to LOAD all components. This query is therefore less likely to result in a filtering limit error.

```yaml
layer = "applications"
```

## Filter events

The **View Filters** panel on the left of the StackState UI can be used to filter the events shown in the [Events Perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-events-perspective). They're also included in the **Event** list in the right panel **View summary** tab and the details tabs - **Component details** and **Direct relation details**.

The following event filters are available:

| Filter       | Description                                                                                                                                                                                                                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Category** | Show only events from one or more [categories](https://archivedocs.stackstate.com/views/k8s-events-perspective#event-category).                                                                                                                                                                                                                                                |
| **Type**     | Click the **Type** filter box to open a list of all event types that have been generated for the currently filtered components in the current time window. You can select one or more event types to refine the events displayed.                                                                                                                                              |
| **Source**   | Events can be generated by StackState or retrieved from an external source system, such as Kubernetes or ServiceNow, by an integration. Click the **Source** filter box to open a list of all source systems for events that have been generated for the currently filtered components in the current time window. Select one or more source systems to see only those events. |
| **Tags**     | Relevant event properties will be added as tags when an event is retrieved from an external system. For example `status:open` or `status:production`. This can help to identify events relevant to a specific problem or environment.                                                                                                                                          |

![Events filters](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-533bce0d99d1d4bfe296c45aa050ff9c2f6d308e%2Fk8s-filters-events.png?alt=media)


# Overview perspective

StackState v6.0

The Overview Perspective shows a list of all the components in your view. Depending on the type of view and the components in the view, the structure of the overview perspective will be different.

For example, the table structure used on the [kubernetes views](https://archivedocs.stackstate.com/views/k8s-views) will reflect the most important properties of the component types included in each view: as seen below, the `services` view has a different table structure than the `pods` view.

![Overview table structure comparison](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c1f29fff9642112ea0d2afc2e9c53c61b456b3e3%2Fk8s-overview-perspective-table-comparison.png?alt=media)

For [custom views](https://archivedocs.stackstate.com/views/k8s-custom-views) and [explore views](https://archivedocs.stackstate.com/views/k8s-explore-views), the overview perspective table will have a generic one-size-fits-all structure, composed out of the most common properties, because of the diversity of component types that might be included in the view.

![Overview table generic structure](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-075c595d8545819fa677ba478a5450840f3ac652%2Fk8s-overview-perspective-generic-table.png?alt=media)

Although a table layout will be used in most of the view types for the overview perspective, in some cases a cards layout will also be provided, allowing you to change between different modes of displaying the contents of the overview perspective.

![Overview cards layout](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6fddd5b0f2d8d4dc45641c2360bf605f3cc4c6f6%2Fk8s-overview-perspective-cards-layout.png?alt=media)


# Highlights perspective

StackState v6.0

The highlights page shows an overview of the most important information about a specific Kubernetes resource. Here you can see the health of the resource, the monitors that are active on the resource and the logs, events and the key metrics for the resource

![Highlights perspective](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ebfd5f97b615eedd1e40b884e1e240fd9148e85e%2Fk8s-pod-highlights.png?alt=media)


# Topology perspective

StackState v6.0

## Overview

The Topology Perspective displays the components in your IT landscape and their relationships.

![Topology perspective](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-0436f53549a0ca90e9bbe4ae94dec5e44b97b6db%2Fk8s-topology-perspective.png?alt=media)

## Legend

Click on the Legend button (?) in the bottom right of the screen (just below the zoom controls) to display an explanation of the icons and colors used in the topology visualization.

![Topology perspective legend](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-91c5bfa96707d46ca190f93bd0552f08d891c311%2Fk8s-topology-perspective-legend.png?alt=media)

## Components

The Topology Perspective shows the filtered components and relations in a selected [view](https://archivedocs.stackstate.com/views/k8s-view-structure). Components that have one or more [monitors](https://archivedocs.stackstate.com/monitors-and-alerts/k8s-monitors) configured will report a calculated health state.

* Select a component to display [detailed component information](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/concepts/components.md#component-details) in the right panel details tab - **Component details**.
* Hover over a component to open the [component context menu](#component-context-menu).

➡️ [Learn more about components](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/concepts/components.md#components)

### Component context menu

When you hover the mouse pointer over a component, the component context menu is displayed. This gives you information about the component, which includes:

* The component name and type
* [Health state](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/concepts/health-state.md) and [propagated health state](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/concepts/health-state.md#element-propagated-health-state) of the component.
* [Actions](#actions) specific to the component.
* [Shortcuts](#shortcuts) specific to the component.

![Component context menu](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-f22ff0461ad2d63651b145114504a8fb0f4eab6e%2Fk8s-component-contex-menu.png?alt=media)

### Actions

Actions can be used to expand the topology selection to show all dependencies for the selected component. Other actions may be available for specific components, such as component actions that are installed as part of a StackPack.

A list of the available **Actions** is included in the right panel details tab when you select a component - **Component details**. Actions are also listed in the component context menu, which is displayed when you hover the mouse pointer over a component.

### Shortcuts

Shortcuts give you direct access to detailed information about the specific component:

* **Open component view** - Opens the [component view](https://archivedocs.stackstate.com/views/k8s-component-views) for this component. The component view provides you with a bird's eye view of everything that matters about this component and its direct neighbors, depending on the component type you are viewing.
* **Explore component** - Opens an [explore view](https://archivedocs.stackstate.com/views/k8s-explore-views) containing only this component. The explore view allows you to investigate a single component from all perspectives without needing to adjust the view filters. Double-clicking a component achieves the same result.
* **Show properties** - Opens the properties popup for the component. This is the same as clicking **SHOW ALL PROPERTIES** in the right panel details tab when detailed information about a component is displayed - **Component details**.

## Relations

Relations show how components in the topology are connected together. They're represented by a dashed or solid line and have an arrowhead showing the direction of dependency between the components they link.

Select a relation to open detailed information about it in the right panel details tab - **Direct relation details**, **Indirect relation details** or **Grouped relation details** depending on the relation type that has been selected.

➡️ [Learn more about relations](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/concepts/relations.md)

## Visualization settings

The way components and relations are displayed in the topology perspective can be customized in the visualization settings menu in the top right corner of the visualizer:

* Grid - should components be organized by [layer and domain](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/concepts/layers_domains_environments.md).
* Grouping - should all components be displayed individually or should like components be grouped. For details, see [component grouping](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/views/topology-perspective.md#grouping).
* Indirect relations - should relations between components be shown if these connect through other components that aren't displayed in the view. For details, see [relations](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/concepts/relations.md).

The Visualization Settings are saved together with the View. For details, see the page [Visualization settings](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/views/visualization_settings.md).

![Visualization settings](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-9a263a92c0f2ebbc5ab5d3f744fa6ceed2eeae32%2Fk8s-visualization-settings.png?alt=media)

## Navigation

### Zoom in and out

There are zoom buttons located in the bottom right corner of the topology visualizer. The **plus** button zooms in on the topology, the **minus** button zooms out. In between both buttons is the **fit to screen** button which zooms out so the complete topology becomes visible.

### Find component

You can locate a specific component in the topology by clicking `CTRL` + `SHIFT` + `F` and typing the first few letters of the component name. Alternatively, you can select the **Find component** magnifying glass icon in the bottom right corner of the topology visualizer.

See the full list of [StackState keyboard shortcuts](https://github.com/StackVista/stackstate-docs/blob/k8s-troubleshooting/use/keyboard-shortcuts.md).

### Show root cause

If there are components with monitors on them which are outside the view but might influence the component in the view, the Topology Perspective will show the health state of all components shown.

* **Don't show root cause** - Don't show the root causes of components shown by the current topology filters.
* **Show root cause only** - Only show the root causes of components shown by the current topology filters that have a `CRITICAL` or `DEVIATING` propagated health. Indirect relations are visualized if a component directly depends on at least one invisible component that leads to the root cause.
* **Show full root cause tree** - Show all paths from components shown by the current topology filters that have a `CRITICAL` or `DEVIATING` propagated health to their root causes.

![Root cause](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-07d1baab092f71c67d404686b6810e3b66bed8d9%2Fk8s-show-root-cause.png?alt=media)

## List mode

The components in the topology visualization can also be shown in a list instead of a graph:

![Filtering(list format)](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c9c59b276cb4798cbc95fe8b3e1bd0885039425a%2Fk8s-topology-perspective-list-mode.png?alt=media)

### Export as CSV

From list mode, the component list can be exported as a CSV file. The CSV file includes `name`, `state`, `type` and `updated` details for each component in the view.

1. From the topology perspective, click the **List mode** icon on the top right to open the topology in list mode.
2. Click **Download as CSV** from the top of the page.
   * The component list will be downloaded as a CSV file named `<view_name>.csv`.


# Events perspective

StackState v6.0

## Overview

The Events Perspective shows events and changes for the elements in the current [view](https://archivedocs.stackstate.com/views/k8s-view-structure) or filtered topology.

![Events perspective](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c914f6471f7c4830d7f7f3c36350976f3160efce%2Fk8s-events-perspective.png?alt=media)

## Filter displayed events

The events displayed can be filtered in the **filters** menu in the top right corner of the view UI. Event filters will be applied to all the events shown in the view: the events perspective, highlights perspectives and the timeline.

### Filter by properties

The [event filters](https://archivedocs.stackstate.com/views/k8s-filters#filter-events) set in the **filters** menu can be used to refine the events displayed based on event category, type, source system and tags.

### Filter by source component

The [topology filters](https://archivedocs.stackstate.com/views/k8s-filters#filter-topology) set in the **filters** menu define the elements (components and relations) for which events will be displayed. Only events relating to elements that match the applied topology filters or the view itself will be visible. You can adjust the components for which events are displayed by updating the topology filters.

### Filter by timestamp

The Events Perspective and events lists show events that match the [Telemetry interval](https://archivedocs.stackstate.com/k8sts-timeline-time-travel#telemetry-interval) selected in the timeline at the bottom of the view UI. Adjust the telemetry interval to show only events that were generated at that time.

## Time travel

The Events Perspective lists events that were generated:

* by the topology elements that existed at the point in time specified by the [topology time](https://archivedocs.stackstate.com/k8sts-timeline-time-travel#topology-time).
* within the selected [telemetry interval](https://archivedocs.stackstate.com/k8sts-timeline-time-travel#telemetry-interval)

This allows you to time travel to both events generated by topology elements available at a specific point in history and events generated within a specific time window. Selecting a new topology time will time travel to the topology that was available at that point in history. The events list will be updated to include events for the topology elements available at that time and within the selected telemetry interval.

For example:

* Adjust the **Telemetry interval** to increase or decrease the number of events displayed.
* Adjust the **Topology time** to time travel to the topology available at that point in history. Events generated within the selected telemetry interval by topology elements that existed at the topology time will be displayed.
* Click a timestamp from the **Properties** of an event to jump to this topology time. This will update the events list to display events that were generated:
  * by topology elements that existed at that moment in time.
  * within the specified telemetry interval (this will be adjusted to fit the selected timestamp if required).

![Events timeline](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-e6d037c00da819eecb2de775d36822255f5f7122%2Fk8s-events-perspective-timeline.png?alt=media)

## See also

* [Filtering data](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-filters)
* [Working with StackState views](https://archivedocs.stackstate.com/views/k8s-view-structure)


# Metrics perspective

StackState v6.0

The Metrics Perspective shows metrics for the selected resource.

![Metrics perspective](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-37c5b6e03a0b2a7027f4d62db67885b05ac21694%2Fk8s-metrics-perspective.png?alt=media)

## Charts

Charts show metrics data for the selected components in near real-time - data is fetched every 30 seconds. If a process is stopped and no more data is received, the process will eventually leave the chart as the data shifts left at least every 30 seconds. If more data arrives during the 30-second interval, it will be pushed to a chart.

## Ordering

Metric charts are ordered on priority and name. Both are configured on the [metric binding](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-add-charts).


# Traces perspective

StackState v6.0

The Traces Perspective shows spans for a component and their related metrics. This allows you to monitor the performance of the applications in your IT infrastructure directly in StackState.

Click on any span in the list to see the descendant spans that belong to it. When expanded, the timeline for a span shows when each descendant started and completed. Parent spans in the same trace are collapsed by default, but can be expanded as needed.\
Spans are colored differently according to their OpenTelemetry ServiceName. When inspecting a trace and seeing the list of its spans, you can click on any span to see further details.

![Traces perspective](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c96f1bd8d996755ac07caaa8742f280cf987e5e2%2Fk8s-traces-perspective.png?alt=media)

## Filter traces

The trace filters allow you to refine the traces displayed based on span status (Error, Ok or Unset), parent type (External, Internal or Root) and duration.

In addition to these filters, the traces match the **Time Window** selected in the timeline control at the bottom of the StackState UI. Adjust the time window to show only traces from that time.

### Filtering the duration

As shown in the second screenshot, it is possible to select a duration interval for the span Duration by brushing the histogram. Zooming out can be achieved by clearing all filters, or by brushing the entire range.

## Span details

In StackState, a [view](https://archivedocs.stackstate.com/views/k8s-view-structure) shows you a sub-selection of your IT infrastructure for a particular Kubernetes resource. The traces perspective shows the spans related to the resource, along with their descendants. As a descendant span can originate from an other resource, it is possible to navigate to it from the span details. The "parent spans" link will expand the view to show the full trace.

![A descendant span details](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c7fbbedfd125fcc5bd2458df9bb41e38890113dc%2Fk8s-traces-perspective-span-details.png?alt=media)

The two images above illustrate these concepts by showing a checkout service whose main responsibility is to create an order from a cart. You can see an example of a trace and its spans for a request to place an order. A descendant span has been highlighted and its details are shown, including links to components that are related to it.

Similarly brushing a trace will zoom in on a particular time section of the trace. The selection can be reset by clicking later.

## Time Travel

When using the Traces Perspective, just like in other perspectives, you can either be in live mode or [time travel to the past](https://archivedocs.stackstate.com/k8sts-timeline-time-travel#time-travel).


# Timeline and time travel

StackState v6.0

## Overview

The timeline at the bottom of the StackState UI allows you to travel back in time to the state of the topology at a specific point in the past. You can then navigate through all telemetry available for the selected topology snapshot. Health and events charts in the timeline give an overview of the state of the topology during the selected telemetry interval.

![Timeline](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-783f5fc90368a430432bfbf85620d4a3d4a3231b%2Fk8s-timeline.png?alt=media)

## Timeline

### Telemetry interval

The telemetry interval specifies the time window for which events, metrics and traces are available in the StackState perspectives. It runs from left to right on the timeline.

![Telemetry interval](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-34cb5bb852b3cc202fd2651cbdf5b441741d6ddc%2Fv51_telemetry_interval.png?alt=media)

The selected telemetry interval can be either relative (live mode), or set to a custom telemetry interval (time travel mode). By default, the telemetry interval is set to a relative telemetry interval - in live mode and shows telemetry from the last hour. You can zoom in/out or set a custom telemetry interval to view telemetry from a specific point in time.

#### Set the telemetry interval

{% hint style="info" %}

* The telemetry interval can be a maximum of 6 months.
* When a custom telemetry interval is set for the telemetry interval, StackState will pause the [topology time](#topology-time) and enter [time travel mode](#time-travel).
  {% endhint %}

The telemetry interval can be set in the following ways:

* **Zoom in**

![Click and drag on the timeline to set a custom telemetry interval on your selection](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-0ce639a8b3a80b1918f3a018809b549179722622%2Fv51_timeline_click_drag.png?alt=media)

* **Zoom out**

![Click the magnifying glass to double the size of the telemetry interval](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-5b48031c24a0c0d908824e0bd0d4f31a64a5da4c%2Fv51_telemetry_interval_zoom_out.png?alt=media)

* **Use the telemetry interval jumper arrows**

![Click the time jumper arrows to move the telemetry interval backwards or forwards through time](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-0d5097cb9edf92dad96915cf3690f5b486ea4508%2Fv51_telemetry_interval_jumper.png?alt=media)

* **Set a relative or custom telemetry interval**

![Use the popup "Set the telemetry interval" to specify a telemetry interval](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-9cb0492b41a1c3caa31337d7c87303afe3a56a80%2Fv51_timeline_telemetry_interval.png?alt=media)

### Topology time

The topology in StackState is based on a snapshot of your environments as observed at that moment. The moment from which this snapshot is taken is specified by the topology time. By default, StackState is in live mode with the topology time set to the current time. You can [time travel](#time-travel) to a previous state of the topology by selecting a custom topology time. This helps you to investigate an issue at a certain moment in time. Even if a pod is long gone you can still see how it was connected, its logs, events, related resources, events and more.

![Topology time](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-4190c8ca3c234b844f84888b9bf11402be240869%2Fv51_topology_time.png?alt=media)

On the timeline, the selected topology time is indicated by the play head - a black line with the current topology time at the top. It's also specified in the **Topology time** box at the top of the timeline.

#### Set the topology time

The topology time can be set in the following ways:

* **Click on the timeline**

![Click anywhere on the timeline to set the topology time to that moment](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-a91d35fe48ad1493eb1fe29ae603cf7137f38090%2Fv51_topology_time_timeline.png?alt=media)

* **Use the topology time jumper arrows**

![Click the topology time jumper arrows to move the topology time backwards or forwards in time to the next set of events](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-a506c21f98d0851d77ed11bc0075e7321c0a8c0e%2Fv51_topology_time_jumper.png?alt=media)

* **Set a custom topology time**

![Use the popup "Set the topology time" to specify a topology time](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ffdb1417f6231627a52421fd38dd709b2b5af944%2Fv51_topology_time_popup.png?alt=media)

* **Click a timestamp**

![Click a timestamp to jump to that specific topology time](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-62f346890f15b98965a17403de48041e8a1ce76d%2Fv51_topology_time_timestamp.png?alt=media)

#### Topology time outside the telemetry interval

If the selected topology time is a time outside the currently selected [telemetry interval](#telemetry-interval), the message "The topology time is out of the current telemetry interval" will be displayed and the **Topology time** box at the top of the timeline will be highlighted black. As the timeline shows the telemetry interval from left to right, the play head indicating the current topology time won't be visible on the timeline.

![Topology time outside telemetry interval](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-110996c90c7f075141e1cbc4e1059008f65034b5%2Fv51_topology_time_outside_telemetry_interval.png?alt=media)

You can still browse topology and telemetry as expected:

* In the [Topology Perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-topology-perspective) the state of the topology at the selected topology time is visualized.
* In all perspectives, telemetry is displayed that was generated in the selected telemetry interval and relates to the topology elements that existed at the selected topology time.

#### Live mode

To stop time travelling and return the topology time to live mode, click **Go live** or **BACK TO LIVE** at the top of the screen.

![Go live](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ba39d90e6e05d981b6ce9c443450714809e444d0%2Fv51_timeline_go_live.png?alt=media)

### Health

The health state of a view during the selected telemetry interval is displayed as a colour in the timeline **Health** line.

For single resources, the health will be shown over time, in an overview a grey line is displayed.

![Health state not available](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-aa38135134262971d3e0c71e18c58862fa5b25f0%2Fv51_timeline_no_health_state.png?alt=media)

### Events

The **Events** line in the timeline shows a bar chart with the number of events generated at each point in time. This helps you to see moments in the past with a lot of activity. Note that only events generated by topology elements that existed at the selected [topology time](#topology-time) are displayed.

To zoom in on an event bar of interest, click and drag to select a smaller telemetry interval around it on the timeline.

![Click and drag to select a telemetry interval](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-0ce639a8b3a80b1918f3a018809b549179722622%2Fv51_timeline_click_drag.png?alt=media)

{% hint style="info" %}
A single click on the timeline will move the play head to this point in time, and thus time travel to the state of the topology at the selected [topology time](#topology-time). Only events generated by topology elements that existed at the newly selected topology time will now be displayed.
{% endhint %}

## Time travel

In each of the StackState perspectives, you can either be in live mode or in the past. In live mode, StackState will constantly poll for new data. When you time-travel through topology or telemetry, you are effectively working with a snapshot of your infrastructure. The data available is based on two selections:

* [Topology time](#topology-time) - a specific moment in time for which you want to fetch a snapshot of your Kubernetes resources.
* [Telemetry interval](#telemetry-interval) - the time range for which you want to see telemetry and traces.

To stop time travelling and return to live mode, click **Go live** or **BACK TO LIVE** at the top of the screen.

![Go live](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-ba39d90e6e05d981b6ce9c443450714809e444d0%2Fv51_timeline_go_live.png?alt=media)


# Network configuration

StackState v6.0

StackState is a SaaS offering that's hosted in the cloud. To be able to communicate from your premises/cloud to the StackState SaaS, the StackState Agent needs to be able to connect to the StackState SaaS Receiver API. When your cluster is running in a private network, you might need to configure your network to allow the StackState Agent to connect to the StackState Receiver API, because your network configuration might disallow egress traffic to the internet. This page describes how to configure your network to allow to install the StackState Agent, as well as to allow the StackState Agent to communicate with the StackState Receiver API.

{% hint style="info" %}
Traffic between the StackState Agent and the StackState Receiver API is always initiated by the StackState Agent. The StackState Receiver API doesn't initiate any traffic to the StackState Agent.
{% endhint %}

## StackState Agent installation

The installation of the StackState Agent is done through Helm. By default the Helm Chart is configured to pull the StackState Agent container images from the Quay.io docker registry. If your network configuration disallows egress traffic to the internet, you have a number of options to install the StackState Agent:

1. Configure your network to allow egress traffic to the Quay.io container registry from your Kubernetes cluster.
2. Proxy the Quay.io container registry through your own container registry.
3. Pull the Docker images into your own container registry.

For option 2 and 3, you need to configure the Helm Chart to pull the StackState Agent container images from your own container registry. A guide to configure the StackState Agent Helm Chart to pull images from your own container registry can be found [here](https://archivedocs.stackstate.com/agent/k8s-custom-registry).

## StackState Agent communication

The StackState Agent communicates with the StackState Receiver API over HTTPS. The different parts of the StackState Agent connect to the StackState Receiver API, hosted in your tenant in, see the following diagram:

![StackState Agent communication](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fdb802ea8966ca254fa22c28b4056f8f8a327d96%2Fk8s-agent-communication.png?alt=media)

All communication is done over HTTPS, using the standard HTTPS port 443. The StackState Agent uses the following endpoints to communicate with the StackState Receiver API:

* **https\://\<tenant>.app.stackstate.io/receiver/stsAgent** - the StackState Agent sends metrics, events and topology data to the StackState Receiver API.

In order to allow the StackState Agent to communicate with the StackState Receiver API, you need to configure your network to allow egress traffic to the StackState Receiver API. The StackState Receiver API is hosted in the cloud and has an specific IP specific for your tenant. You need to allow egress traffic to the internet. In order to obtain the correct IP addresses to allow egress traffic to, you can use the following command:

```bash
$ dig +short <tenant>.app.stackstate.io
```

Alternatively, you can visit the following URL in your browser: `https://www.nslookup.io/domains/<tenant>.app.stackstate.io/dns-records/`


# Proxy Configuration

The StackState Kubernetes Agent allows you to configure HTTP or HTTPS proxy settings for the connections it initiates.

## Proxy for communication with StackState

To configure the agent to proxy connections to the StackState backend, you can use Helm configuration.

### Helm Configuration

#### Via `values.yaml` File

1. Open your Helm chart `values.yaml` file.
2. Locate the `global.proxy.url` configuration and specify the proxy URL:

   ```yaml
   global:
     proxy:
       url: "https://proxy.example.com:8080"
   ```
3. Optionally, if the proxy does not have a signed certificate, disable SSL verification by setting `global.skipSslValidation` to `true`:

   ```yaml
   global:
     skipSslValidation: true
   ```

#### Via Command Line Flag

1. During installation of the Helm chart, use the `--set` flag to specify the proxy URL:

   ```bash
   helm install stackstate-k8s-agent stackstate/stackstate-k8s-agent --set global.proxy.url="https://proxy.example.com:8080"
   ```
2. To disable SSL validation via the command line, use:

   ```bash
   helm install stackstate-k8s-agent stackstate/stackstate-k8s-agent --set global.skipSslValidation=true
   ```


# Using a custom registry

StackState v6.0

## Overview

This page describes how to use a custom image registry to install the StackState Agent. There are many reasons why you might want to do this, for example:

* You want to use an image registry that is behind a firewall or on-premises.
* You have specific security requirements that prevent you from using public image registries like Docker Hub.

In this guide you can find how to copy the required Docker images to your own registry, and how to configure the Helm chart to pull images from the custom registry.

## Copying images to another registry

This section describes how to copy the images used by the StackState Agent to another registry. The images are listed in the [Images](#images) section.

### Prerequisites

The following prerequisites are required to copy the images:

* Setup a registry if you don't have one available. You can use [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) or [Azure Container Registry (ACR)](https://azure.microsoft.com/en-us/products/container-registry/) for example.
* Have the access credentials for your newly setup registry available.
* Have the `docker` command line tool installed.
* Install the `copy_images.sh` script from the [StackState Agent Helm Chart](https://github.com/StackVista/helm-charts/tree/master/stable/stackstate-k8s-agent/installation/copy_images.sh)

### Copying the images

To copy the images, execute the following steps:

```
> docker login -u <username> --password-stdin <registry>
Password: ********
Login Succeeded
> ./copy_images.sh -d <registry>
```

* The script will detect when an ECR registry is used and automatically create the required repositories. Most other registries will automatically create repositories when the first image is pushed to it.
* The script has a dry-run option that can be activated with the `-t` flag. This will show the images that will be copied without actually copying them, for example:
* Additional optional flags can be used when running the script:
  * `-c` specify a different chart to use.
  * `-r` specify a different repository to use.

### Images

The images listed below are used in the StackState Agent Helm Chart:

* [quay.io/stackstate/container-tools](https://quay.io/stackstate/container-tools)
* [quay.io/stackstate/generic-sidecar-injector](https://quay.io/stackstate/generic-sidecar-injector)
* [quay.io/stackstate/http-header-injector-proxy-init](https://quay.io/stackstate/http-header-injector-proxy-init)
* [quay.io/stackstate/http-header-injector-proxy](https://quay.io/stackstate/http-header-injector-proxy)
* [quay.io/stackstate/stackstate-k8s-agent](https://quay.io/repository/stackstate/stackstate-k8s-agent)
* [quay.io/stackstate/stackstate-k8s-process-agent](https://quay.io/repository/stackstate/stackstate-k8s-process-agent)
* [quay.io/stackstate/stackstate-k8s-cluster-agent](https://quay.io/repository/stackstate/stackstate-k8s-cluster-agent)

## Configuring the Helm Chart to use a custom registry

This section describes the values that need to be configured in the StackState Agent Helm Chart to use a custom registry.

The following values need to be configured:

* **global.imageRegistry** - the registry to use.
* **all.image.pullSecretUsername** and **all.image.pullSecretPassword** The authentication details required for the `global.imageRegistry`.

For example:

```yaml
global:
  imageRegistry: 57413481473.dkr.ecr.eu-west-1.amazonaws.com
  imagePullCredentials:
    default:
      username: johndoe
      password: my_secret-p@ssw0rd
```


# Custom Secret Management

## Overview

The stackstate/stackstate-k8s-agent (starting from version 1.0.79) supports specifying the name of a custom secret that contains the API key and cluster authorization token. This feature is useful for users who wish to manage their own secrets and avoid the automatic creation of secrets by the Helm chart.

## Regarding the Helm Chart

### Configuration Options

* `stackstate.manageOwnSecrets`: A boolean flag that determines whether the user wishes to manage their own secrets. Default value is `false`.
* `stackstate.customSecretName`: (Optional) Name of the custom secret to be created by the user. Required if `stackstate.manageOwnSecrets` is set to `true`.
* `stackstate.customApiKeySecretKey`: (Optional) Key name for the API key within the custom secret. Required if `stackstate.manageOwnSecrets` is set to `true`.
* `stackstate.customClusterAuthTokenSecretKey`: (Optional) Key name for the cluster authorization token within the custom secret. Required if `stackstate.manageOwnSecrets` is set to `true`.

### Behavior Description

* **Automatic Secret Creation**: By default, the chart continues to automatically create secrets as before if `stackstate.manageOwnSecrets` is set to `false`.
* **Custom Secret Management**: If `stackstate.manageOwnSecrets` is set to `true`, the chart expects the user to provide the name of the custom secret (`stackstate.customSecretName`) along with the keys for the API key and authorization token (`stackstate.customApiKeySecretKey` and `stackstate.customClusterAuthTokenSecretKey`, respectively).
* **Implied Omission**: When specifying that you would like to manage your own secrets, the chart will ignore values for `stackstate.apiKey` and `stackstate.cluster.authToken`.

## How to Use in values.yaml

1. **Using Automatic Secret Creation (Default)**:

   ```yaml
   stackstate:
     manageOwnSecrets: false
     apiKey: "<your api key>"
   ```
2. **Managing Own Secrets**:

   ```yaml
   stackstate:
     manageOwnSecrets: true
     customSecretName: my-custom-secret
     customApiKeySecretKey: api-key
     customClusterAuthTokenSecretKey: auth-token
   ```


# Request tracing

StackState v6.0

## Observability through load balancers, service meshes and between clusters

StackState can observe connections between services and pods in different Clusters, or when the connections go through a Service Mesh or Load Balancer. Observing these connections is done through `request tracing`. Traced requests will result in connections in the [topology perspective](https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-topology-perspective), to give insight in the dependencies across an application and help with finding the root cause of an incident.

## How does it work

Request tracing is done by injecting a unique header (the `X-Request-ID` header) into all HTTP traffic. This unique header is observed at both client and server through an eBPF probe installed with the StackState Agent. These observations are sent to StackState, which uses the observations to understand which clients and server are connected.

The `X-Request-Id` headers are [injected](#enabling-the-trace-header-injection-sidecar) by a sidecar proxy that can be automatically injected by the StackState Agent. The sidecar gets injected by a [mutating webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook), which injects the sidecar into every pod for which the `http-header-injector.stackstate.io/inject: enabled` annotation is defined. Sidecar injection is not supported on OpenShift.

It's also possible to add the `X-Request-Id` header if your application [already has a proxy or LoadBalancer](#add-the-trace-header-id-to-an-existing-proxy), is deployed to an [Istio service mesh](#add-the-trace-header-id-with-envoy-filter) enabled Kubernetes cluster or through [instrumenting your own code](#instrument-your-application). Advantage of this is that the extra sidecar proxy isn't needed.

## Enabling the trace header injection sidecar

Enabling trace header injection is a two-step process:

1. Install the mutating webhook into the cluster by adding `--set httpHeaderInjectorWebhook.enabled=true` to the helm upgrade invocation when installing the StackState agent. By default the sidecar injector generates its own self-signed certificate, requiring cluster roles to install these into the cluster. It is also possible to [manage your own certificates](https://archivedocs.stackstate.com/agent/k8sts-agent-request-tracing/k8sts-agent-request-tracing-certificates) in a more restricted environment.
2. For every pod that has a endpoint which processes http(s) requests, place the annotation `http-header-injector.stackstate.io/inject: enabled` to have the sidecar injected.

{% hint style="warning" %}
**Enabling the mutating webhook will only take effect upon pod restart**

If the annotation is placed before the webhook is installed. Installing the webhook has no effect until the pods get restarted.
{% endhint %}

### Disabling trace header injection

Disabling the trace header injection can be done with the reverse process:

1. Remove the `http-header-injector.stackstate.io/inject: enabled` annotation from all pods.
2. Redeploy the StackState Agent without the `--set httpHeaderInjectorWebhook.enabled=true` setting.

{% hint style="warning" %}
**Disabling the mutating webhook will only take effect upon pod restart**

If step 1 is skipped and only the mutating webhook is disabled, all pods need a restart for the sidecar to be removed.
{% endhint %}

### Overhead

Request tracing adds a small, fixed amount of CPU overhead for each HTTP request header that gets injected and observed. The exact amount is dependent on the system that it's ran on, so it's advised to enable this feature first in an acceptance environment to observe the impact before moving to production. The sidecar proxy takes a minimum of 25Mb of memory per pod it's deployed with, up to a maximum of 40Mb.

## Add the trace header id to an existing proxy

To add the `X-Request-Id` header from an existing proxy, two properties are important:

1. Each request/response pair has to get a unique ID.
2. The `X-Request-Id` header should be added to both request and response, to be observed on both client and server.

### Add the trace header id in envoy

In envoy, the `X-Request-Id` header can be enabled by setting `generate_request_id: true` and `always_set_request_id_in_response: true` for [http connections](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto)

## Istio

An [Envoy Filter](https://istio.io/latest/docs/reference/config/networking/envoy-filter/) can be used to set the trace header for Envoy.

### Add the trace header id with envoy filter

Use `kubectl` to apply the following definition to the Kubernetes cluster,

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: EnvoyFilter
metadata:
  name: responsed-x-request-id-always
  namespace: istio-system
spec:
  configPatches:
    - applyTo: NETWORK_FILTER
      match:
        context: ANY
        listener:
          filterChain:
            filter:
              name: envoy.filters.network.http_connection_manager
      patch:
        operation: MERGE
        value:
          typed_config:
            '@type': >-
              type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
            always_set_request_id_in_response: true
            generate_request_id: true
            preserve_external_request_id: true
  priority: 0
```

## Instrument your application

It's also possible to add the `X-Request-Id` header form either the client side to each request, or on the server side to each response. It's important to ensure each request/response gets a unique `X-Request-Id` value. Also, the `X-Request-Id` requires that if an ID is already present in a request, the response should contain that same ID.

## Supported systems/technologies

* HTTP/1.0 and HTTP/1.1 with keepAlive
* Trace header injection and trace observation on unencrypted traffic
* Trace observation for OpenSSL Encrypted traffic
* Trace header injection alongside LinkerD
* Any LoadBalancer that forwards the `X-Request-Id` header in requests and responses
* Any cross-cluster networking solution that forwards the `X-Request-Id` header in requests and responses

## Known Issues

### No sidecar is injected for my pods

To make sure you setup is ok, first validate the following steps were taken:

* The `--set httpHeaderInjectorWebhook.enabled=true` flag was set during installation of the agent
* The pod has `http-header-injector.stackstate.io/inject: enabled` set
* The pod was restarted

If this does not resolve the issue, the following could be the issue:

#### Cluster networking policies

The cluster can have networking policies setup, preventing the kubernetes control-plane apiserver from contacting the mutatingvalidationwebhook which injects the sidecar. To validate this, look at the logs of the kube-apiserver, which is either in the kube-system namespace or could be managed by your cloud provider. An error like the following should be found in those logs:

```
Failed calling webhook, failing open stackstate-agent-http-header-injector-webhook.stackstate.io: failed calling webhook "stackstate-agent-http-header-injector-webhook.stackstate.io": failed to call webhook: Post "https://stackstate-agent-http-header-injector.monitoring.svc:8443/mutate?timeout=10s": context deadline exceeded
```

If this happens, be sure to adapt your cluster network policies such that the apiserver can reach the mutatingvalidationwebhook.


# Certificates for sidecar injection

StackState v6.0

The [sidecar injection mechanism](https://archivedocs.stackstate.com/agent/k8sts-agent-request-tracing/..#enabling-the-trace-header-injection-sidecar), which gets enabled when using `--set httpHeaderInjectorWebhook.enabled=true` when installing the agent, creates a self-signed certificate and uses a `ClusterRole` which grants write access to `Secret` and `MutatingWebhookConfiguration` objects in the Kubernetes cluster.

If for security purposes it is undesirable to create `ClusterRoles` which grant cluster-wide write rights, or there are alternative ways to provide a certificate:

1. Generate a self-signed certificate [locally](#generate-a-certificate-locally).
2. Use the k8s [cert-manager](https://cert-manager.io/) (if it already on the cluster) [with a `ClusterIssuer`](#generate-a-certificate-using-the-cert-manager).

## Generate a certificate locally

To generate a certificate locally, take the following steps:

1. Download the certificate generation script and run it to produce a helm values (`tls_values.yaml`) file with the right certificate:

```
wget https://raw.githubusercontent.com/StackVista/http-header-injector/main/scripts/generate_ca_cert.sh
chmod +x generate_ca_cert.sh
./generate_ca_cert.sh <helm-agent-release-name> <helm-agent-namespace>
```

Be sure to use the release name that will be used in the helm command and the namespace, otherwise the certificate will be invalid. 2. Install the agent adding the additional configuration by adding `--set httpHeaderInjectorWebhook.enabled=true -f tls_values.yaml` to the helm invocation command

## Generate a certificate using the cert-manager

If your cluster has the [cert-manager](https://cert-manager.io/) installed, and a `ClusterIssuer` configured, it is possible to use the certificate issued by the `ClusterIssuer` in the agent for the sidecar injector. To do this, add the following command line arguments to install the agent: `--set httpHeaderInjectorWebhook.enabled=true --set-string httpHeaderInjectorWebhook.webhook.tls.mode="cert-manager" --set-string httpHeaderInjectorWebhook.webhook.tls.certManager.issuer="<my-cluster-issuer>"`. Be sure to replace my-cluster-issuer with the name of the issuer in your cluster.


# Getting started

StackState v6.0

![Open Telemetry collector and 2 instrumented applications sending metrics and traces to StackState](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-9fc9eb9a0525a01f3e5331dfd2254b4f2bbeffc9%2Fopen-telemetry.svg?alt=media)

StackState supports [Open Telemetry](https://opentelemetry.io/docs/what-is-opentelemetry/). Open Telemetry is a set of standardized protocols and an open-source framework to collect, transform and ship telemetry data such as traces, metrics and logs. Open telemetry supports a wide variety of programming languages and platforms.

StackState has support for both metrics and traces and adds the Open Telemetry metrics and traces to the (Kubernetes) topology data that is provided by the StackState agent. Therefore it is still needed to also install the StackState agent. Support for logs and using Open Telemetry without the StackState agent is coming soon.

Open Telemetry consists of several different components. For usage with StackState, the [SDKs](https://archivedocs.stackstate.com/open-telemetry/languages) to instrument your application and the [Open Telemetry collector](https://archivedocs.stackstate.com/open-telemetry/collector) are the most important parts. We'll show how to configure both for usage with StackState.

If your application is already instrumented with Open Telemetry or with any other library that is supported by Open Telemetry, like Jaeger or Zipkin, the collector can be used to ship that data to StackState and no additional instrumentation is needed.

StackState requires the collector to be configured with specific processors and authentication to make sure all data used by StackState is available.

## References

* [Open Telemetry collector](https://opentelemetry.io/docs/collector/) on the Open Telemetry documentation
* [SDKs to instrument your application](https://opentelemetry.io/docs/languages/) on the Open Telemetry documentation


# Open telemetry collector

StackState v6.0

The OpenTelemetry Collector offers a vendor-agnostic implementation to receive, process and export telemetry data. Applications instrumented with Open Telemetry SDKs can use the collector to send telemetry data to StackState (traces and metrics).

Your applications, when set up with OpenTelemetry SDKs, can use the collector to send telemetry data, like traces and metrics, straight to StackState. The collector is set up to receive this data by default via OTLP, the native open telemetry protocol. It can also receive data in other formats provided by other instrumentation SDKs like Jaeger and Zipkin for traces, and Influx and Prometheus for metrics.

Usually, the collector is running close to your application, like in the same Kubernetes cluster, making the process efficient.

For StackState integration, it's simple: StackState offers an OTLP endpoint using the gRPC protocol and uses bearer tokens for authentication. This means configuring your OpenTelemetry collector to send data to StackState is easy and standardized.

## Pre-requisites

1. A Kubernetes cluster with an application that is [instrumented with Open Telemetry](https://archivedocs.stackstate.com/open-telemetry/languages)
2. An API key for StackState
3. Permissions to deploy the open telemetry collector in a namespace on the cluster (i.e. create resources like deployments and configmaps in a namespace). To be able to enrich the data with Kubernetes attributes permission is needed to create a [cluster role](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/main/charts/opentelemetry-collector/templates/clusterrole.yaml) and role binding.

## Kubernetes configuration and deployment

To install and configure the collector for usage with StackState we'll use the [Open Telemetry Collector helm chart](https://opentelemetry.io/docs/kubernetes/helm/collector/) and add the configuration needed for StackState:

1. [Configure the collector](#configure-the-collector)
   1. helm chart configuration
   2. generating metrics from traces
   3. sending the data to StackState
   4. combine it all together in pipelines
2. [Create a Kubernetes secret for the StackState API key](#create-secret-for-the-api-key)
3. [Deploy the collector](#deploy-the-collector)
4. [Configure your instrumented applicatins to send telemetry to the collector](#configure-applications)

### Configure the collector

Here is the full values file needed, continue reading below the file for an explanation of the different parts. Or skip ahead to the next step, but make sure to replace:

* `<otlp-stackstate-endpoint>` with the OTLP endpoint of your StackState. If, for example, you access StackState on `play.stackstate.com` the OTLP endpoint is `otlp-play.stackstate.com`. So simply prefixing `otlp-` to the normal StackState url will do.
* `<your-cluster-name>` with the cluster name you configured in StackState. **This must be the same cluster name used when installing the StackState agent**. Using a differnt cluster name will result in an empty traces perspective for Kubernetes components.

{% hint style="warning" %}
The Kubernetes attributes and the span metrics namespace are required for StackState to provide full functionality.
{% endhint %}

{% hint style="info" %}
The suggested configuration includes tail sampling for traces. Sampling can be fully customized and, depending on your applications and the volume of traces, it may be needed to [change this configuration](#trace-sampling). For example an increase (or decrease) in `max_total_spans_per_second`. It is highly recommended to keep sampling enabled to keep resource usage and cost under control.
{% endhint %}

{% code title="otel-collector.yaml" lineNumbers="true" %}

```yaml
extraEnvsFrom:
  - secretRef:
      name: open-telemetry-collector
mode: deployment
ports:
  metrics:
    enabled: true
presets:
  kubernetesAttributes:
    enabled: true
    extractAllPodLabels: true
config:
  extensions:
    bearertokenauth:
      scheme: StackState
      token: "${env:API_KEY}"
  exporters:
    otlp/stackstate:
      auth:
        authenticator: bearertokenauth
      endpoint: <otlp-stackstate-endpoint>:443
  processors:
    tail_sampling:
      decision_wait: 10s
      policies:
      - name: rate-limited-composite
        type: composite
        composite:
          max_total_spans_per_second: 500
          policy_order: [errors, slow-traces, rest]
          composite_sub_policy:
          - name: errors
            type: status_code
            status_code: 
              status_codes: [ ERROR ]
          - name: slow-traces
            type: latency
            latency:
              threshold_ms: 1000
          - name: rest
            type: always_sample
          rate_allocation:
          - policy: errors
            percent: 33
          - policy: slow-traces
            percent: 33
          - policy: rest
            percent: 34
    resource:
      attributes:
      - key: k8s.cluster.name
        action: upsert
        value: <your-cluster-name>
      - key: service.instance.id
        from_attribute: k8s.pod.uid
        action: insert
    filter/dropMissingK8sAttributes:
      error_mode: ignore
      traces:
        span:
          - resource.attributes["k8s.node.name"] == nil
          - resource.attributes["k8s.pod.uid"] == nil
          - resource.attributes["k8s.namespace.name"] == nil
          - resource.attributes["k8s.pod.name"] == nil
  connectors:
    spanmetrics:
      metrics_expiration: 5m
      namespace: otel_span
    routing/traces:
      error_mode: ignore
      match_once: false
      table: 
      - statement: route()
        pipelines: [traces/sampling, traces/spanmetrics]
  service:
    extensions:
      - health_check
      - bearertokenauth
    pipelines:
      traces:
        receivers: [otlp]
        processors: [filter/dropMissingK8sAttributes, memory_limiter, resource]
        exporters: [routing/traces]
      traces/spanmetrics:
        receivers: [routing/traces]
        processors: []
        exporters: [spanmetrics]
      traces/sampling:
        receivers: [routing/traces]
        processors: [tail_sampling, batch]
        exporters: [debug, otlp/stackstate]
      metrics:
        receivers: [otlp, spanmetrics, prometheus]
        processors: [memory_limiter, resource, batch]
        exporters: [debug, otlp/stackstate]
```

{% endcode %}

The `config` section customizes the collector config itself and is discussed in the next section. The other parts are:

* `extraEnvsFrom`: Sets environment variables from the specified secret, in the next step this secret is created for storing the StackState API key (Receiver / [Ingestion API Key](https://archivedocs.stackstate.com/security/k8s-ingestion-api-keys))
* `mode`: Run the collector as a Kubernetes deployment, when to use the other modes is discussed [here](https://opentelemetry.io/docs/kubernetes/helm/collector/).
* `ports`: Used to enable the metrics port such that the collector can scrape its own metrics
* `presets`: Used to enable the default configuration for adding Kubernetes metadata as attributes, this includes Kubernetes labels and metadata like namespace, pod, deployment etc. Enabling the metadata also introduces the cluster role and role binding mentioned in the pre-requisites.

#### Configuration

The `service` section determines what components of the collector are enabled. The configuration for those components comes from the other sections (extensions, receivers, connectors, processors and exporters). The `extensions` section enables:

* `health_check`, doesn't need additional configuration but adds an endpoint for Kubernetes liveness and readiness probes
* `bearertokenauth`, this extension adds an authentication header to each request with the StackState API key. In its configuration, we can see it is getting the StackState API key from the environment variable `API_KEY`.

The `pipelines` section defines pipelines for the traces and metrics. The metrics pipeline defines:

* `receivers`, to receive metrics from instrumented applications (via the OTLP protocol, `otlp`), from spans (the `spanmetrics` connector) and by scraping Prometheus endpoints (the `prometheus` receiver). The latter is configured by default in the collector Helm chart to scrape the collectors own metrics
* `processors`: The `memory_limiter` helps to prevent out-of-memory errors. The `batch` processor helps better compress the data and reduce the number of outgoing connections required to transmit the data. The `resource` processor adds additional resource attributes (discussed separately)
* `exporters`: The `debug` exporter simply logs to stdout which helps when troubleshooting. The `otlp/stackstate` exporter sends telemetry data to StackState using the OTLP protocol. It is configured to use the bearertokenauth extension for authentication to send data to the StackState OTLP endpoint.

For traces, there are 3 pipelines that are connected:

* `traces`: The pipeline that receives traces from SDKs (via the `otlp` receiver) and does the initial processing using the same processors as for metrics. It exports into a router which routes all spans to both other traces pipelines. This setup makes it possible to calculate span metrics for all spans while applying sampling to the traces that are exported.
* `traces/spanmetrics`: Use the `spanmetrics` connector as an exporter to generate metrics from the spans (`otel_span_duration` and `otel_span_calls`). It is configured to not report time series anymore when no spans have been observed for 5 minutes. StackState expects the span metrics to be prefixed with `otel_span_`, which is taken care of by the `namespace` configuration.
* `traces/sampling`: The pipeline that exports traces to StackState using the OTLP protocol, but uses the tail sampling processor to make the trace volume that is sent to StackState predictable to keep the cost predictable as well. Sampling is discussed in a [separate section](#trace-sampling).

The `resource` processor is configured for both metrics and traces. It adds extra resource attributes:

* The `k8s.cluster.name` is added by providing the cluster name in the configuration. StackState needs the cluster name and Open Telemetry does not have a consistent way of determining it. Because some SDKs, in some environments, provide a cluster name that does not match what StackState expects the cluster name is an `upsert` (overwrites any pre-existing value).
* The `service.instance.id` is added based on the pod uid. It is recommended to always provide a service instance id, and the pod uid is an easy way to get a unique identifier if the SDKs don't provide one.

#### Trace Sampling

It is highly recommended to use sampling for traces:

* To manage resource usage by only processing and storing the most relevant traces
* To manage costs and have predictable costs
* To reduce noise and focus on the important traces only, for example by filtering out health checks

There are 2 approaches for sampling, head sampling and tail sampling. This [Open Telemetry docs page](https://opentelemetry.io/docs/concepts/sampling/) discusses the pros and cons of both approaches in detail. The collector configuration provided here uses tail sampling to support these requirements:

1. Have predictable cost by having a predictable trace volume
2. Have a large sample of all errors
3. Have a large sample of all slow traces
4. Have a sample of all other traces to see the normal application behavior

Criteria 2 and 3 can only be fulfilled by tail sampling. Let's look at the sampling policies used in the configuration of the tail sampler now:

* There is only one top-level policy, it is a `composite` policy. It uses a rate limit, allowing at most 500 traces per second, giving a predictable trace volume. It uses other policies as sub-policies to make the actual sampling decissions.
* The `errors` policy is of type `status_code` and is configured to only sample traces that contain errors. 33% of the rate limit is reserved for errors, via the `rate_allocation` section of the composite policy.
* The `slow-traces` policy is of type `latency` and filters all traces slower than 1 second. 33% of the rate limits is reserved for the slow traces.
* The `rest` policy is of the `always_sample` type. It will sample all traces until it hits the rate limit enforced by the composite policy, which is 34% of the total rate limit of 500 traces.

There are many more policies available that can be added to the configuration when needed. For example, it is possible to filter traces based on certain attributes (only for a specific application or customer). The tail sampler can also be replaced with the probabilistic sampler. For all configuration options please use the documentation of these processors:

* [Tail sampling](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor)
* [Probabilistic sampling](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/probabilisticsamplerprocessor)

### Create a secret for the API key

The collector needs a Kubernetes secret with the StackState API key. Create that in the same namespace (here we are using the `open-telemetry` namespace) where the collector will be installed (replace `<stackstate-api-key>` with your API key):

```bash
kubectl create secret generic open-telemetry-collector \
    --namespace open-telemetry \
    --from-literal=API_KEY='<stackstate-api-key>' 
```

StackState supports two types of keys:

* Receiver API Key
* Ingestion API Key

#### Receiver API Key

You can find the API key for StackState on the Kubernetes Stackpack installation screen:

1. Open StackState
2. Navigate to StackPacks and select the Kubernetes StackPack
3. Open one of the installed instances
4. Scroll down to the first set of installation instructions. It shows the API key as `STACKSTATE_RECEIVER_API_KEY` in text and as `'stackstate.apiKey'` in the command.

#### Ingestion API Key

StackState supports creating multiple Ingestion Keys. This allows you to assign a unique key to each OpenTelemetry Collector for better security and access control. For instructions on generating an Ingestion API Key, refer to the [documentation page](https://archivedocs.stackstate.com/security/k8s-ingestion-api-keys).

### Deploy the collector

To deploy the collector first make sure you have the Open Telemetry helm charts repository configured:

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
```

Now install the collector, using the configuration defined in the previous steps:

```bash
helm upgrade --install opentelemetry-collector open-telemetry/opentelemetry-collector \
  --values otel-collector.yaml \
  --namespace open-telemetry
```

### Configure applications

The collector as it is configured now is ready to receive and send telemetry data. The only thing left to do is to update the SDK configuration for your applications to send their telemetry via the collector to the agent.

Use the [generic configuration for the SDKs](https://archivedocs.stackstate.com/open-telemetry/languages/sdk-exporter-config) to export data to the collector. Follow the [language-specific instrumentation instructions](https://archivedocs.stackstate.com/open-telemetry/languages) to enable the SDK for your applications.

## Related resources

The Open Telemetry documentation provides much more details on the configuration and alternative installation options:

* Open Telemetry Collector configuration: <https://opentelemetry.io/docs/collector/configuration/>
* Kubernetes installation of the collector: <https://opentelemetry.io/docs/kubernetes/helm/collector/>
* Using the Kubernetes operator instead of the collector Helm chart: <https://opentelemetry.io/docs/kubernetes/operator/>
* Open Telemetry sampling: <https://opentelemetry.io/blog/2022/tail-sampling/>


# Languages

StackState v6.0

Open telemetry provides [SDKs for many languages](https://opentelemetry.io/docs/languages/) to (auto-)instrument your application. Instrumentation enables your application to send traces, metrics and logs to StackState. Auto-instrumentation captures traces, metrics and logs for popular libraries and frameworks without any further manual intervention except including the SDK in your application.

Open Telemetry has many more SDKs than are documented here. If your language is not documented here you can use the documentation at [opentelemetry.io](https://opentelemetry.io/docs/languages/) in combination with the [SDK exporter configuration](https://archivedocs.stackstate.com/open-telemetry/languages/sdk-exporter-config) needed for StackState.


# Generic Exporter configuration

StackState v6.0

All SDKs, regardless of the language, use the same basic configuration for defining the Open Telemetry [service name](https://opentelemetry.io/docs/concepts/glossary/#service) and the exporter endpoint (i.e. where the telemetry is sent).

These can be configured by setting environment variables for your instrumented application.

In Kubernetes set these environment variables in the manifest for your workload (replace `<the-service-name>` with a name for your application service):

```yaml
...
spec:
  containers:
  - env:
    - name: OTEL_EXPORTER_OTLP_ENDPOINT 
      value: http://opentelemetry-collector.open-telemetry.svc.cluster.local:4317
    - name: OTEL_SERVICE_NAME
      value: <the-service-name>
    - name: OTEL_EXPORTER_OTLP_PROTOCOL
      value: grpc
...
```

The endpoint specified in the example assumes the collector was installed using the defaults from [the installation guide](https://archivedocs.stackstate.com/open-telemetry/collector). It uses port `4317` which uses the `gRPC` version of the OTLP protocol. Some instrumentations only support HTTP, in that case, use port `4318`.

The service name can also be derived from Kubernetes labels that may already be present. For example like this:

```yaml
spec:
  containers:
  - env:
    - name: OTEL_SERVICE_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.labels['app.kubernetes.io/component']
```

## gRPC vs HTTP

OTLP, the Open Telemetry Protocol, supports gRPC and protobuf over HTTP. Some SDKs also support JSON over HTTP. In the previous section, the exporter protocol is set to `gRPC`, this usually gives the best performance and is the default for many SDKs. However, in some cases it may be problematic:

* Some firewalls are not setup to handle gRPC
* (reverse) proxies and load balancers may not support gRPC without additional configuration
* gRPC's long-lived connections may cause problems when load-balancing.

To switch to HTTP instead of gRPC change the protocol to `http` *and* use port `4318`.

To summarize, use HTTP in case gRPC is given problems:

* `grpc` protocol uses port `4317`
* `http` protocol uses port `4318`


# Java

StackState v6.0

The Java SDK supports instrumenting applications on the JVM. As a result it not only supports Java but also other JVM languages like Kotlin and Scala.

## Automatic instrumentation

Automatic instrumentation for Java uses a Java agent JAR that can be attached to any Java 8+ application. It dynamically injects bytecode to capture telemetry from many [popular libraries and frameworks](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/docs/supported-libraries.md), including several Kotlin and Scala libraries. It can be used to capture telemetry data at the “edges” of an app or service, such as inbound requests, outbound HTTP calls, database calls, and so on.

Automatic instrumentation does not require any modifications of the application. To set it up follow these steps:

1. Download [opentelemetry-javaagent.jar](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar) from [Releases](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases) of the opentelemetry-java-instrumentation repository and include the JAR file in the docker image of your application. The JAR file contains the agent and instrumentation libraries.
2. Update the command that starts your application to load the Java agent, either by updating the docker image entry point or command or by updating the `command` in the Kubernetes manifest for your application. Add `-javaagent:/path/to/opentelemetry-javaagent.jar`:

```bash
java -javaagent:/path/to/opentelemetry-javaagent.jar -jar myapp.jar
```

3. Deploy your application with the extra environment variables [to configure the service name and exporter endpoint](https://archivedocs.stackstate.com/open-telemetry/languages/sdk-exporter-config).
4. [Verify](https://archivedocs.stackstate.com/open-telemetry/languages/verify) StackState is receiving traces and/or metrics

For more details please refer to the [Open Telemetry documentation](https://opentelemetry.io/docs/languages/java/automatic/).

## Manual instrumentation

Manual instrumentation can be used when you need metrics, traces or logs from parts of the code that are not supported by the auto instrumentation. For example unsupported libraries, in-house code or business-level metrics.

To capture that data you need to modify your application.

1. Include the Open Telemetry SDK as a dependency
2. Add code to your application to capture metrics, spans or logs where needed

There is detailed documentation for this on the [Open Telemetry Java SDK doc pages](https://opentelemetry.io/docs/languages/java/instrumentation/).

Make sure you use the OTLP exporter (this is the default) and [auto-configuration](https://opentelemetry.io/docs/languages/java/instrumentation/#autoconfiguration). When deploying the application the service name and exporter are [configured via environment variables](https://archivedocs.stackstate.com/open-telemetry/languages/sdk-exporter-config).

## Metrics in StackState

For some Java metrics, for example, garbage collector metrics, StackState has defined charts on the related components. For Kubernetes, the charts are available on the pods. It is possible to [add charts for more metrics](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-add-charts), this works for metrics from automatic instrumentation but also for application-specific metrics from manual instrumentation.


# Node.js

StackState v6.0

## Automatic instrumentation

Automatic instrumentation for Node.js is done by including the automatic instrumentation Javascript libraries with your application. A wide range of [libraries and frameworks is supported](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/metapackages/auto-instrumentations-node#supported-instrumentations).

Automatic instrumentation does not require any modifications of the application. To set it up follow these steps:

1. Add the Open Telemetry instrumentation SDK to your application:

```bash
npm install --save @opentelemetry/api
npm install --save @opentelemetry/auto-instrumentations-node
```

2. Update the command that starts your application to load the SDK, either by updating the docker image entry point or command or by updating the `command` in the Kubernetes manifest for your application. Add `--require @opentelemetry/auto-instrumentations-node/register`:

```bash
node --require @opentelemetry/auto-instrumentations-node/register app.js
```

3. Deploy your application with the extra environment variables [to configure the service name and exporter endpoint](https://archivedocs.stackstate.com/open-telemetry/languages/sdk-exporter-config).
4. [Verify](https://archivedocs.stackstate.com/open-telemetry/languages/verify) StackState is receiving traces and/or metrics

For more details please refer to the [Open Telemetry documentation](https://opentelemetry.io/docs/languages/js/automatic/).

{% hint style="warning" %}
The auto instrumentation configured via environment variables only supports traces until this [Open Telemetry issue](https://github.com/open-telemetry/opentelemetry-js/issues/4551) is resolved. To enable metrics from the automatic instrumentation code changes are needed. Please follow the instructions in the [Open Telemetry documentation](https://opentelemetry.io/docs/languages/js/exporters/#usage-with-nodejs) to make these changes.
{% endhint %}

## Manual instrumentation

Manual instrumentation can be used when you need metrics, traces or logs from parts of the code that are not supported by the auto instrumentation. For example unsupported libraries, in-house code or business-level metrics.

To capture that data you need to modify your application.

1. Include the Open Telemetry SDK as a dependency
2. Add code to your application to capture metrics, spans or logs where needed

There is detailed documentation for this on the [Open Telemetry Javascript SDK doc pages](https://opentelemetry.io/docs/languages/js/instrumentation/).

Make sure you use the OTLP exporter and configure the exporter endpoint correctly from the code. See also the [Open Telemetry documentation](https://opentelemetry.io/docs/languages/js/exporters/#usage-with-nodejs). Assuming you set up the exporter as [documented](https://archivedocs.stackstate.com/open-telemetry/collector) the endpoint that needs to be configured is `http://opentelemetry-collector.open-telemetry.svc.cluster.local:4317`, using gRPC. See also [gRPC vs HTTP](https://archivedocs.stackstate.com/open-telemetry/sdk-exporter-config#grpc-vs-http) in case gRPC is problematic.


# .NET

StackState v6.0

## Automatic instrumentation

Automatic instrumentation for .NET can automatically capture traces and metrics for a variety of [libraries and frameworks](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/blob/main/docs/internal/instrumentation-libraries.md).

Automatic instrumentation does not require any modifications of the application. To set it up follow these steps:

1. Download the [glibc](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/releases/latest/download/opentelemetry-dotnet-instrumentation-linux-glibc.zip) or [musl](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/releases/latest/download/opentelemetry-dotnet-instrumentation-linux-musl.zip) version of the instrumentation libraries (musl for Alpine, glibc for most other docker images) from the [Releases](https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases) of the opentelemetry-dotnet-instrumentation repository. Unzip the files and include them in your application docker image in a directory, here we use `/autoinstrumentation`.
2. Set the following env vars, here we do it via the `env` of the container in the Kubernetes pod spec:

```yaml
env: 
- name: CORECLR_ENABLE_PROFILING
  value: "1"
- name: CORECLR_PROFILER
  value: "{918728DD-259F-4A6A-AC2B-B85E1B658318}"
- name: CORECLR_PROFILER_PATH
  # for glibc:
  value: "/autoinstrumentation/linux-x64/OpenTelemetry.AutoInstrumentation.Native.so"
  # For musl use instead:
  # value: "/autoinstrumentation/linux-musl-x64/OpenTelemetry.AutoInstrumentation.Native.so"
- name: DOTNET_ADDITIONAL_DEPS
  value: "/autoinstrumentation/AdditionalDeps"
- name: DOTNET_SHARED_STORE
  value: "/autoinstrumentation/store"
- name: DOTNET_STARTUP_HOOKS
  value: "/autoinstrumentation/net/OpenTelemetry.AutoInstrumentation.StartupHook.dll"
- name: OTEL_DOTNET_AUTO_HOME
  value: "/autoinstrumentation"
```

3. Also add the extra environment variables [to configure the service name and exporter endpoint](https://archivedocs.stackstate.com/open-telemetry/languages/sdk-exporter-config) on the pod.
4. Deploy your application with the changes
5. [Verify](https://archivedocs.stackstate.com/open-telemetry/languages/verify) StackState is receiving traces and/or metrics

For more details please refer to the [Open Telemetry documentation](https://opentelemetry.io/docs/languages/java/automatic/).

## Manual instrumentation

Manual instrumentation can be used when you need metrics, traces or logs from parts of the code that are not supported by the auto instrumentation. For example unsupported libraries, in-house code or business-level metrics.

To capture that data you need to modify your application.

1. Include the Open Telemetry SDK as a dependency
2. Add code to your application to capture metrics, spans or logs where needed

There is detailed documentation for this on the [Open Telemetry .NET SDK doc pages](https://opentelemetry.io/docs/languages/net/instrumentation/).

Make sure you use the OTLP exporter (this is the default) and [auto-configuration](https://opentelemetry.io/docs/languages/java/instrumentation/#autoconfiguration). When deploying the application the service name and exporter are [configured via environment variables](https://archivedocs.stackstate.com/open-telemetry/languages/sdk-exporter-config).

## Metrics in StackState

For some .NET metrics, for example, garbage collector metrics, StackState has defined charts on the related components. For Kubernetes,the charts are available on the pods. It is possible to [add charts for more metrics](https://archivedocs.stackstate.com/metrics/custom-charts/k8s-add-charts), this works for metrics from automatic instrumentation but also for application-specific metrics from manual instrumentation.


# Verify the results

StackState v6.0

If the collector and the instrumentation setup has been successful data should be available in StackState within about a minute or two.

You can check that StackState is receiving traces:

1. Open StackState in a browser
2. Find (one of) the pods that is instrumented
3. Select the pod to open the Highlights page
4. Open the trace perspective. If the pod is serving traffic it should now show traces

To check that StackState is receiving metrics:

1. Open StackState in a browser
2. Open the metrics explorer from the menu
3. Search for the metrics exposed by your application

If there are still no metrics after 5 minutes something is likely mis-configured. See [troubleshooting](https://archivedocs.stackstate.com/open-telemetry/troubleshooting) for help.


# Troubleshooting

StackState v6.0

There are a lot of configuration options but more importantly, every (Kubernetes) environment is slightly different. To find out where the problem is the quickest approach is to pick a pod from which telemetry data is expected:

1. Check the beginning of the logs for the pod, SDKs will log warnings or errors when instrumentation fails at startup
2. Check the logs also for any errors related to sending data to the collector
3. Check the logs of the collector pod(s) for configuration or initialization errors, these will be logged right after the startup of the pod
4. Check the collector logs also for errors related to sending data to StackState

The error(s) in the logs usually give a good indication of the problem. We list the most common causes for Open Telemetry data not being available for some or all of your instrumented applications. If the problem is not listed here you can also look at the [language-specific SDK documentation](https://opentelemetry.io/docs/languages/) or the [collector documentation](https://opentelemetry.io/docs/collector/troubleshooting/) from Open Telemetry.

## Use the same Kubernetes cluster name

Make sure you use the same Kubernetes cluster name for the same cluster when:

* Installing the Open Telemetry Collector
* Installing the StackState agent
* Installing the Kubernetes StackPack

When different names are used for the same cluster StackState will not be able to match the data from Open Telemetry with the data from the StackState agent and the traces perspective will remain empty.

## The collector cannot send data to StackState

### StackState's OTLP endpoint and API key are misconfigured

If there are connection errors it is possible the OTLP endpoint is incorrect. If there are authentication/authorization errors (status codes 401 and 403) it is likely the API key is not valid (anymore). Check that the configured OTLP endpoint is the URL for your StackState, prefixed with `otlp-` and suffixed with `:443`. For example, the OTLP endpoint for `play.stackstate.com` is `otlp-play.stackstate.com:443`.

To ensure the api key is configured correctly check that:

1. the secret contains a valid API key (verify this in StackState)
2. the secret is used as environment variables on the pod
3. the `bearertokenauth` extension is using the correct scheme and the value from the `API_KEY` environment variable
4. the `bearertokenauth` extension is used by the `otlp/stackstate` exporter

### Some proxies and firewalls don't work well with gRPC

If the collector needs to send data through a proxy or a firewall it can be that they either block the traffic completely or possibly drop some parts of the gRPC messages or unexpectedly drop the long-lived gRPC connection completely. The easiest fix is to switch from gRPC to use HTTP instead, by replacing the `otlp/stackstate` exporter configuration and all its references with the `otlp-http/stackstate` exporter with this configuration.

```yaml
    otlp-http/stackstate:
      auth:
        authenticator: bearertokenauth
      endpoint: <otlp-http-stackstate-endpoint>:4318
```

Here `<otlp-http-stackstate-endpoint>` is similar to the `<otlp-stackstate-endpoint>`, but instead of a `otlp-` prefix it has `otlp-http-` prefix, for example, `otlp-http-play.stackstate.com`.

## The instrumented application cannot send data to the collector

### The URL is incorrect or traffic is blocked

If the SDK logs errors about not being able to resolve the collector DNS name it may be the configured collector URL is incorrect. In Kubernetes, your application is usually deployed in a separate namespace from the collector. This means that the SDK needs to be configured with the fully qualified domain name for the collector service: `http://<service-name>.<namespace>.svc.cluster.local:4317`. In the [collector installation steps](https://archivedocs.stackstate.com/open-telemetry/collector), this was `http://opentelemetry-collector.open-telemetry.svc.cluster.local:4317`, but if you used a different namespace or release name for the collector this may be different for your situation.

If the SDK logs network connection timeouts it can be that either there is a misconfiguration on the collector or the [wrong port](#the-language-sdk-uses-the-wrong-port) is used. But it is also possible that Kubernetes network policies are blocking network traffic from your application to the collector. This is best verified with your Kubernetes administrator. Network policies should at least allow TCP traffic on the configured port (4317 and/or 4318) from all of your applications to the collector.

### The language SDK doesn't support gRPC

Not all language SDKs have support for gRPC. If OTLP over gRPC is not supported it is best to switch to OTLP over HTTP. The [SDK exporter config](https://archivedocs.stackstate.com/languages/sdk-exporter-config#grpc-vs-http) describes how to make this switch.

### The language SDK uses the wrong port

Using the wrong port usually appears as a connection error but can also show up as network connections being unexpectedly closed. Make sure the SDK exporter is using the right port when sending data. See the [SDK exporter config](https://archivedocs.stackstate.com/languages/sdk-exporter-config#grpc-vs-http).

### Some proxies and firewalls don't work well with gRPC

If the collector needs to send data through a proxy or a firewall it can be that they either block the traffic completely or possibly drop some parts of the gRPC messages or unexpectedly drop the long-lived gRPC connection completely. The [SDK exporter config](https://archivedocs.stackstate.com/languages/sdk-exporter-config#grpc-vs-http) describes how to switch from gRPC to HTTP instead.

## Kubernetes pods with hostNetwork enabled

The Open Telemetry collector enriches the telemetry data with Kubernetes metadata. The way it is configured all telemetry data that cannot be enriched is dropped. However, the collector cannot enrich pods that are running with `hostNetwork: true` set automatically. This is not possible because pod identification happens using the IP address of the pod and pods that use the host network use the IP address of the host.

To help the collector to identify a pod we can add the `k8s.pod.uid` attribute to the metadata by instructing the SDK to add it directly. To do this modify your pod spec and add the following environment variables to your instrumented application container:

```yaml
env:
  - name: POD_UID
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.uid
  - name: OTEL_RESOURCE_ATTRIBUTES
    value: k8s.pod.uid=$(POD_UID)
```

If the `OTEL_RESOURCE_ATTRIBUTES` env var is already set simply add the `k8s.pod.uid`, using a comma as separator. The value is a comma-separated list.

## Node.js application on Google Kubernetes Engine

The Node.js SDK, only on GKE, expects that the Kubernetes namespace is set via the `NAMESPACE` environment variable. If it is not set it will still add the `k8s.namespace.name` attribute but with an empty value. This prevents the Kubernetes attributes processor from inserting the correct namespace name. Until this is fixed a workaround is to update your pod spec and add this environment variable to the instrumented container(s):

```yaml
env:
  - name: NAMESPACE
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.namespace
```

## No metrics available for Node.js application

The auto instrumentation for Node.js, configured via environment variables, only supports traces. At least until this [Open Telemetry issue](https://github.com/open-telemetry/opentelemetry-js/issues/4551) is resolved. To enable metrics from the automatic instrumentation code changes are needed. Please follow the instructions in the [Open Telemetry documentation](https://opentelemetry.io/docs/languages/js/exporters/#usage-with-nodejs) to make these changes.

## Kubernetes attributes cannot be added

During the installation of the collector, a cluster role and cluster role binding are created in Kubernetes that allows the collector to read metadata from Kubernetes resources. If this fails or they get removed the collector will not be able to query the Kubernetes API anymore. This will appear as errors in the collector log, the errors include the resource types for which the metadata could not be retrieved.

To fix this re-install the collector with the Helm chart and make sure you have the required permissions to create the cluster role and cluster role binding. Alternatively, ask your cluster administrator to do the collector installation with the required permissions.


# StackState CLI

StackState v6.0

## Overview

The StackState `sts` CLI provides easy access to the functionality provided by the StackState APIs. It can be used for automation using StackState data, to configure StackState and to develop StackPacks.

## Install the `sts` CLI

### Windows

Follow the steps below to install the StackState `sts` CLI on Windows.

{% tabs %}
{% tab title="Installer" %}
Open a **Powershell** terminal (version 5.1 or later), change the `<URL>` and `<API-TOKEN>` and run the command below. After installation, the `sts` command will be available for the current user on both the Powershell terminal and the command prompt (cmd.exe).

```powershell
. { iwr -useb https://dl.stackstate.com/stackstate-cli/install.ps1 } | iex; install -StsUrl "<URL>" -StsApiToken "<API-TOKEN>"
```

Alternatively, go to the **CLI** page in the StackState UI and copy the **Quick installation** command for **Windows** - this is pre-filled with the correct `<URL>` and `<API-TOKEN>` for your StackState instance.
{% endtab %}

{% tab title="Manual install steps" %}
Open a **Powershell** terminal (version 5.1 or later) and run the steps below. This can be done one step at a time, or joined together as a single script. After installation, the `sts` command will be available for the current user on both the Powershell terminal and the command prompt (cmd.exe).

1. Set the source version and target path for the CLI:

   ```powershell
   $CLI_PATH = $env:USERPROFILE +"\stackstate-cli"
   If (!(test-path $CLI_PATH)) { md $CLI_PATH }
   Invoke-WebRequest https://dl.stackstate.com/stackstate-cli/LATEST_VERSION -OutFile $CLI_PATH\VERSION
   $VERSION=type $CLI_PATH\VERSION
   $VERSION=$VERSION -replace "[v]"
   $CLI_DL = "https://dl.stackstate.com/stackstate-cli/v$VERSION/stackstate-cli-$VERSION.windows-x86_64.zip"
   echo "Installing StackState CLI v$VERSION to: $CLI_PATH"
   ```
2. Download and unpack the CLI to the target CLI path. Remove remaining artifacts:

   ```powershell
   Invoke-WebRequest $CLI_DL -OutFile $CLI_PATH\stackstate-cli.zip
   Expand-Archive -Path "$CLI_PATH\stackstate-cli.zip" -DestinationPath $CLI_PATH -Force
   rm $CLI_PATH\stackstate-cli.zip, $CLI_PATH\VERSION
   ```
3. Register the CLI path to the current user's PATH. This will make the `sts` command available everywhere:

   ```powershell
    $PATH = (Get-ItemProperty -Path "Registry::HKEY_CURRENT_USER\Environment" -Name PATH).Path
    if ( $PATH -notlike "*$CLI_PATH*" ) {
      $PATH = "$PATH;$CLI_PATH"
      (Set-ItemProperty -Path "Registry::HKEY_CURRENT_USER\Environment" -Name PATH –Value $PATH)
      $MACHINE_PATH = (Get-ItemProperty -Path "Registry::HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment" -Name PATH).path
      $env:Path = "$PATH;$MACHINE_PATH"
    }
   ```
4. Verify that the CLI works:

   ```powershell
   sts version
   ```

{% endtab %}
{% endtabs %}

### macOS

Follow the steps below to install the StackState `sts` CLI on macOS.

{% tabs %}
{% tab title="Installer" %}
Open a terminal, change the `<URL>` and `<API-TOKEN>` and run the command below.

* The default install location is `/usr/local/bin`, which might require sudo permissions depending on the version of your machine.
* You can specify an install location by adding `STS_CLI_LOCATION` to the command, as shown below. Note that the path provided must be available in your OS Path or the script might fail to complete.

After installation, the `sts` command will be available for the current user.

```bash
# Install in default location `/usr/local/bin`
curl -o- https://dl.stackstate.com/stackstate-cli/install.sh | STS_URL="<URL>" STS_API_TOKEN="<API-TOKEN>" bash

# Install in a specified location
curl -o- https://dl.stackstate.com/stackstate-cli/install.sh | STS_URL="<URL>" STS_API_TOKEN="<API-TOKEN>" STS_CLI_LOCATION="<INSTALL-PATH>" bash
```

Alternatively, go to the **CLI** page in the StackState UI and copy the **Quick installation** command for **MacOS** - this is pre-filled with the correct `<URL>` and `<API-TOKEN>` for your StackState instance and will install the CLI at the default location.
{% endtab %}

{% tab title="Manual install steps" %}
Open a terminal and run the steps below. This can be done one step at a time, or all together as a single script. After installation, the `sts` command will be available for the current user.

3. Download the latest CLI version for x86\_64 (Intel) or arm64 (M1).

   ```bash
   (VERSION=`curl https://dl.stackstate.com/stackstate-cli/LATEST_VERSION` &&
     VERSION=${VERSION#v} &&
     ARCH=`uname -m` &&
     curl https://dl.stackstate.com/stackstate-cli/v$VERSION/stackstate-cli-$VERSION.darwin-$ARCH.tar.gz | tar xz --directory /usr/local/bin)
   ```
4. Verify that the CLI works:

   ```bash
   sts version
   ```

{% endtab %}
{% endtabs %}

### Linux

Follow the steps below to install the StackState `sts` CLI on Linux.

{% tabs %}
{% tab title="Installer" %}
Open a terminal, change the `<URL>` and `<API-TOKEN>` and run the command below. After installation, the `sts` command will be available for the current user.

```bash
curl -o- https://dl.stackstate.com/stackstate-cli/install.sh | STS_URL="<URL>" STS_API_TOKEN="<API-TOKEN>" bash
```

Alternatively, go to the **CLI** page in the StackState UI and copy the **Quick installation** command for **Linux** - this is pre-filled with the correct `<URL>` and `<API-TOKEN>` for your StackState instance.
{% endtab %}

{% tab title="Manual install steps" %}
Open a terminal and run the steps below. This can be done one step at a time, or all together as a single script. After installation, the `sts` command will be available for the current user.

1. Download and unpack the latest version for x86\_64:

   ```bash
   (VERSION=`curl https://dl.stackstate.com/stackstate-cli/LATEST_VERSION` && VERSION=${VERSION#v} &&
   curl https://dl.stackstate.com/stackstate-cli/v$VERSION/stackstate-cli-$VERSION.linux-x86_64.tar.gz | tar xz --directory /usr/local/bin)
   ```
2. Verify that the CLI works:

   ```bash
   sts version
   ```

{% endtab %}
{% endtabs %}

### Docker

To run the latest version of the CLI using Docker execute:

```bash
docker run stackstate/stackstate-cli2
```

Alternatively, go to the **CLI** page in the StackState UI and copy the **Quick installation** command for **Docker** - this is pre-filled with the correct `<URL>` and `<API-TOKEN>` required to configure the CLI for your StackState instance.

You can now run CLI commands by adding appending them to the end of the `docker run` command (for example, `docker run stackstate/stackstate-cli2 version`).

## Configure the `sts` CLI

### Quick start

{% hint style="warning" %}
The most secure way to use your API token is through an environment variable. You can store the API token with a secrets manager and inject it as an environment variable into your shell.
{% endhint %}

#### Linux, macOS and Windows

1. In the StackState UI, go to **Main menu** > **CLI** and copy your API token.
2. Run the command below, where `<URL>` is the URL to your StackState instance and `<API-TOKEN>` is the API token you copied from the CLI page in the StackState UI:

   ```bash
   sts context save --name <NAME> --url <URL> --api-token <API-TOKEN>
   ```
3. The connection to your StackState instance will be tested and a configuration file stored at `~/.config/stackstate-cli/config.yaml`.

#### Docker

The Docker version of the CLI can't be configured with a config file. Specify the configuration of your StackState instance using environment variables and pass these to Docker:

* `STS_CLI_URL` - the URL to your StackState instance.
* `STS_CLI_API_TOKEN` - the API token taken from the StackState UI **Main menu** > **CLI** page.

For example:

```
docker run \
   -e STS_CLI_URL \
   -e STS_CLI_API_TOKEN \
   stackstate/stackstate-cli2 settings list --type Layer
```

### Authentication

#### API token

By default, the CLI will authenticate using the API token that you provided when the CLI configuration was saved.

#### Service tokens

You can optionally use the CLI to create one or more service tokens to authenticate with the StackState Base and Admin APIs. For example, a service token can be used to authenticate in CI (Continuous Integration) scenarios where no real user is doing the operations on the StackState instance.

To create a service token, run the command below:

```bash
sts service-token create --name <NAME> --roles <ROLE(s)> [--expiration <yyyy-MM-dd>]
```

This will create a new service token and print it. The `--expiration` parameter is optional and can be used to set the expiration date of the service token.

Once you have this, you can configure the CLI to use it:

```bash
sts context save --name <NAME> --service-token <TOKEN> --url <URL>
```

### Manage multiple contexts

The `sts` CLI supports configuration and management of different (authentication) contexts. This enables you to easily switch between an administrative and regular user, or to switch between different StackState instances. For example, you could use a different context for a test and production instance of StackState. You can list, save, delete, set and validate contexts in the `sts` CLI. Run `sts context -h` for details of the available commands and their usage.

### Configuration options

You don't need a configuration file to run the `sts` CLI. You can also configure the CLI through a combination of environment variables and flags.

If multiple types of configuration are presented to the CLI the order of processing will be:

1. Flags
2. Environment variables
3. Config file

| Environment variable    | Flag              | Description                                                                                                                                                                                                                                     |
| ----------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `STS_CLI_URL`           | `--url`           | URL to your StackState instance.                                                                                                                                                                                                                |
| `STS_CLI_API_TOKEN`     | `--api-token`     | API token to your StackState instance. The most secure way to use your API token is through an environment variable. You can store the API token with a secrets manager and inject it as an environment variable into your shell.               |
| `STS_CLI_SERVICE_TOKEN` | `--service-token` | A service token to your StackState instance. The most secure way to use your service token is through an environment variable. You can store the service token with a secrets manager and inject it as an environment variable into your shell. |
| `STS_CLI_API_PATH`      | n/a               | The path appended to the end of the URL to get the API endpoint. (Defaults to `/api`)                                                                                                                                                           |
| `STS_CLI_CONTEXT`       | `--context`       | The name of the context to use.                                                                                                                                                                                                                 |

Next to overriding specific parts of the config file, it's also possible to override the default config file location. This is done through the `--config <PATH>` flag.

## Upgrade

To upgrade to the latest version of the `sts` CLI, [run the install command again](#install-the-new-sts-cli).

You can check the version of the `sts` CLI that you are currently running with the command `sts version`.

## Uninstall

Follow the instructions below to uninstall the StackState CLI.

{% tabs %}
{% tab title="Windows" %}
{% tabs %}
{% tab title="Uninstaller" %}
Open a **Powershell** terminal and run:

```powershell
. { iwr -useb https://dl.stackstate.com/stackstate-cli/install.ps1 } | iex; uninstall
```

The `sts` CLI and all associated configuration are now removed for the current user.
{% endtab %}

{% tab title="Manual" %}
Open a **Powershell** terminal and run each step one-by-one or all at once. The `sts` CLI and all associated configuration will be removed for the current user.

1. Remove binary:

   ```powershell
   $CLI_PATH = $env:USERPROFILE+"\stackstate-cli"
   rm -R $CLI_PATH 2>1  > $null
   ```
2. Remove config:

   ```powershell
   rm -R $env:USERPROFILE+"\.config\stackstate-cli" 2>1  > $null
   ```
3. Remove the CLI from the environment path:

   ```
   $PATH = (Get-ItemProperty -Path ‘Registry::HKEY_CURRENT_USER\Environment’ -Name PATH).Path
   $i = $PATH.IndexOf(";$CLI_PATH")
   if ($i -ne -1) {
     $PATH = $PATH.Remove($i, $CLI_PATH.Length+1)
     (Set-ItemProperty -Path 'Registry::HKEY_CURRENT_USER\Environment' -Name PATH –Value $PATH)
   }
   ```

{% endtab %}
{% endtabs %}
{% endtab %}

{% tab title="macOS" %}
{% tabs %}
{% tab title="Uninstaller" %}
Open a terminal and run:

```bash
curl -o- https://dl.stackstate.com/stackstate-cli/uninstall.sh | bash
```

The `sts` CLI and all associated configuration are now removed for the current user.
{% endtab %}

{% tab title="Manual" %}
To manually uninstall the `sts` CLI, follow the steps below.

1. Open a terminal.
2. To remove the `sts` CLI, run the command:

   ```bash
   rm -r /usr/local/bin/sts
   ```
3. To remove configuration for the `sts` CLI, run the command:

   ```bash
   rm -r ~/.config/stackstate-cli
   ```

The `sts` CLI and all associated configuration are now removed for the current user.
{% endtab %}
{% endtabs %}
{% endtab %}

{% tab title="Linux" %}
{% tabs %}
{% tab title="Uninstaller" %}
Open a terminal and run:

```bash
curl -o- https://dl.stackstate.com/stackstate-cli/uninstall.sh | bash
```

The `sts` CLI and all associated configuration are now removed for the current user.
{% endtab %}

{% tab title="Manual" %}
To manually uninstall the `sts` CLI, follow the steps below.

1. Open a terminal.
2. To remove the `sts` CLI, run the command:

   ```bash
   rm -r /usr/local/bin/sts
   ```
3. To remove configuration for the `sts` CLI, run the command:

   ```bash
   rm -r ~/.config/stackstate-cli
   ```

The `sts` CLI and all associated configuration are now removed for the current user.
{% endtab %}
{% endtabs %}
{% endtab %}

{% tab title="Docker" %}
To remove the CLI image and containers run:

```bash
docker rmi -f stackstate/stackstate-cli2
```

{% endtab %}
{% endtabs %}

## Open source

The StackState `sts` CLI is open source and can be found on GitHub at:

* <https://github.com/stackvista/stackstate-cli>


# Install StackState

StackState Self-hosted


# Requirements

StackState Self-hosted

## Overview

Requirements for [StackState client (browser)](#client-browser) can be found at the bottom of the page.

## Kubernetes and OpenShift

### Supported versions

StackState can be installed on a Kubernetes or OpenShift cluster using the Helm charts provided by StackState. These Helm charts require Helm v3.x to install and are supported on:

* **Kubernetes:** 1.21 to 1.28
* **Amazon Elastic Kubernetes Service (EKS):** 1.26 to 1.28
* **Azure Kubernetes Service (AKS):** 1.27 to 1.28
* **Google Kubernetes Engine (GKE):** 1.26 to 1.28
* **OpenShift:** 4.9 to 4.14

### Resource requirements

There are different installation options available for StackState. It is possible to install StackState either in a High-Availability (HA) or single instance (non-HA) setup. The non-HA setup is recommended for testing purposes only. For production environments, it is recommended to install StackState in a HA setup. For a standard, production, deployment, the StackState Helm chart will deploy many services in a redundant setup with 3 instances of each service.

In the table below you can find the resource requirements for the different installation options. For the HA setup you can find different installation profiles depending on the size of the environment being observed.

|                     | non-HA | HA - small profile | HA - default profile |
| ------------------- | ------ | ------------------ | -------------------- |
| **CPU Requests**    | 11     | 14,5               | 16,5                 |
| **CPU Limits**      | 31,5   | 50                 | 50                   |
| **Memory Requests** | 55Gi   | 67Gi               | 87Gi                 |
| **Memory Limits**   | 55Gi   | 89Gi               | 92Gi                 |

These are just the upper and lower bounds of the resources that can be consumed by StackState in the different installation options. The actual resource usage will depend on the features used, configured resource limits and dynamic usage patterns, such as Deployment or DaemonSet scaling. For our Self-hosted customers, we recommend to start with the default requirements and monitor the resource usage of the StackState components.

{% hint style="info" %}
The minimum requirements do not include spare CPU/Memory capacity to ensure smooth application rolling updates.
{% endhint %}

For installation of StackState please follow the installation instructions provided below:

* [Kubernetes](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/kubernetes_install)
* [OpenShift](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/openshift_install)
* [Non-high availability setup](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/non_high_availability_setup)
* [Small profile setup](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/small_profile_setup)

### Storage

StackState uses persistent volume claims for the services that need to store data. The default storage class for the cluster will be used for all services unless this is overridden by values specified on the command line or in a `values.yaml` file. All services come with a pre-configured volume size that should be good to get you started, but can be customized later using variables as required.

For our different installation profiles, the following are the defaulted storage requirements:

|                         | non-HA | HA - small profile | HA - default profile |
| ----------------------- | ------ | ------------------ | -------------------- |
| **Storage requirement** | 950GB  | 2TB                | 2TB                  |

For more details on the defaults used, see the page [Configure storage](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/storage).

### Ingress

By default, the StackState Helm chart will deploy a router pod and service. This service's port `8080` is the only entry point that needs to be exposed via Ingress. You can access StackState without configuring Ingress by forwarding this port:

```
kubectl port-forward service/<helm-release-name>-stackstate-k8s-router 8080:8080 --namespace stackstate
```

When configuring Ingress, make sure to allow for large request body sizes (50MB) that may be sent occasionally by data sources like the StackState Agent or the AWS integration.

For more details on configuring Ingress, have a look at the page [Configure Ingress docs](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/ingress).

### Namespace resource limits

It isn't recommended to set a ResourceQuota as this can interfere with resource requests. The resources required by StackState will vary according to the features used, configured resource limits and dynamic usage patterns, such as Deployment or DaemonSet scaling.

If it's necessary to set a ResourceQuota for your implementation, the namespace resource limit should be set to match the node [sizing requirements](#resource-requirements).

## Client (browser)

To use the StackState GUI, you must use one of the following web browsers:

* Chrome
* Firefox


# Kubernetes / OpenShift

StackState Self-hosted


# Kubernetes install

StackState Self-hosted

## Before you start

{% hint style="info" %}
Extra notes for installing on:

* **Kubernetes clusters with limited permissions**: Read the [required permissions](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/required_permissions).
* **OpenShift**: Refer to the [OpenShift installation instructions](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/openshift_install).
  {% endhint %}

Before you start the installation of StackState:

* Check the [requirements](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/requirements) to make sure that your Kubernetes environment fits the setup that you will use (recommended, minimal or non- high availability).
* Check that you have the [required permissions](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/required_permissions).
* Request access credentials to pull the StackState Docker images from [StackState support](https://support.stackstate.com/).
* Add the StackState helm repository to the local helm client:

```
helm repo add stackstate https://helm.stackstate.io
helm repo update
```

## Install StackState

{% hint style="info" %}
For environments without internet access, also known as air-gapped environments, first follow [these extra instructions](https://archivedocs.stackstate.com/self-hosted-setup/no_internet/stackstate_installation).

Also make sure to follow the air-gapped instalaltion instructions whenever those are present for a step.
{% endhint %}

1. [Create the namespace where StackState will be installed](#create-namespace)
2. [Generate the `values.yaml` file](#generate-values.yaml)
3. [Deploy StackState with Helm](#deploy-stackstate-with-helm)
4. [Access the StackState UI](#access-the-stackstate-ui)

### Create namespace

Start by creating the namespace where you want to install StackState and deploy the secret in that namespace. In our walkthrough we will use the namespace `stackstate`:

```
kubectl create namespace stackstate
```

### Generate `values.yaml`

The `values.yaml` file is required to deploy StackState with Helm. It contains your StackState license key, StackState Receiver API key and other important information.

{% hint style="info" %}
**Before you continue:** Make sure you have the latest version of the Helm charts with `helm repo update`.
{% endhint %}

The StackState `values.yaml` file can be generated by running a separate Helm Chart, the `stackstate/stackstate-values` chart. A sample command line is:

```
> helm template \
  --set license='<your license>' \
  --set baseUrl='<stackstate-base-url>' \
  --set pullSecret.username='<your-registry-username>' \
  --set pullSecret.password='<your-registry-password>' \
  sts-values \
  stackstate/stackstate-values > values.yaml
```

This command will generate a values.yaml file which contains the necessary configuration for installing the StackState Helm Chart.

{% hint style="info" %}
The StackState administrator passwords will be autogenerated by the above command and are output as comments in the generated `values.yaml` file. The actual values contain the `bcrypt` hashes of those passwords so that they're securely stored in the Helm release in the cluster.
{% endhint %}

The values that can be passed to this chart are:

| Configuration             | Value                 | Description                                                                                                                                                                                                                                                                                                                        |
| ------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Receiver API Key          | `receiverApiKey`      | The API key used by StackState to receive data from agents. This is a secret key that should be kept private. If you omit this, a random key will be generated for you.                                                                                                                                                            |
| Base URL                  | `baseUrl`             | The `<STACKSTATE_BASE_URL>`. The external URL for StackState that users and agents will use to connect. For example `https://stackstate.internal`. If you haven't decided on an Ingress configuration yet, use `http://localhost:8080`. This can be updated later in the generated file.                                           |
| Username and password\*\* | `-u` `-p`             | The username and password used by StackState to pull images from quay.io/stackstate repositories. For air-gapped environments these need to be the username and password for the local docker registry.                                                                                                                            |
| License key               | `license`             | The StackState license key.                                                                                                                                                                                                                                                                                                        |
| Admin API password        | `adminApiPassword`    | The password for the admin API. Note that this API contains system maintenance functionality and should only be accessible by the maintainers of the StackState installation. If you omit this, a random password will be generated for you. If you do pass this value and it's not bcrypt hashed, the chart will hash it for you. |
| Default password          | `adminPassword`       | The password for the default user (`admin`) to access StackState's UI. If you omit this, a random password will be generated for you. If you do pass this value and it's not bcrypt hashed, the chart will hash it for you.                                                                                                        |
| Image Registry            | `imageRegistry`       | The registry where the StackState images are hosted. If not provided, the default value will be 'quay.io'                                                                                                                                                                                                                          |
| Pull Secret Username      | `pullSecret.username` | The username used to pull images from the Docker registry where the StackState images are hosted.                                                                                                                                                                                                                                  |
| Pull Secret Password      | `pullSecret.password` | The password used to pull images from the Docker registry where the StackState images are hosted.                                                                                                                                                                                                                                  |

{% hint style="info" %}
Store the generated `values.yaml` file somewhere safe. You can reuse this file for upgrades, which will save time and (more importantly) will ensure that StackState continues to use the same API key. This is desirable as it means Agents and other data providers for StackState won't need to be updated.
{% endhint %}

### Deploy StackState with Helm

The recommended deployment of StackState is a production ready, high availability setup with many services running redundantly. If required, it's also possible to run StackState in a non-redundant setup, where each service has only a single replica. This setup is only recommended for a test environment.

For air-gapped environments follow the instructions for the air-gapped installations.

{% tabs %}
{% tab title="High availability setup" %}
To deploy StackState in a high availability setup on Kubernetes:

1. Before you deploy:
   * [Create the namespace where StackState will be installed](#create-namespace)
   * [Generate `values.yaml`](#generate-values.yaml)
2. **(Optionally)** [Create a `small_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/small_profile_setup) if you want to deploy a small profile setup. Add the `--values small_values.yaml` flag to the command below.
3. Deploy the latest StackState version to the `stackstate` namespace with the following command:

```
helm upgrade \
  --install \
  --namespace stackstate \
  --values values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}

{% tab title="Non-high availability setup" %}
To deploy StackState in a non-high availability setup on Kubernetes:

1. Before you deploy:
   * [Create the namespace where StackState will be installed](#create-namespace)
   * [Generate `values.yaml`](#generate-values.yaml)
   * [Create `nonha_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/non_high_availability_setup)
2. Deploy the latest StackState version to the `stackstate` namespace with the following command:

```bash
helm upgrade \
  --install \
  --namespace stackstate \
  --values values.yaml \
  --values nonha_values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}

{% tab title="Air-gapped, high availability setup" %}
To deploy StackState in a air-gapped, high availability setup on Kubernetes:

1. Before you deploy:
   * [Follow these extra instructions for air-gapped installations](https://archivedocs.stackstate.com/self-hosted-setup/no_internet/stackstate_installation).
   * [Create the namespace where StackState will be installed](#create-namespace)
   * [Generate `values.yaml`](#generate-values.yaml)
2. **(Optionally)** [Create a `small_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/small_profile_setup) if you want to deploy a small profile setup. Add the `--values small_values.yaml` flag to the command below.
3. Deploy the latest StackState version to the `stackstate` namespace with the following command:

{% hint style="info" %}
If you've created a `small_values.yaml` file, add `--values small_values.yaml` to the command below.
{% endhint %}

```
helm upgrade \
  --install \
  --namespace stackstate \
  --values local-docker-registry.yaml \
  --values values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}

{% tab title="Air-gapped, non-high availability setup" %}
To deploy StackState in a air-gapped, non-high availability setup on Kubernetes:

1. Before you deploy:
   * [Follow these extra instructions for air-gapped installations](https://archivedocs.stackstate.com/self-hosted-setup/no_internet/stackstate_installation).
   * [Create the namespace where StackState will be installed](#create-namespace)
   * [Generate `values.yaml`](#generate-values.yaml)
   * [Create `nonha_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/non_high_availability_setup)
2. Deploy the latest StackState version to the `stackstate` namespace with the following command:

```bash
helm upgrade \
  --install \
  --namespace stackstate \
  --values local-docker-registry.yaml \
  --values values.yaml \
  --values nonha_values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}
{% endtabs %}

After the install, the StackState release should be listed in the StackState namespace and all pods should be running:

```
# Check the release is listed
helm list --namespace stackstate

# Check pods are running
# It may take some time for all pods to be installed or available
kubectl get pods --namespace stackstate
```

### Access the StackState UI

After StackState has been deployed you can check if all pods are up and running:

```
kubectl get pods --namespace stackstate
```

When all pods are up, you can enable a port-forward:

```
kubectl port-forward service/<helm-release-name>-stackstate-k8s-router 8080:8080 --namespace stackstate
```

StackState will now be available in your browser at `https://localhost:8080`. Log in with the username `admin` and the default password provided in the `values.yaml` file.

Next steps are

* [Expose StackState outside of the cluster](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/ingress)
* [Start monitoring your Kubernetes clusters](https://archivedocs.stackstate.com/get-started/k8s-quick-start-guide)
* Give your [co-workers access](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication).


# OpenShift install

StackState Self-hosted

## Before you start

{% hint style="info" %}
Extra notes for installing on:

* **OpenShift clusters with limited permissions**: Read the [required permissions](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/required_permissions).
* **Kubernetes**: Refer to the [Kubernetes installation instructions](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/kubernetes_install).
  {% endhint %}

Before you start the installation of StackState:

* Check that your OpenShift environment meets the [requirements](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/requirements)
* Request access credentials to pull the StackState Docker images from [StackState support](https://support.stackstate.com/).
* Ensure you have the OpenShift command line tools installed (`oc`)
* Add the StackState helm repository to the local helm client:

```
helm repo add stackstate https://helm.stackstate.io
helm repo update
```

## Install StackState

{% hint style="info" %}
For environments without internet access, also known as air-gapped environments, first follow [these extra instructions](https://archivedocs.stackstate.com/self-hosted-setup/no_internet/stackstate_installation).

Also make sure to follow the air-gapped instalaltion instructions whenever those are present for a step.
{% endhint %}

1. [Create the project where StackState will be installed](#create-project)
2. [Generate the `values.yaml` file](#generate-values.yaml)
3. [Create the `openshift-values.yaml` file](#create-openshift-values.yaml)
4. [Deploy StackState with Helm](#deploy-stackstate-with-helm)
5. [Access the StackState UI](#access-the-stackstate-ui)
6. [Manually create `SecurityContextConfiguration` objects](#manually-create-securitycontextconfiguration-objects)

### Create project

Start by creating the project where you want to install StackState. In our walkthrough we will use the namespace `stackstate`:

```
oc new-project stackstate
```

{% hint style="info" %}
The project name is used in `helm` and `kubectl` commands as the namespace name in the `--namespace` flag
{% endhint %}

### Generate `values.yaml`

The `values.yaml` file is required to deploy StackState with Helm. It contains your StackState license key, StackState Receiver API key and other important information.

{% hint style="info" %}
**Before you continue:** Make sure you have the latest version of the Helm charts with `helm repo update`.
{% endhint %}

The StackState `values.yaml` file can be generated by running a separate Helm Chart, the `stackstate/stackstate-values` chart. A sample command line is:

```
> helm template \
  --set license='<your license>' \
  --set baseUrl='<stackstate-base-url>' \
  --set pullSecret.username='<your-registry-username>' \
  --set pullSecret.password='<your-registry-password>' \
  sts-values \
  stackstate/stackstate-values > values.yaml
```

This command will generate a values.yaml file which contains the necessary configuration for installing the StackState Helm Chart.

{% hint style="info" %}
The StackState administrator passwords will be autogenerated by the above command and are output as comments in the generated `values.yaml` file. The actual values contain the `bcrypt` hashes of those passwords so that they're securely stored in the Helm release in the cluster.
{% endhint %}

The values that can be passed to this chart are:

| Configuration             | Value                 | Description                                                                                                                                                                                                                                                                                                                        |
| ------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Receiver API Key          | `receiverApiKey`      | The API key used by StackState to receive data from agents. This is a secret key that should be kept private. If you omit this, a random key will be generated for you.                                                                                                                                                            |
| Base URL                  | `baseUrl`             | The `<STACKSTATE_BASE_URL>`. The external URL for StackState that users and agents will use to connect. For example `https://stackstate.internal`. If you haven't decided on an Ingress configuration yet, use `http://localhost:8080`. This can be updated later in the generated file.                                           |
| Username and password\*\* | `-u` `-p`             | The username and password used by StackState to pull images from quay.io/stackstate repositories. For air-gapped environments these need to be the username and password for the local docker registry.                                                                                                                            |
| License key               | `license`             | The StackState license key.                                                                                                                                                                                                                                                                                                        |
| Admin API password        | `adminApiPassword`    | The password for the admin API. Note that this API contains system maintenance functionality and should only be accessible by the maintainers of the StackState installation. If you omit this, a random password will be generated for you. If you do pass this value and it's not bcrypt hashed, the chart will hash it for you. |
| Default password          | `adminPassword`       | The password for the default user (`admin`) to access StackState's UI. If you omit this, a random password will be generated for you. If you do pass this value and it's not bcrypt hashed, the chart will hash it for you.                                                                                                        |
| Image Registry            | `imageRegistry`       | The registry where the StackState images are hosted. If not provided, the default value will be 'quay.io'                                                                                                                                                                                                                          |
| Pull Secret Username      | `pullSecret.username` | The username used to pull images from the Docker registry where the StackState images are hosted.                                                                                                                                                                                                                                  |
| Pull Secret Password      | `pullSecret.password` | The password used to pull images from the Docker registry where the StackState images are hosted.                                                                                                                                                                                                                                  |

{% hint style="info" %}
Store the generated `values.yaml` file somewhere safe. You can reuse this file for upgrades, which will save time and (more importantly) will ensure that StackState continues to use the same API key. This is desirable as it means Agents and other data providers for StackState won't need to be updated.
{% endhint %}

### Create `openshift-values.yaml`

Because OpenShift has stricter security model than plain Kubernetes, all of the standard security contexts in the deployment need to be disabled.

Create a Helm values file `openshift-values.yaml` with the following content and store it next to the generated `values.yaml` file. This contains the values that are needed for an OpenShift deployment.

```yaml
elasticsearch:
  prometheus-elasticsearch-exporter:
    podSecurityContext: ""
  sysctlInitContainer:
    enabled: false
scc:
  enabled: true
```

### Deploy StackState with Helm

The recommended deployment of StackState is a production ready, high availability setup with many services running redundantly. If required, it's also possible to run StackState in a non-redundant setup, where each service has only a single replica. This setup is only recommended for a test environment.

For air-gapped environments follow the instructions for the air-gapped installations.

{% tabs %}
{% tab title="High availability setup" %}
To deploy StackState in a high availability setup on OpenShift:

1. Before you deploy:
   * [Create the project where StackState will be installed](#create-project)
   * [Generate `values.yaml`](#generate-values.yaml)
   * [Create `openshift-values.yaml`](#create-openshift-values.yaml)
2. **(Optionally)** [Create a `small_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/small_profile_setup) if you want to deploy a small profile setup. Add the `--values small_values.yaml` flag to the command below.
3. Deploy the latest StackState version to the `stackstate` namespace with the following command:

```
helm upgrade \
  --install \
  --namespace stackstate \
  --values values.yaml \
  --values openshift-values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}

{% tab title="Non-high availability setup" %}
To deploy StackState in a non-high availability setup on OpenShift:

1. Before you deploy:
   * [Create the project where StackState will be installed](#create-project)
   * [Generate `values.yaml`](#generate-values.yaml)
   * [Create `openshift-values.yaml`](#create-openshift-values.yaml)
   * [Create `nonha_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/non_high_availability_setup)
2. Deploy the latest StackState version to the `stackstate` namespace with the following command:

```bash
helm upgrade \
  --install \
  --namespace stackstate \
  --values local-docker-registry.yaml \
  --values values.yaml \
  --values nonha_values.yaml \
  --values openshift-values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}

{% tab title="Air-gapped, high availability setup" %}
To deploy StackState in a high availability setup on OpenShift:

1. Before you deploy:
   * [Create the project where StackState will be installed](#create-project)
   * [Generate `values.yaml`](#generate-values.yaml)
   * [Create `openshift-values.yaml`](#create-openshift-values.yaml)
2. **(Optionally)** [Create a `small_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/small_profile_setup) if you want to deploy a small profile setup. Add the `--values small_values.yaml` flag to the command below.
3. Deploy the latest StackState version to the `stackstate` namespace with the following command:

```
helm upgrade \
  --install \
  --namespace stackstate \
  --values local-docker-registry.yaml \
  --values values.yaml \
  --values openshift-values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}

{% tab title="Air-gapped, non-high availability setup" %}
To deploy StackState in a non-high availability setup on OpenShift:

1. Before you deploy:
   * [Create the project where StackState will be installed](#create-project)
   * [Generate `values.yaml`](#generate-values.yaml)
   * [Create `openshift-values.yaml`](#create-openshift-values.yaml)
   * [Create `nonha_values.yaml`](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/non_high_availability_setup)
2. Deploy the latest StackState version to the `stackstate` namespace with the following command:

```bash
helm upgrade \
  --install \
  --namespace stackstate \
  --values values.yaml \
  --values nonha_values.yaml \
  --values openshift-values.yaml \
stackstate \
stackstate/stackstate-k8s
```

{% endtab %}
{% endtabs %}

After the install, the StackState release should be listed in the StackState namespace and all pods should be running:

```
# Check the release is listed
helm list --namespace stackstate

# Check pods are running
# It may take some time for all pods to be installed or available
kubectl get pods --namespace stackstate
```

### Access the StackState UI

After StackState has been deployed, you can check if all pods are up and running:

```
kubectl get pods --namespace stackstate
```

When all pods are up, you can enable a port-forward:

```
kubectl port-forward service/stackstate-router 8080:8080 --namespace stackstate
```

StackState will now be available in your browser at `https://localhost:8080`. Log in with the username `admin` and the default password provided in the `values.yaml` file.

Next steps are

* [Expose StackState outside of the cluster](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/ingress)
* [Start monitoring your Kubernetes clusters](https://archivedocs.stackstate.com/get-started/k8s-quick-start-guide)
* Give your [co-workers access](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication).

## Manually create `SecurityContextConfiguration` objects

If you can't use an administrator account to install StackState on OpenShift, ask your administrator to apply the below `SecurityContextConfiguration` objects.

```yaml
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: {{ template "common.fullname.short" . }}-{{ .Release.Namespace }}
  labels:
    {{- include "common.labels.standard" . | nindent 4 }}
  annotations:
    helm.sh/hook: pre-install
    stackstate.io/note: "Ignored by helm uninstall, has to be deleted manually"
fsGroup:
  type: RunAsAny
groups:
- system:serviceaccounts:{{ .Release.Namespace }}
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: MustRunAs
supplementalGroups:
  type: RunAsAny
volumes:
- configMap
- downwardAPI
- emptyDir
- ephemeral
- persistentVolumeClaim
- projected
- secret
allowHostDirVolumePlugin: false
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: true
allowPrivilegedContainer: false
readOnlyRootFilesystem: false
```

## See also

* [Create a `nonha_values.yaml` file](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/non_high_availability_setup)
* [Create a `small_values.yaml` file](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/small_profile_setup)
* For other configuration and management options, refer to the Kubernetes documentation - [manage a StackState Kubernetes installation](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/kubernetes_install)


# Required Permissions

StackState Self-hosted

## Overview

All of StackState's own components can run without any extra permissions. However, to install StackState successfully, you need some additional privileges, or ensure that the requirements described in this page are met.

## Service-to-service authentication and authorization

To allow communication between StackState services StackState uses Kubernetes service accounts. To be able to verify their validity and roles the helm chart creates a `ClusterRole` and a `ClusterRoleBinding` resources. Creating these cluster-wide resources is often prohibited for users that aren't a Kubernetes/OpenShift administrator. For that case the creation can be disabled and instead the roles and role bindings need to be [created manually](#manually-create-cluster-wide-resources) by your cluster admin.

### Disable automatic creation of cluster-wide resources

The automatic creation of cluster-wide resources during installation of StackState can be disabled by adding the following section to the `values.yaml` file used to install StackState:

{% tabs %}
{% tab title="values.yaml" %}

```yaml
cluster-role:
  enabled: false
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
If the creation of the cluster role and cluster role binding has been disabled please make sure to follow the instructions below to manually create them using the [instructions below](#manually-create-cluster-wide-resources).
{% endhint %}

### Manually create cluster-wide resources

If you need to manually create the cluster-wide resources, ask your Kubernetes/OpenShift administrator to create the 3 resources below in the clsuter.

{% hint style="info" %}
Verify that you specify the correct service account and namespace for the bound `ServiceAccount` for both of the `ClusterRoleBinding` resources. The example assumes the `stackstate` namespace is used, if some other namespace is used changed the namespace in the examples. Also the service accounts referenced need to be changed to `<namespace>-stackstate-k8s-api`.
{% endhint %}

{% tabs %}
{% tab title="clusterrole-authorization.yaml" %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: stackstate-authorization
rules:
- apiGroups:
  - rbac.authorization.k8s.io
  resources:
  - rolebindings
  verbs:
  - list
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="clusterrolebinding-authentication.yaml" %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: stackstate-authentication
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: stackstate-stackstate-k8s-api
  namespace: stackstate
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="clusterrolebinding-authorization.yaml" %}

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: stackstate-authorization
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: stackstate-authorization
subjects:
- kind: ServiceAccount
  name: stackstate-stackstate-k8s-api
  namespace: stackstate
```

{% endtab %}
{% endtabs %}

## Elasticsearch

StackState uses Elasticsearch to store its indices. There are some additional requirements for the nodes that Elasticsearch runs on.

As the `vm.max_map_count` Linux system setting is usually lower than required for Elasticsearch to start, an init container is used that runs in privileged mode and as the root user. The init container is enabled by default to allow the `vm.max_map_count` system setting to be changed.

### Disable the privileged Elasticsearch init container

In case you or your Kubernetes/OpenShift administrators don't want the privileged Elasticsearch init container to be enabled by default, you can disable this behavior in the file `values.yaml` used to install StackState:

{% tabs %}
{% tab title="values.yaml" %}

```yaml
elasticsearch:
  sysctlInitContainer:
    enabled: false
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
If this is disabled, you will need to ensure that the `vm.max_map_count` setting is changed from its common default value of `65530` to `262144`. If this isn't done, Elasticsearch will fail to start up and its pods will be in a restart loop.
{% endhint %}

To inspect the current `vm.max_map_count` setting, run the following command. Note that it runs a privileged pod:

```
kubectl run -i --tty sysctl-check-max-map-count --privileged=true  --image=busybox --restart=Never --rm=true -- sysctl vm.max_map_count
```

If the current `vm.max_map_count` setting isn't at least `262144`, it will need to be increased in a different way or Elasticsearch will fail to start up and its pods will be in a restart loop. The logs will contain an error message like this:

```
bootstrap checks failed
max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

### Increase Linux system settings for Elasticsearch

Depending on what your Kubernetes/OpenShift administrators prefer, the `vm.max_map_count` can be set to a higher default on all nodes by either changing the default node configuration (for example via init scripts) or by having a DaemonSet do this right after node startup. The former is very dependent on your clsuter setup, so there are no general solutions there.

Below is an example that can be used as a starting point for a DaemonSet to change the `vm.max_map_count` setting:

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: set-vm-max-map-count
  labels:
    k8s-app: set-vm-max-map-count
spec:
  selector:
    matchLabels:
      name: set-vm-max-map-count
  template:
    metadata:
      labels:
        name: set-vm-max-map-count
    spec:
      # Make sure the setting always gets changed as soon as possible:
      tolerations:
      - effect: NoSchedule
        operator: Exists
      - effect: NoExecute
        key: node.kubernetes.io/not-ready
        operator: Exists
      # Optional node selector (assumes nodes for Elasticsearch are labeled `elasticsearch:yes`
      # nodeSelector:
      #  elasticsearch: yes
      initContainers:
        - name: set-vm-max-map-count
          image: busybox
          securityContext:
            runAsUser: 0
            privileged: true
          command: ["sysctl", "-w", "vm.max_map_count=262144"]
          resources:
            limits:
              cpu: 100m
              memory: 100Mi
            requests:
              cpu: 100m
              memory: 100Mi
      # A pause container is needed to prevent a restart loop of the pods in the daemonset
      # See also this Kubernetes issue https://github.com/kubernetes/kubernetes/issues/36601
      containers:
        - name: pause
          image: google/pause
          resources:
            limits:
              cpu: 50m
              memory: 50Mi
            requests:
              cpu: 50m
              memory: 50Mi
```

To limit the number of nodes that this is applied to, nodes can be labeled. NodeSelectors on both this DaemonSet, as shown in the example, and the Elasticsearch deployment can then be set to run only on nodes with the specific label. For Elasticsearch, the node selector can be specified via the values:

```yaml
elasticsearch:
  nodeSelector:
    elasticsearch: yes
  sysctlInitContainer:
    enabled: false
```

## See also

* [Install StackState on Kubernetes](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/kubernetes_install)
* [Install StackState on OpenShift](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/openshift_install)


# Non-high availability setup

StackState Self-hosted

## Overview

The recommended Kubernetes/OpenShift deployment of StackState is a production ready setup with many services running redundantly. If required, it's also possible to run StackState in a non-redundant setup, where each service has only a single replica.

{% hint style="info" %}
The non-high availability setup is only suitable for situations that don't require high availability.
{% endhint %}

## Create `nonha_values.yaml`

To deploy StackState in a non-high availability setup, you will need a `nonha_values.yaml` file. Follow the instructions below to create this file and use it for deployment of StackState.

1. Create a Helm values file `nonha_values.yaml` with the following content and store it next to the generated `values.yaml` file:

```yaml
# This files defines additional Helm values to run StackState on a 
# non-high availability production setup. Use this file in combination
# with a regular values.yaml file that contains your API key, etc.
elasticsearch:
  minimumMasterNodes: 1
  replicas: 1

hbase:
  hbase:
    master:
      replicaCount: 1
    regionserver:
      replicaCount: 1
  hdfs:
    datanode:
      replicaCount: 1
    secondarynamenode:
      enabled: false
  tephra:
    replicaCount: 1

kafka:
  replicaCount: 1
  defaultReplicationFactor: 1
  offsetsTopicReplicationFactor: 1
  transactionStateLogReplicationFactor: 1
stackstate:
  components:
    ui:
      replicaCount: 1
victoria-metrics-1:
  enabled: false
zookeeper:
  replicaCount: 1
clickhouse:
  replicaCount: 1
```

2. Continue with the instructions to deploy StackState with Helm:
   * [Deploy on Kubernetes](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_install#deploy-stackstate-with-helm).
   * [Deploy on OpenShift](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/openshift_install#deploy-stackstate-with-helm).


# Small profile setup

StackState Self-hosted

## Overview

The recommended Kubernetes/OpenShift deployment of StackState is a production ready setup suited for observing large clusters. If the setup is not expected to be big, it can be tuned down to consume less resources. This is called the small profile setup.

{% hint style="info" %}
The small profile setup is only suitable for situations that observe up to roughly 100 nodes.
{% endhint %}

## Create `small_values.yaml`

To deploy StackState in a small profile setup, you will need a `small_values.yaml` file. Follow the instructions below to create this file and use it for deployment of StackState.

1. Create a Helm values file `small_values.yaml` with the following content and store it next to the generated `values.yaml` file:

```yaml
# This files defines additional Helm values to run StackState on a
# small profile production setup. Use this file in combination
# with a regular values.yaml file that contains your API key, etc.
elasticsearch:
  esJavaOpts: "-Xmx3g -Xms3g -Des.allow_insecure_settings=true -Dlog4j2.formatMsgNoLookups=true"
  esConfig:
    elasticsearch.yml: |
      cluster.routing.allocation.disk.watermark.low: "80%"
      cluster.routing.allocation.disk.watermark.high: "85%"
  resources:
    requests:
      cpu: "250m"
      memory: "4Gi"
hbase:
  hbase:
    master:
      resources:
        requests:
          memory: "512Mi"
          cpu: "50m"
    regionserver:
      resources:
        requests:
          memory: "1Gi"
          cpu: "500m"
  hdfs:
    datanode:
      resources:
        requests:
          memory: "2Gi"
          cpu: "100m"
    namenode:
      resources:
        requests:
          memory: "512Mi"
          cpu: "50m"
kafka:
  resources:
    requests:
      cpu: "500m"
      memory: "1536Mi"
  persistence:
    size: 400Gi
stackstate:
  components:
    api:
      resources:
        requests:
          memory: "2Gi"
          cpu: "400m"
    state:
      resources:
        requests:
          memory: "1536Mi"
          cpu: "1200m"
        limits:
          cpu: "1200m"
    kafka2prom:
      resources:
        requests:
          cpu: "300m"
          memory: 2200Mi
        limits:
          memory: 2200Mi
    viewHealth:
      resources:
        requests:
          memory: "2Gi"
          cpu: "1000m"
    checks:
      resources:
        requests:
          memory: "3Gi"
          cpu: "500m"
    correlate:
      resources:
        requests:
          memory: "2600Mi"
          cpu: "1000m"
        limits:
          memory: "2600Mi"
      replicaCount: 2
      extraEnv:
        open:
          CONFIG_FORCE_stackstate_correlate_correlateConnections_extra_maxBufferSize: 1000M
    healthSync:
      resources:
        requests:
          memory: "2000Mi"
          cpu: "250m"
        limits:
          memory: "2000Mi"
    initializer:
      resources:
        requests:
          memory: "512Mi"
          cpu: "250m"
    e2es:
      resources:
        requests:
          memory: "768Mi"
          cpu: "250m"
    receiver:
      resources:
        requests:
          memory: "3Gi"
          cpu: "1000m"
    sync:
      resources:
        requests:
          memory: "3Gi"
          cpu: "500m"
    slicing:
      resources:
        requests:
          memory: "1536Mi"
          cpu: "250m"
    problemProducer:
      resources:
        requests:
          memory: "1536Mi"
          cpu: "250m"
minio:
  resources:
    requests:
      cpu: 250m
      memory: 256Mi
    limits:
      memory: 256Mi
kafkaup-operator:
  resources:
    requests:
      cpu: 10m
victoria-metrics-0:
  server:
    persistentVolume:
      size: 60Gi
victoria-metrics-1:
  server:
    persistentVolume:
      size: 60Gi
```

2. Continue with the instructions to deploy StackState with Helm:
   * [Deploy on Kubernetes](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_install#deploy-stackstate-with-helm).
   * [Deploy on OpenShift](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/openshift_install#deploy-stackstate-with-helm).


# Override default configuration

StackState Self-hosted

A number of values can be set in the [StackState Helm chart](https://github.com/StackVista/helm-charts/tree/stackstate-6.x/stable/stackstate-k8s). For example, it's possible to customize the `tolerations` and `nodeSelectors` for each of the components. You can also add customized configuration and include environment variables

## Custom configuration for StackState `api`

For the StackState `api` service, custom configuration can be dropped directly into the Helm chart. This is the advised way to override the default configuration that StackState ships with and is especially convenient for customizing authentication. Configuration set in this way will be available to the StackState configuration file in [HOCON](https://github.com/lightbend/config/blob/master/HOCON.md) format.

For example, you can set a custom "forgot password link" for the StackState login page:

{% tabs %}
{% tab title="values.yaml" %}

```
stackstate:
  components:
    api:
      config: |
        stackstate.api.authentication.forgotPasswordLink =
        "https://www.stackstate.com/forgotPassword.html"
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
Note that custom configuration set here will be overridden by [environment variables](#environment-variables).
{% endhint %}

## Environment variables

The configuration for all of the StackState services (`receiver`, `k2es-*`, `correlation` and `api`) can be customized using environment variables. Environment variables are specified in the `values.yaml` file and can be either `secret` (such as passwords) or `open` (for normal values). To convert a configuration item to an environment variable name, replace `.` with `_` and add the prefix `CONFIG_FORCE_`.

```
# configuration item
stackstate.api.authentication.forgotPasswordLink

# environment variable name
CONFIG_FORCE_stackstate_api_authentication_forgotPasswordLink
```

For example, you can set a custom "forgot password link" for the StackState login page:

{% tabs %}
{% tab title="values.yaml" %}

```
stackstate:
  components:
    api:
      extraEnv:
        # The value for open env vars is defined on the deployment
        open:
          CONFIG_FORCE_stackstate_api_authentication_forgotPasswordLink: "https://www.stackstate.com/forgotPassword.html"
        # The value for secret env vars is defined in a secret and referenced from the deployment
        secret:
          CONFIG_FORCE_stackstate_authentication_adminPassword: "d8e8fca2dc0f896fd7cb4cb0031ba249"
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
For the StackState `api` service, environment variables will override [custom configuration set using `config`](#custom-configuration-for-stackstate-api).
{% endhint %}

* Full details on the naming of all the different services can be found in the [StackState Helm chart readme](https://github.com/StackVista/helm-charts/tree/stackstate-6.x/stable/stackstate-k8s).
* Find more details on [customizing authentication](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication).


# Configure storage

StackState Self-hosted

## Storage defaults

StackState doesn't specify a specific storage class on its PVC's (persistent volume claims) by default, for cloud providers like EKS and AKS this means the default storage class will be used.

The defaults for those storage classes are typically to delete the PV (persistent volume) when the PVC is deleted. However, even when running `helm delete` to remove a stackstate release the PVC's will remain present within the namespace and will be reused if a `helm install` is run in the same namespace with the same release name.

To remove the PVC's either remove them manually with `kubectl delete pvc` or delete the entire namespace.

## Customize storage

You can customize the `storageClass` and `size` settings for different volumes in the Helm chart. These example values files show how to change the storage class or the volume size. These can be merged to change both at the same time.

{% tabs %}
{% tab title="Changing storage class" %}

```yaml
global:
  # The storage class for most of the persistent volumes
  storageClass: "standard"

elasticsearch:
  volumeClaimTemplate:
    storageClassName: "standard"

victoria-metrics-0:
  server:
    persistentVolume:
      storageClass: "standard"
victoria-metrics-1:
  server:
    persistentVolume:
      storageClass: "standard"
```

{% endtab %}

{% tab title="Changing volume size" %}

```yaml
elasticsearch:
  volumeClaimTemplate:
    resources:
      requests:
        # size of volume for each Elasticsearch pod
        storage: 250Gi

hbase:
  hdfs:
    datanode:
      persistence:
        # size of volume for HDFS data nodes
        size: 250Gi

    namenode:
      persistence:
        # size of volume for HDFS name nodes
        size: 20Gi


kafka:
  persistence:
    # size of persistent volume for each Kafka pod
    size: 50Gi


zookeeper:
  persistence:
    # size of persistent volume for each Zookeeper pod
    size: 50Gi

victoria-metrics-0:
  server:
    persistentVolume:
      size: 250Gi
victoria-metrics-1:
  server:
    persistentVolume:
      size: 250Gi

stackstate:
  components:
    checks:
      tmpToPVC:
        volumeSize: 2Gi
    healthSync:
      tmpToPVC:
        volumeSize: 2Gi
    state:
      tmpToPVC:
        volumeSize: 2Gi
    sync:
      tmpToPVC:
        volumeSize: 2Gi
    vmagent:
      persistence:
        size: 10Gi
```

{% endtab %}
{% endtabs %}


# Exposing StackState outside of the cluster

StackState Self-hosted

## Overview

StackState can be exposed with a Kubernetes Ingress resource. The example on this page shows how to configure an nginx-ingress controller using [Helm for StackState running on Kubernetes](#configure-ingress-via-the-stackstate-helm-chart). This page also documents which service/port combination to expose when using a different method of configuring ingress traffic.

When observing the cluster that also hosts StackState, the agent traffic can be kept entirely within the cluster itself by [changing the agent configuration](#agents-in-the-same-cluster) during agent installation.

## Configure ingress via the StackState Helm chart

The StackState Helm chart exposes an `ingress` section in its values. This is disabled by default. The example below shows how to use the Helm chart to configure an nginx-ingress controller with TLS encryption enabled. Note that setting up the controller itself and the certificates is beyond the scope of this document.

To configure the ingress for StackState, create a file `ingress_values.yaml` with contents like below. Replace `MY_DOMAIN` with your own domain (that's linked with your ingress controller) and set the correct name for the `tls-secret`. Consult the documentation of your ingress controller for the correct annotations to set. All fields below are optional, for example, if no TLS will be used, omit that section but be aware that StackState also doesn't encrypt the traffic.

```
ingress:
  enabled: true
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "50m"
  hosts:
    - host: stackstate.MY_DOMAIN
  tls:
    - hosts:
        - stackstate.MY_DOMAIN
      secretName: tls-secret
```

The thing that stands out in this file is the Nginx annotation to increase the allowed `proxy-body-size` to `50m` (larger than any expected request). By default, Nginx allows body sizes of maximum `1m`. StackState Agents and other data providers can sometimes send much larger requests. For this reason, you should make sure that the allowed body size is large enough, regardless of whether you are using Nginx or another ingress controller. Make sure to update the `baseUrl` in the values file generated during initial installation, it will be used by StackState to generate convenient installation instructions for the agent.

Include the `ingress_values.yaml` file when you run the `helm upgrade` command to deploy StackState:

```
helm upgrade \
  --install \
  --namespace "stackstate" \
  --values "ingress_values.yaml" \
  --values "values.yaml" \
stackstate \
stackstate/stackstate-k8s
```

## Configure Ingress Rule for Open Telemetry Traces via the StackState Helm chart

The StackState Helm chart exposes an `opentelemetry-collector` service in its values where a dedicated `ingress` can be created. This is disabled by default. The ingress needed for `opentelemetry-collector` purposed needs to support GRPC protocol. The example below shows how to use the Helm chart to configure an nginx-ingress controller with GRPC and TLS encryption enabled. Note that setting up the controller itself and the certificates is beyond the scope of this document.

To configure the `opentelemetry-collector` ingress for StackState, create a file `ingress_otel_values.yaml` with contents like below. Replace `MY_DOMAIN` with your own domain (that's linked with your ingress controller) and set the correct name for the `otlp-tls-secret`. Consult the documentation of your ingress controller for the correct annotations to set. All fields below are optional, for example, if no TLS will be used, omit that section but be aware that StackState also doesn't encrypt the traffic.

```
opentelemetry-collector:
  ingress:
    enabled: true
    annotations:
      nginx.ingress.kubernetes.io/proxy-body-size: "50m"
      nginx.ingress.kubernetes.io/backend-protocol: GRPC
    hosts:
      - host: otlp-stackstate.MY_DOMAIN
        paths:
          - path: /
            pathType: Prefix
            port: 4317
    tls:
      - hosts:
          - otlp-stackstate.MY_DOMAIN
        secretName: otlp-tls-secret
```

The thing that stands out in this file is the Nginx annotation to increase the allowed `proxy-body-size` to `50m` (larger than any expected request). By default, Nginx allows body sizes of maximum `1m`. StackState Agents and other data providers can sometimes send much larger requests. For this reason, you should make sure that the allowed body size is large enough, regardless of whether you are using Nginx or another ingress controller. Make sure to update the `baseUrl` in the values file generated during initial installation, it will be used by StackState to generate convenient installation instructions for the agent.

Include the `ingress_otel_values.yaml` file when you run the `helm upgrade` command to deploy StackState:

```
helm upgrade \
  --install \
  --namespace "stackstate" \
  --values "ingress_otel_values.yaml" \
  --values "values.yaml" \
stackstate \
stackstate/stackstate-k8s
```

## Configure via external tools

To make StackState accessible outside of the Kubernetes cluster it's installed in, it's enough to route traffic to port `8080` of the `<namespace>-stackstate-k8s-router` service. The UI of StackState can be accessed directly under the root path of that service (i.e. `http://<namespace>-stackstate-k8s-router:8080`) while agents will use the `/receiver` path (`http://<namespace>-stackstate-k8s-router:8080/receiver`).

Make sure to update the `baseUrl` in the values file generated during initial installation, it will be used by StackState to generate convenient installation instructions for the agent.

{% hint style="info" %}
When manually configuring an Nginx or similar HTTP server as reverse proxy make sure that it can proxy websockets as well. For Nginx this can be configured by including the following directives in the `location` directive:

```
proxy_set_header Upgrade                 $http_upgrade;
proxy_set_header Connection              "Upgrade";
```

{% endhint %}

{% hint style="warning" %}
StackState itself doesn't use TLS encrypted traffic, TLS encryption is expected to be handled by the ingress controller or external load balancers.
{% endhint %}

## Agents in the same cluster

Agents that are deployed to the same cluster as StackState can of course use the external URL on which StackState is exposed, but it's also possible to configure the agent to directly connect to the StackState instance via the Kubernetes internal network only. To do that replace the value of the `'stackstate.url'` in the `helm install` command from the [Agent Kubernetes installation](https://archivedocs.stackstate.com/get-started/k8s-quick-start-guide) with the internal cluster URL for the router service (see also above): `http://<namespace>-stackstate-k8s-router.<namespace>.svc.cluster.local:8080/receiver/stsAgent` (the `<namespace>` sections need to be replaced with the namespace of StackState).

## See also

* [AKS (learn.microsoft.com)](https://learn.microsoft.com/en-us/azure/aks/ingress-tls?tabs=azure-cli)
* [EKS Official docs](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html) (not using nginx)
* [EKS blog post](https://aws.amazon.com/blogs/opensource/network-load-balancer-nginx-ingress-controller-eks/) (using nginx)


# Initial run guide

StackState Self-hosted

## Overview

This page provides all the information you need to install and run StackState.

## Installation instructions

{% tabs %}
{% tab title="Kubernetes" %}
Install StackState on [Kubernetes](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift).
{% endtab %}

{% tab title="OpenShift" %}
Install StackState on [OpenShift](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/openshift_install).
{% endtab %}
{% endtabs %}

## Address and port

{% tabs %}
{% tab title="Kubernetes" %}
To access the StackState UI:

1. [Enable a port-forward](https://archivedocs.stackstate.com/self-hosted-setup/kubernetes_openshift/kubernetes_install#access-the-stackstate-ui).
2. Access the StackState UI at: <https://localhost:8080>
   {% endtab %}

{% tab title="OpenShift" %}
To access the StackState UI:

1. [Enable a port-forward](https://archivedocs.stackstate.com/self-hosted-setup/kubernetes_openshift/openshift_install#access-the-stackstate-ui).
2. Access the StackState UI at: <https://localhost:8080>
   {% endtab %}
   {% endtabs %}

## Default username and password

{% tabs %}
{% tab title="Kubernetes" %}
StackState is configured by default with the following administrator account:

* **username:** `admin`
* **password:** Set during installation. This is collected by the `generate_values.sh` script and stored in MD5 hash format in `values.yaml`
  {% endtab %}

{% tab title="OpenShift" %}
StackState is configured by default with the following administrator account:

* **username:** `admin`
* **password:** Set during installation. This is collected by the `generate_values.sh` script and stored in MD5 hash format in `values.yaml`
  {% endtab %}
  {% endtabs %}

## Troubleshooting

If you run into any problems during the installation of StackState or first run, check the [StackState installation troubleshooting guide](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/troubleshooting).

## Next steps

Once you have StackState up and running, you can get started setting up integrations

* [Install StackPacks to integrate with external systems](https://archivedocs.stackstate.com/get-started/k8s-quick-start-guide)
* [Explore your Kubernetes cluster](https://archivedocs.stackstate.com/views/k8s-views)


# Troubleshooting

StackState Self-hosted

## Quick troubleshooting guide

Here is a quick guide for troubleshooting the startup of StackState:

1. Check that the install completed successfully and the release is listed:

   ```
   helm list --namespace stackstate
   ```
2. Check that all pods in the StackState namespace are running:

   ```
   kubectl get pods
   ```

   In a first deployment it can be that containers in several pods restart a few times, because they are waiting for other pods to start up and be in the `ready` state. This can be delayed due to scheduling and docker image pulling delays.

   Pods that are in `pending` state are usually an indication of a problem:

   * The pod is unschedulable due to lack of resources in the cluster. If a cluster auto-scaler is active it will often be able to resolve this automatically, otherwise manual intervention is needed to add more nodes to the cluster
   * The pod is unschedulable, there are nodes it would fit on, but those nodes have `taints` that the pod doesn not tolerate. To solve this more nodes can be added that don't have the taints, but StackState can also be [configured](https://archivedocs.stackstate.com/self-hosted-setup/kubernetes_openshift/customize_config#override-default-configuration) to tolerate certain taints and run on the tainted nodes.
   * The pod is waiting for the Persistent Volumes (PVs) to be mounted. A cause can be that the StackState Helm chart doesn't specify a `storageClassName` but relies on the cluster having a default storage class. When there is no default for the cluster it's required to [specify a storage class](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/kubernetes_openshift/storage) via the Helm values of StackState.

   For pods with state `ImagePullBackOff` also check the exact error message, common causes are:

   * An incorrect username/password used to pull the images
   * Connecting to the docker registry failed, this can be due to authentication issues or connectivity issues (firewalls, air-gapped installations)
   * A typo in the overriden docker image registry URL

   To find out a more detailed cause for the `Pending`, `ImagePullBackOff` or `CrashLoopBackOff` states use this command:

   ```
   kubectl describe pod<pod-name>
   ```

   The output contains an `event` section at the end which usually contains the problem. It also has a `State` section for each container that has more details for termination of the container.
3. [Check the logs](https://archivedocs.stackstate.com/self-hosted-setup/install-stackstate/troubleshooting/kubernetes-logs) for errors.
4. Check the Knowledge base on the [StackState Support site](https://support.stackstate.com/).

## Known issues

Check the [StackState support Knowledge base](https://support.stackstate.com/hc/en-us/sections/360004684540-Known-issues) to find troubleshooting steps for all known issues.


# Logs

StackState Self-hosted v5.1.x

## Overview

In a Kubernetes setup, StackState functions are distributed across different pods and logs for each function are stored per pod and container. You can access recent logs using `kubectl`, although for long term storage it's recommended to set up log aggregation.

## Kubernetes pods for logging

StackState logs are stored per pod and container. The table below shows the pod to access for logs relating to specific StackState functions. Note that actual pod names will include a number or random string suffix (for example, `stackstate-receiver-5b9d79db86-h2hkz`) and may also include the release name specified when StackState was deployed as a prefix.

{% hint style="info" %}
Note that logs stored on pods will be regularly removed. For long term access to logs, it's advised that you set up [log aggregation](#log-aggregation) for your Kubernetes cluster.
{% endhint %}

| StackState function                           | Logs on pod                |
| --------------------------------------------- | -------------------------- |
| API (including topology, charts and settings) | `stackstate-api`           |
| Data indexing into Elasticsearch              | `stackstate-e2es` (events) |
| Data ingestion                                | `stackstate-receiver`      |
| Event handlers                                | `stackstate-view-health`   |
| Monitor                                       | `stackstate-checks`        |
| State propagation                             | `stackstate-state`         |
| Synchronization                               | `stackstate-sync`          |
| View health state                             | `stackstate-view-health`   |

You can access logs on a specific pod using the `kubectl logs` command.

For example:

```sh
$ kubectl logs stackstate-api-0
```

## Access recent logs

### Pod or container logs

The most recent logs can be retrieved from Kubernetes using the `kubectl logs` command. Check the [pod that you need to monitor](#kubernetes-pods-for-logging) to retrieve a specific log.

For example:

```sh
# Snapshot of logs for all containers of <pod-name>
$ kubectl logs <pod-name> --all-containers=true

# Stream logs for all containers of <pod-name>
$ kubectl logs -f <pod-name> --all-containers=true

# Snapshot of logs for a specific container of <pod-name>
$ kubectl logs -c <container-name> <pod-name>

# Snapshot of logs for previous terminated container of <pod-name>
$ kubectl logs -p -c <container-name> <pod-name>
```

### Synchronization logs

All synchronization logs can be found in a pod `stackstate-sync-<suffix>`. You can use the synchronization name to locate specific log information in a log snapshot.

For example:

```sh
# Logs of the synchronization for a specific Kubernetes cluster
$ kubectl logs stackstate-sync-0 | grep "Kubernetes - \<cluster-name\>"

# Logs of the Agent synchronization
$ kubectl logs stackstate-sync-0 | grep "Agent"
```

## Log aggregation

For long term storage of StackState log data, it's advised that you set up log aggregation on your Kubernetes cluster. This can be done using a third party system for storage such as Elasticsearch, Splunk or Logz.io and a log shipper such as Logstash or Fluentd.

For more details of how this can be done, check:

* Shipping logs with [Fluentd (fluentd.org)](https://docs.fluentd.org/container-deployment/kubernetes)
* A complete overview of setting up [log aggregation into Elasticsearch (bitnami.com)](https://docs.bitnami.com/tutorials/integrate-logging-kubernetes-kibana-elasticsearch-fluentd/)

## See also

* [kubectl command reference (kubernetes.io/docs)](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)


# Configure StackState

StackState Self-hosted


# Slack notifications

StackState Self-hosted

{% hint style="warning" %}
SaaS users of StackState can use Slack notifications without extra configuration. This guide is only applicable for self-hosted StackState installations, that are planning to use the Slack notification channel.
{% endhint %}

Before you can use the Slack notification channel in StackState, you first need to follow the following steps to set up both Slack and StackState:

1. Create a Slack app for StackState in your workspace
2. Configure StackState with the credentials for that Slack app.

## Creating a Slack app for StackState

{% hint style="info" %}
You need to have the permissions in Slack to manage Slack apps for your workspace.
{% endhint %}

Go to the [Slack API page](https://api.slack.com/apps) and click on the **Create New App** button.

* Select the "From an app manifest" option in the dialog that opens.
* Select the workspace you want to send notifications to and click next.
* Copy the contents of the Slack app manifest below and paste it into the text area. Make sure to replace the values in `redirect_urls` with the URL(s) of your StackState instance. Click next.
* Verify that the URL is correct and that the "bot scopes" listed are `channels:join, channels:read, chat:write, groups:read` and click the create button to create the app.
* On the "Basic information" page of the App it's possible to change the icon (in the Display information section), you can replace it with, for example, the StackState logo <img src="https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-57a9af1fec5e1c31eb0fef2e3b1ca500ea448ae6%2Fstackstate-logo.png?alt=media" alt="StackState logo" data-size="line">.

{% code title="Slack app manifest for StackState" overflow="wrap" %}

```json
{
    "display_information": {
        "name": "StackState",
        "description": "Receive notification messages from StackState",
        "background_color": "#000000"
    },
    "features": {
        "bot_user": {
            "display_name": "StackState",
            "always_online": true
        }
    },
    "oauth_config": {
        "redirect_urls": [
            "https://the.url.of.your.stackstate.installation"
        ],
        "scopes": {
            "bot": [
                "channels:join",
                "channels:read",
                "chat:write",
                "groups:read"
            ]
        }
    },
    "settings": {
        "org_deploy_enabled": false,
        "socket_mode_enabled": false,
        "token_rotation_enabled": false
    }
}
```

{% endcode %}

## Configure StackState with the credentials for that Slack app

StackState needs to be configured with the credentials for the Slack app that you created. You can do this by adding the following to the `values.yaml` file of your StackState installation:

```yaml
stackstate:
  components:
    all:
      extraEnv:
        open:
          CONFIG_FORCE_stackstate_notifications_channels_slack_authentication_clientId: "<app client id>"
        secret:
          CONFIG_FORCE_stackstate_notifications_channels_slack_authentication_clientSecret: "<app client secret>"
```

The `<app client id>` and `<app client secret>` values can be found in the "App credentials" section on the "Basic Information" page of the Slack app you created. Apply these configuration changes by running the same Helm command used during installation of StackState ([for Kubernetes](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/kubernetes_install#deploy-stackstate-with-helm) or [OpenShift](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/openshift_install#deploy-stackstate-with-helm)).

You're now ready to use the Slack notification channel!


# Stackpacks

StackState Self-hosted v5.1.x

## Overview

StackPacks extend StackState functionality and offer automated integration with external systems. They can be easily installed and uninstalled from the StackPacks page in StackState.

There are two types of StackPack - Add-ons and Integrations. The available StackPack add-ons and integrations can be found on the **StackPacks** page in the StackState UI.

## Install or uninstall a StackPack

StackPacks can be installed and uninstalled from the **StackPacks** page in StackState. Full instructions to install and uninstall the StackPack are provided.

{% hint style="info" %}
**Note that:**

* A StackPack may require **manual** installation steps or configuration of the external system. Please read the instructions provided carefully.
* When a StackPack or StackPack instance is uninstalled, **all data received via the StackPack (instance) will be removed from StackState.**
* Any (manual) configuration or installation of StackPack components in an external system may need to be uninstalled separately.
  {% endhint %}

### StackPack instances

Some StackPacks allow you to connect to multiple accounts on an external system. Each account is configured in a separate instance of the StackPack.

For example, the AWS StackPack can connect to multiple AWS accounts and combine information from all accounts in StackState. For each account, a separate StackState instance is configured with the information required to receive data from that AWS account.

## Upgrade a StackPack

{% hint style="warning" %}
When a StackPack is upgraded, **any changes made to configuration items from that StackPack will be overwritten**. For details, see [locked configuration items](#locked-configuration-items).
{% endhint %}

If a new StackPack version is available, an alert will be displayed on the StackState UI StackPack page and you will have the option to view the upgrade details and read the release notes. If the new release is a minor upgrade from the currently installed version, you can also upgrade the StackPack from here.

### New minor StackPack version

To upgrade to a new minor version of a StackPack, click **UPGRADE NOW** on the StackPack page in the StackState UI.

Note that all StackPack configuration items will be overwritten when you upgrade. To continue using any changes made to these, choose to **KEEP** the existing configuration when you upgrade the StackPack. For details, see [locked configuration items](#locked-configuration-items).

### New major StackPack version

{% hint style="warning" %}
When a StackPack is upgraded, **any changes made to configuration items from that StackPack will be overwritten**. For details, see [locked configuration items](#locked-configuration-items).
{% endhint %}

To upgrade to a new major version of a StackPack, [uninstall and reinstall](#install-or-uninstall-a-stackpack) the StackPack.

{% hint style="success" %}
Continue using changes made to customized StackPack configuration items after upgrade:

1. Before you upgrade, export each customized item:
   * Go to the **Settings** page in the StackState UI.
   * Click **Export** in the **...** menu for each customized item.
2. Upgrade the StackPack (uninstall and reinstall).
3. Change the `name` and `identifier` for each exported item:
   * Open the export file in a text editor.
   * Edit the top-level `name` and `identifier` fields.
   * Save the export.
4. [Import](https://archivedocs.stackstate.com/data-management/backup_restore/configuration_backup#import-configuration) the updated export file(s).
5. The customized configuration items will now be available in StackState and can be copied to the newly installed StackPack configuration items.
   {% endhint %}

## Locked configuration items

StackPacks contain configuration information for StackState that's installed when the StackPack (instance) is installed. Amongst other things, this could be component templates, functions, component actions and views. When a StackPack is upgraded, **the configuration items installed by the previous version of the StackPack will be overwritten by those from the newer StackPack.** This means that any manual change made to these configuration items will be overwritten when the StackPack is upgraded.

To prevent a user from making changes to configuration items installed by a StackPack that will be overwritten on upgrade, these configuration items are **locked** by default. This means that they're protected from being changed by the user and must explicitly be **unlocked** before they can be changed.

{% hint style="success" %}
You can [make a back-up of configuration items](https://archivedocs.stackstate.com/self-hosted-setup/data-management/backup_restore/configuration_backup). Note that the lock status of configuration items won't be exported as part of a configuration backup.
{% endhint %}


# Release Notes

StackState Self-hosted

Check the release notes for the latest features, enhancements, and bug fixes in StackState.


# v1.11.0 - 18/07/2024

StackState Self-hosted

## Release Notes StackState version 6.0.0 Helm Chart version 1.11.0

### New Features & Enhancements:

* Trace Explorer: Introduced a new Trace Explorer, accessible via the main menu, providing enhanced visibility into your trace data.
* Microsoft Teams Notifications: Added support for Microsoft Teams notifications, enabling better communication and alerting within your team.
* OpenTelemetry Integration: Added general support for OpenTelemetry Traces and Metrics. OpenTelemetry authentication now also supports [Ingestion API Keys](https://archivedocs.stackstate.com/security/k8s-ingestion-api-keys).
* ClickHouse Database Backups: Added support for full and incremental backups to the ClickHouse database. Backups are disabled by default; follow the documentation to enable and configure this feature.
* Improved Trace Performance: Enhanced storage and query performance for traces. Important: This upgrade will remove all existing trace data.
* OpenShift 4.14 Support: The latest agent now supports OpenShift 4.14.
* Receiver API Key Management: The `stackstate.apiKey` is no longer a required value. You can now supply the receiver API key as a self-managed secret. For more details, refer to the [documentation](https://archivedocs.stackstate.com/agent/k8s-custom-secrets-setup).
* Custom Labels and Annotations: Resources deployed by the `stackstate-k8s-agent` Helm chart resources can now be customized with additional labels and annotations via the `global.extraLabels` and `global.extraAnnotations` Helm values.
* Right-Hand Side Panel Enhancements: The Right-Hand Side panel now includes:
  * Three mini charts showing highlighted metrics.
  * A mini health timeline for better visibility of system health.
  * Similar mini charts have been added to the topology explorer component popover.

### Bug Fixes:

* X-Forwarded-For Logs: Suppressed errors in logs when the `x-forwarded-for` header contains comma-separated list of IP addresses with port numbers.
* Minio Helm Chart: The Minio Helm chart now correctly respects the globally defined `imageRegistry`.
* Saved Queries (Splunk): Fixed a bug where retrieving the list of saved queries was incorrectly pulling data from the global namespace.
* MonitorFunctions on Windows: MonitorFunctions created on Windows OS with `\r` are now converted to UNIX style (). Note: Functions created previously will not be migrated automatically; they must be manually updated by reopening and saving them.

### Security Updates:

* Vulnerabilities Addressed: Fixed several vulnerabilities in the StackState CLI, including:
  * CVE-2022-27664
  * CVE-2022-41721
  * CVE-2022-41723
  * CVE-2023-39325
  * CVE-2023-3978
  * CVE-2023-44487
  * CVE-2022-32149
  * CVE-2024-24786
  * CVE-2022-25645

### Breaking Changes:

* Openshift Installations: For OpenShift installations, the `elasticsearch.prometheus-elasticsearch-exporter.podSecurityContext` must now be set to an empty string ("").
* Propagated Health: Dropped support for propagated health. User can now use the AggregatedHealth monitor to get an aggregated health state on higher level components.

### Other Updates:

* MetricBindings Management: Added permissions to manage `MetricBindings`, which are assigned to the `stackstate-k8s-admin` role.
* Topological Relations: Fixed missing indirect relations for paths containing hierarchical relations.


# v1.11.3 - 15/08/2024

StackState Self-hosted

## Release Notes StackState version 6.0.0-snapshot.20240815083601-master-bd8cfc5 Helm Chart version 1.11.3

### New Features & Enhancements:

### Bug Fixes:

* Backup: Fix for exporting settings when Teams Notification Enabled.
* Backup: Fix StackGraph and Configuration backup jobs failing due to missing AWS ClI tool.

### Security Updates:

### Breaking Changes:

* Helm values `backup.configuration.scheduled.backupRetentionTimeDelta` and `backup.stackGraph.scheduled.backupRetentionTimeDelta` have changed format from Python timedelta to GNU `date --date`. If the values have been overridden in the value files they have to be adjusted for the new format.

For example,

```yaml
backup:
  stackGraph:
    scheduled:
      backupRetentionTimeDelta: days = 30
  configuration:
    scheduled:
      backupRetentionTimeDelta: days = 365
```

has to be replaced with

```yaml
backup:
  stackGraph:
    scheduled:
      backupRetentionTimeDelta: 30 days ago
  configuration:
    scheduled:
      backupRetentionTimeDelta: 365 days ago
```

### Other Updates:


# v1.11.4 - 29/08/2024

StackState Self-hosted

## Release Notes StackState version 6.0.0-snapshot.20240829112751-master-8082a57 Helm Chart version 1.11.4

### New Features & Enhancements:

### Bug Fixes:

* Deployment: Do not create the Clickhouse Cronjobs if Clickhouse is not enabled.

### Security Updates:

### Breaking Changes:

### Other Updates:


# v1.12.0 - 24/10/2024

StackState Self-hosted

## Release Notes StackState version 6.0.0-snapshot.20241023094532-stackstate-6.x-7be52ad Helm Chart version 1.12.0

### New Features & Enhancements:

* Introduces a new command-line accessible [configuration backup mechanism](https://archivedocs.stackstate.com/self-hosted-setup/data-management/backup_restore/configuration_backup) for just the configuration of SUSE Observability. This replaces the previous export/import backup method, improving reliability of the restoration process. Note that the import and export api's still exist but should not be used for configuration backups.

### Bug Fixes:

### Security Updates:

### Breaking Changes:

### Other Updates:


# v1.12.1 - 08/11/2024

StackState Self-hosted

## Release Notes StackState version 6.0.0-snapshot.20241023094532-stackstate-6.x-7be52ad Helm Chart version 1.12.1

### New Features & Enhancements:

### Bug Fixes:

* A removed `ServiceAccount`, for the backup cronjob, was still referenced when upgrading from an older Helm chart version

### Security Updates:

### Breaking Changes:

### Other Updates:


# Upgrade StackState

StackState Self-hosted


# Steps to upgrade

StackState Self-hosted

## Overview

This document describes the upgrade procedure for StackState.

## Before you upgrade

When executing a StackState upgrade, be aware of the following:

{% hint style="warning" %}
**Always read the** [**version-specific upgrade notes**](https://archivedocs.stackstate.com/self-hosted-setup/upgrade-stackstate/version-specific-upgrade-instructions) **before upgrading StackState.**
{% endhint %}

{% hint style="warning" %}
When upgrading a StackPack, **any changes you have made to configuration items from that StackPack will be overwritten**. See [Configuration Locking](https://archivedocs.stackstate.com/configure-stackstate/about-stackpacks#locked-configuration-items) for more information.
{% endhint %}

{% hint style="danger" %}
If there are **hotfixes** installed in your StackState installation, contact StackState technical support prior to upgrading.
{% endhint %}

## Steps to upgrade

### Minor or maintenance StackState release

A minor release of StackState is indicated by a change in the second digit of the version number, for example 4.1.0. Maintenance releases are identified by a change in the third digit of the version number, for example 4.1.1.

If you are upgrading to a new **minor** StackState release or a **maintenance** release, StackState itself and the StackPacks will be compatible with the current installation.

A minor upgrade consists of the following steps:

1. [Create a backup](#create-a-backup)
2. [Upgrade StackState](#upgrade-stackstate)
3. [Verify the new installation](#verify-the-new-installation)
4. Check if any installed StackPacks require an upgrade

### Major StackState release

A major release of StackState is indicated by a change in the first digit of the version number, for example 4.0.0.

If you upgrade to a new **major** StackState release, StackState and the installed StackPacks may be incompatible with the current installation. For details, check the [version-specific upgrade notes](https://archivedocs.stackstate.com/self-hosted-setup/upgrade-stackstate/version-specific-upgrade-instructions).

A major upgrade consists of the following steps:

1. [Create a backup](#create-a-backup)
2. Optional: [Uninstall StackPacks](#uninstall-stackpacks-optional)
3. [Upgrade StackState](#upgrade-stackstate)
4. Optional: [Install StackPacks](#install-stackpacks-optional)
5. [Verify the new installation](#verify-the-new-installation)

## Walkthrough of an upgrade

### Create a backup

Before upgrading StackState it's recommended to back up your configuration and topology data:

* [Kubernetes backup](https://archivedocs.stackstate.com/self-hosted-setup/data-management/backup_restore/kubernetes_backup)
* [Configuration backup](https://archivedocs.stackstate.com/self-hosted-setup/data-management/backup_restore/configuration_backup)

{% hint style="info" %}
Note that it won't be possible to restore the backup on the upgraded version of StackState. The StackState backup can only be restored in the StackState version before the upgrade.
{% endhint %}

### Upgrade StackState

Be sure to check the release notes and any optional upgrade notes before running the upgrade.

{% tabs %}
{% tab title="Kubernetes" %}

1. Get the latest helm chart by running `helm repo update`.
2. Check the [version specific upgrade notes](https://archivedocs.stackstate.com/self-hosted-setup/upgrade-stackstate/version-specific-upgrade-instructions) for all changes between your current version and the version that you will upgrade to. If there have been changes made to configuration items specified in your `values.yaml` file, the file should be updated.
3. To upgrade, use the same helm command as for the [first time Kubernetes installation](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/kubernetes_install#deploy-stackstate-with-helm). The new helm chart will pull newer versions of Docker images and handle the upgrade.
   {% endtab %}

{% tab title="OpenShift" %}
2\. Get the latest helm chart by running `helm repo update`.
3\. Check the [version specific upgrade notes](https://archivedocs.stackstate.com/self-hosted-setup/upgrade-stackstate/version-specific-upgrade-instructions) for all changes between your current version and the version that you will upgrade to. If there have been changes made to configuration items specified in your `values.yaml` file, the file should be updated.
4\. [Update the `openshift-values.yaml`](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/openshift_install#additional-openshift-values-file) file.
5\. To upgrade, use the same helm command as for the [first time OpenShift installation](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/openshift_install#deploy-stackstate-with-helm). The new helm chart will pull newer versions of Docker images and handle the upgrade.
{% endtab %}
{% endtabs %}

### Verify the new installation

Once StackState has been upgraded and started, verify that the new installation of StackState is reachable and that the application is running.

## See also

* [Manually upgrade a StackPack](https://archivedocs.stackstate.com/configure-stackstate/about-stackpacks#upgrade-a-stackpack)
* [Version-specific upgrade notes](https://archivedocs.stackstate.com/self-hosted-setup/upgrade-stackstate/version-specific-upgrade-instructions)


# Version-specific upgrade instructions

StackState Self-hosted

## Overview

{% hint style="warning" %}
**Review the instructions provided on this page before you upgrade!**

This page provides specific instructions and details of any required manual steps to upgrade to each supported version of StackState. Any significant change that may impact how StackState runs after upgrade will be described here, such as a change in memory requirements or configuration.

**Read and apply all instructions from the version that you are currently running up to the version that you will upgrade to.**
{% endhint %}

## Upgrade instructions

### Next version

## See also

* [Release Notes](https://archivedocs.stackstate.com/self-hosted-setup/release-notes)
* [Steps to upgrade StackState](https://archivedocs.stackstate.com/self-hosted-setup/upgrade-stackstate/steps-to-upgrade)


# Uninstall StackState

StackState Self-hosted

## Overview

1. [Uninstall the Helm cart](#un-install-the-helm-chart)
2. [Remove remaining resources](#remove-remaining-resources)
3. [Remove manually created resources](#remove-manually-created-resources)

## Un-install the Helm chart

{% hint style="info" %}
Un-installing the helm chart will preserve all data because helm will not remove the Persistent Volume Claims nor the namespace. To remove those as well also [remove the remaining resources](#remove-remaining-resources).
{% endhint %}

To un-install StackState the first action is to run the `helm uninstall` command. This command will remove all resources created by the `helm upgrade --install` command.

Uninstall the `stackstate` release from the `stackstate` namespace like this, replace the namespace or release name with any custom names used during installation:

```
helm uninstall --namespace stackstate stackstate
```

The command will return almost immediately but shutting down all the pods and removing all other resources can take a while. Check if all pods are gone with:

```
kubectl get pods --namespace stackstate
```

If you want to re-install StackState later and have the old data still available this is all, for a full uninstall continue with the next 2 sections.

## Remove remaining resources

{% hint style="warning" %}
Removing the Persistent Volume Claims and/or the namespace will result in all data being lost that was stored in StackState.
{% endhint %}

To remove the namespace and with that, the Persistent Volume Claims and their linked Persistent Volumes simply remove the entire namespace:

```
kubectl delete namespace stackstate
```

When the command returns the namespace and all volumes will have been removed.

To only remove the Persistent Volume Claims (PVCs) and keep the namespace run:

```
kubectl delete pvc --all -n stackstate
```

On OpenShift the Helm chart also created a security context constraint (SCC). It is not cleaned up automatically by Helm but instead needs to be manually removed:

```
# The scc is always named stackstate-k8s-<namespace>
oc delete scc stackstate-k8s-stackstate
```

## Remove manually created resources

{% hint style="info" %}
Even if you intend to re-install StackState on the same cluster but in a different namespace these can be removed. The resources contain references to the StackState namespace.
{% endhint %}

As described in the [required permissions](https://archivedocs.stackstate.com/install-stackstate/kubernetes_openshift/required_permissions#manually-create-cluster-wide-resources) it might have been necessary that your cluster admin created some resources manually. These resources can now be removed again, but that also is a manual task that requires admin permission.

Delete the cluster role and the cluster role bindings that have been created like this:

```
kubectl delete cluster-role stackstate-authorization
kubectl delete cluster-role-binding stackstate-authorization
kubectl delete cluster-role-binding stackstate-authentication
```




---

[Next Page](/llms-full.txt/1)

