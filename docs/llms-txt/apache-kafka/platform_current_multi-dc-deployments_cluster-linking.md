# Source: https://docs.confluent.io/platform/current/multi-dc-deployments/cluster-linking/index.md

<a id="cluster-linking"></a>

# Cluster Linking for Confluent Platform

The following sections provide an overview of Cluster Linking on Confluent Platform, including an explanation of what it is and how it works,
use cases and architectures, best practices, and more.

## What is Cluster Linking?

Cluster Linking enables you to directly connect clusters and mirror
topics from one cluster to another.
Cluster Linking makes it easy to build multi-datacenter, multi-region,
and hybrid cloud deployments. It is secure, performant, tolerant of
network latency, and built into Confluent Server and Confluent Cloud.

Unlike [Replicator](../replicator/index.md#replicator-detail) and MirrorMaker 2, Cluster Linking
does not require running Connect to move messages from one cluster to another,
and it creates identical âmirror topicsâ with globally consistent offsets. We call
this âbyte-for-byteâ replication. Messages on the source topics are mirrored
precisely on the destination cluster, at the same partitions and offsets.
No duplicated records will appear in a mirror topic with regards to what the source topic contains.

## Capabilities and comparisons

Cluster Linking replicates topics from one Kafka or Confluent cluster to another,
providing the following capabilities:

- Global Replication: Unify data and applications from regions and continents around the world.
- Hybrid cloud: Create a secure, scalable, and seamless bridge-to-cloud by linking an
  on-premise Confluent Platform cluster in a private cloud to a Confluent Cloud cluster in a
  public cloud.
- HA/DR: Build a multi-region high availability and disaster recovery (âHA/DRâ) strategy
  that achieves low recovery times (RTOs) and minimal data loss (RPOs) by
  replicating topic data and metadata to another cluster.
- Cluster migration: Migrate from an older cluster to one in a newer environment, region, or cloud.
- Aggregation: Combine data from many smaller clusters into one aggregate cluster.
- Data sharing: Exchange data between different teams, lines-of-business, and organizations.

Compared to other Kafka replication options, Cluster Linking offers these advantages:

- Built into Confluent Server and Confluent Cloud, so it does not depend on additional components, connectors,
  virtual machines, or custom processes.
- Creates exact mirrors of topics, including offsets, to enable migration, failover, and rationalizing
  about your system without offset translation or custom tooling.
- Can be dynamically updated via REST APIs, CLIs, and Kubernetes CRDs.
- For compressed messages, byte-to-byte replication achieves faster throughput by avoiding
  decompression-and-recompression.

<a id="cl-supported-on-cp"></a>

## Whatâs supported

<a id="kraft-zoo-cl-overview"></a>

### KRaft and ZooKeeper

- As of Confluent Platform 8.0, ZooKeeper is no longer available for new deployments. Confluent recommends migrating to KRaft mode for new deployments.
  To learn more about running Kafka in KRaft mode, see [KRaft Overview for Confluent Platform](../../kafka-metadata/kraft.md#kraft-overview) and the KRaft steps in the [Quick Start for Confluent Platform](../../get-started/platform-quickstart.md#quickstart).
  To learn about migrating from older versions, see [Migrate from ZooKeeper to KRaft on Confluent Platform](../../installation/migrate-zk-kraft.md#migrate-zk-kraft).
- Specifically, in relation to this migration to KRaft, `password.encoder.secret` is not required for KRaft mode, but is required when [migrating from ZooKeeper to KRaft](../../installation/migrate-zk-kraft.md#migrate-zk-kraft).
  Use of this parameter for Cluster Linking, when needed for older versions on ZooKeeper, is shown in [Tutorial: Link Confluent Platform and Confluent Cloud Clusters](hybrid-cp.md#cluster-link-hybrid-cp). To learn more about how this is handled in Confluent Platform 8.0 and later, see [Update password configurations dynamically](../../kafka/dynamic-config.md#dynamic-config-passwords-upgrade).
- This documentation provides examples for KRaft mode only. Earlier versions of this documentation provide examples for both KRaft and ZooKeeper.
- Some examples in the various tutorials show a *combined mode* configuration, where for each cluster the broker and controller run on the same server.
  Currently, combined mode is not intended for production use but is shown here to simplify the tutorial.
  If you want to run controllers and brokers on separate servers, use KRaft in isolated mode. To learn more, see [KRaft Overview for Confluent Platform](../../kafka-metadata/kraft.md#kraft-overview) and [KRaft Configuration for Confluent Platform](../../kafka-metadata/config-kraft.md#configure-kraft).

### Supported platform and tools compatibilities

Cluster Linking is included as a part of Confluent Server. There are no additional or other licensing costs for Cluster Linking
on Confluent Platform outside of the cost of the Confluent [Enterprise license subscription](../../installation/license.md#cp-enterprise-subs-license). Following are the requirements for and supported features
of Cluster Linking.

- Requires Confluent Server destination cluster of Confluent Platform 7.x.x on the destination cluster.
- Works with all [clients](../../clients/overview.md#kafka-clients).
- Requires an inter-broker protocol (IBP) of 2.4 or higher on the source cluster, and an IBP of 2.7 or higher on the
  destination cluster. More specifically, for current Confluent Platform 7.x.x versions, if IBP of source cluster is 2.7 or lower,
  IBP of destination must be 2.7. If IBP of source cluster is 2.8 or higher, IBP of destination may be 2.7 or higher.
  What is not supported is for clusters using Confluent Platform 7.x.x to have a mismatch between source and destination IBP outside of these parameters.
  For a guide to upgrading, see [Steps for upgrading to 8.2.x](../../installation/upgrade.md#rolling-upgrade).
- Built-in custom resource in [Confluent for Kubernetes](https://docs.confluent.io/operator/2.2.0/co-link-clusters.html#co-link-clusters).
- Compatible with [Ansible](https://docs.confluent.io/ansible/current/overview.html). To learn more, see [Using Cluster Linking with Ansible](configs.md#cluster-linking-with-ansible).
- Provides support for authentication and authorization, as described in [Manage Security for Cluster Linking on Confluent Platform](security.md#cluster-link-security).
- The source cluster can be Kafka or Confluent Server or Confluent Cloud; the destination cluster must be [Confluent Server](../../installation/available_packages.md#confluent-server-package), which is bundled with Confluent Enterprise.
- Bidirectional links between two clusters are supported; but these must be established as two separate links, not a single link.
  The [Hybrid tutorial](hybrid-cp.md#cluster-link-hybrid-cp) gives an example of creating a bi-directional link between an on-premises Confluent Platform cluster and a Confluent Cloud cluster.
- In addition to self-managed deployments on Confluent Platform, Cluster Linking is also available as a managed service on [Confluent Cloud](/cloud/current/multi-cloud/cluster-linking/index.html) and in [Hybrid cloud](#hybrid-cloud-cluster-linking).

| Source                                                    | Destination                         |
|-----------------------------------------------------------|-------------------------------------|
| Confluent Platform 7.0.x or later <sup>[1](#f1)</sup>     | Confluent Platform 7.0.0 or later   |
| Confluent Cloud                                           | Confluent Platform 7.0.0 or later   |
| Kafka 3.0.x or later <sup>[1](#f1)</sup>                  | Confluent Platform 7.0.0 or later   |
| Confluent Platform 7.0.x or later <sup>[1](#f1)</sup>     | Confluent Cloud <sup>[2](#f2)</sup> |
| Confluent Cloud                                           | Confluent Cloud <sup>[2](#f2)</sup> |
| Kafka 3.0.x or later <sup>[1](#f1)</sup>                  | Confluent Cloud <sup>[2](#f2)</sup> |
| Confluent Platform 7.1.0 or later (source-initiated link) | Confluent Platform 7.1.0 or later   |
| Confluent Platform 7.1.0 or later (source-initiated link) | Confluent Cloud                     |

### Footnotes

* <a id='f1'>**[1]**</a> See [Cluster Linking on Confluent Cloud](/cloud/current/multi-cloud/cluster-linking/index.html) for supported Confluent Cloud source and destination combinations.
* <a id='f2'>**[2]**</a> Cluster Linking is supported on all currently supported versions of Confluent Platform and Kafka, as described in [Confluent Platform and Apache Kafka compatibility](../../installation/versions-interoperability.md#cp-ak-compatibility). The exception to this is for migration use cases from Confluent Platform or Kafka to Confluent Cloud, where the source cluster can be Confluent Platform 5.5.0 or later Or Kafka 2.5.0 or later. For migration use cases and for versions earlier than Confluent Platform 5.4.0 or Kafka 2.4.0, you must disable the âincremental fetchâ request by setting the broker configuration `max.incremental.fetch.session.cache.slots=0` and restart all the source brokers.

## Upgrade notes

- When upgrading from Confluent Platform 6.2.0 to 7.0.0 or later version, make sure that `acl.sync.enabled` is not set to `true` in `$CONFLUENT_HOME/server.properties`.
  (The default is `false`, so if this property is not specified, you can assume it is set to `false`.) If `acl.sync.enabled` is set to `true` during upgrade,
  existing cluster links will be marked as âfailedâ (state is `LINK_FAILED`).

## Use cases and architectures

The following use cases can be achieved by the configurations and architectures shown.

<a id="hybrid-cloud-cluster-linking"></a>

### Hybrid cloud

**Use Case:** Easily create a persistent and seamless bridge from on-premise environments
to cloud environments. A cluster link between a Confluent Platform cluster in your datacenter and a Confluent Cloud
cluster in a public cloud acts as a single  secure, scalable hybrid data bridge that can be used
by hundreds of topics, applications, and data systems. Cluster Linking can tolerate the high latency
and unpredictable networking availability that you might have between on-premise infrastructure
and the cloud, and recovers from reconnections automatically. Cluster Linking can replicate data
bidirectionally between your datacenter and the cloud without any firewall holes or special IP filters
because your datacenter always makes an outbound connection.  Cluster Linking creates a byte-for-byte,
globally consistent copy of your data that preserves offsets, making it easy to migrate on-premise applications
to the cloud. Cluster Linking built into Confluent Platform and does not require any additional components to manage.

![image](images/clusterlinking-usecase-hybrid.png)

**Tutorial**: [Tutorial: Link Confluent Platform and Confluent Cloud Clusters](hybrid-cp.md#cluster-link-hybrid-cp)

### Disaster recovery

**Use Case:** Create a Disaster Recovery (âDRâ) cluster that is available to failover should
your primary cluster experience an outage or disaster. Cluster Linking keeps your DR cluster
in sync with data, metadata, topic structure, topic configurations, and consumer offsets so
that you can achieve low recovery point objectives (âRPOsâ) and recovery time objectives (âRTOsâ),
often measured in minutes. Cluster Linking for DR does not require an expensive network, complicated
management, or extra software components. And because Cluster Linking preserves offsets and syncs consumer offsets,
consumer applications of all languages can failover and pickup near the point where they left off,
achieving low downtime without custom code or interceptors.

![image](images/clusterlinking-usecase-dr.png)

### Global replication

**Use Case:** Stream data between the continents and regions where your business operates. Unify
data from every region to create a global real-time event mesh. Aggregate data from different
regions to drive the real-time applications and analytics that power your business. By making geo-local reads
of real-time data possible, this can act like a content delivery network (CDN) for your Kafka events
throughout the public cloud, private cloud, and at the edge.

![image](images/clusterlinking-usecase-global.png)

### Data sharing

**Use Case:** Share data between different teams, lines of business, or organizations
in a pattern that provides high isolation between teams and efficient operational management.
Cluster Linking keeps an in-sync mirror copy of relevant data on the consuming teamâs
cluster. This isolation empowers the consuming team to scale up hundreds of consumer
applications, stream processing apps, and data sinks without impacting the producing
teamâs cluster: for the producing team, itâs the same load as one additional consumer.
The producing team simply issues a security credential with access to the topics that
the consuming team is allowed to read. Then the consuming team can create a cluster link,
which they control, monitor, and manage.

![image](images/clusterlinking-usecase-datasharing.png)

**Tutorial**: [Tutorial: Share Data Across Topics Using Cluster Linking for Confluent Platform](topic-data-sharing.md#tutorial-topic-data-sharing)

**Customer Success Story (video)**: [Real-Time Inter-Agency Data Sharing With Kafka](https://www.confluent.io/events/current-2022/real-time-inter-agency-data-sharing-with-kafka/),
Kafka and Cluster Linking have transformed how government agencies share data: in real-time with faster onboarding of new data sets,
real-time event notification, reduced cost for data sharing, and enhanced and enriched data sets for improved data quality.

### Cluster migration

**Use Case:** Seamlessly move from an on-premises Kafka or Confluent Platform cluster to a Confluent Cloud cluster,
or from older infrastructure to new infrastructure, with low downtime and no data loss.
Cluster Linkingâs native offset preservation and consumer offset syncing allows every consumer
application to switch from the old cluster to the new one when itâs ready. Topics can be
migrated over one by one, or in a batch. Cluster Linking handles topic creation,
configuration, and syncing.

![image](images/clusterlinking-usecase-migration.png)

**Tutorial**: [Tutorial: Migrate Data with Cluster Linking on Confluent Platform](migrate-cp.md#cluster-linking-migrate-cp)

**Customer Success Story**: In [SAS Powers Instant, Real-Time Omnichannel Marketing at Massive Scale with Confluentâs Hybrid Capabilities](https://assets.confluent.io/m/3ecb86a059d2fe13/original/20220627-CS-SAS_Institute.pdf),
the subtopic âA much easier migration thanks to Cluster Linking â describes how SAS used Cluster Linking to migrate to Confluent for Kubernetes and other cloud-native solutions.

<a id="cp-cluster-linking-scale"></a>

## Scaling Cluster Linking

Because Cluster Linking fetches data from source topics, the first scaling
unit to inspect is the number of partitions in the source topics. Having enough
partitions lets Cluster Linking mirror data in parallel. Having too few
partitions can make Cluster Linking bottleneck on partitions that are more heavily used.

In a Confluent Platform or Apache KafkaÂ® cluster, you can scale Cluster Linking throughput as follows:

- On the cluster link configurations, change the number of fetcher threads or change the fetch size to get better batching.
- Improve the clusterâs maximum throughput by scaling the brokers vertically or horizontally.
- Use the options listed under [Cluster Link Replication Configurations](configs.md#cp-replication-configs)
  to tune cluster link performance, which helps scale cluster link throughput.

In Confluent Cloud, Cluster Linking scales with the ingress and egress quotas of
your cluster. Cluster Linking is able to use all remaining bandwidth in a
clusterâs throughput quota: 150 MB/s per CKU egress on a Confluent Cloud source
cluster or 50 MB/s per CKU ingress on a Confluent Cloud destination cluster,
whichever is hit first. Therefore, to scale Cluster Linking throughput, simply adjust
the number of CKUs on either the source, the destination, or both.

#### NOTE
On the destination cluster, Cluster Linking write takes lower priority
than Kafka clients producing to that cluster; Cluster Linking will be throttled first.

Confluent proactively monitors all cluster links in Confluent Cloud and will
perform tuning when necessary. If you find that your cluster link is not hitting
these limits even after a full day of sustained traffic, contact Confluent Support.

To learn more, see [recommended guidelines for Confluent Cloud](/cloud/current/clusters/cluster-types.html#dimensions-with-a-recommended-guideline).

<a id="cluster-linking-limitations"></a>

## Known limitations and best practices

- When deleting a cluster link, first check that all mirror topics are in the `STOPPED` state. If any are in the `PENDING_STOPPED` state,
  deleting a cluster link can cause irrecoverable errors on those mirror topics due to a temporary limitation.
- In Confluent Platform 7.1 and later, REST API calls to list and get source-initiated cluster links will have their destination cluster IDs
  returned under the parameter `destination_cluster_id`, or with Confluent CLI v4 as `destination_cluster`. (This is a change from previous releases, where these were returned under `source_cluster_id`.)
- For Confluent Platform in general, you should not use unauthenticated listeners. For Cluster Linking, this is even more important because Cluster Linking can access the listeners.
  As a best practice, always configure authentication on listeners. To learn more, see the [Enable Security for a KRaft-Based Cluster in Confluent Platform](../../security/security_tutorial.md#security-tutorial), the [Authentication in Confluent Platform](../../security/authentication/overview.md#authentication-overview), and the
  listener configuration examples in the brokers for the various protocols such as [SASL](../../security/authentication/overview.md#kafka-sasl-auth) and [Use TLS Authentication in Confluent Platform](../../security/authentication/mutual-tls/overview.md#kafka-ssl-authentication). See also, [Manage Security for Cluster Linking on Confluent Platform](security.md#cluster-link-security).
- All TLS/SSL key stores, trust stores and Kerberos keytab files must be stored at the same location on
  each broker in a given cluster. If not, cluster links may fail. Alternatively, you can
  [configure a PEM certificate in-line](https://cwiki.apache.org/confluence/display/KAFKA/KIP-651+-+Support+PEM+format+for+SSL+certificates+and+private+key)
  on the cluster link configuration.
- Cluster link configurations stored in files (TLS/SSL key stores, trust stores, Kerberos keytab files)
  should not be stored in `/tmp` because `/tmp` files may get deleted, leaving links and mirrors in a bad state on some brokers.
- Confluent Control Center will only display mirror topics correctly if the Confluent Platform cluster and Control Center are connected to a
  [REST Proxy API v3 for Confluent Platform](../../kafka-rest/api.md#rest-proxy-v3). If not connected to the v3 Confluent REST API, Control Center will display mirror topics
  as regular topics, which can lead to showing features that are not actually available on mirror topics;
  for example, producing messages or editing configurations. To learn how to configure these clusters
  for the v3 REST API, see [Required Configurations for Control Center](configs.md#cluster-linking-configs-c3).
- Prerequisites are provided per tutorial or use case because these differ depending on the context.
  Tutorials are provided on [topic data sharing](topic-data-sharing.md#tutorial-topic-data-sharing) and [Tutorial: Link Confluent Platform and Confluent Cloud Clusters](hybrid-cp.md#cluster-link-hybrid-cp).
  Additional requirements for secure setups are provided in [Manage Security for Cluster Linking on Confluent Platform](security.md#cluster-link-security).
- Cluster Linking has not yet been fully tested to mirror topics that contain records produced using the Kafka transactions feature. Therefore, using Cluster Linking to mirror such topics is not supported and not recommended.
- [Cluster Linking for Confluent Platform](#cluster-linking) between a source cluster running Confluent Platform 7.0.x or earlier (non-KRaft) and a
  destination cluster running in KRaft mode is not supported. Link creation may succeed, but the
  connection will ultimately fail (with a `SOURCE_UNAVAILABLE` error message). To work around this issue,
  make sure the source cluster is running Confluent Platform version 7.1.0 or later. If you have links from a Confluent Platform source
  cluster to a Confluent Cloud destination cluster, you must upgrade your source clusters to Confluent Platform 7.1.0 or later to avoid this issue.
- ACL migration (ACL sync), previously available in Confluent Platform 6.0.0 through 6.2.x, was removed in Confluent Platform 7.0.0 due to a security vulnerability,
  then re-introduced in Confluent Platform 7.1.0 with the vulnerability resolved. If you are using ACL migration in your pre-7.1.0 deployments,
  you should disable it or upgrade to 7.1.x. To learn more, see [Authorization (ACLs)](security.md#cluster-link-acls).
- Any customer-owned firewall that allows the cluster link connection from source cluster brokers to destination cluster brokers
  must allow the TCP connection to persist in order for Cluster Linking to work.
- Prefixing is not supported in 7.1.0. For more information, see the note at the top of this section: [Prefix Mirror Topics and Consumer Group Names](mirror-topics-cp.md#cluster-link-prefix-concepts).
- Cluster Linking cannot replicate messages that use the v0 or v1 message format from the earliest versions of Kafka. Cluster Linking
  can replicate messages in the v2 format (introduced in Apache KafkaÂ® v 0.11) and later. If Cluster Linking encounters a message with the v0 or v1 format,
  it will fail that mirror topic; that is, it will transition to a FAILED state and stop replication for that topic. To replicate a topic that
  contains messages in the v0 or v1 format, either begin replication for that topic after the last message in the v0 or v1 format, using the cluster link
  configuration `mirror.start.offset.spec`, or use [Confluent Replicator](../replicator/index.md#replicator-detail) to replicate topics and messages.
- An issue exists where [consumer group offsets](mirror-topics-cp.md#mirror-topics-consumer-offsets) that are deleted on the destination cluster (especially auto-deleted)
  persist, instead of being removed as expected. (Under the hood, the offsets are being re-replicated to the destination before retention settings delete the offsets from source.
  This results in extended retention of inactive consumer group offsets.) To prevent this from happening, you can extend retention on the destination to make sure data is deleted
  on the source before it is deleted on the destination. To do this, increase `offsets.retention.minutes` on destination cluster by at least double `offsets.retention.check.interval.ms`.
- Cluster Linking does not support the use of a proxy for authentication to the cluster. For supported security configurations, see [Manage Security for Cluster Linking on Confluent Platform](security.md#cluster-link-security).

## Related content

- Blog post: [Building Real-Time Hybrid Architectures with Cluster Linking and Confluent Platform 7.0](https://www.confluent.io/blog/introducing-confluent-platform-7-0/)
- Podcast: [Multi-Cluster Apache Kafka with Cluster Linking ft. Nikhil Bhatia](https://developer.confluent.io/podcast/multi-cluster-apache-kafka-with-cluster-linking-ft-nikhil-bhatia)
- Blog post: [Project Metamorphosis Month 5: Global Event Streaming in Confluent Cloud](https://www.confluent.io/blog/global-event-streaming-with-cluster-linking-confluent-cloud/)
- [Confluentâs Hybrid Cloud and Multicloud Solution Overview](https://www.confluent.io/use-case/hybrid-and-multicloud/), which includes customer testimonials, case studies, and holistic reference architectures
- Kafka Summit video: [Rethinking Geo-replication for the Cloud](https://www.confluent.io/events/kafka-summit-apac-2021/rethinking-geo-replication-for-the-cloud/)
- [Cluster Linking on Confluent Cloud](/cloud/current/multi-cloud/cluster-linking/index.html)
- [Tutorial: Share Data Across Topics Using Cluster Linking for Confluent Platform](topic-data-sharing.md#tutorial-topic-data-sharing)
- [Command Reference for Cluster Linking on Confluent Platform](commands.md#cluster-link-commands)
- [Configure Cluster Linking on Confluent Platform](configs.md#cluster-link-configs)
- [Monitor Cluster Metrics and Optimize Links for Cluster Linking on Confluent Platform](metrics.md#cluster-linking-metrics)
- [Manage Security for Cluster Linking on Confluent Platform](security.md#cluster-link-security)
