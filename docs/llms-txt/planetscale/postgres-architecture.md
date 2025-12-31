# Source: https://planetscale.com/docs/postgres/postgres-architecture.md

# PlanetScale Postgres architecture

> PlanetScale Postgres is a managed PostgreSQL service built on modern cloud infrastructure.

## Overview

Our architecture provides high availability through availability zone distribution, automated failover, and redundancy across multiple components. PlanetScale Postgres is built around a `shared nothing` architecture in alignment with PlanetScale's [principles of extreme fault tolerance](https://planetscale.com/blog/the-principles-of-extreme-fault-tolerance).

This document explains the core components of our PostgreSQL infrastructure, from regional deployment patterns to cluster configuration options and operational capabilities.

## Regional and availability zone architecture

### Geographic distribution

PlanetScale Postgres deploys database clusters across multiple availability zones within a single region. This design provides:

* **Zone-level fault tolerance**: Database instances are automatically distributed across separate availability zones
* **Network isolation**: Each availability zone operates independently with its own network infrastructure

### Cluster design

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-arch-diagram.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7b6b4c86cfe2b872a394857c2c993ca9" alt="PlanetScale Postgres cluster topology" data-og-width="2612" width="2612" data-og-height="1654" height="1654" data-path="docs/postgres/postgres-arch-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-arch-diagram.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=cdc9609e609cf49ace22f2b4b846b009 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-arch-diagram.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7cf762ad536dddec55ac042a59983c5a 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-arch-diagram.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=0d9c08d45218a9d93cb1689146dcc28e 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-arch-diagram.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=280b440805dde747c16a85dab9b1e629 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-arch-diagram.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f97af7f19f67144887e6dbd47e999bdd 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-arch-diagram.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=6a59558fafc819270def2c432b10f203 2500w" />
</Frame>

PlanetScale Postgres uses a primary-replica architecture distributed across availability zones to provide high availability without compromising performance. This design ensures that your database can survive infrastructure failures while maintaining fast read and write operations.

### Primary-replica architecture

Each production PostgreSQL cluster consists of:

**Primary instance (1)**:

* Handles all write operations
* Located in one availability zone
* Serves read operations when replicas are unavailable
* Source of truth for data replication

**Replica instances (2)**:

* Handle read-only operations
* Located in separate availability zones from primary
* Continuously synchronized with primary through streaming replication
* Available for promotion to primary during failover events

## Orchestration layer

The orchestration layer manages the lifecycle, health, and operations of PostgreSQL clusters across multiple availability zones. This infrastructure layer handles everything from initial deployment to ongoing maintenance and failover operations.

### Kubernetes-based management

Our PostgreSQL clusters run on Kubernetes infrastructure, providing:

* **Automated deployment**: Consistent cluster provisioning across availability zones
* **Health monitoring**: Continuous monitoring of database instance health
* **Resource management**: Dynamic allocation of compute and storage resources
* **Configuration management**: Centralized management of PostgreSQL parameters and settings

### Custom operator

Our custom Kubernetes operator manages all cluster nodes and handles PostgreSQL operations that would otherwise require deep database knowledge. Based on our extensive experience running databases at massive scale, our operator was built for rock-solid handling of PostgreSQL replication, backup requirements, and the specific steps needed for safe failover operations:

* **Failover coordination**: Automated promotion of replica instances when primary fails
* **Backup scheduling**: Coordinated backup operations across all instances
* **Configuration synchronization**: Ensures consistent settings across primary and replicas
* **Scaling operations**: Manages instance resizing and replica addition/removal

## Data replication

**Streaming replication**:
PostgreSQL's built-in streaming replication keeps replicas synchronized with the primary in near real-time. Changes are continuously streamed to replicas, ensuring data consistency across all instances:

* Continuous data streaming from primary to replicas
* Changes confirmed by at least one replica
* Automatic lag monitoring and alerting

**Connection routing**:

* Port 5432: Direct PostgreSQL connections
* Port 6432: [PgBouncer](/docs/postgres/connecting/pgbouncer) connection pooling for optimized connection management
* SSL/TLS encryption required for all connections

## Instance configurability

PlanetScale Postgres offers flexible instance configuration to match your workload requirements and cost constraints. You can choose different CPU architectures, storage types, and performance characteristics to optimize for your specific use case.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-create-config.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b5961c4d1abf29e63f3c902a8e9c47e0" alt="Creating a database" data-og-width="3240" width="3240" data-og-height="1914" height="1914" data-path="docs/postgres/postgres-create-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-create-config.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ef9b11bb9e53f3ac5c02b6d1884a8bc2 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-create-config.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=1422a26ed1ea5d30f8beb1934cad2ed6 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-create-config.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=27fedf06bc5dfa9f4ed92c119eb932e0 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-create-config.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7f60c011f695cfebbc3afac3fc555582 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-create-config.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=cca597a2ca45ec3cc1c358bc8567e280 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-create-config.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=22dc4f7f5e2ea9fb7b86ccb6ecd0f1d7 2500w" />
</Frame>

### CPU architecture options

**ARM64 (AWS Graviton)**:

* Cost-optimized instances with good performance characteristics
* Compatible with all PostgreSQL features and extensions
* Lower power consumption and cost per compute unit

**x86-64 (Intel/AMD)**:

* Traditional architecture with broad compatibility
* Optimized for single-threaded performance requirements
* Full compatibility with existing tooling and applications

Learn more about [CPU architecture selection](/docs/postgres/cluster-configuration/cpu-architectures).

### Storage types

Storage choice significantly impacts database performance and cost. PlanetScale offers two distinct storage options optimized for different workload patterns:

**PlanetScale Metal**:

* Direct-attached NVMe storage for maximum performance
* Lower I/O latency compared to network-attached storage
* Fixed storage capacity based on instance size
* Optimal for I/O-intensive workloads

**Network-attached storage (EBS)**:

* Flexible storage scaling up to 16 TiB
* Configurable IOPS and throughput settings
* Automatic storage scaling based on usage patterns
* Cost-effective for variable storage requirements

Learn more about [storage configuration](/docs/postgres/cluster-configuration/cluster-storage).

### Performance and scaling relationships

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-dashboard-summary-metal.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=345b1f6de02345683e2930b488366963" alt="Database dashboard summary" data-og-width="1478" width="1478" data-og-height="1356" height="1356" data-path="docs/postgres/postgres-dashboard-summary-metal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-dashboard-summary-metal.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=113ca5c69f03eda03e1b5c5b67d67c0c 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-dashboard-summary-metal.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c15cd5ef2833c586046f95d6bb5f421e 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-dashboard-summary-metal.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=411e3a832ca7c696b197a652e9966da3 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-dashboard-summary-metal.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=1bdb3a58becea1d98b5a4836c85c18db 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-dashboard-summary-metal.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b5931e8fcc8777d8d9f13c10d5ab78b7 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-dashboard-summary-metal.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=082752ba89e2c1d112cc4806e2c2ea3c 2500w" />
</Frame>

Understanding how different configuration choices affect performance helps you optimize your database for both cost and performance. These relationships guide capacity planning and scaling decisions:

**Compute scaling**:

* Instance size directly affects CPU, memory, and network capacity
* Larger instances support more concurrent connections
* Memory allocation affects query performance and caching efficiency

**Storage performance**:

* Network-attached storage can autoscale to meet storage needs
* Network-attached storage allows for configurable IOPS and disk bandwidth
* PlanetScale Metal provides increased IOPS and ultra-low latency storage
* Throughput limits vary by instance size and storage configuration

## Operational capabilities

PlanetScale Postgres provides comprehensive operational tools that give you visibility into database performance, health, and behavior. These capabilities help you monitor, troubleshoot, and optimize your database without requiring additional setup or external tools.

### Insights and query analysis

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-insights.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bf30109675fb87450bcd6ed21c393d53" alt="PlanetScale Insights" data-og-width="2886" width="2886" data-og-height="1818" height="1818" data-path="docs/postgres/postgres-insights.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-insights.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a2edb1ed14543563a939f9c39bec3dfa 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-insights.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=70eac6f83cf01c5a848423179f627aa3 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-insights.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=78832331964bf584a87fcf1911cae4f0 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-insights.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=16f258115045ade9afdfbf5a49bc58e2 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-insights.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7c76f76b2e962be0819b3942592e005c 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-insights.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c5955ab193acd7ce486483649c19fbff 2500w" />
</Frame>

**Query performance insights**:

* Automatic detection of slow-running queries and anomalies
* Query execution plan analysis and recommendations
* Historical query performance tracking
* Identification of resource-intensive operations

### Metrics and monitoring

Comprehensive metrics collection provides real-time visibility into database health and performance trends. All metrics are collected automatically and made available through both the dashboard and programmatic interfaces:

**Built-in metrics collection**:

* CPU, memory, and storage utilization across all instances
* Connection count and pooling efficiency
* Replication lag and synchronization status

Learn more about [monitoring and metrics](/docs/postgres/monitoring/metrics).

### Logs and diagnostics

Centralized logging aggregates all database-related logs in a searchable format with 7-day retention. This unified logging system helps with troubleshooting, security monitoring, and performance analysis:

**Centralized logging**:

* PostgreSQL server logs from all instances
* Query execution logs with configurable detail levels
* Error logs with automatic categorization and alerting
* Connection and authentication logs for security monitoring

**Log analysis tools**:

* Search and filtering capabilities across all log sources
* Export capabilities for external analysis tools

### Cluster configuration options

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-config-changes.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=68b5e2bb085005c963fcee511e91c2ec" alt="Tracking changes" data-og-width="2918" width="2918" data-og-height="2174" height="2174" data-path="docs/postgres/postgres-config-changes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-config-changes.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c60901964cc0483780030f0a103e5096 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-config-changes.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a27d443002284bb2f944fe276e9f6142 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-config-changes.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bc8c4b60c795e7d96699b3039a63acfa 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-config-changes.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f30ab7a68574ecd9eea4a22b1043b558 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-config-changes.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f3980cd9e96a56718c3bcb4fae8ec040 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-config-changes.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=16764f6b7ac0cb4094b4453740e62cd5 2500w" />
</Frame>

Flexible configuration options allow you to customize PostgreSQL behavior, enable additional functionality, and optimize performance for your specific workload requirements:

**Extension management**:

* Curated set of PostgreSQL extensions tested for compatibility
* Both Native and Community extensions available
* Managed through dashboard or CLI

Learn more about [extension configuration](/docs/postgres/extensions).

**Parameter tuning**:

* Pre-configured parameter sets optimized for different workload types
* Customizable PostgreSQL configuration parameters
* Automatic parameter adjustment based on instance size changes
* Configuration change tracking

Learn more about [parameter configuration](/docs/postgres/cluster-configuration/parameters).

**Custom Backups and Point-in-time recovery**:

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-pitr.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=5f20ac9f7c14b2f9d118fa389c18798e" alt="Postgres PITR" data-og-width="1766" width="1766" data-og-height="1202" height="1202" data-path="docs/postgres/postgres-pitr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-pitr.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=21542d969f50893d2cd6aa269ad740b0 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-pitr.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=afee9060f9579020f416edbaa323df3e 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-pitr.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e04dc1293ae594ecc2a9b9216e25bc3a 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-pitr.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e3cf7ed4df22fd48516cb8c211997b74 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-pitr.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=da264a289609af221c182500e8324aaf 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/postgres-pitr.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=5e6c752164cb954efa845c8916343f1f 2500w" />
</Frame>

* Automated backup scheduling with configurable retention periods
* Custom backup timing to minimize impact on production workloads
* Point-in-time recovery capabilities within retention windows

Learn more about [backup and restore operations](/docs/postgres/backups).

## Development workflow integration

PlanetScale Postgres integrates with development workflows through database branching and comprehensive migration support. These features enable safe schema changes and smooth transitions from other PostgreSQL platforms.

### Database branching

**Environment isolation**:

* Create isolated database environments from production backups
* Independent schema and data changes without affecting production
* Cost-optimized single-instance architecture for development branches
* Automatic promotion to full high-availability architecture when needed

### Third-party integrations

PlanetScale Postgres integrates with popular monitoring and development tools through standard protocols and APIs. These integrations allow you to incorporate database metrics into existing workflows and toolchains:

**Monitoring system integrations**:

* [Prometheus endpoints](/docs/postgres/monitoring/prometheus-postgres) for custom metrics collection
* [Datadog integration](/docs/postgres/monitoring/prometheus-metrics-datadog-postgres) for unified monitoring dashboards

**Development tool integrations**:

* Standard PostgreSQL connection protocols for universal tool compatibility
* Support for popular database administration tools
* API access for programmatic management and monitoring

## Related documentation

<CardGroup>
  <Card href="/docs/postgres/cluster-configuration" title="Cluster Configuration" icon="angles-right" horizontal />

  <Card href="/docs/postgres/scaling/replicas" title="Scaling with Replicas" icon="angles-right" horizontal />

  <Card href="/docs/postgres/backups" title="Backup and Recovery" icon="angles-right" horizontal />

  <Card href="/docs/postgres/monitoring/metrics" title="Monitoring and Metrics" icon="angles-right" horizontal />

  <Card href="/docs/postgres/branching" title="Database Branching" icon="angles-right" horizontal />
</CardGroup>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt