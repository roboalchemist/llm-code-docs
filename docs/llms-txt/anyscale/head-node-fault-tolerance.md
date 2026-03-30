# Source: https://docs.anyscale.com/administration/resource-management/head-node-fault-tolerance.md

# Configure head node fault tolerance

[View Markdown](/administration/resource-management/head-node-fault-tolerance.md)

# Configure head node fault tolerance

This page provides an overview of configuring head node fault tolerance for Anyscale services. Anyscale recommends enabling head node fault tolerance for all production services.

Anyscale recommends configuring head node fault tolerance at the cloud level for cloud resources configured with the virtual machine (VM) stack. See [Enable head node fault tolerance for an Anyscale cloud](#enable).

Kubernetes deployments don't support cloud-level fault tolerance configuration. You must provision your own Redis-compatible cluster and configure `ray_gcs_external_storage_config` in each service config. See [Manually configure fault tolerance for an Anyscale service](#manual).

important

Head node fault tolerance isn't supported for serverless Anyscale clouds (also called Anyscale-hosted clouds).

## What is head node fault tolerance?[​](#what-is-head-node-fault-tolerance "Direct link to What is head node fault tolerance?")

Head node fault tolerance uses a Redis-compatible external storage cluster to prevent service outages due to head node instability, out-of-memory issues, or machine failure.

With head node fault tolerance enabled, Anyscale services can continue to serve responses using replicas on worker nodes during head node recovery.

## Enable head node fault tolerance for an Anyscale cloud[​](#enable "Direct link to Enable head node fault tolerance for an Anyscale cloud")

Anyscale recommends that you enable head node fault tolerance at the cloud level. When you enable head node fault tolerance for an Anyscale cloud, all services deployed in that cloud use the feature by default.

important

When you enable head node fault tolerance, Anyscale deploys additional resources in your cloud provider account that have ongoing costs. While Anyscale doesn't charge for these resources, they incur charges in your cloud provider account even if you aren't using Anyscale services.

* Anyscale clouds on AWS use MemoryDB with 2 GiB of memory and a replica. See [Amazon MemoryDB pricing](https://aws.amazon.com/memorydb/pricing/).
* Anyscale clouds on Google Cloud use Memorystore with 5 GiB of memory and a replica. See [Memorystore for Redis Cluster pricing](https://cloud.google.com/memorystore/docs/cluster/pricing).

If you need help disabling head node fault tolerance, contact [Anyscale support](mailto:support@anyscale.com).

If you use `anyscale cloud setup` to deploy an Anyscale cloud on the VM stack, you can enable head node fault tolerance during cloud deployment by including the flag `--enable-head-node-fault-tolerance`. Anyscale automatically configures MemoryDB or Memorystore in your cloud provider account.

You can update an existing Anyscale cloud to enable fault tolerance by running the following command:

```
anyscale cloud update --name <cloud-name> --enable-head-node-fault-tolerance
```

Anyscale provides Terraform modules to help you configure and deploy custom Anyscale clouds on AWS and Google Cloud. You can use these scripts to help configure Redis-compatible storage for use with `anyscale cloud register`.

See [Introduction to Anyscale clouds](/admin/cloud.md).

### Turn off head node fault tolerance for a service[​](#turn-off-head-node-fault-tolerance-for-a-service "Direct link to Turn off head node fault tolerance for a service")

You can turn off head node fault tolerance for a service in your Anyscale cloud by using the `ray_gcs_external_storage_config` in the service config, as in the following example:

```
name: my-service
applications:
  - import_path: main:app
ray_gcs_external_storage_config:
  enabled: False
```

Disabling fault tolerance using the service config doesn't remove the Redis-compatible cluster from your Anyscale cloud deployment or deprovision resources in your cloud provider. If you need help removing this infrastructure, contact [Anyscale support](mailto:support@anyscale.com).

## Manually configure fault tolerance for an Anyscale service[​](#manual "Direct link to Manually configure fault tolerance for an Anyscale service")

This section covers manually provisioning a Redis-compatible cluster and configuring fault tolerance at the service level. You must follow these instructions to use head node fault tolerance with Anyscale cloud resources deployed on Kubernetes.

note

Anyscale recommends configuring head node fault tolerance at the cloud level for clouds deployed with the VM stack. See [Enable head node fault tolerance for an Anyscale cloud](#enable).

Cloud-level configuration shares a single Redis cluster across all services in your Anyscale cloud, which is sufficient for most use cases. Only use per-service configuration if you need dedicated Redis clusters for specific services.

### Requirements[​](#requirements "Direct link to Requirements")

Your Redis-compatible cluster must meet the following requirements:

note

You can't use a multi-shard Redis cluster. Anyscale only supports single shard Redis clusters and recommends replication across availability zones.

Anyscale doesn't support TLS for Google Cloud Memorystore.

* Kubernetes
* VM stack

- Accessible from your Kubernetes cluster's network.
- Single shard configuration.
- At least 1 replica for high availability.
- At least 1 GiB of storage.
  <!-- -->
  * A 10-node service initially requires around 20 MB of storage. Over time, the usage for a cluster can increase to 100 MB or more.

* Created in the same cloud region as your Anyscale cloud.
* Created inside the Anyscale-managed VPC using the Anyscale-managed security group (`anyscale-security-group`).
* Single shard configuration.
* At least 1 replica for high availability.
* At least 1 GiB of storage.
  <!-- -->
  * A 10-node service initially requires around 20 MB of storage. Over time, the usage for a cluster can increase to 100 MB or more.

### Configure fault tolerance in your service config[​](#service-config "Direct link to Configure fault tolerance in your service config")

Once you have provisioned a Redis-compatible cluster, add the [RayGCSExternalStorageConfig](/reference/service-api.md#raygcsexternalstorageconfig) config to the [ServiceConfig](/reference/service-api.md#serviceconfig) to enable head node fault tolerance, as in the following examples:

* YAML
* Python

```
name: my-service
working_dir: .
applications:
  - import_path: main:app
ray_gcs_external_storage_config:
  enabled: True
  address: redis-cluster-hostname:6379
  # Path to TLS certificates if enabled.
  certificate_path: "/etc/ssl/certs/ca-certificates.crt"
```

```
from anyscale.service.models import ServiceConfig, RayGCSExternalStorageConfig

config = ServiceConfig(
  name="my-service",
  working_dir=".",
  applications=[{"import_path": "main:app"}],
  ray_gcs_external_storage_config=RayGCSExternalStorageConfig(
    enabled=True,
    address="redis-cluster-hostname:6379",
    certificate_path="/etc/ssl/certs/ca-certificates.crt",
  ),
)
```

* Use the following address pattern for Google Cloud Memorystore: `<ip-address>:<port>`
* Use the following address pattern for AWS MemoryDB: `<user-provided-name>.<random-string>.clustercfg.memorydb.<region>.amazonaws.com:6379`
* If you have TLS enabled, prefix the address with `rediss://`. For example: `rediss://<user-provided-name>.<random-string>.clustercfg.memorydb.<region>.amazonaws.com:6379`.
* The `certificate_path` only needs to be updated when using private certificates.

## Configure alerting for your fault tolerance resources[​](#alerting "Direct link to Configure alerting for your fault tolerance resources")

If the Redis-compatible external storage cluster reaches its maximum memory capacity, your services may experience significant disruptions. Anyscale recommends configuring alerts using either [AWS CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) or [Google Cloud Alerting](https://cloud.google.com/monitoring/alerts).

* AWS
* Google Cloud

AWS CloudWatch Alerts

* Configure an alert on the `DatabaseMemoryUsagePercentage` metric.
* Configure the alert condition to trigger if the maximum value exceeds 80%.

Google Cloud Alerting

* Configure an alert on the `Cloud Memorystore Redis Instance - Memory Usage Ratio` metric.
* Configure the alert condition to trigger if the maximum value exceeds 80%.

If the alarm triggers, Anyscale recommends either terminating services to alleviate the memory load or scaling up the Redis-compatible cluster's memory capacity.
