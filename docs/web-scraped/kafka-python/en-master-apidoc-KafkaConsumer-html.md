# Source: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

Title: <no title> — kafka-python 2.3.0 documentation

URL Source: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

Markdown Content:
[kafka-python](https://kafka-python.readthedocs.io/en/master/index.html)

_class_ kafka.KafkaConsumer[_*topics_, _**configs_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer "Link to this definition")
Consume records from a Kafka cluster.

The consumer will transparently handle the failure of servers in the Kafka cluster, and adapt as topic-partitions are created or migrate between brokers. It also interacts with the assigned kafka Group Coordinator node to allow multiple consumers to load balance consumption of topics (requires kafka >= 0.9.0.0).

The consumer is not thread safe and should not be shared across threads.

Parameters:
***topics** (_str_) – optional list of topics to subscribe to. If not set, call [`subscribe()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.subscribe "kafka.KafkaConsumer.subscribe") or [`assign()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.assign "kafka.KafkaConsumer.assign") before consuming records.

Keyword Arguments:

* **bootstrap_servers** – ‘host[:port]’ string (or list of ‘host[:port]’ strings) that the consumer should contact to bootstrap initial cluster metadata. This does not have to be the full node list. It just needs to have at least one broker that will respond to a Metadata API Request. Default port is 9092. If no servers are specified, will default to localhost:9092.

* **client_id** (_str_) – A name for this client. This string is passed in each request to servers and can be used to identify specific server-side log entries that correspond to this client. Also submitted to GroupCoordinator for logging with respect to consumer group administration. Default: ‘kafka-python-{version}’

* **group_id** (_str_ _or_ _None_) – The name of the consumer group to join for dynamic partition assignment (if enabled), and to use for fetching and committing offsets. If None, auto-partition assignment (via group coordinator) and offset commits are disabled. Default: None

* **group_instance_id** (_str_) – A unique identifier of the consumer instance provided by end user. Only non-empty strings are permitted. If set, the consumer is treated as a static member, which means that only one instance with this ID is allowed in the consumer group at any time. This can be used in combination with a larger session timeout to avoid group rebalances caused by transient unavailability (e.g. process restarts). If not set, the consumer will join the group as a dynamic member, which is the traditional behavior. Default: None

* **key_deserializer** (_callable_) – Any callable that takes a raw message key and returns a deserialized key.

* **value_deserializer** (_callable_) – Any callable that takes a raw message value and returns a deserialized value.

* **enable_incremental_fetch_sessions** – (bool): Use incremental fetch sessions when available / supported by kafka broker. See KIP-227. Default: True.

* **fetch_min_bytes** (_int_) – Minimum amount of data the server should return for a fetch request, otherwise wait up to fetch_max_wait_ms for more data to accumulate. Default: 1.

* **fetch_max_wait_ms** (_int_) – The maximum amount of time in milliseconds the server will block before answering the fetch request if there isn’t sufficient data to immediately satisfy the requirement given by fetch_min_bytes. Default: 500.

* **fetch_max_bytes** (_int_) – The maximum amount of data the server should return for a fetch request. This is not an absolute maximum, if the first message in the first non-empty partition of the fetch is larger than this value, the message will still be returned to ensure that the consumer can make progress. NOTE: consumer performs fetches to multiple brokers in parallel so memory usage will depend on the number of brokers containing partitions for the topic. Supported Kafka version >= 0.10.1.0. Default: 52428800 (50 MB).

* **max_partition_fetch_bytes** (_int_) – The maximum amount of data per-partition the server will return. The maximum total memory used for a request = #partitions * max_partition_fetch_bytes. This size must be at least as large as the maximum message size the server allows or else it is possible for the producer to send messages larger than the consumer can fetch. If that happens, the consumer can get stuck trying to fetch a large message on a certain partition. Default: 1048576.

* **request_timeout_ms** (_int_) – Client request timeout in milliseconds. Default: 305000.

* **retry_backoff_ms** (_int_) – Milliseconds to backoff when retrying on errors. Default: 100.

* **reconnect_backoff_ms** (_int_) – The amount of time in milliseconds to wait before attempting to reconnect to a given host. Default: 50.

* **reconnect_backoff_max_ms** (_int_) – The maximum amount of time in milliseconds to backoff/wait when reconnecting to a broker that has repeatedly failed to connect. If provided, the backoff per host will increase exponentially for each consecutive connection failure, up to this maximum. Once the maximum is reached, reconnection attempts will continue periodically with this fixed rate. To avoid connection storms, a randomization factor of 0.2 will be applied to the backoff resulting in a random range between 20% below and 20% above the computed value. Default: 30000.

* **max_in_flight_requests_per_connection** (_int_) – Requests are pipelined to kafka brokers up to this number of maximum requests per broker connection. Default: 5.

* **auto_offset_reset** (_str_) – A policy for resetting offsets on OffsetOutOfRange errors: ‘earliest’ will move to the oldest available message, ‘latest’ will move to the most recent. Any other value will raise the exception. Default: ‘latest’.

* **enable_auto_commit** (_bool_) – If True , the consumer’s offset will be periodically committed in the background. Default: True.

* **auto_commit_interval_ms** (_int_) – Number of milliseconds between automatic offset commits, if enable_auto_commit is True. Default: 5000.

* **default_offset_commit_callback** (_callable_) – Called as callback(offsets, response) response will be either an Exception or an OffsetCommitResponse struct. This callback can be used to trigger custom actions when a commit request completes.

* **check_crcs** (_bool_) – Automatically check the CRC32 of the records consumed. This ensures no on-the-wire or on-disk corruption to the messages occurred. This check adds some overhead, so it may be disabled in cases seeking extreme performance. Default: True

* **isolation_level** (_str_) – Configure KIP-98 transactional consumer by setting to ‘read_committed’. This will cause the consumer to skip records from aborted transactions. Default: ‘read_uncommitted’

* **allow_auto_create_topics** (_bool_) – Enable/disable auto topic creation on metadata request. Only available with api_version >= (0, 11). Default: True

* **metadata_max_age_ms** (_int_) – The period of time in milliseconds after which we force a refresh of metadata, even if we haven’t seen any partition leadership changes to proactively discover any new brokers or partitions. Default: 300000

* **partition_assignment_strategy** (_list_) – List of objects to use to distribute partition ownership amongst consumer instances when group management is used. Default: [RangePartitionAssignor, RoundRobinPartitionAssignor]

* **max_poll_records** (_int_) – The maximum number of records returned in a single call to [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "kafka.KafkaConsumer.poll"). Default: 500

* **max_poll_interval_ms** (_int_) – The maximum delay between invocations of [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "kafka.KafkaConsumer.poll") when using consumer group management. This places an upper bound on the amount of time that the consumer can be idle before fetching more records. If [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "kafka.KafkaConsumer.poll") is not called before expiration of this timeout, then the consumer is considered failed and the group will rebalance in order to reassign the partitions to another member. Default 300000

* **session_timeout_ms** (_int_) – The timeout used to detect failures when using Kafka’s group management facilities. The consumer sends periodic heartbeats to indicate its liveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker will remove this consumer from the group and initiate a rebalance. Note that the value must be in the allowable range as configured in the broker configuration by group.min.session.timeout.ms and group.max.session.timeout.ms. Default: 10000

* **heartbeat_interval_ms** (_int_) – The expected time in milliseconds between heartbeats to the consumer coordinator when using Kafka’s group management facilities. Heartbeats are used to ensure that the consumer’s session stays active and to facilitate rebalancing when new consumers join or leave the group. The value must be set lower than session_timeout_ms, but typically should be set no higher than 1/3 of that value. It can be adjusted even lower to control the expected time for normal rebalances. Default: 3000

* **receive_buffer_bytes** (_int_) – The size of the TCP receive buffer (SO_RCVBUF) to use when reading data. Default: None (relies on system defaults). The java client defaults to 32768.

* **send_buffer_bytes** (_int_) – The size of the TCP send buffer (SO_SNDBUF) to use when sending data. Default: None (relies on system defaults). The java client defaults to 131072.

* **socket_options** (_list_) – List of tuple-arguments to socket.setsockopt to apply to broker connection sockets. Default: [(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)]

* **consumer_timeout_ms** (_int_) – number of milliseconds to block during message iteration before raising StopIteration (i.e., ending the iterator). Default block forever [float(‘inf’)].

* **security_protocol** (_str_) – Protocol used to communicate with brokers. Valid values are: PLAINTEXT, SSL, SASL_PLAINTEXT, SASL_SSL. Default: PLAINTEXT.

* **ssl_context** (_ssl.SSLContext_) – Pre-configured SSLContext for wrapping socket connections. If provided, all other ssl_* configurations will be ignored. Default: None.

* **ssl_check_hostname** (_bool_) – Flag to configure whether ssl handshake should verify that the certificate matches the brokers hostname. Default: True.

* **ssl_cafile** (_str_) – Optional filename of ca file to use in certificate verification. Default: None.

* **ssl_certfile** (_str_) – Optional filename of file in pem format containing the client certificate, as well as any ca certificates needed to establish the certificate’s authenticity. Default: None.

* **ssl_keyfile** (_str_) – Optional filename containing the client private key. Default: None.

* **ssl_password** (_str_) – Optional password to be used when loading the certificate chain. Default: None.

* **ssl_crlfile** (_str_) – Optional filename containing the CRL to check for certificate expiration. By default, no CRL check is done. When providing a file, only the leaf certificate will be checked against this CRL. Default: None.

* **ssl_ciphers** (_str_) – optionally set the available ciphers for ssl connections. It should be a string in the OpenSSL cipher list format. If no cipher can be selected (because compile-time options or other configuration forbids use of all the specified ciphers), an ssl.SSLError will be raised. See ssl.SSLContext.set_ciphers

* **api_version** (_tuple_) –

Specify which Kafka API version to use. If set to None, the client will attempt to determine the broker version via ApiVersionsRequest API or, for brokers earlier than 0.10, probing various known APIs. Dynamic version checking is performed eagerly during **init** and can raise NoBrokersAvailableError if no connection was made before timeout (see api_version_auto_timeout_ms below). Different versions enable different functionality.

Examples

(3, 9) most recent broker release, enable all supported features (0, 11) enables message format v2 (internal) (0, 10, 0) enables sasl authentication and message format v1 (0, 9) enables full group coordination features with automatic

> partition assignment and rebalancing,

(0, 8, 2) enables kafka-storage offset commits with manual
partition assignment only,

(0, 8, 1) enables zookeeper-storage offset commits with manual
partition assignment only,

(0, 8, 0) enables basic functionality but requires manual
partition assignment and offset management.

Default: None

* **api_version_auto_timeout_ms** (_int_) – number of milliseconds to throw a timeout exception from the constructor when checking the broker api version. Only applies if api_version set to None. Default: 2000

* **connections_max_idle_ms** – Close idle connections after the number of milliseconds specified by this config. The broker closes idle connections after connections.max.idle.ms, so this avoids hitting unexpected socket disconnected errors on the client. Default: 540000

* **metric_reporters** (_list_) – A list of classes to use as metrics reporters. Implementing the AbstractMetricsReporter interface allows plugging in classes that will be notified of new metric creation. Default: []

* **metrics_enabled** (_bool_) – Whether to track metrics on this instance. Default True.

* **metrics_num_samples** (_int_) – The number of samples maintained to compute metrics. Default: 2

* **metrics_sample_window_ms** (_int_) – The maximum age in milliseconds of samples used to compute metrics. Default: 30000

* **selector** (_selectors.BaseSelector_) – Provide a specific selector implementation to use for I/O multiplexing. Default: selectors.DefaultSelector

* **exclude_internal_topics** (_bool_) – Whether records from internal topics (such as offsets) should be exposed to the consumer. If set to True the only way to receive records from an internal topic is subscribing to it. Requires 0.10+ Default: True

* **sasl_mechanism** (_str_) – Authentication mechanism when security_protocol is configured for SASL_PLAINTEXT or SASL_SSL. Valid values are: PLAIN, GSSAPI, OAUTHBEARER, SCRAM-SHA-256, SCRAM-SHA-512.

* **sasl_plain_username** (_str_) – username for sasl PLAIN and SCRAM authentication. Required if sasl_mechanism is PLAIN or one of the SCRAM mechanisms.

* **sasl_plain_password** (_str_) – password for sasl PLAIN and SCRAM authentication. Required if sasl_mechanism is PLAIN or one of the SCRAM mechanisms.

* **sasl_kerberos_name** (_str_ _or_ _gssapi.Name_) – Constructed gssapi.Name for use with sasl mechanism handshake. If provided, sasl_kerberos_service_name and sasl_kerberos_domain name are ignored. Default: None.

* **sasl_kerberos_service_name** (_str_) – Service name to include in GSSAPI sasl mechanism handshake. Default: ‘kafka’

* **sasl_kerberos_domain_name** (_str_) – kerberos domain name to use in GSSAPI sasl mechanism handshake. Default: one of bootstrap servers

* **sasl_oauth_token_provider** (_kafka.sasl.oauth.AbstractTokenProvider_) – OAuthBearer token provider instance. Default: None

* **socks5_proxy** (_str_) – Socks5 proxy URL. Default: None

* **kafka_client** (_callable_) – Custom class / callable for creating KafkaClient instances

assign[_partitions_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.assign)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.assign "Link to this definition")
Manually assign a list of TopicPartitions to this consumer.

Parameters:
**partitions** (_list_ _of_[_TopicPartition_](https://kafka-python.readthedocs.io/en/master/apidoc/TopicPartition.html#kafka.TopicPartition "kafka.TopicPartition")) – Assignment for this instance.

Raises:

* **IllegalStateError** – If consumer has already called

* **subscribe** –

Warning

It is not possible to use both manual partition assignment with [`assign()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.assign "kafka.KafkaConsumer.assign") and group assignment with [`subscribe()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.subscribe "kafka.KafkaConsumer.subscribe").

Note

This interface does not support incremental assignment and will replace the previous assignment (if there was one).

Note

Manual topic assignment through this method does not use the consumer’s group management functionality. As such, there will be no rebalance operation triggered when group membership or cluster and topic metadata change.

assignment()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.assignment)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.assignment "Link to this definition")
Get the TopicPartitions currently assigned to this consumer.

If partitions were directly assigned using [`assign()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.assign "kafka.KafkaConsumer.assign"), then this will simply return the same partitions that were previously assigned. If topics were subscribed using [`subscribe()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.subscribe "kafka.KafkaConsumer.subscribe"), then this will give the set of topic partitions currently assigned to the consumer (which may be None if the assignment hasn’t happened yet, or if the partitions are in the process of being reassigned).

Returns:
{TopicPartition, …}

Return type:
set

beginning_offsets[_partitions_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.beginning_offsets)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.beginning_offsets "Link to this definition")
Get the first offset for the given partitions.

This method does not change the current consumer position of the partitions.

Note

This method may block indefinitely if the partition does not exist.

Parameters:
**partitions** (_list_) – List of TopicPartition instances to fetch offsets for.

Returns:
The earliest available offsets for the given partitions.

Return type:
`{TopicPartition: int}`

Raises:

* **UnsupportedVersionError** – If the broker does not support looking up the offsets by timestamp.

* **KafkaTimeoutError** – If fetch failed in request_timeout_ms.

bootstrap_connected()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.bootstrap_connected)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.bootstrap_connected "Link to this definition")
Return True if the bootstrap is connected.

close[_autocommit=True_, _timeout\_ms=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.close)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.close "Link to this definition")
Close the consumer, waiting indefinitely for any needed cleanup.

Keyword Arguments:

* **autocommit** (_bool_) – If auto-commit is configured for this consumer, this optional flag causes the consumer to attempt to commit any pending consumed offsets prior to close. Default: True

* **timeout_ms** (_num_ _,_ _optional_) – Milliseconds to wait for auto-commit. Default: None

commit[_offsets=None_, _timeout\_ms=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.commit)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.commit "Link to this definition")
Commit offsets to kafka, blocking until success or error.

This commits offsets only to Kafka. The offsets committed using this API will be used on the first fetch after every rebalance and also on startup. As such, if you need to store offsets in anything other than Kafka, this API should not be used. To avoid re-processing the last message read if a consumer is restarted, the committed offset should be the next message your application should consume, i.e.: last_offset + 1.

Blocks until either the commit succeeds or an unrecoverable error is encountered (in which case it is thrown to the caller).

Currently only supports kafka-topic offset storage (not zookeeper).

Parameters:
**offsets** (_dict_ _,_ _optional_) – {TopicPartition: OffsetAndMetadata} dict to commit with the configured group_id. Defaults to currently consumed offsets for all subscribed partitions.

commit_async[_offsets=None_, _callback=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.commit_async)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.commit_async "Link to this definition")
Commit offsets to kafka asynchronously, optionally firing callback.

This commits offsets only to Kafka. The offsets committed using this API will be used on the first fetch after every rebalance and also on startup. As such, if you need to store offsets in anything other than Kafka, this API should not be used. To avoid re-processing the last message read if a consumer is restarted, the committed offset should be the next message your application should consume, i.e.: last_offset + 1.

This is an asynchronous call and will not block. Any errors encountered are either passed to the callback (if provided) or discarded.

Parameters:

* **offsets** (_dict_ _,_ _optional_) – {TopicPartition: OffsetAndMetadata} dict to commit with the configured group_id. Defaults to currently consumed offsets for all subscribed partitions.

* **callback** (_callable_ _,_ _optional_) – Called as callback(offsets, response) with response as either an Exception or an OffsetCommitResponse struct. This callback can be used to trigger custom actions when a commit request completes.

Returns:
kafka.future.Future

committed[_partition_, _metadata=False_, _timeout\_ms=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.committed)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.committed "Link to this definition")
Get the last committed offset for the given partition.

This offset will be used as the position for the consumer in the event of a failure.

This call will block to do a remote call to get the latest committed offsets from the server.

Parameters:

* **partition** ([_TopicPartition_](https://kafka-python.readthedocs.io/en/master/apidoc/TopicPartition.html#kafka.TopicPartition "kafka.TopicPartition")) – The partition to check.

* **metadata** (_bool_ _,_ _optional_) – If True, return OffsetAndMetadata struct instead of offset int. Default: False.

Returns:
The last committed offset (int or OffsetAndMetadata), or None if there was no prior commit.

Raises:

* **KafkaTimeoutError if timeout_ms provided** –

* **BrokerResponseErrors if OffsetFetchRequest raises an error.** –

end_offsets[_partitions_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.end_offsets)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.end_offsets "Link to this definition")
Get the last offset for the given partitions. The last offset of a partition is the offset of the upcoming message, i.e. the offset of the last available message + 1.

This method does not change the current consumer position of the partitions.

Note

This method may block indefinitely if the partition does not exist.

Parameters:
**partitions** (_list_) – List of TopicPartition instances to fetch offsets for.

Returns:
The end offsets for the given partitions.

Return type:
`{TopicPartition: int}`

Raises:

* **UnsupportedVersionError** – If the broker does not support looking up the offsets by timestamp.

* **KafkaTimeoutError** – If fetch failed in request_timeout_ms

highwater[_partition_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.highwater)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.highwater "Link to this definition")
Last known highwater offset for a partition.

A highwater offset is the offset that will be assigned to the next message that is produced. It may be useful for calculating lag, by comparing with the reported position. Note that both position and highwater refer to the _next_ offset – i.e., highwater offset is one greater than the newest available message.

Highwater offsets are returned in FetchResponse messages, so will not be available if no FetchRequests have been sent for this partition yet.

Parameters:
**partition** ([_TopicPartition_](https://kafka-python.readthedocs.io/en/master/apidoc/TopicPartition.html#kafka.TopicPartition "kafka.TopicPartition")) – Partition to check

Returns:
Offset if available

Return type:
int or None

metrics[_raw=False_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.metrics)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.metrics "Link to this definition")
Get metrics on consumer performance.

This is ported from the Java Consumer, for details see: [https://kafka.apache.org/documentation/#consumer_monitoring](https://kafka.apache.org/documentation/#consumer_monitoring)

Warning

This is an unstable interface. It may change in future releases without warning.

offsets_for_times[_timestamps_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.offsets_for_times)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.offsets_for_times "Link to this definition")
Look up the offsets for the given partitions by timestamp. The returned offset for each partition is the earliest offset whose timestamp is greater than or equal to the given timestamp in the corresponding partition.

This is a blocking call. The consumer does not have to be assigned the partitions.

If the message format version in a partition is before 0.10.0, i.e. the messages do not have timestamps, `None` will be returned for that partition. `None` will also be returned for the partition if there are no messages in it.

Note

This method may block indefinitely if the partition does not exist.

Parameters:
**timestamps** (_dict_) – `{TopicPartition: int}` mapping from partition to the timestamp to look up. Unit should be milliseconds since beginning of the epoch (midnight Jan 1, 1970 (UTC))

Returns:
mapping from partition to the timestamp and offset of the first message with timestamp greater than or equal to the target timestamp.

Return type:
`{TopicPartition: OffsetAndTimestamp}`

Raises:

* **ValueError** – If the target timestamp is negative

* **UnsupportedVersionError** – If the broker does not support looking up the offsets by timestamp.

* **KafkaTimeoutError** – If fetch failed in request_timeout_ms

partitions_for_topic[_topic_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.partitions_for_topic)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.partitions_for_topic "Link to this definition")
This method first checks the local metadata cache for information about the topic. If the topic is not found (either because the topic does not exist, the user is not authorized to view the topic, or the metadata cache is not populated), then it will issue a metadata update call to the cluster.

Parameters:
**topic** (_str_) – Topic to check.

Returns:
Partition ids

Return type:
set

pause[_*partitions_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.pause)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.pause "Link to this definition")
Suspend fetching from the requested partitions.

Future calls to [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "kafka.KafkaConsumer.poll") will not return any records from these partitions until they have been resumed using [`resume()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.resume "kafka.KafkaConsumer.resume").

Note: This method does not affect partition subscription. In particular, it does not cause a group rebalance when automatic assignment is used.

Parameters:
***partitions** ([_TopicPartition_](https://kafka-python.readthedocs.io/en/master/apidoc/TopicPartition.html#kafka.TopicPartition "kafka.TopicPartition")) – Partitions to pause.

paused()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.paused)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.paused "Link to this definition")
Get the partitions that were previously paused using [`pause()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.pause "kafka.KafkaConsumer.pause").

Returns:
{partition (TopicPartition), …}

Return type:
set

poll[_timeout\_ms=0_, _max\_records=None_, _update\_offsets=True_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.poll)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "Link to this definition")
Fetch data from assigned topics / partitions.

Records are fetched and returned in batches by topic-partition. On each poll, consumer will try to use the last consumed offset as the starting offset and fetch sequentially. The last consumed offset can be manually set through [`seek()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.seek "kafka.KafkaConsumer.seek") or automatically set as the last committed offset for the subscribed list of partitions.

Incompatible with iterator interface – use one or the other, not both.

Parameters:

* **timeout_ms** (_int_ _,_ _optional_) – Milliseconds spent waiting in poll if data is not available in the buffer. If 0, returns immediately with any records that are available currently in the buffer, else returns empty. Must not be negative. Default: 0

* **max_records** (_int_ _,_ _optional_) – The maximum number of records returned in a single call to [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "kafka.KafkaConsumer.poll"). Default: Inherit value from max_poll_records.

Returns:Topic to list of records since the last fetch for the
subscribed list of topics and partitions.

Return type:
dict

position[_partition_, _timeout\_ms=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.position)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.position "Link to this definition")
Get the offset of the next record that will be fetched

Parameters:
**partition** ([_TopicPartition_](https://kafka-python.readthedocs.io/en/master/apidoc/TopicPartition.html#kafka.TopicPartition "kafka.TopicPartition")) – Partition to check

Returns:
Offset or None

Return type:
int

resume[_*partitions_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.resume)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.resume "Link to this definition")
Resume fetching from the specified (paused) partitions.

Parameters:
***partitions** ([_TopicPartition_](https://kafka-python.readthedocs.io/en/master/apidoc/TopicPartition.html#kafka.TopicPartition "kafka.TopicPartition")) – Partitions to resume.

seek[_partition_, _offset_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.seek)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.seek "Link to this definition")
Manually specify the fetch offset for a TopicPartition.

Overrides the fetch offsets that the consumer will use on the next [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "kafka.KafkaConsumer.poll"). If this API is invoked for the same partition more than once, the latest offset will be used on the next [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.poll "kafka.KafkaConsumer.poll").

Note: You may lose data if this API is arbitrarily used in the middle of consumption to reset the fetch offsets.

Parameters:

* **partition** ([_TopicPartition_](https://kafka-python.readthedocs.io/en/master/apidoc/TopicPartition.html#kafka.TopicPartition "kafka.TopicPartition")) – Partition for seek operation

* **offset** (_int_) – Message offset in partition

Raises:
**AssertionError** – If offset is not an int >= 0; or if partition is not currently assigned.

seek_to_beginning[_*partitions_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.seek_to_beginning)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.seek_to_beginning "Link to this definition")
Seek to the oldest available offset for partitions.

Parameters:
***partitions** – Optionally provide specific TopicPartitions, otherwise default to all assigned partitions.

Raises:
**AssertionError** – If any partition is not currently assigned, or if no partitions are assigned.

seek_to_end[_*partitions_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.seek_to_end)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.seek_to_end "Link to this definition")
Seek to the most recent available offset for partitions.

Parameters:
***partitions** – Optionally provide specific TopicPartitions, otherwise default to all assigned partitions.

Raises:
**AssertionError** – If any partition is not currently assigned, or if no partitions are assigned.

subscribe(_topics=()_, _pattern=None_, _listener=None_)[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.subscribe)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.subscribe "Link to this definition")
Subscribe to a list of topics, or a topic regex pattern.

Partitions will be dynamically assigned via a group coordinator. Topic subscriptions are not incremental: this list will replace the current assignment (if there is one).

This method is incompatible with [`assign()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.assign "kafka.KafkaConsumer.assign").

Parameters:

* **topics** (_list_) – List of topics for subscription.

* **pattern** (_str_) – Pattern to match available topics. You must provide either topics or pattern, but not both.

* **listener** (_ConsumerRebalanceListener_) –

Optionally include listener callback, which will be called before and after each rebalance operation.

As part of group management, the consumer will keep track of the list of consumers that belong to a particular group and will trigger a rebalance operation if one of the following events trigger:

    *   Number of partitions change for any of the subscribed topics

    *   Topic is created or deleted

    *   An existing member of the consumer group dies

    *   A new member is added to the consumer group

When any of these events are triggered, the provided listener will be invoked first to indicate that the consumer’s assignment has been revoked, and then again when the new assignment has been received. Note that this listener will immediately override any listener set in a previous call to subscribe. It is guaranteed, however, that the partitions revoked/assigned through this interface are from topics subscribed in this call.

Raises:

* **IllegalStateError** – If called after previously calling [`assign()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.assign "kafka.KafkaConsumer.assign").

* **AssertionError** – If neither topics or pattern is provided.

* **TypeError** – If listener is not a ConsumerRebalanceListener.

subscription()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.subscription)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.subscription "Link to this definition")
Get the current topic subscription.

Returns:
{topic, …}

Return type:
set

topics()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.topics)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.topics "Link to this definition")
Get all topics the user is authorized to view. This will always issue a remote call to the cluster to fetch the latest information.

Returns:
topics

Return type:
set

unsubscribe()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/consumer/group.html#KafkaConsumer.unsubscribe)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer.unsubscribe "Link to this definition")
Unsubscribe from all topics and clear all assigned partitions.
