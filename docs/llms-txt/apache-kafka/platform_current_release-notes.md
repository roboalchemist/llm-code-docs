# Source: https://docs.confluent.io/platform/current/release-notes/index.md

<a id="release-notes"></a>

# Release Notes for Confluent Platform 8.2

8.2 is a major release of Confluent Platform that provides you with Apache KafkaÂ® 4.2,
the latest stable version of Kafka.

The technical details of this release are summarized below.

<!-- update when blog is released -->
<!-- For more information about the |cp| 8.2 release, check out the -->
<!-- `release blog <https://www.confluent.io/blog/introducing-confluent-platform-8-2/>`__. -->
<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

## Kafka brokers

Confluent Platform 8.2 features Kafka 4.2.

This version of Confluent Platform includes many changes. Before you upgrade to Confluent Platform 8.2, review the [Upgrade Confluent Platform](../installation/upgrade.md#upgrade) guide and
the [Kafka 4.2 upgrade guide](https://kafka.apache.org/documentation/#upgrade). These guides provide detailed,
step-by-step upgrade instructions, rolling upgrade considerations, and information about breaking changes
and compatibility issues.

## Confluent Community software / Kafka

New features in Confluent Platform 8.2 include the following:

* [KIP-932 Queues for Kafka:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-932%3A+Queues+for+Kafka)
  Queues for Kafka is now generally available. This feature provides native queuing capabilities in Kafka
  through share groups and share consumers. Multiple consumers can now process messages from the same
  topic-partition concurrently without manual offset management. This release includes several key enhancements:
  - [KIP-1206 Strict max fetch records in share fetch](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1206%3A+Strict+max+fetch+records+in+share+fetch)
    This KIP strictly enforces the maximum number of records returned in a share consumer fetch request.
    This ensures you have predictable memory usage and prevents the broker from overwhelming consumers with excess data.
  - [KIP-1222 Acquisition lock timeout renewal in share consumer explicit mode](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1222%3A+Acquisition+lock+timeout+renewal+in+share+consumer+explicit+mode)
    The renew acquisition mode lets you prevent locks from timing out during long-running processing tasks,
    ensuring records are not prematurely redelivered to other group members.
  - [KIP-1226 Introducing share partition lag persistence and retrieval](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1226%3A+Introducing+Share+Partition+Lag+Persistence+and+Retrieval)
    This KIP introduces share partition lag metrics. These metrics persist and expose lag information, allowing you
    to monitor how far behind share consumers are within their groups and scale your consumers accordingly.
* [KIP-1071 Streams rebalance protocol:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1071%3A+Streams+Rebalance+Protocol)
  The broker-driven rebalancing system for Kafka Streams applications is now generally available. This protocol
  shifts rebalancing responsibility from clients to brokers, simplifying application management and improving
  rebalance performance.
* [KIP-1216 Add rebalance listener metrics for Kafka Streams:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1216%3A+Add+rebalance+listener+metrics+for+Kafka+Streams)
  This KIP adds metrics to monitor the execution of rebalance listeners. These metrics help you evaluate the performance of
  rebalancing phasesâsuch as partition assignment and revocationâand identify bottlenecks in your application-level
  rebalance logic.
* [KIP-848 Consumer group protocol continued improvements:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-848%3A+The+Next+Generation+of+the+Consumer+Rebalance+Protocol)
  This KIP continues to improve the next-generation consumer group protocol. Key performance enhancements
  include resolving intermittent delays in asynchronous consumer fetches and optimizing CPU usage when using
  small `max.poll.records` configurations, resulting in better client stability.
* [KIP-1224 Adaptive append.linger.ms for the group coordinator and share coordinator:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1224%3A+Adaptive+append.linger.ms+for+the+group+coordinator+and+share+coordinator)
  This KIP introduces adaptive batching for group and share coordinators. The coordinator now automatically adjusts
  the internal `append.linger.ms` value based on your workload to optimize throughput and lower latency for coordinator
  state updates.
* [KIP-1100 Rename org.apache.kafka.server:type=AssignmentsManager and org.apache.kafka.storage.internals.log.RemoteStorageThreadPool metrics:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1100%3A+Rename+org.apache.kafka.server%3Atype%3DAssignmentsManager+and+org.apache.kafka.storage.internals.log.RemoteStorageThreadPool+metrics)
  This KIP renames the JMX MBean names for `AssignmentsManager` and `RemoteStorageThreadPool`
  to follow standard naming conventions. This change improves metric consistency and makes them easier for you to discover.
* [KIP-1179 Introduce remote.log.manager.follower.thread.pool.size config:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1179%3A+Introduce+remote.log.manager.follower.thread.pool.size+config)
  This KIP introduces the `remote.log.manager.follower.thread.pool.size` configuration, and makes it dynamically updatable.
  This lets you adjust the thread pool size for remote log followers without a broker restart, providing better control
  over tiered storage. It also deprecates the older, static `remote.log.manager.thread.pool.size` configuration.
* [KIP-1180 Add generic feature level metrics:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1180%3A+Add+generic+feature+level+metrics)
  This KIP adds new metrics to expose the current version state of cluster features, including `metadata.version`. These metrics are registered under
  `kafka.server:type=FeatureLevel,name=[FeatureName]`. These metrics let you monitor active feature levels across your Kafka cluster programmatically.
* [KIP-1186 Update AddRaftVoterRequest RPC to support auto-join:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1186%3A+Update+AddRaftVoterRequest+RPC+to+support+auto-join)
  This KIP updates the `AddRaftVoterRequest` RPC to allow new KRaft controllers to join the quorum
  automatically. This removes the requirement to manually update the `voters` configuration on all existing
  nodes before adding a new member to the quorum.
* [KIP-1190 Add a metric for controller thread idleness:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1190%3A+Add+a+metric+for+controller+thread+idleness)
  This KIP introduces the `ControllerThreadIdleRatio` metric. This tracks the fraction of time the controller thread
  spends idling, helping you identify when the controller is approaching its maximum processing capacity for metadata operations.
* [KIP-1193 Deprecate MX4J support:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1193%3A+Deprecate+MX4J+Support)
  This KIP deprecates support for MX4J and its associated configurations (`mx4j.enable` and `mx4j.port`).
  If you use MX4J monitoring, you should transition to standard JMX interfaces or built-in metrics reporters.
* [KIP-1197 Introduce new method to improve the TopicBasedRemoteLogMetadataManagerâs initialization:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1197%3A+Introduce+new+method+to+improve+the+TopicBasedRemoteLogMetadataManager%27s+initialization)
  This KIP introduces an optimized initialization workflow for the `TopicBasedRemoteLogMetadataManager`.
  By improving how the manager bootstraps from the internal metadata topic, this change reduces startup
  time for brokers using tiered storage.
* [KIP-1207 Fix RequestHandlerAvgIdlePercent metric in KRaft combined mode:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1207%3A+Fix+anomaly+of+JMX+metrics+RequestHandlerAvgIdlePercent+in+kraft+combined+mode)
  This KIP corrects the `RequestHandlerAvgIdlePercent` metric in KRaft combined mode. The metric now accurately reflects
  the idleness of specific request handler pools rather than incorrectly aggregating data across both broker and controller handlers.
* [KIP-1217 KIP-714 Metrics Plugin Changes:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1217%3A+KIP-714+Metrics+Plugin+Changes)
  This KIP enhances the client telemetry framework introduced in [KIP-714 Client metrics and observability](https://cwiki.apache.org/confluence/display/KAFKA/KIP-714%3A+Client+metrics+and+observability).
  by adding `push_interval_ms` to the `ClientTelemetryReceiver` context.
  This allows your custom telemetry plugins to know exactly how often a client is configured to push metrics,
  enabling more accurate server-side data aggregation.
* [KIP-1228 Add transaction version to WriteTxnMarkersRequest:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1228%3A+Add+Transaction+Version+to+WriteTxnMarkersRequest)
  This KIP adds a transaction version field to the `WriteTxnMarkersRequest` RPC, which strengthens transaction
  guarantees and enables better coordination between transaction coordinators and partition leaders.
* [KIP-1229 Add idle thread ratio metric to MetadataLoader:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1229%3A+Add+Idle+Thread+Ratio+Metric+to+MetadataLoader)
  This KIP adds the `MetadataLoaderIdleRatio` metric to track how much time the metadata loader thread spends waiting
  for new metadata images. This metric is essential for diagnosing delays in how quickly a broker applies updates
  from the KRaft controller.
* [KIP-1147 Improve consistency of command-line arguments:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1147%3A+Improve+consistency+of+command-line+arguments)
  This KIP standardizes command-line argument naming across Kafka tools to provide a more consistent user experience. Key changes include adding the
  `--bootstrap-server` flag to tools like `kafka-producer-perf-test.sh` and `kafka-metadata-shell.sh`. It also standardizes `--command-property`
  for individual configuration overrides and `--command-config` for configuration files, replacing legacy tool-specific flags such as `--producer-property`,
  `--consumer-property`, and `--consumer.config`.
* [KIP-1160 Enable returning supported features from a specific broker:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1160%3A+Enable+returning+supported+features+from+a+specific+broker)
  This KIP enhances the `Admin.describeFeatures()` API to let you query supported features from a specific broker by its node ID.
  It also updates the `kafka-features.sh` tool with a new `--node-id` option. This lets you verify feature compatibility on individual
  nodes, which is especially useful during rolling upgrades.
* [KIP-1172 Improve EndtoEndLatency tool:](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=347933443)
  This KIP refactors the `EndToEndLatency` tool to improve its usability and standardizes its parameters. It introduces common flags
  including `--bootstrap-server`, `--topic`, `--num-records`, and `--record-size`. It also adds the ability to pass specific client
  configurations using `--producer-props` and `--consumer-props`.
* [KIP-1192 Add include argument to ConsumerPerformance tool:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1192%3A+Add+include+argument+to+ConsumerPerformance+tool)
  This KIP adds the `include` argument to the `kafka-consumer-perf-test.sh` tool. This lets you provide a regular expression
  to select multiple topics for performance testing, aligning the toolâs behavior with the standard Kafka consumer.
* [KIP-1227 Expose rack ID in MemberDescription and ShareMemberDescription:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1227%3A+Expose+Rack+ID+in+MemberDescription+and+ShareMemberDescription)
  This KIP adds the `rackId()` method to the `MemberDescription` and `ShareMemberDescription` classes in the Admin API.
  This lets you retrieve the rack information for members of consumer groups and share groups, helping you
  verify rack-aware assignments and troubleshoot distribution issues across your infrastructure.
* [KIP-1157 Enforce KafkaPrincipalSerde Implementation for KafkaPrincipalBuilder:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1157%3A+Enforce+KafkaPrincipalSerde+Implementation+for+KafkaPrincipalBuilder)
  This KIP introduces a source-incompatible change. If you have custom `KafkaPrincipalBuilder` implementations,
  you must now implement `KafkaPrincipalSerde` methods to handle principal serialization and deserialization.
  Update and recompile your custom principal builders against the new libraries to prevent runtime errors in KRaft mode.
* [KIP-1052 Enable warmup in producer perf test:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1052%3A+Enable+warmup+in+producer+performance+test)
  This KIP adds the `--warmup-records` option to the `kafka-producer-perf-test` tool. This lets you define a specific number of
  records to send before the main performance test begins.

For a full list of KIPs, features, and bug fixes, see the [Apache Kafka 4.2 release notes](https://archive.apache.org/dist/kafka/4.2.0/RELEASE_NOTES.html).
You can also watch the Kafka 4.2 release video that follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4Yw1TzJe1Z8?si=WcGOVcFCxmGgpwEl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Clients

This release updates client libraries with the following improvements:

* [KIP-1120 Add client-id to AppInfo metrics:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1120%3A+AppInfo+metrics+don%27t+contain+the+client-id)
  This KIP adds the `client-id` tag to `AppInfo` metrics. This prevents MBean name collisions when you run multiple Kafka clients in the same JVM,
  which lets you monitor each instance uniquely using JMX.
* [KIP-1136 Make ConsumerGroupMetadata an interface:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1136%3A+Make+ConsumerGroupMetadata+an+interface)
  This KIP converts `ConsumerGroupMetadata` from a concrete class to an interface. This change ensures that you use the metadata
  instances provided directly by the consumer rather than instantiating them manually to bypass deprecation warnings in other APIs.
* [KIP-1161 Unifying list-type configuration validation and default values:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1161%3A+Unifying+LIST-Type+Configuration+Validation+and+Default+Values)
  This KIP standardizes how `ConfigDef` validates list-type configurations. It ensures that default values are validated using the same
  logic as user-supplied values and provides consistent handling of empty strings and whitespace across all Kafka components.
* [KIP-1175 Fix typo in producer config:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1175%3A+Fix+the+typo+%60PARTITIONER_ADPATIVE_PARTITIONING_ENABLE%60+in+ProducerConfig)
  This KIP corrects a typo in the `ProducerConfig` constant name and its corresponding string. The misspelled `PARTITIONER_ADPATIVE_PARTITIONING_ENABLE_CONFIG`
  (`partitioner.adpative.partitioning.enable`) is now deprecated in favor of the correctly spelled `PARTITIONER_ADAPTIVE_PARTITIONING_ENABLE_CONFIG`.
  Both versions remain supported for backward compatibility.
* [KIP-1205 Improve RecordHeader to be thread-safe:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1205%3A+Improve+RecordHeader+to+be+Thread-Safe)
  This KIP enhances the `RecordHeader` implementation to be thread-safe. This prevents
  concurrency issues when record headers are accessed or modified by multiple threads simultaneously.

<!-- commented out for now
.. |af-cp-long| -->
<!-- """""""""""" -->
<!-- .. .. important:: -->
<!-- Starting with |cp| 8.2, |af-cp-long| follows separate versioning, beginning with version 2.3, -->
<!-- and has separate documentation. For detailed information, see the -->
<!-- `Confluent Platform for Apache Flink documentation <https://docs.confluent.io/platform/current/flink/index.html>`__. -->
<!-- .. |af-cp-long| version 2.3 includes the following changes in |cp| 8.2: -->
<!-- * Flink SQL is now generally available (GA) in |af-cp-long|. You can now: -->
<!-- * Discover and manage |af| SQL catalogs registered with |af-cp-long|. -->
<!-- * Configure secrets and compute pools used by SQL statements. -->
<!-- * Author and submit Flink SQL statements, and inspect statement states and recent results using the |confluent-cli| or the |c3++|. -->
<!-- * For |af-cp-long| 2.3: -->
<!-- * Adds support for ``CREATE TABLE`` and ``DROP TABLE`` statements. These statements let you manage |ak| topics and |sr| data declaratively. -->
<!-- * Enables the use of ``ALTER TABLE`` to modify the properties of SQL tables that are inferred from existing |ak| topics. With property modifications, -->
<!-- you can control the semantics of source or sink data by modifying watermarking settings or configuring upsert and retraction semantics. -->
<!-- Running queries can produce updating results, such as joins or aggregations, or various kinds of windowing operators. -->
<!-- * Includes a new ``shared`` compute pool type that enables optimization of resources when running multiple SQL statements in the same |af| session cluster. -->
<!-- * Provides new features to help you reduce the complexity of managing |af| estates: -->
<!-- * You can run |af| applications in multiple Kubernetes clusters. -->
<!-- * You can use |c3++| to manage savepoints and large volumes of resource labels. -->
<!-- * |af-cp-long| is now OpenShift certified. -->

## Cluster management

### Confluent for Kubernetes

For Confluent for Kubernetes release notes, see [Confluent for Kubernetes Release Notes](https://docs.confluent.io/operator/current/release-notes.html).

### Ansible Playbooks for Confluent Platform

For Ansible Playbooks for Confluent Platform release notes, see the [Ansible Playbooks for Confluent Platform](https://docs.confluent.io/ansible/7.4/overview.html).

## Confluent Control Center

Starting with Confluent Platform 8.0, Confluent Control Center packages are hosted in a separate repository under the name
`confluent-control-center-next-gen`, beginning with version 2.0. Control Center is now shipped
independently of Confluent Platform releases. For more information, see the [support plans and compatibility](https://docs.confluent.io/platform/current/control-center/installation/overview.html#compatibility-with-cp) documentation
and the [Control Center Next-Gen Release Notes](https://docs.confluent.io/control-center/2.2/release-notes.html).

<a id="release-notes-streams"></a>

## Kafka Streams

Kafka Streams includes the following changes in Confluent Platform 8.2.

* [KIP-1034 Dead letter queue in Kafka Streams:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1034%3A+Dead+letter+queue+in+Kafka+Streams)
  This KIP adds native dead-letter queue (DLQ) support to Kafka Streams. You can now configure your application
  to redirect records that fail processing or serialization to a designated âdead-letterâ topic. This prevents
  a single malformed record from stopping your entire pipeline and lets you analyze or reprocess failed data later.
* [KIP-1146 Anchored punctuation:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1146%3A+Anchored+Punctuation)
  This KIP introduces anchored punctuation, letting you schedule punctuations to trigger at specific
  intervals relative to a fixed point in time. This supports both stream-time and wall-clock
  time, ensuring that periodic tasksâsuch as windowing or cleanupâoccur at predictable, aligned boundaries
  regardless of when the application started.
* [KIP-1153 Refactor Kafka Streams CloseOptions to fluent API style:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1153%3A+Refactor+Kafka+Streams+CloseOptions+to+Fluent+API+Style)
  This KIP refactors the `CloseOptions` class to use a fluent API style. This change makes it easier for you to
  chain configuration methods when closing a `KafkaStreams` instance, improving code readability and developer
  experience.
* [KIP-1195 Deprecate and remove org.apache.kafka.streams.errors.BrokerNotFoundException:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1195%3A+deprecate+and+remove+org.apache.kafka.streams.errors.BrokerNotFoundException)
  This KIP removes the unused and redundant `BrokerNotFoundException`. Because this exception was rarely thrown
  and overlaps with the standard TimeoutException during metadata lookups, it has been removed to simplify
  the Kafka Streams error hierarchy.
* [KIP-1221 Add application-id tag to Kafka Streams state metric:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1221%3A+Add+application-id+tag+to+Kafka+Streams+state+metric)
  This KIP adds the `application-id` tag to the state metric in Kafka Streams. This lets you
  differentiate between multiple Streams applications running within the same JVM or process when
  monitoring the lifecycle state (such as `RUNNING` or `REBALANCING`) using JMX.
* [KIP-1230 Add config for file system permissions:](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1230%3A+Add+config+for+file+system+permissions)
  This KIP introduces the `state.dir.permission` configuration for Kafka Streams. You can now explicitly
  set the POSIX file permissions (for example, `700`) for the local state directory created by the Streams application.
  This provides better security and compliance in multi-tenant environments by ensuring that state stores are
  only accessible by the authorized user.

## Schema Registry

Schema Registry includes the following changes in Confluent Platform 8.2.

* The `/mode` delete operation now supports a `recursive` flag. When you set
  this flag to `true`, the operation deletes the mode for all subjects in the default
  context. For example, `/mode?recursive=true`.
* The `GET /contexts` endpoint now accepts an optional `contextPrefix` query parameter.
  When you provide this parameter, the endpoint returns only contexts that begin with
  the specified prefix. For example, `GET /contexts?contextPrefix=.ctx`.
* The `GET /subjects/{subject}/metadata` and `POST /subjects/{subject}/versions`
  endpoints now support a new `Confluent-Accept-Unknown-Properties` header. When you
  set this header to `true`, the response includes fields added in version 8.0,
  such as `Guid`.
* Authorization checks now prevent unauthorized cross-context schema access during
  unqualified subject lookups. If you attempt to access schemas across contexts without
  proper permissions, the server returns a `403 Forbidden` error.
  The following configurations control this behavior:
  - `confluent.schema.registry.context.authorization.enabled`: Enables the authorization
    check. The default value is `false`.
  - `confluent.schema.registry.context.authorization.excluded.principals`: Specifies
    a list of principals, such as administrators, that are exempt from these checks.

## Kafka Connect

Kafka Connect includes the following changes in Confluent Platform 8.2.

### Credential masking enhancement

Kafka Connect masks sensitive and password-type configuration fields in connector REST API responses with asterisks (`*`) to prevent sensitive data exposure and improve security.
Masking is enabled by default. If your deployment uses the Kafka Connect REST API to extract connector secrets, this change affects your workflows.
For more information, see the [Masking of plaintext credentials via the connectors REST endpoint](https://support.confluent.io/hc/en-us/articles/44021406187668-Masking-of-plaintext-credentials-via-the-connectors-REST-endpoint) advisory.

To control this behavior, use the `connect.password.field.masking.disable` configuration property, which defaults to `false`.

Confluent Platform 8.2 includes the following credential masking improvements:

* Confluent for Kubernetes (CFK) reconciliation loops now work with credential masking enabled.
  CFK can manage connectors as custom resources (CRs) when you enable credential masking.
* The masking logic now provides more comprehensive protection of credentials in connector REST API responses.

### Connector Versions

In line with the [Support policy for self-managed connectors](../connect/supported.md#support-lifecycle-policy-sm-connectors), a specific minimum version of connectors is required for support in Confluent Platform 8.2.
For details, see [Supported Connector Versions in Confluent Platform 8.2](../connect/supported-connector-version.md#minimum-connector-version-8-2).

## Unified Stream Manager

For Unified Stream Manager updates, see the [Supported Versions and Interoperability for Confluent Platform](../installation/versions-interoperability.md#interoperability-versions) documentation and [Confluent Cloud release notes](https://docs.confluent.io/cloud/current/release-notes/index.html).

## ksqlDB

ksqlDB continues to be available as part of Confluent Platform 8.2. For more information, see
[Use Docker to Install ksqlDB for Confluent Platform](../ksqldb/operate-and-deploy/installation/install-ksqldb-with-docker.md#ksqldb-install-configure-with-docker).

## Confluent Private Cloud

All Confluent Private Cloud features require a valid license to function correctly. For information about managing your license, see [Manage Confluent Platform Licenses](../installation/license.md#cp-license-overview).

## Security

* Confluent Platform 8.2 supports FIPS 140-3 compliance. This ensures that cryptographic
  modules meet the updated security requirements specified by the Federal Information Processing Standard (FIPS).
* The Metadata Service (MDS) includes enhancements for File Store-based user identities. These enhancements
  improve identity management capabilities. This helps avoid restarts for user identity refresh when `FILE` Store is used for user identities by hot reloading.

  Additionally, MDS enforces security checks on the FILE user store credentials file and its containing directory permissions.

  If you are upgrading your Confluent Platform and use FILE-based user store
  (`confluent.metadata.server.user.store=FILE`), you must verify that the password
  file and its containing directory permissions meet the following security requirements
  before upgrading. If you are not using orchestration tools like
  Confluent for Kubernetes or Ansible Playbooks for Confluent Platform, you must correct these permissions manually:
  - The password file must not be world-readable.
  - The directory containing the password file must not be world-writable, unless the
    sticky bit is set.

  If these permissions are not corrected before the upgrade, MDS will fail to start.
  For details, see [Security checks on FILE and directory permissions](../kafka/configure-mds/mds-file-configuration.md#mds-file-security-checks).

<a id="other-improvements-and-changes"></a>

## Other improvements and changes

This release includes the following additional improvements and changes.

### Docker base image transition

Starting with Confluent Platform 8.3.0, all Confluent Platform Docker images use a `ubi-micro` base image. Confluent Platform 8.2 and
earlier versions use the `ubi-minimal` base image.

## Deprecation warnings

This release includes the following deprecation warnings.

### Docker image retention policy

To ensure the security and performance of the Confluent registry, Confluent removes Docker images for
end-of-life (EOL) versions from public access.

Confluent recommends upgrading regularly to newer versions of supported images for improved performance,
security, and user experience. If you use legacy versions, migrate to a supported release to avoid
disruptions.

### Confluent Health+

Confluent Health+ is entering its end-of-life (EOL) process. Health+ is deprecated and users
should plan to migrate to Unified Stream Manager (USM). While Health+ remains operational for existing
users, it is scheduled to be retired, or to sunset, in 2026. Starting with Confluent Platform version 8.1,
Health+ is discontinued for new deployments and Unified Stream Manager is the recommended alternative for all users.

To begin your migration planning, see [Unified Stream Manager in Confluent Platform](../usm/overview.md#usm-overview).

### Confluent Manager for Apache Flink version 1

Confluent is deprecating Confluent Manager for Apache Flink (CMF) version 1.x. If you use this version,
you should migrate to CMF version 2.2 or later, which is backwards compatible. Support for patching and
bug fixes ends on May 25, 2025, and CMF version 1.1 will be fully deprecated in September 2026.

## Supported versions and interoperability

For the full list of supported versions and interoperability of Confluent Platform and its components,
see [Supported Versions and Interoperability for Confluent Platform](../installation/versions-interoperability.md#interoperability-versions).

<a id="release-notes-download"></a>

## How to download

You can download Confluent Platform at [https://confluent.io/download/](https://www.confluent.io/download/#confluent-platform). For detailed information,
see the [Install Confluent Platform On-Premises](../installation/overview.md#installation) section.

#### IMPORTANT
The Confluent Platform package includes Confluent Server by default and requires a
`confluent.license` key in your `server.properties` file.
The Confluent Server broker checks for a license during start up. You must
supply a license string in each brokerâs properties file using the
`confluent.license` property as shown in the following code:

```none
confluent.license=LICENCE_STRING_HERE_NO_QUOTES
```

If you want to use the Kafka broker, download the `confluent-community` package.
The Kafka broker is the default in all Debian or RHEL and CentOS packages.

For more information about migrating to Confluent Server, see [Migrate Confluent Platform to Confluent Server](../installation/migrate-confluent-server.md#migrate-confluent-server).

To upgrade Confluent Platform to a newer version, see the [Upgrade Confluent Platform](../installation/upgrade.md#upgrade) documentation.

<a id="release-notes-question"></a>

## Questions?

If you have questions about this release, you can reach out through the
[community mailing list](https://groups.google.com/forum/?pli=1#!forum/confluent-platform) or
[community Slack](https://slackpass.io/confluentcommunity). If you are a Confluent customer, you are encouraged to
contact our support team directly.

To provide feedback on the Confluent documentation, click the **Give us feedback** button
located near the footer of each page.
