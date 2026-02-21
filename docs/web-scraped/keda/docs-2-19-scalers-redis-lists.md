# Source: https://keda.sh/docs/2.19/scalers/redis-lists/

Title: KEDA | Redis Lists

URL Source: https://keda.sh/docs/2.19/scalers/redis-lists/

Markdown Content:
Redis Lists | KEDA
===============

[![Image 1: Keda logo](https://keda.sh/img/logos/keda-horizontal-color.png)](https://keda.sh/)[](https://keda.sh/docs/2.19/scalers/redis-lists/)

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

[Community](https://keda.sh/docs/2.19/scalers/redis-lists/)

[Overview](https://keda.sh/community/)[Get Involved](https://keda.sh/community/#get-involved)[End-Users](https://keda.sh/community/#end-users)[Partners](https://keda.sh/community/#partners)[Supported by](https://keda.sh/community/#supported-by)[Videos](https://keda.sh/videos/)[Samples](https://github.com/kedacore/samples)

[Project](https://keda.sh/docs/2.19/scalers/redis-lists/)

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

    *           *   [Trigger Specification](https://keda.sh/docs/2.19/scalers/redis-lists/#trigger-specification)
        *   [Authentication Parameters](https://keda.sh/docs/2.19/scalers/redis-lists/#authentication-parameters)
        *   [Example](https://keda.sh/docs/2.19/scalers/redis-lists/#example)

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

Redis Lists Latest

Scale applications based on Redis Lists.

 Availability:v1.0+ Maintainer:Community

[Scaler code](https://github.com/kedacore/keda/blob/main/pkg/scalers/redis_scaler.go)

 Version  2.19  (latest) 

[2.20 (unreleased)](https://keda.sh/docs/2.20/scalers/redis-lists)[2.19 (latest)](https://keda.sh/docs/2.19/scalers/redis-lists)[2.18](https://keda.sh/docs/2.18/scalers/redis-lists)[2.17](https://keda.sh/docs/2.17/scalers/redis-lists)[2.16](https://keda.sh/docs/2.16/scalers/redis-lists)[2.15](https://keda.sh/docs/2.15/scalers/redis-lists)[2.14](https://keda.sh/docs/2.14/scalers/redis-lists)[2.13](https://keda.sh/docs/2.13/scalers/redis-lists)[2.12](https://keda.sh/docs/2.12/scalers/redis-lists)[2.11](https://keda.sh/docs/2.11/scalers/redis-lists)[2.10](https://keda.sh/docs/2.10/scalers/redis-lists)[2.9](https://keda.sh/docs/2.9/scalers/redis-lists)[2.8](https://keda.sh/docs/2.8/scalers/redis-lists)[2.7](https://keda.sh/docs/2.7/scalers/redis-lists)[2.6](https://keda.sh/docs/2.6/scalers/redis-lists)[2.5](https://keda.sh/docs/2.5/scalers/redis-lists)[2.4](https://keda.sh/docs/2.4/scalers/redis-lists)[2.3](https://keda.sh/docs/2.3/scalers/redis-lists)[2.2](https://keda.sh/docs/2.2/scalers/redis-lists)[2.1](https://keda.sh/docs/2.1/scalers/redis-lists)[2.0](https://keda.sh/docs/2.0/scalers/redis-lists)[1.5](https://keda.sh/docs/1.5/scalers/redis-lists)[1.4](https://keda.sh/docs/1.4/scalers/redis-lists)

[Suggest a change](https://github.com/kedacore/keda-docs/blob/main/content/docs/2.19/scalers/redis-lists.md)

### Trigger Specification [](https://keda.sh/docs/2.19/scalers/redis-lists/#trigger-specification)

This specification describes the `redis` trigger that scales based on the length of a list in Redis.

```yaml
triggers:
- type: redis
  metadata:
    address: localhost:6379 # Format must be host:port
    usernameFromEnv: REDIS_USERNAME # optional
    passwordFromEnv: REDIS_PASSWORD
    listName: mylist # Required
    listLength: "5" # Required
    activationListLength: "5" # optional
    enableTLS: "false" # optional
    unsafeSsl: "false" # optional
    databaseIndex: "0" # optional
    # Alternatively, you can use existing environment variables to read configuration from:
    # See details in "Parameter list" section
    addressFromEnv: REDIS_HOST # Optional. You can use this instead of `address` parameter
```

**Parameter list:**

*   `address` - The host and port of the Redis server.
*   `host` - The host of the Redis server. Alternative to `address` and requires `port` to be configured as well.
*   `port` - The port of the Redis server. Alternative to `address` and requires `host` to be configured as well.
*   `usernameFromEnv` - Environment variable to read the authentication username from to authenticate with the Redis server.
*   `passwordFromEnv` - Environment variable to read the authentication password from to authenticate with the Redis server. 
    *   Both the hostname, username and password fields need to be set to the names of the environment variables in the target deployment that contain the host name, username and password respectively.

*   `listName` - Name of the Redis List that you want to monitor.
*   `listLength` - Average target value to trigger scaling actions.
*   `activationListLength` - Target value for activating the scaler. Learn more about activation [here](https://keda.sh/docs/2.19/concepts/scaling-deployments/#activating-and-scaling-thresholds). (Default: `0`, Optional)
*   `enableTLS` - Allow a connection to a redis queue using tls. (Values: `true`, `false`, Default: `false`, Optional)
*   `unsafeSsl` - Used for skipping certificate check e.g: using self-signed certs. (Values: `true`,`false`, Default: `false`, Optional, This requires `enableTLS: true`)
*   `databaseIndex` - Index of Redis database to use. If not specified, the default value is 0.

Some parameters could be provided using environmental variables, instead of setting them directly in metadata. Here is a list of parameters you can use to retrieve values from environment variables:

*   `addressFromEnv` - The host and port of the Redis server, similar to `address`, but reads it from an environment variable on the scale target.
*   `hostFromEnv` - The host of the Redis server, similar to `host`, but reads it from an environment variable on the scale target.
*   `portFromEnv` - The port of the Redis server, similar to `port`, but reads it from an environment variable on the scale target.

### Authentication Parameters [](https://keda.sh/docs/2.19/scalers/redis-lists/#authentication-parameters)

You can authenticate by using a username (optional) and password.

**Connection Authentication:**

*   `address` - The hostname and port for the Redis server (host:port format).
*   `host` - The hostname of the Redis server. If specified, the `port` should also be specified.
*   `port` - The port of the Redis server. If specified, the `host` should also be specified.

**TLS:**

Parameters used for configuring TLS authentication. Note this can not be used together with `enableTLS` and `unsafeSsl` on the `ScaledObject`, which is used to define using insecure TLS with skipping certificate check.

*   `tls` - To enable SSL auth for Redis, set this to `enable`. If not set, TLS for Redis is not used. (Values: `enable`, `disable`, Default: `disable`, Optional)
*   `ca` - Certificate authority file for TLS authentication. (Optional)
*   `cert` - Certificate for client authentication. (Optional)
*   `key` - Key for client authentication. (Optional)
*   `keyPassword` - If set the `keyPassword` is used to decrypt the provided `key`. (Optional)

**Authentication:**

*   `username` - Redis username to authenticate with.
*   `password` - Redis password to authenticate with.

### Example [](https://keda.sh/docs/2.19/scalers/redis-lists/#example)

Here is an example of how to deploy a scaled object with the `redis` scale trigger which uses `TriggerAuthentication`.

You can also provide the `usernameFromEnv` and `passwordFromEnv` on the `ScaledObject` directly.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: votes-db-secret
  namespace: my-project
type: Opaque
data:
  redis_username: YWRtaW4=
  redis_password: YWRtaW4=
---
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-redis-secret
  namespace: my-project
spec:
  secretTargetRef:
  - parameter: username
    name: votes-db-secret
    key: redis_username
  - parameter: password
    name: votes-db-secret
    key: redis_password
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: redis-scaledobject
  namespace: my-project
spec:
  scaleTargetRef:
    name: votes
  triggers:
  - type: redis
    metadata:
      address: localhost:6379
      listName: mylist
      listLength: "10"
    authenticationRef:
      name: keda-trigger-auth-redis-secret
```

![Image 2: KEDA Logo](https://keda.sh/img/logos/keda-icon-white.png)

[Blog](https://keda.sh/blog)

[Community](https://keda.sh/docs/2.19/scalers/redis-lists/)

[Project](https://keda.sh/docs/2.19/scalers/redis-lists/)

[Enterprise](https://keda.sh/enterprise/)

[Twitter](https://twitter.com/kedaorg)[GitHub](https://github.com/kedacore/keda)[Slack](https://kubernetes.slack.com/messages/CKZJ36A5D)

© KEDA Authors 2014-2026 | Documentation Distributed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0)

![Image 3](https://static.scarf.sh/a.png?x-pxid=46ce89e3-f6ce-454e-9740-490aaee3da5e)

© 2026 [The Linux Foundation](https://linuxfoundation.org/). All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage](https://linuxfoundation.org/trademark-usage) page.
