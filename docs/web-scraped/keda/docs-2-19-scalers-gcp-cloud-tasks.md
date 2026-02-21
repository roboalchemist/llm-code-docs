# Source: https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/

Title: KEDA | Google Cloud Platform Cloud Tasks

URL Source: https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/

Markdown Content:
Google Cloud Platform Cloud Tasks | KEDA
===============

[![Image 1: Keda logo](https://keda.sh/img/logos/keda-horizontal-color.png)](https://keda.sh/)[](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/)

Search

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

[Community](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/)

[Overview](https://keda.sh/community/)[Get Involved](https://keda.sh/community/#get-involved)[End-Users](https://keda.sh/community/#end-users)[Partners](https://keda.sh/community/#partners)[Supported by](https://keda.sh/community/#supported-by)[Videos](https://keda.sh/videos/)[Samples](https://github.com/kedacore/samples)

[Project](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/)

[Support](https://keda.sh/support/)[Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md)[Changelog](https://github.com/kedacore/keda/blob/main/CHANGELOG.md)[Governance](https://github.com/kedacore/governance/blob/main/GOVERNANCE.md)[Roadmap](https://github.com/kedacore/keda/blob/main/ROADMAP.md)[Breaking Changes & Deprecations](https://github.com/kedacore/governance/blob/main/DEPRECATIONS.md)[Contributing](https://github.com/kedacore/keda/blob/main/CONTRIBUTING.md)[Colors and Logos](https://github.com/kedacore/governance/blob/main/BRANDING.md)[License](https://github.com/kedacore/keda/blob/main/LICENSE)[Maintainers](https://github.com/kedacore/governance/blob/main/MEMBERS.md)[Learning Resources](https://keda.sh/resources/)[Merch](https://store.cncf.io/collections/keda)

[Enterprise](https://keda.sh/enterprise/)

[](https://twitter.com/kedaorg)[](https://github.com/kedacore/keda)[](https://kubernetes.slack.com/messages/CKZJ36A5D)

[Getting Started](https://keda.sh/docs/2.19/)

*   [Setup Autoscaling with KEDA](https://keda.sh/docs/2.19/setupscaler/)
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

    *           *   [Trigger Specification](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#trigger-specification)
        *   [Authentication Parameters](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#authentication-parameters)
        *   [Example](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example)
        *   [Example using TriggerAuthentication](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example-using-triggerauthentication)
        *   [Example using TriggerAuthentication with GCP Identity](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example-using-triggerauthentication-with-gcp-identity)

    *   [Example using ClusterTriggerAuthentication with GCP Identity](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example-using-clustertriggerauthentication-with-gcp-identity)

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

Google Cloud Platform Cloud Tasks Latest

Scale applications based on Google Cloud Platform Cloud Tasks.

 Availability:v2.12+ Maintainer:Community

[Scaler code](https://github.com/kedacore/keda/blob/main/pkg/scalers/gcp_cloud_tasks_scaler.go)

 Version  2.19  (latest) 

[2.20 (unreleased)](https://keda.sh/docs/2.20/scalers/gcp-cloud-tasks)[2.19 (latest)](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks)[2.18](https://keda.sh/docs/2.18/scalers/gcp-cloud-tasks)[2.17](https://keda.sh/docs/2.17/scalers/gcp-cloud-tasks)[2.16](https://keda.sh/docs/2.16/scalers/gcp-cloud-tasks)[2.15](https://keda.sh/docs/2.15/scalers/gcp-cloud-tasks)[2.14](https://keda.sh/docs/2.14/scalers/gcp-cloud-tasks)[2.13](https://keda.sh/docs/2.13/scalers/gcp-cloud-tasks)[2.12](https://keda.sh/docs/2.12/scalers/gcp-cloud-tasks)

[Suggest a change](https://github.com/kedacore/keda-docs/blob/main/content/docs/2.19/scalers/gcp-cloud-tasks.md)

> 💡 **WARNING:** This scaler is deprecated and won’t receive any modification. [Read more about it here](https://keda.sh/blog/2025-09-15-gcp-deprecations/).

### Trigger Specification [](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#trigger-specification)

This specification describes the `gcp-cloudtasks` trigger for Google Cloud Platform Cloud Tasks.

```yaml
triggers:
- type: gcp-cloudtasks
  metadata:
    value: "5" # Optional - Default is 100
    activationValue: "10.5" # Optional - Default is 0
    filterDuration: '1' # Optional - Default is 2
    queueName: "myqueue" # Required
    projectID: "myproject" # Required, the project where the queue resides
    credentialsFromEnv: GOOGLE_APPLICATION_CREDENTIALS_JSON # Required
```

The Google Cloud Platform (GCP) Cloud Tasks trigger allows you to scale based on the number of tasks queued in you queue.

The `credentialsFromEnv` property maps to the name of an environment variable in the scale target (`scaleTargetRef`) that contains the service account credentials (JSON). KEDA will use those to connect to Google Cloud Platform and collect the required stack driver metrics in order to read the number of messages in the Cloud Task queue.

*   `value` - Target value for the scaler. (Default: `100`, Optional, This value can be a float)
*   `activationValue` - Target value for activating the scaler. Learn more about activation [here](https://keda.sh/docs/2.19/concepts/scaling-deployments/#activating-and-scaling-thresholds). (Default: `0`, Optional, This value can be a float)
*   `queueName` defines the queue that should be monitored.
*   `projectID` defines the GCP project where the queue that should be monitored resides.
*   `filterDuration` - Duration (in minutes) for filtering metrics. (Default: `2`)

### Authentication Parameters [](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#authentication-parameters)

You can use `TriggerAuthentication` CRD to configure the authenticate by providing the service account credentials in JSON.

**Credential based authentication:**

*   `GoogleApplicationCredentials` - Service account credentials in JSON.

### Example [](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example)

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cloudtasks-scaledobject
  namespace: keda-cloudtasks-test
spec:
  scaleTargetRef:
    name: keda-cloudtasks-go
  triggers:
  - type: gcp-cloudtasks
    metadata:
      activationValue: "5"
      projectID: "myproject" # Required
      queueName: "myqueue" # Required
      credentialsFromEnv: GOOGLE_APPLICATION_CREDENTIALS_JSON # Required
```

### Example using TriggerAuthentication [](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example-using-triggerauthentication)

```yaml
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-gcp-credentials
spec:
  secretTargetRef:
  - parameter: GoogleApplicationCredentials
    name: cloudtasks-secret        # Required. Refers to the name of the secret
    key: GOOGLE_APPLICATION_CREDENTIALS_JSON       # Required.
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cloudtasks-scaledobject
spec:
  scaleTargetRef:
    name: keda-cloudtasks-go
  triggers:
  - type: gcp-cloudtasks
    authenticationRef:
      name: keda-trigger-auth-gcp-credentials
    metadata:
      activationValue: "5"
      projectID: "myproject" # Required
      queueName: "myqueue" # Required
```

**Identity based authentication:**

You can also use `TriggerAuthentication` CRD to configure the authentication using the associated service account of the running machine in Google Cloud. You only need to create a `TriggerAuthentication` as this example, and reference it in the `ScaledObject`. `ClusterTriggerAuthentication` can also be used if you intend to use it globally in your cluster.

### Example using TriggerAuthentication with GCP Identity [](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example-using-triggerauthentication-with-gcp-identity)

```yaml
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-gcp-credentials
spec:
  podIdentity:
    provider: gcp
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cloudtasks-scaledobject
spec:
  scaleTargetRef:
    name: keda-cloudtasks-go
  triggers:
  - type: gcp-cloudtasks
    authenticationRef:
      name: keda-trigger-auth-gcp-credentials
    metadata:
      activationValue: "5"
      projectID: "myproject" # Required
      queueName: "myqueue" # Required
```

Example using ClusterTriggerAuthentication with GCP Identity [](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/#example-using-clustertriggerauthentication-with-gcp-identity)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```yaml
apiVersion: keda.sh/v1alpha1
kind: ClusterTriggerAuthentication
metadata:
  name: keda-clustertrigger-auth-gcp-credentials
spec:
  podIdentity:
    provider: gcp
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cloudtasks-scaledobject
spec:
  scaleTargetRef:
    name: keda-cloudtasks-go
  triggers:
  - type: gcp-cloudtasks
    authenticationRef:
      name: keda-clustertrigger-auth-gcp-credentials
      kind: ClusterTriggerAuthentication
    metadata:
      activationValue: "5"
      projectID: "myproject" # Required
      queueName: "myqueue" # Required
```

![Image 2: KEDA Logo](https://keda.sh/img/logos/keda-icon-white.png)

[Blog](https://keda.sh/blog)

[Community](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/)

[Project](https://keda.sh/docs/2.19/scalers/gcp-cloud-tasks/)

[Enterprise](https://keda.sh/enterprise/)

[Twitter](https://twitter.com/kedaorg)[GitHub](https://github.com/kedacore/keda)[Slack](https://kubernetes.slack.com/messages/CKZJ36A5D)

© KEDA Authors 2014-2026 | Documentation Distributed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0)

![Image 3](https://static.scarf.sh/a.png?x-pxid=46ce89e3-f6ce-454e-9740-490aaee3da5e)

© 2026 [The Linux Foundation](https://linuxfoundation.org/). All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage) page.
