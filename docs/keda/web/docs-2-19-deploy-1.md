# Source: https://keda.sh/docs/2.19/deploy/

Title: KEDA | Deploying KEDA

URL Source: https://keda.sh/docs/2.19/deploy/

Markdown Content:
Deploying KEDA | KEDA
===============

[![Image 1: Keda logo](https://keda.sh/img/logos/keda-horizontal-color.png)](https://keda.sh/)[](https://keda.sh/docs/2.19/deploy/)

[Docs](https://keda.sh/docs/2.19/)

[Deploying KEDA](https://keda.sh/docs/2.19/deploy)

[Concepts](https://keda.sh/docs/2.19/concepts)

[Scaling Deployments, StatefulSets & Custom Resources](https://keda.sh/docs/2.19/concepts/scaling-deployments/)

[Scaling Jobs](https://keda.sh/docs/2.19/concepts/scaling-jobs/)

[Authentication](https://keda.sh/docs/2.19/concepts/authentication/)

[External Scalers](https://keda.sh/docs/2.19/concepts/external-scalers/)

[Admission Webhooks](https://keda.sh/docs/2.19/concepts/admission-webhooks/)

[Troubleshooting](https://keda.sh/docs/2.19/concepts/troubleshooting/)

[Architecture](https://keda.sh/docs/2.19/concepts/#keda-architecture)

[Scalers](https://keda.sh/docs/2.19/scalers)

[Operate](https://keda.sh/docs/2.19/operate/)

[Integrations](https://keda.sh/docs/2.19/integrations/)

[Auth providers](https://keda.sh/docs/2.19/authentication-providers)

[Migration Guide](https://keda.sh/docs/2.19/migration/)

[FAQ](https://keda.sh/docs/2.19/reference/faq/)

[Troubleshooting Guide](https://keda.sh/docs/2.19/troubleshooting/)

[Docs](https://keda.sh/docs/2.19)

[Deploying KEDA](https://keda.sh/docs/2.19/deploy)[Concepts](https://keda.sh/docs/2.19/concepts)[Architecture](https://keda.sh/docs/2.19/concepts/#keda-architecture)[Scalers](https://keda.sh/docs/2.19/scalers)[Operate](https://keda.sh/docs/2.19/operate/)[Integrations](https://keda.sh/docs/2.19/integrations/)[Auth providers](https://keda.sh/docs/2.19/authentication-providers)[Migration Guide](https://keda.sh/docs/2.19/migration/)[FAQ](https://keda.sh/docs/2.19/reference/faq/)[Troubleshooting Guide](https://keda.sh/docs/2.19/troubleshooting/)

[Blog](https://keda.sh/blog)

[Community](https://keda.sh/docs/2.19/deploy/)

[Overview](https://keda.sh/community/)[Get Involved](https://keda.sh/community/#get-involved)[End-Users](https://keda.sh/community/#end-users)[Partners](https://keda.sh/community/#partners)[Supported by](https://keda.sh/community/#supported-by)[Videos](https://keda.sh/videos/)[Samples](https://github.com/kedacore/samples)

[Project](https://keda.sh/docs/2.19/deploy/)

[Support](https://keda.sh/support/)[Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md)[Changelog](https://github.com/kedacore/keda/blob/main/CHANGELOG.md)[Governance](https://github.com/kedacore/governance/blob/main/GOVERNANCE.md)[Roadmap](https://github.com/kedacore/keda/blob/main/ROADMAP.md)[Breaking Changes & Deprecations](https://github.com/kedacore/governance/blob/main/DEPRECATIONS.md)[Contributing](https://github.com/kedacore/keda/blob/main/CONTRIBUTING.md)[Colors and Logos](https://github.com/kedacore/governance/blob/main/BRANDING.md)[License](https://github.com/kedacore/keda/blob/main/LICENSE)[Maintainers](https://github.com/kedacore/governance/blob/main/MEMBERS.md)[Learning Resources](https://keda.sh/resources/)[Merch](https://store.cncf.io/collections/keda)

[Enterprise](https://keda.sh/enterprise/)

[](https://twitter.com/kedaorg)[](https://github.com/kedacore/keda)[](https://kubernetes.slack.com/messages/CKZJ36A5D)

[Getting Started](https://keda.sh/docs/2.19/)

*   [Setup Autoscaling with KEDA](https://keda.sh/docs/2.19/setupscaler/)
*   [Deploying KEDA](https://keda.sh/docs/2.19/deploy/)

    *   [Deploying with Helm](https://keda.sh/docs/2.19/deploy/#helm)
        *   [Prerequisites](https://keda.sh/docs/2.19/deploy/#prerequisites)
        *   [Installing](https://keda.sh/docs/2.19/deploy/#installing)
        *   [Uninstalling](https://keda.sh/docs/2.19/deploy/#uninstalling)

    *   [Deploying with Operator Hub](https://keda.sh/docs/2.19/deploy/#operatorhub)
        *   [Prerequisites](https://keda.sh/docs/2.19/deploy/#prerequisites-1)
        *   [Installing](https://keda.sh/docs/2.19/deploy/#installing-1)
        *   [Uninstalling](https://keda.sh/docs/2.19/deploy/#uninstalling-1)

    *   [Deploying KEDA using the YAML files](https://keda.sh/docs/2.19/deploy/#yaml)
        *   [Prerequisites](https://keda.sh/docs/2.19/deploy/#prerequisites-2)
        *   [Installing](https://keda.sh/docs/2.19/deploy/#installing-2)
        *   [Uninstalling](https://keda.sh/docs/2.19/deploy/#uninstalling-2)

    *   [Deploying KEDA on MicroK8s](https://keda.sh/docs/2.19/deploy/#microk8s)
        *   [Prerequisites](https://keda.sh/docs/2.19/deploy/#prerequisites-3)
        *   [Installing](https://keda.sh/docs/2.19/deploy/#installing-3)
        *   [Uninstalling](https://keda.sh/docs/2.19/deploy/#uninstalling-3)

    *   [Getting Started with KEDA: A Simple Example](https://keda.sh/docs/2.19/deploy/#getting-started-with-keda-a-simple-example)
        *   [Step 1: Deploy a Sample Application](https://keda.sh/docs/2.19/deploy/#step-1-deploy-a-sample-application)
        *   [Step 2: Expose the Application](https://keda.sh/docs/2.19/deploy/#step-2-expose-the-application)
        *   [Step 3: Create a ScaledObject](https://keda.sh/docs/2.19/deploy/#step-3-create-a-scaledobject)
        *   [Step 4: Test the Scaling Behavior](https://keda.sh/docs/2.19/deploy/#step-4-test-the-scaling-behavior)
        *   [Cleanup](https://keda.sh/docs/2.19/deploy/#cleanup)

*   [Migration Guide](https://keda.sh/docs/2.19/migration/)
*   [Troubleshooting](https://keda.sh/docs/2.19/troubleshooting/)

[KEDA Concepts](https://keda.sh/docs/2.19/concepts/)

*   [Scaling Deployments, StatefulSets & Custom Resources](https://keda.sh/docs/2.19/concepts/scaling-deployments/)
*   [Scaling Jobs](https://keda.sh/docs/2.19/concepts/scaling-jobs/)
*   [Authentication](https://keda.sh/docs/2.19/concepts/authentication/)
*   [External Scalers](https://keda.sh/docs/2.19/concepts/external-scalers/)
*   [Admission Webhooks](https://keda.sh/docs/2.19/concepts/admission-webhooks/)
*   [Troubleshooting](https://keda.sh/docs/2.19/concepts/troubleshooting/)

[Operate](https://keda.sh/docs/2.19/operate/)

*   [Admission Webhooks](https://keda.sh/docs/2.19/operate/admission-webhooks/)
*   [CloudEvent Support](https://keda.sh/docs/2.19/operate/cloud-events/)
*   [Cluster](https://keda.sh/docs/2.19/operate/cluster/)
*   [KEDA Metrics Server](https://keda.sh/docs/2.19/operate/metrics-server/)
*   [Schema](https://keda.sh/docs/2.19/operate/schema/)
*   [Security](https://keda.sh/docs/2.19/operate/security/)

[Reference](https://keda.sh/docs/2.19/reference/)

*   [Glossary](https://keda.sh/docs/2.19/reference/glossary/)
*   [FAQ](https://keda.sh/docs/2.19/reference/faq/)
*   [Events reference](https://keda.sh/docs/2.19/reference/events/)
*   [ScaledObject specification](https://keda.sh/docs/2.19/reference/scaledobject-spec/)
*   [ScaledJob specification](https://keda.sh/docs/2.19/reference/scaledjob-spec/)

[Scalers](https://keda.sh/docs/2.19/scalers/)

*   [ActiveMQ](https://keda.sh/docs/2.19/scalers/activemq/)
*   [ActiveMQ Artemis](https://keda.sh/docs/2.19/scalers/artemis/)
*   [Apache Kafka](https://keda.sh/docs/2.19/scalers/apache-kafka/)
*   [Apache Kafka (Experimental)](https://keda.sh/docs/2.19/scalers/apache-kafka-go/)
*   [Apache Pulsar](https://keda.sh/docs/2.19/scalers/pulsar/)
*   [ArangoDB](https://keda.sh/docs/2.19/scalers/arangodb/)
*   [AWS CloudWatch](https://keda.sh/docs/2.19/scalers/aws-cloudwatch/)
*   [AWS DynamoDB](https://keda.sh/docs/2.19/scalers/aws-dynamodb/)
*   [AWS DynamoDB Streams](https://keda.sh/docs/2.19/scalers/aws-dynamodb-streams/)
*   [AWS Kinesis Stream](https://keda.sh/docs/2.19/scalers/aws-kinesis/)
*   [AWS SQS Queue](https://keda.sh/docs/2.19/scalers/aws-sqs/)
*   [Azure Application Insights](https://keda.sh/docs/2.19/scalers/azure-app-insights/)
*   [Azure Blob Storage](https://keda.sh/docs/2.19/scalers/azure-storage-blob/)
*   [Azure Data Explorer](https://keda.sh/docs/2.19/scalers/azure-data-explorer/)
*   [Azure Event Hubs](https://keda.sh/docs/2.19/scalers/azure-event-hub/)
*   [Azure Log Analytics](https://keda.sh/docs/2.19/scalers/azure-log-analytics/)
*   [Azure Monitor](https://keda.sh/docs/2.19/scalers/azure-monitor/)
*   [Azure Pipelines](https://keda.sh/docs/2.19/scalers/azure-pipelines/)
*   [Azure Service Bus](https://keda.sh/docs/2.19/scalers/azure-service-bus/)
*   [Azure Storage Queue](https://keda.sh/docs/2.19/scalers/azure-storage-queue/)
*   [Beanstalkd](https://keda.sh/docs/2.19/scalers/beanstalkd/)
*   [Cassandra](https://keda.sh/docs/2.19/scalers/cassandra/)
*   [CouchDB](https://keda.sh/docs/2.19/scalers/couchdb/)
*   [CPU](https://keda.sh/docs/2.19/scalers/cpu/)
*   [Cron](https://keda.sh/docs/2.19/scalers/cron/)
*   [Datadog](https://keda.sh/docs/2.19/scalers/datadog/)
*   [Dynatrace](https://keda.sh/docs/2.19/scalers/dynatrace/)
*   [Elasticsearch](https://keda.sh/docs/2.19/scalers/elasticsearch/)
*   [Etcd](https://keda.sh/docs/2.19/scalers/etcd/)
*   [External](https://keda.sh/docs/2.19/scalers/external/)
*   [External Push](https://keda.sh/docs/2.19/scalers/external-push/)
*   [Forgejo](https://keda.sh/docs/2.19/scalers/forgejo/)
*   [Github Runner Scaler](https://keda.sh/docs/2.19/scalers/github-runner/)
*   [Google Cloud Platform Cloud Tasks](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/)
*   [Google Cloud Platform Pub/Sub](https://keda.sh/docs/2.19/scalers/gcp-pub-sub/)
*   [Google Cloud Platform Stackdriver](https://keda.sh/docs/2.19/scalers/gcp-stackdriver/)
*   [Google Cloud Platform Storage](https://keda.sh/docs/2.19/scalers/gcp-storage/)
*   [Graphite](https://keda.sh/docs/2.19/scalers/graphite/)
*   [Huawei Cloudeye](https://keda.sh/docs/2.19/scalers/huawei-cloudeye/)
*   [IBM MQ](https://keda.sh/docs/2.19/scalers/ibm-mq/)
*   [InfluxDB](https://keda.sh/docs/2.19/scalers/influxdb/)
*   [Kubernetes Resource](https://keda.sh/docs/2.19/scalers/kubernetes-resource/)
*   [Kubernetes Workload](https://keda.sh/docs/2.19/scalers/kubernetes-workload/)
*   [Liiklus Topic](https://keda.sh/docs/2.19/scalers/liiklus-topic/)
*   [Loki](https://keda.sh/docs/2.19/scalers/loki/)
*   [Memory](https://keda.sh/docs/2.19/scalers/memory/)
*   [Metrics API](https://keda.sh/docs/2.19/scalers/metrics-api/)
*   [MongoDB](https://keda.sh/docs/2.19/scalers/mongodb/)
*   [MSSQL](https://keda.sh/docs/2.19/scalers/mssql/)
*   [MySQL](https://keda.sh/docs/2.19/scalers/mysql/)
*   [NATS JetStream](https://keda.sh/docs/2.19/scalers/nats-jetstream/)
*   [NATS Streaming](https://keda.sh/docs/2.19/scalers/nats-streaming/)
*   [New Relic](https://keda.sh/docs/2.19/scalers/new-relic/)
*   [NSQ](https://keda.sh/docs/2.19/scalers/nsq/)
*   [OpenStack Metric](https://keda.sh/docs/2.19/scalers/openstack-metric/)
*   [OpenStack Swift](https://keda.sh/docs/2.19/scalers/openstack-swift/)
*   [PostgreSQL](https://keda.sh/docs/2.19/scalers/postgresql/)
*   [Predictkube](https://keda.sh/docs/2.19/scalers/predictkube/)
*   [Prometheus](https://keda.sh/docs/2.19/scalers/prometheus/)
*   [RabbitMQ Queue](https://keda.sh/docs/2.19/scalers/rabbitmq-queue/)
*   [Redis Lists](https://keda.sh/docs/2.19/scalers/redis-lists/)
*   [Redis Lists (supports Redis Cluster)](https://keda.sh/docs/2.19/scalers/redis-cluster-lists/)
*   [Redis Lists (supports Redis Sentinel)](https://keda.sh/docs/2.19/scalers/redis-sentinel-lists/)
*   [Redis Streams](https://keda.sh/docs/2.19/scalers/redis-streams/)
*   [Redis Streams (supports Redis Cluster)](https://keda.sh/docs/2.19/scalers/redis-cluster-streams/)
*   [Redis Streams (supports Redis Sentinel)](https://keda.sh/docs/2.19/scalers/redis-sentinel-streams/)
*   [Selenium Grid Scaler](https://keda.sh/docs/2.19/scalers/selenium-grid-scaler/)
*   [Solace PubSub+ Event Broker](https://keda.sh/docs/2.19/scalers/solace-pub-sub/)
*   [Solace PubSub+ Event Broker - Direct Messaging](https://keda.sh/docs/2.19/scalers/solace-pub-sub-dm/)
*   [SolarWinds](https://keda.sh/docs/2.19/scalers/solarwinds/)
*   [Solr](https://keda.sh/docs/2.19/scalers/solr/)
*   [Splunk](https://keda.sh/docs/2.19/scalers/splunk/)
*   [Splunk Observability](https://keda.sh/docs/2.19/scalers/splunk-observability/)
*   [Sumo Logic](https://keda.sh/docs/2.19/scalers/sumologic/)
*   [Temporal](https://keda.sh/docs/2.19/scalers/temporal/)

[Authentication Providers](https://keda.sh/docs/2.19/authentication-providers/)

*   [AWS (IRSA) Pod Identity Webhook](https://keda.sh/docs/2.19/authentication-providers/aws/)
*   [AWS EKS Pod Identity Webhook](https://keda.sh/docs/2.19/authentication-providers/aws-eks/)
*   [AWS Secret Manager](https://keda.sh/docs/2.19/authentication-providers/aws-secret-manager/)
*   [Azure AD Workload Identity](https://keda.sh/docs/2.19/authentication-providers/azure-ad-workload-identity/)
*   [Azure Key Vault secret](https://keda.sh/docs/2.19/authentication-providers/azure-key-vault/)
*   [Bound service account token](https://keda.sh/docs/2.19/authentication-providers/bound-service-account-token/)
*   [Config Map](https://keda.sh/docs/2.19/authentication-providers/configmap/)
*   [Environment variable](https://keda.sh/docs/2.19/authentication-providers/environment-variable/)
*   [File path](https://keda.sh/docs/2.19/authentication-providers/file-path/)
*   [GCP Secret Manager](https://keda.sh/docs/2.19/authentication-providers/gcp-secret-manager/)
*   [GCP Workload Identity](https://keda.sh/docs/2.19/authentication-providers/gcp-workload-identity/)
*   [Hashicorp Vault secret](https://keda.sh/docs/2.19/authentication-providers/hashicorp-vault/)
*   [Secret](https://keda.sh/docs/2.19/authentication-providers/secret/)

[Integrations](https://keda.sh/docs/2.19/integrations/)

*   [Integrate with OpenTelemetry Collector (Experimental)](https://keda.sh/docs/2.19/integrations/opentelemetry/)
*   [Integrate with Prometheus](https://keda.sh/docs/2.19/integrations/prometheus/)
*   [KEDA Integration with Istio](https://keda.sh/docs/2.19/integrations/istio-integration/)

Deploying KEDA Latest

 Version  2.19  (latest) 

[2.20 (unreleased)](https://keda.sh/docs/2.20/deploy)[2.19 (latest)](https://keda.sh/docs/2.19/deploy)[2.18](https://keda.sh/docs/2.18/deploy)[2.17](https://keda.sh/docs/2.17/deploy)[2.16](https://keda.sh/docs/2.16/deploy)[2.15](https://keda.sh/docs/2.15/deploy)[2.14](https://keda.sh/docs/2.14/deploy)[2.13](https://keda.sh/docs/2.13/deploy)[2.12](https://keda.sh/docs/2.12/deploy)[2.11](https://keda.sh/docs/2.11/deploy)[2.10](https://keda.sh/docs/2.10/deploy)[2.9](https://keda.sh/docs/2.9/deploy)[2.8](https://keda.sh/docs/2.8/deploy)[2.7](https://keda.sh/docs/2.7/deploy)[2.6](https://keda.sh/docs/2.6/deploy)[2.5](https://keda.sh/docs/2.5/deploy)[2.4](https://keda.sh/docs/2.4/deploy)[2.3](https://keda.sh/docs/2.3/deploy)[2.2](https://keda.sh/docs/2.2/deploy)[2.1](https://keda.sh/docs/2.1/deploy)[2.0](https://keda.sh/docs/2.0/deploy)[1.5](https://keda.sh/docs/1.5/deploy)[1.4](https://keda.sh/docs/1.4/deploy)

[Suggest a change](https://github.com/kedacore/keda-docs/blob/main/content/docs/2.19/deploy.md)

KEDA offers multiple installation methods, each with unique benefits to suit various environments and needs. If you’re looking for flexibility and customization, deploying with **Helm** is ideal; it integrates well with environments that have established Helm workflows and allows easy configuration adjustments. For a straightforward setup, installing through **Operator Hub** provides a quick, one-click deployment with automatic updates, which is great for users seeking minimal customization.

Using **YAML files** offers the most control over your setup, making it perfect for environments requiring strict configurations or where Helm and Operator Hub are not options. Finally, deploying KEDA on **MicroK8s** is excellent for local or development testing, providing a lightweight Kubernetes environment that’s fast to set up without the commitment of a full cluster.

Each method balances convenience, control, and compatibility differently: Helm is best for extensive customization, Operator Hub for simplicity, YAML files for precise configuration, and MicroK8s for local experimentation. Select the option that aligns with your deployment requirements and environment.

> 💡 **NOTE:** KEDA requires Kubernetes cluster version 1.30 and higher

Don’t see what you need? Feel free to [create an issue](https://github.com/kedacore/keda/issues/new) on our GitHub repo.

Deploying with Helm [](https://keda.sh/docs/2.19/deploy/#helm)
--------------------------------------------------------------

### Prerequisites [](https://keda.sh/docs/2.19/deploy/#prerequisites)

To deploy KEDA using Helm, make sure Helm is installed and configured on your system. Helm is a package manager for Kubernetes that simplifies the deployment process by handling complex configurations and templating, which is particularly useful for managing multiple instances or custom settings. It’s recommended to use the latest version of Helm to ensure compatibility with KEDA and access to the newest features.

If you’re new to Helm, start by familiarizing yourself with basic Helm commands ([`helm install`](https://helm.sh/docs/helm/helm_install/)`, helm upgrade, helm repo add`). Ensure that you have permissions to install charts on your Kubernetes cluster, as some environments may restrict access. A properly configured Helm setup will allow you to deploy KEDA quickly and make adjustments to configurations with ease.

### Installing [](https://keda.sh/docs/2.19/deploy/#installing)

1.   To deploy KEDA using Helm, first add the official KEDA Helm repository:

```sh
helm repo add kedacore https://kedacore.github.io/charts  
helm repo update
``` 
2.   Install `keda` by running:

**Helm 3**

```sh
helm install keda kedacore/keda --namespace keda --create-namespace
``` 
This command installs KEDA in a dedicated namespace (keda). You can customize the installation by passing additional configuration values with `--set`, allowing you to adjust parameters like replica counts, scaling metrics, or logging levels. Once installed, verify the deployment by checking the KEDA namespace for running pods:

```sh
kubectl get pods -n keda
``` 

To deploy KEDA’s Custom Resource Definitions (CRDs) separately from the Helm chart, follow these steps:

1.   **Download the CRD YAML File**: Visit the [KEDA GitHub releases page](https://github.com/kedacore/keda/releases) and locate the `keda-2.xx.x-crds.yaml` file corresponding to your desired version.

2.   **Apply the CRDs to Your Cluster**: Use `kubectl` to apply the CRD definitions:

```sh
kubectl apply -f keda-2.xx.x-crds.yaml
``` 
Replace `2.xx.x` with the specific version number you downloaded.

By deploying the CRDs separately, you can manage them independently of the Helm chart, providing flexibility in your deployment process.

> 💡 **NOTE:** When upgrading to KEDA version 2.2.1 or later, it’s important to address potential issues with CRDs. Starting with v2.2.1, KEDA’s Helm chart manages CRDs automatically, which can lead to upgrade failures if you previously installed KEDA using an earlier version. To prevent errors during the upgrade process, such as conflicts or failed deployments, consult KEDA’s [troubleshooting guide](https://keda.sh/docs/2.0/troubleshooting/) for detailed instructions on resolving CRD-related issues.

Deploying KEDA with Helm is straightforward and allows easy updates and configuration adjustments, making it a flexible choice for most environments.

### Uninstalling [](https://keda.sh/docs/2.19/deploy/#uninstalling)

To uninstall KEDA, use the following Helm command:

```sh
helm uninstall keda –namespace keda
```

This command removes KEDA from your cluster while retaining your configuration files in case you need to reinstall later. If you also want to delete the keda namespace, run:

```sh
kubectl delete namespace keda
```

Uninstalling with Helm is efficient and keeps your cluster clean, especially if you’re testing configurations or upgrading to a new KEDA version.

You can remove finalizers with the following command:

```sh
kubectl patch scaledobject <resource-name> -p '{"metadata":{"finalizers":null}}' --type=merge
kubectl patch scaledjob <resource-name> -p '{"metadata":{"finalizers":null}}' --type=merge
```

Replace <_resource-name_> with the specific name of each resource. Removing finalizers ensures that these resources are fully removed, preventing any unintended orphaned resources in your cluster.

Deploying with Operator Hub [](https://keda.sh/docs/2.19/deploy/#operatorhub)
-----------------------------------------------------------------------------

### Prerequisites [](https://keda.sh/docs/2.19/deploy/#prerequisites-1)

Before deploying KEDA through Operator Hub, ensure you have access to a Kubernetes marketplace that supports Operator Hub (for example, [OpenShift](https://docs.redhat.com/en) or an [Operator Lifecycle Manager](https://olm.operatorframework.io/docs/) (OLM)-enabled cluster). You’ll also need the appropriate permissions to install operators in your cluster, as some environments may restrict access.

If you’re using OpenShift, you can access Operator Hub directly through the OpenShift Console. For other Kubernetes distributions, verify that the OLM is installed, as it manages the installation and lifecycle of operators from Operator Hub. Ensuring these prerequisites are met will allow for a smooth installation of KEDA from Operator Hub.

### Installing [](https://keda.sh/docs/2.19/deploy/#installing-1)

To deploy KEDA through Operator Hub, start by navigating to your cluster’s Operator Hub interface. If you’re using OpenShift, access Operator Hub directly from the OpenShift Console. For other Kubernetes environments, ensure the **Operator Lifecycle Manager (OLM)** is installed.

Search for “KEDA” in Operator Hub, select the KEDA Operator, and click **Install**. Choose your preferred installation options, such as the target namespace, and confirm the installation. Once KEDA is installed, verify the deployment by checking that the KEDA Operator pod is running in the designated namespace.

1.   On Operator Hub Marketplace locate and install KEDA operator to namespace `keda`
2.   Create `KedaController` resource named `keda` in namespace `keda`![Image 2: Operator Hub installation](https://raw.githubusercontent.com/kedacore/keda-olm-operator/main/images/keda-olm-install.gif) ![Image 3: Operator Hub installation](https://raw.githubusercontent.com/kedacore/keda-olm-operator/main/images/keda-olm-install.gif)  Using Operator Hub simplifies KEDA deployment, offering easy setup and automated lifecycle management within your Kubernetes environment.

> 💡 **NOTE:** For more details on deploying KEDA with the Operator Hub installation method, refer to the official repository:
> 
> 
> [KEDA Operator Hub Repository](https://github.com/kedacore/keda-olm-operator)
> 
> 
> This repository provides additional guidance, configuration options, and troubleshooting tips for installing KEDA via Operator Hub in various Kubernetes environments.
> 
> 
> For beginners exploring the [`keda-olm-operator repository`](https://github.com/kedacore/keda-olm-operator), the following files and directories are particularly helpful:
> 
> 
> - **`README.md`:** This file provides an overview of the project, including installation instructions and usage examples. It’s a great starting point to understand the purpose and functionality of the operator.
> 
> 
> - **`config/samples/`**: This directory contains sample YAML files that demonstrate how to configure KEDA resources. Reviewing these samples can help you learn how to define and apply custom resources in your Kubernetes cluster.
> 
> 
> - **`Makefile`**: The `Makefile` includes commands for building and deploying the operator. Examining this file can give you insights into the development and deployment processes used in the project.

### Uninstalling [](https://keda.sh/docs/2.19/deploy/#uninstalling-1)

To uninstall KEDA, go to your cluster’s Operator Hub interface and locate the **Installed Operators** section. Find the KEDA Operator in the list, select it, and choose **Uninstall**. Confirm the uninstallation to remove the operator from your cluster.

If you deployed KEDA in a specific namespace, you may also want to delete that namespace to fully clean up any remaining resources. Uninstalling with Operator Hub keeps your cluster organized by removing all KEDA-related components with a few clicks.

Deploying KEDA using the YAML files [](https://keda.sh/docs/2.19/deploy/#yaml)
------------------------------------------------------------------------------

### Prerequisites [](https://keda.sh/docs/2.19/deploy/#prerequisites-2)

Before deploying KEDA with YAML files, ensure you have `kubectl` installed and configured to interact with your Kubernetes cluster. You’ll also need the KEDA YAML manifests, which you can download from the [KEDA GitHub releases page](https://github.com/kedacore/keda/releases). This method provides full control over configuration and is ideal if you need a highly customized setup or don’t have access to Helm or Operator Hub. Make sure you have the appropriate permissions to apply these configurations in your cluster.

### Installing [](https://keda.sh/docs/2.19/deploy/#installing-2)

Once the KEDA YAML manifests are downloaded, apply the files to your cluster with the following command:

```sh
# Including admission webhooks
kubectl apply --server-side -f https://github.com/kedacore/keda/releases/download/v2.19.0/keda-2.19.0.yaml
# Without admission webhooks
kubectl apply --server-side -f https://github.com/kedacore/keda/releases/download/v2.19.0/keda-2.19.0-core.yaml
```

Alternatively you can download the file and deploy it from the local path:

```sh
# Including admission webhooks
kubectl apply --server-side -f keda-2.19.0.yaml
# Without admission webhooks
kubectl apply --server-side -f keda-2.19.0-core.yaml
```

The `--server-side` flag allows Kubernetes to manage complex resources, like CRDs and admission webhooks, directly on the server. This approach reduces conflicts and ensures configurations are efficiently merged. For more information, see [this issue](https://github.com/kedacore/keda/issues/4740).

> 💡 **NOTE:** If you prefer working directly from the [KEDA GitHub repository](https://github.com/kedacore/keda), you can find the necessary YAML files in the `/config` directory. Cloning the repository allows you to manage and deploy KEDA configurations locally:
> 
> 
> 
> ```sh
> git clone https://github.com/kedacore/keda && cd keda
> 
> VERSION=2.19.0 make deploy
> ```
> 
> 
> This approach gives you full access to KEDA’s configuration files, allowing you to explore, modify, or tailor the YAML manifests before deploying. Using make deploy with the specified version will install KEDA directly from your local setup, offering flexibility for customization.

After applying the YAML, verify the deployment by checking the KEDA namespace:

```sh
kubectl get pods -n keda
```

Deploying KEDA this way provides control over configuration while leveraging server-side merging for smoother updates.

### Uninstalling [](https://keda.sh/docs/2.19/deploy/#uninstalling-2)

If you installed KEDA using the released YAML files, you can uninstall it by running the following commands:

```sh
# Including admission webhooks
kubectl delete -f https://github.com/kedacore/keda/releases/download/v2.19.0/keda-2.19.0.yaml
# Without admission webhooks
kubectl delete -f https://github.com/kedacore/keda/releases/download/v2.19.0/keda-2.19.0-core.yaml
```

If you downloaded the files locally, uninstall with:

```sh
# Including admission webhooks
kubectl delete -f keda-2.19.0.yaml
# Without admission webhooks
kubectl delete -f keda-2.19.0-core.yaml
```

For users who cloned the KEDA GitHub repository, navigate to the cloned directory and use:

```sh
VERSION=2.19.0 make undeploy
```

Deploying KEDA on MicroK8s [](https://keda.sh/docs/2.19/deploy/#microk8s)
-------------------------------------------------------------------------

### Prerequisites [](https://keda.sh/docs/2.19/deploy/#prerequisites-3)

Before deploying KEDA on [**MicroK8s**](https://microk8s.io/), ensure that you have MicroK8s installed and running on your local machine. MicroK8s is a lightweight Kubernetes distribution, ideal for testing and local development. You’ll need `kubectl` configured to interact with your MicroK8s cluster, which is typically included with MicroK8s but may require enabling (`microk8s kubectl`).

Additionally, confirm that your MicroK8s setup includes the **Helm 3** and **DNS** add-ons:

*   **Helm 3**: KEDA utilizes Helm charts for deployment, making Helm 3 essential for managing KEDA’s installation and configuration.
*   **DNS**: Kubernetes services rely on DNS for internal communication. Enabling the DNS add-on ensures that KEDA components can resolve service names within the cluster, facilitating proper operation.

### Installing [](https://keda.sh/docs/2.19/deploy/#installing-3)

To install KEDA on MicroK8s, start by enabling necessary add-ons and then deploy KEDA using the Helm 3 add-on.

1.   Enable Helm and DNS Add-ons (if not already enabled):

```sh
microk8s enable dns helm3use
``` 
2.   Add the KEDA Helm Repository:

```sh
microk8s helm3 repo add kedacore https://kedacore.github.io/charts

microk8s helm3 repo update
``` 
3.   Install KEDA Using Helm.

Deploy KEDA into your MicroK8s cluster by running:

```sh
microk8s helm3 install keda kedacore/keda --namespace keda --create-namespace
``` 
4.   Verify the Installation.

Check that KEDA is running by listing the pods in the keda namespace:

```sh
microk8s kubectl get pods -n keda
``` 

This approach allows you to quickly set up KEDA on MicroK8s, providing a streamlined environment for local testing and development.

### Uninstalling [](https://keda.sh/docs/2.19/deploy/#uninstalling-3)

To uninstall KEDA from your MicroK8s environment, disable the KEDA add-on:

```sh
microk8s disable keda
```

This command removes KEDA and its associated components from your cluster, ensuring a clean uninstallation. If you deployed KEDA using Helm, uninstall it with:

```sh
microk8s helm3 uninstall keda --namespace keda
```

After running these commands, KEDA will be fully removed from your MicroK8s setup.

Getting Started with KEDA: A Simple Example [](https://keda.sh/docs/2.19/deploy/#getting-started-with-keda-a-simple-example)
----------------------------------------------------------------------------------------------------------------------------

To help you begin with KEDA, we’ll walk through a straightforward example that demonstrates its event-driven scaling capabilities. This “Hello KEDA” exercise will guide you through setting up a basic application that scales based on external events, providing a hands-on introduction to KEDA’s functionality.

Before starting, ensure you have the following:

*   **Kubernetes Cluster**: A running Kubernetes cluster. You can use Minikube, Kind, or any cloud-based Kubernetes service.
*   **kubectl**: The Kubernetes command-line tool, configured to interact with your cluster.
*   **KEDA Installed**: KEDA should be installed in your cluster.

### Step 1: Deploy a Sample Application [](https://keda.sh/docs/2.19/deploy/#step-1-deploy-a-sample-application)

We’ll deploy a simple application that responds to HTTP requests. For this example, we’ll use a basic Python HTTP server.

1.   **Create a Deployment Manifest**: Save the following YAML as `deployment.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
   name: http-app
spec:
   replicas: 1
   selector:
      matchLabels:
         app: http-app
   template:
      metadata:
         labels:
            app: http-app
      spec:
         containers:
         - name: http-app
           image: hashicorp/http-echo
           args:
              - "-text=Hello, KEDA!"
           ports:
              - containerPort: 5678
``` 
2.   **Apply the Deployment**: Run the following command to create the deployment:

```sh
kubectl apply -f deployment.yaml
``` 

### Step 2: Expose the Application [](https://keda.sh/docs/2.19/deploy/#step-2-expose-the-application)

To access the application, we’ll create a Service.

1.   **Create a Service Manifest**: Save the following YAML as `service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
   name: http-app-service
spec:
   selector:
      app: http-app
   ports:
      - protocol: TCP
        port: 80
        targetPort: 5678
   type: LoadBalancer
``` 
2.   **Apply the Service**: Run the following command to create the service:

```sh
kubectl apply -f service.yaml
``` 
3.   **Retrieve the External IP**: After a few moments, retrieve the external IP address:

```sh
kubectl get service http-app-service
``` 

### Step 3: Create a ScaledObject [](https://keda.sh/docs/2.19/deploy/#step-3-create-a-scaledobject)

We’ll create a `ScaledObject` to enable KEDA to scale our deployment based on HTTP request rates.

1.   **Create a ScaledObject Manifest**: Save the following YAML as `scaledobject.yaml`:

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
   name: http-app-scaledobject
spec:
   scaleTargetRef:
      name: http-app
   minReplicaCount: 1
   maxReplicaCount: 10
   triggers:
      - type: prometheus
        metadata:
           serverAddress: http://prometheus-server.default.svc.cluster.local:9090
           threshold: '5'
           query: sum(rate(http_requests_total[1m]))
``` 
> 💡 **NOTE:** This example assumes you have Prometheus installed in your cluster and scraping metrics from your application. Adjust the `serverAddress` and `query` as needed.

2.   **Apply the ScaledObject**: Run the following command to create the ScaledObject:

```sh
kubectl apply -f scaledobject.yaml
``` 

### Step 4: Test the Scaling Behavior [](https://keda.sh/docs/2.19/deploy/#step-4-test-the-scaling-behavior)

We’ll create a `ScaledObject` to enable KEDA to scale our deployment based on HTTP request rates. To observe KEDA’s scaling in action:

1.   **Generate Load**: Use a tool like curl or hey to send multiple requests to your application’s external IP:

```sh
hey -z 1m -c 10 http://<EXTERNAL-IP>
``` 
Replace `<EXTERNAL-IP>` with the external IP address obtained earlier.

2.   **Monitor Scaling:** Run the following command to watch the scaling behavior:

```sh
kubectl get pods -w
``` 
You should see the number of pods increase as the load increases and decrease when the load subsides.

### Cleanup [](https://keda.sh/docs/2.19/deploy/#cleanup)

After completing the exercise, clean up the resources:

```sh
kubectl delete -f scaledobject.yaml
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
```

This example provides a hands-on introduction to KEDA’s event-driven scaling capabilities. By following these steps, you can see how KEDA integrates with Kubernetes to scale applications based on external events.

![Image 4: KEDA Logo](https://keda.sh/img/logos/keda-icon-white.png)

[Blog](https://keda.sh/blog)

[Community](https://keda.sh/docs/2.19/deploy/)

[Project](https://keda.sh/docs/2.19/deploy/)

[Enterprise](https://keda.sh/enterprise/)

[Twitter](https://twitter.com/kedaorg)[GitHub](https://github.com/kedacore/keda)[Slack](https://kubernetes.slack.com/messages/CKZJ36A5D)

© KEDA Authors 2014-2026 | Documentation Distributed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0)

![Image 5](https://static.scarf.sh/a.png?x-pxid=46ce89e3-f6ce-454e-9740-490aaee3da5e)

© 2026 [The Linux Foundation](https://linuxfoundation.org/). All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage) page.
