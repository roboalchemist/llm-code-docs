# Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.21.0

Title: semconv package - go.opentelemetry.io/otel/semconv/v1.21.0 - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.21.0

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
go.opentelemetry.io/otel
 
semconv
 
v1.21.0
semconv
package
Version: v1.40.0 Latest 
Published: Feb 2, 2026 
License: Apache-2.0, BSD-3-Clause 
Imports: 1 
Imported by: 606
Details
 Valid go.mod file 
 Redistributable license 
 Tagged version 
 Stable version 
Learn more about best practices
Repository
github.com/open-telemetry/opentelemetry-go
Links
 Open Source Insights
Jump to ...
README
Documentation
Source Files
 README ¶
Semconv v1.21.0

 Documentation ¶
Overview ¶

Package semconv implements OpenTelemetry semantic conventions.

OpenTelemetry semantic conventions are agreed standardized naming patterns for OpenTelemetry things. This package represents the v1.21.0 version of the OpenTelemetry semantic conventions.

Index ¶
Constants
Variables
func AWSDynamoDBAttributeDefinitions(val ...string) attribute.KeyValue
func AWSDynamoDBAttributesToGet(val ...string) attribute.KeyValue
func AWSDynamoDBConsistentRead(val bool) attribute.KeyValue
func AWSDynamoDBConsumedCapacity(val ...string) attribute.KeyValue
func AWSDynamoDBCount(val int) attribute.KeyValue
func AWSDynamoDBExclusiveStartTable(val string) attribute.KeyValue
func AWSDynamoDBGlobalSecondaryIndexUpdates(val ...string) attribute.KeyValue
func AWSDynamoDBGlobalSecondaryIndexes(val ...string) attribute.KeyValue
func AWSDynamoDBIndexName(val string) attribute.KeyValue
func AWSDynamoDBItemCollectionMetrics(val string) attribute.KeyValue
func AWSDynamoDBLimit(val int) attribute.KeyValue
func AWSDynamoDBLocalSecondaryIndexes(val ...string) attribute.KeyValue
func AWSDynamoDBProjection(val string) attribute.KeyValue
func AWSDynamoDBProvisionedReadCapacity(val float64) attribute.KeyValue
func AWSDynamoDBProvisionedWriteCapacity(val float64) attribute.KeyValue
func AWSDynamoDBScanForward(val bool) attribute.KeyValue
func AWSDynamoDBScannedCount(val int) attribute.KeyValue
func AWSDynamoDBSegment(val int) attribute.KeyValue
func AWSDynamoDBSelect(val string) attribute.KeyValue
func AWSDynamoDBTableCount(val int) attribute.KeyValue
func AWSDynamoDBTableNames(val ...string) attribute.KeyValue
func AWSDynamoDBTotalSegments(val int) attribute.KeyValue
func AWSECSClusterARN(val string) attribute.KeyValue
func AWSECSContainerARN(val string) attribute.KeyValue
func AWSECSTaskARN(val string) attribute.KeyValue
func AWSECSTaskFamily(val string) attribute.KeyValue
func AWSECSTaskRevision(val string) attribute.KeyValue
func AWSEKSClusterARN(val string) attribute.KeyValue
func AWSLambdaInvokedARN(val string) attribute.KeyValue
func AWSLogGroupARNs(val ...string) attribute.KeyValue
func AWSLogGroupNames(val ...string) attribute.KeyValue
func AWSLogStreamARNs(val ...string) attribute.KeyValue
func AWSLogStreamNames(val ...string) attribute.KeyValue
func AWSRequestID(val string) attribute.KeyValue
func AWSS3Bucket(val string) attribute.KeyValue
func AWSS3CopySource(val string) attribute.KeyValue
func AWSS3Delete(val string) attribute.KeyValue
func AWSS3Key(val string) attribute.KeyValue
func AWSS3PartNumber(val int) attribute.KeyValue
func AWSS3UploadID(val string) attribute.KeyValue
func BrowserBrands(val ...string) attribute.KeyValue
func BrowserLanguage(val string) attribute.KeyValue
func BrowserMobile(val bool) attribute.KeyValue
func BrowserPlatform(val string) attribute.KeyValue
func ClientAddress(val string) attribute.KeyValue
func ClientPort(val int) attribute.KeyValue
func ClientSocketAddress(val string) attribute.KeyValue
func ClientSocketPort(val int) attribute.KeyValue
func CloudAccountID(val string) attribute.KeyValue
func CloudAvailabilityZone(val string) attribute.KeyValue
func CloudRegion(val string) attribute.KeyValue
func CloudResourceID(val string) attribute.KeyValue
func CloudeventsEventID(val string) attribute.KeyValue
func CloudeventsEventSource(val string) attribute.KeyValue
func CloudeventsEventSpecVersion(val string) attribute.KeyValue
func CloudeventsEventSubject(val string) attribute.KeyValue
func CloudeventsEventType(val string) attribute.KeyValue
func CodeColumn(val int) attribute.KeyValue
func CodeFilepath(val string) attribute.KeyValue
func CodeFunction(val string) attribute.KeyValue
func CodeLineNumber(val int) attribute.KeyValue
func CodeNamespace(val string) attribute.KeyValue
func ContainerCommand(val string) attribute.KeyValue
func ContainerCommandArgs(val ...string) attribute.KeyValue
func ContainerCommandLine(val string) attribute.KeyValue
func ContainerID(val string) attribute.KeyValue
func ContainerImageID(val string) attribute.KeyValue
func ContainerImageName(val string) attribute.KeyValue
func ContainerImageTag(val string) attribute.KeyValue
func ContainerName(val string) attribute.KeyValue
func ContainerRuntime(val string) attribute.KeyValue
func DBCassandraCoordinatorDC(val string) attribute.KeyValue
func DBCassandraCoordinatorID(val string) attribute.KeyValue
func DBCassandraIdempotence(val bool) attribute.KeyValue
func DBCassandraPageSize(val int) attribute.KeyValue
func DBCassandraSpeculativeExecutionCount(val int) attribute.KeyValue
func DBCassandraTable(val string) attribute.KeyValue
func DBConnectionString(val string) attribute.KeyValue
func DBCosmosDBClientID(val string) attribute.KeyValue
func DBCosmosDBContainer(val string) attribute.KeyValue
func DBCosmosDBRequestCharge(val float64) attribute.KeyValue
func DBCosmosDBRequestContentLength(val int) attribute.KeyValue
func DBCosmosDBStatusCode(val int) attribute.KeyValue
func DBCosmosDBSubStatusCode(val int) attribute.KeyValue
func DBJDBCDriverClassname(val string) attribute.KeyValue
func DBMSSQLInstanceName(val string) attribute.KeyValue
func DBMongoDBCollection(val string) attribute.KeyValue
func DBName(val string) attribute.KeyValue
func DBOperation(val string) attribute.KeyValue
func DBRedisDBIndex(val int) attribute.KeyValue
func DBSQLTable(val string) attribute.KeyValue
func DBStatement(val string) attribute.KeyValue
func DBUser(val string) attribute.KeyValue
func DeploymentEnvironment(val string) attribute.KeyValue
func DestinationAddress(val string) attribute.KeyValue
func DestinationDomain(val string) attribute.KeyValue
func DestinationPort(val int) attribute.KeyValue
func DeviceID(val string) attribute.KeyValue
func DeviceManufacturer(val string) attribute.KeyValue
func DeviceModelIdentifier(val string) attribute.KeyValue
func DeviceModelName(val string) attribute.KeyValue
func EnduserID(val string) attribute.KeyValue
func EnduserRole(val string) attribute.KeyValue
func EnduserScope(val string) attribute.KeyValue
func EventName(val string) attribute.KeyValue
func ExceptionEscaped(val bool) attribute.KeyValue
func ExceptionMessage(val string) attribute.KeyValue
func ExceptionStacktrace(val string) attribute.KeyValue
func ExceptionType(val string) attribute.KeyValue
func FaaSColdstart(val bool) attribute.KeyValue
func FaaSCron(val string) attribute.KeyValue
func FaaSDocumentCollection(val string) attribute.KeyValue
func FaaSDocumentName(val string) attribute.KeyValue
func FaaSDocumentTime(val string) attribute.KeyValue
func FaaSInstance(val string) attribute.KeyValue
func FaaSInvocationID(val string) attribute.KeyValue
func FaaSInvokedName(val string) attribute.KeyValue
func FaaSInvokedRegion(val string) attribute.KeyValue
func FaaSMaxMemory(val int) attribute.KeyValue
func FaaSName(val string) attribute.KeyValue
func FaaSTime(val string) attribute.KeyValue
func FaaSVersion(val string) attribute.KeyValue
func FeatureFlagKey(val string) attribute.KeyValue
func FeatureFlagProviderName(val string) attribute.KeyValue
func FeatureFlagVariant(val string) attribute.KeyValue
func GCPCloudRunJobExecution(val string) attribute.KeyValue
func GCPCloudRunJobTaskIndex(val int) attribute.KeyValue
func GCPGceInstanceHostname(val string) attribute.KeyValue
func GCPGceInstanceName(val string) attribute.KeyValue
func GraphqlDocument(val string) attribute.KeyValue
func GraphqlOperationName(val string) attribute.KeyValue
func HTTPMethod(val string) attribute.KeyValue
func HTTPRequestBodySize(val int) attribute.KeyValue
func HTTPRequestContentLength(val int) attribute.KeyValue
func HTTPRequestMethodOriginal(val string) attribute.KeyValue
func HTTPResendCount(val int) attribute.KeyValue
func HTTPResponseBodySize(val int) attribute.KeyValue
func HTTPResponseContentLength(val int) attribute.KeyValue
func HTTPResponseStatusCode(val int) attribute.KeyValue
func HTTPRoute(val string) attribute.KeyValue
func HTTPScheme(val string) attribute.KeyValue
func HTTPStatusCode(val int) attribute.KeyValue
func HTTPTarget(val string) attribute.KeyValue
func HTTPURL(val string) attribute.KeyValue
func HerokuAppID(val string) attribute.KeyValue
func HerokuReleaseCommit(val string) attribute.KeyValue
func HerokuReleaseCreationTimestamp(val string) attribute.KeyValue
func HostID(val string) attribute.KeyValue
func HostImageID(val string) attribute.KeyValue
func HostImageName(val string) attribute.KeyValue
func HostImageVersion(val string) attribute.KeyValue
func HostName(val string) attribute.KeyValue
func HostType(val string) attribute.KeyValue
func K8SClusterName(val string) attribute.KeyValue
func K8SClusterUID(val string) attribute.KeyValue
func K8SContainerName(val string) attribute.KeyValue
func K8SContainerRestartCount(val int) attribute.KeyValue
func K8SCronJobName(val string) attribute.KeyValue
func K8SCronJobUID(val string) attribute.KeyValue
func K8SDaemonSetName(val string) attribute.KeyValue
func K8SDaemonSetUID(val string) attribute.KeyValue
func K8SDeploymentName(val string) attribute.KeyValue
func K8SDeploymentUID(val string) attribute.KeyValue
func K8SJobName(val string) attribute.KeyValue
func K8SJobUID(val string) attribute.KeyValue
func K8SNamespaceName(val string) attribute.KeyValue
func K8SNodeName(val string) attribute.KeyValue
func K8SNodeUID(val string) attribute.KeyValue
func K8SPodName(val string) attribute.KeyValue
func K8SPodUID(val string) attribute.KeyValue
func K8SReplicaSetName(val string) attribute.KeyValue
func K8SReplicaSetUID(val string) attribute.KeyValue
func K8SStatefulSetName(val string) attribute.KeyValue
func K8SStatefulSetUID(val string) attribute.KeyValue
func LogFileName(val string) attribute.KeyValue
func LogFileNameResolved(val string) attribute.KeyValue
func LogFilePath(val string) attribute.KeyValue
func LogFilePathResolved(val string) attribute.KeyValue
func LogRecordUID(val string) attribute.KeyValue
func MessageCompressedSize(val int) attribute.KeyValue
func MessageID(val int) attribute.KeyValue
func MessageUncompressedSize(val int) attribute.KeyValue
func MessagingBatchMessageCount(val int) attribute.KeyValue
func MessagingClientID(val string) attribute.KeyValue
func MessagingDestinationAnonymous(val bool) attribute.KeyValue
func MessagingDestinationName(val string) attribute.KeyValue
func MessagingDestinationTemplate(val string) attribute.KeyValue
func MessagingDestinationTemporary(val bool) attribute.KeyValue
func MessagingKafkaConsumerGroup(val string) attribute.KeyValue
func MessagingKafkaDestinationPartition(val int) attribute.KeyValue
func MessagingKafkaMessageKey(val string) attribute.KeyValue
func MessagingKafkaMessageOffset(val int) attribute.KeyValue
func MessagingKafkaMessageTombstone(val bool) attribute.KeyValue
func MessagingMessageConversationID(val string) attribute.KeyValue
func MessagingMessageID(val string) attribute.KeyValue
func MessagingMessagePayloadCompressedSizeBytes(val int) attribute.KeyValue
func MessagingMessagePayloadSizeBytes(val int) attribute.KeyValue
func MessagingRabbitmqDestinationRoutingKey(val string) attribute.KeyValue
func MessagingRocketmqClientGroup(val string) attribute.KeyValue
func MessagingRocketmqMessageDelayTimeLevel(val int) attribute.KeyValue
func MessagingRocketmqMessageDeliveryTimestamp(val int) attribute.KeyValue
func MessagingRocketmqMessageGroup(val string) attribute.KeyValue
func MessagingRocketmqMessageKeys(val ...string) attribute.KeyValue
func MessagingRocketmqMessageTag(val string) attribute.KeyValue
func MessagingRocketmqNamespace(val string) attribute.KeyValue
func MessagingSystem(val string) attribute.KeyValue
func NetHostName(val string) attribute.KeyValue
func NetHostPort(val int) attribute.KeyValue
func NetPeerName(val string) attribute.KeyValue
func NetPeerPort(val int) attribute.KeyValue
func NetProtocolName(val string) attribute.KeyValue
func NetProtocolVersion(val string) attribute.KeyValue
func NetSockHostAddr(val string) attribute.KeyValue
func NetSockHostPort(val int) attribute.KeyValue
func NetSockPeerAddr(val string) attribute.KeyValue
func NetSockPeerName(val string) attribute.KeyValue
func NetSockPeerPort(val int) attribute.KeyValue
func NetworkCarrierIcc(val string) attribute.KeyValue
func NetworkCarrierMcc(val string) attribute.KeyValue
func NetworkCarrierMnc(val string) attribute.KeyValue
func NetworkCarrierName(val string) attribute.KeyValue
func NetworkProtocolName(val string) attribute.KeyValue
func NetworkProtocolVersion(val string) attribute.KeyValue
func OSDescription(val string) attribute.KeyValue
func OSName(val string) attribute.KeyValue
func OSVersion(val string) attribute.KeyValue
func OTelLibraryName(val string) attribute.KeyValue
func OTelLibraryVersion(val string) attribute.KeyValue
func OTelScopeName(val string) attribute.KeyValue
func OTelScopeVersion(val string) attribute.KeyValue
func OTelStatusDescription(val string) attribute.KeyValue
func PeerService(val string) attribute.KeyValue
func Pool(val string) attribute.KeyValue
func ProcessCommand(val string) attribute.KeyValue
func ProcessCommandArgs(val ...string) attribute.KeyValue
func ProcessCommandLine(val string) attribute.KeyValue
func ProcessExecutableName(val string) attribute.KeyValue
func ProcessExecutablePath(val string) attribute.KeyValue
func ProcessOwner(val string) attribute.KeyValue
func ProcessPID(val int) attribute.KeyValue
func ProcessParentPID(val int) attribute.KeyValue
func ProcessRuntimeDescription(val string) attribute.KeyValue
func ProcessRuntimeName(val string) attribute.KeyValue
func ProcessRuntimeVersion(val string) attribute.KeyValue
func RPCJsonrpcErrorCode(val int) attribute.KeyValue
func RPCJsonrpcErrorMessage(val string) attribute.KeyValue
func RPCJsonrpcRequestID(val string) attribute.KeyValue
func RPCJsonrpcVersion(val string) attribute.KeyValue
func RPCMethod(val string) attribute.KeyValue
func RPCService(val string) attribute.KeyValue
func ServerAddress(val string) attribute.KeyValue
func ServerPort(val int) attribute.KeyValue
func ServerSocketAddress(val string) attribute.KeyValue
func ServerSocketDomain(val string) attribute.KeyValue
func ServerSocketPort(val int) attribute.KeyValue
func ServiceInstanceID(val string) attribute.KeyValue
func ServiceName(val string) attribute.KeyValue
func ServiceNamespace(val string) attribute.KeyValue
func ServiceVersion(val string) attribute.KeyValue
func SourceAddress(val string) attribute.KeyValue
func SourceDomain(val string) attribute.KeyValue
func SourcePort(val int) attribute.KeyValue
func TelemetryAutoVersion(val string) attribute.KeyValue
func TelemetrySDKName(val string) attribute.KeyValue
func TelemetrySDKVersion(val string) attribute.KeyValue
func ThreadID(val int) attribute.KeyValue
func ThreadName(val string) attribute.KeyValue
func URLFragment(val string) attribute.KeyValue
func URLFull(val string) attribute.KeyValue
func URLPath(val string) attribute.KeyValue
func URLQuery(val string) attribute.KeyValue
func URLScheme(val string) attribute.KeyValue
func UserAgentOriginal(val string) attribute.KeyValue
func WebEngineDescription(val string) attribute.KeyValue
func WebEngineName(val string) attribute.KeyValue
func WebEngineVersion(val string) attribute.KeyValue
Constants ¶
View Source
const (
	// ClientAddressKey is the attribute Key conforming to the "client.address"
	// semantic conventions. It represents the client address - unix domain
	// socket name, IPv4 or IPv6 address.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/tmp/my.sock', '10.1.2.80'
	// Note: When observed from the server side, and when communicating through
	// an intermediary, `client.address` SHOULD represent client address behind
	// any intermediaries (e.g. proxies) if it's available.
	ClientAddressKey = attribute.Key("client.address")

	// ClientPortKey is the attribute Key conforming to the "client.port"
	// semantic conventions. It represents the client port number
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 65123
	// Note: When observed from the server side, and when communicating through
	// an intermediary, `client.port` SHOULD represent client port behind any
	// intermediaries (e.g. proxies) if it's available.
	ClientPortKey = attribute.Key("client.port")

	// ClientSocketAddressKey is the attribute Key conforming to the
	// "client.socket.address" semantic conventions. It represents the
	// immediate client peer address - unix domain socket name, IPv4 or IPv6
	// address.
	//
	// Type: string
	// RequirementLevel: Recommended (If different than `client.address`.)
	// Stability: stable
	// Examples: '/tmp/my.sock', '127.0.0.1'
	ClientSocketAddressKey = attribute.Key("client.socket.address")

	// ClientSocketPortKey is the attribute Key conforming to the
	// "client.socket.port" semantic conventions. It represents the immediate
	// client peer port number
	//
	// Type: int
	// RequirementLevel: Recommended (If different than `client.port`.)
	// Stability: stable
	// Examples: 35555
	ClientSocketPortKey = attribute.Key("client.socket.port")
)

These attributes may be used to describe the client in a connection-based network interaction where there is one side that initiates the connection (the client is the side that initiates the connection). This covers all TCP network interactions since TCP is connection-based and one side initiates the connection (an exception is made for peer-to-peer communication over TCP where the "user-facing" surface of the protocol / API does not expose a clear notion of client and server). This also covers UDP network interactions where one side initiates the interaction, e.g. QUIC (HTTP/3) and DNS.

View Source
const (
	// HTTPMethodKey is the attribute Key conforming to the "http.method"
	// semantic conventions. It represents the deprecated, use
	// `http.request.method` instead.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 'GET', 'POST', 'HEAD'
	HTTPMethodKey = attribute.Key("http.method")

	// HTTPStatusCodeKey is the attribute Key conforming to the
	// "http.status_code" semantic conventions. It represents the deprecated,
	// use `http.response.status_code` instead.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 200
	HTTPStatusCodeKey = attribute.Key("http.status_code")

	// HTTPSchemeKey is the attribute Key conforming to the "http.scheme"
	// semantic conventions. It represents the deprecated, use `url.scheme`
	// instead.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 'http', 'https'
	HTTPSchemeKey = attribute.Key("http.scheme")

	// HTTPURLKey is the attribute Key conforming to the "http.url" semantic
	// conventions. It represents the deprecated, use `url.full` instead.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 'https://www.foo.bar/search?q=OpenTelemetry#SemConv'
	HTTPURLKey = attribute.Key("http.url")

	// HTTPTargetKey is the attribute Key conforming to the "http.target"
	// semantic conventions. It represents the deprecated, use `url.path` and
	// `url.query` instead.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: '/search?q=OpenTelemetry#SemConv'
	HTTPTargetKey = attribute.Key("http.target")

	// HTTPRequestContentLengthKey is the attribute Key conforming to the
	// "http.request_content_length" semantic conventions. It represents the
	// deprecated, use `http.request.body.size` instead.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 3495
	HTTPRequestContentLengthKey = attribute.Key("http.request_content_length")

	// HTTPResponseContentLengthKey is the attribute Key conforming to the
	// "http.response_content_length" semantic conventions. It represents the
	// deprecated, use `http.response.body.size` instead.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 3495
	HTTPResponseContentLengthKey = attribute.Key("http.response_content_length")
)

Describes deprecated HTTP attributes.

View Source
const (
	// NetSockPeerNameKey is the attribute Key conforming to the
	// "net.sock.peer.name" semantic conventions. It represents the deprecated,
	// use `server.socket.domain` on client spans.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: '/var/my.sock'
	NetSockPeerNameKey = attribute.Key("net.sock.peer.name")

	// NetSockPeerAddrKey is the attribute Key conforming to the
	// "net.sock.peer.addr" semantic conventions. It represents the deprecated,
	// use `server.socket.address` on client spans and `client.socket.address`
	// on server spans.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: '192.168.0.1'
	NetSockPeerAddrKey = attribute.Key("net.sock.peer.addr")

	// NetSockPeerPortKey is the attribute Key conforming to the
	// "net.sock.peer.port" semantic conventions. It represents the deprecated,
	// use `server.socket.port` on client spans and `client.socket.port` on
	// server spans.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 65531
	NetSockPeerPortKey = attribute.Key("net.sock.peer.port")

	// NetPeerNameKey is the attribute Key conforming to the "net.peer.name"
	// semantic conventions. It represents the deprecated, use `server.address`
	// on client spans and `client.address` on server spans.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 'example.com'
	NetPeerNameKey = attribute.Key("net.peer.name")

	// NetPeerPortKey is the attribute Key conforming to the "net.peer.port"
	// semantic conventions. It represents the deprecated, use `server.port` on
	// client spans and `client.port` on server spans.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 8080
	NetPeerPortKey = attribute.Key("net.peer.port")

	// NetHostNameKey is the attribute Key conforming to the "net.host.name"
	// semantic conventions. It represents the deprecated, use
	// `server.address`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 'example.com'
	NetHostNameKey = attribute.Key("net.host.name")

	// NetHostPortKey is the attribute Key conforming to the "net.host.port"
	// semantic conventions. It represents the deprecated, use `server.port`.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 8080
	NetHostPortKey = attribute.Key("net.host.port")

	// NetSockHostAddrKey is the attribute Key conforming to the
	// "net.sock.host.addr" semantic conventions. It represents the deprecated,
	// use `server.socket.address`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: '/var/my.sock'
	NetSockHostAddrKey = attribute.Key("net.sock.host.addr")

	// NetSockHostPortKey is the attribute Key conforming to the
	// "net.sock.host.port" semantic conventions. It represents the deprecated,
	// use `server.socket.port`.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 8080
	NetSockHostPortKey = attribute.Key("net.sock.host.port")

	// NetTransportKey is the attribute Key conforming to the "net.transport"
	// semantic conventions. It represents the deprecated, use
	// `network.transport`.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: deprecated
	NetTransportKey = attribute.Key("net.transport")

	// NetProtocolNameKey is the attribute Key conforming to the
	// "net.protocol.name" semantic conventions. It represents the deprecated,
	// use `network.protocol.name`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 'amqp', 'http', 'mqtt'
	NetProtocolNameKey = attribute.Key("net.protocol.name")

	// NetProtocolVersionKey is the attribute Key conforming to the
	// "net.protocol.version" semantic conventions. It represents the
	// deprecated, use `network.protocol.version`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: '3.1.1'
	NetProtocolVersionKey = attribute.Key("net.protocol.version")

	// NetSockFamilyKey is the attribute Key conforming to the
	// "net.sock.family" semantic conventions. It represents the deprecated,
	// use `network.transport` and `network.type`.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: deprecated
	NetSockFamilyKey = attribute.Key("net.sock.family")
)

These attributes may be used for any network related operation.

View Source
const (
	// DestinationDomainKey is the attribute Key conforming to the
	// "destination.domain" semantic conventions. It represents the domain name
	// of the destination system.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'foo.example.com'
	// Note: This value may be a host name, a fully qualified domain name, or
	// another host naming format.
	DestinationDomainKey = attribute.Key("destination.domain")

	// DestinationAddressKey is the attribute Key conforming to the
	// "destination.address" semantic conventions. It represents the peer
	// address, for example IP address or UNIX socket name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '10.5.3.2'
	DestinationAddressKey = attribute.Key("destination.address")

	// DestinationPortKey is the attribute Key conforming to the
	// "destination.port" semantic conventions. It represents the peer port
	// number
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 3389, 2888
	DestinationPortKey = attribute.Key("destination.port")
)

These attributes may be used to describe the receiver of a network exchange/packet. These should be used when there is no client/server relationship between the two sides, or when that relationship is unknown. This covers low-level network interactions (e.g. packet tracing) where you don't know if there was a connection or which side initiated it. This also covers unidirectional UDP flows and peer-to-peer communication where the "user-facing" surface of the protocol / API does not expose a clear notion of client and server.

View Source
const (
	// HTTPRequestMethodKey is the attribute Key conforming to the
	// "http.request.method" semantic conventions. It represents the hTTP
	// request method.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'GET', 'POST', 'HEAD'
	// Note: HTTP request method value SHOULD be "known" to the
	// instrumentation.
	// By default, this convention defines "known" methods as the ones listed
	// in [RFC9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-methods)
	// and the PATCH method defined in
	// [RFC5789](https://www.rfc-editor.org/rfc/rfc5789.html).
	//
	// If the HTTP request method is not known to instrumentation, it MUST set
	// the `http.request.method` attribute to `_OTHER` and, except if reporting
	// a metric, MUST
	// set the exact method received in the request line as value of the
	// `http.request.method_original` attribute.
	//
	// If the HTTP instrumentation could end up converting valid HTTP request
	// methods to `_OTHER`, then it MUST provide a way to override
	// the list of known HTTP methods. If this override is done via environment
	// variable, then the environment variable MUST be named
	// OTEL_INSTRUMENTATION_HTTP_KNOWN_METHODS and support a comma-separated
	// list of case-sensitive known HTTP methods
	// (this list MUST be a full override of the default known method, it is
	// not a list of known methods in addition to the defaults).
	//
	// HTTP method names are case-sensitive and `http.request.method` attribute
	// value MUST match a known HTTP method name exactly.
	// Instrumentations for specific web frameworks that consider HTTP methods
	// to be case insensitive, SHOULD populate a canonical equivalent.
	// Tracing instrumentations that do so, MUST also set
	// `http.request.method_original` to the original value.
	HTTPRequestMethodKey = attribute.Key("http.request.method")

	// HTTPResponseStatusCodeKey is the attribute Key conforming to the
	// "http.response.status_code" semantic conventions. It represents the
	// [HTTP response status
	// code](https://tools.ietf.org/html/rfc7231#section-6).
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (If and only if one was
	// received/sent.)
	// Stability: stable
	// Examples: 200
	HTTPResponseStatusCodeKey = attribute.Key("http.response.status_code")
)

Describes HTTP attributes.

View Source
const (
	// EventNameKey is the attribute Key conforming to the "event.name"
	// semantic conventions. It represents the name identifies the event.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'click', 'exception'
	EventNameKey = attribute.Key("event.name")

	// EventDomainKey is the attribute Key conforming to the "event.domain"
	// semantic conventions. It represents the domain identifies the business
	// context for the events.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	// Note: Events across different domains may have same `event.name`, yet be
	// unrelated events.
	EventDomainKey = attribute.Key("event.domain")
)

Attributes for Events represented using Log Records.

View Source
const (
	// LogFileNameKey is the attribute Key conforming to the "log.file.name"
	// semantic conventions. It represents the basename of the file.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'audit.log'
	LogFileNameKey = attribute.Key("log.file.name")

	// LogFilePathKey is the attribute Key conforming to the "log.file.path"
	// semantic conventions. It represents the full path to the file.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/var/log/mysql/audit.log'
	LogFilePathKey = attribute.Key("log.file.path")

	// LogFileNameResolvedKey is the attribute Key conforming to the
	// "log.file.name_resolved" semantic conventions. It represents the
	// basename of the file, with symlinks resolved.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'uuid.log'
	LogFileNameResolvedKey = attribute.Key("log.file.name_resolved")

	// LogFilePathResolvedKey is the attribute Key conforming to the
	// "log.file.path_resolved" semantic conventions. It represents the full
	// path to the file, with symlinks resolved.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/var/lib/docker/uuid.log'
	LogFilePathResolvedKey = attribute.Key("log.file.path_resolved")
)

A file to which log was emitted.

View Source
const (
	// TypeKey is the attribute Key conforming to the "type" semantic
	// conventions. It represents the type of memory.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'heap', 'non_heap'
	TypeKey = attribute.Key("type")

	// PoolKey is the attribute Key conforming to the "pool" semantic
	// conventions. It represents the name of the memory pool.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'G1 Old Gen', 'G1 Eden space', 'G1 Survivor Space'
	// Note: Pool names are generally obtained via
	// [MemoryPoolMXBean#getName()](https://docs.oracle.com/en/java/javase/11/docs/api/java.management/java/lang/management/MemoryPoolMXBean.html#getName()).
	PoolKey = attribute.Key("pool")
)

Describes JVM memory metric attributes.

View Source
const (
	// ServerAddressKey is the attribute Key conforming to the "server.address"
	// semantic conventions. It represents the logical server hostname, matches
	// server FQDN if available, and IP or socket address if FQDN is not known.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'example.com'
	ServerAddressKey = attribute.Key("server.address")

	// ServerPortKey is the attribute Key conforming to the "server.port"
	// semantic conventions. It represents the logical server port number
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 80, 8080, 443
	ServerPortKey = attribute.Key("server.port")

	// ServerSocketDomainKey is the attribute Key conforming to the
	// "server.socket.domain" semantic conventions. It represents the domain
	// name of an immediate peer.
	//
	// Type: string
	// RequirementLevel: Recommended (If different than `server.address`.)
	// Stability: stable
	// Examples: 'proxy.example.com'
	// Note: Typically observed from the client side, and represents a proxy or
	// other intermediary domain name.
	ServerSocketDomainKey = attribute.Key("server.socket.domain")

	// ServerSocketAddressKey is the attribute Key conforming to the
	// "server.socket.address" semantic conventions. It represents the physical
	// server IP address or Unix socket address. If set from the client, should
	// simply use the socket's peer address, and not attempt to find any actual
	// server IP (i.e., if set from client, this may represent some proxy
	// server instead of the logical server).
	//
	// Type: string
	// RequirementLevel: Recommended (If different than `server.address`.)
	// Stability: stable
	// Examples: '10.5.3.2'
	ServerSocketAddressKey = attribute.Key("server.socket.address")

	// ServerSocketPortKey is the attribute Key conforming to the
	// "server.socket.port" semantic conventions. It represents the physical
	// server port.
	//
	// Type: int
	// RequirementLevel: Recommended (If different than `server.port`.)
	// Stability: stable
	// Examples: 16456
	ServerSocketPortKey = attribute.Key("server.socket.port")
)

These attributes may be used to describe the server in a connection-based network interaction where there is one side that initiates the connection (the client is the side that initiates the connection). This covers all TCP network interactions since TCP is connection-based and one side initiates the connection (an exception is made for peer-to-peer communication over TCP where the "user-facing" surface of the protocol / API does not expose a clear notion of client and server). This also covers UDP network interactions where one side initiates the interaction, e.g. QUIC (HTTP/3) and DNS.

View Source
const (
	// SourceDomainKey is the attribute Key conforming to the "source.domain"
	// semantic conventions. It represents the domain name of the source
	// system.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'foo.example.com'
	// Note: This value may be a host name, a fully qualified domain name, or
	// another host naming format.
	SourceDomainKey = attribute.Key("source.domain")

	// SourceAddressKey is the attribute Key conforming to the "source.address"
	// semantic conventions. It represents the source address, for example IP
	// address or Unix socket name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '10.5.3.2'
	SourceAddressKey = attribute.Key("source.address")

	// SourcePortKey is the attribute Key conforming to the "source.port"
	// semantic conventions. It represents the source port number
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 3389, 2888
	SourcePortKey = attribute.Key("source.port")
)

These attributes may be used to describe the sender of a network exchange/packet. These should be used when there is no client/server relationship between the two sides, or when that relationship is unknown. This covers low-level network interactions (e.g. packet tracing) where you don't know if there was a connection or which side initiated it. This also covers unidirectional UDP flows and peer-to-peer communication where the "user-facing" surface of the protocol / API does not expose a clear notion of client and server.

View Source
const (
	// NetworkTransportKey is the attribute Key conforming to the
	// "network.transport" semantic conventions. It represents the [OSI
	// Transport Layer](https://osi-model.com/transport-layer/) or
	// [Inter-process Communication
	// method](https://en.wikipedia.org/wiki/Inter-process_communication). The
	// value SHOULD be normalized to lowercase.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'tcp', 'udp'
	NetworkTransportKey = attribute.Key("network.transport")

	// NetworkTypeKey is the attribute Key conforming to the "network.type"
	// semantic conventions. It represents the [OSI Network
	// Layer](https://osi-model.com/network-layer/) or non-OSI equivalent. The
	// value SHOULD be normalized to lowercase.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'ipv4', 'ipv6'
	NetworkTypeKey = attribute.Key("network.type")

	// NetworkProtocolNameKey is the attribute Key conforming to the
	// "network.protocol.name" semantic conventions. It represents the [OSI
	// Application Layer](https://osi-model.com/application-layer/) or non-OSI
	// equivalent. The value SHOULD be normalized to lowercase.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'amqp', 'http', 'mqtt'
	NetworkProtocolNameKey = attribute.Key("network.protocol.name")

	// NetworkProtocolVersionKey is the attribute Key conforming to the
	// "network.protocol.version" semantic conventions. It represents the
	// version of the application layer protocol used. See note below.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '3.1.1'
	// Note: `network.protocol.version` refers to the version of the protocol
	// used and might be different from the protocol client's version. If the
	// HTTP client used has a version of `0.27.2`, but sends HTTP version
	// `1.1`, this attribute should be set to `1.1`.
	NetworkProtocolVersionKey = attribute.Key("network.protocol.version")
)

These attributes may be used for any network related operation.

View Source
const (
	// NetworkConnectionTypeKey is the attribute Key conforming to the
	// "network.connection.type" semantic conventions. It represents the
	// internet connection type.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'wifi'
	NetworkConnectionTypeKey = attribute.Key("network.connection.type")

	// NetworkConnectionSubtypeKey is the attribute Key conforming to the
	// "network.connection.subtype" semantic conventions. It represents the
	// this describes more details regarding the connection.type. It may be the
	// type of cell technology connection, but it could be used for describing
	// details about a wifi connection.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'LTE'
	NetworkConnectionSubtypeKey = attribute.Key("network.connection.subtype")

	// NetworkCarrierNameKey is the attribute Key conforming to the
	// "network.carrier.name" semantic conventions. It represents the name of
	// the mobile carrier.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'sprint'
	NetworkCarrierNameKey = attribute.Key("network.carrier.name")

	// NetworkCarrierMccKey is the attribute Key conforming to the
	// "network.carrier.mcc" semantic conventions. It represents the mobile
	// carrier country code.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '310'
	NetworkCarrierMccKey = attribute.Key("network.carrier.mcc")

	// NetworkCarrierMncKey is the attribute Key conforming to the
	// "network.carrier.mnc" semantic conventions. It represents the mobile
	// carrier network code.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '001'
	NetworkCarrierMncKey = attribute.Key("network.carrier.mnc")

	// NetworkCarrierIccKey is the attribute Key conforming to the
	// "network.carrier.icc" semantic conventions. It represents the ISO 3166-1
	// alpha-2 2-character country code associated with the mobile carrier
	// network.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'DE'
	NetworkCarrierIccKey = attribute.Key("network.carrier.icc")
)

These attributes may be used for any network related operation.

View Source
const (
	// HTTPRequestMethodOriginalKey is the attribute Key conforming to the
	// "http.request.method_original" semantic conventions. It represents the
	// original HTTP method sent by the client in the request line.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If and only if it's different
	// than `http.request.method`.)
	// Stability: stable
	// Examples: 'GeT', 'ACL', 'foo'
	HTTPRequestMethodOriginalKey = attribute.Key("http.request.method_original")

	// HTTPRequestBodySizeKey is the attribute Key conforming to the
	// "http.request.body.size" semantic conventions. It represents the size of
	// the request payload body in bytes. This is the number of bytes
	// transferred excluding headers and is often, but not always, present as
	// the
	// [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length)
	// header. For requests using transport encoding, this should be the
	// compressed size.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 3495
	HTTPRequestBodySizeKey = attribute.Key("http.request.body.size")

	// HTTPResponseBodySizeKey is the attribute Key conforming to the
	// "http.response.body.size" semantic conventions. It represents the size
	// of the response payload body in bytes. This is the number of bytes
	// transferred excluding headers and is often, but not always, present as
	// the
	// [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length)
	// header. For requests using transport encoding, this should be the
	// compressed size.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 3495
	HTTPResponseBodySizeKey = attribute.Key("http.response.body.size")
)

Semantic conventions for HTTP client and server Spans.

View Source
const (
	// MessagingMessageIDKey is the attribute Key conforming to the
	// "messaging.message.id" semantic conventions. It represents a value used
	// by the messaging system as an identifier for the message, represented as
	// a string.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '452a7c7c7c7048c2f887f61572b18fc2'
	MessagingMessageIDKey = attribute.Key("messaging.message.id")

	// MessagingMessageConversationIDKey is the attribute Key conforming to the
	// "messaging.message.conversation_id" semantic conventions. It represents
	// the [conversation ID](#conversations) identifying the conversation to
	// which the message belongs, represented as a string. Sometimes called
	// "Correlation ID".
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'MyConversationID'
	MessagingMessageConversationIDKey = attribute.Key("messaging.message.conversation_id")

	// MessagingMessagePayloadSizeBytesKey is the attribute Key conforming to
	// the "messaging.message.payload_size_bytes" semantic conventions. It
	// represents the (uncompressed) size of the message payload in bytes. Also
	// use this attribute if it is unknown whether the compressed or
	// uncompressed payload size is reported.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 2738
	MessagingMessagePayloadSizeBytesKey = attribute.Key("messaging.message.payload_size_bytes")

	// MessagingMessagePayloadCompressedSizeBytesKey is the attribute Key
	// conforming to the "messaging.message.payload_compressed_size_bytes"
	// semantic conventions. It represents the compressed size of the message
	// payload in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 2048
	MessagingMessagePayloadCompressedSizeBytesKey = attribute.Key("messaging.message.payload_compressed_size_bytes")
)

Semantic convention describing per-message attributes populated on messaging spans or links.

View Source
const (
	// MessagingDestinationNameKey is the attribute Key conforming to the
	// "messaging.destination.name" semantic conventions. It represents the
	// message destination name
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'MyQueue', 'MyTopic'
	// Note: Destination name SHOULD uniquely identify a specific queue, topic
	// or other entity within the broker. If
	// the broker does not have such notion, the destination name SHOULD
	// uniquely identify the broker.
	MessagingDestinationNameKey = attribute.Key("messaging.destination.name")

	// MessagingDestinationTemplateKey is the attribute Key conforming to the
	// "messaging.destination.template" semantic conventions. It represents the
	// low cardinality representation of the messaging destination name
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/customers/{customerID}'
	// Note: Destination names could be constructed from templates. An example
	// would be a destination name involving a user name or product id.
	// Although the destination name in this case is of high cardinality, the
	// underlying template is of low cardinality and can be effectively used
	// for grouping and aggregation.
	MessagingDestinationTemplateKey = attribute.Key("messaging.destination.template")

	// MessagingDestinationTemporaryKey is the attribute Key conforming to the
	// "messaging.destination.temporary" semantic conventions. It represents a
	// boolean that is true if the message destination is temporary and might
	// not exist anymore after messages are processed.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	MessagingDestinationTemporaryKey = attribute.Key("messaging.destination.temporary")

	// MessagingDestinationAnonymousKey is the attribute Key conforming to the
	// "messaging.destination.anonymous" semantic conventions. It represents a
	// boolean that is true if the message destination is anonymous (could be
	// unnamed or have auto-generated name).
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	MessagingDestinationAnonymousKey = attribute.Key("messaging.destination.anonymous")
)

Semantic convention for attributes that describe messaging destination on broker

View Source
const (
	// MessagingKafkaMessageKeyKey is the attribute Key conforming to the
	// "messaging.kafka.message.key" semantic conventions. It represents the
	// message keys in Kafka are used for grouping alike messages to ensure
	// they're processed on the same partition. They differ from
	// `messaging.message.id` in that they're not unique. If the key is `null`,
	// the attribute MUST NOT be set.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'myKey'
	// Note: If the key type is not string, it's string representation has to
	// be supplied for the attribute. If the key has no unambiguous, canonical
	// string form, don't include its value.
	MessagingKafkaMessageKeyKey = attribute.Key("messaging.kafka.message.key")

	// MessagingKafkaConsumerGroupKey is the attribute Key conforming to the
	// "messaging.kafka.consumer.group" semantic conventions. It represents the
	// name of the Kafka Consumer Group that is handling the message. Only
	// applies to consumers, not producers.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'my-group'
	MessagingKafkaConsumerGroupKey = attribute.Key("messaging.kafka.consumer.group")

	// MessagingKafkaDestinationPartitionKey is the attribute Key conforming to
	// the "messaging.kafka.destination.partition" semantic conventions. It
	// represents the partition the message is sent to.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 2
	MessagingKafkaDestinationPartitionKey = attribute.Key("messaging.kafka.destination.partition")

	// MessagingKafkaMessageOffsetKey is the attribute Key conforming to the
	// "messaging.kafka.message.offset" semantic conventions. It represents the
	// offset of a record in the corresponding Kafka partition.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 42
	MessagingKafkaMessageOffsetKey = attribute.Key("messaging.kafka.message.offset")

	// MessagingKafkaMessageTombstoneKey is the attribute Key conforming to the
	// "messaging.kafka.message.tombstone" semantic conventions. It represents
	// a boolean that is true if the message is a tombstone.
	//
	// Type: boolean
	// RequirementLevel: ConditionallyRequired (If value is `true`. When
	// missing, the value is assumed to be `false`.)
	// Stability: stable
	MessagingKafkaMessageTombstoneKey = attribute.Key("messaging.kafka.message.tombstone")
)

Attributes for Apache Kafka

View Source
const (
	// MessagingRocketmqNamespaceKey is the attribute Key conforming to the
	// "messaging.rocketmq.namespace" semantic conventions. It represents the
	// namespace of RocketMQ resources, resources in different namespaces are
	// individual.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'myNamespace'
	MessagingRocketmqNamespaceKey = attribute.Key("messaging.rocketmq.namespace")

	// MessagingRocketmqClientGroupKey is the attribute Key conforming to the
	// "messaging.rocketmq.client_group" semantic conventions. It represents
	// the name of the RocketMQ producer/consumer group that is handling the
	// message. The client type is identified by the SpanKind.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'myConsumerGroup'
	MessagingRocketmqClientGroupKey = attribute.Key("messaging.rocketmq.client_group")

	// MessagingRocketmqMessageDeliveryTimestampKey is the attribute Key
	// conforming to the "messaging.rocketmq.message.delivery_timestamp"
	// semantic conventions. It represents the timestamp in milliseconds that
	// the delay message is expected to be delivered to consumer.
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (If the message type is delay
	// and delay time level is not specified.)
	// Stability: stable
	// Examples: 1665987217045
	MessagingRocketmqMessageDeliveryTimestampKey = attribute.Key("messaging.rocketmq.message.delivery_timestamp")

	// MessagingRocketmqMessageDelayTimeLevelKey is the attribute Key
	// conforming to the "messaging.rocketmq.message.delay_time_level" semantic
	// conventions. It represents the delay time level for delay message, which
	// determines the message delay time.
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (If the message type is delay
	// and delivery timestamp is not specified.)
	// Stability: stable
	// Examples: 3
	MessagingRocketmqMessageDelayTimeLevelKey = attribute.Key("messaging.rocketmq.message.delay_time_level")

	// MessagingRocketmqMessageGroupKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.group" semantic conventions. It represents
	// the it is essential for FIFO message. Messages that belong to the same
	// message group are always processed one by one within the same consumer
	// group.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If the message type is FIFO.)
	// Stability: stable
	// Examples: 'myMessageGroup'
	MessagingRocketmqMessageGroupKey = attribute.Key("messaging.rocketmq.message.group")

	// MessagingRocketmqMessageTypeKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.type" semantic conventions. It represents
	// the type of message.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	MessagingRocketmqMessageTypeKey = attribute.Key("messaging.rocketmq.message.type")

	// MessagingRocketmqMessageTagKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.tag" semantic conventions. It represents the
	// secondary classifier of message besides topic.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'tagA'
	MessagingRocketmqMessageTagKey = attribute.Key("messaging.rocketmq.message.tag")

	// MessagingRocketmqMessageKeysKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.keys" semantic conventions. It represents
	// the key(s) of message, another way to mark message besides message id.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'keyA', 'keyB'
	MessagingRocketmqMessageKeysKey = attribute.Key("messaging.rocketmq.message.keys")

	// MessagingRocketmqConsumptionModelKey is the attribute Key conforming to
	// the "messaging.rocketmq.consumption_model" semantic conventions. It
	// represents the model of message consumption. This only applies to
	// consumer spans.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	MessagingRocketmqConsumptionModelKey = attribute.Key("messaging.rocketmq.consumption_model")
)

Attributes for Apache RocketMQ

View Source
const (
	// URLSchemeKey is the attribute Key conforming to the "url.scheme"
	// semantic conventions. It represents the [URI
	// scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component
	// identifying the used protocol.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'https', 'ftp', 'telnet'
	URLSchemeKey = attribute.Key("url.scheme")

	// URLFullKey is the attribute Key conforming to the "url.full" semantic
	// conventions. It represents the absolute URL describing a network
	// resource according to [RFC3986](https://www.rfc-editor.org/rfc/rfc3986)
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'https://www.foo.bar/search?q=OpenTelemetry#SemConv',
	// '//localhost'
	// Note: For network calls, URL usually has
	// `scheme://host[:port][path][?query][#fragment]` format, where the
	// fragment is not transmitted over HTTP, but if it is known, it should be
	// included nevertheless.
	// `url.full` MUST NOT contain credentials passed via URL in form of
	// `https://username:password@www.example.com/`. In such case username and
	// password should be redacted and attribute's value should be
	// `https://REDACTED:REDACTED@www.example.com/`.
	// `url.full` SHOULD capture the absolute URL when it is available (or can
	// be reconstructed) and SHOULD NOT be validated or modified except for
	// sanitizing purposes.
	URLFullKey = attribute.Key("url.full")

	// URLPathKey is the attribute Key conforming to the "url.path" semantic
	// conventions. It represents the [URI
	// path](https://www.rfc-editor.org/rfc/rfc3986#section-3.3) component
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/search'
	// Note: When missing, the value is assumed to be `/`
	URLPathKey = attribute.Key("url.path")

	// URLQueryKey is the attribute Key conforming to the "url.query" semantic
	// conventions. It represents the [URI
	// query](https://www.rfc-editor.org/rfc/rfc3986#section-3.4) component
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'q=OpenTelemetry'
	// Note: Sensitive content provided in query string SHOULD be scrubbed when
	// instrumentations can identify it.
	URLQueryKey = attribute.Key("url.query")

	// URLFragmentKey is the attribute Key conforming to the "url.fragment"
	// semantic conventions. It represents the [URI
	// fragment](https://www.rfc-editor.org/rfc/rfc3986#section-3.5) component
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'SemConv'
	URLFragmentKey = attribute.Key("url.fragment")
)

Attributes describing URL.

View Source
const (
	// FeatureFlagKeyKey is the attribute Key conforming to the
	// "feature_flag.key" semantic conventions. It represents the unique
	// identifier of the feature flag.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'logo-color'
	FeatureFlagKeyKey = attribute.Key("feature_flag.key")

	// FeatureFlagProviderNameKey is the attribute Key conforming to the
	// "feature_flag.provider_name" semantic conventions. It represents the
	// name of the service provider that performs the flag evaluation.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'Flag Manager'
	FeatureFlagProviderNameKey = attribute.Key("feature_flag.provider_name")

	// FeatureFlagVariantKey is the attribute Key conforming to the
	// "feature_flag.variant" semantic conventions. It represents the sHOULD be
	// a semantic identifier for a value. If one is unavailable, a stringified
	// version of the value can be used.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'red', 'true', 'on'
	// Note: A semantic identifier, commonly referred to as a variant, provides
	// a means
	// for referring to a value without including the value itself. This can
	// provide additional context for understanding the meaning behind a value.
	// For example, the variant `red` maybe be used for the value `#c05543`.
	//
	// A stringified version of the value can be used in situations where a
	// semantic identifier is unavailable. String representation of the value
	// should be determined by the implementer.
	FeatureFlagVariantKey = attribute.Key("feature_flag.variant")
)

This semantic convention defines the attributes used to represent a feature flag evaluation as an event.

View Source
const (
	// MessageTypeKey is the attribute Key conforming to the "message.type"
	// semantic conventions. It represents the whether this is a received or
	// sent message.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	MessageTypeKey = attribute.Key("message.type")

	// MessageIDKey is the attribute Key conforming to the "message.id"
	// semantic conventions. It represents the mUST be calculated as two
	// different counters starting from `1` one for sent messages and one for
	// received message.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Note: This way we guarantee that the values will be consistent between
	// different implementations.
	MessageIDKey = attribute.Key("message.id")

	// MessageCompressedSizeKey is the attribute Key conforming to the
	// "message.compressed_size" semantic conventions. It represents the
	// compressed size of the message in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	MessageCompressedSizeKey = attribute.Key("message.compressed_size")

	// MessageUncompressedSizeKey is the attribute Key conforming to the
	// "message.uncompressed_size" semantic conventions. It represents the
	// uncompressed size of the message in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	MessageUncompressedSizeKey = attribute.Key("message.uncompressed_size")
)

RPC received/sent message.

View Source
const (
	// BrowserBrandsKey is the attribute Key conforming to the "browser.brands"
	// semantic conventions. It represents the array of brand name and version
	// separated by a space
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: ' Not A;Brand 99', 'Chromium 99', 'Chrome 99'
	// Note: This value is intended to be taken from the [UA client hints
	// API](https://wicg.github.io/ua-client-hints/#interface)
	// (`navigator.userAgentData.brands`).
	BrowserBrandsKey = attribute.Key("browser.brands")

	// BrowserPlatformKey is the attribute Key conforming to the
	// "browser.platform" semantic conventions. It represents the platform on
	// which the browser is running
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Windows', 'macOS', 'Android'
	// Note: This value is intended to be taken from the [UA client hints
	// API](https://wicg.github.io/ua-client-hints/#interface)
	// (`navigator.userAgentData.platform`). If unavailable, the legacy
	// `navigator.platform` API SHOULD NOT be used instead and this attribute
	// SHOULD be left unset in order for the values to be consistent.
	// The list of possible values is defined in the [W3C User-Agent Client
	// Hints
	// specification](https://wicg.github.io/ua-client-hints/#sec-ch-ua-platform).
	// Note that some (but not all) of these values can overlap with values in
	// the [`os.type` and `os.name` attributes](./os.md). However, for
	// consistency, the values in the `browser.platform` attribute should
	// capture the exact value that the user agent provides.
	BrowserPlatformKey = attribute.Key("browser.platform")

	// BrowserMobileKey is the attribute Key conforming to the "browser.mobile"
	// semantic conventions. It represents a boolean that is true if the
	// browser is running on a mobile device
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	// Note: This value is intended to be taken from the [UA client hints
	// API](https://wicg.github.io/ua-client-hints/#interface)
	// (`navigator.userAgentData.mobile`). If unavailable, this attribute
	// SHOULD be left unset.
	BrowserMobileKey = attribute.Key("browser.mobile")

	// BrowserLanguageKey is the attribute Key conforming to the
	// "browser.language" semantic conventions. It represents the preferred
	// language of the user using the browser
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'en', 'en-US', 'fr', 'fr-FR'
	// Note: This value is intended to be taken from the Navigator API
	// `navigator.language`.
	BrowserLanguageKey = attribute.Key("browser.language")
)

The web browser in which the application represented by the resource is running. The `browser.*` attributes MUST be used only for resources that represent applications running in a web browser (regardless of whether running on a mobile or desktop device).

View Source
const (
	// CloudProviderKey is the attribute Key conforming to the "cloud.provider"
	// semantic conventions. It represents the name of the cloud provider.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	CloudProviderKey = attribute.Key("cloud.provider")

	// CloudAccountIDKey is the attribute Key conforming to the
	// "cloud.account.id" semantic conventions. It represents the cloud account
	// ID the resource is assigned to.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '111111111111', 'opentelemetry'
	CloudAccountIDKey = attribute.Key("cloud.account.id")

	// CloudRegionKey is the attribute Key conforming to the "cloud.region"
	// semantic conventions. It represents the geographical region the resource
	// is running.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'us-central1', 'us-east-1'
	// Note: Refer to your provider's docs to see the available regions, for
	// example [Alibaba Cloud
	// regions](https://www.alibabacloud.com/help/doc-detail/40654.htm), [AWS
	// regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/),
	// [Azure
	// regions](https://azure.microsoft.com/en-us/global-infrastructure/geographies/),
	// [Google Cloud regions](https://cloud.google.com/about/locations), or
	// [Tencent Cloud
	// regions](https://www.tencentcloud.com/document/product/213/6091).
	CloudRegionKey = attribute.Key("cloud.region")

	// CloudResourceIDKey is the attribute Key conforming to the
	// "cloud.resource_id" semantic conventions. It represents the cloud
	// provider-specific native identifier of the monitored cloud resource
	// (e.g. an
	// [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
	// on AWS, a [fully qualified resource
	// ID](https://learn.microsoft.com/en-us/rest/api/resources/resources/get-by-id)
	// on Azure, a [full resource
	// name](https://cloud.google.com/apis/design/resource_names#full_resource_name)
	// on GCP)
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'arn:aws:lambda:REGION:ACCOUNT_ID:function:my-function',
	// '//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID',
	// '/subscriptions/<SUBSCIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>'
	// Note: On some cloud providers, it may not be possible to determine the
	// full ID at startup,
	// so it may be necessary to set `cloud.resource_id` as a span attribute
	// instead.
	//
	// The exact value to use for `cloud.resource_id` depends on the cloud
	// provider.
	// The following well-known definitions MUST be used if you set this
	// attribute and they apply:
	//
	// * **AWS Lambda:** The function
	// [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
	//   Take care not to use the "invoked ARN" directly but replace any
	//   [alias
	// suffix](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html)
	//   with the resolved function version, as the same runtime instance may
	// be invokable with
	//   multiple different aliases.
	// * **GCP:** The [URI of the
	// resource](https://cloud.google.com/iam/docs/full-resource-names)
	// * **Azure:** The [Fully Qualified Resource
	// ID](https://docs.microsoft.com/en-us/rest/api/resources/resources/get-by-id)
	// of the invoked function,
	//   *not* the function app, having the form
	// `/subscriptions/<SUBSCIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>`.
	//   This means that a span attribute MUST be used, as an Azure function
	// app can host multiple functions that would usually share
	//   a TracerProvider.
	CloudResourceIDKey = attribute.Key("cloud.resource_id")

	// CloudAvailabilityZoneKey is the attribute Key conforming to the
	// "cloud.availability_zone" semantic conventions. It represents the cloud
	// regions often have multiple, isolated locations known as zones to
	// increase availability. Availability zone represents the zone where the
	// resource is running.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'us-east-1c'
	// Note: Availability zones are called "zones" on Alibaba Cloud and Google
	// Cloud.
	CloudAvailabilityZoneKey = attribute.Key("cloud.availability_zone")

	// CloudPlatformKey is the attribute Key conforming to the "cloud.platform"
	// semantic conventions. It represents the cloud platform in use.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Note: The prefix of the service SHOULD match the one specified in
	// `cloud.provider`.
	CloudPlatformKey = attribute.Key("cloud.platform")
)

A cloud environment (e.g. GCP, Azure, AWS)

View Source
const (
	// AWSECSContainerARNKey is the attribute Key conforming to the
	// "aws.ecs.container.arn" semantic conventions. It represents the Amazon
	// Resource Name (ARN) of an [ECS container
	// instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples:
	// 'arn:aws:ecs:us-west-1:123456789123:container/32624152-9086-4f0e-acae-1a75b14fe4d9'
	AWSECSContainerARNKey = attribute.Key("aws.ecs.container.arn")

	// AWSECSClusterARNKey is the attribute Key conforming to the
	// "aws.ecs.cluster.arn" semantic conventions. It represents the ARN of an
	// [ECS
	// cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'arn:aws:ecs:us-west-2:123456789123:cluster/my-cluster'
	AWSECSClusterARNKey = attribute.Key("aws.ecs.cluster.arn")

	// AWSECSLaunchtypeKey is the attribute Key conforming to the
	// "aws.ecs.launchtype" semantic conventions. It represents the [launch
	// type](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html)
	// for an ECS task.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	AWSECSLaunchtypeKey = attribute.Key("aws.ecs.launchtype")

	// AWSECSTaskARNKey is the attribute Key conforming to the
	// "aws.ecs.task.arn" semantic conventions. It represents the ARN of an
	// [ECS task
	// definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples:
	// 'arn:aws:ecs:us-west-1:123456789123:task/10838bed-421f-43ef-870a-f43feacbbb5b'
	AWSECSTaskARNKey = attribute.Key("aws.ecs.task.arn")

	// AWSECSTaskFamilyKey is the attribute Key conforming to the
	// "aws.ecs.task.family" semantic conventions. It represents the task
	// definition family this task definition is a member of.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry-family'
	AWSECSTaskFamilyKey = attribute.Key("aws.ecs.task.family")

	// AWSECSTaskRevisionKey is the attribute Key conforming to the
	// "aws.ecs.task.revision" semantic conventions. It represents the revision
	// for this task definition.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '8', '26'
	AWSECSTaskRevisionKey = attribute.Key("aws.ecs.task.revision")
)

Resources used by AWS Elastic Container Service (ECS).

View Source
const (
	// AWSLogGroupNamesKey is the attribute Key conforming to the
	// "aws.log.group.names" semantic conventions. It represents the name(s) of
	// the AWS log group(s) an application is writing to.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/aws/lambda/my-function', 'opentelemetry-service'
	// Note: Multiple log groups must be supported for cases like
	// multi-container applications, where a single application has sidecar
	// containers, and each write to their own log group.
	AWSLogGroupNamesKey = attribute.Key("aws.log.group.names")

	// AWSLogGroupARNsKey is the attribute Key conforming to the
	// "aws.log.group.arns" semantic conventions. It represents the Amazon
	// Resource Name(s) (ARN) of the AWS log group(s).
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples:
	// 'arn:aws:logs:us-west-1:123456789012:log-group:/aws/my/group:*'
	// Note: See the [log group ARN format
	// documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html#CWL_ARN_Format).
	AWSLogGroupARNsKey = attribute.Key("aws.log.group.arns")

	// AWSLogStreamNamesKey is the attribute Key conforming to the
	// "aws.log.stream.names" semantic conventions. It represents the name(s)
	// of the AWS log stream(s) an application is writing to.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'logs/main/10838bed-421f-43ef-870a-f43feacbbb5b'
	AWSLogStreamNamesKey = attribute.Key("aws.log.stream.names")

	// AWSLogStreamARNsKey is the attribute Key conforming to the
	// "aws.log.stream.arns" semantic conventions. It represents the ARN(s) of
	// the AWS log stream(s).
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples:
	// 'arn:aws:logs:us-west-1:123456789012:log-group:/aws/my/group:log-stream:logs/main/10838bed-421f-43ef-870a-f43feacbbb5b'
	// Note: See the [log stream ARN format
	// documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html#CWL_ARN_Format).
	// One log group can contain several log streams, so these ARNs necessarily
	// identify both a log group and a log stream.
	AWSLogStreamARNsKey = attribute.Key("aws.log.stream.arns")
)

Resources specific to Amazon Web Services.

View Source
const (
	// GCPCloudRunJobExecutionKey is the attribute Key conforming to the
	// "gcp.cloud_run.job.execution" semantic conventions. It represents the
	// name of the Cloud Run
	// [execution](https://cloud.google.com/run/docs/managing/job-executions)
	// being run for the Job, as set by the
	// [`CLOUD_RUN_EXECUTION`](https://cloud.google.com/run/docs/container-contract#jobs-env-vars)
	// environment variable.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'job-name-xxxx', 'sample-job-mdw84'
	GCPCloudRunJobExecutionKey = attribute.Key("gcp.cloud_run.job.execution")

	// GCPCloudRunJobTaskIndexKey is the attribute Key conforming to the
	// "gcp.cloud_run.job.task_index" semantic conventions. It represents the
	// index for a task within an execution as provided by the
	// [`CLOUD_RUN_TASK_INDEX`](https://cloud.google.com/run/docs/container-contract#jobs-env-vars)
	// environment variable.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 0, 1
	GCPCloudRunJobTaskIndexKey = attribute.Key("gcp.cloud_run.job.task_index")
)

Resource used by Google Cloud Run.

View Source
const (
	// GCPGceInstanceNameKey is the attribute Key conforming to the
	// "gcp.gce.instance.name" semantic conventions. It represents the instance
	// name of a GCE instance. This is the value provided by `host.name`, the
	// visible name of the instance in the Cloud Console UI, and the prefix for
	// the default hostname of the instance as defined by the [default internal
	// DNS
	// name](https://cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'instance-1', 'my-vm-name'
	GCPGceInstanceNameKey = attribute.Key("gcp.gce.instance.name")

	// GCPGceInstanceHostnameKey is the attribute Key conforming to the
	// "gcp.gce.instance.hostname" semantic conventions. It represents the
	// hostname of a GCE instance. This is the full value of the default or
	// [custom
	// hostname](https://cloud.google.com/compute/docs/instances/custom-hostname-vm).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'my-host1234.example.com',
	// 'sample-vm.us-west1-b.c.my-project.internal'
	GCPGceInstanceHostnameKey = attribute.Key("gcp.gce.instance.hostname")
)

Resources used by Google Compute Engine (GCE).

View Source
const (
	// HerokuReleaseCreationTimestampKey is the attribute Key conforming to the
	// "heroku.release.creation_timestamp" semantic conventions. It represents
	// the time and date the release was created
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '2022-10-23T18:00:42Z'
	HerokuReleaseCreationTimestampKey = attribute.Key("heroku.release.creation_timestamp")

	// HerokuReleaseCommitKey is the attribute Key conforming to the
	// "heroku.release.commit" semantic conventions. It represents the commit
	// hash for the current release
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'e6134959463efd8966b20e75b913cafe3f5ec'
	HerokuReleaseCommitKey = attribute.Key("heroku.release.commit")

	// HerokuAppIDKey is the attribute Key conforming to the "heroku.app.id"
	// semantic conventions. It represents the unique identifier for the
	// application
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '2daa2797-e42b-4624-9322-ec3f968df4da'
	HerokuAppIDKey = attribute.Key("heroku.app.id")
)

Heroku dyno metadata

View Source
const (
	// ContainerNameKey is the attribute Key conforming to the "container.name"
	// semantic conventions. It represents the container name used by container
	// runtime.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry-autoconf'
	ContainerNameKey = attribute.Key("container.name")

	// ContainerIDKey is the attribute Key conforming to the "container.id"
	// semantic conventions. It represents the container ID. Usually a UUID, as
	// for example used to [identify Docker
	// containers](https://docs.docker.com/engine/reference/run/#container-identification).
	// The UUID might be abbreviated.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'a3bf90e006b2'
	ContainerIDKey = attribute.Key("container.id")

	// ContainerRuntimeKey is the attribute Key conforming to the
	// "container.runtime" semantic conventions. It represents the container
	// runtime managing this container.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'docker', 'containerd', 'rkt'
	ContainerRuntimeKey = attribute.Key("container.runtime")

	// ContainerImageNameKey is the attribute Key conforming to the
	// "container.image.name" semantic conventions. It represents the name of
	// the image the container was built on.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'gcr.io/opentelemetry/operator'
	ContainerImageNameKey = attribute.Key("container.image.name")

	// ContainerImageTagKey is the attribute Key conforming to the
	// "container.image.tag" semantic conventions. It represents the container
	// image tag.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '0.1'
	ContainerImageTagKey = attribute.Key("container.image.tag")

	// ContainerImageIDKey is the attribute Key conforming to the
	// "container.image.id" semantic conventions. It represents the runtime
	// specific image identifier. Usually a hash algorithm followed by a UUID.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples:
	// 'sha256:19c92d0a00d1b66d897bceaa7319bee0dd38a10a851c60bcec9474aa3f01e50f'
	// Note: Docker defines a sha256 of the image id; `container.image.id`
	// corresponds to the `Image` field from the Docker container inspect
	// [API](https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerInspect)
	// endpoint.
	// K8S defines a link to the container registry repository with digest
	// `"imageID": "registry.azurecr.io
	// /namespace/service/dockerfile@sha256:bdeabd40c3a8a492eaf9e8e44d0ebbb84bac7ee25ac0cf8a7159d25f62555625"`.
	// OCI defines a digest of manifest.
	ContainerImageIDKey = attribute.Key("container.image.id")

	// ContainerCommandKey is the attribute Key conforming to the
	// "container.command" semantic conventions. It represents the command used
	// to run the container (i.e. the command name).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'otelcontribcol'
	// Note: If using embedded credentials or sensitive data, it is recommended
	// to remove them to prevent potential leakage.
	ContainerCommandKey = attribute.Key("container.command")

	// ContainerCommandLineKey is the attribute Key conforming to the
	// "container.command_line" semantic conventions. It represents the full
	// command run by the container as a single string representing the full
	// command. [2]
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'otelcontribcol --config config.yaml'
	ContainerCommandLineKey = attribute.Key("container.command_line")

	// ContainerCommandArgsKey is the attribute Key conforming to the
	// "container.command_args" semantic conventions. It represents the all the
	// command arguments (including the command/executable itself) run by the
	// container. [2]
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'otelcontribcol, --config, config.yaml'
	ContainerCommandArgsKey = attribute.Key("container.command_args")
)

A container instance.

View Source
const (
	// DeviceIDKey is the attribute Key conforming to the "device.id" semantic
	// conventions. It represents a unique identifier representing the device
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '2ab2916d-a51f-4ac8-80ee-45ac31a28092'
	// Note: The device identifier MUST only be defined using the values
	// outlined below. This value is not an advertising identifier and MUST NOT
	// be used as such. On iOS (Swift or Objective-C), this value MUST be equal
	// to the [vendor
	// identifier](https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor).
	// On Android (Java or Kotlin), this value MUST be equal to the Firebase
	// Installation ID or a globally unique UUID which is persisted across
	// sessions in your application. More information can be found
	// [here](https://developer.android.com/training/articles/user-data-ids) on
	// best practices and exact implementation details. Caution should be taken
	// when storing personal data or anything which can identify a user. GDPR
	// and data protection laws may apply, ensure you do your own due
	// diligence.
	DeviceIDKey = attribute.Key("device.id")

	// DeviceModelIdentifierKey is the attribute Key conforming to the
	// "device.model.identifier" semantic conventions. It represents the model
	// identifier for the device
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'iPhone3,4', 'SM-G920F'
	// Note: It's recommended this value represents a machine readable version
	// of the model identifier rather than the market or consumer-friendly name
	// of the device.
	DeviceModelIdentifierKey = attribute.Key("device.model.identifier")

	// DeviceModelNameKey is the attribute Key conforming to the
	// "device.model.name" semantic conventions. It represents the marketing
	// name for the device model
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'iPhone 6s Plus', 'Samsung Galaxy S6'
	// Note: It's recommended this value represents a human readable version of
	// the device model rather than a machine readable alternative.
	DeviceModelNameKey = attribute.Key("device.model.name")

	// DeviceManufacturerKey is the attribute Key conforming to the
	// "device.manufacturer" semantic conventions. It represents the name of
	// the device manufacturer
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Apple', 'Samsung'
	// Note: The Android OS provides this field via
	// [Build](https://developer.android.com/reference/android/os/Build#MANUFACTURER).
	// iOS apps SHOULD hardcode the value `Apple`.
	DeviceManufacturerKey = attribute.Key("device.manufacturer")
)

The device on which the process represented by this resource is running.

View Source
const (
	// FaaSNameKey is the attribute Key conforming to the "faas.name" semantic
	// conventions. It represents the name of the single function that this
	// runtime instance executes.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'my-function', 'myazurefunctionapp/some-function-name'
	// Note: This is the name of the function as configured/deployed on the
	// FaaS
	// platform and is usually different from the name of the callback
	// function (which may be stored in the
	// [`code.namespace`/`code.function`](/docs/general/general-attributes.md#source-code-attributes)
	// span attributes).
	//
	// For some cloud providers, the above definition is ambiguous. The
	// following
	// definition of function name MUST be used for this attribute
	// (and consequently the span name) for the listed cloud
	// providers/products:
	//
	// * **Azure:**  The full name `<FUNCAPP>/<FUNC>`, i.e., function app name
	//   followed by a forward slash followed by the function name (this form
	//   can also be seen in the resource JSON for the function).
	//   This means that a span attribute MUST be used, as an Azure function
	//   app can host multiple functions that would usually share
	//   a TracerProvider (see also the `cloud.resource_id` attribute).
	FaaSNameKey = attribute.Key("faas.name")

	// FaaSVersionKey is the attribute Key conforming to the "faas.version"
	// semantic conventions. It represents the immutable version of the
	// function being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '26', 'pinkfroid-00002'
	// Note: Depending on the cloud provider and platform, use:
	//
	// * **AWS Lambda:** The [function
	// version](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html)
	//   (an integer represented as a decimal string).
	// * **Google Cloud Run (Services):** The
	// [revision](https://cloud.google.com/run/docs/managing/revisions)
	//   (i.e., the function name plus the revision suffix).
	// * **Google Cloud Functions:** The value of the
	//   [`K_REVISION` environment
	// variable](https://cloud.google.com/functions/docs/env-var#runtime_environment_variables_set_automatically).
	// * **Azure Functions:** Not applicable. Do not set this attribute.
	FaaSVersionKey = attribute.Key("faas.version")

	// FaaSInstanceKey is the attribute Key conforming to the "faas.instance"
	// semantic conventions. It represents the execution environment ID as a
	// string, that will be potentially reused for other invocations to the
	// same function/function version.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '2021/06/28/[$LATEST]2f399eb14537447da05ab2a2e39309de'
	// Note: * **AWS Lambda:** Use the (full) log stream name.
	FaaSInstanceKey = attribute.Key("faas.instance")

	// FaaSMaxMemoryKey is the attribute Key conforming to the
	// "faas.max_memory" semantic conventions. It represents the amount of
	// memory available to the serverless function converted to Bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 134217728
	// Note: It's recommended to set this attribute since e.g. too little
	// memory can easily stop a Java AWS Lambda function from working
	// correctly. On AWS Lambda, the environment variable
	// `AWS_LAMBDA_FUNCTION_MEMORY_SIZE` provides this information (which must
	// be multiplied by 1,048,576).
	FaaSMaxMemoryKey = attribute.Key("faas.max_memory")
)

A serverless instance.

View Source
const (
	// HostIDKey is the attribute Key conforming to the "host.id" semantic
	// conventions. It represents the unique host ID. For Cloud, this must be
	// the instance_id assigned by the cloud provider. For non-containerized
	// systems, this should be the `machine-id`. See the table below for the
	// sources to use to determine the `machine-id` based on operating system.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'fdbf79e8af94cb7f9e8df36789187052'
	HostIDKey = attribute.Key("host.id")

	// HostNameKey is the attribute Key conforming to the "host.name" semantic
	// conventions. It represents the name of the host. On Unix systems, it may
	// contain what the hostname command returns, or the fully qualified
	// hostname, or another name specified by the user.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry-test'
	HostNameKey = attribute.Key("host.name")

	// HostTypeKey is the attribute Key conforming to the "host.type" semantic
	// conventions. It represents the type of host. For Cloud, this must be the
	// machine type.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'n1-standard-1'
	HostTypeKey = attribute.Key("host.type")

	// HostArchKey is the attribute Key conforming to the "host.arch" semantic
	// conventions. It represents the CPU architecture the host system is
	// running on.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	HostArchKey = attribute.Key("host.arch")

	// HostImageNameKey is the attribute Key conforming to the
	// "host.image.name" semantic conventions. It represents the name of the VM
	// image or OS install the host was instantiated from.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'infra-ami-eks-worker-node-7d4ec78312', 'CentOS-8-x86_64-1905'
	HostImageNameKey = attribute.Key("host.image.name")

	// HostImageIDKey is the attribute Key conforming to the "host.image.id"
	// semantic conventions. It represents the vM image ID or host OS image ID.
	// For Cloud, this value is from the provider.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'ami-07b06b442921831e5'
	HostImageIDKey = attribute.Key("host.image.id")

	// HostImageVersionKey is the attribute Key conforming to the
	// "host.image.version" semantic conventions. It represents the version
	// string of the VM image or host OS as defined in [Version
	// Attributes](README.md#version-attributes).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '0.1'
	HostImageVersionKey = attribute.Key("host.image.version")
)

A host is defined as a computing instance. For example, physical servers, virtual machines, switches or disk array.

View Source
const (
	// K8SClusterNameKey is the attribute Key conforming to the
	// "k8s.cluster.name" semantic conventions. It represents the name of the
	// cluster.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry-cluster'
	K8SClusterNameKey = attribute.Key("k8s.cluster.name")

	// K8SClusterUIDKey is the attribute Key conforming to the
	// "k8s.cluster.uid" semantic conventions. It represents a pseudo-ID for
	// the cluster, set to the UID of the `kube-system` namespace.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '218fc5a9-a5f1-4b54-aa05-46717d0ab26d'
	// Note: K8S does not have support for obtaining a cluster ID. If this is
	// ever
	// added, we will recommend collecting the `k8s.cluster.uid` through the
	// official APIs. In the meantime, we are able to use the `uid` of the
	// `kube-system` namespace as a proxy for cluster ID. Read on for the
	// rationale.
	//
	// Every object created in a K8S cluster is assigned a distinct UID. The
	// `kube-system` namespace is used by Kubernetes itself and will exist
	// for the lifetime of the cluster. Using the `uid` of the `kube-system`
	// namespace is a reasonable proxy for the K8S ClusterID as it will only
	// change if the cluster is rebuilt. Furthermore, Kubernetes UIDs are
	// UUIDs as standardized by
	// [ISO/IEC 9834-8 and ITU-T
	// X.667](https://www.itu.int/ITU-T/studygroups/com17/oid.html).
	// Which states:
	//
	// > If generated according to one of the mechanisms defined in Rec.
	//   ITU-T X.667 | ISO/IEC 9834-8, a UUID is either guaranteed to be
	//   different from all other UUIDs generated before 3603 A.D., or is
	//   extremely likely to be different (depending on the mechanism chosen).
	//
	// Therefore, UIDs between clusters should be extremely unlikely to
	// conflict.
	K8SClusterUIDKey = attribute.Key("k8s.cluster.uid")
)

A Kubernetes Cluster.

View Source
const (
	// K8SNodeNameKey is the attribute Key conforming to the "k8s.node.name"
	// semantic conventions. It represents the name of the Node.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'node-1'
	K8SNodeNameKey = attribute.Key("k8s.node.name")

	// K8SNodeUIDKey is the attribute Key conforming to the "k8s.node.uid"
	// semantic conventions. It represents the UID of the Node.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '1eb3a0c6-0477-4080-a9cb-0cb7db65c6a2'
	K8SNodeUIDKey = attribute.Key("k8s.node.uid")
)

A Kubernetes Node object.

View Source
const (
	// K8SPodUIDKey is the attribute Key conforming to the "k8s.pod.uid"
	// semantic conventions. It represents the UID of the Pod.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SPodUIDKey = attribute.Key("k8s.pod.uid")

	// K8SPodNameKey is the attribute Key conforming to the "k8s.pod.name"
	// semantic conventions. It represents the name of the Pod.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry-pod-autoconf'
	K8SPodNameKey = attribute.Key("k8s.pod.name")
)

A Kubernetes Pod object.

View Source
const (
	// K8SContainerNameKey is the attribute Key conforming to the
	// "k8s.container.name" semantic conventions. It represents the name of the
	// Container from Pod specification, must be unique within a Pod. Container
	// runtime usually uses different globally unique name (`container.name`).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'redis'
	K8SContainerNameKey = attribute.Key("k8s.container.name")

	// K8SContainerRestartCountKey is the attribute Key conforming to the
	// "k8s.container.restart_count" semantic conventions. It represents the
	// number of times the container was restarted. This attribute can be used
	// to identify a particular container (running or stopped) within a
	// container spec.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 0, 2
	K8SContainerRestartCountKey = attribute.Key("k8s.container.restart_count")
)

A container in a [PodTemplate](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates).

View Source
const (
	// K8SReplicaSetUIDKey is the attribute Key conforming to the
	// "k8s.replicaset.uid" semantic conventions. It represents the UID of the
	// ReplicaSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SReplicaSetUIDKey = attribute.Key("k8s.replicaset.uid")

	// K8SReplicaSetNameKey is the attribute Key conforming to the
	// "k8s.replicaset.name" semantic conventions. It represents the name of
	// the ReplicaSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry'
	K8SReplicaSetNameKey = attribute.Key("k8s.replicaset.name")
)

A Kubernetes ReplicaSet object.

View Source
const (
	// K8SDeploymentUIDKey is the attribute Key conforming to the
	// "k8s.deployment.uid" semantic conventions. It represents the UID of the
	// Deployment.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SDeploymentUIDKey = attribute.Key("k8s.deployment.uid")

	// K8SDeploymentNameKey is the attribute Key conforming to the
	// "k8s.deployment.name" semantic conventions. It represents the name of
	// the Deployment.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry'
	K8SDeploymentNameKey = attribute.Key("k8s.deployment.name")
)

A Kubernetes Deployment object.

View Source
const (
	// K8SStatefulSetUIDKey is the attribute Key conforming to the
	// "k8s.statefulset.uid" semantic conventions. It represents the UID of the
	// StatefulSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SStatefulSetUIDKey = attribute.Key("k8s.statefulset.uid")

	// K8SStatefulSetNameKey is the attribute Key conforming to the
	// "k8s.statefulset.name" semantic conventions. It represents the name of
	// the StatefulSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry'
	K8SStatefulSetNameKey = attribute.Key("k8s.statefulset.name")
)

A Kubernetes StatefulSet object.

View Source
const (
	// K8SDaemonSetUIDKey is the attribute Key conforming to the
	// "k8s.daemonset.uid" semantic conventions. It represents the UID of the
	// DaemonSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SDaemonSetUIDKey = attribute.Key("k8s.daemonset.uid")

	// K8SDaemonSetNameKey is the attribute Key conforming to the
	// "k8s.daemonset.name" semantic conventions. It represents the name of the
	// DaemonSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry'
	K8SDaemonSetNameKey = attribute.Key("k8s.daemonset.name")
)

A Kubernetes DaemonSet object.

View Source
const (
	// K8SJobUIDKey is the attribute Key conforming to the "k8s.job.uid"
	// semantic conventions. It represents the UID of the Job.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SJobUIDKey = attribute.Key("k8s.job.uid")

	// K8SJobNameKey is the attribute Key conforming to the "k8s.job.name"
	// semantic conventions. It represents the name of the Job.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry'
	K8SJobNameKey = attribute.Key("k8s.job.name")
)

A Kubernetes Job object.

View Source
const (
	// K8SCronJobUIDKey is the attribute Key conforming to the
	// "k8s.cronjob.uid" semantic conventions. It represents the UID of the
	// CronJob.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SCronJobUIDKey = attribute.Key("k8s.cronjob.uid")

	// K8SCronJobNameKey is the attribute Key conforming to the
	// "k8s.cronjob.name" semantic conventions. It represents the name of the
	// CronJob.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'opentelemetry'
	K8SCronJobNameKey = attribute.Key("k8s.cronjob.name")
)

A Kubernetes CronJob object.

View Source
const (
	// OSTypeKey is the attribute Key conforming to the "os.type" semantic
	// conventions. It represents the operating system type.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	OSTypeKey = attribute.Key("os.type")

	// OSDescriptionKey is the attribute Key conforming to the "os.description"
	// semantic conventions. It represents the human readable (not intended to
	// be parsed) OS version information, like e.g. reported by `ver` or
	// `lsb_release -a` commands.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Microsoft Windows [Version 10.0.18363.778]', 'Ubuntu 18.04.1
	// LTS'
	OSDescriptionKey = attribute.Key("os.description")

	// OSNameKey is the attribute Key conforming to the "os.name" semantic
	// conventions. It represents the human readable operating system name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'iOS', 'Android', 'Ubuntu'
	OSNameKey = attribute.Key("os.name")

	// OSVersionKey is the attribute Key conforming to the "os.version"
	// semantic conventions. It represents the version string of the operating
	// system as defined in [Version
	// Attributes](/docs/resource/README.md#version-attributes).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '14.2.1', '18.04.1'
	OSVersionKey = attribute.Key("os.version")
)

The operating system (OS) on which the process represented by this resource is running.

View Source
const (
	// ProcessPIDKey is the attribute Key conforming to the "process.pid"
	// semantic conventions. It represents the process identifier (PID).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 1234
	ProcessPIDKey = attribute.Key("process.pid")

	// ProcessParentPIDKey is the attribute Key conforming to the
	// "process.parent_pid" semantic conventions. It represents the parent
	// Process identifier (PID).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 111
	ProcessParentPIDKey = attribute.Key("process.parent_pid")

	// ProcessExecutableNameKey is the attribute Key conforming to the
	// "process.executable.name" semantic conventions. It represents the name
	// of the process executable. On Linux based systems, can be set to the
	// `Name` in `proc/[pid]/status`. On Windows, can be set to the base name
	// of `GetProcessImageFileNameW`.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (See alternative attributes
	// below.)
	// Stability: stable
	// Examples: 'otelcol'
	ProcessExecutableNameKey = attribute.Key("process.executable.name")

	// ProcessExecutablePathKey is the attribute Key conforming to the
	// "process.executable.path" semantic conventions. It represents the full
	// path to the process executable. On Linux based systems, can be set to
	// the target of `proc/[pid]/exe`. On Windows, can be set to the result of
	// `GetProcessImageFileNameW`.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (See alternative attributes
	// below.)
	// Stability: stable
	// Examples: '/usr/bin/cmd/otelcol'
	ProcessExecutablePathKey = attribute.Key("process.executable.path")

	// ProcessCommandKey is the attribute Key conforming to the
	// "process.command" semantic conventions. It represents the command used
	// to launch the process (i.e. the command name). On Linux based systems,
	// can be set to the zeroth string in `proc/[pid]/cmdline`. On Windows, can
	// be set to the first parameter extracted from `GetCommandLineW`.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (See alternative attributes
	// below.)
	// Stability: stable
	// Examples: 'cmd/otelcol'
	ProcessCommandKey = attribute.Key("process.command")

	// ProcessCommandLineKey is the attribute Key conforming to the
	// "process.command_line" semantic conventions. It represents the full
	// command used to launch the process as a single string representing the
	// full command. On Windows, can be set to the result of `GetCommandLineW`.
	// Do not set this if you have to assemble it just for monitoring; use
	// `process.command_args` instead.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (See alternative attributes
	// below.)
	// Stability: stable
	// Examples: 'C:\\cmd\\otecol --config="my directory\\config.yaml"'
	ProcessCommandLineKey = attribute.Key("process.command_line")

	// ProcessCommandArgsKey is the attribute Key conforming to the
	// "process.command_args" semantic conventions. It represents the all the
	// command arguments (including the command/executable itself) as received
	// by the process. On Linux-based systems (and some other Unixoid systems
	// supporting procfs), can be set according to the list of null-delimited
	// strings extracted from `proc/[pid]/cmdline`. For libc-based executables,
	// this would be the full argv vector passed to `main`.
	//
	// Type: string[]
	// RequirementLevel: ConditionallyRequired (See alternative attributes
	// below.)
	// Stability: stable
	// Examples: 'cmd/otecol', '--config=config.yaml'
	ProcessCommandArgsKey = attribute.Key("process.command_args")

	// ProcessOwnerKey is the attribute Key conforming to the "process.owner"
	// semantic conventions. It represents the username of the user that owns
	// the process.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'root'
	ProcessOwnerKey = attribute.Key("process.owner")
)

An operating system process.

View Source
const (
	// ProcessRuntimeNameKey is the attribute Key conforming to the
	// "process.runtime.name" semantic conventions. It represents the name of
	// the runtime of this process. For compiled native binaries, this SHOULD
	// be the name of the compiler.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'OpenJDK Runtime Environment'
	ProcessRuntimeNameKey = attribute.Key("process.runtime.name")

	// ProcessRuntimeVersionKey is the attribute Key conforming to the
	// "process.runtime.version" semantic conventions. It represents the
	// version of the runtime of this process, as returned by the runtime
	// without modification.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '14.0.2'
	ProcessRuntimeVersionKey = attribute.Key("process.runtime.version")

	// ProcessRuntimeDescriptionKey is the attribute Key conforming to the
	// "process.runtime.description" semantic conventions. It represents an
	// additional description about the runtime of the process, for example a
	// specific vendor customization of the runtime environment.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Eclipse OpenJ9 Eclipse OpenJ9 VM openj9-0.21.0'
	ProcessRuntimeDescriptionKey = attribute.Key("process.runtime.description")
)

The single (language) runtime instance which is monitored.

View Source
const (
	// ServiceNameKey is the attribute Key conforming to the "service.name"
	// semantic conventions. It represents the logical name of the service.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'shoppingcart'
	// Note: MUST be the same for all instances of horizontally scaled
	// services. If the value was not specified, SDKs MUST fallback to
	// `unknown_service:` concatenated with
	// [`process.executable.name`](process.md#process), e.g.
	// `unknown_service:bash`. If `process.executable.name` is not available,
	// the value MUST be set to `unknown_service`.
	ServiceNameKey = attribute.Key("service.name")

	// ServiceVersionKey is the attribute Key conforming to the
	// "service.version" semantic conventions. It represents the version string
	// of the service API or implementation. The format is not defined by these
	// conventions.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '2.0.0', 'a01dbef8a'
	ServiceVersionKey = attribute.Key("service.version")
)

A service instance.

View Source
const (
	// ServiceNamespaceKey is the attribute Key conforming to the
	// "service.namespace" semantic conventions. It represents a namespace for
	// `service.name`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Shop'
	// Note: A string value having a meaning that helps to distinguish a group
	// of services, for example the team name that owns a group of services.
	// `service.name` is expected to be unique within the same namespace. If
	// `service.namespace` is not specified in the Resource then `service.name`
	// is expected to be unique for all services that have no explicit
	// namespace defined (so the empty/unspecified namespace is simply one more
	// valid namespace). Zero-length namespace string is assumed equal to
	// unspecified namespace.
	ServiceNamespaceKey = attribute.Key("service.namespace")

	// ServiceInstanceIDKey is the attribute Key conforming to the
	// "service.instance.id" semantic conventions. It represents the string ID
	// of the service instance.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'my-k8s-pod-deployment-1',
	// '627cc493-f310-47de-96bd-71410b7dec09'
	// Note: MUST be unique for each instance of the same
	// `service.namespace,service.name` pair (in other words
	// `service.namespace,service.name,service.instance.id` triplet MUST be
	// globally unique). The ID helps to distinguish instances of the same
	// service that exist at the same time (e.g. instances of a horizontally
	// scaled service). It is preferable for the ID to be persistent and stay
	// the same for the lifetime of the service instance, however it is
	// acceptable that the ID is ephemeral and changes during important
	// lifetime events for the service (e.g. service restarts). If the service
	// has no inherent unique ID that can be used as the value of this
	// attribute it is recommended to generate a random Version 1 or Version 4
	// RFC 4122 UUID (services aiming for reproducible UUIDs may also use
	// Version 5, see RFC 4122 for more recommendations).
	ServiceInstanceIDKey = attribute.Key("service.instance.id")
)

A service instance.

View Source
const (
	// TelemetrySDKNameKey is the attribute Key conforming to the
	// "telemetry.sdk.name" semantic conventions. It represents the name of the
	// telemetry SDK as defined above.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'opentelemetry'
	// Note: The OpenTelemetry SDK MUST set the `telemetry.sdk.name` attribute
	// to `opentelemetry`.
	// If another SDK, like a fork or a vendor-provided implementation, is
	// used, this SDK MUST set the
	// `telemetry.sdk.name` attribute to the fully-qualified class or module
	// name of this SDK's main entry point
	// or another suitable identifier depending on the language.
	// The identifier `opentelemetry` is reserved and MUST NOT be used in this
	// case.
	// All custom identifiers SHOULD be stable across different versions of an
	// implementation.
	TelemetrySDKNameKey = attribute.Key("telemetry.sdk.name")

	// TelemetrySDKLanguageKey is the attribute Key conforming to the
	// "telemetry.sdk.language" semantic conventions. It represents the
	// language of the telemetry SDK.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	TelemetrySDKLanguageKey = attribute.Key("telemetry.sdk.language")

	// TelemetrySDKVersionKey is the attribute Key conforming to the
	// "telemetry.sdk.version" semantic conventions. It represents the version
	// string of the telemetry SDK.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: '1.2.3'
	TelemetrySDKVersionKey = attribute.Key("telemetry.sdk.version")
)

The telemetry SDK used to capture data recorded by the instrumentation libraries.

View Source
const (
	// WebEngineNameKey is the attribute Key conforming to the "webengine.name"
	// semantic conventions. It represents the name of the web engine.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'WildFly'
	WebEngineNameKey = attribute.Key("webengine.name")

	// WebEngineVersionKey is the attribute Key conforming to the
	// "webengine.version" semantic conventions. It represents the version of
	// the web engine.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '21.0.0'
	WebEngineVersionKey = attribute.Key("webengine.version")

	// WebEngineDescriptionKey is the attribute Key conforming to the
	// "webengine.description" semantic conventions. It represents the
	// additional description of the web engine (e.g. detailed version and
	// edition information).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'WildFly Full 21.0.0.Final (WildFly Core 13.0.1.Final) -
	// 2.2.2.Final'
	WebEngineDescriptionKey = attribute.Key("webengine.description")
)

Resource describing the packaged software running the application code. Web engines are typically executed using process.runtime.

View Source
const (
	// OTelScopeNameKey is the attribute Key conforming to the
	// "otel.scope.name" semantic conventions. It represents the name of the
	// instrumentation scope - (`InstrumentationScope.Name` in OTLP).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'io.opentelemetry.contrib.mongodb'
	OTelScopeNameKey = attribute.Key("otel.scope.name")

	// OTelScopeVersionKey is the attribute Key conforming to the
	// "otel.scope.version" semantic conventions. It represents the version of
	// the instrumentation scope - (`InstrumentationScope.Version` in OTLP).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '1.0.0'
	OTelScopeVersionKey = attribute.Key("otel.scope.version")
)

Attributes used by non-OTLP exporters to represent OpenTelemetry Scope's concepts.

View Source
const (
	// OTelLibraryNameKey is the attribute Key conforming to the
	// "otel.library.name" semantic conventions. It represents the deprecated,
	// use the `otel.scope.name` attribute.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: 'io.opentelemetry.contrib.mongodb'
	OTelLibraryNameKey = attribute.Key("otel.library.name")

	// OTelLibraryVersionKey is the attribute Key conforming to the
	// "otel.library.version" semantic conventions. It represents the
	// deprecated, use the `otel.scope.version` attribute.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: deprecated
	// Examples: '1.0.0'
	OTelLibraryVersionKey = attribute.Key("otel.library.version")
)

Span attributes used by non-OTLP exporters to represent OpenTelemetry Scope's concepts.

View Source
const (
	// ExceptionTypeKey is the attribute Key conforming to the "exception.type"
	// semantic conventions. It represents the type of the exception (its
	// fully-qualified class name, if applicable). The dynamic type of the
	// exception should be preferred over the static type in languages that
	// support it.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'java.net.ConnectException', 'OSError'
	ExceptionTypeKey = attribute.Key("exception.type")

	// ExceptionMessageKey is the attribute Key conforming to the
	// "exception.message" semantic conventions. It represents the exception
	// message.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Division by zero', "Can't convert 'int' object to str
	// implicitly"
	ExceptionMessageKey = attribute.Key("exception.message")

	// ExceptionStacktraceKey is the attribute Key conforming to the
	// "exception.stacktrace" semantic conventions. It represents a stacktrace
	// as a string in the natural representation for the language runtime. The
	// representation is to be determined and documented by each language SIG.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Exception in thread "main" java.lang.RuntimeException: Test
	// exception\\n at '
	//  'com.example.GenerateTrace.methodB(GenerateTrace.java:13)\\n at '
	//  'com.example.GenerateTrace.methodA(GenerateTrace.java:9)\\n at '
	//  'com.example.GenerateTrace.main(GenerateTrace.java:5)'
	ExceptionStacktraceKey = attribute.Key("exception.stacktrace")
)

The shared attributes used to report a single exception associated with a span or log.

View Source
const (
	// CloudeventsEventIDKey is the attribute Key conforming to the
	// "cloudevents.event_id" semantic conventions. It represents the
	// [event_id](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#id)
	// uniquely identifies the event.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: '123e4567-e89b-12d3-a456-426614174000', '0001'
	CloudeventsEventIDKey = attribute.Key("cloudevents.event_id")

	// CloudeventsEventSourceKey is the attribute Key conforming to the
	// "cloudevents.event_source" semantic conventions. It represents the
	// [source](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#source-1)
	// identifies the context in which an event happened.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'https://github.com/cloudevents',
	// '/cloudevents/spec/pull/123', 'my-service'
	CloudeventsEventSourceKey = attribute.Key("cloudevents.event_source")

	// CloudeventsEventSpecVersionKey is the attribute Key conforming to the
	// "cloudevents.event_spec_version" semantic conventions. It represents the
	// [version of the CloudEvents
	// specification](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#specversion)
	// which the event uses.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '1.0'
	CloudeventsEventSpecVersionKey = attribute.Key("cloudevents.event_spec_version")

	// CloudeventsEventTypeKey is the attribute Key conforming to the
	// "cloudevents.event_type" semantic conventions. It represents the
	// [event_type](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#type)
	// contains a value describing the type of event related to the originating
	// occurrence.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'com.github.pull_request.opened',
	// 'com.example.object.deleted.v2'
	CloudeventsEventTypeKey = attribute.Key("cloudevents.event_type")

	// CloudeventsEventSubjectKey is the attribute Key conforming to the
	// "cloudevents.event_subject" semantic conventions. It represents the
	// [subject](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#subject)
	// of the event in the context of the event producer (identified by
	// source).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'mynewfile.jpg'
	CloudeventsEventSubjectKey = attribute.Key("cloudevents.event_subject")
)

Attributes for CloudEvents. CloudEvents is a specification on how to define event data in a standard way. These attributes can be attached to spans when performing operations with CloudEvents, regardless of the protocol being used.

View Source
const (
	// DBSystemKey is the attribute Key conforming to the "db.system" semantic
	// conventions. It represents an identifier for the database management
	// system (DBMS) product being used. See below for a list of well-known
	// identifiers.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	DBSystemKey = attribute.Key("db.system")

	// DBConnectionStringKey is the attribute Key conforming to the
	// "db.connection_string" semantic conventions. It represents the
	// connection string used to connect to the database. It is recommended to
	// remove embedded credentials.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Server=(localdb)\\v11.0;Integrated Security=true;'
	DBConnectionStringKey = attribute.Key("db.connection_string")

	// DBUserKey is the attribute Key conforming to the "db.user" semantic
	// conventions. It represents the username for accessing the database.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'readonly_user', 'reporting_user'
	DBUserKey = attribute.Key("db.user")

	// DBJDBCDriverClassnameKey is the attribute Key conforming to the
	// "db.jdbc.driver_classname" semantic conventions. It represents the
	// fully-qualified class name of the [Java Database Connectivity
	// (JDBC)](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/)
	// driver used to connect.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'org.postgresql.Driver',
	// 'com.microsoft.sqlserver.jdbc.SQLServerDriver'
	DBJDBCDriverClassnameKey = attribute.Key("db.jdbc.driver_classname")

	// DBNameKey is the attribute Key conforming to the "db.name" semantic
	// conventions. It represents the this attribute is used to report the name
	// of the database being accessed. For commands that switch the database,
	// this should be set to the target database (even if the command fails).
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If applicable.)
	// Stability: stable
	// Examples: 'customers', 'main'
	// Note: In some SQL databases, the database name to be used is called
	// "schema name". In case there are multiple layers that could be
	// considered for database name (e.g. Oracle instance name and schema
	// name), the database name to be used is the more specific layer (e.g.
	// Oracle schema name).
	DBNameKey = attribute.Key("db.name")

	// DBStatementKey is the attribute Key conforming to the "db.statement"
	// semantic conventions. It represents the database statement being
	// executed.
	//
	// Type: string
	// RequirementLevel: Recommended (Should be collected by default only if
	// there is sanitization that excludes sensitive information.)
	// Stability: stable
	// Examples: 'SELECT * FROM wuser_table', 'SET mykey "WuValue"'
	DBStatementKey = attribute.Key("db.statement")

	// DBOperationKey is the attribute Key conforming to the "db.operation"
	// semantic conventions. It represents the name of the operation being
	// executed, e.g. the [MongoDB command
	// name](https://docs.mongodb.com/manual/reference/command/#database-operations)
	// such as `findAndModify`, or the SQL keyword.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If `db.statement` is not
	// applicable.)
	// Stability: stable
	// Examples: 'findAndModify', 'HMSET', 'SELECT'
	// Note: When setting this to an SQL keyword, it is not recommended to
	// attempt any client-side parsing of `db.statement` just to get this
	// property, but it should be set if the operation name is provided by the
	// library being instrumented. If the SQL statement has an ambiguous
	// operation, or performs more than one operation, this value may be
	// omitted.
	DBOperationKey = attribute.Key("db.operation")
)

The attributes used to perform database client calls.

View Source
const (
	// DBCassandraPageSizeKey is the attribute Key conforming to the
	// "db.cassandra.page_size" semantic conventions. It represents the fetch
	// size used for paging, i.e. how many rows will be returned at once.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 5000
	DBCassandraPageSizeKey = attribute.Key("db.cassandra.page_size")

	// DBCassandraConsistencyLevelKey is the attribute Key conforming to the
	// "db.cassandra.consistency_level" semantic conventions. It represents the
	// consistency level of the query. Based on consistency values from
	// [CQL](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/dml/dmlConfigConsistency.html).
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	DBCassandraConsistencyLevelKey = attribute.Key("db.cassandra.consistency_level")

	// DBCassandraTableKey is the attribute Key conforming to the
	// "db.cassandra.table" semantic conventions. It represents the name of the
	// primary table that the operation is acting upon, including the keyspace
	// name (if applicable).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'mytable'
	// Note: This mirrors the db.sql.table attribute but references cassandra
	// rather than sql. It is not recommended to attempt any client-side
	// parsing of `db.statement` just to get this property, but it should be
	// set if it is provided by the library being instrumented. If the
	// operation is acting upon an anonymous table, or more than one table,
	// this value MUST NOT be set.
	DBCassandraTableKey = attribute.Key("db.cassandra.table")

	// DBCassandraIdempotenceKey is the attribute Key conforming to the
	// "db.cassandra.idempotence" semantic conventions. It represents the
	// whether or not the query is idempotent.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	DBCassandraIdempotenceKey = attribute.Key("db.cassandra.idempotence")

	// DBCassandraSpeculativeExecutionCountKey is the attribute Key conforming
	// to the "db.cassandra.speculative_execution_count" semantic conventions.
	// It represents the number of times a query was speculatively executed.
	// Not set or `0` if the query was not executed speculatively.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 0, 2
	DBCassandraSpeculativeExecutionCountKey = attribute.Key("db.cassandra.speculative_execution_count")

	// DBCassandraCoordinatorIDKey is the attribute Key conforming to the
	// "db.cassandra.coordinator.id" semantic conventions. It represents the ID
	// of the coordinating node for a query.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'be13faa2-8574-4d71-926d-27f16cf8a7af'
	DBCassandraCoordinatorIDKey = attribute.Key("db.cassandra.coordinator.id")

	// DBCassandraCoordinatorDCKey is the attribute Key conforming to the
	// "db.cassandra.coordinator.dc" semantic conventions. It represents the
	// data center of the coordinating node for a query.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'us-west-2'
	DBCassandraCoordinatorDCKey = attribute.Key("db.cassandra.coordinator.dc")
)

Call-level attributes for Cassandra

View Source
const (
	// DBCosmosDBClientIDKey is the attribute Key conforming to the
	// "db.cosmosdb.client_id" semantic conventions. It represents the unique
	// Cosmos client instance id.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '3ba4827d-4422-483f-b59f-85b74211c11d'
	DBCosmosDBClientIDKey = attribute.Key("db.cosmosdb.client_id")

	// DBCosmosDBOperationTypeKey is the attribute Key conforming to the
	// "db.cosmosdb.operation_type" semantic conventions. It represents the
	// cosmosDB Operation Type.
	//
	// Type: Enum
	// RequirementLevel: ConditionallyRequired (when performing one of the
	// operations in this list)
	// Stability: stable
	DBCosmosDBOperationTypeKey = attribute.Key("db.cosmosdb.operation_type")

	// DBCosmosDBConnectionModeKey is the attribute Key conforming to the
	// "db.cosmosdb.connection_mode" semantic conventions. It represents the
	// cosmos client connection mode.
	//
	// Type: Enum
	// RequirementLevel: ConditionallyRequired (if not `direct` (or pick gw as
	// default))
	// Stability: stable
	DBCosmosDBConnectionModeKey = attribute.Key("db.cosmosdb.connection_mode")

	// DBCosmosDBContainerKey is the attribute Key conforming to the
	// "db.cosmosdb.container" semantic conventions. It represents the cosmos
	// DB container name.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (if available)
	// Stability: stable
	// Examples: 'anystring'
	DBCosmosDBContainerKey = attribute.Key("db.cosmosdb.container")

	// DBCosmosDBRequestContentLengthKey is the attribute Key conforming to the
	// "db.cosmosdb.request_content_length" semantic conventions. It represents
	// the request payload size in bytes
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	DBCosmosDBRequestContentLengthKey = attribute.Key("db.cosmosdb.request_content_length")

	// DBCosmosDBStatusCodeKey is the attribute Key conforming to the
	// "db.cosmosdb.status_code" semantic conventions. It represents the cosmos
	// DB status code.
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (if response was received)
	// Stability: stable
	// Examples: 200, 201
	DBCosmosDBStatusCodeKey = attribute.Key("db.cosmosdb.status_code")

	// DBCosmosDBSubStatusCodeKey is the attribute Key conforming to the
	// "db.cosmosdb.sub_status_code" semantic conventions. It represents the
	// cosmos DB sub status code.
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (when response was received and
	// contained sub-code.)
	// Stability: stable
	// Examples: 1000, 1002
	DBCosmosDBSubStatusCodeKey = attribute.Key("db.cosmosdb.sub_status_code")

	// DBCosmosDBRequestChargeKey is the attribute Key conforming to the
	// "db.cosmosdb.request_charge" semantic conventions. It represents the rU
	// consumed for that operation
	//
	// Type: double
	// RequirementLevel: ConditionallyRequired (when available)
	// Stability: stable
	// Examples: 46.18, 1.0
	DBCosmosDBRequestChargeKey = attribute.Key("db.cosmosdb.request_charge")
)

Call-level attributes for Cosmos DB.

View Source
const (
	// OTelStatusCodeKey is the attribute Key conforming to the
	// "otel.status_code" semantic conventions. It represents the name of the
	// code, either "OK" or "ERROR". MUST NOT be set if the status code is
	// UNSET.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	OTelStatusCodeKey = attribute.Key("otel.status_code")

	// OTelStatusDescriptionKey is the attribute Key conforming to the
	// "otel.status_description" semantic conventions. It represents the
	// description of the Status if it has a value, otherwise not set.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'resource not found'
	OTelStatusDescriptionKey = attribute.Key("otel.status_description")
)

Span attributes used by non-OTLP exporters to represent OpenTelemetry Span's concepts.

View Source
const (
	// FaaSTriggerKey is the attribute Key conforming to the "faas.trigger"
	// semantic conventions. It represents the type of the trigger which caused
	// this function invocation.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Note: For the server/consumer span on the incoming side,
	// `faas.trigger` MUST be set.
	//
	// Clients invoking FaaS instances usually cannot set `faas.trigger`,
	// since they would typically need to look in the payload to determine
	// the event type. If clients set it, it should be the same as the
	// trigger that corresponding incoming would have (i.e., this has
	// nothing to do with the underlying transport used to make the API
	// call to invoke the lambda, which is often HTTP).
	FaaSTriggerKey = attribute.Key("faas.trigger")

	// FaaSInvocationIDKey is the attribute Key conforming to the
	// "faas.invocation_id" semantic conventions. It represents the invocation
	// ID of the current function invocation.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'af9d5aa4-a685-4c5f-a22b-444f80b3cc28'
	FaaSInvocationIDKey = attribute.Key("faas.invocation_id")
)

This semantic convention describes an instance of a function that runs without provisioning or managing of servers (also known as serverless functions or Function as a Service (FaaS)) with spans.

View Source
const (
	// FaaSDocumentCollectionKey is the attribute Key conforming to the
	// "faas.document.collection" semantic conventions. It represents the name
	// of the source on which the triggering operation was performed. For
	// example, in Cloud Storage or S3 corresponds to the bucket name, and in
	// Cosmos DB to the database name.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'myBucketName', 'myDBName'
	FaaSDocumentCollectionKey = attribute.Key("faas.document.collection")

	// FaaSDocumentOperationKey is the attribute Key conforming to the
	// "faas.document.operation" semantic conventions. It represents the
	// describes the type of the operation that was performed on the data.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	FaaSDocumentOperationKey = attribute.Key("faas.document.operation")

	// FaaSDocumentTimeKey is the attribute Key conforming to the
	// "faas.document.time" semantic conventions. It represents a string
	// containing the time when the data was accessed in the [ISO
	// 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format
	// expressed in [UTC](https://www.w3.org/TR/NOTE-datetime).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '2020-01-23T13:47:06Z'
	FaaSDocumentTimeKey = attribute.Key("faas.document.time")

	// FaaSDocumentNameKey is the attribute Key conforming to the
	// "faas.document.name" semantic conventions. It represents the document
	// name/table subjected to the operation. For example, in Cloud Storage or
	// S3 is the name of the file, and in Cosmos DB the table name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'myFile.txt', 'myTableName'
	FaaSDocumentNameKey = attribute.Key("faas.document.name")
)

Semantic Convention for FaaS triggered as a response to some data source operation such as a database or filesystem read/write.

View Source
const (
	// FaaSTimeKey is the attribute Key conforming to the "faas.time" semantic
	// conventions. It represents a string containing the function invocation
	// time in the [ISO
	// 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format
	// expressed in [UTC](https://www.w3.org/TR/NOTE-datetime).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '2020-01-23T13:47:06Z'
	FaaSTimeKey = attribute.Key("faas.time")

	// FaaSCronKey is the attribute Key conforming to the "faas.cron" semantic
	// conventions. It represents a string containing the schedule period as
	// [Cron
	// Expression](https://docs.oracle.com/cd/E12058_01/doc/doc.1014/e12030/cron_expressions.htm).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '0/5 * * * ? *'
	FaaSCronKey = attribute.Key("faas.cron")
)

Semantic Convention for FaaS scheduled to be executed regularly.

View Source
const (
	// FaaSInvokedNameKey is the attribute Key conforming to the
	// "faas.invoked_name" semantic conventions. It represents the name of the
	// invoked function.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'my-function'
	// Note: SHOULD be equal to the `faas.name` resource attribute of the
	// invoked function.
	FaaSInvokedNameKey = attribute.Key("faas.invoked_name")

	// FaaSInvokedProviderKey is the attribute Key conforming to the
	// "faas.invoked_provider" semantic conventions. It represents the cloud
	// provider of the invoked function.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	// Note: SHOULD be equal to the `cloud.provider` resource attribute of the
	// invoked function.
	FaaSInvokedProviderKey = attribute.Key("faas.invoked_provider")

	// FaaSInvokedRegionKey is the attribute Key conforming to the
	// "faas.invoked_region" semantic conventions. It represents the cloud
	// region of the invoked function.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (For some cloud providers, like
	// AWS or GCP, the region in which a function is hosted is essential to
	// uniquely identify the function and also part of its endpoint. Since it's
	// part of the endpoint being called, the region is always known to
	// clients. In these cases, `faas.invoked_region` MUST be set accordingly.
	// If the region is unknown to the client or not required for identifying
	// the invoked function, setting `faas.invoked_region` is optional.)
	// Stability: stable
	// Examples: 'eu-central-1'
	// Note: SHOULD be equal to the `cloud.region` resource attribute of the
	// invoked function.
	FaaSInvokedRegionKey = attribute.Key("faas.invoked_region")
)

Contains additional attributes for outgoing FaaS spans.

View Source
const (
	// EnduserIDKey is the attribute Key conforming to the "enduser.id"
	// semantic conventions. It represents the username or client_id extracted
	// from the access token or
	// [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) header
	// in the inbound request from outside the system.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'username'
	EnduserIDKey = attribute.Key("enduser.id")

	// EnduserRoleKey is the attribute Key conforming to the "enduser.role"
	// semantic conventions. It represents the actual/assumed role the client
	// is making the request under extracted from token or application security
	// context.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'admin'
	EnduserRoleKey = attribute.Key("enduser.role")

	// EnduserScopeKey is the attribute Key conforming to the "enduser.scope"
	// semantic conventions. It represents the scopes or granted authorities
	// the client currently possesses extracted from token or application
	// security context. The value would come from the scope associated with an
	// [OAuth 2.0 Access
	// Token](https://tools.ietf.org/html/rfc6749#section-3.3) or an attribute
	// value in a [SAML 2.0
	// Assertion](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'read:message, write:files'
	EnduserScopeKey = attribute.Key("enduser.scope")
)

These attributes may be used for any operation with an authenticated and/or authorized enduser.

View Source
const (
	// ThreadIDKey is the attribute Key conforming to the "thread.id" semantic
	// conventions. It represents the current "managed" thread ID (as opposed
	// to OS thread ID).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 42
	ThreadIDKey = attribute.Key("thread.id")

	// ThreadNameKey is the attribute Key conforming to the "thread.name"
	// semantic conventions. It represents the current thread name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'main'
	ThreadNameKey = attribute.Key("thread.name")
)

These attributes may be used for any operation to store information about a thread that started a span.

View Source
const (
	// CodeFunctionKey is the attribute Key conforming to the "code.function"
	// semantic conventions. It represents the method or function name, or
	// equivalent (usually rightmost part of the code unit's name).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'serveRequest'
	CodeFunctionKey = attribute.Key("code.function")

	// CodeNamespaceKey is the attribute Key conforming to the "code.namespace"
	// semantic conventions. It represents the "namespace" within which
	// `code.function` is defined. Usually the qualified class or module name,
	// such that `code.namespace` + some separator + `code.function` form a
	// unique identifier for the code unit.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'com.example.MyHTTPService'
	CodeNamespaceKey = attribute.Key("code.namespace")

	// CodeFilepathKey is the attribute Key conforming to the "code.filepath"
	// semantic conventions. It represents the source code file name that
	// identifies the code unit as uniquely as possible (preferably an absolute
	// file path).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/usr/local/MyApplication/content_root/app/index.php'
	CodeFilepathKey = attribute.Key("code.filepath")

	// CodeLineNumberKey is the attribute Key conforming to the "code.lineno"
	// semantic conventions. It represents the line number in `code.filepath`
	// best representing the operation. It SHOULD point within the code unit
	// named in `code.function`.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 42
	CodeLineNumberKey = attribute.Key("code.lineno")

	// CodeColumnKey is the attribute Key conforming to the "code.column"
	// semantic conventions. It represents the column number in `code.filepath`
	// best representing the operation. It SHOULD point within the code unit
	// named in `code.function`.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 16
	CodeColumnKey = attribute.Key("code.column")
)

These attributes allow to report this unit of code and therefore to provide more context about the span.

View Source
const (
	// AWSDynamoDBTableNamesKey is the attribute Key conforming to the
	// "aws.dynamodb.table_names" semantic conventions. It represents the keys
	// in the `RequestItems` object field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Users', 'Cats'
	AWSDynamoDBTableNamesKey = attribute.Key("aws.dynamodb.table_names")

	// AWSDynamoDBConsumedCapacityKey is the attribute Key conforming to the
	// "aws.dynamodb.consumed_capacity" semantic conventions. It represents the
	// JSON-serialized value of each item in the `ConsumedCapacity` response
	// field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '{ "CapacityUnits": number, "GlobalSecondaryIndexes": {
	// "string" : { "CapacityUnits": number, "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number } }, "LocalSecondaryIndexes": { "string" :
	// { "CapacityUnits": number, "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number } }, "ReadCapacityUnits": number, "Table":
	// { "CapacityUnits": number, "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number }, "TableName": "string",
	// "WriteCapacityUnits": number }'
	AWSDynamoDBConsumedCapacityKey = attribute.Key("aws.dynamodb.consumed_capacity")

	// AWSDynamoDBItemCollectionMetricsKey is the attribute Key conforming to
	// the "aws.dynamodb.item_collection_metrics" semantic conventions. It
	// represents the JSON-serialized value of the `ItemCollectionMetrics`
	// response field.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '{ "string" : [ { "ItemCollectionKey": { "string" : { "B":
	// blob, "BOOL": boolean, "BS": [ blob ], "L": [ "AttributeValue" ], "M": {
	// "string" : "AttributeValue" }, "N": "string", "NS": [ "string" ],
	// "NULL": boolean, "S": "string", "SS": [ "string" ] } },
	// "SizeEstimateRangeGB": [ number ] } ] }'
	AWSDynamoDBItemCollectionMetricsKey = attribute.Key("aws.dynamodb.item_collection_metrics")

	// AWSDynamoDBProvisionedReadCapacityKey is the attribute Key conforming to
	// the "aws.dynamodb.provisioned_read_capacity" semantic conventions. It
	// represents the value of the `ProvisionedThroughput.ReadCapacityUnits`
	// request parameter.
	//
	// Type: double
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 1.0, 2.0
	AWSDynamoDBProvisionedReadCapacityKey = attribute.Key("aws.dynamodb.provisioned_read_capacity")

	// AWSDynamoDBProvisionedWriteCapacityKey is the attribute Key conforming
	// to the "aws.dynamodb.provisioned_write_capacity" semantic conventions.
	// It represents the value of the
	// `ProvisionedThroughput.WriteCapacityUnits` request parameter.
	//
	// Type: double
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 1.0, 2.0
	AWSDynamoDBProvisionedWriteCapacityKey = attribute.Key("aws.dynamodb.provisioned_write_capacity")

	// AWSDynamoDBConsistentReadKey is the attribute Key conforming to the
	// "aws.dynamodb.consistent_read" semantic conventions. It represents the
	// value of the `ConsistentRead` request parameter.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	AWSDynamoDBConsistentReadKey = attribute.Key("aws.dynamodb.consistent_read")

	// AWSDynamoDBProjectionKey is the attribute Key conforming to the
	// "aws.dynamodb.projection" semantic conventions. It represents the value
	// of the `ProjectionExpression` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Title', 'Title, Price, Color', 'Title, Description,
	// RelatedItems, ProductReviews'
	AWSDynamoDBProjectionKey = attribute.Key("aws.dynamodb.projection")

	// AWSDynamoDBLimitKey is the attribute Key conforming to the
	// "aws.dynamodb.limit" semantic conventions. It represents the value of
	// the `Limit` request parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 10
	AWSDynamoDBLimitKey = attribute.Key("aws.dynamodb.limit")

	// AWSDynamoDBAttributesToGetKey is the attribute Key conforming to the
	// "aws.dynamodb.attributes_to_get" semantic conventions. It represents the
	// value of the `AttributesToGet` request parameter.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'lives', 'id'
	AWSDynamoDBAttributesToGetKey = attribute.Key("aws.dynamodb.attributes_to_get")

	// AWSDynamoDBIndexNameKey is the attribute Key conforming to the
	// "aws.dynamodb.index_name" semantic conventions. It represents the value
	// of the `IndexName` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'name_to_group'
	AWSDynamoDBIndexNameKey = attribute.Key("aws.dynamodb.index_name")

	// AWSDynamoDBSelectKey is the attribute Key conforming to the
	// "aws.dynamodb.select" semantic conventions. It represents the value of
	// the `Select` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'ALL_ATTRIBUTES', 'COUNT'
	AWSDynamoDBSelectKey = attribute.Key("aws.dynamodb.select")
)

Attributes that exist for multiple DynamoDB request types.

View Source
const (
	// AWSDynamoDBGlobalSecondaryIndexesKey is the attribute Key conforming to
	// the "aws.dynamodb.global_secondary_indexes" semantic conventions. It
	// represents the JSON-serialized value of each item of the
	// `GlobalSecondaryIndexes` request field
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '{ "IndexName": "string", "KeySchema": [ { "AttributeName":
	// "string", "KeyType": "string" } ], "Projection": { "NonKeyAttributes": [
	// "string" ], "ProjectionType": "string" }, "ProvisionedThroughput": {
	// "ReadCapacityUnits": number, "WriteCapacityUnits": number } }'
	AWSDynamoDBGlobalSecondaryIndexesKey = attribute.Key("aws.dynamodb.global_secondary_indexes")

	// AWSDynamoDBLocalSecondaryIndexesKey is the attribute Key conforming to
	// the "aws.dynamodb.local_secondary_indexes" semantic conventions. It
	// represents the JSON-serialized value of each item of the
	// `LocalSecondaryIndexes` request field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '{ "IndexARN": "string", "IndexName": "string",
	// "IndexSizeBytes": number, "ItemCount": number, "KeySchema": [ {
	// "AttributeName": "string", "KeyType": "string" } ], "Projection": {
	// "NonKeyAttributes": [ "string" ], "ProjectionType": "string" } }'
	AWSDynamoDBLocalSecondaryIndexesKey = attribute.Key("aws.dynamodb.local_secondary_indexes")
)

DynamoDB.CreateTable

View Source
const (
	// AWSDynamoDBExclusiveStartTableKey is the attribute Key conforming to the
	// "aws.dynamodb.exclusive_start_table" semantic conventions. It represents
	// the value of the `ExclusiveStartTableName` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Users', 'CatsTable'
	AWSDynamoDBExclusiveStartTableKey = attribute.Key("aws.dynamodb.exclusive_start_table")

	// AWSDynamoDBTableCountKey is the attribute Key conforming to the
	// "aws.dynamodb.table_count" semantic conventions. It represents the the
	// number of items in the `TableNames` response parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 20
	AWSDynamoDBTableCountKey = attribute.Key("aws.dynamodb.table_count")
)

DynamoDB.ListTables

View Source
const (
	// AWSDynamoDBSegmentKey is the attribute Key conforming to the
	// "aws.dynamodb.segment" semantic conventions. It represents the value of
	// the `Segment` request parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 10
	AWSDynamoDBSegmentKey = attribute.Key("aws.dynamodb.segment")

	// AWSDynamoDBTotalSegmentsKey is the attribute Key conforming to the
	// "aws.dynamodb.total_segments" semantic conventions. It represents the
	// value of the `TotalSegments` request parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 100
	AWSDynamoDBTotalSegmentsKey = attribute.Key("aws.dynamodb.total_segments")

	// AWSDynamoDBCountKey is the attribute Key conforming to the
	// "aws.dynamodb.count" semantic conventions. It represents the value of
	// the `Count` response parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 10
	AWSDynamoDBCountKey = attribute.Key("aws.dynamodb.count")

	// AWSDynamoDBScannedCountKey is the attribute Key conforming to the
	// "aws.dynamodb.scanned_count" semantic conventions. It represents the
	// value of the `ScannedCount` response parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 50
	AWSDynamoDBScannedCountKey = attribute.Key("aws.dynamodb.scanned_count")
)

DynamoDB.Scan

View Source
const (
	// AWSDynamoDBAttributeDefinitionsKey is the attribute Key conforming to
	// the "aws.dynamodb.attribute_definitions" semantic conventions. It
	// represents the JSON-serialized value of each item in the
	// `AttributeDefinitions` request field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '{ "AttributeName": "string", "AttributeType": "string" }'
	AWSDynamoDBAttributeDefinitionsKey = attribute.Key("aws.dynamodb.attribute_definitions")

	// AWSDynamoDBGlobalSecondaryIndexUpdatesKey is the attribute Key
	// conforming to the "aws.dynamodb.global_secondary_index_updates" semantic
	// conventions. It represents the JSON-serialized value of each item in the
	// the `GlobalSecondaryIndexUpdates` request field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '{ "Create": { "IndexName": "string", "KeySchema": [ {
	// "AttributeName": "string", "KeyType": "string" } ], "Projection": {
	// "NonKeyAttributes": [ "string" ], "ProjectionType": "string" },
	// "ProvisionedThroughput": { "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number } }'
	AWSDynamoDBGlobalSecondaryIndexUpdatesKey = attribute.Key("aws.dynamodb.global_secondary_index_updates")
)

DynamoDB.UpdateTable

View Source
const (
	// AWSS3BucketKey is the attribute Key conforming to the "aws.s3.bucket"
	// semantic conventions. It represents the S3 bucket name the request
	// refers to. Corresponds to the `--bucket` parameter of the [S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)
	// operations.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'some-bucket-name'
	// Note: The `bucket` attribute is applicable to all S3 operations that
	// reference a bucket, i.e. that require the bucket name as a mandatory
	// parameter.
	// This applies to almost all S3 operations except `list-buckets`.
	AWSS3BucketKey = attribute.Key("aws.s3.bucket")

	// AWSS3KeyKey is the attribute Key conforming to the "aws.s3.key" semantic
	// conventions. It represents the S3 object key the request refers to.
	// Corresponds to the `--key` parameter of the [S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)
	// operations.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'someFile.yml'
	// Note: The `key` attribute is applicable to all object-related S3
	// operations, i.e. that require the object key as a mandatory parameter.
	// This applies in particular to the following operations:
	//
	// -
	// [copy-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/copy-object.html)
	// -
	// [delete-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html)
	// -
	// [get-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html)
	// -
	// [head-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/head-object.html)
	// -
	// [put-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html)
	// -
	// [restore-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/restore-object.html)
	// -
	// [select-object-content](https://docs.aws.amazon.com/cli/latest/reference/s3api/select-object-content.html)
	// -
	// [abort-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/s3api/abort-multipart-upload.html)
	// -
	// [complete-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/s3api/complete-multipart-upload.html)
	// -
	// [create-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/s3api/create-multipart-upload.html)
	// -
	// [list-parts](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-parts.html)
	// -
	// [upload-part](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html)
	// -
	// [upload-part-copy](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html)
	AWSS3KeyKey = attribute.Key("aws.s3.key")

	// AWSS3CopySourceKey is the attribute Key conforming to the
	// "aws.s3.copy_source" semantic conventions. It represents the source
	// object (in the form `bucket`/`key`) for the copy operation.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'someFile.yml'
	// Note: The `copy_source` attribute applies to S3 copy operations and
	// corresponds to the `--copy-source` parameter
	// of the [copy-object operation within the S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/copy-object.html).
	// This applies in particular to the following operations:
	//
	// -
	// [copy-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/copy-object.html)
	// -
	// [upload-part-copy](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html)
	AWSS3CopySourceKey = attribute.Key("aws.s3.copy_source")

	// AWSS3UploadIDKey is the attribute Key conforming to the
	// "aws.s3.upload_id" semantic conventions. It represents the upload ID
	// that identifies the multipart upload.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'dfRtDYWFbkRONycy.Yxwh66Yjlx.cph0gtNBtJ'
	// Note: The `upload_id` attribute applies to S3 multipart-upload
	// operations and corresponds to the `--upload-id` parameter
	// of the [S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)
	// multipart operations.
	// This applies in particular to the following operations:
	//
	// -
	// [abort-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/s3api/abort-multipart-upload.html)
	// -
	// [complete-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/s3api/complete-multipart-upload.html)
	// -
	// [list-parts](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-parts.html)
	// -
	// [upload-part](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html)
	// -
	// [upload-part-copy](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html)
	AWSS3UploadIDKey = attribute.Key("aws.s3.upload_id")

	// AWSS3DeleteKey is the attribute Key conforming to the "aws.s3.delete"
	// semantic conventions. It represents the delete request container that
	// specifies the objects to be deleted.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples:
	// 'Objects=[{Key=string,VersionID=string},{Key=string,VersionID=string}],Quiet=boolean'
	// Note: The `delete` attribute is only applicable to the
	// [delete-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html)
	// operation.
	// The `delete` attribute corresponds to the `--delete` parameter of the
	// [delete-objects operation within the S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-objects.html).
	AWSS3DeleteKey = attribute.Key("aws.s3.delete")

	// AWSS3PartNumberKey is the attribute Key conforming to the
	// "aws.s3.part_number" semantic conventions. It represents the part number
	// of the part being uploaded in a multipart-upload operation. This is a
	// positive integer between 1 and 10,000.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 3456
	// Note: The `part_number` attribute is only applicable to the
	// [upload-part](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html)
	// and
	// [upload-part-copy](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html)
	// operations.
	// The `part_number` attribute corresponds to the `--part-number` parameter
	// of the
	// [upload-part operation within the S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html).
	AWSS3PartNumberKey = attribute.Key("aws.s3.part_number")
)

Attributes that exist for S3 request types.

View Source
const (
	// GraphqlOperationNameKey is the attribute Key conforming to the
	// "graphql.operation.name" semantic conventions. It represents the name of
	// the operation being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'findBookByID'
	GraphqlOperationNameKey = attribute.Key("graphql.operation.name")

	// GraphqlOperationTypeKey is the attribute Key conforming to the
	// "graphql.operation.type" semantic conventions. It represents the type of
	// the operation being executed.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'query', 'mutation', 'subscription'
	GraphqlOperationTypeKey = attribute.Key("graphql.operation.type")

	// GraphqlDocumentKey is the attribute Key conforming to the
	// "graphql.document" semantic conventions. It represents the GraphQL
	// document being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'query findBookByID { bookByID(id: ?) { name } }'
	// Note: The value may be sanitized to exclude sensitive information.
	GraphqlDocumentKey = attribute.Key("graphql.document")
)

Semantic conventions to apply when instrumenting the GraphQL implementation. They map GraphQL operations to attributes on a Span.

View Source
const (
	// MessagingSystemKey is the attribute Key conforming to the
	// "messaging.system" semantic conventions. It represents a string
	// identifying the messaging system.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'kafka', 'rabbitmq', 'rocketmq', 'activemq', 'AmazonSQS'
	MessagingSystemKey = attribute.Key("messaging.system")

	// MessagingOperationKey is the attribute Key conforming to the
	// "messaging.operation" semantic conventions. It represents a string
	// identifying the kind of messaging operation as defined in the [Operation
	// names](#operation-names) section above.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	// Note: If a custom value is used, it MUST be of low cardinality.
	MessagingOperationKey = attribute.Key("messaging.operation")

	// MessagingBatchMessageCountKey is the attribute Key conforming to the
	// "messaging.batch.message_count" semantic conventions. It represents the
	// number of messages sent, received, or processed in the scope of the
	// batching operation.
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (If the span describes an
	// operation on a batch of messages.)
	// Stability: stable
	// Examples: 0, 1, 2
	// Note: Instrumentations SHOULD NOT set `messaging.batch.message_count` on
	// spans that operate with a single message. When a messaging client
	// library supports both batch and single-message API for the same
	// operation, instrumentations SHOULD use `messaging.batch.message_count`
	// for batching APIs and SHOULD NOT use it for single-message APIs.
	MessagingBatchMessageCountKey = attribute.Key("messaging.batch.message_count")

	// MessagingClientIDKey is the attribute Key conforming to the
	// "messaging.client_id" semantic conventions. It represents a unique
	// identifier for the client that consumes or produces a message.
	//
	// Type: string
	// RequirementLevel: Recommended (If a client id is available)
	// Stability: stable
	// Examples: 'client-5', 'myhost@8742@s8083jm'
	MessagingClientIDKey = attribute.Key("messaging.client_id")
)

General attributes used in messaging systems.

View Source
const (
	// RPCSystemKey is the attribute Key conforming to the "rpc.system"
	// semantic conventions. It represents a string identifying the remoting
	// system. See below for a list of well-known identifiers.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	RPCSystemKey = attribute.Key("rpc.system")

	// RPCServiceKey is the attribute Key conforming to the "rpc.service"
	// semantic conventions. It represents the full (logical) name of the
	// service being called, including its package name, if applicable.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'myservice.EchoService'
	// Note: This is the logical name of the service from the RPC interface
	// perspective, which can be different from the name of any implementing
	// class. The `code.namespace` attribute may be used to store the latter
	// (despite the attribute name, it may include a class name; e.g., class
	// with method actually executing the call on the server side, RPC client
	// stub class on the client side).
	RPCServiceKey = attribute.Key("rpc.service")

	// RPCMethodKey is the attribute Key conforming to the "rpc.method"
	// semantic conventions. It represents the name of the (logical) method
	// being called, must be equal to the $method part in the span name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'exampleMethod'
	// Note: This is the logical name of the method from the RPC interface
	// perspective, which can be different from the name of any implementing
	// method/function. The `code.function` attribute may be used to store the
	// latter (e.g., method actually executing the call on the server side, RPC
	// client stub method on the client side).
	RPCMethodKey = attribute.Key("rpc.method")
)

Semantic conventions for remote procedure calls.

View Source
const (
	// RPCJsonrpcVersionKey is the attribute Key conforming to the
	// "rpc.jsonrpc.version" semantic conventions. It represents the protocol
	// version as in `jsonrpc` property of request/response. Since JSON-RPC 1.0
	// does not specify this, the value can be omitted.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If other than the default
	// version (`1.0`))
	// Stability: stable
	// Examples: '2.0', '1.0'
	RPCJsonrpcVersionKey = attribute.Key("rpc.jsonrpc.version")

	// RPCJsonrpcRequestIDKey is the attribute Key conforming to the
	// "rpc.jsonrpc.request_id" semantic conventions. It represents the `id`
	// property of request or response. Since protocol allows id to be int,
	// string, `null` or missing (for notifications), value is expected to be
	// cast to string for simplicity. Use empty string in case of `null` value.
	// Omit entirely if this is a notification.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '10', 'request-7', ”
	RPCJsonrpcRequestIDKey = attribute.Key("rpc.jsonrpc.request_id")

	// RPCJsonrpcErrorCodeKey is the attribute Key conforming to the
	// "rpc.jsonrpc.error_code" semantic conventions. It represents the
	// `error.code` property of response if it is an error response.
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (If response is not successful.)
	// Stability: stable
	// Examples: -32700, 100
	RPCJsonrpcErrorCodeKey = attribute.Key("rpc.jsonrpc.error_code")

	// RPCJsonrpcErrorMessageKey is the attribute Key conforming to the
	// "rpc.jsonrpc.error_message" semantic conventions. It represents the
	// `error.message` property of response if it is an error response.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'Parse error', 'User already exists'
	RPCJsonrpcErrorMessageKey = attribute.Key("rpc.jsonrpc.error_message")
)

Tech-specific attributes for [JSON RPC](https://www.jsonrpc.org/).

View Source
const (
	// AWSDynamoDBScanForwardKey is the attribute Key conforming to the
	// "aws.dynamodb.scan_forward" semantic conventions. It represents the
	// value of the `ScanIndexForward` request parameter.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	AWSDynamoDBScanForwardKey = attribute.Key("aws.dynamodb.scan_forward")
)

DynamoDB.Query

View Source
const (
	// AWSEKSClusterARNKey is the attribute Key conforming to the
	// "aws.eks.cluster.arn" semantic conventions. It represents the ARN of an
	// EKS cluster.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'arn:aws:ecs:us-west-2:123456789123:cluster/my-cluster'
	AWSEKSClusterARNKey = attribute.Key("aws.eks.cluster.arn")
)

Resources used by AWS Elastic Kubernetes Service (EKS).

View Source
const (
	// AWSLambdaInvokedARNKey is the attribute Key conforming to the
	// "aws.lambda.invoked_arn" semantic conventions. It represents the full
	// invoked ARN as provided on the `Context` passed to the function
	// (`Lambda-Runtime-Invoked-Function-ARN` header on the
	// `/runtime/invocation/next` applicable).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'arn:aws:lambda:us-east-1:123456:function:myfunction:myalias'
	// Note: This may be different from `cloud.resource_id` if an alias is
	// involved.
	AWSLambdaInvokedARNKey = attribute.Key("aws.lambda.invoked_arn")
)

Span attributes used by AWS Lambda (in addition to general `faas` attributes).

View Source
const (
	// AWSRequestIDKey is the attribute Key conforming to the "aws.request_id"
	// semantic conventions. It represents the AWS request ID as returned in
	// the response headers `x-amz-request-id` or `x-amz-requestid`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '79b9da39-b7ae-508a-a6bc-864b2829c622', 'C9ER4AJX75574TDJ'
	AWSRequestIDKey = attribute.Key("aws.request_id")
)

The `aws` conventions apply to operations using the AWS SDK. They map request or response parameters in AWS SDK API calls to attributes on a Span. The conventions have been collected over time based on feedback from AWS users of tracing and will continue to evolve as new interesting conventions are found. Some descriptions are also provided for populating general OpenTelemetry semantic conventions based on these APIs.

View Source
const (
	// DBMSSQLInstanceNameKey is the attribute Key conforming to the
	// "db.mssql.instance_name" semantic conventions. It represents the
	// Microsoft SQL Server [instance
	// name](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=sql-server-ver15)
	// connecting to. This name is used to determine the port of a named
	// instance.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'MSSQLSERVER'
	// Note: If setting a `db.mssql.instance_name`, `server.port` is no longer
	// required (but still recommended if non-standard).
	DBMSSQLInstanceNameKey = attribute.Key("db.mssql.instance_name")
)

Connection-level attributes for Microsoft SQL Server

View Source
const (
	// DBMongoDBCollectionKey is the attribute Key conforming to the
	// "db.mongodb.collection" semantic conventions. It represents the
	// collection being accessed within the database stated in `db.name`.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'customers', 'products'
	DBMongoDBCollectionKey = attribute.Key("db.mongodb.collection")
)

Call-level attributes for MongoDB

View Source
const (
	// DBRedisDBIndexKey is the attribute Key conforming to the
	// "db.redis.database_index" semantic conventions. It represents the index
	// of the database being accessed as used in the [`SELECT`
	// command](https://redis.io/commands/select), provided as an integer. To
	// be used instead of the generic `db.name` attribute.
	//
	// Type: int
	// RequirementLevel: ConditionallyRequired (If other than the default
	// database (`0`).)
	// Stability: stable
	// Examples: 0, 1, 15
	DBRedisDBIndexKey = attribute.Key("db.redis.database_index")
)

Call-level attributes for Redis

View Source
const (
	// DBSQLTableKey is the attribute Key conforming to the "db.sql.table"
	// semantic conventions. It represents the name of the primary table that
	// the operation is acting upon, including the database name (if
	// applicable).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: stable
	// Examples: 'public.users', 'customers'
	// Note: It is not recommended to attempt any client-side parsing of
	// `db.statement` just to get this property, but it should be set if it is
	// provided by the library being instrumented. If the operation is acting
	// upon an anonymous table, or more than one table, this value MUST NOT be
	// set.
	DBSQLTableKey = attribute.Key("db.sql.table")
)

Call-level attributes for SQL databases

View Source
const (
	// DeploymentEnvironmentKey is the attribute Key conforming to the
	// "deployment.environment" semantic conventions. It represents the name of
	// the [deployment
	// environment](https://en.wikipedia.org/wiki/Deployment_environment) (aka
	// deployment tier).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'staging', 'production'
	DeploymentEnvironmentKey = attribute.Key("deployment.environment")
)

The software deployment.

View Source
const (
	// ExceptionEscapedKey is the attribute Key conforming to the
	// "exception.escaped" semantic conventions. It represents the sHOULD be
	// set to true if the exception event is recorded at a point where it is
	// known that the exception is escaping the scope of the span.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	// Note: An exception is considered to have escaped (or left) the scope of
	// a span,
	// if that span is ended while the exception is still logically "in
	// flight".
	// This may be actually "in flight" in some languages (e.g. if the
	// exception
	// is passed to a Context manager's `__exit__` method in Python) but will
	// usually be caught at the point of recording the exception in most
	// languages.
	//
	// It is usually not possible to determine at the point where an exception
	// is thrown
	// whether it will escape the scope of a span.
	// However, it is trivial to know that an exception
	// will escape, if one checks for an active exception just before ending
	// the span,
	// as done in the [example above](#recording-an-exception).
	//
	// It follows that an exception may still escape the scope of the span
	// even if the `exception.escaped` attribute was not set or set to false,
	// since the event might have been recorded at a time where it was not
	// clear whether the exception will escape.
	ExceptionEscapedKey = attribute.Key("exception.escaped")
)

The attributes used to report a single exception associated with a span.

View Source
const (
	// ExceptionEventName is the name of the Span event representing an exception.
	ExceptionEventName = "exception"
)
View Source
const (
	// FaaSColdstartKey is the attribute Key conforming to the "faas.coldstart"
	// semantic conventions. It represents a boolean that is true if the
	// serverless function is executed for the first time (aka cold-start).
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	FaaSColdstartKey = attribute.Key("faas.coldstart")
)

Contains additional attributes for incoming FaaS spans.

View Source
const (
	// HTTPResendCountKey is the attribute Key conforming to the
	// "http.resend_count" semantic conventions. It represents the ordinal
	// number of request resending attempt (for any reason, including
	// redirects).
	//
	// Type: int
	// RequirementLevel: Recommended (if and only if request was retried.)
	// Stability: stable
	// Examples: 3
	// Note: The resend count SHOULD be updated each time an HTTP request gets
	// resent by the client, regardless of what was the cause of the resending
	// (e.g. redirection, authorization failure, 503 Server Unavailable,
	// network issues, or any other).
	HTTPResendCountKey = attribute.Key("http.resend_count")
)

Semantic Convention for HTTP Client

View Source
const (
	// HTTPRouteKey is the attribute Key conforming to the "http.route"
	// semantic conventions. It represents the matched route (path template in
	// the format used by the respective server framework). See note below
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If and only if it's available)
	// Stability: stable
	// Examples: '/users/:userID?', '{controller}/{action}/{id?}'
	// Note: MUST NOT be populated when this is not supported by the HTTP
	// server framework as the route attribute should have low-cardinality and
	// the URI path can NOT substitute it.
	// SHOULD include the [application
	// root](/docs/http/http-spans.md#http-server-definitions) if there is one.
	HTTPRouteKey = attribute.Key("http.route")
)

HTTP Server attributes

View Source
const (
	// K8SNamespaceNameKey is the attribute Key conforming to the
	// "k8s.namespace.name" semantic conventions. It represents the name of the
	// namespace that the pod is running in.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'default'
	K8SNamespaceNameKey = attribute.Key("k8s.namespace.name")
)

A Kubernetes Namespace.

View Source
const (
	// LogIostreamKey is the attribute Key conforming to the "log.iostream"
	// semantic conventions. It represents the stream associated with the log.
	// See below for a list of well-known values.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	LogIostreamKey = attribute.Key("log.iostream")
)

Describes Log attributes

View Source
const (
	// LogRecordUIDKey is the attribute Key conforming to the "log.record.uid"
	// semantic conventions. It represents a unique identifier for the Log
	// Record.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '01ARZ3NDEKTSV4RRFFQ69G5FAV'
	// Note: If an id is provided, other log records with the same id will be
	// considered duplicates and can be removed safely. This means, that two
	// distinguishable log records MUST have different values.
	// The id MAY be an [Universally Unique Lexicographically Sortable
	// Identifier (ULID)](https://github.com/ulid/spec), but other identifiers
	// (e.g. UUID) may be used as needed.
	LogRecordUIDKey = attribute.Key("log.record.uid")
)

The attributes described in this section are rather generic. They may be used in any Log Record they apply to.

View Source
const (
	// MessagingRabbitmqDestinationRoutingKeyKey is the attribute Key
	// conforming to the "messaging.rabbitmq.destination.routing_key" semantic
	// conventions. It represents the rabbitMQ message routing key.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If not empty.)
	// Stability: stable
	// Examples: 'myKey'
	MessagingRabbitmqDestinationRoutingKeyKey = attribute.Key("messaging.rabbitmq.destination.routing_key")
)

Attributes for RabbitMQ

View Source
const (
	// OpentracingRefTypeKey is the attribute Key conforming to the
	// "opentracing.ref_type" semantic conventions. It represents the
	// parent-child Reference type
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Note: The causal relationship between a child Span and a parent Span.
	OpentracingRefTypeKey = attribute.Key("opentracing.ref_type")
)

Semantic conventions for the OpenTracing Shim

View Source
const (
	// PeerServiceKey is the attribute Key conforming to the "peer.service"
	// semantic conventions. It represents the
	// [`service.name`](/docs/resource/README.md#service) of the remote
	// service. SHOULD be equal to the actual `service.name` resource attribute
	// of the remote service if any.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'AuthTokenCache'
	PeerServiceKey = attribute.Key("peer.service")
)

Operations that access some remote service.

View Source
const (
	// RPCConnectRPCErrorCodeKey is the attribute Key conforming to the
	// "rpc.connect_rpc.error_code" semantic conventions. It represents the
	// [error codes](https://connect.build/docs/protocol/#error-codes) of the
	// Connect request. Error codes are always string values.
	//
	// Type: Enum
	// RequirementLevel: ConditionallyRequired (If response is not successful
	// and if error code available.)
	// Stability: stable
	RPCConnectRPCErrorCodeKey = attribute.Key("rpc.connect_rpc.error_code")
)

Tech-specific attributes for Connect RPC.

View Source
const (
	// RPCGRPCStatusCodeKey is the attribute Key conforming to the
	// "rpc.grpc.status_code" semantic conventions. It represents the [numeric
	// status
	// code](https://github.com/grpc/grpc/blob/v1.33.2/doc/statuscodes.md) of
	// the gRPC request.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	RPCGRPCStatusCodeKey = attribute.Key("rpc.grpc.status_code")
)

Tech-specific attributes for gRPC.

View Source
const SchemaURL = "https://opentelemetry.io/schemas/1.21.0"

SchemaURL is the schema URL that matches the version of the semantic conventions that this package defines. Semconv packages starting from v1.4.0 must declare non-empty schema URL in the form https://opentelemetry.io/schemas/<version>

View Source
const (
	// TelemetryAutoVersionKey is the attribute Key conforming to the
	// "telemetry.auto.version" semantic conventions. It represents the version
	// string of the auto instrumentation agent, if used.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '1.2.3'
	TelemetryAutoVersionKey = attribute.Key("telemetry.auto.version")
)

The telemetry SDK used to capture data recorded by the instrumentation libraries.

View Source
const (
	// UserAgentOriginalKey is the attribute Key conforming to the
	// "user_agent.original" semantic conventions. It represents the value of
	// the [HTTP
	// User-Agent](https://www.rfc-editor.org/rfc/rfc9110.html#field.user-agent)
	// header sent by the client.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'CERN-LineMode/2.15 libwww/2.17b3'
	UserAgentOriginalKey = attribute.Key("user_agent.original")
)

Describes user-agent attributes.

Variables ¶
View Source
var (
	// ip_tcp
	NetTransportTCP = NetTransportKey.String("ip_tcp")
	// ip_udp
	NetTransportUDP = NetTransportKey.String("ip_udp")
	// Named or anonymous pipe
	NetTransportPipe = NetTransportKey.String("pipe")
	// In-process communication
	NetTransportInProc = NetTransportKey.String("inproc")
	// Something else (non IP-based)
	NetTransportOther = NetTransportKey.String("other")
)
View Source
var (
	// IPv4 address
	NetSockFamilyInet = NetSockFamilyKey.String("inet")
	// IPv6 address
	NetSockFamilyInet6 = NetSockFamilyKey.String("inet6")
	// Unix domain socket path
	NetSockFamilyUnix = NetSockFamilyKey.String("unix")
)
View Source
var (
	// CONNECT method
	HTTPRequestMethodConnect = HTTPRequestMethodKey.String("CONNECT")
	// DELETE method
	HTTPRequestMethodDelete = HTTPRequestMethodKey.String("DELETE")
	// GET method
	HTTPRequestMethodGet = HTTPRequestMethodKey.String("GET")
	// HEAD method
	HTTPRequestMethodHead = HTTPRequestMethodKey.String("HEAD")
	// OPTIONS method
	HTTPRequestMethodOptions = HTTPRequestMethodKey.String("OPTIONS")
	// PATCH method
	HTTPRequestMethodPatch = HTTPRequestMethodKey.String("PATCH")
	// POST method
	HTTPRequestMethodPost = HTTPRequestMethodKey.String("POST")
	// PUT method
	HTTPRequestMethodPut = HTTPRequestMethodKey.String("PUT")
	// TRACE method
	HTTPRequestMethodTrace = HTTPRequestMethodKey.String("TRACE")
	// Any HTTP method that the instrumentation has no prior knowledge of
	HTTPRequestMethodOther = HTTPRequestMethodKey.String("_OTHER")
)
View Source
var (
	// Events from browser apps
	EventDomainBrowser = EventDomainKey.String("browser")
	// Events from mobile apps
	EventDomainDevice = EventDomainKey.String("device")
	// Events from Kubernetes
	EventDomainK8S = EventDomainKey.String("k8s")
)
View Source
var (
	// Logs from stdout stream
	LogIostreamStdout = LogIostreamKey.String("stdout")
	// Events from stderr stream
	LogIostreamStderr = LogIostreamKey.String("stderr")
)
View Source
var (
	// Heap memory
	TypeHeap = TypeKey.String("heap")
	// Non-heap memory
	TypeNonHeap = TypeKey.String("non_heap")
)
View Source
var (
	// TCP
	NetworkTransportTCP = NetworkTransportKey.String("tcp")
	// UDP
	NetworkTransportUDP = NetworkTransportKey.String("udp")
	// Named or anonymous pipe. See note below
	NetworkTransportPipe = NetworkTransportKey.String("pipe")
	// Unix domain socket
	NetworkTransportUnix = NetworkTransportKey.String("unix")
)
View Source
var (
	// IPv4
	NetworkTypeIpv4 = NetworkTypeKey.String("ipv4")
	// IPv6
	NetworkTypeIpv6 = NetworkTypeKey.String("ipv6")
)
View Source
var (
	// wifi
	NetworkConnectionTypeWifi = NetworkConnectionTypeKey.String("wifi")
	// wired
	NetworkConnectionTypeWired = NetworkConnectionTypeKey.String("wired")
	// cell
	NetworkConnectionTypeCell = NetworkConnectionTypeKey.String("cell")
	// unavailable
	NetworkConnectionTypeUnavailable = NetworkConnectionTypeKey.String("unavailable")
	// unknown
	NetworkConnectionTypeUnknown = NetworkConnectionTypeKey.String("unknown")
)
View Source
var (
	// GPRS
	NetworkConnectionSubtypeGprs = NetworkConnectionSubtypeKey.String("gprs")
	// EDGE
	NetworkConnectionSubtypeEdge = NetworkConnectionSubtypeKey.String("edge")
	// UMTS
	NetworkConnectionSubtypeUmts = NetworkConnectionSubtypeKey.String("umts")
	// CDMA
	NetworkConnectionSubtypeCdma = NetworkConnectionSubtypeKey.String("cdma")
	// EVDO Rel. 0
	NetworkConnectionSubtypeEvdo0 = NetworkConnectionSubtypeKey.String("evdo_0")
	// EVDO Rev. A
	NetworkConnectionSubtypeEvdoA = NetworkConnectionSubtypeKey.String("evdo_a")
	// CDMA2000 1XRTT
	NetworkConnectionSubtypeCdma20001xrtt = NetworkConnectionSubtypeKey.String("cdma2000_1xrtt")
	// HSDPA
	NetworkConnectionSubtypeHsdpa = NetworkConnectionSubtypeKey.String("hsdpa")
	// HSUPA
	NetworkConnectionSubtypeHsupa = NetworkConnectionSubtypeKey.String("hsupa")
	// HSPA
	NetworkConnectionSubtypeHspa = NetworkConnectionSubtypeKey.String("hspa")
	// IDEN
	NetworkConnectionSubtypeIden = NetworkConnectionSubtypeKey.String("iden")
	// EVDO Rev. B
	NetworkConnectionSubtypeEvdoB = NetworkConnectionSubtypeKey.String("evdo_b")
	// LTE
	NetworkConnectionSubtypeLte = NetworkConnectionSubtypeKey.String("lte")
	// EHRPD
	NetworkConnectionSubtypeEhrpd = NetworkConnectionSubtypeKey.String("ehrpd")
	// HSPAP
	NetworkConnectionSubtypeHspap = NetworkConnectionSubtypeKey.String("hspap")
	// GSM
	NetworkConnectionSubtypeGsm = NetworkConnectionSubtypeKey.String("gsm")
	// TD-SCDMA
	NetworkConnectionSubtypeTdScdma = NetworkConnectionSubtypeKey.String("td_scdma")
	// IWLAN
	NetworkConnectionSubtypeIwlan = NetworkConnectionSubtypeKey.String("iwlan")
	// 5G NR (New Radio)
	NetworkConnectionSubtypeNr = NetworkConnectionSubtypeKey.String("nr")
	// 5G NRNSA (New Radio Non-Standalone)
	NetworkConnectionSubtypeNrnsa = NetworkConnectionSubtypeKey.String("nrnsa")
	// LTE CA
	NetworkConnectionSubtypeLteCa = NetworkConnectionSubtypeKey.String("lte_ca")
)
View Source
var (
	// Normal message
	MessagingRocketmqMessageTypeNormal = MessagingRocketmqMessageTypeKey.String("normal")
	// FIFO message
	MessagingRocketmqMessageTypeFifo = MessagingRocketmqMessageTypeKey.String("fifo")
	// Delay message
	MessagingRocketmqMessageTypeDelay = MessagingRocketmqMessageTypeKey.String("delay")
	// Transaction message
	MessagingRocketmqMessageTypeTransaction = MessagingRocketmqMessageTypeKey.String("transaction")
)
View Source
var (
	// Clustering consumption model
	MessagingRocketmqConsumptionModelClustering = MessagingRocketmqConsumptionModelKey.String("clustering")
	// Broadcasting consumption model
	MessagingRocketmqConsumptionModelBroadcasting = MessagingRocketmqConsumptionModelKey.String("broadcasting")
)
View Source
var (
	// sent
	MessageTypeSent = MessageTypeKey.String("SENT")
	// received
	MessageTypeReceived = MessageTypeKey.String("RECEIVED")
)
View Source
var (
	// Alibaba Cloud
	CloudProviderAlibabaCloud = CloudProviderKey.String("alibaba_cloud")
	// Amazon Web Services
	CloudProviderAWS = CloudProviderKey.String("aws")
	// Microsoft Azure
	CloudProviderAzure = CloudProviderKey.String("azure")
	// Google Cloud Platform
	CloudProviderGCP = CloudProviderKey.String("gcp")
	// Heroku Platform as a Service
	CloudProviderHeroku = CloudProviderKey.String("heroku")
	// IBM Cloud
	CloudProviderIbmCloud = CloudProviderKey.String("ibm_cloud")
	// Tencent Cloud
	CloudProviderTencentCloud = CloudProviderKey.String("tencent_cloud")
)
View Source
var (
	// Alibaba Cloud Elastic Compute Service
	CloudPlatformAlibabaCloudECS = CloudPlatformKey.String("alibaba_cloud_ecs")
	// Alibaba Cloud Function Compute
	CloudPlatformAlibabaCloudFc = CloudPlatformKey.String("alibaba_cloud_fc")
	// Red Hat OpenShift on Alibaba Cloud
	CloudPlatformAlibabaCloudOpenshift = CloudPlatformKey.String("alibaba_cloud_openshift")
	// AWS Elastic Compute Cloud
	CloudPlatformAWSEC2 = CloudPlatformKey.String("aws_ec2")
	// AWS Elastic Container Service
	CloudPlatformAWSECS = CloudPlatformKey.String("aws_ecs")
	// AWS Elastic Kubernetes Service
	CloudPlatformAWSEKS = CloudPlatformKey.String("aws_eks")
	// AWS Lambda
	CloudPlatformAWSLambda = CloudPlatformKey.String("aws_lambda")
	// AWS Elastic Beanstalk
	CloudPlatformAWSElasticBeanstalk = CloudPlatformKey.String("aws_elastic_beanstalk")
	// AWS App Runner
	CloudPlatformAWSAppRunner = CloudPlatformKey.String("aws_app_runner")
	// Red Hat OpenShift on AWS (ROSA)
	CloudPlatformAWSOpenshift = CloudPlatformKey.String("aws_openshift")
	// Azure Virtual Machines
	CloudPlatformAzureVM = CloudPlatformKey.String("azure_vm")
	// Azure Container Instances
	CloudPlatformAzureContainerInstances = CloudPlatformKey.String("azure_container_instances")
	// Azure Kubernetes Service
	CloudPlatformAzureAKS = CloudPlatformKey.String("azure_aks")
	// Azure Functions
	CloudPlatformAzureFunctions = CloudPlatformKey.String("azure_functions")
	// Azure App Service
	CloudPlatformAzureAppService = CloudPlatformKey.String("azure_app_service")
	// Azure Red Hat OpenShift
	CloudPlatformAzureOpenshift = CloudPlatformKey.String("azure_openshift")
	// Google Bare Metal Solution (BMS)
	CloudPlatformGCPBareMetalSolution = CloudPlatformKey.String("gcp_bare_metal_solution")
	// Google Cloud Compute Engine (GCE)
	CloudPlatformGCPComputeEngine = CloudPlatformKey.String("gcp_compute_engine")
	// Google Cloud Run
	CloudPlatformGCPCloudRun = CloudPlatformKey.String("gcp_cloud_run")
	// Google Cloud Kubernetes Engine (GKE)
	CloudPlatformGCPKubernetesEngine = CloudPlatformKey.String("gcp_kubernetes_engine")
	// Google Cloud Functions (GCF)
	CloudPlatformGCPCloudFunctions = CloudPlatformKey.String("gcp_cloud_functions")
	// Google Cloud App Engine (GAE)
	CloudPlatformGCPAppEngine = CloudPlatformKey.String("gcp_app_engine")
	// Red Hat OpenShift on Google Cloud
	CloudPlatformGCPOpenshift = CloudPlatformKey.String("gcp_openshift")
	// Red Hat OpenShift on IBM Cloud
	CloudPlatformIbmCloudOpenshift = CloudPlatformKey.String("ibm_cloud_openshift")
	// Tencent Cloud Cloud Virtual Machine (CVM)
	CloudPlatformTencentCloudCvm = CloudPlatformKey.String("tencent_cloud_cvm")
	// Tencent Cloud Elastic Kubernetes Service (EKS)
	CloudPlatformTencentCloudEKS = CloudPlatformKey.String("tencent_cloud_eks")
	// Tencent Cloud Serverless Cloud Function (SCF)
	CloudPlatformTencentCloudScf = CloudPlatformKey.String("tencent_cloud_scf")
)
View Source
var (
	// ec2
	AWSECSLaunchtypeEC2 = AWSECSLaunchtypeKey.String("ec2")
	// fargate
	AWSECSLaunchtypeFargate = AWSECSLaunchtypeKey.String("fargate")
)
View Source
var (
	// AMD64
	HostArchAMD64 = HostArchKey.String("amd64")
	// ARM32
	HostArchARM32 = HostArchKey.String("arm32")
	// ARM64
	HostArchARM64 = HostArchKey.String("arm64")
	// Itanium
	HostArchIA64 = HostArchKey.String("ia64")
	// 32-bit PowerPC
	HostArchPPC32 = HostArchKey.String("ppc32")
	// 64-bit PowerPC
	HostArchPPC64 = HostArchKey.String("ppc64")
	// IBM z/Architecture
	HostArchS390x = HostArchKey.String("s390x")
	// 32-bit x86
	HostArchX86 = HostArchKey.String("x86")
)
View Source
var (
	// Microsoft Windows
	OSTypeWindows = OSTypeKey.String("windows")
	// Linux
	OSTypeLinux = OSTypeKey.String("linux")
	// Apple Darwin
	OSTypeDarwin = OSTypeKey.String("darwin")
	// FreeBSD
	OSTypeFreeBSD = OSTypeKey.String("freebsd")
	// NetBSD
	OSTypeNetBSD = OSTypeKey.String("netbsd")
	// OpenBSD
	OSTypeOpenBSD = OSTypeKey.String("openbsd")
	// DragonFly BSD
	OSTypeDragonflyBSD = OSTypeKey.String("dragonflybsd")
	// HP-UX (Hewlett Packard Unix)
	OSTypeHPUX = OSTypeKey.String("hpux")
	// AIX (Advanced Interactive eXecutive)
	OSTypeAIX = OSTypeKey.String("aix")
	// SunOS, Oracle Solaris
	OSTypeSolaris = OSTypeKey.String("solaris")
	// IBM z/OS
	OSTypeZOS = OSTypeKey.String("z_os")
)
View Source
var (
	// cpp
	TelemetrySDKLanguageCPP = TelemetrySDKLanguageKey.String("cpp")
	// dotnet
	TelemetrySDKLanguageDotnet = TelemetrySDKLanguageKey.String("dotnet")
	// erlang
	TelemetrySDKLanguageErlang = TelemetrySDKLanguageKey.String("erlang")
	// go
	TelemetrySDKLanguageGo = TelemetrySDKLanguageKey.String("go")
	// java
	TelemetrySDKLanguageJava = TelemetrySDKLanguageKey.String("java")
	// nodejs
	TelemetrySDKLanguageNodejs = TelemetrySDKLanguageKey.String("nodejs")
	// php
	TelemetrySDKLanguagePHP = TelemetrySDKLanguageKey.String("php")
	// python
	TelemetrySDKLanguagePython = TelemetrySDKLanguageKey.String("python")
	// ruby
	TelemetrySDKLanguageRuby = TelemetrySDKLanguageKey.String("ruby")
	// rust
	TelemetrySDKLanguageRust = TelemetrySDKLanguageKey.String("rust")
	// swift
	TelemetrySDKLanguageSwift = TelemetrySDKLanguageKey.String("swift")
	// webjs
	TelemetrySDKLanguageWebjs = TelemetrySDKLanguageKey.String("webjs")
)
View Source
var (
	// The parent Span depends on the child Span in some capacity
	OpentracingRefTypeChildOf = OpentracingRefTypeKey.String("child_of")
	// The parent Span does not depend in any way on the result of the child Span
	OpentracingRefTypeFollowsFrom = OpentracingRefTypeKey.String("follows_from")
)
View Source
var (
	// Some other SQL database. Fallback only. See notes
	DBSystemOtherSQL = DBSystemKey.String("other_sql")
	// Microsoft SQL Server
	DBSystemMSSQL = DBSystemKey.String("mssql")
	// Microsoft SQL Server Compact
	DBSystemMssqlcompact = DBSystemKey.String("mssqlcompact")
	// MySQL
	DBSystemMySQL = DBSystemKey.String("mysql")
	// Oracle Database
	DBSystemOracle = DBSystemKey.String("oracle")
	// IBM DB2
	DBSystemDB2 = DBSystemKey.String("db2")
	// PostgreSQL
	DBSystemPostgreSQL = DBSystemKey.String("postgresql")
	// Amazon Redshift
	DBSystemRedshift = DBSystemKey.String("redshift")
	// Apache Hive
	DBSystemHive = DBSystemKey.String("hive")
	// Cloudscape
	DBSystemCloudscape = DBSystemKey.String("cloudscape")
	// HyperSQL DataBase
	DBSystemHSQLDB = DBSystemKey.String("hsqldb")
	// Progress Database
	DBSystemProgress = DBSystemKey.String("progress")
	// SAP MaxDB
	DBSystemMaxDB = DBSystemKey.String("maxdb")
	// SAP HANA
	DBSystemHanaDB = DBSystemKey.String("hanadb")
	// Ingres
	DBSystemIngres = DBSystemKey.String("ingres")
	// FirstSQL
	DBSystemFirstSQL = DBSystemKey.String("firstsql")
	// EnterpriseDB
	DBSystemEDB = DBSystemKey.String("edb")
	// InterSystems Caché
	DBSystemCache = DBSystemKey.String("cache")
	// Adabas (Adaptable Database System)
	DBSystemAdabas = DBSystemKey.String("adabas")
	// Firebird
	DBSystemFirebird = DBSystemKey.String("firebird")
	// Apache Derby
	DBSystemDerby = DBSystemKey.String("derby")
	// FileMaker
	DBSystemFilemaker = DBSystemKey.String("filemaker")
	// Informix
	DBSystemInformix = DBSystemKey.String("informix")
	// InstantDB
	DBSystemInstantDB = DBSystemKey.String("instantdb")
	// InterBase
	DBSystemInterbase = DBSystemKey.String("interbase")
	// MariaDB
	DBSystemMariaDB = DBSystemKey.String("mariadb")
	// Netezza
	DBSystemNetezza = DBSystemKey.String("netezza")
	// Pervasive PSQL
	DBSystemPervasive = DBSystemKey.String("pervasive")
	// PointBase
	DBSystemPointbase = DBSystemKey.String("pointbase")
	// SQLite
	DBSystemSqlite = DBSystemKey.String("sqlite")
	// Sybase
	DBSystemSybase = DBSystemKey.String("sybase")
	// Teradata
	DBSystemTeradata = DBSystemKey.String("teradata")
	// Vertica
	DBSystemVertica = DBSystemKey.String("vertica")
	// H2
	DBSystemH2 = DBSystemKey.String("h2")
	// ColdFusion IMQ
	DBSystemColdfusion = DBSystemKey.String("coldfusion")
	// Apache Cassandra
	DBSystemCassandra = DBSystemKey.String("cassandra")
	// Apache HBase
	DBSystemHBase = DBSystemKey.String("hbase")
	// MongoDB
	DBSystemMongoDB = DBSystemKey.String("mongodb")
	// Redis
	DBSystemRedis = DBSystemKey.String("redis")
	// Couchbase
	DBSystemCouchbase = DBSystemKey.String("couchbase")
	// CouchDB
	DBSystemCouchDB = DBSystemKey.String("couchdb")
	// Microsoft Azure Cosmos DB
	DBSystemCosmosDB = DBSystemKey.String("cosmosdb")
	// Amazon DynamoDB
	DBSystemDynamoDB = DBSystemKey.String("dynamodb")
	// Neo4j
	DBSystemNeo4j = DBSystemKey.String("neo4j")
	// Apache Geode
	DBSystemGeode = DBSystemKey.String("geode")
	// Elasticsearch
	DBSystemElasticsearch = DBSystemKey.String("elasticsearch")
	// Memcached
	DBSystemMemcached = DBSystemKey.String("memcached")
	// CockroachDB
	DBSystemCockroachdb = DBSystemKey.String("cockroachdb")
	// OpenSearch
	DBSystemOpensearch = DBSystemKey.String("opensearch")
	// ClickHouse
	DBSystemClickhouse = DBSystemKey.String("clickhouse")
	// Cloud Spanner
	DBSystemSpanner = DBSystemKey.String("spanner")
	// Trino
	DBSystemTrino = DBSystemKey.String("trino")
)
View Source
var (
	// all
	DBCassandraConsistencyLevelAll = DBCassandraConsistencyLevelKey.String("all")
	// each_quorum
	DBCassandraConsistencyLevelEachQuorum = DBCassandraConsistencyLevelKey.String("each_quorum")
	// quorum
	DBCassandraConsistencyLevelQuorum = DBCassandraConsistencyLevelKey.String("quorum")
	// local_quorum
	DBCassandraConsistencyLevelLocalQuorum = DBCassandraConsistencyLevelKey.String("local_quorum")
	// one
	DBCassandraConsistencyLevelOne = DBCassandraConsistencyLevelKey.String("one")
	// two
	DBCassandraConsistencyLevelTwo = DBCassandraConsistencyLevelKey.String("two")
	// three
	DBCassandraConsistencyLevelThree = DBCassandraConsistencyLevelKey.String("three")
	// local_one
	DBCassandraConsistencyLevelLocalOne = DBCassandraConsistencyLevelKey.String("local_one")
	// any
	DBCassandraConsistencyLevelAny = DBCassandraConsistencyLevelKey.String("any")
	// serial
	DBCassandraConsistencyLevelSerial = DBCassandraConsistencyLevelKey.String("serial")
	// local_serial
	DBCassandraConsistencyLevelLocalSerial = DBCassandraConsistencyLevelKey.String("local_serial")
)
View Source
var (
	// invalid
	DBCosmosDBOperationTypeInvalid = DBCosmosDBOperationTypeKey.String("Invalid")
	// create
	DBCosmosDBOperationTypeCreate = DBCosmosDBOperationTypeKey.String("Create")
	// patch
	DBCosmosDBOperationTypePatch = DBCosmosDBOperationTypeKey.String("Patch")
	// read
	DBCosmosDBOperationTypeRead = DBCosmosDBOperationTypeKey.String("Read")
	// read_feed
	DBCosmosDBOperationTypeReadFeed = DBCosmosDBOperationTypeKey.String("ReadFeed")
	// delete
	DBCosmosDBOperationTypeDelete = DBCosmosDBOperationTypeKey.String("Delete")
	// replace
	DBCosmosDBOperationTypeReplace = DBCosmosDBOperationTypeKey.String("Replace")
	// execute
	DBCosmosDBOperationTypeExecute = DBCosmosDBOperationTypeKey.String("Execute")
	// query
	DBCosmosDBOperationTypeQuery = DBCosmosDBOperationTypeKey.String("Query")
	// head
	DBCosmosDBOperationTypeHead = DBCosmosDBOperationTypeKey.String("Head")
	// head_feed
	DBCosmosDBOperationTypeHeadFeed = DBCosmosDBOperationTypeKey.String("HeadFeed")
	// upsert
	DBCosmosDBOperationTypeUpsert = DBCosmosDBOperationTypeKey.String("Upsert")
	// batch
	DBCosmosDBOperationTypeBatch = DBCosmosDBOperationTypeKey.String("Batch")
	// query_plan
	DBCosmosDBOperationTypeQueryPlan = DBCosmosDBOperationTypeKey.String("QueryPlan")
	// execute_javascript
	DBCosmosDBOperationTypeExecuteJavascript = DBCosmosDBOperationTypeKey.String("ExecuteJavaScript")
)
View Source
var (
	// Gateway (HTTP) connections mode
	DBCosmosDBConnectionModeGateway = DBCosmosDBConnectionModeKey.String("gateway")
	// Direct connection
	DBCosmosDBConnectionModeDirect = DBCosmosDBConnectionModeKey.String("direct")
)
View Source
var (
	// The operation has been validated by an Application developer or Operator to have completed successfully
	OTelStatusCodeOk = OTelStatusCodeKey.String("OK")
	// The operation contains an error
	OTelStatusCodeError = OTelStatusCodeKey.String("ERROR")
)
View Source
var (
	// A response to some data source operation such as a database or filesystem read/write
	FaaSTriggerDatasource = FaaSTriggerKey.String("datasource")
	// To provide an answer to an inbound HTTP request
	FaaSTriggerHTTP = FaaSTriggerKey.String("http")
	// A function is set to be executed when messages are sent to a messaging system
	FaaSTriggerPubsub = FaaSTriggerKey.String("pubsub")
	// A function is scheduled to be executed regularly
	FaaSTriggerTimer = FaaSTriggerKey.String("timer")
	// If none of the others apply
	FaaSTriggerOther = FaaSTriggerKey.String("other")
)
View Source
var (
	// When a new object is created
	FaaSDocumentOperationInsert = FaaSDocumentOperationKey.String("insert")
	// When an object is modified
	FaaSDocumentOperationEdit = FaaSDocumentOperationKey.String("edit")
	// When an object is deleted
	FaaSDocumentOperationDelete = FaaSDocumentOperationKey.String("delete")
)
View Source
var (
	// Alibaba Cloud
	FaaSInvokedProviderAlibabaCloud = FaaSInvokedProviderKey.String("alibaba_cloud")
	// Amazon Web Services
	FaaSInvokedProviderAWS = FaaSInvokedProviderKey.String("aws")
	// Microsoft Azure
	FaaSInvokedProviderAzure = FaaSInvokedProviderKey.String("azure")
	// Google Cloud Platform
	FaaSInvokedProviderGCP = FaaSInvokedProviderKey.String("gcp")
	// Tencent Cloud
	FaaSInvokedProviderTencentCloud = FaaSInvokedProviderKey.String("tencent_cloud")
)
View Source
var (
	// GraphQL query
	GraphqlOperationTypeQuery = GraphqlOperationTypeKey.String("query")
	// GraphQL mutation
	GraphqlOperationTypeMutation = GraphqlOperationTypeKey.String("mutation")
	// GraphQL subscription
	GraphqlOperationTypeSubscription = GraphqlOperationTypeKey.String("subscription")
)
View Source
var (
	// publish
	MessagingOperationPublish = MessagingOperationKey.String("publish")
	// receive
	MessagingOperationReceive = MessagingOperationKey.String("receive")
	// process
	MessagingOperationProcess = MessagingOperationKey.String("process")
)
View Source
var (
	// gRPC
	RPCSystemGRPC = RPCSystemKey.String("grpc")
	// Java RMI
	RPCSystemJavaRmi = RPCSystemKey.String("java_rmi")
	// .NET WCF
	RPCSystemDotnetWcf = RPCSystemKey.String("dotnet_wcf")
	// Apache Dubbo
	RPCSystemApacheDubbo = RPCSystemKey.String("apache_dubbo")
	// Connect RPC
	RPCSystemConnectRPC = RPCSystemKey.String("connect_rpc")
)
View Source
var (
	// OK
	RPCGRPCStatusCodeOk = RPCGRPCStatusCodeKey.Int(0)
	// CANCELLED
	RPCGRPCStatusCodeCancelled = RPCGRPCStatusCodeKey.Int(1)
	// UNKNOWN
	RPCGRPCStatusCodeUnknown = RPCGRPCStatusCodeKey.Int(2)
	// INVALID_ARGUMENT
	RPCGRPCStatusCodeInvalidArgument = RPCGRPCStatusCodeKey.Int(3)
	// DEADLINE_EXCEEDED
	RPCGRPCStatusCodeDeadlineExceeded = RPCGRPCStatusCodeKey.Int(4)
	// NOT_FOUND
	RPCGRPCStatusCodeNotFound = RPCGRPCStatusCodeKey.Int(5)
	// ALREADY_EXISTS
	RPCGRPCStatusCodeAlreadyExists = RPCGRPCStatusCodeKey.Int(6)
	// PERMISSION_DENIED
	RPCGRPCStatusCodePermissionDenied = RPCGRPCStatusCodeKey.Int(7)
	// RESOURCE_EXHAUSTED
	RPCGRPCStatusCodeResourceExhausted = RPCGRPCStatusCodeKey.Int(8)
	// FAILED_PRECONDITION
	RPCGRPCStatusCodeFailedPrecondition = RPCGRPCStatusCodeKey.Int(9)
	// ABORTED
	RPCGRPCStatusCodeAborted = RPCGRPCStatusCodeKey.Int(10)
	// OUT_OF_RANGE
	RPCGRPCStatusCodeOutOfRange = RPCGRPCStatusCodeKey.Int(11)
	// UNIMPLEMENTED
	RPCGRPCStatusCodeUnimplemented = RPCGRPCStatusCodeKey.Int(12)
	// INTERNAL
	RPCGRPCStatusCodeInternal = RPCGRPCStatusCodeKey.Int(13)
	// UNAVAILABLE
	RPCGRPCStatusCodeUnavailable = RPCGRPCStatusCodeKey.Int(14)
	// DATA_LOSS
	RPCGRPCStatusCodeDataLoss = RPCGRPCStatusCodeKey.Int(15)
	// UNAUTHENTICATED
	RPCGRPCStatusCodeUnauthenticated = RPCGRPCStatusCodeKey.Int(16)
)
View Source
var (
	// cancelled
	RPCConnectRPCErrorCodeCancelled = RPCConnectRPCErrorCodeKey.String("cancelled")
	// unknown
	RPCConnectRPCErrorCodeUnknown = RPCConnectRPCErrorCodeKey.String("unknown")
	// invalid_argument
	RPCConnectRPCErrorCodeInvalidArgument = RPCConnectRPCErrorCodeKey.String("invalid_argument")
	// deadline_exceeded
	RPCConnectRPCErrorCodeDeadlineExceeded = RPCConnectRPCErrorCodeKey.String("deadline_exceeded")
	// not_found
	RPCConnectRPCErrorCodeNotFound = RPCConnectRPCErrorCodeKey.String("not_found")
	// already_exists
	RPCConnectRPCErrorCodeAlreadyExists = RPCConnectRPCErrorCodeKey.String("already_exists")
	// permission_denied
	RPCConnectRPCErrorCodePermissionDenied = RPCConnectRPCErrorCodeKey.String("permission_denied")
	// resource_exhausted
	RPCConnectRPCErrorCodeResourceExhausted = RPCConnectRPCErrorCodeKey.String("resource_exhausted")
	// failed_precondition
	RPCConnectRPCErrorCodeFailedPrecondition = RPCConnectRPCErrorCodeKey.String("failed_precondition")
	// aborted
	RPCConnectRPCErrorCodeAborted = RPCConnectRPCErrorCodeKey.String("aborted")
	// out_of_range
	RPCConnectRPCErrorCodeOutOfRange = RPCConnectRPCErrorCodeKey.String("out_of_range")
	// unimplemented
	RPCConnectRPCErrorCodeUnimplemented = RPCConnectRPCErrorCodeKey.String("unimplemented")
	// internal
	RPCConnectRPCErrorCodeInternal = RPCConnectRPCErrorCodeKey.String("internal")
	// unavailable
	RPCConnectRPCErrorCodeUnavailable = RPCConnectRPCErrorCodeKey.String("unavailable")
	// data_loss
	RPCConnectRPCErrorCodeDataLoss = RPCConnectRPCErrorCodeKey.String("data_loss")
	// unauthenticated
	RPCConnectRPCErrorCodeUnauthenticated = RPCConnectRPCErrorCodeKey.String("unauthenticated")
)
Functions ¶
func AWSDynamoDBAttributeDefinitions ¶
func AWSDynamoDBAttributeDefinitions(val ...string) attribute.KeyValue

AWSDynamoDBAttributeDefinitions returns an attribute KeyValue conforming to the "aws.dynamodb.attribute_definitions" semantic conventions. It represents the JSON-serialized value of each item in the `AttributeDefinitions` request field.

func AWSDynamoDBAttributesToGet ¶
func AWSDynamoDBAttributesToGet(val ...string) attribute.KeyValue

AWSDynamoDBAttributesToGet returns an attribute KeyValue conforming to the "aws.dynamodb.attributes_to_get" semantic conventions. It represents the value of the `AttributesToGet` request parameter.

func AWSDynamoDBConsistentRead ¶
func AWSDynamoDBConsistentRead(val bool) attribute.KeyValue

AWSDynamoDBConsistentRead returns an attribute KeyValue conforming to the "aws.dynamodb.consistent_read" semantic conventions. It represents the value of the `ConsistentRead` request parameter.

func AWSDynamoDBConsumedCapacity ¶
func AWSDynamoDBConsumedCapacity(val ...string) attribute.KeyValue

AWSDynamoDBConsumedCapacity returns an attribute KeyValue conforming to the "aws.dynamodb.consumed_capacity" semantic conventions. It represents the JSON-serialized value of each item in the `ConsumedCapacity` response field.

func AWSDynamoDBCount ¶
func AWSDynamoDBCount(val int) attribute.KeyValue

AWSDynamoDBCount returns an attribute KeyValue conforming to the "aws.dynamodb.count" semantic conventions. It represents the value of the `Count` response parameter.

func AWSDynamoDBExclusiveStartTable ¶
func AWSDynamoDBExclusiveStartTable(val string) attribute.KeyValue

AWSDynamoDBExclusiveStartTable returns an attribute KeyValue conforming to the "aws.dynamodb.exclusive_start_table" semantic conventions. It represents the value of the `ExclusiveStartTableName` request parameter.

func AWSDynamoDBGlobalSecondaryIndexUpdates ¶
func AWSDynamoDBGlobalSecondaryIndexUpdates(val ...string) attribute.KeyValue

AWSDynamoDBGlobalSecondaryIndexUpdates returns an attribute KeyValue conforming to the "aws.dynamodb.global_secondary_index_updates" semantic conventions. It represents the JSON-serialized value of each item in the the `GlobalSecondaryIndexUpdates` request field.

func AWSDynamoDBGlobalSecondaryIndexes ¶
func AWSDynamoDBGlobalSecondaryIndexes(val ...string) attribute.KeyValue

AWSDynamoDBGlobalSecondaryIndexes returns an attribute KeyValue conforming to the "aws.dynamodb.global_secondary_indexes" semantic conventions. It represents the JSON-serialized value of each item of the `GlobalSecondaryIndexes` request field

func AWSDynamoDBIndexName ¶
func AWSDynamoDBIndexName(val string) attribute.KeyValue

AWSDynamoDBIndexName returns an attribute KeyValue conforming to the "aws.dynamodb.index_name" semantic conventions. It represents the value of the `IndexName` request parameter.

func AWSDynamoDBItemCollectionMetrics ¶
func AWSDynamoDBItemCollectionMetrics(val string) attribute.KeyValue

AWSDynamoDBItemCollectionMetrics returns an attribute KeyValue conforming to the "aws.dynamodb.item_collection_metrics" semantic conventions. It represents the JSON-serialized value of the `ItemCollectionMetrics` response field.

func AWSDynamoDBLimit ¶
func AWSDynamoDBLimit(val int) attribute.KeyValue

AWSDynamoDBLimit returns an attribute KeyValue conforming to the "aws.dynamodb.limit" semantic conventions. It represents the value of the `Limit` request parameter.

func AWSDynamoDBLocalSecondaryIndexes ¶
func AWSDynamoDBLocalSecondaryIndexes(val ...string) attribute.KeyValue

AWSDynamoDBLocalSecondaryIndexes returns an attribute KeyValue conforming to the "aws.dynamodb.local_secondary_indexes" semantic conventions. It represents the JSON-serialized value of each item of the `LocalSecondaryIndexes` request field.

func AWSDynamoDBProjection ¶
func AWSDynamoDBProjection(val string) attribute.KeyValue

AWSDynamoDBProjection returns an attribute KeyValue conforming to the "aws.dynamodb.projection" semantic conventions. It represents the value of the `ProjectionExpression` request parameter.

func AWSDynamoDBProvisionedReadCapacity ¶
func AWSDynamoDBProvisionedReadCapacity(val float64) attribute.KeyValue

AWSDynamoDBProvisionedReadCapacity returns an attribute KeyValue conforming to the "aws.dynamodb.provisioned_read_capacity" semantic conventions. It represents the value of the `ProvisionedThroughput.ReadCapacityUnits` request parameter.

func AWSDynamoDBProvisionedWriteCapacity ¶
func AWSDynamoDBProvisionedWriteCapacity(val float64) attribute.KeyValue

AWSDynamoDBProvisionedWriteCapacity returns an attribute KeyValue conforming to the "aws.dynamodb.provisioned_write_capacity" semantic conventions. It represents the value of the `ProvisionedThroughput.WriteCapacityUnits` request parameter.

func AWSDynamoDBScanForward ¶
func AWSDynamoDBScanForward(val bool) attribute.KeyValue

AWSDynamoDBScanForward returns an attribute KeyValue conforming to the "aws.dynamodb.scan_forward" semantic conventions. It represents the value of the `ScanIndexForward` request parameter.

func AWSDynamoDBScannedCount ¶
func AWSDynamoDBScannedCount(val int) attribute.KeyValue

AWSDynamoDBScannedCount returns an attribute KeyValue conforming to the "aws.dynamodb.scanned_count" semantic conventions. It represents the value of the `ScannedCount` response parameter.

func AWSDynamoDBSegment ¶
func AWSDynamoDBSegment(val int) attribute.KeyValue

AWSDynamoDBSegment returns an attribute KeyValue conforming to the "aws.dynamodb.segment" semantic conventions. It represents the value of the `Segment` request parameter.

func AWSDynamoDBSelect ¶
func AWSDynamoDBSelect(val string) attribute.KeyValue

AWSDynamoDBSelect returns an attribute KeyValue conforming to the "aws.dynamodb.select" semantic conventions. It represents the value of the `Select` request parameter.

func AWSDynamoDBTableCount ¶
func AWSDynamoDBTableCount(val int) attribute.KeyValue

AWSDynamoDBTableCount returns an attribute KeyValue conforming to the "aws.dynamodb.table_count" semantic conventions. It represents the the number of items in the `TableNames` response parameter.

func AWSDynamoDBTableNames ¶
func AWSDynamoDBTableNames(val ...string) attribute.KeyValue

AWSDynamoDBTableNames returns an attribute KeyValue conforming to the "aws.dynamodb.table_names" semantic conventions. It represents the keys in the `RequestItems` object field.

func AWSDynamoDBTotalSegments ¶
func AWSDynamoDBTotalSegments(val int) attribute.KeyValue

AWSDynamoDBTotalSegments returns an attribute KeyValue conforming to the "aws.dynamodb.total_segments" semantic conventions. It represents the value of the `TotalSegments` request parameter.

func AWSECSClusterARN ¶
func AWSECSClusterARN(val string) attribute.KeyValue

AWSECSClusterARN returns an attribute KeyValue conforming to the "aws.ecs.cluster.arn" semantic conventions. It represents the ARN of an [ECS cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html).

func AWSECSContainerARN ¶
func AWSECSContainerARN(val string) attribute.KeyValue

AWSECSContainerARN returns an attribute KeyValue conforming to the "aws.ecs.container.arn" semantic conventions. It represents the Amazon Resource Name (ARN) of an [ECS container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html).

func AWSECSTaskARN ¶
func AWSECSTaskARN(val string) attribute.KeyValue

AWSECSTaskARN returns an attribute KeyValue conforming to the "aws.ecs.task.arn" semantic conventions. It represents the ARN of an [ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html).

func AWSECSTaskFamily ¶
func AWSECSTaskFamily(val string) attribute.KeyValue

AWSECSTaskFamily returns an attribute KeyValue conforming to the "aws.ecs.task.family" semantic conventions. It represents the task definition family this task definition is a member of.

func AWSECSTaskRevision ¶
func AWSECSTaskRevision(val string) attribute.KeyValue

AWSECSTaskRevision returns an attribute KeyValue conforming to the "aws.ecs.task.revision" semantic conventions. It represents the revision for this task definition.

func AWSEKSClusterARN ¶
func AWSEKSClusterARN(val string) attribute.KeyValue

AWSEKSClusterARN returns an attribute KeyValue conforming to the "aws.eks.cluster.arn" semantic conventions. It represents the ARN of an EKS cluster.

func AWSLambdaInvokedARN ¶
func AWSLambdaInvokedARN(val string) attribute.KeyValue

AWSLambdaInvokedARN returns an attribute KeyValue conforming to the "aws.lambda.invoked_arn" semantic conventions. It represents the full invoked ARN as provided on the `Context` passed to the function (`Lambda-Runtime-Invoked-Function-ARN` header on the `/runtime/invocation/next` applicable).

func AWSLogGroupARNs ¶
func AWSLogGroupARNs(val ...string) attribute.KeyValue

AWSLogGroupARNs returns an attribute KeyValue conforming to the "aws.log.group.arns" semantic conventions. It represents the Amazon Resource Name(s) (ARN) of the AWS log group(s).

func AWSLogGroupNames ¶
func AWSLogGroupNames(val ...string) attribute.KeyValue

AWSLogGroupNames returns an attribute KeyValue conforming to the "aws.log.group.names" semantic conventions. It represents the name(s) of the AWS log group(s) an application is writing to.

func AWSLogStreamARNs ¶
func AWSLogStreamARNs(val ...string) attribute.KeyValue

AWSLogStreamARNs returns an attribute KeyValue conforming to the "aws.log.stream.arns" semantic conventions. It represents the ARN(s) of the AWS log stream(s).

func AWSLogStreamNames ¶
func AWSLogStreamNames(val ...string) attribute.KeyValue

AWSLogStreamNames returns an attribute KeyValue conforming to the "aws.log.stream.names" semantic conventions. It represents the name(s) of the AWS log stream(s) an application is writing to.

func AWSRequestID ¶
func AWSRequestID(val string) attribute.KeyValue

AWSRequestID returns an attribute KeyValue conforming to the "aws.request_id" semantic conventions. It represents the AWS request ID as returned in the response headers `x-amz-request-id` or `x-amz-requestid`.

func AWSS3Bucket ¶
func AWSS3Bucket(val string) attribute.KeyValue

AWSS3Bucket returns an attribute KeyValue conforming to the "aws.s3.bucket" semantic conventions. It represents the S3 bucket name the request refers to. Corresponds to the `--bucket` parameter of the [S3 API](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html) operations.

func AWSS3CopySource ¶
func AWSS3CopySource(val string) attribute.KeyValue

AWSS3CopySource returns an attribute KeyValue conforming to the "aws.s3.copy_source" semantic conventions. It represents the source object (in the form `bucket`/`key`) for the copy operation.

func AWSS3Delete ¶
func AWSS3Delete(val string) attribute.KeyValue

AWSS3Delete returns an attribute KeyValue conforming to the "aws.s3.delete" semantic conventions. It represents the delete request container that specifies the objects to be deleted.

func AWSS3Key ¶
func AWSS3Key(val string) attribute.KeyValue

AWSS3Key returns an attribute KeyValue conforming to the "aws.s3.key" semantic conventions. It represents the S3 object key the request refers to. Corresponds to the `--key` parameter of the [S3 API](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html) operations.

func AWSS3PartNumber ¶
func AWSS3PartNumber(val int) attribute.KeyValue

AWSS3PartNumber returns an attribute KeyValue conforming to the "aws.s3.part_number" semantic conventions. It represents the part number of the part being uploaded in a multipart-upload operation. This is a positive integer between 1 and 10,000.

func AWSS3UploadID ¶
func AWSS3UploadID(val string) attribute.KeyValue

AWSS3UploadID returns an attribute KeyValue conforming to the "aws.s3.upload_id" semantic conventions. It represents the upload ID that identifies the multipart upload.

func BrowserBrands ¶
func BrowserBrands(val ...string) attribute.KeyValue

BrowserBrands returns an attribute KeyValue conforming to the "browser.brands" semantic conventions. It represents the array of brand name and version separated by a space

func BrowserLanguage ¶
func BrowserLanguage(val string) attribute.KeyValue

BrowserLanguage returns an attribute KeyValue conforming to the "browser.language" semantic conventions. It represents the preferred language of the user using the browser

func BrowserMobile ¶
func BrowserMobile(val bool) attribute.KeyValue

BrowserMobile returns an attribute KeyValue conforming to the "browser.mobile" semantic conventions. It represents a boolean that is true if the browser is running on a mobile device

func BrowserPlatform ¶
func BrowserPlatform(val string) attribute.KeyValue

BrowserPlatform returns an attribute KeyValue conforming to the "browser.platform" semantic conventions. It represents the platform on which the browser is running

func ClientAddress ¶
func ClientAddress(val string) attribute.KeyValue

ClientAddress returns an attribute KeyValue conforming to the "client.address" semantic conventions. It represents the client address - unix domain socket name, IPv4 or IPv6 address.

func ClientPort ¶
func ClientPort(val int) attribute.KeyValue

ClientPort returns an attribute KeyValue conforming to the "client.port" semantic conventions. It represents the client port number

func ClientSocketAddress ¶
func ClientSocketAddress(val string) attribute.KeyValue

ClientSocketAddress returns an attribute KeyValue conforming to the "client.socket.address" semantic conventions. It represents the immediate client peer address - unix domain socket name, IPv4 or IPv6 address.

func ClientSocketPort ¶
func ClientSocketPort(val int) attribute.KeyValue

ClientSocketPort returns an attribute KeyValue conforming to the "client.socket.port" semantic conventions. It represents the immediate client peer port number

func CloudAccountID ¶
func CloudAccountID(val string) attribute.KeyValue

CloudAccountID returns an attribute KeyValue conforming to the "cloud.account.id" semantic conventions. It represents the cloud account ID the resource is assigned to.

func CloudAvailabilityZone ¶
func CloudAvailabilityZone(val string) attribute.KeyValue

CloudAvailabilityZone returns an attribute KeyValue conforming to the "cloud.availability_zone" semantic conventions. It represents the cloud regions often have multiple, isolated locations known as zones to increase availability. Availability zone represents the zone where the resource is running.

func CloudRegion ¶
func CloudRegion(val string) attribute.KeyValue

CloudRegion returns an attribute KeyValue conforming to the "cloud.region" semantic conventions. It represents the geographical region the resource is running.

func CloudResourceID ¶
func CloudResourceID(val string) attribute.KeyValue

CloudResourceID returns an attribute KeyValue conforming to the "cloud.resource_id" semantic conventions. It represents the cloud provider-specific native identifier of the monitored cloud resource (e.g. an [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) on AWS, a [fully qualified resource ID](https://learn.microsoft.com/en-us/rest/api/resources/resources/get-by-id) on Azure, a [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) on GCP)

func CloudeventsEventID ¶
func CloudeventsEventID(val string) attribute.KeyValue

CloudeventsEventID returns an attribute KeyValue conforming to the "cloudevents.event_id" semantic conventions. It represents the [event_id](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#id) uniquely identifies the event.

func CloudeventsEventSource ¶
func CloudeventsEventSource(val string) attribute.KeyValue

CloudeventsEventSource returns an attribute KeyValue conforming to the "cloudevents.event_source" semantic conventions. It represents the [source](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#source-1) identifies the context in which an event happened.

func CloudeventsEventSpecVersion ¶
func CloudeventsEventSpecVersion(val string) attribute.KeyValue

CloudeventsEventSpecVersion returns an attribute KeyValue conforming to the "cloudevents.event_spec_version" semantic conventions. It represents the [version of the CloudEvents specification](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#specversion) which the event uses.

func CloudeventsEventSubject ¶
func CloudeventsEventSubject(val string) attribute.KeyValue

CloudeventsEventSubject returns an attribute KeyValue conforming to the "cloudevents.event_subject" semantic conventions. It represents the [subject](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#subject) of the event in the context of the event producer (identified by source).

func CloudeventsEventType ¶
func CloudeventsEventType(val string) attribute.KeyValue

CloudeventsEventType returns an attribute KeyValue conforming to the "cloudevents.event_type" semantic conventions. It represents the [event_type](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#type) contains a value describing the type of event related to the originating occurrence.

func CodeColumn ¶
func CodeColumn(val int) attribute.KeyValue

CodeColumn returns an attribute KeyValue conforming to the "code.column" semantic conventions. It represents the column number in `code.filepath` best representing the operation. It SHOULD point within the code unit named in `code.function`.

func CodeFilepath ¶
func CodeFilepath(val string) attribute.KeyValue

CodeFilepath returns an attribute KeyValue conforming to the "code.filepath" semantic conventions. It represents the source code file name that identifies the code unit as uniquely as possible (preferably an absolute file path).

func CodeFunction ¶
func CodeFunction(val string) attribute.KeyValue

CodeFunction returns an attribute KeyValue conforming to the "code.function" semantic conventions. It represents the method or function name, or equivalent (usually rightmost part of the code unit's name).

func CodeLineNumber ¶
func CodeLineNumber(val int) attribute.KeyValue

CodeLineNumber returns an attribute KeyValue conforming to the "code.lineno" semantic conventions. It represents the line number in `code.filepath` best representing the operation. It SHOULD point within the code unit named in `code.function`.

func CodeNamespace ¶
func CodeNamespace(val string) attribute.KeyValue

CodeNamespace returns an attribute KeyValue conforming to the "code.namespace" semantic conventions. It represents the "namespace" within which `code.function` is defined. Usually the qualified class or module name, such that `code.namespace` + some separator + `code.function` form a unique identifier for the code unit.

func ContainerCommand ¶
func ContainerCommand(val string) attribute.KeyValue

ContainerCommand returns an attribute KeyValue conforming to the "container.command" semantic conventions. It represents the command used to run the container (i.e. the command name).

func ContainerCommandArgs ¶
func ContainerCommandArgs(val ...string) attribute.KeyValue

ContainerCommandArgs returns an attribute KeyValue conforming to the "container.command_args" semantic conventions. It represents the all the command arguments (including the command/executable itself) run by the container. [2]

func ContainerCommandLine ¶
func ContainerCommandLine(val string) attribute.KeyValue

ContainerCommandLine returns an attribute KeyValue conforming to the "container.command_line" semantic conventions. It represents the full command run by the container as a single string representing the full command. [2]

func ContainerID ¶
func ContainerID(val string) attribute.KeyValue

ContainerID returns an attribute KeyValue conforming to the "container.id" semantic conventions. It represents the container ID. Usually a UUID, as for example used to [identify Docker containers](https://docs.docker.com/engine/reference/run/#container-identification). The UUID might be abbreviated.

func ContainerImageID ¶
func ContainerImageID(val string) attribute.KeyValue

ContainerImageID returns an attribute KeyValue conforming to the "container.image.id" semantic conventions. It represents the runtime specific image identifier. Usually a hash algorithm followed by a UUID.

func ContainerImageName ¶
func ContainerImageName(val string) attribute.KeyValue

ContainerImageName returns an attribute KeyValue conforming to the "container.image.name" semantic conventions. It represents the name of the image the container was built on.

func ContainerImageTag ¶
func ContainerImageTag(val string) attribute.KeyValue

ContainerImageTag returns an attribute KeyValue conforming to the "container.image.tag" semantic conventions. It represents the container image tag.

func ContainerName ¶
func ContainerName(val string) attribute.KeyValue

ContainerName returns an attribute KeyValue conforming to the "container.name" semantic conventions. It represents the container name used by container runtime.

func ContainerRuntime ¶
func ContainerRuntime(val string) attribute.KeyValue

ContainerRuntime returns an attribute KeyValue conforming to the "container.runtime" semantic conventions. It represents the container runtime managing this container.

func DBCassandraCoordinatorDC ¶
func DBCassandraCoordinatorDC(val string) attribute.KeyValue

DBCassandraCoordinatorDC returns an attribute KeyValue conforming to the "db.cassandra.coordinator.dc" semantic conventions. It represents the data center of the coordinating node for a query.

func DBCassandraCoordinatorID ¶
func DBCassandraCoordinatorID(val string) attribute.KeyValue

DBCassandraCoordinatorID returns an attribute KeyValue conforming to the "db.cassandra.coordinator.id" semantic conventions. It represents the ID of the coordinating node for a query.

func DBCassandraIdempotence ¶
func DBCassandraIdempotence(val bool) attribute.KeyValue

DBCassandraIdempotence returns an attribute KeyValue conforming to the "db.cassandra.idempotence" semantic conventions. It represents the whether or not the query is idempotent.

func DBCassandraPageSize ¶
func DBCassandraPageSize(val int) attribute.KeyValue

DBCassandraPageSize returns an attribute KeyValue conforming to the "db.cassandra.page_size" semantic conventions. It represents the fetch size used for paging, i.e. how many rows will be returned at once.

func DBCassandraSpeculativeExecutionCount ¶
func DBCassandraSpeculativeExecutionCount(val int) attribute.KeyValue

DBCassandraSpeculativeExecutionCount returns an attribute KeyValue conforming to the "db.cassandra.speculative_execution_count" semantic conventions. It represents the number of times a query was speculatively executed. Not set or `0` if the query was not executed speculatively.

func DBCassandraTable ¶
func DBCassandraTable(val string) attribute.KeyValue

DBCassandraTable returns an attribute KeyValue conforming to the "db.cassandra.table" semantic conventions. It represents the name of the primary table that the operation is acting upon, including the keyspace name (if applicable).

func DBConnectionString ¶
func DBConnectionString(val string) attribute.KeyValue

DBConnectionString returns an attribute KeyValue conforming to the "db.connection_string" semantic conventions. It represents the connection string used to connect to the database. It is recommended to remove embedded credentials.

func DBCosmosDBClientID ¶
func DBCosmosDBClientID(val string) attribute.KeyValue

DBCosmosDBClientID returns an attribute KeyValue conforming to the "db.cosmosdb.client_id" semantic conventions. It represents the unique Cosmos client instance id.

func DBCosmosDBContainer ¶
func DBCosmosDBContainer(val string) attribute.KeyValue

DBCosmosDBContainer returns an attribute KeyValue conforming to the "db.cosmosdb.container" semantic conventions. It represents the cosmos DB container name.

func DBCosmosDBRequestCharge ¶
func DBCosmosDBRequestCharge(val float64) attribute.KeyValue

DBCosmosDBRequestCharge returns an attribute KeyValue conforming to the "db.cosmosdb.request_charge" semantic conventions. It represents the rU consumed for that operation

func DBCosmosDBRequestContentLength ¶
func DBCosmosDBRequestContentLength(val int) attribute.KeyValue

DBCosmosDBRequestContentLength returns an attribute KeyValue conforming to the "db.cosmosdb.request_content_length" semantic conventions. It represents the request payload size in bytes

func DBCosmosDBStatusCode ¶
func DBCosmosDBStatusCode(val int) attribute.KeyValue

DBCosmosDBStatusCode returns an attribute KeyValue conforming to the "db.cosmosdb.status_code" semantic conventions. It represents the cosmos DB status code.

func DBCosmosDBSubStatusCode ¶
func DBCosmosDBSubStatusCode(val int) attribute.KeyValue

DBCosmosDBSubStatusCode returns an attribute KeyValue conforming to the "db.cosmosdb.sub_status_code" semantic conventions. It represents the cosmos DB sub status code.

func DBJDBCDriverClassname ¶
func DBJDBCDriverClassname(val string) attribute.KeyValue

DBJDBCDriverClassname returns an attribute KeyValue conforming to the "db.jdbc.driver_classname" semantic conventions. It represents the fully-qualified class name of the [Java Database Connectivity (JDBC)](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/) driver used to connect.

func DBMSSQLInstanceName ¶
func DBMSSQLInstanceName(val string) attribute.KeyValue

DBMSSQLInstanceName returns an attribute KeyValue conforming to the "db.mssql.instance_name" semantic conventions. It represents the Microsoft SQL Server [instance name](https://docs.microsoft.com/en-us/sql/connect/jdbc/building-the-connection-url?view=sql-server-ver15) connecting to. This name is used to determine the port of a named instance.

func DBMongoDBCollection ¶
func DBMongoDBCollection(val string) attribute.KeyValue

DBMongoDBCollection returns an attribute KeyValue conforming to the "db.mongodb.collection" semantic conventions. It represents the collection being accessed within the database stated in `db.name`.

func DBName ¶
func DBName(val string) attribute.KeyValue

DBName returns an attribute KeyValue conforming to the "db.name" semantic conventions. It represents the this attribute is used to report the name of the database being accessed. For commands that switch the database, this should be set to the target database (even if the command fails).

func DBOperation ¶
func DBOperation(val string) attribute.KeyValue

DBOperation returns an attribute KeyValue conforming to the "db.operation" semantic conventions. It represents the name of the operation being executed, e.g. the [MongoDB command name](https://docs.mongodb.com/manual/reference/command/#database-operations) such as `findAndModify`, or the SQL keyword.

func DBRedisDBIndex ¶
func DBRedisDBIndex(val int) attribute.KeyValue

DBRedisDBIndex returns an attribute KeyValue conforming to the "db.redis.database_index" semantic conventions. It represents the index of the database being accessed as used in the [`SELECT` command](https://redis.io/commands/select), provided as an integer. To be used instead of the generic `db.name` attribute.

func DBSQLTable ¶
func DBSQLTable(val string) attribute.KeyValue

DBSQLTable returns an attribute KeyValue conforming to the "db.sql.table" semantic conventions. It represents the name of the primary table that the operation is acting upon, including the database name (if applicable).

func DBStatement ¶
func DBStatement(val string) attribute.KeyValue

DBStatement returns an attribute KeyValue conforming to the "db.statement" semantic conventions. It represents the database statement being executed.

func DBUser ¶
func DBUser(val string) attribute.KeyValue

DBUser returns an attribute KeyValue conforming to the "db.user" semantic conventions. It represents the username for accessing the database.

func DeploymentEnvironment ¶
func DeploymentEnvironment(val string) attribute.KeyValue

DeploymentEnvironment returns an attribute KeyValue conforming to the "deployment.environment" semantic conventions. It represents the name of the [deployment environment](https://en.wikipedia.org/wiki/Deployment_environment) (aka deployment tier).

func DestinationAddress ¶
func DestinationAddress(val string) attribute.KeyValue

DestinationAddress returns an attribute KeyValue conforming to the "destination.address" semantic conventions. It represents the peer address, for example IP address or UNIX socket name.

func DestinationDomain ¶
func DestinationDomain(val string) attribute.KeyValue

DestinationDomain returns an attribute KeyValue conforming to the "destination.domain" semantic conventions. It represents the domain name of the destination system.

func DestinationPort ¶
func DestinationPort(val int) attribute.KeyValue

DestinationPort returns an attribute KeyValue conforming to the "destination.port" semantic conventions. It represents the peer port number

func DeviceID ¶
func DeviceID(val string) attribute.KeyValue

DeviceID returns an attribute KeyValue conforming to the "device.id" semantic conventions. It represents a unique identifier representing the device

func DeviceManufacturer ¶
func DeviceManufacturer(val string) attribute.KeyValue

DeviceManufacturer returns an attribute KeyValue conforming to the "device.manufacturer" semantic conventions. It represents the name of the device manufacturer

func DeviceModelIdentifier ¶
func DeviceModelIdentifier(val string) attribute.KeyValue

DeviceModelIdentifier returns an attribute KeyValue conforming to the "device.model.identifier" semantic conventions. It represents the model identifier for the device

func DeviceModelName ¶
func DeviceModelName(val string) attribute.KeyValue

DeviceModelName returns an attribute KeyValue conforming to the "device.model.name" semantic conventions. It represents the marketing name for the device model

func EnduserID ¶
func EnduserID(val string) attribute.KeyValue

EnduserID returns an attribute KeyValue conforming to the "enduser.id" semantic conventions. It represents the username or client_id extracted from the access token or [Authorization](https://tools.ietf.org/html/rfc7235#section-4.2) header in the inbound request from outside the system.

func EnduserRole ¶
func EnduserRole(val string) attribute.KeyValue

EnduserRole returns an attribute KeyValue conforming to the "enduser.role" semantic conventions. It represents the actual/assumed role the client is making the request under extracted from token or application security context.

func EnduserScope ¶
func EnduserScope(val string) attribute.KeyValue

EnduserScope returns an attribute KeyValue conforming to the "enduser.scope" semantic conventions. It represents the scopes or granted authorities the client currently possesses extracted from token or application security context. The value would come from the scope associated with an [OAuth 2.0 Access Token](https://tools.ietf.org/html/rfc6749#section-3.3) or an attribute value in a [SAML 2.0 Assertion](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html).

func EventName ¶
func EventName(val string) attribute.KeyValue

EventName returns an attribute KeyValue conforming to the "event.name" semantic conventions. It represents the name identifies the event.

func ExceptionEscaped ¶
func ExceptionEscaped(val bool) attribute.KeyValue

ExceptionEscaped returns an attribute KeyValue conforming to the "exception.escaped" semantic conventions. It represents the sHOULD be set to true if the exception event is recorded at a point where it is known that the exception is escaping the scope of the span.

func ExceptionMessage ¶
func ExceptionMessage(val string) attribute.KeyValue

ExceptionMessage returns an attribute KeyValue conforming to the "exception.message" semantic conventions. It represents the exception message.

func ExceptionStacktrace ¶
func ExceptionStacktrace(val string) attribute.KeyValue

ExceptionStacktrace returns an attribute KeyValue conforming to the "exception.stacktrace" semantic conventions. It represents a stacktrace as a string in the natural representation for the language runtime. The representation is to be determined and documented by each language SIG.

func ExceptionType ¶
func ExceptionType(val string) attribute.KeyValue

ExceptionType returns an attribute KeyValue conforming to the "exception.type" semantic conventions. It represents the type of the exception (its fully-qualified class name, if applicable). The dynamic type of the exception should be preferred over the static type in languages that support it.

func FaaSColdstart ¶
func FaaSColdstart(val bool) attribute.KeyValue

FaaSColdstart returns an attribute KeyValue conforming to the "faas.coldstart" semantic conventions. It represents a boolean that is true if the serverless function is executed for the first time (aka cold-start).

func FaaSCron ¶
func FaaSCron(val string) attribute.KeyValue

FaaSCron returns an attribute KeyValue conforming to the "faas.cron" semantic conventions. It represents a string containing the schedule period as [Cron Expression](https://docs.oracle.com/cd/E12058_01/doc/doc.1014/e12030/cron_expressions.htm).

func FaaSDocumentCollection ¶
func FaaSDocumentCollection(val string) attribute.KeyValue

FaaSDocumentCollection returns an attribute KeyValue conforming to the "faas.document.collection" semantic conventions. It represents the name of the source on which the triggering operation was performed. For example, in Cloud Storage or S3 corresponds to the bucket name, and in Cosmos DB to the database name.

func FaaSDocumentName ¶
func FaaSDocumentName(val string) attribute.KeyValue

FaaSDocumentName returns an attribute KeyValue conforming to the "faas.document.name" semantic conventions. It represents the document name/table subjected to the operation. For example, in Cloud Storage or S3 is the name of the file, and in Cosmos DB the table name.

func FaaSDocumentTime ¶
func FaaSDocumentTime(val string) attribute.KeyValue

FaaSDocumentTime returns an attribute KeyValue conforming to the "faas.document.time" semantic conventions. It represents a string containing the time when the data was accessed in the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format expressed in [UTC](https://www.w3.org/TR/NOTE-datetime).

func FaaSInstance ¶
func FaaSInstance(val string) attribute.KeyValue

FaaSInstance returns an attribute KeyValue conforming to the "faas.instance" semantic conventions. It represents the execution environment ID as a string, that will be potentially reused for other invocations to the same function/function version.

func FaaSInvocationID ¶
func FaaSInvocationID(val string) attribute.KeyValue

FaaSInvocationID returns an attribute KeyValue conforming to the "faas.invocation_id" semantic conventions. It represents the invocation ID of the current function invocation.

func FaaSInvokedName ¶
func FaaSInvokedName(val string) attribute.KeyValue

FaaSInvokedName returns an attribute KeyValue conforming to the "faas.invoked_name" semantic conventions. It represents the name of the invoked function.

func FaaSInvokedRegion ¶
func FaaSInvokedRegion(val string) attribute.KeyValue

FaaSInvokedRegion returns an attribute KeyValue conforming to the "faas.invoked_region" semantic conventions. It represents the cloud region of the invoked function.

func FaaSMaxMemory ¶
func FaaSMaxMemory(val int) attribute.KeyValue

FaaSMaxMemory returns an attribute KeyValue conforming to the "faas.max_memory" semantic conventions. It represents the amount of memory available to the serverless function converted to Bytes.

func FaaSName ¶
func FaaSName(val string) attribute.KeyValue

FaaSName returns an attribute KeyValue conforming to the "faas.name" semantic conventions. It represents the name of the single function that this runtime instance executes.

func FaaSTime ¶
func FaaSTime(val string) attribute.KeyValue

FaaSTime returns an attribute KeyValue conforming to the "faas.time" semantic conventions. It represents a string containing the function invocation time in the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format expressed in [UTC](https://www.w3.org/TR/NOTE-datetime).

func FaaSVersion ¶
func FaaSVersion(val string) attribute.KeyValue

FaaSVersion returns an attribute KeyValue conforming to the "faas.version" semantic conventions. It represents the immutable version of the function being executed.

func FeatureFlagKey ¶
func FeatureFlagKey(val string) attribute.KeyValue

FeatureFlagKey returns an attribute KeyValue conforming to the "feature_flag.key" semantic conventions. It represents the unique identifier of the feature flag.

func FeatureFlagProviderName ¶
func FeatureFlagProviderName(val string) attribute.KeyValue

FeatureFlagProviderName returns an attribute KeyValue conforming to the "feature_flag.provider_name" semantic conventions. It represents the name of the service provider that performs the flag evaluation.

func FeatureFlagVariant ¶
func FeatureFlagVariant(val string) attribute.KeyValue

FeatureFlagVariant returns an attribute KeyValue conforming to the "feature_flag.variant" semantic conventions. It represents the sHOULD be a semantic identifier for a value. If one is unavailable, a stringified version of the value can be used.

func GCPCloudRunJobExecution ¶
func GCPCloudRunJobExecution(val string) attribute.KeyValue

GCPCloudRunJobExecution returns an attribute KeyValue conforming to the "gcp.cloud_run.job.execution" semantic conventions. It represents the name of the Cloud Run [execution](https://cloud.google.com/run/docs/managing/job-executions) being run for the Job, as set by the [`CLOUD_RUN_EXECUTION`](https://cloud.google.com/run/docs/container-contract#jobs-env-vars) environment variable.

func GCPCloudRunJobTaskIndex ¶
func GCPCloudRunJobTaskIndex(val int) attribute.KeyValue

GCPCloudRunJobTaskIndex returns an attribute KeyValue conforming to the "gcp.cloud_run.job.task_index" semantic conventions. It represents the index for a task within an execution as provided by the [`CLOUD_RUN_TASK_INDEX`](https://cloud.google.com/run/docs/container-contract#jobs-env-vars) environment variable.

func GCPGceInstanceHostname ¶
func GCPGceInstanceHostname(val string) attribute.KeyValue

GCPGceInstanceHostname returns an attribute KeyValue conforming to the "gcp.gce.instance.hostname" semantic conventions. It represents the hostname of a GCE instance. This is the full value of the default or [custom hostname](https://cloud.google.com/compute/docs/instances/custom-hostname-vm).

func GCPGceInstanceName ¶
func GCPGceInstanceName(val string) attribute.KeyValue

GCPGceInstanceName returns an attribute KeyValue conforming to the "gcp.gce.instance.name" semantic conventions. It represents the instance name of a GCE instance. This is the value provided by `host.name`, the visible name of the instance in the Cloud Console UI, and the prefix for the default hostname of the instance as defined by the [default internal DNS name](https://cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names).

func GraphqlDocument ¶
func GraphqlDocument(val string) attribute.KeyValue

GraphqlDocument returns an attribute KeyValue conforming to the "graphql.document" semantic conventions. It represents the GraphQL document being executed.

func GraphqlOperationName ¶
func GraphqlOperationName(val string) attribute.KeyValue

GraphqlOperationName returns an attribute KeyValue conforming to the "graphql.operation.name" semantic conventions. It represents the name of the operation being executed.

func HTTPMethod ¶
func HTTPMethod(val string) attribute.KeyValue

HTTPMethod returns an attribute KeyValue conforming to the "http.method" semantic conventions. It represents the deprecated, use `http.request.method` instead.

func HTTPRequestBodySize ¶
func HTTPRequestBodySize(val int) attribute.KeyValue

HTTPRequestBodySize returns an attribute KeyValue conforming to the "http.request.body.size" semantic conventions. It represents the size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

func HTTPRequestContentLength ¶
func HTTPRequestContentLength(val int) attribute.KeyValue

HTTPRequestContentLength returns an attribute KeyValue conforming to the "http.request_content_length" semantic conventions. It represents the deprecated, use `http.request.body.size` instead.

func HTTPRequestMethodOriginal ¶
func HTTPRequestMethodOriginal(val string) attribute.KeyValue

HTTPRequestMethodOriginal returns an attribute KeyValue conforming to the "http.request.method_original" semantic conventions. It represents the original HTTP method sent by the client in the request line.

func HTTPResendCount ¶
func HTTPResendCount(val int) attribute.KeyValue

HTTPResendCount returns an attribute KeyValue conforming to the "http.resend_count" semantic conventions. It represents the ordinal number of request resending attempt (for any reason, including redirects).

func HTTPResponseBodySize ¶
func HTTPResponseBodySize(val int) attribute.KeyValue

HTTPResponseBodySize returns an attribute KeyValue conforming to the "http.response.body.size" semantic conventions. It represents the size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

func HTTPResponseContentLength ¶
func HTTPResponseContentLength(val int) attribute.KeyValue

HTTPResponseContentLength returns an attribute KeyValue conforming to the "http.response_content_length" semantic conventions. It represents the deprecated, use `http.response.body.size` instead.

func HTTPResponseStatusCode ¶
func HTTPResponseStatusCode(val int) attribute.KeyValue

HTTPResponseStatusCode returns an attribute KeyValue conforming to the "http.response.status_code" semantic conventions. It represents the [HTTP response status code](https://tools.ietf.org/html/rfc7231#section-6).

func HTTPRoute ¶
func HTTPRoute(val string) attribute.KeyValue

HTTPRoute returns an attribute KeyValue conforming to the "http.route" semantic conventions. It represents the matched route (path template in the format used by the respective server framework). See note below

func HTTPScheme ¶
func HTTPScheme(val string) attribute.KeyValue

HTTPScheme returns an attribute KeyValue conforming to the "http.scheme" semantic conventions. It represents the deprecated, use `url.scheme` instead.

func HTTPStatusCode ¶
func HTTPStatusCode(val int) attribute.KeyValue

HTTPStatusCode returns an attribute KeyValue conforming to the "http.status_code" semantic conventions. It represents the deprecated, use `http.response.status_code` instead.

func HTTPTarget ¶
func HTTPTarget(val string) attribute.KeyValue

HTTPTarget returns an attribute KeyValue conforming to the "http.target" semantic conventions. It represents the deprecated, use `url.path` and `url.query` instead.

func HTTPURL ¶
func HTTPURL(val string) attribute.KeyValue

HTTPURL returns an attribute KeyValue conforming to the "http.url" semantic conventions. It represents the deprecated, use `url.full` instead.

func HerokuAppID ¶
func HerokuAppID(val string) attribute.KeyValue

HerokuAppID returns an attribute KeyValue conforming to the "heroku.app.id" semantic conventions. It represents the unique identifier for the application

func HerokuReleaseCommit ¶
func HerokuReleaseCommit(val string) attribute.KeyValue

HerokuReleaseCommit returns an attribute KeyValue conforming to the "heroku.release.commit" semantic conventions. It represents the commit hash for the current release

func HerokuReleaseCreationTimestamp ¶
func HerokuReleaseCreationTimestamp(val string) attribute.KeyValue

HerokuReleaseCreationTimestamp returns an attribute KeyValue conforming to the "heroku.release.creation_timestamp" semantic conventions. It represents the time and date the release was created

func HostID ¶
func HostID(val string) attribute.KeyValue

HostID returns an attribute KeyValue conforming to the "host.id" semantic conventions. It represents the unique host ID. For Cloud, this must be the instance_id assigned by the cloud provider. For non-containerized systems, this should be the `machine-id`. See the table below for the sources to use to determine the `machine-id` based on operating system.

func HostImageID ¶
func HostImageID(val string) attribute.KeyValue

HostImageID returns an attribute KeyValue conforming to the "host.image.id" semantic conventions. It represents the vM image ID or host OS image ID. For Cloud, this value is from the provider.

func HostImageName ¶
func HostImageName(val string) attribute.KeyValue

HostImageName returns an attribute KeyValue conforming to the "host.image.name" semantic conventions. It represents the name of the VM image or OS install the host was instantiated from.

func HostImageVersion ¶
func HostImageVersion(val string) attribute.KeyValue

HostImageVersion returns an attribute KeyValue conforming to the "host.image.version" semantic conventions. It represents the version string of the VM image or host OS as defined in [Version Attributes](README.md#version-attributes).

func HostName ¶
func HostName(val string) attribute.KeyValue

HostName returns an attribute KeyValue conforming to the "host.name" semantic conventions. It represents the name of the host. On Unix systems, it may contain what the hostname command returns, or the fully qualified hostname, or another name specified by the user.

func HostType ¶
func HostType(val string) attribute.KeyValue

HostType returns an attribute KeyValue conforming to the "host.type" semantic conventions. It represents the type of host. For Cloud, this must be the machine type.

func K8SClusterName ¶
func K8SClusterName(val string) attribute.KeyValue

K8SClusterName returns an attribute KeyValue conforming to the "k8s.cluster.name" semantic conventions. It represents the name of the cluster.

func K8SClusterUID ¶
func K8SClusterUID(val string) attribute.KeyValue

K8SClusterUID returns an attribute KeyValue conforming to the "k8s.cluster.uid" semantic conventions. It represents a pseudo-ID for the cluster, set to the UID of the `kube-system` namespace.

func K8SContainerName ¶
func K8SContainerName(val string) attribute.KeyValue

K8SContainerName returns an attribute KeyValue conforming to the "k8s.container.name" semantic conventions. It represents the name of the Container from Pod specification, must be unique within a Pod. Container runtime usually uses different globally unique name (`container.name`).

func K8SContainerRestartCount ¶
func K8SContainerRestartCount(val int) attribute.KeyValue

K8SContainerRestartCount returns an attribute KeyValue conforming to the "k8s.container.restart_count" semantic conventions. It represents the number of times the container was restarted. This attribute can be used to identify a particular container (running or stopped) within a container spec.

func K8SCronJobName ¶
func K8SCronJobName(val string) attribute.KeyValue

K8SCronJobName returns an attribute KeyValue conforming to the "k8s.cronjob.name" semantic conventions. It represents the name of the CronJob.

func K8SCronJobUID ¶
func K8SCronJobUID(val string) attribute.KeyValue

K8SCronJobUID returns an attribute KeyValue conforming to the "k8s.cronjob.uid" semantic conventions. It represents the UID of the CronJob.

func K8SDaemonSetName ¶
func K8SDaemonSetName(val string) attribute.KeyValue

K8SDaemonSetName returns an attribute KeyValue conforming to the "k8s.daemonset.name" semantic conventions. It represents the name of the DaemonSet.

func K8SDaemonSetUID ¶
func K8SDaemonSetUID(val string) attribute.KeyValue

K8SDaemonSetUID returns an attribute KeyValue conforming to the "k8s.daemonset.uid" semantic conventions. It represents the UID of the DaemonSet.

func K8SDeploymentName ¶
func K8SDeploymentName(val string) attribute.KeyValue

K8SDeploymentName returns an attribute KeyValue conforming to the "k8s.deployment.name" semantic conventions. It represents the name of the Deployment.

func K8SDeploymentUID ¶
func K8SDeploymentUID(val string) attribute.KeyValue

K8SDeploymentUID returns an attribute KeyValue conforming to the "k8s.deployment.uid" semantic conventions. It represents the UID of the Deployment.

func K8SJobName ¶
func K8SJobName(val string) attribute.KeyValue

K8SJobName returns an attribute KeyValue conforming to the "k8s.job.name" semantic conventions. It represents the name of the Job.

func K8SJobUID ¶
func K8SJobUID(val string) attribute.KeyValue

K8SJobUID returns an attribute KeyValue conforming to the "k8s.job.uid" semantic conventions. It represents the UID of the Job.

func K8SNamespaceName ¶
func K8SNamespaceName(val string) attribute.KeyValue

K8SNamespaceName returns an attribute KeyValue conforming to the "k8s.namespace.name" semantic conventions. It represents the name of the namespace that the pod is running in.

func K8SNodeName ¶
func K8SNodeName(val string) attribute.KeyValue

K8SNodeName returns an attribute KeyValue conforming to the "k8s.node.name" semantic conventions. It represents the name of the Node.

func K8SNodeUID ¶
func K8SNodeUID(val string) attribute.KeyValue

K8SNodeUID returns an attribute KeyValue conforming to the "k8s.node.uid" semantic conventions. It represents the UID of the Node.

func K8SPodName ¶
func K8SPodName(val string) attribute.KeyValue

K8SPodName returns an attribute KeyValue conforming to the "k8s.pod.name" semantic conventions. It represents the name of the Pod.

func K8SPodUID ¶
func K8SPodUID(val string) attribute.KeyValue

K8SPodUID returns an attribute KeyValue conforming to the "k8s.pod.uid" semantic conventions. It represents the UID of the Pod.

func K8SReplicaSetName ¶
func K8SReplicaSetName(val string) attribute.KeyValue

K8SReplicaSetName returns an attribute KeyValue conforming to the "k8s.replicaset.name" semantic conventions. It represents the name of the ReplicaSet.

func K8SReplicaSetUID ¶
func K8SReplicaSetUID(val string) attribute.KeyValue

K8SReplicaSetUID returns an attribute KeyValue conforming to the "k8s.replicaset.uid" semantic conventions. It represents the UID of the ReplicaSet.

func K8SStatefulSetName ¶
func K8SStatefulSetName(val string) attribute.KeyValue

K8SStatefulSetName returns an attribute KeyValue conforming to the "k8s.statefulset.name" semantic conventions. It represents the name of the StatefulSet.

func K8SStatefulSetUID ¶
func K8SStatefulSetUID(val string) attribute.KeyValue

K8SStatefulSetUID returns an attribute KeyValue conforming to the "k8s.statefulset.uid" semantic conventions. It represents the UID of the StatefulSet.

func LogFileName ¶
func LogFileName(val string) attribute.KeyValue

LogFileName returns an attribute KeyValue conforming to the "log.file.name" semantic conventions. It represents the basename of the file.

func LogFileNameResolved ¶
func LogFileNameResolved(val string) attribute.KeyValue

LogFileNameResolved returns an attribute KeyValue conforming to the "log.file.name_resolved" semantic conventions. It represents the basename of the file, with symlinks resolved.

func LogFilePath ¶
func LogFilePath(val string) attribute.KeyValue

LogFilePath returns an attribute KeyValue conforming to the "log.file.path" semantic conventions. It represents the full path to the file.

func LogFilePathResolved ¶
func LogFilePathResolved(val string) attribute.KeyValue

LogFilePathResolved returns an attribute KeyValue conforming to the "log.file.path_resolved" semantic conventions. It represents the full path to the file, with symlinks resolved.

func LogRecordUID ¶
func LogRecordUID(val string) attribute.KeyValue

LogRecordUID returns an attribute KeyValue conforming to the "log.record.uid" semantic conventions. It represents a unique identifier for the Log Record.

func MessageCompressedSize ¶
func MessageCompressedSize(val int) attribute.KeyValue

MessageCompressedSize returns an attribute KeyValue conforming to the "message.compressed_size" semantic conventions. It represents the compressed size of the message in bytes.

func MessageID ¶
func MessageID(val int) attribute.KeyValue

MessageID returns an attribute KeyValue conforming to the "message.id" semantic conventions. It represents the mUST be calculated as two different counters starting from `1` one for sent messages and one for received message.

func MessageUncompressedSize ¶
func MessageUncompressedSize(val int) attribute.KeyValue

MessageUncompressedSize returns an attribute KeyValue conforming to the "message.uncompressed_size" semantic conventions. It represents the uncompressed size of the message in bytes.

func MessagingBatchMessageCount ¶
func MessagingBatchMessageCount(val int) attribute.KeyValue

MessagingBatchMessageCount returns an attribute KeyValue conforming to the "messaging.batch.message_count" semantic conventions. It represents the number of messages sent, received, or processed in the scope of the batching operation.

func MessagingClientID ¶
func MessagingClientID(val string) attribute.KeyValue

MessagingClientID returns an attribute KeyValue conforming to the "messaging.client_id" semantic conventions. It represents a unique identifier for the client that consumes or produces a message.

func MessagingDestinationAnonymous ¶
func MessagingDestinationAnonymous(val bool) attribute.KeyValue

MessagingDestinationAnonymous returns an attribute KeyValue conforming to the "messaging.destination.anonymous" semantic conventions. It represents a boolean that is true if the message destination is anonymous (could be unnamed or have auto-generated name).

func MessagingDestinationName ¶
func MessagingDestinationName(val string) attribute.KeyValue

MessagingDestinationName returns an attribute KeyValue conforming to the "messaging.destination.name" semantic conventions. It represents the message destination name

func MessagingDestinationTemplate ¶
func MessagingDestinationTemplate(val string) attribute.KeyValue

MessagingDestinationTemplate returns an attribute KeyValue conforming to the "messaging.destination.template" semantic conventions. It represents the low cardinality representation of the messaging destination name

func MessagingDestinationTemporary ¶
func MessagingDestinationTemporary(val bool) attribute.KeyValue

MessagingDestinationTemporary returns an attribute KeyValue conforming to the "messaging.destination.temporary" semantic conventions. It represents a boolean that is true if the message destination is temporary and might not exist anymore after messages are processed.

func MessagingKafkaConsumerGroup ¶
func MessagingKafkaConsumerGroup(val string) attribute.KeyValue

MessagingKafkaConsumerGroup returns an attribute KeyValue conforming to the "messaging.kafka.consumer.group" semantic conventions. It represents the name of the Kafka Consumer Group that is handling the message. Only applies to consumers, not producers.

func MessagingKafkaDestinationPartition ¶
func MessagingKafkaDestinationPartition(val int) attribute.KeyValue

MessagingKafkaDestinationPartition returns an attribute KeyValue conforming to the "messaging.kafka.destination.partition" semantic conventions. It represents the partition the message is sent to.

func MessagingKafkaMessageKey ¶
func MessagingKafkaMessageKey(val string) attribute.KeyValue

MessagingKafkaMessageKey returns an attribute KeyValue conforming to the "messaging.kafka.message.key" semantic conventions. It represents the message keys in Kafka are used for grouping alike messages to ensure they're processed on the same partition. They differ from `messaging.message.id` in that they're not unique. If the key is `null`, the attribute MUST NOT be set.

func MessagingKafkaMessageOffset ¶
func MessagingKafkaMessageOffset(val int) attribute.KeyValue

MessagingKafkaMessageOffset returns an attribute KeyValue conforming to the "messaging.kafka.message.offset" semantic conventions. It represents the offset of a record in the corresponding Kafka partition.

func MessagingKafkaMessageTombstone ¶
func MessagingKafkaMessageTombstone(val bool) attribute.KeyValue

MessagingKafkaMessageTombstone returns an attribute KeyValue conforming to the "messaging.kafka.message.tombstone" semantic conventions. It represents a boolean that is true if the message is a tombstone.

func MessagingMessageConversationID ¶
func MessagingMessageConversationID(val string) attribute.KeyValue

MessagingMessageConversationID returns an attribute KeyValue conforming to the "messaging.message.conversation_id" semantic conventions. It represents the [conversation ID](#conversations) identifying the conversation to which the message belongs, represented as a string. Sometimes called "Correlation ID".

func MessagingMessageID ¶
func MessagingMessageID(val string) attribute.KeyValue

MessagingMessageID returns an attribute KeyValue conforming to the "messaging.message.id" semantic conventions. It represents a value used by the messaging system as an identifier for the message, represented as a string.

func MessagingMessagePayloadCompressedSizeBytes ¶
func MessagingMessagePayloadCompressedSizeBytes(val int) attribute.KeyValue

MessagingMessagePayloadCompressedSizeBytes returns an attribute KeyValue conforming to the "messaging.message.payload_compressed_size_bytes" semantic conventions. It represents the compressed size of the message payload in bytes.

func MessagingMessagePayloadSizeBytes ¶
func MessagingMessagePayloadSizeBytes(val int) attribute.KeyValue

MessagingMessagePayloadSizeBytes returns an attribute KeyValue conforming to the "messaging.message.payload_size_bytes" semantic conventions. It represents the (uncompressed) size of the message payload in bytes. Also use this attribute if it is unknown whether the compressed or uncompressed payload size is reported.

func MessagingRabbitmqDestinationRoutingKey ¶
func MessagingRabbitmqDestinationRoutingKey(val string) attribute.KeyValue

MessagingRabbitmqDestinationRoutingKey returns an attribute KeyValue conforming to the "messaging.rabbitmq.destination.routing_key" semantic conventions. It represents the rabbitMQ message routing key.

func MessagingRocketmqClientGroup ¶
func MessagingRocketmqClientGroup(val string) attribute.KeyValue

MessagingRocketmqClientGroup returns an attribute KeyValue conforming to the "messaging.rocketmq.client_group" semantic conventions. It represents the name of the RocketMQ producer/consumer group that is handling the message. The client type is identified by the SpanKind.

func MessagingRocketmqMessageDelayTimeLevel ¶
func MessagingRocketmqMessageDelayTimeLevel(val int) attribute.KeyValue

MessagingRocketmqMessageDelayTimeLevel returns an attribute KeyValue conforming to the "messaging.rocketmq.message.delay_time_level" semantic conventions. It represents the delay time level for delay message, which determines the message delay time.

func MessagingRocketmqMessageDeliveryTimestamp ¶
func MessagingRocketmqMessageDeliveryTimestamp(val int) attribute.KeyValue

MessagingRocketmqMessageDeliveryTimestamp returns an attribute KeyValue conforming to the "messaging.rocketmq.message.delivery_timestamp" semantic conventions. It represents the timestamp in milliseconds that the delay message is expected to be delivered to consumer.

func MessagingRocketmqMessageGroup ¶
func MessagingRocketmqMessageGroup(val string) attribute.KeyValue

MessagingRocketmqMessageGroup returns an attribute KeyValue conforming to the "messaging.rocketmq.message.group" semantic conventions. It represents the it is essential for FIFO message. Messages that belong to the same message group are always processed one by one within the same consumer group.

func MessagingRocketmqMessageKeys ¶
func MessagingRocketmqMessageKeys(val ...string) attribute.KeyValue

MessagingRocketmqMessageKeys returns an attribute KeyValue conforming to the "messaging.rocketmq.message.keys" semantic conventions. It represents the key(s) of message, another way to mark message besides message id.

func MessagingRocketmqMessageTag ¶
func MessagingRocketmqMessageTag(val string) attribute.KeyValue

MessagingRocketmqMessageTag returns an attribute KeyValue conforming to the "messaging.rocketmq.message.tag" semantic conventions. It represents the secondary classifier of message besides topic.

func MessagingRocketmqNamespace ¶
func MessagingRocketmqNamespace(val string) attribute.KeyValue

MessagingRocketmqNamespace returns an attribute KeyValue conforming to the "messaging.rocketmq.namespace" semantic conventions. It represents the namespace of RocketMQ resources, resources in different namespaces are individual.

func MessagingSystem ¶
func MessagingSystem(val string) attribute.KeyValue

MessagingSystem returns an attribute KeyValue conforming to the "messaging.system" semantic conventions. It represents a string identifying the messaging system.

func NetHostName ¶
func NetHostName(val string) attribute.KeyValue

NetHostName returns an attribute KeyValue conforming to the "net.host.name" semantic conventions. It represents the deprecated, use `server.address`.

func NetHostPort ¶
func NetHostPort(val int) attribute.KeyValue

NetHostPort returns an attribute KeyValue conforming to the "net.host.port" semantic conventions. It represents the deprecated, use `server.port`.

func NetPeerName ¶
func NetPeerName(val string) attribute.KeyValue

NetPeerName returns an attribute KeyValue conforming to the "net.peer.name" semantic conventions. It represents the deprecated, use `server.address` on client spans and `client.address` on server spans.

func NetPeerPort ¶
func NetPeerPort(val int) attribute.KeyValue

NetPeerPort returns an attribute KeyValue conforming to the "net.peer.port" semantic conventions. It represents the deprecated, use `server.port` on client spans and `client.port` on server spans.

func NetProtocolName ¶
func NetProtocolName(val string) attribute.KeyValue

NetProtocolName returns an attribute KeyValue conforming to the "net.protocol.name" semantic conventions. It represents the deprecated, use `network.protocol.name`.

func NetProtocolVersion ¶
func NetProtocolVersion(val string) attribute.KeyValue

NetProtocolVersion returns an attribute KeyValue conforming to the "net.protocol.version" semantic conventions. It represents the deprecated, use `network.protocol.version`.

func NetSockHostAddr ¶
func NetSockHostAddr(val string) attribute.KeyValue

NetSockHostAddr returns an attribute KeyValue conforming to the "net.sock.host.addr" semantic conventions. It represents the deprecated, use `server.socket.address`.

func NetSockHostPort ¶
func NetSockHostPort(val int) attribute.KeyValue

NetSockHostPort returns an attribute KeyValue conforming to the "net.sock.host.port" semantic conventions. It represents the deprecated, use `server.socket.port`.

func NetSockPeerAddr ¶
func NetSockPeerAddr(val string) attribute.KeyValue

NetSockPeerAddr returns an attribute KeyValue conforming to the "net.sock.peer.addr" semantic conventions. It represents the deprecated, use `server.socket.address` on client spans and `client.socket.address` on server spans.

func NetSockPeerName ¶
func NetSockPeerName(val string) attribute.KeyValue

NetSockPeerName returns an attribute KeyValue conforming to the "net.sock.peer.name" semantic conventions. It represents the deprecated, use `server.socket.domain` on client spans.

func NetSockPeerPort ¶
func NetSockPeerPort(val int) attribute.KeyValue

NetSockPeerPort returns an attribute KeyValue conforming to the "net.sock.peer.port" semantic conventions. It represents the deprecated, use `server.socket.port` on client spans and `client.socket.port` on server spans.

func NetworkCarrierIcc ¶
func NetworkCarrierIcc(val string) attribute.KeyValue

NetworkCarrierIcc returns an attribute KeyValue conforming to the "network.carrier.icc" semantic conventions. It represents the ISO 3166-1 alpha-2 2-character country code associated with the mobile carrier network.

func NetworkCarrierMcc ¶
func NetworkCarrierMcc(val string) attribute.KeyValue

NetworkCarrierMcc returns an attribute KeyValue conforming to the "network.carrier.mcc" semantic conventions. It represents the mobile carrier country code.

func NetworkCarrierMnc ¶
func NetworkCarrierMnc(val string) attribute.KeyValue

NetworkCarrierMnc returns an attribute KeyValue conforming to the "network.carrier.mnc" semantic conventions. It represents the mobile carrier network code.

func NetworkCarrierName ¶
func NetworkCarrierName(val string) attribute.KeyValue

NetworkCarrierName returns an attribute KeyValue conforming to the "network.carrier.name" semantic conventions. It represents the name of the mobile carrier.

func NetworkProtocolName ¶
func NetworkProtocolName(val string) attribute.KeyValue

NetworkProtocolName returns an attribute KeyValue conforming to the "network.protocol.name" semantic conventions. It represents the [OSI Application Layer](https://osi-model.com/application-layer/) or non-OSI equivalent. The value SHOULD be normalized to lowercase.

func NetworkProtocolVersion ¶
func NetworkProtocolVersion(val string) attribute.KeyValue

NetworkProtocolVersion returns an attribute KeyValue conforming to the "network.protocol.version" semantic conventions. It represents the version of the application layer protocol used. See note below.

func OSDescription ¶
func OSDescription(val string) attribute.KeyValue

OSDescription returns an attribute KeyValue conforming to the "os.description" semantic conventions. It represents the human readable (not intended to be parsed) OS version information, like e.g. reported by `ver` or `lsb_release -a` commands.

func OSName ¶
func OSName(val string) attribute.KeyValue

OSName returns an attribute KeyValue conforming to the "os.name" semantic conventions. It represents the human readable operating system name.

func OSVersion ¶
func OSVersion(val string) attribute.KeyValue

OSVersion returns an attribute KeyValue conforming to the "os.version" semantic conventions. It represents the version string of the operating system as defined in [Version Attributes](/docs/resource/README.md#version-attributes).

func OTelLibraryName ¶
func OTelLibraryName(val string) attribute.KeyValue

OTelLibraryName returns an attribute KeyValue conforming to the "otel.library.name" semantic conventions. It represents the deprecated, use the `otel.scope.name` attribute.

func OTelLibraryVersion ¶
func OTelLibraryVersion(val string) attribute.KeyValue

OTelLibraryVersion returns an attribute KeyValue conforming to the "otel.library.version" semantic conventions. It represents the deprecated, use the `otel.scope.version` attribute.

func OTelScopeName ¶
func OTelScopeName(val string) attribute.KeyValue

OTelScopeName returns an attribute KeyValue conforming to the "otel.scope.name" semantic conventions. It represents the name of the instrumentation scope - (`InstrumentationScope.Name` in OTLP).

func OTelScopeVersion ¶
func OTelScopeVersion(val string) attribute.KeyValue

OTelScopeVersion returns an attribute KeyValue conforming to the "otel.scope.version" semantic conventions. It represents the version of the instrumentation scope - (`InstrumentationScope.Version` in OTLP).

func OTelStatusDescription ¶
func OTelStatusDescription(val string) attribute.KeyValue

OTelStatusDescription returns an attribute KeyValue conforming to the "otel.status_description" semantic conventions. It represents the description of the Status if it has a value, otherwise not set.

func PeerService ¶
func PeerService(val string) attribute.KeyValue

PeerService returns an attribute KeyValue conforming to the "peer.service" semantic conventions. It represents the [`service.name`](/docs/resource/README.md#service) of the remote service. SHOULD be equal to the actual `service.name` resource attribute of the remote service if any.

func Pool ¶
func Pool(val string) attribute.KeyValue

Pool returns an attribute KeyValue conforming to the "pool" semantic conventions. It represents the name of the memory pool.

func ProcessCommand ¶
func ProcessCommand(val string) attribute.KeyValue

ProcessCommand returns an attribute KeyValue conforming to the "process.command" semantic conventions. It represents the command used to launch the process (i.e. the command name). On Linux based systems, can be set to the zeroth string in `proc/[pid]/cmdline`. On Windows, can be set to the first parameter extracted from `GetCommandLineW`.

func ProcessCommandArgs ¶
func ProcessCommandArgs(val ...string) attribute.KeyValue

ProcessCommandArgs returns an attribute KeyValue conforming to the "process.command_args" semantic conventions. It represents the all the command arguments (including the command/executable itself) as received by the process. On Linux-based systems (and some other Unixoid systems supporting procfs), can be set according to the list of null-delimited strings extracted from `proc/[pid]/cmdline`. For libc-based executables, this would be the full argv vector passed to `main`.

func ProcessCommandLine ¶
func ProcessCommandLine(val string) attribute.KeyValue

ProcessCommandLine returns an attribute KeyValue conforming to the "process.command_line" semantic conventions. It represents the full command used to launch the process as a single string representing the full command. On Windows, can be set to the result of `GetCommandLineW`. Do not set this if you have to assemble it just for monitoring; use `process.command_args` instead.

func ProcessExecutableName ¶
func ProcessExecutableName(val string) attribute.KeyValue

ProcessExecutableName returns an attribute KeyValue conforming to the "process.executable.name" semantic conventions. It represents the name of the process executable. On Linux based systems, can be set to the `Name` in `proc/[pid]/status`. On Windows, can be set to the base name of `GetProcessImageFileNameW`.

func ProcessExecutablePath ¶
func ProcessExecutablePath(val string) attribute.KeyValue

ProcessExecutablePath returns an attribute KeyValue conforming to the "process.executable.path" semantic conventions. It represents the full path to the process executable. On Linux based systems, can be set to the target of `proc/[pid]/exe`. On Windows, can be set to the result of `GetProcessImageFileNameW`.

func ProcessOwner ¶
func ProcessOwner(val string) attribute.KeyValue

ProcessOwner returns an attribute KeyValue conforming to the "process.owner" semantic conventions. It represents the username of the user that owns the process.

func ProcessPID ¶
func ProcessPID(val int) attribute.KeyValue

ProcessPID returns an attribute KeyValue conforming to the "process.pid" semantic conventions. It represents the process identifier (PID).

func ProcessParentPID ¶
func ProcessParentPID(val int) attribute.KeyValue

ProcessParentPID returns an attribute KeyValue conforming to the "process.parent_pid" semantic conventions. It represents the parent Process identifier (PID).

func ProcessRuntimeDescription ¶
func ProcessRuntimeDescription(val string) attribute.KeyValue

ProcessRuntimeDescription returns an attribute KeyValue conforming to the "process.runtime.description" semantic conventions. It represents an additional description about the runtime of the process, for example a specific vendor customization of the runtime environment.

func ProcessRuntimeName ¶
func ProcessRuntimeName(val string) attribute.KeyValue

ProcessRuntimeName returns an attribute KeyValue conforming to the "process.runtime.name" semantic conventions. It represents the name of the runtime of this process. For compiled native binaries, this SHOULD be the name of the compiler.

func ProcessRuntimeVersion ¶
func ProcessRuntimeVersion(val string) attribute.KeyValue

ProcessRuntimeVersion returns an attribute KeyValue conforming to the "process.runtime.version" semantic conventions. It represents the version of the runtime of this process, as returned by the runtime without modification.

func RPCJsonrpcErrorCode ¶
func RPCJsonrpcErrorCode(val int) attribute.KeyValue

RPCJsonrpcErrorCode returns an attribute KeyValue conforming to the "rpc.jsonrpc.error_code" semantic conventions. It represents the `error.code` property of response if it is an error response.

func RPCJsonrpcErrorMessage ¶
func RPCJsonrpcErrorMessage(val string) attribute.KeyValue

RPCJsonrpcErrorMessage returns an attribute KeyValue conforming to the "rpc.jsonrpc.error_message" semantic conventions. It represents the `error.message` property of response if it is an error response.

func RPCJsonrpcRequestID ¶
func RPCJsonrpcRequestID(val string) attribute.KeyValue

RPCJsonrpcRequestID returns an attribute KeyValue conforming to the "rpc.jsonrpc.request_id" semantic conventions. It represents the `id` property of request or response. Since protocol allows id to be int, string, `null` or missing (for notifications), value is expected to be cast to string for simplicity. Use empty string in case of `null` value. Omit entirely if this is a notification.

func RPCJsonrpcVersion ¶
func RPCJsonrpcVersion(val string) attribute.KeyValue

RPCJsonrpcVersion returns an attribute KeyValue conforming to the "rpc.jsonrpc.version" semantic conventions. It represents the protocol version as in `jsonrpc` property of request/response. Since JSON-RPC 1.0 does not specify this, the value can be omitted.

func RPCMethod ¶
func RPCMethod(val string) attribute.KeyValue

RPCMethod returns an attribute KeyValue conforming to the "rpc.method" semantic conventions. It represents the name of the (logical) method being called, must be equal to the $method part in the span name.

func RPCService ¶
func RPCService(val string) attribute.KeyValue

RPCService returns an attribute KeyValue conforming to the "rpc.service" semantic conventions. It represents the full (logical) name of the service being called, including its package name, if applicable.

func ServerAddress ¶
func ServerAddress(val string) attribute.KeyValue

ServerAddress returns an attribute KeyValue conforming to the "server.address" semantic conventions. It represents the logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known.

func ServerPort ¶
func ServerPort(val int) attribute.KeyValue

ServerPort returns an attribute KeyValue conforming to the "server.port" semantic conventions. It represents the logical server port number

func ServerSocketAddress ¶
func ServerSocketAddress(val string) attribute.KeyValue

ServerSocketAddress returns an attribute KeyValue conforming to the "server.socket.address" semantic conventions. It represents the physical server IP address or Unix socket address. If set from the client, should simply use the socket's peer address, and not attempt to find any actual server IP (i.e., if set from client, this may represent some proxy server instead of the logical server).

func ServerSocketDomain ¶
func ServerSocketDomain(val string) attribute.KeyValue

ServerSocketDomain returns an attribute KeyValue conforming to the "server.socket.domain" semantic conventions. It represents the domain name of an immediate peer.

func ServerSocketPort ¶
func ServerSocketPort(val int) attribute.KeyValue

ServerSocketPort returns an attribute KeyValue conforming to the "server.socket.port" semantic conventions. It represents the physical server port.

func ServiceInstanceID ¶
func ServiceInstanceID(val string) attribute.KeyValue

ServiceInstanceID returns an attribute KeyValue conforming to the "service.instance.id" semantic conventions. It represents the string ID of the service instance.

func ServiceName ¶
func ServiceName(val string) attribute.KeyValue

ServiceName returns an attribute KeyValue conforming to the "service.name" semantic conventions. It represents the logical name of the service.

func ServiceNamespace ¶
func ServiceNamespace(val string) attribute.KeyValue

ServiceNamespace returns an attribute KeyValue conforming to the "service.namespace" semantic conventions. It represents a namespace for `service.name`.

func ServiceVersion ¶
func ServiceVersion(val string) attribute.KeyValue

ServiceVersion returns an attribute KeyValue conforming to the "service.version" semantic conventions. It represents the version string of the service API or implementation. The format is not defined by these conventions.

func SourceAddress ¶
func SourceAddress(val string) attribute.KeyValue

SourceAddress returns an attribute KeyValue conforming to the "source.address" semantic conventions. It represents the source address, for example IP address or Unix socket name.

func SourceDomain ¶
func SourceDomain(val string) attribute.KeyValue

SourceDomain returns an attribute KeyValue conforming to the "source.domain" semantic conventions. It represents the domain name of the source system.

func SourcePort ¶
func SourcePort(val int) attribute.KeyValue

SourcePort returns an attribute KeyValue conforming to the "source.port" semantic conventions. It represents the source port number

func TelemetryAutoVersion ¶
func TelemetryAutoVersion(val string) attribute.KeyValue

TelemetryAutoVersion returns an attribute KeyValue conforming to the "telemetry.auto.version" semantic conventions. It represents the version string of the auto instrumentation agent, if used.

func TelemetrySDKName ¶
func TelemetrySDKName(val string) attribute.KeyValue

TelemetrySDKName returns an attribute KeyValue conforming to the "telemetry.sdk.name" semantic conventions. It represents the name of the telemetry SDK as defined above.

func TelemetrySDKVersion ¶
func TelemetrySDKVersion(val string) attribute.KeyValue

TelemetrySDKVersion returns an attribute KeyValue conforming to the "telemetry.sdk.version" semantic conventions. It represents the version string of the telemetry SDK.

func ThreadID ¶
func ThreadID(val int) attribute.KeyValue

ThreadID returns an attribute KeyValue conforming to the "thread.id" semantic conventions. It represents the current "managed" thread ID (as opposed to OS thread ID).

func ThreadName ¶
func ThreadName(val string) attribute.KeyValue

ThreadName returns an attribute KeyValue conforming to the "thread.name" semantic conventions. It represents the current thread name.

func URLFragment ¶
func URLFragment(val string) attribute.KeyValue

URLFragment returns an attribute KeyValue conforming to the "url.fragment" semantic conventions. It represents the [URI fragment](https://www.rfc-editor.org/rfc/rfc3986#section-3.5) component

func URLFull ¶
func URLFull(val string) attribute.KeyValue

URLFull returns an attribute KeyValue conforming to the "url.full" semantic conventions. It represents the absolute URL describing a network resource according to [RFC3986](https://www.rfc-editor.org/rfc/rfc3986)

func URLPath ¶
func URLPath(val string) attribute.KeyValue

URLPath returns an attribute KeyValue conforming to the "url.path" semantic conventions. It represents the [URI path](https://www.rfc-editor.org/rfc/rfc3986#section-3.3) component

func URLQuery ¶
func URLQuery(val string) attribute.KeyValue

URLQuery returns an attribute KeyValue conforming to the "url.query" semantic conventions. It represents the [URI query](https://www.rfc-editor.org/rfc/rfc3986#section-3.4) component

func URLScheme ¶
func URLScheme(val string) attribute.KeyValue

URLScheme returns an attribute KeyValue conforming to the "url.scheme" semantic conventions. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

func UserAgentOriginal ¶
func UserAgentOriginal(val string) attribute.KeyValue

UserAgentOriginal returns an attribute KeyValue conforming to the "user_agent.original" semantic conventions. It represents the value of the [HTTP User-Agent](https://www.rfc-editor.org/rfc/rfc9110.html#field.user-agent) header sent by the client.

func WebEngineDescription ¶
func WebEngineDescription(val string) attribute.KeyValue

WebEngineDescription returns an attribute KeyValue conforming to the "webengine.description" semantic conventions. It represents the additional description of the web engine (e.g. detailed version and edition information).

func WebEngineName ¶
func WebEngineName(val string) attribute.KeyValue

WebEngineName returns an attribute KeyValue conforming to the "webengine.name" semantic conventions. It represents the name of the web engine.

func WebEngineVersion ¶
func WebEngineVersion(val string) attribute.KeyValue

WebEngineVersion returns an attribute KeyValue conforming to the "webengine.version" semantic conventions. It represents the version of the web engine.

Types ¶

This section is empty.

 Source Files ¶
View all Source files
attribute_group.go
doc.go
event.go
exception.go
resource.go
schema.go
trace.go
Why Go
Use Cases
Case Studies
Get Started
Playground
Tour
Stack Overflow
Help
Packages
Standard Library
Sub-repositories
About Go Packages
About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct
Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly
Copyright
Terms of Service
Privacy Policy
Report an Issue

Theme Toggle

Shortcuts Modal
