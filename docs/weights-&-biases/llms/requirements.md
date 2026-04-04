# Source: https://docs.wandb.ai/platform/hosting/self-managed/requirements.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-Managed infrastructure requirements

> Infrastructure and software requirements for W&B Self-Managed deployments

This page provides a comprehensive overview of the infrastructure and software requirements for deploying W\&B Self-Managed. Review these requirements before beginning your deployment.

<Note>
  W\&B recommends fully managed deployment options such as [W\&B Multi-tenant Cloud](/platform/hosting/hosting-options/multi_tenant_cloud) or [W\&B Dedicated Cloud](/platform/hosting/hosting-options/dedicated-cloud) deployment types. W\&B fully managed services are simple and secure to use, with minimum to no configuration required.
</Note>

For complete architectural guidance, see the [reference architecture](/platform/hosting/self-managed/ref-arch/).

## Software version requirements

| Software   | Minimum version                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes | v1.32 or newer ([Supported Kubernetes versions](https://kubernetes.io/releases/patch-releases/))                                |
| Helm       | v3.x                                                                                                                            |
| MySQL      | v8.0.x is required, v8.0.32 or newer; v8.0.44 or newer is recommended.<br />Aurora MySQL 3.x releases, must be v3.05.2 or newer |
| Redis      | v7.x                                                                                                                            |

## Hardware requirements

**CPU Architecture**: W\&B runs on Intel (x86) CPU architecture only. ARM is not supported.

**Sizing**: For CPU, memory, and disk sizing recommendations for Kubernetes nodes and MySQL, see the [Sizing section](/platform/hosting/self-managed/ref-arch/#sizing) in the reference architecture. Requirements vary based on whether you're running Models, Weave, or both.

For detailed sizing recommendations based on your use case (Models only, Weave only, or both), see the [reference architecture sizing section](/platform/hosting/self-managed/ref-arch/#sizing).

## Kubernetes

W\&B Server is deployed as a [Kubernetes Operator](/platform/hosting/self-managed/operator/) that manages multiple pods. Your Kubernetes cluster must meet these requirements:

* **Version**: See [Software version requirements](#software-version-requirements) above
* **Ingress controller**: A fully-configured and functioning ingress controller (Nginx, Istio, Traefik, or cloud provider ingress)
* **Persistent volumes**: Capability to provision persistent volumes
* **CPU architecture**: Intel or AMD 64-bit (ARM is not supported)

W\&B supports deployment on [OpenShift Kubernetes clusters](https://www.redhat.com/en/technologies/cloud-computing/openshift) in cloud, on-premises, and air-gapped environments. For specific configuration instructions, see the [OpenShift section](/platform/hosting/self-managed/operator/#openshift-kubernetes-clusters) in the Operator guide.

For complete Kubernetes requirements, including load balancer and ingress configuration, see the [reference architecture Kubernetes section](/platform/hosting/self-managed/ref-arch/#kubernetes).

## MySQL database

W\&B requires an external MySQL database.

For production, W\&B strongly recommends using managed database services:

* [AWS RDS Aurora MySQL](https://aws.amazon.com/rds/aurora/)
* [Google Cloud SQL for MySQL](https://cloud.google.com/sql/mysql)
* [Azure Database for MySQL](https://azure.microsoft.com/en-us/products/mysql/)

Managed database services provide automated backups, monitoring, high availability, patching, and reduce operational overhead.

See the [reference architecture](/platform/hosting/self-managed/ref-arch/#mysql) for complete MySQL requirements, including sizing recommendations and configuration parameters. For database creation SQL, see the [bare-metal guide](/platform/hosting/self-managed/bare-metal/#mysql-database). For questions about your deployment's database configuration, contact [support](mailto:support@wandb.com) or your AISE.

**W\&B strongly recommends using managed database services** such as AWS RDS Aurora MySQL, Google Cloud SQL for MySQL, or Azure Database for MySQL for production deployments. Managed services provide automated backups, monitoring, high availability, patching, and significantly reduce operational complexity.

### MySQL configuration parameters

If you are running your own MySQL instance, configure MySQL with these settings:

```
binlog_format = 'ROW'
binlog_row_image = 'MINIMAL'
innodb_flush_log_at_trx_commit = 1
innodb_online_alter_log_max_size = 268435456
max_prepared_stmt_count = 1048576
sort_buffer_size = '67108864'
sync_binlog = 1
```

These settings have been validated by W\&B for optimal performance and reliability.

### Database creation

For instructions to manually create the MySQL database and user:

Create a database and a user with the following SQL commands. Replace `SOME_PASSWORD` with a secure password of your choice:

```sql  theme={null}
CREATE USER 'wandb_local'@'%' IDENTIFIED BY 'SOME_PASSWORD';
CREATE DATABASE wandb_local CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
GRANT ALL ON wandb_local.* TO 'wandb_local'@'%' WITH GRANT OPTION;
```

For additional considerations, including backups, performance, monitoring, and availability, see the [reference architecture MySQL section](/platform/hosting/self-managed/ref-arch/#mysql).

## Redis

W\&B depends on a single-node Redis 7.x deployment used by W\&B's components for job queuing and data caching. For convenience during testing and development of proofs of concept, W\&B Self-Managed includes a local Redis deployment that is not appropriate for production deployments.

For production deployments, W\&B can connect to a Redis instance in the following environments:

* [AWS Elasticache](https://aws.amazon.com/elasticache/)
* [Google Cloud Memory Store](https://cloud.google.com/memorystore?hl=en)
* [Azure Cache for Redis](https://azure.microsoft.com/en-us/products/cache)
* Redis deployment hosted in your cloud or on-premise infrastructure

W\&B can connect to a Redis instance in the following environments:

* [AWS Elasticache](https://aws.amazon.com/pm/elasticache/)
* [Google Cloud Memory Store](https://cloud.google.com/memorystore?hl=en)
* [Azure Cache for Redis](https://azure.microsoft.com/en-us/products/cache)
* Redis deployment hosted in your cloud or on-premises infrastructure

## Object storage

W\&B requires object storage with pre-signed URL and CORS support.

**Recommended storage providers:**

* [Amazon S3](https://aws.amazon.com/s3/): Object storage service offering industry-leading scalability, data availability, security, and performance.
* [Google Cloud Storage](https://cloud.google.com/storage): Managed service for storing unstructured data at scale.
* [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs): Cloud-based object storage solution for storing massive amounts of unstructured data.
* [CoreWeave AI Object Storage](https://docs.coreweave.com/products/storage/object-storage): High-performance, S3-compatible object storage service optimized for AI workloads.
* Enterprise S3-compatible storage: [MinIO Enterprise (AIStor)](https://www.min.io/product/aistor), [NetApp StorageGRID](https://www.netapp.com/data-storage/storagegrid/), or other enterprise-grade solutions

<Note>
  MinIO Open Source is in [maintenance mode](https://github.com/minio/minio) with no active development or pre-compiled binaries. For production deployments, W\&B recommends using managed object storage services or enterprise S3-compatible solutions such as MinIO Enterprise (AIStor).
</Note>

For detailed bucket provisioning instructions including IAM policies, CORS configuration, and access setup, see the [Bring Your Own Bucket (BYOB) guide](/platform/hosting/data-security/secure-storage-connector).

See the [reference architecture object storage section](/platform/hosting/self-managed/ref-arch/#object-storage) for complete requirements.

### Provision your storage bucket

Before configuring W\&B, provision your object storage bucket with proper IAM policies, CORS configuration, and access credentials.

**See the [Bring Your Own Bucket (BYOB) guide](/platform/hosting/data-security/secure-storage-connector) for detailed step-by-step provisioning instructions for:**

* Amazon S3 (including IAM policies and bucket policies)
* Google Cloud Storage (including PubSub notifications)
* Azure Blob Storage (including managed identities)
* CoreWeave AI Object Storage
* S3-compatible storage (MinIO Enterprise, NetApp StorageGRID, and other enterprise solutions)

### Configure W\&B to use your bucket

After provisioning your bucket, configure W\&B to use it through the Operator's Helm values. See the [Operator object storage configuration section](/platform/hosting/self-managed/operator/#object-storage-bucket) for details.

## Networking

For a networked deployment, egress to these endpoints is required during *both* installation and runtime:

* [https://deploy.wandb.ai](https://deploy.wandb.ai)
* [https://charts.wandb.ai](https://charts.wandb.ai)
* [https://quay.io](https://quay.io) (used for Prometheus images)

<Note>
  Additional container registries may be required depending on your deployment configuration:

  * `https://gcr.io` is needed when deploying Bufstream and etcd for Weave online evaluations.
</Note>

To learn about air-gapped deployments, refer to [Kubernetes operator for air-gapped instances](/platform/hosting/self-managed/operator-airgapped/).

Access to W\&B and to the object storage is required for the training infrastructure and for each system that tracks the needs of experiments.

### DNS

The fully-qualified domain name (FQDN) of the W\&B deployment must resolve to the IP address of the ingress/load balancer using an A record.

### Load balancer and ingress

The W\&B Kubernetes Operator exposes services using a Kubernetes ingress controller, which routes to service endpoints based on URL paths. The ingress controller must be accessible by all machines that execute machine learning payloads or access the service through web browsers.

For detailed load balancer options, ingress controller requirements, and configuration examples, see the [reference architecture load balancer section](/platform/hosting/self-managed/ref-arch/#load-balancer-and-ingress).

## SSL/TLS

W\&B requires a valid signed SSL/TLS certificate for secure communication between clients and the server. SSL/TLS termination must occur on the ingress/load balancer. The W\&B Server application does not terminate SSL or TLS connections.

**Important**: W\&B does not support self-signed certificates and custom CAs. Using self-signed certificates will cause challenges for users and is not supported.

If possible, using a service like [Let's Encrypt](https://letsencrypt.org) is a great way to provide trusted certificates to your load balancer. Services like Caddy and Cloudflare manage SSL for you.

If your security policies require SSL communication within your trusted networks, consider using a tool like Istio and [side car containers](https://istio.io/latest/docs/reference/config/networking/sidecar/).

## License

A valid W\&B Server license is required for all Self-Managed deployments.

You need a W\&B license to deploy W\&B Self-Managed.

1. If you do not already have a W\&B account, create one.
2. If you need an enterprise trial license with support for important security and other enterprise-friendly capabilities, [submit a request](https://wandb.ai/site/for-enterprise/self-hosted-trial) or reach out to your W\&B team.
3. Otherwise, open the [Deploy Manager](https://deploy.wandb.ai/deploy) to generate a free trial license. The URL redirects you to a **Get a License for W\&B Local** form. Provide the following information:
   * The owner of the license
   * The deployment type
   * A name and optional description for the instance
4. Click **Generate License Key**.

A page displays with an overview of your deployment along with the license associated with the instance.

## Next steps

After ensuring your infrastructure meets these requirements:

* **Cloud and on-premises deployments**: See [Deploy W\&B with Kubernetes Operator](/platform/hosting/self-managed/operator) for Helm and Terraform deployment options.
* **Air-gapped deployments**: See [Deploy on Air-Gapped Kubernetes](/platform/hosting/self-managed/on-premises-deployments/kubernetes-airgapped) for disconnected environments.
* **All deployment methods**: See [Deploy with Kubernetes Operator](/platform/hosting/self-managed/operator) for the core operator deployment guide
