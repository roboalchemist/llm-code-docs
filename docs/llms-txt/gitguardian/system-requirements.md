# Source: https://docs.gitguardian.com/self-hosting/system-requirements.md

# System requirements

> Hardware, software, and infrastructure requirements for deploying GitGuardian self-hosted, including Kubernetes, database, and Redis specifications.

The self-hosted version of GitGuardian is deployed as a Kubernetes application. We recommend installing GitGuardian on an **existing cluster using Helm**. You can find more information on how to [choose your installation method](./installation/choose-embedded-existing) on our dedicated page.

## Hardware requirements

### Architecture

GitGuardian Platform self-hosted supports the following CPU architectures:

- AMD64: Fully supported across all installation methods
- ARM64: Supported for Helm-based installations only (Existing Cluster with Helm). KOTS and Embedded Cluster installations are AMD64-only

All container images are published as multi-architecture (multi-arch) manifests. You do not need to specify a Docker `--platform` flag; the appropriate image variant will be selected automatically based on the node architecture.

### Existing Kubernetes cluster installation

For sizing recommendations, refer to our [Scaling GitGuardian](./management/infrastructure-management/scaling) page.

### Embedded Kubernetes cluster installation

| Component       | Required Capacity |
| :-------------- | :---------------- |
| CPU             | 8 cores           |
| Memory          | 48 GB             |
| Root disk space | 300 GB            |

This installation has some limitations:
- Multi-node support is in beta
- Changing node hostnames is not supported
- Automatic updates not supported
- Support bundles over 100MB in the Admin Console
- Installing on STIG- and CIS-hardened OS images is not supported

More details on [Replicated](https://docs.replicated.com/vendor/embedded-overview#limitations).

## Software requirements

### Kubernetes for Existing Clusters

For Existing Cluster installations, GitGuardian supports the following Kubernetes versions: 1.30 to 1.35.

GitGuardian needs a dedicated namespace.

:::note
If you plan to install GitGuardian on an OpenShift cluster, please refer to the **[detailed guidelines for OpenShift cluster installation](./installation/openshift)**.
:::

### GCP Marketplace

The [GCP Marketplace](https://console.cloud.google.com/marketplace/product/gitguardian-public/gitguardiansaas) deployment uses Helm, providing all the benefits of Helm-based installations with consolidated billing through your GCP account. The initial deployment is done through the GCP console, but upgrades are performed directly with Helm. The same Helm requirements below apply.

For database setup instructions, see [Cloud SQL: PostgreSQL on GCP](./installation/databases/postgres-cloudsql) and [Memorystore: Redis on GCP](./installation/databases/redis-memorystore). For GCP-specific deployment details, see the [GCP Marketplace deployment guide](https://github.com/GitGuardian/gcpmarketplace).

### Helm

The [Existing Cluster with Helm](./installation/installation-existing-cluster-helm)
installation method requires [Helm](https://helm.sh) version **3.13+**.

:::caution
- Helm version 3.18.0 is not supported due to a bug in Helm, which is fixed in 3.18.1 and later versions.
:::

Use a Helm version that aligns with your Kubernetes version to avoid compatibility issues.
Refer to the [Helm version support policy](https://helm.sh/docs/topics/version_skew/) for the list of compatible versions.

:::info FIPS Compliance
**FIPS 140-3 (Federal Information Processing Standards) compliance is available exclusively for Helm-based installations.** If you require FIPS 140-3 compliant cryptographic modules for regulatory compliance, you must choose the Helm installation method and set `global.fips.enabled: true` in your Helm values. For airgap installations, additional image renaming steps are required. For more details, see the [Security Recommendations](./security/recommendations) page.
:::

Helm installation also supports some optional custom resources. If you wish to use them, you must have the appropriate controllers and operators:

- **IngressController:** we provide an example of an `ingress` controller.
  You can also configure any other [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) class. Read our [Ingress Configuration](./management/infrastructure-management/ingress) topic.
- **Istio:** we support Istio for traffic routing and end-to-end encryption (sidecars).
- **Prometheus Operator:** we can deploy ServiceMonitors to expose observability metrics on our application.
- **Vault:** we allow the use of Vault through [external-secrets](https://external-secrets.io/) SecretStore.
- **CertManager:** we allow certificate management through [cert-manager](https://cert-manager.io/) ClusterIssuer.

### PostgreSQL

GitGuardian currently supports PostgreSQL 15 to 18, with PostgreSQL 17 being the recommended version.

:::caution
PostgreSQL versions 13 and 14 are not supported anymore starting 2025.1.0 release. We strongly recommend upgrading to PostgreSQL 16+ at your earliest convenience.
:::

You'll need to install the following extensions:

| Extension | Usage                                                                                                     | Minimal Version |
| --------- | --------------------------------------------------------------------------------------------------------- | --------------- |
| btree_gin | Provides GIN capability to base datatypes (int, timestamp, ...) so all columns can be used in GIN indexes | 1.3             |
| pg_trgm   | Provides functions and operators enabling fast searching for similar strings using GiST and GIN indexes   | 1.5             |
| plpgsql   | Allows the creation of stored procedures and triggers using the procedural programming language PL/pgSQL  | 1.0             |
| pgvector  | Provides vector similarity search using new types, functions, operators and indexes                       | 0.7.0 (0.8.0 recommended) |

Depending on your installation, extensions may already be available. This is the case for the major cloud managed PostgreSQL databases. Otherwise, you might have to carry out some extra actions:

* plpgsql extension is installed by default.
* btree_gin and pg_trgm extensions are available in the _postgresql-contrib_ package.
* [pgvector](https://github.com/pgvector/pgvector?tab=readme-ov-file#installation) extension is available as a package for Debian, Ubuntu or Yum based OSes. If you are using Docker, you can use the available [docker image](https://hub.docker.com/r/pgvector/pgvector). You can also install it via the [pgxn](https://pypi.org/project/pgxnclient/) client.

To make these extensions available in your database, you must run the following commands while connected as a `superuser` on the database instance:

```sql
CREATE EXTENSION IF NOT EXISTS btree_gin;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS plpgsql;
CREATE EXTENSION IF NOT EXISTS vector;
```

For additional guidance on databases, see [Configure your database](./installation/databases/database-config).

For sizing recommendations, refer to our [Scaling GitGuardian](./management/infrastructure-management/scaling) page.

:::tip High Availability and Databases
For large-scale deployments, we recommend using an **external PostgreSQL database** and leveraging your provider's replication mechanisms for high availability.
:::

:::warning Connection Poolers
We recommend avoiding connection poolers (such as [PgBouncer](https://www.pgbouncer.org)) with GitGuardian, as they may cause unexpected behavior or impact performance. Direct connections to PostgreSQL are recommended.
:::

### Redis

GitGuardian currently supports Redis 6 to 8, with Redis 7 being the recommended version. Additionally, we support **Valkey** (a Redis-compatible fork of Redis 7.2) as an alternative Redis implementation.

**How GitGuardian Uses Redis**: Redis serves as the message broker for distributed job processing (Celery), caches frequently accessed data, and stores temporary scan results.

For large-scale deployment, we highly recommend using an external Redis. For sizing recommendations, refer to our [Scaling GitGuardian](./management/infrastructure-management/scaling) page.

For High Availability, we support [Redis Sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/) for Existing cluster. **Redis Cluster is not supported**.

:::warning
The Redis instance must be dedicated exclusively to the GitGuardian application. Sharing the instance with other applications may lead to unexpected behavior, data corruption, and performance issues.
:::

:::info
The `FLUSHDB` command must be enabled on the Redis instance, as it is essential for the proper functioning of certain features in our application. Ensure that this command is not shadowed in your Redis configuration (e.g., `rename-command "FLUSHDB" ""`).

Be aware that if Redis has an eviction policy set (such as `noeviction`, `allkeys-lru`, etc.), and the policy is set to `noeviction`, Redis will not evict any data. This can cause new writes to fail when the memory limit is reached, so choose your eviction policy carefully.
:::

### KOTS

The "Existing cluster with KOTS" installation method is using [KOTS](https://kots.io/). We use the latest KOTS version available to validate
our releases. You can find version compatibility on the [KOTS compatibility page](https://docs.replicated.com/enterprise/installing-general-requirements#kubernetes-version-compatibility).

The [KOTS Admin Console](./management/infrastructure-management/admin-console) will have full control over this namespace. The following
role needs to be created:

```bash
Name:         kotsadm-role
Labels:       kots.io/kotsadm=true
Annotations:  <none>
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  *.*        []                 []              [*]
```

We are using the following objects:

- **PersistentVolumeClaims:** we are using persistent volume claims for KOTS,
  workers and the embedded databases.
- **IngressController:** we can provide a default ingress, an
  [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
  is needed to handle it.

You need to have the appropriate controllers and operators to handle them.

### Kubernetes and OS for Embedded Clusters

For Embedded Kubernetes cluster installations, please note that these setups are intended primarily for trial or Proof of Concept (PoC) purposes and are not recommended for production use.

#### Kubernetes

For **Embedded cluster installations (instances installed in 2025 or after)**, Kubernetes is upgraded automatically when updating the GitGuardian application through the KOTS Admin Console.

For **Embedded cluster legacy (kURL) installations (instances installed in 2024 or before)**, follow the [upgrade procedure](./management/infrastructure-management/upgrade-kots#upgrading-kubernetes-on-embedded-cluster-legacy-kurl-instances-installed-in-2024-or-before) to update your Kubernetes version.

#### Operating system

Ensure that you adhere to the [Replicated](https://docs.replicated.com/enterprise/installing-general-requirements) and [Embedded Cluster](https://docs.replicated.com/enterprise/installing-embedded-requirements) system requirements.

:::note
We strongly recommend applying the latest patches available for your operating system distribution before beginning the installation.
:::

## Domain name requirements

You will need a Fully Qualified Domain Name (FQDN) to install the application (ex: `gitguardian.mycorp.local`). This cannot be an IP.
You will also need a TLS certificate for HTTPS access or use the default self-signed certificates.
