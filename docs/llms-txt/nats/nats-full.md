# Nats Documentation

Source: https://docs.nats.io/llms-full.txt

---

# Welcome

## The official [NATS](https://nats.io/) documentation

NATS is a simple, secure and high performance open source data layer for cloud native applications, IoT messaging, and microservices architectures.

We feel that it should be the backbone of your communication between services. It doesn't matter what language, protocol, or platform you are using; NATS is the best way to connect your services.

### 10,000 foot view

* Publish and subscribe to messages at millions of messages per second. At most once delivery.
* Supports fan-in/out delivery patterns
* Request/reply
* Every major language is supported
* Persistence via JetStream
  * at least once delivery or **exactly once** delivery
  * work queues
  * stream processing
  * data replication
  * data retention
  * data deduplication
  * Higher order data structures
    * Key/Value with watchers, versioning, and TTL
    * Object storage with versioning
* Security
  * TLS
  * JWT-based zero trust security
* Clustering
  * High availability
  * Fault tolerance
  * Auto-discovery
* Protocols supported
  * TCP
  * MQTT
  * WebSockets

All of this in a single binary that is easy to deploy and manage. No external dependencies, just drop it in and add a configuration file to point to other NATS servers and you are ready to go. In fact, you can even embed NATS in your application (for Go users)!

## Guided tour

1. In general we recommend trying to solve your problems first using [Core NATS](https://docs.nats.io/nats-concepts/core-nats).
2. If you need to share state between services, take a look at the [KV](https://docs.nats.io/nats-concepts/jetstream/key-value-store) or [Object Store](https://docs.nats.io/nats-concepts/jetstream/obj_store) in JetStream.
3. When you need lower level access to persistence streams, move on to using [JetStream](https://docs.nats.io/nats-concepts/jetstream) directly for more advanced messaging patterns.
4. Learn about [deployment strategies](https://docs.nats.io/nats-concepts/service_infrastructure/adaptive_edge_deployment)
5. Secure your deployments with [zero trust security](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt)

## Contribute

NATS is Open Source as is this documentation. Please [let us know](mailto:info@nats.io) if you have updates and/or suggestions for these docs. You can also create a Pull Request using the `Edit on GitHub` link on each page.

## Additional questions?

Feel free to chat with us on Slack [slack.nats.io](https://slack.nats.io).

Thank you from the entire NATS Team of Maintainers for your interest in NATS!


# What's New!

The NATS.io team is continually working to bring you features that enhance your NATS experience. Below, you will find summaries of new NATS implementations. Release notes for the latest patch releases are available on [GitHub Releases](https://github.com/nats-io/nats-server/releases)

## Roadmap for future releases

See <https://nats.io/about/#roadmap>

## Server release v2.12.0

Check out the:

* [Upgrade guide](https://docs.nats.io/release-notes/whats_new/whats_new_212)
* [Release notes](https://github.com/nats-io/nats-server/releases/tag/v2.12.0)

## Server release v2.11.0

Check out the:

* [Upgrade guide](https://docs.nats.io/release-notes/whats_new/whats_new_211)
* [Release notes](https://github.com/nats-io/nats-server/releases/tag/v2.11.0)

## Server release v2.10.0

Check out the:

* [Upgrade guide](https://docs.nats.io/release-notes/whats_new/whats_new_210)
* [Podcast EP06: The journey and features of the NATS.io 2.10 release](https://youtu.be/9J4pRzHSc2k)
* [Release notes](https://github.com/nats-io/nats-server/releases/tag/v2.10.0)

## Server release v2.9.0

Please check out the [announcement post](https://nats.io/blog/nats-server-29-release/) on the blog and the [detailed release notes](https://github.com/nats-io/nats-server/releases/tag/v2.9.0) in the server repo.

## Server release v2.8.0

### LeafNode

Support for a `min_version` in the `leafnodes{}` that would reject servers with a lower version. Note that this would work only for servers that are v2.8.0 and above.

### Monitoring

* Server version in monitoring landing page.
* Logging to `/healthz` endpoint when failure occurs.
* MQTT and Websocket blocks in the `/varz` endpoint.

### JetStream

* Consumer check added to `healthz` endpoint.
* Max stream bytes checks.
* Ability to limit a consumer's `MaxAckPending` value.
* Allow streams and consumers to migrate between clusters. *This feature is considered "beta"*.
* New `unique_tag` option in `jetstream{}` configuration block to prevent placing a stream in the same availability zone twice.
* Stream `Alternates` field in `StreamInfo` response. They provide a priority list of mirrors and the source in relation to where the request originated.
* Deterministic subject tokens to partition mapping.

For full release information, see links below;

* Release notes [2.8.0](https://github.com/nats-io/nats-server/releases/tag/v2.8.0)
* Full list of Changes [2.7.4...2.8.0](https://github.com/nats-io/nats-server/compare/v2.7.4...v2.8.0)

## Server release v2.7.0

### **Notice for JetStream Users**

See [important note](https://github.com/nats-io/nats-server/pull/2693#issuecomment-996212582) if using LeafNode regarding domains.

### Configuration

Ability to configure account limits (`max_connections`, `max_subscriptions`, `max_payload`, `max_leafnodes`) in server configuration file.

### JetStream

* Overflow placement for streams. A stream can now be placed in the closest cluster from the origin request if it can be placed there.
* Support for ephemeral Pull consumers (client libraries will need to be updated to allow those).
* New consumer configuration options
  * For Pull Consumers: `MaxRequestBatch` to limit the batch size any client can request `MaxRequestExpires` to limit the expiration any client can request
  * For ephemeral consumers: `InactiveThreshold` duration that instructs the server to cleanup ephemeral consumers that are inactive for that long.
* Ability to configure `max_file_store` and `max_memory_store` in the `jetstream{}` block as strings with the following suffixes `K`, `M`, `G` and `T`, for instance: `max_file_store: "256M"`.
* Support for the JWT field `MaxBytesRequired`, which defines a per-account maximum bytes for assets.

### MQTT

Support for websocket protocol. MQTT clients must connect to the opened websocket port and add `/mqtt` to the URL path.

### TLS

Ability to rate-limit the clients connections by adding the `connection_rate_limit: <number of connections per seconds>` in the `tls{}` top-level block.

For full release information, see links below;

* Release notes [2.7.0](https://github.com/nats-io/nats-server/releases/tag/v2.7.0)
* Full list of Changes [2.6.6...2.7.0](https://github.com/nats-io/nats-server/compare/v2.6.6...v2.7.0)

## Server release v2.6.0

### **Notice for JetStream Users**

See important [note](https://github.com/nats-io/nats-server/releases/tag/v2.4.0) if upgrading from a version prior to NATS Server v2.4.0.

### Notice for MQTT Users

See important [notes](https://github.com/nats-io/nats-server/releases/tag/v2.5.0) if upgrading from a version prior to v2.5.0.

### Monitoring

* JetStream's reserved memory and memory used from accounts with reservations in `/jsz` and `/varz` endpoints.
* Hardened systemd service.

For full release information, see links below;

* Release notes [2.6.0](https://github.com/nats-io/nats-server/releases/tag/v2.6.0)
* Full list of Changes [2.5.0...2.6.0](https://github.com/nats-io/nats-server/compare/v2.6.0...v2.5.0)

## Server release v2.5.0

### **Notice for JetStream Users**

See important [note](https://github.com/nats-io/nats.docs/blob/master/release_notes/README.md#notice-for-jetstream-users) if upgrading from a version prior to NATS Server v2.4.0.

### MQTT/Monitoring

* `MQTTClient` in the `/connz` connections report and system events CONNECT and DISCONNECT. Ability to select on `mqtt_client`.

### MQTT Improvement

* Sessions are now all stored inside a single stream, as opposed to individual streams, reducing resources usage.

### MQTT Update

* Due to the aforementioned improvement described above, when an MQTT client connects for the first time after an upgrade to this server version, the server will migrate all individual `$MQTT_sess_<xxxx>` streams to a new `$MQTT_sess` stream for the user's account.

For full release information, see links below;

* Release notes [2.5.0](https://github.com/nats-io/nats-server/releases/tag/v2.5.0)
* Full list of Changes [2.4.0...2.5.0](https://github.com/nats-io/nats-server/compare/v2.4.0...v2.5.0)

## Server release v2.4.0

### Notice for JetStream Users

With the latest release of the NATS server, we have fixed bugs around queue subscriptions and have restricted undesired behavior that could be confusing or introduce data loss by unintended/undefined behavior of client applications. If you are using queue subscriptions on a JetStream Push Consumer or have created multiple push subscriptions on the same consumer, you may be affected and need to upgrade your client version along with the server version. We’ve detailed the behavior with different client versions below.

With a NATS Server **prior** to v2.4.0 and client libraries **prior** to these versions: NATS C client v3.1.0, Go client v1.12.0, Java client 2.12.0-SNAPSHOT, NATS.js v2.2.0, NATS.ws v1.3.0, NATS.deno v1.2.0, NATS .NET 0.14.0-pre2:

* It was possible to create multiple non-queue subscription instances for the same JetStream durable consumer. This is not correct since each instance will receive the same copy of a message and acknowledgment is therefore meaningless since the first instance to acknowledge the message will prevent other instances to control if/when a message should be acknowledged.
* Similar to the first issue, it was possible to create many different queue groups for one single JetStream consumer.
* For queue subscriptions, if no consumer nor durable name was provided, the libraries would create ephemeral JetStream consumers, which meant that each member of the same group would receive the same message as the other members, which was not the expected behavior. Users assumed that 2 members subscribing to “foo” with the queue group named “bar” would load-balance the consumption of messages from the stream/consumer.
* It was possible to create a queue subscription on a JetStream consumer configured with heartbeat and/or flow control. This does not make sense because by definition, queue members would receive some (randomly distributed) messages, so the library would think that heartbeats are missed, and flow control would also be disrupted.

If above client libraries are not updated to the latest but the NATS Server is upgraded to v2.4.0:

* It is still possible to create multiple non-queue subscription instances for the same JetStream durable consumer. Since the check is performed by the library (with the help of a new field called `PushBound` in the consumer information object set by the server), this misbehavior is still possible.
* Queue subscriptions will not receive any message. This is because the server now has a new field `DeliverGroup` in the consumer configuration, which won’t be set for existing JetStream consumers and by the older libraries, and detects interest (and starts delivering) only when a subscription on the deliver subject for a queue subscription matching the “deliver group” name is found. Since the JetStream consumer is thought to be a non-deliver-group consumer, the opposite happens: the server detects a core NATS *queue* subscription on the “deliver subject”, therefore does not trigger delivery on the JetStream consumer’s “deliver subject”.

The 2 other issues are still present because those checks are done in the updated libraries.

If the above client libraries are updated to the latest version, but the NATS Server is still to version prior to v2.4.0 (that is, up to v2.3.4):

* It is still possible to create multiple non-queue subscription instances for the same JetStream durable consumer. This is because the JetStream consumer’s information retrieved by the library will not have the `PushBound` boolean set by the server, therefore will not be able to alert the user that they are trying to create multiple subscription instances for the same JetStream consumer.
* Queue subscriptions will fail because the consumer information returned will not contain the `DeliverGroup` field. The error will be likely to the effect that the user tries to create a queue subscription to a non-queue JetStream consumer. Note that if the application creates a queue subscription for a non-yet created JetStream consumer, then this call will succeed, however, adding new members or restarting the application with the now existing JetStream consumer will fail.
* Creating queue subscriptions without a named consumer/durable will now result in the library using the queue name as the durable name.
* Trying to create a queue subscription with a consumer configuration that has heartbeat and/or flow control will now return an error message.

For completeness, using the latest client libraries and NATS Server v2.4.0:

* Trying to start multiple non-queue subscriptions instances for the same JetStream consumer will now return an error to the effect that the user is trying to create a “duplicate subscription”. That is, there is already an active subscription on that JetStream consumer. It is now only possible to create a queue group for a JetStream consumer created for that group. The `DeliverGroup` field will be set by the library or need to be provided when creating the consumer externally.
* Trying to create a queue subscription without a durable nor consumer name results in the library creating/using the queue group as the JetStream consumer’s durable name.
* Trying to create a queue subscription with a consumer configuration that has heartbeat and/or flow control will now return an error message.

Note that if the server v2.4.0 recovers existing JetStream consumers that were created prior to v2.4.0 (and with older libraries), none of them will have a `DeliverGroup`, so none of them can be used for queue subscriptions. They will have to be recreated.

### JetStream

* Domain to the content of a `PubAck` protocol
* `PushBound` boolean in `ConsumerInfo` to indicate that a push consumer is already bound to an active subscription
* `DeliverGroup` string in `ConsumerConfig` to specify which deliver group (or queue group name) the consumer is created for
* Warning log statement in situations where catchup for a stream resulted in an error

### Monitoring

* The ability for normal accounts to access scoped `connz` information

### Misc

* Operator option `resolver_pinned_accounts` to ensure users are signed by certain accounts

For full release information, see links below;

* Release notes [2.4.0](https://github.com/nats-io/nats-server/releases/tag/v2.4.0)
* Full list of Changes [2.3.4...2.4.0](https://github.com/nats-io/nats-server/compare/v2.3.4...v2.4.0)

## Server release v2.3.0

* [OCSP support](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/ocsp)

### JetStream

* Richer API errors. JetStream errors now contain an ErrCode that uniquely describes the error.
* Ability to send more advanced Stream purge requests that can purge all messages for a specific subject
* Stream can now be configured with a per-subject message limit
* Encryption of JetStream data at rest

For full release information, see links below;

* Release notes [2.3.0](https://github.com/nats-io/nats-server/releases/tag/v2.3.0)
* Full list of Changes [2.2.6...2.3.0](https://github.com/nats-io/nats-server/compare/v2.2.6...v2.3.0)

## Server release v2.2.0

See [NATS 2.2](https://docs.nats.io/release-notes/whats_new/whats_new_22) for new features.

## Server release v2.1.7

### Monitoring Endpoints Available via System Services

Monitoring endpoints as listed in the table below are accessible as system services using the following subject pattern:

* `$SYS.REQ.SERVER.<id>.<endpoint-name>` (request server monitoring endpoint corresponding to endpoint name.)
* `$SYS.REQ.SERVER.PING.<endpoint-name>` (from all server request server monitoring endpoint corresponding to endpoint name - will return multiple messages)

For more information on monitoring endpoints see [NATS Server Configurations System Events](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts).

### Addition of `no_auth_user` Configuration

Configuration of `no_auth_user` allows you to refer to a configured user/account when no credentials are provided.

For more information and examples, see [Securing NATS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats)

For full release information, see links below;

* Release notes [2.1.7](https://github.com/nats-io/nats-server/releases/tag/v2.1.7)
* Full list of Changes [2.1.6...2.1.7](https://github.com/nats-io/nats-server/compare/v2.1.6...v2.1.7)

## Server release v2.1.6

### TLS Configuration for Account Resolver

This release adds the ability to specify TLS configuration for the account resolver.

```
resolver_tls {
  cert_file: ...
  key_file: ...
  ca_file: ...
}
```

### Additional Trace & Debug Verbosity Options

`trace_verbose` and command line parameters `-VV` and `-DVV` added. See [NATS Logging Configuration](https://docs.nats.io/running-a-nats-service/configuration/logging#configuring-logging)

### Subscription Details in Monitoring Endpoints

We've added the option to include subscription details in monitoring endpoints `/routez` and `/connz`. For instance `/connz?subs=detail` will now return not only the subjects of the subscription, but the queue name (if applicable) and some other details.

* Release notes [2.1.6](https://github.com/nats-io/nats-server/releases/tag/v2.1.6)
* Full list of Changes [2.1.4...2.1.6](https://github.com/nats-io/nats-server/compare/v2.1.4...v2.1.6)

## Server release v2.1.4

### Log Rotation

NATS introduces `logfile_size_limit` allowing auto-rotation of log files when the size is greater than the configured limit set in `logfile_size_limit` as a number of bytes. You can provide the size with units, such as MB, GB, etc. The backup files will have the same name as the original log file with the suffix .yyyy.mm.dd.hh.mm.ss.micros. For more information see Configuring Logging in the [NATS Server Configuration section](https://docs.nats.io/running-a-nats-service/configuration/logging).

* Release notes [2.1.4](https://github.com/nats-io/nats-server/releases/tag/v2.1.4)
* Full list of Changes [2.1.2...2.1.4](https://github.com/nats-io/nats-server/compare/v2.1.2...v2.1.4)

## Server release v2.1.2

### Queue Permissions

Queue Permissions allow you to express authorization for queue groups. As queue groups are integral to implementing horizontally scalable microservices, control of who is allowed to join a specific queue group is important to the overall security model. Original PR - <https://github.com/nats-io/nats-server/pull/1143>

More information on Queue Permissions can be found in the [Developing with NATS](https://docs.nats.io/using-nats/developer/receiving/queues) section.

## Server release v2.1.0

### Service Latency Tracking

As services and service mesh functionality has become prominent, we have been looking at ways to make running scalable services on NATS.io a great experience. One area we have been looking at is observability. With publish/subscribe systems, everything is inherently observable, however we realized it was not as simple as it could be. We wanted the ability to transparently add service latency tracking to any given service with no changes to the application. We also realized that global systems, such as those NATS.io can support, needed something more than a single metric. The solution was to allow any sampling rate to be attached to an exported service, with a delivery subject for all collected metrics. We collect metrics that show the requestor’s view of latency, the responder’s view of latency and the NATS subsystem itself, even when requestor and responder are in different parts of the world and connected to different servers in a NATS supercluster.

* Release notes [2.1.0](https://github.com/nats-io/nats-server/releases/tag/v2.1.0)
* Full list of Changes [2.0.4...2.1.0](https://github.com/nats-io/nats-server/compare/v2.0.4...v2.1.0)

## Server release v2.0.4

### Response Only Permissions

For services, the authorization for responding to requests usually included wildcards for \_INBOX.> and possibly $GR.> with a supercluster for sending responses. What we really wanted was the ability to allow a service responder to only respond to the reply subject it was sent.

### Response Types

Exported Services were originally tied to a single response. We added the type for the service response and now support singletons (default), streams and chunked. Stream responses represent multiple response messages, chunked represents a single response that may have to be broken up into multiple messages.

* Release notes [2.0.4](https://github.com/nats-io/nats-server/releases/tag/v2.0.4)
* Full list of Changes [2.0.2...2.0.4](https://github.com/nats-io/nats-server/compare/v2.0.2...v2.0.4)


# NATS 2.12

This guide is tailored for existing NATS users upgrading from NATS version v2.11.x. This will read as a summary with links to specific documentation pages to learn more about the feature or improvement.

## Features

### Streams

* **Atomic batch publish:** The `AllowAtomicPublish` stream configuration option allows to atomically publish N messages into a stream. This includes support for replicated and non-replicated streams, as well as doing per-message consistency checks prior to committing the batch. More information is available in [ADR-50](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-50.md).
* **Distributed Counter CRDT:** The `AllowMsgCounter` stream configuration option allows increment/decrement counter semantics on a stream. These counter streams can also be mirrored or aggregated through stream mirroring and sourcing. More information is available in [ADR-49](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-49.md)
* **Delayed Message Scheduling:** The `AllowMsgSchedules` stream configuration option allows the scheduling of messages. Users can use this feature for delayed publishing/scheduling of messages. More information is available in [ADR-51](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-51.md)

### Consumers

* **Prioritized pull consumer policy:** In addition to the consumer policies like overflow or client pinning, a new `prioritized` policy has been added. In contrast with the overflow policy, this allows a consumer to receive messages sooner instead of delaying failover, but at the cost of potentially flip-flopping work between clients. More information is available in [ADR-42](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-42.md#prioritized-policy)

### Operations

* **Server metadata:** Similar to `server_tags` which contains a set of tags describing the server, `server_metadata` is a map containing string keys and values describing metadata of the server.
* **Promoting mirrors:** A stream that’s mirroring can now be promoted to be the primary, enabling new disaster recovery methodology. The current primary stream should be deleted or have its configured subjects removed prior to promoting mirrors, before configuring the promoted mirrors to start listening on those subjects.
* **Exponential backoff on route and gateway connections:** Cluster routes and gateways can now use exponential backoff on reconnection attempts by setting `connect_backoff`. If `true`, will start exponential backoff at 1 second up to 30 seconds. This can slow down the speed of reconnection but significantly reduces the amount of DNS queries and general connection attempts during server restarts or outages.
* **Offline assets:** When downgrading to an older version, the server can now recognize new features were used and puts the stream and/or consumer into an unsupported/offline mode. For more information, read also the downgrade considerations. More information is available in [ADR-44](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-44.md#offline-assets)
* **Stream/consumer scaleup and reset disk/state protection:** The server now has better protections against leader elections based on empty state. This also improves reliability of replicated in-memory streams. Usually a quorum of servers needs to be online and contain data. Now all but one server can be restarted and the in-memory stream’s data can reliably be caught back up. However, during such a scenario all servers involved with replication of that stream will need to be available, not just what’s needed for quorum. This lets the servers decide the best course of action to preserve all data.

## Improvements

* **Async stream flushing:** Replicated streams will now asynchronously flush data to the underlying store on disk, resulting in a significant improvement in performance. Writes to a replicated stream are still persisted synchronously in the Raft log prior to committing them, so the improved performance has no downsides with respect to consistency.
* **Elastic pointers in the filestore:** File-based streams now use elastic pointers for its write-through caches. This allows the server to better respond during garbage collection, these caches can be evicted early to avoid out-of-memory conditions (see upgrade considerations below).
* **Use cipher suites from `crypto/tls`:** New cipher suites are now automatically added. Additionally, insecure cipher suites are disabled by default, but can be allowed when enabling `allow_insecure_cipher_suites`.
* **System events for the `$G` account:** The global account (`$G`) will now also produce system events, such as connect and disconnect events.
* **`GOMAXPROCS` and `GOMEMLIMIT` in server stats:** The server stats already contained the CPU and memory usage of the server but now also contains the effective Go limits.
* **New subject transforms: `partition(n)` and `random(n)`:** In addition to `partition(n, …)` which allows to determine a partition number based on tokens at specified indices, `partition(n)` and `random(n)` are convenience functions to create a partition or random number up to `n` based on the whole subject.
* **Account name and user logging:** Any logging related to a client connection, for example when reaching maximum connections or for authentication errors, will now include the account name and user of that client connection.
* **Logging improvements:** Any logging related to a client connection now includes the account and user name. Connection closed logging now includes the remote server name.
* **Isolated leaf node property:** In a large deployment with lots of leaf nodes, propagating east-west interest can result in a lot of traffic, which is wasted if leaf nodes don't need to be able to publish/subscribe to each other directly. Instead of the workaround of setting the cluster name of those leaf nodes to be the same, the `isolate_leafnode_interest` property can now be used.
* **Disable leaf node connection through config reload:** This allows disabling a remote leaf node using configuration reload, when using `disabled: true`. If changed from false to true, a solicited leaf node will be disconnected and will not reconnect. If changed from true to false, the leafnode will be solicited again.

## Upgrade Considerations

#### Memory usage

With the new elastic pointers in the filestore, it is expected that a NATS Server running 2.12 may show a different memory usage pattern to before. In some systems this may result in lower resident set size (RSS) reported, in others it may result in higher, depending on the number of assets and publish/access patterns.

For the first time, the server will be able to respond to memory pressure by freeing filestore caches on demand and returning the memory to the operating system. This reduces the chance that sudden spikes in utilisation will result in an out-of-memory (OOM) kill. However, this means that the server can more optimistically retain caches in memory when available resources allow in order to facilitate improved read access times.

This behaviour is largely controlled by the GC thresholds as set by the `GOMEMLIMIT` [environment variable](https://tip.golang.org/doc/gc-guide#Memory_limit). You may wish to tune this value in your environment based on available system memory, or in the case of Kubernetes environments, memory reservations.

#### Strict JetStream API

Starting from version v2.11, the server would start logging the following statement if an invalid JetStream request was received:

```
[WRN] Invalid JetStream request '$G > $JS.API.STREAM.CREATE.test-stream': json: unknown field "unknown"  
```

Starting from version v2.12, the server will not only log, but also return an error to the client as “strict mode” is now enabled by default. This means invalid JetStream requests will be rejected by default.

If the above log message is observed, please make sure that the application or client is sending correct requests to the server and that NATS client libraries are up-to-date. Strict mode can be temporarily disabled in the server configuration, allowing you more time to fix the issue:

```
jetstream {  
  strict: false  
}  
```

## Downgrade Considerations

#### Stream state

When downgrading from v2.12 to v2.11, the stream state files on disk will be rebuilt due to a change in the format of these files in v2.12. This requires re-scanning all stream message blocks, which may use higher CPU than usual and will likely take longer for the restarted node to report healthy. This will only happen on the first restart after downgrading and will not result in data loss.

When downgrading, only downgrade to v2.11.9 or higher. Starting from this version, the server will recognize the use of new v2.12 features and will safely put the stream and/or consumer that uses these new features into an unsupported/offline mode. Importantly, this will both protect the data as well as the server itself from accessing unsupported features or data.


# NATS 2.11

This guide is tailored for existing NATS users upgrading from NATS version v2.10.x. This will read as a summary with links to specific documentation pages to learn more about the feature or improvement.

## Features

### Observability

* **Distributed message tracing:** Users can now trace messages as they move through the system by setting a `Nats-Trace-Dest` header to an inbox subject. Servers on the message path will return events to the provided subject that report each time a message enters or leaves a server, by which connection type, when subject mappings occur, or when messages traverse an account import/export boundary. Additionally, the `Nats-Trace-Only` header (if set to true) will allow tracing events to propagate on a specific subject without delivering them to subscribers of that subject.

### Streams

* **JetStream per-message TTLs:** It is now possible to age out individual messages using a per-message TTL. The `Nats-TTL` header, in either string or integer format (in seconds) allows for individual message expiration independent of stream limits. This can be combined with other limits in place on the stream. More information is available in [ADR-43](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-43.md).
* **Subject delete markers on MaxAge:** The `SubjectDeleteMarkerTTL` stream configuration option now allows for the placement of delete marker messages in the stream when the configured `MaxAge` limit causes the last message for a given subject to be deleted. The delete markers include a `Nats-Marker-Reason` header explaining which limit was responsible for the deletion.
* **Stream ingest rate limiting:** New options `max_buffered_size` and `max_buffered_msgs` in the `jetstream` configuration block enable rate limiting on Core NATS publishing into JetStream streams, protecting the system from overload.

### Consumers

* **Pull consumer priority groups:** Pull consumers now support priority groups with pinning and overflow, enabling flexible failover and priority management when multiple clients are pulling from the same consumer. Configurable policies based on the number of pending messages on the consumer, or the number of pending acks, can control when messages overflow from one client to another, enabling new design patterns or regional awareness.
* **Consumer pausing:** Message delivery to consumers can be temporarily suspended using the new pause API endpoint (or the `PauseUntil` configuration option when creating), ideal for maintenance or migrations. Message delivery automatically resumes once the configured deadline has passed. Consumer clients continue to receive heartbeat messages as usual to ensure that they do not surface errors during the pause.

### Operations

* **Replication traffic in asset accounts:** Raft replication traffic can optionally be moved into the same account in which replicated assets live on a per-account basis, rather than being sent and received in the system account using the new [`cluster_traffic` property ](https://docs.nats.io/running-a-nats-service/configuration#jetstream-account-settings)in the JetStream account settings of an account. When combined with multiple route connections, this can help to reduce latencies and avoid head-of-line blocking issues that may occur in heavily-loaded multi-tenant or multi-account deployments.
* **TLS first on leafnode connections:** A new `handshake_first` in the leafnode `tls` block allows setting up leafnode connections that perform TLS negotiation first, before any other protocol handshakes take place.
* **Configuration state digest:** A new `-t` command line flag on the server binary can generate a hash of the configuration file. The `config_digest` item in `varz` displays the hash of the currently running configuration file, making it possible to check whether a configuration file has changed on disk compared to the currently running configuration.
* **TPM encryption on Windows:** When running on Windows, the filestore can now store encryption keys in the TPM, useful in environments where physical access may be a concern.

### MQTT

* **SparkplugB:** The built-in MQTT support is now compliant with SparkplugB Aware, with support for `NBIRTH` and `NDEATH` messages.

## Improvements

* **Replicated delete proposals:** Message removals in clustered interest-based or workqueue streams are now propagated via Raft to guarantee consistent removal order across replicas, reducing a number of possible ways that a cluster failure can result in de-synced streams.
* **Metalayer, stream and consumer consistency:** A new leader now only responds to read/write requests after synchronizing with its Raft log, preventing desynchronization between KV key updates and the stream during leader changes.
* **Replicated consumer reliability:** Replicated consumers now consistently redeliver unacknowledged messages after a leader change.
* **Consumer starting sequence:** The consumer starting sequence is now always respected, except for internal hidden consumers for sources/mirrors.

## Upgrade Considerations

#### Stream ingest rate limiting

The NATS Server can now return a 429 error with type `JSStreamTooManyRequests` when too many messages have been queued up for a stream. It should not generally be possible to hit this limit while using JetStream publishes and waiting for PubAcks, but may trigger if trying to publish into JetStream using Core NATS publishes without waiting for PubAcks, which is not advised.

The new `max_buffered_size` and `max_buffered_msgs` options control how many messages can be queued for each stream before the rate limit is hit, therefore if needed, you can increase these limits on your deployments. The default values for `max_buffered_size` and `max_buffered_msgs` are 128MB and 10,000 respectively, whereas in v2.10 these were unlimited.

You can detect in the server logs whether running into a queue limit with the following warning:

```
[WRN] Dropping messages due to excessive stream ingest rate on 'account' > 'my-stream': IPQ len limit reached
```

If your application starts to log the above warnings then you can first try to increase the limits to higher values while investigating the fast publishers, for example:

```
jetstream {
  max_buffered_msgs: 50000
  max_buffered_size: 256mib
}
```

#### Replicated delete proposals

Since stream deletes are now replicated through group proposals in a replicated stream, there may be a slight increase in replication traffic on this version.

#### JetStream healthcheck

The `js-server-only` healthcheck no longer checks for the health of the metaleader on v2.11.0. Since this healthcheck was designed to detect the server readiness (or in k8s for the readiness probe) checking the metaleader would sometimes cause a NATS server to be considered unhealthy when restarting the servers. In v2.11, this should no longer be an issue. If the previous behavior from v2.10 is preferred, there is a new healthcheck option `js-meta-only` which can be used to check whether the meta group is healthy.

#### Exit code

Earlier versions of the NATS Server would return an exit code 1 when gracefully shut down, i.e. after SIGTERM. From v2.11, an exit code of 0 (zero) will now be returned instead.

#### Server, cluster and gateway names

Configurations that have server, cluster, and gateway names with spaces are now considered invalid, as this can cause problems at the protocol level. A server running NATS v2.11 will fail to start with spaces configured in these names. Please ensure that spaces are not used in server, cluster or gateway names.

## Downgrade Considerations

#### Stream state

When downgrading from v2.11 to v2.10, the stream state files on disk will be rebuilt due to a change in the format of these files in v2.11. This requires re-scanning all stream message blocks, which may use higher CPU than usual and will likely take longer for the restarted node to report healthy. This will only happen on the first restart after downgrading and will not result in data loss.


# NATS 2.10

This guide is tailored for existing NATS users upgrading from NATS version 2.9.x. This will read as a summary with links to specific documentation pages to learn more about the feature or improvement.

## Upgrade considerations

### Client versions

Although all existing client versions will work, new client versions will expose additional options used to leverage new features. The minimum client versions that have full 2.10.0 support include:

* CLI - [v0.1.0](https://github.com/nats-io/natscli/releases/tag/v0.1.0)
* nats.go - [v1.30.0](https://github.com/nats-io/nats.go/releases/tag/v1.30.0)
* nats.rs - [v0.32.0](https://github.com/nats-io/nats.rs/releases/tag/async-nats%2Fv0.32.0)
* nats.deno - [v1.17.0](https://github.com/nats-io/nats.deno/releases/tag/v1.17.0)
* nats.js - [v2.17.0](https://github.com/nats-io/nats.js/releases/tag/v2.17.0)
* nats.ws - [v1.18.0](https://github.com/nats-io/nats.ws/releases/tag/v1.18.0)
* nats.java - [v2.17.0](https://github.com/nats-io/nats.java/releases/tag/2.17.0)
* nats.net - [v1.1.0](https://github.com/nats-io/nats.net/releases/tag/1.1.0)
* nats.net.v2 - Coming soon!
* nats.py - Coming soon!
* nats.c - Coming soon!

### Helm charts

* k8s/nats - [v1.1.0](https://github.com/nats-io/k8s/releases/tag/nats-1.1.0)
* k8s/nack - [v0.24.0](https://github.com/nats-io/k8s/releases/tag/nack-0.24.0)

### Downgrade warnings

For critical infrastructure like NATS, zero downtime upgrades are table stakes. Although the best practice for all infrastructure like this is for users to thoroughly test a new release against your specific workloads, inevitably there are cases where an upgrade occurs in production followed by a decision to downgrade. This is never recommended and can cause more harm than good for most infrastructure and data systems.

Below are a few important considerations if downgrading is required.

#### Storage format changes

2.10.0 brings on-disk storage changes which bring significant performance improvements. These are not compatible with previous versions of the NATS Server. If an upgrade is performed to a server with existing stream data on disk, followed by a downgrade, the older version server will not understand the stream data in the new format.

However, being mindful of the possibility of the need to downgrade, a special version of the 2.9.x series was released with awareness of key changes in the new storage format, allowing it to startup properly.

The takeaway is that if a downgrade is the only resort, it must be to 2.9.22 or later to ensure storage format changes are handled appropriately.

#### Stream and consumer config options

There are new stream and consumer configuration options that could be problematic if a downgrade occurs since previous versions of the server have no awareness of them. Examples include:

* Multi-filter consumers - Downgrading would result in no filter being applied since the new field is configured as a list rather than a single string.
* Subject-transform on streams - Downgrading would result in the subject transform not being applied since the server has no awareness of it.
* Compression on streams - Downgrading when compression is enabled on streams will cause those streams to become unloadable since the older server versions will not understand the compression being used.

## Features

### Platforms

* Experimental support for [IBM z/OS](https://docs.nats.io/running-a-nats-service/introduction/installation#supported-operating-systems-and-architectures)
* Experimental support for [NetBSD](https://docs.nats.io/running-a-nats-service/introduction/installation#supported-operating-systems-and-architectures)

### Reload

* A server reload can now be performed by sending a message on [`$SYS.REQ.SERVER.<server-id>.RELOAD`](https://docs.nats.io/running-a-nats-service/configuration#configuration-reloading) by a client authenticated in the system account.

### JetStream

* A new [`sync_interval` server config option](https://docs.nats.io/running-a-nats-service/configuration#jetstream) has been added to change the default sync interval of stream data when written to disk, including allowing all writes to be flushed immediately. This option is only relevant if you need to modify durability guarantees.

### Subject mapping

* Subject mappings can now be [cluster-scoped](https://docs.nats.io/nats-concepts/subject_mapping#cluster-scoped-mappings) and weighted, enabling the ability to have different mappings or weights on a per cluster basis.
* The requirement to use all wildcard tokens in subject mapping or transforms has been relaxed. This can be applied to config or account-based subject mapping, stream subject transforms, and stream republishing, but not on subject mappings that are associated with stream and service import/export between accounts.

### Streams

* A [`subject_transform` field](https://docs.nats.io/nats-concepts/jetstream/streams#subjecttransforms) has been added enabling per-stream subject transforms. This applies to standard streams, mirrors, and sourced streams.
* A [`metadata` field](https://docs.nats.io/nats-concepts/jetstream/streams#configuration) has been added to stream configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.
* A [`first_seq` field](https://docs.nats.io/nats-concepts/jetstream/streams#configuration) has been added to stream configuration enabling explicitly setting the initial sequence on stream creation.
* A [`compression` field](https://docs.nats.io/nats-concepts/jetstream/streams#configuration) has been added to stream configuration enabling on-disk compression for file-based streams.
* The ability to edit the [`republish` config option](https://docs.nats.io/nats-concepts/jetstream/streams#republish) on a stream after stream creation was added.
* A [`Nats-Time-Stamp` header](https://docs.nats.io/nats-concepts/jetstream/headers#republish) is now included in republished messages containing the original message's timestamp.
* A `ts` field has been added to stream info responses indicating the server time of the snapshot. This was added to allow for local time calculations relying on the local clock.
* An array of subject-transforms (subject filter + subject transform destination) can be added to a mirror or source configuration (can not use the single subject filter/subject transform destination fields at the same time as the array).
* A stream configured with `sources` can source from the same stream multiple times when distinct filter+transform options are used, allowing for some messages of a stream to be sourced more than once.

### Consumers

* A [`filter_subjects` field](https://docs.nats.io/nats-concepts/jetstream/consumers#filtersubjects) has been added which enables applying server-side filtering against multiple disjoint subjects, rather than only one.
* A [`metadata` field](https://docs.nats.io/nats-concepts/jetstream/consumers#configuration) has been added to consumer configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.
* A `ts` field has been added to consumer info responses indicating the server time of the snapshot. This was added to allow for local time calculations without relying on the local clock.

### Key-value

* A [`metadata` field](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/key-value-store.md#configuration) has been added to key-value configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.
* A bucket configured as a mirror or sourcing from other buckets

### Object store

* A [`metadata` field](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/object-store.md#configuration) has been added to object store configuration enabling arbitrary user-defined key-value data. This is to supplant or augment the `description` field.

### Authn/Authz

* A pluggable server extension, referred to as [auth callout](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout), has been added. This provides a mechanism for delegating authentication checks against a bring-your-own (BYO) provider and, optionally, dynamically declaring permissions for the authenticated user.

### Monitoring

* A `unique_tag` field has been added to the [`/varz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#general-information) and [`/jsz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#jetstream-information) HTTP endpoint responses, corresponding to the value of `unique_tag` defined in the server config.
* A `slow_consumer_stats` field has been added to the [`/varz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#general-information) HTTP endpoint providing a count of slow consumers for clients, routes, gateways, and leafnodes.
* A `raft=1` query parameter has been added to the [`/jsz`](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#jetstream-information) HTTP endpoint which adds `stream_raft_group` and `consumer_raft_groups` fields to the response.
* A `num_subscriptions` field has been added to the [`$SYS.REQ.SERVER.PING.STATZ`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.server.less-than-id-greater-than.statsz-requesting-server-stats-summary) NATS endpoint responses.
* A system account responder for [`$SYS.REQ.SERVER.PING.IDZ`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.server.ping.idz-discovering-servers) has been added which returns info for the server that the client is connected to.
* A system account responder for [`$SYS.REQ.SERVER.PING.PROFILEZ`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.server.less-than-id-greater-than.profilez-request-profiling-information) has been added and works even if a profiling port is not enabled in the server configuration.
* A user account responder for [`$SYS.REQ.USER.INFO`](https://docs.nats.io/running-a-nats-service/configuration/sys_accounts/sys_accounts#usdsys.req.user.info-request-connected-user-information) has been added which allows a connected user to query for the account they are in and permissions they have.

### MQTT

* Support for [QoS2](https://docs.nats.io/running-a-nats-service/configuration/mqtt) has been added. Check out the new [MQTT implementation details](https://github.com/nats-io/nats-server/blob/main/server/README-MQTT.md) overview.

### Clustering

* When defining routes between servers, a handful of optimizations have been introduced including a pool of TCP connections between servers, optional pinning of accounts to connections, and optional compression of traffic. There is quite a bit to dig into, so check out the [v2 routes](https://docs.nats.io/running-a-nats-service/configuration/clustering/v2_routes) page for details.

### Leafnodes

* A [`handshake_first` config option](https://docs.nats.io/running-a-nats-service/configuration/leafnodes#tls-first-handshake) has been added enabling TLS-first handshakes for leafnode connections.

### Windows

* The [`NATS_STARTUP_DELAY` environment variable](https://docs.nats.io/running-a-nats-service/introduction/windows_srv#nats_startup_delay-environment-variable) has been added to allow changing the default startup for the server of 10 seconds

## Improvements

### Reload

* The [`nats-server --signal` command](https://docs.nats.io/running-a-nats-service/nats_admin/signals#multiple-processes) now supports a glob expression on the `<pid>` argument which would match a subset of all `nats-server` instances running on the host.

### Streams

* Prior to 2.10, setting [`republish` configuration](https://docs.nats.io/nats-concepts/jetstream/streams#republish) on mirrors would result in an error. On sourcing streams, only messages that were actively between stored matching configured `subjects` would be republished. The behavior has been relaxed to allow republishing on mirrors and includes all messages on sourcing streams.

### Consumers

* A new header has been added on a fetch response that indicates to clients the fetch has been fulfilled without requiring clients to rely on heartbeats. It avoids some conditions in which the client would issue fetch requests that could go over limits or have more fetch requests pending than required.

### Leafnodes

* Previously, a leafnode configured with two or more remotes binding to the same hub account would be rejected. This restriction has been relaxed since each remote could be binding to a different local account.

### MQTT

* Previously a dot `.` in an MQTT topic was not supported, however now it is! Check out the [topic-subject conversion table](https://docs.nats.io/running-a-nats-service/configuration/mqtt) for details.


# NATS 2.2

NATS 2.2 is the largest feature release since version 2.0. The 2.2 release provides highly scalable, highly performant, secure and easy-to-use next generation streaming in the form of JetStream, allows remote access via websockets, has simplified NATS account management, native MQTT support, and further enables NATS toward our goal of securely democratizing streams and services for the hyperconnected world we live in.

## Next Generation Streaming

JetStream is the next generation streaming platform for NATS, highly resilient, highly available, and easy to use. We’ve spent a long time listening to our community, learning from our experiences, looking at the needs of today, and thinking deeply about the needs of tomorrow. We built JetStream to address these needs.

JetStream:

* is easy to deploy and manage, built into the NATS server
* simplifies and accelerates development
* supports wildcard subjects
* supports at least once delivery and exactly once within a window
* is horizontally scalable at runtime with no interruptions
* persists data via streams and delivers or replays via consumers
* supports multiple patterns to consume data on the same stream
* supports push and pull modes when consuming messages
* is account aware
* allows for detailed granularity of security, by stream, by consumer, by function

Get started with [JetStream](https://docs.nats.io/nats-concepts/jetstream).

## Security and Simplified Account Management

Account management just became much easier. This version of NATS has a built-in account management system, eliminating the need to set up an account manager when not using the memory account resolver. With automated default system account generation, and the ability to preload accounts, simply enable a set of servers in your deployment to be account resolvers or account resolver caches, and they will handle public account information provided to the NATS system through the NATS nsc tooling. Have enterprise-scale account management up and running in minutes.

### CIDR Block Account Restrictions

By specifying a CIDR block restriction for a user, policy can be applied to limit connections from clients within a certain range or set of IP addresses. Use this as another layer of security atop user credentials to better secure your distributed system. Ensure your applications can only connect from within a specific cloud, enterprise, geographic location, virtual or physical network.

### Time-Based Account Restrictions

Scoped to the user, you can now [specify a specific block of time](https://docs.nats.io/using-nats/nats-tools/nsc/basics#user-authorization) during the day when applications can connect. For example, permit certain users or applications to access the system during specified business hours, or protect business operations during the busiest parts of the day from batch driven back-office applications that could adversely impact the system when run at the wrong time.

### Default User Permissions

Now you can specify [default user permissions](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization#examples) within an account. This significantly reduces efforts around policy, reduces chances for error in permissioning, and simplifies the provisioning of user credentials.

## WebSockets

Connect mobile and web applications to any NATS server using [WebSockets](https://docs.nats.io/running-a-nats-service/configuration/websocket). Built to more easily traverse firewalls and load balancers, NATS WebSocket support provides even more flexibility to NATS deployments and makes it easier to communicate to the edge and endpoints. This is currently supported in NATS server leaf nodes, nats.ts, nats.deno, and the nats.js clients.

## Native MQTT Support

With the [Adaptive Edge architecture](https://nats.io/blog/synadia-adaptive-edge/) and the ease with which NATS can extend a cloud deployment to the edge, it makes perfect sense to leverage existing investments in IoT deployments. It’s expensive to update devices and large edge deployments. Our goal is to enable the hyperconnected world, so we added first-class support for [MQTT 3.1.1](https://docs.nats.io/running-a-nats-service/configuration/mqtt) directly into the NATS Server.

Seamlessly integrate existing IoT deployments using MQTT 3.1.1 with a cloud-native NATS deployment. Add a leaf node that is MQTT enabled and instantly send and receive messages to your MQTT applications and devices from a NATS deployment whether it be edge, single-cloud, multi-cloud, on-premise, or any combination thereof.

## Build Better Systems

We’ve added a variety of features to allow you to build a more resilient, secure, and simply better system at scale.

### Message Headers

We’ve added the ability to optionally use headers, following the HTTP semantics familiar to developers. Headers naturally apply overhead, which was why we resisted adding them for so long. By creating new internal protocol messages transparent to developers, we maintain the extremely fast processing of simple NATS messages that we have always had while supporting headers for those who would like to leverage them. Adding headers to messages allows you to provide application-specific metadata, such as compression or encryption-related information, without touching the payload. We also provide some NATS specific headers for use in JetStream and other features.

### Seamless Maintenance with Lame Duck Notifications

When taking down a server for maintenance, servers can be signaled to enter [Lame Duck Mode](https://docs.nats.io/running-a-nats-service/nats_admin/lame_duck_mode) where they do not accept new connections and evict existing connections over a period of time. Maintainer supported clients will notify applications that a server has entered this state and will be shutting down, allowing a client to smoothly transition to another server or cluster and better maintain business continuity during scheduled maintenance periods.

### React Quicker with No-Responder Notifications

Why wait for timeouts when services aren’t available? When a request is made to a service (request-reply) and the NATS Server knows there are no services available the server will short circuit the request. A “no-responders” protocol message will be sent back to the requesting client which will break from blocking API calls. This allows applications to immediately react which further enables building a highly responsive system at scale, even in the face of application failures and network partitions.

### Subject Mapping and Traffic Shaping

Reduce risk when onboarding new services. Canary deployments, A/B testing, and transparent teeing of data streams are now fully supported in NATS. The NATS Server allows accounts to form subject mappings from one subject to another for both client inbound and service import invocations and allows weighted sets for the destinations. Map any percentage - 1 to 100 percent of your traffic - to other subjects, and change this at runtime with a server configuration reload. You can even artificially drop a percentage of traffic to introduce chaos testing into your system. See [Configuring Subject Mapping and Traffic Shaping](https://docs.nats.io/running-a-nats-service/configuration/configuring_subject_mapping) in NATS Server configuration for more details.

### Account Monitoring - More Meaningful Metrics

NATS now allows for [fine-grained monitoring](https://docs.nats.io/running-a-nats-service/nats_admin/monitoring#monitoring-nats) to identify usage metrics tied to a particular account. Inspect messages and bytes sent or received and various connection statistics for a particular account. Accounts can represent anything - a group of applications, a team or organization, a geographic location, or even roles. If NATS is enabling your SaaS solution you could use NATS account scoped metrics to bill users.


# NATS 2.0

NATS 2.0 was the largest feature release since the original code base for the server was released. NATS 2.0 was created to allow a new way of thinking about NATS as a shared utility, solving problems at scale through distributed security, multi-tenancy, larger networks, and secure sharing of data.

## Rationale

NATS 2.0 was created to address problems in large scale distributed computing.

It is difficult at best to combine identity management end-to-end (or end-to-edge), with data sharing, while adhering to policy and compliance. Current distributed systems increase significantly in operational complexity as they scale upward. Problems arise around service discovery, connectivity, scaling for volume, and application onboarding and updates. Disaster recovery is difficult, especially as systems have evolved to operate in silos defined by technology rather than business needs. As complexity increases, systems become expensive to operate in terms of time and money. They become fragile making it difficult to deploy services and applications hindering innovation, increasing time to value and total cost of ownership.

We decided to:

* **Reduce total cost of ownership**: Users want reduced TCO for their

  distributed systems. This is addressed by an easy to use technology that

  can operate at global scale with simple configuration and a resilient

  and cloud-native architecture.
* **Decrease Time to Value**: As systems scale, *time to value* increases.

  Operations resist change due to risk in touching a complex and fragile

  system. Providing isolation contexts can help mitigate this.
* **Support manageable large scale deployments**: No data silos defined by

  software, instead easily managed through software to provide exactly what the

  business needs. We wanted to provide easy to configure disaster recovery.
* **Decentralize security**: Provide security supporting one

  technology end-to-end where organizations may self-manage making it

  easier to support a massive number of endpoints.

To achieve this, we added a number of new features that are transparent to existing clients with 100% backward client compatibility.

## Accounts

Accounts are securely isolated communication contexts that allow multi-tenancy spanning a NATS deployment. Accounts allow users to bifurcate technology from business driven use cases, where data silos are created by design, not software limitations. When a client connects, it specifies an account or will default to authentication with a global account.

At least some services need to share data outside of their account. Data can be securely shared between accounts with secure services and streams. Only mutual agreement between account owners permit data flow, and the import account has complete control over its own subject space.

This means within an account, limitations may be set and subjects can be used without worry of collisions with other groups or organizations. Development groups choose any subjects without affecting the rest of the system, and open up accounts to export or import only the services and streams they need.

Accounts are easy, secure, and cost effective. There is one NATS deployment to manage, but organizations and development teams can self manage with more autonomy reducing time to value with faster, more agile development practices.

### Service and Streams

Services and streams are mechanisms to share messages between accounts.

Think of a service as an RPC endpoint into an account. Behind that account there might be many microservices working in concert to handle requests, but from outside the account there is simply one subject exposed.

**Service** definitions share an endpoint:

* Export a service to allow other accounts to import
* Import a service to allow requests to be sent securely and seamlessly to another account

Use cases include most applications - anything that accepts a request and returns a response.

**Stream** definitions allow continuous data flow between accounts:

* Export a stream to allow egress
* Import a stream to allow ingress

Use cases include Observability, Metrics, and Data analytics. Any application or endpoint reading a stream of data.

Note that services and streams operate with **zero** client configuration or API changes. Services may even move between accounts, entirely transparent to end clients.

### System Accounts

The system account publishes system messages under established subject patterns. These are internal NATS system messages that may be useful to operators.

Server initiated events and data include:

* Client connection events
* Account connection status
* Authentication errors
* Leaf node connection events
* Server stats summary

Tools and clients with proper privileges can request:

* Service statistics
* Server discovery and metrics

Account servers will also publish messages when an account changes.

With this information and system metadata you can build useful monitoring and anomaly detection tools.

## Global Deployments

NATS 2.0 supports global deployments, allowing for global topologies that optimize for WANs while extend to the edge or devices.

### Self Healing

While self healing features have been part of NATS 1.X releases, we ensured they continue to work in global deployments. These include:

* Client and server connections automatically reconnect
* Auto-Discovery where servers exchange server topology changes with each

  other and with clients, in real time with zero configuration changes and

  zero downtime while being entirely transparent to clients. Clients can

  failover to servers they were not originally configured with.
* NATS server clusters dynamically adjust to new or removed servers allowing

  for seamless rolling upgrades and scaling up or down.

### Superclusters

Conceptually, superclusters are clusters of NATS clusters. Create superclusters to deploy a truly global NATS network. Superclusters use a novel spline based technology with a unique approach to topology, keeping one hop semantics and optimizing WAN traffic through optimistic sends with interest graph pruning. Superclusters provide transparent, intelligent support for geo-distributed queue subscribers.

### Disaster Recovery

Superclusters inherently support disaster recovery. With geo-distributed queue subscribers, local clients are preferred, then an RTT is used to find the lowest latency NATS cluster containing a matching queue subscriber in the supercluster.

What does this mean?

Let's say you have a set of load balanced services in US East Coast (US-EAST), another set in the EU (EU-WEST), and a supercluster consisting of a NATS cluster in US-EAST connected to a NATS cluster in EU-WEST. Clients in the US would connect to a US-EAST, and services connected to that cluster would service those clients. Clients in Europe would automatically use services connected to EU-WEST. If the services in US-EAST disconnect, clients in US-EAST will begin using services in EU-WEST.

Once the Eastern US services have reconnected to US-EAST, those services will immediately begin servicing the Eastern US clients since they're local to the NATS cluster. This is automatic and entirely transparent to the client. There is no extra configuration in NATS servers.

This is **zero configuration disaster recovery**.

### Leaf Nodes

Leaf nodes are NATS servers running in a special configuration, allowing hub and spoke topologies to extend superclusters.

Leaf nodes can also bridge separate security domains. e.g. IoT, mobile, web. They are ideal for edge computing, IoT hubs, or data centers that need to be connected to a global NATS deployment. Local applications that communicate using the loopback interface with physical VM or Container security can leverage leaf nodes as well.

Leaf nodes:

* Transparently and securely bind to a remote NATS account
* Securely bridge specific local data to a wider NATS deployment
* Are 100% transparent to clients which remain simple, lightweight, and easy to develop
* Allow for a local security scheme while using new NATS security features globally
* Can create a DMZ between a local NATS deployment and external NATS cluster or supercluster.

## Decentralized Security

### Operators, Accounts, and Users

NATS 2.0 Security consists of defining Operators, Accounts, and Users within a NATS deployment.

* An **Operator** provides the root of trust for the system, may represent

  a company or enterprise

  * Creates **Accounts** for account administrators. An account represents

    an organization, business unit, or service offering with a secure context

    within the NATS deployment, for example an IT system monitoring group, a

    set of microservices, or a regional IoT deployment. Account creation

    would likely be managed by a central group.
* **Accounts** define limits and may securely expose services and streams.
  * Account managers create **Users** with permissions
* **Users** have specific credentials and permissions.

### Trust Chain

PKI (NKeys encoded [Ed25519](https://ed25519.cr.yp.to/)) and signed JWTs create a hierarchy of Operators, Accounts, and Users creating a scalable and flexible distributed security mechanism.

* **Operators** are represented by a self signed JWT and is the only thing that

  is required to be configured in the server. This JWT is usually signed by a

  master key that is kept offline. The JWT will contain valid signing keys that

  can be revoked with the master updating this JWT.

  * Operators will sign **Account** JWTs with various signing keys.
  * **Accounts** sign **User** JWTs, again with various signing keys.
* Clients or leaf nodes present **User** credentials and a signed nonce when connecting.
  * The server uses resolvers to obtain JWTs and verify the client trust chain.

This allows for rapid change of permissions, authentication and limits, to a secure multi-tenant NATS system.


# Overview

**What is NATS?**\
NATS is a connective technology that powers modern distributed systems. A connective technology is responsible for addressing, discovery and exchanging of messages that drive the common patterns in distributed systems; asking and answering questions, aka services/microservices, and making and processing statements, or stream processing.

**Challenges faced by modern distributed systems**\
Modern distributed systems are defined by an ever increasing number of hyper-connected moving parts and the additional data they generate. They employ both services and streams to drive business value. They are also being defined by location independence and mobility, and not just for things we would typically recognize as front end technologies. Today’s systems and the backend processes, microservices and stream processing are being asked to be location independent and mobile as well, all while being secure.

These modern systems present challenges to technologies that have been used to connect mobile front ends to fairly static backends. These incumbent technologies typically manage addressing and discovery via hostname (DNS) or IP and port, utilize a 1:1 communication pattern, and have multiple different security patterns for authentication and authorization. Although not perfect, incumbent technologies have been good enough in many situations, but times are changing quickly. As microservices, functions, and stream processing are being asked to move to the edge, these technologies and the assumptions they make are being challenged.

## What makes the NATS connective technology unique for these modern systems?

**Effortless M:N connectivity:** NATS manages addressing and discovery based on subjects and not hostname and ports. Defaulting to M:N communications, which is a superset of 1:1, meaning it can do 1:1 but can also do so much more. If you have a 1:1 system that is successful in development, ask how many other moving parts are required for production to work around the assumption of 1:1? Things like load balancers, log systems, and network security models, as well as proxies and sidecars. If your production system requires all of these things just to get around the fact that the connective technology being used, e.g. HTTP or gRPC, is 1:1, it’s time to give NATS.io a look.

**Deploy anywhere:** NATS can be deployed nearly anywhere; on bare metal, in a VM, as a container, inside K8S, on a device, or whichever environment you choose. NATS runs well within deployment frameworks or without.

**Secure:** Similarly, NATS is secure by default and makes no requirements on network perimeter security models. When you start considering mobilizing your backend microservices and stream processors, many times the biggest roadblock is security.

### Scalable, Future-Proof Deployments

NATS infrastructure and clients communicate all topology changes in real-time. This means that NATS clients do not need to change when NATS deployments change. Having to change clients with deployments would be like having to reboot your phone every time your cell provider added or changed a cell tower. This sounds ridiculous of course, but think about how many systems today have their front ends tied so closely to the backend, that any change requires a complete front end reboot or at least a reconfiguration. NATS clients and applications need no such change when backend servers are added and removed and changed. Even DNS is only used to bootstrap first contact, after that, NATS handles endpoint locations transparently.

### Hybrid Deployments

Another advantage to utilizing a NATS is that it allows a hybrid mix of SaaS/Utility computing with separately owned and operated systems. Meaning you can have a shared NATS service with core microservices, streams and stream processing be extended by groups or individuals who have a need to run their own NATS infrastructure. You are not forced to choose one or the other.

### Adaptability

Today’s systems will fall short with new demands. As modern systems continue to evolve and utilize more components and process more data, supporting patterns beyond 1:1 communications, with addressing and discovery tied to DNS is critical. Foundational technologies like NATS promise the most return on investment. Incumbent technologies will not work as modern systems unify cloud, Edge, IoT and beyond. NATS does.

### Use Cases

NATS can run anywhere, from large servers and cloud instances, through edge gateways and even IoT devices. Use cases for NATS include:

* Cloud Messaging
  * Services (microservices, service mesh)
  * Event/Data Streaming (observability, analytics, ML/AI)
* Command and Control
  * IoT and Edge
  * Telemetry / Sensor Data / Command and Control
* Augmenting or Replacing Legacy Messaging Systems


# Compare NATS

NATS Comparison to Kafka, Rabbit, gRPC, and others

This feature comparison is a summary of a few of the major components in several of the popular messaging technologies of today. This is by no means an exhaustive list and each technology should be investigated thoroughly to decide which will work best for your implementation.

In this comparison, we will be featuring NATS, Apache Kafka, RabbitMQ, Apache Pulsar, and gRPC.

## Language and Platform Coverage

| Project    | Client Languages and Platforms                                                                                                                                                                                                                                                                  |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | Core NATS: 48 known client types, 11 supported by maintainers, 18 contributed by the community. NATS Streaming: 7 client types supported by maintainers, 4 contributed by the community. NATS servers can be compiled on architectures supported by Golang. NATS provides binary distributions. |
| **gRPC**   | 13 client languages.                                                                                                                                                                                                                                                                            |
| **Kafka**  | 18 client types supported across the community and by Confluent. Kafka servers can run on platforms supporting java; very wide support.                                                                                                                                                         |
| **Pulsar** | 7 client languages, 5 third-party clients - tested on macOS and Linux.                                                                                                                                                                                                                          |
| **Rabbit** | At least 10 client platforms that are maintainer-supported with over 50 community supported client types. Servers are supported on the following platforms: Linux, Windows NT.                                                                                                                  |

## Built-in Patterns

| Project    | Supported Patterns                                                                                                                                                                                                                              |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | Streams and Services through built-in publish/subscribe, request-reply, and load-balanced queue subscriber patterns. Dynamic request permissioning and request subject obfuscation is supported.                                                |
| **gRPC**   | One service, which may have streaming semantics, per channel. Load Balancing for a service can be done either client-side or by using a proxy.                                                                                                  |
| **Kafka**  | Streams through publish/subscribe. Load balancing can be achieved with consumer groups. Application code must correlate requests with replies over multiple topics for a service (request-reply) pattern.                                       |
| **Pulsar** | Streams through publish/subscribe. Multiple competing consumer patterns support load balancing. Application code must correlate requests with replies over multiple topics for a service (request-reply) pattern.                               |
| **Rabbit** | Streams through publish/subscribe, and services with a direct reply-to feature. Load balancing can be achieved with a Work Queue. Applications must correlate requests with replies over multiple topics for a service (request-reply) pattern. |

## Delivery Guarantees

| Project    | Quality of Service / Guarantees                                          |
| ---------- | ------------------------------------------------------------------------ |
| **NATS**   | At most once, at least once, and exactly once is available in JetStream. |
| **gRPC**   | At most once.                                                            |
| **Kafka**  | At most once, at least once, and exactly once.                           |
| **Pulsar** | At most once, at least once, and exactly once.                           |
| **Rabbit** | At most once, at least once.                                             |

## Multi-tenancy and Sharing

| Project    | Multi-tenancy Support                                                                                                                                                      |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | NATS supports true multi-tenancy and decentralized security through accounts and defining shared streams and services.                                                     |
| **gRPC**   | N/A                                                                                                                                                                        |
| **Kafka**  | Multi-tenancy is not supported.                                                                                                                                            |
| **Pulsar** | Multi-tenancy is implemented through tenants; built-in data sharing across tenants is not supported. Each tenant can have its own authentication and authorization scheme. |
| **Rabbit** | Multi-tenancy is supported with vhosts; data sharing is not supported.                                                                                                     |

## AuthN

| Project    | Authentication                                                                                                                            |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | NATS supports TLS, NATS credentials, NKEYS (NATS ED25519 keys), username and password, or simple token.                                   |
| **gRPC**   | TLS, ALT, Token, channel and call credentials, and a plug-in mechanism.                                                                   |
| **Kafka**  | Supports Kerberos and TLS. Supports JAAS and an out-of-box authorizer implementation that uses ZooKeeper to store connection and subject. |
| **Pulsar** | TLS Authentication, Athenz, Kerberos, JSON Web Token Authentication.                                                                      |
| **Rabbit** | TLS, SASL, username and password, and pluggable authorization.                                                                            |

## AuthZ

| Project    | Authorization                                                                                                                                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | Account limits including number of connections, message size, number of imports and exports. User-level publish and subscribe permissions, connection restrictions, CIDR address restrictions, and time of day restrictions. |
| **gRPC**   | Users can configure call credentials to authorize fine-grained individual calls on a service.                                                                                                                                |
| **Kafka**  | Supports JAAS, ACLs for a rich set of Kafka resources including topics, clusters, groups, and others.                                                                                                                        |
| **Pulsar** | Permissions may be granted to specific roles for lists of operations such as produce and consume.                                                                                                                            |
| **Rabbit** | ACLs dictate permissions for configure, write, and read operations on resources like exchanges, queues, transactions, and others. Authentication is pluggable.                                                               |

## Message Retention and Persistence

| Project    | Message Retention and Persistence Support                                                                                                                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | Supports memory and file persistence. Messages can be replayed by time, count, or sequence number, and durable subscriptions are supported. With NATS streaming, scripts can archive old log segments to cold storage.                              |
| **gRPC**   | N/A                                                                                                                                                                                                                                                 |
| **Kafka**  | Supports file-based persistence. Messages can be replayed by specifying an offset, and durable subscriptions are supported. Log compaction is supported as well as KSQL.                                                                            |
| **Pulsar** | Supports tiered storage including file, Amazon S3 or Google Cloud Storage (GCS). Pulsar can replay messages from a specific position and supports durable subscriptions. Pulsar SQL and topic compaction is supported, as well as Pulsar functions. |
| **Rabbit** | Supports file-based persistence. Rabbit supported queue-based semantics (vs log), so no message replay is available.                                                                                                                                |

## High Availability and Fault Tolerance

| Project    | HA and FT Support                                                                                                                                                                                                                                                       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | Core NATS supports full mesh clustering with self-healing features to provide high availability to clients. NATS streaming has warm failover backup servers with two modes (FT and full clustering). JetStream supports horizontal scalability with built-in mirroring. |
| **gRPC**   | N/A. gRPC relies on external resources for HA/FT.                                                                                                                                                                                                                       |
| **Kafka**  | Fully replicated cluster members are coordinated via Zookeeper.                                                                                                                                                                                                         |
| **Pulsar** | Pulsar supports clustered brokers with geo-replication.                                                                                                                                                                                                                 |
| **Rabbit** | Clustering Support with full data replication via federation plugins. Clusters require low-latency networks where network partitions are rare.                                                                                                                          |

## Deployment

| Project    | Supported Deployment Models                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | The NATS network element (server) is a small static binary that can be deployed anywhere from large instances in the cloud to resource constrained devices like a Raspberry PI. NATS supports the Adaptive Edge architecture which allows for large, flexible deployments. Single servers, leaf nodes, clusters, and superclusters (cluster of clusters) can be combined in any fashion for an extremely flexible deployment amenable to cloud, on-premise, edge and IoT. Clients are unaware of topology and can connect to any NATS server in a deployment. |
| **gRPC**   | gRPC is point to point and does not have a server or broker to deploy or manage, but always requires additional pieces for production deployments.                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Kafka**  | Kafka supports clustering with mirroring to loosely coupled remote clusters. Clients are tied to partitions defined within clusters. Kafka servers require a JVM, eight cores, 64 GB to128 GB of RAM, two or more 8-TB SAS/SSD disks, and a 10-Gig NIC. [*(1)*](#references)\_\_                                                                                                                                                                                                                                                                              |
| **Pulsar** | Pulsar supports clustering and built-in geo-replication between clusters. Clients may connect to any cluster with an appropriately configured tenant and namespace. Pulsar requires a JVM and requires at least 6 Linux machines or VMs. 3 running ZooKeeper. 3 running a Pulsar broker and a BookKeeper bookie. [*(2)*](#references)\_\_                                                                                                                                                                                                                     |
| **Rabbit** | Rabbit supports clusters and cross-cluster message propagation through a federation plugin. Clients are unaware of topology and may connect to any cluster. The server requires the Erlang VM and dependencies.                                                                                                                                                                                                                                                                                                                                               |

## Monitoring

| Project    | Monitoring Tooling                                                                                                                                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **NATS**   | NATS supports exporting monitoring data to Prometheus and has Grafana dashboards to monitor and configure alerts. There are also development monitoring tools such as nats-top. Robust side car deployment or a simple connect-and-view model with NATS surveyor is supported. |
| **gRPC**   | External components such as a service mesh are required to monitor gRPC.                                                                                                                                                                                                       |
| **Kafka**  | Kafka has a number of management tools and consoles including Confluent Control Center, Kafka, Kafka Web Console, Kafka Offset Monitor.                                                                                                                                        |
| **Pulsar** | CLI tools, per-topic dashboards, and third-party tools.                                                                                                                                                                                                                        |
| **Rabbit** | CLI tools, a plugin-based management system with dashboards and third-party tools.                                                                                                                                                                                             |

## Management

| Project    | Management Tooling                                                                                                                                                                                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **NATS**   | NATS separates operations from security. User and Account management in a deployment may be decentralized and managed through a CLI. Server (network element) configuration is separated from security with a command line and configuration file which can be reloaded with changes at runtime. |
| **gRPC**   | External components such as a service mesh are required to manage gRPC.                                                                                                                                                                                                                          |
| **Kafka**  | Kafka has a number of management tools and consoles including Confluent Control Center, Kafka, Kafka Web Console, Kafka Offset Monitor.                                                                                                                                                          |
| **Pulsar** | CLI tools, per-topic dashboards, and third-party tools.                                                                                                                                                                                                                                          |
| **Rabbit** | CLI tools, a plugin-based management system with dashboards and third-party tools.                                                                                                                                                                                                               |

## Integrations

| Project    | Built-in and Third Party Integrations                                                                                                                                                                                                                                                   |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NATS**   | NATS supports WebSockets, a Kafka bridge, an IBM MQ Bridge, a Redis Connector, Apache Spark, Apache Flink, CoreOS, Elastic, Elasticsearch, Prometheus, Telegraf, Logrus, Fluent Bit, Fluentd, OpenFAAS, HTTP, and MQTT, and [more](https://nats.io/download/#connectors-and-utilities). |
| **gRPC**   | There are a number of third party integrations including HTTP, JSON, Prometheus, Grift and others. [*(3)*](#references)\_\_                                                                                                                                                             |
| **Kafka**  | Kafka has a large number of integrations in its ecosystem, including stream processing (Storm, Samza, Flink), Hadoop, database (JDBC, Oracle Golden Gate), Search and Query (ElasticSearch, Hive), and a variety of logging and other integrations.                                     |
| **Pulsar** | Pulsar has many integrations, including ActiveMQ, Cassandra, Debezium, Flume, Elasticsearch, Kafka, Redis, and others.                                                                                                                                                                  |
| **Rabbit** | RabbitMQ has many plugins, including protocols (MQTT, STOMP), WebSockets, and various authorization and authentication plugins.                                                                                                                                                         |

## References

1. <https://docs.cloudera.com/HDPDocuments/HDF3/HDF-3.1.0/bk_planning-your-deployment/content/ch_hardware-sizing.html>
2. <https://pulsar.apache.org/docs/4.0.x/deploy-bare-metal/>
3. <https://github.com/grpc-ecosystem>


# What is NATS

Software applications and services need to exchange data. NATS is an infrastructure that allows such data exchange, segmented in the form of messages. We call this a "**message oriented middleware**".

With NATS, application developers can:

* Effortlessly build distributed and scalable client-server applications.
* Store and distribute data in realtime in a general manner. This can flexibly be achieved across various environments, languages, cloud providers and on-premises systems.

### NATS Client Applications

Developers use one of the NATS client libraries in their application code to allow them to publish, subscribe, request and reply between instances of the application or between completely separate applications. Those applications are generally referred to as 'client applications' or sometimes just as 'clients' throughout this manual (since from the point of view of the NATS server, they are clients).

### NATS Service Infrastructure

The NATS services are provided by one or more NATS server processes that are configured to interconnect with each other and provide a *NATS service infrastructure*. The NATS service infrastructure can scale from a single NATS server process running on an end device (the `nats-server` process is less than 20 MB in size!) all the way to a public global super-cluster of many clusters spanning all major cloud providers and all regions of the world such as Synadia's NGS.

### Connecting NATS Client applications to the NATS servers

To connect a NATS client application with a NATS service, and then subscribe or publish messages to subjects, it only needs to be configured with:

1. **URL:** A ['NATS URL'](https://docs.nats.io/using-nats/developer/connecting#nats-url). This is a string (in a URL format) that specifies the IP address and port where the NATS server(s) can be reached, and what kind of connection to establish (plain TCP, TLS, or Websocket).
2. **Authentication** (if needed): [Authentication](https://docs.nats.io/using-nats/developer/connecting#authentication-details) details for the application to identify itself with the NATS server(s). NATS supports multiple authentication schemes (username/password, decentralized JWT, token, TLS certificates and Nkey with challenge).

## Simple messaging design

NATS makes it easy for applications to communicate by sending and receiving messages. These messages are addressed and identified by subject strings, and do not depend on network location.

Data is encoded and framed as a message and sent by a publisher. The message is received, decoded, and processed by one or more subscribers.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-19a2ced7956b0b0681a8d97c2684d8669120eaec%2Fintro.svg?alt=media\&token=2060c455-8ed1-4c18-b903-9cf12265117d)

With this simple design, NATS lets programs share common message-handling code, isolate resources and interdependencies, and scale by easily handling an increase in message volume, whether those are service requests or stream data.

### NATS Quality of service (QoS)

NATS offers multiple qualities of service, depending on whether the application uses just the *Core NATS* functionality or also leverages the added functionalities enabled by *NATS JetStream* (JetStream is built into `nats-server` but may not be enabled on all service infrastructures).

* **At most once QoS:** *Core NATS* offers an **at most once** quality of service. If a subscriber is not listening on the subject (no subject match), or is not active when the message is sent, the message is not received. This is the same level of guarantee that TCP/IP provides. *Core NATS* is a fire-and-forget messaging system. It will only hold messages in memory and will never write messages directly to disk.
* **At-least / exactly once QoS:** If you need higher qualities of service (**at least once** and **exactly once**), or functionalities such as persistent streaming, de-coupled flow control, and Key/Value Store, you can use [NATS JetStream](https://docs.nats.io/nats-concepts/jetstream), which is built in to the NATS server (but needs to be enabled). Of course, you can also always build additional reliability into your client applications yourself with proven and scalable reference designs such as acks and sequence numbers.


# Walkthrough Setup

We have provided Walkthroughs for you to try NATS (and JetStream) on your own. In order to follow along with the walkthroughs, you could choose one of these options:

* The `nats` CLI tool must be installed, and a local NATS server must be installed (or you can use a remote server you have access to).
* You can use Synadia's NGS.
* You could even use the demo server from where you installed NATS. This is accessible via `nats://demo.nats.io` (this is a NATS connection URL; not a browser URL. You pass it to a NATS client application).

## Installing the [`nats`](https://docs.nats.io/using-nats/nats-tools/nats_cli) CLI Tool

Please refer to the [installation section in the readme](https://github.com/nats-io/natscli?tab=readme-ov-file#installation).

## Installing the NATS server locally (if needed)

If you are going to run a server locally you need to first install it and start it.\
Please refer to the [nats server installation doc](https://docs.nats.io/running-a-nats-service/introduction/installation)

Alternatively if you already know how to use NATS on a remote server, you only need to pass the server URL to `nats` using the `-s` option or preferably create a context using `nats context add`, to specify the server URL(s) and credentials file containing your user JWT.

### Start the NATS server (if needed)

To start a simple demonstration server locally, simply run:

```bash
nats-server
```

(or `nats-server -m 8222` if you want to enable the HTTP monitoring functionality)

When the server starts successfully, you will see the following messages:

```
[14524] 2021/10/25 22:53:53.525530 [INF] Starting nats-server
[14524] 2021/10/25 22:53:53.525640 [INF]   Version:  2.6.1
[14524] 2021/10/25 22:53:53.525643 [INF]   Git:      [not set]
[14524] 2021/10/25 22:53:53.525647 [INF]   Name:     NDAUZCA4GR3FPBX4IFLBS4VLAETC5Y4PJQCF6APTYXXUZ3KAPBYXLACC
[14524] 2021/10/25 22:53:53.525650 [INF]   ID:       NDAUZCA4GR3FPBX4IFLBS4VLAETC5Y4PJQCF6APTYXXUZ3KAPBYXLACC
[14524] 2021/10/25 22:53:53.526392 [INF] Starting http monitor on 0.0.0.0:8222
[14524] 2021/10/25 22:53:53.526445 [INF] Listening for client connections on 0.0.0.0:4222
[14524] 2021/10/25 22:53:53.526684 [INF] Server is ready
```

The NATS server listens for client connections on TCP Port 4222.


# Subject-Based Messaging

NATS is a system for publishing and listening for messages on named communication channels we call `Subjects`. Fundamentally, NATS is an `interest-based` messaging system, where the listener has to `subscribe` to a subset of `subjects`.

In other middleware systems subjects may be called `topics`, `channels`, `streams` (Note that in NATS the term `stream` is used for a [JetStream](https://docs.nats.io/nats-concepts/jetstream) message storage).

**What is a subject?** At its simplest, a subject is just a string of characters that form a name the publisher and subscriber can use to find each other. More commonly [subject hierarchies](#subject-hierarchies) are used to scope messages into semantic namespaces.

{% hint style="info" %}
Please check the [constraint and conventions](#characters-allowed-and-recommended-for-subject-names) on naming for subjects here.
{% endhint %}

**Location transparency** Through subject-based addressing, NATS provides location transparency across a (large) cloud of routed NATS servers.

* Subject subscriptions are automatically propagated within the server cloud.
* Messages will be automatically routed to all interested subscribers, independent of location.
* Messages with no subscribers to their subject are automatically discarded (Please see the [JetStream](https://docs.nats.io/nats-concepts/jetstream) feature for message persistence).

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-dc7b8771a8a77c9042d216ca3868ec0fa7b05fff%2Fsubjects1.svg?alt=media\&token=427c1afa-f21d-4a03-b2aa-8a04c7b82e8b)

## Wildcards

NATS provides two *wildcards* that can take the place of one or more elements in a dot-separated subject. Publishers will always send a message to a fully specified subject, without the wildcard. While subscribers can use these wildcards to listen to multiple subjects with a single subscription.

## Subject hierarchies

The `.` character is used to create a subject hierarchy. For example, a world clock application might define the following to logically group related subjects:

```markup
time.us
time.us.east
time.us.east.atlanta
time.eu.east
time.eu.east.warsaw
```

## Subject usage best practices

There is no hard limit to subject size, but it is recommended to keep the maximum number of tokens in your subjects to a reasonable value. E.g. a maximum of 16 tokens and the subject length to less than 256 characters.

### Number of subjects

NATS can manage 10s of millions of subjects efficiently, therefore, you can use fine-grained addressing for your business entities. Subjects are ephemeral resources, which will disappear when no longer subscribed to.

Still, subject subscriptions need to be cached by the server in memory. Consider when increasing your subscribed subject count to more than one million you will need more than 1GB of server memory and it will grow linearly from there.

### Subject-based filtering and security

The message subject can be filtered with various means and through various configuration elements in your NATS server cluster. For example, but not limited to:

* Security - allow/deny per user
* Import/export between accounts
* Automatic transformations
* When inserting messages into JetStream streams
* When sourcing/mirroring JetStream streams
* When connecting leaf nodes (NATS edge servers)
* ...

A well-designed subject hierarchy will make the job a lot easier for those tasks.

### Naming things

{% hint style="info" %}
There are only two hard problems in computer science: cache invalidation, naming things, and off-by-one errors. -- Unknown author
{% endhint %}

A subject hierarchy is a powerful tool for addressing your application resources. Most NATS users therefore encode business semantics into the subject name. You are free to choose a structure fit for your purpose, but you should refrain from over-complicating your subject design at the start of the project.

**Some guidelines:**

* Use the first token(s) to establish a general namespace.

```shell
factory1.tools.group42.unit17
```

* Use the final token(s)for identifiers

```shell
service.deploy.server-acme.app123
```

* A subject *should* be used for more than one message.
* Subscriptions *should* be stable (exist for receiving more than one message).
* Use wildcard subscriptions over subscribing to individual subjects whenever feasible.
* Name business or physical entities. Refrain from encoding too much data into the subject.
* Encode (business) intent into the subject, not technical details.

Pragmatic:

```shell
orders.online.store123.order171711
```

Maybe not so useful:

```shell
orders.online.us.server42.ccpayment.premium.store123.electronics.deliver-dhl.order171711.create
```

* NATS messages support headers. These can be used for additional metadata. There are subscription modes, which deliver headers only, allowing for efficient scanning of metadata in the message flow.

### Matching a single token

The first wildcard is `*` which will match a single token. For example, if an application wanted to listen for eastern time zones, they could subscribe to `time.*.east`, which would match `time.us.east` and `time.eu.east`. Note that `*` can not match a substring within a token `time.New*.east`.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-b70adb26feafc88e119d7455639c57bb82bba9a4%2Fsubjects2.svg?alt=media\&token=3800522c-1420-405b-b953-44bf54c467e0)

### Matching multiple tokens

The second wildcard is `>` which will match one or more tokens, and can only appear at the end of the subject. For example, `time.us.>` will match `time.us.east` and `time.us.east.atlanta`, while `time.us.*` would only match `time.us.east` since it can't match more than one token.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-e73c731e2444069e3aedf8e14a6cd6bb8aced13d%2Fsubjects3.svg?alt=media\&token=985e2ccc-9cad-4d1b-ac71-47e935dcdb84)

### Monitoring and wire taps

Subject to your security configuration, wildcards can be used for monitoring by creating something called a *wire tap*. In the simplest case, you can create a subscriber for `>`. This application will receive all messages -- again, subject to security settings -- sent on your NATS cluster.

### Mixing wildcards

The wildcard `*` can appear multiple times in the same subject. Both types can be used as well. For example, `*.*.east.>` will receive `time.us.east.atlanta`.

## Characters allowed and recommended for subject names

For compatibility across clients and ease of maintaining configuration files, we recommend using alphanumeric characters, `-` (dash) and `_` (underscore) ASCII characters for subject and other entity names created by the user.

UTF-8 (UTF8) characters are supported in subjects. Please use UTF-8 characters at your own risk. Using multilingual names for technical entities can create many issues for editing, configuration files, display, and cross-border collaboration.

The rules and recommendations here apply to ALL system names, subjects, streams, durables, buckets, keys (in key-value stores), as NATS will create API subjects that contain those names. NATS will enforce these constraints in most cases, but we recommend not relying on this.

* **Allowed characters**: Any Unicode character except `null`, space, `.`, `*` and `>`
* **Recommended characters:** (`a` - `z`), (`A` - `Z`), (`0` - `9`), `-` and `_` (names are case sensitive, and cannot contain whitespace).
* **Naming Conventions** If you want to delimit words, use either PascalCase as in `MyServiceOrderCreate` or `-` and `_` as in `my-service-order-create`
* **Special characters:** The period `.` (which is used to separate the tokens in the subject) and `*` and also `>` (the `*` and `>` are used as wildcards) are reserved and cannot be used.
* **Reserved names:** By convention subject names starting with a `$` are reserved for system use (e.g. subject names starting with `$SYS` or `$JS` or `$KV`, etc...). Many system subjects also use `_` (underscore) (e.g. \_INBOX , KV\_ABC, OBJ\_XYZ etc.)

Good names

```markup
time.us
time.us2.east1
time.new-york
time.SanFrancisco
```

Deprecated subject names

```markup
location.Malmö
$location.Stockholm
_Subjects_.mysubject
```

Forbidden stream names

```markup
all*data
<my_stream>
service.stream.1
```

### Pedantic mode

By default, for the sake of efficiency, subject names are not verified during message publishing. In particular, when generating subjects programmatically, this will result in illegal subjects which cannot be subscribed to. E.g. subjects containing wildcards may be ignored.

To enable subject name verification, activate `pedantic` mode in the client connection options.

```markup
//Java
Options options = Options.builder()
    .server("nats://127.0.0.1:4222")
    .pedantic()
    .build();
Connection nc = Nats.connect(options)
```


# Core NATS

Core NATS is the foundational functionality in a NATS system. It operates on a publish-subscribe model using subject/topic-based addressing. This model offers two significant advantages: location independence and a default many-to-many (M:N) communication pattern. These fundamental concepts enable powerful and innovative solutions for common development patterns, such as microservices, without requiring additional technologies like load balancers, API gateways, or DNS configuration.

NATS systems can be enhanced with [JetStream](https://docs.nats.io/nats-concepts/jetstream), which adds persistence capabilities. While Core NATS provides best-effort, at-most-once message delivery, JetStream introduces at-least-once and exactly-once semantics.


# Publish-Subscribe

## Publish-Subscribe

NATS implements a publish-subscribe message distribution model for one-to-many communication. A publisher sends a message on a subject and any active subscriber listening on that subject receives the message. Subscribers can also register interest in wildcard subjects that work a bit like a regular expression (but only a bit). This one-to-many pattern is sometimes called a fan-out.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-22d59af386038cc2717176561ffc95c63c295926%2Fpubsub.svg?alt=media\&token=cc54babb-76c4-4389-87fc-11e63429b341)

## Messages

Messages are composed of:

1. A subject.
2. A payload in the form of a byte array.
3. Any number of header fields.
4. An optional 'reply' address field.

Messages have a maximum size (which is set in the server configuration with `max_payload`). The size is set to 1 MB by default, but can be increased up to 64 MB if needed (though we recommend keeping the max message size to something more reasonable like 8 MB).


# Pub/Sub Walkthrough

NATS is a [publish subscribe](https://docs.nats.io/nats-concepts/core-nats/pubsub) messaging system [based on subjects](https://docs.nats.io/nats-concepts/subjects). Subscribers listening on a subject receive messages published on that subject. If the subscriber is not actively listening on the subject, the message is not received. Subscribers can use the wildcard tokens such as `*` and `>` to match a single token or to match the tail of a subject.

## NATS Pub/Sub Walkthrough

This simple walkthrough demonstrates some ways in which subscribers listen on subjects, and publishers send messages on specific subjects.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-a0d442c25fbeedf8400da6e26a2894e78df505ed%2Fpubsubtut.svg?alt=media\&token=6e58b7ba-9f48-4b32-9cd1-46a70d3d3739)

### Walkthrough prerequisites

If you have not already done so, you need to [install](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) the `nats` CLI Tool and optionally the nats-server on your machine.

#### 1. Create Subscriber 1

In a shell or command prompt session, start a client subscriber program.

```bash
nats sub <subject>
```

Here, `<subject>` is a subject to listen on. It helps to use unique and well thought-through subject strings because you need to ensure that messages reach the correct subscribers even when wildcards are used.

For example:

```bash
nats sub msg.test
```

You should see the message: *Listening on \[msg.test]*

#### 2. Create a Publisher and publish a message

In another shell or command prompt, create a NATS publisher and send a message.

```bash
nats pub <subject> <message>
```

Where `<subject>` is the subject name and `<message>` is the text to publish.

For example:

```bash
nats pub msg.test "NATS MESSAGE"
```

#### 3. Verify message publication and receipt

You'll notice that the publisher sends the message and prints: *Published \[msg.test] : 'NATS MESSAGE'*.

The subscriber receives the message and prints: *\[#1] Received on \[msg.test]: 'NATS MESSAGE'*.

If the receiver does not get the message, you'll need to check if you are using the same subject name for the publisher and the subscriber.

#### 4. Try publishing another message

```bash
nats pub msg.test "NATS MESSAGE 2"
```

You'll notice that the subscriber receives the message.\
Note that a message count is incremented each time your subscribing client receives a message on that subject.

#### 5. Create Subscriber 2

In a new shell or command prompt, start a new NATS subscriber.

```bash
nats sub msg.test
```

#### 6. Publish another message using the publisher client

```bash
nats pub msg.test "NATS MESSAGE 3"
```

Verify that both subscribing clients receive the message.

#### 7. Create Subscriber 3

In a new shell or command prompt session, create a new subscriber that listens on a different subject.

```bash
nats sub msg.test.new
```

#### 8. Publish another message

```bash
nats pub msg.test "NATS MESSAGE 4"
```

Subscriber 1 and Subscriber 2 receive the message, but Subscriber 3 does not. Why? Because Subscriber 3 is not listening on the message subject used by the publisher.

#### 9. Alter Subscriber 3 to use a wildcard

Change the last subscriber to listen on msg.\* and run it:

```bash
nats sub msg.*
```

Note: NATS supports the use of wildcard characters for message subscribers only. You cannot publish a message using a wildcard subject.

#### 10. Publish another message

```bash
nats pub msg.test "NATS MESSAGE 5"
```

This time, all three subscribing clients should receive the message.

Do try out a few more variations of substrings and wildcards to test your understanding.

## See Also

Publish-subscribe pattern with the NATS CLI

{% embed url="<https://www.youtube.com/watch?v=jLTVhP08Tq0>" %}
Publish-subscribe pattern - NATS CLI
{% endembed %}


# Request-Reply

Request-Reply is a common pattern in modern distributed systems. A request is sent, and the application either waits on the response with a certain timeout, or receives a response asynchronously.

The increased complexity of modern systems necessitates features like [location transparency](https://en.wikipedia.org/wiki/Location_transparency), scale-up and scale-down, observability (measuring a system's state based on the data it generates) and more. In order to implement this feature-set, various other technologies needed to incorporate additional components, sidecars (processes or services that support the primary application) and proxies. NATS on the other hand, implemented Request-Reply much more easily.

### NATS makes Request-Reply simple and powerful

* NATS supports the Request-Reply pattern using its core communication mechanism — publish and subscribe. A request is published on a given subject using a reply subject. Responders listen on that subject and send responses to the reply subject. Reply subjects are called "**inbox**". These are unique subjects that are dynamically directed back to the requester, regardless of the location of either party.
* Multiple NATS responders can form dynamic queue groups. Therefore, it's not necessary to manually add or remove subscribers from the group for them to start or stop being distributed messages. It’s done automatically. This allows responders to scale up or down as per demand.
* NATS applications "drain before exiting" (processing buffered messages before closing the connection). This allows the applications to scale down without dropping requests.
* Since NATS is based on publish-subscribe, observability is as simple as running another application that can view requests and responses to measure latency, watch for anomalies, direct scalability and more.
* The power of NATS even allows multiple responses, where the first response is utilized and the system efficiently discards the additional ones. This allows for a sophisticated pattern to have multiple responders, reduce response latency and jitter.

### The pattern

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-dc10798d4afca301adba55c1e85c599b25a2ae24%2Freqrepl.svg?alt=media\&token=c224906b-c08b-492f-b083-cf247bc60efd)

Try NATS request-reply on your own, using a live server by walking through the [request-reply walkthrough.](https://docs.nats.io/nats-concepts/core-nats/reqreply/reqreply_walkthrough)

### No responders

When a request is sent to a subject that has no subscribers, it can be convenient to know about it right away. For this use-case, a NATS client can [opt-into no\_responder messages](https://docs.nats.io/reference/reference-protocols/nats-protocol#syntax-1). This requires a server and client that support headers. When enabled, a request sent to a subject with no subscribers will immediately receive a reply that has no body, and a `503` status.

Most clients will represent this case by raising or returning an error. For example:

```go
m, err := nc.Request("foo", nil, time.Second);
# err == nats.ErrNoResponders
```


# Request-Reply Walkthrough

NATS supports [request-reply](https://docs.nats.io/nats-concepts/core-nats/reqreply) messaging. In this tutorial you explore how to exchange point-to-point messages using NATS.

## Prerequisites

If you have not already done so, you need to [install](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) the `nats` CLI Tool and optionally, the nats-server on your machine.

## Walkthrough

Start two terminal sessions. These will be used to run the NATS request and reply clients.

### In one terminal, run the reply client listener

```bash
nats reply help.please 'OK, I CAN HELP!!!'
```

You should see the message: *Listening on \[help.please]*

This means that the NATS receiver client is listening for request messages on the "help.please" subject. In NATS, the receiver is a subscriber.

### In the other terminal, run the request client

```bash
nats request help.please 'I need help!'
```

The NATS requestor client makes a request by sending the message "I need help!" on the “help.please” subject.

The NATS receiver client receives the message, formulates the reply ("OK, I CAN HELP!!!"), and sends it to the inbox of the requester.


# Queue Groups

When subscribers register themselves to receive messages from a publisher, the 1:N fan-out pattern of messaging ensures that any message sent by a publisher, reaches all subscribers that have registered. NATS provides an additional feature named "queue", which allows subscribers to register themselves as part of a queue. Subscribers that are part of a queue, form the "queue group".

## How queue groups function

As an example, consider message delivery occurring in the 1:N pattern to all subscribers based on the subject name (delivery happens even to subscribers that are not part of a queue group). If a subscriber is registered based on a queue name, it will always receive messages it is subscribed to, based on the subject name. However, if more subscribers are added to the same queue name, they become a queue group, and only one randomly chosen subscriber of the queue group will consume a message each time a message is received by the queue group. Such distributed queues are a built-in load balancing feature that NATS provides.

**Advantages**

* Ensures application fault tolerance
* Workload processing can be scaled up or down
* Scale your consumers up or down without duplicate messages
* No extra configuration required
* Queue groups are defined by the application and their queue subscribers, rather than the server configuration

Queue group names follow the same naming rules as [subjects](https://docs.nats.io/nats-concepts/subjects). Foremost, they are case sensitive and cannot contain whitespace. Consider structuring queue groups hierarchically using a period `.`. Some server functionalities like [queue permissions](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization#queue-permissions) can use [wildcard matching](https://docs.nats.io/subjects#wildcards) on them.

Queue subscribers are ideal for scaling services. Scale up is as simple as running another application, scale down is terminating the application with a signal that drains the in flight requests. This flexibility and lack of any configuration changes makes NATS an excellent service communication technology that can work with all platform technologies.

### No responder

When a request is made to a service (request/reply) and the NATS Server knows there are no services available (since there are no client applications currently subscribing to the subject in a queue-group) the server will send a “no-responders” protocol message back to the requesting client which will break from blocking API calls. This allows applications to react immediately. This further enables building a highly responsive system at scale, even in the face of application failures and network partitions.

## Stream as a queue

With [JetStream](https://docs.nats.io/nats-concepts/jetstream) a stream can also be used as a queue by setting the retention policy to `WorkQueuePolicy` and leveraging [`pull` consumers](https://docs.nats.io/nats-concepts/jetstream/consumers) to get easy horizontal scalability of the processing (or using an explicit ack push consumer with a queue group of subscribers).

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-62652b3e6dd556e3cb1c3bb474ec10038334c600%2Fqueue.svg?alt=media\&token=4028a127-cbec-4958-a020-08564cb3acdb)

### Queuing geo-affinity

When connecting to a globally distributed NATS super-cluster, there is an automatic service geo-affinity due to the fact that a service request message will only be routed to another cluster (i.e. another region) if there are no listeners on the cluster available to handle the request locally.

### Tutorial

Try NATS queue subscriptions on your own, using a live server by walking through the [queueing walkthrough](https://docs.nats.io/nats-concepts/core-nats/queue/queues_walkthrough).


# Queueing Walkthrough

NATS supports a form of load balancing using [queue groups](https://docs.nats.io/nats-concepts/core-nats/queue). Subscribers register a queue group name. A single subscriber in the group is randomly selected to receive the message.

## Walkthrough prerequisites

If you have not already done so, you need to [install](https://docs.nats.io/nats-concepts/what-is-nats/walkthrough_setup) the `nats` CLI Tool and optionally the nats-server on your machine.

### 1. Start the first member of the queue group

The `nats reply` instances don't just subscribe to the subject but also automatically join a queue group (`"NATS-RPLY-22"` by default)

```bash
nats reply foo "service instance A Reply# {{Count}}"
```

### 2. Start a second member of the queue-group

In a new window

```bash
nats reply foo "service instance B Reply# {{Count}}"
```

### 3. Start a third member of the queue-group

In a new window

```bash
nats reply foo "service instance C Reply# {{Count}}"
```

### 4. Publish a NATS message

```bash
nats request foo "Simple request"
```

### 5. Verify message publication and receipt

You should see that only one of the my-queue group subscribers receives the message and replies it, and you can also see which one of the available queue-group subscribers processed the request from the reply message received (i.e. service instance A, B or C)

### 6. Publish another message

```bash
nats request foo "Another simple request"
```

You should see that a different queue group subscriber receives the message this time, chosen at random among the 3 queue group members.

You can also send any number of requests back-to-back. From the received messages, you'll see the distribution of those requests amongst the members of the queue-group. For example: `nats request foo --count 10 "Request {{Count}}"`

### 7. Stop/start queue-group members

You can at any time start yet another service instance, or kill one and see how the queue-group automatically takes care of adding/removing those instances from the group.

## See Also

Queue groups using the NATS CLI

{% embed url="<https://youtu.be/jLTVhP08Tq0?t=101>" %}
Queue Groups NATS CLI
{% endembed %}


# JetStream

NATS has a built-in persistence engine called [JetStream](https://docs.nats.io/using-nats/developer/develop_jetstream) which enables messages to be stored and replayed at a later time. Unlike *NATS Core* which requires you to have an active subscription to process messages as they happen, JetStream allows the NATS server to capture messages and replay them to consumers as needed. This functionality enables a different quality of service for your NATS messages, and enables fault-tolerant and high-availability configurations.

JetStream is built into `nats-server`. If you have a cluster of JetStream-enabled servers you can enable data replication and thus guard against failures and service disruptions.

JetStream was created to address the problems identified with streaming technology today - complexity, fragility, and a lack of scalability. Some technologies address these better than others, but no current streaming technology is truly multi-tenant, horizontally scalable, or supports multiple deployment models. No other technology that we are aware of can scale from edge to cloud using the same security context while having complete deployment observability for operations.

#### Additional capabilities enabled by JetStream

The JetStream persistence layer enables additional use cases typically not found in messaging systems. Being built on top of JetStream they inherit the core capabilities of JetStream, replication, security, routing limits, and mirroring.

* [Key Value Store](#key-value-store) A map (associative array) with atomic operations
* [Object Store](#object-store) File transfer, replications and storage API. Uses chunked transfers for scalability.

Key/Value and File transfer are capabilities commonly found in in-memory databases or deployment tools. While NATS does not intend to compete with the feature set of such tools, it is our goal to provide the developer with reasonable complete set of data storage and replications features for use cases like micro service, edge deployments and server management.

#### Configuration

To configure a `nats-server` with JetStream refer to:

* [Configuring JetStream](https://docs.nats.io/running-a-nats-service/configuration/resource_management)
* [JetStream Clustering](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering)

#### Examples

For runnable JetStream code examples, refer to [NATS by Example](https://natsbyexample.com).

#### Goals

JetStream was developed with the following goals in mind:

* The system must be easy to configure and operate and be observable.
* The system must be secure and operate well with NATS 2.0 security models.
* The system must scale horizontally and be applicable to a high ingestion rate.
* The system must support multiple use cases.
* The system must self-heal.
* The system must allow NATS messages to be part of a stream as desired.
* The system must display payload agnostic behavior.
* The system must not have third party dependencies.

### JetStream capabilities

#### Streaming: temporal decoupling between the publishers and subscribers

One of the tenets of basic publish/subscribe messaging is that there is a required temporal coupling between the publishers and the subscribers: subscribers only receive the messages that are published when they are actively connected to the messaging system (i.e. they do not receive messages that are published while they are not subscribing or not running or disconnected). The traditional way for messaging systems to provide temporal decoupling of the publishers and subscribers is through the 'durable subscriber' functionality or sometimes through 'queues', but neither one is perfect:

* durable subscribers need to be created *before* the messages get published
* queues are meant for workload distribution and consumption, not to be used as a mechanism for message replay.

However, in many use cases, you do not need to 'consume exactly once' functionality but rather the ability to replay messages on demand, as many times as you want. This need has led to the popularity of some 'streaming' messaging platforms.

JetStream provides *both* the ability to *consume* messages as they are published (i.e. 'queueing') as well as the ability to *replay* messages on demand (i.e. 'streaming'). See [retention policies](#Retention-policies-and-limits) below.

**Replay policies**

JetStream consumers support multiple replay policies, depending on whether the consuming application wants to receive either:

* *all* of the messages currently stored in the stream, meaning a complete 'replay' and you can select the 'replay policy' (i.e. the speed of the replay) to be either:
  * *instant* (meaning the messages are delivered to the consumer as fast as it can take them).
  * *original* (meaning the messages are delivered to the consumer at the rate they were published into the stream, which can be very useful for example for staging production traffic).
* the *last* message stored in the stream, or the *last message for each subject* (as streams can capture more than one subject).
* starting from a specific *sequence number*.
* starting from a specific *start time*.

**Retention policies and limits**

JetStream enables new functionalities and higher qualities of service on top of the base 'Core NATS' functionality. However, practically speaking, streams can't always just keep growing 'forever' and therefore JetStream supports multiple retention policies as well as the ability to impose size limits on streams.

**Limits**

You can impose the following limits on a stream

* Maximum message age.
* Maximum total stream size (in bytes).
* Maximum number of messages in the stream.
* Maximum individual message size.
* You can also set limits on the number of consumers that can be defined for the stream at any given point in time.

You must also select a **discard policy** which specifies what should happen once the stream has reached one of its limits and a new message is published:

* *discard old* means that the stream will automatically delete the oldest message in the stream to make room for the new messages.
* *discard new* means that the new message is discarded (and the JetStream publish call returns an error indicating that a limit was reached).

**Retention policy**

You can choose what kind of retention you want for each stream:

* *limits* (the default) is to provide a replay of messages in the stream.
* *work queue* (the stream is used as a shared queue and messages are removed from it as they are consumed) is to provide the exactly-once consumption of messages in the stream.
* *interest* (messages are kept in the stream for as long as there are consumers that haven't delivered the message yet) is a variation of work queue that only retains messages if there is interest (consumers currently defined on the stream) for the message's subject.

Note that regardless of the retention policy selected, the limits (and the discard policy) *always* apply.

**Subject mapping transformations**

JetStream also enables the ability to apply subject mapping transformations to messages as they are ingested into a stream.

#### Persistent and Consistent distributed storage

You can choose the durability as well as the resilience of the message storage according to your needs.

* Memory storage.
* File storage.
* Replication (1 (none), 2, 3) between nats servers for Fault Tolerance.

JetStream uses a NATS optimized RAFT distributed quorum algorithm to distribute the persistence service between NATS servers in a cluster while maintaining immediate consistency (as opposed to [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)) even in the face of failures.

For writes (publications to a stream), the formal consistency model of NATS JetStream is [Linearizable](https://jepsen.io/consistency/models/linearizable). On the read side (listening to or replaying messages from streams) the formal models don't really apply because JetStream does not support atomic batching of multiple operations together (so the only kind of 'transaction' is the persisting, replicating and voting of a single operation on the stream) but in essence, JetStream is [serializable](https://jepsen.io/consistency/models/serializable) because messages are added to a stream in one global order (which you can control using compare and publish).

Do note, while we do guarantee immediate consistency when it comes to [monotonic writes](https://jepsen.io/consistency/models/monotonic-writes) and [monotonic reads](https://jepsen.io/consistency/models/monotonic-reads). We don't guarantee [read your writes](https://jepsen.io/consistency/models/read-your-writes) at this time, as reads through *direct get* requests may be served by followers or mirrors. More consistent results can be achieved by sending get requests to the stream leader.

JetStream can also provide encryption at rest of the messages being stored.

In JetStream the configuration for storing messages is defined separately from how they are consumed. Storage is defined in a [*Stream*](https://docs.nats.io/nats-concepts/jetstream/streams) and consuming messages is defined by multiple [*Consumers*](https://docs.nats.io/nats-concepts/jetstream/consumers).

**Stream replication factor**

A stream's replication factor (R, often referred to as the number 'Replicas') determines how many places it is stored allowing you to tune to balance risk with resource usage and performance. A stream that is easily rebuilt or temporary might be memory-based with a R=1 and a stream that can tolerate some downtime might be file-based R-1.

Typical usage to operate in typical outages and balance performance would be a file-based stream with R=3. A highly resilient, but less performant and more expensive configuration is R=5, the replication factor limit.

Rather than defaulting to the maximum, we suggest selecting the best option based on the use case behind the stream. This optimizes resource usage to create a more resilient system at scale.

* Replicas=1 - Cannot operate during an outage of the server servicing the stream. Highly performant.
* Replicas=2 - No significant benefit at this time. We recommend using Replicas=3 instead.
* Replicas=3 - Can tolerate the loss of one server servicing the stream. An ideal balance between risk and performance.
* Replicas=4 - No significant benefit over Replicas=3 except marginally in a 5 node cluster.
* Replicas=5 - Can tolerate simultaneous loss of two servers servicing the stream. Mitigates risk at the expense of performance.

**Mirroring and Sourcing between streams**

JetStream also allows server administrators to easily mirror streams, for example between different JetStream domains in order to offer disaster recovery. You can also define a stream that 'sources' from one or more other streams.

**Syncing data to disk**

JetStream’s file-based streams persist messages to disk. However, while JetStream does flush file writes to the OS synchronously, under the default configuration it does not immediately `fsync` data to disk. The server uses a configurable `sync_interval` option, with a default value of 2 minutes, which controls how often the server will `fsync` its data. The data will be `fsync`-ed no later than this interval. This has important consequences for durability with respect to OS failures (meaning ungraceful exit of the Operating System such as a power outage, and not just ungraceful exit or killing of the `nats-server` process itself):

In a non-replicated setup, an OS failure may result in data loss. A client might publish a message and receive an acknowledgment, but the data may not yet be safely stored to disk. As a result, after an OS failure recovery, a server may have lost recently acknowledged messages.

In a replicated setup, a published message is acknowledged after it successfully replicated to at least a quorum of servers. However, replication alone is not enough to guarantee the strongest level of durability against multiple systemic failures.

* If multiple servers fail simultaneously, all due to an OS failure, and before their data has been `fsync`-ed, the cluster may fail to recover the most recently acknowledged messages.
* If a failed server lost data locally due to an OS failure, although extremely rare, there are some combinations of events where it may rejoin the cluster and form a new majority with nodes that have never received or persisted a given message. The cluster may then proceed with incomplete data causing acknowledged messages to be lost.

Setting a lower `sync_interval` increases the frequency of disk writes, and reduces the window for potential data loss, but at the expense of performance. Additionally, setting `sync_interval: always` will make sure servers `fsync` after every message before it is acknowledged. This setting, combined with replication in different data centers or availability zones, provides the strongest durability guarantees but at the slowest performance.

The default settings have been chosen to balance performance and risk of data loss in what we consider to be a typical production deployment scenario across multiple availability zones.

For example, consider a stream with 3 replicas deployed across three separate availability zones. For the stream state to diverge across nodes would require that:

* One of the 3 servers is already offline, isolated or partitioned.
* A second server’s OS needs to fail such that it loses writes of messages that were only available on 2 out of 3 nodes due to them not being `fsync`-ed.
* The stream leader that’s part of the above 2 out of 3 nodes needs to go down or become isolated/partitioned.
* The first server of the original partition that didn’t receive the writes recovers from the partition.
* The OS-failed server now returns and comes in contact with the first server but not with the previous stream leader.

In the end, 2 out of 3 nodes will be available, the previous stream leader with the writes will be unavailable, one server will have lost some writes due to the OS failure, and one server will have never seen these writes due to the earlier partition. The last two servers could then form a majority and accept new writes, essentially losing some of the former writes.

Importantly this is a failure condition where stream state could diverge, but in a system that is deployed across multiple availability zones, it would require multiple faults to align precisely in the right way.

A potential mitigation to a failure of this kind is not automatically bringing back a server process that was OS-failed until it is known that a majority of the remaining servers have received the new writes, or by peer-removing the crashed server and admitting it as a new and wiped peer and allowing it to recover over the network from existing healthy nodes (although this could be expensive depending on the amount of data involved).

For use cases where minimizing loss is an absolute priority, `sync_interval: always` can of course still be configured, but note that this will have a server-wide performance impact that may affect throughput or latencies. For production environments, operators should evaluate whether the default is correct for their use case, target environment, costs, and performance requirements.

Alternatively, a hybrid approach can be used where existing clusters still function under their default `sync_interval` settings but a new cluster gets added that’s configured with `sync_interval: always`, and utilizes server tags. The placement of a stream can then be specified to have this stream store data on this higher durability cluster through the use of [placement tags](https://docs.nats.io/nats-concepts/streams#placement).

```
# Configure a cluster that's dedicated to always sync writes.
server_tags: ["sync:always"]

jetstream {
    sync_interval: always
}
```

Create a replicated stream that’s specifically placed in the cluster using `sync_interval: always`, to ensure the strongest durability only for stream writes that require this level of durability.

```
nats stream add --replicas 3 --tag sync:always
```

#### De-coupled flow control

JetStream provides decoupled flow control over streams, the flow control is not 'end to end' where the publisher(s) are limited to publish no faster than the slowest of all the consumers (i.e. the lowest common denominator) can receive but is instead happening individually between each client application (publishers or consumers) and the nats server.

When using the JetStream publish calls to publish to streams there is an acknowledgment mechanism between the publisher and the NATS server, and you have the choice of making synchronous or asynchronous (i.e. 'batched') JetStream publish calls.

On the subscriber side, the sending of messages from the NATS server to the client applications receiving or consuming messages from streams is also flow controlled.

#### Exactly once semantics

Because publications to streams using the JetStream publish calls are acknowledged by the server the base quality of service offered by streams is '*at least once*', meaning that while reliable and normally duplicate free there are some specific failure scenarios that could result in a publishing application believing (wrongly) that a message was not published successfully and therefore publishing it again, and there are failure scenarios that could result in a client application's consumption acknowledgment getting lost and therefore in the message being re-sent to the consumer by the server. Those failure scenarios while being rare and even difficult to reproduce do exist and can result in perceived 'message duplication' at the application level.

Therefore, JetStream also offers an '*exactly once*' quality of service. For the publishing side, it relies on the publishing application attaching a unique message or publication ID in a message header and on the server keeping track of those IDs for a configurable rolling period of time in order to detect the publisher publishing the same message twice. For the subscribers a *double* acknowledgment mechanism is used to avoid a message being erroneously re-sent to a subscriber by the server after some kinds of failures.

#### Consumers

JetStream [consumers](https://docs.nats.io/nats-concepts/jetstream/consumers) are 'views' on a stream, they are subscribed to (or pulled) by client applications to receive copies of (or to consume if the stream is set as a working queue) messages stored in the stream.

**Fast push consumers**

Client applications can choose to use fast un-acknowledged `push` (ordered) consumers to receive messages as fast as possible (for the selected replay policy) on a specified delivery subject or to an inbox. Those consumers are meant to be used to 'replay' rather than 'consume' the messages in a stream.

**Horizontally scalable pull consumers with batching**

Client applications can also use and share `pull` consumers that are demand-driven, support batching and must explicitly acknowledge message reception and processing which means that they can be used to consume (i.e. use the stream as a distributed queue) as well as process the messages in a stream.

Pull consumers can and are meant to be shared between applications (just like queue groups) in order to provide easy and transparent horizontal scalability of the processing or consumption of messages in a stream without having (for example) to worry about having to define partitions or worry about fault-tolerance.

Note: using pull consumers doesn't mean that you can't get updates (new messages published into the stream) 'pushed' in real-time to your application, as you can pass a (reasonable) timeout to the consumer's Fetch call and call it in a loop.

**Consumer acknowledgments**

While you can decide to use un-acknowledged consumers trading quality of service for the fastest possible delivery of messages, most processing is not idem-potent and requires higher qualities of service (such as the ability to automatically recover from various failure scenarios that could result in some messages not being processed or being processed more than once) and you will want to use acknowledged consumers. JetStream supports more than one kind of acknowledgment:

* Some consumers support acknowledging *all* the messages up to the sequence number of the message being acknowledged, some consumers provide the highest quality of service but require acknowledging the reception and processing of each message explicitly as well as the maximum amount of time the server will wait for an acknowledgment for a specific message before re-delivering it (to another process attached to the consumer).
* You can also send back *negative* acknowledgements.
* You can even send *in progress* acknowledgments (to indicate that you are still processing the message in question and need more time before acking or nacking it).

### Key Value Store

The JetStream persistence layer enables the Key Value store: the ability to store, retrieve and delete `value` messages associated with a `key` into a `bucket`.

* [Concepts](https://docs.nats.io/nats-concepts/jetstream/key-value-store)
* [Walkthrough](https://docs.nats.io/nats-concepts/jetstream/key-value-store/kv_walkthrough)
* [API and details](https://docs.nats.io/using-nats/developer/develop_jetstream/kv)

#### Watch and History

You can subscribe to changes in a Key Value on the bucket or individual key level with `watch` and optionally retrieve a `history` of the values (and deletions) that have happened on a particular key.

#### Atomic updates and locking

The Key Value store supports atomic `create` and `update` operations. This enables pessimistic locks (by creating a key and holding on to it) and optimistic locks (using CAS - compare and set).

### Object Store

The Object Store is similar to the Key Value Store. The key being replaced by a file name and value being designed to store arbitrarily large `objects` (e.g. files, even if they are very large) rather than 'values' that are message-sized (i.e. limited to 1Mb by default). This is achieved by chunking messages.

* [Concepts](https://docs.nats.io/nats-concepts/jetstream/obj_store)
* [Walkthrough](https://docs.nats.io/nats-concepts/jetstream/obj_store/obj_walkthrough)
* [API and details](https://docs.nats.io/using-nats/developer/develop_jetstream/object)

## Legacy

Note that JetStream completely replaces the [STAN](https://github.com/nats-io/nats.docs/blob/master/legacy/stan/README.md) legacy NATS streaming layer.


# Streams

Streams are message stores, each stream defines how messages are stored and what the limits (duration, size, interest) of the retention are. Streams consume normal [NATS subjects](https://docs.nats.io/nats-concepts/subjects), any message published on those subjects will be captured in the defined storage system. You can do a normal publish to the subject for unacknowledged delivery, though it’s better to use the JetStream publish calls instead as the JetStream server will reply with an acknowledgement that it was successfully stored.

![Orders](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-dedcc17f082fa1e39497c54ed8191b6424ee7792%2Fstreams-and-consumers-75p.png?alt=media\&token=3dc2026b-8ef1-4f5b-a844-b3dbce6abbd9)

The diagram above shows the concept of storing all `ORDERS.*` in the Stream even though there are many types of order related messages. We’ll show how you can selectively consume subsets of messages later. Relatively speaking the Stream is the most resource consuming component so being able to combine related data in this manner is important to consider.

Streams can consume many subjects. Here we have `ORDERS.*` but we could also consume `SHIPPING.state` into the same Stream should that make sense.

## Stream limits and message retention

Streams support various retention policies which define when messages in the stream can be automatically deleted, such as when stream limits are hit (like max count, size or age of messages), or also more novel options that apply on top of the limits such as interest-based retention or work-queue semantics (see [Retention Policy](#retentionpolicy)).

Upon reaching message limits, the server will automatically discard messages either by removing the oldest messages to make room for new ones (`DiscardOld`) or by refusing to store new messages (`DiscardNew`). For more details, see [Discard Policy](#discardpolicy).

Streams support deduplication using a `Nats-Msg-Id` header and a sliding window within which to track duplicate messages. See the [Message Deduplication](https://docs.nats.io/using-nats/developer/develop_jetstream/model_deep_dive#message-deduplication) section.

For examples on how to configure streams with your preferred NATS client, see [NATS by Example](https://natsbyexample.com).

## Configuration

Below are the set of stream configuration options that can be defined. The `Version` column indicates the version of the server the option was introduced. The `Editable` column indicates the option can be edited after the stream created. See client-specific examples [here](https://natsbyexample.com).

| Field                                 | Description                                                                                                                                                                                                                                                                                               | Version | Editable             |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------- |
| Name                                  | Identifies the stream and has to be unique within JetStream account. Names cannot contain whitespace, `.`, `*`, `>`, path separators (forward or backwards slash), and non-printable characters.                                                                                                          | 2.2.0   | No                   |
| [Storage](#storagetype)               | The storage type for stream data.                                                                                                                                                                                                                                                                         | 2.2.0   | No                   |
| [Subjects](#subjects)                 | A list of subjects to bind. Wildcards are supported. Cannot be set for [mirror](#mirrors) streams.                                                                                                                                                                                                        | 2.2.0   | Yes                  |
| Replicas                              | How many replicas to keep for each message in a clustered JetStream, maximum 5.                                                                                                                                                                                                                           | 2.2.0   | Yes                  |
| MaxAge                                | Maximum age of any message in the Stream, expressed in nanoseconds.                                                                                                                                                                                                                                       | 2.2.0   | Yes                  |
| MaxBytes                              | Maximum number of bytes stored in the stream. Adheres to Discard Policy, removing oldest or refusing new messages if the Stream exceeds this size.                                                                                                                                                        | 2.2.0   | Yes                  |
| MaxMsgs                               | Maximum number of messages stored in the stream. Adheres to Discard Policy, removing oldest or refusing new messages if the Stream exceeds this number of messages.                                                                                                                                       | 2.2.0   | Yes                  |
| MaxMsgSize                            | The largest message that will be accepted by the Stream. The size of a message is a sum of payload and headers.                                                                                                                                                                                           | 2.2.0   | Yes                  |
| MaxConsumers                          | Maximum number of Consumers that can be defined for a given Stream, `-1` for unlimited.                                                                                                                                                                                                                   | 2.2.0   | No                   |
| NoAck                                 | Default `false`. Disables acknowledging messages that are received by the Stream. This is mandatory when archiving messages which have a reply subject set. E.g. requests in an Request/Reply communication. By default JetStream will acknowledge each message with an empty reply on the reply subject. | 2.2.0   | Yes                  |
| [Retention](#retentionpolicy)         | Declares the retention policy for the stream.                                                                                                                                                                                                                                                             | 2.2.0   | No                   |
| [Discard](#discardpolicy)             | The behavior of discarding messages when any streams’ limits have been reached.                                                                                                                                                                                                                           | 2.2.0   | Yes                  |
| DuplicateWindow                       | The window within which to track duplicate messages, expressed in nanoseconds.                                                                                                                                                                                                                            | 2.2.0   | Yes                  |
| [Placement](#placement)               | Used to declare where the stream should be placed via tags and/or an explicit cluster name.                                                                                                                                                                                                               | 2.2.0   | Yes                  |
| [Mirror](#mirrors)                    | If set, indicates this stream is a mirror of another stream.                                                                                                                                                                                                                                              | 2.2.0   | Yes (since 2.12.0)   |
| [Sources](#stream-sources)            | If defined, declares one or more streams this stream will source messages from.                                                                                                                                                                                                                           | 2.2.0   | Yes                  |
| MaxMsgsPerSubject                     | Limits maximum number of messages in the stream to retain *per subject*.                                                                                                                                                                                                                                  | 2.3.0   | Yes                  |
| Description                           | A verbose description of the stream.                                                                                                                                                                                                                                                                      | 2.3.3   | Yes                  |
| Sealed                                | Sealed streams do not allow messages to be deleted via limits or API, sealed streams can not be unsealed via configuration update. Can only be set on already created streams via the Update API.                                                                                                         | 2.6.2   | Yes (once)           |
| DenyDelete                            | Restricts the ability to delete messages from a stream via the API.                                                                                                                                                                                                                                       | 2.6.2   | No                   |
| DenyPurge                             | Restricts the ability to purge messages from a stream via the API.                                                                                                                                                                                                                                        | 2.6.2   | No                   |
| [AllowRollup](#allowrollup)           | Allows the use of the `Nats-Rollup` header to replace all contents of a stream, or subject in a stream, with a single new message.                                                                                                                                                                        | 2.6.2   | Yes                  |
| [RePublish](#republish)               | If set, messages stored to the stream will be immediately *republished* to the configured subject.                                                                                                                                                                                                        | 2.8.3   | Yes                  |
| AllowDirect                           | If true, and the stream has more than one replica, each replica will respond to *direct get* requests for individual messages, not only the leader.                                                                                                                                                       | 2.9.0   | Yes                  |
| MirrorDirect                          | If true, and the stream is a mirror, the mirror will participate in a serving *direct get* requests for individual messages from origin stream.                                                                                                                                                           | 2.9.0   | Yes                  |
| DiscardNewPerSubject                  | If true, applies discard new semantics on a per subject basis. Requires `DiscardPolicy` to be `DiscardNew` and the `MaxMsgsPerSubject` to be set.                                                                                                                                                         | 2.9.0   | Yes                  |
| Metadata                              | A set of application-defined key-value pairs for associating metadata on the stream.                                                                                                                                                                                                                      | 2.10.0  | Yes                  |
| Compression                           | If file-based and a compression algorithm is specified, the stream data will be compressed on disk. Valid options are nothing (empty string) or `s2` for Snappy compression.                                                                                                                              | 2.10.0  | Yes                  |
| FirstSeq                              | If specified, a new stream will be created with its initial sequence set to this value.                                                                                                                                                                                                                   | 2.10.0  | No                   |
| [SubjectTransform](#subjecttransform) | Applies a subject transform (to matching messages) before storing the message.                                                                                                                                                                                                                            | 2.10.0  | Yes                  |
| ConsumerLimits                        | Sets default limits for consumers created for a stream. Those can be overridden per consumer.                                                                                                                                                                                                             | 2.10.0  | Yes                  |
| AllowMsgTTL                           | If set, allows header initiated per-message TTLs, instead of relying solely on MaxAge.                                                                                                                                                                                                                    | 2.11.0  | No (can only enable) |
| SubjectDeleteMarkerTTL                | If set, a subject delete marker will be placed after the last message of a subject ages out. This defines the TTL of the delete marker that's left behind.                                                                                                                                                | 2.11.0  | Yes                  |
| AllowAtomicPublish                    | If set, allows atomically writing a batch of N messages into the stream.                                                                                                                                                                                                                                  | 2.12.0  | Yes                  |
| AllowMsgCounter                       | If set, the stream will function as a counter stream, hosting distributed counter CRDTs.                                                                                                                                                                                                                  | 2.12.0  | No                   |
| AllowMsgSchedules                     | If set, allows message scheduling in the stream.                                                                                                                                                                                                                                                          | 2.12.0  | No (can only enable) |

### StorageType

The storage types include:

* `File` (default) - Uses file-based storage for stream data.
* `Memory` - Uses memory-based storage for stream data.

### Subjects

*Note: a stream configured as a* [*mirror*](#mirrors) *cannot be configured with a set of subjects. A mirror implicitly sources a subset of the origin stream (optionally with a filter), but does not subscribe to additional subjects.*

If no explicit subject is specified, the default subject will be the same name as the stream. Multiple subjects can be specified and edited over time. Note, if messages are stored by a stream on a subject that is subsequently removed from the stream config, consumers will still observe those messages if their subject filter overlaps.

### RetentionPolicy

The retention options include:

* `LimitsPolicy` (default) - Retention based on the various limits that are set including: `MaxMsgs`, `MaxBytes`, `MaxAge`, and `MaxMsgsPerSubject`. If any of these limits are set, whichever limit is hit first will cause the automatic deletion of the respective message(s). See a [full code example](https://natsbyexample.com/examples/jetstream/limits-stream/go).
* `WorkQueuePolicy` - Retention with the typical behavior of a FIFO queue. Each message can be consumed only once. This is enforced by only allowing *one* consumer to be created *per subject* for a work-queue stream (i.e. the consumers' subject filter(s) must *not* overlap). Once a given message is ack’ed, it will be deleted from the stream. See a [full code example](https://natsbyexample.com/examples/jetstream/workqueue-stream/go).
* `InterestPolicy` - Retention based on the consumer *interest* in the stream and messages. The base case is that there are zero consumers defined for a stream. If messages are published to the stream, they will be immediately deleted so there is no *interest*. This implies that consumers need to be bound to the stream ahead of messages being published to the stream. Once a given message is ack’ed by *all* consumers filtering on the subject, the message is deleted (same behavior as `WorkQueuePolicy`). See a [full code example](https://natsbyexample.com/examples/jetstream/interest-stream/go).

{% hint style="warning" %}
If the `InterestPolicy` or `WorkQueuePolicy` is chosen for a stream, note that any limits, if defined, will still be enforced. For example, given a work-queue stream, if `MaxMsgs` are set and the default discard policy of *old*, messages will be automatically deleted even if the consumer did not receive them.
{% endhint %}

{% hint style="info" %}
If the `InterestPolicy` is chosen for a stream, note that when a consumer is deleted, either manually or as part of a server cleanup when the consumer's `InactiveThreshold` is reached, and that consumer was the last one that marked interest in a set of subjects, the server may not immediately delete all messages that belong to that set of subjects, for performance reasons. Instead, deletion may be deferred until those messages reach the start of the stream.
{% endhint %}

{% hint style="info" %}
`WorkQueuePolicy` streams will only delete messages enforced by limits or when a message has been successfully `Ack’d` by its consumer. Messages that have attempted redelivery and have reached `MaxDeliver` attempts for the consumer will remain in the stream and must be manually deleted via the JetStream API.
{% endhint %}

### DiscardPolicy

The discard behavior applies only for streams that have at least one limit defined. The options include:

* `DiscardOld` (default) - This policy will delete the oldest messages in order to maintain the limit. For example, if `MaxAge` is set to one minute, the server will automatically delete messages older than one minute with this policy.
* `DiscardNew` - This policy will reject *new* messages from being appended to the stream if it would *exceed* one of the limits. An extension to this policy is `DiscardNewPerSubject` which will apply this policy on a per-subject basis within the stream.

### Placement

Refers to the placement of the stream assets (data) within a NATS deployment, be it a single cluster or a supercluster. A given stream, including all replicas (not mirrors), are bound to a single cluster. So when creating or moving a stream, a cluster will be chosen to host the assets.

Without declaring explicit placement for a stream, by default, the stream will be created within the cluster that the client is connected to assuming it has sufficient storage available.

By declaring stream placement, where these assets are located can be controlled explicitly. This is generally useful to co-locate with the most active clients (publishers or consumers) or may be required for data sovereignty reasons.

Placement is supported in all client SDKs as well as the CLI. For example, adding a stream via the CLI to place a stream in a specific cluster looks like this:

```
nats stream add --cluster aws-us-east1-c1
```

For this to work, all servers in a given cluster must define the `name` field within the [`cluster`](https://docs.nats.io/running-a-nats-service/configuration/clustering/cluster_config) server configuration block.

```
cluster {
  name: aws-us-east1-c1
  # etc..
}
```

If you have multiple clusters that form a supercluster, then each is required to have a different name.

Another placement option are *tags*. Each server can have its own set of tags, [defined in configuration](https://docs.nats.io/running-a-nats-service/configuration#cluster-configuration-monitoring-and-tracing), typically describing properties of geography, hosting provider, sizing tiers, etc. In addition, tags are often used in conjunction with the `jetstream.unique_tag` config option to ensure that replicas must be placed on servers having *different* values for the tag.

For example, a server A, B, and C in the above cluster might all the same configuration except for the availability zone they are deployed to.

```
// Server A
server_tags: ["cloud:aws", "region:us-east1", "az:a"]

jetstream: {
  unique_tag: "az"
}

// Server B
server_tags: ["cloud:aws", "region:us-east1", "az:b"]

jetstream: {
  unique_tag: "az"
}

// Server C
server_tags: ["cloud:aws", "region:us-east1", "az:c"]

jetstream: {
  unique_tag: "az"
}
```

Now we can create a stream by using tags, for example indicating we want a stream in us-east1.

```
nats stream add --tag region:us-east1
```

If we had a second cluster in Google Cloud with the same region tag, the stream could be placed in either the AWS or GCP cluster. However, the `unique_tag` constraint ensures each replica will be placed in a different AZ in the cluster that was selected implicitly by the placement tags.

Although less common, note that both the cluster *and* tags can be used for placement. This would be used if a single cluster contains servers have different properties.

### Sources and Mirrors

When a stream is configured with a `source` or `mirror`, it will automatically and asynchronously replicate messages from the origin stream. There are several options when declaring the configuration.

A source or mirror stream can have its own retention policy, replication, and storage type. Changes to the source or mirror, e.g. deleting messages or publishing, do not reflect on the origin stream.

{% hint style="info" %}
`Sources` is a generalization of the `Mirror` and allows for sourcing data from one or more streams concurrently. We suggest to use `Sources` in new configurations. If you require the target stream to act as a read-only replica:

* Configure the stream without listen subjects **or**
* Temporarily disable the listen subjects through client authorizations.
  {% endhint %}

#### Stream sources

A stream defining `Sources` is a generalized replication mechanism and allows for sourcing data from one or more streams concurrently as well as allowing direct write/publish by clients. Essentially the source streams and client writes are aggregated into a single interleaved stream. Subject transformation and filtering allow for powerful data distribution architectures.

#### Mirrors

A mirror can source its messages from exactly one stream and a clients can not directly write to the mirror. Although messages cannot be published to a mirror directly by clients, messages can be deleted on-demand (beyond the retention policy), and consumers have all capabilities available on regular streams.

**For details see:**

* [Source and Mirror](https://docs.nats.io/nats-concepts/jetstream/source_and_mirror)

### AllowRollup

If enabled, the `AllowRollup` stream option allows for a published message having a `Nats-Rollup` header indicating all prior messages should be purged. The scope of the *purge* is defined by the header value, either `all` or `sub`.

The `Nats-Rollup: all` header will purge all prior messages in the stream. Whereas the `sub` value will purge all prior messages for a given subject.

A common use case for rollup is for state snapshots, where the message being published has accumulated all the necessary state from the prior messages, relative to the stream or a particular subject.

### RePublish

If enabled, the `RePublish` stream option will result in the server re-publishing messages received into a stream automatically and immediately after a successful write, to a distinct destination subject.

For high scale needs where, currently, a dedicated consumer may add too much overhead, clients can establish a core NATS subscription to the destination subject and receive messages that were appended to the stream in real-time.

The fields for configuring republish include:

* `Source` - An optional subject pattern which is a subset of the subjects bound to the stream. It defaults to all messages in the stream, e.g. `>`.
* `Destination` - The destination subject messages will be re-published to. The source and destination must be a valid [subject mapping](https://docs.nats.io/nats-concepts/subject_mapping).
* `HeadersOnly` - If true, the message data will not be included in the re-published message, only an additional header `Nats-Msg-Size` indicating the size of the message in bytes.

For each message that is republished, a set of [headers](https://docs.nats.io/nats-concepts/jetstream/headers) are automatically added.

**Note:** The `reply-subject` is being removed on republished messages, even if `no-ack` is set on the stream.

### SubjectTransform

If configured, the `SubjectTransform` will perform a subject transform to matching subjects of messages received by the stream and transform the subject, before storing it in the stream. The transform configuration specifies a `Source` and `Destination` field, following the rules of [subject transform](https://docs.nats.io/running-a-nats-service/configuration/configuring_subject_mapping).


# Source and Mirror Streams

When a stream is configured with a `source` or `mirror`, it will automatically and asynchronously replicate messages from the origin stream.

`source` or `mirror` are designed to be robust and will recover from a loss of connection. They are suitable for geographic distribution over high latency and unreliable connections. E.g. even a leaf node starting and connecting intermittently every few days will still receive or send messages over the source/mirror link.\
Another use case is when [connecting streams cross-account](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/accounts#exporting-and-importing).

There are several options available when declaring the configuration.

* `Name` - Name of the origin stream to source messages from.
* `StartSeq` - An optional start sequence of the origin stream to start mirroring from.
* `StartTime` - An optional message start time to start mirroring from. Any messages that are equal to or greater than the start time will be included.
* `FilterSubject` - An optional filter subject which will include only messages that match the subject, typically including a wildcard. Note, this cannot be used with `SubjectTransforms`.
* `SubjectTransforms` - An optional set of [subject transforms](https://docs.nats.io/running-a-nats-service/configuration/configuring_subject_mapping) to apply when sourcing messages from the origin stream. Note, in this context, the `Source` will act as a filter on the origin stream and the `Destination` can optionally be provided to apply a transform. Since multiple subject transforms can be used, disjoint subjects can be sourced from the origin stream while maintaining the order of the messages. Note, this cannot be used with `FilterSubject`.
* `Domain` - An optional JetStream domain of where the origin stream exists. This is commonly used in a hub cluster and leafnode topology.

The stream using a source or mirror configuration can have its own retention policy, replication, and storage type.

{% hint style="info" %}

* Changes to the stream using source or mirror, e.g. deleting messages or publishing, do not reflect back on the origin stream from which the data was received.
* Deletes in the origin stream are NOT replicated through a `source` or `mirror` agreement.
  {% endhint %}

{% hint style="info" %}
`Sources` is a generalization of the `Mirror` and allows for sourcing data from one or more streams concurrently.\
If you require the target stream to act as a read-only replica:

* Configure the stream without listen subjects **or**
* Temporarily disable the listen subjects through client authorizations.
  {% endhint %}

## General behavior

* All configurations are made on the receiving side. The stream from which data is sourced and mirrored does not need to be configured. No cleanup is required on the origin side if the receiver disappears.
* A stream can be the origin (source) for multiple streams. This is useful for geographic distribution or for designing "fan out" topologies where data needs to be distributed reliable to a large number (up to millions) of client connections.
* Leaf nodes and leaf node domains are explicitly supported through the `API prefix`

## Source specific

A stream defining `Sources` is a generalized replication mechanism and allows for sourcing data from **one or more streams** concurrently. A stream with sources can still act as a regular stream allowing direct write/publish by local clients to the stream. Essentially the source streams and local client writes are aggregated into a single interleaved stream.\
Combined with subject transformation and filtering sourcing allows to design sophisticated data distribution architectures.

{% hint style="info" %}
Sourcing messages does not retain sequence numbers. But it retain the in stream sequence of messages . Between streams sourced to the same target, the sequence of messages is undefined.
{% endhint %}

## Mirror specific

A mirror can source its messages from **exactly one stream** and a clients can not directly write to the mirror. Although messages cannot be published to a mirror directly by clients, messages can be deleted on-demand (beyond the retention policy), and consumers have all capabilities available on regular streams.

{% hint style="info" %}

* Mirrored messages retains the sequence numbers and timestamps of the origin stream.
* Mirrors can be used for for (geographic) load distribution with the `MirrorDirect` stream attribute. See: <https://docs.nats.io/nats-concepts/jetstream/streams#configuration>
  {% endhint %}

## Expected behavior in edge conditions

* Source and mirror contracts are designed with one-way (geographic) data replication in mind. Neither configuration provides a full synchronization between streams, which would include deletes or replication of other stream attributes.
* The content of the stream from which a source or mirror is drawn needs to be reasonable stable. Quickly deleting messages after publishing them may result in inconsistent replication due to the asynchronous nature of the replication process.
* Sources and Mirror try to be be efficient in replicating messages and are lenient towards the source/mirror origin being unreachable (event for extended periods of time), e.g. when using leaf nodes, which are connected intermittently. For sake of efficiency the recovery interval in case of a disconnect is 10-20s.
* Mirror and source agreements do not create a visible consumer in the origin stream.

### WorkQueue retention

Source and mirror works with origin stream with workqueue retention in a limited context. The source/mirror will act as a consumer removing messages from the origin stream.

The implementation is not resilient when connecting over intermittent leaf node connections though. Within a cluster where the target stream (with the source/mirror agreement) it will generally work well.

{% hint style="warning" %}
Source and mirror for workqueue based streams is only partially supported. It is not resilient against connection loss over leaf nodes.

The consumer pulling message from a remote stream is not durable and other clients may be able to consume and remove messages from the workqueue while leaf connection is down.
{% endhint %}

{% hint style="warning" %}
If you try to create additional (conflicting) consumers on the origin workqueue stream the behavior becomes undefined. A workqueue allows only one consumer per subject. If the source/mirror connection is active local clients trying to create additional consumers will fail. In reverse a source/mirror cannot be created when there is already a local consumer for the same subjects.
{% endhint %}

### Interest base retention

{% hint style="warning" %}
Source and mirror for interest based streams is not supported. Jetstream does not forbid this configuration but the behavior is undefined and may change in the future.
{% endhint %}


# Example

Streams with source and mirror configurations are best managed through a client API. If you intend to create such a configuration from command line with NATS CLI you should use a JSON configuration.

```
nats stream add --config stream_with_sources.json
```

## Example stream configuration with two sources

**Minimal example**

```
{
  "name": "SOURCE_TARGET",
  "subjects": [
    "foo1.ext.*",
    "foo2.ext.*"
  ],
  "discard": "old",
  "duplicate_window": 120000000000,
  "sources": [
    {
      "name": "SOURCE1_ORIGIN",
    },
  ],
  "deny_delete": false,
  "sealed": false,
  "max_msg_size": -1,
  "allow_rollup_hdrs": false,
  "max_bytes": -1,
  "storage": "file",
  "allow_direct": false,
  "max_age": 0,
  "max_consumers": -1,
  "max_msgs_per_subject": -1,
  "num_replicas": 1,
  "name": "SOURCE_TARGET",
  "deny_purge": false,
  "compression": "none",
  "max_msgs": -1,
  "retention": "limits",
  "mirror_direct": false
}
```

**With additional options**

```
{
  "name": "SOURCE_TARGET",
  "subjects": [
    "foo1.ext.*",
    "foo2.ext.*"
  ],
  "discard": "old",
  "duplicate_window": 120000000000,
  "sources": [
    {
      "name": "SOURCE1_ORIGIN",
      "filter_subject": "foo1.bar",
      "opt_start_seq": 42,
      "external": {
        "deliver": "",
        "api": "$JS.domainA.API"
      }
    },
    {
      "name": "SOURCE2_ORIGIN",
      "filter_subject": "foo2.bar"
    }
  ],
  "consumer_limits": {
    
  },
  "deny_delete": false,
  "sealed": false,
  "max_msg_size": -1,
  "allow_rollup_hdrs": false,
  "max_bytes": -1,
  "storage": "file",
  "allow_direct": false,
  "max_age": 0,
  "max_consumers": -1,
  "max_msgs_per_subject": -1,
  "num_replicas": 1,
  "name": "SOURCE_TARGET",
  "deny_purge": false,
  "compression": "none",
  "max_msgs": -1,
  "retention": "limits",
  "mirror_direct": false
}
```

## Example stream configuration with mirror

**Minimal example**

```
{
  "name": "MIRROR_TARGET"
  "discard": "old",
  "mirror": {
    "name": "MIRROR_ORIGIN"
  },
  "deny_delete": false,
  "sealed": false,
  "max_msg_size": -1,
  "allow_rollup_hdrs": false,
  "max_bytes": -1,
  "storage": "file",
  "allow_direct": false,
  "max_age": 0,
  "max_consumers": -1,
  "max_msgs_per_subject": -1,
  "num_replicas": 1,
  "name": "MIRROR_TARGET",
  "deny_purge": false,
  "compression": "none",
  "max_msgs": -1,
  "retention": "limits",
  "mirror_direct": false
}
```

**With additional options**

```
{
  "name": "MIRROR_TARGET"
  "discard": "old",
  "mirror": {
    "opt_start_time": "2024-07-11T08:57:20.4441646Z",
    "external": {
      "deliver": "",
      "api": "$JS.domainB.API"
    },
    "name": "MIRROR_ORIGIN"
  },
  "consumer_limits": {
    
  },
  "deny_delete": false,
  "sealed": false,
  "max_msg_size": -1,
  "allow_rollup_hdrs": false,
  "max_bytes": -1,
  "storage": "file",
  "allow_direct": false,
  "max_age": 0,
  "max_consumers": -1,
  "max_msgs_per_subject": -1,
  "num_replicas": 1,
  "name": "MIRROR_TARGET",
  "deny_purge": false,
  "compression": "none",
  "max_msgs": -1,
  "retention": "limits",
  "mirror_direct": false
}
```


# Consumers

A consumer is a stateful **view** of a stream. It acts as an interface for clients to *consume* a subset of messages stored in a stream and will keep track of which messages were delivered and acknowledged by clients.

Unlike [Core NATS](https://docs.nats.io/nats-concepts/core-nats), which provides an at most once delivery guarantee, a consumer in JetStream can provide an at least **once delivery** guarantee.

While **Streams** are responsible for storing the published messages, the consumer is responsible for tracking the delivery and acknowledgments. This tracking ensures that if a message is not acknowledged (un-acked or 'nacked'), the consumer will automatically attempt to re-deliver it. JetStream consumers support various acknowledgment types and policies. If a message is not acknowledged within a user-specified number of delivery attempts, an advisory notification is emitted.

## Dispatch type - Pull / Push

Consumers can be **push**-based where messages will be delivered to a specified subject or **pull**-based which allows clients to request batches of messages on demand. The choice of what kind of consumer to use depends on the use-case.

If there is a need to process messages in an application controlled manner and easily scale horizontally, you would use a 'pull consumer'. A simple client application that wants a replay of messages from a stream sequentially you would use an 'ordered push consumer'. An application that wants to benefit from load balancing or acknowledge messages individually will use a regular push consumer.

{% hint style="info" %}
We recommend pull consumers for new projects. In particular when scalability, detailed flow control or error handling are a concern.
{% endhint %}

### Ordered Consumers

Ordered consumers are the convenient default type of push & pull consumers designed for applications that want to efficiently consume a stream for data inspection or analysis.

* Always ephemeral
* No acknowledgements (if gap is detected, consumer is recreated)
* Automatic flow control/pull processing
* Single-threaded dispatching
* No load balancing

## Persistence - Durable / Ephemeral

In addition to the choice of being push or pull, a consumer can also be **ephemeral** or **durable**. A consumer is considered *durable* when an explicit name is set on the `Durable` field when creating the consumer, or when `InactiveThreshold` is set.

Durables and ephemeral have the same message delivery semantics but an ephemeral consumer will not have persisted state or fault tolerance (server memory only) and will be automatically *cleaned up* (deleted) after a period of inactivity, when no subscriptions are bound to the consumer.

By default, consumers will have the same replication factor as the stream they consume, and will remain even when there are periods of inactivity (unless `InactiveThreshold` is set explicitly). Consumers can recover from server and client failure.

{% embed url="<https://youtu.be/334XuMma1fk>" %}
NATS JS Consumers - The ONE feature that makes NATS more powerful than Kafka, Pulsar, RabbitMQ, & redis
{% endembed %}

## Configuration

Below are the set of consumer configuration options that can be defined. The `Version` column indicates the version of nats-server in which the option was introduced. The `Editable` column indicates the option can be edited after the consumer is created.

### General

| Field                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Version | Editable |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| Durable                           | If set, clients can have subscriptions bind to the consumer and *resume* until the consumer is explicitly deleted. A durable name cannot contain whitespace, `.`, `*`, `>`, path separators (forward or backward slash), or non-printable characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 2.2.0   | No       |
| [FilterSubject](#filtersubjects)  | A subject that overlaps with the subjects bound to the stream to filter delivery to subscribers. Note: This cannot be used with the `FilterSubjects` field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 2.2.0   | Yes      |
| [AckPolicy](#ackpolicy)           | The requirement of client acknowledgments, either `AckExplicit`, `AckNone`, or `AckAll`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 2.2.0   | No       |
| AckWait                           | The duration that the server will wait for an acknowledgment for any individual message *once it has been delivered to a consumer*. If an acknowledgment is not received in time, the message will be redelivered. This setting is only effective when `BackOff` is **not configured**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 2.2.0   | Yes      |
| [DeliverPolicy](#deliverpolicy)   | The point in the stream from which to receive messages: `DeliverAll`, `DeliverLast`, `DeliverNew`, `DeliverByStartSequence`, `DeliverByStartTime`, or `DeliverLastPerSubject`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 2.2.0   | No       |
| OptStartSeq                       | Used with the `DeliverByStartSequence` deliver policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 2.2.0   | No       |
| OptStartTime                      | Used with the `DeliverByStartTime` deliver policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2.2.0   | No       |
| Description                       | A description of the consumer. This can be particularly useful for ephemeral consumers to indicate their purpose since a durable name cannot be provided.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 2.3.3   | Yes      |
| InactiveThreshold                 | Duration that instructs the server to clean up consumers inactive for that long. Prior to 2.9, this only applied to ephemeral consumers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 2.2.0   | Yes      |
| [MaxAckPending](#maxackpending)   | Defines the maximum number of messages, without acknowledgment, that can be outstanding. Once this limit is reached, message delivery will be suspended. This limit applies across *all* of the consumer's bound subscriptions. A value of -1 means there can be any number of pending acknowledgments (i.e., no flow control). The default is 1000.                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2.2.0   | Yes      |
| MaxDeliver                        | The maximum number of times a specific message delivery will be attempted. Applies to any message that is re-sent due to acknowledgment policy (i.e., due to a negative acknowledgment or no acknowledgment sent by the client). The default is -1 (redeliver until acknowledged). Messages that have reached the maximum delivery count will stay in the stream.                                                                                                                                                                                                                                                                                                                                                                                                                           | 2.2.0   | Yes      |
| Backoff                           | A sequence of delays controlling the re-delivery of messages on acknowledgment timeout (but not on `nak`). The sequence length must be less than or equal to `MaxDeliver`. If backoff is not set, a timeout will result in immediate re-delivery. E.g., `MaxDeliver=5` `backoff=[5s, 30s, 300s, 3600s, 84000s]` will re-deliver a message 5 times over one day. When `MaxDeliver` is larger than the backoff list, the last delay in the list will apply for the remaining deliveries. Note that backoff is NOT applied to `nak`ed messages. A `nak` will result in immediate re-delivery unless `nakWithDelay` is used to set the re-delivery delay explicitly. When `BackOff` is set, it **overrides `AckWait` entirely**. The first value in the BackOff determines the `AckWait` value. | 2.7.1   | Yes      |
| ReplayPolicy                      | If the policy is `ReplayOriginal`, the messages in the stream will be pushed to the client at the same rate they were originally received, simulating the original timing. If the policy is `ReplayInstant` (default), the messages will be pushed to the client as fast as possible while adhering to the acknowledgment policy, Max Ack Pending, and the client's ability to consume those messages.                                                                                                                                                                                                                                                                                                                                                                                      | 2.2.0   | No       |
| Replicas                          | Sets the number of replicas for the consumer's state. By default, when the value is set to zero, consumers inherit the number of replicas from the stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 2.8.3   | Yes      |
| MemoryStorage                     | If set, forces the consumer state to be kept in memory rather than inherit the storage type of the stream (default is file storage). This reduces I/O from acknowledgments, useful for ephemeral consumers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 2.8.3   | No       |
| SampleFrequency                   | Sets the percentage of acknowledgments that should be sampled for observability, 0-100. This value is a string and allows both `30` and `30%` as valid values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 2.2.0   | Yes      |
| Metadata                          | A set of application-defined key-value pairs for associating metadata with the consumer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 2.10.0  | Yes      |
| [FilterSubjects](#filtersubjects) | A set of subjects that overlap with the subjects bound to the stream to filter delivery to subscribers. Note: This cannot be used with the `FilterSubject` field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2.10.0  | Yes      |
| HeadersOnly                       | Delivers only the headers of messages in the stream, adding a `Nats-Msg-Size` header indicating the size of the removed payload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 2.6.2   | Yes      |

#### AckPolicy

The policy choices include:

* `AckExplicit`: The default policy. Each individual message must be acknowledged. Recommended for most reliability and functionality.
* `AckNone`: No acknowledgment needed; the server assumes acknowledgment on delivery.
* `AckAll`: Acknowledge only the last message received in a series; all previous messages are automatically acknowledged. Will acknowledge all pending messages for all subscribers for Pull Consumer.

If an acknowledgment is required but not received within the `AckWait` window, the message will be redelivered.

> **Warning**: The server may consider an acknowledgment arriving out of the window. For instance, in a queue situation, if a first process fails to acknowledge within the window and the message has been redelivered to another consumer, the acknowledgment from the first consumer will be considered.

#### DeliverPolicy

The policy choices include:

* `DeliverAll`: Default policy. Start receiving from the earliest available message in the stream.
* `DeliverLast`: Start with the last message added to the stream, or the last message matching the consumer's filter subject if defined.
* `DeliverLastPerSubject`: Start with the latest message for each filtered subject currently in the stream.
* `DeliverNew`: Start receiving messages created after the consumer was created.
* `DeliverByStartSequence`: Start at the first message with the specified sequence number. The consumer must specify `OptStartSeq` defining the sequence number.
* `DeliverByStartTime`: Start with messages on or after the specified time. The consumer must specify `OptStartTime` defining the start time.

#### MaxAckPending

The `MaxAckPending` capability provides flow control and applies to both push and pull consumers. For push consumers, `MaxAckPending` is the only form of flow control. For pull consumers, client-driven message delivery creates implicit one-to-one flow control with subscribers.

For high throughput, set `MaxAckPending` to a high value. For applications with high latency due to external services, use a lower value and adjust `AckWait` to avoid re-deliveries.

#### FilterSubjects

A filter subject provides server-side filtering of messages before delivery to clients.

For example, a stream `factory-events` with subject `factory-events.*.*` can have a consumer `factory-A` with a filter `factory-events.A.*` to deliver only events for factory `A`.

A consumer can have a singular `FilterSubject` or plural `FilterSubjects`. Multiple filters can be applied, such as `[factory-events.A.*, factory-events.B.*]` or specific event types `[factory-events.*.item_produced, factory-events.*.item_packaged]`.

> **Warning**: For granular consumer permissions, a single filter uses `$JS.API.CONSUMER.CREATE.{stream}.{consumer}.{filter}` to restrict users to specific filters. Multiple filters use the general `$JS.API.CONSUMER.DURABLE.CREATE.{stream}.{consumer}`, which does not include the `{filter}` token. Use a different strategy for granular permissions.

### Pull-specific

These options apply only to pull consumers. For configuration examples, see [NATS by Example](https://natsbyexample.com/examples/jetstream/pull-consumer/go).

| Field              | Description                                                                                                                                                          | Version | Editable |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| MaxWaiting         | The maximum number of waiting pull requests.                                                                                                                         | 2.2.0   | No       |
| MaxRequestExpires  | The maximum duration a single pull request will wait for messages to be available to pull.                                                                           | 2.7.0   | Yes      |
| MaxRequestBatch    | The maximum batch size a single pull request can make. When set with `MaxRequestMaxBytes`, the batch size will be constrained by whichever limit is hit first.       | 2.7.0   | Yes      |
| MaxRequestMaxBytes | The maximum total bytes that can be requested in a given batch. When set with `MaxRequestBatch`, the batch size will be constrained by whichever limit is hit first. | 2.8.3   | Yes      |

### Push-specific

These options apply only to push consumers. For configuration examples, see [NATS by Example](https://natsbyexample.com/examples/jetstream/push-consumer/go).

| Field          | Description                                                                                                                                                                                                                                                                                                                                                                 | Version | Editable |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| DeliverSubject | The subject to deliver messages to. Setting this field decides whether the consumer is push or pull-based. With a deliver subject, the server will *push* messages to clients subscribed to this subject.                                                                                                                                                                   | 2.2.0   | No       |
| DeliverGroup   | The queue group name used to distribute messages among subscribers. Analogous to a [queue group](https://docs.nats.io/nats-concepts/core-nats/queue) in core NATS.                                                                                                                                                                                                          | 2.2.0   | Yes      |
| FlowControl    | Enables per-subscription flow control using a sliding-window protocol. This protocol relies on the server and client exchanging messages to regulate when and how many messages are pushed to the client. This one-to-one flow control mechanism works in tandem with the one-to-many flow control imposed by `MaxAckPending` across all subscriptions bound to a consumer. | 2.2.0   | Yes      |
| IdleHeartbeat  | If set, the server will regularly send a status message to the client during inactivity, indicating that the JetStream service is up and running. The status message will have a code of 100 and no reply address. Note: This mechanism is handled transparently by supported clients.                                                                                      | 2.2.0   | Yes      |
| RateLimit      | Throttles the delivery of messages to the consumer, in bits per second.                                                                                                                                                                                                                                                                                                     | 2.2.0   | Yes      |

***


# Example

Consider this architecture

![Orders](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-dedcc17f082fa1e39497c54ed8191b6424ee7792%2Fstreams-and-consumers-75p.png?alt=media\&token=3dc2026b-8ef1-4f5b-a844-b3dbce6abbd9)

While it is an incomplete architecture it does show a number of key points:

* Many related subjects are stored in a Stream
* Consumers can have different modes of operation and receive just subsets of the messages
* Multiple Acknowledgement modes are supported

A new order arrives on `ORDERS.received`, gets sent to the `NEW` Consumer who, on success, will create a new message on `ORDERS.processed`. The `ORDERS.processed` message again enters the Stream where a `DISPATCH` Consumer receives it and once processed it will create an `ORDERS.completed` message which will again enter the Stream. These operations are all `pull` based meaning they are work queues and can scale horizontally. All require acknowledged delivery ensuring no order is missed.

All messages are delivered to a `MONITOR` Consumer without any acknowledgement and using Pub/Sub semantics - they are pushed to the monitor.

As messages are acknowledged to the `NEW` and `DISPATCH` Consumers, a percentage of them are Sampled and messages indicating redelivery counts, ack delays and more, are delivered to the monitoring system.

## Example Configuration

[Additional documentation](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/administration) introduces the `nats` utility and how you can use it to create, monitor, and manage streams and consumers, but for completeness and reference this is how you'd create the ORDERS scenario. We'll configure a 1 year retention for order related messages:

```bash
nats stream add ORDERS --subjects "ORDERS.*" --ack --max-msgs=-1 --max-bytes=-1 --max-age=1y --storage file --retention limits --max-msg-size=-1 --discard=old
nats consumer add ORDERS NEW --filter ORDERS.received --ack explicit --pull --deliver all --max-deliver=-1 --sample 100
nats consumer add ORDERS DISPATCH --filter ORDERS.processed --ack explicit --pull --deliver all --max-deliver=-1 --sample 100
nats consumer add ORDERS MONITOR --filter '' --ack none --target monitor.ORDERS --deliver last --replay instant
```


# JetStream Walkthrough

The following is a small walkthrough on creating a stream and a consumer and interacting with the stream using the [nats cli](https://github.com/nats-io/natscli).

## Prerequisite: enabling JetStream

If you are running a local `nats-server` stop it and restart it with JetStream enabled using `nats-server -js` (if that's not already done)

You can then check that JetStream is enabled by using

```shell
nats account info
```

```
Account Information

                           User: 
                        Account: $G
                        Expires: never
                      Client ID: 5
                      Client IP: 127.0.0.1
                            RTT: 128µs
              Headers Supported: true
                Maximum Payload: 1.0 MiB
                  Connected URL: nats://127.0.0.1:4222
              Connected Address: 127.0.0.1:4222
            Connected Server ID: NAMR7YBNZA3U2MXG2JH3FNGKBDVBG2QTMWVO6OT7XUSKRINKTRFBRZEC
       Connected Server Version: 2.11.0-dev
                 TLS Connection: no

JetStream Account Information:

Account Usage:

                        Storage: 0 B
                         Memory: 0 B
                        Streams: 0
                      Consumers: 0

Account Limits:

            Max Message Payload: 1.0 MiB

  Tier: Default:

      Configuration Requirements:

        Stream Requires Max Bytes Set: false
         Consumer Maximum Ack Pending: Unlimited

      Stream Resource Usage Limits:

                               Memory: 0 B of Unlimited
                    Memory Per Stream: Unlimited
                              Storage: 0 B of Unlimited
                   Storage Per Stream: Unlimited
                              Streams: 0 of Unlimited
                            Consumers: 0 of Unlimited
```

If you see the below then JetStream is *not* enabled

```
JetStream Account Information:

   JetStream is not supported in this account
```

## 1. Creating a stream

Let's start by creating a stream to capture and store the messages published on the subject "foo".

Enter `nats stream add <Stream name>` (in the examples below we will name the stream "my\_stream"), then enter "foo" as the subject name and hit return to use the defaults for all the other stream attributes:

```shell
nats stream add my_stream
```

```
? Subjects foo
? Storage file
? Replication 1
? Retention Policy Limits
? Discard Policy Old
? Stream Messages Limit -1
? Per Subject Messages Limit -1
? Total Stream Size -1
? Message TTL -1
? Max Message Size -1
? Duplicate tracking time window 2m0s
? Allow message Roll-ups No
? Allow message deletion Yes
? Allow purging subjects or the entire stream Yes
Stream my_stream was created

Information for Stream my_stream created 2024-06-07 12:29:36

              Subjects: foo
              Replicas: 1
               Storage: File

Options:

             Retention: Limits
       Acknowledgments: true
        Discard Policy: Old
      Duplicate Window: 2m0s
            Direct Get: true
     Allows Msg Delete: true
          Allows Purge: true
        Allows Rollups: false

Limits:

      Maximum Messages: unlimited
   Maximum Per Subject: unlimited
         Maximum Bytes: unlimited
           Maximum Age: unlimited
  Maximum Message Size: unlimited
     Maximum Consumers: unlimited

State:

              Messages: 0
                 Bytes: 0 B
        First Sequence: 0
         Last Sequence: 0
      Active Consumers: 0
```

You can then check the information about the stream you just created:

```shell
nats stream info my_stream
```

```
Information for Stream my_stream created 2024-06-07 12:29:36

              Subjects: foo
              Replicas: 1
               Storage: File

Options:

             Retention: Limits
       Acknowledgments: true
        Discard Policy: Old
      Duplicate Window: 2m0s
            Direct Get: true
     Allows Msg Delete: true
          Allows Purge: true
        Allows Rollups: false

Limits:

      Maximum Messages: unlimited
   Maximum Per Subject: unlimited
         Maximum Bytes: unlimited
           Maximum Age: unlimited
  Maximum Message Size: unlimited
     Maximum Consumers: unlimited

State:

              Messages: 0
                 Bytes: 0 B
        First Sequence: 0
         Last Sequence: 0
      Active Consumers: 0
```

## 2. Publish some messages into the stream

Let's now start a publisher

```shell
nats pub foo --count=1000 --sleep 1s "publication #{{.Count}} @ {{.TimeStamp}}"
```

As messages are being published on the subject "foo" they are also captured and stored in the stream, you can check that by using `nats stream info my_stream` and even look at the messages themselves using `nats stream view my_stream` or `nats stream get my_stream`

## 3. Creating a consumer

Now at this point if you create a 'Core NATS' (i.e. non-streaming) subscriber to listen for messages on the subject 'foo', you will *only* receive the messages being published after the subscriber was started, this is normal and expected for the basic 'Core NATS' messaging. In order to receive a 'replay' of all the messages contained in the stream (including those that were published in the past) we will now create a 'consumer'

We can administratively create a consumer using the 'nats consumer add ' command, in this example we will name the consumer "pull\_consumer", and we will leave the delivery subject to 'nothing' (i.e. just hit return at the prompt) because we are creating a 'pull consumer' and select `all` for the start policy, you can then just use the defaults and hit return for all the other prompts. The stream the consumer is created on should be the stream 'my\_stream' we just created above.

```shell
nats consumer add
```

```
? Consumer name pull_consumer
? Delivery target (empty for Pull Consumers) 
? Start policy (all, new, last, subject, 1h, msg sequence) all
? Acknowledgment policy explicit
? Replay policy instant
? Filter Stream by subjects (blank for all) 
? Maximum Allowed Deliveries -1
? Maximum Acknowledgments Pending 0
? Deliver headers only without bodies No
? Add a Retry Backoff Policy No
? Select a Stream my_stream
Information for Consumer my_stream > pull_consumer created 2024-06-07T12:32:09-05:00

Configuration:

                    Name: pull_consumer
               Pull Mode: true
          Deliver Policy: All
              Ack Policy: Explicit
                Ack Wait: 30.00s
           Replay Policy: Instant
         Max Ack Pending: 1,000
       Max Waiting Pulls: 512

State:

  Last Delivered Message: Consumer sequence: 0 Stream sequence: 0
    Acknowledgment Floor: Consumer sequence: 0 Stream sequence: 0
        Outstanding Acks: 0 out of maximum 1,000
    Redelivered Messages: 0
    Unprocessed Messages: 74
           Waiting Pulls: 0 of maximum 512
```

You can check on the status of any consumer at any time using `nats consumer info` or view the messages in the stream using `nats stream view my_stream` or `nats stream get my_stream`, or even remove individual messages from the stream using `nats stream rmm`

## 3. Subscribing from the consumer

Now that the consumer has been created and since there are messages in the stream we can now start subscribing to the consumer:

```shell
nats consumer next my_stream pull_consumer --count 1000
```

This will print out all the messages in the stream starting with the first message (which was published in the past) and continuing with new messages as they are published until the count is reached.

Note that in this example we are creating a pull consumer with a 'durable' name, this means that the consumer can be shared between as many consuming processes as you want. For example instead of running a single `nats consumer next` with a count of 1000 messages you could have started two instances of `nats consumer` each with a message count of 500 and you would see the consumption of the messages from the consumer distributed between those instances of `nats`

#### Replaying the messages again

Once you have iterated over all the messages in the stream with the consumer, you can get them again by simply creating a new consumer or by deleting that consumer (`nats consumer rm`) and re-creating it (`nats consumer add`).

## 4. Cleaning up

You can clean up a stream (and release the resources associated with it (e.g. the messages stored in the stream)) using `nats stream purge`

You can also delete a stream (which will also automatically delete all of the consumers that may be defined on that stream) using `nats stream rm`


# Key/Value Store

JetStream, the persistence layer of NATS, not only allows for the higher qualities of service and features associated with 'streaming', but it also enables some functionalities not found in messaging systems.

One such feature is the Key/Value store functionality, which allows client applications to create `buckets` and use them as immediately (as opposed to eventually) consistent, persistent [associative arrays](https://en.wikipedia.org/wiki/Associative_array) (or maps). Note that this is an abstraction on top of the Stream functionality. Buckets are materialized as Streams (with a name starting with `KV_`), everything you can do with a bucket you can do with a Stream, but you ultimately have more functionality and flexibility and control when using the Stream functionality directly.

Do note, while we do guarantee immediate consistency when it comes to [monotonic writes](https://jepsen.io/consistency/models/monotonic-writes) and [monotonic reads](https://jepsen.io/consistency/models/monotonic-reads). We don't guarantee [read your writes](https://jepsen.io/consistency/models/read-your-writes) at this time, as reads through *direct get* requests may be served by followers or mirrors. More consistent results can be achieved by sending get requests to the underlying stream leader of the Key/Value store.

* [Walkthrough](https://docs.nats.io/nats-concepts/jetstream/key-value-store/kv_walkthrough)
* [Details](https://docs.nats.io/using-nats/developer/develop_jetstream/kv)

## Managing a Key Value store

1. Create a bucket, which corresponds to a stream in the underlying storage. Define KV/Stream limits as appropriate
2. Use the operation below.

## Map style operations

You can use KV buckets to perform the typical operations you would expect from an immediately consistent key/value store:

* put: associate a value with a key
* get: retrieve the value associated with a key
* delete: clear any value associated with a key
* purge: clear all the values associated with all keys
* keys: get a copy of all of the keys (with a value or operation associated with it)

## Atomic operations used for locking and concurrency control

* create: associate the value with a key only if there is currently no value associated with that key (i.e. compare to null and set)
* update: compare and set (aka compare and swap) the value for a key

## Limiting size, TTL etc.

You can set limits for your buckets, such as:

* the maximum size of the bucket
* the maximum size for any single value
* a TTL: how long the store will keep values for

## Treating the Key Value store as a message stream

Finally, you can even do things that typically can not be done with a Key/Value Store:

* watch: watch for changes happening for a key, which is similar to subscribing (in the publish/subscribe sense) to the key: the watcher receives updates due to put or delete operations on the key pushed to it in real-time as they happen
* watch all: watch for all the changes happening on all the keys in the bucket
* history: retrieve a history of the values (and delete operations) associated with each key over time (by default the history of buckets is set to 1, meaning that only the latest value/operation is stored)

## Notes

A valid key can contain the following characters: `a-z`, `A-Z`, `0-9`, `_`, `-`, `.`, `=` and `/`, i.e. it can be a dot-separated list of tokens (which means that you can then use wildcards to match hierarchies of keys when watching a bucket). The value can be any byte array.


# Key/Value Store Walkthrough

The Key/Value Store is a JetStream feature, so we need to verify it is enabled by

```shell
nats account info
```

which may return

```
JetStream Account Information:

   JetStream is not supported in this account
```

In this case, you should enable JetStream.

## Prerequisite: enabling JetStream

If you are running a local `nats-server` stop it and restart it with JetStream enabled using `nats-server -js` (if that's not already done)

You can then check that JetStream is enabled by using

```shell
nats account info
```

```
Connection Information:

               Client ID: 6
               Client IP: 127.0.0.1
                     RTT: 64.996µs
       Headers Supported: true
         Maximum Payload: 1.0 MiB
           Connected URL: nats://127.0.0.1:4222
       Connected Address: 127.0.0.1:4222
     Connected Server ID: ND2XVDA4Q363JOIFKJTPZW3ZKZCANH7NJI4EJMFSSPTRXDBFG4M4C34K

JetStream Account Information:

           Memory: 0 B of Unlimited
          Storage: 0 B of Unlimited
          Streams: 0 of Unlimited
        Consumers: 0 of Unlimited 
```

## Creating a KV bucket

A 'KV bucket' is like a stream; you need to create it before using it, as in `nats kv add <KV Bucket Name>`:

```shell
nats kv add my-kv
```

```
my_kv Key-Value Store Status

         Bucket Name: my-kv
         History Kept: 1
        Values Stored: 0
           Compressed: false
   Backing Store Kind: JetStream
          Bucket Size: 0 B
  Maximum Bucket Size: unlimited
   Maximum Value Size: unlimited
          Maximum Age: unlimited
     JetStream Stream: KV_my-kv
              Storage: File
```

## Storing a value

Now that we have a bucket, we can assign, or 'put', a value to a specific key:

```shell
nats kv put my-kv Key1 Value1
```

which should return the key's value `Value1`

## Getting a value

We can fetch, or 'get', the value for a key "Key1":

```shell
nats kv get my-kv Key1
```

```
my-kv > Key1 created @ 12 Oct 21 20:08 UTC

Value1
```

## Deleting a value

You can always delete a key and its value by using

```shell
nats kv del my-kv Key1
```

It is harmless to delete a non-existent key (check this!!).

## Atomic operations

K/V Stores can also be used in concurrent design patterns, such as semaphores, by using atomic 'create' and 'update' operations.

E.g. a client wanting exclusive use of a file can lock it by creating a key, whose value is the file name, with `create` and deleting this key after completing use of that file. A client can increase the reslience against failure by using a timeout for the `bucket` containing this key. The client can use `update` with a revision number to keep the `bucket` alive.

Updates can also be used for more fine-grained concurrency control, sometimes known as `optimistic locking`, where multiple clients can try a task, but only one can successfully complete it.

### Create (aka exclusive locking)

Create a lock/semaphore with the `create` operation.

```shell
nats kv create my-sem Semaphore1 Value1
```

Only one `create` can succeed. First come, first serve. All concurrent attempts will result in an error until the key is deleted

```shell
nats kv create my-sem Semaphore1 Value1
nats: error: nats: wrong last sequence: 1: key exists
```

### Update with CAS (aka optimistic locking)

We can also atomically `update`, sometimes known as a CAS (compare and swap) operation, a key with an additional parameter `revision`

```shell
nats kv update my-sem Semaphore1 Value2 13
```

A second attempt with the same revision 13, will fail

```shell
nats kv update my-sem Semaphore1 Value2 13
nats: error: nats: wrong last sequence: 14
```

## Watching a K/V Store

An unusual functionality of a K/V Store is being able to 'watch' a bucket, or a specific key in that bucket, and receive real-time updates to changes in the store.

For the example above, run `nats kv watch my-kv`. This will start a watcher on the bucket we have just created earlier. By default, the KV bucket has a history size of one, and so it only remembers the last change. In our case, the watcher should see a delete of the value associated with the key "Key1":

```shell
nats kv watch my-kv
```

```
[2021-10-12 13:15:03] DEL my-kv > Key1
```

If we now concurrently change the value of 'my-kv' by

```shell
nats kv put my-kv Key1 Value2
```

The watcher will see that change:

```shell
[2021-10-12 13:25:14] PUT my-kv > Key1: Value2
```

## Cleaning up

When you are finished using a bucket, you can delete the bucket, and its resources, by using the `rm` operator:

```shell
nats kv rm my-kv
```


# Object Store

JetStream, the persistence layer of NATS, not only allows for the higher qualities of service and features associated with 'streaming', but it also enables some functionalities not found in messaging systems.

One such feature is the Object store functionality, which allows client applications to create `buckets` (corresponding to streams) that can store a set of files. Files are stored and transmitted in chunks, allowing files of arbitrary size to be transferred safely over the NATS infrastructure.

**Note:** Object store is not a distributed storage system. All files in a bucket will need to fit on the target file system.

* [Walkthrough](https://docs.nats.io/nats-concepts/jetstream/obj_store/obj_walkthrough)
* [Details](https://docs.nats.io/using-nats/developer/develop_jetstream/object)

## Basic Capabilities

The Object Store implements a chunking mechanism, allowing you to for example store and retrieve files (i.e. the object) of any size by associating them with a path or file name as the key.

* `add` a `bucket` to hold the files.
* `put` Add a file to the bucket
* `get` Retrieve the file and store it to a designated location
* `del` Delete a file

## Advanced Capabilities

* `watch` Subscribe to changes in the bucket. Will receive notifications on successful `put` and `del` operations.


# Object Store Walkthrough

If you are running a local `nats-server` stop it and restart it with JetStream enabled using `nats-server -js` (if that's not already done)

You can then check that JetStream is enabled by using

```shell
nats account info
```

Which should output something like:

```
Connection Information:

               Client ID: 6
               Client IP: 127.0.0.1
                     RTT: 64.996µs
       Headers Supported: true
         Maximum Payload: 1.0 MiB
           Connected URL: nats://127.0.0.1:4222
       Connected Address: 127.0.0.1:4222
     Connected Server ID: ND2XVDA4Q363JOIFKJTPZW3ZKZCANH7NJI4EJMFSSPTRXDBFG4M4C34K

JetStream Account Information:

           Memory: 0 B of Unlimited
          Storage: 0 B of Unlimited
          Streams: 0 of Unlimited
        Consumers: 0 of Unlimited
```

If you see the below instead then JetStream is *not* enabled

```
JetStream Account Information:

   JetStream is not supported in this account
```

## Creating an Object Store bucket

Just like you need to create streams before you can use them you need to first create an Object Store bucket

```shell
nats object add myobjbucket
```

which outputs

```
myobjbucket Object Store Status

         Bucket Name: myobjbucket
            Replicas: 1
                 TTL: unlimitd
              Sealed: false
                Size: 0 B
  Backing Store Kind: JetStream
    JetStream Stream: OBJ_myobjbucket
```

## Putting a file in the bucket

```shell
nats object put myobjbucket ~/Movies/NATS-logo.mov
```

```
1.5 GiB / 1.5 GiB [====================================================================================]

Object information for myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov

               Size: 1.5 GiB
  Modification Time: 14 Apr 22 00:34 +0000
             Chunks: 12,656
             Digest: sha-256 8ee0679dd1462de393d81a3032d71f43d2bc89c0c8a557687cfe2787e926
```

## Putting a file in the bucket by providing a name

By default the full file path is used as a key. Provide the key explicitly (e.g. a relative path ) with `--name`

```shell
nats object put --name /Movies/NATS-logo.mov myobjbucket ~/Movies/NATS-logo.mov
```

```
1.5 GiB / 1.5 GiB [====================================================================================]

Object information for myobjbucket > /Movies/NATS-logo.mov

               Size: 1.5 GiB
  Modification Time: 14 Apr 22 00:34 +0000
             Chunks: 12,656
             Digest: sha-256 8ee0679dd1462de393d81a3032d71f43d2bc89c0c8a557687cfe2787e926
```

## Listing the objects in a bucket

```shell
nats object ls myobjbucket
```

```
╭───────────────────────────────────────────────────────────────────────────╮
│                              Bucket Contents                              │
├─────────────────────────────────────┬─────────┬───────────────────────────┤
│ Name                                │ Size    │ Time                      │
├─────────────────────────────────────┼─────────┼───────────────────────────┤
│ /Users/jnmoyne/Movies/NATS-logo.mov │ 1.5 GiB │ 2022-04-13T17:34:55-07:00 │
│ /Movies/NATS-logo.mov               │ 1.5 GiB │ 2022-04-13T17:35:41-07:00 │
╰─────────────────────────────────────┴─────────┴───────────────────────────╯
```

## Getting an object from the bucket

```shell
nats object get myobjbucket ~/Movies/NATS-logo.mov
```

```
1.5 GiB / 1.5 GiB [====================================================================================]

Wrote: 1.5 GiB to /Users/jnmoyne/NATS-logo.mov in 5.68s average 279 MiB/s
```

## Getting an object from the bucket with a specific output path

By default, the file will be stored relative to the local path under its name (not the full path). To specify an output path use `--output`

```shell
nats object get myobjbucket --output /temp/Movies/NATS-logo.mov /Movies/NATS-logo.mov
```

```
1.5 GiB / 1.5 GiB [====================================================================================]

Wrote: 1.5 GiB to /temp/Movies/NATS-logo.mov in 5.68s average 279 MiB/s
```

## Removing an object from the bucket

```shell
nats object rm myobjbucket ~/Movies/NATS-logo.mov
```

```
? Delete 1.5 GiB byte file myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov? Yes
Removed myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov
myobjbucket Object Store Status

         Bucket Name: myobjbucket
            Replicas: 1
                 TTL: unlimitd
              Sealed: false
                Size: 16 MiB
  Backing Store Kind: JetStream
    JetStream Stream: OBJ_myobjbucket
```

## Getting information about the bucket

```shell
nats object info myobjbucket
```

```
myobjbucket Object Store Status

         Bucket Name: myobjbucket
            Replicas: 1
                 TTL: unlimitd
              Sealed: false
                Size: 1.6 GiB
  Backing Store Kind: JetStream
    JetStream Stream: OBJ_myobjbucket
```

## Watching for changes to a bucket

```shell
nats object watch myobjbucket
```

```
[2022-04-13 17:51:28] PUT myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov: 1.5 GiB bytes in 12,656 chunks
[2022-04-13 17:53:27] DEL myobjbucket > /Users/jnmoyne/Movies/NATS-logo.mov
```

### Sealing a bucket

You can seal a bucket, meaning that no further changes are allowed on that bucket

```shell
nats object seal myobjbucket
```

```
? Really seal Bucket myobjbucket, sealed buckets can not be unsealed or modified Yes
myobjbucket has been sealed
myobjbucket Object Store Status

         Bucket Name: myobjbucket
            Replicas: 1
                 TTL: unlimitd
              Sealed: true
                Size: 1.6 GiB
  Backing Store Kind: JetStream
    JetStream Stream: OBJ_myobjbucket
```

## Deleting a bucket

Using `nats object rm myobjbucket` will delete the bucket and all the files stored in it.


# Headers

Message headers are used in a variety of JetStream contexts, such de-duplication, auto-purging of messages, metadata from republished messages, and more.

`Nats-` is a reserved namespace. Please use a different prefix for your own headers. This list may not be complete. Additional headers may be used for API internal messages or messages used for monitoring and control.

## Publish

Headers that can be set by a client when a message being published. These headers are recognized by the server.

| Name                                          | Description                                                                                                                                                                                                       | Example                                                                                                                                                           | Version |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `Nats-Msg-Id`                                 | Client-defined unique identifier for a message that will be used by the server apply de-duplication within the configured `Duplicate Window`.                                                                     | `9f01ccf0-8c34-4789-8688-231a2538a98b`                                                                                                                            | 2.2.0   |
| `Nats-Expected-Stream`                        | Used to assert the published message is received by some expected stream.                                                                                                                                         | `my-stream`                                                                                                                                                       | 2.2.0   |
| `Nats-Expected-Last-Msg-Id`                   | Used to apply optimistic concurrency control at the stream-level. The value is the last expected `Nats-Msg-Id` and the server will reject a publish if the current ID does not match.                             | `9f01ccf0-8c34-4789-8688-231a2538a98b`                                                                                                                            | 2.2.0   |
| `Nats-Expected-Last-Sequence`                 | Used to apply optimistic concurrency control at the stream-level. The value is the last expected sequence and the server will reject a publish if the current sequence does not match.                            | `328`                                                                                                                                                             | 2.2.0   |
| `Nats-Expected-Last-Subject-Sequence`         | Used to apply optimistic concurrency control at the subject-level. The value is the last expected sequence and the server will reject a publish if the current sequence does not match for the message's subject. | `38`                                                                                                                                                              | 2.3.1   |
| `Nats-Expected-Last-Subject-Sequence-Subject` | A subject which may include wildcards. Used with `Nats-Expected-Last-Subject-Sequence`. Server will enforce last sequence against the given subject rather than the one being published.                          | `events.orders.1.>`                                                                                                                                               | 2.11.0  |
| `Nats-Rollup`                                 | Used to apply a purge of all prior messages in a stream or at the subject-level. The `rollup message` will stay in the stream. Requires the allow rollups to be set on the stream.                                | `all` purges the full stream, `sub` purges the subject on which this messages was sent. Wildcards subjects are not allowed and will result in undefined behavior. | 2.6.2   |
| `Nats-TTL`                                    | Used to set a per message TTL. Requires the per message ttl flag to be set on the stream.                                                                                                                         | `1h`, `10s` (go duration string format)                                                                                                                           | 2.11    |

## RePublish or direct get

When messages are being re-published (must be configured in stream settings) from a stream or retrieved with a direct get operation from stream these headers are being set.

Do not set these headers on client published messages.

| Name                 | Description                                                                                                                                                                                                                                                           | Example                       | Version |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------- |
| `Nats-Stream`        | Name of the stream the message was republished from.                                                                                                                                                                                                                  | `Nats-Stream: my-stream`      | 2.8.3   |
| `Nats-Subject`       | The original subject of the message.                                                                                                                                                                                                                                  | `events.mouse_clicked`        | 2.8.3   |
| `Nats-Sequence`      | The original sequence of the message.                                                                                                                                                                                                                                 | `193`                         | 2.8.3   |
| `Nats-Last-Sequence` | The last sequence of the message having the same subject, otherwise zero if this is the first message for the subject.                                                                                                                                                | `190`                         | 2.8.3   |
| `Nats-Time-Stamp`    | The original timestamp of the message.                                                                                                                                                                                                                                | `2023-08-23T19:53:05.762416Z` | 2.10.0  |
| `Nats-Num-Pending`   | Number of messages pending in the multi/batched get response. or details see: [ADR-31](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-31.md)                                                                                               | `5`                           | 2.10.0  |
| `Nats-UpTo-Sequence` | On the last messages of multi/batched get response. The `up-to-seq` value of the original request. Helps the client to continue incomplete batch requests. For details see: [ADR-31](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-31.md) |                               | 2.11.0  |

## Sources

Headers that are implicitly added to messages sourced from other streams.

The format of the header content may change in the future. Please parse conservatively and assume that additional fields may be added or that older nats-server version have fewer fields.

| Name                 | Description                                                                                                                                                                                                                                                | Example                                   | Version |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------- |
| `Nats-Stream-Source` | <p>Contains space delimited:<br>- Origin stream name (disambiguated with domain hash if cross domain sourced)<br>- The original sequence number<br>- The list of subject filters<br>- The list of destination transforms<br>- The original subject<br></p> | `ORDERS:vSF0ECo6 17 foo.* bar.$1 foo.abc` | 2.2.0   |

## Tracing

When tracing is activated every subsystem that touches a message will produce Trace Events. These Events are aggregated per server and published to a destination subject.

Note that two variants exist. `traceparent` as per the trace context standard and ad hoc tracing through `Nats-Trace-Dest`.

Introduced in version 2.11 - see [ADR-41](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-41.md)

| Name                        | Description                                                                                                                                                                               | Example            | Version |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------- |
| `traceparent`               | Triggers tracing as per the <https://www.w3.org/TR/trace-context/> standard. Requires the `msg-trace` section to be configured on the account level.                                      | N/A                | 2.11    |
| `Nats-Trace-Dest`           | The subject that will receive the Trace messages                                                                                                                                          | trace.receiver.all | 2.11    |
| `Nats-Trace-Only`           | Optional. Defaults to `false`. Set to `true` to skip message delivery. If true only traces will be produced, but the messages is not sent to a subscribing client or stored in JetStream. | `true`             | 2.11    |
| `Accept-Encoding`           | Optional. Enables compression of the payload of the trace messages.                                                                                                                       | `gzip`, `snappy`   | 2.11    |
| `Nats-Trace-Hop`            | Internal. **Do not set**. Set by the server to count hops.                                                                                                                                | `<hop count>`      | 2.11    |
| `Nats-Trace-Origin-Account` | Internal. **Do not set**. Set by the server when an account boundary is crossed                                                                                                           | `<account name>`   | 2.11    |

## Scheduler

Message scheduling in streams. Needs to be enabled on the stream with "allow schedules" flag.

Introduced in version 2.11 - see [ADR-51](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-51.md)

| Name                      | Description                                                                                                                                                                                                     | Example                                                                          | Version |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------- |
| `Nats-Schedule`           | When the message will be sent to the target subject. Several formats are suppported: A timestamp for sending a messages once. Crontab format for repeated messages and simple alias for common crontab formats. | `0 30 14 * * *`, `@hourly`, `daily`, `@at 2009-11-10T23:00:00Z` (RFC3339 format) | 2.11    |
| `Nats-Schedule-TTL`       | Optional. The TTL to be set on the final message on the target subject.                                                                                                                                         | `1h`, `10s` (valid go duration string)                                           | 2.11    |
| `Nats-Schedule-Target`    | The target subject the final message will be sent to. Note that this must be distinct from the scheduling subject the message arrived in.                                                                       | `orders`                                                                         | 2.11    |
| `Nats-Schedule-Source`    | Optional. Instructs the schedule to read the last message on the given subject and publish it. If the Subject is empty, nothing is published, wildcards are not supported.                                      | `orders.customer_acme`                                                           | 2.11    |
| `Nats-Schedule-Time-Zone` | Optional. The time zone used for the Cron schedule. If not specified, the Cron schedule will be in UTC. Not allowed to be used if the schedule is not a Cron schedule.                                          | `CET`                                                                            | 2.11    |

The final scheduled message will contain the following headers.

| Name                 | Description                                                                            | Example                | Version |
| -------------------- | -------------------------------------------------------------------------------------- | ---------------------- | ------- |
| `Nats-Scheduler`     | The subject holding the schedule                                                       | `orders.schedule.1234` | 2.11    |
| `Nats-Schedule-Next` | Timestamp for next invocation for cron schedule messages or purge for delayed messages | `2009-11-10T23:00:00Z` | 2.11    |
| `Nats-TTL`           | The TTL value when Nats-Schedule-TTL was set                                           | `1h`, `10s`            | 2.11    |

##

## Batch send

Introduced in version 2.12 with optimizations in 2.14 - see [ADR-50](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-50.md)

Atomic batch sends will use the following headers. Batches are atomic on send only, but a client may reconstruct a batch using the headers below.

| Name                  | Description                                                                                                                                                 | Example                    | Version |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------- |
| `Nats-Batch-Id`       | Unique identifier for the batch.                                                                                                                            | `<uuid>` (<=64 characters) | 2.12    |
| `Nats-Batch-Sequence` | Monotonously increasing id, starting with `1`                                                                                                               | `1`, `2`                   | 2.12    |
| `Nats-Batch-Commit`   | Only on last message. `1` commit the batch including this message. `eob` commit the batch excluding this message. Any other value will terminate the batch. | `1`, `eob`                 | 2.12    |

## Internal

Headers used internally by API clients and the server. Should not be set by user.

This is list is not exhaustive. Headers used in error replies may not be documented.

| Name                      | Description                                                                                                                                                                                                                                                                                                                                            | Example                     | Version |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ------- |
| `Nats-Required-Api-Level` | Optional. The required API level for the JetStream request. Servers from version 2.11 will return an error if larger than the support API level.                                                                                                                                                                                                       | `2` (Integer value)         | 2.11    |
| `Nats-Request-Info`       | When messages cross account boundaries a header with origin information (account, user etc) may be added.                                                                                                                                                                                                                                              |                             | 2.2.0   |
| `Nats-Marker-Reason`      | When messages are removed from a KV where subject delete markers are supported, a delete marker will be placed. And notifications are sent to interested watchers. The message payload is empty and the removal reason is indicated through this header. See [ADR-48](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-48.md) | `MaxAge`, `Remove`, `Purge` | 2.12    |
| `Nats-Incr`               | Used in KV stores to atomically increment counter. Any valid integer (including 0) starting with a sign.. See [ADR-49](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-49.md)                                                                                                                                                | `+1`, `+42`, `-1`, `+0`     | 2.12    |
| `Nats-Counter-Sources`    | Tracking `Nats-Incr` when messages are sourced. For details see: [ADR-49](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-49.md)                                                                                                                                                                                             |                             | 2.12    |

Nats-Counter-Sources

## Mirror

Headers used for internal flow-control messages for a mirror.

This is for information only and may change without notice.

| Name                    | Description | Example | Version |
| ----------------------- | ----------- | ------- | ------- |
| `Nats-Last-Consumer`    |             |         | 2.2.1   |
| `Nats-Last-Stream`      |             |         | 2.2.1   |
| `Nats-Consumer-Stalled` |             |         | 2.4.0   |
| `Nats-Response-Type`    |             |         | 2.6.4   |


# Subject Mapping and Partitioning

Subject mapping and transforms is a powerful feature of the NATS server. Transformations (we will use mapping and transform interchangeably) apply to various situations when messages are generated and ingested, acting as translations and in some scenarios as filters.

{% hint style="warning" %}
Mapping and transforms is an advanced topic. Before proceeding, please ensure you understand NATS concepts like clusters, accounts and streams.
{% endhint %}

**Transforms can be defined (for details see below):**

* On the root of the config file (applying to the default $G account). Applying to all matching messages entering through client or leaf node connection into this account. Non-matching subjects will be unchanged.
* On the individual account level following the same rules as above.
* On subjects, which are imported into an account.
* In [JetStream](#subject-mapping-and-transforms-in-streams) context:
  * On messages imported by streams
  * On messages republished by JetStream
  * On messages copied to a stream via a source or mirror. For this purpose, the transform acts as a filter.

**Transforms may be used for:**

* Translating between namespaces. E.g. when mapping between accounts, but also when clusters and leaf nodes implement different semantics for the same subject.
* Suppressing subjects. E.g. Temporarily for testing.
* For backward compatibility after changing the subject naming hierarchy.
* Merging subjects together.
* [Disambiguation and isolation on super-clusters or leaf nodes](#cluster-scoped-mappings), by using different transforms in different clusters and leaf nodes.
* Testing. E.g. merging a test subject temporarily into a production subject or rerouting a production subject away from a production consumer.
* [Partitioning subjects](#deterministic-subject-token-partitioning) and JetStream streams
* [Filtering](#subject-mapping-and-transforms-in-streams) messages copied (sourced/mirrored) into a JetStream stream
* [Chaos testing and sampling. Mappings can be weighted](#weighted-mappings). Allowing for a certain percentage of messages to be rerouted, simulating loss, failure etc.
* ...

**Priority and sequence of operations**

* Transforms are applied as soon as a message enters the scope in which the transform was defined (cluster, account, leaf node, stream) and independent of how they arrived (publish by client, passing through gateway, stream import, stream source/mirror). And before any routing or subscription interest is applied. The message will appear as if published from the transformed subject under all circumstances.
* Transforms are **not applied recursively** in the same scope. This is necessary to prevent trivial loops. In the example below only the first matching rule is applied.

```shell
mappings: {
	transform.order target.order
	target.order transform.order
}
```

* Transforms are **applied in sequence** as they pass through different scopes. For example:
  1. A subject is transformed while being published
  2. Routed to a leaf node and transformed when received on the leaf node
  3. Imported into a stream and stored under a transformed name
  4. Republished from the stream to Core NATS under a final target subject

On a central cluster:

```
server_name: "hub"
cluster: { name: "hub" }
mappings: {
	orders.* orders.central.{{wildcard(1)}}
}
```

OR

```
server_name: "hub"
cluster: { name: "hub" }
mappings: {
	orders.> orders.central.>}
}
```

On a leaf cluster

```
server_name: "store1"
cluster: { name: "store1" }
mappings: {
	orders.central.* orders.local.{{wildcard(1)}}
}
```

A stream config on the leaf cluster

```
{
  "name": "orders",
  "subjects": [ "orders.local.*"],
  "subject_transform":{"src":"orders.local.*","dest":"orders.{{wildcard(1)}}"},
  "retention": "limits",
  ...
  "republish": {
    "src": "orders.*",
    "dest": "orders.trace.{{wildcard(1)}}"
  },
```

**Security**

When using **config file-based account management** (not using JWT security), you can define the core NATS account level subject transforms in server configuration files, and simply need to reload the configuration whenever you change a transform for the change to take effect.

When using **operator JWT security** (distributed security) with the built-in resolver you define the transforms and the import/exports in the account JWT, so after modifying them, they will take effect as soon as you push the updated account JWT to the servers.

**Testing and debugging**

{% hint style="info" %}
You can easily test individual subject transform rules using the [`nats`](https://docs.nats.io/using-nats/nats-tools/nats_cli) CLI tool command `nats server mapping`. See examples below.
{% endhint %}

From NATS server 2.11 (and NATS versions published thereafter) the handling of subjects, including mappings can be observed with `nats trace`

In the example below a message is first disambiguated from `orders.device1.order1` -> `orders.hub.device1.order1`. Then imported into a stream and stored under its original name.

```shell
nats trace orders.device1.order1

Tracing message route to subject orders.device1.order1

Client "NATS CLI Version development" cid:16 cluster:"hub" server:"hub" version:"2.11.0-dev"
    Mapping subject:"orders.hub.device1.order1"
--J JetStream action:"stored" stream:"orders" subject:"orders.device1.order1"
--X No active interest

Legend: Client: --C Router: --> Gateway: ==> Leafnode: ~~> JetStream: --J Error: --X

Egress Count:

  JetStream: 1
```

{% endhint %}

## Simple mappings

The example of `foo:bar` is straightforward. All messages the server receives on subject `foo` are remapped and can be received by clients subscribed to `bar`.

```
nats server mapping foo bar foo
> bar
```

When no subject is provided the command will operate in interactive mode:

```
nats server mapping foo bar
> Enter subjects to test, empty subject terminates.
>
> ? Subject foo
> bar

> ? Subject test
> Error: no matching transforms available
```

Example server config. Note that the mappings below apply only to the default $G account.

```
server_name: "hub"
cluster: { name: "hub" }
mappings: {
    orders.flush  orders.central.flush 
	orders.* orders.central.{{wildcard(1)}}
}
```

Mapping a full wildcard

```
server_name: "hub"
cluster: { name: "hub" }
mappings: {
    orders.>  orders.central.> 
}
```

With accounts. While this mapping applies to a specific account.

```
server_name: "hub"
cluster: { name: "hub" }

accounts {
    accountA: { 
        mappings: {
            orders.flush  orders.central.flush 
        	orders.* orders.central.{{wildcard(1)}}
        }
    }
}
```

## Mapping a full wildcard '>'

A full wildcard token can be used ONCE in source expression and must be present on the destination expression as well exactly once.

Example: Prefixing a subject:

```
nats server mapping ">"  "baz.>" bar.a.b
> baz.bar.b.a
```

## Subject token reordering

Wildcard tokens may be referenced by position number in the destination mapping using (only for versions 2.8.0 and above of `nats-server`). Syntax: `{{wildcard(position)}}`. E.g. `{{wildcard(1)}}` references the first wildcard token, `{{wildcard(2)}}` references the second wildcard token, etc..

Example: with this transform `"bar.*.*" : "baz.{{wildcard(2)}}.{{wildcard(1)}}"`, messages that were originally published to `bar.a.b` are remapped in the server to `baz.b.a`. Messages arriving at the server on `bar.one.two` would be mapped to `baz.two.one`, and so forth. Try it for yourself using `nats server mapping`.

```
nats server mapping "bar.*.*"  "baz.{{wildcard(2)}}.{{wildcard(1)}}" bar.a.b
> baz.b.a
```

{% hint style="info" %}
An older style deprecated mapping syntax using `$1`.`$2` en lieu of `{{wildcard(1)}}.{{wildcard(2)}}` may be seen in other examples.
{% endhint %}

## Dropping subject tokens

You can drop tokens from the subject by not using all the wildcard tokens in the destination transform, with the exception of mappings defined as part of import/export between accounts in which case *all* the wildcard tokens must be used in the transform destination.

```
nats server mapping "orders.*.*" "foo.{{wildcard(2)}}" orders.local.order1
> orders.order1
```

{% hint style="info" %}
Import/export mapping must be mapped bidirectionally unambiguous.
{% endhint %}

## Splitting tokens

There are two ways you can split tokens:

### Splitting on a separator

You can split a token on each occurrence of a separator string using the `split(separator)` transform function.

Examples:

* Split on '-': `nats server mapping "*" "{{split(1,-)}}" foo-bar` returns `foo.bar`.
* Split on '--': `nats server mapping "*" "{{split(1,--)}}" foo--bar` returns `foo.bar`.

### Splitting at an offset

You can split a token in two at a specific location from the start or the end of the token using the `SplitFromLeft(wildcard index, offset)` and `SplitFromRight(wildcard index, offset)` transform functions (note that the upper camel case on all subject transform function names is optional you can also use all lowercase function names if you prefer).

Examples:

* Split the token at 4 from the left: `nats server mapping "*" "{{splitfromleft(1,4)}}" 1234567` returns `1234.567`.
* Split the token at 4 from the right: `nats server mapping "*" "{{splitfromright(1,4)}}" 1234567` returns `123.4567`.

## Slicing tokens

You can slice tokens into multiple parts at a specific interval from the start or the end of the token by using the `SliceFromLeft(wildcard index, number of characters)` and `SliceFromRight(wildcard index, number of characters)` mapping functions.

Examples:

* Split every 2 characters from the left: `nats server mapping "*" "{{slicefromleft(1,2)}}" 1234567` returns `12.34.56.7`.
* Split every 2 characters from the right: `nats server mapping "*" "{{slicefromright(1,2)}}" 1234567` returns `1.23.45.67`.

## Deterministic subject token partitioning

Deterministic token partitioning allows you to use subject-based addressing to deterministically divide (partition) a flow of messages where one or more of the subject tokens is mapped into a partition key. Deterministically means, the same tokens are always mapped into the same key. The mapping will appear random and may not be `fair` for a small number of subjects.

For example: new customer orders are published on `neworders.<customer id>`, you can partition those messages over 3 partition numbers (buckets), using the `partition(number of partitions, wildcard token positions...)` function which returns a partition number (between 0 and number of partitions-1) by using the following mapping `"neworders.*" : "neworders.{{wildcard(1)}}.{{partition(3,1)}}"`.

```
nats server mapping "neworders.*" "neworders.{{wildcard(1)}}.{{partition(3,1)}}" neworders.customerid1
> neworders.customerid1.0
```

{% hint style="info" %}
Note that multiple token positions can be specified to form a kind of *composite partition key*. For example, a subject with the form `foo.*.*` can have a partition transform of `foo.{{wildcard(1)}}.{{wildcard(2)}}.{{partition(5,1,2)}}` which will result in five partitions in the form `foo.*.*.<n>`, but using the hash of the two wildcard tokens when computing the partition number.

```
nats server mapping "foo.*.*" "foo.{{wildcard(1)}}.{{wildcard(2)}}.{{partition(5,1,2)}}" foo.us.customerid 
> foo.us.customerid.0
```

{% endhint %}

This particular transform means that any message published on `neworders.<customer id>` will be mapped to `neworders.<customer id>.<a partition number 0, 1, or 2>`. i.e.:

| Published on          | Mapped to               |
| --------------------- | ----------------------- |
| neworders.customerid1 | neworders.customerid1.0 |
| neworders.customerid2 | neworders.customerid2.2 |
| neworders.customerid3 | neworders.customerid3.1 |
| neworders.customerid4 | neworders.customerid4.2 |
| neworders.customerid5 | neworders.customerid5.1 |
| neworders.customerid6 | neworders.customerid6.0 |

The transform is deterministic because (as long as the number of partitions is 3) 'customerid1' will always map to the same partition number. The mapping is hash-based, its distribution is random but tends towards 'perfectly balanced' distribution (i.e. the more keys you map the more the number of keys for each partition will tend to converge to the same number).

You can partition on more than one subject wildcard token at a time, e.g.: `{{partition(10,1,2)}}` distributes the union of token wildcards 1 and 2 over 10 partitions.

| Published on | Mapped to |
| ------------ | --------- |
| foo.1.a      | foo.1.a.1 |
| foo.1.b      | foo.1.b.0 |
| foo.2.b      | foo.2.b.9 |
| foo.2.a      | foo.2.a.2 |

What this deterministic partition transform enables is the distribution of the messages that are subscribed to using a single subscriber (on `neworders.*`) into three separate subscribers (respectively on `neworders.*.0`, `neworders.*.1` and `neworders.*.2`) that can operate in parallel.

```
nats server mapping "foo.*.*" "foo.{{wildcard(1)}}.{{wildcard(2)}}.{{partition(3,1,2)}}"
```

### When is deterministic partitioning uselful

The core NATS queue-groups and JetStream durable consumer mechanisms to distribute messages amongst a number of subscribers are partition-less and non-deterministic, meaning that there is no guarantee that two sequential messages published on the same subject are going to be distributed to the same subscriber. While in most use cases a completely dynamic, demand-driven distribution is what you need, it does come at the cost of guaranteed ordering because if two subsequent messages can be sent to two different subscribers which would then both process those messages at the same time at different speeds (or the message has to be re-transmitted, or the network is slow, etc.) and that could result in potential 'out of order' message delivery.

This means that if the application requires strictly ordered message processing, you need to limit distribution of messages to 'one at a time' (per consumer/queue-group, i.e. using the 'max acks pending' setting), which in turn hurts scalability because it means no matter how many workers you have subscribed, only one is doing any processing work at a time.

Being able to evenly split (i.e. partition) subjects in a deterministic manner (meaning that all the messages on a particular subject are always mapped to the same partition) allows you to distribute and scale the processing of messages in a subject stream while still maintaining strict ordering per subject. For example, inserting a partition number as a token in the message subject as part of the stream definition and then using subject filters to create a consumer per partition (or set of partitions).

Another scenario for deterministic partitioning is in the extreme message publication rate scenarios where you are reaching the limits of the throughput of incoming messages into a stream capturing messages using a wildcard subject. This limit can be ultimately reached at very high message rate due to the fact that a single nats-server process is acting as the RAFT leader (coordinator) for any given stream and can therefore become a limiting factor. In that case, distributing (i.e. partitioning) that stream into a number of smaller streams (each one with its own RAFT leader and therefore all these RAFT leaders are spread over all of the JetStream-enabled nats-servers in the cluster rather than a single one) in order to scale.

Yet another use case where deterministic partitioning can help is if you want to leverage local data caching of data (context or potentially heavy historical data for example) that the subscribing process need to access as part of the processing of the messages.

## Weighted mappings

Traffic can be split by percentage from one subject transform to multiple subject transforms.

### For A/B testing or canary releases

Here's an example for canary deployments, starting with version 1 of your service.

Applications would make requests of a service at `myservice.requests`. The responders doing the work of the server would subscribe to `myservice.requests.v1`. Your configuration would look like this:

```
  myservice.requests: [
    { destination: myservice.requests.v1, weight: 100% }
  ]
```

All requests to `myservice.requests` will go to version 1 of your service.

When version 2 comes along, you'll want to test it with a canary deployment. Version 2 would subscribe to `myservice.requests.v2`. Launch instances of your service.

Update the configuration file to redirect some portion of the requests made to `myservice.requests` to version 2 of your service.

For example the configuration below means 98% of the requests will be sent to version 1 and 2% to version 2.

```
    myservice.requests: [
        { destination: myservice.requests.v1, weight: 98% },
        { destination: myservice.requests.v2, weight: 2% }
    ]
```

Once you've determined Version 2 is stable you can switch 100% of the traffic over to it and you can then shut down the version 1 instance of your service.

### For traffic shaping in testing

Traffic shaping is also useful in testing. You might have a service that runs in QA that simulates failure scenarios which could receive 20% of the traffic to test the service requestor.

`myservice.requests.*: [{ destination: myservice.requests.{{wildcard(1)}}, weight: 80% }, { destination: myservice.requests.fail.{{wildcard(1)}}, weight: 20% }`

### For artificial loss

Alternatively, introduce loss into your system for chaos testing by mapping a percentage of traffic to the same subject. In this drastic example, 50% of the traffic published to `foo.loss.a` would be artificially dropped by the server.

`foo.loss.>: [ { destination: foo.loss.>, weight: 50% } ]`

You can both split and introduce loss for testing. Here, 90% of requests would go to your service, 8% would go to a service simulating failure conditions, and the unaccounted for 2% would simulate message loss.

`myservice.requests: [{ destination: myservice.requests.v3, weight: 90% }, { destination: myservice.requests.v3.fail, weight: 8% }]` the remaining 2% is "lost"

## Cluster scoped mappings

If you are running a super-cluster you can define transforms that apply only to messages being published from a specific cluster.

For example if you have 3 clusters named `east` `central` and `west` and you want to map messages published on `foo` in the `east` cluster to `foo.east`, those published in the `central` cluster to `foo.central` and so on for `west` you can do so by using the `cluster` keyword in the mapping source and destination.

```
mappings = {
        "foo":[
               {destination:"foo.west", weight: 100%, cluster: "west"},
               {destination:"foo.central", weight: 100%, cluster: "central"},
               {destination:"foo.east", weight: 100%, cluster: "east"}
        ]
}
```

This means that the application can be portable in terms of deployment and does not need to be configured with the name of the cluster it happens to be connected in order to compose the subject: it just publishes to `foo` and the server will map it to the appropriate subject based on the cluster it's running in.

## Subject mapping and transforms in streams

You can define subject mapping transforms as part of the stream configuration.

Transforms can be applied in multiple places in the stream configuration:

* You can apply a subject mapping transformation as part of a stream mirror
* You can apply a subject mapping transformation as part of a stream source
* You can apply an overall stream ingress subject mapping transformation that applies to all matching messages regardless of how they are ingested into the stream
* You can also apply a subject mapping transformation as part of the re-publishing of messages

Note that when used in Mirror, Sources or Republish, the subject transforms are filters with optional transformation, while when used in the Stream configuration it only transforms the subjects of the matching messages and does not act as a filter.

```
{
  "name": "orders",
  "subjects": [ "orders.local.*"],
  "subject_transform":{"src":"orders.local.*","dest":"orders.{{wildcard(1)}}"},
  "retention": "limits",
  ...
  "sources": [
    {
      "name": "other_orders",
      "subject_transforms": [
        {
          "src": "orders.online.*",
          "dest": "orders.{{wildcard(1)}}"
        }
      ]
    }
  ],
  "republish": {
    "src": "orders.*",
    "dest": "orders.trace.{{wildcard(1)}}"
  }
    
}
```

{% hint style="info" %}
For `sources` and `republish` transforms the `src` expression will act as a filter. Non-matching subjects will be ignored.

For the stream level `subject_transform` non-matching subjects will stay untouched.
{% endhint %}

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-a265cee62a0bf0e0b5d4c4ec68995c9ae39ec6fe%2Fstream-transform.png?alt=media\&token=eb61f7ba-76df-4d3a-b150-926c9af92e4d)


# NATS Service Infrastructure

NATS is a client/server system in the fact that you have 'NATS client applications' (applications using one of the NATS client libraries) that connect to 'NATS servers' that provide the NATS service. The NATS servers work together to provide a NATS service infrastructure to their client applications.

NATS is extremely flexible and scalable and allows the service infrastructure to be as small as a single process running locally on your local machine and as large as an 'Internet of NATS' of Leaf Nodes, and Leaf Node clusters all interconnected in a secure way over a global shared NATS super-cluster.

Regardless of the size and complexity of the NATS service infrastructure being used, the only configuration needed by the client applications being the location (NATS URLs) of one or more NATS servers and depending on the required security, their credentials.

Note that if your application is written in Golang then you even have the option of embedding the NATS server functionality into the application itself (however you need to then configure your application instances with nats-server configuration information).

You do not actually need to run your NATS service infrastructure, instead you can instead make use of a public NATS infrastructure offered by a NATS Service Provider such as [Synadia Cloud](https://www.synadia.com/cloud?utm_source=nats_docs\&utm_medium=nats), think of Synadia Cloud as being an 'Internet of NATS' (literally an "InterNATS") and of Synadia as being an "InterNATS Service Provider".

## The Evolution of your NATS service infrastructure

You will typically start by running a single instance of nats-server on your local development machine, and have your applications connect to it while you do your application development and local testing.

Next you will probably want to start testing and running those applications and servers in a VPC, or a region or in some on-prem location, so you will deploy either single NATS server or clusters of NATS servers in your VPCs/regions/on-prem/etc... locations and in each location have the applications connect their local nats-server or nats-server cluster. You can then connect those local nats-servers or local nats-server clusters together by making them leaf nodes connecting to a 'backbone' cluster or super-cluster, or by connecting them directly together via gateway connections.

If you have many client applications (e.g., applications deployed on end-user devices all over the Internet, or for example many IoT devices) or many servers in a lot of locations you will then scale your NATS service infrastructure by deploying clusters of NATS servers in multiple locations and multiple cloud providers and VPCs. You will then need to connect those clusters into a global super-cluster and then devise a scheme to intelligently direct your client applications to the right 'closest' NATS server cluster.

## Running your own NATS service infrastructure

You can deploy and run your own NATS service infrastructure of nats-server instances, composed of servers, clusters of servers, super-cluster and leaf node NATS servers.

### Virtualization and containerization considerations

If using Kubernetes we recommend you use the [Helm charts](https://github.com/nats-io/k8s/tree/main/helm/charts/nats).


# NATS Adaptive Deployment Architectures

From a single process to a global super-cluster with leaf node servers, you can always adapt your NATS service deployment to your needs. From servers and VPCs in many clouds, to partially connected small edge devices and everything in between, you can always easily extend and scale your NATS service as your needs grow.

## A single server

The simplest version of a NATS service infrastructure is a single `nats-server` process. The `nats-server` binary is highly optimized, very lightweight and extremely efficient in its resources' usage.

Client applications establish a connection to the URL of that nats-server process (e.g. `"nats://localhost"`).

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-abdace979135d2d0cf9bbf8577ea541f00d460ce%2Fsingle-server.svg?alt=media\&token=841d1dc8-8da1-4a2b-9886-c5ab3edb893e)

## A cluster of servers

If you need a fault-tolerant NATS service or if you need to scale your service capacity, you can cluster a set of nats-server processes together in a cluster.

Client applications establish and maintain a connection to (one of) the nats server URL(s) composing the cluster (e.g. `"nats://server1","nats://server2",...`).

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-de823670ac5261744954b734e9da5318f9edacdf%2Fserver-cluster.svg?alt=media\&token=538eb10b-db3e-4e45-a58d-ac77ef1da4e6)

## A super-cluster

You can go further than a single cluster and have disaster recovery and get global deployments (e.g. on multiple locations or regions, multiple VPCs or multiple Cloud providers) by deploying multiple clusters and connecting them together via gateway connections (which are interest pruned).

Client applications establish a connection to (one of) the nats server URL(s) of one of the clusters (e.g. `"nats://us-west-1.company.com","nats://us-west-2.company.com",...`).

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-e6809f92dc0c0c1f74af41ec28fb21245925385e%2Fsuper_cluster.svg?alt=media\&token=a142733f-fa43-432d-9088-ac91f24415e3)

## With Leaf Nodes

You can easily 'extend' the NATS service provided by a cluster or super-cluster by deploying 'locally' one or more **leaf node** nats servers that proxy and route traffic between their client applications and the NATS service infrastructure. The context of 'locality' in this case is not just physical: it could mean a location, an edge device or a single development machine, but it could also service a VPC, a group of server processes for a specific application or different accounts, or even a business unit. Leaf node NATS servers can be configured to connect to their cluster over a WebSocket connection (rather than TLS or plain TCP).

Leaf nodes appear to the cluster as a single account connection. Leaf nodes can provide continuous NATS service for their clients, even while being temporarily disconnected from the cluster(s). You can even enable JetStream on the leaf nodes in order to create local streams that are mirrored (mirroring is store and forward and therefore can recover from connectivity outages) to global streams in the upstream cluster(s).

Client applications are configured with the URLs of their 'local' leaf node server(s) and establish a connection to (one of) the leaf node server(s) (e.g. `"nats://leaf-node-1","nats://leaf-node-2",...`).

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-534fd24bb16a7e8f11711d2e5d4717e8c1c7f724%2Fleaf_nodes.svg?alt=media\&token=aec8860f-ae26-412d-a6e8-22fcac7475c3)

## See Also

NATS Clusters

{% embed url="<https://youtu.be/srARy0m9SdI>" %}
Clusters
{% endembed %}

NATS Super-clusters

{% embed url="<https://youtu.be/6O_sNSJ2p70>" %}
Super-clusters
{% endembed %}

NATS Leaf Nodes

{% embed url="<https://youtu.be/WH55czo1BNk>" %}
Leaf Nodes
{% endembed %}

NATS Service Geo-affinity in Queues

{% embed url="<https://youtu.be/jLTVhP08Tq0?t=190>" %}
Geo-affinity in Queues
{% endembed %}


# Security

NATS has a lot of security features:

* Connections can be [*encrypted* with TLS](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls)
* Client connections can be [*authenticated*](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro) in many ways:
  * [Token Authentication](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tokens)
  * [Username/Password credentials](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password)
  * [TLS Certificate](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/tls_mutual_auth)
  * [NKEY with Challenge](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth)
  * [Decentralized JWT Authentication/Authorization](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt)
  * You can also integrate NATS with your existing authentication/authorization system or create your own custom authentication using the [Auth callout](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_callout)
* Authenticated clients are identified as users and have a set of [*authorizations*](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/authorization)

You can use [accounts](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/accounts) for multi-tenancy: each account has its own independent 'subject namespace' and you control the import/export of both streams of messages and services between accounts, and any number of users that client applications can be authenticated as. The subjects or subject wildcards that a user is allowed to publish and/or subscribe to can be controlled either through server configuration or as part of signed JWTs.

JWT authentication/authorization administration is decentralized because each account private key holder can manage their users and their authorizations on their own, without the need for any configuration change on the NATS servers by minting their own JWTs and distributing them to the users. There is no need for the NATS server to ever store any user private keys as they only need to validate the signature chain of trust contained in the user JWT presented by the client application to validate that they have the proper public key for that user.

The JetStream persistence layer of NATS also provides [encryption at rest](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/encryption_at_rest).


# Connectivity

NATS supports several kinds of connectivity *directly* to the NATS servers.

* Plain NATS connections
* TLS encrypted NATS connections
* [WebSocket](https://github.com/nats-io/nats.ws) NATS connections
* [MQTT](https://docs.nats.io/running-a-nats-service/configuration/mqtt) client connections

There is also a number of adapters available to bridge traffic to and from other messaging systems

* [Kafka Bridge](https://github.com/nats-io/nats-kafka)
* [JMS](https://github.com/nats-io/nats-jms-bridge) which can also be used to bridge MQ and RabbitMQ, since they both offer a JMS interface


# NATS Tools

## Using NATS from client application

The most common form of connecting to the NATS messaging system will be through an application built with any of the [40+ client libraries](https://docs.nats.io/using-nats/developer) available for NATS.

The client application will connect to an instance of the NATS server, be it a single server, a cluster of servers or even a global super-cluster such as [Synadia Cloud](https://www.synadia.com/cloud?utm_source=nats_docs\&utm_medium=nats), sending and receiving messages via a range of subscribers contracts. If the application is written in GoLang the NATS server can even be [embedded into a Go](https://dev.to/karanpratapsingh/embedding-nats-in-go-19o) application.

Client APIs will also allow access to almost all server configuration tasks when using an account with sufficient permissions.

## Command Line Tooling

Besides using the client API to manage NATS servers, the NATS ecosystem also has many tools to interact with other applications and services over NATS and streams, support server configuration, enhance monitoring or tune performance such as:

* General interaction and management
  * [nats](https://docs.nats.io/using-nats/nats-tools/nats_cli) - The `nats` Command Line Tool is the easiest way to interact with, test and manage NATS and JetStream from a terminal or from scripts. It's list of features are ever growing, so please download the [latest version](https://github.com/nats-io/natscli/releases).
* Security
  * [nk](https://docs.nats.io/using-nats/nats-tools/nk) - Generate NKeys for use with JSon Web Tokens (JWT) used with nsc
  * [nsc](https://docs.nats.io/using-nats/nats-tools/nsc) - Configure Operators, Accounts, Users and permission offline to later push them to a production server. This is the preferred tools to create security configuration unless you are using [Synadia Control Plane](https://www.docs.synadia.com/platform/control-plane?utm_source=nats_docs\&utm_medium=nats)
  * [nats account server](https://nats-io.gitbook.io/legacy-nats-docs/nats-account-server) - (**legacy, replaced by the built-in NATS resolver**) a custom security server. NAS can still be used as a reference implementation for you tailor-made security integration.
* Monitoring
  * [nats top](https://docs.nats.io/using-nats/nats-tools/nats_top) - Monitor NATS Servers
  * [prometheus-nats-exporter](https://github.com/nats-io/prometheus-nats-exporter) - Export NATS server metrics to [Prometheus](https://prometheus.io/) and a [Grafana](https://grafana.com) dashboard.
* Benchmarking
  * see [nats bench](https://docs.nats.io/using-nats/nats-tools/nats_cli/natsbench) subcommand of the [nats](https://docs.nats.io/using-nats/nats-tools/nats_cli) tool


# nats

A command line utility to interact with and manage NATS.

This utility replaces various past tools that were named in the form `nats-sub` and `nats-pub`, adds several new capabilities and supports full JetStream management.

Check out the repo for all the details: [github.com/nats-io/natscli](https://github.com/nats-io/natscli).

## Installing `nats`

Please refer to the [installation section in the readme](https://github.com/nats-io/natscli?tab=readme-ov-file#installation).

You can read about execution policies [here](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies).

Binaries are also available as [GitHub Releases](https://github.com/nats-io/natscli/releases).

## Using `nats`

### Getting help

* [NATS Command Line Interface README](https://github.com/nats-io/natscli#readme)
* `nats help`
* `nats help [<command>...]` or `nats [<command>...] --help`
* Remember to look at the cheat sheets!
  * `nats cheat`
  * `nats cheat --sections`
  * `nats cheat <section>>`

### Interacting with NATS

* `nats context`
* `nats account`
* `nats pub`
* `nats sub`
* `nats request`
* `nats reply`
* `nats bench`

### Monitoring NATS

* `nats events`
* `nats rtt`
* `nats server`
* `nats latency`
* `nats governor`

### Managing and interacting with streams

* `nats stream`
* `nats consumer`
* `nats backup`
* `nats restore`

### Managing and interacting with the K/V Store

* `nats kv`

### Get reference information

* `nats errors`
* `nats schema`

## Configuration Contexts

The CLI has a number of configuration settings that can be passed either as command line arguments or set in environment variables.

```shell
nats --help
```

Output extract

```
...
  -s, --server=URL              NATS server urls ($NATS_URL)
      --user=USER               Username or Token ($NATS_USER)
      --password=PASSWORD       Password ($NATS_PASSWORD)
      --creds=FILE              User credentials ($NATS_CREDS)
      --nkey=FILE               User NKEY ($NATS_NKEY)
      --tlscert=FILE            TLS public certificate ($NATS_CERT)
      --tlskey=FILE             TLS private key ($NATS_KEY)
      --tlsca=FILE              TLS certificate authority chain ($NATS_CA)
      --socks-proxy=PROXY       SOCKS5 proxy for connecting to NATS server
                                ($NATS_SOCKS_PROXY)
      --colors=SCHEME           Sets a color scheme to use ($NATS_COLOR)
      --timeout=DURATION        Time to wait on responses from NATS
                                ($NATS_TIMEOUT)
      --context=NAME            Configuration context ($NATS_CONTEXT)
...
```

The server URL can be set using the `--server` CLI flag, or the `NATS_URL` environment variable, or using [NATS Contexts](#nats-contexts).

The password can be set using the `--password` CLI flag, or the `NATS_PASSWORD` environment variable, or using [NATS Contexts](#nats-contexts). For example: if you want to create a script that prompts the user for the system user password (so that for example it doesn't appear in `ps` or `history` or maybe you don't want it stored in the profile) and then execute one or more `nats` commands you do something like:

```shell
#!/bin/bash
echo "-n" "system user password: "
read -s NATS_PASSWORD
export NATS_PASSWORD
nats server report jetstream --user system
```

### NATS Contexts

A context is a named configuration that stores all of these settings. You can designate a default context and switch between contexts.

A context can be created with `nats context create my_context_name` and then modified with`nats context edit my_context_name`:

```json
{
  "description": "",
  "url": "nats://127.0.0.1:4222",
  "token": "",
  "user": "",
  "password": "",
  "creds": "",
  "nkey": "",
  "cert": "",
  "key": "",
  "ca": "",
  "nsc": "",
  "jetstream_domain": "",
  "jetstream_api_prefix": "",
  "jetstream_event_prefix": "",
  "inbox_prefix": "",
  "user_jwt": ""
}
```

This context is stored in the file `~/.config/nats/context/my_context_name.json`.

A context can also be created by specifying settings with `nats context save`

```shell
nats context save example --server nats://nats.example.net:4222 --description 'Example.Net Server'
nats context save local --server nats://localhost:4222 --description 'Local Host' --select 
```

List your contexts

```shell
nats context ls
```

```
Known contexts:

   example             Example.Net Server
   local*              Local Host
```

We passed `--select` to the `local` one meaning it will be the default when nothing is set.

Select a context

```shell
nats context select
```

Check the round trip time to the server (using the currently selected context)

```shell
nats rtt
```

```
nats://localhost:4222:

   nats://127.0.0.1:4222: 245.115µs
       nats://[::1]:4222: 390.239µs
```

You can also specify a context directly

```shell
nats rtt --context example
```

```
nats://nats.example.net:4222:

   nats://192.0.2.10:4222: 41.560815ms
   nats://192.0.2.11:4222: 41.486609ms
   nats://192.0.2.12:4222: 41.178009ms
```

All `nats` commands are context aware and the `nats context` command has various commands to view, edit and remove contexts.

Server URLs and Credential paths can be resolved via the `nsc` command by specifying an URL, for example to find user `new` within the `orders` account of the `acme` operator you can use this:

```shell
nats context save example --description 'Example.Net Server' --nsc nsc://acme/orders/new
```

The server list and credentials path will now be resolved via `nsc`, if these are specifically set in the context, the specific context configuration will take precedence.

## Generating bcrypted passwords

The server supports hashing of passwords and authentication tokens using `bcrypt`. To take advantage of this, simply replace the plaintext password in the configuration with its `bcrypt` hash, and the server will automatically utilize `bcrypt` as needed. See also: [Bcrypted Passwords](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/username_password#bcrypted-passwords).

The `nats` utility has a command for creating `bcrypt` hashes. This can be used for a password or a token in the configuration.

```shell
nats server passwd
```

```
? Enter password [? for help] **********************
? Reenter password [? for help] **********************

$2a$11$3kIDaCxw.Glsl1.u5nKa6eUnNDLV5HV9tIuUp7EHhMt6Nm9myW1aS
```

To use the password on the server, add the hash into the server configuration file's authorization section.

```
  authorization {
    user: derek
    password: $2a$11$3kIDaCxw.Glsl1.u5nKa6eUnNDLV5HV9tIuUp7EHhMt6Nm9myW1aS
  }
```

Note the client will still have to provide the plain text version of the password, the server however will only store the hash to verify that the password is correct when supplied.

## See Also

Publish-subscribe pattern using the NATS CLI

{% embed url="<https://www.youtube.com/watch?v=jLTVhP08Tq0>" %}
Publish-subscribe Pattern using NATS CLI
{% endembed %}


# nats bench

NATS is fast and lightweight, and places a priority on performance. The `nats` CLI tool can, amongst many other things, be used for running benchmarks and measuring performance of your target NATS service infrastructure. In this tutorial, you learn how to benchmark and tune NATS on your systems and environment.

Note: the numbers below are just examples and were obtained using a MacBook Pro M4 (November 2024) running version 2.12.1 of `nats-server`:

```
 Model Name:	MacBook Pro
  Model Identifier:	Mac16,1
  Model Number:	MW2U3LL/A
  Chip:	Apple M4
  Total Number of Cores:	10 (4 performance and 6 efficiency)
  Memory:	16 GB
  System Firmware Version:	13822.1.2
  OS Loader Version:	13822.1.2
```

## Prerequisites

* [Install the NATS CLI Tool](https://docs.nats.io/using-nats/nats-tools/nats_cli)
* [Install the NATS server](https://docs.nats.io/running-a-nats-service/introduction/installation)

## Start the NATS server with monitoring enabled

```bash
nats-server -m 8222 -js
```

Verify that the NATS server starts successfully, as well as the HTTP monitor:

```
[[2932] 2025/10/28 12:29:02.879297 [INF] Starting nats-server
[2932] 2025/10/28 12:29:02.879658 [INF]   Version:  2.12.1
[2932] 2025/10/28 12:29:02.879661 [INF]   Git:      [fab5f99]
[2932] 2025/10/28 12:29:02.879664 [INF]   Name:     NBIYCV5UNYPP2ZBZJZNGQ7UJNJILSQZCD6MK2CPWU6UY7PHYPKWOYYS4
[2932] 2025/10/28 12:29:02.879667 [INF]   Node:     YNleYaHo
[2932] 2025/10/28 12:29:02.879668 [INF]   ID:       NBIYCV5UNYPP2ZBZJZNGQ7UJNJILSQZCD6MK2CPWU6UY7PHYPKWOYYS4
[2932] 2025/10/28 12:29:02.880586 [INF] Starting http monitor on 0.0.0.0:8222
[2932] 2025/10/28 12:29:02.880696 [INF] Starting JetStream
[2932] 2025/10/28 12:29:02.880755 [WRN] Temporary storage directory used, data could be lost on system reboot
[2932] 2025/10/28 12:29:02.881014 [INF]     _ ___ _____ ___ _____ ___ ___   _   __  __
[2932] 2025/10/28 12:29:02.881018 [INF]  _ | | __|_   _/ __|_   _| _ \ __| /_\ |  \/  |
[2932] 2025/10/28 12:29:02.881019 [INF] | || | _|  | | \__ \ | | |   / _| / _ \| |\/| |
[2932] 2025/10/28 12:29:02.881020 [INF]  \__/|___| |_| |___/ |_| |_|_\___/_/ \_\_|  |_|
[2932] 2025/10/28 12:29:02.881020 [INF] 
[2932] 2025/10/28 12:29:02.881021 [INF]          https://docs.nats.io/jetstream
[2932] 2025/10/28 12:29:02.881022 [INF] 
[2932] 2025/10/28 12:29:02.881022 [INF] ---------------- JETSTREAM ----------------
[2932] 2025/10/28 12:29:02.881023 [INF]   Strict:          true
[2932] 2025/10/28 12:29:02.881026 [INF]   Max Memory:      12.00 GB
[2932] 2025/10/28 12:29:02.881027 [INF]   Max Storage:     233.86 GB
[2932] 2025/10/28 12:29:02.881027 [INF]   Store Directory: "/var/folders/cx/x13pjm0n3ds6w4q_4xhr_c0r0000gn/T/nats/jetstream"
[2932] 2025/10/28 12:29:02.881029 [INF]   API Level:       2
[2932] 2025/10/28 12:29:02.881030 [INF] -------------------------------------------
[2932] 2025/10/28 12:29:02.881335 [INF] Listening for client connections on 0.0.0.0:4222
[2932] 2025/10/28 12:29:02.881434 [INF] Server is ready
```

## Run a publisher throughput test

Let's run a first test to see how fast a single publisher can publish one million 16 byte messages to the NATS server. This should yield very high numbers as there is no subscriber on the subject being used.

```bash
nats bench pub foo --size 16 --msgs 1000000
```

The output tells you the number of messages and the number of payload bytes that the client was able to publish per second:

```
12:45:18 Starting Core NATS publisher benchmark [clients=1, msg-size=16 B, msgs=1,000,000, multi-subject=false, multi-subject-max=100,000, sleep=0s, subject=foo]
12:45:18 [1] Starting Core NATS publisher, publishing 1,000,000 messages
Finished      0s [================================================================] 100%

NATS Core NATS publisher stats: 14,786,683 msgs/sec ~ 226 MiB/sec ~ 0.07us
```

## Run a publish/subscribe throughput test

While the measurement above is an interesting data point, it is purely an academic measurement as you will usually have one (or more) subscribers for the messages being published.

Let's look at throughput for a single publisher with a single subscriber. For this, we need to run two instances of `nats bench` at the same time (e.g. in two shell windows), one to subscribe and one to publish.

First start the subscriber (it doesn't start measuring until it receives the first message from the publisher).

```bash
nats bench sub foo --size 16 --msgs 1000000
```

Then start the publisher.

```bash
nats bench pub foo --size 16 --msgs 1000000
```

Publisher's output:

```
13:15:53 Starting Core NATS publisher benchmark [clients=1, msg-size=16 B, msgs=1,000,000, multi-subject=false, multi-subject-max=100,000, sleep=0s, subject=foo]
13:15:53 [1] Starting Core NATS publisher, publishing 1,000,000 messages
Finished      0s [================================================================] 100%

NATS Core NATS publisher stats: 4,925,767 msgs/sec ~ 75 MiB/sec ~ 0.20us
```

Subscriber's output:

```
13:15:50 Starting Core NATS subscriber benchmark [clients=1, msg-size=16 B, msgs=1,000,000, multi-subject=false, subject=foo]
13:15:50 [1] Starting Core NATS subscriber, expecting 1,000,000 messages
Finished      0s [============================================================] 100%

NATS Core NATS subscriber stats: 4,928,153 msgs/sec ~ 75 MiB/sec ~ 0.20us
```

We can also increase the size of the messages using `--size`, for example:

Publisher:

```bash
nats bench pub foo --size 16kb
```

```
13:20:18 Starting Core NATS publisher benchmark [clients=1, msg-size=16 KiB, msgs=100,000, multi-subject=false, multi-subject-max=100,000, sleep=0s, subject=foo]
13:20:18 [1] Starting Core NATS publisher, publishing 100,000 messages
Finished      0s [================================================================] 100%

NATS Core NATS publisher stats: 230,800 msgs/sec ~ 3.5 GiB/sec ~ 4.33us
```

Subscriber:

```bash
nats bench sub foo --size 16kb
```

```
13:20:15 Starting Core NATS subscriber benchmark [clients=1, msg-size=16 KiB, msgs=100,000, multi-subject=false, subject=foo]
13:20:15 [1] Starting Core NATS subscriber, expecting 100,000 messages
Finished      0s [============================================================] 100%

NATS Core NATS subscriber stats: 226,091 msgs/sec ~ 3.4 GiB/sec ~ 4.42us
```

As expected, while the number of messages per second decreases with the larger messages, the throughput, however, increases massively.

## Run a 1:N throughput test

You can also measure performance with a message fan-out where multiple subscribers receive a copy of the message. You can do this using the `--client` flag, each client being a Go-routine, making it's own connection to the server and subscribing to the subject.

When specifying multiple clients `nats bench` will also report aggregated statistics.

For example for a fan-out of 4:

```bash
nats bench sub foo --clients 4
```

and

```bash
nats bench pub foo
```

Publisher's output:

```
13:34:26 Starting Core NATS publisher benchmark [clients=1, msg-size=128 B, msgs=100,000, multi-subject=false, multi-subject-max=100,000, sleep=0s, subject=foo]
13:34:26 [1] Starting Core NATS publisher, publishing 100,000 messages
Finished      0s [================================================================] 100%

NATS Core NATS publisher stats: 1,012,200 msgs/sec ~ 124 MiB/sec ~ 0.99us
```

Subscribers' output:

```
13:34:24 Starting Core NATS subscriber benchmark [clients=4, msg-size=128 B, msgs=100,000, multi-subject=false, subject=foo]
13:34:24 [1] Starting Core NATS subscriber, expecting 100,000 messages
13:34:24 [2] Starting Core NATS subscriber, expecting 100,000 messages
13:34:24 [3] Starting Core NATS subscriber, expecting 100,000 messages
13:34:24 [4] Starting Core NATS subscriber, expecting 100,000 messages
Finished      0s [============================================================] 100%
Finished      0s [============================================================] 100%
Finished      0s [============================================================] 100%
Finished      0s [============================================================] 100%

  [1] 1,013,938 msgs/sec ~ 124 MiB/sec ~ 0.99us (100,000 msgs)
  [2] 1,014,120 msgs/sec ~ 124 MiB/sec ~ 0.99us (100,000 msgs)
  [3] 1,007,242 msgs/sec ~ 123 MiB/sec ~ 0.99us (100,000 msgs)
  [4] 1,004,311 msgs/sec ~ 123 MiB/sec ~ 1.00us (100,000 msgs)

 NATS Core NATS subscriber aggregated stats: 4,015,923 msgs/sec ~ 490 MiB/sec
 message rates min 1,004,311 | avg 1,009,902 | max 1,014,120 | stddev 4,254 msgs
 avg latencies min 0.99us | avg 0.99us | max 1.00us | stddev 0.00us
```

## Run a N:M throughput test

When more than 1 publisher client is specified, `nats bench` evenly distributes the total number of messages (`--msgs`) across the number of publishers (`--clients`).

So let's increase the number of publishers and also increase the number of messages so the benchmark run lasts a little bit longer:

Subscriber:

```bash
nats bench sub foo --clients 4 --msgs 1000000
```

Publisher:

```bash
nats bench pub foo --clients 4 --msgs 1000000
```

Publisher's output

```
13:40:24 Starting Core NATS publisher benchmark [clients=4, msg-size=128 B, msgs=1,000,000, multi-subject=false, multi-subject-max=100,000, sleep=0s, subject=foo]
13:40:24 [1] Starting Core NATS publisher, publishing 250,000 messages
13:40:24 [2] Starting Core NATS publisher, publishing 250,000 messages
13:40:24 [3] Starting Core NATS publisher, publishing 250,000 messages
13:40:24 [4] Starting Core NATS publisher, publishing 250,000 messages
Finished      0s [================================================================] 100%
Finished      0s [================================================================] 100%
Finished      0s [================================================================] 100%
Finished      0s [================================================================] 100%

  [1] 272,785 msgs/sec ~ 33 MiB/sec ~ 3.67us (250,000 msgs)
  [2] 271,251 msgs/sec ~ 33 MiB/sec ~ 3.69us (250,000 msgs)
  [3] 270,340 msgs/sec ~ 33 MiB/sec ~ 3.70us (250,000 msgs)
  [4] 270,040 msgs/sec ~ 33 MiB/sec ~ 3.70us (250,000 msgs)

 NATS Core NATS publisher aggregated stats: 1,080,144 msgs/sec ~ 132 MiB/sec
 message rates min 270,040 | avg 271,104 | max 272,785 | stddev 1,068 msgs
 avg latencies min 3.67us | avg 3.69us | max 3.70us | stddev 0.01us
```

Subscriber's output:

```
13:40:18 Starting Core NATS subscriber benchmark [clients=4, msg-size=128 B, msgs=1,000,000, multi-subject=false, subject=foo]
13:40:18 [1] Starting Core NATS subscriber, expecting 1,000,000 messages
13:40:18 [2] Starting Core NATS subscriber, expecting 1,000,000 messages
13:40:18 [3] Starting Core NATS subscriber, expecting 1,000,000 messages
13:40:18 [4] Starting Core NATS subscriber, expecting 1,000,000 messages
Finished      0s [============================================================] 100%
Finished      0s [============================================================] 100%
Finished      0s [============================================================] 100%
Finished      0s [============================================================] 100%

  [1] 1,080,830 msgs/sec ~ 132 MiB/sec ~ 0.93us (1,000,000 msgs)
  [2] 1,080,869 msgs/sec ~ 132 MiB/sec ~ 0.93us (1,000,000 msgs)
  [3] 1,080,849 msgs/sec ~ 132 MiB/sec ~ 0.93us (1,000,000 msgs)
  [4] 1,080,821 msgs/sec ~ 132 MiB/sec ~ 0.93us (1,000,000 msgs)

 NATS Core NATS subscriber aggregated stats: 4,323,201 msgs/sec ~ 528 MiB/sec
 message rates min 1,080,821 | avg 1,080,842 | max 1,080,869 | stddev 18 msgs
 avg latencies min 0.93us | avg 0.93us | max 0.93us | stddev 0.00us
```

## Run a request-reply latency test

You can also test request/reply performance using `nats bench service`.

In one shell start a nats bench to act as a server and let it run:

```bash
nats bench service serve foo
```

And in another shell send some requests (each request is sent synchronously, one after the other):

```bash
nats bench service request foo
```

```
13:46:43 Starting Core NATS service requester benchmark [clients=1, msg-size=128 B, msgs=100,000, sleep=0s, subject=foo]
13:46:43 [1] Starting Core NATS service requester, requesting 100,000 messages
Finished      5s [================================================================] 100%

NATS Core NATS service requester stats: 19,659 msgs/sec ~ 2.4 MiB/sec ~ 50.87us
```

In this case, the average latency of request-reply between the two `nats bench` processes over NATS was 50.87 micro-seconds. However, since those requests are made synchronously, we can not measure throughput this way. We need to generate a lot more load by having more than one client making those synchronous requests at the same time, and we will also run more than one service instance (as you would in production) such that the requests are load-balanced between the service instances using the queue group functionality.

Start the service instances and leave running:

```bash
nats bench service serve foo --size 16 --clients 2
```

Clients making requests (since we are using a lot of clients to generate load, we will not show the progress bar while running the benchmark):

```bash
nats bench service request foo --size 16 --clients 50 --no-progress
```

```
13:57:56 Starting Core NATS service requester benchmark [clients=50, msg-size=16 B, msgs=100,000, sleep=0s, subject=foo]
13:57:56 [1] Starting Core NATS service requester, requesting 2,000 messages
13:57:56 [2] Starting Core NATS service requester, requesting 2,000 messages
...
13:57:56 [49] Starting Core NATS service requester, requesting 2,000 messages
13:57:56 [50] Starting Core NATS service requester, requesting 2,000 messages

  [1] 2,735 msgs/sec ~ 43 KiB/sec ~ 365.62us (2,000 msgs)
  [2] 2,700 msgs/sec ~ 42 KiB/sec ~ 370.24us (2,000 msgs)
  ...
  [49] 2,651 msgs/sec ~ 41 KiB/sec ~ 377.14us (2,000 msgs)
  [50] 2,649 msgs/sec ~ 41 KiB/sec ~ 377.48us (2,000 msgs)

 NATS Core NATS service requester aggregated stats: 132,438 msgs/sec ~ 2.0 MiB/sec
 message rates min 2,649 | avg 2,673 | max 2,735 | stddev 17 msgs
 avg latencies min 365.62us | avg 373.93us | max 377.48us | stddev 2.43us
```

## Run JetStream benchmarks

You can measure JetStream performance using the `nats bench js` commands.

### Measure JetStream publication performance

You can measure the performance of publishing (storing) messages into a stream using `nats bench js pub`, which offers 3 options:

* `nats bench js pub sync` publishes the messages synchronously one after the other (so while it's good for measuring latency, it's not good to measure throughput).
* `nats bench js pub async` publishes a batch of messages asynchronously, waits for all the publications' acknowledgements and moves on to the next batch (which is a good way to measure throughput).
* `nats bench js pub batch` uses the atomic batch publish (while batching is currently implemented only to provide atomicity, it has the side effect of potentially helping throughout, especially for smaller messages).
*

`nats bench js pub` will by default use a stream called `benchstream`, and `--create` will automatically create the stream if it doesn't exist yet. Also you can use `--purge` to clear the stream first. You can specify stream attributes like `--replicas 3` or `--storage memory`, or `--maxbytes` or operate on any existing stream with `--stream`.

For example, test latency of publishing to a memory stream:

```bash
nats bench js pub sync jsfoo --size 16 --create --storage memory
```

```
18:47:47 Starting JetStream synchronous publisher benchmark [batch=0, clients=1, dedup-window=2m0s, deduplication=false, max-bytes=1,073,741,824, msg-size=16 B, msgs=100,000, multi-subject=false, multi-subject-max=100,000, purge=false, replicas=1, sleep=0s, storage=memory, stream=benchstream, subject=jsfoo]
18:47:47 Using stream: benchstream
18:47:47 [1] Starting JetStream synchronous publisher, publishing 100,000 messages
Publishing    2s [================================================================] 100%

NATS JetStream synchronous publisher stats: 35,734 msgs/sec ~ 558 KiB/sec ~ 27.98us
```

Test throughput using batch publishing:

```bash
nats bench js pub batch jsfoo --size 16 --batch 1000 --purge --storage memory
```

```
18:51:27 Starting JetStream batched publisher benchmark [batch=1,000, clients=1, msg-size=16 B, msgs=100,000, multi-subject=false, multi-subject-max=100,000, purge=true, sleep=0s, stream=benchstream, subject=jsfoo]
18:51:27 Using stream: benchstream
18:51:27 Purging the stream
18:51:27 [1] Starting JetStream batched publisher, publishing 100,000 messages
Finished      0s [================================================================] 100%

NATS JetStream batched publisher stats: 627,430 msgs/sec ~ 9.6 MiB/sec ~ 1.59us
```

Remove the stream and test to file storage (which is the default)

```bash
nats stream rm -f benchstream
nats bench js pub async jsfoo --create
```

```
13:09:34 Starting JetStream asynchronous publisher benchmark [batch=500, clients=1, dedup-window=2m0s, deduplication=false, max-bytes=1,073,741,824, msg-size=128 B, msgs=100,000, multi-subject=false, multi-subject-max=100,000, purge=false, replicas=1, sleep=0s, storage=file, stream=benchstream, subject=jsfoo]
13:09:34 Using stream: benchstream
13:09:34 [1] Starting JetStream asynchronous publisher, publishing 100,000 messages
Finished      0s [================================================================] 100%

NATS JetStream asynchronous publisher stats: 403,828 msgs/sec ~ 49 MiB/sec ~ 2.48us
```

You can even measure publish performance to an `--replicas 1` stream with asynchronous persistence using `--persistasync` which yields throughput similar to when using memory storage, as by default JetStream flushes disk writes synchronously, meaning that even if the `nats-server` process is killed suddenly no messages will be lost as the OS already has them in it's buffer and will flush them to disk (it can be also configured to not just flush but also sync after every write in which case no message will be lost even if the whole host goes down suddenly, at the expense of latency obviously)).

### Measure JetStream consumption (replay) performance

Once you have stored some messages on a stream you can measure the replay performance in multiple ways:

* `nats bench js ordered` uses an ordered *ephemeral* consumer to receive the messages (so each client gets its own copy of the messages).
* `nats bench js consume` uses the `Consume()` (callback) function on a *durable* consumer to receive the messages.
* `nats bench js fetch` uses the `Fetch()` function on a *durable* consumer to receive messages in batches.
* `nats bench js get` gets the messages directly by sequence number (either synchronously one by one or using 'batched gets') *without using a consumer*.

Starting with ordered consumer:

```bash
nats bench js ordered
```

```
13:33:48 Starting JetStream ordered ephemeral consumer benchmark [clients=1, msg-size=128 B, msgs=100,000, purge=false, sleep=0s, stream=benchstream]
13:33:48 [1] Starting JetStream ordered ephemeral consumer, expecting 100,000 messages
Finished      0s [================================================================] 100%

NATS JetStream ordered ephemeral consumer stats: 1,201,540 msgs/sec ~ 147 MiB/sec ~ 0.83us
```

Then using consume to distribute consumption of messages between multiple clients throught a durable consumer with explicit acknowledgements:

```bash
nats bench js consume --clients 4 --no-progress
```

```
13:46:04 Starting JetStream durable consumer (callback) benchmark [acks=explicit, batch=500, clients=4, consumer=nats-bench, double-acked=false, msg-size=128 B, msgs=100,000, purge=false, sleep=0s, stream=benchstream]
13:46:04 [1] Starting JetStream durable consumer (callback), expecting 25,000 messages
13:46:04 [2] Starting JetStream durable consumer (callback), expecting 25,000 messages
13:46:04 [3] Starting JetStream durable consumer (callback), expecting 25,000 messages
13:46:04 [4] Starting JetStream durable consumer (callback), expecting 25,000 messages

  [1] 73,230 msgs/sec ~ 8.9 MiB/sec ~ 13.66us (25,000 msgs)
  [2] 72,921 msgs/sec ~ 8.9 MiB/sec ~ 13.71us (25,000 msgs)
  [3] 72,696 msgs/sec ~ 8.9 MiB/sec ~ 13.76us (25,000 msgs)
  [4] 72,687 msgs/sec ~ 8.9 MiB/sec ~ 13.76us (25,000 msgs)

 NATS JetStream durable consumer (callback) aggregated stats: 290,438 msgs/sec ~ 36 MiB/sec
 message rates min 72,687 | avg 72,883 | max 73,230 | stddev 220 msgs
 avg latencies min 13.66us | avg 13.72us | max 13.76us | stddev 0.04us
```

Using fetch with two clients to retrieve batches of 400 messages through a durable consumer and without explicit acknowledgements:

```bash
nats bench js fetch --acks none --clients 2
```

```
14:09:10 Starting JetStream durable consumer (fetch) benchmark [acks=none, batch=500, clients=2, consumer=nats-bench, double-acked=false, msg-size=128 B, msgs=100,000, purge=false, sleep=0s, stream=benchstream]
14:09:10 [1] Starting JetStream durable consumer (fetch), expecting 50,000 messages
14:09:10 [2] Starting JetStream durable consumer (fetch), expecting 50,000 messages
Finished      0s [================================================================] 100%
Finished      0s [================================================================] 100%

  [1] 567,330 msgs/sec ~ 69 MiB/sec ~ 1.76us (50,000 msgs)
  [2] 567,067 msgs/sec ~ 69 MiB/sec ~ 1.76us (50,000 msgs)

 NATS JetStream durable consumer (fetch) aggregated stats: 1,128,932 msgs/sec ~ 138 MiB/sec
 message rates min 567,067 | avg 567,198 | max 567,330 | stddev 131 msgs
 avg latencies min 1.76us | avg 1.76us | max 1.76us | stddev 0.00us
```

Measuring the latency of direct synchronous gets:

```bash
nats bench js get sync
```

```
14:13:30 Starting JetStream synchronous getter benchmark [clients=1, msg-size=128 B, msgs=100,000, sleep=0s, stream=benchstream]
14:13:30 [1] Starting JetStream synchronous getter, expecting 100,000 messages
Finished      3s [================================================================] 100%

NATS JetStream synchronous getter stats: 33,244 msgs/sec ~ 4.1 MiB/sec ~ 30.08us
```

And finally measuring throughput using batched gets with a fan out of 2:

```bash
nats bench js get batch --clients 2
```

```
14:11:09 Starting JetStream batched direct getter benchmark [batch=500, clients=2, filter=>, msg-size=128 B, msgs=100,000, sleep=0s, stream=benchstream]
14:11:09 [1] Starting JetStream batched direct getter, expecting 100,000 messages
14:11:09 [2] Starting JetStream batched direct getter, expecting 100,000 messages
Finished      0s [================================================================] 100%
Finished      0s [================================================================] 100%

  [1] 509,387 msgs/sec ~ 62 MiB/sec ~ 1.96us (100,000 msgs)
  [2] 500,449 msgs/sec ~ 61 MiB/sec ~ 2.00us (100,000 msgs)

 NATS JetStream batched direct getter aggregated stats: 1,000,898 msgs/sec ~ 122 MiB/sec
 message rates min 500,449 | avg 504,918 | max 509,387 | stddev 4,469 msgs
 avg latencies min 1.96us | avg 1.98us | max 2.00us | stddev 0.02us
```

### Measuring publication and consumption together

While measuring publication and consumption to and from a stream separately yields interesting metrics, during normal operations most of the time the consumers are going to be on-line and consuming while the messages are being published to the stream.

First purge the stream and start the consuming instance of `nats bench`, for example using an ordered consumer and 8 clients (so a fan out of 8):

```bash
nats bench js ordered --purge --clients 8 --no-progress
```

Then start publishing to the stream, for example using 8 clients doing asynchronous publications:

```bash
nats bench js pub async jsfoo --clients 8 --no-progress
```

```
15:23:08 Starting JetStream asynchronous publisher benchmark [batch=500, clients=8, msg-size=128 B, msgs=100,000, multi-subject=false, multi-subject-max=100,000, purge=false, sleep=0s, stream=benchstream, subject=jsfoo]
15:23:08 Using stream: benchstream
15:23:08 [1] Starting JetStream asynchronous publisher, publishing 12,500 messages
15:23:08 [2] Starting JetStream asynchronous publisher, publishing 12,500 messages
...
15:23:08 [7] Starting JetStream asynchronous publisher, publishing 12,500 messages
15:23:08 [8] Starting JetStream asynchronous publisher, publishing 12,500 messages

  [1] 33,289 msgs/sec ~ 4.1 MiB/sec ~ 30.04us (12,500 msgs)
  [2] 33,242 msgs/sec ~ 4.1 MiB/sec ~ 30.08us (12,500 msgs)
  ...
  [7] 31,947 msgs/sec ~ 3.9 MiB/sec ~ 31.30us (12,500 msgs)
  [8] 31,586 msgs/sec ~ 3.9 MiB/sec ~ 31.66us (12,500 msgs)

 NATS JetStream asynchronous publisher aggregated stats: 252,544 msgs/sec ~ 31 MiB/sec
 message rates min 31,586 | avg 32,614 | max 33,289 | stddev 638 msgs
 avg latencies min 30.04us | avg 30.67us | max 31.66us | stddev 0.60us 
```

Consumer's output:

```
15:23:02 Starting JetStream ordered ephemeral consumer benchmark [clients=8, msg-size=128 B, msgs=100,000, purge=true, sleep=0s, stream=benchstream]
15:23:02 [1] Starting JetStream ordered ephemeral consumer, expecting 100,000 messages
15:23:02 [2] Starting JetStream ordered ephemeral consumer, expecting 100,000 messages
...
15:23:02 [7] Starting JetStream ordered ephemeral consumer, expecting 100,000 messages
15:23:02 [8] Starting JetStream ordered ephemeral consumer, expecting 100,000 messages

  [1] 111,627 msgs/sec ~ 14 MiB/sec ~ 8.96us (100,000 msgs)
  [2] 110,534 msgs/sec ~ 14 MiB/sec ~ 9.05us (100,000 msgs)
  ...
  [7] 109,849 msgs/sec ~ 13 MiB/sec ~ 9.10us (100,000 msgs)
  [8] 109,797 msgs/sec ~ 13 MiB/sec ~ 9.11us (100,000 msgs)

 NATS JetStream ordered ephemeral consumer aggregated stats: 878,326 msgs/sec ~ 107 MiB/sec
 message rates min 109,797 | avg 110,306 | max 111,627 | stddev 556 msgs
 avg latencies min 8.96us | avg 9.07us | max 9.11us | stddev 0.05us
```

### Measure KV performance

`nats bench kv` can be used to measure Key Value performance using synchronous put and get operations.

First put some data in the KV:

```bash
nats bench kv put
```

```
14:26:04 Starting JetStream KV putter benchmark [bucket=benchbucket, clients=1, msg-size=128 B, msgs=100,000, purge=false, sleep=0s]
14:26:04 [1] Starting JetStream KV putter, publishing 100,000 messages
Putting       3s [================================================================] 100%

NATS JetStream KV putter stats: 30,067 msgs/sec ~ 3.7 MiB/sec ~ 33.26us
```

Then simulate a bunch of clients doing gets on random keys:

```bash
nats bench kv get --clients 16 --randomize 100000 --no-progress
```

```
14:28:33 Starting JetStream KV getter benchmark [bucket=benchbucket, clients=16, msg-size=128 B, msgs=100,000, randomize=100,000, sleep=0s]
14:28:33 [1] Starting JetStream KV getter, trying to get 6,250 messages
14:28:33 [2] Starting JetStream KV getter, trying to get 6,250 messages
...
14:28:33 [15] Starting JetStream KV getter, trying to get 6,250 messages
14:28:33 [16] Starting JetStream KV getter, trying to get 6,250 messages

  [1] 6,568 msgs/sec ~ 821 KiB/sec ~ 152.23us (6,250 msgs)
  [2] 6,579 msgs/sec ~ 822 KiB/sec ~ 151.98us (6,250 msgs)
  ...
  [15] 6,474 msgs/sec ~ 809 KiB/sec ~ 154.45us (6,250 msgs)
  [16] 6,451 msgs/sec ~ 806 KiB/sec ~ 155.01us (6,250 msgs)

 NATS JetStream KV getter aggregated stats: 102,844 msgs/sec ~ 13 MiB/sec
 message rates min 6,448 | avg 6,509 | max 6,579 | stddev 40 msgs
 avg latencies min 151.98us | avg 153.61us | max 155.08us | stddev 0.96us
```

### Play around with the knobs

Don't be afraid to test different JetStream storage and replication options (assuming you have access to a JetStream enabled cluster of servers if you want to go beyond `--replicas 1`), and of course the number of publishing/subscribing clients, and the batch and message sizes.

You can also use `nats bench` as a tool to generate traffic at a steady rate by using the `--sleep` flag to introduce a delay between the publication of each message (or batch of messages). You can also use that same flag to simulate processing time when consuming messages.

Note: If you change the attributes of a stream between runs you will have to delete the stream (e.g. run `nats stream rm benchstream`)

### Leave no trace: clean up the resources when you are finished

Once you have finished benchmarking streams, remember that if you have stored many messages in the stream (which is very easy and fast to do) your stream may end up using a certain amount of resources on the nats-server(s) infrastructure (i.e. memory and files) that you may want to reclaim.

You can instruct use the `--purge` bench command flag to tell `nats` to purge the stream of messages before starting its benchmark, or purge the stream manually using `nats stream purge benchstream` or just delete it altogether using `nats stream rm benchstream`.


# nk

`nk` is a command line tool that generates `nkeys`. NKeys are a highly secure public-key signature system based on [Ed25519](https://ed25519.cr.yp.to/).

With NKeys the server can verify identity without ever storing secrets on the server. The authentication system works by requiring a connecting client to provide its public key and digitally sign a challenge with its private key. The server generates a random challenge with every connection request, making it immune to playback attacks. The generated signature is validated a public key, thus proving the identity of the client. If the public key validation succeeds, authentication succeeds.

> NKey is an awesome replacement for token authentication, because a connecting client will have to prove it controls the private key for the authorized public key.

## Installing nk

To get started with NKeys, you’ll need the `nk` tool from <https://github.com/nats-io/nkeys/tree/master/nk> repository. If you have *go* installed, enter the following at a command prompt:

```bash
go install github.com/nats-io/nkeys/nk@latest
```

## Generating NKeys and Configuring the Server

To generate a *User* NKEY:

```shell
nk -gen user -pubout
```

```
SUACSSL3UAHUDXKFSNVUZRF5UHPMWZ6BFDTJ7M6USDXIEDNPPQYYYCU3VY
UDXU4RCSJNZOIQHZNWXHXORDPRTGNJAHAHFRGZNEEJCPQTT2M7NLCNF4
```

The first output line starts with the letter `S` for *Seed*. The second letter `U` stands for *User*. Seeds are private keys; you should treat them as secrets and guard them with care.

The second line starts with the letter `U` for *User*, and is a public key which can be safely shared.

To use `nkey` authentication, add a user, and set the `nkey` property to the public key of the user you want to authenticate. You are only required to use the public key and no other properties are required. Here is a snippet of configuration for the `nats-server`:

```
authorization: {
  users: [
    { nkey: UDXU4RCSJNZOIQHZNWXHXORDPRTGNJAHAHFRGZNEEJCPQTT2M7NLCNF4 }
  ]
}
```

To complete the end-to-end configuration and use an `nkey`, the [client is configured](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth#client-configuration) to use the seed, which is the private key.


# nsc

NATS account configurations are built using the `nsc` tool. The NSC tool allows you to:

* Create and edit Operators, Accounts, Users
* Manage publish and subscribe permissions for Users
* Define Service and Stream exports from an account
* Reference Service and Streams from another account
* Generate Activation tokens that grants access to a private service or stream
* Generate User credential files
* Describe Operators, Accounts, Users, and Activations
* Push and pull account JWTs to an account JWTs server

## Installation

Installing `nsc` is easy:

```shell
curl -L https://raw.githubusercontent.com/nats-io/nsc/master/install.py | python
```

> Additional ways of installing nsc are described at [nsc's github repository](https://github.com/nats-io/nsc#install)

The script will download the latest version of `nsc` and install it into your system.

In case NSC is not initialized already do `nsc init`

Output of `tree -L 2 nsc/`

```
nsc/
├── accounts
│   ├── nats
│   └── nsc.json
└── nkeys
    ├── creds
    └── keys
5 directories, 1 file
```

**IMPORTANT**: `nsc` version 2.2.0 has been released. This version of nsc only supports `nats-server` v2.2.0 and `nats-account-server` v1.0.0. For more information please refer to the [nsc 2.2.0 release notes](https://github.com/nats-io/nsc/releases/tag/2.2.0).

## Tutorials

You can find various task-oriented tutorials to working with the tool here:

* [Basic Usage](https://docs.nats.io/using-nats/nats-tools/nsc/basics)
* [Configuring Account Streams Import/Export](https://docs.nats.io/using-nats/nats-tools/nsc/streams)
* [Configuring Account Services Import/Export](https://docs.nats.io/using-nats/nats-tools/nsc/services)
* [Signing Keys](https://docs.nats.io/using-nats/nats-tools/nsc/signing_keys)
* [Revoking Users or Activations](https://docs.nats.io/using-nats/nats-tools/nsc/revocation)
* [Working with Managed Operators](https://docs.nats.io/using-nats/nats-tools/nsc/managed)

## Tool Documentation

For more specific browsing of the tool syntax, check out the `nsc` tool documentation. It can be found within the tool itself:

```shell
nsc help
```

Or an online version [here](https://nats-io.github.io/nsc).


# Basics

NSC allows you to manage identities. Identities take the form of *nkeys*. Nkeys are a public-key signature system based on Ed25519 for the NATS ecosystem.

The nkey identities are associated with NATS configuration in the form of a JSON Web Token (JWT). The JWT is digitally signed by the private key of an issuer forming a chain of trust. The `nsc` tool creates and manages these identities and allows you to deploy them to a JWT account server, which in turn makes the configurations available to nats-servers.

There’s a logical hierarchy to the entities:

* `Operators` are responsible for running nats-servers, and issuing account JWTs. Operators set the limits on what an account can do, such as the number of connections, data limits, etc.
* `Accounts` are responsible for issuing user JWTs. An account defines streams and services that can be exported to other accounts. Likewise, they import streams and services from other accounts.
* `Users` are issued by an account, and encode limits regarding usage and authorization over the account's subject space.

NSC allows you to create, edit, and delete these entities, and will be central to all account-based configuration.

In this guide, you’ll run end-to-end on some of the configuration scenarios:

* Generate NKey identities and their associated JWTs
* Make JWTs accessible to a nats-server
* Configure a nats-server to use JWTs

Let’s run through the process of creating some identities and JWTs and work through the process.

## Creating an Operator, Account and User

Let’s create an operator called `MyOperator`.

*There is an additional switch `--sys` that sets up the system account which is required for interacting with the NATS server. You can create and set the system account later.*

```bash
nsc add operator MyOperator
```

```
[ OK ] generated and stored operator key "ODSWWTKZLRDFBPXNMNAY7XB2BIJ45SV756BHUT7GX6JQH6W7AHVAFX6C"
[ OK ] added operator "MyOperator"
[ OK ] When running your own nats-server, make sure they run at least version 2.2.0
```

With the above command, the tool generated an NKEY for the operator, stored the private key safely in its keystore.

Lets add a service URL to the operator. Service URLs specify where the nats-server is listening. Tooling such as `nsc` can make use of that configuration:

```bash
nsc edit operator --service-url nats://localhost:4222
```

```
[ OK ] added service url "nats://localhost:4222"
[ OK ] edited operator "MyOperator"
```

Creating an account is just as easy:

```bash
nsc add account MyAccount
```

```
[ OK ] generated and stored account key "AD2M34WBNGQFYK37IDX53DPRG74RLLT7FFWBOBMBUXMAVBCVAU5VKWIY"
[ OK ] added account "MyAccount"
```

As expected, the tool generated an NKEY representing the account and stored the private key safely in the keystore.

Finally, let's create a user:

```bash
nsc add user MyUser
```

```
[ OK ] generated and stored user key "UAWBXLSZVZHNDIURY52F6WETFCFZLXYUEFJAHRXDW7D2K4445IY4BVXP"
[ OK ] generated user creds file `~/.nkeys/creds/MyOperator/MyAccount/MyUser.creds`
[ OK ] added user "MyUser" to account "MyAccount"
```

As expected, the tool generated an NKEY representing the user, and stored the private key safely in the keystore. In addition, the tool generated a *credentials* file. A credentials file contains the JWT for the user and the private key for the user. Credential files are used by NATS clients to identify themselves to the system. The client will extract and present the JWT to the nats-server and use the private key to verify its identity.

### NSC Assets

NSC manages three different directories:

* The nsc home directory which stores nsc related data. By default nsc home lives in `~/.nsc` and can be changed via the `$NSC_HOME` environment variable.
* An *nkeys* directory, which stores all the private keys. This directory by default lives in `~/.nkeys` and can be changed via the `$NKEYS_PATH` environment variable. The contents of the nkeys directory should be treated as secrets.
* A *stores* directory, which contains JWTs representing the various entities. This directory lives in `$NSC_HOME/nats`, and can be changed using the command `nsc env -s <dir>`. The stores directory can stored under revision control. The JWTs themselves do not contain any secrets.

#### The NSC Stores Directory

The stores directory contains a number of directories. Each named by an operator in question, which in turn contains all accounts and users:

```bash
tree ~/.nsc/nats
```

```
/Users/myusername/.nsc/nats
└── MyOperator
    ├── MyOperator.jwt
    └── accounts
        └── MyAccount
            ├── MyAccount.jwt
            └── users
                └── MyUser.jwt
```

These JWTs are the same artifacts that the NATS servers will use to check the validity of an account, its limits, and the JWTs that are presented by clients when they connect to the nats-server.

#### The NKEYS Directory

The nkeys directory contains all the private keys and credential files. As mentioned before, care must be taken to keep these files secure.

The structure keys directory is machine friendly. All keys are sharded by their kind `O` for operators, `A` for accounts, `U` for users. These prefixes are also part of the public key. The second and third letters in the public key are used to create directories where other like-named keys are stored.

```shell
tree ~/.nkeys
```

```
/Users/myusername/.nkeys
├── creds
│   └── MyOperator
│       └── MyAccount
│           └── MyUser.creds
└── keys
    ├── A
    │   └── DE
    │       └── ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE.nk
    ├── O
    │   └── AF
    │       └── OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG.nk
    └── U
        └── DB
            └── UDBD5FNQPSLIO6CDMIS5D4EBNFKYWVDNULQTFTUZJXWFNYLGFF52VZN7.nk
```

The `nk` files themselves are named after the complete public key, and stored in a single string - the private key in question:

```bash
cat ~/.nkeys/keys/U/DB/UDBD5FNQPSLIO6CDMIS5D4EBNFKYWVDNULQTFTUZJXWFNYLGFF52VZN7.nk 
```

```
SUAG35IAY2EF5DOZRV6MUSOFDGJ6O2BQCZHSRPLIK6J3GVCX366BFAYSNA
```

The private keys are encoded into a string, and always begin with an `S` for *seed*. The second letter starts with the type of key in question. `O` for operators, `A` for accounts, `U` for users.

In addition to containing keys, the nkeys directory contains a `creds` directory. This directory is organized in a way friendly to humans. It stores user credential files or `creds` files for short. A credentials file contains a copy of the user JWT and the private key for the user. These files are used by NATS clients to connect to a NATS server:

```bash
cat ~/.nkeys/creds/MyOperator/MyAccount/MyUser.creds
```

```
-----BEGIN NATS USER JWT-----
eyJ0eXAiOiJKV1QiLCJhbGciOiJlZDI1NTE5LW5rZXkifQ.eyJqdGkiOiI0NUc3MkhIQUVCRFBQV05ZWktMTUhQNUFYWFRSSUVDQlNVQUI2VDZRUjdVM1JZUFZaM05BIiwiaWF0IjoxNjM1Mzc1NTYxLCJpc3MiOiJBRDJNMzRXQk5HUUZZSzM3SURYNTNEUFJHNzRSTExUN0ZGV0JPQk1CVVhNQVZCQ1ZBVTVWS1dJWSIsIm5hbWUiOiJNeVVzZXIiLCJzdWIiOiJVQVdCWExTWlZaSE5ESVVSWTUyRjZXRVRGQ0ZaTFhZVUVGSkFIUlhEVzdEMks0NDQ1SVk0QlZYUCIsIm5hdHMiOnsicHViIjp7fSwic3ViIjp7fSwic3VicyI6LTEsImRhdGEiOi0xLCJwYXlsb2FkIjotMSwidHlwZSI6InVzZXIiLCJ2ZXJzaW9uIjoyfX0.CGymhGYHfdZyhUeucxNs9TthSjy_27LVZikqxvm-pPLili8KNe1xyOVnk_w-xPWdrCx_t3Se2lgXmoy3wBcVCw
------END NATS USER JWT------

************************* IMPORTANT *************************
NKEY Seed printed below can be used to sign and prove identity.
NKEYs are sensitive and should be treated as secrets.

-----BEGIN USER NKEY SEED-----
SUAP2AY6UAWHOXJBWDNRNKJ2DHNC5VA2DFJZTF6C6PMLKUCOS2H2E2BA2E
------END USER NKEY SEED------

*************************************************************
```

### Listing Keys

You can list the current entities you are working with by doing:

```bash
nsc list keys
```

```
+----------------------------------------------------------------------------------------------+
|                                             Keys                                             |
+------------+----------------------------------------------------------+-------------+--------+
| Entity     | Key                                                      | Signing Key | Stored |
+------------+----------------------------------------------------------+-------------+--------+
| MyOperator | ODSWWTKZLRDFBPXNMNAY7XB2BIJ45SV756BHUT7GX6JQH6W7AHVAFX6C |             | *      |
|  MyAccount | AD2M34WBNGQFYK37IDX53DPRG74RLLT7FFWBOBMBUXMAVBCVAU5VKWIY |             | *      |
|   MyUser   | UAWBXLSZVZHNDIURY52F6WETFCFZLXYUEFJAHRXDW7D2K4445IY4BVXP |             | *      |
+------------+----------------------------------------------------------+-------------+--------+
```

The different entity names are listed along with their public key, and whether the key is stored. Stored keys are those that are found in the nkeys directory.

In some cases you may want to view the private keys:

```shell
nsc list keys --show-seeds
```

```
+---------------------------------------------------------------------------------------+
|                                      Seeds Keys                                       |
+------------+------------------------------------------------------------+-------------+
| Entity     | Private Key                                                | Signing Key |
+------------+------------------------------------------------------------+-------------+
| MyOperator | SOAJ3JDZBE6JKJO277CQP5RIAA7I7HBI44RDCMTIV3TQRYQX35OTXSMHAE |             |
|  MyAccount | SAAACXWSQIKJ4L2SEAUZJR3BCNSRCN32V5UJSABCSEP35Q7LQRPV6F4JPI |             |
|   MyUser   | SUAP2AY6UAWHOXJBWDNRNKJ2DHNC5VA2DFJZTF6C6PMLKUCOS2H2E2BA2E |             |
+------------+------------------------------------------------------------+-------------+
[ ! ] seed is not stored
[ERR] error reading seed
```

If you don't have the seed (perhaps you don't control the operator), nsc will decorate the row with a `!`. If you have more than one account, you can show them all by specifying the `--all` flag.

## The Operator JWT

You can view a human readable version of the JWT by using `nsc`:

```bash
nsc describe operator
```

```
+----------------------------------------------------------------------------------+
|                                 Operator Details                                 |
+-----------------------+----------------------------------------------------------+
| Name                  | MyOperator                                               |
| Operator ID           | ODSWWTKZLRDFBPXNMNAY7XB2BIJ45SV756BHUT7GX6JQH6W7AHVAFX6C |
| Issuer ID             | ODSWWTKZLRDFBPXNMNAY7XB2BIJ45SV756BHUT7GX6JQH6W7AHVAFX6C |
| Issued                | 2021-10-27 22:58:28 UTC                                  |
| Expires               |                                                          |
| Operator Service URLs | nats://localhost:4222                                    |
| Require Signing Keys  | false                                                    |
+-----------------------+----------------------------------------------------------+
```

Since the operator JWT is just a JWT you can use other tools, such as jwt.io to decode a JWT and inspect its contents. All JWTs have a header, payload, and signature:

```
{
  "typ": "jwt",
  "alg": "ed25519"
}
{
  "jti": "ZP2X3T2R57SLXD2U5J3OLLYIVW2LFBMTXRPMMGISQ5OF7LANUQPQ",
  "iat": 1575468772,
  "iss": "OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG",
  "name": "O",
  "sub": "OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG",
  "type": "operator",
  "nats": {
    "operator_service_urls": [
      "nats://localhost:4222"
    ]
  }
}
```

All NATS JWTs will use the `algorithm` ed25519 for signature. The payload will list different things. On our basically empty operator, we will only have standard JWT `claim` fields:

`jti` - a jwt id `iat` - the timestamp when the JWT was issued in UNIX time `iss` - the issuer of the JWT, in this case the operator's public key `sub` - the subject or identity represented by the JWT, in this case the same operator `type` - since this is an operator JWT, `operator` is the type

NATS specific is the `nats` object, which is where we add NATS specific JWT configuration to the JWT claim.

Because the issuer and subject are one and the same, this JWT is self-signed.

### The Account JWT

Again we can inspect the account:

```bash
nsc describe account
```

```
+--------------------------------------------------------------------------------------+
|                                   Account Details                                    |
+---------------------------+----------------------------------------------------------+
| Name                      | MyAccount                                                |
| Account ID                | AD2M34WBNGQFYK37IDX53DPRG74RLLT7FFWBOBMBUXMAVBCVAU5VKWIY |
| Issuer ID                 | ODSWWTKZLRDFBPXNMNAY7XB2BIJ45SV756BHUT7GX6JQH6W7AHVAFX6C |
| Issued                    | 2021-10-27 22:59:01 UTC                                  |
| Expires                   |                                                          |
+---------------------------+----------------------------------------------------------+
| Max Connections           | Unlimited                                                |
| Max Leaf Node Connections | Unlimited                                                |
| Max Data                  | Unlimited                                                |
| Max Exports               | Unlimited                                                |
| Max Imports               | Unlimited                                                |
| Max Msg Payload           | Unlimited                                                |
| Max Subscriptions         | Unlimited                                                |
| Exports Allows Wildcards  | True                                                     |
| Response Permissions      | Not Set                                                  |
+---------------------------+----------------------------------------------------------+
| Jetstream                 | Disabled                                                 |
+---------------------------+----------------------------------------------------------+
| Imports                   | None                                                     |
| Exports                   | None                                                     |
+---------------------------+----------------------------------------------------------+
```

### The User JWT

Finally the user JWT:

```bash
nsc describe user
```

```
+---------------------------------------------------------------------------------+
|                                      User                                       |
+----------------------+----------------------------------------------------------+
| Name                 | MyUser                                                   |
| User ID              | UAWBXLSZVZHNDIURY52F6WETFCFZLXYUEFJAHRXDW7D2K4445IY4BVXP |
| Issuer ID            | AD2M34WBNGQFYK37IDX53DPRG74RLLT7FFWBOBMBUXMAVBCVAU5VKWIY |
| Issued               | 2021-10-27 22:59:21 UTC                                  |
| Expires              |                                                          |
| Bearer Token         | No                                                       |
| Response Permissions | Not Set                                                  |
+----------------------+----------------------------------------------------------+
| Max Msg Payload      | Unlimited                                                |
| Max Data             | Unlimited                                                |
| Max Subs             | Unlimited                                                |
| Network Src          | Any                                                      |
| Time                 | Any                                                      |
+----------------------+----------------------------------------------------------+
```

The user id is the public key for the user, the issuer is the account. This user can publish and subscribe to anything, as no limits are set.

When a user connects to a nats-server, it presents it's user JWT and signs a nonce using its private key. The server verifies if the user is who they say they are by validating that the nonce was signed using the private key associated with the public key, representing the identify of the user. Next, the server fetches the issuer account and validates that the account was issued by a trusted operator completing the chain of trust verification.

Let’s put all of this together, and create a simple server configuration that accepts sessions from `U`.

## Account Server Configuration

To configure a server to use accounts, you need to configure it to select the type of *account resolver* it will use. The preferred option being to configure the server to use the built-in [NATS Based Resolver](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/jwt/resolver#nats-based-resolver).

## NATS Server Configuration

If you don’t have a nats-server installed, let’s do that now:

```shell
go get github.com/nats-io/nats-server
```

Let’s create a configuration that references our operator JWT and the nats-account-server as a resolver. You can use `nsc` itself to generate the security part of the server configuration that you can just add to your `nats-server` config file.

For example to use the NATS resolver (which is the recommended resolver configuration) use `nsc generate config --nats-resolver`.

Edit this generated configuration as needed (e.g. adjust the location where the server will store the JWTs in `resolver.dir`) and paste it into your nats-server configuration (or save it to a file and import that file from within you server config file).

At minimum, the server requires the `operator` JWT, which we have pointed at directly, and a resolver.

e.g.

```shell
nsc generate config --nats-resolver > resolver.conf
```

And example server config `myconfig.cfg`

```
server_name: servertest
listen: 127.0.0.1:4222
http: 8222

jetstream: enabled

include resolver.conf
```

Now start this local test server using `nats-server -c myconfig.cfg`

The nats-server requires a designated account for operations and monitoring of the server, cluster, or supercluster. If you see this error message:

`nats-server: using nats based account resolver - the system account needs to be specified in configuration or the operator jwt`

Then there is no system account to interact with the server and you need to add one to the configuration or operator JWT. Let’s add one to the operator JWT using `nsc`:

```shell
nsc add account -n SYS`
nsc edit operator --system-account SYS
```

(and re-generate `resolver.conf`)

Now start the local test server using: `nats-server -c myconfig.cfg`

## Pushing the local nsc changes to the nats server

In order for the nats servers to know about the account(s) you have created or changes to the attributes for those accounts, you need to push any new accounts or any changes to account attributes you may have done locally using `nsc` into the built-in account resolver of the nats-server. You can do this using `nsc push`:

For example to push the account named 'MyAccount' that you have just created into the nats server running locally on your machine use:

```shell
nsc push -a MyAccount -u nats://localhost
```

You can also use `nsc pull -u nats://localhost` to pull the view of the accounts that the local NATS server has into your local nsc copy (i.e. in `~/.nsc`)

As soon as you 'push' an the account JWT to the server (that server's built-in NATS account resolver will take care of distributing that new (or new version of) the account JWT to the other nats servers in the cluster) then the changes will take effect and for example any users you may have created with that account will then be able to connect to any of the nats server in the cluster using the user's JWT.

## Client Testing

Install the `nats` CLI Tool if you haven't already.

Create a subscriber:

```shell
nats sub --creds ~/.nkeys/creds/MyOperator/MyAccount/MyUser.creds ">"
```

Publish a message:

```shell
nats pub --creds ~/.nkeys/creds/MyOperator/MyAccount/MyUser.creds hello NATS 
```

Subscriber shows:

```
Received on [hello]: ’NATS’
```

### Create a `nats` context

If you are going to use those credentials with `nats` you should create a context so you don't have to pass the connection and authentication arguments each time:

```shell
nats context add myuser --creds ~/.nkeys/creds/MyOperator/MyAccount/MyUser.creds
```

### NSC Embeds NATS tooling

To make it easier to work, you can use the NATS clients built right into NSC. These tools know how to find the credential files in the keyring. For convenience, the tools are aliased to `sub`, `pub`, `req`, `reply`:

```bash
nsc sub --user MyUser ">"
...

nsc pub --user MyUser hello NATS
...
```

See `nsc tool -h` for more detailed information.

## User Authorization

User authorization, as expected, also works with JWT authentication. With `nsc` you can specify authorization for specific subjects to which the user can or cannot publish or subscribe. By default a user doesn't have any limits on the subjects that it can publish or subscribe to. Any message stream or message published in the account is subscribable by the user. The user can also publish to any subject or imported service. Note that authorization, if configured, must be specified on a per user basis.

When specifying limits it is important to remember that clients by default use generated "inboxes" to allow publish requests. When specifying subscribe and publish permissions, you need to enable clients to subscribe and publish to `_INBOX.>`. You can further restrict it, but you'll be responsible for segmenting the subject space so as to not break request-reply communications between clients.

Let's say you have a service that your account clients can make requests to under `q`. To enable the service to receive and respond to requests it requires permissions to subscribe to `q` and publish permissions under `_INBOX.>`:

```bash
nsc add user s --allow-pub "_INBOX.>" --allow-sub q
```

```
[ OK ] added pub pub "_INBOX.>"
[ OK ] added sub "q"
[ OK ] generated and stored user key "UDYQFIF75SQU2NU3TG4JXJ7C5LFCWAPXX5SSRB276YQOOFXHFIGHXMEL"
[ OK ] generated user creds file `~/.nkeys/creds/MyOperator/MyAccount/s.creds`
[ OK ] added user "s" to account "MyAccount"
```

```shell
nsc describe user s
```

```
+---------------------------------------------------------------------------------+
|                                      User                                       |
+----------------------+----------------------------------------------------------+
| Name                 | s                                                        |
| User ID              | UDYQFIF75SQU2NU3TG4JXJ7C5LFCWAPXX5SSRB276YQOOFXHFIGHXMEL |
| Issuer ID            | AD2M34WBNGQFYK37IDX53DPRG74RLLT7FFWBOBMBUXMAVBCVAU5VKWIY |
| Issued               | 2021-10-27 23:23:16 UTC                                  |
| Expires              |                                                          |
| Bearer Token         | No                                                       |
+----------------------+----------------------------------------------------------+
| Pub Allow            | _INBOX.>                                                 |
| Sub Allow            | q                                                        |
| Response Permissions | Not Set                                                  |
+----------------------+----------------------------------------------------------+
| Max Msg Payload      | Unlimited                                                |
| Max Data             | Unlimited                                                |
| Max Subs             | Unlimited                                                |
| Network Src          | Any                                                      |
| Time                 | Any                                                      |
+----------------------+----------------------------------------------------------+
```

As you can see, this client is now limited to publishing responses to `_INBOX.>` addresses and subscribing to the service's request subject.

Similarly, we can limit a client:

```bash
nsc add user c --allow-pub q --allow-sub "_INBOX.>"
```

```
[ OK ] added pub pub "q"
[ OK ] added sub "_INBOX.>"
[ OK ] generated and stored user key "UDIRTIVVHCW2FLLDHTS27ENXLVNP4EO4Z5MR7FZUNXFXWREPGQJ4BRRE"
[ OK ] generated user creds file `~/.nkeys/creds/MyOperator/MyAccount/c.creds`
[ OK ] added user "c" to account "MyAccount"
```

Lets look at that new user

```shell
nsc describe user c
```

```
+---------------------------------------------------------------------------------+
|                                      User                                       |
+----------------------+----------------------------------------------------------+
| Name                 | c                                                        |
| User ID              | UDIRTIVVHCW2FLLDHTS27ENXLVNP4EO4Z5MR7FZUNXFXWREPGQJ4BRRE |
| Issuer ID            | AD2M34WBNGQFYK37IDX53DPRG74RLLT7FFWBOBMBUXMAVBCVAU5VKWIY |
| Issued               | 2021-10-27 23:26:09 UTC                                  |
| Expires              |                                                          |
| Bearer Token         | No                                                       |
+----------------------+----------------------------------------------------------+
| Pub Allow            | q                                                        |
| Sub Allow            | _INBOX.>                                                 |
| Response Permissions | Not Set                                                  |
+----------------------+----------------------------------------------------------+
| Max Msg Payload      | Unlimited                                                |
| Max Data             | Unlimited                                                |
| Max Subs             | Unlimited                                                |
| Network Src          | Any                                                      |
| Time                 | Any                                                      |
+----------------------+----------------------------------------------------------+
```

The client has the opposite permissions of the service. It can publish on the request subject `q`, and receive replies on an inbox.

## The NSC Environment

As your projects become more involved, you may work with one or more accounts. NSC tracks your current operator and account. If you are not in a directory containing an operator, account or user, it will use the last operator/account context.

To view your current environment:

```shell
nsc env
```

```
+------------------------------------------------------------------------------------------------------+
|                                           NSC Environment                                            |
+--------------------+-----+---------------------------------------------------------------------------+
| Setting            | Set | Effective Value                                                           |
+--------------------+-----+---------------------------------------------------------------------------+
| $NSC_CWD_ONLY      | No  | If set, default operator/account from cwd only                            |
| $NSC_NO_GIT_IGNORE | No  | If set, no .gitignore files written                                       |
| $NKEYS_PATH        | No  | ~/.nkeys                                                                  |
| $NSC_HOME          | No  | ~/.nsc                                                                    |
| Config             |     | ~/.nsc/nsc.json                                                           |
| $NATS_CA           | No  | If set, root CAs in the referenced file will be used for nats connections |
|                    |     | If not set, will default to the system trust store                        |
+--------------------+-----+---------------------------------------------------------------------------+
| From CWD           |     | No                                                                        |
| Stores Dir         |     | ~/.nsc/nats                                                               |
| Default Operator   |     | MyOperator                                                                |
| Default Account    |     | MyAccount                                                                 |
| Root CAs to trust  |     | Default: System Trust Store                                               |
+--------------------+-----+---------------------------------------------------------------------------+
```

If you have multiple accounts, you can use `nsc env --account <account name>` to set the account as the current default. If you have defined `NKEYS_PATH` or `NSC_HOME` in the environment, you'll also see their current effective values. Finally, if you want to set the stores directory to anything other than the default, you can do `nsc env --store <dir containing an operator>`. If you have multiple accounts, you can try having multiple terminals, each in a directory for a different account.


# Streams

To share messages you publish with other accounts, you have to *Export* a *Stream*. *Exports* are associated with the account performing the export and advertised in exporting account’s JWT.

### Adding a Public Stream Export

To add a stream to your account:

```shell
nsc add export --name abc --subject "a.b.c.>"
```

```
  [ OK ] added public stream export "abc"
```

> Note that we have exported stream with a subject that contains a wildcard. Any subject that matches the pattern will be exported.

To review the stream export:

```shell
nsc describe account
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ A                                                        │
│ Account ID                │ ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-05 13:35:42 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Imports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────────╮
│                          Exports                          │
├──────┬────────┬─────────┬────────┬─────────────┬──────────┤
│ Name │ Type   │ Subject │ Public │ Revocations │ Tracking │
├──────┼────────┼─────────┼────────┼─────────────┼──────────┤
│ abc  │ Stream │ a.b.c.> │ Yes    │ 0           │ N/A      │
╰──────┴────────┴─────────┴────────┴─────────────┴──────────╯
```

Messages this account publishes on `a.b.c.>` will be forwarded to all accounts that import this stream.

### Importing a Stream

Importing a stream enables you to receive messages that are published by a different *Account*. To import a Stream, you have to create an *Import*. To create an *Import* you need to know:

* The exporting account’s public key
* The subject where the stream is published
* You can map the stream’s subject to a different subject
* Self-imports are not valid; you can only import streams from other accounts.

With the required information, we can add an import to the public stream.

```bash
nsc add account B
```

```
[ OK ] generated and stored account key "AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H"
[ OK ] added account "B"
```

```shell
nsc add import --src-account ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE --remote-subject "a.b.c.>"
```

```
[ OK ] added stream import "a.b.c.>"
```

> Notice that messages published by the remote account will be received on the same subject as they are originally published. Sometimes you would like to prefix messages received from a stream. To add a prefix specify `--local-subject`. Subscribers in our account can listen to `abc.>`. For example if `--local-subject abc`, The message will be received as `abc.a.b.c.>`.

And verifying it:

```shell
nsc describe account
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ B                                                        │
│ Account ID                │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-05 13:39:55 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Exports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────╮
│                                   Imports                                   │
├─────────┬────────┬─────────┬──────────────┬─────────┬──────────────┬────────┤
│ Name    │ Type   │ Remote  │ Local/Prefix │ Expires │ From Account │ Public │
├─────────┼────────┼─────────┼──────────────┼─────────┼──────────────┼────────┤
│ a.b.c.> │ Stream │ a.b.c.> │              │         │ A            │ Yes    │
╰─────────┴────────┴─────────┴──────────────┴─────────┴──────────────┴────────╯
```

Let's also add a user to make requests from the service:

```bash
nsc add user b
```

```
[ OK ] generated and stored user key "UDKNTNEL5YD66U2FZZ2B3WX2PLJFKEFHAPJ3NWJBFF44PT76Y2RAVFVE"
[ OK ] generated user creds file "~/.nkeys/creds/O/B/b.creds"
[ OK ] added user "b" to account "B"
```

### Pushing the changes to the NATS servers

If your NATS servers are configured to use the built-in NATS resolver, remember that you need to 'push' any account changes you may have done locally using `nsc add` to the servers for those changes to take effect.

e.g. `nsc push -i` or `nsc push -a B -u nats://localhost`

### Testing the Stream

```bash
nsc sub --account B --user b "a.b.c.>"
```

then

```shell
nsc pub --account A --user U a.b.c.hello world
```

## Securing Streams

If you want to create a stream that is only accessible to accounts you designate, you can create a *private* stream. The export will be visible in your account, but *subscribing* accounts will require an authorization token that must be created by you and generated specifically for the subscribing account.

The authorization token is simply a JWT signed by your account where you authorize the client account to import your export.

### Creating a Private Stream Export

```shell
nsc add export --subject "private.abc.*" --private --account A
```

This is similar to when we defined an export, but this time we added the `--private` flag. The other thing to note is that the subject for the request has a wildcard. This enables the account to map specific subjects to specifically authorized accounts.

```shell
nsc describe account A
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ A                                                        │
│ Account ID                │ ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-05 14:24:02 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Imports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────────────────╮
│                                 Exports                                  │
├───────────────┬────────┬───────────────┬────────┬─────────────┬──────────┤
│ Name          │ Type   │ Subject       │ Public │ Revocations │ Tracking │
├───────────────┼────────┼───────────────┼────────┼─────────────┼──────────┤
│ abc           │ Stream │ a.b.c.>       │ Yes    │ 0           │ N/A      │
│ private.abc.* │ Stream │ private.abc.* │ No     │ 0           │ N/A      │
╰───────────────┴────────┴───────────────┴────────┴─────────────┴──────────╯
```

### Generating an Activation Token

For a foreign account to *import* a private stream, you have to generate an activation token. In addition to granting permissions to the account, the activation token also allows you to subset the exported stream's subject.

To generate a token, you'll need to know the public key of the account importing the service. We can easily find the public key for account B by running:

```bash
nsc list keys --account B
```

```
╭──────────────────────────────────────────────────────────────────────────────────────────╮
│                                           Keys                                           │
├────────┬──────────────────────────────────────────────────────────┬─────────────┬────────┤
│ Entity │ Key                                                      │ Signing Key │ Stored │
├────────┼──────────────────────────────────────────────────────────┼─────────────┼────────┤
│ O      │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │             │ *      │
│  B     │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │             │ *      │
│   b    │ UDKNTNEL5YD66U2FZZ2B3WX2PLJFKEFHAPJ3NWJBFF44PT76Y2RAVFVE │             │ *      │
╰────────┴──────────────────────────────────────────────────────────┴─────────────┴────────╯
```

```bash
nsc generate activation --account A --target-account AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H --subject private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H -o /tmp/activation.jwt
```

```
[ OK ] generated "private.abc.*" activation for account "AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H"
[ OK ] wrote account description to "/tmp/activation.jwt"
```

The command took the account that has the export ('A'), the public key of account B, the subject where the stream will publish to account B.

For completeness, the contents of the JWT file look like this:

```shell
cat /tmp/activation.jwt
```

```
-----BEGIN NATS ACTIVATION JWT-----
eyJ0eXAiOiJqd3QiLCJhbGciOiJlZDI1NTE5In0.eyJqdGkiOiJIS1FPQU9aQkVKS1JYNFJRUVhXS0xYSVBVTlNOSkRRTkxXUFBTSTQ3NkhCVVNYT0paVFFRIiwiaWF0IjoxNTc1NTU1OTczLCJpc3MiOiJBREVUUFQzNldCSUJVS00zSUJDVk00QTVZVVNEWEZFSlBXNE02R0dWQllDQlc3UlJORlRWNU5HRSIsIm5hbWUiOiJwcml2YXRlLmFiYy5BQU00NkUzWUY1V09aU0U1V05ZV0hOM1lZSVNWWk9TSTZYSFRGMlE2NEVDUFhTRlFaUk9KTVAySCIsInN1YiI6IkFBTTQ2RTNZRjVXT1pTRTVXTllXSE4zWVlJU1ZaT1NJNlhIVEYyUTY0RUNQWFNGUVpST0pNUDJIIiwidHlwZSI6ImFjdGl2YXRpb24iLCJuYXRzIjp7InN1YmplY3QiOiJwcml2YXRlLmFiYy5BQU00NkUzWUY1V09aU0U1V05ZV0hOM1lZSVNWWk9TSTZYSFRGMlE2NEVDUFhTRlFaUk9KTVAySCIsInR5cGUiOiJzdHJlYW0ifX0.yD2HWhRQYUFy5aQ7zNV0YjXzLIMoTKnnsBB_NsZNXP-Qr5fz7nowyz9IhoP7UszkN58m__ovjIaDKI9ml0l9DA
------END NATS ACTIVATION JWT------
```

When decoded it looks like this:

```shell
nsc describe jwt -f /tmp/activation.jwt 
```

```
╭────────────────────────────────────────────────────────────────────────────────────────╮
│                                       Activation                                       │
├─────────────────┬──────────────────────────────────────────────────────────────────────┤
│ Name            │ private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
│ Account ID      │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H             │
│ Issuer ID       │ ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE             │
│ Issued          │ 2019-12-05 14:26:13 UTC                                              │
│ Expires         │                                                                      │
├─────────────────┼──────────────────────────────────────────────────────────────────────┤
│ Hash ID         │ GWIS5YCSET4EXEOBXVMQKXAR4CLY4IIXFV4MEMRUXPSQ7L4YTZ4Q====             │
├─────────────────┼──────────────────────────────────────────────────────────────────────┤
│ Import Type     │ Stream                                                               │
│ Import Subject  │ private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
├─────────────────┼──────────────────────────────────────────────────────────────────────┤
│ Max Messages    │ Unlimited                                                            │
│ Max Msg Payload │ Unlimited                                                            │
│ Network Src     │ Any                                                                  │
│ Time            │ Any                                                                  │
╰─────────────────┴──────────────────────────────────────────────────────────────────────╯
```

The token can be shared directly with the client account.

> If you manage many tokens for many accounts, you may want to host activation tokens on a web server and share the URL with the account. The benefit to the hosted approach is that any updates to the token would be available to the importing account whenever their account is updated, provided the URL you host them in is stable.

## Importing a Private Stream

Importing a private stream is more natural than a public one as the activation token given to you already has all of the necessary details. Note that the token can be an actual file path or a remote URL.

```shell
nsc add import --account B --token /tmp/activation.jwt
```

```
[ OK ] added stream import "private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H"
```

Describe account B

```shell
nsc describe account B
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ B                                                        │
│ Account ID                │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-05 14:29:16 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Exports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                Imports                                                                                                │
├──────────────────────────────────────────────────────────────────────┬────────┬──────────────────────────────────────────────────────────────────────┬──────────────┬─────────┬──────────────┬────────┤
│ Name                                                                 │ Type   │ Remote                                                               │ Local/Prefix │ Expires │ From Account │ Public │
├──────────────────────────────────────────────────────────────────────┼────────┼──────────────────────────────────────────────────────────────────────┼──────────────┼─────────┼──────────────┼────────┤
│ a.b.c.>                                                              │ Stream │ a.b.c.>                                                              │              │         │ A            │ Yes    │
│ private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │ Stream │ private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │              │         │ A            │ No     │
╰──────────────────────────────────────────────────────────────────────┴────────┴──────────────────────────────────────────────────────────────────────┴──────────────┴─────────┴──────────────┴────────╯
```

### Testing the Private Stream

Testing a private stream is no different than testing a public one:

```bash
nsc tools sub --account B --user b private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H
```

then

```shell
nsc tools pub --account A --user U private.abc.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H hello
```


# Services

To share services that other accounts can reach via request reply, you have to *Export* a *Service*. *Services* are associated with the account performing the replies and are advertised in the exporting accounts' JWT.

## Adding a Public Service Export

To add a service to your account:

```bash
nsc add export --name help --subject help --service
```

```
[ OK ] added public service export "help"
```

To review the service export:

```bash
nsc describe account
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ A                                                        │
│ Account ID                │ ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-04 18:20:42 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Imports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭────────────────────────────────────────────────────────────╮
│                          Exports                           │
├──────┬─────────┬─────────┬────────┬─────────────┬──────────┤
│ Name │ Type    │ Subject │ Public │ Revocations │ Tracking │
├──────┼─────────┼─────────┼────────┼─────────────┼──────────┤
│ help │ Service │ help    │ Yes    │ 0           │ -        │
╰──────┴─────────┴─────────┴────────┴─────────────┴──────────╯
```

## Importing a Service

Importing a service enables you to send requests to the remote *Account*. To import a Service, you have to create an *Import*. To create an import you need to know:

* The exporting account’s public key
* The subject the service is listening on
* You can map the service’s subject to a different subject
* Self-imports are not valid; you can only import services from other accounts.

To learn how to inspect a JWT from an account server, [check this article](https://github.com/nats-io/nats.docs/blob/master/legacy/nas/inspecting_jwts.md).

First let's create a second account to import the service into:

```bash
nsc add account B
```

```
[ OK ] generated and stored account key "AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H"
[ OK ] added account "B"
```

Add the import of the subject 'help'

```shell
nsc add import --src-account ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE --remote-subject help --service
```

```
[ OK ] added service import "help"
```

Verifying our work:

```bash
nsc describe account
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ B                                                        │
│ Account ID                │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-04 20:12:42 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Exports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────────────────╮
│                                 Imports                                  │
├──────┬─────────┬────────┬──────────────┬─────────┬──────────────┬────────┤
│ Name │ Type    │ Remote │ Local/Prefix │ Expires │ From Account │ Public │
├──────┼─────────┼────────┼──────────────┼─────────┼──────────────┼────────┤
│ help │ Service │ help   │ help         │         │ A            │ Yes    │
╰──────┴─────────┴────────┴──────────────┴─────────┴──────────────┴────────╯
```

Let's also add a user to make requests from the service:

```bash
nsc add user b
```

```
[ OK ] generated and stored user key "UDKNTNEL5YD66U2FZZ2B3WX2PLJFKEFHAPJ3NWJBFF44PT76Y2RAVFVE"
[ OK ] generated user creds file "~/.nkeys/creds/O/B/b.creds"
[ OK ] added user "b" to account "B"
```

### Pushing the changes to the nats servers

If your nats servers are configured to use the built-in NATS resolver, remember that you need to 'push' any account changes you may have done (locally) using `nsc add` to the servers for those changes to take effect.

e.g. `nsc push -i` or `nsc push -a B -u nats://localhost`

### Testing the Service

To test the service, we can install the ['nats'](https://docs.nats.io/using-nats/nats-tools/nats_cli) CLI tool:

Set up a process to handle the request. This process will run from account 'A' using user 'U':

```shell
nats reply --creds ~/.nkeys/creds/O/A/U.creds help "I will help"                
```

Remember you can also do:

```shell
nsc reply --account A --user U help "I will help"
```

Send the request:

```shell
nats request --creds ~/.nkeys/creds/O/B/b.creds help me
```

The service receives the request:

```
Received on [help]: 'me'
```

And the response is received by the requestor:

```
Received  [_INBOX.v6KAX0v1bu87k49hbg3dgn.StIGJF0D] : 'I will help'
```

Or more simply:

```bash
nsc reply --account A --user U help "I will help"
nsc req --account B --user b help me
```

```
published request: [help] : 'me'
received reply: [_INBOX.GCJltVq1wRSb5FoJrJ6SE9.w8utbBXR] : 'I will help'
```

## Securing Services

If you want to create a service that is only accessible to accounts you designate you can create a *private* service. The export will be visible in your account, but subscribing accounts will require an authorization token that must be created by you and generated specifically for the requesting account. The authorization token is simply a JWT signed by your account where you authorize the client account to import your service.

### Creating a Private Service Export

```shell
nsc add export --subject "private.help.*" --private --service --account A
```

```
[ OK ] added private service export "private.help.*"
```

As before, we declared an export, but this time we added the `--private` flag. The other thing to note is that the subject for the request has a wildcard. This enables the account to map specific subjects to specifically authorized accounts.

```bash
nsc describe account A
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ A                                                        │
│ Account ID                │ ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-04 20:19:19 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Imports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────╮
│                                   Exports                                   │
├────────────────┬─────────┬────────────────┬────────┬─────────────┬──────────┤
│ Name           │ Type    │ Subject        │ Public │ Revocations │ Tracking │
├────────────────┼─────────┼────────────────┼────────┼─────────────┼──────────┤
│ help           │ Service │ help           │ Yes    │ 0           │ -        │
│ private.help.* │ Service │ private.help.* │ No     │ 0           │ -        │
╰────────────────┴─────────┴────────────────┴────────┴─────────────┴──────────╯
```

### Generating an Activation Token

For the foreign account to *import* a private service and be able to send requests, you have to generate an activation token. The activation token in addition to granting permission to the account allows you to subset the service’s subject:

To generate a token, you’ll need to know the public key of the account importing the service. We can easily find the public key for account B by running:

```bash
nsc list keys --account B
```

```
╭──────────────────────────────────────────────────────────────────────────────────────────╮
│                                           Keys                                           │
├────────┬──────────────────────────────────────────────────────────┬─────────────┬────────┤
│ Entity │ Key                                                      │ Signing Key │ Stored │
├────────┼──────────────────────────────────────────────────────────┼─────────────┼────────┤
│ O      │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │             │ *      │
│  B     │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │             │ *      │
│   b    │ UDKNTNEL5YD66U2FZZ2B3WX2PLJFKEFHAPJ3NWJBFF44PT76Y2RAVFVE │             │ *      │
╰────────┴──────────────────────────────────────────────────────────┴─────────────┴────────╯
```

```shell
nsc generate activation --account A --target-account AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H --subject private.help.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H -o /tmp/activation.jwt
```

```
[ OK ] generated "private.help.*" activation for account "AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H"
[ OK ] wrote account description to "/tmp/activation.jwt"
```

The command took the account that has the export ('A'), the public key of account B, the subject where requests from account B will be handled, and an output file where the token can be stored. The subject for the export allows the service to handle all requests coming in on private.help.\*, but account B can only request from a specific subject.

For completeness, the contents of the JWT file looks like this:

```bash
cat /tmp/activation.jwt
```

```
-----BEGIN NATS ACTIVATION JWT-----
eyJ0eXAiOiJqd3QiLCJhbGciOiJlZDI1NTE5In0.eyJqdGkiOiJUS01LNEFHT1pOVERDTERGUk9QTllNM0hHUVRDTEJTUktNQUxXWTVSUUhFVEVNNE1VTDdBIiwiaWF0IjoxNTc1NDkxNjEwLCJpc3MiOiJBREVUUFQzNldCSUJVS00zSUJDVk00QTVZVVNEWEZFSlBXNE02R0dWQllDQlc3UlJORlRWNU5HRSIsIm5hbWUiOiJwcml2YXRlLmhlbHAuQUFNNDZFM1lGNVdPWlNFNVdOWVdITjNZWUlTVlpPU0k2WEhURjJRNjRFQ1BYU0ZRWlJPSk1QMkgiLCJzdWIiOiJBQU00NkUzWUY1V09aU0U1V05ZV0hOM1lZSVNWWk9TSTZYSFRGMlE2NEVDUFhTRlFaUk9KTVAySCIsInR5cGUiOiJhY3RpdmF0aW9uIiwibmF0cyI6eyJzdWJqZWN0IjoicHJpdmF0ZS5oZWxwLkFBTTQ2RTNZRjVXT1pTRTVXTllXSE4zWVlJU1ZaT1NJNlhIVEYyUTY0RUNQWFNGUVpST0pNUDJIIiwidHlwZSI6InNlcnZpY2UifX0.4tFx_1UzPUwbV8wFNIJsQYu91K9hZaGRLE10nOphfHGetvMPv1384KC-1AiNdhApObSDFosdDcpjryD0QxaDCQ
------END NATS ACTIVATION JWT------
```

When decoded it looks like this:

```shell
nsc describe jwt -f /tmp/activation.jwt
```

```
╭─────────────────────────────────────────────────────────────────────────────────────────╮
│                                       Activation                                        │
├─────────────────┬───────────────────────────────────────────────────────────────────────┤
│ Name            │ private.help.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
│ Account ID      │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H              │
│ Issuer ID       │ ADETPT36WBIBUKM3IBCVM4A5YUSDXFEJPW4M6GGVBYCBW7RRNFTV5NGE              │
│ Issued          │ 2019-12-04 20:33:30 UTC                                               │
│ Expires         │                                                                       │
├─────────────────┼───────────────────────────────────────────────────────────────────────┤
│ Hash ID         │ DD6BZKI2LTQKAJYD5GTSI4OFUG72KD2BF74NFVLUNO47PR4OX64Q====              │
├─────────────────┼───────────────────────────────────────────────────────────────────────┤
│ Import Type     │ Service                                                               │
│ Import Subject  │ private.help.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
├─────────────────┼───────────────────────────────────────────────────────────────────────┤
│ Max Messages    │ Unlimited                                                             │
│ Max Msg Payload │ Unlimited                                                             │
│ Network Src     │ Any                                                                   │
│ Time            │ Any                                                                   │
╰─────────────────┴───────────────────────────────────────────────────────────────────────╯
```

The token can be shared directly with the client account.

> If you manage many tokens for many accounts, you may want to host activation tokens on a web server and share the URL with the account. The benefit to the hosted approach is that any updates to the token would be available to the importing account whenever their account is updated, provided the URL you host them in is stable. When using a JWT account server, the tokens can be stored right on the server and shared by an URL that is printed when the token is generated.

## Importing a Private Service

Importing a private service is more natural than a public one because the activation token stores all the necessary details. Again, the token can be an actual file path or a remote URL.

```shell
nsc add import --account B -u /tmp/activation.jwt --local-subject private.help --name private.help
```

```
[ OK ] added service import "private.help.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H"
```

Describe account B

```shell
nsc describe account B
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ B                                                        │
│ Account ID                │ AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │
│ Issuer ID                 │ OAFEEYZSYYVI4FXLRXJTMM32PQEI3RGOWZJT7Y3YFM4HB7ACPE4RTJPG │
│ Issued                    │ 2019-12-04 20:38:06 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Exports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                     Imports                                                                     │
├──────────────┬─────────┬───────────────────────────────────────────────────────────────────────┬──────────────┬─────────┬──────────────┬────────┤
│ Name         │ Type    │ Remote                                                                │ Local/Prefix │ Expires │ From Account │ Public │
├──────────────┼─────────┼───────────────────────────────────────────────────────────────────────┼──────────────┼─────────┼──────────────┼────────┤
│ help         │ Service │ help                                                                  │ help         │         │ A            │ Yes    │
│ private.help │ Service │ private.help.AAM46E3YF5WOZSE5WNYWHN3YYISVZOSI6XHTF2Q64ECPXSFQZROJMP2H │ private.help │         │ A            │ No     │
╰──────────────┴─────────┴───────────────────────────────────────────────────────────────────────┴──────────────┴─────────┴──────────────┴────────╯
```

When importing a service, you can specify the local subject you want to use to make requests. The local subject in this case is `private.help`. However when the request is forwarded by NATS, the request is sent on the remote subject.

### Testing the Private Service

Testing a private service is no different than a public one:

```bash
nsc reply --account A --user U "private.help.*" "help is here"
nsc req --account B --user b private.help help_me
```

```
published request: [private.help] : 'help_me'
received reply: [_INBOX.3MhS0iCHfqO8wUl1x59bHB.jpE2jvEj] : 'help is here'
```


# Signing Keys

As previously discussed, NKEYs are identities, and if someone gets a hold of an account or operator nkey they can do everything you can do as you.

NATS has strategies to let you deal with scenarios where your private keys escape out in the wild.

The first and most important line of defense is *Signing Keys*. *Signing Keys* allow you have multiple NKEY identities of the same kind (Operator or Account) that have the same degree of trust as the standard *Issuer* nkey.

The concept behind the signing key is that you can issue a JWT for an operator or an account that lists multiple nkeys. Typically the issuer will match the *Subject* of the entity issuing the JWT. With SigningKeys, a JWT is considered valid if it is signed by the *Subject* of the *Issuer* or one of its signing keys. This enables guarding the private key of the Operator or Account more closely while allowing *Accounts*, *Users* or *Activation Tokens* be signed using alternate private keys.

If an issue should arise where somehow a signing key escapes into the wild, you would remove the compromised signing key from the entity, add a new one, and reissue the entity. When a JWT is validated, if the signing key is missing, the operation is rejected. You are also on the hook to re-issue all JWTs (accounts, users, activation tokens) that were signed with the compromised signing key.

This is effectively a large hammer. You can mitigate the process a bit by having a larger number of signing keys and then rotating the signing keys to get a distribution you can easily handle in case of a compromise. In a future release, we’ll have a revocation process were you can invalidate a single JWT by its unique JWT ID (JTI). For now a sledge hammer you have.

With greater security process, there’s greater complexity. With that said, `nsc` doesn’t track public or private signing keys. As these are only identities that when in use presume a manual use. That means that you the user will have to track and manage your private keys more closely.

Let’s get a feel for the workflow. We are going to:

* Create an operator with a signing key
* Create an account with a signing key
* The account will be signed using the operator’s signing key
* Create an user with the account’s signing key

All signing key operations revolve around the global `nsc` flag `-K` or `--private-key`. Whenever you want to modify an entity, you have to supply the parent key so that the JWT is signed. Normally this happens automatically but in the case of signing keys, you’ll have to supply the flag by hand.

Creating the operator:

```shell
nsc add operator O2
```

```
[ OK ] generated and stored operator key "OABX3STBZZRBHMWMIMVHNQVNUG2O3D54BMZXX5LMBYKSAPDSHIWPMMFY"
[ OK ] added operator "O2"
```

To add a signing key we have to first generate one with `nsc`:

```shell
nsc generate nkey --operator --store
```

```
SOAEW6Z4HCCGSLZJYZQMGFQY2SY6ZKOPIAKUQ5VZY6CW23WWYRNHTQWVOA
OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5
operator key stored ~/.nkeys/keys/O/AZ/OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5.nk
```

> On a production environment private keys should be saved to a file and always referenced from the secured file.

Now we are going to edit the operator by adding a signing key with the `--sk` flag providing the generated operator public key (the one starting with `O`):

```shell
nsc edit operator --sk OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5
```

```
[ OK ] added signing key "OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5"
[ OK ] edited operator "O2"
```

Check our handy work:

```shell
nsc describe operator
```

```
╭─────────────────────────────────────────────────────────────────────────╮
│                            Operator Details                             │
├──────────────┬──────────────────────────────────────────────────────────┤
│ Name         │ O2                                                       │
│ Operator ID  │ OABX3STBZZRBHMWMIMVHNQVNUG2O3D54BMZXX5LMBYKSAPDSHIWPMMFY │
│ Issuer ID    │ OABX3STBZZRBHMWMIMVHNQVNUG2O3D54BMZXX5LMBYKSAPDSHIWPMMFY │
│ Issued       │ 2019-12-05 14:36:16 UTC                                  │
│ Expires      │                                                          │
├──────────────┼──────────────────────────────────────────────────────────┤
│ Signing Keys │ OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5 │
╰──────────────┴──────────────────────────────────────────────────────────╯
```

Now let’s create an account called `A` and sign it with the generated operator private signing key. To sign it with the key specify the `-K` flag and the private key or a path to the private key:

```shell
nsc add account A -K ~/.nkeys/keys/O/AZ/OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5.nk
```

```
[ OK ] generated and stored account key "ACDXQQ6KD5MVSFMK7GNF5ARK3OJC6PEICWCH5PQ7HO27VKGCXQHFE33B"
[ OK ] added account "A"
```

Let’s generate an account signing key, again we use `nk`:

```bash
nsc generate nkey --account --store
```

```
SAAA4BVFTJMBOW3GAYB3STG3VWFSR4TP4QJKG2OCECGA26SKONPFGC4HHE
ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7
account key stored ~/.nkeys/keys/A/DU/ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7.nk
```

Let’s add the signing key to the account, and remember to sign the account with the operator signing key:

```shell
nsc edit account --sk ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7 -K ~/.nkeys/keys/O/AZ/OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5.nk
```

```
[ OK ] added signing key "ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7"
[ OK ] edited account "A"
```

Let's take a look at the account

```shell
nsc describe account
```

```
╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                   Account Details                                    │
├───────────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                      │ A                                                        │
│ Account ID                │ ACDXQQ6KD5MVSFMK7GNF5ARK3OJC6PEICWCH5PQ7HO27VKGCXQHFE33B │
│ Issuer ID                 │ OAZBRNE7DQGDYT5CSAGWDMI5ENGKOEJ57BXVU6WUTHFEAO3CU5GLQYF5 │
│ Issued                    │ 2019-12-05 14:48:22 UTC                                  │
│ Expires                   │                                                          │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Signing Keys              │ ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7 │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Connections           │ Unlimited                                                │
│ Max Leaf Node Connections │ Unlimited                                                │
│ Max Data                  │ Unlimited                                                │
│ Max Exports               │ Unlimited                                                │
│ Max Imports               │ Unlimited                                                │
│ Max Msg Payload           │ Unlimited                                                │
│ Max Subscriptions         │ Unlimited                                                │
│ Exports Allows Wildcards  │ True                                                     │
├───────────────────────────┼──────────────────────────────────────────────────────────┤
│ Imports                   │ None                                                     │
│ Exports                   │ None                                                     │
╰───────────────────────────┴──────────────────────────────────────────────────────────╯
```

We can see that the signing key `ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7` was added to the account. Also the issuer is the operator signing key (specified by the `-K`).

Now let’s create a user and sign it with the account signing key starting with `ADUQTJD4TF4O`.

```shell
nsc add user U -K ~/.nkeys/keys/A/DU/ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7.nk
```

```
[ OK ] generated and stored user key "UD47TOTKVDY4IQRGI6D7XMLZPHZVNV5FCD4CNQICLV3FXLQBY72A4UXL"
[ OK ] generated user creds file "~/.nkeys/creds/O2/A/U.creds"
[ OK ] added user "U" to account "A"
```

Check the user

```shell
nsc describe user
```

```
╭─────────────────────────────────────────────────────────────────────────────────╮
│                                      User                                       │
├──────────────────────┬──────────────────────────────────────────────────────────┤
│ Name                 │ U                                                        │
│ User ID              │ UD47TOTKVDY4IQRGI6D7XMLZPHZVNV5FCD4CNQICLV3FXLQBY72A4UXL │
│ Issuer ID            │ ADUQTJD4TF4O6LTTHCKDKSHKGBN2NECCHHMWFREPKNO6MPA7ZETFEEF7 │
│ Issuer Account       │ ACDXQQ6KD5MVSFMK7GNF5ARK3OJC6PEICWCH5PQ7HO27VKGCXQHFE33B │
│ Issued               │ 2019-12-05 14:50:07 UTC                                  │
│ Expires              │                                                          │
├──────────────────────┼──────────────────────────────────────────────────────────┤
│ Response Permissions │ Not Set                                                  │
├──────────────────────┼──────────────────────────────────────────────────────────┤
│ Max Messages         │ Unlimited                                                │
│ Max Msg Payload      │ Unlimited                                                │
│ Network Src          │ Any                                                      │
│ Time                 │ Any                                                      │
╰──────────────────────┴──────────────────────────────────────────────────────────╯
```

As expected, the issuer is now the signing key we generated earlier. To map the user to the actual account, an `Issuer Account` field was added to the JWT that identifies the public key of account *A*.

## Scoped Signing Keys

Scoped Signing Keys simplify user permission management. Previously if you wanted to limit the permissions of users, you had to specify permissions on a per-user basis. With scoped signing keys, you associate a signing key with a set of permissions. This configuration lives on the account JWT and is managed with the `nsc edit signing-key` command. You can add as many scoped signing keys as necessary.

To issue a user with a set of permissions, simply sign the user with the signing key having the permission set you want. The user configuration must *not* have any permissions assigned to it.

On connect, the nats-server will assign the permissions associated with that signing key to the user. If you update the permissions associated with a signing key, the server will immediately update permissions for users signed with that key.

```shell
nsc add account A
```

```
[ OK ] generated and stored account key "ADLGEVANYDKDQ6WYXPNBEGVUURXZY4LLLK5BJPOUDN6NGNXLNH4ATPWR"
[ OK ] push jwt to account server:
       [ OK ] pushed account jwt to the account server
       > NGS created a new free billing account for your JWT, A [ADLGEVANYDKD].
       > Use the 'ngs' command to manage your billing plan.
       > If your account JWT is *not* in ~/.nsc, use the -d flag on ngs commands to locate it.
[ OK ] pull jwt from account server
[ OK ] added account "A"
```

Generate the signing key

```shell
nsc edit account -n A --sk generate
```

```
[ OK ] added signing key "AAZQXKDPOTGUCOCOGDW7HWWVR5WEGF3KYL7EKOEHW2XWRS2PT5AOTRH3"
[ OK ] push jwt to account server
[ OK ] pull jwt from account server
[ OK ] account server modifications:
       > allow wildcard exports changed from true to false
[ OK ] edited account "A"
```

Add a service to the account

```shell
nsc edit signing-key --account A --role service --sk AAZQXKDPOTGUCOCOGDW7HWWVR5WEGF3KYL7EKOEHW2XWRS2PT5AOTRH3 --allow-sub "q.>" --deny-pub ">" --allow-pub-response
```

```
[ OK ] set max responses to 1
[ OK ] added deny pub ">"
[ OK ] added sub "q.>"
[ OK ] push jwt to account server
[ OK ] pull jwt from account server
[ OK ] edited signing key "AAZQXKDPOTGUCOCOGDW7HWWVR5WEGF3KYL7EKOEHW2XWRS2PT5AOTRH3"
```

Since the signing key has a unique role name within an account, it can be subsequently used for easier referencing.

```shell
nsc add user U -K service
```

```
[ OK ] generated and stored user key "UBFRJ6RNBYJWSVFBS7O4ZW5MM6J3EPE75II3ULPVUWOUH7K7A23D3RQE"
[ OK ] generated user creds file `~/test/issue-2621/keys/creds/synadia/A/U.creds`
[ OK ] added user "U" to account "A"
```

To see the permissions for the user enter `nsc describe user` - you will see in the report that the user is scoped, and has the permissions listed. You can inspect and modify the scoped permissions with `nsc edit signing-key` - pushing updates to the account will reassign user permissions.

### Template functions

*Available as of NATS 2.9.0*

Although scoped signing keys are very useful and improve security, by limiting the scope of a particular signing key, the permissions that are set may be too rigid in multi-user setups. For example, given two users `pam` and `joe`, we may want to allow them to subscribe to their own namespaced subject in order to service requests, e.g. `pam.>` and `joe.>`. The permission *structure* is the same between these users, but they differ in the concrete subjects which are further scoped to some property about that user.

Template functions can be used to declare the structure within a scope signing key, but utilize basic templating so that each user that is created with the signing key has user-specific subjects.

The following template functions will expand when a user is created.

* `{{name()}}` - expands to the name of the user, e.g. `pam`
* `{{subject()}}` - expands to the user public nkey value of the user, e.g. `UAC...`
* `{{account-name()}}` - expands to the signing account name, e.g. `sales`
* `{{account-subject()}}` - expands to the account public nkey value, e.g. `AXU...`
* `{{tag(key)}}` - expands `key:value` tags associated with the signing key

For example, given a scoped signing key with a templated `--allow-sub` subject:

```
nsc edit signing-key \
  --account sales \
  --role team-service \
  --sk AXUQXKDPOTGUCOCOGDW7HWWVR5WEGF3KYL7EKOEHW2XWRS2PT5AOTRH3 \
  --allow-sub "{{account-name()}}.{{tag(team)}}.{{name()}}.>" \
  --allow-pub-response
```

We can create two users in different teams.

```
nsc add user pam -K team-service --tag team:support
nsc add user joe -K team-service --tag team:leads
```

The resulting `--allow-sub` permission per user would be expanded to:

```
sales.support.pam.>
```

and

```
sales.leads.joe.>
```


# Revocation

NATS supports two types of revocations. Both of these are stored in the Account JWT, so that the nats-server can see the revocations and apply them.

Users are revoked by public key and time. Access to an export, called an activation, can be revoked for a specific account at a specific time. The use of time here can be confusing, but is designed to support the primary uses of revocation.

When a user or activation is revoked at time T, it means that any user JWT or activation token created before that time is invalid. If a new user JWT or new activation token is created after T it can be used. This allows an account owner to revoke a user and renew their access at the same time.

Let's look at an example. Suppose you created a user JWT with access to the subject "billing". Later you decide you don't want that user to have access to "billing". Revoke the user, say at noon on May 1st 2019, and create a new user JWT without access to "billing". The user can no longer log in with the old JWT because it is revoked, but they can log in with the new JWT because it was created after noon May 1st 2019.

`nsc` provides a number of commands to create, remove or list revocations:

```bash
nsc revocations -h
```

```
Manage revocation for users and activations from an account

Usage:
  nsc revocations [command]

Available Commands:
  add-user          Revoke a user
  add_activation    Revoke an accounts access to an export
  delete-user       Remove a user revocation
  delete_activation Remove an account revocation from an export
  list-users        List users revoked in an account
  list_activations  List account revocations for an export

Flags:
  -h, --help   help for revocations

Global Flags:
  -i, --interactive          ask questions for various settings
  -K, --private-key string   private key

Use "nsc revocations [command] --help" for more information about a command.
```

Both add commands take the flag `--at` which defaults to 0, for now, which can be used to set the unix timestamp as described above. By default revocations are at the current time, but you can set them in the past for situations where you know when a problem occurred and was fixed.

Deleting a revocation is permanent and can allow an old activation or user JWT to be valid again. Therefore delete should only be used if you are sure the tokens in question have expired.

### Pushing the changes to the nats servers

If your nats servers are configured to use the built-in NATS resolver, remember that you need to 'push' any account changes you may have done (locally) using `nsc revocations` to the servers for those changes to take effect.

i.e. `nsc push -i` or `nsc push -a B -u nats://localhost`

If there are any clients currently connected with as a user that gets added to the revocations, their connections will be immediately terminated as soon as you 'push' your revocations to a nats server.


# Managed Operators

You can use `nsc` to administer multiple operators. Operators can be thought of as the owners of nats-servers, and fall into two categories: local and managed. The key difference is that managed operators are ones which you don't have the nkey for. An example of a managed operator is Synadia's [NGS](https://www.synadia.com/cloud?utm_source=nats_docs\&utm_medium=nats).

Accounts, as represented by their JWTs, are signed by the operator. Some operators may use local copies of JWTs (i.e. using the memory resolver), but most should use the NATS account resolver built-in to 'nats-server' to manage their JWTs. Synadia uses a custom server for their JWTs that works similarly to the open-sourced account server.

There are a few special commands when dealing with server based operators:

* Account JWTs can be pushed to the server using `nsc push`
* Account JWTs can be pulled from a server using `nsc pull`

For managed operators this push/pull behavior is built into `nsc`. Each time you edit your account JWT `nsc` will push the change to a managed operator's server and pull the signed response. If this fails the JWT on disk may not match the value on the server. You can always push or pull the account again without editing it. Note - push only works if the operator JWT was configured with an account server URL.

The managed operator will not only sign your account JWT with its key, but may also edit the JWT to include limits to constrain your access to their NATS servers. Some operators may also add demonstration or standard imports. Generally you can remove these, although the operator gets the final call on all Account edits. As with any deployment, the managed operator doesn't track user JWTs.

To start using a managed operator you need to tell `nsc` about it. There are a couple ways to do this. First you can manually tell `nsc` to download the operator JWT using the `add operator` command:

```bash
nsc add operator -i
```

The operator JWT (or details) should be provided to you by the operator. The second way to add a managed operator is with the `init` command:

```bash
nsc init -o synadia -n MyFirstAccount
```

You can use the name of an existing operator, or a well known one (currently only "synadia").

Once you add a managed operator you can add accounts to it normally, with the caveat that new accounts are pushed and pulled as described above.

## Defining "Well Known Operators"

To define a well known operator, you would tell `nsc` about an operator that you want people in your environment to use by name with a simple environment variable of the form `nsc_<operator name>_operator` the value of this environment variable should be the URL for getting the operator JWT. For example:

```bash
export nsc_zoom_operator=https://account-server-host/jwt/v1/operator
```

will tell `nsc` that there is a well known operator named zoom with its JWT at `https://account-server-host/jwt/v1/operator`. With this definition you can now use the `-u` flag with the name "zoom" to add the operator to an `nsc` store directory.

The operator JWT should have its account JWT server property set to point to the appropriate URL. For our example this would be:

```bash
nsc edit operator -u https://account-server-host/jwt/v1
```

You can also set one or more service urls. These allow the `nsc tool` actions like pub and sub to work. For example:

```bash
nsc edit operator -n nats://localhost:4222
nsc tool pub hello world
```


# nats-top

[nats-top](https://github.com/nats-io/nats-top) is a [top](http://man7.org/linux/man-pages/man1/top.1.html)-like tool for monitoring nats-server servers.

{% hint style="info" %}
The `nats-top` functionality is now available in the [`nats`](https://github.com/nats-io/nats.docs/blob/master/using-nats/nats-tools/using-nats/nats-tools/nats_cli/README.md) CLI tool using the `nats top` command.
{% endhint %}

The nats-top tool provides a dynamic real-time view of a NATS server. nats-top can display a variety of system summary information about the NATS server, such as subscription, pending bytes, number of messages, and more, in real time. For example:

```bash
nats-top
```

```
nats-server version 0.6.4 (uptime: 31m42s)
Server:
  Load: CPU: 0.8%   Memory: 5.9M  Slow Consumers: 0
  In:   Msgs: 34.2K  Bytes: 3.0M  Msgs/Sec: 37.9  Bytes/Sec: 3389.7
  Out:  Msgs: 68.3K  Bytes: 6.0M  Msgs/Sec: 75.8  Bytes/Sec: 6779.4

Connections: 4
  HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION SUBSCRIPTIONS
  127.0.0.1:56134      2        5       0           11.6K       11.6K       1.1M        905.1K      go       1.1.0   foo, hello
  127.0.1.1:56138      3        1       0           34.2K       0           3.0M        0           go       1.1.0    _INBOX.a96f3f6853616154d23d1b5072
  127.0.0.1:56144      4        5       0           11.2K       11.1K       873.5K      1.1M        go       1.1.0   foo, hello
  127.0.0.1:56151      5        8       0           11.4K       11.5K       1014.6K     1.0M        go       1.1.0   foo, hello
```

## Installation

nats-top can be installed using `go install`. For example:

```bash
go install github.com/nats-io/nats-top
```

With newer versions of Go, you will be required to use `go install github.com/nats-io/nats-top@latest`.

NOTE: You may have to run the above command as user `sudo` depending on your setup. If you receive an error that you cannot install nats-top because your $GOPATH is not set, when in fact it is set, use command `sudo -E go get github.com/nats-io/nats-top` to install nats-top. The `-E` flag tells sudo to preserve the current user's environment.

## Usage

Once installed, nats-top can be run with the command `nats-top` and optional arguments.

```bash
nats-top [-s server] [-m monitor] [-n num_connections] [-d delay_in_secs] [-sort by]
```

## Options

Optional arguments inclde the following:

| Option               | Description                                                   |
| -------------------- | ------------------------------------------------------------- |
| `-m monitor`         | Monitoring http port from nats-server.                        |
| `-n num_connections` | Limit the connections requested to the server (default 1024). |
| `-d delay_in_secs`   | Screen refresh interval (default 1 second).                   |
| `-sort by`           | Field to use for sorting the connections (see below).         |

## Commands

While in nats-top view, you can use the following commands.

### option

Use the `o<option>` command to set the primary sort key to the `<option>` value. The option value can be one of the following: `cid`, `subs`, `pending`, `msgs_to`, `msgs_from`, `bytes_to`, `bytes_from`, `lang`, `version`.

You can also set the sort option on the command line using the `-sort` flag. For example: `nats-top -sort bytes_to`.

### limit

Use the `n<limit>` command to set the sample size of connections to request from the server.

You can also set this on the command line using the `-n num_connections` flag. For example: `nats-top -n 1`.

Note that if `n<limit>` is used in conjunction with `-sort`, the server will respect both options allowing queries such as the following: Query for the connection with largest number of subscriptions: `nats-top -n 1 -sort subs`.

### s, ? and q Commands

Use the `s` command to toggle displaying connection subscriptions.

Use the `?` command to show help message with options.

Use the `q` command to quit nats-top.

### Tutorial

For a walkthrough with `nats-top` check out the [tutorial](https://docs.nats.io/using-nats/nats-tools/nats_top/nats-top-tutorial).


# Tutorial

You can use [nats-top](https://github.com/nats-io/nats-top) to monitor in realtime NATS server connections and message statistics.

## Prerequisites

* [Set up your Go environment](https://golang.org/doc/install)
* [Install the NATS server](https://docs.nats.io/running-a-nats-service/introduction/installation)

## 1. Install nats-top

```bash
go install github.com/nats-io/nats-top@latest
```

You may need to run the following instead:

```bash
sudo -E go install github.com/nats-io/nats-top
```

## 2. Start the NATS server with monitoring enabled

```bash
nats-server -m 8222
```

## 3. Start nats-top

```bash
nats-top
```

Result:

```
nats-server version 0.6.6 (uptime: 2m2s)
Server:
  Load: CPU:  0.0%  Memory: 6.3M  Slow Consumers: 0
  In:   Msgs: 0  Bytes: 0  Msgs/Sec: 0.0  Bytes/Sec: 0
  Out:  Msgs: 0  Bytes: 0  Msgs/Sec: 0.0  Bytes/Sec: 0

Connections: 0
  HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION
```

## 4. Run NATS client programs

Run some NATS client programs and exchange messages.

For the best experience, you will want to run multiple subscribers, at least 2 or 3. Refer to the [example pub-sub clients](https://docs.nats.io/running-a-nats-service/clients).

## 5. Check nats-top for statistics

```
nats-server version 0.6.6 (uptime: 30m51s)
Server:
  Load: CPU:  0.0%  Memory: 10.3M  Slow Consumers: 0
  In:   Msgs: 56  Bytes: 302  Msgs/Sec: 0.0  Bytes/Sec: 0
  Out:  Msgs: 98  Bytes: 512  Msgs/Sec: 0.0  Bytes/Sec: 0

Connections: 3
  HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION
  ::1:58651            6        1       0           52          0           260         0           go       1.1.0
  ::1:58922            38       1       0           21          0           105         0           go       1.1.0
  ::1:58953            39       1       0           21          0           105         0           go       1.1.0
```

## 6. Sort nats-top statistics

In nats-top, enter the command `o` followed by the option, such as `bytes_to`. You see that nats-top sorts the BYTES\_TO column in ascending order.

```
nats-server version 0.6.6 (uptime: 45m40s)
Server:
  Load: CPU:  0.0%  Memory: 10.4M  Slow Consumers: 0
  In:   Msgs: 81  Bytes: 427  Msgs/Sec: 0.0  Bytes/Sec: 0
  Out:  Msgs: 154  Bytes: 792  Msgs/Sec: 0.0  Bytes/Sec: 0
sort by [bytes_to]:
Connections: 3
  HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION
  ::1:59259            83       1       0           4           0           20          0           go       1.1.0
  ::1:59349            91       1       0           2           0           10          0           go       1.1.0
  ::1:59342            90       1       0           0           0           0           0           go       1.1.0
```

## 7. Use different sort options

Use some different sort options to explore nats-top, such as:

`cid`, `subs`, `pending`, `msgs_to`, `msgs_from`, `bytes_to`, `bytes_from`, `lang`, `version`

You can also set the sort option on the command line using the `-sort` flag. For example: `nats-top -sort bytes_to`.

## 8. Display the registered subscriptions.

In nats-top, enter the command `s` to toggle displaying connection subscriptions. When enabled, you see the subscription subject in nats-top table:

```
nats-server version 0.6.6 (uptime: 1h2m23s)
Server:
  Load: CPU:  0.0%  Memory: 10.4M  Slow Consumers: 0
  In:   Msgs: 108  Bytes: 643  Msgs/Sec: 0.0  Bytes/Sec: 0
  Out:  Msgs: 185  Bytes: 1.0K  Msgs/Sec: 0.0  Bytes/Sec: 0

Connections: 3
  HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION SUBSCRIPTIONS
  ::1:59708            115      1       0           6           0           48          0           go       1.1.0   foo.bar
  ::1:59758            122      1       0           1           0           8           0           go       1.1.0   foo
  ::1:59817            124      1       0           0           0           0           0           go       1.1.0   foo
```

## 9. Quit nats-top

Use the `q` command to quit nats-top.

## 10. Restart nats-top with a specified query

For example, to query for the connection with largest number of subscriptions:

```bash
nats-top -n 1 -sort subs
```

Result: nats-top displays only the client connection with the largest number of subscriptions:

```
nats-server version 0.6.6 (uptime: 1h7m0s)
Server:
  Load: CPU:  0.0%  Memory: 10.4M  Slow Consumers: 0
  In:   Msgs: 109  Bytes: 651  Msgs/Sec: 0.0  Bytes/Sec: 0
  Out:  Msgs: 187  Bytes: 1.0K  Msgs/Sec: 0.0  Bytes/Sec: 0

Connections: 3
  HOST                 CID      SUBS    PENDING     MSGS_TO     MSGS_FROM   BYTES_TO    BYTES_FROM  LANG     VERSION
  ::1:59708            115      1       0           6           0           48          0           go       1.1.0
```


# Developing With NATS

Developing with NATS involves a blend of distributed application techniques, common NATS features, and library-specific syntax. Besides this guide, most libraries provide auto-generated API documentation, along with language and platform-specific examples, guides, and other resources.

| Language   | Links                                                                                                                                                                                                                                                                                 | Supported by Synadia |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Golang     | [nats.go](https://github.com/nats-io/nats.go), [godoc](http://godoc.org/github.com/nats-io/nats.go)                                                                                                                                                                                   | Yes                  |
| Java       | [nats.java](https://github.com/nats-io/nats.java), [javadoc](https://javadoc.io/doc/io.nats/jnats), [nats.java examples](https://github.com/nats-io/nats.java/tree/main/src/examples/java/io/nats/examples), [java-nats-examples repo](https://github.com/nats-io/java-nats-examples) | Yes                  |
| .NET       | [nats.net](https://github.com/nats-io/nats.net), [docs](http://nats-io.github.io/nats.net/), [package](https://www.nuget.org/packages/NATS.Net)                                                                                                                                       | Yes                  |
| Rust       | [nats.rs](https://github.com/nats-io/nats.rs), [rust doc](https://docs.rs/async-nats/latest/async_nats/)                                                                                                                                                                              | Yes                  |
| JavaScript | [nats.js](https://github.com/nats-io/nats.js), [jsdoc](https://nats-io.github.io/nats.js/)                                                                                                                                                                                            | Yes                  |
| Python     | [nats.py](https://github.com/nats-io/nats.py), [doc](https://nats-io.github.io/nats.py/)                                                                                                                                                                                              | Yes                  |
| C          | [nats.c](https://github.com/nats-io/nats.c), [doc](http://nats-io.github.io/nats.c)                                                                                                                                                                                                   | Yes                  |
| Ruby       | [nats-pure.rb](https://github.com/nats-io/nats-pure.rb), [yard](https://www.rubydoc.info/gems/nats)                                                                                                                                                                                   |                      |
| Elixir     | [nats.ex](https://github.com/nats-io/nats.ex), [hex doc](https://hex.pm/packages/gnat)                                                                                                                                                                                                |                      |
| Zig        | [nats.zig](https://github.com/nats-io/nats.zig)                                                                                                                                                                                                                                       |                      |
| Swift      | [nats.swift](https://github.com/nats-io/nats.swift)                                                                                                                                                                                                                                   |                      |

Not all libraries have their own documentation, depending on the language community, but be sure to check out the client libraries' README for more information.

There are many other NATS client libraries and examples contributed and maintained by the community and available on GitHub, such as:

* [Kotlin](https://github.com/nats-io/kotlin-nats-examples)
* [Dart](https://github.com/dgofman/nats_client), [Dart](https://github.com/chartchuo/dart-nats) and [Dart](https://github.com/c16a/nats-dart)
* [Tcl](https://github.com/Kazmirchuk/nats-tcl)
* [Crystal](https://github.com/jgaskins/nats)
* [PHP](https://github.com/basis-company/nats.php) and [PHP](https://github.com/repejota/phpnats)
* [Pascal](https://github.com/biot2/nats.pas/blob/main/nats.core.pas)
* and many [more](https://github.com/search?o=desc\&p=1\&q=nats+client\&s=updated\&type=Repositories)...


# Anatomy of a NATS application

## What do you use NATS for?

You can use NATS to exchange information with and make requests to other applications. You can also use NATS to make your application into a distributed peer-to-peer application.

At a high level your application can use NATS to:

1. Send (Publish) information to other applications or instances of your application.
2. Receive (Subscribe) information (in real-time or whenever your application runs) from other applications or instances of your application.
3. Make a request to a server or the service provided by another application.
4. Store shared (consistent) state/data between other applications or instances of your application.
5. Be informed in real-time about any new data being sent, or any changes to the shared state/data.

Using NATS means that, as an application developer you never have to worry about:

* Who sends the information that you want to receive.
* Who is interested in the information you are sending to others, or how many are interested or where they are.
* Where the service you are sending a request to is located, or how many currently active instances of that service there are.
* How many partitions or servers there are in the cluster.
* Security (just identify yourself).
* Whether your application is up and running at the time the information is sent or not (using JetStream).
* Flow control (using JetStream)
* Higher qualities of services such as **exactly-once** (using JetStream)
* Fault-tolerance, and which servers are up or down at any given time.
* The topology of the NATS server infrastructure or how it is architected.

## Anatomy of a NATS Client Application

A NATS Client Application will use the NATS Client Library in the following way:

At initialization time it will first connect (securely if needed) to a NATS Service Infrastructure (i.e. one of the NATS servers).

Once successfully connected the application will:

* Create messages and publish them to subjects or streams.
* Subscribe to subject(s) or stream consumers to receive messages from other processes.
* Publish request messages to a service and receive a reply message.
* Receive request messages and send back replies or acknowledgements.
* Associate and retrieve messages associated with keys in KV buckets.
* Store and retrieve arbitrary large blobs with keys in the object store.

Finally, when the application terminates it should disconnect from the NATS Service Infrastructure.

See the following sections to learn more about those activities.

## Connecting and disconnecting

The first thing any application needs to do is connect to NATS. Depending on the way the NATS Service Infrastructure being used is configured the connection may need to be secured, and therefore the application also needs to be able to specify security credentials at connection time. An application can create as many NATS connections as needed (each connection being completely independent, it could for example connect twice as two different users), although typically most applications only make a single NATS connection.

Once you have obtained a valid connection, you can use that connection in your application to use all of the Core NATS functionalities such as subscribing to subjects, publishing messages, making requests (and getting a JetStream context).

Finally, the application will need to disconnect safely from NATS.

### [Connect to NATS](https://docs.nats.io/using-nats/developer/connecting)

### Monitoring the NATS connection

It is recommended that the application use [connection event listeners](https://docs.nats.io/using-nats/developer/connecting/events/events) in order to be alerted and log whenever connections, reconnections or disconnections happen. Note that in case of a disconnection from the NATS server process the client library will automatically attempt to [reconnect](https://docs.nats.io/using-nats/developer/connecting/reconnect) to one of the other NATS servers in the cluster. You can also always check the [current connection status](https://docs.nats.io/using-nats/developer/connecting/events).

### Disconnecting safely from NATS

The recommended way to disconnect is to use [Drain()](https://docs.nats.io/using-nats/developer/receiving/drain) which will wait for any ongoing processing to conclude and clean everything properly, but if you need to close the connection immediately you can use `close()` from your connection object.

## Working with messages

Messages store the data that applications exchange with each other. A message has a *subject*, a *data payload* (byte array), and may also have a *reply-to* and *header* fields.

You get messages returned or passed to your callbacks from subscribing, or making requests. The publish (and request) operations typically just take a subject and a byte array data payload and create the message for you, but you can also create a message yourself (if you want to set some headers).

Some messages can be 'acknowledged' (for example message received from JetStream pull consumers), and there are multiple forms of acknowledgements (including negative acknowledgements, and acknowledgements indicating that your application has properly received the message but needs more time to process it).

#### Structured data

Some libraries allow you to easily [send](https://docs.nats.io/using-nats/developer/sending/structure) and [receive](https://docs.nats.io/using-nats/developer/receiving/structure) structured data.

## Using Core NATS

Once your application has successfully connected to the NATS Server infrastructure, you can then start using the returned connection object to interact with NATS.

### Core NATS Publishing

You can directly [publish](https://docs.nats.io/using-nats/developer/sending) on a connection some data addressed by a subject (or publish a pre-created messages with headers).

#### Flush and Ping/Pong

Because of caching, if your application is highly sensitive to latency, you may want to [flush](https://docs.nats.io/using-nats/developer/sending/caches) after publishing.

Many of the client libraries use the [PING/PONG interaction](https://docs.nats.io/using-nats/developer/connecting/pingpong) built into the NATS protocol to ensure that flush pushed all of the buffered messages to the server. When an application calls flush, most libraries will put a PING on the outgoing queue of messages, and wait for the server to respond with a PONG before saying that the flush was successful.

Even though the client may use PING/PONG for flush, pings sent this way do not count towards [max outgoing pings](https://docs.nats.io/using-nats/developer/connecting/pingpong).

### Core NATS Subscribing

The process of subscribing involves having the client library tell the NATS that an application is interested in a particular subject. When an application is done with a subscription it unsubscribes telling the server to stop sending messages.

Receiving messages with NATS can be library dependent, some languages, like Go or Java, provide synchronous and asynchronous APIs, while others may only support one type of subscription. In general, applications can receive messages [asynchronously](https://docs.nats.io/using-nats/developer/receiving/async) or [synchronously](https://docs.nats.io/using-nats/developer/receiving/sync).

You can always subscribe to more than one subject at a time using [wildcards](https://docs.nats.io/using-nats/developer/receiving/wildcards).

A client will receive a message for each matching subscription, so if a connection has multiple subscriptions using identical or overlapping subjects (say `foo` and `>`) the same message will be sent to the client multiple times.

#### Subscribe as part of a queue group

You can also subscribe [as part of a distributed *queue group*](https://docs.nats.io/using-nats/developer/receiving/queues). All the subscribers with the same queue group name form the distributed queue. The NATS Servers automatically distributes the messages published on the matching subject(s) between the members of the queue group.

On a given subject there can be more than one queue group created by subscribing applications, each queue group being an independent queue and distributing its own copy of the messages between the queue group members.

#### Slow consumers

One thing to keep in mind when making Core NATS subscriptions to subjects is that your application must be able to keep up with the flow of messages published on the subject(s) or it will otherwise become a [slow consumer](https://docs.nats.io/using-nats/developer/connecting/events/slow)

### Unsubscribing

When you no longer want to receive the messages on a particular subject you must call [unsubscribe](https://docs.nats.io/using-nats/developer/receiving/unsubscribing), or you can [automatically unsubscribe](https://docs.nats.io/using-nats/developer/receiving/unsub_after) after receiving a specific number of messages.

### Making requests to services

You can also use NATS to easily and transparently invoke services without needing to know about the location or number of servers for the service. The connection's [request](https://docs.nats.io/using-nats/developer/sending/request_reply) call publishes a message on the specified subject that contains a [reply-to](https://docs.nats.io/using-nats/developer/sending/replyto) inbox subject and then waits for a reply message to be received by that inbox.

### Servicing and replying to requests

The server applications servicing those requests simply need to subscribe to the subject on which the requests are published, process the request messages they receive and [reply](https://docs.nats.io/using-nats/developer/receiving/reply) to the message on the subject contained in the request message's [Reply-to](https://docs.nats.io/using-nats/developer/receiving/reply) attribute.

Typically, there is no reason not to want to make your service distributed (i.e. scalable and fault-tolerant). This means that unless there's a specific reason not to, application servicing requests should [subscribe to the request subject using the same queue group name](https://docs.nats.io/using-nats/developer/receiving/queues). You can have more than one queue group present on a subject (for example you could have one queue group to distribute the processing of the requests between service instances, and another queue group to distribute the logging or monitoring of the requests being made to the service).

## Streaming with JetStream

Some applications can make use of the extra functionalities enabled by [JetStream](https://docs.nats.io/using-nats/developer/develop_jetstream) (streams, KV Store, Object Store). Just like you use the Core NATS connection object to invoke Core NATS operations, you use a [*JetStream context*](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/js/context.md) to invoke JetStream operations. You can specify things like the timeout value for all the operations executed from the context. JS context are light-weight, so while it is safe to share a JS context between threads, for best performance do not be afraid to have a context per thread.

### Streaming functionalities

You can use [streams](https://docs.nats.io/using-nats/develop_jetstream/model_deep_dive#stream-limits-retention-and-policy) for two broad use cases:

* Temporal decoupling: the ability for a subscribing application to get on demand a replay of the messages stored in the stream due to past (and possibly future) publications.
* Queuing: the ability for instances of the subscribing application to get, and safely process and remove (i.e. consume) from the stream individual or batches of messages, effectively using a stream as a distributed work queue.

### Defining streams

Before you can use a stream to replay or consume messages published on a subject, it must be defined. The stream definition attributes specify

* what is being stored (i.e. which subject(s) the stream monitors)
* how it is being stored (e.g. file or memory storage, number of replicas)
* how long the messages are stored (e.g. depending on limits, or on interest, or as a work queue): the retention policy

Streams can be (and often are) administratively defined ahead of time (for example using the NATS CLI Tool). The application can also [manage streams (and consumers) programmatically](https://docs.nats.io/using-nats/developer/develop_jetstream/streams).

### Publishing to streams

Any message published, on a subject monitored by a stream gets stored in the stream. If your application publishes a message using the Core NATS publish call (from the connection object) on a stream's subject, the message will get stored in the stream, the Core NATS publishers do not know or care whether there is a stream for that subject or not. However, if you know that there is going to be a stream defined for that subject you will get higher quality of service by [publishing using the JetStream Context's publish call](https://docs.nats.io/using-nats/developer/develop_jetstream/publish) (rather than the connection's publish call). This is because JetStream publications will receive an acknowledgement (or not) from the NATS Servers when the message has been positively received *and* stored in the stream (while Core NATS publications are not acknowledged by the NATS Servers). This difference is also the reason why there are both synchronous and asynchronous versions of the JetStream publish operation.

### Stream consumers

Stream *consumers* are how application get messages from stream. To make another analogy to database concepts a consumers can be seen as a kind of 'views' (on a stream):

* Consumers can have a *subject filter* to select messages from the stream according to their subject names.
* Consumers have an *ack policy* which defines whether application must *acknowledge* the reception and processing of the messages being sent to them by the consumers (note that explicit acknowledgements are *required* for some types of streams and consumer to work properly). As well as how long to wait for acknowledgements for and how many times the consumer should try to re-deliver un-acknowledged messages for.
* Consumers have a [*deliver policy*](https://docs.nats.io/using-nats/develop_jetstream/model_deep_dive#consumer-starting-position) specifying where in the stream the consumer should start delivering messages from.
* Consumers have a *replay policy* to specify the speed at which messages are being replayed at by the consumer.

Consumers also have a small amount of state on the NATS Server to store some message sequence numbers 'cursors'. You can have as many consumers as you need per stream.

Client applications either create *ephemeral* consumers, or define/find *durable* consumers. Applications either subscribe to 'push' consumers (consumers defined with a delivery subject and optionally a queue group name for that delivery subject), or fetch on demand (including an optional prefetch) from 'pull' consumers (consumers defined without a delivery subject or queue group name as they don't need any while providing the same functionality).

#### Ephemeral consumers

[Ephemeral consumers](https://docs.nats.io/using-nats/develop_jetstream/model_deep_dive#ephemeral-consumers) are, as the name suggest, not meant to last and are automatically cleaned up by the NATS Servers when the application instance that created them shuts down. Ephemeral consumers are created on-demand by individual application instances and are used only by the application instance that created them.

Applications typically use ephemeral *ordered push consumers* to get they own copy of the messages stored in a stream whenever they want.

#### Durable consumers

Durable consumers are, as the name suggest, meant to be 'always on', and used (shared) by multiple instances of the client application or by applications that get stopped and restarted multiple times and need to maintain state from one run of the application to another.

Durable consumers can be managed administratively using the NATS CLI Tool, or programmatically by the application itself. A consumer is created as a durable consumer simply by specifying a durable name at creation time.

Applications typically use *durable pull consumers* to distribute and scale horizontally the processing (or consumption) of the messages in a stream.

#### Consumer acknowledgements

Some types of consumers (e.g. pull consumers) require the application receiving messages from the consumer to *explicitly* [acknowledge](https://docs.nats.io/using-nats/develop_jetstream/model_deep_dive#acknowledgement-models) the reception and processing of those messages. The application can invoke one of the following acknowledgement functions on the message received from the consumer:

* `ack()` to positively acknowledge the reception and processing of the message
* `term()` to indicate that the message could not be and will never be able to be processed and should not be sent again later. Use term when the request is invalid.
* `nack()` to negatively acknowledge the processing of the message, indicating that the message should be sent again. Use nack when the request is valid but you are unable to process it. If this inability to process happens because of a temporary condition, you should also close your subscription temporarily until you are able to process again.
* `inProgress()` to indicate that the processing of the message is still on-going and more time is needed (before the message is considered for being sent again)

### Higher Qualities of Service

Besides temporal decoupling and queuing, JetStream also enables higher qualities of service compared to Core NATS. Defining a stream on a subject and using consumers brings the quality of service up to *at least once*, meaning that you are guaranteed to get the message (even if your application is down at publication time) but there are some corner case failure scenarios in which you could result in message duplication due to double publication of the message, or double processing of a message due to acknowledgement loss or crashing after processing but before acknowledging. You can enable and use [message de-duplication](https://docs.nats.io/using-nats/develop_jetstream/model_deep_dive#message-deduplication) and double-acking to protect against those failure scenarios and get [exactly once](https://docs.nats.io/using-nats/develop_jetstream/model_deep_dive#exactly-once-delivery) quality of service.

### Key Value Store

The [Key Value Store](https://docs.nats.io/using-nats/developer/develop_jetstream/kv) functionality is implemented on top of JetStream, but offers a different interface in the form of keys and values rather than subject names and messages. You can use a bucket to put (including compare and set), get and delete a value (a byte array like a message payload) associated with a key (a string, like a subject). It also allows you to 'watch' for changes to the bucket as they happen. And finally it allows you to maintain a history of the values associated with a key over time, as well as get a specific revision of the value.

### Object Store

**NOTICE: Technology Preview**

The Object Store is similar to the Key Value Store but meant to be used where the values can be of any arbitrary large size, as opposed to limited to the maximum size of a NATS message, as it the case with the Key Value Store.


# Connecting

In order for a NATS client application to connect to the NATS service, and then subscribe or publish messages to subjects, it needs to be able to be configured with the details of how to connect to the NATS service infrastructure and of how to authenticate with it.

## NATS URL

1. A 'NATS URL' is a string (in a URL format) that specifies the IP address and port where the NATS server(s) can be reached, and what kind of connection to establish:
   * TLS encrypted *only* TCP connection (i.e. NATS URLs starting with `tls://...`)
   * TLS encrypted if the server is configured for it or plain un-encrypted TCP connection otherwise (i.e. NATS URLs starting with `nats://...`)
   * Websocket connection (i.e. NATS URLs starting with `ws://...`)

### Connecting to clusters

Note that when connecting to a NATS service infrastructure with clusters there is more than one URL and the application should allow for more than one URL to be specified in its NATS connect call (typically you pass a comma separated list of URLs as the URL, e.g. `"nats://server1:port1,nats://server2:port2"`).

When connecting to a cluster it is best to provide the complete set of 'seed' URLs for the cluster.

## Authentication details

1. If required: authentication details for the application to identify itself with the NATS server(s). NATS supports multiple authentication schemes:
   * [Username/Password credentials](https://docs.nats.io/using-nats/developer/connecting/userpass) (which can be passed as part of the NATS URL)
   * [Decentralized JWT Authentication/Authorization](https://docs.nats.io/using-nats/developer/connecting/creds) (where the application is configured with the location of 'credentials file' containing the JWT and private Nkey)
   * [Token Authentication](https://docs.nats.io/using-nats/developer/token#connecting-with-a-token) (where the application is configured with a Token string)
   * [TLS Certificate](https://docs.nats.io/using-nats/developer/tls#connecting-with-tls-and-verify-client-identity) (where the client is configured to use a client TLS certificate and the servers are configured to map the TLS client certificates to users defined in the server configuration)
   * [NKEY with Challenge](https://docs.nats.io/using-nats/developer/connecting/nkey) (where the client is configured with a Seed and User NKeys)

### Runtime configuration

Your application should expose a way to be configured at run time with the NATS URL(s) to use. If you want to use a secure infrastructure, the application must provide for the definition of either the credentials file (.creds) to use, or the means to encode the token, or Nkey, in the URL(s).

## Connection Options

Besides the connectivity and security details, there are numerous options for a NATS connection ranging from [timeouts](https://docs.nats.io/using-nats/developer/reconnect#connection-timeout-attributes) to [reconnect settings](https://docs.nats.io/using-nats/developer/reconnect#reconnection-attributes) to setting [asynchronous error and connection event callback handlers](https://docs.nats.io/using-nats/developer/reconnect#advisories) in your application.

## See Also

WebSocket and NATS

{% embed url="<https://www.youtube.com/watch?v=AbAR9zgJnjY>" %}
WebSocket and NATS | Hello World
{% endembed %}

NATS WebSockets and React

{% embed url="<https://www.youtube.com/watch?v=XS_Q0i6orSk>" %}
NATS WebSockets and React
{% endembed %}


# Connecting to the Default Server

Some libraries also provide a special way to connect to a *default* url, which is generally `nats://localhost:4222`:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect(nats.DefaultURL)
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect();

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect();
// Do something with the connection
doSomething();
// When done close it
await nc.close();
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect()

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

// It's optional to call ConnectAsync()
// as it will be called when needed automatically
await client.ConnectAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn = NULL;
natsStatus          s;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
if (s != NATS_OK)
  // handle error

// Destroy connection, no-op if conn is NULL.
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Connecting to a Specific Server

The NATS client libraries can take a full URL, `nats://demo.nats.io:4222`, to specify a specific server host and port to connect to.

Libraries are removing the requirement for an explicit protocol and may allow `demo.nats.io:4222` or just `demo.nats.io`. In the later example the default port 4222 will be used. Check with your specific client library's documentation to see what URL formats are supported.

For example, to connect to the demo server with a URL you can use:

{% tabs %}
{% tab title="Go" %}

```java
// If connecting to the default port, the URL can be simplified
// to just the hostname/IP.
// That is, the connect below is equivalent to:
// nats.Connect("nats://demo.nats.io:4222")
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection nc = Nats.connect("nats://demo.nats.io:4222");
```

{% endtab %}

{% tab title="Java" %}

```
// Connection is AutoCloseable
try (Connection nc = Nats.connect("nats://demo.nats.io:4222")) {
    // Do something with the connection
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({ servers: "demo.nats.io" });
// Do something with the connection
doSomething();
await nc.close();
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(servers=["nats://demo.nats.io:4222"])

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient("nats://demo.nats.io:4222");

// It's optional to call ConnectAsync()
// as it will be called when needed automatically
await client.ConnectAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://demo.nats.io:4222"]) do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn = NULL;
natsStatus          s;

// If connecting to the default port, the URL can be simplified
// to just the hostname/IP.
// That is, the connect below is equivalent to:
// natsConnection_ConnectTo(&conn, "nats://demo.nats.io:4222");
s = natsConnection_ConnectTo(&conn, "demo.nats.io");
if (s != NATS_OK)
  // handle error

// Destroy connection, no-op if conn is NULL.
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Connecting to a Cluster

When connecting to a cluster, there are a few things to think about.

* Passing a URL for each cluster member (semi-optional)
* The connection algorithm
* The reconnect algorithm (discussed later)
* Server provided URLs

When a client library first tries to connect it will use the list of URLs provided to the connection options or function. These URLs are usually checked in random order as to not have every client connect to the same server. The first successful connection is used. Randomization can be [explicitly disabled](https://docs.nats.io/using-nats/developer/connecting/reconnect/random).

After a client connects to the server, the server may provide a list of URLs for additional known servers. This allows a client to connect to one server and still have other servers available during reconnect.

To ensure the initial connection, your code should include a list of reasonable *front line* or *seed* servers. Those servers may know about other members of the cluster, and may tell the client about those members. But you don't have to configure the client to pass every valid member of the cluster in the connect method.

By providing the ability to pass multiple connect options, NATS can handle the possibility of a machine going down or being unavailable to a client. By adding the ability of the server to feed clients a list of known servers as part of the client-server protocol the mesh created by a cluster can grow and change organically while the clients are running.

*Note, failure behavior is library dependent, please check the documentation for your client library on information about what happens if the connect fails.*

{% tabs %}
{% tab title="Go" %}

```go
servers := []string{"nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"}

nc, err := nats.Connect(strings.Join(servers, ","))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://127.0.0.1:1222,nats://127.0.0.1:1223,nats://127.0.0.1:1224")
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    servers: [
      "nats://demo.nats.io:4222",
      "nats://localhost:4222",
    ],
});
// Do something with the connection
doSomething();
// When done close it
await nc.close();
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(servers=[
   "nats://127.0.0.1:1222",
   "nats://127.0.0.1:1223",
   "nats://127.0.0.1:1224"
   ])

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient("nats://127.0.0.1:1222,nats://127.0.0.1:1223,nats://127.0.0.1:1224");

// It's optional to call ConnectAsync()
// as it will be called when needed automatically
await client.ConnectAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"]) do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;
const char          *servers[] = {"nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"};

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetServers(opts, servers, 3);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Connection Name

Connections can be assigned a name which will appear in some of the server monitoring data. This name is not required, but is **highly recommended** as a friendly connection name will help in monitoring, error reporting, debugging, and testing.

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io", nats.Name("API Name Option Example"))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .connectionName("API Name Option Example") // Set Name
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
 const nc = await connect({
    name: "my-connection",
    servers: ["demo.nats.io:4222"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(
    servers=["nats://demo.nats.io:4222"], 
    name="API Name Option Example")

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient(name: "API Name Option Example", url: "nats://demo.nats.io:4222");

// It's optional to call ConnectAsync()
// as it will be called when needed automatically
await client.ConnectAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://demo.nats.io:4222"], name: "API Name Option Example") do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsOptions         *opts    = NULL;
natsStatus          s        = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetName(opts, "API Name Option Example");
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Authenticating with a User and Password

For this example, start the server using:

```bash
nats-server --user myname --pass password
```

You can encrypt passwords to pass to `nats-server` using the simple [NATS CLI tool:](https://docs.nats.io/using-nats/nats-tools/nats_cli)

```bash
nats server passwd
```

```
? Enter password [? for help] **********************
? Reenter password [? for help] **********************

$2a$11$qbtrnb0mSG2eV55xoyPqHOZx/lLBlryHRhU3LK2oOPFRwGF/5rtGK
```

and use the hashed password in the server config. The client still uses the plain text version.

The code uses localhost:4222 so that you can start the server on your machine to try them out.

## Connecting with a User/Password

When logging in with a password `nats-server` will take either a plain text password or an encrypted password.

{% tabs %}
{% tab title="Go" %}

```go
// Set a user and plain text password
nc, err := nats.Connect("127.0.0.1", nats.UserInfo("myname", "password"))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://localhost:4222")
    .userInfo("myname","password") // Set a user and plain text password
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
 const nc = await connect({
      port: ns.port,
      user: "byname",
      pass: "password",
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://myname:password@demo.nats.io:4222"])

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://localhost:4222",
    AuthOpts = new NatsAuthOpts
    {
        Username = "myname",
        Password = "password",
    }
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers:["nats://myname:password@127.0.0.1:4222"], name: "my-connection") do |nc|
   nc.on_error do |e|
    puts "Error: #{e}"
  end

   nc.on_reconnect do
    puts "Got reconnected to #{nc.connected_server}"
  end

  nc.on_disconnect do |reason|
    puts "Got disconnected! #{reason}"
  end

  nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetUserInfo(opts, "myname", "password");
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

## Connecting with a User/Password in the URL

Most clients make it easy to pass the user name and password by accepting them in the URL for the server. This standard format is:

> nats\://*user*:*password*@server:port

Using this format, you can connect to a server using authentication as easily as you connected with a URL:

{% tabs %}
{% tab title="Go" %}

```go
// Set a user and plain text password
nc, err := nats.Connect("myname:password@127.0.0.1")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://myname:password@localhost:4222");

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// JavaScript clients don't support username/password in urls use `user` and `pass` options.
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://myname:password@demo.nats.io:4222"])

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var nc = new NatsClient(new NatsOpts
{
    // .NET client doesn't support username/password in URLs
    // use `Username` and `Password` options.
    Url = "nats://demo.nats.io:4222",
    AuthOpts = new NatsAuthOpts
    {
        Username = "myname",
        Password = "password",
    }
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers:["nats://myname:password@127.0.0.1:4222"], name: "my-connection") do |nc|
   nc.on_error do |e|
    puts "Error: #{e}"
  end

   nc.on_reconnect do
    puts "Got reconnected to #{nc.connected_server}"
  end

  nc.on_disconnect do |reason|
    puts "Got disconnected! #{reason}"
  end

  nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetURL(opts, "nats://myname:password@127.0.0.1:4222");
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Authenticating with a Token

Tokens are basically random strings, much like a password, and can provide a simple authentication mechanism in some situations. However, tokens are only as safe as they are secret so other authentication schemes can provide more security in large installations. It is highly recommended to use one of the other NATS authentication mechanisms.

For this example, start the server using:

```bash
nats-server --auth mytoken
```

The code uses localhost:4222 so that you can start the server on your machine to try them out.

## Connecting with a Token

{% tabs %}
{% tab title="Go" %}

```go
// Set a token
nc, err := nats.Connect("127.0.0.1", nats.Name("API Token Example"), nats.Token("mytoken"))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .token("mytoken") // Set a token
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
  port: ns.port,
  token: "aToK3n",
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"], token="mytoken")

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "127.0.0.1",
    Name = "API Token Example",
    AuthOpts = new NatsAuthOpts
    {
        Token = "mytoken"
    }
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
NATS.start(token: "mytoken") do |nc|
  puts "Connected using token"
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetToken(opts, "mytoken");
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

## Connecting with a Token in the URL

Some client libraries will allow you to pass the token as part of the server URL using the form:

> nats\://*token*@server:port

Again, once you construct this URL you can connect as if this was a normal URL.

{% tabs %}
{% tab title="Go" %}

```go
// Token in URL
nc, err := nats.Connect("mytoken@localhost")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://mytoken@localhost:4222");//Token in URL

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
  // JavaScript doesn't support tokens in urls use the `token` option
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://mytoken@demo.nats.io:4222"])

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    // .NET client doesn't support tokens in URLs
    // use Token option instead.
    AuthOpts = new NatsAuthOpts
    {
        Token = "mytoken"
    }
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
NATS.start("mytoken@127.0.0.1:4222") do |nc|
  puts "Connected using token!"
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetURL(opts, "nats://mytoken@127.0.0.1:4222");
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Authenticating with an NKey

The 2.0 version of NATS server introduces a new challenge response authentication option. This challenge response is based on a wrapper we call [NKeys](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth). The server can use these keys in several ways for authentication. The simplest is for the server to be configured with a list of known public keys and for the clients to respond to the challenge by signing it with its private key. (A printable private NKey is referred to as seed). This challenge-response ensures security by ensuring that the client has the private key, but also protects the private key from the server, which never has access to it!

Handling challenge response may require more than just a setting in the connection options, depending on the client library.

{% tabs %}
{% tab title="Go" %}

```go
opt, err := nats.NkeyOptionFromSeed("seed.txt")
if err != nil {
    log.Fatal(err)
}
nc, err := nats.Connect("127.0.0.1", opt)
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
NKey theNKey = NKey.createUser(null); // really should load from somewhere
Options options = new Options.Builder()
    .server("nats://localhost:4222")
    .authHandler(new AuthHandler(){
        public char[] getID() {
            try {
                return theNKey.getPublicKey();
            } catch (GeneralSecurityException|IOException|NullPointerException ex) {
                return null;
            }
        }

        public byte[] sign(byte[] nonce) {
            try {
                return theNKey.sign(nonce);
            } catch (GeneralSecurityException|IOException|NullPointerException ex) {
                return null;
            }
        }

        public char[] getJWT() {
            return null;
        }
    })
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// seed should be stored and treated like a secret
const seed = new TextEncoder().encode(
  "SUAEL6GG2L2HIF7DUGZJGMRUFKXELGGYFMHF76UO2AYBG3K4YLWR3FKC2Q",
);
const nc = await connect({
  port: ns.port,
  authenticator: nkeyAuthenticator(seed),
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

async def error_cb(e):
    print("Error:", e)

await nc.connect("nats://localhost:4222",
                 nkeys_seed="./path/to/nkeys/user.nk",
                 error_cb=error_cb,
                 )

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "127.0.0.1",
    Name = "API NKey Example",
    AuthOpts = new NatsAuthOpts
    {
        NKeyFile = "/path/to/nkeys/user.nk"
    }
});
```

{% endtab %}

{% tab title="C" %}

```c
static natsStatus
sigHandler(
    char            **customErrTxt,
    unsigned char   **signature,
    int             *signatureLength,
    const char      *nonce,
    void            *closure)
{
    // Sign the given `nonce` and return the signature as `signature`.
    // This needs to allocate memory. The length of the signature is
    // returned as `signatureLength`.
    // If an error occurs the user can return specific error text through
    // `customErrTxt`. The library will free this pointer.

    return NATS_OK;
}

(...)

natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;
const char          *pubKey    = "my public key......";

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetNKey(opts, pubKey, sigHandler, NULL);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Authenticating with a Credentials File

The 2.0 version of NATS server introduced the idea of decentralized authentication based on [JSON Web Tokens (JWT)](https://jwt.io/). Clients interact with this new scheme using a [user JWT](https://docs.nats.io/running-a-nats-service/nats_admin/security) and corresponding [NKey](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/auth_intro/nkey_auth) private key. To help make connecting with a JWT easier, the client libraries support the concept of a credentials file. This file contains both the private key and the JWT and can be generated with the `nsc` [tool](https://docs.nats.io/using-nats/nats-tools/nsc). The contents will look like the following and should be protected because it contains a private key. This credentials file is unused and only for example purposes.

```
-----BEGIN NATS USER JWT-----
eyJ0eXAiOiJqd3QiLCJhbGciOiJlZDI1NTE5In0.eyJqdGkiOiJUVlNNTEtTWkJBN01VWDNYQUxNUVQzTjRISUw1UkZGQU9YNUtaUFhEU0oyWlAzNkVMNVJBIiwiaWF0IjoxNTU4MDQ1NTYyLCJpc3MiOiJBQlZTQk0zVTQ1REdZRVVFQ0tYUVM3QkVOSFdHN0tGUVVEUlRFSEFKQVNPUlBWV0JaNEhPSUtDSCIsIm5hbWUiOiJvbWVnYSIsInN1YiI6IlVEWEIyVk1MWFBBU0FKN1pEVEtZTlE3UU9DRldTR0I0Rk9NWVFRMjVIUVdTQUY3WlFKRUJTUVNXIiwidHlwZSI6InVzZXIiLCJuYXRzIjp7InB1YiI6e30sInN1YiI6e319fQ.6TQ2ilCDb6m2ZDiJuj_D_OePGXFyN3Ap2DEm3ipcU5AhrWrNvneJryWrpgi_yuVWKo1UoD5s8bxlmwypWVGFAA
------END NATS USER JWT------

************************* IMPORTANT *************************
NKEY Seed printed below can be used to sign and prove identity.
NKEYs are sensitive and should be treated as secrets.

-----BEGIN USER NKEY SEED-----
SUAOY5JZ2WJKVR4UO2KJ2P3SW6FZFNWEOIMAXF4WZEUNVQXXUOKGM55CYE
------END USER NKEY SEED------

*************************************************************
```

Given a creds file, a client can authenticate as a specific user belonging to a specific account:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("127.0.0.1", nats.UserCredentials("path_to_creds_file"))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://localhost:4222")
    .authHandler(Nats.credentials("path_to_creds_file"))
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// credentials file contains the JWT and the secret signing key
  const authenticator = credsAuthenticator(creds);
  const nc = await connect({
    port: ns.port,
    authenticator: authenticator,
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

async def error_cb(e):
    print("Error:", e)

await nc.connect("nats://localhost:4222",
                 user_credentials="path_to_creds_file",
                 error_cb=error_cb,
                 )

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient("127.0.0.1", credsFile: "/path/to/file.creds");
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    // Pass the credential file this way if the file contains both user JWT and seed.
    // Otherwise, if the content is split, the first file is the user JWT, the second
    // contains the seed.
    s = natsOptions_SetUserCredentialsFromFiles(opts, "path_to_creds_file", NULL);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Encrypting Connections with TLS

## Encrypting Connections with TLS

While authentication limits which clients can connect, TLS can be used to encrypt traffic between client/server and check the server’s identity. Additionally - in the most secure version of TLS with NATS - the server can be configured to verify the client's identity, thus authenticating it. When started in [TLS mode](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls), a `nats-server` will require all clients to connect with TLS. Moreover, if configured to connect with TLS, client libraries will fail to connect to a server without TLS.

### Connecting with TLS and verify client identity

Using TLS to connect to a server that verifies the client's identity is straightforward. The client has to provide a certificate and private key. The NATS client will use these to prove it's identity to the server. For the client to verify the server's identity, the CA certificate is provided as well.

Use example certificates created in [self signed certificates for testing](https://docs.nats.io/running-a-nats-service/configuration/securing_nats/tls#creating-self-signed-certificates-for-testing).

```bash
nats-server --tls --tlscert=server-cert.pem --tlskey=server-key.pem --tlscacert rootCA.pem --tlsverify
```

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("localhost",
    nats.ClientCert("client-cert.pem", "client-key.pem"),
    nats.RootCAs("rootCA.pem"))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
// This examples requires certificates to be in the java keystore format (.jks).
// To do so openssl is used to generate a pkcs12 file (.p12) from client-cert.pem and client-key.pem.
// The resulting file is then imported int a java keystore named keystore.jks using keytool which is part of java jdk.
// keytool is also used to import the CA certificate rootCA.pem into truststore.jks.  
// 
// openssl pkcs12 -export -out keystore.p12 -inkey client-key.pem -in client-cert.pem -password pass:password
// keytool -importkeystore -srcstoretype PKCS12 -srckeystore keystore.p12 -srcstorepass password -destkeystore keystore.jks -deststorepass password
//
// keytool -importcert -trustcacerts -file rootCA.pem -storepass password -noprompt -keystore truststore.jks
class SSLUtils {
    public static String KEYSTORE_PATH = "keystore.jks";
    public static String TRUSTSTORE_PATH = "truststore.jks";
    public static String STORE_PASSWORD = "password";
    public static String KEY_PASSWORD = "password";
    public static String ALGORITHM = "SunX509";

    public static KeyStore loadKeystore(String path) throws Exception {
        KeyStore store = KeyStore.getInstance("JKS");
        BufferedInputStream in = new BufferedInputStream(new FileInputStream(path));
        try {
            store.load(in, STORE_PASSWORD.toCharArray());
        } finally {
            in.close();
        }

        return store;
    }

    public static KeyManager[] createTestKeyManagers() throws Exception {
        KeyStore store = loadKeystore(KEYSTORE_PATH);
        KeyManagerFactory factory = KeyManagerFactory.getInstance(ALGORITHM);
        factory.init(store, KEY_PASSWORD.toCharArray());
        return factory.getKeyManagers();
    }

    public static TrustManager[] createTestTrustManagers() throws Exception {
        KeyStore store = loadKeystore(TRUSTSTORE_PATH);
        TrustManagerFactory factory = TrustManagerFactory.getInstance(ALGORITHM);
        factory.init(store);
        return factory.getTrustManagers();
    }

    public static SSLContext createSSLContext() throws Exception {
        SSLContext ctx = SSLContext.getInstance(Options.DEFAULT_SSL_PROTOCOL);
        ctx.init(createTestKeyManagers(), createTestTrustManagers(), new SecureRandom());
        return ctx;
    }
}

public class ConnectTLS {
    public static void main(String[] args) {

        try {
            SSLContext ctx = SSLUtils.createSSLContext();
            Options options = new Options.Builder()
                .server("nats://localhost:4222")
                .sslContext(ctx) // Set the SSL context
                .build();
            Connection nc = Nats.connect(options);

            // Do something with the connection

            nc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// tls options available depend on the javascript
// runtime, please verify the readme for the
// client you are using for specific details
// this example showing the node library
const nc = await connect({
  port: ns.port,
  debug: true,
  tls: {
    caFile: caCertPath,
    keyFile: clientKeyPath,
    certFile: clientCertPath,
  },
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

ssl_ctx = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
ssl_ctx.load_verify_locations('rootCA.pem')
ssl_ctx.load_cert_chain(certfile='client-cert.pem',
                        keyfile='client-key.pem')
await nc.connect(io_loop=loop, tls=ssl_ctx)

await nc.connect(servers=["nats://demo.nats.io:4222"], tls=ssl_ctx)

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    TlsOpts = new NatsTlsOpts
    {
        CaFile = "rootCA.pem",
        KeyFile = "client-key.pem",
        CertFile = "client-cert.pem",
    }
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
EM.run do

  options = {
    :servers => [
      'nats://localhost:4222',
    ],
    :tls => {
      :private_key_file => 'client-key.pem',
      :cert_chain_file  => 'client-cert.pem',
      :ca_file => 'rootCA.pem'
    }
  }

  NATS.connect(options) do |nc|
    puts "#{Time.now.to_f} - Connected to NATS at #{nc.connected_server}"

    nc.subscribe("hello") do |msg|
      puts "#{Time.now.to_f} - Received: #{msg}"
    end

    nc.flush do
      nc.publish("hello", "world")
    end

    EM.add_periodic_timer(0.1) do
      next unless nc.connected?
      nc.publish("hello", "hello")
    end

    # Set default callbacks
    nc.on_error do |e|
      puts "#{Time.now.to_f } - Error: #{e}"
    end

    nc.on_disconnect do |reason|
      puts "#{Time.now.to_f} - Disconnected: #{reason}"
    end

    nc.on_reconnect do |nc|
      puts "#{Time.now.to_f} - Reconnected to NATS server at #{nc.connected_server}"
    end

    nc.on_close do
      puts "#{Time.now.to_f} - Connection to NATS closed"
      EM.stop
    end
  end
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_LoadCertificatesChain(opts, "client-cert.pem", "client-key.pem");
if (s == NATS_OK)
    s = natsOptions_LoadCATrustedCertificates(opts, "rootCA.pem");
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

### Connecting with the TLS Protocol

Clients (such as Go, Java, Javascript, Ruby and Type Script) support providing a URL containing the `tls` protocol to the NATS connect call. This will turn on TLS without the need for further code changes. However, in that case there is likely some form of default or environmental settings to allow the TLS libraries of your programming language to find certificate and trusted CAs. Unless these settings are taken into accounts or otherwise modified, this way of connecting is very likely to fail.

## See Also

* [OSCP Stapling in Java](https://nats.io/blog/java-ocsp-stapling/)


# Setting a Connect Timeout

Each library has its own, language preferred way, to pass connection options. One of the most common options is a connect timeout. It limits how long it can take to establish a connection to a server. Should multiple URLs be provided, this timeout applies to each cluster member individually. To set the maximum time to connect to a server to 10 seconds:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io", nats.Name("API Options Example"), nats.Timeout(10*time.Second))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .connectionTimeout(Duration.ofSeconds(10)) // Set timeout
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    reconnectTimeWait: 10 * 1000, // 10s
    servers: ["demo.nats.io"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(
  servers=["nats://demo.nats.io:4222"],
  connect_timeout=10)

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://demo.nats.io:4222",
    ConnectTimeout = TimeSpan.FromSeconds(10)
});

// You don't have to call ConnectAsync() explicitly,
// first operation will make the connection otherwise.
await client.ConnectAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# There is currently no connect timeout as part of the Ruby NATS client API, but you can use a timer to mimic it.
require 'nats/client'

timer = EM.add_timer(10) do
  NATS.connect do |nc|
    # Do something with the connection

    # Close the connection
    nc.close
  end
end
EM.cancel_timer(timer)
```

{% endtab %}

{% tab title="C" %}

```c
nnatsConnection      *conn    = NULL;
 natsOptions         *opts    = NULL;
 natsStatus          s        = NATS_OK;

 s = natsOptions_Create(&opts);
 if (s == NATS_OK)
     // Set the timeout to 10 seconds (10,000 milliseconds)
     s = natsOptions_SetTimeout(opts, 10000);
 if (s == NATS_OK)
     s = natsConnection_Connect(&conn, opts);

 (...)

 // Destroy objects that were created
 natsConnection_Destroy(conn);
 natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Ping/Pong Protocol

NATS client applications use a PING/PONG protocol to check that there is a working connection to the NATS service. Periodically the client will send PING messages to the server, which responds with a PONG. This period is configured by specifying a ping interval on the client connection settings.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-06ebb703571bae3f457bcb328f9f7d55ea14b971%2Fpingpong.svg?alt=media\&token=981a213b-c37e-4370-93bd-4e709e3b0d58)

The connection will be closed as stale when the client reaches a number of pings which recieved no pong in response, which is configured by specifying the maximum pings outstanding on the client connection settings.

The ping interval and the maximum pings outstanding work together to specify how quickly the client connection will be notified of a problem. This will also help when there is a remote network partition where the operating system does not detect a socket error. Upon connection close, the client will attempt to reconnect. When it knows about other servers, these will be tried next.

In the presence of traffic, such as messages or client side pings, the server will not initiate the PING/PONG interaction.

On connections with significant traffic, the client will often figure out there is a problem between PINGS, and as a result the default ping interval is typically on the order of minutes. To close an unresponsive connection after 100s, set the ping interval to 20s and the maximum pings outstanding to 5:

{% tabs %}
{% tab title="Go" %}

```go
// Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
nc, err := nats.Connect("demo.nats.io", nats.Name("API Ping Example"), nats.PingInterval(20*time.Second), nats.MaxPingsOutstanding(5))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io")
    .pingInterval(Duration.ofSeconds(20)) // Set Ping Interval
    .maxPingsOut(5) // Set max pings in flight
    .build();

// Connection is AutoCloseable
try (Connection nc = Nats.connect(options)) {
    // Do something with the connection
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
const nc = await connect({
    pingInterval: 20 * 1000,
    maxPingOut: 5,
    servers: ["demo.nats.io:4222"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(
   servers=["nats://demo.nats.io:4222"],
   # Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
   ping_interval=20,
   max_outstanding_pings=5,
   )

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://demo.nats.io:4222",
    
    // Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
    PingInterval = TimeSpan.FromSeconds(20),
    MaxPingOut = 5,
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
# Set Ping Interval to 20 seconds and Max Pings Outstanding to 5
NATS.start(ping_interval: 20, max_outstanding_pings: 5) do |nc|
   nc.on_reconnect do
    puts "Got reconnected to #{nc.connected_server}"
  end

  nc.on_disconnect do |reason|
    puts "Got disconnected! #{reason}"
  end

  # Do something with the connection
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsOptions         *opts    = NULL;
natsStatus          s        = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    // Set Ping interval to 20 seconds (20,000 milliseconds)
    s = natsOptions_SetPingInterval(opts, 20000);
if (s == NATS_OK)
    // Set the limit to 5
    s = natsOptions_SetMaxPingsOut(opts, 5);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Turning Off Echo'd Messages

By default a NATS connection will echo messages if the connection also has interest in the published subject. This means that if a publisher on a connection sends a message to a subject any subscribers on that same connection will receive the message. Clients can opt to turn off this behavior, such that regardless of interest, the message will not be delivered to subscribers on the same connection.

The NoEcho option can be useful in BUS patterns where all applications subscribe and publish to the same subject. Usually a publish represents a state change that the application already knows about, so in the case where the application publishes an update it does not need to process the update itself.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-5a09f42db59d94cf40b825de3e3c436bc0250eef%2Fnoecho.svg?alt=media\&token=796746d0-f2dc-4112-9eb2-90e6f6086bff)

Keep in mind that each connection will have to turn off echo, and that it is per connection, not per application. Also, turning echo on and off can result in a major change to your applications communications protocol since messages will flow or stop flowing based on this setting and the subscribing code won't have any indication as to why.

{% tabs %}
{% tab title="Go" %}

```go
// Turn off echo
nc, err := nats.Connect("demo.nats.io", nats.Name("API NoEcho Example"), nats.NoEcho())
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .noEcho() // Turn off echo
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    servers: ["demo.nats.io"],
    noEcho: true,
});

const sub = nc.subscribe(subj, { callback: (_err, _msg) => {} });
nc.publish(subj);
await sub.drain();
// we won't get our own messages
t.is(sub.getProcessed(), 0);
```

{% endtab %}

{% tab title="Python" %}

```python
ncA = NATS()
ncB = NATS()

await ncA.connect(no_echo=True)
await ncB.connect()

async def handler(msg):
   # Messages sent by `ncA' will not be received.
   print("[Received] ", msg)

await ncA.subscribe("greetings", cb=handler)
await ncA.flush()
await ncA.publish("greetings", b'Hello World!')
await ncB.publish("greetings", b'Hello World!')

# Do something with the connection

await asyncio.sleep(1)
await ncA.drain()
await ncB.drain()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://demo.nats.io:4222",
    
    // Turn off echo
    Echo = false
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
NATS.start("nats://demo.nats.io:4222", no_echo: true) do |nc|
  # ...
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsOptions         *opts    = NULL;
natsStatus          s        = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetNoEcho(opts, true);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Miscellaneous functionalities

This section contains miscellaneous functionalities and options for connect.

## Get the Maximum Payload Size

While the client can't control the maximum payload size, clients may provide a way for applications to obtain the configured [`max_payload`](https://docs.nats.io/running-a-nats-service/configuration#limits) after the connection is made. This will allow the application to chunk or limit data as needed to pass through the server.

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

mp := nc.MaxPayload()
log.Printf("Maximum payload is %v bytes", mp)

// Do something with the max payload
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

long mp = nc.getMaxPayload();
System.out.println("max payload for the server is " + mp + " bytes");
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
t.log(`max payload for the server is ${nc.info.max_payload} bytes`);
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

print("Maximum payload is %d bytes" % nc.max_payload)

# Do something with the max payload.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient("nats://demo.nats.io:4222");

// Make sure we connect to a server to receive the server info,
// since connecting to servers is lazy in .NET client.
await client.ConnectAsync();

Console.WriteLine($"MaxPayload = {client.Connection.ServerInfo.MaxPayload}");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(max_outstanding_pings: 5) do |nc|
  nc.on_reconnect do
    puts "Got reconnected to #{nc.connected_server}"
  end

  nc.on_disconnect do |reason|
    puts "Got disconnected! #{reason}"
  end

  # Do something with the max_payload
  puts "Maximum Payload is #{nc.server_info[:max_payload]} bytes"
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsStatus          s        = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
if (s == NATS_OK)
{
    int64_t mp = natsConnection_GetMaxPayload(conn);
    printf("Max payload: %d\n", (int) mp);
}

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

## Turn On Pedantic Mode

The NATS server provides a *pedantic* mode that performs extra checks on the protocol.

One example of such a check is if a subject used for publishing contains a [wildcard](https://docs.nats.io/nats-concepts/subjects#wildcards) character. The server will not use it as wildcard and therefore omits this check.

By default, this setting is off but you can turn it on to test your application:

{% tabs %}
{% tab title="Go" %}

```go
opts := nats.GetDefaultOptions()
opts.Url = "demo.nats.io"
// Turn on Pedantic
opts.Pedantic = true
nc, err := opts.Connect()
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder().
                            server("nats://demo.nats.io:4222").
                            pedantic(). // Turn on pedantic
                            build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// the pedantic option is useful for developing nats clients.
// the javascript clients also provide `debug` which will
// print to the console all the protocol interactions
// with the server
const nc = await connect({
    pedantic: true,
    servers: ["demo.nats.io:4222"],
    debug: true,
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"], pedantic=True)

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// Not available in the NATS .NET client
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(pedantic: true) do |nc|
   nc.on_reconnect do
    puts "Got reconnected to #{nc.connected_server}"
  end

  nc.on_disconnect do |reason|
    puts "Got disconnected! #{reason}"
  end

  nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsOptions         *opts    = NULL;
natsStatus          s        = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetPedantic(opts, true);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

## Set the Maximum Control Line Size

The protocol between the client and the server is fairly simple and relies on a control line and sometimes a body. The control line contains the operations being sent, like PING or PONG, followed by a carriage return and line feed, CRLF or "\r\n". The server has a [`max_control_line`](https://docs.nats.io/running-a-nats-service/configuration#limits) option that can limit the maximum size of a control line. For PING and PONG this doesn't come into play, but for messages that contain subject names and possibly queue group names, the control line length can be important as it effectively limits the possibly combined length. Some clients will try to limit the control line size internally to prevent an error from the server. These clients may or may not allow you to set the size being used, but if they do, the size should be set to match the server configuration.

> It is not recommended to set this to a value that is higher than the one of other clients or the nats-server.

For example, to set the maximum control line size to 2k:

{% tabs %}
{% tab title="Go" %}

```go
// This does not apply to the NATS Go Client
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder().
                            server("nats://demo.nats.io:4222").
                            maxControlLine(2 * 1024). // Set the max control line to 2k
                            build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// the max control line is determined automatically by the client
```

{% endtab %}

{% tab title="Python" %}

```python
# Asyncio NATS client does not allow custom control lines.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// control line is not configurable on NATS .NET client.
// required memory is allocated dynamically from the array pool.
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# There is no need to customize this in the Ruby NATS client.
```

{% endtab %}

{% tab title="C" %}

```c
// control line is not configurable on C NATS client.
```

{% endtab %}
{% endtabs %}

## Turn On/Off Verbose Mode

Clients can request *verbose* mode from NATS server. When requested by a client, the server will reply to every message from that client with either a +OK or an error -ERR. However, the client will not block and wait for a response. Errors will be sent without verbose mode as well and client libraries handle them as documented.

> This functionality is only used for debugging the client library or the nats-server themselves. By default the server sets it to on, but every client turns it off.

To turn on verbose mode:

{% tabs %}
{% tab title="Go" %}

```go
opts := nats.GetDefaultOptions()
opts.Url = "demo.nats.io"
// Turn on Verbose
opts.Verbose = true
nc, err := opts.Connect()
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder().
                            server("nats://demo.nats.io:4222").
                            verbose(). // Turn on verbose
                            build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    verbose: true,
    servers: ["demo.nats.io:4222"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"], verbose=True)

# Do something with the connection.
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(verbose: true) do |nc|
   nc.on_reconnect do
    puts "Got reconnected to #{nc.connected_server}"
  end

  nc.on_disconnect do |reason|
    puts "Got disconnected! #{reason}"
  end

  nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsOptions         *opts    = NULL;
natsStatus          s        = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetVerbose(opts, true);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Automatic Reconnections

All the client libraries maintained on the [nats.io GitHub page](https://github.com/nats-io) will automatically attempt to re-connect if their current server connection gets disconnected for any reason. Upon re-connection the client library will automatically re-establish all the subscriptions, there is nothing for the application programmer to do.

Unless specifically [disabled](https://docs.nats.io/using-nats/developer/connecting/reconnect/disable) client will try to re-connect to one of the servers it knows about, either through the URLs provided in the `connect` call or the URLs provided by the NATS system during earlier connects. This feature allows NATS applications and the NATS system itself to self-heal and reconfigure itself with no additional configuration or intervention.

You can adjust the [wait time](https://docs.nats.io/using-nats/developer/connecting/reconnect/wait) between connections attempts, the [maximum](https://docs.nats.io/using-nats/developer/connecting/reconnect/max) number of reconnection attempts, and adjust the size of the reconnection [buffer](https://docs.nats.io/using-nats/developer/connecting/reconnect/buffer).

## Advisories

Your application can register callback to receive [events](https://docs.nats.io/using-nats/developer/connecting/reconnect/events) to be notified about the following connection events:

* `ClosedCB ConnHandler`

The ClosedCB handler is called when a client will no longer be connected.

* `DisconnectedCB ConnHandler`

The DisconnectedCB handler is called whenever the connection is disconnected. It will not be called if DisconnectedErrCB is set **DEPRECATED**: Use DisconnectedErrCB instead which passes error that caused the disconnect event.

* `DisconnectedErrCB ConnErrHandler`

The DisconnectedErrCB handler is called whenever the connection is disconnected. Disconnected error could be nil, for instance when user explicitly closes the connection. **NOTE**: DisconnectedCB will not be called if DisconnectedErrCB is set

* `ReconnectedCB ConnHandler`

The ReconnectedCB handler is called whenever the connection is successfully reconnected.

* `DiscoveredServersCB ConnHandler`

The DiscoveredServersCB handler is called whenever a new server has joined the cluster.

* `AsyncErrorCB ErrHandler`

The AsyncErrorCB handler is called whenever asynchronous connection errors happen (e.g. slow consumer errors)

## Connection timeout attributes

* `Timeout time.Duration`

Timeout sets the timeout for a Dial operation on a connection. Default is `2 * time.Second`

* `PingInterval time.Duration`

PingInterval is the period at which the client will be sending ping commands to the server, disabled if 0 or negative. Default is `2 * time.Minute`

* `MaxPingsOut int`

MaxPingsOut is the maximum number of pending ping commands that can be awaiting a response before raising an ErrStaleConnection error. Default is `2`

## Reconnection attributes

Besides the error and advisory callbacks mentioned above you can also set a few reconnection attributes in the connection options:

* `AllowReconnect bool`

AllowReconnect enables reconnection logic to be used when we encounter a disconnect from the current server. Default is `true`

* `MaxReconnect int`

MaxReconnect sets the number of reconnect attempts that will be tried before giving up. If negative, then it will never give up trying to reconnect. Default is `60`

* `ReconnectWait time.Duration`

ReconnectWait sets the time to backoff after attempting to (and failing to) reconnect. Default is `2 * time.Second`

* `CustomReconnectDelayCB ReconnectDelayHandler`

CustomReconnectDelayCB is invoked after the library tried every URL in the server list and failed to reconnect. It passes to the user the current number of attempts. This function returns the amount of time the library will sleep before attempting to reconnect again. It is strongly recommended that this value contains some jitter to prevent all connections to attempt reconnecting at the same time.

* `ReconnectJitter time.Duration`

ReconnectJitter sets the upper bound for a random delay added to *ReconnectWait* during a reconnect when no TLS is used. Note that any jitter is capped with ReconnectJitterMax. Default is `100 * time.Millisecond`

* `ReconnectJitterTLS time.Duration`

ReconnectJitterTLS sets the upper bound for a random delay added to *ReconnectWait* during a reconnect when TLS is used. Note that any jitter is capped with ReconnectJitterMax. Default is `1 * time.Second`

* `ReconnectBufSize int`

ReconnectBufSize is the size of the backing bufio during reconnect. Once this has been exhausted publish operations will return an error. Default is `8 * 1024 * 1024`

* `RetryOnFailedConnect bool`

RetryOnFailedConnect sets the connection in reconnecting state right away if it can't connect to a server in the initial set. The *MaxReconnect* and *ReconnectWait* options are used for this process, similarly to when an established connection is disconnected. If a ReconnectHandler is set, it will be invoked on the first successful reconnect attempt (if the initial connect fails), and if a ClosedHandler is set, it will be invoked if it fails to connect (after exhausting the MaxReconnect attempts). Default is `false`


# Disabling Reconnect

You can disable automatic reconnect with connection options:

{% tabs %}
{% tab title="Go" %}

```go
// Disable reconnect attempts
nc, err := nats.Connect("demo.nats.io", nats.NoReconnect())
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .noReconnect() // Disable reconnect attempts
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
 const nc = await connect({
    reconnect: false,
    servers: ["demo.nats.io"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(
   servers=[
      "nats://demo.nats.io:1222",
      "nats://demo.nats.io:1223",
      "nats://demo.nats.io:1224"
      ],
   allow_reconnect=False,
   )

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://demo.nats.io:4222",
    
    // .NET client does not support disabling reconnects,
    // but you can set the maximum number of reconnect attempts
    MaxReconnectRetry = 1,
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"], reconnect: false) do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsOptions         *opts    = NULL;
natsStatus          s        = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetAllowReconnect(opts, false);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Set the Number of Reconnect Attempts

Applications can set the maximum reconnect attempts per server. This includes the server provided to the client's connect call, as well as the server the client discovered through another server. Once reconnect to a server fails the specified amount of times in a row, it will be removed from the connect list. After a successful reconnect to a server, the client will reset that server's failed reconnect attempt count. If a server was removed from the connect list, it can be rediscovered on connect. This effectively resets the connect attempt count as well. If the client runs out of servers to reconnect, it will close the connection and [raise an error](https://docs.nats.io/using-nats/developer/connecting/reconnect/events).

{% tabs %}
{% tab title="Go" %}

```go
// Set max reconnects attempts
nc, err := nats.Connect("demo.nats.io", nats.MaxReconnects(10))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .maxReconnects(10) // Set max reconnect attempts
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    maxReconnectAttempts: 10,
    servers: ["demo.nats.io"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(
   servers=["nats://demo.nats.io:4222"],
   max_reconnect_attempts=10,
   )

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://demo.nats.io:4222",
    
    // Set the maximum number of reconnect attempts
    MaxReconnectRetry = 10,
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"], max_reconnect_attempts: 10) do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn    = NULL;
natsOptions         *opts    = NULL;
natsStatus          s        = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetMaxReconnect(opts, 10);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Avoiding the Thundering Herd

When a server goes down, there is a possible anti-pattern called the *Thundering Herd* where all of the clients try to reconnect immediately, thus creating a denial of service attack. In order to prevent this, most NATS client libraries randomize the servers they attempt to connect to. This setting has no effect if only a single server is used, but in the case of a cluster, randomization, or shuffling, will ensure that no one server bears the brunt of the client reconnect attempts.

However, if you want to disable the randomization process for connect and reconnect, so that servers are always checked in the same order, you can do that in most libraries with a connection option:

{% tabs %}
{% tab title="Go" %}

```go
servers := []string{"nats://127.0.0.1:1222",
    "nats://127.0.0.1:1223",
    "nats://127.0.0.1:1224",
}

nc, err := nats.Connect(strings.Join(servers, ","), nats.DontRandomize())
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://127.0.0.1:1222,nats://127.0.0.1:1223,nats://127.0.0.1:1224")
    .noRandomize() // Disable randomizing servers in the bootstrap and later discovered 
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    noRandomize: false,
    servers: ["127.0.0.1:4443", "demo.nats.io"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(
   servers=[
      "nats://demo.nats.io:1222",
      "nats://demo.nats.io:1223",
      "nats://demo.nats.io:1224"
      ],
   dont_randomize=True,
   )

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://127.0.0.1:1222,nats://127.0.0.1:1223,nats://127.0.0.1:1224",
    NoRandomize = true,
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"], dont_randomize_servers: true) do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;
const char          *servers[] = {"nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"};

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetServers(opts, servers, 3);
if (s == NATS_OK)
    s = natsOptions_SetNoRandomize(opts, true);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Pausing Between Reconnect Attempts

It doesn’t make much sense to try to connect to the same server over and over. To prevent this sort of thrashing, and wasted reconnect attempts, especially when using TLS, libraries provide a wait setting. Generally clients make sure that between two reconnect attempts to the **same** server at least a certain amount of time has passed. The concrete implementation depends on the library used.

This setting not only prevents wasting client resources, it also alleviates a [*thundering herd*](https://docs.nats.io/using-nats/developer/connecting/reconnect/random) situation when additional servers are not available.

{% tabs %}
{% tab title="Go" %}

```go
// Set reconnect interval to 10 seconds
nc, err := nats.Connect("demo.nats.io", nats.ReconnectWait(10*time.Second))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .reconnectWait(Duration.ofSeconds(10))  // Set Reconnect Wait
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    reconnectTimeWait: 10 * 1000, // 10s
    servers: ["demo.nats.io"],
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()
await nc.connect(
   servers=["nats://demo.nats.io:4222"],
   reconnect_time_wait=10,
   )

# Do something with the connection

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient(new NatsOpts
{
    Url = "nats://127.0.0.1:1222,nats://127.0.0.1:1223,nats://127.0.0.1:1224",
    
    // Set reconnect interval to between 5-10 seconds
    ReconnectWaitMin = TimeSpan.FromSeconds(5),
    ReconnectWaitMax = TimeSpan.FromSeconds(10),
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"], reconnect_time_wait: 10) do |nc|
   # Do something with the connection

   # Close the connection
   nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    // Set reconnect interval to 10 seconds (10,000 milliseconds)
    s = natsOptions_SetReconnectWait(opts, 10000);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Listening for Reconnect Events

Because reconnect is primarily under the covers, many libraries provide an event listener you can use to be notified of reconnect events. This event can be especially important for applications sending a lot of messages.

{% tabs %}
{% tab title="Go" %}

```go
// Connection event handlers are invoked asynchronously
// and the state of the connection may have changed when
// the callback is invoked.
nc, err := nats.Connect("demo.nats.io",
    nats.DisconnectErrHandler(func(nc *nats.Conn, err error) {
        // handle disconnect error event
    }),
    nats.ReconnectHandler(func(nc *nats.Conn) {
        // handle reconnect event
    }))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
class MyConnectionListener implements ConnectionListener {
    public void connectionEvent(Connection conn, Events event) {
        switch (event) {
            case CONNECTED:
                // The connection has successfully completed the handshake with the nats-server.
                break;
            case CLOSED:
                // The connection is permanently closed, either by manual action or failed reconnects
                break;
            case DISCONNECTED:
                // The connection lost its connection, but may try to reconnect if configured to
                break;
            case RECONNECTED:
                // The connection was connected, lost its connection and successfully reconnected.
                break;
            case RESUBSCRIBED:
                // The connection was reconnected and the server has been notified of all subscriptions.
                break;
            case DISCOVERED_SERVERS:
                // The connection was made aware of new servers from the current server connection.
                break;
            case LAME_DUCK:
                // connected server is coming down soon, might want to prepare for it
                break;
        }
    }
}

MyConnectionListener listener = new MyConnectionListener();

Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .connectionListener(listener)
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({
    maxReconnectAttempts: 10,
    servers: ["demo.nats.io"],
  });

  (async () => {
    for await (const s of nc.status()) {
      switch (s.type) {
        case Events.Reconnect:
          t.log(`client reconnected - ${s.data}`);
          break;
        default:
      }
    }
  })().then();
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

async def disconnected_cb():
   print("Got disconnected!")

async def reconnected_cb():
   # See who we are connected to on reconnect.
   print("Got reconnected to {url}".format(url=nc.connected_url.netloc))

await nc.connect(
   servers=["nats://demo.nats.io:4222"],
   reconnect_time_wait=10,
   reconnected_cb=reconnected_cb,
   disconnected_cb=disconnected_cb,
   )

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

client.Connection.ConnectionDisconnected += async (sender, args) =>
{
    Console.WriteLine($"Disconnected: {args.Message}");
};

client.Connection.ConnectionOpened += async (sender, args) =>
{
    Console.WriteLine($"Connected: {args.Message}");
};

client.Connection.ReconnectFailed += async (sender, args) =>
{
    Console.WriteLine($"Reconnect Failed: {args.Message}");
};

await client.ConnectAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers: ["nats://127.0.0.1:1222", "nats://127.0.0.1:1223", "nats://127.0.0.1:1224"]) do |nc|
   # Do something with the connection
   nc.on_reconnect do
    puts "Got reconnected to #{nc.connected_server}"
  end

  nc.on_disconnect do |reason|
    puts "Got disconnected! #{reason}"
  end
end
```

{% endtab %}

{% tab title="C" %}

```c
static void
disconnectedCB(natsConnection *conn, void *closure)
{
    // Handle disconnect error event
}

static void
reconnectedCB(natsConnection *conn, void *closure)
{
    // Handle reconnect event
}

(...)

natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);

// Connection event handlers are invoked asynchronously
// and the state of the connection may have changed when
// the callback is invoked.
if (s == NATS_OK)
    s = natsOptions_SetDisconnectedCB(opts, disconnectedCB, NULL);
if (s == NATS_OK)
    s = natsOptions_SetReconnectedCB(opts, reconnectedCB, NULL);

if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Buffering Messages During Reconnect Attempts

The Core NATS client libraries try as much as possible to be fire and forget, and you should use JetStream functionalities to get higher qualities of service that can deal with Core NATS messages being dropped due to the server connection being interrupted. That said, one of the features that may be included in the library you are using is the ability to buffer outgoing messages when the connection is down.

During a short reconnect, the client can allow applications to publish messages that, because the server is offline, will be cached in the client. The library will then send those messages once reconnected. When the maximum reconnect buffer is reached, messages will no longer be publishable by the client and an error will be returned.

Be aware, while the message appears to be sent to the application it is possible that it is never sent because the connection is never remade. Your applications should use patterns like acknowledgements or use the JetStream publish call to ensure delivery.

For clients that support this feature, you are able to configure the size of this buffer with bytes, messages or both.

{% tabs %}
{% tab title="Go" %}

```go
// Set reconnect buffer size in bytes (5 MB)
nc, err := nats.Connect("demo.nats.io", nats.ReconnectBufSize(5*1024*1024))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
Options options = new Options.Builder()
    .server("nats://demo.nats.io:4222")
    .reconnectBufferSize(5 * 1024 * 1024)  // Set buffer in bytes
    .build();
Connection nc = Nats.connect(options);

// Do something with the connection

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// Reconnect buffer size is not configurable on NATS JavaScript client
```

{% endtab %}

{% tab title="Python" %}

```python
# Asyncio NATS client currently does not implement a reconnect buffer
```

{% endtab %}

{% tab title="C#" %}

```csharp
// Reconnect buffer size is not configurable on NATS .NET client
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# There is currently no reconnect pending buffer as part of the Ruby NATS client
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    // Set reconnect buffer size in bytes (5 MB)
    s = natsOptions_SetReconnectBufSize(opts, 5*1024*1024);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

> *As mentioned throughout this document, each client library may behave slightly differently. Please check the documentation for the library you are using.*


# Monitoring the Connection

Managing the interaction with the server is primarily the job of the client library but most of the libraries also provide some insight into what is happening under the covers.

For example, the client library may provide a mechanism to get the connection's current status:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io", nats.Name("API Example"))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

getStatusTxt := func(nc *nats.Conn) string {
    switch nc.Status() {
    case nats.CONNECTED:
        return "Connected"
    case nats.CLOSED:
        return "Closed"
    default:
        return "Other"
    }
}
log.Printf("The connection is %v\n", getStatusTxt(nc))

nc.Close()

log.Printf("The connection is %v\n", getStatusTxt(nc))
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

System.out.println("The Connection is: " + nc.getStatus()); // CONNECTED

nc.close();

System.out.println("The Connection is: " + nc.getStatus()); // CLOSED
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
  // you can find out where you connected:
t.log(`connected to a nats server version ${nc.info.version}`);

// or information about the data in/out of the client:
const stats = nc.stats();
t.log(`client sent ${stats.outMsgs} messages and received ${stats.inMsgs}`);
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(
   servers=["nats://demo.nats.io:4222"],
   )

# Do something with the connection.

print("The connection is connected?", nc.is_connected)

while True:
  if nc.is_reconnecting:
    print("Reconnecting to NATS...")
    break
  await asyncio.sleep(1)

await nc.close()

print("The connection is closed?", nc.is_closed)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

Console.WriteLine($"{client.Connection.ConnectionState}"); // Closed

await client.ConnectAsync();

Console.WriteLine($"{client.Connection.ConnectionState}"); // Open
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
NATS.start(max_reconnect_attempts: 2) do |nc|
  puts "Connect is connected?: #{nc.connected?}"

  timer = EM.add_periodic_timer(1) do
    if nc.closing?
      puts "Connection closed..."
      EM.cancel_timer(timer)
      NATS.stop
    end

    if nc.reconnecting?
      puts "Reconnecting to NATS..."
      next
    end
  end
end
```

{% endtab %}
{% endtabs %}


# Listen for Connection Events

While the connection status is interesting, it is perhaps more interesting to know when the status changes. Most, if not all, of the NATS client libraries provide a way to listen for events related to the connection and its status.

The actual API for these listeners is language dependent, but the following examples show a few of the more common use cases. See the API documentation for the client library you are using for more specific instructions.

Connection events may include the connection being closed, disconnected or reconnected. Reconnecting involves a disconnect and connect, but depending on the library implementation may also include multiple disconnects as the client tries to find a server, or the server is rebooted.

{% tabs %}
{% tab title="Go" %}

```go
// There is not a single listener for connection events in the NATS Go Client.
// Instead, you can set individual event handlers using:
nc, err := nats.Connect("demo.nats.io",
    nats.DisconnectErrHandler(func(_ *nats.Conn, err error) {
        log.Printf("client disconnected: %v", err)
    }),
    nats.ReconnectHandler(func(_ *nats.Conn) {
        log.Printf("client reconnected")
    }),
    nats.ClosedHandler(func(_ *nats.Conn) {
        log.Printf("client closed")
    }))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

DisconnectHandler(cb ConnHandler)
ReconnectHandler(cb ConnHandler)
ClosedHandler(cb ConnHandler)
DiscoveredServersHandler(cb ConnHandler)
ErrorHandler(cb ErrHandler)
```

{% endtab %}

{% tab title="Java" %}

```java
class MyConnectionListener implements ConnectionListener {
    public void connectionEvent(Connection natsConnection, Events event) {
        System.out.println("Connection event - " + event);
    }
}

public class SetConnectionListener {
    public static void main(String[] args) {
        try {
            Options options = new Options.Builder()
                .server("nats://demo.nats.io:4222")
                .connectionListener(new MyConnectionListener()) // Set the listener
                .build();
            Connection nc = Nats.connect(options);

            // Do something with the connection

            nc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({ servers: ["demo.nats.io"] });
nc.closed().then(() => {
  t.log("the connection closed!");
});

(async () => {
    for await (const s of nc.status()) {
      switch (s.type) {
        case Events.Disconnect:
          t.log(`client disconnected - ${s.data}`);
          break;
        case Events.LDM:
          t.log("client has been requested to reconnect");
          break;
        case Events.Update:
          t.log(`client received a cluster update - ${s.data}`);
          break;
        case Events.Reconnect:
          t.log(`client reconnected - ${s.data}`);
          break;
        case Events.Error:
          t.log("client got a permissions error");
          break;
        case DebugEvents.Reconnecting:
          t.log("client is attempting to reconnect");
          break;
        case DebugEvents.StaleConnection:
          t.log("client has a stale connection");
          break;
        default:
          t.log(`got an unknown status ${s.type}`);
      }
    }
})().then();
```

{% endtab %}

{% tab title="Python" %}

```python
# Asyncio NATS client can be defined a number of event callbacks
async def disconnected_cb():
    print("Got disconnected!")

async def reconnected_cb():
    # See who we are connected to on reconnect.
    print("Got reconnected to {url}".format(url=nc.connected_url.netloc))

async def error_cb(e):
    print("There was an error: {}".format(e))

async def closed_cb():
    print("Connection is closed")

# Setup callbacks to be notified on disconnects and reconnects
options["disconnected_cb"] = disconnected_cb
options["reconnected_cb"] = reconnected_cb

# Setup callbacks to be notified when there is an error
# or connection is closed.
options["error_cb"] = error_cb
options["closed_cb"] = closed_cb

await nc.connect(**options)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

client.Connection.ConnectionDisconnected += async (sender, args) =>
{
    Console.WriteLine($"Disconnected: {args.Message}");
};

client.Connection.ConnectionOpened += async (sender, args) =>
{
    Console.WriteLine($"Connected: {args.Message}");
};

client.Connection.ReconnectFailed += async (sender, args) =>
{
    Console.WriteLine($"Reconnect Failed: {args.Message}");
};

await client.ConnectAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# There is not a single listener for connection events in the Ruby NATS Client.
# Instead, you can set individual event handlers using:

NATS.on_disconnect do
end

NATS.on_reconnect do
end

NATS.on_close do
end

NATS.on_error do
end
```

{% endtab %}

{% tab title="C" %}

```c
static void
disconnectedCB(natsConnection *conn, void *closure)
{
    // Do something
    printf("Connection disconnected\n");
}

static void
reconnectedCB(natsConnection *conn, void *closure)
{
    // Do something
    printf("Connection reconnected\n");
}

static void
closedCB(natsConnection *conn, void *closure)
{
    // Do something
    printf("Connection closed\n");
}

(...)

natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetDisconnectedCB(opts, disconnectedCB, NULL);
if (s == NATS_OK)
    s = natsOptions_SetReconnectedCB(opts, reconnectedCB, NULL);
if (s == NATS_OK)
    s = natsOptions_SetClosedCB(opts, closedCB, NULL);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

## Listen for New Servers

When working with a cluster, servers may be added or changed. Some of the clients allow you to listen for this notification:

{% tabs %}
{% tab title="Go" %}

```go
// Be notified if a new server joins the cluster.
// Print all the known servers and the only the ones that were discovered.
nc, err := nats.Connect("demo.nats.io",
    nats.DiscoveredServersHandler(func(nc *nats.Conn) {
        log.Printf("Known servers: %v\n", nc.Servers())
        log.Printf("Discovered servers: %v\n", nc.DiscoveredServers())
    }))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
class ServersAddedListener implements ConnectionListener {
    public void connectionEvent(Connection nc, Events event) {
        if (event == Events.DISCOVERED_SERVERS) {
            for (String server : nc.getServers()) {
                System.out.println("Known server: "+server);
            }
        }
    }
}

public class ListenForNewServers {
    public static void main(String[] args) {

        try {
            Options options = new Options.Builder().
                                        server("nats://demo.nats.io:4222").
                                        connectionListener(new ServersAddedListener()). // Set the listener
                                        build();
            Connection nc = Nats.connect(options);

            // Do something with the connection

            nc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({ servers: ["demo.nats.io:4222"] });
(async () => {
  for await (const s of nc.status()) {
    switch (s.type) {
      case Status.Update:
        t.log(`servers added - ${s.data.added}`);
        t.log(`servers deleted - ${s.data.deleted}`);
        break;
      default:
    }
  }
})().then();
```

{% endtab %}

{% tab title="Python" %}

```python
# Asyncio NATS client does not support discovered servers handler right now
```

{% endtab %}

{% tab title="C#" %}

```csharp
// NATS .NET client does not support discovered servers handler right now
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# The Ruby NATS client does not support discovered servers handler right now
```

{% endtab %}

{% tab title="C" %}

```c
static void
discoveredServersCB(natsConnection *conn, void *closure)
{
    natsStatus  s         = NATS_OK;
    char        **servers = NULL;
    int         count     = 0;

    s = natsConnection_GetDiscoveredServers(conn, &servers, &count);
    if (s == NATS_OK)
    {
        int i;

        // Do something...
        for (i=0; i<count; i++)
            printf("Discovered server: %s\n", servers[i]);

        // Free allocated memory
        for (i=0; i<count; i++)
            free(servers[i]);
        free(servers);
    }
}

(...)

natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetDiscoveredServersCB(opts, discoveredServersCB, NULL);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)


// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

## Listen for Errors

The client library may separate server-to-client errors from events. Many server events are not handled by application code and result in the connection being closed. Listening for the errors can be very useful for debugging problems.

{% tabs %}
{% tab title="Go" %}

```go
// Set the callback that will be invoked when an asynchronous error occurs.
nc, err := nats.Connect("demo.nats.io",
    nats.ErrorHandler(func(_ *nats.Conn, _ *nats.Subscription, err error) {
        log.Printf("Error: %v", err)
    }))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
class MyErrorListener implements ErrorListener {
    public void errorOccurred(Connection conn, String error)
    {
        System.out.println("The server notificed the client with: "+error);
    }

    public void exceptionOccurred(Connection conn, Exception exp) {
        System.out.println("The connection handled an exception: "+exp.getLocalizedMessage());
    }

    public void slowConsumerDetected(Connection conn, Consumer consumer) {
        System.out.println("A slow consumer was detected.");
    }
}

public class SetErrorListener {
    public static void main(String[] args) {

        try {
            Options options = new Options.Builder().
                                        server("nats://demo.nats.io:4222").
                                        errorListener(new MyErrorListener()). // Set the listener
                                        build();
            Connection nc = Nats.connect(options);

            // Do something with the connection

            nc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({ servers: ["demo.nats.io"] });

// if the client gets closed with an error you can trap that
// condition in the closed handler like this:
nc.closed().then((err) => {
  if (err) {
    t.log(`the connection closed with an error ${err.message}`);
  } else {
    t.log(`the connection closed.`);
  }
});

// if you have a status listener, it will too get notified
(async () => {
  for await (const s of nc.status()) {
    switch (s.type) {
      case Status.Error:
        // typically if you get this the nats connection will close
        t.log("client got an async error from the server");
        break;
      default:
        t.log(`got an unknown status ${s.type}`);
    }
  }
})().then();
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

async def error_cb(e):
   print("Error: ", e)

await nc.connect(
   servers=["nats://demo.nats.io:4222"],
   reconnect_time_wait=10,
   error_cb=error_cb,
   )

# Do something with the connection.
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using Microsoft.Extensions.Logging;
using NATS.Client.Core;
using NATS.Net;

// NATS .NET client does not support error handler right now
// instead, you can use the logger since server errors are logged
// with the error level and eventId 1005 (Protocol Log Event).
await using var client = new NatsClient(new NatsOpts
{
    LoggerFactory = LoggerFactory.Create(builder => builder.AddConsole()),
});
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers:["nats://demo.nats.io:4222"]) do |nc|
   nc.on_error do |e|
    puts "Error: #{e}"
  end

  nc.close
end
```

{% endtab %}

{% tab title="C" %}

```c
static void
errorCB(natsConnection *conn, natsSubscription *sub, natsStatus s, void *closure)
{
    // Do something
    printf("Error: %d - %s\n", s, natsStatus_GetText(s));
}

(...)

natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetErrorHandler(opts, errorCB, NULL);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Slow Consumers

NATS is designed to move messages through the server quickly. As a result, NATS depends on the applications to consider and respond to changing message rates. The server will do a bit of impedance matching, but if a client is too slow the server will eventually cut them off by closing the connection. These cut off connections are called [*slow consumers*](https://docs.nats.io/running-a-nats-service/nats_admin/slow_consumers).

One way some of the libraries deal with bursty message traffic is to buffer incoming messages for a subscription. So if an application can handle 10 messages per second and sometimes receives 20 messages per second, the library may hold the extra 10 to give the application time to catch up. To the server, the application will appear to be handling the messages and consider the connection healthy. Most client libraries will notify the application that there is a SlowConsumer error and discard messages.

Receiving and dropping messages from the server keeps the connection to the server healthy, but creates an application requirement. There are several common patterns:

* Use request-reply to throttle the sender and prevent overloading the subscriber
* Use a queue with multiple subscribers splitting the work
* Persist messages with something like NATS streaming

Libraries that cache incoming messages may provide two controls on the incoming queue, or pending messages. These are useful if the problem is bursty publishers and not a continuous performance mismatch. Disabling these limits can be dangerous in production and although setting these limits to 0 may help find problems, it is also a dangerous proposition in production.

> Check your libraries documentation for the default settings, and support for disabling these limits.

The incoming cache is usually per subscriber, but again, check the specific documentation for your client library.

## Limiting Incoming/Pending Messages by Count and Bytes

The first way that the incoming queue can be limited is by message count. The second way to limit the incoming queue is by total size. For example, to limit the incoming cache to 1,000 messages or 5mb whichever comes first:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Subscribe
sub1, err := nc.Subscribe("updates", func(m *nats.Msg) {})
if err != nil {
    log.Fatal(err)
}

// Set limits of 1000 messages or 5MB, whichever comes first
sub1.SetPendingLimits(1000, 5*1024*1024)

// Subscribe
sub2, err := nc.Subscribe("updates", func(m *nats.Msg) {})
if err != nil {
    log.Fatal(err)
}

// Set no limits for this subscription
sub2.SetPendingLimits(-1, -1)

// Close the connection
nc.Close()
```

{% endtab %}

{% tab title="Java" %}

```java
// Consumer (Dispatcher, Subscription) API
// void setPendingLimits(long maxMessages, long maxBytes)

Connection nc = Nats.connect("nats://demo.nats.io:4222");

Dispatcher d = nc.createDispatcher((msg) -> {
    // handle message
});

d.subscribe("updates");

d.setPendingLimits(1_000, 5 * 1024 * 1024); // Set limits on a dispatcher

// Subscribe
Subscription sub = nc.subscribe("updates");

sub.setPendingLimits(1_000, 5 * 1024 * 1024); // Set limits on a subscription

// Do something

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// slow pending limits are not configurable on node-nats
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

future = asyncio.Future()

async def cb(msg):
  nonlocal future
  future.set_result(msg)

# Set limits of 1000 messages or 5MB
await nc.subscribe("updates", cb=cb, pending_bytes_limit=5*1024*1024, pending_msgs_limit=1000)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using System.Threading.Channels;
using NATS.Client.Core;

await using var client = new NatsClient();

// Set limits of 1000 messages.
// Note: setting the channel capacity over 1024 is not recommended
// as the channel's backing array will be allocated on the LOH (large object heap).
// NATS .NET client does not support setting a limit on the number of bytes
var subOpts = new NatsSubOpts
{
    ChannelOpts = new NatsSubChannelOpts
    {
        Capacity = 1000,
        FullMode = BoundedChannelFullMode.DropOldest
    }
};
await foreach (var msg in client.SubscribeAsync<string>(subject: "updates", opts: subOpts))
{
    Console.WriteLine($"Received: {msg.Subject}: {msg.Data}");    
}
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# The Ruby NATS client currently does not have option to specify a subscribers pending limits.
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsSubscription    *sub1      = NULL;
natsSubscription    *sub2      = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_Subscribe(&sub1, conn, "updates", onMsg, NULL);

// Set limits of 1000 messages or 5MB, whichever comes first
if (s == NATS_OK)
    s = natsSubscription_SetPendingLimits(sub1, 1000, 5*1024*1024);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_Subscribe(&sub2, conn, "updates", onMsg, NULL);

// Set no limits for this subscription
if (s == NATS_OK)
    s = natsSubscription_SetPendingLimits(sub2, -1, -1);

(...)

// Destroy objects that were created
natsSubscription_Destroy(sub1);
natsSubscription_Destroy(sub2);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

## Detect a Slow Consumer and Check for Dropped Messages

When a slow consumer is detected and messages are about to be dropped, the library may notify the application. This process may be similar to other errors or may involve a custom callback.

Some libraries, like Java, will not send this notification on every dropped message because that could be noisy. Rather the notification may be sent once per time the subscriber gets behind. Libraries may also provide a way to get a count of dropped messages so that applications can at least detect a problem is occurring.

{% tabs %}
{% tab title="Go" %}

```go
// Set the callback that will be invoked when an asynchronous error occurs.
nc, err := nats.Connect("demo.nats.io", nats.ErrorHandler(logSlowConsumer))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Do something with the connection
```

{% endtab %}

{% tab title="Java" %}

```java
class SlowConsumerReporter implements ErrorListener {
    public void errorOccurred(Connection conn, String error)
    {
    }

    public void exceptionOccurred(Connection conn, Exception exp) {
    }

    // Detect slow consumers
    public void slowConsumerDetected(Connection conn, Consumer consumer) {
        // Get the dropped count
        System.out.println("A slow consumer dropped messages: "+ consumer.getDroppedCount());
    }
}

public class SlowConsumerListener {
    public static void main(String[] args) {

        try {
            Options options = new Options.Builder().
                                        server("nats://demo.nats.io:4222").
                                        errorListener(new SlowConsumerReporter()). // Set the listener
                                        build();
            Connection nc = Nats.connect(options);

            // Do something with the connection

            nc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// slow consumer detection is not configurable on NATS JavaScript client.
```

{% endtab %}

{% tab title="Python" %}

```python
   nc = NATS()

   async def error_cb(e):
     if type(e) is nats.aio.errors.ErrSlowConsumer:
       print("Slow consumer error, unsubscribing from handling further messages...")
       await nc.unsubscribe(e.sid)

   await nc.connect(
      servers=["nats://demo.nats.io:4222"],
      error_cb=error_cb,
      )

   msgs = []
   future = asyncio.Future()
   async def cb(msg):
       nonlocal msgs
       nonlocal future
       print(msg)
       msgs.append(msg)

       if len(msgs) == 3:
         # Head of line blocking on other messages caused
         # by single message processing taking too long...
         await asyncio.sleep(1)

   await nc.subscribe("updates", cb=cb, pending_msgs_limit=5)

   for i in range(0, 10):
     await nc.publish("updates", "msg #{}".format(i).encode())
     await asyncio.sleep(0)

   try:
     await asyncio.wait_for(future, 1)
   except asyncio.TimeoutError:
     pass

   for msg in msgs:
     print("[Received]", msg)

   await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using System.Threading.Channels;
using NATS.Client.Core;

await using var client = new NatsClient();

// Set the event handler for slow consumers
client.Connection.MessageDropped += async (sender, eventArgs) =>
{
    Console.WriteLine($"Dropped message: {eventArgs.Subject}: {eventArgs.Data}");
    Console.WriteLine($"Current channel size: {eventArgs.Pending}");
};

var subOpts = new NatsSubOpts
{
    ChannelOpts = new NatsSubChannelOpts
    {
        Capacity = 10,
        FullMode = BoundedChannelFullMode.DropOldest

        // If set to wait (default), you won't be able to detect slow consumers
        // FullMode = BoundedChannelFullMode.Wait,
    }
};

using var cts = new CancellationTokenSource();

var subscription = Task.Run(async () =>
{
    await foreach (var msg in client.SubscribeAsync<string>(subject: "updates", opts: subOpts, cancellationToken: cts.Token))
    {
        Console.WriteLine($"Received: {msg.Subject}: {msg.Data}");    
    }
});

for (int i = 0; i < 1_000; i++)
{
    await client.PublishAsync(subject: "updates", data: $"message payload {i}");
}

await cts.CancelAsync();

await subscription;
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# The Ruby NATS client currently does not have option to customize slow consumer limits per sub.
```

{% endtab %}

{% tab title="C" %}

```c
static void
errorCB(natsConnection *conn, natsSubscription *sub, natsStatus s, void *closure)
{

    // Do something
    printf("Error: %d - %s", s, natsStatus_GetText(s));
}

(...)

natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsStatus          s          = NATS_OK;

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    s = natsOptions_SetErrorHandler(opts, errorCB, NULL);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}


# Receiving Messages

In general, applications can receive messages asynchronously or synchronously. Receiving messages with NATS can be library dependent.

Some languages, like Go or Java, provide synchronous and asynchronous APIs, while others may only support one type of subscription.

In all cases, the process of subscribing involves having the client library tell the NATS system that an application is interested in a particular subject. When an application is done with a subscription it unsubscribes telling the server to stop sending messages.

A client will receive a message for each matching subscription, so if a connection has multiple subscriptions using identical or overlapping subjects (say `foo` and `>`) the same message will be sent to the client multiple times.

Note: The client API (asynchronous) subscribe call can return before the subscription is actually fully established at the nats-server. Call `Flush()` on the connection right after you call subscribe if you need to synchronize with the subscription being ready at the server level.


# Synchronous Subscriptions

Synchronous subscriptions require the application to wait for messages. This type of subscription is easy to set-up and use, but requires the application to deal with looping if multiple messages are expected. For situations where a single message is expected, synchronous subscriptions are sometimes easier to manage, depending on the language.

For example, to subscribe to the subject `updates` and receive a single message you could do:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Subscribe
sub, err := nc.SubscribeSync("updates")
if err != nil {
    log.Fatal(err)
}

// Wait for a message
msg, err := sub.NextMsg(10 * time.Second)
if err != nil {
    log.Fatal(err)
}

// Use the response
log.Printf("Reply: %s", msg.Data)
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Subscribe
Subscription sub = nc.subscribe("updates");

// Read a message
Message msg = sub.nextMessage(Duration.ZERO);

String str = new String(msg.getData(), StandardCharsets.UTF_8);
System.out.println(str);

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// node-nats subscriptions are always async.
```

{% endtab %}

{% tab title="Python" %}

```python
# Asyncio NATS client currently does not have a sync subscribe API
```

{% endtab %}

{% tab title="C#" %}

```csharp
// NATS .NET subscriptions are always async.
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# The Ruby NATS client subscriptions are all async.
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsSubscription    *sub       = NULL;
natsMsg             *msg       = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_SubscribeSync(&sub, conn, "updates");

// Wait for messages
if (s == NATS_OK)
    s = natsSubscription_NextMsg(&msg, sub, 10000);

if (s == NATS_OK)
{
    printf("Received msg: %s - %.*s\n",
            natsMsg_GetSubject(msg),
            natsMsg_GetDataLength(msg),
            natsMsg_GetData(msg));

    // Destroy message that was received
    natsMsg_Destroy(msg);
}

(...)

// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Asynchronous Subscriptions

Asynchronous subscriptions use callbacks of some form to notify an application when a message arrives. These subscriptions are usually easier to work with, but do represent some form of internal work and resource usage, i.e. threads, by the library. Check your library's documentation for any resource usage associated with asynchronous subscriptions.

***Note: For a given subscription, messages are dispatched serially, one message at a time. If your application does not care about processing ordering and would prefer the messages to be dispatched concurrently, it is the application's responsibility to move them to some internal queue to be picked up by threads/go routines.***

The following example subscribes to the subject `updates` and handles the incoming messages:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Use a WaitGroup to wait for a message to arrive
wg := sync.WaitGroup{}
wg.Add(1)

// Subscribe
if _, err := nc.Subscribe("updates", func(m *nats.Msg) {
    wg.Done()
}); err != nil {
    log.Fatal(err)
}

// Wait for a message to come in
wg.Wait()
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Use a latch to wait for a message to arrive
CountDownLatch latch = new CountDownLatch(1);

// Create a dispatcher and inline message handler
Dispatcher d = nc.createDispatcher((msg) -> {
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(str);
    latch.countDown();
});

// Subscribe
d.subscribe("updates");

// Wait for a message to come in
latch.await(); 

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const sc = StringCodec();
// this is an example of a callback subscription
// https://github.com/nats-io/nats.js/blob/master/README.md#async-vs-callbacks
nc.subscribe("updates", {
  callback: (err, msg) => {
    if (err) {
      t.error(err.message);
    } else {
      t.log(sc.decode(msg.data));
    }
  },
  max: 1,
});

// here's an iterator subscription - note the code in the
// for loop will block until the iterator completes
// either from a break/return from the iterator, an
// unsubscribe after the message arrives, or in this case
// an auto-unsubscribe after the first message is received
const sub = nc.subscribe("updates", { max: 1 });
for await (const m of sub) {
  t.log(sc.decode(m.data));
}

// subscriptions have notifications, simply wait
// the closed promise
sub.closed
  .then(() => {
    t.log("subscription closed");
  })
  .catch((err) => {
    t.err(`subscription closed with an error ${err.message}`);
  });
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

future = asyncio.Future()

async def cb(msg):
  nonlocal future
  future.set_result(msg)

await nc.subscribe("updates", cb=cb)
await nc.publish("updates", b'All is Well')
await nc.flush()

# Wait for message to come in
msg = await asyncio.wait_for(future, 1)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

// Subscribe to the "updates" subject and receive messages as <string> type.
// The default serializer understands all primitive types, strings,
// byte arrays, and uses JSON for complex types.
await foreach (var msg in client.SubscribeAsync<string>("updates"))
{
    Console.WriteLine($"Received: {msg.Data}");
    
    if (msg.Data == "exit")
    {
        // When we exit the loop, we unsubscribe from the subject
        // as a result of enumeration completion.
        break;
    }
}
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  nc.subscribe("updates") do |msg|
    puts msg
    nc.close
  end

  nc.publish("updates", "All is Well")
end
```

{% endtab %}

{% tab title="C" %}

```c
static void
onMsg(natsConnection *conn, natsSubscription *sub, natsMsg *msg, void *closure)
{
    printf("Received msg: %s - %.*s\n",
           natsMsg_GetSubject(msg),
           natsMsg_GetDataLength(msg),
           natsMsg_GetData(msg));

    // Need to destroy the message!
    natsMsg_Destroy(msg);
}

(...)

natsConnection      *conn = NULL;
natsSubscription    *sub  = NULL;
natsStatus          s;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
if (s == NATS_OK)
{
    // Creates an asynchronous subscription on subject "foo".
    // When a message is sent on subject "foo", the callback
    // onMsg() will be invoked by the client library.
    // You can pass a closure as the last argument.
    s = natsConnection_Subscribe(&sub, conn, "foo", onMsg, NULL);
}

(...)


// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Unsubscribing

The client libraries provide a means to unsubscribe a previous subscription request.

This process requires an interaction with the server, so for an asynchronous subscription there may be a small window of time where a message comes through as the unsubscribe is processed by the library. Ignoring that slight edge case, the client library will clean up any outstanding messages and tell the server that the subscription is no longer used.

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Sync Subscription
sub, err := nc.SubscribeSync("updates")
if err != nil {
    log.Fatal(err)
}
if err := sub.Unsubscribe(); err != nil {
    log.Fatal(err)
}

// Async Subscription
sub, err = nc.Subscribe("updates", func(_ *nats.Msg) {})
if err != nil {
    log.Fatal(err)
}
if err := sub.Unsubscribe(); err != nil {
    log.Fatal(err)
}
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");
Dispatcher d = nc.createDispatcher((msg) -> {
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(str);
});

// Sync Subscription have an unsubscribe API
Subscription sub = nc.subscribe("updates");
sub.unsubscribe();

// Async Subscriptions on the dispatcher must unsubscribe via the dispatcher,
// not the subscription
d.subscribe("updates");
d.unsubscribe("updates");

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const sc = StringCodec();
// set up a subscription to process a request
const sub = nc.subscribe(createInbox(), (_err, m) => {
  m.respond(sc.encode(new Date().toLocaleTimeString()));
});
// without arguments the subscription will cancel when the server receives it
// you can also specify how many messages are expected by the subscription
sub.unsubscribe();
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

future = asyncio.Future()

async def cb(msg):
  nonlocal future
  future.set_result(msg)

sub = await nc.subscribe("updates", cb=cb)
await nc.publish("updates", b'All is Well')

# Remove interest in subject
await sub.unsubscribe()

# Won't be received...
await nc.publish("updates", b'...')
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

// Cancel the subscription after 10 seconds
using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(10));

// Subscribe to the "updates" subject
// We unsubscribe when we receive the message "exit"
// or when the cancellation token is triggered.
await foreach (var msg in client.SubscribeAsync<string>("updates").WithCancellation(cts.Token))
{
    Console.WriteLine($"Received: {msg.Data}");
    
    if (msg.Data == "exit")
    {
        // When we exit the loop, we unsubscribe from the subject
        break;
    }
}

Console.WriteLine("Unsubscribed from updates");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  Fiber.new do
    f = Fiber.current

    sid = nc.subscribe("time") do |msg, reply|
      f.resume Time.now
    end

    nc.publish("time", 'What is the time?', NATS.create_inbox)

    # Use the response
    msg = Fiber.yield
    puts "Reply: #{msg}"

    nc.unsubscribe(sid)

    # Won't be received
    nc.publish("time", 'What is the time?', NATS.create_inbox)

  end.resume
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsSubscription    *sub       = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_SubscribeSync(&sub, conn, "updates");

// Unsubscribe
if (s == NATS_OK)
    s = natsSubscription_Unsubscribe(sub);

(...)

// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Unsubscribing After N Messages

NATS provides a special form of unsubscribe that is configured with a message count and takes effect when that many messages are sent to a subscriber. This mechanism is very useful if only a single message is expected.

The message count you provide is the total message count for a subscriber. So if you unsubscribe with a count of 1, the server will stop sending messages to that subscription after it has received one message. If the subscriber has already received one or more messages, the unsubscribe will be immediate. This action based on history can be confusing if you try to auto-unsubscribe on a long running subscription, but is logical for a new one.

Auto-unsubscribe is based on the total messages sent to a subscriber, not just the new ones. Most of the client libraries also track the max message count after an auto-unsubscribe request. On reconnect, this enables clients to resend the unsubscribe with an updated total.

The following example shows unsubscribe after a single message:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Sync Subscription
sub, err := nc.SubscribeSync("updates")
if err != nil {
    log.Fatal(err)
}
if err := sub.AutoUnsubscribe(1); err != nil {
    log.Fatal(err)
}

// Async Subscription
sub, err = nc.Subscribe("updates", func(_ *nats.Msg) {})
if err != nil {
    log.Fatal(err)
}
if err := sub.AutoUnsubscribe(1); err != nil {
    log.Fatal(err)
}
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");
Dispatcher d = nc.createDispatcher((msg) -> {
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(str);
});

/ subscribe then unsubscribe after 10 "more" messages
// It's technically possible to get more than 10 total if messages are already in
// flight by the time the server receives the unsubscribe message

// Sync Subscription, 
Subscription sub = nc.subscribe("updates");
sub.unsubscribe(10);

// Async Subscription directly in the dispatcher
d.subscribe("updates");
d.unsubscribe("updates", 10);

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const sc = StringCodec();
// `max` specifies the number of messages that the server will forward.
// The server will auto-cancel.
const subj = createInbox();
const sub1 = nc.subscribe(subj, {
  callback: (_err, msg) => {
    t.log(`sub1 ${sc.decode(msg.data)}`);
  },
  max: 10,
});

// another way after 10 messages
const sub2 = nc.subscribe(subj, {
  callback: (_err, msg) => {
    t.log(`sub2 ${sc.decode(msg.data)}`);
  },
});
// if the subscription already received 10 messages, the handler
// won't get any more messages
sub2.unsubscribe(10);
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

async def cb(msg):
  print(msg)

sid = await nc.subscribe("updates", cb=cb)
await nc.auto_unsubscribe(sid, 1)
await nc.publish("updates", b'All is Well')

# Won't be received...
await nc.publish("updates", b'...')
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient();

// Unsubscribe after 10 messages
var opts = new NatsSubOpts { MaxMsgs = 10 };

var count = 0;

// Subscribe to updates with options
await foreach (var msg in client.SubscribeAsync<string>("updates", opts: opts))
{
    Console.WriteLine($"Received[{++count}]: {msg.Data}");
}

Console.WriteLine("Unsubscribed from updates");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  Fiber.new do
    f = Fiber.current

    nc.subscribe("time", max: 1) do |msg, reply|
      f.resume Time.now
    end

    nc.publish("time", 'What is the time?', NATS.create_inbox)

    # Use the response
    msg = Fiber.yield
    puts "Reply: #{msg}"

    # Won't be received
    nc.publish("time", 'What is the time?', NATS.create_inbox)

  end.resume
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsSubscription    *sub       = NULL;
natsMsg             *msg       = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_SubscribeSync(&sub, conn, "updates");

// Unsubscribe after 1 message is received
if (s == NATS_OK)
    s = natsSubscription_AutoUnsubscribe(sub, 1);

// Wait for messages
if (s == NATS_OK)
    s = natsSubscription_NextMsg(&msg, sub, 10000);

if (s == NATS_OK)
{
    printf("Received msg: %s - %.*s\n",
            natsMsg_GetSubject(msg),
            natsMsg_GetDataLength(msg),
            natsMsg_GetData(msg));

    // Destroy message that was received
    natsMsg_Destroy(msg);
}

(...)

// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Replying to a Message

Incoming messages have an optional reply-to field. If that field is set, it will contain a subject to which a reply is expected.

For example, the following code will listen for that request and respond with the time.

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Subscribe
sub, err := nc.SubscribeSync("time")
if err != nil {
    log.Fatal(err)
}

// Read a message
msg, err := sub.NextMsg(10 * time.Second)
if err != nil {
    log.Fatal(err)
}

// Get the time
timeAsBytes := []byte(time.Now().String())

// Send the time as the response.
msg.Respond(timeAsBytes)
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Subscribe to the "time" subject and reply with the current time
Subscription sub = nc.subscribe("time");

// Read a message
Message msg = sub.nextMessage(Duration.ZERO);

// Get the time
Calendar cal = Calendar.getInstance();
SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
byte[] timeAsBytes = sdf.format(cal.getTime()).getBytes(StandardCharsets.UTF_8);

// Send the time to the reply to subject
nc.publish(msg.getReplyTo(), timeAsBytes);

// Flush and close the connection
nc.flush(Duration.ZERO);
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const sc = StringCodec();
// set up a subscription to process a request
const sub = nc.subscribe("time");
for await (const m of sub) {
  m.respond(sc.encode(new Date().toLocaleDateString()));
}
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

future = asyncio.Future()

async def cb(msg):
  nonlocal future
  future.set_result(msg)

await nc.subscribe("time", cb=cb)

await nc.publish_request("time", new_inbox(), b'What is the time?')
await nc.flush()

# Read the message
msg = await asyncio.wait_for(future, 1)

# Send the time
time_as_bytes = "{}".format(datetime.now()).encode()
await nc.publish(msg.reply, time_as_bytes)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

// Subscribe to the "time" subject and reply with the current time
await foreach (var msg in client.SubscribeAsync<string>("time"))
{
    await msg.ReplyAsync(DateTime.Now);
}
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  Fiber.new do
    f = Fiber.current

    nc.subscribe("time") do |msg, reply|
      f.resume Time.now
    end

    nc.publish("time", 'What is the time?', NATS.create_inbox)

    # Use the response
    msg = Fiber.yield
    puts "Reply: #{msg}"

  end.resume
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsSubscription    *sub       = NULL;
natsMsg             *msg       = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_SubscribeSync(&sub, conn, "time");

// Wait for messages
if (s == NATS_OK)
    s = natsSubscription_NextMsg(&msg, sub, 10000);

if (s == NATS_OK)
{
    char buf[64];

    snprintf(buf, sizeof(buf), "%lld", nats_Now());

    // Send the time as a response
    s = natsConnection_Publish(conn, natsMsg_GetReply(msg), buf, (int) strlen(buf));

    // Destroy message that was received
    natsMsg_Destroy(msg);
}

(...)

// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Wildcard Subscriptions

There is no special code to subscribe with a [wildcard subject](https://docs.nats.io/nats-concepts/subjects#wildcards). Wildcards are a normal part of the subject name. However, it is a common technique to use the subject provided with the incoming message to determine what to do with the message.

For example, you can subscribe using `*` and then act based on the actual subject.

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Use a WaitGroup to wait for 2 messages to arrive
wg := sync.WaitGroup{}
wg.Add(2)

// Subscribe
if _, err := nc.Subscribe("time.*.east", func(m *nats.Msg) {
    log.Printf("%s: %s", m.Subject, m.Data)
    wg.Done()
}); err != nil {
    log.Fatal(err)
}

// Wait for the 2 messages to come in
wg.Wait()
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Use a latch to wait for 2 messages to arrive
CountDownLatch latch = new CountDownLatch(2);

// Create a dispatcher and inline message handler
Dispatcher d = nc.createDispatcher((msg) -> {
    String subject = msg.getSubject();
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(subject + ": " + str);
    latch.countDown();
});

// Subscribe
d.subscribe("time.*.east");

// Wait for messages to come in
latch.await();

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
nc.subscribe("time.us.*", (_err, msg) => {
    // converting timezones correctly in node requires a library
    // this doesn't take into account *many* things.
    let time;
    switch (msg.subject) {
      case "time.us.east":
        time = new Date().toLocaleTimeString("en-us", {
          timeZone: "America/New_York",
        });
        break;
      case "time.us.central":
        time = new Date().toLocaleTimeString("en-us", {
          timeZone: "America/Chicago",
        });
        break;
      case "time.us.mountain":
        time = new Date().toLocaleTimeString("en-us", {
          timeZone: "America/Denver",
        });
        break;
      case "time.us.west":
        time = new Date().toLocaleTimeString("en-us", {
          timeZone: "America/Los_Angeles",
        });
        break;
      default:
        time = "I don't know what you are talking about Willis";
    }
    t.log(subject, time);
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

# Use queue to wait for 2 messages to arrive
queue = asyncio.Queue()
async def cb(msg):
  await queue.put_nowait(msg)

await nc.subscribe("time.*.east", cb=cb)

# Send 2 messages and wait for them to come in
await nc.publish("time.A.east", b'A')
await nc.publish("time.B.east", b'B')

msg_A = await queue.get()
msg_B = await queue.get()

print("Msg A:", msg_A)
print("Msg B:", msg_B)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

var count = 0;
await foreach (var msg in client.SubscribeAsync<string>("time.*.east"))
{
    Console.WriteLine($"Received {++count}: {msg.Subject}: {msg.Data}");
    
    if (count == 2)
    {
        break;
    }
}

Console.WriteLine("Done");

// Output:
// Received 1: time.us.east: 2024-10-21T22:11:24 America/New_York (-04)
// Received 2: time.eu.east: 2024-10-22T04:11:24 Europe/Warsaw (+02)
// Done
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  Fiber.new do
    f = Fiber.current

    nc.subscribe("time.*.east") do |msg, reply|
      f.resume Time.now
    end

    nc.publish("time.A.east", "A")
    nc.publish("time.B.east", "B")

    # Use the response
    msg_A = Fiber.yield
    puts "Msg A: #{msg_A}"

    msg_B = Fiber.yield
    puts "Msg B: #{msg_B}"

  end.resume
end
```

{% endtab %}

{% tab title="C" %}

```c
static void
onMsg(natsConnection *conn, natsSubscription *sub, natsMsg *msg, void *closure)
{
    printf("Received msg: %s - %.*s\n",
           natsMsg_GetSubject(msg),
           natsMsg_GetDataLength(msg),
           natsMsg_GetData(msg));

    // Need to destroy the message!
    natsMsg_Destroy(msg);
}


(...)

natsConnection      *conn = NULL;
natsSubscription    *sub  = NULL;
natsStatus          s;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
if (s == NATS_OK)
    s = natsConnection_Subscribe(&sub, conn, "time.*.east", onMsg, NULL);

(...)


// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

or do something similar with `>`:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Use a WaitGroup to wait for 4 messages to arrive
wg := sync.WaitGroup{}
wg.Add(4)

// Subscribe
if _, err := nc.Subscribe("time.>", func(m *nats.Msg) {
    log.Printf("%s: %s", m.Subject, m.Data)
    wg.Done()
}); err != nil {
    log.Fatal(err)
}

// Wait for the 4 messages to come in
wg.Wait()

// Close the connection
nc.Close()
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Use a latch to wait for 4 messages to arrive
CountDownLatch latch = new CountDownLatch(4);

// Create a dispatcher and inline message handler
Dispatcher d = nc.createDispatcher((msg) -> {
    String subject = msg.getSubject();
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(subject + ": " + str);
    latch.countDown();
});

// Subscribe
d.subscribe("time.>");

// Wait for messages to come in
latch.await();

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
let nc = NATS.connect({
    url: "nats://demo.nats.io:4222"
});

nc.subscribe('time.>', (msg, reply, subject) => {
    // converting timezones correctly in node requires a library
    // this doesn't take into account *many* things.
    let time = "";
    switch (subject) {
        case 'time.us.east':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/New_York"});
            break;
        case 'time.us.central':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/Chicago"});
            break;
        case 'time.us.mountain':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/Denver"});
            break;
        case 'time.us.west':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/Los_Angeles"});
            break;
        default:
            time = "I don't know what you are talking about Willis";
    }
    t.log(subject, time);
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

# Use queue to wait for 4 messages to arrive
queue = asyncio.Queue()
async def cb(msg):
  await queue.put(msg)

await nc.subscribe("time.>", cb=cb)

# Send 2 messages and wait for them to come in
await nc.publish("time.A.east", b'A')
await nc.publish("time.B.east", b'B')
await nc.publish("time.C.west", b'C')
await nc.publish("time.D.west", b'D')

for i in range(0, 4):
  msg = await queue.get()
  print("Msg:", msg)

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

var count = 0;
await foreach (var msg in client.SubscribeAsync<string>("time.>"))
{
    Console.WriteLine($"Received {++count}: {msg.Subject}: {msg.Data}");
    
    if (count == 4)
    {
        break;
    }
}

Console.WriteLine("Done");

// Output:
// Received 1: time.us.east: 2024-10-21T22:11:24 America/New_York (-04)
// Received 2: time.us.east.atlanta: 2024-10-21T22:11:24 America/New_York (-04)
// Received 3: time.eu.east: 2024-10-22T04:11:24 Europe/Warsaw (+02)
// Received 4: time.eu.east.warsaw: 2024-10-22T04:11:24 Europe/Warsaw (+02)
// Done
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  Fiber.new do
    f = Fiber.current

    nc.subscribe("time.>") do |msg, reply|
      f.resume Time.now.to_f
    end

    nc.publish("time.A.east", "A")
    nc.publish("time.B.east", "B")
    nc.publish("time.C.west", "C")
    nc.publish("time.D.west", "D")

    # Use the response
    4.times do 
      msg = Fiber.yield
      puts "Msg: #{msg}"
    end
  end.resume
end
```

{% endtab %}

{% tab title="TypeScript" %}

```typescript
await nc.subscribe('time.>', (err, msg) => {
    // converting timezones correctly in node requires a library
    // this doesn't take into account *many* things.
    let time = "";
    switch (msg.subject) {
        case 'time.us.east':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/New_York"});
            break;
        case 'time.us.central':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/Chicago"});
            break;
        case 'time.us.mountain':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/Denver"});
            break;
        case 'time.us.west':
            time = new Date().toLocaleTimeString("en-us", {timeZone: "America/Los_Angeles"});
            break;
        default:
            time = "I don't know what you are talking about Willis";
    }
    t.log(msg.subject, time);
});
```

{% endtab %}

{% tab title="C" %}

```c
static void
onMsg(natsConnection *conn, natsSubscription *sub, natsMsg *msg, void *closure)
{
    printf("Received msg: %s - %.*s\n",
           natsMsg_GetSubject(msg),
           natsMsg_GetDataLength(msg),
           natsMsg_GetData(msg));

    // Need to destroy the message!
    natsMsg_Destroy(msg);
}


(...)

natsConnection      *conn = NULL;
natsSubscription    *sub  = NULL;
natsStatus          s;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
if (s == NATS_OK)
    s = natsConnection_Subscribe(&sub, conn, "time.>", onMsg, NULL);

(...)


// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

The following example can be used to test these two subscribers. The `*` subscriber should receive at most 2 messages, while the `>` subscriber receives 4. More importantly the `time.*.east` subscriber won't receive on `time.us.east.atlanta` because that won't match.

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

zoneID, err := time.LoadLocation("America/New_York")
if err != nil {
    log.Fatal(err)
}
now := time.Now()
zoneDateTime := now.In(zoneID)
formatted := zoneDateTime.String()

nc.Publish("time.us.east", []byte(formatted))
nc.Publish("time.us.east.atlanta", []byte(formatted))

zoneID, err = time.LoadLocation("Europe/Warsaw")
if err != nil {
    log.Fatal(err)
}
zoneDateTime = now.In(zoneID)
formatted = zoneDateTime.String()

nc.Publish("time.eu.east", []byte(formatted))
nc.Publish("time.eu.east.warsaw", []byte(formatted))
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");
ZoneId zoneId = ZoneId.of("America/New_York");
ZonedDateTime zonedDateTime = ZonedDateTime.ofInstant(Instant.now(), zoneId);
String formatted = zonedDateTime.format(DateTimeFormatter.ISO_ZONED_DATE_TIME);

nc.publish("time.us.east", formatted.getBytes(StandardCharsets.UTF_8));
nc.publish("time.us.east.atlanta", formatted.getBytes(StandardCharsets.UTF_8));

zoneId = ZoneId.of("Europe/Warsaw");
zonedDateTime = ZonedDateTime.ofInstant(Instant.now(), zoneId);
formatted = zonedDateTime.format(DateTimeFormatter.ISO_ZONED_DATE_TIME);
nc.publish("time.eu.east", formatted.getBytes(StandardCharsets.UTF_8));
nc.publish("time.eu.east.warsaw", formatted.getBytes(StandardCharsets.UTF_8));

nc.flush(Duration.ZERO);
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
nc.publish('time.us.east');
nc.publish('time.us.central');
nc.publish('time.us.mountain');
nc.publish('time.us.west');
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

await nc.publish("time.us.east", b'...')
await nc.publish("time.us.east.atlanta", b'...')

await nc.publish("time.eu.east", b'...')
await nc.publish("time.eu.east.warsaw", b'...')

await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
// dotnet add package NodaTime
using NATS.Net;
using NodaTime;

await using var client = new NatsClient();

Instant now = SystemClock.Instance.GetCurrentInstant();

{
    DateTimeZone zone = DateTimeZoneProviders.Tzdb["America/New_York"];
    string formatted = now.InZone(zone).ToString();
    await client.PublishAsync("time.us.east", formatted);
    await client.PublishAsync("time.us.east.atlanta", formatted);
}

{
    DateTimeZone zone = DateTimeZoneProviders.Tzdb["Europe/Warsaw"];
    string formatted = now.InZone(zone).ToString();
    await client.PublishAsync("time.eu.east", formatted);
    await client.PublishAsync("time.eu.east.warsaw", formatted);
}
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
NATS.start do |nc|
   nc.publish("time.us.east", '...')
   nc.publish("time.us.east.atlanta", '...')

   nc.publish("time.eu.east", '...')
   nc.publish("time.eu.east.warsaw", '...')

   nc.drain
end
```

{% endtab %}

{% tab title="TypeScript" %}

```typescript
nc.publish('time.us.east');
nc.publish('time.us.central');
nc.publish('time.us.mountain');
nc.publish('time.us.west');
```

{% endtab %}
{% endtabs %}


# Queue Subscriptions

Subscribing to a [queue group](https://docs.nats.io/nats-concepts/core-nats/queue) is only slightly different than subscribing to a subject alone. The application simply includes a queue name with the subscription. The server will load balance between all members of the queue group. In a cluster setup, every member has the same chance of receiving a particular message.

Keep in mind that queue groups in NATS are dynamic and do not require any server configuration.

![](https://1487470910-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LqMYcZML1bsXrN3Ezg0%2Fuploads%2Fgit-blob-e4f2a6428a4be494475b4c811af461ff0908ec2a%2Fqueues.svg?alt=media\&token=b34513af-ce5b-47c2-99cc-1287ae802d6d)

As an example, to subscribe to the queue `workers` with the subject `updates`:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Use a WaitGroup to wait for 10 messages to arrive
wg := sync.WaitGroup{}
wg.Add(10)

// Create a queue subscription on "updates" with queue name "workers"
if _, err := nc.QueueSubscribe("updates", "workers", func(m *nats.Msg) {
    wg.Done()
}); err != nil {
    log.Fatal(err)
}

// Wait for messages to come in
wg.Wait()
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Use a latch to wait for 10 messages to arrive
CountDownLatch latch = new CountDownLatch(10);

// Create a dispatcher and inline message handler
Dispatcher d = nc.createDispatcher((msg) -> {
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(str);
    latch.countDown();
});

// Subscribe to the "updates" subject with a queue group named "workers"
d.subscribe("updates", "workers");

// Wait for a message to come in
latch.await(); 

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
nc.subscribe(subj, {
    queue: "workers",
    callback: (_err, _msg) => {
      t.log("worker1 got message");
    },
});

nc.subscribe(subj, {
    queue: "workers",
    callback: (_err, _msg) => {
      t.log("worker2 got message");
    },
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

future = asyncio.Future()

async def cb(msg):
  nonlocal future
  future.set_result(msg)

await nc.subscribe("updates", queue="workers", cb=cb)
await nc.publish("updates", b'All is Well')

msg = await asyncio.wait_for(future, 1)
print("Msg", msg)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

var count = 0;

// Subscribe to the "updates" subject with a queue group named "workers"
await foreach (var msg in client.SubscribeAsync<string>(subject: "updates", queueGroup: "workers"))
{
    Console.WriteLine($"Received {++count}: {msg.Subject}: {msg.Data}");
    
    // Break after 10 messages
    if (count == 10)
    {
        break;
    }
}

Console.WriteLine("Done");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  Fiber.new do
    f = Fiber.current

    nc.subscribe("updates", queue: "worker") do |msg, reply|
      f.resume Time.now
    end

    nc.publish("updates", "A")

    # Use the response
    msg = Fiber.yield
    puts "Msg: #{msg}"
  end.resume
end
```

{% endtab %}

{% tab title="C" %}

```c
static void
onMsg(natsConnection *conn, natsSubscription *sub, natsMsg *msg, void *closure)
{
    printf("Received msg: %s - %.*s\n",
           natsMsg_GetSubject(msg),
           natsMsg_GetDataLength(msg),
           natsMsg_GetData(msg));

    // Need to destroy the message!
    natsMsg_Destroy(msg);
}


(...)

natsConnection      *conn = NULL;
natsSubscription    *sub  = NULL;
natsStatus          s;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Create a queue subscription on "updates" with queue name "workers"
if (s == NATS_OK)
    s = natsConnection_QueueSubscribe(&sub, conn, "updates", "workers", onMsg, NULL);

(...)


// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

If you run this example with the publish examples that send to `updates`, you will see that one of the instances gets a message while the others you run won't. But the instance that receives the message will change.


# Draining Messages Before Disconnect

This feature is the ability to drain connections or subscriptions and then close the connection. Closing a connection (using `close()`), or unsubscribing from a subscription, are generally considered immediate requests. When you close or unsubscribe the library will halt messages in any pending queue or cache for subscribers. When you drain a subscription or connection, it will process any inflight and cached/pending messages before closing.

Drain provides clients that use queue subscriptions with a way to bring down applications without losing any messages. A client can bring up a new queue member, drain and shut down the old queue member, all without losing messages sent to the old client. Without drain, there is the possibility of lost messages due to delivery timing.

The libraries can provide drain on a connection or on a subscriber, or both.

For a connection the process is essentially:

1. Drain all subscriptions
2. Stop new messages from being published
3. Flush any remaining published messages
4. Close

The API for drain can generally be used instead of close:

As an example of draining a connection:

{% tabs %}
{% tab title="Go" %}

```go
wg := sync.WaitGroup{}
wg.Add(1)

errCh := make(chan error, 1)

// To simulate a timeout, you would set the DrainTimeout()
// to a value less than the time spent in the message callback,
// so say: nats.DrainTimeout(10*time.Millisecond).

nc, err := nats.Connect("demo.nats.io",
    nats.DrainTimeout(10*time.Second),
    nats.ErrorHandler(func(_ *nats.Conn, _ *nats.Subscription, err error) {
        errCh <- err
    }),
    nats.ClosedHandler(func(_ *nats.Conn) {
        wg.Done()
    }))
if err != nil {
    log.Fatal(err)
}

// Just to not collide using the demo server with other users.
subject := nats.NewInbox()

// Subscribe, but add some delay while processing.
if _, err := nc.Subscribe(subject, func(_ *nats.Msg) {
    time.Sleep(200 * time.Millisecond)
}); err != nil {
    log.Fatal(err)
}

// Publish a message
if err := nc.Publish(subject, []byte("hello")); err != nil {
    log.Fatal(err)
}

// Drain the connection, which will close it when done.
if err := nc.Drain(); err != nil {
    log.Fatal(err)
}

// Wait for the connection to be closed.
wg.Wait()

// Check if there was an error
select {
case e := <-errCh:
    log.Fatal(e)
default:
}
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Use a latch to wait for a message to arrive
CountDownLatch latch = new CountDownLatch(1);

// Create a dispatcher and inline message handler
Dispatcher d = nc.createDispatcher((msg) -> {
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(str);
    latch.countDown();
});

// Subscribe
d.subscribe("updates");

// Wait for a message to come in
latch.await();

// Drain the connection, which will close it
CompletableFuture<Boolean> drained = nc.drain(Duration.ofSeconds(10));

// Wait for the drain to complete
drained.get();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const nc = await connect({ servers: "demo.nats.io" });
const sub = nc.subscribe(createInbox(), () => {});
nc.publish(sub.getSubject());
await nc.drain();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from nats.aio.client import Client as NATS

async def example(loop):
    nc = NATS()

    await nc.connect("nats://127.0.0.1:4222", loop=loop)

    async def handler(msg):
        print("[Received] ", msg)
        await nc.publish(msg.reply, b'I can help')

        # Can check whether client is in draining state
        if nc.is_draining:
            print("Connection is draining")

    await nc.subscribe("help", "workers", cb=handler)
    await nc.flush()

    requests = []
    for i in range(0, 10):
        request = nc.request("help", b'help!', timeout=1)
        requests.append(request)

    # Wait for all the responses
    responses = []
    responses = await asyncio.gather(*requests)

    # Gracefully close the connection.
    await nc.drain()

    print("Received {} responses".format(len(responses)))
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

var client = new NatsClient();

var subject = client.Connection.NewInbox();

// Make sure to use a cancellation token to end all subscriptions
using var cts = new CancellationTokenSource();

var sync = false;
var process = Task.Run(async () =>
{
    await foreach (var msg in client.SubscribeAsync<int>(subject, cancellationToken: cts.Token))
    {
        if (msg.Data == -1)
        {
            sync = true;
            continue;
        }
        Console.WriteLine($"Received: {msg.Data}");
        await Task.Delay(TimeSpan.FromMilliseconds(300));
    }

    Console.WriteLine("Subscription completed");
});

// Make sure the subscription is ready
while (sync == false)
{
    await Task.Delay(TimeSpan.FromMilliseconds(100));
    await client.PublishAsync(subject, -1);
}

for (var i = 0; i < 5; i++)
{
    await client.PublishAsync(subject, i);
}
Console.WriteLine("Published 5 messages");

// Cancelling the subscription will unsubscribe from the subject
// and messages that are already in the buffer will be processed
await cts.CancelAsync();
Console.WriteLine("Cancelled subscription");

// Ping the server to make sure all in-flight messages are processed
// as a side effect of the ping, the server will respond with a pong
// making sure the connection all previous messages are sent on the wire.
await client.PingAsync();

// Disposing the NATS client will close the connection
await client.DisposeAsync();
Console.WriteLine("Disposed NATS client");

Console.WriteLine("Waiting for all messages to be processed");
await process;

Console.WriteLine("Done");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
NATS.start(drain_timeout: 1) do |nc|
  NATS.subscribe('foo', queue: "workers") do |msg, reply, sub|
    nc.publish(reply, "ACK:#{msg}")
  end

  NATS.subscribe('bar', queue: "workers") do |msg, reply, sub|
    nc.publish(reply, "ACK:#{msg}")
  end

  NATS.subscribe('quux', queue: "workers") do |msg, reply, sub|
    nc.publish(reply, "ACK:#{msg}")
  end

  EM.add_timer(2) do
    next if NATS.draining?

    # Drain gracefully closes the connection.
    NATS.drain do
      puts "Done draining. Connection is closed."
    end
  end
end
```

{% endtab %}

{% tab title="C" %}

```c
static void
onMsg(natsConnection *conn, natsSubscription *sub, natsMsg *msg, void *closure)
{
    printf("Received msg: %s - %.*s\n",
           natsMsg_GetSubject(msg),
           natsMsg_GetDataLength(msg),
           natsMsg_GetData(msg));

    // Add some delay while processing
    nats_Sleep(200);

    // Need to destroy the message!
    natsMsg_Destroy(msg);
}

static void
closeHandler(natsConnection *conn, void *closure)
{
    cond_variable cv = (cond_variable) closure;

    notify_cond_variable(cv);
}

(...)


natsConnection      *conn      = NULL;
natsOptions         *opts      = NULL;
natsSubscription    *sub       = NULL;
natsStatus          s          = NATS_OK;
cond_variable       cv         = new_cond_variable(); // some fictuous way to notify between threads.

s = natsOptions_Create(&opts);
if (s == NATS_OK)
    // Setup a close handler and pass a reference to our condition variable.
    s = natsOptions_SetClosedCB(opts, closeHandler, (void*) cv);
if (s == NATS_OK)
    s = natsConnection_Connect(&conn, opts);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_Subscribe(&sub, conn, "foo", onMsg, NULL);

// Publish a message
if (s == NATS_OK)
    s = natsConnection_PublishString(conn, "foo", "hello");

// Drain the connection, which will close it when done.
if (s == NATS_OK)
    s = natsConnection_Drain(conn);

// Wait for the connection to be closed
if (s == NATS_OK)
    cond_variable_wait(cv);

(...)

// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
natsOptions_Destroy(opts);
```

{% endtab %}
{% endtabs %}

The mechanics of drain for a subscription are simpler:

1. Unsubscribe
2. Process all cached or inflight messages
3. Clean up

The API for drain can generally be used instead of unsubscribe:

{% tabs %}
{% tab title="Go" %}

```go
    nc, err := nats.Connect("demo.nats.io")
    if err != nil {
        log.Fatal(err)
    }
    defer nc.Close()

    done := sync.WaitGroup{}
    done.Add(1)

    count := 0
    errCh := make(chan error, 1)

    msgAfterDrain := "not this one"

    // Just to not collide using the demo server with other users.
    subject := nats.NewInbox()

    // This callback will process each message slowly
    sub, err := nc.Subscribe(subject, func(m *nats.Msg) {
        if string(m.Data) == msgAfterDrain {
            errCh <- fmt.Errorf("Should not have received this message")
            return
        }
        time.Sleep(100 * time.Millisecond)
        count++
        if count == 2 {
            done.Done()
        }
    })

    // Send 2 messages
    for i := 0; i < 2; i++ {
        nc.Publish(subject, []byte("hello"))
    }

    // Call Drain on the subscription. It unsubscribes but
    // wait for all pending messages to be processed.
    if err := sub.Drain(); err != nil {
        log.Fatal(err)
    }

    // Send one more message, this message should not be received
    nc.Publish(subject, []byte(msgAfterDrain))

    // Wait for the subscription to have processed the 2 messages.
    done.Wait()

    // Now check that the 3rd message was not received
    select {
    case e := <-errCh:
        log.Fatal(e)
    case <-time.After(200 * time.Millisecond):
        // OK!
    }
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// Use a latch to wait for a message to arrive
CountDownLatch latch = new CountDownLatch(1);

// Create a dispatcher and inline message handler
Dispatcher d = nc.createDispatcher((msg) -> {
    String str = new String(msg.getData(), StandardCharsets.UTF_8);
    System.out.println(str);
    latch.countDown();
});

// Subscribe
d.subscribe("updates");

// Wait for a message to come in
latch.await();

// Messages that have arrived will be processed
CompletableFuture<Boolean> drained = d.drain(Duration.ofSeconds(10));

// Wait for the drain to complete
drained.get();

// Close the connection
nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const sub = nc.subscribe(subj, { callback: (_err, _msg) => {} });
nc.publish(subj);
nc.publish(subj);
nc.publish(subj);
await sub.drain();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
from nats.aio.client import Client as NATS

async def example(loop):
    nc = NATS()

    await nc.connect("nats://127.0.0.1:4222", loop=loop)

    async def handler(msg):
        print("[Received] ", msg)
        await nc.publish(msg.reply, b'I can help')

        # Can check whether client is in draining state
        if nc.is_draining:
            print("Connection is draining")

    sid = await nc.subscribe("help", "workers", cb=handler)
    await nc.flush()

    # Gracefully unsubscribe the subscription
    await nc.drain(sid)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

var subject = client.Connection.NewInbox();

// Make sure to use a cancellation token to end the subscription
using var cts = new CancellationTokenSource();

var sync = false;
var process = Task.Run(async () =>
{
    await foreach (var msg in client.SubscribeAsync<int>(subject, cancellationToken: cts.Token))
    {
        if (msg.Data == -1)
        {
            sync = true;
            continue;
        }
        Console.WriteLine($"Received: {msg.Data}");
        await Task.Delay(TimeSpan.FromMilliseconds(300));
    }

    Console.WriteLine("Subscription completed");
});

// Make sure the subscription is ready
while (sync == false)
{
    await Task.Delay(TimeSpan.FromMilliseconds(100));
    await client.PublishAsync(subject, -1);
}

for (var i = 0; i < 5; i++)
{
    await client.PublishAsync(subject, i);
}
Console.WriteLine("Published 5 messages");

// Cancelling the subscription will unsubscribe from the subject
// and messages that are already in the buffer will be processed
await cts.CancelAsync();
Console.WriteLine("Cancelled subscription");

Console.WriteLine("Waiting for subscription to complete");
await process;

Console.WriteLine("Done");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
# There is currently no API to drain a single subscription, the whole connection can be drained though via NATS.drain
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsSubscription    *sub       = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Subscribe
if (s == NATS_OK)
    s = natsConnection_Subscribe(&sub, conn, "foo", onMsg, NULL);

// Publish 2 messages
if (s == NATS_OK)
{
    int i;
    for (i=0; (s == NATS_OK) && (i<2); i++)
    {
        s = natsConnection_PublishString(conn, "foo", "hello");
    }
}

// Call Drain on the subscription. It unsubscribes but
// wait for all pending messages to be processed.
if (s == NATS_OK)
    s = natsSubscription_Drain(sub);

(...)

// Destroy objects that were created
natsSubscription_Destroy(sub);
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

Because draining can involve messages flowing to the server, for a flush and asynchronous message processing, the timeout for drain should generally be higher than the timeout for a simple message request-reply or similar.


# Receiving Structured Data

Client libraries may provide tools to help receive structured data, like JSON. The core traffic to the NATS server will always be opaque byte arrays. The server does not process message payloads in any form. For libraries that don't provide helpers, you can always encode and decode data before sending the associated bytes to the NATS client.

For example, to receive JSON you could do:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io",
    nats.ErrorHandler(func(nc *nats.Conn, s *nats.Subscription, err error) {
        if s != nil {
        log.Printf("Async error in %q/%q: %v", s.Subject, s.Queue, err)
        } else {
        log.Printf("Async error outside subscription: %v", err)
        }
    }))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()
ec, err := nats.NewEncodedConn(nc, nats.JSON_ENCODER)
if err != nil {
    log.Fatal(err)
}
defer ec.Close()

// Define the object
type stock struct {
    Symbol string
    Price  int
}

wg := sync.WaitGroup{}
wg.Add(1)

// Subscribe
// Decoding errors will be passed to the function supplied via
// nats.ErrorHandler above, and the callback supplied here will
// not be invoked.
if _, err := ec.Subscribe("updates", func(s *stock) {
    log.Printf("Stock: %s - Price: %v", s.Symbol, s.Price)
    wg.Done()
}); err != nil {
    log.Fatal(err)
}

// Wait for a message to come in
wg.Wait()
```

{% endtab %}

{% tab title="Java" %}

```java
class StockForJsonSub {
    public String symbol;
    public float price;

    public String toString() {
        return symbol + " is at " + price;
    }
}

public class SubscribeJSON {
    public static void main(String[] args) {

        try {
            Connection nc = Nats.connect("nats://demo.nats.io:4222");

            // Use a latch to wait for 10 messages to arrive
            CountDownLatch latch = new CountDownLatch(10);

            // Create a dispatcher and inline message handler
            Dispatcher d = nc.createDispatcher((msg) -> {
                Gson gson = new Gson();

                String json = new String(msg.getData(), StandardCharsets.UTF_8);
                StockForJsonSub stk = gson.fromJson(json, StockForJsonSub.class);

                // Use the object
                System.out.println(stk);

                latch.countDown();
            });

            // Subscribe
            d.subscribe("updates");

            // Wait for a message to come in
            latch.await(); 

            // Close the connection
            nc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const sub = nc.subscribe(subj, {
  callback: (_err, msg) => {
    t.log(`${msg.json()}`);
  },
  max: 1,
});
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio
import json
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrTimeout

async def run(loop):
    nc = NATS()

    await nc.connect(servers=["nats://127.0.0.1:4222"], loop=loop)

    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        print(data)

    sid = await nc.subscribe("updates", cb=message_handler)
    await nc.flush()

    await nc.auto_unsubscribe(sid, 2)
    await nc.publish("updates", json.dumps({"symbol": "GOOG", "price": 1200 }).encode())
    await asyncio.sleep(1, loop=loop)
    await nc.close()
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

// NATS .NET has a built-in serializer that does the 'unsurprising' thing
// for most types. Most primitive types are serialized as expected.
// For any other type, JSON serialization is used. You can also provide
// your own serializers by implementing the INatsSerializer and
// INasSerializerRegistry interfaces. See also for more information:
// https://nats-io.github.io/nats.net/documentation/advanced/serialization.html
await using var nc = new NatsClient();

CancellationTokenSource cts = new();

// Subscribe for int, string, bytes, json
List<Task> tasks =
[
    Task.Run(async () =>
    {
        await foreach (var msg in nc.SubscribeAsync<int>("x.int", cancellationToken: cts.Token))
        {
            Console.WriteLine($"Received int: {msg.Data}");
        }
    }),

    Task.Run(async () =>
    {
        await foreach (var msg in nc.SubscribeAsync<string>("x.string", cancellationToken: cts.Token))
        {
            Console.WriteLine($"Received string: {msg.Data}");
        }
    }),

    Task.Run(async () =>
    {
        await foreach (var msg in nc.SubscribeAsync<byte[]>("x.bytes", cancellationToken: cts.Token))
        {
            if (msg.Data != null)
            {
                Console.Write($"Received bytes: ");
                foreach (var b in msg.Data)
                {
                    Console.Write("0x{0:X2} ", b);
                }
                Console.WriteLine();
            }
        }
    }),

    Task.Run(async () =>
    {
        await foreach (var msg in nc.SubscribeAsync<MyData>("x.json", cancellationToken: cts.Token))
        {
            Console.WriteLine($"Received data: {msg.Data}");
        }
    }),
];

// Give the subscriber tasks some time to subscribe
await Task.Delay(1000);

await nc.PublishAsync<int>("x.int", 100);
await nc.PublishAsync<string>("x.string", "Hello, World!");
await nc.PublishAsync<byte[]>("x.bytes", new byte[] { 0x41, 0x42, 0x43 });
await nc.PublishAsync<MyData>("x.json", new MyData(30, "bar"));

await cts.CancelAsync();

await Task.WhenAll(tasks);

public record MyData(int Id, string Name);

// Output:
// Received int: 100
// Received bytes: 0x41 0x42 0x43
// Received string: Hello, World!
// Received data: MyData { Id = 30, Name = bar }

// See also for more information:
// https://nats-io.github.io/nats.net/documentation/advanced/serialization.html
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'json'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  nc.subscribe("updates") do |msg|
    m = JSON.parse(msg)

    # {"symbol"=>"GOOG", "price"=>12}
    p m
  end
end
```

{% endtab %}

{% tab title="C" %}

```c
// Structured data is not configurable in C NATS Client.
```

{% endtab %}
{% endtabs %}


# Sending Messages

NATS sends and receives messages using a protocol that includes a target subject, an optional reply subject and an array of bytes. Some libraries may provide helpers to convert other data formats to and from bytes, but the NATS server will treat all messages as opaque byte arrays.

All of the NATS clients are designed to make sending a message simple. For example, to send the string “All is Well” to the “updates” subject as a UTF-8 string of bytes you would do:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io", nats.Name("API PublishBytes Example"))
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

if err := nc.Publish("updates", []byte("All is Well")); err != nil {
    log.Fatal(err)
}
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

nc.publish("updates", "All is Well".getBytes(StandardCharsets.UTF_8));
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const sc = StringCodec();
nc.publish("updates", sc.encode("All is Well"));
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

await nc.publish("updates", b'All is Well')
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient(url: "demo.nats.io", name: "API Publish String Example");

// The default serializer uses UTF-8 encoding for strings
await client.PublishAsync<string>(subject: "updates", data: "All is Well");
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  nc.publish("updates", "All is Well")
end
```

{% endtab %}
{% endtabs %}


# Including a Reply Subject

The optional reply-to field when publishing a message can be used on the receiving side to respond. The reply-to subject is often called an *inbox*, and most libraries may provide a method for generating unique inbox subjects. Most libraries also provide for the request-reply pattern with a single call. For example to send a request to the subject `time`, with no content for the messages, you might:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Create a unique subject name for replies.
uniqueReplyTo := nats.NewInbox()

// Listen for a single response
sub, err := nc.SubscribeSync(uniqueReplyTo)
if err != nil {
    log.Fatal(err)
}

// Send the request.
// If processing is synchronous, use Request() which returns the response message.
if err := nc.PublishRequest("time", uniqueReplyTo, nil); err != nil {
    log.Fatal(err)
}

// Read the reply
msg, err := sub.NextMsg(time.Second)
if err != nil {
    log.Fatal(err)
}

// Use the response
log.Printf("Reply: %s", msg.Data)
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// set up a listener for "time" requests
Dispatcher d = nc.createDispatcher(msg -> {
    System.out.println("Received time request");
    nc.publish(msg.getReplyTo(), ("" + System.currentTimeMillis()).getBytes());
});
d.subscribe("time");

// make a subject for replies and subscribe to that
String replyToThis = NUID.nextGlobal();
Subscription sub = nc.subscribe(replyToThis);

// publish to the "time" subject with reply-to subject that was set up
nc.publish("time", replyToThis, null);

// wait for a response
Message msg = sub.nextMessage(1000);

// look at the response
long time = Long.parseLong(new String(msg.getData()));
System.out.println(new Date(time));

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// set up a subscription to process the request
const sc = StringCodec();
nc.subscribe("time", {
  callback: (_err, msg) => {
    msg.respond(sc.encode(new Date().toLocaleTimeString()));
  },
});

// create a subscription subject that the responding send replies to
const inbox = createInbox();
const sub = nc.subscribe(inbox, {
  max: 1,
  callback: (_err, msg) => {
    t.log(`the time is ${sc.decode(msg.data)}`);
  },
});

nc.publish("time", Empty, { reply: inbox });
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

future = asyncio.Future()

async def sub(msg):
  nonlocal future
  future.set_result(msg)

await nc.connect(servers=["nats://demo.nats.io:4222"])
await nc.subscribe("time", cb=sub)

unique_reply_to = nc.new_inbox()
await nc.publish("time", b'', unique_reply_to)

# Use the response
msg = await asyncio.wait_for(future, 1)
print("Reply:", msg)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.Core;

await using var client = new NatsClient();

await client.ConnectAsync();

// Create a new inbox for the subscription subject
string inbox = client.Connection.NewInbox();

// Use core API to subscribe to have a more fine-grained control over
// the subscriptions. We use <string> as the type, but we are not
// really interested in the message payload.
await using INatsSub<string> timeSub
    = await client.Connection.SubscribeCoreAsync<string>("time");

Task responderTask = Task.Run(async () =>
{
    await foreach (var msg in timeSub.Msgs.ReadAllAsync())
    {
        // The default serializer uses StandardFormat with Utf8Formatter
        // when formatting DateTimeOffset types.
        await msg.ReplyAsync<DateTimeOffset>(DateTimeOffset.UtcNow);
    }
});

// Subscribe to the inbox with the expected type of the response
await using INatsSub<DateTimeOffset> inboxSub
    = await client.Connection.SubscribeCoreAsync<DateTimeOffset>(inbox);

// The default serializer uses UTF-8 encoding for strings
await client.PublishAsync(subject: "time", replyTo: inbox);

// Read the response from subscription message channel reader
NatsMsg<DateTimeOffset> reply = await inboxSub.Msgs.ReadAsync();

// Print the current time in RFC1123 format taking advantage of the
// DateTimeOffset's formatting capabilities.
Console.WriteLine($"The current date and time is: {reply.Data:R}");

await inboxSub.UnsubscribeAsync();
await timeSub.UnsubscribeAsync();

// make sure the responder task is completed cleanly
await responderTask;

// Output:
// The current date and time is: Tue, 22 Oct 2024 12:21:09 GMT
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  Fiber.new do
    f = Fiber.current

    nc.subscribe("time") do |msg, reply|
      f.resume msg
    end

    nc.publish("time", 'example', NATS.create_inbox)

    # Use the response
    msg = Fiber.yield
    puts "Reply: #{msg}"

  end.resume
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);
// Publish a message and provide a reply subject
if (s == NATS_OK)
    s = natsConnection_PublishRequestString(conn, "request", "reply", "this is the request");

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}


# Request-Reply Semantics

The pattern of sending a message and receiving a response is encapsulated in most client libraries into a request method. Under the covers this method will publish a message with a unique reply-to subject and wait for the response before returning.

In the older versions of some libraries a completely new reply-to subject is created each time. In newer versions, a subject hierarchy is used so that a single subscriber in the client library listens for a wildcard, and requests are sent with a unique child subject of a single subject.

The primary difference between the request method and publishing with a reply-to is that the library is only going to accept one response, and in most libraries the request will be treated as a synchronous action. The library may even provide a way to set the timeout.

For example, updating the previous publish example we may request `time` with a one second timeout:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Send the request
msg, err := nc.Request("time", nil, time.Second)
if err != nil {
    log.Fatal(err)
}

// Use the response
log.Printf("Reply: %s", msg.Data)

// Close the connection
nc.Close()
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

// set up a listener for "time" requests
Dispatcher d = nc.createDispatcher(msg -> {
    System.out.println("Received time request");
    nc.publish(msg.getReplyTo(), ("" + System.currentTimeMillis()).getBytes());
});
d.subscribe("time");

// make a request to the "time" subject and wait 1 second for a response
Message msg = nc.request("time", null, Duration.ofSeconds(1));

// look at the response
long time = Long.parseLong(new String(msg.getData()));
System.out.println(new Date(time));

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
// set up a subscription to process the request
const sc = StringCodec();
nc.subscribe("time", {
  callback: (_err, msg) => {
    msg.respond(sc.encode(new Date().toLocaleTimeString()));
  },
});

const r = await nc.request("time");
t.log(sc.decode(r.data));
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

async def sub(msg):
  await nc.publish(msg.reply, b'response')

await nc.connect(servers=["nats://demo.nats.io:4222"])
await nc.subscribe("time", cb=sub)

# Send the request
try:
  msg = await nc.request("time", b'', timeout=1)
  # Use the response
  print("Reply:", msg)
except asyncio.TimeoutError:
  print("Timed out waiting for response")
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

using CancellationTokenSource cts = new();

// Process the time messages in a separate task
Task subscription = Task.Run(async () =>
{
    await foreach (var msg in client.SubscribeAsync<string>("time", cancellationToken: cts.Token))
    {
        await msg.ReplyAsync(DateTimeOffset.Now);
    }
});

// Wait for the subscription task to be ready
await Task.Delay(1000);

var reply = await client.RequestAsync<DateTimeOffset>("time");

Console.WriteLine($"Reply: {reply.Data:O}");

await cts.CancelAsync();
await subscription;

// Output:
// Reply: 2024-10-23T05:20:55.0000000+01:00
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  nc.subscribe("time") do |msg, reply|
    nc.publish(reply, "response")
  end

  Fiber.new do
    # Use the response
    msg = nc.request("time", "")
    puts "Reply: #{msg}"
  end.resume
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsMsg             *msg       = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Send a request and wait for up to 1 second
if (s == NATS_OK)
    s = natsConnection_RequestString(&msg, conn, "request", "this is the request", 1000);

if (s == NATS_OK)
{
    printf("Received msg: %s - %.*s\n",
           natsMsg_GetSubject(msg),
           natsMsg_GetDataLength(msg),
           natsMsg_GetData(msg));

    // Destroy the message that was received
    natsMsg_Destroy(msg);
}

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

You can think of request-reply in the library as a subscribe, get one message, unsubscribe pattern. In Go this might look something like:

```go
sub, err := nc.SubscribeSync(replyTo)
if err != nil {
    log.Fatal(err)
}

// Send the request immediately
nc.PublishRequest(subject, replyTo, []byte(input))
nc.Flush()

// Wait for a single response
for {
    msg, err := sub.NextMsg(1 * time.Second)
    if err != nil {
        log.Fatal(err)
    }

    response = string(msg.Data)
    break
}
sub.Unsubscribe()
```

## Scatter-Gather

You can expand the request-reply pattern into something often called scatter-gather. To receive multiple messages, with a timeout, you could do something like the following, where the loop getting messages is using time as the limitation, not the receipt of a single message:

```go
sub, err := nc.SubscribeSync(replyTo)
if err != nil {
    log.Fatal(err)
}
nc.Flush()

// Send the request
nc.PublishRequest(subject, replyTo, []byte(input))

// Wait for a single response
max := 100 * time.Millisecond
start := time.Now()
for time.Now().Sub(start) < max {
    msg, err := sub.NextMsg(1 * time.Second)
    if err != nil {
        break
    }

    responses = append(responses, string(msg.Data))
}
sub.Unsubscribe()
```

Or, you can loop on a counter and a timeout to try to get *at least N* responses:

```go
sub, err := nc.SubscribeSync(replyTo)
if err != nil {
    log.Fatal(err)
}
nc.Flush()

// Send the request
nc.PublishRequest(subject, replyTo, []byte(input))

// Wait for a single response
max := 500 * time.Millisecond
start := time.Now()
for time.Now().Sub(start) < max {
    msg, err := sub.NextMsg(1 * time.Second)
    if err != nil {
        break
    }

    responses = append(responses, string(msg.Data))

    if len(responses) >= minResponses {
        break
    }
}
sub.Unsubscribe()
```


# Caches, Flush and Ping

For performance reasons, most if not all, of the client libraries will buffer outgoing data so that bigger chunks can be written to the network at one time. This may be as simple as a byte buffer that stores a few messages before being pushed to the network.

These buffers do not hold messages forever, generally they are designed to hold messages in high throughput scenarios, while still providing good latency in low throughput situations.

It is the libraries job to make sure messages flow in a high performance manner. But there may be times when an application needs to know that a message has "hit the wire." In this case, applications can use a flush call to tell the library to move data through the system.

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

// Just to not collide using the demo server with other users.
subject := nats.NewInbox()

if err := nc.Publish(subject, []byte("All is Well")); err != nil {
    log.Fatal(err)
}
// Sends a PING and wait for a PONG from the server, up to the given timeout.
// This gives guarantee that the server has processed the above message.
if err := nc.FlushTimeout(time.Second); err != nil {
    log.Fatal(err)
}
```

{% endtab %}

{% tab title="Java" %}

```java
Connection nc = Nats.connect("nats://demo.nats.io:4222");

nc.publish("updates", "All is Well".getBytes(StandardCharsets.UTF_8));
nc.flush(Duration.ofSeconds(1)); // Flush the message queue

nc.close();
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const start = Date.now();
nc.flush().then(() => {
  t.log("round trip completed in", Date.now() - start, "ms");
});
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

await nc.publish("updates", b'All is Well')

# Sends a PING and wait for a PONG from the server, up to the given timeout.
# This gives guarantee that the server has processed above message.
await nc.flush(timeout=1)
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

await client.PublishAsync("updates", "All is well");

// Sends a PING and wait for a PONG from the server.
// This gives a guarantee that the server has processed the above message
// since the underlining TCP connection sends and receives messages in order.
await client.PingAsync();
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'fiber'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  nc.subscribe("updates") do |msg|
    puts msg
  end

  nc.publish("updates", "All is Well")

  nc.flush do
    # Sends a PING and wait for a PONG from the server, up to the given timeout.
    # This gives guarantee that the server has processed above message at this point.
  end
end
```

{% endtab %}

{% tab title="C" %}

```c
natsConnection      *conn      = NULL;
natsStatus          s          = NATS_OK;

s = natsConnection_ConnectTo(&conn, NATS_DEFAULT_URL);

// Send a request and wait for up to 1 second
if (s == NATS_OK)
    s = natsConnection_PublishString(conn, "foo", "All is Well");

// Sends a PING and wait for a PONG from the server, up to the given timeout.
// This gives guarantee that the server has processed the above message.
if (s == NATS_OK)
    s = natsConnection_FlushTimeout(conn, 1000);

(...)

// Destroy objects that were created
natsConnection_Destroy(conn);
```

{% endtab %}
{% endtabs %}

## Flush and Ping/Pong

Many of the client libraries use the [PING/PONG interaction](https://docs.nats.io/using-nats/developer/connecting/pingpong) built into the NATS protocol to ensure that flush pushed all of the buffered messages to the server. When an application calls flush, most libraries will put a PING on the outgoing queue of messages, and wait for the server to respond with a PONG before saying that the flush was successful.

Even though the client may use PING/PONG for flush, pings sent this way do not count towards [max outgoing pings](https://docs.nats.io/using-nats/developer/connecting/pingpong).


# Sending Structured Data

Some client libraries provide helpers to send structured data while others depend on the application to perform any encoding and decoding and just take byte arrays for sending. The following example shows how to send JSON but this could easily be altered to send a protocol buffer, YAML or some other format. JSON is a text format so we also have to encode the string in most languages to bytes. We are using UTF-8, the JSON standard encoding.

Take a simple *stock ticker* that sends the symbol and price of each stock:

{% tabs %}
{% tab title="Go" %}

```go
nc, err := nats.Connect("demo.nats.io")
if err != nil {
    log.Fatal(err)
}
defer nc.Close()

ec, err := nats.NewEncodedConn(nc, nats.JSON_ENCODER)
if err != nil {
    log.Fatal(err)
}
defer ec.Close()

// Define the object
type stock struct {
    Symbol string
    Price  int
}

// Publish the message
if err := ec.Publish("updates", &stock{Symbol: "GOOG", Price: 1200}); err != nil {
    log.Fatal(err)
}
```

{% endtab %}

{% tab title="Java" %}

```java
class StockForJsonPub {
    public String symbol;
    public float price;
}

public class PublishJSON {
    public static void main(String[] args) {
        try {
            Connection nc = Nats.connect("nats://demo.nats.io:4222");

            // Create the data object
            StockForJsonPub stk = new StockForJsonPub();
            stk.symbol="GOOG";
            stk.price=1200;

            // use Gson to encode the object to JSON
            GsonBuilder builder = new GsonBuilder();
            Gson gson = builder.create();
            String json = gson.toJson(stk);

            // Publish the message
            nc.publish("updates", json.getBytes(StandardCharsets.UTF_8));

            // Make sure the message goes through before we close
            nc.flush(Duration.ZERO);
            nc.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
nc.publish("updates", JSON.stringify({ ticker: "GOOG", price: 2868.87 }));
```

{% endtab %}

{% tab title="Python" %}

```python
nc = NATS()

await nc.connect(servers=["nats://demo.nats.io:4222"])

await nc.publish("updates", json.dumps({"symbol": "GOOG", "price": 1200 }).encode())
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;

await using var client = new NatsClient();

using var cts = new CancellationTokenSource();

Task process = Task.Run(async () =>
{
    // Let's deserialize the message as a UTF-8 string to see
    // the published serialized output in the console
    await foreach (var msg in client.SubscribeAsync<string>("updates", cancellationToken: cts.Token))
    {
        Console.WriteLine($"Received: {msg.Data}");
    }
});

// Wait for the subscription task to be ready
await Task.Delay(1000);

var stock = new Stock { Symbol = "MSFT", Price = 123.45 };

// The default serializer uses System.Text.Json to serialize the object
await client.PublishAsync<Stock>("updates", stock);

// Define the object
public record Stock {
    public string Symbol { get; set; }
    public double Price { get; set; }
}

// Output:
// Received: {"Symbol":"MSFT","Price":123.45}
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'nats/client'
require 'json'

NATS.start(servers:["nats://127.0.0.1:4222"]) do |nc|
  nc.publish("updates", {"symbol": "GOOG", "price": 1200}.to_json)
end
```

{% endtab %}

{% tab title="C" %}

```c
// Structured data is not configurable in C NATS Client.
```

{% endtab %}
{% endtabs %}


# Building Services

Recently we have agreed upon an [initial specification](https://github.com/nats-io/nats-architecture-and-design/blob/main/adr/ADR-32.md) for a services protocol so that we can add first-class services support to NATS clients and support this in our tooling. This services protocol is an agreement between clients and tooling and doesn't require any special functionality from the NATS server or JetStream.

To check if the NATS client in your favorite language supports the new services API, make sure you check the docs and GitHub repository for that client. The services API is relatively new and not all clients may support it yet.

To see the services API in action in different languages, take a look at the [NATS By Example](https://natsbyexample.com/examples/services/intro/go) samples.

## Concepts

There are a few high level concepts in the services API worth understanding before you start developing your own services.

### Service

The service is the highest level abstraction and refers to a group of logically related functionality. Services are required to have names and versions that conform to the [semver](https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string) rules. Services are discoverable within a NATS system.

### Endpoint

A service endpoint is the entity with which clients interact. You can think of an endpoint as a single operation within a service. All services must have at least 1 endpoint.

### Group

A group is a collection of endpoints. These are optional and can provide a logical association between endpoints as well as an optional common subject prefix for all endpoints.

## Service Operations

The services API supports 3 operations for discoverability and observability. While the NATS client will take care of responding on these subjects, it is still the developer's responsibility to respond to requests made the service's actual endpoints.

* `PING` - Requests made on the `$SRV.PING.>` subject gather replies from running services. This facilitates service listing by tooling.
* `STATS` - Requests made on the `$SRV.STATS.>` subject query statistics from services. Available stats include total requests, total errors, and total processing time.
* `INFO` - Requests made on the `$SRV.INFO.>` subject obtain the service definition and metadata, including groups, endpoints, etc.


# JetStream

## Deciding to use streaming and higher qualities of service

In modern systems, applications can expose services or produce and consume data streams. A basic aspect of publish-subscribe messaging is temporal coupling: the subscribers need to be up and running to receive the message when it is published. At a high level, if observability is required, applications need to consume messages in the future, need to consume at their own pace, or need all messages, then JetStream's streaming functionalities provide the temporal de-coupling between publishers and consumers.

Using streaming and its associated higher qualities of service is the facet of messaging with the highest cost in terms of compute and storage.

### When to use streaming

Streaming is ideal when:

* Data producers and consumers are highly decoupled. They may be online at different times and consumers must receive messages.
* A historical record of the data in the stream is required. This is when a replay of data is required by a consumer.
* The last message on a stream is required for initialization and the producer may be offline.
* A-priori knowledge of consumers is not available, but consumers must receive messages. This is often a false assumption.
* The data in messages being sent have a lifespan beyond that of the intended application lifespan.
* Applications need to consume data at their own pace.
* You want decoupled flow control between the publishers and the consumers of the stream
* You need 'exactly once' quality of service with de-duplication of publications and double-acknowledged consumption

Note that no assumptions should ever be made of who will receive and process data in the future, or for what purpose.

### When to use Core NATS

Using core NATS is ideal as the fast request path for scalable services where there is tolerance for message loss or when applications themselves handle message delivery guarantees.

These include:

* Service patterns where there is a tightly coupled request-reply
  * A request is made, and the application handles error cases upon timeout

    (resends, errors, etc). \_\_Relying on a messaging system to resend here is

    considered an anti-pattern.\_\_
* Where only the last message received is important and new messages will be received frequently enough for applications to tolerate a lost message. This might be a stock ticker stream, frequent exchange of messages in a service control plane, or device telemetry.
* Message TTL is low, where the value of the data being transmitted degrades or expires quickly.
* The expected consumer set for a message is available a-priori and consumers are expected to be live. The request-reply pattern works well here or consumers can send an application level acknowledgement.
* Control plane messages.

## JetStream functionality overview

### Streams

* You can use 'Add Stream' to idempotently define streams and their attributes (i.e. source subjects, retention and storage policies, limits)
* You can use 'Purge' to purge the messages in a stream
* You can use 'Delete' to delete a stream

### Publish to a stream

There is interoperability between 'Core NATS' and JetStream in the fact that the streams are listening to core NATS messages. *However* you will notice that the NATS client libraries' JetStream calls include some 'Publish' calls and so may be wondering what is the difference between a 'Core NATS Publish' and a 'JetStream Publish'.

So yes, when a 'Core NATS' application publishes a message on a Stream's subject, that message will indeed get stored in the stream, but that's not really the intent as you are then publishing with the lower quality of service provided by Core NATS. So, while it will definitely work to just use the Core NATS Publish call to publish to a stream, look at it more as a convenience that you can use to help ease the migration of your applications to use streaming rather the desired end state or ideal design.

Instead, it is better for applications to use the JetStream Publish calls (which Core NATS subscribers not using Streams will still receive like any other publication) when publishing to a stream as:

* JetStream publish calls are acknowledged by the JetStream enabled servers, which allows for the following higher qualities of service
  * If the publisher receives the acknowledgement from the server it can safely discard any state it has for that publication, the message has not only been received correctly by the server, but it has also been successfully persisted.
  * Whether you use the synchronous or the asynchronous JetStream publish calls, there is an implied flow control between the publisher and the JetStream infrastructure.
  * You can have 'exactly-once' quality of service by the JetStream publishing application inserting a unique publication ID in a header field of the message.

#### See Also

* [Sync and Async JetStream publishing in Java](https://nats.io/blog/sync-async-publish-java-client/#synchronous-and-asynchronous-publishing-with-the-nats-java-library)

### Create a consumer

[Consumers](https://docs.nats.io/nats-concepts/jetstream/consumers) are 'views' into a stream, with their own cursor. They are how client applications get messages from a stream (i.e. 'replayed') for processing or consumption. They can filter messages in the stream according to a 'filtering subject' and define which part of the stream is replayed according to a 'replay policy'.

You can create *push* or *pull* consumers:

* *Push* consumers (specifically ordered push consumers) are the best way for an application to receive its own complete copy of the selected messages in the stream.
* *Pull* consumers are the best way to scale horizontally the processing (or consuming) of the selected messages in the stream using multiple client applications sharing the same pull consumer, and allow for the processing of messages in batches.

Consumers can be ephemeral or durable, and support different sets of acknowledgement policies; none, this sequence number, this sequence number and all before it.

#### Replay policy

You select which of the messages in the stream you want to have delivered to your consumer

* all
* from a sequence number
* from a point in time
* the last message
* the last message(s) for all the subject(s) in the stream

And you can select the replay speed to be instant or to match the initial publication rate into the stream

### Subscribe from a consumer

Client applications 'subscribe' from consumers using the JetStream's Subscribe, QueueSubscribe or PullSubscribe (and variations) calls. Note that since the initial release of JetStream, clients have developed a more ergonomic API to work with [Consumers](https://github.com/nats-io/nats.go/blob/main/jetstream/README.md#consumers) to process messages.

#### Acknowledging messages

Some consumers require the client application code to acknowledge the processing or consumption of the message, but there is more than one way to acknowledge (or not) a message

* `Ack` Acknowledges a message was completely handled
* `Nak` Signals that the message will not be processed now and processing can move onto the next message, NAK'd message will be retried
* `InProgress` When sent before the AckWait period indicates that work is ongoing and the period should be extended by another equal to `AckWait`
* `Term` Instructs the server to stop redelivery of a message without acknowledging it as successfully processed

#### See Also

* Java
  * [JetStream Java tutorial](https://nats.io/blog/hello-world-java-client/)
  * [JetStream stream creation in Java](https://nats.io/blog/jetstream-java-client-01-stream-create/)
  * [JetStream publishing in Java](https://nats.io/blog/jetstream-java-client-02-publish/)
  * [Consumers in Java](https://nats.io/blog/jetstream-java-client-03-consume/)
  * [Push consumers in Java](https://nats.io/blog/jetstream-java-client-04-push-subscribe/#jetstream-push-consumers-with-the-natsio-java-library)
  * [Pull consumers in Java](https://nats.io/blog/jetstream-java-client-05-pull-subscribe/#jetstream-pull-consumers-with-the-natsio-java-library)


# JetStream Model Deep Dive

## Stream Limits, Retention, and Policy

Streams store data on disk, but we cannot store all data forever, so we need ways to control their size automatically.

There are 3 features that come into play when Streams decide how long they store data.

The `Retention Policy` describes based on what criteria a set will evict messages from its storage:

| Retention Policy  | Description                                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LimitsPolicy`    | Limits are set for how many messages, how big the storage and how old messages may be.                                                                                                                                                                                                                                                                                     |
| `WorkQueuePolicy` | Messages are kept until they are consumed: meaning delivered ( by *the* consumer filtering on the message's subject (in this mode of operation you can not have any overlapping consumers defined on the Stream - each subject captured by the stream can only have one consumer at a time)) to a subscribing application and explicitly acknowledged by that application. |
| `InterestPolicy`  | Messages are kept as long as there are Consumers on the stream (matching the message's subject if they are filtered consumers) for which the message has not yet been ACKed. Once all currently defined consumers have received explicit acknowledgement from a subscribing application for the message it is then removed from the stream.                                |

In all Retention Policies the basic limits apply as upper bounds, these are `MaxMsgs` for how many messages are kept in total, `MaxBytes` for how big the set can be in total and `MaxAge` for what is the oldest message that will be kept. These are the only limits in play with `LimitsPolicy` retention.

One can then define additional ways a message may be removed from the Stream earlier than these limits. In `WorkQueuePolicy` the messages will be removed as soon as *the* Consumer received an Acknowledgement. In `InterestPolicy` messages will be removed as soon as *all* Consumers of the stream for that subject have received an Acknowledgement for the message.

In both `WorkQueuePolicy` and `InterestPolicy` the age, size and count limits will still apply as upper bounds.

A final control is the Maximum Size any single message may have. NATS have it's own limit for maximum size (1 MiB by default), but you can say a Stream will only accept messages up to 1024 bytes using `MaxMsgSize`.

The `Discard Policy` sets how messages are discarded when limits set by `LimitsPolicy` are reached. The `DiscardOld` option removes old messages making space for new, while `DiscardNew` refuses any new messages.

The `WorkQueuePolicy` mode is a specialized mode where a message, once consumed and acknowledged, is removed from the Stream.

## Message Deduplication

JetStream support idempotent message writes by ignoring duplicate messages as indicated by the `Nats-Msg-Id` header.

```shell
nats req -H Nats-Msg-Id:1 ORDERS.new hello1
nats req -H Nats-Msg-Id:1 ORDERS.new hello2
nats req -H Nats-Msg-Id:1 ORDERS.new hello3
nats req -H Nats-Msg-Id:1 ORDERS.new hello4
```

Here we set a `Nats-Msg-Id:1` header which tells JetStream to ensure we do not have duplicates of this message - we only consult the message ID not the body.

```shell
nats stream info ORDERS
```

and in the output you can see that the duplicate publications were detected and only one message (the first one) is actually stored in the stream

```
....
State:

            Messages: 1
               Bytes: 67 B
```

The default window to track duplicates in is 2 minutes, this can be set on the command line using `--dupe-window` when creating a stream, though we would caution against large windows.

## Acknowledgement Models

Streams support acknowledging receiving a message, if you send a `Request()` to a subject covered by the configuration of the Stream the service will reply to you once it stored the message. If you just publish, it will not. A Stream can be set to disable Acknowledgements by setting `NoAck` to `true` in it's configuration.

Consumers have 3 acknowledgement modes:

| Mode          | Description                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AckExplicit` | This requires every message to be specifically acknowledged, it's the only supported option for pull-based Consumers                                    |
| `AckAll`      | In this mode if you acknowledge message `100` it will also acknowledge message `1`-`99`, this is good for processing batches and to reduce ack overhead |
| `AckNone`     | No acknowledgements are supported                                                                                                                       |

To understand how Consumers track messages we will start with a clean `ORDERS` Stream and `DISPATCH` Consumer.

```shell
nats str info ORDERS
```

```
...
Statistics:

            Messages: 0
               Bytes: 0 B
            FirstSeq: 0
             LastSeq: 0
    Active Consumers: 1
```

The Set is entirely empty

```shell
nats con info ORDERS DISPATCH
```

```
...
State:

  Last Delivered Message: Consumer sequence: 1 Stream sequence: 1
    Acknowledgment floor: Consumer sequence: 0 Stream sequence: 0
        Pending Messages: 0
    Redelivered Messages: 0
```

The Consumer has no messages outstanding and has never had any (Consumer sequence is 1).

We publish one message to the Stream and see that the Stream received it:

```shell
nats pub ORDERS.processed "order 4"
```

```
Published 7 bytes to ORDERS.processed
$ nats str info ORDERS
...
Statistics:

            Messages: 1
               Bytes: 53 B
            FirstSeq: 1
             LastSeq: 1
    Active Consumers: 1
```

As the Consumer is pull-based, we can fetch the message, ack it, and check the Consumer state:

```shell
nats con next ORDERS DISPATCH
```

```
--- received on ORDERS.processed
order 4

Acknowledged message

$ nats con info ORDERS DISPATCH
...
State:

  Last Delivered Message: Consumer sequence: 2 Stream sequence: 2
    Acknowledgment floor: Consumer sequence: 1 Stream sequence: 1
        Pending Messages: 0
    Redelivered Messages: 0
```

The message got delivered and acknowledged - `Acknowledgement floor` is `1` and `1`, the sequence of the Consumer is `2` which means its had only the one message through and got acked. Since it was acked, nothing is pending or redelivering.

We'll publish another message, fetch it but not Ack it this time and see the status:

```shell
nats pub ORDERS.processed "order 5"
```

```
Published 7 bytes to ORDERS.processed
```

Get the next message from the consumer (but do not acknowledge it)

```shell
nats consumer next ORDERS DISPATCH --no-ack
```

```
--- received on ORDERS.processed
order 5
```

Show the consumer info

```shell
nats consumer info ORDERS DISPATCH
```

```
State:

  Last Delivered Message: Consumer sequence: 3 Stream sequence: 3
    Acknowledgment floor: Consumer sequence: 1 Stream sequence: 1
        Pending Messages: 1
    Redelivered Messages: 0
```

Now we can see the Consumer has processed 2 messages (obs sequence is 3, next message will be 3) but the Ack floor is still 1 - thus 1 message is pending acknowledgement. Indeed this is confirmed in the `Pending messages`.

If I fetch it again and again do not ack it:

```shell
nats consumer next ORDERS DISPATCH --no-ack
```

```
--- received on ORDERS.processed
order 5
```

Show the consumer info again

```shell
nats consumer info ORDERS DISPATCH
```

```
State:

  Last Delivered Message: Consumer sequence: 4 Stream sequence: 3
    Acknowledgment floor: Consumer sequence: 1 Stream sequence: 1
        Pending Messages: 1
    Redelivered Messages: 1
```

The Consumer sequence increases - each delivery attempt increases the sequence - and our redelivered count also goes up.

Finally, if I then fetch it again and ack it this time:

```shell
nats consumer next ORDERS DISPATCH 
```

```
--- received on ORDERS.processed
order 5

Acknowledged message
```

Show the consumer info

```shell
nats consumer info ORDERS DISPATCH
```

```
State:

  Last Delivered Message: Consumer sequence: 5 Stream sequence: 3
    Acknowledgment floor: Consumer sequence: 1 Stream sequence: 1
        Pending Messages: 0
    Redelivered Messages: 0
```

Having now Acked the message there are no more pending.

Additionally, there are a few types of acknowledgements:

| Type          | Bytes       | Description                                                                                                                        |
| ------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `AckAck`      | nil, `+ACK` | Acknowledges a message was completely handled                                                                                      |
| `AckNak`      | `-NAK`      | Signals that the message will not be processed now and processing can move onto the next message, NAK'd message will be retried    |
| `AckProgress` | `+WPI`      | When sent before the AckWait period indicates that work is ongoing and the period should be extended by another equal to `AckWait` |
| `AckNext`     | `+NXT`      | Acknowledges the message was handled and requests delivery of the next message to the reply subject. Only applies to Pull-mode.    |
| `AckTerm`     | `+TERM`     | Instructs the server to stop redelivery of a message without acknowledging it as successfully processed                            |

So far all of the examples were the `AckAck` type of acknowledgement, by replying to the Ack with the body as indicated in `Bytes` you can pick what mode of acknowledgement you want. Note that this description is documenting the internal JetStream protocol. Client libraries offer APIs for performing all the above acknowledgments using specific APIs where you don't worry about the internal protocol payloads.

All of these acknowledgement modes, except `AckNext`, support double acknowledgement - if you set a reply subject when acknowledging the server will in turn acknowledge having received your ACK.

The `+NXT` acknowledgement can have a few formats: `+NXT 10` requests 10 messages and `+NXT {"no_wait": true}` which is the same data that can be sent in a Pull Request.

## Exactly Once Semantics

JetStream supports Exactly Once publication and consumption by combining Message Deduplication and double acks.

On the publishing side you can avoid duplicate message ingestion using the [Message Deduplication](#message-deduplication) feature.

Consumers can be 100% sure a message was correctly processed by requesting the server Acknowledge having received your acknowledgement (sometimes referred to as double-acking) by calling the message's `AckSync()` (rather than `Ack()`) function which sets a reply subject on the Ack and waits for a response from the server on the reception and processing of the acknowledgement. If the response received from the server indicates success you can be sure that the message will never be re-delivered by the consumer (due to a loss of your acknowledgement).

## Consumer Starting Position

When setting up a Consumer you can decide where to start, the system supports the following for the `DeliverPolicy`:

| Policy              | Description                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| `all`               | Delivers all messages that are available                                   |
| `last`              | Delivers the latest message, like a `tail -n 1 -f`                         |
| `new`               | Delivers only new messages that arrive after subscribe time                |
| `by_start_time`     | Delivers from a specific time onward. Requires `OptStartTime` to be set    |
| `by_start_sequence` | Delivers from a specific stream sequence. Requires `OptStartSeq` to be set |

Regardless of what mode you set, this is only the starting point. Once started it will always give you what you have not seen or acknowledged. So this is merely how it picks the very first message.

Let's look at each of these, first we make a new Stream `ORDERS` and add 100 messages to it.

Now create a `DeliverAll` pull-based Consumer:

```shell
nats consumer add ORDERS ALL --pull --filter ORDERS.processed --ack none --replay instant --deliver all 
nats consumer next ORDERS ALL
```

```
--- received on ORDERS.processed
order 1

Acknowledged message
```

Now create a `DeliverLast` pull-based Consumer:

```shell
nats consumer add ORDERS LAST --pull --filter ORDERS.processed --ack none --replay instant --deliver last
nats consumer next ORDERS LAST
```

```
--- received on ORDERS.processed
order 100

Acknowledged message
```

Now create a `MsgSetSeq` pull-based Consumer:

```shell
nats consumer add ORDERS TEN --pull --filter ORDERS.processed --ack none --replay instant --deliver 10
nats consumer next ORDERS TEN
```

```
--- received on ORDERS.processed
order 10

Acknowledged message
```

And finally a time-based Consumer. Let's add some messages a minute apart:

```shell
nats stream purge ORDERS
for i in 1 2 3
do
  nats pub ORDERS.processed "order ${i}"
  sleep 60
done
```

Then create a Consumer that starts 2 minutes ago:

```shell
nats consumer add ORDERS 2MIN --pull --filter ORDERS.processed --ack none --replay instant --deliver 2m
nats consumer next ORDERS 2MIN
```

```
--- received on ORDERS.processed
order 2

Acknowledged message
```

## Ephemeral Consumers

So far, all the Consumers you have seen were Durable, meaning they exist even after you disconnect from JetStream. In our Orders scenario, though the `MONITOR` a Consumer could very well be a short-lived thing there just while an operator is debugging the system, there is no need to remember the last seen position if all you are doing is wanting to observe the real-time state.

In this case, we can make an Ephemeral Consumer by first subscribing to the delivery subject, then creating a durable and giving it no durable name. An Ephemeral Consumer exists as long as any subscription is active on its delivery subject. It is automatically be removed, after a short grace period to handle restarts, when there are no subscribers.

Terminal 1:

```shell
nats sub my.monitor
```

Terminal 2:

```shell
nats consumer add ORDERS --filter '' --ack none --target 'my.monitor' --deliver last --replay instant --ephemeral
```

The `--ephemeral` switch tells the system to make an Ephemeral Consumer.

## Consumer Message Rates

Typically, what you want is if a new Consumer is made the selected messages are delivered to you as quickly as possible. You might want to replay messages at the rate they arrived though, meaning if messages first arrived 1 minute apart, and you make a new Consumer it will get the messages a minute apart.

This is useful in load testing scenarios etc. This is called the `ReplayPolicy` and have values of `ReplayInstant` and `ReplayOriginal`.

You can only set `ReplayPolicy` on push-based Consumers.

```shell
nats consumer add ORDERS REPLAY --target out.original --filter ORDERS.processed --ack none --deliver all --sample 100 --replay original
```

```
...
     Replay Policy: original
...
```

Now let's publish messages into the Set 10 seconds apart:

```shell
for i in 1 2 3                                                                                                                                                      <15:15:35
do
  nats pub ORDERS.processed "order ${i}"
  sleep 10
done
```

```
Published [ORDERS.processed] : 'order 1'
Published [ORDERS.processed] : 'order 2'
Published [ORDERS.processed] : 'order 3'
```

And when we consume them they will come to us 10 seconds apart:

```shell
nats sub -t out.original
```

```
Listening on [out.original]
2020/01/03 15:17:26 [#1] Received on [ORDERS.processed]: 'order 1'
2020/01/03 15:17:36 [#2] Received on [ORDERS.processed]: 'order 2'
2020/01/03 15:17:46 [#3] Received on [ORDERS.processed]: 'order 3'
^C
```

## Ack Sampling

In the earlier sections we saw that samples are being sent to a monitoring system. Let's look at that in depth; how the monitoring system works and what it contains.

As messages pass through a Consumer you'd be interested in knowing how many are being redelivered and how many times but also how long it takes for messages to be acknowledged.

Consumers can sample Ack'ed messages for you and publish samples so your monitoring system can observe the health of a Consumer. We will add support for this to [NATS Surveyor](https://github.com/nats-io/nats-surveyor).

### Configuration

You can configure a Consumer for sampling bypassing the `--sample 80` option to `nats consumer add`, this tells the system to sample 80% of Acknowledgements.

When viewing info of a Consumer you can tell if it's sampled or not:

```shell
nats consumer info ORDERS NEW
```

Output contains

```
...
     Sampling Rate: 100
...
```

## Storage Overhead

JetStream file storage is very efficient, storing as little extra information about the message as possible.

We do store some message data with each message, namely:

* Message headers
* The subject it was received on
* The time it was received
* The message payload
* A hash of the message
* The message sequence
* A few other bits like the length of the subject and the length of headers

Without any headers the size is:

```
length of the message record (4bytes) + seq(8) + ts(8) + subj_len(2) + subj + msg + hash(8)
```

A 5 byte `hello` message without headers will take 39 bytes.

With headers:

```
length of the message record (4bytes) + seq(8) + ts(8) + subj_len(2) + subj + hdr_len(4) + hdr + msg + hash(8)
```

So if you are publishing many small messages the overhead will be, relatively speaking, quite large, but for larger messages the overhead is very small. If you publish many small messages it's worth trying to optimize the subject length.


# Managing Streams and consumers

Streams and durable consumers can be defined administratively outside the application (typically using the NATS CLI Tool) in which case the application only needs to know about the well-known names of the durable consumers it wants to use. But you can also manage streams and consumers programmatically.

Common stream management operations are:

* Add a stream. Adding a stream is an idempotent function, which means that if a stream does not exist, it will be created, and if a stream already exists, then the add operation will succeed only if the existing stream matches exactly the attributes specified in the 'add' call.
* Delete a stream.
* Purge a stream (delete all the messages stored in the stream)
* Get or remove a specific message from a stream by sequence number
* Add or update (or delete) a consumer
* Get info and statistics on streams/consumers/account. Get/remove/get information on individual messages stored in a stream.

{% tabs %}
{% tab title="Go" %}

```go
func ExampleJetStreamManager() {
	nc, _ := nats.Connect("localhost")

	js, _ := nc.JetStream()

	// Create a stream
	js.AddStream(&nats.StreamConfig{
		Name:     "example-stream",
		Subjects: []string{"example-subject"},
		MaxBytes: 1024,
	})

	// Update a stream
	js.UpdateStream(&nats.StreamConfig{
		Name:     "example-stream",
		MaxBytes: 2048,
	})

	// Create a durable consumer
	js.AddConsumer("example-stream", &nats.ConsumerConfig{
		Durable: "example-consumer-name",
	})

	// Get information about all streams (with Context JSOpt)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	for info := range js.StreamsInfo(nats.Context(ctx)) {
		fmt.Println("stream name: ", info.Config.Name)
	}

	// Get information about all consumers (with MaxWait JSOpt)
	for info := range js.ConsumersInfo("example-stream", nats.MaxWait(10*time.Second)) {
		fmt.Println("consumer name: ", info.Name)
	}

	// Delete a consumer
	js.DeleteConsumer("example-stream", "example-consumer-name")

	// Delete a stream
	js.DeleteStream("example-stream")
}
```

{% endtab %}

{% tab title="Java" %}

```java
try (Connection nc = Nats.connect("localhost")) {
    JetStreamManagement jsm = nc.jetStreamManagement();

    // Create a stream
    StreamInfo si = jsm.addStream(StreamConfiguration.builder()
        .name("example-stream")
        .subjects("example-subject")
        .maxBytes(1024)
        .build());
    StreamConfiguration config = si.getConfiguration();
    System.out.println("stream name: " + config.getName() + ", max_bytes: " + config.getMaxBytes());

    // Update a stream
    si = jsm.updateStream(StreamConfiguration.builder()
        .name("example-stream")
        .maxBytes(2048)
        .build());
    config = si.getConfiguration();
    System.out.println("stream name: " + config.getName() + ", max_bytes: " + config.getMaxBytes());

    // Create a durable consumer
    jsm.createConsumer("example-stream", ConsumerConfiguration.builder()
        .durable("example-consumer-name")
        .build());

    // Get information about all streams
    List<StreamInfo> streams = jsm.getStreams();
    for (StreamInfo info : streams) {
        System.out.println("stream name: " + info.getConfiguration().getName());
    }

    // Get information about all consumers
    List<ConsumerInfo> consumers = jsm.getConsumers("example-stream");
    for (ConsumerInfo ci : consumers) {
        System.out.println("consumer name: " + ci.getName());
    }

    // Delete a consumer
    jsm.deleteConsumer("example-stream", "example-consumer-name");

    // Delete a stream
    jsm.deleteStream("example-stream");
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
import { AckPolicy, connect, Empty } from "../../src/mod.ts";

const nc = await connect();
const jsm = await nc.jetstreamManager();

// list all the streams, the `next()` function
// retrieves a paged result.
const streams = await jsm.streams.list().next();
streams.forEach((si) => {
    console.log(si);
});

// add a stream
const stream = "mystream";
const subj = `mystream.*`;
await jsm.streams.add({ name: stream, subjects: [subj] });

// publish a reg nats message directly to the stream
for (let i = 0; i < 10; i++) {
    nc.publish(`${subj}.a`, Empty);
}

// find a stream that stores a specific subject:
const name = await jsm.streams.find("mystream.A");

// retrieve info about the stream by its name
const si = await jsm.streams.info(name);

// update a stream configuration
si.config.subjects?.push("a.b");
await jsm.streams.update(name, si.config);

// get a particular stored message in the stream by sequence
// this is not associated with a consumer
const sm = await jsm.streams.getMessage(stream, { seq: 1 });
console.log(sm.seq);

// delete the 5th message in the stream, securely erasing it
await jsm.streams.deleteMessage(stream, 5);

// purge all messages in the stream, the stream itself
// remains.
await jsm.streams.purge(stream);

// purge all messages with a specific subject (filter can be a wildcard)
await jsm.streams.purge(stream, { filter: "a.b" });

// purge messages with a specific subject keeping some messages
await jsm.streams.purge(stream, { filter: "a.c", keep: 5 });

// purge all messages with upto (not including seq)
await jsm.streams.purge(stream, { seq: 100 });

// purge all messages with upto sequence that have a matching subject
await jsm.streams.purge(stream, { filter: "a.d", seq: 100 });

// list all consumers for a stream:
const consumers = await jsm.consumers.list(stream).next();
consumers.forEach((ci) => {
    console.log(ci);
});

// add a new durable pull consumer
await jsm.consumers.add(stream, {
    durable_name: "me",
    ack_policy: AckPolicy.Explicit,
});

// retrieve a consumer's configuration
const ci = await jsm.consumers.info(stream, "me");
console.log(ci);

// delete a particular consumer
await jsm.consumers.delete(stream, "me");
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio

import nats
from nats.errors import TimeoutError
    
async def main():
    nc = await nats.connect("localhost")

    # Create JetStream context.
    js = nc.jetstream()
        
    # Persist messages on 'foo's subject.
    await js.add_stream(name="sample-stream", subjects=["foo"])

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())    
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.JetStream;
using NATS.Client.JetStream.Models;

await using var client = new NatsClient();

INatsJSContext js = client.CreateJetStreamContext();

// Create a stream
var streamConfig = new StreamConfig(name: "example-stream", subjects: ["example-subject"])
{
    MaxBytes = 1024,
};
await js.CreateStreamAsync(streamConfig);

// Update the stream
var streamConfigUpdated = streamConfig with { MaxBytes = 2048 };
await js.UpdateStreamAsync(streamConfigUpdated);

// Create a durable consumer
await js.CreateConsumerAsync("example-stream", new ConsumerConfig("example-consumer-name"));

// Get information about all streams
await foreach (var stream in js.ListStreamsAsync())
{
    Console.WriteLine($"stream name: {stream.Info.Config.Name}");
}

// Get information about all consumers in a stream
await foreach (var consumer in js.ListConsumersAsync("example-stream"))
{
    Console.WriteLine($"consumer name: {consumer.Info.Config.Name}");
}

// Delete a consumer
await js.DeleteConsumerAsync("example-stream", "example-consumer-name");

// Delete a stream
await js.DeleteStreamAsync("example-stream");

// Output:
// stream name: example-stream
// consumer name: example-consumer-name
```

{% endtab %}

{% tab title="C" %}

```c
#include "examples.h"

static const char *usage = ""\
"-stream        stream name (default is 'foo')\n" \
"-txt           text to send (default is 'hello')\n" \
"-count         number of messages to send\n" \
"-sync          publish synchronously (default is async)\n";

static void
_jsPubErr(jsCtx *js, jsPubAckErr *pae, void *closure)
{
    int *errors = (int*) closure;

    printf("Error: %u - Code: %u - Text: %s\n", pae->Err, pae->ErrCode, pae->ErrText);
    printf("Original message: %.*s\n", natsMsg_GetDataLength(pae->Msg), natsMsg_GetData(pae->Msg));

    *errors = (*errors + 1);

    // If we wanted to resend the original message, we would do something like that:
    //
    // js_PublishMsgAsync(js, &(pae->Msg), NULL);
    //
    // Note that we use `&(pae->Msg)` so that the library set it to NULL if it takes
    // ownership, and the library will not destroy the message when this callback returns.

    // No need to destroy anything, everything is handled by the library.
}

int main(int argc, char **argv)
{
    natsConnection      *conn  = NULL;
    natsStatistics      *stats = NULL;
    natsOptions         *opts  = NULL;
    jsCtx               *js    = NULL;
    jsOptions           jsOpts;
    jsErrCode           jerr   = 0;
    natsStatus          s;
    int                 dataLen=0;
    volatile int        errors = 0;
    bool                delStream = false;

    opts = parseArgs(argc, argv, usage);
    dataLen = (int) strlen(payload);

    s = natsConnection_Connect(&conn, opts);

    if (s == NATS_OK)
        s = jsOptions_Init(&jsOpts);

    if (s == NATS_OK)
    {
        if (async)
        {
            jsOpts.PublishAsync.ErrHandler           = _jsPubErr;
            jsOpts.PublishAsync.ErrHandlerClosure    = (void*) &errors;
        }
        s = natsConnection_JetStream(&js, conn, &jsOpts);
    }

    if (s == NATS_OK)
    {
        jsStreamInfo    *si = NULL;

        // First check if the stream already exists.
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_NOT_FOUND)
        {
            jsStreamConfig  cfg;

            // Since we are the one creating this stream, we can delete at the end.
            delStream = true;

            // Initialize the configuration structure.
            jsStreamConfig_Init(&cfg);
            cfg.Name = stream;
            // Set the subject
            cfg.Subjects = (const char*[1]){subj};
            cfg.SubjectsLen = 1;
            // Make it a memory stream.
            cfg.Storage = js_MemoryStorage;
            // Add the stream,
            s = js_AddStream(&si, js, &cfg, NULL, &jerr);
        }
        if (s == NATS_OK)
        {
            printf("Stream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            // Need to destroy the returned stream object.
            jsStreamInfo_Destroy(si);
        }
    }

    if (s == NATS_OK)
        s = natsStatistics_Create(&stats);

    if (s == NATS_OK)
    {
        printf("\nSending %" PRId64 " messages to subject '%s'\n", total, stream);
        start = nats_Now();
    }

    for (count = 0; (s == NATS_OK) && (count < total); count++)
    {
        if (async)
            s = js_PublishAsync(js, subj, (const void*) payload, dataLen, NULL);
        else
        {
            jsPubAck *pa = NULL;

            s = js_Publish(&pa, js, subj, (const void*) payload, dataLen, NULL, &jerr);
            if (s == NATS_OK)
            {
                if (pa->Duplicate)
                    printf("Got a duplicate message! Sequence=%" PRIu64 "\n", pa->Sequence);

                jsPubAck_Destroy(pa);
            }
        }
    }

    if ((s == NATS_OK) && async)
    {
        jsPubOptions    jsPubOpts;

        jsPubOptions_Init(&jsPubOpts);
        // Let's set it to 30 seconds, if getting "Timeout" errors,
        // this may need to be increased based on the number of messages
        // being sent.
        jsPubOpts.MaxWait = 30000;
        s = js_PublishAsyncComplete(js, &jsPubOpts);
        if (s == NATS_TIMEOUT)
        {
            // Let's get the list of pending messages. We could resend,
            // etc, but for now, just destroy them.
            natsMsgList list;

            js_PublishAsyncGetPendingList(&list, js);
            natsMsgList_Destroy(&list);
        }
    }

    if (s == NATS_OK)
    {
        jsStreamInfo *si = NULL;

        elapsed = nats_Now() - start;
        printStats(STATS_OUT, conn, NULL, stats);
        printPerf("Sent");

        if (errors != 0)
            printf("There were %d asynchronous errors\n", errors);

        // Let's report some stats after the run
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_OK)
        {
            printf("\nStream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            jsStreamInfo_Destroy(si);
        }
    }
    if (delStream && (js != NULL))
    {
        printf("\nDeleting stream %s: ", stream);
        s = js_DeleteStream(js, stream, NULL, &jerr);
        if (s == NATS_OK)
            printf("OK!");
        printf("\n");
    }
    if (s != NATS_OK)
    {
        printf("Error: %u - %s - jerr=%u\n", s, natsStatus_GetText(s), jerr);
        nats_PrintLastErrorStack(stderr);
    }

    // Destroy all our objects to avoid report of memory leak
    jsCtx_Destroy(js);
    natsStatistics_Destroy(stats);
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

    // To silence reports of memory still in used with valgrind
    nats_Close();

    return 0;
}
```

{% endtab %}
{% endtabs %}


# Consumer Details

Consumers are how client applications get the messages stored in the streams. You can have many consumers on a single stream. Consumers are like a view on a stream, can filter messages and have some state (maintained by the servers) associated with them.

Consumers can be 'durable' or 'ephemeral'.

## Durable versus ephemeral consumers

Durable consumer persist message delivery progress on the server side. A durable consumer can be retrieved by name and shared between client instance for load balancing. It can be made highly available through replicas.

An ephemeral consumer does not persist delivery progress and will automatically be deleted when there are no more client instances connected.

### Durable consumers

Durable consumers are meant to be used by multiple instances of an application, either to distribute and scale out the processing, or to persist the position of the consumer over the stream between runs of an application.

Durable consumers as the name implies are meant to last 'forever' and are typically created and deleted administratively rather than by the application code which only needs to specify the durable's well known name to use it.

You create a durable consumer using the `nats consumer add` CLI tool command, or programmatically by passing a durable name option to the subscription creation call.

### Ephemeral consumers

Ephemeral consumers are meant to be used by a single instance of an application (e.g. to get its own replay of the messages in the stream).

Ephemeral consumers are not meant to last 'forever', they are defined automatically at subscription time by the client library and disappear after the application disconnect.

You (automatically) create an ephemeral consumer when you call the js.Subscribe function without specifying the Durable or Bind subscription options. Calling Drain on that subscription automatically deletes the underlying ephemeral consumer. You can also explicitly create an ephemeral consumer by not passing a durable name option to the jsm.AddConsumer call.

Ephemeral consumers otherwise have the same control over message acknowledged and re-delivery as durable consumers.

## Push and Pull consumers

Clients implement two implementations of consumers identified as 'push' or 'pull'.

### Push consumers

Push consumers receive messages on a specific subject where message flow is controlled by the server. Load balancing is supported through NATS core queue groups. The messages from the stream are distributed automatically between the subscribing clients to the push consumers.

### Pull consumers

Pull consumers request messages explicitly from the server in batches, giving the client full control over dispatching, flow control, pending (unacknowledged) messages and load balancing. Pull consuming client make `fetch()` calls in a dispatch loop.

{% hint style="info" %}
We recommend using pull consumers for new projects. In particular when scalability, detailed flow control or error handling are a design focus. Most client API have been updated to provide convenient interfaces for consuming messages through callback handler or iterators without the need to manage message retrieval.
{% endhint %}

`fetch()` calls can be immediate or have a defined timeout, allowing for either controlled (1 by 1) consumption or `realtime` delivery with minimal polling overhead.

Pull consumers create less CPU load on the NATS servers and therefore scale better (note that the push consumers are still quite fast and scalable, you may only notice the difference between the two if you have sustained high message rates).

#### Pull

{% tabs %}
{% tab title="Go" %}

```go
func ExampleJetStream() {
    nc, err := nats.Connect("localhost")
    if err != nil {
        log.Fatal(err)
    }

	// Use the JetStream context to produce and consumer messages
	// that have been persisted.
	js, err := nc.JetStream(nats.PublishAsyncMaxPending(256))
	if err != nil {
		log.Fatal(err)
	}

	js.AddStream(&nats.StreamConfig{
		Name:     "FOO",
		Subjects: []string{"foo"},
	})

	js.Publish("foo", []byte("Hello JS!"))

	// Publish messages asynchronously.
	for i := 0; i < 500; i++ {
		js.PublishAsync("foo", []byte("Hello JS Async!"))
	}
	select {
	case <-js.PublishAsyncComplete():
	case <-time.After(5 * time.Second):
		fmt.Println("Did not resolve in time")
	}

	// Create Pull based consumer with maximum 128 inflight.
	sub, _ := js.PullSubscribe("foo", "wq", nats.PullMaxWaiting(128))

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	for {
		select {
		case <-ctx.Done():
			return
		default:
		}

        // Fetch will return as soon as any message is available rather than wait until the full batch size is available, using a batch size of more than 1 allows for higher throughput when needed.
		msgs, _ := sub.Fetch(10, nats.Context(ctx))
		for _, msg := range msgs {
			msg.Ack()
		}
	}
}
```

{% endtab %}

{% tab title="Java" %}

```java
package io.nats.examples.jetstream.simple;

import io.nats.client.*;
import io.nats.client.api.ConsumerConfiguration;
import io.nats.examples.jetstream.ResilientPublisher;
import java.io.IOException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.atomic.AtomicInteger;
import static io.nats.examples.jetstream.NatsJsUtils.createOrReplaceStream;

/**
* This example will demonstrate simplified consume with a handler
*/
public class MessageConsumerExample {
 private static final String STREAM = "consume-stream";
 private static final String SUBJECT = "consume-subject";
 private static final String CONSUMER_NAME = "consume-consumer";
 private static final String MESSAGE_PREFIX = "consume";
 private static final int STOP_COUNT = 500;
 private static final int REPORT_EVERY = 100;
 private static final String SERVER = "nats://localhost:4222";

 public static void main(String[] args) {
     Options options = Options.builder().server(SERVER).build();
     try (Connection nc = Nats.connect(options)) {
         JetStreamManagement jsm = nc.jetStreamManagement();
         createOrReplaceStream(jsm, STREAM, SUBJECT);

         //Utility for filling the stream with some messages
         System.out.println("Starting publish...");
         ResilientPublisher publisher = new ResilientPublisher(nc, jsm, STREAM, SUBJECT).basicDataPrefix(MESSAGE_PREFIX).jitter(10);
         Thread pubThread = new Thread(publisher);
         pubThread.start();

         // get stream context, create consumer and get the consumer context
         StreamContext streamContext;
         ConsumerContext consumerContext;
         CountDownLatch latch = new CountDownLatch(1);
         AtomicInteger atomicCount = new AtomicInteger();
         long start = System.nanoTime();

         streamContext = nc.getStreamContext(STREAM);
         streamContext.createOrUpdateConsumer(ConsumerConfiguration.builder().durable(CONSUMER_NAME).build());
         consumerContext = streamContext.getConsumerContext(CONSUMER_NAME);

         MessageHandler handler = msg -> {
             msg.ack();
             int count = atomicCount.incrementAndGet();
             if (count % REPORT_EVERY == 0) {
            	 System.out.println("Handler" + ": Received " + count + " messages in " + (System.nanoTime() - start) / 1_000_000 + "ms.");
             }
             if (count == STOP_COUNT) {
                 latch.countDown();
             }
         };

     	 // create the consumer and install handler
     	 MessageConsumer consumer = consumerContext.consume(handler);
     	 //Waiting for the handler signalling us to stop
         latch.await();
         // When stop is called, no more pull requests will be made, but messages already requested
         // will still come across the wire to the client.
         System.out.println("Stopping the consumer...");
         consumer.stop();
         // wait until the consumer is finished processing backlog
         while (!consumer.isFinished()) {
             Thread.sleep(10);
         }
         System.out.println("Final" + ": Received " + atomicCount.get() + " messages in " + (System.nanoTime() - start) / 1_000_000 + "ms.");

         publisher.stop(); // otherwise the ConsumerContext background thread will complain when the connection goes away
         pubThread.join();
     }
     catch (JetStreamApiException | IOException e) {
         // JetStreamApiException:
         //      1. the stream or consumer did not exist
         //      2. api calls under the covers theoretically this could fail, but practically it won't.
         // IOException:
         //      likely a connection problem
         System.err.println("Exception should not handled, exiting.");
         System.exit(-1);
     }
     catch (Exception e) {
         System.err.println("Exception should not handled, exiting.");
         System.exit(-1);
     }
 }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
import { AckPolicy, connect, nanos } from "../../src/mod.ts";
import { nuid } from "../../nats-base-client/nuid.ts";

const nc = await connect();

const stream = nuid.next();
const subj = nuid.next();
const durable = nuid.next();

const jsm = await nc.jetstreamManager();
await jsm.streams.add({ name: stream, subjects: [subj] });

const js = nc.jetstream();
await js.publish(subj);
await js.publish(subj);
await js.publish(subj);
await js.publish(subj);

const psub = await js.pullSubscribe(subj, {
  mack: true,
  // artificially low ack_wait, to show some messages
  // not getting acked being redelivered
  config: {
    durable_name: durable,
    ack_policy: AckPolicy.Explicit,
    ack_wait: nanos(4000),
  },
});

(async () => {
  for await (const m of psub) {
    console.log(
      `[${m.seq}] ${
        m.redelivered ? `- redelivery ${m.info.redeliveryCount}` : ""
      }`
    );
    if (m.seq % 2 === 0) {
      m.ack();
    }
  }
})();

const fn = () => {
  console.log("[PULL]");
  psub.pull({ batch: 1000, expires: 10000 });
};

// do the initial pull
fn();
// and now schedule a pull every so often
const interval = setInterval(fn, 10000); // and repeat every 2s

setTimeout(() => {
  clearInterval(interval);
  nc.drain();
}, 20000);
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio

import nats
from nats.errors import TimeoutError

async def main():
    nc = await nats.connect("localhost")

    # Create JetStream context.
    js = nc.jetstream()

    # Persist messages on 'foo's subject.
    await js.add_stream(name="sample-stream", subjects=["foo"])

    for i in range(0, 10):
        ack = await js.publish("foo", f"hello world: {i}".encode())
        print(ack)

    # Create pull based consumer on 'foo'.
    psub = await js.pull_subscribe("foo", "psub")

    # Fetch and ack messagess from consumer.
    for i in range(0, 10):
        msgs = await psub.fetch(1)
        for msg in msgs:
            print(msg)

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.JetStream;
using NATS.Client.JetStream.Models;

await using var client = new NatsClient();

INatsJSContext js = client.CreateJetStreamContext();

// Create a stream
var streamConfig = new StreamConfig(name: "FOO", subjects: ["foo"]);
await js.CreateStreamAsync(streamConfig);

// Publish a message
{
    PubAckResponse ack = await js.PublishAsync("foo", "Hello, JetStream!");
    ack.EnsureSuccess();
}

// Publish messages concurrently
List<NatsJSPublishConcurrentFuture> futures = new();
for (var i = 0; i < 500; i++)
{
    NatsJSPublishConcurrentFuture future
        = await js.PublishConcurrentAsync("foo", "Hello, JetStream 1!");
    futures.Add(future);
}

foreach (var future in futures)
{
    await using (future)
    {
        PubAckResponse ack = await future.GetResponseAsync();
        ack.EnsureSuccess();
    }
}


// Create a consumer with a maximum 128 inflight messages
INatsJSConsumer consumer = await js.CreateConsumerAsync("FOO", new ConsumerConfig(name: "foo")
{
    MaxWaiting = 128,
});

using CancellationTokenSource cts = new(TimeSpan.FromSeconds(10));

while (cts.IsCancellationRequested == false)
{
    var opts = new NatsJSFetchOpts { MaxMsgs = 10 };
    await foreach (NatsJSMsg<string> msg in consumer.FetchAsync<string>(opts, cancellationToken: cts.Token))
    {
        await msg.AckAsync(cancellationToken: cts.Token);
    }
}
```

{% endtab %}

{% tab title="C" %}

```c
#include "examples.h"

static const char *usage = ""\
"-gd            use global message delivery thread pool\n" \
"-sync          receive synchronously (default is asynchronous)\n" \
"-pull          use pull subscription\n" \
"-fc            enable flow control\n" \
"-count         number of expected messages\n";

static void
onMsg(natsConnection *nc, natsSubscription *sub, natsMsg *msg, void *closure)
{
    if (print)
        printf("Received msg: %s - %.*s\n",
               natsMsg_GetSubject(msg),
               natsMsg_GetDataLength(msg),
               natsMsg_GetData(msg));

    if (start == 0)
        start = nats_Now();

    // We should be using a mutex to protect those variables since
    // they are used from the subscription's delivery and the main
    // threads. For demo purposes, this is fine.
    if (++count == total)
        elapsed = nats_Now() - start;

    // Since this is auto-ack callback, we don't need to ack here.
    natsMsg_Destroy(msg);
}

static void
asyncCb(natsConnection *nc, natsSubscription *sub, natsStatus err, void *closure)
{
    printf("Async error: %u - %s\n", err, natsStatus_GetText(err));

    natsSubscription_GetDropped(sub, (int64_t*) &dropped);
}

int main(int argc, char **argv)
{
    natsConnection      *conn  = NULL;
    natsStatistics      *stats = NULL;
    natsOptions         *opts  = NULL;
    natsSubscription    *sub   = NULL;
    natsMsg             *msg   = NULL;
    jsCtx               *js    = NULL;
    jsErrCode           jerr   = 0;
    jsOptions           jsOpts;
    jsSubOptions        so;
    natsStatus          s;
    bool                delStream = false;

    opts = parseArgs(argc, argv, usage);

    printf("Created %s subscription on '%s'.\n",
        (pull ? "pull" : (async ? "asynchronous" : "synchronous")), subj);

    s = natsOptions_SetErrorHandler(opts, asyncCb, NULL);

    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);

    if (s == NATS_OK)
        s = jsOptions_Init(&jsOpts);

    if (s == NATS_OK)
        s = jsSubOptions_Init(&so);
    if (s == NATS_OK)
    {
        so.Stream = stream;
        so.Consumer = durable;
        if (flowctrl)
        {
            so.Config.FlowControl = true;
            so.Config.Heartbeat = (int64_t)1E9;
        }
    }

    if (s == NATS_OK)
        s = natsConnection_JetStream(&js, conn, &jsOpts);

    if (s == NATS_OK)
    {
        jsStreamInfo    *si = NULL;

        // First check if the stream already exists.
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_NOT_FOUND)
        {
            jsStreamConfig  cfg;

            // Since we are the one creating this stream, we can delete at the end.
            delStream = true;

            // Initialize the configuration structure.
            jsStreamConfig_Init(&cfg);
            cfg.Name = stream;
            // Set the subject
            cfg.Subjects = (const char*[1]){subj};
            cfg.SubjectsLen = 1;
            // Make it a memory stream.
            cfg.Storage = js_MemoryStorage;
            // Add the stream,
            s = js_AddStream(&si, js, &cfg, NULL, &jerr);
        }
        if (s == NATS_OK)
        {
            printf("Stream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            // Need to destroy the returned stream object.
            jsStreamInfo_Destroy(si);
        }
    }

    if (s == NATS_OK)
    {
        if (pull)
            s = js_PullSubscribe(&sub, js, subj, durable, &jsOpts, &so, &jerr);
        else if (async)
            s = js_Subscribe(&sub, js, subj, onMsg, NULL, &jsOpts, &so, &jerr);
        else
            s = js_SubscribeSync(&sub, js, subj, &jsOpts, &so, &jerr);
    }
    if (s == NATS_OK)
        s = natsSubscription_SetPendingLimits(sub, -1, -1);

    if (s == NATS_OK)
        s = natsStatistics_Create(&stats);

    if ((s == NATS_OK) && pull)
    {
        natsMsgList list;
        int         i;

        for (count = 0; (s == NATS_OK) && (count < total); )
        {
            s = natsSubscription_Fetch(&list, sub, 1024, 5000, &jerr);
            if (s != NATS_OK)
                break;

            if (start == 0)
                start = nats_Now();

            count += (int64_t) list.Count;
            for (i=0; (s == NATS_OK) && (i<list.Count); i++)
                s = natsMsg_Ack(list.Msgs[i], &jsOpts);

            natsMsgList_Destroy(&list);
        }
    }
    else if ((s == NATS_OK) && async)
    {
        while (s == NATS_OK)
        {
            if (count + dropped == total)
                break;

            nats_Sleep(1000);
        }
    }
    else if (s == NATS_OK)
    {
        for (count = 0; (s == NATS_OK) && (count < total); count++)
        {
            s = natsSubscription_NextMsg(&msg, sub, 5000);
            if (s != NATS_OK)
                break;

            if (start == 0)
                start = nats_Now();

            s = natsMsg_Ack(msg, &jsOpts);
            natsMsg_Destroy(msg);
        }
    }

    if (s == NATS_OK)
    {
        printStats(STATS_IN|STATS_COUNT, conn, sub, stats);
        printPerf("Received");
    }
    if (s == NATS_OK)
    {
        jsStreamInfo *si = NULL;

        // Let's report some stats after the run
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_OK)
        {
            printf("\nStream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            jsStreamInfo_Destroy(si);
        }
        if (delStream)
        {
            printf("\nDeleting stream %s: ", stream);
            s = js_DeleteStream(js, stream, NULL, &jerr);
            if (s == NATS_OK)
                printf("OK!");
            printf("\n");
        }
    }
    else
    {
        printf("Error: %u - %s - jerr=%u\n", s, natsStatus_GetText(s), jerr);
        nats_PrintLastErrorStack(stderr);
    }

    // Destroy all our objects to avoid report of memory leak
    jsCtx_Destroy(js);
    natsStatistics_Destroy(stats);
    natsSubscription_Destroy(sub);
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

    // To silence reports of memory still in used with valgrind
    nats_Close();

    return 0;
}
```

{% endtab %}
{% endtabs %}

A push consumer can also be used in some other use cases such as without a queue group, or with no acknowledgement or cumulative acknowledgements.

#### Push

{% tabs %}
{% tab title="Go" %}

```go
func ExampleJetStream() {
	nc, err := nats.Connect("localhost")
	if err != nil {
		log.Fatal(err)
	}

	// Use the JetStream context to produce and consumer messages
	// that have been persisted.
	js, err := nc.JetStream(nats.PublishAsyncMaxPending(256))
	if err != nil {
		log.Fatal(err)
	}

	js.AddStream(&nats.StreamConfig{
		Name:     "FOO",
		Subjects: []string{"foo"},
	})

	js.Publish("foo", []byte("Hello JS!"))

	// Publish messages asynchronously.
	for i := 0; i < 500; i++ {
		js.PublishAsync("foo", []byte("Hello JS Async!"))
	}
	select {
	case <-js.PublishAsyncComplete():
	case <-time.After(5 * time.Second):
		fmt.Println("Did not resolve in time")
	}

	// Create async consumer on subject 'foo'. Async subscribers
	// ack a message once exiting the callback.
	js.Subscribe("foo", func(msg *nats.Msg) {
		meta, _ := msg.Metadata()
		fmt.Printf("Stream Sequence  : %v\n", meta.Sequence.Stream)
		fmt.Printf("Consumer Sequence: %v\n", meta.Sequence.Consumer)
	})

	// Async subscriber with manual acks.
	js.Subscribe("foo", func(msg *nats.Msg) {
		msg.Ack()
	}, nats.ManualAck())

	// Async queue subscription where members load balance the
	// received messages together.
	// If no consumer name is specified, either with nats.Bind()
	// or nats.Durable() options, the queue name is used as the
	// durable name (that is, as if you were passing the
	// nats.Durable(<queue group name>) option.
	// It is recommended to use nats.Bind() or nats.Durable()
	// and preferably create the JetStream consumer beforehand
	// (using js.AddConsumer) so that the JS consumer is not
	// deleted on an Unsubscribe() or Drain() when the member
	// that created the consumer goes away first.
	// Check Godoc for the QueueSubscribe() API for more details.
	js.QueueSubscribe("foo", "group", func(msg *nats.Msg) {
		msg.Ack()
	}, nats.ManualAck())

	// Subscriber to consume messages synchronously.
	sub, _ := js.SubscribeSync("foo")
	msg, _ := sub.NextMsg(2 * time.Second)
	msg.Ack()

	// We can add a member to the group, with this member using
	// the synchronous version of the QueueSubscribe.
	sub, _ = js.QueueSubscribeSync("foo", "group")
	msg, _ = sub.NextMsg(2 * time.Second)
	msg.Ack()

	// ChanSubscribe
	msgCh := make(chan *nats.Msg, 8192)
	sub, _ = js.ChanSubscribe("foo", msgCh)

	select {
	case msg := <-msgCh:
		fmt.Println("[Received]", msg)
	case <-time.After(1 * time.Second):
	}
}
```

{% endtab %}

{% tab title="Java" %}

```java
package io.nats.examples.jetstream;

import io.nats.client.*;
import io.nats.client.api.PublishAck;
import io.nats.examples.ExampleArgs;
import io.nats.examples.ExampleUtils;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

import static io.nats.examples.jetstream.NatsJsUtils.createStreamExitWhenExists;

/**
 * This example will demonstrate JetStream push subscribing using a durable consumer and a queue
 */
public class NatsJsPushSubQueueDurable {
    static final String usageString =
        "\nUsage: java -cp <classpath> NatsJsPushSubQueueDurable [-s server] [-strm stream] [-sub subject] [-q queue] [-dur durable] [-mcnt msgCount] [-scnt subCount]"
            + "\n\nDefault Values:"
            + "\n   [-strm stream]   qdur-stream"
            + "\n   [-sub subject]   qdur-subject"
            + "\n   [-q queue]       qdur-queue"
            + "\n   [-dur durable]   qdur-durable"
            + "\n   [-mcnt msgCount] 100"
            + "\n   [-scnt subCount] 5"
            + "\n\nUse tls:// or opentls:// to require tls, via the Default SSLContext\n"
            + "\nSet the environment variable NATS_NKEY to use challenge response authentication by setting a file containing your private key.\n"
            + "\nSet the environment variable NATS_CREDS to use JWT/NKey authentication by setting a file containing your user creds.\n"
            + "\nUse the URL in the -s server parameter for user/pass/token authentication.\n";

    public static void main(String[] args) {
        ExampleArgs exArgs = ExampleArgs.builder("Push Subscribe, Durable Consumer, Queue", args, usageString)
                .defaultStream("qdur-stream")
                .defaultSubject("qdur-subject")
                .defaultQueue("qdur-queue")
                .defaultDurable("qdur-durable")
                .defaultMsgCount(100)
                .defaultSubCount(5)
                .build();

        try (Connection nc = Nats.connect(ExampleUtils.createExampleOptions(exArgs.server, true))) {

            // Create a JetStreamManagement context.
            JetStreamManagement jsm = nc.jetStreamManagement();

            // Use the utility to create a stream stored in memory.
            createStreamExitWhenExists(jsm, exArgs.stream, exArgs.subject);

            // Create our JetStream context
            JetStream js = nc.jetStream();

            System.out.println();

            // Setup the subscribers
            // - the PushSubscribeOptions can be re-used since all the subscribers are the same
            // - use a concurrent integer to track all the messages received
            // - have a list of subscribers and threads so I can track them
            PushSubscribeOptions pso = PushSubscribeOptions.builder().durable(exArgs.durable).build();
            AtomicInteger allReceived = new AtomicInteger();
            List<JsQueueSubscriber> subscribers = new ArrayList<>();
            List<Thread> subThreads = new ArrayList<>();
            for (int id = 1; id <= exArgs.subCount; id++) {
                // setup the subscription
                JetStreamSubscription sub = js.subscribe(exArgs.subject, exArgs.queue, pso);
                // create and track the runnable
                JsQueueSubscriber qs = new JsQueueSubscriber(id, exArgs, js, sub, allReceived);
                subscribers.add(qs);
                // create, track and start the thread
                Thread t = new Thread(qs);
                subThreads.add(t);
                t.start();
            }
            nc.flush(Duration.ofSeconds(1)); // flush outgoing communication with/to the server

            // create and start the publishing
            Thread pubThread = new Thread(new JsPublisher(js, exArgs));
            pubThread.start();

            // wait for all threads to finish
            pubThread.join();
            for (Thread t : subThreads) {
                t.join();
            }

            // report
            for (JsQueueSubscriber qs : subscribers) {
                qs.report();
            }

            System.out.println();

            // delete the stream since we are done with it.
            jsm.deleteStream(exArgs.stream);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    static class JsPublisher implements Runnable {
        JetStream js;
        ExampleArgs exArgs;

        public JsPublisher(JetStream js, ExampleArgs exArgs) {
            this.js = js;
            this.exArgs = exArgs;
        }

        @Override
        public void run() {
            for (int x = 1; x <= exArgs.msgCount; x++) {
                try {
                    PublishAck pa = js.publish(exArgs.subject, ("Data # " + x).getBytes(StandardCharsets.US_ASCII));
                } catch (IOException | JetStreamApiException e) {
                    // something pretty wrong here
                    e.printStackTrace();
                    System.exit(-1);
                }
            }
        }
    }

    static class JsQueueSubscriber implements Runnable {
        int id;
        int thisReceived;
        List<String> datas;

        ExampleArgs exArgs;
        JetStream js;
        JetStreamSubscription sub;
        AtomicInteger allReceived;

        public JsQueueSubscriber(int id, ExampleArgs exArgs, JetStream js, JetStreamSubscription sub, AtomicInteger allReceived) {
            this.id = id;
            thisReceived = 0;
            datas = new ArrayList<>();
            this.exArgs = exArgs;
            this.js = js;
            this.sub = sub;
            this.allReceived = allReceived;
        }

        public void report() {
            System.out.printf("Sub # %d handled %d messages.\n", id, thisReceived);
        }

        @Override
        public void run() {
            while (allReceived.get() < exArgs.msgCount) {
                try {
                    Message msg = sub.nextMessage(Duration.ofMillis(500));
                    while (msg != null) {
                        thisReceived++;
                        allReceived.incrementAndGet();
                        String data = new String(msg.getData(), StandardCharsets.US_ASCII);
                        datas.add(data);
                        System.out.printf("QS # %d message # %d %s\n", id, thisReceived, data);
                        msg.ack();

                        msg = sub.nextMessage(Duration.ofMillis(500));
                    }
                } catch (InterruptedException e) {
                    // just try again
                }
            }
            System.out.printf("QS # %d completed.\n", id);
        }
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
import { AckPolicy, connect } from "../../src/mod.ts";
import { nuid } from "../../nats-base-client/nuid.ts";

const nc = await connect();

// create a regular subscription - this is plain nats
const sub = nc.subscribe("my.messages", { max: 5 });
const done = (async () => {
  for await (const m of sub) {
    console.log(m.subject);
    m.respond();
  }
})();

const jsm = await nc.jetstreamManager();
const stream = nuid.next();
const subj = nuid.next();
await jsm.streams.add({ name: stream, subjects: [`${subj}.>`] });

// create a consumer that delivers to the subscription
await jsm.consumers.add(stream, {
  ack_policy: AckPolicy.Explicit,
  deliver_subject: "my.messages",
});

// publish some old nats messages
nc.publish(`${subj}.A`);
nc.publish(`${subj}.B`);
nc.publish(`${subj}.C`);
nc.publish(`${subj}.D.A`);
nc.publish(`${subj}.F.A.B`);

await done;
await nc.close();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio

import nats
from nats.errors import TimeoutError


async def main():
    nc = await nats.connect("localhost")

    # Create JetStream context.
    js = nc.jetstream()

    # Persist messages on 'foo's subject.
    await js.add_stream(name="sample-stream", subjects=["foo"])

    for i in range(0, 10):
        ack = await js.publish("foo", f"hello world: {i}".encode())
        print(ack)

    # Create pull based consumer on 'foo'.
    psub = await js.pull_subscribe("foo", "psub")

    # Fetch and ack messagess from consumer.
    for i in range(0, 10):
        msgs = await psub.fetch(1)
        for msg in msgs:
            print(msg)

    # Create single push based subscriber that is durable across restarts.
    sub = await js.subscribe("foo", durable="myapp")
    msg = await sub.next_msg()
    await msg.ack()

    # Create deliver group that will be have load balanced messages.
    async def qsub_a(msg):
        print("QSUB A:", msg)
        await msg.ack()

    async def qsub_b(msg):
        print("QSUB B:", msg)
        await msg.ack()
    await js.subscribe("foo", "workers", cb=qsub_a)
    await js.subscribe("foo", "workers", cb=qsub_b)

    for i in range(0, 10):
        ack = await js.publish("foo", f"hello world: {i}".encode())
        print("\t", ack)

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
```

{% endtab %}

{% tab title="C#" %}

```csharp
// NATS .NET doesn't publicly support push consumers and treats all consumers
// as just consumers. The mecahnics of the consuming messages are abstracted
// away from the applications and are handled by the library.
```

{% endtab %}

{% tab title="C" %}

```c
#include "examples.h"

static const char *usage = ""\
"-gd            use global message delivery thread pool\n" \
"-sync          receive synchronously (default is asynchronous)\n" \
"-pull          use pull subscription\n" \
"-fc            enable flow control\n" \
"-count         number of expected messages\n";

static void
onMsg(natsConnection *nc, natsSubscription *sub, natsMsg *msg, void *closure)
{
    if (print)
        printf("Received msg: %s - %.*s\n",
               natsMsg_GetSubject(msg),
               natsMsg_GetDataLength(msg),
               natsMsg_GetData(msg));

    if (start == 0)
        start = nats_Now();

    // We should be using a mutex to protect those variables since
    // they are used from the subscription's delivery and the main
    // threads. For demo purposes, this is fine.
    if (++count == total)
        elapsed = nats_Now() - start;

    // Since this is auto-ack callback, we don't need to ack here.
    natsMsg_Destroy(msg);
}

static void
asyncCb(natsConnection *nc, natsSubscription *sub, natsStatus err, void *closure)
{
    printf("Async error: %u - %s\n", err, natsStatus_GetText(err));

    natsSubscription_GetDropped(sub, (int64_t*) &dropped);
}

int main(int argc, char **argv)
{
    natsConnection      *conn  = NULL;
    natsStatistics      *stats = NULL;
    natsOptions         *opts  = NULL;
    natsSubscription    *sub   = NULL;
    natsMsg             *msg   = NULL;
    jsCtx               *js    = NULL;
    jsErrCode           jerr   = 0;
    jsOptions           jsOpts;
    jsSubOptions        so;
    natsStatus          s;
    bool                delStream = false;

    opts = parseArgs(argc, argv, usage);

    printf("Created %s subscription on '%s'.\n",
        (pull ? "pull" : (async ? "asynchronous" : "synchronous")), subj);

    s = natsOptions_SetErrorHandler(opts, asyncCb, NULL);

    if (s == NATS_OK)
        s = natsConnection_Connect(&conn, opts);

    if (s == NATS_OK)
        s = jsOptions_Init(&jsOpts);

    if (s == NATS_OK)
        s = jsSubOptions_Init(&so);
    if (s == NATS_OK)
    {
        so.Stream = stream;
        so.Consumer = durable;
        if (flowctrl)
        {
            so.Config.FlowControl = true;
            so.Config.Heartbeat = (int64_t)1E9;
        }
    }

    if (s == NATS_OK)
        s = natsConnection_JetStream(&js, conn, &jsOpts);

    if (s == NATS_OK)
    {
        jsStreamInfo    *si = NULL;

        // First check if the stream already exists.
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_NOT_FOUND)
        {
            jsStreamConfig  cfg;

            // Since we are the one creating this stream, we can delete at the end.
            delStream = true;

            // Initialize the configuration structure.
            jsStreamConfig_Init(&cfg);
            cfg.Name = stream;
            // Set the subject
            cfg.Subjects = (const char*[1]){subj};
            cfg.SubjectsLen = 1;
            // Make it a memory stream.
            cfg.Storage = js_MemoryStorage;
            // Add the stream,
            s = js_AddStream(&si, js, &cfg, NULL, &jerr);
        }
        if (s == NATS_OK)
        {
            printf("Stream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            // Need to destroy the returned stream object.
            jsStreamInfo_Destroy(si);
        }
    }

    if (s == NATS_OK)
    {
        if (pull)
            s = js_PullSubscribe(&sub, js, subj, durable, &jsOpts, &so, &jerr);
        else if (async)
            s = js_Subscribe(&sub, js, subj, onMsg, NULL, &jsOpts, &so, &jerr);
        else
            s = js_SubscribeSync(&sub, js, subj, &jsOpts, &so, &jerr);
    }
    if (s == NATS_OK)
        s = natsSubscription_SetPendingLimits(sub, -1, -1);

    if (s == NATS_OK)
        s = natsStatistics_Create(&stats);

    if ((s == NATS_OK) && pull)
    {
        natsMsgList list;
        int         i;

        for (count = 0; (s == NATS_OK) && (count < total); )
        {
            s = natsSubscription_Fetch(&list, sub, 1024, 5000, &jerr);
            if (s != NATS_OK)
                break;

            if (start == 0)
                start = nats_Now();

            count += (int64_t) list.Count;
            for (i=0; (s == NATS_OK) && (i<list.Count); i++)
                s = natsMsg_Ack(list.Msgs[i], &jsOpts);

            natsMsgList_Destroy(&list);
        }
    }
    else if ((s == NATS_OK) && async)
    {
        while (s == NATS_OK)
        {
            if (count + dropped == total)
                break;

            nats_Sleep(1000);
        }
    }
    else if (s == NATS_OK)
    {
        for (count = 0; (s == NATS_OK) && (count < total); count++)
        {
            s = natsSubscription_NextMsg(&msg, sub, 5000);
            if (s != NATS_OK)
                break;

            if (start == 0)
                start = nats_Now();

            s = natsMsg_Ack(msg, &jsOpts);
            natsMsg_Destroy(msg);
        }
    }

    if (s == NATS_OK)
    {
        printStats(STATS_IN|STATS_COUNT, conn, sub, stats);
        printPerf("Received");
    }
    if (s == NATS_OK)
    {
        jsStreamInfo *si = NULL;

        // Let's report some stats after the run
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_OK)
        {
            printf("\nStream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            jsStreamInfo_Destroy(si);
        }
        if (delStream)
        {
            printf("\nDeleting stream %s: ", stream);
            s = js_DeleteStream(js, stream, NULL, &jerr);
            if (s == NATS_OK)
                printf("OK!");
            printf("\n");
        }
    }
    else
    {
        printf("Error: %u - %s - jerr=%u\n", s, natsStatus_GetText(s), jerr);
        nats_PrintLastErrorStack(stderr);
    }

    // Destroy all our objects to avoid report of memory leak
    jsCtx_Destroy(js);
    natsStatistics_Destroy(stats);
    natsSubscription_Destroy(sub);
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

    // To silence reports of memory still in used with valgrind
    nats_Close();.

    return 0;
}
```

{% endtab %}
{% endtabs %}

## Ordered Consumers

Ordered consumers are a convenient form of ephemeral push consumer for applications, that want to efficiently consume a stream for data inspection or analysis.

The API consumer is guaranteed delivery of messages in sequence and without gaps.

* Always ephemeral - minimal overhead for the server
* Single threaded in sequence dispatching
* Client checks message sequence and will prevent gaps in the delivery
* Can recover from server node failure and reconnect
* Does not recover from client failure as it is ephemeral

{% tabs %}
{% tab title="Go" %}

```go
func ExampleJetStream() {
	nc, err := nats.Connect("localhost")
	if err != nil {
		log.Fatal(err)
	}

	// Use the JetStream context to produce and consumer messages
	// that have been persisted.
	js, err := nc.JetStream(nats.PublishAsyncMaxPending(256))
	if err != nil {
		log.Fatal(err)
	}

	js.AddStream(&nats.StreamConfig{
		Name:     "FOO",
		Subjects: []string{"foo"},
	})

	js.Publish("foo", []byte("Hello JS!"))

	// ordered push consumer
	js.Subscribe("foo", func(msg *nats.Msg) {
		meta, _ := msg.Metadata()
		fmt.Printf("Stream Sequence  : %v\n", meta.Sequence.Stream)
		fmt.Printf("Consumer Sequence: %v\n", meta.Sequence.Consumer)
	}, nats.OrderedConsumer())
}
```

{% endtab %}

{% tab title="Java" %}

```java
package io.nats.examples.jetstream;

import io.nats.client.*;
import io.nats.client.api.PublishAck;
import io.nats.client.impl.NatsMessage;
import io.nats.examples.ExampleArgs;
import io.nats.examples.ExampleUtils;

import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.temporal.TemporalUnit;

public class myExample {
 public static void main(String[] args) {
  final String subject = "foo";

  try (Connection nc = Nats.connect(ExampleUtils.createExampleOptions("localhost"))) {

   // Create a JetStream context.  This hangs off the original connection
   // allowing us to produce data to streams and consume data from
   // JetStream consumers.
   JetStream js = nc.jetStream();

   // This example assumes there is a stream already created on subject "foo" and some messages already stored in that stream

   // create our message handler.
   MessageHandler handler = msg -> {

    System.out.println("\nMessage Received:");

    if (msg.hasHeaders()) {
     System.out.println("  Headers:");
     for (String key : msg.getHeaders().keySet()) {
      for (String value : msg.getHeaders().get(key)) {
       System.out.printf("    %s: %s\n", key, value);
      }
     }
    }

    System.out.printf("  Subject: %s\n  Data: %s\n",
            msg.getSubject(), new String(msg.getData(), StandardCharsets.UTF_8));
    System.out.println("  " + msg.metaData());
   };

   Dispatcher dispatcher = nc.createDispatcher();
   PushSubscribeOptions pso = PushSubscribeOptions.builder().ordered(true).build();
   JetStreamSubscription sub = js.subscribe(subject, dispatcher, handler, false, pso);

   Thread.sleep(100);

   sub.drain(Duration.ofMillis(100));

   nc.drain(Duration.ofMillis(100));
  }
  catch(Exception e)
  {
   e.printStackTrace();
  }
 }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```js
import { connect, consumerOpts } from "../../src/mod.ts";

const nc = await connect();
const js = nc.jetstream();

// note the consumer is not a durable - so when after the
// subscription ends, the server will auto destroy the
// consumer
const opts = consumerOpts();
opts.manualAck();
opts.maxMessages(2);
opts.deliverTo("xxx");
const sub = await js.subscribe("a.>", opts);
await (async () => {
  for await (const m of sub) {
    console.log(m.seq, m.subject);
    m.ack();
  }
})();

await nc.close();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio

import nats
from nats.errors import TimeoutError


async def main():
    nc = await nats.connect("localhost")

    # Create JetStream context.
    js = nc.jetstream()

    # Create ordered consumer with flow control and heartbeats
    # that auto resumes on failures.
    osub = await js.subscribe("foo", ordered_consumer=True)
    data = bytearray()

    while True:
        try:
            msg = await osub.next_msg()
            data.extend(msg.data)
        except TimeoutError:
            break
    print("All data in stream:", len(data))

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.JetStream;
using NATS.Client.JetStream.Models;

await using var client = new NatsClient();

INatsJSContext js = client.CreateJetStreamContext();

var streamConfig = new StreamConfig(name: "FOO", subjects: ["foo"]);
await js.CreateStreamAsync(streamConfig);

PubAckResponse ack = await js.PublishAsync("foo", "Hello, JetStream!");
ack.EnsureSuccess();

INatsJSConsumer orderedConsumer = await js.CreateOrderedConsumerAsync("FOO");

using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(10));

await foreach (NatsJSMsg<string> msg in orderedConsumer.ConsumeAsync<string>(cancellationToken: cts.Token))
{
    NatsJSMsgMetadata? meta = msg.Metadata;
    Console.WriteLine($"Stream Sequence  : {meta?.Sequence.Stream}");
    Console.WriteLine($"Consumer Sequence: {meta?.Sequence.Consumer}");
}
```

{% endtab %}
{% endtabs %}

## Delivery reliability

JetStream consumers can ensure not just the reliability of message delivery but also the reliability of the processing of the messages, even in the face of client application or downstream failures. It does so by using message level acknowledgements and message re-deliveries.

Consumers have an [Acknowledgement Policy](https://docs.nats.io/nats-concepts/jetstream/consumers#ackpolicy) specifying the level of reliability required. In increasing order of reliability the available policies are: 'none' for no application level acknowledgements, 'all' where acknowledging a specific message also implicitly acknowledges all previous messages in the stream, and 'explicit' where each message must be individually acknowledged.

When the consumer is set to require explicit acknowledgements the client applications are able to use more than one kind of [acknowledgement](https://docs.nats.io/using-nats/anatomy#consumer-acknowledgements) to indicate successful (or not) reception and processing of the messages being received from the consumer.

Applications can:

* Acknowledge the successfull processing of a message (`Ack()`).
* Acknowledge the successfull processing of a message and request an acknowledgement of the reception of the acknowledgement by the consumer (`AckSync()`).
* Indicate that the processing is still in progress and more time is needed (`inProgress()`).
* Negatively acknowledge a message, indicating that the client application is currently (temporarily) unable to process the message and that the consumer should attempt to re-deliver it (`Nak()`).
* Terminate a message (typically, because there is a problem with the data inside the message such that the client application is never going to be able to process it), indicating that the consumer should not attempt to re-deliver the message (`Term()`).

After a message is sent from the consumer to a subscribing client application by the server an 'AckWait' timer is started. This timer is deleted when either a positive (`Ack()`) or a termination (`Term()`) acknowledgement is received from the client application. The timer gets reset upon reception of an in-progress (`inProgress()`) acknowledgement.

If at the end of a period of time no acknowledgement has been received from the client application, the server will attempt to re-deliver the message. If there is more than one client application instance subscribing to the consumer, there is no guarantee that the re-delivery would be to any particular client instance.

You can control the timing of re-deliveries using either the single `AckWait` duration attribute of the consumer, or as a sequence of durations in the `BackOff` attribute (which overrides `AckWait`).

You can also control the timing of re-deliveries when messages are negatively acknowledged with `Nak()`, by passing a `nakDelay()` option (or using `NakWithDelay()`), otherwise the re-delivery attempt will happen right after the reception of the Nak by the server.

### "Dead Letter Queues" type functionality

You can set a maximum number of delivery attempts using the consumer's `MaxDeliver` setting.

Whenever a message reaches its maximum number of delivery attempts an advisory message is published on the `$JS.EVENT.ADVISORY.CONSUMER.MAX_DELIVERIES.<STREAM>.<CONSUMER>` subject. The advisory message's payload (use `nats schema info io.nats.jetstream.advisory.v1.max_deliver` for specific information) contains a `stream_seq` field that contains the sequence number of the message in the stream.

Similarly, whenever a client application terminates delivery attempts for the message using `AckTerm` an advisory message is published on the `$JS.EVENT.ADVISORY.CONSUMER.MSG_TERMINATED.<STREAM>.<CONSUMER>` subject, and its payload (see `nats schema info io.nats.jetstream.advisory.v1.terminated`) contains a `stream_seq` field.

You can leverage those advisory messages to implement "Dead Letter Queue" (DLQ) types of functionalities. For example:

* If you only need to know about each time a message is 'dead' (considered un-re-deliverable by the consumer), then listening to the advisories is enough.
* If you also need to have access to the message in question then you can use the message's sequence number included in the advisory to retrieve that specific message by sequence number from the stream. If a message reaches its maximum level of delivery attempts, it will still stay in the stream until it is manually deleted or manually acknowledged.


# Publishing to Streams

{% tabs %}
{% tab title="Go" %}

```go
func ExampleJetStream() {
	nc, err := nats.Connect("localhost")
	if err != nil {
		log.Fatal(err)
	}

	// Use the JetStream context to produce and consumer messages
	// that have been persisted.
	js, err := nc.JetStream(nats.PublishAsyncMaxPending(256))
	if err != nil {
		log.Fatal(err)
	}

	js.AddStream(&nats.StreamConfig{
		Name:     "example-stream",
		Subjects: []string{"example-subject"},
	})

	js.Publish("example-subject", []byte("Hello JS!"))

	// Publish messages asynchronously.
	for i := 0; i < 500; i++ {
		js.PublishAsync("example-subject", []byte("Hello JS Async!"))
	}
	select {
	case <-js.PublishAsyncComplete():
	case <-time.After(5 * time.Second):
		fmt.Println("Did not resolve in time")
	}
}
```

{% endtab %}

{% tab title="Java" %}

```java
try (Connection nc = Nats.connect("localhost")) {
    JetStreamManagement jsm = nc.jetStreamManagement();
    jsm.addStream(StreamConfiguration.builder()
        .name("example-stream")
        .subjects("example-subject")
        .build());

    JetStream js = jsm.jetStream();

    // Publish Synchronously
    PublishAck pa = js.publish("example-subject", "Hello JS Sync!".getBytes());
    System.out.println("Publish Sequence: " + pa.getSeqno());

    // Publish Asynchronously
    CompletableFuture<PublishAck> future =
        js.publishAsync("example-subject", "Hello JS Async!".getBytes());

    try {
        pa = future.get(1, TimeUnit.SECONDS);
        System.out.println("Publish Sequence: " + pa.getSeqno());
    }
    catch (ExecutionException e) {
        // Might have been a problem with the publish,
        // such as a failed expectation (advanced feature)
        // Also could be that the publish ack did not return in time
        // from the internal request timeout
    }
    catch (TimeoutException e) {
        // The future timed out meaning it's timeout was shorter than
        // the publish async's request timeout
    }
    catch (InterruptedException e) {
        // The future.get() thread was interrupted.
    }
}
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
import { connect, Empty } from "../../src/mod.ts";

const nc = await connect();

const jsm = await nc.jetstreamManager();
await jsm.streams.add({ name: "example-stream", subjects: ["example-subject"] });

const js = await nc.jetstream();
// the jetstream client provides a publish that returns
// a confirmation that the message was received and stored
// by the server. You can associate various expectations
// when publishing a message to prevent duplicates.
// If the expectations are not met, the message is rejected.
let pa = await js.publish("example-subject", Empty, {
  msgID: "a",
  expect: { streamName: "example-stream" },
});
console.log(`${pa.stream}[${pa.seq}]: duplicate? ${pa.duplicate}`);

pa = await js.publish("example-subject", Empty, {
  msgID: "a",
  expect: { lastSequence: 1 },
});
console.log(`${pa.stream}[${pa.seq}]: duplicate? ${pa.duplicate}`);

await jsm.streams.delete("example-stream");
await nc.drain();
```

{% endtab %}

{% tab title="Python" %}

```python
import asyncio

import nats
from nats.errors import TimeoutError


async def main():
    nc = await nats.connect("localhost")

    # Create JetStream context.
    js = nc.jetstream()

    # Persist messages on 'example-subject'.
    await js.add_stream(name="example-stream", subjects=["example-subject"])

    for i in range(0, 10):
        ack = await js.publish("example-subject", f"hello world: {i}".encode())
        print(ack)

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net
using NATS.Net;
using NATS.Client.JetStream;
using NATS.Client.JetStream.Models;

await using var client = new NatsClient();

INatsJSContext js = client.CreateJetStreamContext();

// Create a stream
var streamConfig = new StreamConfig(name: "example-stream", subjects: ["example-subject"]);
await js.CreateStreamAsync(streamConfig);

// Publish a message
{
    PubAckResponse ack = await js.PublishAsync("example-subject", "Hello, JetStream!");
    ack.EnsureSuccess();
}

// Publish messages concurrently
List<NatsJSPublishConcurrentFuture> futures = new();
for (var i = 0; i < 500; i++)
{
    NatsJSPublishConcurrentFuture future
        = await js.PublishConcurrentAsync("example-subject", "Hello, JetStream 1!");
    futures.Add(future);
}

foreach (var future in futures)
{
    await using (future)
    {
        PubAckResponse ack = await future.GetResponseAsync();
        ack.EnsureSuccess();
    }
}
```

{% endtab %}

{% tab title="C" %}

```
#include "examples.h"

static const char *usage = ""\
"-stream        stream name (default is 'foo')\n" \
"-txt           text to send (default is 'hello')\n" \
"-count         number of messages to send\n" \
"-sync          publish synchronously (default is async)\n";

static void
_jsPubErr(jsCtx *js, jsPubAckErr *pae, void *closure)
{
    int *errors = (int*) closure;

    printf("Error: %u - Code: %u - Text: %s\n", pae->Err, pae->ErrCode, pae->ErrText);
    printf("Original message: %.*s\n", natsMsg_GetDataLength(pae->Msg), natsMsg_GetData(pae->Msg));

    *errors = (*errors + 1);

    // If we wanted to resend the original message, we would do something like that:
    //
    // js_PublishMsgAsync(js, &(pae->Msg), NULL);
    //
    // Note that we use `&(pae->Msg)` so that the library set it to NULL if it takes
    // ownership, and the library will not destroy the message when this callback returns.

    // No need to destroy anything, everything is handled by the library.
}

int main(int argc, char **argv)
{
    natsConnection      *conn  = NULL;
    natsStatistics      *stats = NULL;
    natsOptions         *opts  = NULL;
    jsCtx               *js    = NULL;
    jsOptions           jsOpts;
    jsErrCode           jerr   = 0;
    natsStatus          s;
    int                 dataLen=0;
    volatile int        errors = 0;
    bool                delStream = false;

    opts = parseArgs(argc, argv, usage);
    dataLen = (int) strlen(payload);

    s = natsConnection_Connect(&conn, opts);

    if (s == NATS_OK)
        s = jsOptions_Init(&jsOpts);

    if (s == NATS_OK)
    {
        if (async)
        {
            jsOpts.PublishAsync.ErrHandler           = _jsPubErr;
            jsOpts.PublishAsync.ErrHandlerClosure    = (void*) &errors;
        }
        s = natsConnection_JetStream(&js, conn, &jsOpts);
    }

    if (s == NATS_OK)
    {
        jsStreamInfo    *si = NULL;

        // First check if the stream already exists.
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_NOT_FOUND)
        {
            jsStreamConfig  cfg;

            // Since we are the one creating this stream, we can delete at the end.
            delStream = true;

            // Initialize the configuration structure.
            jsStreamConfig_Init(&cfg);
            cfg.Name = stream;
            // Set the subject
            cfg.Subjects = (const char*[1]){subj};
            cfg.SubjectsLen = 1;
            // Make it a memory stream.
            cfg.Storage = js_MemoryStorage;
            // Add the stream,
            s = js_AddStream(&si, js, &cfg, NULL, &jerr);
        }
        if (s == NATS_OK)
        {
            printf("Stream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            // Need to destroy the returned stream object.
            jsStreamInfo_Destroy(si);
        }
    }

    if (s == NATS_OK)
        s = natsStatistics_Create(&stats);

    if (s == NATS_OK)
    {
        printf("\nSending %" PRId64 " messages to subject '%s'\n", total, stream);
        start = nats_Now();
    }

    for (count = 0; (s == NATS_OK) && (count < total); count++)
    {
        if (async)
            s = js_PublishAsync(js, subj, (const void*) payload, dataLen, NULL);
        else
        {
            jsPubAck *pa = NULL;

            s = js_Publish(&pa, js, subj, (const void*) payload, dataLen, NULL, &jerr);
            if (s == NATS_OK)
            {
                if (pa->Duplicate)
                    printf("Got a duplicate message! Sequence=%" PRIu64 "\n", pa->Sequence);

                jsPubAck_Destroy(pa);
            }
        }
    }

    if ((s == NATS_OK) && async)
    {
        jsPubOptions    jsPubOpts;

        jsPubOptions_Init(&jsPubOpts);
        // Let's set it to 30 seconds, if getting "Timeout" errors,
        // this may need to be increased based on the number of messages
        // being sent.
        jsPubOpts.MaxWait = 30000;
        s = js_PublishAsyncComplete(js, &jsPubOpts);
        if (s == NATS_TIMEOUT)
        {
            // Let's get the list of pending messages. We could resend,
            // etc, but for now, just destroy them.
            natsMsgList list;

            js_PublishAsyncGetPendingList(&list, js);
            natsMsgList_Destroy(&list);
        }
    }

    if (s == NATS_OK)
    {
        jsStreamInfo *si = NULL;

        elapsed = nats_Now() - start;
        printStats(STATS_OUT, conn, NULL, stats);
        printPerf("Sent");

        if (errors != 0)
            printf("There were %d asynchronous errors\n", errors);

        // Let's report some stats after the run
        s = js_GetStreamInfo(&si, js, stream, NULL, &jerr);
        if (s == NATS_OK)
        {
            printf("\nStream %s has %" PRIu64 " messages (%" PRIu64 " bytes)\n",
                si->Config->Name, si->State.Msgs, si->State.Bytes);

            jsStreamInfo_Destroy(si);
        }
    }
    if (delStream && (js != NULL))
    {
        printf("\nDeleting stream %s: ", stream);
        s = js_DeleteStream(js, stream, NULL, &jerr);
        if (s == NATS_OK)
            printf("OK!");
        printf("\n");
    }
    if (s != NATS_OK)
    {
        printf("Error: %u - %s - jerr=%u\n", s, natsStatus_GetText(s), jerr);
        nats_PrintLastErrorStack(stderr);
    }

    // Destroy all our objects to avoid report of memory leak
    jsCtx_Destroy(js);
    natsStatistics_Destroy(stats);
    natsConnection_Destroy(conn);
    natsOptions_Destroy(opts);

    // To silence reports of memory still in used with valgrind
    nats_Close();

    return 0;
}
```

{% endtab %}
{% endtabs %}


# Using the Key/Value Store

As the Key Value Store is built on top of the JetStream persistence layer you obtain a KeyValueManager object from your JetStream [context](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/js/context.md).

The key must be in the same format as a NATS subject, i.e. it can be a dot separated list of tokens (which means that you can then use wildcards to match hierarchies of keys when watching a bucket), and can only contain [valid characters](https://docs.nats.io/nats-concepts/subjects#characters-allowed-for-subject-names). The value can be any byte array.

### Creating, and deleting KV buckets

You can create as many independent key/value store instance, called 'buckets', as you need. Buckets are typically created, purged or deleted administratively (e.g. using the `nats` CLI tool), but this can also be done using one of the following KeyValueManager calls:

{% tabs %}
{% tab title="Go" %}

```go
// KeyValue will lookup and bind to an existing KeyValue store.
KeyValue(bucket string) (KeyValue, error)
// CreateKeyValue will create a KeyValue store with the following configuration.
CreateKeyValue(cfg *KeyValueConfig) (KeyValue, error)
// DeleteKeyValue will delete this KeyValue store (JetStream stream).
DeleteKeyValue(bucket string) error
```

{% endtab %}

{% tab title="Java" %}

```java
/**
 * Create a key value store.
 * @param config the key value configuration
 * @return bucket info
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws IllegalArgumentException the server is not JetStream enabled
 */
KeyValueStatus create(KeyValueConfiguration config) throws IOException, JetStreamApiException;

/**
* Get the list of bucket names.
* @return list of bucket names
* @throws IOException covers various communication issues with the NATS
*         server such as timeout or interruption
* @throws JetStreamApiException the request had an error related to the data
* @throws InterruptedException if the thread is interrupted
*/
List<String> getBucketNames() throws IOException, JetStreamApiException, InterruptedException;

/**
* Gets the info for an existing bucket.
* @param bucketName the bucket name to use
* @throws IOException covers various communication issues with the NATS
*         server such as timeout or interruption
* @throws JetStreamApiException the request had an error related to the data
* @return the bucket status object
*/
KeyValueStatus getBucketInfo(String bucketName) throws IOException, JetStreamApiException;

/**
* Deletes an existing bucket. Will throw a JetStreamApiException if the delete fails.
* @param bucketName the stream name to use.
* @throws IOException covers various communication issues with the NATS
*         server such as timeout or interruption
* @throws JetStreamApiException the request had an error related to the data
*/
void delete(String bucketName) throws IOException, JetStreamApiException;
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
  static async create(
    js: JetStreamClient,
    name: string,
    opts: Partial<KvOptions> = {},
  ): Promise<KV>

static async bind(
    js: JetStreamClient,
    name: string,
    opts: Partial<{ codec: KvCodecs }> = {},
): Promise<KV>

destroy(): Promise<boolean>
```

{% endtab %}

{% tab title="Python" %}

```python
# from the JetStreamContext

async def key_value(self, bucket: str) -> KeyValue:

async def create_key_value(
    self,
    config: Optional[api.KeyValueConfig] = None,
    **params,
) -> KeyValue:
    """
    create_key_value takes an api.KeyValueConfig and creates a KV in JetStream.
    """
    
async def delete_key_value(self, bucket: str) -> bool:
    """
    delete_key_value deletes a JetStream KeyValue store by destroying
    the associated stream.
    """  
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

// Create a new Key Value Store or get an existing one
ValueTask<INatsKVStore> CreateStoreAsync(string bucket, CancellationToken cancellationToken = default);

// Get a list of bucket names
IAsyncEnumerable<string> GetBucketNamesAsync(CancellationToken cancellationToken = default);

// Gets the status for all buckets
IAsyncEnumerable<NatsKVStatus> GetStatusesAsync(CancellationToken cancellationToken = default);

// Delete a Key Value Store
ValueTask<bool> DeleteStoreAsync(string bucket, CancellationToken cancellationToken = default);

//
```

{% endtab %}

{% tab title="C" %}

```c
NATS_EXTERN natsStatus 	kvConfig_Init (kvConfig *cfg)
 	Initializes a KeyValue configuration structure.
 
NATS_EXTERN natsStatus 	js_CreateKeyValue (kvStore **new_kv, jsCtx *js, kvConfig *cfg)
 	Creates a KeyValue store with a given configuration.
 
NATS_EXTERN natsStatus 	js_KeyValue (kvStore **new_kv, jsCtx *js, const char *bucket)
 	Looks-up and binds to an existing KeyValue store.
 
NATS_EXTERN natsStatus 	js_DeleteKeyValue (jsCtx *js, const char *bucket)
 	Deletes a KeyValue store.
 
NATS_EXTERN void 	kvStore_Destroy (kvStore *kv)
 	Destroys a KeyValue store object.
```

{% endtab %}
{% endtabs %}

### Getting

You can do a get to get the current value on a key, or ask to get a specific revision of the value.

{% tabs %}
{% tab title="Go" %}

```go
// Get returns the latest value for the key.
Get(key string) (entry KeyValueEntry, err error)
// GetRevision returns a specific revision value for the key.
GetRevision(key string, revision uint64) (entry KeyValueEntry, err error)
```

{% endtab %}

{% tab title="Java" %}

```java
/**
* Get the entry for a key
* @param key the key
* @return the KvEntry object or null if not found.
* @throws IOException covers various communication issues with the NATS
*         server such as timeout or interruption
* @throws JetStreamApiException the request had an error related to the data
* @throws IllegalArgumentException the server is not JetStream enabled
*/
KeyValueEntry get(String key) throws IOException, JetStreamApiException;

/**
* Get the specific revision of an entry for a key.
* @param key the key
* @param revision the revision
* @return the KvEntry object or null if not found.
* @throws IOException covers various communication issues with the NATS
*         server such as timeout or interruption
* @throws JetStreamApiException the request had an error related to the data
* @throws IllegalArgumentException the server is not JetStream enabled
*/
KeyValueEntry get(String key, long revision) throws IOException, JetStreamApiException;
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
async get(k: string): Promise<KvEntry | null>
```

{% endtab %}

{% tab title="Python" %}

```python
async def get(self, key: str) -> Entry:
   """
   get returns the latest value for the key.
   """
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

// Get an entry from the bucket using the key
ValueTask<NatsKVEntry<T>> GetEntryAsync<T>(string key, ulong revision = default, INatsDeserialize<T>? serializer = default, CancellationToken cancellationToken = default);

//
```

{% endtab %}

{% tab title="C" %}

```c
NATS_EXTERN natsStatus 	kvStore_Get (kvEntry **new_entry, kvStore *kv, const char *key)
 	Returns the latest entry for the key.
 
NATS_EXTERN natsStatus 	kvStore_GetRevision (kvEntry **new_entry, kvStore *kv, const char *key, uint64_t revision)
 	Returns the entry at the specific revision for the key.
```

{% endtab %}
{% endtabs %}

### Putting

The key is always a string, you can simply use Put to store a byte array, or the convenience `PutString` to put a string. For 'compare and set' functionality you can use `Create` and `Update`.

{% tabs %}
{% tab title="Go" %}

```go
Put(key string, value []byte) (revision uint64, err error)
// PutString will place the string for the key into the store.
PutString(key string, value string) (revision uint64, err error)
// Create will add the key/value pair if it does not exist.
Create(key string, value []byte) (revision uint64, err error)
// Update will update the value if the latest revision matches.
Update(key string, value []byte, last uint64) (revision uint64, err error)
```

{% endtab %}

{% tab title="Java" %}

```java
/**
 * Put a byte[] as the value for a key
 * @param key the key
 * @param value the bytes of the value
 * @return the revision number for the key
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws IllegalArgumentException the server is not JetStream enabled
 */
long put(String key, byte[] value) throws IOException, JetStreamApiException;

/**
 * Put a string as the value for a key
 * @param key the key
 * @param value the UTF-8 string
 * @return the revision number for the key
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws IllegalArgumentException the server is not JetStream enabled
 */
long put(String key, String value) throws IOException, JetStreamApiException;

/**
 * Put a long as the value for a key
 * @param key the key
 * @param value the number
 * @return the revision number for the key
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws IllegalArgumentException the server is not JetStream enabled
 */
long put(String key, Number value) throws IOException, JetStreamApiException;

/**
 * Put as the value for a key iff the key does not exist (there is no history)
 * or is deleted (history shows the key is deleted)
 * @param key the key
 * @param value the bytes of the value
 * @return the revision number for the key
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws IllegalArgumentException the server is not JetStream enabled
 */
long create(String key, byte[] value) throws IOException, JetStreamApiException;

/**
 * Put as the value for a key iff the key exists and its last revision matches the expected
 * @param key the key
 * @param value the bytes of the value
 * @param expectedRevision the expected last revision
 * @return the revision number for the key
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws IllegalArgumentException the server is not JetStream enabled
 */
long update(String key, byte[] value, long expectedRevision) throws IOException, JetStreamApiException;
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
  async put(
    k: string,
    data: Uint8Array,
    opts: Partial<KvPutOptions> = {},
  ): Promise<number>

create(k: string, data: Uint8Array): Promise<number>    
    
update(k: string, data: Uint8Array, version: number): Promise<number>
```

{% endtab %}

{% tab title="Python" %}

```python
async def put(self, key: str, value: bytes) -> int:
    """
    put will place the new value for the key into the store
    and return the revision number.
    """
    
async def update(self, key: str, value: bytes, last: int) -> int:
    """
    update will update the value iff the latest revision matches.
    """    
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

// Put a value into the bucket using the key
// returns revision number
ValueTask<ulong> PutAsync<T>(string key, T value, INatsSerialize<T>? serializer = default, CancellationToken cancellationToken = default);

//
```

{% endtab %}

{% tab title="C" %}

```c
NATS_EXTERN natsStatus 	kvStore_Put (uint64_t *rev, kvStore *kv, const char *key, const void *data, int len)
 	Places the new value for the key into the store.
 
NATS_EXTERN natsStatus 	kvStore_PutString (uint64_t *rev, kvStore *kv, const char *key, const char *data)
 	Places the new value (as a string) for the key into the store.
 
NATS_EXTERN natsStatus 	kvStore_Create (uint64_t *rev, kvStore *kv, const char *key, const void *data, int len)
 	Places the value for the key into the store if and only if the key does not exist.
 
NATS_EXTERN natsStatus 	kvStore_CreateString (uint64_t *rev, kvStore *kv, const char *key, const char *data)
 	Places the value (as a string) for the key into the store if and only if the key does not exist.
 
NATS_EXTERN natsStatus 	kvStore_Update (uint64_t *rev, kvStore *kv, const char *key, const void *data, int len, uint64_t last)
 	Updates the value for the key into the store if and only if the latest revision matches.
 
NATS_EXTERN natsStatus 	kvStore_UpdateString (uint64_t *rev, kvStore *kv, const char *key, const char *data, uint64_t last)
 	Updates the value (as a string) for the key into the store if and only if the latest revision matches.
```

{% endtab %}
{% endtabs %}

### Deleting

You can delete a specific key, or purge the whole key/value bucket.

{% tabs %}
{% tab title="Go" %}

```go
// Delete will place a delete marker and leave all revisions.
Delete(key string) error
// Purge will place a delete marker and remove all previous revisions.
Purge(key string) error
```

{% endtab %}

{% tab title="Java" %}

```java
/**
* Soft deletes the key by placing a delete marker.
* @param key the key
* @throws IOException covers various communication issues with the NATS
*         server such as timeout or interruption
* @throws JetStreamApiException the request had an error related to the data
*/
void delete(String key) throws IOException, JetStreamApiException;

/**
* Purge all values/history from the specific key
* @param key the key
* @throws IOException covers various communication issues with the NATS
*         server such as timeout or interruption
* @throws JetStreamApiException the request had an error related to the data
*/
void purge(String key) throws IOException, JetStreamApiException;
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
delete(k: string): Promise<void>
    
purge(k: string): Promise<void>
```

{% endtab %}

{% tab title="Python" %}

```python
async def delete(self, key: str) -> bool:
    """
    delete will place a delete marker and remove all previous revisions.
    """
    
async def purge(self, key: str) -> bool:
    """
    purge will remove the key and all revisions.
    """    
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

// Delete an entry from the bucket
ValueTask DeleteAsync(string key, NatsKVDeleteOpts? opts = default, CancellationToken cancellationToken = default);

// Purge an entry from the bucket
ValueTask PurgeAsync(string key, NatsKVDeleteOpts? opts = default, CancellationToken cancellationToken = default);

//
```

{% endtab %}

{% tab title="C" %}

```c
NATS_EXTERN natsStatus 	kvStore_Delete (kvStore *kv, const char *key)
 	Deletes a key by placing a delete marker and leaving all revisions.
 
NATS_EXTERN natsStatus 	kvStore_Purge (kvStore *kv, const char *key, kvPurgeOptions *opts)
 	Deletes a key by placing a purge marker and removing all revisions.
 	
NATS_EXTERN natsStatus 	kvStore_PurgeDeletes (kvStore *kv, kvPurgeOptions *opts)
 	Purge and removes delete markers.
```

{% endtab %}
{% endtabs %}

### Getting all the keys

You can get the list of all the keys currently having a value associated using `Keys()`

{% tabs %}
{% tab title="Go" %}

```go
// Keys will return all keys.
Keys(opts ...WatchOpt) ([]string, error)
```

{% endtab %}

{% tab title="Java" %}

```java
/**
 * Get a list of the keys in a bucket.
 * @return List of keys
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws InterruptedException if the thread is interrupted
 */
List<String> keys() throws IOException, JetStreamApiException, InterruptedException;
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
async keys(k = ">"): Promise<QueuedIterator<string>>
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

// Get all the keys in the bucket
IAsyncEnumerable<string> GetKeysAsync(NatsKVWatchOpts? opts = default, CancellationToken cancellationToken = default);

// Get a filtered set of keys in the bucket
IAsyncEnumerable<string> GetKeysAsync(IEnumerable<string> filters, NatsKVWatchOpts? opts = default, CancellationToken cancellationToken = default);

//
```

{% endtab %}

{% tab title="C" %}

```c
NATS_EXTERN natsStatus 	kvStore_Keys (kvKeysList *list, kvStore *kv, kvWatchOptions *opts)
 	Returns all keys in the bucket.
 
NATS_EXTERN void 	kvKeysList_Destroy (kvKeysList *list)
 	Destroys this list of KeyValue store key strings.
```

{% endtab %}
{% endtabs %}

### Getting the history for a key

The JetStream key/value store has a feature you don't usually find in key/value stores: the ability to keep a history of the values associated with a key (rather than just the current value). The depth of the history is specified when the key/value bucket is created, and the default is a history depth of 1 (i.e. no history). The maximum history size is 64, if you need more your use case will be better implemented using the Stream functionality directly (where you can set the max number of messages per subject to any value you want) rather than the KV abstraction.

{% tabs %}
{% tab title="Go" %}

```go
// History will return all historical values for the key.
History(key string, opts ...WatchOpt) ([]KeyValueEntry, error)
```

{% endtab %}

{% tab title="Java" %}

```java
/**
 * Get the history (list of KeyValueEntry) for a key
 * @param key the key
 * @return List of KvEntry
 * @throws IOException covers various communication issues with the NATS
 *         server such as timeout or interruption
 * @throws JetStreamApiException the request had an error related to the data
 * @throws InterruptedException if the thread is interrupted
 */
List<KeyValueEntry> history(String key) throws IOException, JetStreamApiException, InterruptedException;
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
async history(
    opts: { key?: string; headers_only?: boolean } = {},
  ): Promise<QueuedIterator<KvEntry>>
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

// Get the history of an entry by key
IAsyncEnumerable<NatsKVEntry<T>> HistoryAsync<T>(string key, INatsDeserialize<T>? serializer = default, NatsKVWatchOpts? opts = default, CancellationToken cancellationToken = default);

//
```

{% endtab %}

{% tab title="C" %}

```c
NATS_EXTERN natsStatus 	kvStore_History (kvEntryList *list, kvStore *kv, const char *key, kvWatchOptions *opts)
 	Returns all historical entries for the key.
 
NATS_EXTERN void 	kvEntryList_Destroy (kvEntryList *list)
 	Destroys this list of KeyValue store entries.
```

{% endtab %}
{% endtabs %}

### Watching for changes

Watching a key/value bucket is like subscribing to updates: you provide a callback and you can watch all of the keys in the bucket or specify which specific key(s) you want to be kept updated about.

{% tabs %}
{% tab title="Go" %}

```go
// Watch for any updates to keys that match the keys argument which could include wildcards.
// Watch will send a nil entry when it has received all initial values.
Watch(keys string, opts ...WatchOpt) (KeyWatcher, error)
// WatchAll will invoke the callback for all updates.
WatchAll(opts ...WatchOpt) (KeyWatcher, error)
```

{% endtab %}

{% tab title="Java" %}

```java
/**
 * Watch updates for a specific key
 */
NatsKeyValueWatchSubscription watch(String key, KeyValueWatcher watcher, KeyValueWatchOption... watchOptions) throws IOException, JetStreamApiException, InterruptedException;

/**
 * Watch updates for all keys
 */
NatsKeyValueWatchSubscription watchAll(KeyValueWatcher watcher, KeyValueWatchOption... watchOptions) throws IOException, JetStreamApiException, InterruptedException;
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
  async watch(
    opts: {
      key?: string;
      headers_only?: boolean;
      initializedFn?: callbackFn;
    } = {},
  ): Promise<QueuedIterator<KvEntry>>
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

// Start a watcher for specific keys
// Key to watch is subject-based and wildcards may be used
IAsyncEnumerable<NatsKVEntry<T>> WatchAsync<T>(string key, INatsDeserialize<T>? serializer = default, NatsKVWatchOpts? opts = default, CancellationToken cancellationToken = default);

// Start a watcher for specific keys
// Key to watch are subject-based and wildcards may be used
IAsyncEnumerable<NatsKVEntry<T>> WatchAsync<T>(IEnumerable<string> keys, INatsDeserialize<T>? serializer = default, NatsKVWatchOpts? opts = default, CancellationToken cancellationToken = default);

// Start a watcher for all the keys in the bucket
IAsyncEnumerable<NatsKVEntry<T>> WatchAsync<T>(INatsDeserialize<T>? serializer = default, NatsKVWatchOpts? opts = default, CancellationToken cancellationToken = default);

//
```

{% endtab %}

{% tab title="C" %}

```c
NATS_EXTERN natsStatus 	kvStore_Watch (kvWatcher **new_watcher, kvStore *kv, const char *keys, kvWatchOptions *opts)
 	Returns a watcher for any updates to keys that match the keys argument.
 
NATS_EXTERN natsStatus 	kvStore_WatchAll (kvWatcher **new_watcher, kvStore *kv, kvWatchOptions *opts)
 	Returns a watcher for any updates to any keys of the KeyValue store bucket.
```

{% endtab %}
{% endtabs %}


# Using the Object Store

The Object Store allows you to store data of any (i.e. large) size by implementing a chunking mechanism, allowing you to for example store and retrieve files (i.e. the object) of any size by associating them with a path and a file name (i.e. the key). You obtain a ObjectStoreManager object from your JetStream [context](https://github.com/nats-io/nats.docs/blob/master/using-nats/developing-with-nats/js/context.md).

{% tabs %}
{% tab title="Go" %}

```go
// ObjectStoreManager is used to manage object stores. It provides methods
// for CRUD operations on object stores.
type ObjectStoreManager interface {
	// ObjectStore will look up and bind to an existing object store
	// instance.
	//
	// If the object store with given name does not exist, ErrBucketNotFound
	// will be returned.
	ObjectStore(ctx context.Context, bucket string) (ObjectStore, error)

	// CreateObjectStore will create a new object store with the given
	// configuration.
	//
	// If the object store with given name already exists, ErrBucketExists
	// will be returned.
	CreateObjectStore(ctx context.Context, cfg ObjectStoreConfig) (ObjectStore, error)

	// UpdateObjectStore will update an existing object store with the given
	// configuration.
	//
	// If the object store with given name does not exist, ErrBucketNotFound
	// will be returned.
	UpdateObjectStore(ctx context.Context, cfg ObjectStoreConfig) (ObjectStore, error)

	// CreateOrUpdateObjectStore will create a new object store with the given
	// configuration if it does not exist, or update an existing object store
	// with the given configuration.
	CreateOrUpdateObjectStore(ctx context.Context, cfg ObjectStoreConfig) (ObjectStore, error)

	// DeleteObjectStore will delete the provided object store.
	//
	// If the object store with given name does not exist, ErrBucketNotFound
	// will be returned.
	DeleteObjectStore(ctx context.Context, bucket string) error

	// ObjectStoreNames is used to retrieve a list of bucket names.
	// It returns an ObjectStoreNamesLister exposing a channel to receive
	// the names of the object stores.
	//
	// The lister will always close the channel when done (either all names
	// have been read or an error occurred) and therefore can be used in a
	// for-range loop.
	ObjectStoreNames(ctx context.Context) ObjectStoreNamesLister

	// ObjectStores is used to retrieve a list of bucket statuses.
	// It returns an ObjectStoresLister exposing a channel to receive
	// the statuses of the object stores.
	//
	// The lister will always close the channel when done (either all statuses
	// have been read or an error occurred) and therefore can be used in a
	// for-range loop.
	ObjectStores(ctx context.Context) ObjectStoresLister
}

// ObjectStore contains methods to operate on an object store.
// Using the ObjectStore interface, it is possible to:
//
// - Perform CRUD operations on objects (Get, Put, Delete).
//   Get and put expose convenience methods to work with
//   byte slices, strings and files, in addition to streaming [io.Reader]
// - Get information about an object without retrieving it.
// - Update the metadata of an object.
// - Add links to other objects or object stores.
// - Watch for updates to a store
// - List information about objects in a store
// - Retrieve status and configuration of an object store.
type ObjectStore interface {
	// Put will place the contents from the reader into a new object. If the
	// object already exists, it will be overwritten. The object name is
	// required and is taken from the ObjectMeta.Name field.
	//
	// The reader will be read until EOF. ObjectInfo will be returned, containing
	// the object's metadata, digest and instance information.
	Put(ctx context.Context, obj ObjectMeta, reader io.Reader) (*ObjectInfo, error)

	// PutBytes is convenience function to put a byte slice into this object
	// store under the given name.
	//
	// ObjectInfo will be returned, containing the object's metadata, digest
	// and instance information.
	PutBytes(ctx context.Context, name string, data []byte) (*ObjectInfo, error)

	// PutString is convenience function to put a string into this object
	// store under the given name.
	//
	// ObjectInfo will be returned, containing the object's metadata, digest
	// and instance information.
	PutString(ctx context.Context, name string, data string) (*ObjectInfo, error)

	// PutFile is convenience function to put a file contents into this
	// object store. The name of the object will be the path of the file.
	//
	// ObjectInfo will be returned, containing the object's metadata, digest
	// and instance information.
	PutFile(ctx context.Context, file string) (*ObjectInfo, error)

	// Get will pull the named object from the object store. If the object
	// does not exist, ErrObjectNotFound will be returned.
	//
	// The returned ObjectResult will contain the object's metadata and a
	// reader to read the object's contents. The reader will be closed when
	// all data has been read or an error occurs.
	//
	// A GetObjectShowDeleted option can be supplied to return an object
	// even if it was marked as deleted.
	Get(ctx context.Context, name string, opts ...GetObjectOpt) (ObjectResult, error)

	// GetBytes is a convenience function to pull an object from this object
	// store and return it as a byte slice.
	//
	// If the object does not exist, ErrObjectNotFound will be returned.
	//
	// A GetObjectShowDeleted option can be supplied to return an object
	// even if it was marked as deleted.
	GetBytes(ctx context.Context, name string, opts ...GetObjectOpt) ([]byte, error)

	// GetString is a convenience function to pull an object from this
	// object store and return it as a string.
	//
	// If the object does not exist, ErrObjectNotFound will be returned.
	//
	// A GetObjectShowDeleted option can be supplied to return an object
	// even if it was marked as deleted.
	GetString(ctx context.Context, name string, opts ...GetObjectOpt) (string, error)

	// GetFile is a convenience function to pull an object from this object
	// store and place it in a file. If the file already exists, it will be
	// overwritten, otherwise it will be created.
	//
	// If the object does not exist, ErrObjectNotFound will be returned.
	// A GetObjectShowDeleted option can be supplied to return an object
	// even if it was marked as deleted.
	GetFile(ctx context.Context, name, file string, opts ...GetObjectOpt) error

	// GetInfo will retrieve the current information for the object, containing
	// the object's metadata and instance information.
	//
	// If the object does not exist, ErrObjectNotFound will be returned.
	//
	// A GetObjectInfoShowDeleted option can be supplied to return an object
	// even if it was marked as deleted.
	GetInfo(ctx context.Context, name string, opts ...GetObjectInfoOpt) (*ObjectInfo, error)

	// UpdateMeta will update the metadata for the object.
	//
	// If the object does not exist, ErrUpdateMetaDeleted will be returned.
	// If the new name is different from the old name, and an object with the
	// new name already exists, ErrObjectAlreadyExists will be returned.
	UpdateMeta(ctx context.Context, name string, meta ObjectMeta) error

	// Delete will delete the named object from the object store. If the object
	// does not exist, ErrObjectNotFound will be returned. If the object is
	// already deleted, no error will be returned.
	//
	// All chunks for the object will be purged, and the object will be marked
	// as deleted.
	Delete(ctx context.Context, name string) error

	// AddLink will add a link to another object. A link is a reference to
	// another object. The provided name is the name of the link object.
	// The provided ObjectInfo is the info of the object being linked to.
	//
	// If an object with given name already exists, ErrObjectAlreadyExists
	// will be returned.
	// If object being linked to is deleted, ErrNoLinkToDeleted will be
	// returned.
	// If the provided object is a link, ErrNoLinkToLink will be returned.
	// If the provided object is nil or the name is empty, ErrObjectRequired
	// will be returned.
	AddLink(ctx context.Context, name string, obj *ObjectInfo) (*ObjectInfo, error)

	// AddBucketLink will add a link to another object store. A link is a
	// reference to another object store. The provided name is the name of
	// the link object.
	// The provided ObjectStore is the object store being linked to.
	//
	// If an object with given name already exists, ErrObjectAlreadyExists
	// will be returned.
	// If the provided object store is nil ErrBucketRequired will be returned.
	AddBucketLink(ctx context.Context, name string, bucket ObjectStore) (*ObjectInfo, error)

	// Seal will seal the object store, no further modifications will be allowed.
	Seal(ctx context.Context) error

	// Watch for any updates to objects in the store. By default, the watcher will send the latest
	// info for each object and all future updates. Watch will send a nil
	// entry when it has received all initial values. There are a few ways
	// to configure the watcher:
	//
	// - IncludeHistory will have the watcher send all historical information
	// for each object.
	// - IgnoreDeletes will have the watcher not pass any objects with
	// delete markers.
	// - UpdatesOnly will have the watcher only pass updates on objects
	// (without latest info when started).
	Watch(ctx context.Context, opts ...WatchOpt) (ObjectWatcher, error)

	// List will list information about objects in the store.
	//
	// If the object store is empty, ErrNoObjectsFound will be returned.
	List(ctx context.Context, opts ...ListObjectsOpt) ([]*ObjectInfo, error)

	// Status retrieves the status and configuration of the bucket.
	Status(ctx context.Context) (ObjectStoreStatus, error)
}
```

See more at [jetstream/object.go](https://github.com/nats-io/nats.go/blob/main/jetstream/object.go)
{% endtab %}

{% tab title="Java" %}

```java
/**
 * Object Store Management context for creation and access to key value buckets.
 */
public interface ObjectStore {

    /**
     * Get the name of the object store's bucket.
     * @return the name
     */
    String getBucketName();

    /**
     * Place the contents of the input stream into a new object.
     */
    ObjectInfo put(ObjectMeta meta, InputStream inputStream) throws IOException, JetStreamApiException, NoSuchAlgorithmException;

    /**
     * Place the contents of the input stream into a new object.
     */
    ObjectInfo put(String objectName, InputStream inputStream) throws IOException, JetStreamApiException, NoSuchAlgorithmException;

    /**
     * Place the bytes into a new object.
     */
    ObjectInfo put(String objectName, byte[] input) throws IOException, JetStreamApiException, NoSuchAlgorithmException;

    /**
     * Place the contents of the file into a new object using the file name as the object name.
     */
    ObjectInfo put(File file) throws IOException, JetStreamApiException, NoSuchAlgorithmException;

    /**
     * Get an object by name from the store, reading it into the output stream, if the object exists.
     */
    ObjectInfo get(String objectName, OutputStream outputStream) throws IOException, JetStreamApiException, InterruptedException, NoSuchAlgorithmException;

    /**
     * Get the info for an object if the object exists / is not deleted.
     */
    ObjectInfo getInfo(String objectName) throws IOException, JetStreamApiException;

    /**
     * Get the info for an object if the object exists, optionally including deleted.
     */
    ObjectInfo getInfo(String objectName, boolean includingDeleted) throws IOException, JetStreamApiException;

    /**
     * Update the metadata of name, description or headers. All other changes are ignored.
     */
    ObjectInfo updateMeta(String objectName, ObjectMeta meta) throws IOException, JetStreamApiException;

    /**
     * Delete the object by name. A No-op if the object is already deleted.
     */
    ObjectInfo delete(String objectName) throws IOException, JetStreamApiException;

    /**
     * Add a link to another object. A link cannot be for another link.
     */
    ObjectInfo addLink(String objectName, ObjectInfo toInfo) throws IOException, JetStreamApiException;

    /**
     * Add a link to another object store (bucket).
     */
    ObjectInfo addBucketLink(String objectName, ObjectStore toStore) throws IOException, JetStreamApiException;

    /**
     * Close (seal) the bucket to changes. The store (bucket) will be read only.
     */
    ObjectStoreStatus seal() throws IOException, JetStreamApiException;

    /**
     * Get a list of all object [infos] in the store.
     */
    List<ObjectInfo> getList() throws IOException, JetStreamApiException, InterruptedException;

    /**
     * Create a watch on the store (bucket).
     */
    NatsObjectStoreWatchSubscription watch(ObjectStoreWatcher watcher, ObjectStoreWatchOption... watchOptions) throws IOException, JetStreamApiException, InterruptedException;

    /**
     * Get the ObjectStoreStatus object.
     */
    ObjectStoreStatus getStatus() throws IOException, JetStreamApiException;

```

{% endtab %}

{% tab title="Python" %}

```python
    async def object_store(self, bucket: str) -> ObjectStore:

    async def create_object_store(
        self,
        bucket: str = None,
        config: Optional[api.ObjectStoreConfig] = None,
        **params,
    ) -> ObjectStore:
        """
        create_object_store takes an api.ObjectStoreConfig and creates a OBJ in JetStream.
        """
    async def delete_object_store(self, bucket: str) -> bool:
        """
        delete_object_store will delete the underlying stream for the named object.
        """
```

{% endtab %}

{% tab title="C#" %}

```csharp
// dotnet add package NATS.Net

/// <summary>
/// NATS Object Store context.
/// </summary>
public interface INatsObjContext
{
    /// <summary>
    /// Provides access to the JetStream context associated with the Object Store operations.
    /// </summary>
    INatsJSContext JetStreamContext { get; }

    /// <summary>
    /// Create a new object store.
    /// </summary>
    /// <param name="bucket">Bucket name.</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object store object.</returns>
    ValueTask<INatsObjStore> CreateObjectStoreAsync(string bucket, CancellationToken cancellationToken = default);

    /// <summary>
    /// Create a new object store.
    /// </summary>
    /// <param name="config">Object store configuration.</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object store object.</returns>
    ValueTask<INatsObjStore> CreateObjectStoreAsync(NatsObjConfig config, CancellationToken cancellationToken = default);

    /// <summary>
    /// Get an existing object store.
    /// </summary>
    /// <param name="bucket">Bucket name</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>The Object Store object</returns>
    ValueTask<INatsObjStore> GetObjectStoreAsync(string bucket, CancellationToken cancellationToken = default);

    /// <summary>
    /// Delete an object store.
    /// </summary>
    /// <param name="bucket">Name of the bucket.</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Whether delete was successful or not.</returns>
    ValueTask<bool> DeleteObjectStore(string bucket, CancellationToken cancellationToken);
}

/// <summary>
/// NATS Object Store.
/// </summary>
public interface INatsObjStore
{
    /// <summary>
    /// Provides access to the JetStream context associated with the Object Store operations.
    /// </summary>
    INatsJSContext JetStreamContext { get; }

    /// <summary>
    /// Object store bucket name.
    /// </summary>
    string Bucket { get; }

    /// <summary>
    /// Get object by key.
    /// </summary>
    /// <param name="key">Object key.</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object value as a byte array.</returns>
    ValueTask<byte[]> GetBytesAsync(string key, CancellationToken cancellationToken = default);

    /// <summary>
    /// Get object by key.
    /// </summary>
    /// <param name="key">Object key.</param>
    /// <param name="stream">Stream to write the object value to.</param>
    /// <param name="leaveOpen"><c>true</c> to not close the underlying stream when async method returns; otherwise, <c>false</c></param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object metadata.</returns>
    /// <exception cref="NatsObjException">Metadata didn't match the value retrieved e.g. the SHA digest.</exception>
    ValueTask<ObjectMetadata> GetAsync(string key, Stream stream, bool leaveOpen = false, CancellationToken cancellationToken = default);

    /// <summary>
    /// Put an object by key.
    /// </summary>
    /// <param name="key">Object key.</param>
    /// <param name="value">Object value as a byte array.</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object metadata.</returns>
    ValueTask<ObjectMetadata> PutAsync(string key, byte[] value, CancellationToken cancellationToken = default);

    /// <summary>
    /// Put an object by key.
    /// </summary>
    /// <param name="key">Object key.</param>
    /// <param name="stream">Stream to read the value from.</param>
    /// <param name="leaveOpen"><c>true</c> to not close the underlying stream when async method returns; otherwise, <c>false</c></param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object metadata.</returns>
    /// <exception cref="NatsObjException">There was an error calculating SHA digest.</exception>
    /// <exception cref="NatsJSApiException">Server responded with an error.</exception>
    ValueTask<ObjectMetadata> PutAsync(string key, Stream stream, bool leaveOpen = false, CancellationToken cancellationToken = default);

    /// <summary>
    /// Put an object by key.
    /// </summary>
    /// <param name="meta">Object metadata.</param>
    /// <param name="stream">Stream to read the value from.</param>
    /// <param name="leaveOpen"><c>true</c> to not close the underlying stream when async method returns; otherwise, <c>false</c></param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object metadata.</returns>
    /// <exception cref="NatsObjException">There was an error calculating SHA digest.</exception>
    /// <exception cref="NatsJSApiException">Server responded with an error.</exception>
    ValueTask<ObjectMetadata> PutAsync(ObjectMetadata meta, Stream stream, bool leaveOpen = false, CancellationToken cancellationToken = default);

    /// <summary>
    /// Update object metadata
    /// </summary>
    /// <param name="key">Object key</param>
    /// <param name="meta">Object metadata</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object metadata</returns>
    /// <exception cref="NatsObjException">There is already an object with the same name</exception>
    ValueTask<ObjectMetadata> UpdateMetaAsync(string key, ObjectMetadata meta, CancellationToken cancellationToken = default);

    /// <summary>
    /// Add a link to another object
    /// </summary>
    /// <param name="link">Link name</param>
    /// <param name="target">Target object's name</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Metadata of the new link object</returns>
    ValueTask<ObjectMetadata> AddLinkAsync(string link, string target, CancellationToken cancellationToken = default);

    /// <summary>
    /// Add a link to another object
    /// </summary>
    /// <param name="link">Link name</param>
    /// <param name="target">Target object's metadata</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Metadata of the new link object</returns>
    ValueTask<ObjectMetadata> AddLinkAsync(string link, ObjectMetadata target, CancellationToken cancellationToken = default);

    /// <summary>
    /// Add a link to another object store
    /// </summary>
    /// <param name="link">Object's name to be linked</param>
    /// <param name="target">Target object store</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Metadata of the new link object</returns>
    /// <exception cref="NatsObjException">Object with the same name already exists</exception>
    ValueTask<ObjectMetadata> AddBucketLinkAsync(string link, INatsObjStore target, CancellationToken cancellationToken = default);

    /// <summary>
    /// Seal the object store. No further modifications will be allowed.
    /// </summary>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <exception cref="NatsObjException">Update operation failed</exception>
    ValueTask SealAsync(CancellationToken cancellationToken = default);

    /// <summary>
    /// Get object metadata by key.
    /// </summary>
    /// <param name="key">Object key.</param>
    /// <param name="showDeleted">Also retrieve deleted objects.</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object metadata.</returns>
    /// <exception cref="NatsObjException">Object was not found.</exception>
    ValueTask<ObjectMetadata> GetInfoAsync(string key, bool showDeleted = false, CancellationToken cancellationToken = default);

    /// <summary>
    /// List all the objects in this store.
    /// </summary>
    /// <param name="opts">List options</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>An async enumerable object metadata to be used in an <c>await foreach</c></returns>
    IAsyncEnumerable<ObjectMetadata> ListAsync(NatsObjListOpts? opts = default, CancellationToken cancellationToken = default);

    /// <summary>
    /// Retrieves run-time status about the backing store of the bucket.
    /// </summary>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>Object store status</returns>
    ValueTask<NatsObjStatus> GetStatusAsync(CancellationToken cancellationToken = default);

    /// <summary>
    /// Watch for changes in the underlying store and receive meta information updates.
    /// </summary>
    /// <param name="opts">Watch options</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <returns>An async enumerable object metadata to be used in an <c>await foreach</c></returns>
    IAsyncEnumerable<ObjectMetadata> WatchAsync(NatsObjWatchOpts? opts = default, CancellationToken cancellationToken = default);

    /// <summary>
    /// Delete an object by key.
    /// </summary>
    /// <param name="key">Object key.</param>
    /// <param name="cancellationToken">A <see cref="CancellationToken"/> used to cancel the API call.</param>
    /// <exception cref="NatsObjException">Object metadata was invalid or chunks can't be purged.</exception>
    ValueTask DeleteAsync(string key, CancellationToken cancellationToken = default);
}
```

{% endtab %}
{% endtabs %}


# Tutorials

Tutorials are provided to give guidance on commonly used aspects of NATS.

* [Advanced Connect and Custom Dialer in Go](https://docs.nats.io/using-nats/developer/tutorials/custom_dialer)
* [In-Depth JWT Guide](https://docs.nats.io/running-a-nats-service/nats_admin/security/jwt)


# Advanced Connect and Custom Dialer in Go

The Go NATS client features a [CustomDialer](https://godoc.org/github.com/nats-io/go-nats#CustomDialer) option which allows you to customize the connection logic against the NATS server without having to modify the internals of the client. For example, let's say that you want to make the client use the `context` package to use `DialContext` and be able to cancel connecting to NATS altogether with a deadline, you could then do define a Dialer implementation as follows:

```go
package main

import (
    "context"
    "log"
    "net"
    "time"

    "github.com/nats-io/nats.go"
)

type customDialer struct {
    ctx             context.Context
    nc              *nats.Conn
    connectTimeout  time.Duration
    connectTimeWait time.Duration
}

func (cd *customDialer) Dial(network, address string) (net.Conn, error) {
    ctx, cancel := context.WithTimeout(cd.ctx, cd.connectTimeout)
    defer cancel()

    for {
        log.Println("Attempting to connect to", address)
        if ctx.Err() != nil {
            return nil, ctx.Err()
        }

        select {
        case <-cd.ctx.Done():
            return nil, cd.ctx.Err()
        default:
            d := &net.Dialer{}
            if conn, err := d.DialContext(ctx, network, address); err == nil {
                log.Println("Connected to NATS successfully")
                return conn, nil
            } else {
                time.Sleep(cd.connectTimeWait)
            }
        }
    }
}
```

With the dialer implementation above, the NATS client will retry a number of times to connect to the NATS server until the context is no longer valid:

```go
func main() {
    // Parent context cancels connecting/reconnecting altogether.
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()

    var err error
    var nc *nats.Conn
    cd := &customDialer{
        ctx:             ctx,
        connectTimeout:  10 * time.Second,
        connectTimeWait: 1 * time.Second,
    }
    opts := []nats.Option{
        nats.SetCustomDialer(cd),
        nats.ReconnectWait(2 * time.Second),
        nats.ReconnectHandler(func(c *nats.Conn) {
            log.Println("Reconnected to", c.ConnectedUrl())
        }),
        nats.DisconnectHandler(func(c *nats.Conn) {
            log.Println("Disconnected from NATS")
        }),
        nats.ClosedHandler(func(c *nats.Conn) {
            log.Println("NATS connection is closed.")
        }),
        nats.NoReconnect(),
    }
    go func() {
        nc, err = nats.Connect("127.0.0.1:4222", opts...)
    }()

WaitForEstablishedConnection:
    for {
        if err != nil {
            log.Fatal(err)
        }

        // Wait for context to be canceled either by timeout
        // or because of establishing a connection...
        select {
        case <-ctx.Done():
            break WaitForEstablishedConnection
        default:
        }

        if nc == nil || !nc.IsConnected() {
            log.Println("Connection not ready")
            time.Sleep(200 * time.Millisecond)
            continue
        }
        break WaitForEstablishedConnection
    }
    if ctx.Err() != nil {
        log.Fatal(ctx.Err())
    }

    for {
        if nc.IsClosed() {
            break
        }
        if err := nc.Publish("hello", []byte("world")); err != nil {
            log.Println(err)
            time.Sleep(1 * time.Second)
            continue
        }
        log.Println("Published message")
        time.Sleep(1 * time.Second)
    }

    // Disconnect and flush pending messages
    if err := nc.Drain(); err != nil {
        log.Println(err)
    }
    log.Println("Disconnected")
}
```




---

[Next Page](/llms-full.txt/1)

