# Source: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html

Title: <no title> — kafka-python 2.3.0 documentation

URL Source: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html

Markdown Content:
[kafka-python](https://kafka-python.readthedocs.io/en/master/index.html)

_class_ kafka.KafkaClient[_**configs_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient "Link to this definition")
A network client for asynchronous request/response network I/O.

This is an internal class used to implement the user-facing producer and consumer clients.

This class is not thread-safe!

cluster[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.cluster "Link to this definition")
Local cache of cluster metadata, retrieved via MetadataRequests during [`poll()`](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.poll "kafka.KafkaClient.poll").

Type:
[<no title>](https://kafka-python.readthedocs.io/en/master/apidoc/ClusterMetadata.html)

Keyword Arguments:

* **bootstrap_servers** – ‘host[:port]’ string (or list of ‘host[:port]’ strings) that the client should contact to bootstrap initial cluster metadata. This does not have to be the full node list. It just needs to have at least one broker that will respond to a Metadata API Request. Default port is 9092. If no servers are specified, will default to localhost:9092.

* **client_id** (_str_) – a name for this client. This string is passed in each request to servers and can be used to identify specific server-side log entries that correspond to this client. Also submitted to GroupCoordinator for logging with respect to consumer group administration. Default: ‘kafka-python-{version}’

* **reconnect_backoff_ms** (_int_) – The amount of time in milliseconds to wait before attempting to reconnect to a given host. Default: 50.

* **reconnect_backoff_max_ms** (_int_) – The maximum amount of time in milliseconds to backoff/wait when reconnecting to a broker that has repeatedly failed to connect. If provided, the backoff per host will increase exponentially for each consecutive connection failure, up to this maximum. Once the maximum is reached, reconnection attempts will continue periodically with this fixed rate. To avoid connection storms, a randomization factor of 0.2 will be applied to the backoff resulting in a random range between 20% below and 20% above the computed value. Default: 30000.

* **request_timeout_ms** (_int_) – Client request timeout in milliseconds. Default: 30000.

* **connections_max_idle_ms** – Close idle connections after the number of milliseconds specified by this config. The broker closes idle connections after connections.max.idle.ms, so this avoids hitting unexpected socket disconnected errors on the client. Default: 540000

* **retry_backoff_ms** (_int_) – Milliseconds to backoff when retrying on errors. Default: 100.

* **max_in_flight_requests_per_connection** (_int_) – Requests are pipelined to kafka brokers up to this number of maximum requests per broker connection. Default: 5.

* **receive_buffer_bytes** (_int_) – The size of the TCP receive buffer (SO_RCVBUF) to use when reading data. Default: None (relies on system defaults). Java client defaults to 32768.

* **send_buffer_bytes** (_int_) – The size of the TCP send buffer (SO_SNDBUF) to use when sending data. Default: None (relies on system defaults). Java client defaults to 131072.

* **socket_options** (_list_) – List of tuple-arguments to socket.setsockopt to apply to broker connection sockets. Default: [(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)]

* **metadata_max_age_ms** (_int_) – The period of time in milliseconds after which we force a refresh of metadata even if we haven’t seen any partition leadership changes to proactively discover any new brokers or partitions. Default: 300000

* **allow_auto_create_topics** (_bool_) – Enable/disable auto topic creation on metadata request. Only available with api_version >= (0, 11). Default: True

* **security_protocol** (_str_) – Protocol used to communicate with brokers. Valid values are: PLAINTEXT, SSL, SASL_PLAINTEXT, SASL_SSL. Default: PLAINTEXT.

* **ssl_context** (_ssl.SSLContext_) – Pre-configured SSLContext for wrapping socket connections. If provided, all other ssl_* configurations will be ignored. Default: None.

* **ssl_check_hostname** (_bool_) – Flag to configure whether SSL handshake should verify that the certificate matches the broker’s hostname. Default: True.

* **ssl_cafile** (_str_) – Optional filename of CA file to use in certificate verification. Default: None.

* **ssl_certfile** (_str_) – Optional filename of file in PEM format containing the client certificate, as well as any CA certificates needed to establish the certificate’s authenticity. Default: None.

* **ssl_keyfile** (_str_) – Optional filename containing the client private key. Default: None.

* **ssl_password** (_str_) – Optional password to be used when loading the certificate chain. Default: None.

* **ssl_crlfile** (_str_) – Optional filename containing the CRL to check for certificate expiration. By default, no CRL check is done. When providing a file, only the leaf certificate will be checked against this CRL. The CRL can only be checked with Python 3.4+ or 2.7.9+. Default: None.

* **ssl_ciphers** (_str_) – optionally set the available ciphers for ssl connections. It should be a string in the OpenSSL cipher list format. If no cipher can be selected (because compile-time options or other configuration forbids use of all the specified ciphers), an ssl.SSLError will be raised. See ssl.SSLContext.set_ciphers

* **api_version** (_tuple_) –

Specify which Kafka API version to use. If set to None, the client will attempt to determine the broker version via ApiVersionsRequest API or, for brokers earlier than 0.10, probing various known APIs. Dynamic version checking is performed eagerly during **init** and can raise NoBrokersAvailableError if no connection was made before timeout (see api_version_auto_timeout_ms below). Different versions enable different functionality.

Examples

(3, 9) most recent broker release, enable all supported features (0, 10, 0) enables sasl authentication (0, 8, 0) enables basic functionality only

Default: None

* **api_version_auto_timeout_ms** (_int_) – number of milliseconds to throw a timeout exception from the constructor when checking the broker api version. Only applies if api_version set to None. Default: 2000

* **selector** (_selectors.BaseSelector_) – Provide a specific selector implementation to use for I/O multiplexing. Default: selectors.DefaultSelector

* **metrics** (_kafka.metrics.Metrics_) – Optionally provide a metrics instance for capturing network IO stats. Default: None.

* **metric_group_prefix** (_str_) – Prefix for metric names. Default: ‘’

* **sasl_mechanism** (_str_) – Authentication mechanism when security_protocol is configured for SASL_PLAINTEXT or SASL_SSL. Valid values are: PLAIN, GSSAPI, OAUTHBEARER, SCRAM-SHA-256, SCRAM-SHA-512.

* **sasl_plain_username** (_str_) – username for sasl PLAIN and SCRAM authentication. Required if sasl_mechanism is PLAIN or one of the SCRAM mechanisms.

* **sasl_plain_password** (_str_) – password for sasl PLAIN and SCRAM authentication. Required if sasl_mechanism is PLAIN or one of the SCRAM mechanisms.

* **sasl_kerberos_name** (_str_ _or_ _gssapi.Name_) – Constructed gssapi.Name for use with sasl mechanism handshake. If provided, sasl_kerberos_service_name and sasl_kerberos_domain name are ignored. Default: None.

* **sasl_kerberos_service_name** (_str_) – Service name to include in GSSAPI sasl mechanism handshake. Default: ‘kafka’

* **sasl_kerberos_domain_name** (_str_) – kerberos domain name to use in GSSAPI sasl mechanism handshake. Default: one of bootstrap servers

* **sasl_oauth_token_provider** (_kafka.sasl.oauth.AbstractTokenProvider_) – OAuthBearer token provider instance. Default: None

* **socks5_proxy** (_str_) – Socks5 proxy URL. Default: None

add_topic[_topic_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.add_topic)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.add_topic "Link to this definition")
Add a topic to the list of topics tracked via metadata.

Parameters:
**topic** (_str_) – topic to track

Returns:
resolves after metadata request/response

Return type:
Future

Raises:

* **TypeError** – if topic is not a string

* **ValueError** – if topic is invalid: must be chars (a-zA-Z0-9._-), and less than 250 length

api_version[_operation_, _max\_version=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.api_version)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.api_version "Link to this definition")
Find the latest version of the protocol operation supported by both this library and the broker.

This resolves to the lesser of either the latest api version this library supports, or the max version supported by the broker.

Parameters:
**operation** – A list of protocol operation versions from kafka.protocol.

Keyword Arguments:
**max_version** (_int_ _,_ _optional_) – Provide an alternate maximum api version to reflect limitations in user code.

Returns:
The highest api version number compatible between client and broker.

Return type:
int

Raises: IncompatibleBrokerVersion if no matching version is found

await_ready[_node\_id_, _timeout\_ms=30000_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.await_ready)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.await_ready "Link to this definition")
Invokes poll to discard pending disconnects, followed by client.ready and 0 or more client.poll invocations until the connection to node is ready, the timeoutMs expires or the connection fails.

It returns true if the call completes normally or false if the timeoutMs expires. If the connection fails, an IOException is thrown instead. Note that if the NetworkClient has been configured with a positive connection timeoutMs, it is possible for this method to raise an IOException for a previous connection which has recently disconnected.

This method is useful for implementing blocking behaviour on top of the non-blocking NetworkClient, use it with care.

bootstrap_connected()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.bootstrap_connected)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.bootstrap_connected "Link to this definition")
Return True if a bootstrap node is connected

check_version[_node\_id=None_, _timeout=None_, _**kwargs_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.check_version)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.check_version "Link to this definition")
Attempt to guess the version of a Kafka broker.

Keyword Arguments:

* **node_id** (_str_ _,_ _optional_) – Broker node id from cluster metadata. If None, attempts to connect to any available broker until version is identified. Default: None

* **timeout** (_num_ _,_ _optional_) – Maximum time in seconds to try to check broker version. If unable to identify version before timeout, raise error (see below). Default: api_version_auto_timeout_ms / 1000

Returns: version tuple, i.e. (3, 9), (2, 0), (0, 10, 2) etc

Raises:

* **NodeNotReadyError****(****if node_id is provided****)** –

* **NoBrokersAvailable****(****if node_id is None****)** –

close[_node\_id=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.close)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.close "Link to this definition")
Close one or all broker connections.

Parameters:
**node_id** (_int_ _,_ _optional_) – the id of the node to close

connected[_node\_id_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.connected)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.connected "Link to this definition")
Return True iff the node_id is connected.

connection_delay[_node\_id_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.connection_delay)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.connection_delay "Link to this definition")
Return the number of milliseconds to wait, based on the connection state, before attempting to send data. When connecting or disconnected, this respects the reconnect backoff time. When connected, returns a very large number to handle slow/stalled connections.

Parameters:
**node_id** (_int_) – The id of the node to check

Returns:
The number of milliseconds to wait.

Return type:
int

get_api_versions()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.get_api_versions)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.get_api_versions "Link to this definition")
Return the ApiVersions map, if available.

Note: Only available after bootstrap; requires broker version 0.10.0 or later.

Returns: a map of dict mapping {api_key : (min_version, max_version)}, or None if ApiVersion is not supported by the kafka cluster.

in_flight_request_count[_node\_id=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.in_flight_request_count)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.in_flight_request_count "Link to this definition")
Get the number of in-flight requests for a node or all nodes.

Parameters:
**node_id** (_int_ _,_ _optional_) – a specific node to check. If unspecified, return the total for all nodes

Returns:
pending in-flight requests for the node, or all nodes if None

Return type:
int

is_disconnected[_node\_id_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.is_disconnected)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.is_disconnected "Link to this definition")
Check whether the node connection has been disconnected or failed.

A disconnected node has either been closed or has failed. Connection failures are usually transient and can be resumed in the next ready() call, but there are cases where transient failures need to be caught and re-acted upon.

Parameters:
**node_id** (_int_) – the id of the node to check

Returns:
True iff the node exists and is disconnected

Return type:
bool

is_ready[_node\_id_, _metadata\_priority=True_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.is_ready)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.is_ready "Link to this definition")
Check whether a node is ready to send more requests.

In addition to connection-level checks, this method also is used to block additional requests from being sent during a metadata refresh.

Parameters:

* **node_id** (_int_) – id of the node to check

* **metadata_priority** (_bool_) – Mark node as not-ready if a metadata refresh is required. Default: True

Returns:
True if the node is ready and metadata is not refreshing

Return type:
bool

least_loaded_node()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.least_loaded_node)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.least_loaded_node "Link to this definition")
Choose the node with fewest outstanding requests, with fallbacks.

This method will prefer a node with an existing connection (not throttled) with no in-flight-requests. If no such node is found, a node will be chosen randomly from all nodes that are not throttled or “blacked out” (i.e., are not subject to a reconnect backoff). If no node metadata has been obtained, will return a bootstrap node.

Returns:
node_id or None if no suitable node was found

least_loaded_node_refresh_ms()[[source]](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.least_loaded_node_refresh_ms)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.least_loaded_node_refresh_ms "Link to this definition")
Return connection or throttle delay in milliseconds for next available node.

This method is used primarily for retry/backoff during metadata refresh during / after a cluster outage, in which there are no available nodes.

Returns:
delay_ms

Return type:
float

maybe_connect[_node\_id_, _wakeup=True_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.maybe_connect)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.maybe_connect "Link to this definition")
Queues a node for asynchronous connection during the next .poll()

poll[_timeout\_ms=None_, _future=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.poll)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.poll "Link to this definition")
Try to read and write to sockets.

This method will also attempt to complete node connections, refresh stale metadata, and run previously-scheduled tasks.

Parameters:

* **timeout_ms** (_int_ _,_ _optional_) – maximum amount of time to wait (in ms) for at least one response. Must be non-negative. The actual timeout will be the minimum of timeout, request timeout and metadata timeout. Default: request_timeout_ms

* **future** (_Future_ _,_ _optional_) – if provided, blocks until future.is_done

Returns:
responses received (can be empty)

Return type:
list

ready[_node\_id_, _metadata\_priority=True_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.ready)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.ready "Link to this definition")
Check whether a node is connected and ok to send more requests.

Parameters:

* **node_id** (_int_) – the id of the node to check

* **metadata_priority** (_bool_) – Mark node as not-ready if a metadata refresh is required. Default: True

Returns:
True if we are ready to send to the given node

Return type:
bool

send[_node\_id_, _request_, _wakeup=True_, _request\_timeout\_ms=None_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.send)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.send "Link to this definition")
Send a request to a specific node. Bytes are placed on an internal per-connection send-queue. Actual network I/O will be triggered in a subsequent call to .poll()

Parameters:

* **node_id** (_int_) – destination node

* **request** (_Struct_) – request object (not-encoded)

Keyword Arguments:

* **wakeup** (_bool_ _,_ _optional_) – optional flag to disable thread-wakeup.

* **request_timeout_ms** (_int_ _,_ _optional_) – Provide custom timeout in milliseconds. If response is not processed before timeout, client will fail the request and close the connection. Default: None (uses value from client configuration)

Raises:
**AssertionError** – if node_id is not in current cluster metadata

Returns:
resolves to Response struct or Error

Return type:
Future

set_topics[_topics_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.set_topics)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.set_topics "Link to this definition")
Set specific topics to track for metadata.

Parameters:
**topics** (_list_ _of_ _str_) – topics to check for metadata

Returns:
resolves after metadata request/response

Return type:
Future

throttle_delay[_node\_id_]([source)](https://kafka-python.readthedocs.io/en/master/_modules/kafka/client_async.html#KafkaClient.throttle_delay)[](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html#kafka.KafkaClient.throttle_delay "Link to this definition")
Return the number of milliseconds to wait until a broker is no longer throttled. When disconnected / connecting, returns 0.
