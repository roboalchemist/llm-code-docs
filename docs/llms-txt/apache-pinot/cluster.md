# Source: https://docs.pinot.apache.org/release-0.4.0/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-0.9.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-0.9.0/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-1.0.0/reference/cluster.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/components/cluster.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/concepts/components/cluster.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/concepts/components/cluster.md

# Source: https://docs.pinot.apache.org/release-1.4.0/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/concepts/components/cluster.md

# Source: https://docs.pinot.apache.org/configuration-reference/cluster.md

# Source: https://docs.pinot.apache.org/basics/concepts/components/cluster.md

# Cluster

A Pinot cluster is a collection of the software processes and hardware resources required to ingest, store, and process data. For detail about Pinot cluster components, see [Physical architecture](https://docs.pinot.apache.org/basics/pinot-storage-model#physical-architecture).

A Pinot cluster consists of the following processes, which are typically deployed on separate hardware resources in production. In development, they can fit comfortably into Docker containers on a typical laptop:

* **Controller**: Maintains cluster metadata and manages cluster resources.
* **Zookeeper**: Manages the Pinot cluster on behalf of the controller. Provides fault-tolerant, persistent storage of metadata, including table configurations, schemas, segment metadata, and cluster state.
* **Broker**: Accepts queries from client processes and forwards them to servers for processing.
* **Server**: Provides storage for segment files and compute for query processing.
* (Optional) **Minion**: Computes background tasks other than query processing, minimizing impact on query latency. Optimizes segments, and builds additional indexes to ensure performance (even if data is deleted).

The simplest possible Pinot cluster consists of four components: a server, a broker, a controller, and a Zookeeper node. In production environments, these components typically run on separate server instances, and scale out as needed for data volume, load, availability, and latency. Pinot clusters in production range from fewer than ten total instances to more than 1,000.

Pinot uses [Apache Zookeeper](https://zookeeper.apache.org/) as a distributed metadata store and [Apache Helix](http://helix.apache.org/) for cluster management.

Helix is a cluster management solution that maintains a persistent, fault-tolerant map of the intended state of the Pinot cluster. Helix constantly monitors the cluster to ensure that the right hardware resources are allocated for the present configuration. When the configuration changes, Helix schedules or decommissions hardware resources to reflect the new configuration. When elements of the cluster change state catastrophically, Helix schedules hardware resources to keep the actual cluster consistent with the ideal represented in the metadata. From a physical perspective, Helix takes the form of a controller process plus agents running on servers and brokers.

## Cluster configuration

For details of cluster configuration settings, see [Cluster configuration reference](https://docs.pinot.apache.org/configuration-reference/cluster).

## Cluster components

Helix divides nodes into logical components based on their responsibilities:

### Participant

Participants are the nodes that host distributed, partitioned resources

Pinot servers are modeled as participants. For details about server nodes, see [Server](https://docs.pinot.apache.org/basics/concepts/components/cluster/server).

### Spectator

Spectators are the nodes that observe the current state of each participant and use that information to access the resources. Spectators are notified of state changes in the cluster (state of a participant, or that of a partition in a participant).

Pinot brokers are modeled as spectators. For details about broker nodes, see [Broker](https://docs.pinot.apache.org/basics/concepts/components/cluster/broker).

### Controller

The node that observes and controls the Participant nodes. It is responsible for coordinating all transitions in the cluster and ensuring that state constraints are satisfied while maintaining cluster stability.

Pinot controllers are modeled as controllers. For details about controller nodes, see [Controller](https://docs.pinot.apache.org/basics/concepts/components/cluster/controller).

## Logical view

Another way to visualize the cluster is a logical view, where:

* A cluster contains [tenants](https://docs.pinot.apache.org/basics/concepts/components/cluster/tenant)
* Tenants contain [tables](https://docs.pinot.apache.org/basics/concepts/components/table)
* Tables contain [segments](https://docs.pinot.apache.org/basics/concepts/components/table/segment)

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-M1cGq_K6f87emCw4pkc%2F-M1cHtSieWXlok7s8_HW%2FClusterLogical.jpg?alt=media\&token=5a8dc566-b8a3-4e2c-9f01-b32392ab3e69)

## Set up a Pinot cluster

Typically, there is only one cluster per environment/data center. There is no need to create multiple Pinot clusters because Pinot supports [tenants](https://docs.pinot.apache.org/basics/concepts/components/cluster/tenant).

To set up a cluster, see one of the following guides:

* [Running Pinot in Docker](https://docs.pinot.apache.org/basics/getting-started/running-pinot-in-docker)
* [Running Pinot locally](https://docs.pinot.apache.org/basics/getting-started/running-pinot-locally)
