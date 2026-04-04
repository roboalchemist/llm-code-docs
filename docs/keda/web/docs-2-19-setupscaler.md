# Source: https://keda.sh/docs/2.19/setupscaler/

Title: KEDA | Setup Autoscaling with KEDA

URL Source: https://keda.sh/docs/2.19/setupscaler/

Markdown Content:
Setup Autoscaling with KEDA | KEDA
===============

[![Image 1: Keda logo](https://keda.sh/img/logos/keda-horizontal-color.png)](https://keda.sh/)[](https://keda.sh/docs/2.19/setupscaler/)

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

[Community](https://keda.sh/docs/2.19/setupscaler/)

[Overview](https://keda.sh/community/)[Get Involved](https://keda.sh/community/#get-involved)[End-Users](https://keda.sh/community/#end-users)[Partners](https://keda.sh/community/#partners)[Supported by](https://keda.sh/community/#supported-by)[Videos](https://keda.sh/videos/)[Samples](https://github.com/kedacore/samples)

[Project](https://keda.sh/docs/2.19/setupscaler/)

[Support](https://keda.sh/support/)[Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md)[Changelog](https://github.com/kedacore/keda/blob/main/CHANGELOG.md)[Governance](https://github.com/kedacore/governance/blob/main/GOVERNANCE.md)[Roadmap](https://github.com/kedacore/keda/blob/main/ROADMAP.md)[Breaking Changes & Deprecations](https://github.com/kedacore/governance/blob/main/DEPRECATIONS.md)[Contributing](https://github.com/kedacore/keda/blob/main/CONTRIBUTING.md)[Colors and Logos](https://github.com/kedacore/governance/blob/main/BRANDING.md)[License](https://github.com/kedacore/keda/blob/main/LICENSE)[Maintainers](https://github.com/kedacore/governance/blob/main/MEMBERS.md)[Learning Resources](https://keda.sh/resources/)[Merch](https://store.cncf.io/collections/keda)

[Enterprise](https://keda.sh/enterprise/)

[](https://twitter.com/kedaorg)[](https://github.com/kedacore/keda)[](https://kubernetes.slack.com/messages/CKZJ36A5D)

[Getting Started](https://keda.sh/docs/2.19/)

*   [Setup Autoscaling with KEDA](https://keda.sh/docs/2.19/setupscaler/)

    *   [Prerequisites](https://keda.sh/docs/2.19/setupscaler/#prerequisites)
    *   [Step 1: Identify the Scaler You Need](https://keda.sh/docs/2.19/setupscaler/#step-1-identify-the-scaler-you-need)
    *   [Step 2: Install the Required Scaler (if needed)](https://keda.sh/docs/2.19/setupscaler/#step-2-install-the-required-scaler-if-needed)
    *   [Step 3: Create a ScaledObject Configuration File](https://keda.sh/docs/2.19/setupscaler/#step-3-create-a-scaledobject-configuration-file)
    *   [Step 4: Apply the ScaledObject Configuration](https://keda.sh/docs/2.19/setupscaler/#step-4-apply-the-scaledobject-configuration)
    *   [Step 5: Monitor Scaling Events](https://keda.sh/docs/2.19/setupscaler/#step-5-monitor-scaling-events)

*   [Deploying KEDA](https://keda.sh/docs/2.19/deploy/)
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

Setup Autoscaling with KEDA Latest

Procedure to Setup a Scaler in KEDA

 Version  2.19  (latest) 

[2.20 (unreleased)](https://keda.sh/docs/2.20/setupscaler)[2.19 (latest)](https://keda.sh/docs/2.19/setupscaler)[2.18](https://keda.sh/docs/2.18/setupscaler)[2.17](https://keda.sh/docs/2.17/setupscaler)[2.16](https://keda.sh/docs/2.16/setupscaler)[2.15](https://keda.sh/docs/2.15/setupscaler)[2.14](https://keda.sh/docs/2.14/setupscaler)

[Suggest a change](https://github.com/kedacore/keda-docs/blob/main/content/docs/2.19/setupscaler.md)

Prerequisites [](https://keda.sh/docs/2.19/setupscaler/#prerequisites)
----------------------------------------------------------------------

1.   **Kubernetes Cluster**:

    *   Ensure you have a running Kubernetes cluster set up and accessible.
    *   If you don’t have a cluster yet, follow the [official Kubernetes documentation](https://kubernetes.io/docs/setup/) to create a new cluster suitable for your environment (local machine, cloud provider, etc.).

2.   **KEDA Installation**:

    *   KEDA needs to be installed on your Kubernetes cluster before you can use it.
    *   Follow the [KEDA installation guide](https://keda.sh/docs/2.19/deploy/) carefully, including any prerequisites specific to your Kubernetes setup.
    *   The installation guide provides instructions for different installation methods (e.g., YAML, Helm charts, etc.). Choose the method that suits your needs.

3.   **kubectl**:

    *   The `kubectl` command-line tool is required to interact with your Kubernetes cluster.
    *   Follow the [official kubectl installation guide](https://kubernetes.io/docs/tasks/tools/#kubectl) to install `kubectl` on your operating system.
    *   Once installed, configure `kubectl` to communicate with your Kubernetes cluster by following the cluster-specific instructions provided by your Kubernetes setup.

Step 1: Identify the Scaler You Need [](https://keda.sh/docs/2.19/setupscaler/#step-1-identify-the-scaler-you-need)
-------------------------------------------------------------------------------------------------------------------

KEDA supports various scalers that correspond to different event sources or triggers. Determining the right scaler is crucial for scaling your application based on the desired event source.

1.   Visit the [KEDA Scalers documentation](https://keda.sh/docs/2.19/scalers/) and browse through the list of available scalers.
2.   Identify the scaler that matches the event source you want to use for scaling your application. For example: 
    *   If you want to scale based on incoming HTTP traffic, you would need the [HTTP Add-on](https://kedacore.github.io/http-add-on/).

> **Note:** The HTTP Add-on is still in beta stage and may not provide the full functionality or stability expected in a production environment.

    *   If you want to scale based on messages in a RabbitMQ queue, you would need the **RabbitMQ scaler**.

    *   If you want to scale based on a cron schedule, you would need the **Cron scaler**.

3.   Open the documentation page for your chosen scaler and familiarize yourself with its specific requirements and configuration options.

Step 2: Install the Required Scaler (if needed) [](https://keda.sh/docs/2.19/setupscaler/#step-2-install-the-required-scaler-if-needed)
---------------------------------------------------------------------------------------------------------------------------------------

Some scalers are part of the core KEDA installation, while others need to be installed separately as add-ons.

1.   Refer to the documentation of your chosen scaler to check if it needs to be installed separately.
2.   If the scaler needs to be installed separately, follow the installation instructions provided in the scaler’s documentation carefully. 
    *   The installation process typically involves running a command (e.g., `helm install` for Helm charts) or applying YAML manifests using `kubectl`.

3.   Verify that the scaler has been installed successfully by checking the output of the installation process or by running any provided verification commands.

Step 3: Create a ScaledObject Configuration File [](https://keda.sh/docs/2.19/setupscaler/#step-3-create-a-scaledobject-configuration-file)
-------------------------------------------------------------------------------------------------------------------------------------------

KEDA uses a custom resource called `ScaledObject` to define how your application should be scaled based on the chosen event source or trigger.

1.   Create a new file (e.g., `scaledobject.yaml`) in a text editor or using the command line.
2.   Define the `ScaledObject` configuration in this file, following the structure and examples provided in the documentation of your chosen scaler.
3.   Typically, the `ScaledObject` configuration includes the following sections: 
    *   `metadata`: Specifies the name and namespace for the `ScaledObject`.
    *   `spec.scaleTargetRef`: Identifies the Kubernetes deployment or other resource that should be scaled.
    *   `spec.pollingInterval` (optional): Specifies how often KEDA should check for scaling events (defaults to 15 seconds).
    *   `spec.cooldownPeriod` (optional): Specifies the cool-down period in seconds after a scaling event (defaults to 300 seconds).
    *   `spec.maxReplicaCount` (optional): Specifies the maximum number of replicas to scale up to (defaults to 100).
    *   `spec.triggers`: Defines the specific configuration for your chosen scaler, including any required parameters or settings.

4.   Refer to the scaler’s documentation for detailed explanations and examples of the `triggers` section and any other required or optional configuration settings.
5.   Save the `scaledobject.yaml` file after making the necessary modifications.

Step 4: Apply the ScaledObject Configuration [](https://keda.sh/docs/2.19/setupscaler/#step-4-apply-the-scaledobject-configuration)
-----------------------------------------------------------------------------------------------------------------------------------

Once you have created the `ScaledObject` configuration file, apply it to your Kubernetes cluster using `kubectl`:

1.   Open a terminal or command prompt and navigate to the directory containing the `scaledobject.yaml` file.

2.   Run the following command to apply the `ScaledObject` configuration:

```bash
kubectl apply -f scaledobject.yaml
``` ```plaintext
scaledobject.keda.sh/<scaled-object-name> created
``` 
3.   Verify that the `ScaledObject` has been created successfully by running:

```bash
kubectl get scaledobjects
``` 
This should display the `ScaledObject` you just created.

```plaintext
NAME              SCALETARGETKIND   SCALETARGETNAME   MIN   MAX   TRIGGERS   AUTHENTICATION   READY   ACTIVE   FALLBACK   AGE
<scaled-object-name>   Deployment        <deployment-name>   1     10    cpu                    <none>            True    False    <none>      10s
``` 

After applying the `ScaledObject` configuration, KEDA will start monitoring the specified event source and scale your application accordingly, based on the configurations you provided.

Step 5: Monitor Scaling Events [](https://keda.sh/docs/2.19/setupscaler/#step-5-monitor-scaling-events)
-------------------------------------------------------------------------------------------------------

You can monitor the scaling events and logs generated by KEDA using the following commands:

1.   List all `ScaledObjects` in your cluster:

```bash
kubectl get scaledobjects
``` 
This will show you the current state of your `ScaledObject` and the number of replicas.

```plaintext
NAME              SCALETARGETKIND   SCALETARGETNAME   MIN   MAX   TRIGGERS   AUTHENTICATION   READY   ACTIVE   FALLBACK   AGE
<scaled-object-name>   Deployment        <deployment-name>   1     10    cpu                    <none>            True    False    <none>      10s
``` 
2.   View the logs of the KEDA operator:

```bash
kubectl logs -n keda -l app=keda-operator
``` 
The KEDA operator logs will show you detailed information about scaling events, decisions made by KEDA based on the event source, and any errors or warnings.

```plaintext
{"level":"info","ts":<timestamp>,"logger":"scalehandler","msg":"Successfully scaled deployment","scaledobject.Namespace":"<namespace>","scaledobject.Name":"<scaled-object-name>","scaler":<scaler-type>}
``` 

![Image 2: KEDA Logo](https://keda.sh/img/logos/keda-icon-white.png)

[Blog](https://keda.sh/blog)

[Community](https://keda.sh/docs/2.19/setupscaler/)

[Project](https://keda.sh/docs/2.19/setupscaler/)

[Enterprise](https://keda.sh/enterprise/)

[Twitter](https://twitter.com/kedaorg)[GitHub](https://github.com/kedacore/keda)[Slack](https://kubernetes.slack.com/messages/CKZJ36A5D)

© KEDA Authors 2014-2026 | Documentation Distributed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0)

![Image 3](https://static.scarf.sh/a.png?x-pxid=46ce89e3-f6ce-454e-9740-490aaee3da5e)

© 2026 [The Linux Foundation](https://linuxfoundation.org/). All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage) page.
