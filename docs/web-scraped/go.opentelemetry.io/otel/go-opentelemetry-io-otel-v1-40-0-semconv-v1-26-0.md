# Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.26.0

Title: semconv package - go.opentelemetry.io/otel/semconv/v1.26.0 - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.26.0

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
 
v1.26.0
semconv
package
Version: v1.40.0 Latest 
Published: Feb 2, 2026 
License: Apache-2.0, BSD-3-Clause 
Imports: 1 
Imported by: 643
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
Semconv v1.26.0

 Documentation ¶
Overview ¶

Package semconv implements OpenTelemetry semantic conventions.

OpenTelemetry semantic conventions are agreed standardized naming patterns for OpenTelemetry things. This package represents the v1.26.0 version of the OpenTelemetry semantic conventions.

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
func AWSECSTaskID(val string) attribute.KeyValue
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
func AndroidOSAPILevel(val string) attribute.KeyValue
func AspnetcoreDiagnosticsHandlerType(val string) attribute.KeyValue
func AspnetcoreRateLimitingPolicy(val string) attribute.KeyValue
func AspnetcoreRequestIsUnhandled(val bool) attribute.KeyValue
func AspnetcoreRoutingIsFallback(val bool) attribute.KeyValue
func BrowserBrands(val ...string) attribute.KeyValue
func BrowserLanguage(val string) attribute.KeyValue
func BrowserMobile(val bool) attribute.KeyValue
func BrowserPlatform(val string) attribute.KeyValue
func ClientAddress(val string) attribute.KeyValue
func ClientPort(val int) attribute.KeyValue
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
func CodeStacktrace(val string) attribute.KeyValue
func ContainerCommand(val string) attribute.KeyValue
func ContainerCommandArgs(val ...string) attribute.KeyValue
func ContainerCommandLine(val string) attribute.KeyValue
func ContainerID(val string) attribute.KeyValue
func ContainerImageID(val string) attribute.KeyValue
func ContainerImageName(val string) attribute.KeyValue
func ContainerImageRepoDigests(val ...string) attribute.KeyValue
func ContainerImageTags(val ...string) attribute.KeyValue
func ContainerName(val string) attribute.KeyValue
func ContainerRuntime(val string) attribute.KeyValue
func DBCassandraCoordinatorDC(val string) attribute.KeyValue
func DBCassandraCoordinatorID(val string) attribute.KeyValue
func DBCassandraIdempotence(val bool) attribute.KeyValue
func DBCassandraPageSize(val int) attribute.KeyValue
func DBCassandraSpeculativeExecutionCount(val int) attribute.KeyValue
func DBClientConnectionsPoolName(val string) attribute.KeyValue
func DBCollectionName(val string) attribute.KeyValue
func DBCosmosDBClientID(val string) attribute.KeyValue
func DBCosmosDBRequestCharge(val float64) attribute.KeyValue
func DBCosmosDBRequestContentLength(val int) attribute.KeyValue
func DBCosmosDBStatusCode(val int) attribute.KeyValue
func DBCosmosDBSubStatusCode(val int) attribute.KeyValue
func DBElasticsearchClusterName(val string) attribute.KeyValue
func DBElasticsearchNodeName(val string) attribute.KeyValue
func DBNamespace(val string) attribute.KeyValue
func DBOperationName(val string) attribute.KeyValue
func DBQueryText(val string) attribute.KeyValue
func DNSQuestionName(val string) attribute.KeyValue
func DeploymentEnvironment(val string) attribute.KeyValue
func DestinationAddress(val string) attribute.KeyValue
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
func FileDirectory(val string) attribute.KeyValue
func FileExtension(val string) attribute.KeyValue
func FileName(val string) attribute.KeyValue
func FilePath(val string) attribute.KeyValue
func FileSize(val int) attribute.KeyValue
func GCPCloudRunJobExecution(val string) attribute.KeyValue
func GCPCloudRunJobTaskIndex(val int) attribute.KeyValue
func GCPGceInstanceHostname(val string) attribute.KeyValue
func GCPGceInstanceName(val string) attribute.KeyValue
func GenAiCompletion(val string) attribute.KeyValue
func GenAiPrompt(val string) attribute.KeyValue
func GenAiRequestMaxTokens(val int) attribute.KeyValue
func GenAiRequestModel(val string) attribute.KeyValue
func GenAiRequestTemperature(val float64) attribute.KeyValue
func GenAiRequestTopP(val float64) attribute.KeyValue
func GenAiResponseFinishReasons(val ...string) attribute.KeyValue
func GenAiResponseID(val string) attribute.KeyValue
func GenAiResponseModel(val string) attribute.KeyValue
func GenAiUsageCompletionTokens(val int) attribute.KeyValue
func GenAiUsagePromptTokens(val int) attribute.KeyValue
func GraphqlDocument(val string) attribute.KeyValue
func GraphqlOperationName(val string) attribute.KeyValue
func HTTPRequestBodySize(val int) attribute.KeyValue
func HTTPRequestMethodOriginal(val string) attribute.KeyValue
func HTTPRequestResendCount(val int) attribute.KeyValue
func HTTPRequestSize(val int) attribute.KeyValue
func HTTPResponseBodySize(val int) attribute.KeyValue
func HTTPResponseSize(val int) attribute.KeyValue
func HTTPResponseStatusCode(val int) attribute.KeyValue
func HTTPRoute(val string) attribute.KeyValue
func HerokuAppID(val string) attribute.KeyValue
func HerokuReleaseCommit(val string) attribute.KeyValue
func HerokuReleaseCreationTimestamp(val string) attribute.KeyValue
func HostCPUCacheL2Size(val int) attribute.KeyValue
func HostCPUFamily(val string) attribute.KeyValue
func HostCPUModelID(val string) attribute.KeyValue
func HostCPUModelName(val string) attribute.KeyValue
func HostCPUStepping(val string) attribute.KeyValue
func HostCPUVendorID(val string) attribute.KeyValue
func HostID(val string) attribute.KeyValue
func HostIP(val ...string) attribute.KeyValue
func HostImageID(val string) attribute.KeyValue
func HostImageName(val string) attribute.KeyValue
func HostImageVersion(val string) attribute.KeyValue
func HostMac(val ...string) attribute.KeyValue
func HostName(val string) attribute.KeyValue
func HostType(val string) attribute.KeyValue
func JvmBufferPoolName(val string) attribute.KeyValue
func JvmGcAction(val string) attribute.KeyValue
func JvmGcName(val string) attribute.KeyValue
func JvmMemoryPoolName(val string) attribute.KeyValue
func JvmThreadDaemon(val bool) attribute.KeyValue
func K8SClusterName(val string) attribute.KeyValue
func K8SClusterUID(val string) attribute.KeyValue
func K8SContainerName(val string) attribute.KeyValue
func K8SContainerRestartCount(val int) attribute.KeyValue
func K8SContainerStatusLastTerminatedReason(val string) attribute.KeyValue
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
func MessagingBatchMessageCount(val int) attribute.KeyValue
func MessagingClientID(val string) attribute.KeyValue
func MessagingDestinationAnonymous(val bool) attribute.KeyValue
func MessagingDestinationName(val string) attribute.KeyValue
func MessagingDestinationPartitionID(val string) attribute.KeyValue
func MessagingDestinationPublishAnonymous(val bool) attribute.KeyValue
func MessagingDestinationPublishName(val string) attribute.KeyValue
func MessagingDestinationTemplate(val string) attribute.KeyValue
func MessagingDestinationTemporary(val bool) attribute.KeyValue
func MessagingEventhubsConsumerGroup(val string) attribute.KeyValue
func MessagingEventhubsMessageEnqueuedTime(val int) attribute.KeyValue
func MessagingGCPPubsubMessageAckDeadline(val int) attribute.KeyValue
func MessagingGCPPubsubMessageAckID(val string) attribute.KeyValue
func MessagingGCPPubsubMessageDeliveryAttempt(val int) attribute.KeyValue
func MessagingGCPPubsubMessageOrderingKey(val string) attribute.KeyValue
func MessagingKafkaConsumerGroup(val string) attribute.KeyValue
func MessagingKafkaMessageKey(val string) attribute.KeyValue
func MessagingKafkaMessageOffset(val int) attribute.KeyValue
func MessagingKafkaMessageTombstone(val bool) attribute.KeyValue
func MessagingMessageBodySize(val int) attribute.KeyValue
func MessagingMessageConversationID(val string) attribute.KeyValue
func MessagingMessageEnvelopeSize(val int) attribute.KeyValue
func MessagingMessageID(val string) attribute.KeyValue
func MessagingOperationName(val string) attribute.KeyValue
func MessagingRabbitmqDestinationRoutingKey(val string) attribute.KeyValue
func MessagingRabbitmqMessageDeliveryTag(val int) attribute.KeyValue
func MessagingRocketmqClientGroup(val string) attribute.KeyValue
func MessagingRocketmqMessageDelayTimeLevel(val int) attribute.KeyValue
func MessagingRocketmqMessageDeliveryTimestamp(val int) attribute.KeyValue
func MessagingRocketmqMessageGroup(val string) attribute.KeyValue
func MessagingRocketmqMessageKeys(val ...string) attribute.KeyValue
func MessagingRocketmqMessageTag(val string) attribute.KeyValue
func MessagingRocketmqNamespace(val string) attribute.KeyValue
func MessagingServicebusDestinationSubscriptionName(val string) attribute.KeyValue
func MessagingServicebusMessageDeliveryCount(val int) attribute.KeyValue
func MessagingServicebusMessageEnqueuedTime(val int) attribute.KeyValue
func NetworkCarrierIcc(val string) attribute.KeyValue
func NetworkCarrierMcc(val string) attribute.KeyValue
func NetworkCarrierMnc(val string) attribute.KeyValue
func NetworkCarrierName(val string) attribute.KeyValue
func NetworkLocalAddress(val string) attribute.KeyValue
func NetworkLocalPort(val int) attribute.KeyValue
func NetworkPeerAddress(val string) attribute.KeyValue
func NetworkPeerPort(val int) attribute.KeyValue
func NetworkProtocolName(val string) attribute.KeyValue
func NetworkProtocolVersion(val string) attribute.KeyValue
func OSBuildID(val string) attribute.KeyValue
func OSDescription(val string) attribute.KeyValue
func OSName(val string) attribute.KeyValue
func OSVersion(val string) attribute.KeyValue
func OTelScopeName(val string) attribute.KeyValue
func OTelScopeVersion(val string) attribute.KeyValue
func OTelStatusDescription(val string) attribute.KeyValue
func OciManifestDigest(val string) attribute.KeyValue
func PeerService(val string) attribute.KeyValue
func ProcessCommand(val string) attribute.KeyValue
func ProcessCommandArgs(val ...string) attribute.KeyValue
func ProcessCommandLine(val string) attribute.KeyValue
func ProcessCreationTime(val string) attribute.KeyValue
func ProcessExecutableName(val string) attribute.KeyValue
func ProcessExecutablePath(val string) attribute.KeyValue
func ProcessExitCode(val int) attribute.KeyValue
func ProcessExitTime(val string) attribute.KeyValue
func ProcessGroupLeaderPID(val int) attribute.KeyValue
func ProcessInteractive(val bool) attribute.KeyValue
func ProcessOwner(val string) attribute.KeyValue
func ProcessPID(val int) attribute.KeyValue
func ProcessParentPID(val int) attribute.KeyValue
func ProcessRealUserID(val int) attribute.KeyValue
func ProcessRealUserName(val string) attribute.KeyValue
func ProcessRuntimeDescription(val string) attribute.KeyValue
func ProcessRuntimeName(val string) attribute.KeyValue
func ProcessRuntimeVersion(val string) attribute.KeyValue
func ProcessSavedUserID(val int) attribute.KeyValue
func ProcessSavedUserName(val string) attribute.KeyValue
func ProcessSessionLeaderPID(val int) attribute.KeyValue
func ProcessUserID(val int) attribute.KeyValue
func ProcessUserName(val string) attribute.KeyValue
func ProcessVpid(val int) attribute.KeyValue
func RPCJsonrpcErrorCode(val int) attribute.KeyValue
func RPCJsonrpcErrorMessage(val string) attribute.KeyValue
func RPCJsonrpcRequestID(val string) attribute.KeyValue
func RPCJsonrpcVersion(val string) attribute.KeyValue
func RPCMessageCompressedSize(val int) attribute.KeyValue
func RPCMessageID(val int) attribute.KeyValue
func RPCMessageUncompressedSize(val int) attribute.KeyValue
func RPCMethod(val string) attribute.KeyValue
func RPCService(val string) attribute.KeyValue
func ServerAddress(val string) attribute.KeyValue
func ServerPort(val int) attribute.KeyValue
func ServiceInstanceID(val string) attribute.KeyValue
func ServiceName(val string) attribute.KeyValue
func ServiceNamespace(val string) attribute.KeyValue
func ServiceVersion(val string) attribute.KeyValue
func SessionID(val string) attribute.KeyValue
func SessionPreviousID(val string) attribute.KeyValue
func SourceAddress(val string) attribute.KeyValue
func SourcePort(val int) attribute.KeyValue
func SystemCPULogicalNumber(val int) attribute.KeyValue
func SystemDevice(val string) attribute.KeyValue
func SystemFilesystemMode(val string) attribute.KeyValue
func SystemFilesystemMountpoint(val string) attribute.KeyValue
func TLSCipher(val string) attribute.KeyValue
func TLSClientCertificate(val string) attribute.KeyValue
func TLSClientCertificateChain(val ...string) attribute.KeyValue
func TLSClientHashMd5(val string) attribute.KeyValue
func TLSClientHashSha1(val string) attribute.KeyValue
func TLSClientHashSha256(val string) attribute.KeyValue
func TLSClientIssuer(val string) attribute.KeyValue
func TLSClientJa3(val string) attribute.KeyValue
func TLSClientNotAfter(val string) attribute.KeyValue
func TLSClientNotBefore(val string) attribute.KeyValue
func TLSClientServerName(val string) attribute.KeyValue
func TLSClientSubject(val string) attribute.KeyValue
func TLSClientSupportedCiphers(val ...string) attribute.KeyValue
func TLSCurve(val string) attribute.KeyValue
func TLSEstablished(val bool) attribute.KeyValue
func TLSNextProtocol(val string) attribute.KeyValue
func TLSProtocolVersion(val string) attribute.KeyValue
func TLSResumed(val bool) attribute.KeyValue
func TLSServerCertificate(val string) attribute.KeyValue
func TLSServerCertificateChain(val ...string) attribute.KeyValue
func TLSServerHashMd5(val string) attribute.KeyValue
func TLSServerHashSha1(val string) attribute.KeyValue
func TLSServerHashSha256(val string) attribute.KeyValue
func TLSServerIssuer(val string) attribute.KeyValue
func TLSServerJa3s(val string) attribute.KeyValue
func TLSServerNotAfter(val string) attribute.KeyValue
func TLSServerNotBefore(val string) attribute.KeyValue
func TLSServerSubject(val string) attribute.KeyValue
func TelemetryDistroName(val string) attribute.KeyValue
func TelemetryDistroVersion(val string) attribute.KeyValue
func TelemetrySDKName(val string) attribute.KeyValue
func TelemetrySDKVersion(val string) attribute.KeyValue
func ThreadID(val int) attribute.KeyValue
func ThreadName(val string) attribute.KeyValue
func URLDomain(val string) attribute.KeyValue
func URLExtension(val string) attribute.KeyValue
func URLFragment(val string) attribute.KeyValue
func URLFull(val string) attribute.KeyValue
func URLOriginal(val string) attribute.KeyValue
func URLPath(val string) attribute.KeyValue
func URLPort(val int) attribute.KeyValue
func URLQuery(val string) attribute.KeyValue
func URLRegisteredDomain(val string) attribute.KeyValue
func URLScheme(val string) attribute.KeyValue
func URLSubdomain(val string) attribute.KeyValue
func URLTemplate(val string) attribute.KeyValue
func URLTopLevelDomain(val string) attribute.KeyValue
func UserAgentName(val string) attribute.KeyValue
func UserAgentOriginal(val string) attribute.KeyValue
func UserAgentVersion(val string) attribute.KeyValue
func WebEngineDescription(val string) attribute.KeyValue
func WebEngineName(val string) attribute.KeyValue
func WebEngineVersion(val string) attribute.KeyValue
Constants ¶
View Source
const (
	// AspnetcoreRateLimitingResultKey is the attribute Key conforming to the
	// "aspnetcore.rate_limiting.result" semantic conventions. It represents
	// the rate-limiting result, shows whether the lease was acquired or
	// contains a rejection reason
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	// Examples: 'acquired', 'request_canceled'
	AspnetcoreRateLimitingResultKey = attribute.Key("aspnetcore.rate_limiting.result")

	// AspnetcoreDiagnosticsHandlerTypeKey is the attribute Key conforming to
	// the "aspnetcore.diagnostics.handler.type" semantic conventions. It
	// represents the full type name of the
	// [`IExceptionHandler`](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.diagnostics.iexceptionhandler)
	// implementation that handled the exception.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (if and only if the exception
	// was handled by this handler.)
	// Stability: stable
	// Examples: 'Contoso.MyHandler'
	AspnetcoreDiagnosticsHandlerTypeKey = attribute.Key("aspnetcore.diagnostics.handler.type")

	// AspnetcoreDiagnosticsExceptionResultKey is the attribute Key conforming
	// to the "aspnetcore.diagnostics.exception.result" semantic conventions.
	// It represents the aSP.NET Core exception middleware handling result
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'handled', 'unhandled'
	AspnetcoreDiagnosticsExceptionResultKey = attribute.Key("aspnetcore.diagnostics.exception.result")

	// AspnetcoreRateLimitingPolicyKey is the attribute Key conforming to the
	// "aspnetcore.rate_limiting.policy" semantic conventions. It represents
	// the rate limiting policy name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'fixed', 'sliding', 'token'
	AspnetcoreRateLimitingPolicyKey = attribute.Key("aspnetcore.rate_limiting.policy")

	// AspnetcoreRequestIsUnhandledKey is the attribute Key conforming to the
	// "aspnetcore.request.is_unhandled" semantic conventions. It represents
	// the flag indicating if request was handled by the application pipeline.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: True
	AspnetcoreRequestIsUnhandledKey = attribute.Key("aspnetcore.request.is_unhandled")

	// AspnetcoreRoutingIsFallbackKey is the attribute Key conforming to the
	// "aspnetcore.routing.is_fallback" semantic conventions. It represents a
	// value that indicates whether the matched route is a fallback route.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: True
	AspnetcoreRoutingIsFallbackKey = attribute.Key("aspnetcore.routing.is_fallback")

	// AspnetcoreRoutingMatchStatusKey is the attribute Key conforming to the
	// "aspnetcore.routing.match_status" semantic conventions. It represents
	// the match result - success or failure
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'success', 'failure'
	AspnetcoreRoutingMatchStatusKey = attribute.Key("aspnetcore.routing.match_status")
)

ASP.NET Core attributes

View Source
const (
	// AWSDynamoDBAttributeDefinitionsKey is the attribute Key conforming to
	// the "aws.dynamodb.attribute_definitions" semantic conventions. It
	// represents the JSON-serialized value of each item in the
	// `AttributeDefinitions` request field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '{ "AttributeName": "string", "AttributeType": "string" }'
	AWSDynamoDBAttributeDefinitionsKey = attribute.Key("aws.dynamodb.attribute_definitions")

	// AWSDynamoDBAttributesToGetKey is the attribute Key conforming to the
	// "aws.dynamodb.attributes_to_get" semantic conventions. It represents the
	// value of the `AttributesToGet` request parameter.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'lives', 'id'
	AWSDynamoDBAttributesToGetKey = attribute.Key("aws.dynamodb.attributes_to_get")

	// AWSDynamoDBConsistentReadKey is the attribute Key conforming to the
	// "aws.dynamodb.consistent_read" semantic conventions. It represents the
	// value of the `ConsistentRead` request parameter.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	AWSDynamoDBConsistentReadKey = attribute.Key("aws.dynamodb.consistent_read")

	// AWSDynamoDBConsumedCapacityKey is the attribute Key conforming to the
	// "aws.dynamodb.consumed_capacity" semantic conventions. It represents the
	// JSON-serialized value of each item in the `ConsumedCapacity` response
	// field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '{ "CapacityUnits": number, "GlobalSecondaryIndexes": {
	// "string" : { "CapacityUnits": number, "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number } }, "LocalSecondaryIndexes": { "string" :
	// { "CapacityUnits": number, "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number } }, "ReadCapacityUnits": number, "Table":
	// { "CapacityUnits": number, "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number }, "TableName": "string",
	// "WriteCapacityUnits": number }'
	AWSDynamoDBConsumedCapacityKey = attribute.Key("aws.dynamodb.consumed_capacity")

	// AWSDynamoDBCountKey is the attribute Key conforming to the
	// "aws.dynamodb.count" semantic conventions. It represents the value of
	// the `Count` response parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 10
	AWSDynamoDBCountKey = attribute.Key("aws.dynamodb.count")

	// AWSDynamoDBExclusiveStartTableKey is the attribute Key conforming to the
	// "aws.dynamodb.exclusive_start_table" semantic conventions. It represents
	// the value of the `ExclusiveStartTableName` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Users', 'CatsTable'
	AWSDynamoDBExclusiveStartTableKey = attribute.Key("aws.dynamodb.exclusive_start_table")

	// AWSDynamoDBGlobalSecondaryIndexUpdatesKey is the attribute Key
	// conforming to the "aws.dynamodb.global_secondary_index_updates" semantic
	// conventions. It represents the JSON-serialized value of each item in the
	// `GlobalSecondaryIndexUpdates` request field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '{ "Create": { "IndexName": "string", "KeySchema": [ {
	// "AttributeName": "string", "KeyType": "string" } ], "Projection": {
	// "NonKeyAttributes": [ "string" ], "ProjectionType": "string" },
	// "ProvisionedThroughput": { "ReadCapacityUnits": number,
	// "WriteCapacityUnits": number } }'
	AWSDynamoDBGlobalSecondaryIndexUpdatesKey = attribute.Key("aws.dynamodb.global_secondary_index_updates")

	// AWSDynamoDBGlobalSecondaryIndexesKey is the attribute Key conforming to
	// the "aws.dynamodb.global_secondary_indexes" semantic conventions. It
	// represents the JSON-serialized value of each item of the
	// `GlobalSecondaryIndexes` request field
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '{ "IndexName": "string", "KeySchema": [ { "AttributeName":
	// "string", "KeyType": "string" } ], "Projection": { "NonKeyAttributes": [
	// "string" ], "ProjectionType": "string" }, "ProvisionedThroughput": {
	// "ReadCapacityUnits": number, "WriteCapacityUnits": number } }'
	AWSDynamoDBGlobalSecondaryIndexesKey = attribute.Key("aws.dynamodb.global_secondary_indexes")

	// AWSDynamoDBIndexNameKey is the attribute Key conforming to the
	// "aws.dynamodb.index_name" semantic conventions. It represents the value
	// of the `IndexName` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'name_to_group'
	AWSDynamoDBIndexNameKey = attribute.Key("aws.dynamodb.index_name")

	// AWSDynamoDBItemCollectionMetricsKey is the attribute Key conforming to
	// the "aws.dynamodb.item_collection_metrics" semantic conventions. It
	// represents the JSON-serialized value of the `ItemCollectionMetrics`
	// response field.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '{ "string" : [ { "ItemCollectionKey": { "string" : { "B":
	// blob, "BOOL": boolean, "BS": [ blob ], "L": [ "AttributeValue" ], "M": {
	// "string" : "AttributeValue" }, "N": "string", "NS": [ "string" ],
	// "NULL": boolean, "S": "string", "SS": [ "string" ] } },
	// "SizeEstimateRangeGB": [ number ] } ] }'
	AWSDynamoDBItemCollectionMetricsKey = attribute.Key("aws.dynamodb.item_collection_metrics")

	// AWSDynamoDBLimitKey is the attribute Key conforming to the
	// "aws.dynamodb.limit" semantic conventions. It represents the value of
	// the `Limit` request parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 10
	AWSDynamoDBLimitKey = attribute.Key("aws.dynamodb.limit")

	// AWSDynamoDBLocalSecondaryIndexesKey is the attribute Key conforming to
	// the "aws.dynamodb.local_secondary_indexes" semantic conventions. It
	// represents the JSON-serialized value of each item of the
	// `LocalSecondaryIndexes` request field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '{ "IndexARN": "string", "IndexName": "string",
	// "IndexSizeBytes": number, "ItemCount": number, "KeySchema": [ {
	// "AttributeName": "string", "KeyType": "string" } ], "Projection": {
	// "NonKeyAttributes": [ "string" ], "ProjectionType": "string" } }'
	AWSDynamoDBLocalSecondaryIndexesKey = attribute.Key("aws.dynamodb.local_secondary_indexes")

	// AWSDynamoDBProjectionKey is the attribute Key conforming to the
	// "aws.dynamodb.projection" semantic conventions. It represents the value
	// of the `ProjectionExpression` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Title', 'Title, Price, Color', 'Title, Description,
	// RelatedItems, ProductReviews'
	AWSDynamoDBProjectionKey = attribute.Key("aws.dynamodb.projection")

	// AWSDynamoDBProvisionedReadCapacityKey is the attribute Key conforming to
	// the "aws.dynamodb.provisioned_read_capacity" semantic conventions. It
	// represents the value of the `ProvisionedThroughput.ReadCapacityUnits`
	// request parameter.
	//
	// Type: double
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1.0, 2.0
	AWSDynamoDBProvisionedReadCapacityKey = attribute.Key("aws.dynamodb.provisioned_read_capacity")

	// AWSDynamoDBProvisionedWriteCapacityKey is the attribute Key conforming
	// to the "aws.dynamodb.provisioned_write_capacity" semantic conventions.
	// It represents the value of the
	// `ProvisionedThroughput.WriteCapacityUnits` request parameter.
	//
	// Type: double
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1.0, 2.0
	AWSDynamoDBProvisionedWriteCapacityKey = attribute.Key("aws.dynamodb.provisioned_write_capacity")

	// AWSDynamoDBScanForwardKey is the attribute Key conforming to the
	// "aws.dynamodb.scan_forward" semantic conventions. It represents the
	// value of the `ScanIndexForward` request parameter.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	AWSDynamoDBScanForwardKey = attribute.Key("aws.dynamodb.scan_forward")

	// AWSDynamoDBScannedCountKey is the attribute Key conforming to the
	// "aws.dynamodb.scanned_count" semantic conventions. It represents the
	// value of the `ScannedCount` response parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 50
	AWSDynamoDBScannedCountKey = attribute.Key("aws.dynamodb.scanned_count")

	// AWSDynamoDBSegmentKey is the attribute Key conforming to the
	// "aws.dynamodb.segment" semantic conventions. It represents the value of
	// the `Segment` request parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 10
	AWSDynamoDBSegmentKey = attribute.Key("aws.dynamodb.segment")

	// AWSDynamoDBSelectKey is the attribute Key conforming to the
	// "aws.dynamodb.select" semantic conventions. It represents the value of
	// the `Select` request parameter.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'ALL_ATTRIBUTES', 'COUNT'
	AWSDynamoDBSelectKey = attribute.Key("aws.dynamodb.select")

	// AWSDynamoDBTableCountKey is the attribute Key conforming to the
	// "aws.dynamodb.table_count" semantic conventions. It represents the
	// number of items in the `TableNames` response parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 20
	AWSDynamoDBTableCountKey = attribute.Key("aws.dynamodb.table_count")

	// AWSDynamoDBTableNamesKey is the attribute Key conforming to the
	// "aws.dynamodb.table_names" semantic conventions. It represents the keys
	// in the `RequestItems` object field.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Users', 'Cats'
	AWSDynamoDBTableNamesKey = attribute.Key("aws.dynamodb.table_names")

	// AWSDynamoDBTotalSegmentsKey is the attribute Key conforming to the
	// "aws.dynamodb.total_segments" semantic conventions. It represents the
	// value of the `TotalSegments` request parameter.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 100
	AWSDynamoDBTotalSegmentsKey = attribute.Key("aws.dynamodb.total_segments")
)

Attributes for AWS DynamoDB.

View Source
const (
	// AWSECSTaskIDKey is the attribute Key conforming to the "aws.ecs.task.id"
	// semantic conventions. It represents the ID of a running ECS task. The ID
	// MUST be extracted from `task.arn`.
	//
	// Type: string
	// RequirementLevel: ConditionallyRequired (If and only if `task.arn` is
	// populated.)
	// Stability: experimental
	// Examples: '10838bed-421f-43ef-870a-f43feacbbb5b',
	// '23ebb8ac-c18f-46c6-8bbe-d55d0e37cfbd'
	AWSECSTaskIDKey = attribute.Key("aws.ecs.task.id")

	// AWSECSClusterARNKey is the attribute Key conforming to the
	// "aws.ecs.cluster.arn" semantic conventions. It represents the ARN of an
	// [ECS
	// cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'arn:aws:ecs:us-west-2:123456789123:cluster/my-cluster'
	AWSECSClusterARNKey = attribute.Key("aws.ecs.cluster.arn")

	// AWSECSContainerARNKey is the attribute Key conforming to the
	// "aws.ecs.container.arn" semantic conventions. It represents the Amazon
	// Resource Name (ARN) of an [ECS container
	// instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'arn:aws:ecs:us-west-1:123456789123:container/32624152-9086-4f0e-acae-1a75b14fe4d9'
	AWSECSContainerARNKey = attribute.Key("aws.ecs.container.arn")

	// AWSECSLaunchtypeKey is the attribute Key conforming to the
	// "aws.ecs.launchtype" semantic conventions. It represents the [launch
	// type](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html)
	// for an ECS task.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	AWSECSLaunchtypeKey = attribute.Key("aws.ecs.launchtype")

	// AWSECSTaskARNKey is the attribute Key conforming to the
	// "aws.ecs.task.arn" semantic conventions. It represents the ARN of a
	// running [ECS
	// task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'arn:aws:ecs:us-west-1:123456789123:task/10838bed-421f-43ef-870a-f43feacbbb5b',
	// 'arn:aws:ecs:us-west-1:123456789123:task/my-cluster/task-id/23ebb8ac-c18f-46c6-8bbe-d55d0e37cfbd'
	AWSECSTaskARNKey = attribute.Key("aws.ecs.task.arn")

	// AWSECSTaskFamilyKey is the attribute Key conforming to the
	// "aws.ecs.task.family" semantic conventions. It represents the family
	// name of the [ECS task
	// definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)
	// used to create the ECS task.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry-family'
	AWSECSTaskFamilyKey = attribute.Key("aws.ecs.task.family")

	// AWSECSTaskRevisionKey is the attribute Key conforming to the
	// "aws.ecs.task.revision" semantic conventions. It represents the revision
	// for the task definition used to create the ECS task.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '8', '26'
	AWSECSTaskRevisionKey = attribute.Key("aws.ecs.task.revision")
)

Attributes for AWS Elastic Container Service (ECS).

View Source
const (
	// AWSLogGroupARNsKey is the attribute Key conforming to the
	// "aws.log.group.arns" semantic conventions. It represents the Amazon
	// Resource Name(s) (ARN) of the AWS log group(s).
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'arn:aws:logs:us-west-1:123456789012:log-group:/aws/my/group:*'
	// Note: See the [log group ARN format
	// documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html#CWL_ARN_Format).
	AWSLogGroupARNsKey = attribute.Key("aws.log.group.arns")

	// AWSLogGroupNamesKey is the attribute Key conforming to the
	// "aws.log.group.names" semantic conventions. It represents the name(s) of
	// the AWS log group(s) an application is writing to.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/aws/lambda/my-function', 'opentelemetry-service'
	// Note: Multiple log groups must be supported for cases like
	// multi-container applications, where a single application has sidecar
	// containers, and each write to their own log group.
	AWSLogGroupNamesKey = attribute.Key("aws.log.group.names")

	// AWSLogStreamARNsKey is the attribute Key conforming to the
	// "aws.log.stream.arns" semantic conventions. It represents the ARN(s) of
	// the AWS log stream(s).
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'arn:aws:logs:us-west-1:123456789012:log-group:/aws/my/group:log-stream:logs/main/10838bed-421f-43ef-870a-f43feacbbb5b'
	// Note: See the [log stream ARN format
	// documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html#CWL_ARN_Format).
	// One log group can contain several log streams, so these ARNs necessarily
	// identify both a log group and a log stream.
	AWSLogStreamARNsKey = attribute.Key("aws.log.stream.arns")

	// AWSLogStreamNamesKey is the attribute Key conforming to the
	// "aws.log.stream.names" semantic conventions. It represents the name(s)
	// of the AWS log stream(s) an application is writing to.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'logs/main/10838bed-421f-43ef-870a-f43feacbbb5b'
	AWSLogStreamNamesKey = attribute.Key("aws.log.stream.names")
)

Attributes for AWS Logs.

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
	// Stability: experimental
	// Examples: 'some-bucket-name'
	// Note: The `bucket` attribute is applicable to all S3 operations that
	// reference a bucket, i.e. that require the bucket name as a mandatory
	// parameter.
	// This applies to almost all S3 operations except `list-buckets`.
	AWSS3BucketKey = attribute.Key("aws.s3.bucket")

	// AWSS3CopySourceKey is the attribute Key conforming to the
	// "aws.s3.copy_source" semantic conventions. It represents the source
	// object (in the form `bucket`/`key`) for the copy operation.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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

	// AWSS3DeleteKey is the attribute Key conforming to the "aws.s3.delete"
	// semantic conventions. It represents the delete request container that
	// specifies the objects to be deleted.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'Objects=[{Key=string,VersionID=string},{Key=string,VersionID=string}],Quiet=boolean'
	// Note: The `delete` attribute is only applicable to the
	// [delete-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html)
	// operation.
	// The `delete` attribute corresponds to the `--delete` parameter of the
	// [delete-objects operation within the S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-objects.html).
	AWSS3DeleteKey = attribute.Key("aws.s3.delete")

	// AWSS3KeyKey is the attribute Key conforming to the "aws.s3.key" semantic
	// conventions. It represents the S3 object key the request refers to.
	// Corresponds to the `--key` parameter of the [S3
	// API](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)
	// operations.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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

	// AWSS3PartNumberKey is the attribute Key conforming to the
	// "aws.s3.part_number" semantic conventions. It represents the part number
	// of the part being uploaded in a multipart-upload operation. This is a
	// positive integer between 1 and 10,000.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
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

	// AWSS3UploadIDKey is the attribute Key conforming to the
	// "aws.s3.upload_id" semantic conventions. It represents the upload ID
	// that identifies the multipart upload.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
)

Attributes for AWS S3.

View Source
const (
	// BrowserBrandsKey is the attribute Key conforming to the "browser.brands"
	// semantic conventions. It represents the array of brand name and version
	// separated by a space
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: ' Not A;Brand 99', 'Chromium 99', 'Chrome 99'
	// Note: This value is intended to be taken from the [UA client hints
	// API](https://wicg.github.io/ua-client-hints/#interface)
	// (`navigator.userAgentData.brands`).
	BrowserBrandsKey = attribute.Key("browser.brands")

	// BrowserLanguageKey is the attribute Key conforming to the
	// "browser.language" semantic conventions. It represents the preferred
	// language of the user using the browser
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'en', 'en-US', 'fr', 'fr-FR'
	// Note: This value is intended to be taken from the Navigator API
	// `navigator.language`.
	BrowserLanguageKey = attribute.Key("browser.language")

	// BrowserMobileKey is the attribute Key conforming to the "browser.mobile"
	// semantic conventions. It represents a boolean that is true if the
	// browser is running on a mobile device
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: This value is intended to be taken from the [UA client hints
	// API](https://wicg.github.io/ua-client-hints/#interface)
	// (`navigator.userAgentData.mobile`). If unavailable, this attribute
	// SHOULD be left unset.
	BrowserMobileKey = attribute.Key("browser.mobile")

	// BrowserPlatformKey is the attribute Key conforming to the
	// "browser.platform" semantic conventions. It represents the platform on
	// which the browser is running
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
)

The web browser attributes

View Source
const (
	// ClientAddressKey is the attribute Key conforming to the "client.address"
	// semantic conventions. It represents the client address - domain name if
	// available without reverse DNS lookup; otherwise, IP address or Unix
	// domain socket name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'client.example.com', '10.1.2.80', '/tmp/my.sock'
	// Note: When observed from the server side, and when communicating through
	// an intermediary, `client.address` SHOULD represent the client address
	// behind any intermediaries,  for example proxies, if it's available.
	ClientAddressKey = attribute.Key("client.address")

	// ClientPortKey is the attribute Key conforming to the "client.port"
	// semantic conventions. It represents the client port number.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 65123
	// Note: When observed from the server side, and when communicating through
	// an intermediary, `client.port` SHOULD represent the client port behind
	// any intermediaries,  for example proxies, if it's available.
	ClientPortKey = attribute.Key("client.port")
)

These attributes may be used to describe the client in a connection-based network interaction where there is one side that initiates the connection (the client is the side that initiates the connection). This covers all TCP network interactions since TCP is connection-based and one side initiates the connection (an exception is made for peer-to-peer communication over TCP where the "user-facing" surface of the protocol / API doesn't expose a clear notion of client and server). This also covers UDP network interactions where one side initiates the interaction, e.g. QUIC (HTTP/3) and DNS.

View Source
const (
	// CloudAccountIDKey is the attribute Key conforming to the
	// "cloud.account.id" semantic conventions. It represents the cloud account
	// ID the resource is assigned to.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '111111111111', 'opentelemetry'
	CloudAccountIDKey = attribute.Key("cloud.account.id")

	// CloudAvailabilityZoneKey is the attribute Key conforming to the
	// "cloud.availability_zone" semantic conventions. It represents the cloud
	// regions often have multiple, isolated locations known as zones to
	// increase availability. Availability zone represents the zone where the
	// resource is running.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'us-east-1c'
	// Note: Availability zones are called "zones" on Alibaba Cloud and Google
	// Cloud.
	CloudAvailabilityZoneKey = attribute.Key("cloud.availability_zone")

	// CloudPlatformKey is the attribute Key conforming to the "cloud.platform"
	// semantic conventions. It represents the cloud platform in use.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: The prefix of the service SHOULD match the one specified in
	// `cloud.provider`.
	CloudPlatformKey = attribute.Key("cloud.platform")

	// CloudProviderKey is the attribute Key conforming to the "cloud.provider"
	// semantic conventions. It represents the name of the cloud provider.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	CloudProviderKey = attribute.Key("cloud.provider")

	// CloudRegionKey is the attribute Key conforming to the "cloud.region"
	// semantic conventions. It represents the geographical region the resource
	// is running.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'us-central1', 'us-east-1'
	// Note: Refer to your provider's docs to see the available regions, for
	// example [Alibaba Cloud
	// regions](https://www.alibabacloud.com/help/doc-detail/40654.htm), [AWS
	// regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/),
	// [Azure
	// regions](https://azure.microsoft.com/global-infrastructure/geographies/),
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
	// ID](https://learn.microsoft.com/rest/api/resources/resources/get-by-id)
	// on Azure, a [full resource
	// name](https://cloud.google.com/apis/design/resource_names#full_resource_name)
	// on GCP)
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
	// ID](https://docs.microsoft.com/rest/api/resources/resources/get-by-id)
	// of the invoked function,
	//   *not* the function app, having the form
	// `/subscriptions/<SUBSCIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>`.
	//   This means that a span attribute MUST be used, as an Azure function
	// app can host multiple functions that would usually share
	//   a TracerProvider.
	CloudResourceIDKey = attribute.Key("cloud.resource_id")
)

A cloud environment (e.g. GCP, Azure, AWS).

View Source
const (
	// CloudeventsEventIDKey is the attribute Key conforming to the
	// "cloudevents.event_id" semantic conventions. It represents the
	// [event_id](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#id)
	// uniquely identifies the event.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '123e4567-e89b-12d3-a456-426614174000', '0001'
	CloudeventsEventIDKey = attribute.Key("cloudevents.event_id")

	// CloudeventsEventSourceKey is the attribute Key conforming to the
	// "cloudevents.event_source" semantic conventions. It represents the
	// [source](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#source-1)
	// identifies the context in which an event happened.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
	// Stability: experimental
	// Examples: '1.0'
	CloudeventsEventSpecVersionKey = attribute.Key("cloudevents.event_spec_version")

	// CloudeventsEventSubjectKey is the attribute Key conforming to the
	// "cloudevents.event_subject" semantic conventions. It represents the
	// [subject](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#subject)
	// of the event in the context of the event producer (identified by
	// source).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'mynewfile.jpg'
	CloudeventsEventSubjectKey = attribute.Key("cloudevents.event_subject")

	// CloudeventsEventTypeKey is the attribute Key conforming to the
	// "cloudevents.event_type" semantic conventions. It represents the
	// [event_type](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#type)
	// contains a value describing the type of event related to the originating
	// occurrence.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'com.github.pull_request.opened',
	// 'com.example.object.deleted.v2'
	CloudeventsEventTypeKey = attribute.Key("cloudevents.event_type")
)

Attributes for CloudEvents.

View Source
const (
	// CodeColumnKey is the attribute Key conforming to the "code.column"
	// semantic conventions. It represents the column number in `code.filepath`
	// best representing the operation. It SHOULD point within the code unit
	// named in `code.function`.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 16
	CodeColumnKey = attribute.Key("code.column")

	// CodeFilepathKey is the attribute Key conforming to the "code.filepath"
	// semantic conventions. It represents the source code file name that
	// identifies the code unit as uniquely as possible (preferably an absolute
	// file path).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/usr/local/MyApplication/content_root/app/index.php'
	CodeFilepathKey = attribute.Key("code.filepath")

	// CodeFunctionKey is the attribute Key conforming to the "code.function"
	// semantic conventions. It represents the method or function name, or
	// equivalent (usually rightmost part of the code unit's name).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'serveRequest'
	CodeFunctionKey = attribute.Key("code.function")

	// CodeLineNumberKey is the attribute Key conforming to the "code.lineno"
	// semantic conventions. It represents the line number in `code.filepath`
	// best representing the operation. It SHOULD point within the code unit
	// named in `code.function`.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 42
	CodeLineNumberKey = attribute.Key("code.lineno")

	// CodeNamespaceKey is the attribute Key conforming to the "code.namespace"
	// semantic conventions. It represents the "namespace" within which
	// `code.function` is defined. Usually the qualified class or module name,
	// such that `code.namespace` + some separator + `code.function` form a
	// unique identifier for the code unit.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'com.example.MyHTTPService'
	CodeNamespaceKey = attribute.Key("code.namespace")

	// CodeStacktraceKey is the attribute Key conforming to the
	// "code.stacktrace" semantic conventions. It represents a stacktrace as a
	// string in the natural representation for the language runtime. The
	// representation is to be determined and documented by each language SIG.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'at
	// com.example.GenerateTrace.methodB(GenerateTrace.java:13)\\n at '
	//  'com.example.GenerateTrace.methodA(GenerateTrace.java:9)\\n at '
	//  'com.example.GenerateTrace.main(GenerateTrace.java:5)'
	CodeStacktraceKey = attribute.Key("code.stacktrace")
)

These attributes allow to report this unit of code and therefore to provide more context about the span.

View Source
const (
	// ContainerCommandKey is the attribute Key conforming to the
	// "container.command" semantic conventions. It represents the command used
	// to run the container (i.e. the command name).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'otelcontribcol'
	// Note: If using embedded credentials or sensitive data, it is recommended
	// to remove them to prevent potential leakage.
	ContainerCommandKey = attribute.Key("container.command")

	// ContainerCommandArgsKey is the attribute Key conforming to the
	// "container.command_args" semantic conventions. It represents the all the
	// command arguments (including the command/executable itself) run by the
	// container. [2]
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'otelcontribcol, --config, config.yaml'
	ContainerCommandArgsKey = attribute.Key("container.command_args")

	// ContainerCommandLineKey is the attribute Key conforming to the
	// "container.command_line" semantic conventions. It represents the full
	// command run by the container as a single string representing the full
	// command. [2]
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'otelcontribcol --config config.yaml'
	ContainerCommandLineKey = attribute.Key("container.command_line")

	// ContainerCPUStateKey is the attribute Key conforming to the
	// "container.cpu.state" semantic conventions. It represents the CPU state
	// for this data point.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'user', 'kernel'
	ContainerCPUStateKey = attribute.Key("container.cpu.state")

	// ContainerIDKey is the attribute Key conforming to the "container.id"
	// semantic conventions. It represents the container ID. Usually a UUID, as
	// for example used to [identify Docker
	// containers](https://docs.docker.com/engine/reference/run/#container-identification).
	// The UUID might be abbreviated.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'a3bf90e006b2'
	ContainerIDKey = attribute.Key("container.id")

	// ContainerImageIDKey is the attribute Key conforming to the
	// "container.image.id" semantic conventions. It represents the runtime
	// specific image identifier. Usually a hash algorithm followed by a UUID.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'sha256:19c92d0a00d1b66d897bceaa7319bee0dd38a10a851c60bcec9474aa3f01e50f'
	// Note: Docker defines a sha256 of the image id; `container.image.id`
	// corresponds to the `Image` field from the Docker container inspect
	// [API](https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerInspect)
	// endpoint.
	// K8S defines a link to the container registry repository with digest
	// `"imageID": "registry.azurecr.io
	// /namespace/service/dockerfile@sha256:bdeabd40c3a8a492eaf9e8e44d0ebbb84bac7ee25ac0cf8a7159d25f62555625"`.
	// The ID is assigned by the container runtime and can vary in different
	// environments. Consider using `oci.manifest.digest` if it is important to
	// identify the same image in different environments/runtimes.
	ContainerImageIDKey = attribute.Key("container.image.id")

	// ContainerImageNameKey is the attribute Key conforming to the
	// "container.image.name" semantic conventions. It represents the name of
	// the image the container was built on.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'gcr.io/opentelemetry/operator'
	ContainerImageNameKey = attribute.Key("container.image.name")

	// ContainerImageRepoDigestsKey is the attribute Key conforming to the
	// "container.image.repo_digests" semantic conventions. It represents the
	// repo digests of the container image as provided by the container
	// runtime.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'example@sha256:afcc7f1ac1b49db317a7196c902e61c6c3c4607d63599ee1a82d702d249a0ccb',
	// 'internal.registry.example.com:5000/example@sha256:b69959407d21e8a062e0416bf13405bb2b71ed7a84dde4158ebafacfa06f5578'
	// Note:
	// [Docker](https://docs.docker.com/engine/api/v1.43/#tag/Image/operation/ImageInspect)
	// and
	// [CRI](https://github.com/kubernetes/cri-api/blob/c75ef5b473bbe2d0a4fc92f82235efd665ea8e9f/pkg/apis/runtime/v1/api.proto#L1237-L1238)
	// report those under the `RepoDigests` field.
	ContainerImageRepoDigestsKey = attribute.Key("container.image.repo_digests")

	// ContainerImageTagsKey is the attribute Key conforming to the
	// "container.image.tags" semantic conventions. It represents the container
	// image tags. An example can be found in [Docker Image
	// Inspect](https://docs.docker.com/engine/api/v1.43/#tag/Image/operation/ImageInspect).
	// Should be only the `<tag>` section of the full name for example from
	// `registry.example.com/my-org/my-image:<tag>`.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'v1.27.1', '3.5.7-0'
	ContainerImageTagsKey = attribute.Key("container.image.tags")

	// ContainerNameKey is the attribute Key conforming to the "container.name"
	// semantic conventions. It represents the container name used by container
	// runtime.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry-autoconf'
	ContainerNameKey = attribute.Key("container.name")

	// ContainerRuntimeKey is the attribute Key conforming to the
	// "container.runtime" semantic conventions. It represents the container
	// runtime managing this container.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'docker', 'containerd', 'rkt'
	ContainerRuntimeKey = attribute.Key("container.runtime")
)

A container instance.

View Source
const (
	// DBClientConnectionsPoolNameKey is the attribute Key conforming to the
	// "db.client.connections.pool.name" semantic conventions. It represents
	// the name of the connection pool; unique within the instrumented
	// application. In case the connection pool implementation doesn't provide
	// a name, instrumentation should use a combination of `server.address` and
	// `server.port` attributes formatted as `server.address:server.port`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myDataSource'
	DBClientConnectionsPoolNameKey = attribute.Key("db.client.connections.pool.name")

	// DBClientConnectionsStateKey is the attribute Key conforming to the
	// "db.client.connections.state" semantic conventions. It represents the
	// state of a connection in the pool
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'idle'
	DBClientConnectionsStateKey = attribute.Key("db.client.connections.state")

	// DBCollectionNameKey is the attribute Key conforming to the
	// "db.collection.name" semantic conventions. It represents the name of a
	// collection (table, container) within the database.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'public.users', 'customers'
	// Note: If the collection name is parsed from the query, it SHOULD match
	// the value provided in the query and may be qualified with the schema and
	// database name.
	// It is RECOMMENDED to capture the value as provided by the application
	// without attempting to do any case normalization.
	DBCollectionNameKey = attribute.Key("db.collection.name")

	// DBNamespaceKey is the attribute Key conforming to the "db.namespace"
	// semantic conventions. It represents the name of the database, fully
	// qualified within the server address and port.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'customers', 'test.users'
	// Note: If a database system has multiple namespace components, they
	// SHOULD be concatenated (potentially using database system specific
	// conventions) from most general to most specific namespace component, and
	// more specific namespaces SHOULD NOT be captured without the more general
	// namespaces, to ensure that "startswith" queries for the more general
	// namespaces will be valid.
	// Semantic conventions for individual database systems SHOULD document
	// what `db.namespace` means in the context of that system.
	// It is RECOMMENDED to capture the value as provided by the application
	// without attempting to do any case normalization.
	DBNamespaceKey = attribute.Key("db.namespace")

	// DBOperationNameKey is the attribute Key conforming to the
	// "db.operation.name" semantic conventions. It represents the name of the
	// operation or command being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'findAndModify', 'HMSET', 'SELECT'
	// Note: It is RECOMMENDED to capture the value as provided by the
	// application without attempting to do any case normalization.
	DBOperationNameKey = attribute.Key("db.operation.name")

	// DBQueryTextKey is the attribute Key conforming to the "db.query.text"
	// semantic conventions. It represents the database query being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'SELECT * FROM wuser_table where username = ?', 'SET mykey
	// "WuValue"'
	DBQueryTextKey = attribute.Key("db.query.text")

	// DBSystemKey is the attribute Key conforming to the "db.system" semantic
	// conventions. It represents the database management system (DBMS) product
	// as identified by the client instrumentation.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: The actual DBMS may differ from the one identified by the client.
	// For example, when using PostgreSQL client libraries to connect to a
	// CockroachDB, the `db.system` is set to `postgresql` based on the
	// instrumentation's best knowledge.
	DBSystemKey = attribute.Key("db.system")
)

This group defines the attributes used to describe telemetry in the context of databases.

View Source
const (
	// DBCassandraConsistencyLevelKey is the attribute Key conforming to the
	// "db.cassandra.consistency_level" semantic conventions. It represents the
	// consistency level of the query. Based on consistency values from
	// [CQL](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/dml/dmlConfigConsistency.html).
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	DBCassandraConsistencyLevelKey = attribute.Key("db.cassandra.consistency_level")

	// DBCassandraCoordinatorDCKey is the attribute Key conforming to the
	// "db.cassandra.coordinator.dc" semantic conventions. It represents the
	// data center of the coordinating node for a query.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'us-west-2'
	DBCassandraCoordinatorDCKey = attribute.Key("db.cassandra.coordinator.dc")

	// DBCassandraCoordinatorIDKey is the attribute Key conforming to the
	// "db.cassandra.coordinator.id" semantic conventions. It represents the ID
	// of the coordinating node for a query.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'be13faa2-8574-4d71-926d-27f16cf8a7af'
	DBCassandraCoordinatorIDKey = attribute.Key("db.cassandra.coordinator.id")

	// DBCassandraIdempotenceKey is the attribute Key conforming to the
	// "db.cassandra.idempotence" semantic conventions. It represents the
	// whether or not the query is idempotent.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	DBCassandraIdempotenceKey = attribute.Key("db.cassandra.idempotence")

	// DBCassandraPageSizeKey is the attribute Key conforming to the
	// "db.cassandra.page_size" semantic conventions. It represents the fetch
	// size used for paging, i.e. how many rows will be returned at once.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 5000
	DBCassandraPageSizeKey = attribute.Key("db.cassandra.page_size")

	// DBCassandraSpeculativeExecutionCountKey is the attribute Key conforming
	// to the "db.cassandra.speculative_execution_count" semantic conventions.
	// It represents the number of times a query was speculatively executed.
	// Not set or `0` if the query was not executed speculatively.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 0, 2
	DBCassandraSpeculativeExecutionCountKey = attribute.Key("db.cassandra.speculative_execution_count")
)

This group defines attributes for Cassandra.

View Source
const (
	// DBCosmosDBClientIDKey is the attribute Key conforming to the
	// "db.cosmosdb.client_id" semantic conventions. It represents the unique
	// Cosmos client instance id.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '3ba4827d-4422-483f-b59f-85b74211c11d'
	DBCosmosDBClientIDKey = attribute.Key("db.cosmosdb.client_id")

	// DBCosmosDBConnectionModeKey is the attribute Key conforming to the
	// "db.cosmosdb.connection_mode" semantic conventions. It represents the
	// cosmos client connection mode.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	DBCosmosDBConnectionModeKey = attribute.Key("db.cosmosdb.connection_mode")

	// DBCosmosDBOperationTypeKey is the attribute Key conforming to the
	// "db.cosmosdb.operation_type" semantic conventions. It represents the
	// cosmosDB Operation Type.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	DBCosmosDBOperationTypeKey = attribute.Key("db.cosmosdb.operation_type")

	// DBCosmosDBRequestChargeKey is the attribute Key conforming to the
	// "db.cosmosdb.request_charge" semantic conventions. It represents the rU
	// consumed for that operation
	//
	// Type: double
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 46.18, 1.0
	DBCosmosDBRequestChargeKey = attribute.Key("db.cosmosdb.request_charge")

	// DBCosmosDBRequestContentLengthKey is the attribute Key conforming to the
	// "db.cosmosdb.request_content_length" semantic conventions. It represents
	// the request payload size in bytes
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	DBCosmosDBRequestContentLengthKey = attribute.Key("db.cosmosdb.request_content_length")

	// DBCosmosDBStatusCodeKey is the attribute Key conforming to the
	// "db.cosmosdb.status_code" semantic conventions. It represents the cosmos
	// DB status code.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 200, 201
	DBCosmosDBStatusCodeKey = attribute.Key("db.cosmosdb.status_code")

	// DBCosmosDBSubStatusCodeKey is the attribute Key conforming to the
	// "db.cosmosdb.sub_status_code" semantic conventions. It represents the
	// cosmos DB sub status code.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1000, 1002
	DBCosmosDBSubStatusCodeKey = attribute.Key("db.cosmosdb.sub_status_code")
)

This group defines attributes for Azure Cosmos DB.

View Source
const (
	// DBElasticsearchClusterNameKey is the attribute Key conforming to the
	// "db.elasticsearch.cluster.name" semantic conventions. It represents the
	// represents the identifier of an Elasticsearch cluster.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'e9106fc68e3044f0b1475b04bf4ffd5f'
	DBElasticsearchClusterNameKey = attribute.Key("db.elasticsearch.cluster.name")

	// DBElasticsearchNodeNameKey is the attribute Key conforming to the
	// "db.elasticsearch.node.name" semantic conventions. It represents the
	// represents the human-readable identifier of the node/instance to which a
	// request was routed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'instance-0000000001'
	DBElasticsearchNodeNameKey = attribute.Key("db.elasticsearch.node.name")
)

This group defines attributes for Elasticsearch.

View Source
const (
	// DestinationAddressKey is the attribute Key conforming to the
	// "destination.address" semantic conventions. It represents the
	// destination address - domain name if available without reverse DNS
	// lookup; otherwise, IP address or Unix domain socket name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'destination.example.com', '10.1.2.80', '/tmp/my.sock'
	// Note: When observed from the source side, and when communicating through
	// an intermediary, `destination.address` SHOULD represent the destination
	// address behind any intermediaries, for example proxies, if it's
	// available.
	DestinationAddressKey = attribute.Key("destination.address")

	// DestinationPortKey is the attribute Key conforming to the
	// "destination.port" semantic conventions. It represents the destination
	// port number
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 3389, 2888
	DestinationPortKey = attribute.Key("destination.port")
)

These attributes may be used to describe the receiver of a network exchange/packet. These should be used when there is no client/server relationship between the two sides, or when that relationship is unknown. This covers low-level network interactions (e.g. packet tracing) where you don't know if there was a connection or which side initiated it. This also covers unidirectional UDP flows and peer-to-peer communication where the "user-facing" surface of the protocol / API doesn't expose a clear notion of client and server.

View Source
const (
	// DeviceIDKey is the attribute Key conforming to the "device.id" semantic
	// conventions. It represents a unique identifier representing the device
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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

	// DeviceManufacturerKey is the attribute Key conforming to the
	// "device.manufacturer" semantic conventions. It represents the name of
	// the device manufacturer
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Apple', 'Samsung'
	// Note: The Android OS provides this field via
	// [Build](https://developer.android.com/reference/android/os/Build#MANUFACTURER).
	// iOS apps SHOULD hardcode the value `Apple`.
	DeviceManufacturerKey = attribute.Key("device.manufacturer")

	// DeviceModelIdentifierKey is the attribute Key conforming to the
	// "device.model.identifier" semantic conventions. It represents the model
	// identifier for the device
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'iPhone3,4', 'SM-G920F'
	// Note: It's recommended this value represents a machine-readable version
	// of the model identifier rather than the market or consumer-friendly name
	// of the device.
	DeviceModelIdentifierKey = attribute.Key("device.model.identifier")

	// DeviceModelNameKey is the attribute Key conforming to the
	// "device.model.name" semantic conventions. It represents the marketing
	// name for the device model
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'iPhone 6s Plus', 'Samsung Galaxy S6'
	// Note: It's recommended this value represents a human-readable version of
	// the device model rather than a machine-readable alternative.
	DeviceModelNameKey = attribute.Key("device.model.name")
)

Describes device attributes.

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
	// Stability: experimental
	// Examples: 'username'
	EnduserIDKey = attribute.Key("enduser.id")

	// EnduserRoleKey is the attribute Key conforming to the "enduser.role"
	// semantic conventions. It represents the actual/assumed role the client
	// is making the request under extracted from token or application security
	// context.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
	// Stability: experimental
	// Examples: 'read:message, write:files'
	EnduserScopeKey = attribute.Key("enduser.scope")
)

Attributes for operations with an authenticated and/or authorized enduser.

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
	// as done in the [example for recording span
	// exceptions](https://opentelemetry.io/docs/specs/semconv/exceptions/exceptions-spans/#recording-an-exception).
	//
	// It follows that an exception may still escape the scope of the span
	// even if the `exception.escaped` attribute was not set or set to false,
	// since the event might have been recorded at a time where it was not
	// clear whether the exception will escape.
	ExceptionEscapedKey = attribute.Key("exception.escaped")

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
)

The shared attributes used to report a single exception associated with a span or log.

View Source
const (
	// FaaSColdstartKey is the attribute Key conforming to the "faas.coldstart"
	// semantic conventions. It represents a boolean that is true if the
	// serverless function is executed for the first time (aka cold-start).
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	FaaSColdstartKey = attribute.Key("faas.coldstart")

	// FaaSCronKey is the attribute Key conforming to the "faas.cron" semantic
	// conventions. It represents a string containing the schedule period as
	// [Cron
	// Expression](https://docs.oracle.com/cd/E12058_01/doc/doc.1014/e12030/cron_expressions.htm).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '0/5 * * * ? *'
	FaaSCronKey = attribute.Key("faas.cron")

	// FaaSDocumentCollectionKey is the attribute Key conforming to the
	// "faas.document.collection" semantic conventions. It represents the name
	// of the source on which the triggering operation was performed. For
	// example, in Cloud Storage or S3 corresponds to the bucket name, and in
	// Cosmos DB to the database name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myBucketName', 'myDBName'
	FaaSDocumentCollectionKey = attribute.Key("faas.document.collection")

	// FaaSDocumentNameKey is the attribute Key conforming to the
	// "faas.document.name" semantic conventions. It represents the document
	// name/table subjected to the operation. For example, in Cloud Storage or
	// S3 is the name of the file, and in Cosmos DB the table name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myFile.txt', 'myTableName'
	FaaSDocumentNameKey = attribute.Key("faas.document.name")

	// FaaSDocumentOperationKey is the attribute Key conforming to the
	// "faas.document.operation" semantic conventions. It represents the
	// describes the type of the operation that was performed on the data.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	FaaSDocumentOperationKey = attribute.Key("faas.document.operation")

	// FaaSDocumentTimeKey is the attribute Key conforming to the
	// "faas.document.time" semantic conventions. It represents a string
	// containing the time when the data was accessed in the [ISO
	// 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format
	// expressed in [UTC](https://www.w3.org/TR/NOTE-datetime).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2020-01-23T13:47:06Z'
	FaaSDocumentTimeKey = attribute.Key("faas.document.time")

	// FaaSInstanceKey is the attribute Key conforming to the "faas.instance"
	// semantic conventions. It represents the execution environment ID as a
	// string, that will be potentially reused for other invocations to the
	// same function/function version.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2021/06/28/[$LATEST]2f399eb14537447da05ab2a2e39309de'
	// Note: * **AWS Lambda:** Use the (full) log stream name.
	FaaSInstanceKey = attribute.Key("faas.instance")

	// FaaSInvocationIDKey is the attribute Key conforming to the
	// "faas.invocation_id" semantic conventions. It represents the invocation
	// ID of the current function invocation.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'af9d5aa4-a685-4c5f-a22b-444f80b3cc28'
	FaaSInvocationIDKey = attribute.Key("faas.invocation_id")

	// FaaSInvokedNameKey is the attribute Key conforming to the
	// "faas.invoked_name" semantic conventions. It represents the name of the
	// invoked function.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'my-function'
	// Note: SHOULD be equal to the `faas.name` resource attribute of the
	// invoked function.
	FaaSInvokedNameKey = attribute.Key("faas.invoked_name")

	// FaaSInvokedProviderKey is the attribute Key conforming to the
	// "faas.invoked_provider" semantic conventions. It represents the cloud
	// provider of the invoked function.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: SHOULD be equal to the `cloud.provider` resource attribute of the
	// invoked function.
	FaaSInvokedProviderKey = attribute.Key("faas.invoked_provider")

	// FaaSInvokedRegionKey is the attribute Key conforming to the
	// "faas.invoked_region" semantic conventions. It represents the cloud
	// region of the invoked function.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'eu-central-1'
	// Note: SHOULD be equal to the `cloud.region` resource attribute of the
	// invoked function.
	FaaSInvokedRegionKey = attribute.Key("faas.invoked_region")

	// FaaSMaxMemoryKey is the attribute Key conforming to the
	// "faas.max_memory" semantic conventions. It represents the amount of
	// memory available to the serverless function converted to Bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 134217728
	// Note: It's recommended to set this attribute since e.g. too little
	// memory can easily stop a Java AWS Lambda function from working
	// correctly. On AWS Lambda, the environment variable
	// `AWS_LAMBDA_FUNCTION_MEMORY_SIZE` provides this information (which must
	// be multiplied by 1,048,576).
	FaaSMaxMemoryKey = attribute.Key("faas.max_memory")

	// FaaSNameKey is the attribute Key conforming to the "faas.name" semantic
	// conventions. It represents the name of the single function that this
	// runtime instance executes.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'my-function', 'myazurefunctionapp/some-function-name'
	// Note: This is the name of the function as configured/deployed on the
	// FaaS
	// platform and is usually different from the name of the callback
	// function (which may be stored in the
	// [`code.namespace`/`code.function`](/docs/general/attributes.md#source-code-attributes)
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

	// FaaSTimeKey is the attribute Key conforming to the "faas.time" semantic
	// conventions. It represents a string containing the function invocation
	// time in the [ISO
	// 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format
	// expressed in [UTC](https://www.w3.org/TR/NOTE-datetime).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2020-01-23T13:47:06Z'
	FaaSTimeKey = attribute.Key("faas.time")

	// FaaSTriggerKey is the attribute Key conforming to the "faas.trigger"
	// semantic conventions. It represents the type of the trigger which caused
	// this function invocation.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	FaaSTriggerKey = attribute.Key("faas.trigger")

	// FaaSVersionKey is the attribute Key conforming to the "faas.version"
	// semantic conventions. It represents the immutable version of the
	// function being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
)

FaaS attributes

View Source
const (
	// FeatureFlagKeyKey is the attribute Key conforming to the
	// "feature_flag.key" semantic conventions. It represents the unique
	// identifier of the feature flag.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'logo-color'
	FeatureFlagKeyKey = attribute.Key("feature_flag.key")

	// FeatureFlagProviderNameKey is the attribute Key conforming to the
	// "feature_flag.provider_name" semantic conventions. It represents the
	// name of the service provider that performs the flag evaluation.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Flag Manager'
	FeatureFlagProviderNameKey = attribute.Key("feature_flag.provider_name")

	// FeatureFlagVariantKey is the attribute Key conforming to the
	// "feature_flag.variant" semantic conventions. It represents the sHOULD be
	// a semantic identifier for a value. If one is unavailable, a stringified
	// version of the value can be used.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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

Attributes for Feature Flags.

View Source
const (
	// FileDirectoryKey is the attribute Key conforming to the "file.directory"
	// semantic conventions. It represents the directory where the file is
	// located. It should include the drive letter, when appropriate.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/home/user', 'C:\\Program Files\\MyApp'
	FileDirectoryKey = attribute.Key("file.directory")

	// FileExtensionKey is the attribute Key conforming to the "file.extension"
	// semantic conventions. It represents the file extension, excluding the
	// leading dot.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'png', 'gz'
	// Note: When the file name has multiple extensions (example.tar.gz), only
	// the last one should be captured ("gz", not "tar.gz").
	FileExtensionKey = attribute.Key("file.extension")

	// FileNameKey is the attribute Key conforming to the "file.name" semantic
	// conventions. It represents the name of the file including the extension,
	// without the directory.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'example.png'
	FileNameKey = attribute.Key("file.name")

	// FilePathKey is the attribute Key conforming to the "file.path" semantic
	// conventions. It represents the full path to the file, including the file
	// name. It should include the drive letter, when appropriate.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/home/alice/example.png', 'C:\\Program
	// Files\\MyApp\\myapp.exe'
	FilePathKey = attribute.Key("file.path")

	// FileSizeKey is the attribute Key conforming to the "file.size" semantic
	// conventions. It represents the file size in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	FileSizeKey = attribute.Key("file.size")
)

Describes file attributes.

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
	// Stability: experimental
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
	// Stability: experimental
	// Examples: 0, 1
	GCPCloudRunJobTaskIndexKey = attribute.Key("gcp.cloud_run.job.task_index")
)

Attributes for Google Cloud Run.

View Source
const (
	// GCPGceInstanceHostnameKey is the attribute Key conforming to the
	// "gcp.gce.instance.hostname" semantic conventions. It represents the
	// hostname of a GCE instance. This is the full value of the default or
	// [custom
	// hostname](https://cloud.google.com/compute/docs/instances/custom-hostname-vm).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'my-host1234.example.com',
	// 'sample-vm.us-west1-b.c.my-project.internal'
	GCPGceInstanceHostnameKey = attribute.Key("gcp.gce.instance.hostname")

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
	// Stability: experimental
	// Examples: 'instance-1', 'my-vm-name'
	GCPGceInstanceNameKey = attribute.Key("gcp.gce.instance.name")
)

Attributes for Google Compute Engine (GCE).

View Source
const (
	// GenAiCompletionKey is the attribute Key conforming to the
	// "gen_ai.completion" semantic conventions. It represents the full
	// response received from the LLM.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: "[{'role': 'assistant', 'content': 'The capital of France is
	// Paris.'}]"
	// Note: It's RECOMMENDED to format completions as JSON string matching
	// [OpenAI messages
	// format](https://platform.openai.com/docs/guides/text-generation)
	GenAiCompletionKey = attribute.Key("gen_ai.completion")

	// GenAiPromptKey is the attribute Key conforming to the "gen_ai.prompt"
	// semantic conventions. It represents the full prompt sent to an LLM.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: "[{'role': 'user', 'content': 'What is the capital of
	// France?'}]"
	// Note: It's RECOMMENDED to format prompts as JSON string matching [OpenAI
	// messages
	// format](https://platform.openai.com/docs/guides/text-generation)
	GenAiPromptKey = attribute.Key("gen_ai.prompt")

	// GenAiRequestMaxTokensKey is the attribute Key conforming to the
	// "gen_ai.request.max_tokens" semantic conventions. It represents the
	// maximum number of tokens the LLM generates for a request.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 100
	GenAiRequestMaxTokensKey = attribute.Key("gen_ai.request.max_tokens")

	// GenAiRequestModelKey is the attribute Key conforming to the
	// "gen_ai.request.model" semantic conventions. It represents the name of
	// the LLM a request is being made to.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'gpt-4'
	GenAiRequestModelKey = attribute.Key("gen_ai.request.model")

	// GenAiRequestTemperatureKey is the attribute Key conforming to the
	// "gen_ai.request.temperature" semantic conventions. It represents the
	// temperature setting for the LLM request.
	//
	// Type: double
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 0.0
	GenAiRequestTemperatureKey = attribute.Key("gen_ai.request.temperature")

	// GenAiRequestTopPKey is the attribute Key conforming to the
	// "gen_ai.request.top_p" semantic conventions. It represents the top_p
	// sampling setting for the LLM request.
	//
	// Type: double
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1.0
	GenAiRequestTopPKey = attribute.Key("gen_ai.request.top_p")

	// GenAiResponseFinishReasonsKey is the attribute Key conforming to the
	// "gen_ai.response.finish_reasons" semantic conventions. It represents the
	// array of reasons the model stopped generating tokens, corresponding to
	// each generation received.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'stop'
	GenAiResponseFinishReasonsKey = attribute.Key("gen_ai.response.finish_reasons")

	// GenAiResponseIDKey is the attribute Key conforming to the
	// "gen_ai.response.id" semantic conventions. It represents the unique
	// identifier for the completion.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'chatcmpl-123'
	GenAiResponseIDKey = attribute.Key("gen_ai.response.id")

	// GenAiResponseModelKey is the attribute Key conforming to the
	// "gen_ai.response.model" semantic conventions. It represents the name of
	// the LLM a response was generated from.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'gpt-4-0613'
	GenAiResponseModelKey = attribute.Key("gen_ai.response.model")

	// GenAiSystemKey is the attribute Key conforming to the "gen_ai.system"
	// semantic conventions. It represents the Generative AI product as
	// identified by the client instrumentation.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'openai'
	// Note: The actual GenAI product may differ from the one identified by the
	// client. For example, when using OpenAI client libraries to communicate
	// with Mistral, the `gen_ai.system` is set to `openai` based on the
	// instrumentation's best knowledge.
	GenAiSystemKey = attribute.Key("gen_ai.system")

	// GenAiUsageCompletionTokensKey is the attribute Key conforming to the
	// "gen_ai.usage.completion_tokens" semantic conventions. It represents the
	// number of tokens used in the LLM response (completion).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 180
	GenAiUsageCompletionTokensKey = attribute.Key("gen_ai.usage.completion_tokens")

	// GenAiUsagePromptTokensKey is the attribute Key conforming to the
	// "gen_ai.usage.prompt_tokens" semantic conventions. It represents the
	// number of tokens used in the LLM prompt.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 100
	GenAiUsagePromptTokensKey = attribute.Key("gen_ai.usage.prompt_tokens")
)

The attributes used to describe telemetry in the context of LLM (Large Language Models) requests and responses.

View Source
const (
	// GraphqlDocumentKey is the attribute Key conforming to the
	// "graphql.document" semantic conventions. It represents the GraphQL
	// document being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'query findBookByID { bookByID(id: ?) { name } }'
	// Note: The value may be sanitized to exclude sensitive information.
	GraphqlDocumentKey = attribute.Key("graphql.document")

	// GraphqlOperationNameKey is the attribute Key conforming to the
	// "graphql.operation.name" semantic conventions. It represents the name of
	// the operation being executed.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'findBookByID'
	GraphqlOperationNameKey = attribute.Key("graphql.operation.name")

	// GraphqlOperationTypeKey is the attribute Key conforming to the
	// "graphql.operation.type" semantic conventions. It represents the type of
	// the operation being executed.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'query', 'mutation', 'subscription'
	GraphqlOperationTypeKey = attribute.Key("graphql.operation.type")
)

Attributes for GraphQL.

View Source
const (
	// HerokuAppIDKey is the attribute Key conforming to the "heroku.app.id"
	// semantic conventions. It represents the unique identifier for the
	// application
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2daa2797-e42b-4624-9322-ec3f968df4da'
	HerokuAppIDKey = attribute.Key("heroku.app.id")

	// HerokuReleaseCommitKey is the attribute Key conforming to the
	// "heroku.release.commit" semantic conventions. It represents the commit
	// hash for the current release
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'e6134959463efd8966b20e75b913cafe3f5ec'
	HerokuReleaseCommitKey = attribute.Key("heroku.release.commit")

	// HerokuReleaseCreationTimestampKey is the attribute Key conforming to the
	// "heroku.release.creation_timestamp" semantic conventions. It represents
	// the time and date the release was created
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2022-10-23T18:00:42Z'
	HerokuReleaseCreationTimestampKey = attribute.Key("heroku.release.creation_timestamp")
)

Attributes for the Android platform on which the Android application is running.

View Source
const (
	// HostArchKey is the attribute Key conforming to the "host.arch" semantic
	// conventions. It represents the CPU architecture the host system is
	// running on.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	HostArchKey = attribute.Key("host.arch")

	// HostCPUCacheL2SizeKey is the attribute Key conforming to the
	// "host.cpu.cache.l2.size" semantic conventions. It represents the amount
	// of level 2 memory cache available to the processor (in Bytes).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 12288000
	HostCPUCacheL2SizeKey = attribute.Key("host.cpu.cache.l2.size")

	// HostCPUFamilyKey is the attribute Key conforming to the
	// "host.cpu.family" semantic conventions. It represents the family or
	// generation of the CPU.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '6', 'PA-RISC 1.1e'
	HostCPUFamilyKey = attribute.Key("host.cpu.family")

	// HostCPUModelIDKey is the attribute Key conforming to the
	// "host.cpu.model.id" semantic conventions. It represents the model
	// identifier. It provides more granular information about the CPU,
	// distinguishing it from other CPUs within the same family.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '6', '9000/778/B180L'
	HostCPUModelIDKey = attribute.Key("host.cpu.model.id")

	// HostCPUModelNameKey is the attribute Key conforming to the
	// "host.cpu.model.name" semantic conventions. It represents the model
	// designation of the processor.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz'
	HostCPUModelNameKey = attribute.Key("host.cpu.model.name")

	// HostCPUSteppingKey is the attribute Key conforming to the
	// "host.cpu.stepping" semantic conventions. It represents the stepping or
	// core revisions.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '1', 'r1p1'
	HostCPUSteppingKey = attribute.Key("host.cpu.stepping")

	// HostCPUVendorIDKey is the attribute Key conforming to the
	// "host.cpu.vendor.id" semantic conventions. It represents the processor
	// manufacturer identifier. A maximum 12-character string.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'GenuineIntel'
	// Note: [CPUID](https://wiki.osdev.org/CPUID) command returns the vendor
	// ID string in EBX, EDX and ECX registers. Writing these to memory in this
	// order results in a 12-character string.
	HostCPUVendorIDKey = attribute.Key("host.cpu.vendor.id")

	// HostIDKey is the attribute Key conforming to the "host.id" semantic
	// conventions. It represents the unique host ID. For Cloud, this must be
	// the instance_id assigned by the cloud provider. For non-containerized
	// systems, this should be the `machine-id`. See the table below for the
	// sources to use to determine the `machine-id` based on operating system.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'fdbf79e8af94cb7f9e8df36789187052'
	HostIDKey = attribute.Key("host.id")

	// HostImageIDKey is the attribute Key conforming to the "host.image.id"
	// semantic conventions. It represents the vM image ID or host OS image ID.
	// For Cloud, this value is from the provider.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'ami-07b06b442921831e5'
	HostImageIDKey = attribute.Key("host.image.id")

	// HostImageNameKey is the attribute Key conforming to the
	// "host.image.name" semantic conventions. It represents the name of the VM
	// image or OS install the host was instantiated from.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'infra-ami-eks-worker-node-7d4ec78312', 'CentOS-8-x86_64-1905'
	HostImageNameKey = attribute.Key("host.image.name")

	// HostImageVersionKey is the attribute Key conforming to the
	// "host.image.version" semantic conventions. It represents the version
	// string of the VM image or host OS as defined in [Version
	// Attributes](/docs/resource/README.md#version-attributes).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '0.1'
	HostImageVersionKey = attribute.Key("host.image.version")

	// HostIPKey is the attribute Key conforming to the "host.ip" semantic
	// conventions. It represents the available IP addresses of the host,
	// excluding loopback interfaces.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '192.168.1.140', 'fe80::abc2:4a28:737a:609e'
	// Note: IPv4 Addresses MUST be specified in dotted-quad notation. IPv6
	// addresses MUST be specified in the [RFC
	// 5952](https://www.rfc-editor.org/rfc/rfc5952.html) format.
	HostIPKey = attribute.Key("host.ip")

	// HostMacKey is the attribute Key conforming to the "host.mac" semantic
	// conventions. It represents the available MAC addresses of the host,
	// excluding loopback interfaces.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'AC-DE-48-23-45-67', 'AC-DE-48-23-45-67-01-9F'
	// Note: MAC Addresses MUST be represented in [IEEE RA hexadecimal
	// form](https://standards.ieee.org/wp-content/uploads/import/documents/tutorials/eui.pdf):
	// as hyphen-separated octets in uppercase hexadecimal form from most to
	// least significant.
	HostMacKey = attribute.Key("host.mac")

	// HostNameKey is the attribute Key conforming to the "host.name" semantic
	// conventions. It represents the name of the host. On Unix systems, it may
	// contain what the hostname command returns, or the fully qualified
	// hostname, or another name specified by the user.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry-test'
	HostNameKey = attribute.Key("host.name")

	// HostTypeKey is the attribute Key conforming to the "host.type" semantic
	// conventions. It represents the type of host. For Cloud, this must be the
	// machine type.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'n1-standard-1'
	HostTypeKey = attribute.Key("host.type")
)

A host is defined as a computing instance. For example, physical servers, virtual machines, switches or disk array.

View Source
const (
	// HTTPConnectionStateKey is the attribute Key conforming to the
	// "http.connection.state" semantic conventions. It represents the state of
	// the HTTP connection in the HTTP connection pool.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'active', 'idle'
	HTTPConnectionStateKey = attribute.Key("http.connection.state")

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
	// Stability: experimental
	// Examples: 3495
	HTTPRequestBodySizeKey = attribute.Key("http.request.body.size")

	// HTTPRequestMethodKey is the attribute Key conforming to the
	// "http.request.method" semantic conventions. It represents the hTTP
	// request method.
	//
	// Type: Enum
	// RequirementLevel: Optional
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
	// the `http.request.method` attribute to `_OTHER`.
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

	// HTTPRequestMethodOriginalKey is the attribute Key conforming to the
	// "http.request.method_original" semantic conventions. It represents the
	// original HTTP method sent by the client in the request line.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'GeT', 'ACL', 'foo'
	HTTPRequestMethodOriginalKey = attribute.Key("http.request.method_original")

	// HTTPRequestResendCountKey is the attribute Key conforming to the
	// "http.request.resend_count" semantic conventions. It represents the
	// ordinal number of request resending attempt (for any reason, including
	// redirects).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 3
	// Note: The resend count SHOULD be updated each time an HTTP request gets
	// resent by the client, regardless of what was the cause of the resending
	// (e.g. redirection, authorization failure, 503 Server Unavailable,
	// network issues, or any other).
	HTTPRequestResendCountKey = attribute.Key("http.request.resend_count")

	// HTTPRequestSizeKey is the attribute Key conforming to the
	// "http.request.size" semantic conventions. It represents the total size
	// of the request in bytes. This should be the total number of bytes sent
	// over the wire, including the request line (HTTP/1.1), framing (HTTP/2
	// and HTTP/3), headers, and request body if any.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1437
	HTTPRequestSizeKey = attribute.Key("http.request.size")

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
	// Stability: experimental
	// Examples: 3495
	HTTPResponseBodySizeKey = attribute.Key("http.response.body.size")

	// HTTPResponseSizeKey is the attribute Key conforming to the
	// "http.response.size" semantic conventions. It represents the total size
	// of the response in bytes. This should be the total number of bytes sent
	// over the wire, including the status line (HTTP/1.1), framing (HTTP/2 and
	// HTTP/3), headers, and response body and trailers if any.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1437
	HTTPResponseSizeKey = attribute.Key("http.response.size")

	// HTTPResponseStatusCodeKey is the attribute Key conforming to the
	// "http.response.status_code" semantic conventions. It represents the
	// [HTTP response status
	// code](https://tools.ietf.org/html/rfc7231#section-6).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 200
	HTTPResponseStatusCodeKey = attribute.Key("http.response.status_code")

	// HTTPRouteKey is the attribute Key conforming to the "http.route"
	// semantic conventions. It represents the matched route, that is, the path
	// template in the format used by the respective server framework.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/users/:userID?', '{controller}/{action}/{id?}'
	// Note: MUST NOT be populated when this is not supported by the HTTP
	// server framework as the route attribute should have low-cardinality and
	// the URI path can NOT substitute it.
	// SHOULD include the [application
	// root](/docs/http/http-spans.md#http-server-definitions) if there is one.
	HTTPRouteKey = attribute.Key("http.route")
)

Semantic convention attributes in the HTTP namespace.

View Source
const (
	// JvmBufferPoolNameKey is the attribute Key conforming to the
	// "jvm.buffer.pool.name" semantic conventions. It represents the name of
	// the buffer pool.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'mapped', 'direct'
	// Note: Pool names are generally obtained via
	// [BufferPoolMXBean#getName()](https://docs.oracle.com/en/java/javase/11/docs/api/java.management/java/lang/management/BufferPoolMXBean.html#getName()).
	JvmBufferPoolNameKey = attribute.Key("jvm.buffer.pool.name")

	// JvmGcActionKey is the attribute Key conforming to the "jvm.gc.action"
	// semantic conventions. It represents the name of the garbage collector
	// action.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'end of minor GC', 'end of major GC'
	// Note: Garbage collector action is generally obtained via
	// [GarbageCollectionNotificationInfo#getGcAction()](https://docs.oracle.com/en/java/javase/11/docs/api/jdk.management/com/sun/management/GarbageCollectionNotificationInfo.html#getGcAction()).
	JvmGcActionKey = attribute.Key("jvm.gc.action")

	// JvmGcNameKey is the attribute Key conforming to the "jvm.gc.name"
	// semantic conventions. It represents the name of the garbage collector.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'G1 Young Generation', 'G1 Old Generation'
	// Note: Garbage collector name is generally obtained via
	// [GarbageCollectionNotificationInfo#getGcName()](https://docs.oracle.com/en/java/javase/11/docs/api/jdk.management/com/sun/management/GarbageCollectionNotificationInfo.html#getGcName()).
	JvmGcNameKey = attribute.Key("jvm.gc.name")

	// JvmMemoryPoolNameKey is the attribute Key conforming to the
	// "jvm.memory.pool.name" semantic conventions. It represents the name of
	// the memory pool.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'G1 Old Gen', 'G1 Eden space', 'G1 Survivor Space'
	// Note: Pool names are generally obtained via
	// [MemoryPoolMXBean#getName()](https://docs.oracle.com/en/java/javase/11/docs/api/java.management/java/lang/management/MemoryPoolMXBean.html#getName()).
	JvmMemoryPoolNameKey = attribute.Key("jvm.memory.pool.name")

	// JvmMemoryTypeKey is the attribute Key conforming to the
	// "jvm.memory.type" semantic conventions. It represents the type of
	// memory.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'heap', 'non_heap'
	JvmMemoryTypeKey = attribute.Key("jvm.memory.type")

	// JvmThreadDaemonKey is the attribute Key conforming to the
	// "jvm.thread.daemon" semantic conventions. It represents the whether the
	// thread is daemon or not.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: stable
	JvmThreadDaemonKey = attribute.Key("jvm.thread.daemon")

	// JvmThreadStateKey is the attribute Key conforming to the
	// "jvm.thread.state" semantic conventions. It represents the state of the
	// thread.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'runnable', 'blocked'
	JvmThreadStateKey = attribute.Key("jvm.thread.state")
)

Java Virtual machine related attributes.

View Source
const (
	// K8SClusterNameKey is the attribute Key conforming to the
	// "k8s.cluster.name" semantic conventions. It represents the name of the
	// cluster.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry-cluster'
	K8SClusterNameKey = attribute.Key("k8s.cluster.name")

	// K8SClusterUIDKey is the attribute Key conforming to the
	// "k8s.cluster.uid" semantic conventions. It represents a pseudo-ID for
	// the cluster, set to the UID of the `kube-system` namespace.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '218fc5a9-a5f1-4b54-aa05-46717d0ab26d'
	// Note: K8S doesn't have support for obtaining a cluster ID. If this is
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

	// K8SContainerNameKey is the attribute Key conforming to the
	// "k8s.container.name" semantic conventions. It represents the name of the
	// Container from Pod specification, must be unique within a Pod. Container
	// runtime usually uses different globally unique name (`container.name`).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
	// Stability: experimental
	K8SContainerRestartCountKey = attribute.Key("k8s.container.restart_count")

	// K8SContainerStatusLastTerminatedReasonKey is the attribute Key
	// conforming to the "k8s.container.status.last_terminated_reason" semantic
	// conventions. It represents the last terminated reason of the Container.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Evicted', 'Error'
	K8SContainerStatusLastTerminatedReasonKey = attribute.Key("k8s.container.status.last_terminated_reason")

	// K8SCronJobNameKey is the attribute Key conforming to the
	// "k8s.cronjob.name" semantic conventions. It represents the name of the
	// CronJob.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry'
	K8SCronJobNameKey = attribute.Key("k8s.cronjob.name")

	// K8SCronJobUIDKey is the attribute Key conforming to the
	// "k8s.cronjob.uid" semantic conventions. It represents the UID of the
	// CronJob.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SCronJobUIDKey = attribute.Key("k8s.cronjob.uid")

	// K8SDaemonSetNameKey is the attribute Key conforming to the
	// "k8s.daemonset.name" semantic conventions. It represents the name of the
	// DaemonSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry'
	K8SDaemonSetNameKey = attribute.Key("k8s.daemonset.name")

	// K8SDaemonSetUIDKey is the attribute Key conforming to the
	// "k8s.daemonset.uid" semantic conventions. It represents the UID of the
	// DaemonSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SDaemonSetUIDKey = attribute.Key("k8s.daemonset.uid")

	// K8SDeploymentNameKey is the attribute Key conforming to the
	// "k8s.deployment.name" semantic conventions. It represents the name of
	// the Deployment.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry'
	K8SDeploymentNameKey = attribute.Key("k8s.deployment.name")

	// K8SDeploymentUIDKey is the attribute Key conforming to the
	// "k8s.deployment.uid" semantic conventions. It represents the UID of the
	// Deployment.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SDeploymentUIDKey = attribute.Key("k8s.deployment.uid")

	// K8SJobNameKey is the attribute Key conforming to the "k8s.job.name"
	// semantic conventions. It represents the name of the Job.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry'
	K8SJobNameKey = attribute.Key("k8s.job.name")

	// K8SJobUIDKey is the attribute Key conforming to the "k8s.job.uid"
	// semantic conventions. It represents the UID of the Job.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SJobUIDKey = attribute.Key("k8s.job.uid")

	// K8SNamespaceNameKey is the attribute Key conforming to the
	// "k8s.namespace.name" semantic conventions. It represents the name of the
	// namespace that the pod is running in.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'default'
	K8SNamespaceNameKey = attribute.Key("k8s.namespace.name")

	// K8SNodeNameKey is the attribute Key conforming to the "k8s.node.name"
	// semantic conventions. It represents the name of the Node.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'node-1'
	K8SNodeNameKey = attribute.Key("k8s.node.name")

	// K8SNodeUIDKey is the attribute Key conforming to the "k8s.node.uid"
	// semantic conventions. It represents the UID of the Node.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '1eb3a0c6-0477-4080-a9cb-0cb7db65c6a2'
	K8SNodeUIDKey = attribute.Key("k8s.node.uid")

	// K8SPodNameKey is the attribute Key conforming to the "k8s.pod.name"
	// semantic conventions. It represents the name of the Pod.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry-pod-autoconf'
	K8SPodNameKey = attribute.Key("k8s.pod.name")

	// K8SPodUIDKey is the attribute Key conforming to the "k8s.pod.uid"
	// semantic conventions. It represents the UID of the Pod.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SPodUIDKey = attribute.Key("k8s.pod.uid")

	// K8SReplicaSetNameKey is the attribute Key conforming to the
	// "k8s.replicaset.name" semantic conventions. It represents the name of
	// the ReplicaSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry'
	K8SReplicaSetNameKey = attribute.Key("k8s.replicaset.name")

	// K8SReplicaSetUIDKey is the attribute Key conforming to the
	// "k8s.replicaset.uid" semantic conventions. It represents the UID of the
	// ReplicaSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SReplicaSetUIDKey = attribute.Key("k8s.replicaset.uid")

	// K8SStatefulSetNameKey is the attribute Key conforming to the
	// "k8s.statefulset.name" semantic conventions. It represents the name of
	// the StatefulSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry'
	K8SStatefulSetNameKey = attribute.Key("k8s.statefulset.name")

	// K8SStatefulSetUIDKey is the attribute Key conforming to the
	// "k8s.statefulset.uid" semantic conventions. It represents the UID of the
	// StatefulSet.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '275ecb36-5aa8-4c2a-9c47-d8bb681b9aff'
	K8SStatefulSetUIDKey = attribute.Key("k8s.statefulset.uid")
)

Kubernetes resource attributes.

View Source
const (
	// LogFileNameKey is the attribute Key conforming to the "log.file.name"
	// semantic conventions. It represents the basename of the file.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'audit.log'
	LogFileNameKey = attribute.Key("log.file.name")

	// LogFileNameResolvedKey is the attribute Key conforming to the
	// "log.file.name_resolved" semantic conventions. It represents the
	// basename of the file, with symlinks resolved.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'uuid.log'
	LogFileNameResolvedKey = attribute.Key("log.file.name_resolved")

	// LogFilePathKey is the attribute Key conforming to the "log.file.path"
	// semantic conventions. It represents the full path to the file.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/var/log/mysql/audit.log'
	LogFilePathKey = attribute.Key("log.file.path")

	// LogFilePathResolvedKey is the attribute Key conforming to the
	// "log.file.path_resolved" semantic conventions. It represents the full
	// path to the file, with symlinks resolved.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/var/lib/docker/uuid.log'
	LogFilePathResolvedKey = attribute.Key("log.file.path_resolved")
)

Attributes for a file to which log was emitted.

View Source
const (
	// MessagingBatchMessageCountKey is the attribute Key conforming to the
	// "messaging.batch.message_count" semantic conventions. It represents the
	// number of messages sent, received, or processed in the scope of the
	// batching operation.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 0, 1, 2
	// Note: Instrumentations SHOULD NOT set `messaging.batch.message_count` on
	// spans that operate with a single message. When a messaging client
	// library supports both batch and single-message API for the same
	// operation, instrumentations SHOULD use `messaging.batch.message_count`
	// for batching APIs and SHOULD NOT use it for single-message APIs.
	MessagingBatchMessageCountKey = attribute.Key("messaging.batch.message_count")

	// MessagingClientIDKey is the attribute Key conforming to the
	// "messaging.client.id" semantic conventions. It represents a unique
	// identifier for the client that consumes or produces a message.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'client-5', 'myhost@8742@s8083jm'
	MessagingClientIDKey = attribute.Key("messaging.client.id")

	// MessagingDestinationAnonymousKey is the attribute Key conforming to the
	// "messaging.destination.anonymous" semantic conventions. It represents a
	// boolean that is true if the message destination is anonymous (could be
	// unnamed or have auto-generated name).
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	MessagingDestinationAnonymousKey = attribute.Key("messaging.destination.anonymous")

	// MessagingDestinationNameKey is the attribute Key conforming to the
	// "messaging.destination.name" semantic conventions. It represents the
	// message destination name
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'MyQueue', 'MyTopic'
	// Note: Destination name SHOULD uniquely identify a specific queue, topic
	// or other entity within the broker. If
	// the broker doesn't have such notion, the destination name SHOULD
	// uniquely identify the broker.
	MessagingDestinationNameKey = attribute.Key("messaging.destination.name")

	// MessagingDestinationPartitionIDKey is the attribute Key conforming to
	// the "messaging.destination.partition.id" semantic conventions. It
	// represents the identifier of the partition messages are sent to or
	// received from, unique within the `messaging.destination.name`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '1'
	MessagingDestinationPartitionIDKey = attribute.Key("messaging.destination.partition.id")

	// MessagingDestinationTemplateKey is the attribute Key conforming to the
	// "messaging.destination.template" semantic conventions. It represents the
	// low cardinality representation of the messaging destination name
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
	// Stability: experimental
	MessagingDestinationTemporaryKey = attribute.Key("messaging.destination.temporary")

	// MessagingDestinationPublishAnonymousKey is the attribute Key conforming
	// to the "messaging.destination_publish.anonymous" semantic conventions.
	// It represents a boolean that is true if the publish message destination
	// is anonymous (could be unnamed or have auto-generated name).
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	MessagingDestinationPublishAnonymousKey = attribute.Key("messaging.destination_publish.anonymous")

	// MessagingDestinationPublishNameKey is the attribute Key conforming to
	// the "messaging.destination_publish.name" semantic conventions. It
	// represents the name of the original destination the message was
	// published to
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'MyQueue', 'MyTopic'
	// Note: The name SHOULD uniquely identify a specific queue, topic, or
	// other entity within the broker. If
	// the broker doesn't have such notion, the original destination name
	// SHOULD uniquely identify the broker.
	MessagingDestinationPublishNameKey = attribute.Key("messaging.destination_publish.name")

	// MessagingMessageBodySizeKey is the attribute Key conforming to the
	// "messaging.message.body.size" semantic conventions. It represents the
	// size of the message body in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1439
	// Note: This can refer to both the compressed or uncompressed body size.
	// If both sizes are known, the uncompressed
	// body size should be used.
	MessagingMessageBodySizeKey = attribute.Key("messaging.message.body.size")

	// MessagingMessageConversationIDKey is the attribute Key conforming to the
	// "messaging.message.conversation_id" semantic conventions. It represents
	// the conversation ID identifying the conversation to which the message
	// belongs, represented as a string. Sometimes called "Correlation ID".
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'MyConversationID'
	MessagingMessageConversationIDKey = attribute.Key("messaging.message.conversation_id")

	// MessagingMessageEnvelopeSizeKey is the attribute Key conforming to the
	// "messaging.message.envelope.size" semantic conventions. It represents
	// the size of the message body and metadata in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 2738
	// Note: This can refer to both the compressed or uncompressed size. If
	// both sizes are known, the uncompressed
	// size should be used.
	MessagingMessageEnvelopeSizeKey = attribute.Key("messaging.message.envelope.size")

	// MessagingMessageIDKey is the attribute Key conforming to the
	// "messaging.message.id" semantic conventions. It represents a value used
	// by the messaging system as an identifier for the message, represented as
	// a string.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '452a7c7c7c7048c2f887f61572b18fc2'
	MessagingMessageIDKey = attribute.Key("messaging.message.id")

	// MessagingOperationNameKey is the attribute Key conforming to the
	// "messaging.operation.name" semantic conventions. It represents the
	// system-specific name of the messaging operation.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'ack', 'nack', 'send'
	MessagingOperationNameKey = attribute.Key("messaging.operation.name")

	// MessagingOperationTypeKey is the attribute Key conforming to the
	// "messaging.operation.type" semantic conventions. It represents a string
	// identifying the type of the messaging operation.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: If a custom value is used, it MUST be of low cardinality.
	MessagingOperationTypeKey = attribute.Key("messaging.operation.type")

	// MessagingSystemKey is the attribute Key conforming to the
	// "messaging.system" semantic conventions. It represents the messaging
	// system as identified by the client instrumentation.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: The actual messaging system may differ from the one known by the
	// client. For example, when using Kafka client libraries to communicate
	// with Azure Event Hubs, the `messaging.system` is set to `kafka` based on
	// the instrumentation's best knowledge.
	MessagingSystemKey = attribute.Key("messaging.system")
)

Attributes describing telemetry around messaging systems and messaging activities.

View Source
const (
	// MessagingKafkaConsumerGroupKey is the attribute Key conforming to the
	// "messaging.kafka.consumer.group" semantic conventions. It represents the
	// name of the Kafka Consumer Group that is handling the message. Only
	// applies to consumers, not producers.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'my-group'
	MessagingKafkaConsumerGroupKey = attribute.Key("messaging.kafka.consumer.group")

	// MessagingKafkaMessageKeyKey is the attribute Key conforming to the
	// "messaging.kafka.message.key" semantic conventions. It represents the
	// message keys in Kafka are used for grouping alike messages to ensure
	// they're processed on the same partition. They differ from
	// `messaging.message.id` in that they're not unique. If the key is `null`,
	// the attribute MUST NOT be set.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myKey'
	// Note: If the key type is not string, it's string representation has to
	// be supplied for the attribute. If the key has no unambiguous, canonical
	// string form, don't include its value.
	MessagingKafkaMessageKeyKey = attribute.Key("messaging.kafka.message.key")

	// MessagingKafkaMessageOffsetKey is the attribute Key conforming to the
	// "messaging.kafka.message.offset" semantic conventions. It represents the
	// offset of a record in the corresponding Kafka partition.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 42
	MessagingKafkaMessageOffsetKey = attribute.Key("messaging.kafka.message.offset")

	// MessagingKafkaMessageTombstoneKey is the attribute Key conforming to the
	// "messaging.kafka.message.tombstone" semantic conventions. It represents
	// a boolean that is true if the message is a tombstone.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	MessagingKafkaMessageTombstoneKey = attribute.Key("messaging.kafka.message.tombstone")
)

This group describes attributes specific to Apache Kafka.

View Source
const (
	// MessagingRabbitmqDestinationRoutingKeyKey is the attribute Key
	// conforming to the "messaging.rabbitmq.destination.routing_key" semantic
	// conventions. It represents the rabbitMQ message routing key.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myKey'
	MessagingRabbitmqDestinationRoutingKeyKey = attribute.Key("messaging.rabbitmq.destination.routing_key")

	// MessagingRabbitmqMessageDeliveryTagKey is the attribute Key conforming
	// to the "messaging.rabbitmq.message.delivery_tag" semantic conventions.
	// It represents the rabbitMQ message delivery tag
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 123
	MessagingRabbitmqMessageDeliveryTagKey = attribute.Key("messaging.rabbitmq.message.delivery_tag")
)

This group describes attributes specific to RabbitMQ.

View Source
const (
	// MessagingRocketmqClientGroupKey is the attribute Key conforming to the
	// "messaging.rocketmq.client_group" semantic conventions. It represents
	// the name of the RocketMQ producer/consumer group that is handling the
	// message. The client type is identified by the SpanKind.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myConsumerGroup'
	MessagingRocketmqClientGroupKey = attribute.Key("messaging.rocketmq.client_group")

	// MessagingRocketmqConsumptionModelKey is the attribute Key conforming to
	// the "messaging.rocketmq.consumption_model" semantic conventions. It
	// represents the model of message consumption. This only applies to
	// consumer spans.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	MessagingRocketmqConsumptionModelKey = attribute.Key("messaging.rocketmq.consumption_model")

	// MessagingRocketmqMessageDelayTimeLevelKey is the attribute Key
	// conforming to the "messaging.rocketmq.message.delay_time_level" semantic
	// conventions. It represents the delay time level for delay message, which
	// determines the message delay time.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 3
	MessagingRocketmqMessageDelayTimeLevelKey = attribute.Key("messaging.rocketmq.message.delay_time_level")

	// MessagingRocketmqMessageDeliveryTimestampKey is the attribute Key
	// conforming to the "messaging.rocketmq.message.delivery_timestamp"
	// semantic conventions. It represents the timestamp in milliseconds that
	// the delay message is expected to be delivered to consumer.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1665987217045
	MessagingRocketmqMessageDeliveryTimestampKey = attribute.Key("messaging.rocketmq.message.delivery_timestamp")

	// MessagingRocketmqMessageGroupKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.group" semantic conventions. It represents
	// the it is essential for FIFO message. Messages that belong to the same
	// message group are always processed one by one within the same consumer
	// group.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myMessageGroup'
	MessagingRocketmqMessageGroupKey = attribute.Key("messaging.rocketmq.message.group")

	// MessagingRocketmqMessageKeysKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.keys" semantic conventions. It represents
	// the key(s) of message, another way to mark message besides message id.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'keyA', 'keyB'
	MessagingRocketmqMessageKeysKey = attribute.Key("messaging.rocketmq.message.keys")

	// MessagingRocketmqMessageTagKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.tag" semantic conventions. It represents the
	// secondary classifier of message besides topic.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'tagA'
	MessagingRocketmqMessageTagKey = attribute.Key("messaging.rocketmq.message.tag")

	// MessagingRocketmqMessageTypeKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.type" semantic conventions. It represents
	// the type of message.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	MessagingRocketmqMessageTypeKey = attribute.Key("messaging.rocketmq.message.type")

	// MessagingRocketmqNamespaceKey is the attribute Key conforming to the
	// "messaging.rocketmq.namespace" semantic conventions. It represents the
	// namespace of RocketMQ resources, resources in different namespaces are
	// individual.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myNamespace'
	MessagingRocketmqNamespaceKey = attribute.Key("messaging.rocketmq.namespace")
)

This group describes attributes specific to RocketMQ.

View Source
const (
	// MessagingGCPPubsubMessageAckDeadlineKey is the attribute Key conforming
	// to the "messaging.gcp_pubsub.message.ack_deadline" semantic conventions.
	// It represents the ack deadline in seconds set for the modify ack
	// deadline request.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 10
	MessagingGCPPubsubMessageAckDeadlineKey = attribute.Key("messaging.gcp_pubsub.message.ack_deadline")

	// MessagingGCPPubsubMessageAckIDKey is the attribute Key conforming to the
	// "messaging.gcp_pubsub.message.ack_id" semantic conventions. It
	// represents the ack id for a given message.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'ack_id'
	MessagingGCPPubsubMessageAckIDKey = attribute.Key("messaging.gcp_pubsub.message.ack_id")

	// MessagingGCPPubsubMessageDeliveryAttemptKey is the attribute Key
	// conforming to the "messaging.gcp_pubsub.message.delivery_attempt"
	// semantic conventions. It represents the delivery attempt for a given
	// message.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 2
	MessagingGCPPubsubMessageDeliveryAttemptKey = attribute.Key("messaging.gcp_pubsub.message.delivery_attempt")

	// MessagingGCPPubsubMessageOrderingKeyKey is the attribute Key conforming
	// to the "messaging.gcp_pubsub.message.ordering_key" semantic conventions.
	// It represents the ordering key for a given message. If the attribute is
	// not present, the message does not have an ordering key.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'ordering_key'
	MessagingGCPPubsubMessageOrderingKeyKey = attribute.Key("messaging.gcp_pubsub.message.ordering_key")
)

This group describes attributes specific to GCP Pub/Sub.

View Source
const (
	// MessagingServicebusDestinationSubscriptionNameKey is the attribute Key
	// conforming to the "messaging.servicebus.destination.subscription_name"
	// semantic conventions. It represents the name of the subscription in the
	// topic messages are received from.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'mySubscription'
	MessagingServicebusDestinationSubscriptionNameKey = attribute.Key("messaging.servicebus.destination.subscription_name")

	// MessagingServicebusDispositionStatusKey is the attribute Key conforming
	// to the "messaging.servicebus.disposition_status" semantic conventions.
	// It represents the describes the [settlement
	// type](https://learn.microsoft.com/azure/service-bus-messaging/message-transfers-locks-settlement#peeklock).
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	MessagingServicebusDispositionStatusKey = attribute.Key("messaging.servicebus.disposition_status")

	// MessagingServicebusMessageDeliveryCountKey is the attribute Key
	// conforming to the "messaging.servicebus.message.delivery_count" semantic
	// conventions. It represents the number of deliveries that have been
	// attempted for this message.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 2
	MessagingServicebusMessageDeliveryCountKey = attribute.Key("messaging.servicebus.message.delivery_count")

	// MessagingServicebusMessageEnqueuedTimeKey is the attribute Key
	// conforming to the "messaging.servicebus.message.enqueued_time" semantic
	// conventions. It represents the UTC epoch seconds at which the message
	// has been accepted and stored in the entity.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1701393730
	MessagingServicebusMessageEnqueuedTimeKey = attribute.Key("messaging.servicebus.message.enqueued_time")
)

This group describes attributes specific to Azure Service Bus.

View Source
const (
	// MessagingEventhubsConsumerGroupKey is the attribute Key conforming to
	// the "messaging.eventhubs.consumer.group" semantic conventions. It
	// represents the name of the consumer group the event consumer is
	// associated with.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'indexer'
	MessagingEventhubsConsumerGroupKey = attribute.Key("messaging.eventhubs.consumer.group")

	// MessagingEventhubsMessageEnqueuedTimeKey is the attribute Key conforming
	// to the "messaging.eventhubs.message.enqueued_time" semantic conventions.
	// It represents the UTC epoch seconds at which the message has been
	// accepted and stored in the entity.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1701393730
	MessagingEventhubsMessageEnqueuedTimeKey = attribute.Key("messaging.eventhubs.message.enqueued_time")
)

This group describes attributes specific to Azure Event Hubs.

View Source
const (
	// NetworkCarrierIccKey is the attribute Key conforming to the
	// "network.carrier.icc" semantic conventions. It represents the ISO 3166-1
	// alpha-2 2-character country code associated with the mobile carrier
	// network.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'DE'
	NetworkCarrierIccKey = attribute.Key("network.carrier.icc")

	// NetworkCarrierMccKey is the attribute Key conforming to the
	// "network.carrier.mcc" semantic conventions. It represents the mobile
	// carrier country code.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '310'
	NetworkCarrierMccKey = attribute.Key("network.carrier.mcc")

	// NetworkCarrierMncKey is the attribute Key conforming to the
	// "network.carrier.mnc" semantic conventions. It represents the mobile
	// carrier network code.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '001'
	NetworkCarrierMncKey = attribute.Key("network.carrier.mnc")

	// NetworkCarrierNameKey is the attribute Key conforming to the
	// "network.carrier.name" semantic conventions. It represents the name of
	// the mobile carrier.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'sprint'
	NetworkCarrierNameKey = attribute.Key("network.carrier.name")

	// NetworkConnectionSubtypeKey is the attribute Key conforming to the
	// "network.connection.subtype" semantic conventions. It represents the
	// this describes more details regarding the connection.type. It may be the
	// type of cell technology connection, but it could be used for describing
	// details about a wifi connection.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'LTE'
	NetworkConnectionSubtypeKey = attribute.Key("network.connection.subtype")

	// NetworkConnectionTypeKey is the attribute Key conforming to the
	// "network.connection.type" semantic conventions. It represents the
	// internet connection type.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'wifi'
	NetworkConnectionTypeKey = attribute.Key("network.connection.type")

	// NetworkIoDirectionKey is the attribute Key conforming to the
	// "network.io.direction" semantic conventions. It represents the network
	// IO operation direction.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'transmit'
	NetworkIoDirectionKey = attribute.Key("network.io.direction")

	// NetworkLocalAddressKey is the attribute Key conforming to the
	// "network.local.address" semantic conventions. It represents the local
	// address of the network connection - IP address or Unix domain socket
	// name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '10.1.2.80', '/tmp/my.sock'
	NetworkLocalAddressKey = attribute.Key("network.local.address")

	// NetworkLocalPortKey is the attribute Key conforming to the
	// "network.local.port" semantic conventions. It represents the local port
	// number of the network connection.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 65123
	NetworkLocalPortKey = attribute.Key("network.local.port")

	// NetworkPeerAddressKey is the attribute Key conforming to the
	// "network.peer.address" semantic conventions. It represents the peer
	// address of the network connection - IP address or Unix domain socket
	// name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '10.1.2.80', '/tmp/my.sock'
	NetworkPeerAddressKey = attribute.Key("network.peer.address")

	// NetworkPeerPortKey is the attribute Key conforming to the
	// "network.peer.port" semantic conventions. It represents the peer port
	// number of the network connection.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 65123
	NetworkPeerPortKey = attribute.Key("network.peer.port")

	// NetworkProtocolNameKey is the attribute Key conforming to the
	// "network.protocol.name" semantic conventions. It represents the [OSI
	// application layer](https://osi-model.com/application-layer/) or non-OSI
	// equivalent.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'amqp', 'http', 'mqtt'
	// Note: The value SHOULD be normalized to lowercase.
	NetworkProtocolNameKey = attribute.Key("network.protocol.name")

	// NetworkProtocolVersionKey is the attribute Key conforming to the
	// "network.protocol.version" semantic conventions. It represents the
	// actual version of the protocol used for network communication.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '1.1', '2'
	// Note: If protocol version is subject to negotiation (for example using
	// [ALPN](https://www.rfc-editor.org/rfc/rfc7301.html)), this attribute
	// SHOULD be set to the negotiated version. If the actual protocol version
	// is not known, this attribute SHOULD NOT be set.
	NetworkProtocolVersionKey = attribute.Key("network.protocol.version")

	// NetworkTransportKey is the attribute Key conforming to the
	// "network.transport" semantic conventions. It represents the [OSI
	// transport layer](https://osi-model.com/transport-layer/) or
	// [inter-process communication
	// method](https://wikipedia.org/wiki/Inter-process_communication).
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'tcp', 'udp'
	// Note: The value SHOULD be normalized to lowercase.
	//
	// Consider always setting the transport when setting a port number, since
	// a port number is ambiguous without knowing the transport. For example
	// different processes could be listening on TCP port 12345 and UDP port
	// 12345.
	NetworkTransportKey = attribute.Key("network.transport")

	// NetworkTypeKey is the attribute Key conforming to the "network.type"
	// semantic conventions. It represents the [OSI network
	// layer](https://osi-model.com/network-layer/) or non-OSI equivalent.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'ipv4', 'ipv6'
	// Note: The value SHOULD be normalized to lowercase.
	NetworkTypeKey = attribute.Key("network.type")
)

These attributes may be used for any network related operation.

View Source
const (
	// OSBuildIDKey is the attribute Key conforming to the "os.build_id"
	// semantic conventions. It represents the unique identifier for a
	// particular build or compilation of the operating system.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'TQ3C.230805.001.B2', '20E247', '22621'
	OSBuildIDKey = attribute.Key("os.build_id")

	// OSDescriptionKey is the attribute Key conforming to the "os.description"
	// semantic conventions. It represents the human readable (not intended to
	// be parsed) OS version information, like e.g. reported by `ver` or
	// `lsb_release -a` commands.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Microsoft Windows [Version 10.0.18363.778]', 'Ubuntu 18.04.1
	// LTS'
	OSDescriptionKey = attribute.Key("os.description")

	// OSNameKey is the attribute Key conforming to the "os.name" semantic
	// conventions. It represents the human readable operating system name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'iOS', 'Android', 'Ubuntu'
	OSNameKey = attribute.Key("os.name")

	// OSTypeKey is the attribute Key conforming to the "os.type" semantic
	// conventions. It represents the operating system type.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	OSTypeKey = attribute.Key("os.type")

	// OSVersionKey is the attribute Key conforming to the "os.version"
	// semantic conventions. It represents the version string of the operating
	// system as defined in [Version
	// Attributes](/docs/resource/README.md#version-attributes).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '14.2.1', '18.04.1'
	OSVersionKey = attribute.Key("os.version")
)

The operating system (OS) on which the process represented by this resource is running.

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

Attributes reserved for OpenTelemetry

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
	// ProcessCommandKey is the attribute Key conforming to the
	// "process.command" semantic conventions. It represents the command used
	// to launch the process (i.e. the command name). On Linux based systems,
	// can be set to the zeroth string in `proc/[pid]/cmdline`. On Windows, can
	// be set to the first parameter extracted from `GetCommandLineW`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'cmd/otelcol'
	ProcessCommandKey = attribute.Key("process.command")

	// ProcessCommandArgsKey is the attribute Key conforming to the
	// "process.command_args" semantic conventions. It represents the all the
	// command arguments (including the command/executable itself) as received
	// by the process. On Linux-based systems (and some other Unixoid systems
	// supporting procfs), can be set according to the list of null-delimited
	// strings extracted from `proc/[pid]/cmdline`. For libc-based executables,
	// this would be the full argv vector passed to `main`.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'cmd/otecol', '--config=config.yaml'
	ProcessCommandArgsKey = attribute.Key("process.command_args")

	// ProcessCommandLineKey is the attribute Key conforming to the
	// "process.command_line" semantic conventions. It represents the full
	// command used to launch the process as a single string representing the
	// full command. On Windows, can be set to the result of `GetCommandLineW`.
	// Do not set this if you have to assemble it just for monitoring; use
	// `process.command_args` instead.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'C:\\cmd\\otecol --config="my directory\\config.yaml"'
	ProcessCommandLineKey = attribute.Key("process.command_line")

	// ProcessContextSwitchTypeKey is the attribute Key conforming to the
	// "process.context_switch_type" semantic conventions. It represents the
	// specifies whether the context switches for this data point were
	// voluntary or involuntary.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	ProcessContextSwitchTypeKey = attribute.Key("process.context_switch_type")

	// ProcessCreationTimeKey is the attribute Key conforming to the
	// "process.creation.time" semantic conventions. It represents the date and
	// time the process was created, in ISO 8601 format.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2023-11-21T09:25:34.853Z'
	ProcessCreationTimeKey = attribute.Key("process.creation.time")

	// ProcessExecutableNameKey is the attribute Key conforming to the
	// "process.executable.name" semantic conventions. It represents the name
	// of the process executable. On Linux based systems, can be set to the
	// `Name` in `proc/[pid]/status`. On Windows, can be set to the base name
	// of `GetProcessImageFileNameW`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'otelcol'
	ProcessExecutableNameKey = attribute.Key("process.executable.name")

	// ProcessExecutablePathKey is the attribute Key conforming to the
	// "process.executable.path" semantic conventions. It represents the full
	// path to the process executable. On Linux based systems, can be set to
	// the target of `proc/[pid]/exe`. On Windows, can be set to the result of
	// `GetProcessImageFileNameW`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/usr/bin/cmd/otelcol'
	ProcessExecutablePathKey = attribute.Key("process.executable.path")

	// ProcessExitCodeKey is the attribute Key conforming to the
	// "process.exit.code" semantic conventions. It represents the exit code of
	// the process.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 127
	ProcessExitCodeKey = attribute.Key("process.exit.code")

	// ProcessExitTimeKey is the attribute Key conforming to the
	// "process.exit.time" semantic conventions. It represents the date and
	// time the process exited, in ISO 8601 format.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2023-11-21T09:26:12.315Z'
	ProcessExitTimeKey = attribute.Key("process.exit.time")

	// ProcessGroupLeaderPIDKey is the attribute Key conforming to the
	// "process.group_leader.pid" semantic conventions. It represents the PID
	// of the process's group leader. This is also the process group ID (PGID)
	// of the process.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 23
	ProcessGroupLeaderPIDKey = attribute.Key("process.group_leader.pid")

	// ProcessInteractiveKey is the attribute Key conforming to the
	// "process.interactive" semantic conventions. It represents the whether
	// the process is connected to an interactive shell.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	ProcessInteractiveKey = attribute.Key("process.interactive")

	// ProcessOwnerKey is the attribute Key conforming to the "process.owner"
	// semantic conventions. It represents the username of the user that owns
	// the process.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'root'
	ProcessOwnerKey = attribute.Key("process.owner")

	// ProcessPagingFaultTypeKey is the attribute Key conforming to the
	// "process.paging.fault_type" semantic conventions. It represents the type
	// of page fault for this data point. Type `major` is for major/hard page
	// faults, and `minor` is for minor/soft page faults.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	ProcessPagingFaultTypeKey = attribute.Key("process.paging.fault_type")

	// ProcessParentPIDKey is the attribute Key conforming to the
	// "process.parent_pid" semantic conventions. It represents the parent
	// Process identifier (PPID).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 111
	ProcessParentPIDKey = attribute.Key("process.parent_pid")

	// ProcessPIDKey is the attribute Key conforming to the "process.pid"
	// semantic conventions. It represents the process identifier (PID).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1234
	ProcessPIDKey = attribute.Key("process.pid")

	// ProcessRealUserIDKey is the attribute Key conforming to the
	// "process.real_user.id" semantic conventions. It represents the real user
	// ID (RUID) of the process.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1000
	ProcessRealUserIDKey = attribute.Key("process.real_user.id")

	// ProcessRealUserNameKey is the attribute Key conforming to the
	// "process.real_user.name" semantic conventions. It represents the
	// username of the real user of the process.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'operator'
	ProcessRealUserNameKey = attribute.Key("process.real_user.name")

	// ProcessRuntimeDescriptionKey is the attribute Key conforming to the
	// "process.runtime.description" semantic conventions. It represents an
	// additional description about the runtime of the process, for example a
	// specific vendor customization of the runtime environment.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Eclipse OpenJ9 Eclipse OpenJ9 VM openj9-0.21.0'
	ProcessRuntimeDescriptionKey = attribute.Key("process.runtime.description")

	// ProcessRuntimeNameKey is the attribute Key conforming to the
	// "process.runtime.name" semantic conventions. It represents the name of
	// the runtime of this process. For compiled native binaries, this SHOULD
	// be the name of the compiler.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'OpenJDK Runtime Environment'
	ProcessRuntimeNameKey = attribute.Key("process.runtime.name")

	// ProcessRuntimeVersionKey is the attribute Key conforming to the
	// "process.runtime.version" semantic conventions. It represents the
	// version of the runtime of this process, as returned by the runtime
	// without modification.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '14.0.2'
	ProcessRuntimeVersionKey = attribute.Key("process.runtime.version")

	// ProcessSavedUserIDKey is the attribute Key conforming to the
	// "process.saved_user.id" semantic conventions. It represents the saved
	// user ID (SUID) of the process.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1002
	ProcessSavedUserIDKey = attribute.Key("process.saved_user.id")

	// ProcessSavedUserNameKey is the attribute Key conforming to the
	// "process.saved_user.name" semantic conventions. It represents the
	// username of the saved user.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'operator'
	ProcessSavedUserNameKey = attribute.Key("process.saved_user.name")

	// ProcessSessionLeaderPIDKey is the attribute Key conforming to the
	// "process.session_leader.pid" semantic conventions. It represents the PID
	// of the process's session leader. This is also the session ID (SID) of
	// the process.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 14
	ProcessSessionLeaderPIDKey = attribute.Key("process.session_leader.pid")

	// ProcessUserIDKey is the attribute Key conforming to the
	// "process.user.id" semantic conventions. It represents the effective user
	// ID (EUID) of the process.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1001
	ProcessUserIDKey = attribute.Key("process.user.id")

	// ProcessUserNameKey is the attribute Key conforming to the
	// "process.user.name" semantic conventions. It represents the username of
	// the effective user of the process.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'root'
	ProcessUserNameKey = attribute.Key("process.user.name")

	// ProcessVpidKey is the attribute Key conforming to the "process.vpid"
	// semantic conventions. It represents the virtual process identifier.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 12
	// Note: The process ID within a PID namespace. This is not necessarily
	// unique across all processes on the host but it is unique within the
	// process namespace that the process exists within.
	ProcessVpidKey = attribute.Key("process.vpid")
)

An operating system process.

View Source
const (
	// RPCConnectRPCErrorCodeKey is the attribute Key conforming to the
	// "rpc.connect_rpc.error_code" semantic conventions. It represents the
	// [error codes](https://connect.build/docs/protocol/#error-codes) of the
	// Connect request. Error codes are always string values.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	RPCConnectRPCErrorCodeKey = attribute.Key("rpc.connect_rpc.error_code")

	// RPCGRPCStatusCodeKey is the attribute Key conforming to the
	// "rpc.grpc.status_code" semantic conventions. It represents the [numeric
	// status
	// code](https://github.com/grpc/grpc/blob/v1.33.2/doc/statuscodes.md) of
	// the gRPC request.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	RPCGRPCStatusCodeKey = attribute.Key("rpc.grpc.status_code")

	// RPCJsonrpcErrorCodeKey is the attribute Key conforming to the
	// "rpc.jsonrpc.error_code" semantic conventions. It represents the
	// `error.code` property of response if it is an error response.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: -32700, 100
	RPCJsonrpcErrorCodeKey = attribute.Key("rpc.jsonrpc.error_code")

	// RPCJsonrpcErrorMessageKey is the attribute Key conforming to the
	// "rpc.jsonrpc.error_message" semantic conventions. It represents the
	// `error.message` property of response if it is an error response.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Parse error', 'User already exists'
	RPCJsonrpcErrorMessageKey = attribute.Key("rpc.jsonrpc.error_message")

	// RPCJsonrpcRequestIDKey is the attribute Key conforming to the
	// "rpc.jsonrpc.request_id" semantic conventions. It represents the `id`
	// property of request or response. Since protocol allows id to be int,
	// string, `null` or missing (for notifications), value is expected to be
	// cast to string for simplicity. Use empty string in case of `null` value.
	// Omit entirely if this is a notification.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '10', 'request-7', ”
	RPCJsonrpcRequestIDKey = attribute.Key("rpc.jsonrpc.request_id")

	// RPCJsonrpcVersionKey is the attribute Key conforming to the
	// "rpc.jsonrpc.version" semantic conventions. It represents the protocol
	// version as in `jsonrpc` property of request/response. Since JSON-RPC 1.0
	// doesn't specify this, the value can be omitted.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2.0', '1.0'
	RPCJsonrpcVersionKey = attribute.Key("rpc.jsonrpc.version")

	// RPCMessageCompressedSizeKey is the attribute Key conforming to the
	// "rpc.message.compressed_size" semantic conventions. It represents the
	// compressed size of the message in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	RPCMessageCompressedSizeKey = attribute.Key("rpc.message.compressed_size")

	// RPCMessageIDKey is the attribute Key conforming to the "rpc.message.id"
	// semantic conventions. It represents the mUST be calculated as two
	// different counters starting from `1` one for sent messages and one for
	// received message.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: This way we guarantee that the values will be consistent between
	// different implementations.
	RPCMessageIDKey = attribute.Key("rpc.message.id")

	// RPCMessageTypeKey is the attribute Key conforming to the
	// "rpc.message.type" semantic conventions. It represents the whether this
	// is a received or sent message.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	RPCMessageTypeKey = attribute.Key("rpc.message.type")

	// RPCMessageUncompressedSizeKey is the attribute Key conforming to the
	// "rpc.message.uncompressed_size" semantic conventions. It represents the
	// uncompressed size of the message in bytes.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	RPCMessageUncompressedSizeKey = attribute.Key("rpc.message.uncompressed_size")

	// RPCMethodKey is the attribute Key conforming to the "rpc.method"
	// semantic conventions. It represents the name of the (logical) method
	// being called, must be equal to the $method part in the span name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'exampleMethod'
	// Note: This is the logical name of the method from the RPC interface
	// perspective, which can be different from the name of any implementing
	// method/function. The `code.function` attribute may be used to store the
	// latter (e.g., method actually executing the call on the server side, RPC
	// client stub method on the client side).
	RPCMethodKey = attribute.Key("rpc.method")

	// RPCServiceKey is the attribute Key conforming to the "rpc.service"
	// semantic conventions. It represents the full (logical) name of the
	// service being called, including its package name, if applicable.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'myservice.EchoService'
	// Note: This is the logical name of the service from the RPC interface
	// perspective, which can be different from the name of any implementing
	// class. The `code.namespace` attribute may be used to store the latter
	// (despite the attribute name, it may include a class name; e.g., class
	// with method actually executing the call on the server side, RPC client
	// stub class on the client side).
	RPCServiceKey = attribute.Key("rpc.service")

	// RPCSystemKey is the attribute Key conforming to the "rpc.system"
	// semantic conventions. It represents a string identifying the remoting
	// system. See below for a list of well-known identifiers.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	RPCSystemKey = attribute.Key("rpc.system")
)

Attributes for remote procedure calls.

View Source
const (
	// ServerAddressKey is the attribute Key conforming to the "server.address"
	// semantic conventions. It represents the server domain name if available
	// without reverse DNS lookup; otherwise, IP address or Unix domain socket
	// name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'example.com', '10.1.2.80', '/tmp/my.sock'
	// Note: When observed from the client side, and when communicating through
	// an intermediary, `server.address` SHOULD represent the server address
	// behind any intermediaries, for example proxies, if it's available.
	ServerAddressKey = attribute.Key("server.address")

	// ServerPortKey is the attribute Key conforming to the "server.port"
	// semantic conventions. It represents the server port number.
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 80, 8080, 443
	// Note: When observed from the client side, and when communicating through
	// an intermediary, `server.port` SHOULD represent the server port behind
	// any intermediaries, for example proxies, if it's available.
	ServerPortKey = attribute.Key("server.port")
)

These attributes may be used to describe the server in a connection-based network interaction where there is one side that initiates the connection (the client is the side that initiates the connection). This covers all TCP network interactions since TCP is connection-based and one side initiates the connection (an exception is made for peer-to-peer communication over TCP where the "user-facing" surface of the protocol / API doesn't expose a clear notion of client and server). This also covers UDP network interactions where one side initiates the interaction, e.g. QUIC (HTTP/3) and DNS.

View Source
const (
	// ServiceInstanceIDKey is the attribute Key conforming to the
	// "service.instance.id" semantic conventions. It represents the string ID
	// of the service instance.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '627cc493-f310-47de-96bd-71410b7dec09'
	// Note: MUST be unique for each instance of the same
	// `service.namespace,service.name` pair (in other words
	// `service.namespace,service.name,service.instance.id` triplet MUST be
	// globally unique). The ID helps to
	// distinguish instances of the same service that exist at the same time
	// (e.g. instances of a horizontally scaled
	// service).
	//
	// Implementations, such as SDKs, are recommended to generate a random
	// Version 1 or Version 4 [RFC
	// 4122](https://www.ietf.org/rfc/rfc4122.txt) UUID, but are free to use an
	// inherent unique ID as the source of
	// this value if stability is desirable. In that case, the ID SHOULD be
	// used as source of a UUID Version 5 and
	// SHOULD use the following UUID as the namespace:
	// `4d63009a-8d0f-11ee-aad7-4c796ed8e320`.
	//
	// UUIDs are typically recommended, as only an opaque value for the
	// purposes of identifying a service instance is
	// needed. Similar to what can be seen in the man page for the
	// [`/etc/machine-id`](https://www.freedesktop.org/software/systemd/man/machine-id.html)
	// file, the underlying
	// data, such as pod name and namespace should be treated as confidential,
	// being the user's choice to expose it
	// or not via another resource attribute.
	//
	// For applications running behind an application server (like unicorn), we
	// do not recommend using one identifier
	// for all processes participating in the application. Instead, it's
	// recommended each division (e.g. a worker
	// thread in unicorn) to have its own instance.id.
	//
	// It's not recommended for a Collector to set `service.instance.id` if it
	// can't unambiguously determine the
	// service instance that is generating that telemetry. For instance,
	// creating an UUID based on `pod.name` will
	// likely be wrong, as the Collector might not know from which container
	// within that pod the telemetry originated.
	// However, Collectors can set the `service.instance.id` if they can
	// unambiguously determine the service instance
	// for that telemetry. This is typically the case for scraping receivers,
	// as they know the target address and
	// port.
	ServiceInstanceIDKey = attribute.Key("service.instance.id")

	// ServiceNameKey is the attribute Key conforming to the "service.name"
	// semantic conventions. It represents the logical name of the service.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'shoppingcart'
	// Note: MUST be the same for all instances of horizontally scaled
	// services. If the value was not specified, SDKs MUST fallback to
	// `unknown_service:` concatenated with
	// [`process.executable.name`](process.md), e.g. `unknown_service:bash`. If
	// `process.executable.name` is not available, the value MUST be set to
	// `unknown_service`.
	ServiceNameKey = attribute.Key("service.name")

	// ServiceNamespaceKey is the attribute Key conforming to the
	// "service.namespace" semantic conventions. It represents a namespace for
	// `service.name`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
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
	// SessionIDKey is the attribute Key conforming to the "session.id"
	// semantic conventions. It represents a unique id to identify a session.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '00112233-4455-6677-8899-aabbccddeeff'
	SessionIDKey = attribute.Key("session.id")

	// SessionPreviousIDKey is the attribute Key conforming to the
	// "session.previous_id" semantic conventions. It represents the previous
	// `session.id` for this user, when known.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '00112233-4455-6677-8899-aabbccddeeff'
	SessionPreviousIDKey = attribute.Key("session.previous_id")
)

Session is defined as the period of time encompassing all activities performed by the application and the actions executed by the end user. Consequently, a Session is represented as a collection of Logs, Events, and Spans emitted by the Client Application throughout the Session's duration. Each Session is assigned a unique identifier, which is included as an attribute in the Logs, Events, and Spans generated during the Session's lifecycle. When a session reaches end of life, typically due to user inactivity or session timeout, a new session identifier will be assigned. The previous session identifier may be provided by the instrumentation so that telemetry backends can link the two sessions.

View Source
const (
	// SignalrConnectionStatusKey is the attribute Key conforming to the
	// "signalr.connection.status" semantic conventions. It represents the
	// signalR HTTP connection closure status.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'app_shutdown', 'timeout'
	SignalrConnectionStatusKey = attribute.Key("signalr.connection.status")

	// SignalrTransportKey is the attribute Key conforming to the
	// "signalr.transport" semantic conventions. It represents the [SignalR
	// transport
	// type](https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/TransportProtocols.md)
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'web_sockets', 'long_polling'
	SignalrTransportKey = attribute.Key("signalr.transport")
)

SignalR attributes

View Source
const (
	// SourceAddressKey is the attribute Key conforming to the "source.address"
	// semantic conventions. It represents the source address - domain name if
	// available without reverse DNS lookup; otherwise, IP address or Unix
	// domain socket name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'source.example.com', '10.1.2.80', '/tmp/my.sock'
	// Note: When observed from the destination side, and when communicating
	// through an intermediary, `source.address` SHOULD represent the source
	// address behind any intermediaries, for example proxies, if it's
	// available.
	SourceAddressKey = attribute.Key("source.address")

	// SourcePortKey is the attribute Key conforming to the "source.port"
	// semantic conventions. It represents the source port number
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 3389, 2888
	SourcePortKey = attribute.Key("source.port")
)

These attributes may be used to describe the sender of a network exchange/packet. These should be used when there is no client/server relationship between the two sides, or when that relationship is unknown. This covers low-level network interactions (e.g. packet tracing) where you don't know if there was a connection or which side initiated it. This also covers unidirectional UDP flows and peer-to-peer communication where the "user-facing" surface of the protocol / API doesn't expose a clear notion of client and server.

View Source
const (
	// SystemCPULogicalNumberKey is the attribute Key conforming to the
	// "system.cpu.logical_number" semantic conventions. It represents the
	// logical CPU number [0..n-1]
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 1
	SystemCPULogicalNumberKey = attribute.Key("system.cpu.logical_number")

	// SystemCPUStateKey is the attribute Key conforming to the
	// "system.cpu.state" semantic conventions. It represents the state of the
	// CPU
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'idle', 'interrupt'
	SystemCPUStateKey = attribute.Key("system.cpu.state")
)

Describes System CPU attributes

View Source
const (
	// SystemPagingDirectionKey is the attribute Key conforming to the
	// "system.paging.direction" semantic conventions. It represents the paging
	// access direction
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'in'
	SystemPagingDirectionKey = attribute.Key("system.paging.direction")

	// SystemPagingStateKey is the attribute Key conforming to the
	// "system.paging.state" semantic conventions. It represents the memory
	// paging state
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'free'
	SystemPagingStateKey = attribute.Key("system.paging.state")

	// SystemPagingTypeKey is the attribute Key conforming to the
	// "system.paging.type" semantic conventions. It represents the memory
	// paging type
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'minor'
	SystemPagingTypeKey = attribute.Key("system.paging.type")
)

Describes System Memory Paging attributes

View Source
const (
	// SystemFilesystemModeKey is the attribute Key conforming to the
	// "system.filesystem.mode" semantic conventions. It represents the
	// filesystem mode
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'rw, ro'
	SystemFilesystemModeKey = attribute.Key("system.filesystem.mode")

	// SystemFilesystemMountpointKey is the attribute Key conforming to the
	// "system.filesystem.mountpoint" semantic conventions. It represents the
	// filesystem mount path
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/mnt/data'
	SystemFilesystemMountpointKey = attribute.Key("system.filesystem.mountpoint")

	// SystemFilesystemStateKey is the attribute Key conforming to the
	// "system.filesystem.state" semantic conventions. It represents the
	// filesystem state
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'used'
	SystemFilesystemStateKey = attribute.Key("system.filesystem.state")

	// SystemFilesystemTypeKey is the attribute Key conforming to the
	// "system.filesystem.type" semantic conventions. It represents the
	// filesystem type
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'ext4'
	SystemFilesystemTypeKey = attribute.Key("system.filesystem.type")
)

Describes Filesystem attributes

View Source
const (
	// TelemetrySDKLanguageKey is the attribute Key conforming to the
	// "telemetry.sdk.language" semantic conventions. It represents the
	// language of the telemetry SDK.
	//
	// Type: Enum
	// RequirementLevel: Required
	// Stability: stable
	TelemetrySDKLanguageKey = attribute.Key("telemetry.sdk.language")

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

	// TelemetrySDKVersionKey is the attribute Key conforming to the
	// "telemetry.sdk.version" semantic conventions. It represents the version
	// string of the telemetry SDK.
	//
	// Type: string
	// RequirementLevel: Required
	// Stability: stable
	// Examples: '1.2.3'
	TelemetrySDKVersionKey = attribute.Key("telemetry.sdk.version")

	// TelemetryDistroNameKey is the attribute Key conforming to the
	// "telemetry.distro.name" semantic conventions. It represents the name of
	// the auto instrumentation agent or distribution, if used.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'parts-unlimited-java'
	// Note: Official auto instrumentation agents and distributions SHOULD set
	// the `telemetry.distro.name` attribute to
	// a string starting with `opentelemetry-`, e.g.
	// `opentelemetry-java-instrumentation`.
	TelemetryDistroNameKey = attribute.Key("telemetry.distro.name")

	// TelemetryDistroVersionKey is the attribute Key conforming to the
	// "telemetry.distro.version" semantic conventions. It represents the
	// version string of the auto instrumentation agent or distribution, if
	// used.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '1.2.3'
	TelemetryDistroVersionKey = attribute.Key("telemetry.distro.version")
)

Attributes for telemetry SDK.

View Source
const (
	// ThreadIDKey is the attribute Key conforming to the "thread.id" semantic
	// conventions. It represents the current "managed" thread ID (as opposed
	// to OS thread ID).
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 42
	ThreadIDKey = attribute.Key("thread.id")

	// ThreadNameKey is the attribute Key conforming to the "thread.name"
	// semantic conventions. It represents the current thread name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'main'
	ThreadNameKey = attribute.Key("thread.name")
)

These attributes may be used for any operation to store information about a thread that started a span.

View Source
const (
	// TLSCipherKey is the attribute Key conforming to the "tls.cipher"
	// semantic conventions. It represents the string indicating the
	// [cipher](https://datatracker.ietf.org/doc/html/rfc5246#appendix-A.5)
	// used during the current connection.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'TLS_RSA_WITH_3DES_EDE_CBC_SHA',
	// 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256'
	// Note: The values allowed for `tls.cipher` MUST be one of the
	// `Descriptions` of the [registered TLS Cipher
	// Suits](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#table-tls-parameters-4).
	TLSCipherKey = attribute.Key("tls.cipher")

	// TLSClientCertificateKey is the attribute Key conforming to the
	// "tls.client.certificate" semantic conventions. It represents the
	// pEM-encoded stand-alone certificate offered by the client. This is
	// usually mutually-exclusive of `client.certificate_chain` since this
	// value also exists in that list.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'MII...'
	TLSClientCertificateKey = attribute.Key("tls.client.certificate")

	// TLSClientCertificateChainKey is the attribute Key conforming to the
	// "tls.client.certificate_chain" semantic conventions. It represents the
	// array of PEM-encoded certificates that make up the certificate chain
	// offered by the client. This is usually mutually-exclusive of
	// `client.certificate` since that value should be the first certificate in
	// the chain.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'MII...', 'MI...'
	TLSClientCertificateChainKey = attribute.Key("tls.client.certificate_chain")

	// TLSClientHashMd5Key is the attribute Key conforming to the
	// "tls.client.hash.md5" semantic conventions. It represents the
	// certificate fingerprint using the MD5 digest of DER-encoded version of
	// certificate offered by the client. For consistency with other hash
	// values, this value should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '0F76C7F2C55BFD7D8E8B8F4BFBF0C9EC'
	TLSClientHashMd5Key = attribute.Key("tls.client.hash.md5")

	// TLSClientHashSha1Key is the attribute Key conforming to the
	// "tls.client.hash.sha1" semantic conventions. It represents the
	// certificate fingerprint using the SHA1 digest of DER-encoded version of
	// certificate offered by the client. For consistency with other hash
	// values, this value should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '9E393D93138888D288266C2D915214D1D1CCEB2A'
	TLSClientHashSha1Key = attribute.Key("tls.client.hash.sha1")

	// TLSClientHashSha256Key is the attribute Key conforming to the
	// "tls.client.hash.sha256" semantic conventions. It represents the
	// certificate fingerprint using the SHA256 digest of DER-encoded version
	// of certificate offered by the client. For consistency with other hash
	// values, this value should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// '0687F666A054EF17A08E2F2162EAB4CBC0D265E1D7875BE74BF3C712CA92DAF0'
	TLSClientHashSha256Key = attribute.Key("tls.client.hash.sha256")

	// TLSClientIssuerKey is the attribute Key conforming to the
	// "tls.client.issuer" semantic conventions. It represents the
	// distinguished name of
	// [subject](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6)
	// of the issuer of the x.509 certificate presented by the client.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'CN=Example Root CA, OU=Infrastructure Team, DC=example,
	// DC=com'
	TLSClientIssuerKey = attribute.Key("tls.client.issuer")

	// TLSClientJa3Key is the attribute Key conforming to the "tls.client.ja3"
	// semantic conventions. It represents a hash that identifies clients based
	// on how they perform an SSL/TLS handshake.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'd4e5b18d6b55c71272893221c96ba240'
	TLSClientJa3Key = attribute.Key("tls.client.ja3")

	// TLSClientNotAfterKey is the attribute Key conforming to the
	// "tls.client.not_after" semantic conventions. It represents the date/Time
	// indicating when client certificate is no longer considered valid.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2021-01-01T00:00:00.000Z'
	TLSClientNotAfterKey = attribute.Key("tls.client.not_after")

	// TLSClientNotBeforeKey is the attribute Key conforming to the
	// "tls.client.not_before" semantic conventions. It represents the
	// date/Time indicating when client certificate is first considered valid.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '1970-01-01T00:00:00.000Z'
	TLSClientNotBeforeKey = attribute.Key("tls.client.not_before")

	// TLSClientServerNameKey is the attribute Key conforming to the
	// "tls.client.server_name" semantic conventions. It represents the also
	// called an SNI, this tells the server which hostname to which the client
	// is attempting to connect to.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'opentelemetry.io'
	TLSClientServerNameKey = attribute.Key("tls.client.server_name")

	// TLSClientSubjectKey is the attribute Key conforming to the
	// "tls.client.subject" semantic conventions. It represents the
	// distinguished name of subject of the x.509 certificate presented by the
	// client.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'CN=myclient, OU=Documentation Team, DC=example, DC=com'
	TLSClientSubjectKey = attribute.Key("tls.client.subject")

	// TLSClientSupportedCiphersKey is the attribute Key conforming to the
	// "tls.client.supported_ciphers" semantic conventions. It represents the
	// array of ciphers offered by the client during the client hello.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '"TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
	// "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "..."'
	TLSClientSupportedCiphersKey = attribute.Key("tls.client.supported_ciphers")

	// TLSCurveKey is the attribute Key conforming to the "tls.curve" semantic
	// conventions. It represents the string indicating the curve used for the
	// given cipher, when applicable
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'secp256r1'
	TLSCurveKey = attribute.Key("tls.curve")

	// TLSEstablishedKey is the attribute Key conforming to the
	// "tls.established" semantic conventions. It represents the boolean flag
	// indicating if the TLS negotiation was successful and transitioned to an
	// encrypted tunnel.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: True
	TLSEstablishedKey = attribute.Key("tls.established")

	// TLSNextProtocolKey is the attribute Key conforming to the
	// "tls.next_protocol" semantic conventions. It represents the string
	// indicating the protocol being tunneled. Per the values in the [IANA
	// registry](https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids),
	// this string should be lower case.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'http/1.1'
	TLSNextProtocolKey = attribute.Key("tls.next_protocol")

	// TLSProtocolNameKey is the attribute Key conforming to the
	// "tls.protocol.name" semantic conventions. It represents the normalized
	// lowercase protocol name parsed from original string of the negotiated
	// [SSL/TLS protocol
	// version](https://www.openssl.org/docs/man1.1.1/man3/SSL_get_version.html#RETURN-VALUES)
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	TLSProtocolNameKey = attribute.Key("tls.protocol.name")

	// TLSProtocolVersionKey is the attribute Key conforming to the
	// "tls.protocol.version" semantic conventions. It represents the numeric
	// part of the version parsed from the original string of the negotiated
	// [SSL/TLS protocol
	// version](https://www.openssl.org/docs/man1.1.1/man3/SSL_get_version.html#RETURN-VALUES)
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '1.2', '3'
	TLSProtocolVersionKey = attribute.Key("tls.protocol.version")

	// TLSResumedKey is the attribute Key conforming to the "tls.resumed"
	// semantic conventions. It represents the boolean flag indicating if this
	// TLS connection was resumed from an existing TLS negotiation.
	//
	// Type: boolean
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: True
	TLSResumedKey = attribute.Key("tls.resumed")

	// TLSServerCertificateKey is the attribute Key conforming to the
	// "tls.server.certificate" semantic conventions. It represents the
	// pEM-encoded stand-alone certificate offered by the server. This is
	// usually mutually-exclusive of `server.certificate_chain` since this
	// value also exists in that list.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'MII...'
	TLSServerCertificateKey = attribute.Key("tls.server.certificate")

	// TLSServerCertificateChainKey is the attribute Key conforming to the
	// "tls.server.certificate_chain" semantic conventions. It represents the
	// array of PEM-encoded certificates that make up the certificate chain
	// offered by the server. This is usually mutually-exclusive of
	// `server.certificate` since that value should be the first certificate in
	// the chain.
	//
	// Type: string[]
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'MII...', 'MI...'
	TLSServerCertificateChainKey = attribute.Key("tls.server.certificate_chain")

	// TLSServerHashMd5Key is the attribute Key conforming to the
	// "tls.server.hash.md5" semantic conventions. It represents the
	// certificate fingerprint using the MD5 digest of DER-encoded version of
	// certificate offered by the server. For consistency with other hash
	// values, this value should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '0F76C7F2C55BFD7D8E8B8F4BFBF0C9EC'
	TLSServerHashMd5Key = attribute.Key("tls.server.hash.md5")

	// TLSServerHashSha1Key is the attribute Key conforming to the
	// "tls.server.hash.sha1" semantic conventions. It represents the
	// certificate fingerprint using the SHA1 digest of DER-encoded version of
	// certificate offered by the server. For consistency with other hash
	// values, this value should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '9E393D93138888D288266C2D915214D1D1CCEB2A'
	TLSServerHashSha1Key = attribute.Key("tls.server.hash.sha1")

	// TLSServerHashSha256Key is the attribute Key conforming to the
	// "tls.server.hash.sha256" semantic conventions. It represents the
	// certificate fingerprint using the SHA256 digest of DER-encoded version
	// of certificate offered by the server. For consistency with other hash
	// values, this value should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// '0687F666A054EF17A08E2F2162EAB4CBC0D265E1D7875BE74BF3C712CA92DAF0'
	TLSServerHashSha256Key = attribute.Key("tls.server.hash.sha256")

	// TLSServerIssuerKey is the attribute Key conforming to the
	// "tls.server.issuer" semantic conventions. It represents the
	// distinguished name of
	// [subject](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6)
	// of the issuer of the x.509 certificate presented by the client.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'CN=Example Root CA, OU=Infrastructure Team, DC=example,
	// DC=com'
	TLSServerIssuerKey = attribute.Key("tls.server.issuer")

	// TLSServerJa3sKey is the attribute Key conforming to the
	// "tls.server.ja3s" semantic conventions. It represents a hash that
	// identifies servers based on how they perform an SSL/TLS handshake.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'd4e5b18d6b55c71272893221c96ba240'
	TLSServerJa3sKey = attribute.Key("tls.server.ja3s")

	// TLSServerNotAfterKey is the attribute Key conforming to the
	// "tls.server.not_after" semantic conventions. It represents the date/Time
	// indicating when server certificate is no longer considered valid.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '2021-01-01T00:00:00.000Z'
	TLSServerNotAfterKey = attribute.Key("tls.server.not_after")

	// TLSServerNotBeforeKey is the attribute Key conforming to the
	// "tls.server.not_before" semantic conventions. It represents the
	// date/Time indicating when server certificate is first considered valid.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '1970-01-01T00:00:00.000Z'
	TLSServerNotBeforeKey = attribute.Key("tls.server.not_before")

	// TLSServerSubjectKey is the attribute Key conforming to the
	// "tls.server.subject" semantic conventions. It represents the
	// distinguished name of subject of the x.509 certificate presented by the
	// server.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'CN=myserver, OU=Documentation Team, DC=example, DC=com'
	TLSServerSubjectKey = attribute.Key("tls.server.subject")
)

Semantic convention attributes in the TLS namespace.

View Source
const (
	// URLDomainKey is the attribute Key conforming to the "url.domain"
	// semantic conventions. It represents the domain extracted from the
	// `url.full`, such as "opentelemetry.io".
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'www.foo.bar', 'opentelemetry.io', '3.12.167.2',
	// '[1080:0:0:0:8:800:200C:417A]'
	// Note: In some cases a URL may refer to an IP and/or port directly,
	// without a domain name. In this case, the IP address would go to the
	// domain field. If the URL contains a [literal IPv6
	// address](https://www.rfc-editor.org/rfc/rfc2732#section-2) enclosed by
	// `[` and `]`, the `[` and `]` characters should also be captured in the
	// domain field.
	URLDomainKey = attribute.Key("url.domain")

	// URLExtensionKey is the attribute Key conforming to the "url.extension"
	// semantic conventions. It represents the file extension extracted from
	// the `url.full`, excluding the leading dot.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'png', 'gz'
	// Note: The file extension is only set if it exists, as not every url has
	// a file extension. When the file name has multiple extensions
	// `example.tar.gz`, only the last one should be captured `gz`, not
	// `tar.gz`.
	URLExtensionKey = attribute.Key("url.extension")

	// URLFragmentKey is the attribute Key conforming to the "url.fragment"
	// semantic conventions. It represents the [URI
	// fragment](https://www.rfc-editor.org/rfc/rfc3986#section-3.5) component
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'SemConv'
	URLFragmentKey = attribute.Key("url.fragment")

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
	// fragment is not transmitted over HTTP, but if it is known, it SHOULD be
	// included nevertheless.
	// `url.full` MUST NOT contain credentials passed via URL in form of
	// `https://username:password@www.example.com/`. In such case username and
	// password SHOULD be redacted and attribute's value SHOULD be
	// `https://REDACTED:REDACTED@www.example.com/`.
	// `url.full` SHOULD capture the absolute URL when it is available (or can
	// be reconstructed). Sensitive content provided in `url.full` SHOULD be
	// scrubbed when instrumentations can identify it.
	URLFullKey = attribute.Key("url.full")

	// URLOriginalKey is the attribute Key conforming to the "url.original"
	// semantic conventions. It represents the unmodified original URL as seen
	// in the event source.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'https://www.foo.bar/search?q=OpenTelemetry#SemConv',
	// 'search?q=OpenTelemetry'
	// Note: In network monitoring, the observed URL may be a full URL, whereas
	// in access logs, the URL is often just represented as a path. This field
	// is meant to represent the URL as it was observed, complete or not.
	// `url.original` might contain credentials passed via URL in form of
	// `https://username:password@www.example.com/`. In such case password and
	// username SHOULD NOT be redacted and attribute's value SHOULD remain the
	// same.
	URLOriginalKey = attribute.Key("url.original")

	// URLPathKey is the attribute Key conforming to the "url.path" semantic
	// conventions. It represents the [URI
	// path](https://www.rfc-editor.org/rfc/rfc3986#section-3.3) component
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: '/search'
	// Note: Sensitive content provided in `url.path` SHOULD be scrubbed when
	// instrumentations can identify it.
	URLPathKey = attribute.Key("url.path")

	// URLPortKey is the attribute Key conforming to the "url.port" semantic
	// conventions. It represents the port extracted from the `url.full`
	//
	// Type: int
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 443
	URLPortKey = attribute.Key("url.port")

	// URLQueryKey is the attribute Key conforming to the "url.query" semantic
	// conventions. It represents the [URI
	// query](https://www.rfc-editor.org/rfc/rfc3986#section-3.4) component
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'q=OpenTelemetry'
	// Note: Sensitive content provided in `url.query` SHOULD be scrubbed when
	// instrumentations can identify it.
	URLQueryKey = attribute.Key("url.query")

	// URLRegisteredDomainKey is the attribute Key conforming to the
	// "url.registered_domain" semantic conventions. It represents the highest
	// registered url domain, stripped of the subdomain.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'example.com', 'foo.co.uk'
	// Note: This value can be determined precisely with the [public suffix
	// list](http://publicsuffix.org). For example, the registered domain for
	// `foo.example.com` is `example.com`. Trying to approximate this by simply
	// taking the last two labels will not work well for TLDs such as `co.uk`.
	URLRegisteredDomainKey = attribute.Key("url.registered_domain")

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

	// URLSubdomainKey is the attribute Key conforming to the "url.subdomain"
	// semantic conventions. It represents the subdomain portion of a fully
	// qualified domain name includes all of the names except the host name
	// under the registered_domain. In a partially qualified domain, or if the
	// qualification level of the full name cannot be determined, subdomain
	// contains all of the names below the registered domain.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'east', 'sub2.sub1'
	// Note: The subdomain portion of `www.east.mydomain.co.uk` is `east`. If
	// the domain has multiple levels of subdomain, such as
	// `sub2.sub1.example.com`, the subdomain field should contain `sub2.sub1`,
	// with no trailing period.
	URLSubdomainKey = attribute.Key("url.subdomain")

	// URLTemplateKey is the attribute Key conforming to the "url.template"
	// semantic conventions. It represents the low-cardinality template of an
	// [absolute path
	// reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '/users/{id}', '/users/:id', '/users?id={id}'
	URLTemplateKey = attribute.Key("url.template")

	// URLTopLevelDomainKey is the attribute Key conforming to the
	// "url.top_level_domain" semantic conventions. It represents the effective
	// top level domain (eTLD), also known as the domain suffix, is the last
	// part of the domain name. For example, the top level domain for
	// example.com is `com`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'com', 'co.uk'
	// Note: This value can be determined precisely with the [public suffix
	// list](http://publicsuffix.org).
	URLTopLevelDomainKey = attribute.Key("url.top_level_domain")
)

Attributes describing URL.

View Source
const (
	// UserAgentNameKey is the attribute Key conforming to the
	// "user_agent.name" semantic conventions. It represents the name of the
	// user-agent extracted from original. Usually refers to the browser's
	// name.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'Safari', 'YourApp'
	// Note: [Example](https://www.whatsmyua.info) of extracting browser's name
	// from original string. In the case of using a user-agent for non-browser
	// products, such as microservices with multiple names/versions inside the
	// `user_agent.original`, the most significant name SHOULD be selected. In
	// such a scenario it should align with `user_agent.version`
	UserAgentNameKey = attribute.Key("user_agent.name")

	// UserAgentOriginalKey is the attribute Key conforming to the
	// "user_agent.original" semantic conventions. It represents the value of
	// the [HTTP
	// User-Agent](https://www.rfc-editor.org/rfc/rfc9110.html#field.user-agent)
	// header sent by the client.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'CERN-LineMode/2.15 libwww/2.17b3', 'Mozilla/5.0 (iPhone; CPU
	// iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)
	// Version/14.1.2 Mobile/15E148 Safari/604.1', 'YourApp/1.0.0
	// grpc-java-okhttp/1.27.2'
	UserAgentOriginalKey = attribute.Key("user_agent.original")

	// UserAgentVersionKey is the attribute Key conforming to the
	// "user_agent.version" semantic conventions. It represents the version of
	// the user-agent extracted from original. Usually refers to the browser's
	// version
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '14.1.2', '1.0.0'
	// Note: [Example](https://www.whatsmyua.info) of extracting browser's
	// version from original string. In the case of using a user-agent for
	// non-browser products, such as microservices with multiple names/versions
	// inside the `user_agent.original`, the most significant version SHOULD be
	// selected. In such a scenario it should align with `user_agent.name`
	UserAgentVersionKey = attribute.Key("user_agent.version")
)

Describes user-agent attributes.

View Source
const (
	// WebEngineDescriptionKey is the attribute Key conforming to the
	// "webengine.description" semantic conventions. It represents the
	// additional description of the web engine (e.g. detailed version and
	// edition information).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'WildFly Full 21.0.0.Final (WildFly Core 13.0.1.Final) -
	// 2.2.2.Final'
	WebEngineDescriptionKey = attribute.Key("webengine.description")

	// WebEngineNameKey is the attribute Key conforming to the "webengine.name"
	// semantic conventions. It represents the name of the web engine.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'WildFly'
	WebEngineNameKey = attribute.Key("webengine.name")

	// WebEngineVersionKey is the attribute Key conforming to the
	// "webengine.version" semantic conventions. It represents the version of
	// the web engine.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '21.0.0'
	WebEngineVersionKey = attribute.Key("webengine.version")
)

The attributes used to describe the packaged software running the application code.

View Source
const (

	// ContainerCPUTime is the metric conforming to the "container.cpu.time"
	// semantic conventions. It represents the total CPU time consumed.
	// Instrument: counter
	// Unit: s
	// Stability: Experimental
	ContainerCPUTimeName        = "container.cpu.time"
	ContainerCPUTimeUnit        = "s"
	ContainerCPUTimeDescription = "Total CPU time consumed"

	// ContainerMemoryUsage is the metric conforming to the
	// "container.memory.usage" semantic conventions. It represents the memory
	// usage of the container.
	// Instrument: counter
	// Unit: By
	// Stability: Experimental
	ContainerMemoryUsageName        = "container.memory.usage"
	ContainerMemoryUsageUnit        = "By"
	ContainerMemoryUsageDescription = "Memory usage of the container."

	// ContainerDiskIo is the metric conforming to the "container.disk.io" semantic
	// conventions. It represents the disk bytes for the container.
	// Instrument: counter
	// Unit: By
	// Stability: Experimental
	ContainerDiskIoName        = "container.disk.io"
	ContainerDiskIoUnit        = "By"
	ContainerDiskIoDescription = "Disk bytes for the container."

	// ContainerNetworkIo is the metric conforming to the "container.network.io"
	// semantic conventions. It represents the network bytes for the container.
	// Instrument: counter
	// Unit: By
	// Stability: Experimental
	ContainerNetworkIoName        = "container.network.io"
	ContainerNetworkIoUnit        = "By"
	ContainerNetworkIoDescription = "Network bytes for the container."

	// DBClientOperationDuration is the metric conforming to the
	// "db.client.operation.duration" semantic conventions. It represents the
	// duration of database client operations.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	DBClientOperationDurationName        = "db.client.operation.duration"
	DBClientOperationDurationUnit        = "s"
	DBClientOperationDurationDescription = "Duration of database client operations."

	// DBClientConnectionCount is the metric conforming to the
	// "db.client.connection.count" semantic conventions. It represents the number
	// of connections that are currently in state described by the `state`
	// attribute.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionCountName        = "db.client.connection.count"
	DBClientConnectionCountUnit        = "{connection}"
	DBClientConnectionCountDescription = "The number of connections that are currently in state described by the `state` attribute"

	// DBClientConnectionIdleMax is the metric conforming to the
	// "db.client.connection.idle.max" semantic conventions. It represents the
	// maximum number of idle open connections allowed.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionIdleMaxName        = "db.client.connection.idle.max"
	DBClientConnectionIdleMaxUnit        = "{connection}"
	DBClientConnectionIdleMaxDescription = "The maximum number of idle open connections allowed"

	// DBClientConnectionIdleMin is the metric conforming to the
	// "db.client.connection.idle.min" semantic conventions. It represents the
	// minimum number of idle open connections allowed.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionIdleMinName        = "db.client.connection.idle.min"
	DBClientConnectionIdleMinUnit        = "{connection}"
	DBClientConnectionIdleMinDescription = "The minimum number of idle open connections allowed"

	// DBClientConnectionMax is the metric conforming to the
	// "db.client.connection.max" semantic conventions. It represents the maximum
	// number of open connections allowed.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionMaxName        = "db.client.connection.max"
	DBClientConnectionMaxUnit        = "{connection}"
	DBClientConnectionMaxDescription = "The maximum number of open connections allowed"

	// DBClientConnectionPendingRequests is the metric conforming to the
	// "db.client.connection.pending_requests" semantic conventions. It represents
	// the number of pending requests for an open connection, cumulative for the
	// entire pool.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: Experimental
	DBClientConnectionPendingRequestsName        = "db.client.connection.pending_requests"
	DBClientConnectionPendingRequestsUnit        = "{request}"
	DBClientConnectionPendingRequestsDescription = "The number of pending requests for an open connection, cumulative for the entire pool"

	// DBClientConnectionTimeouts is the metric conforming to the
	// "db.client.connection.timeouts" semantic conventions. It represents the
	// number of connection timeouts that have occurred trying to obtain a
	// connection from the pool.
	// Instrument: counter
	// Unit: {timeout}
	// Stability: Experimental
	DBClientConnectionTimeoutsName        = "db.client.connection.timeouts"
	DBClientConnectionTimeoutsUnit        = "{timeout}"
	DBClientConnectionTimeoutsDescription = "The number of connection timeouts that have occurred trying to obtain a connection from the pool"

	// DBClientConnectionCreateTime is the metric conforming to the
	// "db.client.connection.create_time" semantic conventions. It represents the
	// time it took to create a new connection.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	DBClientConnectionCreateTimeName        = "db.client.connection.create_time"
	DBClientConnectionCreateTimeUnit        = "s"
	DBClientConnectionCreateTimeDescription = "The time it took to create a new connection"

	// DBClientConnectionWaitTime is the metric conforming to the
	// "db.client.connection.wait_time" semantic conventions. It represents the
	// time it took to obtain an open connection from the pool.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	DBClientConnectionWaitTimeName        = "db.client.connection.wait_time"
	DBClientConnectionWaitTimeUnit        = "s"
	DBClientConnectionWaitTimeDescription = "The time it took to obtain an open connection from the pool"

	// DBClientConnectionUseTime is the metric conforming to the
	// "db.client.connection.use_time" semantic conventions. It represents the time
	// between borrowing a connection and returning it to the pool.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	DBClientConnectionUseTimeName        = "db.client.connection.use_time"
	DBClientConnectionUseTimeUnit        = "s"
	DBClientConnectionUseTimeDescription = "The time between borrowing a connection and returning it to the pool"

	// DBClientConnectionsUsage is the metric conforming to the
	// "db.client.connections.usage" semantic conventions. It represents the
	// deprecated, use `db.client.connection.count` instead.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionsUsageName        = "db.client.connections.usage"
	DBClientConnectionsUsageUnit        = "{connection}"
	DBClientConnectionsUsageDescription = "Deprecated, use `db.client.connection.count` instead."

	// DBClientConnectionsIdleMax is the metric conforming to the
	// "db.client.connections.idle.max" semantic conventions. It represents the
	// deprecated, use `db.client.connection.idle.max` instead.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionsIdleMaxName        = "db.client.connections.idle.max"
	DBClientConnectionsIdleMaxUnit        = "{connection}"
	DBClientConnectionsIdleMaxDescription = "Deprecated, use `db.client.connection.idle.max` instead."

	// DBClientConnectionsIdleMin is the metric conforming to the
	// "db.client.connections.idle.min" semantic conventions. It represents the
	// deprecated, use `db.client.connection.idle.min` instead.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionsIdleMinName        = "db.client.connections.idle.min"
	DBClientConnectionsIdleMinUnit        = "{connection}"
	DBClientConnectionsIdleMinDescription = "Deprecated, use `db.client.connection.idle.min` instead."

	// DBClientConnectionsMax is the metric conforming to the
	// "db.client.connections.max" semantic conventions. It represents the
	// deprecated, use `db.client.connection.max` instead.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	DBClientConnectionsMaxName        = "db.client.connections.max"
	DBClientConnectionsMaxUnit        = "{connection}"
	DBClientConnectionsMaxDescription = "Deprecated, use `db.client.connection.max` instead."

	// DBClientConnectionsPendingRequests is the metric conforming to the
	// "db.client.connections.pending_requests" semantic conventions. It represents
	// the deprecated, use `db.client.connection.pending_requests` instead.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: Experimental
	DBClientConnectionsPendingRequestsName        = "db.client.connections.pending_requests"
	DBClientConnectionsPendingRequestsUnit        = "{request}"
	DBClientConnectionsPendingRequestsDescription = "Deprecated, use `db.client.connection.pending_requests` instead."

	// DBClientConnectionsTimeouts is the metric conforming to the
	// "db.client.connections.timeouts" semantic conventions. It represents the
	// deprecated, use `db.client.connection.timeouts` instead.
	// Instrument: counter
	// Unit: {timeout}
	// Stability: Experimental
	DBClientConnectionsTimeoutsName        = "db.client.connections.timeouts"
	DBClientConnectionsTimeoutsUnit        = "{timeout}"
	DBClientConnectionsTimeoutsDescription = "Deprecated, use `db.client.connection.timeouts` instead."

	// DBClientConnectionsCreateTime is the metric conforming to the
	// "db.client.connections.create_time" semantic conventions. It represents the
	// deprecated, use `db.client.connection.create_time` instead. Note: the unit
	// also changed from `ms` to `s`.
	// Instrument: histogram
	// Unit: ms
	// Stability: Experimental
	DBClientConnectionsCreateTimeName        = "db.client.connections.create_time"
	DBClientConnectionsCreateTimeUnit        = "ms"
	DBClientConnectionsCreateTimeDescription = "Deprecated, use `db.client.connection.create_time` instead. Note: the unit also changed from `ms` to `s`."

	// DBClientConnectionsWaitTime is the metric conforming to the
	// "db.client.connections.wait_time" semantic conventions. It represents the
	// deprecated, use `db.client.connection.wait_time` instead. Note: the unit
	// also changed from `ms` to `s`.
	// Instrument: histogram
	// Unit: ms
	// Stability: Experimental
	DBClientConnectionsWaitTimeName        = "db.client.connections.wait_time"
	DBClientConnectionsWaitTimeUnit        = "ms"
	DBClientConnectionsWaitTimeDescription = "Deprecated, use `db.client.connection.wait_time` instead. Note: the unit also changed from `ms` to `s`."

	// DBClientConnectionsUseTime is the metric conforming to the
	// "db.client.connections.use_time" semantic conventions. It represents the
	// deprecated, use `db.client.connection.use_time` instead. Note: the unit also
	// changed from `ms` to `s`.
	// Instrument: histogram
	// Unit: ms
	// Stability: Experimental
	DBClientConnectionsUseTimeName        = "db.client.connections.use_time"
	DBClientConnectionsUseTimeUnit        = "ms"
	DBClientConnectionsUseTimeDescription = "Deprecated, use `db.client.connection.use_time` instead. Note: the unit also changed from `ms` to `s`."

	// DNSLookupDuration is the metric conforming to the "dns.lookup.duration"
	// semantic conventions. It represents the measures the time taken to perform a
	// DNS lookup.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	DNSLookupDurationName        = "dns.lookup.duration"
	DNSLookupDurationUnit        = "s"
	DNSLookupDurationDescription = "Measures the time taken to perform a DNS lookup."

	// AspnetcoreRoutingMatchAttempts is the metric conforming to the
	// "aspnetcore.routing.match_attempts" semantic conventions. It represents the
	// number of requests that were attempted to be matched to an endpoint.
	// Instrument: counter
	// Unit: {match_attempt}
	// Stability: Stable
	AspnetcoreRoutingMatchAttemptsName        = "aspnetcore.routing.match_attempts"
	AspnetcoreRoutingMatchAttemptsUnit        = "{match_attempt}"
	AspnetcoreRoutingMatchAttemptsDescription = "Number of requests that were attempted to be matched to an endpoint."

	// AspnetcoreDiagnosticsExceptions is the metric conforming to the
	// "aspnetcore.diagnostics.exceptions" semantic conventions. It represents the
	// number of exceptions caught by exception handling middleware.
	// Instrument: counter
	// Unit: {exception}
	// Stability: Stable
	AspnetcoreDiagnosticsExceptionsName        = "aspnetcore.diagnostics.exceptions"
	AspnetcoreDiagnosticsExceptionsUnit        = "{exception}"
	AspnetcoreDiagnosticsExceptionsDescription = "Number of exceptions caught by exception handling middleware."

	// AspnetcoreRateLimitingActiveRequestLeases is the metric conforming to the
	// "aspnetcore.rate_limiting.active_request_leases" semantic conventions. It
	// represents the number of requests that are currently active on the server
	// that hold a rate limiting lease.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: Stable
	AspnetcoreRateLimitingActiveRequestLeasesName        = "aspnetcore.rate_limiting.active_request_leases"
	AspnetcoreRateLimitingActiveRequestLeasesUnit        = "{request}"
	AspnetcoreRateLimitingActiveRequestLeasesDescription = "Number of requests that are currently active on the server that hold a rate limiting lease."

	// AspnetcoreRateLimitingRequestLeaseDuration is the metric conforming to the
	// "aspnetcore.rate_limiting.request_lease.duration" semantic conventions. It
	// represents the duration of rate limiting lease held by requests on the
	// server.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	AspnetcoreRateLimitingRequestLeaseDurationName        = "aspnetcore.rate_limiting.request_lease.duration"
	AspnetcoreRateLimitingRequestLeaseDurationUnit        = "s"
	AspnetcoreRateLimitingRequestLeaseDurationDescription = "The duration of rate limiting lease held by requests on the server."

	// AspnetcoreRateLimitingRequestTimeInQueue is the metric conforming to the
	// "aspnetcore.rate_limiting.request.time_in_queue" semantic conventions. It
	// represents the time the request spent in a queue waiting to acquire a rate
	// limiting lease.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	AspnetcoreRateLimitingRequestTimeInQueueName        = "aspnetcore.rate_limiting.request.time_in_queue"
	AspnetcoreRateLimitingRequestTimeInQueueUnit        = "s"
	AspnetcoreRateLimitingRequestTimeInQueueDescription = "The time the request spent in a queue waiting to acquire a rate limiting lease."

	// AspnetcoreRateLimitingQueuedRequests is the metric conforming to the
	// "aspnetcore.rate_limiting.queued_requests" semantic conventions. It
	// represents the number of requests that are currently queued, waiting to
	// acquire a rate limiting lease.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: Stable
	AspnetcoreRateLimitingQueuedRequestsName        = "aspnetcore.rate_limiting.queued_requests"
	AspnetcoreRateLimitingQueuedRequestsUnit        = "{request}"
	AspnetcoreRateLimitingQueuedRequestsDescription = "Number of requests that are currently queued, waiting to acquire a rate limiting lease."

	// AspnetcoreRateLimitingRequests is the metric conforming to the
	// "aspnetcore.rate_limiting.requests" semantic conventions. It represents the
	// number of requests that tried to acquire a rate limiting lease.
	// Instrument: counter
	// Unit: {request}
	// Stability: Stable
	AspnetcoreRateLimitingRequestsName        = "aspnetcore.rate_limiting.requests"
	AspnetcoreRateLimitingRequestsUnit        = "{request}"
	AspnetcoreRateLimitingRequestsDescription = "Number of requests that tried to acquire a rate limiting lease."

	// KestrelActiveConnections is the metric conforming to the
	// "kestrel.active_connections" semantic conventions. It represents the number
	// of connections that are currently active on the server.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Stable
	KestrelActiveConnectionsName        = "kestrel.active_connections"
	KestrelActiveConnectionsUnit        = "{connection}"
	KestrelActiveConnectionsDescription = "Number of connections that are currently active on the server."

	// KestrelConnectionDuration is the metric conforming to the
	// "kestrel.connection.duration" semantic conventions. It represents the
	// duration of connections on the server.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	KestrelConnectionDurationName        = "kestrel.connection.duration"
	KestrelConnectionDurationUnit        = "s"
	KestrelConnectionDurationDescription = "The duration of connections on the server."

	// KestrelRejectedConnections is the metric conforming to the
	// "kestrel.rejected_connections" semantic conventions. It represents the
	// number of connections rejected by the server.
	// Instrument: counter
	// Unit: {connection}
	// Stability: Stable
	KestrelRejectedConnectionsName        = "kestrel.rejected_connections"
	KestrelRejectedConnectionsUnit        = "{connection}"
	KestrelRejectedConnectionsDescription = "Number of connections rejected by the server."

	// KestrelQueuedConnections is the metric conforming to the
	// "kestrel.queued_connections" semantic conventions. It represents the number
	// of connections that are currently queued and are waiting to start.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Stable
	KestrelQueuedConnectionsName        = "kestrel.queued_connections"
	KestrelQueuedConnectionsUnit        = "{connection}"
	KestrelQueuedConnectionsDescription = "Number of connections that are currently queued and are waiting to start."

	// KestrelQueuedRequests is the metric conforming to the
	// "kestrel.queued_requests" semantic conventions. It represents the number of
	// HTTP requests on multiplexed connections (HTTP/2 and HTTP/3) that are
	// currently queued and are waiting to start.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: Stable
	KestrelQueuedRequestsName        = "kestrel.queued_requests"
	KestrelQueuedRequestsUnit        = "{request}"
	KestrelQueuedRequestsDescription = "Number of HTTP requests on multiplexed connections (HTTP/2 and HTTP/3) that are currently queued and are waiting to start."

	// KestrelUpgradedConnections is the metric conforming to the
	// "kestrel.upgraded_connections" semantic conventions. It represents the
	// number of connections that are currently upgraded (WebSockets). .
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Stable
	KestrelUpgradedConnectionsName        = "kestrel.upgraded_connections"
	KestrelUpgradedConnectionsUnit        = "{connection}"
	KestrelUpgradedConnectionsDescription = "Number of connections that are currently upgraded (WebSockets). ."

	// KestrelTLSHandshakeDuration is the metric conforming to the
	// "kestrel.tls_handshake.duration" semantic conventions. It represents the
	// duration of TLS handshakes on the server.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	KestrelTLSHandshakeDurationName        = "kestrel.tls_handshake.duration"
	KestrelTLSHandshakeDurationUnit        = "s"
	KestrelTLSHandshakeDurationDescription = "The duration of TLS handshakes on the server."

	// KestrelActiveTLSHandshakes is the metric conforming to the
	// "kestrel.active_tls_handshakes" semantic conventions. It represents the
	// number of TLS handshakes that are currently in progress on the server.
	// Instrument: updowncounter
	// Unit: {handshake}
	// Stability: Stable
	KestrelActiveTLSHandshakesName        = "kestrel.active_tls_handshakes"
	KestrelActiveTLSHandshakesUnit        = "{handshake}"
	KestrelActiveTLSHandshakesDescription = "Number of TLS handshakes that are currently in progress on the server."

	// SignalrServerConnectionDuration is the metric conforming to the
	// "signalr.server.connection.duration" semantic conventions. It represents the
	// duration of connections on the server.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	SignalrServerConnectionDurationName        = "signalr.server.connection.duration"
	SignalrServerConnectionDurationUnit        = "s"
	SignalrServerConnectionDurationDescription = "The duration of connections on the server."

	// SignalrServerActiveConnections is the metric conforming to the
	// "signalr.server.active_connections" semantic conventions. It represents the
	// number of connections that are currently active on the server.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Stable
	SignalrServerActiveConnectionsName        = "signalr.server.active_connections"
	SignalrServerActiveConnectionsUnit        = "{connection}"
	SignalrServerActiveConnectionsDescription = "Number of connections that are currently active on the server."

	// FaaSInvokeDuration is the metric conforming to the "faas.invoke_duration"
	// semantic conventions. It represents the measures the duration of the
	// function's logic execution.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	FaaSInvokeDurationName        = "faas.invoke_duration"
	FaaSInvokeDurationUnit        = "s"
	FaaSInvokeDurationDescription = "Measures the duration of the function's logic execution"

	// FaaSInitDuration is the metric conforming to the "faas.init_duration"
	// semantic conventions. It represents the measures the duration of the
	// function's initialization, such as a cold start.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	FaaSInitDurationName        = "faas.init_duration"
	FaaSInitDurationUnit        = "s"
	FaaSInitDurationDescription = "Measures the duration of the function's initialization, such as a cold start"

	// FaaSColdstarts is the metric conforming to the "faas.coldstarts" semantic
	// conventions. It represents the number of invocation cold starts.
	// Instrument: counter
	// Unit: {coldstart}
	// Stability: Experimental
	FaaSColdstartsName        = "faas.coldstarts"
	FaaSColdstartsUnit        = "{coldstart}"
	FaaSColdstartsDescription = "Number of invocation cold starts"

	// FaaSErrors is the metric conforming to the "faas.errors" semantic
	// conventions. It represents the number of invocation errors.
	// Instrument: counter
	// Unit: {error}
	// Stability: Experimental
	FaaSErrorsName        = "faas.errors"
	FaaSErrorsUnit        = "{error}"
	FaaSErrorsDescription = "Number of invocation errors"

	// FaaSInvocations is the metric conforming to the "faas.invocations" semantic
	// conventions. It represents the number of successful invocations.
	// Instrument: counter
	// Unit: {invocation}
	// Stability: Experimental
	FaaSInvocationsName        = "faas.invocations"
	FaaSInvocationsUnit        = "{invocation}"
	FaaSInvocationsDescription = "Number of successful invocations"

	// FaaSTimeouts is the metric conforming to the "faas.timeouts" semantic
	// conventions. It represents the number of invocation timeouts.
	// Instrument: counter
	// Unit: {timeout}
	// Stability: Experimental
	FaaSTimeoutsName        = "faas.timeouts"
	FaaSTimeoutsUnit        = "{timeout}"
	FaaSTimeoutsDescription = "Number of invocation timeouts"

	// FaaSMemUsage is the metric conforming to the "faas.mem_usage" semantic
	// conventions. It represents the distribution of max memory usage per
	// invocation.
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	FaaSMemUsageName        = "faas.mem_usage"
	FaaSMemUsageUnit        = "By"
	FaaSMemUsageDescription = "Distribution of max memory usage per invocation"

	// FaaSCPUUsage is the metric conforming to the "faas.cpu_usage" semantic
	// conventions. It represents the distribution of CPU usage per invocation.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	FaaSCPUUsageName        = "faas.cpu_usage"
	FaaSCPUUsageUnit        = "s"
	FaaSCPUUsageDescription = "Distribution of CPU usage per invocation"

	// FaaSNetIo is the metric conforming to the "faas.net_io" semantic
	// conventions. It represents the distribution of net I/O usage per invocation.
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	FaaSNetIoName        = "faas.net_io"
	FaaSNetIoUnit        = "By"
	FaaSNetIoDescription = "Distribution of net I/O usage per invocation"

	// HTTPServerRequestDuration is the metric conforming to the
	// "http.server.request.duration" semantic conventions. It represents the
	// duration of HTTP server requests.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	HTTPServerRequestDurationName        = "http.server.request.duration"
	HTTPServerRequestDurationUnit        = "s"
	HTTPServerRequestDurationDescription = "Duration of HTTP server requests."

	// HTTPServerActiveRequests is the metric conforming to the
	// "http.server.active_requests" semantic conventions. It represents the number
	// of active HTTP server requests.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: Experimental
	HTTPServerActiveRequestsName        = "http.server.active_requests"
	HTTPServerActiveRequestsUnit        = "{request}"
	HTTPServerActiveRequestsDescription = "Number of active HTTP server requests."

	// HTTPServerRequestBodySize is the metric conforming to the
	// "http.server.request.body.size" semantic conventions. It represents the size
	// of HTTP server request bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	HTTPServerRequestBodySizeName        = "http.server.request.body.size"
	HTTPServerRequestBodySizeUnit        = "By"
	HTTPServerRequestBodySizeDescription = "Size of HTTP server request bodies."

	// HTTPServerResponseBodySize is the metric conforming to the
	// "http.server.response.body.size" semantic conventions. It represents the
	// size of HTTP server response bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	HTTPServerResponseBodySizeName        = "http.server.response.body.size"
	HTTPServerResponseBodySizeUnit        = "By"
	HTTPServerResponseBodySizeDescription = "Size of HTTP server response bodies."

	// HTTPClientRequestDuration is the metric conforming to the
	// "http.client.request.duration" semantic conventions. It represents the
	// duration of HTTP client requests.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	HTTPClientRequestDurationName        = "http.client.request.duration"
	HTTPClientRequestDurationUnit        = "s"
	HTTPClientRequestDurationDescription = "Duration of HTTP client requests."

	// HTTPClientRequestBodySize is the metric conforming to the
	// "http.client.request.body.size" semantic conventions. It represents the size
	// of HTTP client request bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	HTTPClientRequestBodySizeName        = "http.client.request.body.size"
	HTTPClientRequestBodySizeUnit        = "By"
	HTTPClientRequestBodySizeDescription = "Size of HTTP client request bodies."

	// HTTPClientResponseBodySize is the metric conforming to the
	// "http.client.response.body.size" semantic conventions. It represents the
	// size of HTTP client response bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	HTTPClientResponseBodySizeName        = "http.client.response.body.size"
	HTTPClientResponseBodySizeUnit        = "By"
	HTTPClientResponseBodySizeDescription = "Size of HTTP client response bodies."

	// HTTPClientOpenConnections is the metric conforming to the
	// "http.client.open_connections" semantic conventions. It represents the
	// number of outbound HTTP connections that are currently active or idle on the
	// client.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	HTTPClientOpenConnectionsName        = "http.client.open_connections"
	HTTPClientOpenConnectionsUnit        = "{connection}"
	HTTPClientOpenConnectionsDescription = "Number of outbound HTTP connections that are currently active or idle on the client."

	// HTTPClientConnectionDuration is the metric conforming to the
	// "http.client.connection.duration" semantic conventions. It represents the
	// duration of the successfully established outbound HTTP connections.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	HTTPClientConnectionDurationName        = "http.client.connection.duration"
	HTTPClientConnectionDurationUnit        = "s"
	HTTPClientConnectionDurationDescription = "The duration of the successfully established outbound HTTP connections."

	// HTTPClientActiveRequests is the metric conforming to the
	// "http.client.active_requests" semantic conventions. It represents the number
	// of active HTTP requests.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: Experimental
	HTTPClientActiveRequestsName        = "http.client.active_requests"
	HTTPClientActiveRequestsUnit        = "{request}"
	HTTPClientActiveRequestsDescription = "Number of active HTTP requests."

	// JvmMemoryInit is the metric conforming to the "jvm.memory.init" semantic
	// conventions. It represents the measure of initial memory requested.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	JvmMemoryInitName        = "jvm.memory.init"
	JvmMemoryInitUnit        = "By"
	JvmMemoryInitDescription = "Measure of initial memory requested."

	// JvmSystemCPUUtilization is the metric conforming to the
	// "jvm.system.cpu.utilization" semantic conventions. It represents the recent
	// CPU utilization for the whole system as reported by the JVM.
	// Instrument: gauge
	// Unit: 1
	// Stability: Experimental
	JvmSystemCPUUtilizationName        = "jvm.system.cpu.utilization"
	JvmSystemCPUUtilizationUnit        = "1"
	JvmSystemCPUUtilizationDescription = "Recent CPU utilization for the whole system as reported by the JVM."

	// JvmSystemCPULoad1m is the metric conforming to the "jvm.system.cpu.load_1m"
	// semantic conventions. It represents the average CPU load of the whole system
	// for the last minute as reported by the JVM.
	// Instrument: gauge
	// Unit: {run_queue_item}
	// Stability: Experimental
	JvmSystemCPULoad1mName        = "jvm.system.cpu.load_1m"
	JvmSystemCPULoad1mUnit        = "{run_queue_item}"
	JvmSystemCPULoad1mDescription = "Average CPU load of the whole system for the last minute as reported by the JVM."

	// JvmBufferMemoryUsage is the metric conforming to the
	// "jvm.buffer.memory.usage" semantic conventions. It represents the measure of
	// memory used by buffers.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	JvmBufferMemoryUsageName        = "jvm.buffer.memory.usage"
	JvmBufferMemoryUsageUnit        = "By"
	JvmBufferMemoryUsageDescription = "Measure of memory used by buffers."

	// JvmBufferMemoryLimit is the metric conforming to the
	// "jvm.buffer.memory.limit" semantic conventions. It represents the measure of
	// total memory capacity of buffers.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	JvmBufferMemoryLimitName        = "jvm.buffer.memory.limit"
	JvmBufferMemoryLimitUnit        = "By"
	JvmBufferMemoryLimitDescription = "Measure of total memory capacity of buffers."

	// JvmBufferCount is the metric conforming to the "jvm.buffer.count" semantic
	// conventions. It represents the number of buffers in the pool.
	// Instrument: updowncounter
	// Unit: {buffer}
	// Stability: Experimental
	JvmBufferCountName        = "jvm.buffer.count"
	JvmBufferCountUnit        = "{buffer}"
	JvmBufferCountDescription = "Number of buffers in the pool."

	// JvmMemoryUsed is the metric conforming to the "jvm.memory.used" semantic
	// conventions. It represents the measure of memory used.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Stable
	JvmMemoryUsedName        = "jvm.memory.used"
	JvmMemoryUsedUnit        = "By"
	JvmMemoryUsedDescription = "Measure of memory used."

	// JvmMemoryCommitted is the metric conforming to the "jvm.memory.committed"
	// semantic conventions. It represents the measure of memory committed.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Stable
	JvmMemoryCommittedName        = "jvm.memory.committed"
	JvmMemoryCommittedUnit        = "By"
	JvmMemoryCommittedDescription = "Measure of memory committed."

	// JvmMemoryLimit is the metric conforming to the "jvm.memory.limit" semantic
	// conventions. It represents the measure of max obtainable memory.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Stable
	JvmMemoryLimitName        = "jvm.memory.limit"
	JvmMemoryLimitUnit        = "By"
	JvmMemoryLimitDescription = "Measure of max obtainable memory."

	// JvmMemoryUsedAfterLastGc is the metric conforming to the
	// "jvm.memory.used_after_last_gc" semantic conventions. It represents the
	// measure of memory used, as measured after the most recent garbage collection
	// event on this pool.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Stable
	JvmMemoryUsedAfterLastGcName        = "jvm.memory.used_after_last_gc"
	JvmMemoryUsedAfterLastGcUnit        = "By"
	JvmMemoryUsedAfterLastGcDescription = "Measure of memory used, as measured after the most recent garbage collection event on this pool."

	// JvmGcDuration is the metric conforming to the "jvm.gc.duration" semantic
	// conventions. It represents the duration of JVM garbage collection actions.
	// Instrument: histogram
	// Unit: s
	// Stability: Stable
	JvmGcDurationName        = "jvm.gc.duration"
	JvmGcDurationUnit        = "s"
	JvmGcDurationDescription = "Duration of JVM garbage collection actions."

	// JvmThreadCount is the metric conforming to the "jvm.thread.count" semantic
	// conventions. It represents the number of executing platform threads.
	// Instrument: updowncounter
	// Unit: {thread}
	// Stability: Stable
	JvmThreadCountName        = "jvm.thread.count"
	JvmThreadCountUnit        = "{thread}"
	JvmThreadCountDescription = "Number of executing platform threads."

	// JvmClassLoaded is the metric conforming to the "jvm.class.loaded" semantic
	// conventions. It represents the number of classes loaded since JVM start.
	// Instrument: counter
	// Unit: {class}
	// Stability: Stable
	JvmClassLoadedName        = "jvm.class.loaded"
	JvmClassLoadedUnit        = "{class}"
	JvmClassLoadedDescription = "Number of classes loaded since JVM start."

	// JvmClassUnloaded is the metric conforming to the "jvm.class.unloaded"
	// semantic conventions. It represents the number of classes unloaded since JVM
	// start.
	// Instrument: counter
	// Unit: {class}
	// Stability: Stable
	JvmClassUnloadedName        = "jvm.class.unloaded"
	JvmClassUnloadedUnit        = "{class}"
	JvmClassUnloadedDescription = "Number of classes unloaded since JVM start."

	// JvmClassCount is the metric conforming to the "jvm.class.count" semantic
	// conventions. It represents the number of classes currently loaded.
	// Instrument: updowncounter
	// Unit: {class}
	// Stability: Stable
	JvmClassCountName        = "jvm.class.count"
	JvmClassCountUnit        = "{class}"
	JvmClassCountDescription = "Number of classes currently loaded."

	// JvmCPUCount is the metric conforming to the "jvm.cpu.count" semantic
	// conventions. It represents the number of processors available to the Java
	// virtual machine.
	// Instrument: updowncounter
	// Unit: {cpu}
	// Stability: Stable
	JvmCPUCountName        = "jvm.cpu.count"
	JvmCPUCountUnit        = "{cpu}"
	JvmCPUCountDescription = "Number of processors available to the Java virtual machine."

	// JvmCPUTime is the metric conforming to the "jvm.cpu.time" semantic
	// conventions. It represents the cPU time used by the process as reported by
	// the JVM.
	// Instrument: counter
	// Unit: s
	// Stability: Stable
	JvmCPUTimeName        = "jvm.cpu.time"
	JvmCPUTimeUnit        = "s"
	JvmCPUTimeDescription = "CPU time used by the process as reported by the JVM."

	// JvmCPURecentUtilization is the metric conforming to the
	// "jvm.cpu.recent_utilization" semantic conventions. It represents the recent
	// CPU utilization for the process as reported by the JVM.
	// Instrument: gauge
	// Unit: 1
	// Stability: Stable
	JvmCPURecentUtilizationName        = "jvm.cpu.recent_utilization"
	JvmCPURecentUtilizationUnit        = "1"
	JvmCPURecentUtilizationDescription = "Recent CPU utilization for the process as reported by the JVM."

	// MessagingPublishDuration is the metric conforming to the
	// "messaging.publish.duration" semantic conventions. It represents the
	// measures the duration of publish operation.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	MessagingPublishDurationName        = "messaging.publish.duration"
	MessagingPublishDurationUnit        = "s"
	MessagingPublishDurationDescription = "Measures the duration of publish operation."

	// MessagingReceiveDuration is the metric conforming to the
	// "messaging.receive.duration" semantic conventions. It represents the
	// measures the duration of receive operation.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	MessagingReceiveDurationName        = "messaging.receive.duration"
	MessagingReceiveDurationUnit        = "s"
	MessagingReceiveDurationDescription = "Measures the duration of receive operation."

	// MessagingProcessDuration is the metric conforming to the
	// "messaging.process.duration" semantic conventions. It represents the
	// measures the duration of process operation.
	// Instrument: histogram
	// Unit: s
	// Stability: Experimental
	MessagingProcessDurationName        = "messaging.process.duration"
	MessagingProcessDurationUnit        = "s"
	MessagingProcessDurationDescription = "Measures the duration of process operation."

	// MessagingPublishMessages is the metric conforming to the
	// "messaging.publish.messages" semantic conventions. It represents the
	// measures the number of published messages.
	// Instrument: counter
	// Unit: {message}
	// Stability: Experimental
	MessagingPublishMessagesName        = "messaging.publish.messages"
	MessagingPublishMessagesUnit        = "{message}"
	MessagingPublishMessagesDescription = "Measures the number of published messages."

	// MessagingReceiveMessages is the metric conforming to the
	// "messaging.receive.messages" semantic conventions. It represents the
	// measures the number of received messages.
	// Instrument: counter
	// Unit: {message}
	// Stability: Experimental
	MessagingReceiveMessagesName        = "messaging.receive.messages"
	MessagingReceiveMessagesUnit        = "{message}"
	MessagingReceiveMessagesDescription = "Measures the number of received messages."

	// MessagingProcessMessages is the metric conforming to the
	// "messaging.process.messages" semantic conventions. It represents the
	// measures the number of processed messages.
	// Instrument: counter
	// Unit: {message}
	// Stability: Experimental
	MessagingProcessMessagesName        = "messaging.process.messages"
	MessagingProcessMessagesUnit        = "{message}"
	MessagingProcessMessagesDescription = "Measures the number of processed messages."

	// ProcessCPUTime is the metric conforming to the "process.cpu.time" semantic
	// conventions. It represents the total CPU seconds broken down by different
	// states.
	// Instrument: counter
	// Unit: s
	// Stability: Experimental
	ProcessCPUTimeName        = "process.cpu.time"
	ProcessCPUTimeUnit        = "s"
	ProcessCPUTimeDescription = "Total CPU seconds broken down by different states."

	// ProcessCPUUtilization is the metric conforming to the
	// "process.cpu.utilization" semantic conventions. It represents the difference
	// in process.cpu.time since the last measurement, divided by the elapsed time
	// and number of CPUs available to the process.
	// Instrument: gauge
	// Unit: 1
	// Stability: Experimental
	ProcessCPUUtilizationName        = "process.cpu.utilization"
	ProcessCPUUtilizationUnit        = "1"
	ProcessCPUUtilizationDescription = "" /* 131-byte string literal not displayed */

	// ProcessMemoryUsage is the metric conforming to the "process.memory.usage"
	// semantic conventions. It represents the amount of physical memory in use.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	ProcessMemoryUsageName        = "process.memory.usage"
	ProcessMemoryUsageUnit        = "By"
	ProcessMemoryUsageDescription = "The amount of physical memory in use."

	// ProcessMemoryVirtual is the metric conforming to the
	// "process.memory.virtual" semantic conventions. It represents the amount of
	// committed virtual memory.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	ProcessMemoryVirtualName        = "process.memory.virtual"
	ProcessMemoryVirtualUnit        = "By"
	ProcessMemoryVirtualDescription = "The amount of committed virtual memory."

	// ProcessDiskIo is the metric conforming to the "process.disk.io" semantic
	// conventions. It represents the disk bytes transferred.
	// Instrument: counter
	// Unit: By
	// Stability: Experimental
	ProcessDiskIoName        = "process.disk.io"
	ProcessDiskIoUnit        = "By"
	ProcessDiskIoDescription = "Disk bytes transferred."

	// ProcessNetworkIo is the metric conforming to the "process.network.io"
	// semantic conventions. It represents the network bytes transferred.
	// Instrument: counter
	// Unit: By
	// Stability: Experimental
	ProcessNetworkIoName        = "process.network.io"
	ProcessNetworkIoUnit        = "By"
	ProcessNetworkIoDescription = "Network bytes transferred."

	// ProcessThreadCount is the metric conforming to the "process.thread.count"
	// semantic conventions. It represents the process threads count.
	// Instrument: updowncounter
	// Unit: {thread}
	// Stability: Experimental
	ProcessThreadCountName        = "process.thread.count"
	ProcessThreadCountUnit        = "{thread}"
	ProcessThreadCountDescription = "Process threads count."

	// ProcessOpenFileDescriptorCount is the metric conforming to the
	// "process.open_file_descriptor.count" semantic conventions. It represents the
	// number of file descriptors in use by the process.
	// Instrument: updowncounter
	// Unit: {count}
	// Stability: Experimental
	ProcessOpenFileDescriptorCountName        = "process.open_file_descriptor.count"
	ProcessOpenFileDescriptorCountUnit        = "{count}"
	ProcessOpenFileDescriptorCountDescription = "Number of file descriptors in use by the process."

	// ProcessContextSwitches is the metric conforming to the
	// "process.context_switches" semantic conventions. It represents the number of
	// times the process has been context switched.
	// Instrument: counter
	// Unit: {count}
	// Stability: Experimental
	ProcessContextSwitchesName        = "process.context_switches"
	ProcessContextSwitchesUnit        = "{count}"
	ProcessContextSwitchesDescription = "Number of times the process has been context switched."

	// ProcessPagingFaults is the metric conforming to the "process.paging.faults"
	// semantic conventions. It represents the number of page faults the process
	// has made.
	// Instrument: counter
	// Unit: {fault}
	// Stability: Experimental
	ProcessPagingFaultsName        = "process.paging.faults"
	ProcessPagingFaultsUnit        = "{fault}"
	ProcessPagingFaultsDescription = "Number of page faults the process has made."

	// RPCServerDuration is the metric conforming to the "rpc.server.duration"
	// semantic conventions. It represents the measures the duration of inbound
	// RPC.
	// Instrument: histogram
	// Unit: ms
	// Stability: Experimental
	RPCServerDurationName        = "rpc.server.duration"
	RPCServerDurationUnit        = "ms"
	RPCServerDurationDescription = "Measures the duration of inbound RPC."

	// RPCServerRequestSize is the metric conforming to the
	// "rpc.server.request.size" semantic conventions. It represents the measures
	// the size of RPC request messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	RPCServerRequestSizeName        = "rpc.server.request.size"
	RPCServerRequestSizeUnit        = "By"
	RPCServerRequestSizeDescription = "Measures the size of RPC request messages (uncompressed)."

	// RPCServerResponseSize is the metric conforming to the
	// "rpc.server.response.size" semantic conventions. It represents the measures
	// the size of RPC response messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	RPCServerResponseSizeName        = "rpc.server.response.size"
	RPCServerResponseSizeUnit        = "By"
	RPCServerResponseSizeDescription = "Measures the size of RPC response messages (uncompressed)."

	// RPCServerRequestsPerRPC is the metric conforming to the
	// "rpc.server.requests_per_rpc" semantic conventions. It represents the
	// measures the number of messages received per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: Experimental
	RPCServerRequestsPerRPCName        = "rpc.server.requests_per_rpc"
	RPCServerRequestsPerRPCUnit        = "{count}"
	RPCServerRequestsPerRPCDescription = "Measures the number of messages received per RPC."

	// RPCServerResponsesPerRPC is the metric conforming to the
	// "rpc.server.responses_per_rpc" semantic conventions. It represents the
	// measures the number of messages sent per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: Experimental
	RPCServerResponsesPerRPCName        = "rpc.server.responses_per_rpc"
	RPCServerResponsesPerRPCUnit        = "{count}"
	RPCServerResponsesPerRPCDescription = "Measures the number of messages sent per RPC."

	// RPCClientDuration is the metric conforming to the "rpc.client.duration"
	// semantic conventions. It represents the measures the duration of outbound
	// RPC.
	// Instrument: histogram
	// Unit: ms
	// Stability: Experimental
	RPCClientDurationName        = "rpc.client.duration"
	RPCClientDurationUnit        = "ms"
	RPCClientDurationDescription = "Measures the duration of outbound RPC."

	// RPCClientRequestSize is the metric conforming to the
	// "rpc.client.request.size" semantic conventions. It represents the measures
	// the size of RPC request messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	RPCClientRequestSizeName        = "rpc.client.request.size"
	RPCClientRequestSizeUnit        = "By"
	RPCClientRequestSizeDescription = "Measures the size of RPC request messages (uncompressed)."

	// RPCClientResponseSize is the metric conforming to the
	// "rpc.client.response.size" semantic conventions. It represents the measures
	// the size of RPC response messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: Experimental
	RPCClientResponseSizeName        = "rpc.client.response.size"
	RPCClientResponseSizeUnit        = "By"
	RPCClientResponseSizeDescription = "Measures the size of RPC response messages (uncompressed)."

	// RPCClientRequestsPerRPC is the metric conforming to the
	// "rpc.client.requests_per_rpc" semantic conventions. It represents the
	// measures the number of messages received per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: Experimental
	RPCClientRequestsPerRPCName        = "rpc.client.requests_per_rpc"
	RPCClientRequestsPerRPCUnit        = "{count}"
	RPCClientRequestsPerRPCDescription = "Measures the number of messages received per RPC."

	// RPCClientResponsesPerRPC is the metric conforming to the
	// "rpc.client.responses_per_rpc" semantic conventions. It represents the
	// measures the number of messages sent per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: Experimental
	RPCClientResponsesPerRPCName        = "rpc.client.responses_per_rpc"
	RPCClientResponsesPerRPCUnit        = "{count}"
	RPCClientResponsesPerRPCDescription = "Measures the number of messages sent per RPC."

	// SystemCPUTime is the metric conforming to the "system.cpu.time" semantic
	// conventions. It represents the seconds each logical CPU spent on each mode.
	// Instrument: counter
	// Unit: s
	// Stability: Experimental
	SystemCPUTimeName        = "system.cpu.time"
	SystemCPUTimeUnit        = "s"
	SystemCPUTimeDescription = "Seconds each logical CPU spent on each mode"

	// SystemCPUUtilization is the metric conforming to the
	// "system.cpu.utilization" semantic conventions. It represents the difference
	// in system.cpu.time since the last measurement, divided by the elapsed time
	// and number of logical CPUs.
	// Instrument: gauge
	// Unit: 1
	// Stability: Experimental
	SystemCPUUtilizationName        = "system.cpu.utilization"
	SystemCPUUtilizationUnit        = "1"
	SystemCPUUtilizationDescription = "Difference in system.cpu.time since the last measurement, divided by the elapsed time and number of logical CPUs"

	// SystemCPUFrequency is the metric conforming to the "system.cpu.frequency"
	// semantic conventions. It represents the reports the current frequency of the
	// CPU in Hz.
	// Instrument: gauge
	// Unit: {Hz}
	// Stability: Experimental
	SystemCPUFrequencyName        = "system.cpu.frequency"
	SystemCPUFrequencyUnit        = "{Hz}"
	SystemCPUFrequencyDescription = "Reports the current frequency of the CPU in Hz"

	// SystemCPUPhysicalCount is the metric conforming to the
	// "system.cpu.physical.count" semantic conventions. It represents the reports
	// the number of actual physical processor cores on the hardware.
	// Instrument: updowncounter
	// Unit: {cpu}
	// Stability: Experimental
	SystemCPUPhysicalCountName        = "system.cpu.physical.count"
	SystemCPUPhysicalCountUnit        = "{cpu}"
	SystemCPUPhysicalCountDescription = "Reports the number of actual physical processor cores on the hardware"

	// SystemCPULogicalCount is the metric conforming to the
	// "system.cpu.logical.count" semantic conventions. It represents the reports
	// the number of logical (virtual) processor cores created by the operating
	// system to manage multitasking.
	// Instrument: updowncounter
	// Unit: {cpu}
	// Stability: Experimental
	SystemCPULogicalCountName        = "system.cpu.logical.count"
	SystemCPULogicalCountUnit        = "{cpu}"
	SystemCPULogicalCountDescription = "Reports the number of logical (virtual) processor cores created by the operating system to manage multitasking"

	// SystemMemoryUsage is the metric conforming to the "system.memory.usage"
	// semantic conventions. It represents the reports memory in use by state.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	SystemMemoryUsageName        = "system.memory.usage"
	SystemMemoryUsageUnit        = "By"
	SystemMemoryUsageDescription = "Reports memory in use by state."

	// SystemMemoryLimit is the metric conforming to the "system.memory.limit"
	// semantic conventions. It represents the total memory available in the
	// system.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	SystemMemoryLimitName        = "system.memory.limit"
	SystemMemoryLimitUnit        = "By"
	SystemMemoryLimitDescription = "Total memory available in the system."

	// SystemMemoryShared is the metric conforming to the "system.memory.shared"
	// semantic conventions. It represents the shared memory used (mostly by
	// tmpfs).
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	SystemMemorySharedName        = "system.memory.shared"
	SystemMemorySharedUnit        = "By"
	SystemMemorySharedDescription = "Shared memory used (mostly by tmpfs)."

	// SystemMemoryUtilization is the metric conforming to the
	// "system.memory.utilization" semantic conventions.
	// Instrument: gauge
	// Unit: 1
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemMemoryUtilizationName = "system.memory.utilization"
	SystemMemoryUtilizationUnit = "1"

	// SystemPagingUsage is the metric conforming to the "system.paging.usage"
	// semantic conventions. It represents the unix swap or windows pagefile usage.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	SystemPagingUsageName        = "system.paging.usage"
	SystemPagingUsageUnit        = "By"
	SystemPagingUsageDescription = "Unix swap or windows pagefile usage"

	// SystemPagingUtilization is the metric conforming to the
	// "system.paging.utilization" semantic conventions.
	// Instrument: gauge
	// Unit: 1
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemPagingUtilizationName = "system.paging.utilization"
	SystemPagingUtilizationUnit = "1"

	// SystemPagingFaults is the metric conforming to the "system.paging.faults"
	// semantic conventions.
	// Instrument: counter
	// Unit: {fault}
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemPagingFaultsName = "system.paging.faults"
	SystemPagingFaultsUnit = "{fault}"

	// SystemPagingOperations is the metric conforming to the
	// "system.paging.operations" semantic conventions.
	// Instrument: counter
	// Unit: {operation}
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemPagingOperationsName = "system.paging.operations"
	SystemPagingOperationsUnit = "{operation}"

	// SystemDiskIo is the metric conforming to the "system.disk.io" semantic
	// conventions.
	// Instrument: counter
	// Unit: By
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemDiskIoName = "system.disk.io"
	SystemDiskIoUnit = "By"

	// SystemDiskOperations is the metric conforming to the
	// "system.disk.operations" semantic conventions.
	// Instrument: counter
	// Unit: {operation}
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemDiskOperationsName = "system.disk.operations"
	SystemDiskOperationsUnit = "{operation}"

	// SystemDiskIoTime is the metric conforming to the "system.disk.io_time"
	// semantic conventions. It represents the time disk spent activated.
	// Instrument: counter
	// Unit: s
	// Stability: Experimental
	SystemDiskIoTimeName        = "system.disk.io_time"
	SystemDiskIoTimeUnit        = "s"
	SystemDiskIoTimeDescription = "Time disk spent activated"

	// SystemDiskOperationTime is the metric conforming to the
	// "system.disk.operation_time" semantic conventions. It represents the sum of
	// the time each operation took to complete.
	// Instrument: counter
	// Unit: s
	// Stability: Experimental
	SystemDiskOperationTimeName        = "system.disk.operation_time"
	SystemDiskOperationTimeUnit        = "s"
	SystemDiskOperationTimeDescription = "Sum of the time each operation took to complete"

	// SystemDiskMerged is the metric conforming to the "system.disk.merged"
	// semantic conventions.
	// Instrument: counter
	// Unit: {operation}
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemDiskMergedName = "system.disk.merged"
	SystemDiskMergedUnit = "{operation}"

	// SystemFilesystemUsage is the metric conforming to the
	// "system.filesystem.usage" semantic conventions.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemFilesystemUsageName = "system.filesystem.usage"
	SystemFilesystemUsageUnit = "By"

	// SystemFilesystemUtilization is the metric conforming to the
	// "system.filesystem.utilization" semantic conventions.
	// Instrument: gauge
	// Unit: 1
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemFilesystemUtilizationName = "system.filesystem.utilization"
	SystemFilesystemUtilizationUnit = "1"

	// SystemNetworkDropped is the metric conforming to the
	// "system.network.dropped" semantic conventions. It represents the count of
	// packets that are dropped or discarded even though there was no error.
	// Instrument: counter
	// Unit: {packet}
	// Stability: Experimental
	SystemNetworkDroppedName        = "system.network.dropped"
	SystemNetworkDroppedUnit        = "{packet}"
	SystemNetworkDroppedDescription = "Count of packets that are dropped or discarded even though there was no error"

	// SystemNetworkPackets is the metric conforming to the
	// "system.network.packets" semantic conventions.
	// Instrument: counter
	// Unit: {packet}
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemNetworkPacketsName = "system.network.packets"
	SystemNetworkPacketsUnit = "{packet}"

	// SystemNetworkErrors is the metric conforming to the "system.network.errors"
	// semantic conventions. It represents the count of network errors detected.
	// Instrument: counter
	// Unit: {error}
	// Stability: Experimental
	SystemNetworkErrorsName        = "system.network.errors"
	SystemNetworkErrorsUnit        = "{error}"
	SystemNetworkErrorsDescription = "Count of network errors detected"

	// SystemNetworkIo is the metric conforming to the "system.network.io" semantic
	// conventions.
	// Instrument: counter
	// Unit: By
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemNetworkIoName = "system.network.io"
	SystemNetworkIoUnit = "By"

	// SystemNetworkConnections is the metric conforming to the
	// "system.network.connections" semantic conventions.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: Experimental
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemNetworkConnectionsName = "system.network.connections"
	SystemNetworkConnectionsUnit = "{connection}"

	// SystemProcessCount is the metric conforming to the "system.process.count"
	// semantic conventions. It represents the total number of processes in each
	// state.
	// Instrument: updowncounter
	// Unit: {process}
	// Stability: Experimental
	SystemProcessCountName        = "system.process.count"
	SystemProcessCountUnit        = "{process}"
	SystemProcessCountDescription = "Total number of processes in each state"

	// SystemProcessCreated is the metric conforming to the
	// "system.process.created" semantic conventions. It represents the total
	// number of processes created over uptime of the host.
	// Instrument: counter
	// Unit: {process}
	// Stability: Experimental
	SystemProcessCreatedName        = "system.process.created"
	SystemProcessCreatedUnit        = "{process}"
	SystemProcessCreatedDescription = "Total number of processes created over uptime of the host"

	// SystemLinuxMemoryAvailable is the metric conforming to the
	// "system.linux.memory.available" semantic conventions. It represents an
	// estimate of how much memory is available for starting new applications,
	// without causing swapping.
	// Instrument: updowncounter
	// Unit: By
	// Stability: Experimental
	SystemLinuxMemoryAvailableName        = "system.linux.memory.available"
	SystemLinuxMemoryAvailableUnit        = "By"
	SystemLinuxMemoryAvailableDescription = "An estimate of how much memory is available for starting new applications, without causing swapping"
)
View Source
const (
	// AWSEKSClusterARNKey is the attribute Key conforming to the
	// "aws.eks.cluster.arn" semantic conventions. It represents the ARN of an
	// EKS cluster.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'arn:aws:ecs:us-west-2:123456789123:cluster/my-cluster'
	AWSEKSClusterARNKey = attribute.Key("aws.eks.cluster.arn")
)

Attributes for AWS Elastic Kubernetes Service (EKS).

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
	// Stability: experimental
	// Examples: 'arn:aws:lambda:us-east-1:123456:function:myfunction:myalias'
	// Note: This may be different from `cloud.resource_id` if an alias is
	// involved.
	AWSLambdaInvokedARNKey = attribute.Key("aws.lambda.invoked_arn")
)

Attributes for AWS Lambda.

View Source
const (
	// AWSRequestIDKey is the attribute Key conforming to the "aws.request_id"
	// semantic conventions. It represents the AWS request ID as returned in
	// the response headers `x-amz-request-id` or `x-amz-requestid`.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '79b9da39-b7ae-508a-a6bc-864b2829c622', 'C9ER4AJX75574TDJ'
	AWSRequestIDKey = attribute.Key("aws.request_id")
)

Generic attributes for AWS services.

View Source
const (
	// AndroidOSAPILevelKey is the attribute Key conforming to the
	// "android.os.api_level" semantic conventions. It represents the uniquely
	// identifies the framework API revision offered by a version
	// (`os.version`) of the android operating system. More information can be
	// found
	// [here](https://developer.android.com/guide/topics/manifest/uses-sdk-element#APILevels).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '33', '32'
	AndroidOSAPILevelKey = attribute.Key("android.os.api_level")
)

The Android platform on which the Android application is running.

View Source
const (
	// AndroidStateKey is the attribute Key conforming to the "android.state"
	// semantic conventions. It represents the deprecated use the
	// `device.app.lifecycle` event definition including `android.state` as a
	// payload field instead.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: The Android lifecycle states are defined in [Activity lifecycle
	// callbacks](https://developer.android.com/guide/components/activities/activity-lifecycle#lc),
	// and from which the `OS identifiers` are derived.
	AndroidStateKey = attribute.Key("android.state")
)

Attributes that represents an occurrence of a lifecycle transition on the Android platform.

View Source
const (
	// DNSQuestionNameKey is the attribute Key conforming to the
	// "dns.question.name" semantic conventions. It represents the name being
	// queried.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'www.example.com', 'opentelemetry.io'
	// Note: If the name field contains non-printable characters (below 32 or
	// above 126), those characters should be represented as escaped base 10
	// integers (\DDD). Back slashes and quotes should be escaped. Tabs,
	// carriage returns, and line feeds should be converted to \t, \r, and \n
	// respectively.
	DNSQuestionNameKey = attribute.Key("dns.question.name")
)

The shared attributes used to report a DNS query.

View Source
const (
	// DeploymentEnvironmentKey is the attribute Key conforming to the
	// "deployment.environment" semantic conventions. It represents the name of
	// the [deployment
	// environment](https://wikipedia.org/wiki/Deployment_environment) (aka
	// deployment tier).
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'staging', 'production'
	// Note: `deployment.environment` does not affect the uniqueness
	// constraints defined through
	// the `service.namespace`, `service.name` and `service.instance.id`
	// resource attributes.
	// This implies that resources carrying the following attribute
	// combinations MUST be
	// considered to be identifying the same service:
	//
	// * `service.name=frontend`, `deployment.environment=production`
	// * `service.name=frontend`, `deployment.environment=staging`.
	DeploymentEnvironmentKey = attribute.Key("deployment.environment")
)

Attributes for software deployments.

View Source
const (
	// DiskIoDirectionKey is the attribute Key conforming to the
	// "disk.io.direction" semantic conventions. It represents the disk IO
	// operation direction.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'read'
	DiskIoDirectionKey = attribute.Key("disk.io.direction")
)

These attributes may be used for any disk related operation.

View Source
const (
	// ErrorTypeKey is the attribute Key conforming to the "error.type"
	// semantic conventions. It represents the describes a class of error the
	// operation ended with.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: stable
	// Examples: 'timeout', 'java.net.UnknownHostException',
	// 'server_certificate_invalid', '500'
	// Note: The `error.type` SHOULD be predictable, and SHOULD have low
	// cardinality.
	//
	// When `error.type` is set to a type (e.g., an exception type), its
	// canonical class name identifying the type within the artifact SHOULD be
	// used.
	//
	// Instrumentations SHOULD document the list of errors they report.
	//
	// The cardinality of `error.type` within one instrumentation library
	// SHOULD be low.
	// Telemetry consumers that aggregate data from multiple instrumentation
	// libraries and applications
	// should be prepared for `error.type` to have high cardinality at query
	// time when no
	// additional filters are applied.
	//
	// If the operation has completed successfully, instrumentations SHOULD NOT
	// set `error.type`.
	//
	// If a specific domain defines its own set of error identifiers (such as
	// HTTP or gRPC status codes),
	// it's RECOMMENDED to:
	//
	// * Use a domain-specific attribute
	// * Set `error.type` to capture all errors, regardless of whether they are
	// defined within the domain-specific set or not.
	ErrorTypeKey = attribute.Key("error.type")
)

The shared attributes used to report an error.

View Source
const (
	// EventNameKey is the attribute Key conforming to the "event.name"
	// semantic conventions. It represents the identifies the class / type of
	// event.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'browser.mouse.click', 'device.app.lifecycle'
	// Note: Event names are subject to the same rules as [attribute
	// names](https://github.com/open-telemetry/opentelemetry-specification/tree/v1.33.0/specification/common/attribute-naming.md).
	// Notably, event names are namespaced to avoid collisions and provide a
	// clean separation of semantics for events in separate domains like
	// browser, mobile, and kubernetes.
	EventNameKey = attribute.Key("event.name")
)

Attributes for Events represented using Log Records.

View Source
const (
	// ExceptionEventName is the name of the Span event representing an exception.
	ExceptionEventName = "exception"
)
View Source
const (
	// LogIostreamKey is the attribute Key conforming to the "log.iostream"
	// semantic conventions. It represents the stream associated with the log.
	// See below for a list of well-known values.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	LogIostreamKey = attribute.Key("log.iostream")
)

Log attributes

View Source
const (
	// LogRecordUIDKey is the attribute Key conforming to the "log.record.uid"
	// semantic conventions. It represents a unique identifier for the Log
	// Record.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '01ARZ3NDEKTSV4RRFFQ69G5FAV'
	// Note: If an id is provided, other log records with the same id will be
	// considered duplicates and can be removed safely. This means, that two
	// distinguishable log records MUST have different values.
	// The id MAY be an [Universally Unique Lexicographically Sortable
	// Identifier (ULID)](https://github.com/ulid/spec), but other identifiers
	// (e.g. UUID) may be used as needed.
	LogRecordUIDKey = attribute.Key("log.record.uid")
)

The generic attributes that may be used in any Log Record.

View Source
const (
	// OciManifestDigestKey is the attribute Key conforming to the
	// "oci.manifest.digest" semantic conventions. It represents the digest of
	// the OCI image manifest. For container images specifically is the digest
	// by which the container image is known.
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples:
	// 'sha256:e4ca62c0d62f3e886e684806dfe9d4e0cda60d54986898173c1083856cfda0f4'
	// Note: Follows [OCI Image Manifest
	// Specification](https://github.com/opencontainers/image-spec/blob/main/manifest.md),
	// and specifically the [Digest
	// property](https://github.com/opencontainers/image-spec/blob/main/descriptor.md#digests).
	// An example can be found in [Example Image
	// Manifest](https://docs.docker.com/registry/spec/manifest-v2-2/#example-image-manifest).
	OciManifestDigestKey = attribute.Key("oci.manifest.digest")
)

An OCI image manifest.

View Source
const (
	// OpentracingRefTypeKey is the attribute Key conforming to the
	// "opentracing.ref_type" semantic conventions. It represents the
	// parent-child Reference type
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Note: The causal relationship between a child Span and a parent Span.
	OpentracingRefTypeKey = attribute.Key("opentracing.ref_type")
)

Attributes used by the OpenTracing Shim layer.

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
	// Stability: experimental
	// Examples: 'AuthTokenCache'
	PeerServiceKey = attribute.Key("peer.service")
)

Operations that access some remote service.

View Source
const (
	// ProcessCPUStateKey is the attribute Key conforming to the
	// "process.cpu.state" semantic conventions. It represents the CPU state of
	// the process.
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	ProcessCPUStateKey = attribute.Key("process.cpu.state")
)

Attributes for process CPU

View Source
const SchemaURL = "https://opentelemetry.io/schemas/1.26.0"

SchemaURL is the schema URL that matches the version of the semantic conventions that this package defines. Semconv packages starting from v1.4.0 must declare non-empty schema URL in the form https://opentelemetry.io/schemas/<version>

View Source
const (
	// SystemDeviceKey is the attribute Key conforming to the "system.device"
	// semantic conventions. It represents the device identifier
	//
	// Type: string
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: '(identifier)'
	SystemDeviceKey = attribute.Key("system.device")
)

Describes System attributes

View Source
const (
	// SystemMemoryStateKey is the attribute Key conforming to the
	// "system.memory.state" semantic conventions. It represents the memory
	// state
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'free', 'cached'
	SystemMemoryStateKey = attribute.Key("system.memory.state")
)

Describes System Memory attributes

View Source
const (
	// SystemNetworkStateKey is the attribute Key conforming to the
	// "system.network.state" semantic conventions. It represents a stateless
	// protocol MUST NOT set this attribute
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'close_wait'
	SystemNetworkStateKey = attribute.Key("system.network.state")
)

Describes Network attributes

View Source
const (
	// SystemProcessStatusKey is the attribute Key conforming to the
	// "system.process.status" semantic conventions. It represents the process
	// state, e.g., [Linux Process State
	// Codes](https://man7.org/linux/man-pages/man1/ps.1.html#PROCESS_STATE_CODES)
	//
	// Type: Enum
	// RequirementLevel: Optional
	// Stability: experimental
	// Examples: 'running'
	SystemProcessStatusKey = attribute.Key("system.process.status")
)

Describes System Process attributes

Variables ¶
View Source
var (
	// Lease was acquired
	AspnetcoreRateLimitingResultAcquired = AspnetcoreRateLimitingResultKey.String("acquired")
	// Lease request was rejected by the endpoint limiter
	AspnetcoreRateLimitingResultEndpointLimiter = AspnetcoreRateLimitingResultKey.String("endpoint_limiter")
	// Lease request was rejected by the global limiter
	AspnetcoreRateLimitingResultGlobalLimiter = AspnetcoreRateLimitingResultKey.String("global_limiter")
	// Lease request was canceled
	AspnetcoreRateLimitingResultRequestCanceled = AspnetcoreRateLimitingResultKey.String("request_canceled")
)
View Source
var (
	// Exception was handled by the exception handling middleware
	AspnetcoreDiagnosticsExceptionResultHandled = AspnetcoreDiagnosticsExceptionResultKey.String("handled")
	// Exception was not handled by the exception handling middleware
	AspnetcoreDiagnosticsExceptionResultUnhandled = AspnetcoreDiagnosticsExceptionResultKey.String("unhandled")
	// Exception handling was skipped because the response had started
	AspnetcoreDiagnosticsExceptionResultSkipped = AspnetcoreDiagnosticsExceptionResultKey.String("skipped")
	// Exception handling didn't run because the request was aborted
	AspnetcoreDiagnosticsExceptionResultAborted = AspnetcoreDiagnosticsExceptionResultKey.String("aborted")
)
View Source
var (
	// Match succeeded
	AspnetcoreRoutingMatchStatusSuccess = AspnetcoreRoutingMatchStatusKey.String("success")
	// Match failed
	AspnetcoreRoutingMatchStatusFailure = AspnetcoreRoutingMatchStatusKey.String("failure")
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
	// Azure Container Apps
	CloudPlatformAzureContainerApps = CloudPlatformKey.String("azure_container_apps")
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
	// When tasks of the cgroup are in user mode (Linux). When all container processes are in user mode (Windows)
	ContainerCPUStateUser = ContainerCPUStateKey.String("user")
	// When CPU is used by the system (host OS)
	ContainerCPUStateSystem = ContainerCPUStateKey.String("system")
	// When tasks of the cgroup are in kernel mode (Linux). When all container processes are in kernel mode (Windows)
	ContainerCPUStateKernel = ContainerCPUStateKey.String("kernel")
)
View Source
var (
	// idle
	DBClientConnectionsStateIdle = DBClientConnectionsStateKey.String("idle")
	// used
	DBClientConnectionsStateUsed = DBClientConnectionsStateKey.String("used")
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
	// Gateway (HTTP) connections mode
	DBCosmosDBConnectionModeGateway = DBCosmosDBConnectionModeKey.String("gateway")
	// Direct connection
	DBCosmosDBConnectionModeDirect = DBCosmosDBConnectionModeKey.String("direct")
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
	// Any time before Activity.onResume() or, if the app has no Activity, Context.startService() has been called in the app for the first time
	AndroidStateCreated = AndroidStateKey.String("created")
	// Any time after Activity.onPause() or, if the app has no Activity, Context.stopService() has been called when the app was in the foreground state
	AndroidStateBackground = AndroidStateKey.String("background")
	// Any time after Activity.onResume() or, if the app has no Activity, Context.startService() has been called when the app was in either the created or background states
	AndroidStateForeground = AndroidStateKey.String("foreground")
)
View Source
var (
	// read
	DiskIoDirectionRead = DiskIoDirectionKey.String("read")
	// write
	DiskIoDirectionWrite = DiskIoDirectionKey.String("write")
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
	// GraphQL query
	GraphqlOperationTypeQuery = GraphqlOperationTypeKey.String("query")
	// GraphQL mutation
	GraphqlOperationTypeMutation = GraphqlOperationTypeKey.String("mutation")
	// GraphQL subscription
	GraphqlOperationTypeSubscription = GraphqlOperationTypeKey.String("subscription")
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
	// active state
	HTTPConnectionStateActive = HTTPConnectionStateKey.String("active")
	// idle state
	HTTPConnectionStateIdle = HTTPConnectionStateKey.String("idle")
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
	// Heap memory
	JvmMemoryTypeHeap = JvmMemoryTypeKey.String("heap")
	// Non-heap memory
	JvmMemoryTypeNonHeap = JvmMemoryTypeKey.String("non_heap")
)
View Source
var (
	// A thread that has not yet started is in this state
	JvmThreadStateNew = JvmThreadStateKey.String("new")
	// A thread executing in the Java virtual machine is in this state
	JvmThreadStateRunnable = JvmThreadStateKey.String("runnable")
	// A thread that is blocked waiting for a monitor lock is in this state
	JvmThreadStateBlocked = JvmThreadStateKey.String("blocked")
	// A thread that is waiting indefinitely for another thread to perform a particular action is in this state
	JvmThreadStateWaiting = JvmThreadStateKey.String("waiting")
	// A thread that is waiting for another thread to perform an action for up to a specified waiting time is in this state
	JvmThreadStateTimedWaiting = JvmThreadStateKey.String("timed_waiting")
	// A thread that has exited is in this state
	JvmThreadStateTerminated = JvmThreadStateKey.String("terminated")
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
	// One or more messages are provided for publishing to an intermediary. If a single message is published, the context of the "Publish" span can be used as the creation context and no "Create" span needs to be created
	MessagingOperationTypePublish = MessagingOperationTypeKey.String("publish")
	// A message is created. "Create" spans always refer to a single message and are used to provide a unique creation context for messages in batch publishing scenarios
	MessagingOperationTypeCreate = MessagingOperationTypeKey.String("create")
	// One or more messages are requested by a consumer. This operation refers to pull-based scenarios, where consumers explicitly call methods of messaging SDKs to receive messages
	MessagingOperationTypeReceive = MessagingOperationTypeKey.String("receive")
	// One or more messages are delivered to or processed by a consumer
	MessagingOperationTypeDeliver = MessagingOperationTypeKey.String("process")
	// One or more messages are settled
	MessagingOperationTypeSettle = MessagingOperationTypeKey.String("settle")
)
View Source
var (
	// Apache ActiveMQ
	MessagingSystemActivemq = MessagingSystemKey.String("activemq")
	// Amazon Simple Queue Service (SQS)
	MessagingSystemAWSSqs = MessagingSystemKey.String("aws_sqs")
	// Azure Event Grid
	MessagingSystemEventgrid = MessagingSystemKey.String("eventgrid")
	// Azure Event Hubs
	MessagingSystemEventhubs = MessagingSystemKey.String("eventhubs")
	// Azure Service Bus
	MessagingSystemServicebus = MessagingSystemKey.String("servicebus")
	// Google Cloud Pub/Sub
	MessagingSystemGCPPubsub = MessagingSystemKey.String("gcp_pubsub")
	// Java Message Service
	MessagingSystemJms = MessagingSystemKey.String("jms")
	// Apache Kafka
	MessagingSystemKafka = MessagingSystemKey.String("kafka")
	// RabbitMQ
	MessagingSystemRabbitmq = MessagingSystemKey.String("rabbitmq")
	// Apache RocketMQ
	MessagingSystemRocketmq = MessagingSystemKey.String("rocketmq")
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
	// Message is completed
	MessagingServicebusDispositionStatusComplete = MessagingServicebusDispositionStatusKey.String("complete")
	// Message is abandoned
	MessagingServicebusDispositionStatusAbandon = MessagingServicebusDispositionStatusKey.String("abandon")
	// Message is sent to dead letter queue
	MessagingServicebusDispositionStatusDeadLetter = MessagingServicebusDispositionStatusKey.String("dead_letter")
	// Message is deferred
	MessagingServicebusDispositionStatusDefer = MessagingServicebusDispositionStatusKey.String("defer")
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
	// transmit
	NetworkIoDirectionTransmit = NetworkIoDirectionKey.String("transmit")
	// receive
	NetworkIoDirectionReceive = NetworkIoDirectionKey.String("receive")
)
View Source
var (
	// TCP
	NetworkTransportTCP = NetworkTransportKey.String("tcp")
	// UDP
	NetworkTransportUDP = NetworkTransportKey.String("udp")
	// Named or anonymous pipe
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
	// The parent Span depends on the child Span in some capacity
	OpentracingRefTypeChildOf = OpentracingRefTypeKey.String("child_of")
	// The parent Span doesn't depend in any way on the result of the child Span
	OpentracingRefTypeFollowsFrom = OpentracingRefTypeKey.String("follows_from")
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
	// The operation has been validated by an Application developer or Operator to have completed successfully
	OTelStatusCodeOk = OTelStatusCodeKey.String("OK")
	// The operation contains an error
	OTelStatusCodeError = OTelStatusCodeKey.String("ERROR")
)
View Source
var (
	// voluntary
	ProcessContextSwitchTypeVoluntary = ProcessContextSwitchTypeKey.String("voluntary")
	// involuntary
	ProcessContextSwitchTypeInvoluntary = ProcessContextSwitchTypeKey.String("involuntary")
)
View Source
var (
	// major
	ProcessPagingFaultTypeMajor = ProcessPagingFaultTypeKey.String("major")
	// minor
	ProcessPagingFaultTypeMinor = ProcessPagingFaultTypeKey.String("minor")
)
View Source
var (
	// system
	ProcessCPUStateSystem = ProcessCPUStateKey.String("system")
	// user
	ProcessCPUStateUser = ProcessCPUStateKey.String("user")
	// wait
	ProcessCPUStateWait = ProcessCPUStateKey.String("wait")
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
	// sent
	RPCMessageTypeSent = RPCMessageTypeKey.String("SENT")
	// received
	RPCMessageTypeReceived = RPCMessageTypeKey.String("RECEIVED")
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
	// The connection was closed normally
	SignalrConnectionStatusNormalClosure = SignalrConnectionStatusKey.String("normal_closure")
	// The connection was closed due to a timeout
	SignalrConnectionStatusTimeout = SignalrConnectionStatusKey.String("timeout")
	// The connection was closed because the app is shutting down
	SignalrConnectionStatusAppShutdown = SignalrConnectionStatusKey.String("app_shutdown")
)
View Source
var (
	// ServerSentEvents protocol
	SignalrTransportServerSentEvents = SignalrTransportKey.String("server_sent_events")
	// LongPolling protocol
	SignalrTransportLongPolling = SignalrTransportKey.String("long_polling")
	// WebSockets protocol
	SignalrTransportWebSockets = SignalrTransportKey.String("web_sockets")
)
View Source
var (
	// user
	SystemCPUStateUser = SystemCPUStateKey.String("user")
	// system
	SystemCPUStateSystem = SystemCPUStateKey.String("system")
	// nice
	SystemCPUStateNice = SystemCPUStateKey.String("nice")
	// idle
	SystemCPUStateIdle = SystemCPUStateKey.String("idle")
	// iowait
	SystemCPUStateIowait = SystemCPUStateKey.String("iowait")
	// interrupt
	SystemCPUStateInterrupt = SystemCPUStateKey.String("interrupt")
	// steal
	SystemCPUStateSteal = SystemCPUStateKey.String("steal")
)
View Source
var (
	// used
	SystemMemoryStateUsed = SystemMemoryStateKey.String("used")
	// free
	SystemMemoryStateFree = SystemMemoryStateKey.String("free")
	// shared
	SystemMemoryStateShared = SystemMemoryStateKey.String("shared")
	// buffers
	SystemMemoryStateBuffers = SystemMemoryStateKey.String("buffers")
	// cached
	SystemMemoryStateCached = SystemMemoryStateKey.String("cached")
)
View Source
var (
	// in
	SystemPagingDirectionIn = SystemPagingDirectionKey.String("in")
	// out
	SystemPagingDirectionOut = SystemPagingDirectionKey.String("out")
)
View Source
var (
	// used
	SystemPagingStateUsed = SystemPagingStateKey.String("used")
	// free
	SystemPagingStateFree = SystemPagingStateKey.String("free")
)
View Source
var (
	// major
	SystemPagingTypeMajor = SystemPagingTypeKey.String("major")
	// minor
	SystemPagingTypeMinor = SystemPagingTypeKey.String("minor")
)
View Source
var (
	// used
	SystemFilesystemStateUsed = SystemFilesystemStateKey.String("used")
	// free
	SystemFilesystemStateFree = SystemFilesystemStateKey.String("free")
	// reserved
	SystemFilesystemStateReserved = SystemFilesystemStateKey.String("reserved")
)
View Source
var (
	// fat32
	SystemFilesystemTypeFat32 = SystemFilesystemTypeKey.String("fat32")
	// exfat
	SystemFilesystemTypeExfat = SystemFilesystemTypeKey.String("exfat")
	// ntfs
	SystemFilesystemTypeNtfs = SystemFilesystemTypeKey.String("ntfs")
	// refs
	SystemFilesystemTypeRefs = SystemFilesystemTypeKey.String("refs")
	// hfsplus
	SystemFilesystemTypeHfsplus = SystemFilesystemTypeKey.String("hfsplus")
	// ext4
	SystemFilesystemTypeExt4 = SystemFilesystemTypeKey.String("ext4")
)
View Source
var (
	// close
	SystemNetworkStateClose = SystemNetworkStateKey.String("close")
	// close_wait
	SystemNetworkStateCloseWait = SystemNetworkStateKey.String("close_wait")
	// closing
	SystemNetworkStateClosing = SystemNetworkStateKey.String("closing")
	// delete
	SystemNetworkStateDelete = SystemNetworkStateKey.String("delete")
	// established
	SystemNetworkStateEstablished = SystemNetworkStateKey.String("established")
	// fin_wait_1
	SystemNetworkStateFinWait1 = SystemNetworkStateKey.String("fin_wait_1")
	// fin_wait_2
	SystemNetworkStateFinWait2 = SystemNetworkStateKey.String("fin_wait_2")
	// last_ack
	SystemNetworkStateLastAck = SystemNetworkStateKey.String("last_ack")
	// listen
	SystemNetworkStateListen = SystemNetworkStateKey.String("listen")
	// syn_recv
	SystemNetworkStateSynRecv = SystemNetworkStateKey.String("syn_recv")
	// syn_sent
	SystemNetworkStateSynSent = SystemNetworkStateKey.String("syn_sent")
	// time_wait
	SystemNetworkStateTimeWait = SystemNetworkStateKey.String("time_wait")
)
View Source
var (
	// running
	SystemProcessStatusRunning = SystemProcessStatusKey.String("running")
	// sleeping
	SystemProcessStatusSleeping = SystemProcessStatusKey.String("sleeping")
	// stopped
	SystemProcessStatusStopped = SystemProcessStatusKey.String("stopped")
	// defunct
	SystemProcessStatusDefunct = SystemProcessStatusKey.String("defunct")
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
	// ssl
	TLSProtocolNameSsl = TLSProtocolNameKey.String("ssl")
	// tls
	TLSProtocolNameTLS = TLSProtocolNameKey.String("tls")
)
View Source
var (
	// A fallback error value to be used when the instrumentation doesn't define a custom value
	ErrorTypeOther = ErrorTypeKey.String("_OTHER")
)
View Source
var (
	// OpenAI
	GenAiSystemOpenai = GenAiSystemKey.String("openai")
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

AWSDynamoDBGlobalSecondaryIndexUpdates returns an attribute KeyValue conforming to the "aws.dynamodb.global_secondary_index_updates" semantic conventions. It represents the JSON-serialized value of each item in the `GlobalSecondaryIndexUpdates` request field.

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

AWSDynamoDBTableCount returns an attribute KeyValue conforming to the "aws.dynamodb.table_count" semantic conventions. It represents the number of items in the `TableNames` response parameter.

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

AWSECSTaskARN returns an attribute KeyValue conforming to the "aws.ecs.task.arn" semantic conventions. It represents the ARN of a running [ECS task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids).

func AWSECSTaskFamily ¶
func AWSECSTaskFamily(val string) attribute.KeyValue

AWSECSTaskFamily returns an attribute KeyValue conforming to the "aws.ecs.task.family" semantic conventions. It represents the family name of the [ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) used to create the ECS task.

func AWSECSTaskID ¶
func AWSECSTaskID(val string) attribute.KeyValue

AWSECSTaskID returns an attribute KeyValue conforming to the "aws.ecs.task.id" semantic conventions. It represents the ID of a running ECS task. The ID MUST be extracted from `task.arn`.

func AWSECSTaskRevision ¶
func AWSECSTaskRevision(val string) attribute.KeyValue

AWSECSTaskRevision returns an attribute KeyValue conforming to the "aws.ecs.task.revision" semantic conventions. It represents the revision for the task definition used to create the ECS task.

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

func AndroidOSAPILevel ¶
func AndroidOSAPILevel(val string) attribute.KeyValue

AndroidOSAPILevel returns an attribute KeyValue conforming to the "android.os.api_level" semantic conventions. It represents the uniquely identifies the framework API revision offered by a version (`os.version`) of the android operating system. More information can be found [here](https://developer.android.com/guide/topics/manifest/uses-sdk-element#APILevels).

func AspnetcoreDiagnosticsHandlerType ¶
func AspnetcoreDiagnosticsHandlerType(val string) attribute.KeyValue

AspnetcoreDiagnosticsHandlerType returns an attribute KeyValue conforming to the "aspnetcore.diagnostics.handler.type" semantic conventions. It represents the full type name of the [`IExceptionHandler`](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.diagnostics.iexceptionhandler) implementation that handled the exception.

func AspnetcoreRateLimitingPolicy ¶
func AspnetcoreRateLimitingPolicy(val string) attribute.KeyValue

AspnetcoreRateLimitingPolicy returns an attribute KeyValue conforming to the "aspnetcore.rate_limiting.policy" semantic conventions. It represents the rate limiting policy name.

func AspnetcoreRequestIsUnhandled ¶
func AspnetcoreRequestIsUnhandled(val bool) attribute.KeyValue

AspnetcoreRequestIsUnhandled returns an attribute KeyValue conforming to the "aspnetcore.request.is_unhandled" semantic conventions. It represents the flag indicating if request was handled by the application pipeline.

func AspnetcoreRoutingIsFallback ¶
func AspnetcoreRoutingIsFallback(val bool) attribute.KeyValue

AspnetcoreRoutingIsFallback returns an attribute KeyValue conforming to the "aspnetcore.routing.is_fallback" semantic conventions. It represents a value that indicates whether the matched route is a fallback route.

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

ClientAddress returns an attribute KeyValue conforming to the "client.address" semantic conventions. It represents the client address - domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

func ClientPort ¶
func ClientPort(val int) attribute.KeyValue

ClientPort returns an attribute KeyValue conforming to the "client.port" semantic conventions. It represents the client port number.

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

CloudResourceID returns an attribute KeyValue conforming to the "cloud.resource_id" semantic conventions. It represents the cloud provider-specific native identifier of the monitored cloud resource (e.g. an [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) on AWS, a [fully qualified resource ID](https://learn.microsoft.com/rest/api/resources/resources/get-by-id) on Azure, a [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) on GCP)

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

func CodeStacktrace ¶
func CodeStacktrace(val string) attribute.KeyValue

CodeStacktrace returns an attribute KeyValue conforming to the "code.stacktrace" semantic conventions. It represents a stacktrace as a string in the natural representation for the language runtime. The representation is to be determined and documented by each language SIG.

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

func ContainerImageRepoDigests ¶
func ContainerImageRepoDigests(val ...string) attribute.KeyValue

ContainerImageRepoDigests returns an attribute KeyValue conforming to the "container.image.repo_digests" semantic conventions. It represents the repo digests of the container image as provided by the container runtime.

func ContainerImageTags ¶
func ContainerImageTags(val ...string) attribute.KeyValue

ContainerImageTags returns an attribute KeyValue conforming to the "container.image.tags" semantic conventions. It represents the container image tags. An example can be found in [Docker Image Inspect](https://docs.docker.com/engine/api/v1.43/#tag/Image/operation/ImageInspect). Should be only the `<tag>` section of the full name for example from `registry.example.com/my-org/my-image:<tag>`.

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

func DBClientConnectionsPoolName ¶
func DBClientConnectionsPoolName(val string) attribute.KeyValue

DBClientConnectionsPoolName returns an attribute KeyValue conforming to the "db.client.connections.pool.name" semantic conventions. It represents the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation should use a combination of `server.address` and `server.port` attributes formatted as `server.address:server.port`.

func DBCollectionName ¶
func DBCollectionName(val string) attribute.KeyValue

DBCollectionName returns an attribute KeyValue conforming to the "db.collection.name" semantic conventions. It represents the name of a collection (table, container) within the database.

func DBCosmosDBClientID ¶
func DBCosmosDBClientID(val string) attribute.KeyValue

DBCosmosDBClientID returns an attribute KeyValue conforming to the "db.cosmosdb.client_id" semantic conventions. It represents the unique Cosmos client instance id.

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

func DBElasticsearchClusterName ¶
func DBElasticsearchClusterName(val string) attribute.KeyValue

DBElasticsearchClusterName returns an attribute KeyValue conforming to the "db.elasticsearch.cluster.name" semantic conventions. It represents the represents the identifier of an Elasticsearch cluster.

func DBElasticsearchNodeName ¶
func DBElasticsearchNodeName(val string) attribute.KeyValue

DBElasticsearchNodeName returns an attribute KeyValue conforming to the "db.elasticsearch.node.name" semantic conventions. It represents the represents the human-readable identifier of the node/instance to which a request was routed.

func DBNamespace ¶
func DBNamespace(val string) attribute.KeyValue

DBNamespace returns an attribute KeyValue conforming to the "db.namespace" semantic conventions. It represents the name of the database, fully qualified within the server address and port.

func DBOperationName ¶
func DBOperationName(val string) attribute.KeyValue

DBOperationName returns an attribute KeyValue conforming to the "db.operation.name" semantic conventions. It represents the name of the operation or command being executed.

func DBQueryText ¶
func DBQueryText(val string) attribute.KeyValue

DBQueryText returns an attribute KeyValue conforming to the "db.query.text" semantic conventions. It represents the database query being executed.

func DNSQuestionName ¶
func DNSQuestionName(val string) attribute.KeyValue

DNSQuestionName returns an attribute KeyValue conforming to the "dns.question.name" semantic conventions. It represents the name being queried.

func DeploymentEnvironment ¶
func DeploymentEnvironment(val string) attribute.KeyValue

DeploymentEnvironment returns an attribute KeyValue conforming to the "deployment.environment" semantic conventions. It represents the name of the [deployment environment](https://wikipedia.org/wiki/Deployment_environment) (aka deployment tier).

func DestinationAddress ¶
func DestinationAddress(val string) attribute.KeyValue

DestinationAddress returns an attribute KeyValue conforming to the "destination.address" semantic conventions. It represents the destination address - domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

func DestinationPort ¶
func DestinationPort(val int) attribute.KeyValue

DestinationPort returns an attribute KeyValue conforming to the "destination.port" semantic conventions. It represents the destination port number

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

EventName returns an attribute KeyValue conforming to the "event.name" semantic conventions. It represents the identifies the class / type of event.

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

func FileDirectory ¶
func FileDirectory(val string) attribute.KeyValue

FileDirectory returns an attribute KeyValue conforming to the "file.directory" semantic conventions. It represents the directory where the file is located. It should include the drive letter, when appropriate.

func FileExtension ¶
func FileExtension(val string) attribute.KeyValue

FileExtension returns an attribute KeyValue conforming to the "file.extension" semantic conventions. It represents the file extension, excluding the leading dot.

func FileName ¶
func FileName(val string) attribute.KeyValue

FileName returns an attribute KeyValue conforming to the "file.name" semantic conventions. It represents the name of the file including the extension, without the directory.

func FilePath ¶
func FilePath(val string) attribute.KeyValue

FilePath returns an attribute KeyValue conforming to the "file.path" semantic conventions. It represents the full path to the file, including the file name. It should include the drive letter, when appropriate.

func FileSize ¶
func FileSize(val int) attribute.KeyValue

FileSize returns an attribute KeyValue conforming to the "file.size" semantic conventions. It represents the file size in bytes.

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

func GenAiCompletion ¶
func GenAiCompletion(val string) attribute.KeyValue

GenAiCompletion returns an attribute KeyValue conforming to the "gen_ai.completion" semantic conventions. It represents the full response received from the LLM.

func GenAiPrompt ¶
func GenAiPrompt(val string) attribute.KeyValue

GenAiPrompt returns an attribute KeyValue conforming to the "gen_ai.prompt" semantic conventions. It represents the full prompt sent to an LLM.

func GenAiRequestMaxTokens ¶
func GenAiRequestMaxTokens(val int) attribute.KeyValue

GenAiRequestMaxTokens returns an attribute KeyValue conforming to the "gen_ai.request.max_tokens" semantic conventions. It represents the maximum number of tokens the LLM generates for a request.

func GenAiRequestModel ¶
func GenAiRequestModel(val string) attribute.KeyValue

GenAiRequestModel returns an attribute KeyValue conforming to the "gen_ai.request.model" semantic conventions. It represents the name of the LLM a request is being made to.

func GenAiRequestTemperature ¶
func GenAiRequestTemperature(val float64) attribute.KeyValue

GenAiRequestTemperature returns an attribute KeyValue conforming to the "gen_ai.request.temperature" semantic conventions. It represents the temperature setting for the LLM request.

func GenAiRequestTopP ¶
func GenAiRequestTopP(val float64) attribute.KeyValue

GenAiRequestTopP returns an attribute KeyValue conforming to the "gen_ai.request.top_p" semantic conventions. It represents the top_p sampling setting for the LLM request.

func GenAiResponseFinishReasons ¶
func GenAiResponseFinishReasons(val ...string) attribute.KeyValue

GenAiResponseFinishReasons returns an attribute KeyValue conforming to the "gen_ai.response.finish_reasons" semantic conventions. It represents the array of reasons the model stopped generating tokens, corresponding to each generation received.

func GenAiResponseID ¶
func GenAiResponseID(val string) attribute.KeyValue

GenAiResponseID returns an attribute KeyValue conforming to the "gen_ai.response.id" semantic conventions. It represents the unique identifier for the completion.

func GenAiResponseModel ¶
func GenAiResponseModel(val string) attribute.KeyValue

GenAiResponseModel returns an attribute KeyValue conforming to the "gen_ai.response.model" semantic conventions. It represents the name of the LLM a response was generated from.

func GenAiUsageCompletionTokens ¶
func GenAiUsageCompletionTokens(val int) attribute.KeyValue

GenAiUsageCompletionTokens returns an attribute KeyValue conforming to the "gen_ai.usage.completion_tokens" semantic conventions. It represents the number of tokens used in the LLM response (completion).

func GenAiUsagePromptTokens ¶
func GenAiUsagePromptTokens(val int) attribute.KeyValue

GenAiUsagePromptTokens returns an attribute KeyValue conforming to the "gen_ai.usage.prompt_tokens" semantic conventions. It represents the number of tokens used in the LLM prompt.

func GraphqlDocument ¶
func GraphqlDocument(val string) attribute.KeyValue

GraphqlDocument returns an attribute KeyValue conforming to the "graphql.document" semantic conventions. It represents the GraphQL document being executed.

func GraphqlOperationName ¶
func GraphqlOperationName(val string) attribute.KeyValue

GraphqlOperationName returns an attribute KeyValue conforming to the "graphql.operation.name" semantic conventions. It represents the name of the operation being executed.

func HTTPRequestBodySize ¶
func HTTPRequestBodySize(val int) attribute.KeyValue

HTTPRequestBodySize returns an attribute KeyValue conforming to the "http.request.body.size" semantic conventions. It represents the size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

func HTTPRequestMethodOriginal ¶
func HTTPRequestMethodOriginal(val string) attribute.KeyValue

HTTPRequestMethodOriginal returns an attribute KeyValue conforming to the "http.request.method_original" semantic conventions. It represents the original HTTP method sent by the client in the request line.

func HTTPRequestResendCount ¶
func HTTPRequestResendCount(val int) attribute.KeyValue

HTTPRequestResendCount returns an attribute KeyValue conforming to the "http.request.resend_count" semantic conventions. It represents the ordinal number of request resending attempt (for any reason, including redirects).

func HTTPRequestSize ¶
func HTTPRequestSize(val int) attribute.KeyValue

HTTPRequestSize returns an attribute KeyValue conforming to the "http.request.size" semantic conventions. It represents the total size of the request in bytes. This should be the total number of bytes sent over the wire, including the request line (HTTP/1.1), framing (HTTP/2 and HTTP/3), headers, and request body if any.

func HTTPResponseBodySize ¶
func HTTPResponseBodySize(val int) attribute.KeyValue

HTTPResponseBodySize returns an attribute KeyValue conforming to the "http.response.body.size" semantic conventions. It represents the size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Length](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size.

func HTTPResponseSize ¶
func HTTPResponseSize(val int) attribute.KeyValue

HTTPResponseSize returns an attribute KeyValue conforming to the "http.response.size" semantic conventions. It represents the total size of the response in bytes. This should be the total number of bytes sent over the wire, including the status line (HTTP/1.1), framing (HTTP/2 and HTTP/3), headers, and response body and trailers if any.

func HTTPResponseStatusCode ¶
func HTTPResponseStatusCode(val int) attribute.KeyValue

HTTPResponseStatusCode returns an attribute KeyValue conforming to the "http.response.status_code" semantic conventions. It represents the [HTTP response status code](https://tools.ietf.org/html/rfc7231#section-6).

func HTTPRoute ¶
func HTTPRoute(val string) attribute.KeyValue

HTTPRoute returns an attribute KeyValue conforming to the "http.route" semantic conventions. It represents the matched route, that is, the path template in the format used by the respective server framework.

func HerokuAppID ¶
func HerokuAppID(val string) attribute.KeyValue

HerokuAppID returns an attribute KeyValue conforming to the "heroku.app.id" semantic conventions. It represents the unique identifier for the application

func HerokuReleaseCommit ¶
func HerokuReleaseCommit(val string) attribute.KeyValue

HerokuReleaseCommit returns an attribute KeyValue conforming to the "heroku.release.commit" semantic conventions. It represents the commit hash for the current release

func HerokuReleaseCreationTimestamp ¶
func HerokuReleaseCreationTimestamp(val string) attribute.KeyValue

HerokuReleaseCreationTimestamp returns an attribute KeyValue conforming to the "heroku.release.creation_timestamp" semantic conventions. It represents the time and date the release was created

func HostCPUCacheL2Size ¶
func HostCPUCacheL2Size(val int) attribute.KeyValue

HostCPUCacheL2Size returns an attribute KeyValue conforming to the "host.cpu.cache.l2.size" semantic conventions. It represents the amount of level 2 memory cache available to the processor (in Bytes).

func HostCPUFamily ¶
func HostCPUFamily(val string) attribute.KeyValue

HostCPUFamily returns an attribute KeyValue conforming to the "host.cpu.family" semantic conventions. It represents the family or generation of the CPU.

func HostCPUModelID ¶
func HostCPUModelID(val string) attribute.KeyValue

HostCPUModelID returns an attribute KeyValue conforming to the "host.cpu.model.id" semantic conventions. It represents the model identifier. It provides more granular information about the CPU, distinguishing it from other CPUs within the same family.

func HostCPUModelName ¶
func HostCPUModelName(val string) attribute.KeyValue

HostCPUModelName returns an attribute KeyValue conforming to the "host.cpu.model.name" semantic conventions. It represents the model designation of the processor.

func HostCPUStepping ¶
func HostCPUStepping(val string) attribute.KeyValue

HostCPUStepping returns an attribute KeyValue conforming to the "host.cpu.stepping" semantic conventions. It represents the stepping or core revisions.

func HostCPUVendorID ¶
func HostCPUVendorID(val string) attribute.KeyValue

HostCPUVendorID returns an attribute KeyValue conforming to the "host.cpu.vendor.id" semantic conventions. It represents the processor manufacturer identifier. A maximum 12-character string.

func HostID ¶
func HostID(val string) attribute.KeyValue

HostID returns an attribute KeyValue conforming to the "host.id" semantic conventions. It represents the unique host ID. For Cloud, this must be the instance_id assigned by the cloud provider. For non-containerized systems, this should be the `machine-id`. See the table below for the sources to use to determine the `machine-id` based on operating system.

func HostIP ¶
func HostIP(val ...string) attribute.KeyValue

HostIP returns an attribute KeyValue conforming to the "host.ip" semantic conventions. It represents the available IP addresses of the host, excluding loopback interfaces.

func HostImageID ¶
func HostImageID(val string) attribute.KeyValue

HostImageID returns an attribute KeyValue conforming to the "host.image.id" semantic conventions. It represents the vM image ID or host OS image ID. For Cloud, this value is from the provider.

func HostImageName ¶
func HostImageName(val string) attribute.KeyValue

HostImageName returns an attribute KeyValue conforming to the "host.image.name" semantic conventions. It represents the name of the VM image or OS install the host was instantiated from.

func HostImageVersion ¶
func HostImageVersion(val string) attribute.KeyValue

HostImageVersion returns an attribute KeyValue conforming to the "host.image.version" semantic conventions. It represents the version string of the VM image or host OS as defined in [Version Attributes](/docs/resource/README.md#version-attributes).

func HostMac ¶
func HostMac(val ...string) attribute.KeyValue

HostMac returns an attribute KeyValue conforming to the "host.mac" semantic conventions. It represents the available MAC addresses of the host, excluding loopback interfaces.

func HostName ¶
func HostName(val string) attribute.KeyValue

HostName returns an attribute KeyValue conforming to the "host.name" semantic conventions. It represents the name of the host. On Unix systems, it may contain what the hostname command returns, or the fully qualified hostname, or another name specified by the user.

func HostType ¶
func HostType(val string) attribute.KeyValue

HostType returns an attribute KeyValue conforming to the "host.type" semantic conventions. It represents the type of host. For Cloud, this must be the machine type.

func JvmBufferPoolName ¶
func JvmBufferPoolName(val string) attribute.KeyValue

JvmBufferPoolName returns an attribute KeyValue conforming to the "jvm.buffer.pool.name" semantic conventions. It represents the name of the buffer pool.

func JvmGcAction ¶
func JvmGcAction(val string) attribute.KeyValue

JvmGcAction returns an attribute KeyValue conforming to the "jvm.gc.action" semantic conventions. It represents the name of the garbage collector action.

func JvmGcName ¶
func JvmGcName(val string) attribute.KeyValue

JvmGcName returns an attribute KeyValue conforming to the "jvm.gc.name" semantic conventions. It represents the name of the garbage collector.

func JvmMemoryPoolName ¶
func JvmMemoryPoolName(val string) attribute.KeyValue

JvmMemoryPoolName returns an attribute KeyValue conforming to the "jvm.memory.pool.name" semantic conventions. It represents the name of the memory pool.

func JvmThreadDaemon ¶
func JvmThreadDaemon(val bool) attribute.KeyValue

JvmThreadDaemon returns an attribute KeyValue conforming to the "jvm.thread.daemon" semantic conventions. It represents the whether the thread is daemon or not.

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

func K8SContainerStatusLastTerminatedReason ¶
func K8SContainerStatusLastTerminatedReason(val string) attribute.KeyValue

K8SContainerStatusLastTerminatedReason returns an attribute KeyValue conforming to the "k8s.container.status.last_terminated_reason" semantic conventions. It represents the last terminated reason of the Container.

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

func MessagingBatchMessageCount ¶
func MessagingBatchMessageCount(val int) attribute.KeyValue

MessagingBatchMessageCount returns an attribute KeyValue conforming to the "messaging.batch.message_count" semantic conventions. It represents the number of messages sent, received, or processed in the scope of the batching operation.

func MessagingClientID ¶
func MessagingClientID(val string) attribute.KeyValue

MessagingClientID returns an attribute KeyValue conforming to the "messaging.client.id" semantic conventions. It represents a unique identifier for the client that consumes or produces a message.

func MessagingDestinationAnonymous ¶
func MessagingDestinationAnonymous(val bool) attribute.KeyValue

MessagingDestinationAnonymous returns an attribute KeyValue conforming to the "messaging.destination.anonymous" semantic conventions. It represents a boolean that is true if the message destination is anonymous (could be unnamed or have auto-generated name).

func MessagingDestinationName ¶
func MessagingDestinationName(val string) attribute.KeyValue

MessagingDestinationName returns an attribute KeyValue conforming to the "messaging.destination.name" semantic conventions. It represents the message destination name

func MessagingDestinationPartitionID ¶
func MessagingDestinationPartitionID(val string) attribute.KeyValue

MessagingDestinationPartitionID returns an attribute KeyValue conforming to the "messaging.destination.partition.id" semantic conventions. It represents the identifier of the partition messages are sent to or received from, unique within the `messaging.destination.name`.

func MessagingDestinationPublishAnonymous ¶
func MessagingDestinationPublishAnonymous(val bool) attribute.KeyValue

MessagingDestinationPublishAnonymous returns an attribute KeyValue conforming to the "messaging.destination_publish.anonymous" semantic conventions. It represents a boolean that is true if the publish message destination is anonymous (could be unnamed or have auto-generated name).

func MessagingDestinationPublishName ¶
func MessagingDestinationPublishName(val string) attribute.KeyValue

MessagingDestinationPublishName returns an attribute KeyValue conforming to the "messaging.destination_publish.name" semantic conventions. It represents the name of the original destination the message was published to

func MessagingDestinationTemplate ¶
func MessagingDestinationTemplate(val string) attribute.KeyValue

MessagingDestinationTemplate returns an attribute KeyValue conforming to the "messaging.destination.template" semantic conventions. It represents the low cardinality representation of the messaging destination name

func MessagingDestinationTemporary ¶
func MessagingDestinationTemporary(val bool) attribute.KeyValue

MessagingDestinationTemporary returns an attribute KeyValue conforming to the "messaging.destination.temporary" semantic conventions. It represents a boolean that is true if the message destination is temporary and might not exist anymore after messages are processed.

func MessagingEventhubsConsumerGroup ¶
func MessagingEventhubsConsumerGroup(val string) attribute.KeyValue

MessagingEventhubsConsumerGroup returns an attribute KeyValue conforming to the "messaging.eventhubs.consumer.group" semantic conventions. It represents the name of the consumer group the event consumer is associated with.

func MessagingEventhubsMessageEnqueuedTime ¶
func MessagingEventhubsMessageEnqueuedTime(val int) attribute.KeyValue

MessagingEventhubsMessageEnqueuedTime returns an attribute KeyValue conforming to the "messaging.eventhubs.message.enqueued_time" semantic conventions. It represents the UTC epoch seconds at which the message has been accepted and stored in the entity.

func MessagingGCPPubsubMessageAckDeadline ¶
func MessagingGCPPubsubMessageAckDeadline(val int) attribute.KeyValue

MessagingGCPPubsubMessageAckDeadline returns an attribute KeyValue conforming to the "messaging.gcp_pubsub.message.ack_deadline" semantic conventions. It represents the ack deadline in seconds set for the modify ack deadline request.

func MessagingGCPPubsubMessageAckID ¶
func MessagingGCPPubsubMessageAckID(val string) attribute.KeyValue

MessagingGCPPubsubMessageAckID returns an attribute KeyValue conforming to the "messaging.gcp_pubsub.message.ack_id" semantic conventions. It represents the ack id for a given message.

func MessagingGCPPubsubMessageDeliveryAttempt ¶
func MessagingGCPPubsubMessageDeliveryAttempt(val int) attribute.KeyValue

MessagingGCPPubsubMessageDeliveryAttempt returns an attribute KeyValue conforming to the "messaging.gcp_pubsub.message.delivery_attempt" semantic conventions. It represents the delivery attempt for a given message.

func MessagingGCPPubsubMessageOrderingKey ¶
func MessagingGCPPubsubMessageOrderingKey(val string) attribute.KeyValue

MessagingGCPPubsubMessageOrderingKey returns an attribute KeyValue conforming to the "messaging.gcp_pubsub.message.ordering_key" semantic conventions. It represents the ordering key for a given message. If the attribute is not present, the message does not have an ordering key.

func MessagingKafkaConsumerGroup ¶
func MessagingKafkaConsumerGroup(val string) attribute.KeyValue

MessagingKafkaConsumerGroup returns an attribute KeyValue conforming to the "messaging.kafka.consumer.group" semantic conventions. It represents the name of the Kafka Consumer Group that is handling the message. Only applies to consumers, not producers.

func MessagingKafkaMessageKey ¶
func MessagingKafkaMessageKey(val string) attribute.KeyValue

MessagingKafkaMessageKey returns an attribute KeyValue conforming to the "messaging.kafka.message.key" semantic conventions. It represents the message keys in Kafka are used for grouping alike messages to ensure they're processed on the same partition. They differ from `messaging.message.id` in that they're not unique. If the key is `null`, the attribute MUST NOT be set.

func MessagingKafkaMessageOffset ¶
func MessagingKafkaMessageOffset(val int) attribute.KeyValue

MessagingKafkaMessageOffset returns an attribute KeyValue conforming to the "messaging.kafka.message.offset" semantic conventions. It represents the offset of a record in the corresponding Kafka partition.

func MessagingKafkaMessageTombstone ¶
func MessagingKafkaMessageTombstone(val bool) attribute.KeyValue

MessagingKafkaMessageTombstone returns an attribute KeyValue conforming to the "messaging.kafka.message.tombstone" semantic conventions. It represents a boolean that is true if the message is a tombstone.

func MessagingMessageBodySize ¶
func MessagingMessageBodySize(val int) attribute.KeyValue

MessagingMessageBodySize returns an attribute KeyValue conforming to the "messaging.message.body.size" semantic conventions. It represents the size of the message body in bytes.

func MessagingMessageConversationID ¶
func MessagingMessageConversationID(val string) attribute.KeyValue

MessagingMessageConversationID returns an attribute KeyValue conforming to the "messaging.message.conversation_id" semantic conventions. It represents the conversation ID identifying the conversation to which the message belongs, represented as a string. Sometimes called "Correlation ID".

func MessagingMessageEnvelopeSize ¶
func MessagingMessageEnvelopeSize(val int) attribute.KeyValue

MessagingMessageEnvelopeSize returns an attribute KeyValue conforming to the "messaging.message.envelope.size" semantic conventions. It represents the size of the message body and metadata in bytes.

func MessagingMessageID ¶
func MessagingMessageID(val string) attribute.KeyValue

MessagingMessageID returns an attribute KeyValue conforming to the "messaging.message.id" semantic conventions. It represents a value used by the messaging system as an identifier for the message, represented as a string.

func MessagingOperationName ¶
func MessagingOperationName(val string) attribute.KeyValue

MessagingOperationName returns an attribute KeyValue conforming to the "messaging.operation.name" semantic conventions. It represents the system-specific name of the messaging operation.

func MessagingRabbitmqDestinationRoutingKey ¶
func MessagingRabbitmqDestinationRoutingKey(val string) attribute.KeyValue

MessagingRabbitmqDestinationRoutingKey returns an attribute KeyValue conforming to the "messaging.rabbitmq.destination.routing_key" semantic conventions. It represents the rabbitMQ message routing key.

func MessagingRabbitmqMessageDeliveryTag ¶
func MessagingRabbitmqMessageDeliveryTag(val int) attribute.KeyValue

MessagingRabbitmqMessageDeliveryTag returns an attribute KeyValue conforming to the "messaging.rabbitmq.message.delivery_tag" semantic conventions. It represents the rabbitMQ message delivery tag

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

func MessagingServicebusDestinationSubscriptionName ¶
func MessagingServicebusDestinationSubscriptionName(val string) attribute.KeyValue

MessagingServicebusDestinationSubscriptionName returns an attribute KeyValue conforming to the "messaging.servicebus.destination.subscription_name" semantic conventions. It represents the name of the subscription in the topic messages are received from.

func MessagingServicebusMessageDeliveryCount ¶
func MessagingServicebusMessageDeliveryCount(val int) attribute.KeyValue

MessagingServicebusMessageDeliveryCount returns an attribute KeyValue conforming to the "messaging.servicebus.message.delivery_count" semantic conventions. It represents the number of deliveries that have been attempted for this message.

func MessagingServicebusMessageEnqueuedTime ¶
func MessagingServicebusMessageEnqueuedTime(val int) attribute.KeyValue

MessagingServicebusMessageEnqueuedTime returns an attribute KeyValue conforming to the "messaging.servicebus.message.enqueued_time" semantic conventions. It represents the UTC epoch seconds at which the message has been accepted and stored in the entity.

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

func NetworkLocalAddress ¶
func NetworkLocalAddress(val string) attribute.KeyValue

NetworkLocalAddress returns an attribute KeyValue conforming to the "network.local.address" semantic conventions. It represents the local address of the network connection - IP address or Unix domain socket name.

func NetworkLocalPort ¶
func NetworkLocalPort(val int) attribute.KeyValue

NetworkLocalPort returns an attribute KeyValue conforming to the "network.local.port" semantic conventions. It represents the local port number of the network connection.

func NetworkPeerAddress ¶
func NetworkPeerAddress(val string) attribute.KeyValue

NetworkPeerAddress returns an attribute KeyValue conforming to the "network.peer.address" semantic conventions. It represents the peer address of the network connection - IP address or Unix domain socket name.

func NetworkPeerPort ¶
func NetworkPeerPort(val int) attribute.KeyValue

NetworkPeerPort returns an attribute KeyValue conforming to the "network.peer.port" semantic conventions. It represents the peer port number of the network connection.

func NetworkProtocolName ¶
func NetworkProtocolName(val string) attribute.KeyValue

NetworkProtocolName returns an attribute KeyValue conforming to the "network.protocol.name" semantic conventions. It represents the [OSI application layer](https://osi-model.com/application-layer/) or non-OSI equivalent.

func NetworkProtocolVersion ¶
func NetworkProtocolVersion(val string) attribute.KeyValue

NetworkProtocolVersion returns an attribute KeyValue conforming to the "network.protocol.version" semantic conventions. It represents the actual version of the protocol used for network communication.

func OSBuildID ¶
func OSBuildID(val string) attribute.KeyValue

OSBuildID returns an attribute KeyValue conforming to the "os.build_id" semantic conventions. It represents the unique identifier for a particular build or compilation of the operating system.

func OSDescription ¶
func OSDescription(val string) attribute.KeyValue

OSDescription returns an attribute KeyValue conforming to the "os.description" semantic conventions. It represents the human readable (not intended to be parsed) OS version information, like e.g. reported by `ver` or `lsb_release -a` commands.

func OSName ¶
func OSName(val string) attribute.KeyValue

OSName returns an attribute KeyValue conforming to the "os.name" semantic conventions. It represents the human readable operating system name.

func OSVersion ¶
func OSVersion(val string) attribute.KeyValue

OSVersion returns an attribute KeyValue conforming to the "os.version" semantic conventions. It represents the version string of the operating system as defined in [Version Attributes](/docs/resource/README.md#version-attributes).

func OTelScopeName ¶
func OTelScopeName(val string) attribute.KeyValue

OTelScopeName returns an attribute KeyValue conforming to the "otel.scope.name" semantic conventions. It represents the name of the instrumentation scope - (`InstrumentationScope.Name` in OTLP).

func OTelScopeVersion ¶
func OTelScopeVersion(val string) attribute.KeyValue

OTelScopeVersion returns an attribute KeyValue conforming to the "otel.scope.version" semantic conventions. It represents the version of the instrumentation scope - (`InstrumentationScope.Version` in OTLP).

func OTelStatusDescription ¶
func OTelStatusDescription(val string) attribute.KeyValue

OTelStatusDescription returns an attribute KeyValue conforming to the "otel.status_description" semantic conventions. It represents the description of the Status if it has a value, otherwise not set.

func OciManifestDigest ¶
func OciManifestDigest(val string) attribute.KeyValue

OciManifestDigest returns an attribute KeyValue conforming to the "oci.manifest.digest" semantic conventions. It represents the digest of the OCI image manifest. For container images specifically is the digest by which the container image is known.

func PeerService ¶
func PeerService(val string) attribute.KeyValue

PeerService returns an attribute KeyValue conforming to the "peer.service" semantic conventions. It represents the [`service.name`](/docs/resource/README.md#service) of the remote service. SHOULD be equal to the actual `service.name` resource attribute of the remote service if any.

func ProcessCommand ¶
func ProcessCommand(val string) attribute.KeyValue

ProcessCommand returns an attribute KeyValue conforming to the "process.command" semantic conventions. It represents the command used to launch the process (i.e. the command name). On Linux based systems, can be set to the zeroth string in `proc/[pid]/cmdline`. On Windows, can be set to the first parameter extracted from `GetCommandLineW`.

func ProcessCommandArgs ¶
func ProcessCommandArgs(val ...string) attribute.KeyValue

ProcessCommandArgs returns an attribute KeyValue conforming to the "process.command_args" semantic conventions. It represents the all the command arguments (including the command/executable itself) as received by the process. On Linux-based systems (and some other Unixoid systems supporting procfs), can be set according to the list of null-delimited strings extracted from `proc/[pid]/cmdline`. For libc-based executables, this would be the full argv vector passed to `main`.

func ProcessCommandLine ¶
func ProcessCommandLine(val string) attribute.KeyValue

ProcessCommandLine returns an attribute KeyValue conforming to the "process.command_line" semantic conventions. It represents the full command used to launch the process as a single string representing the full command. On Windows, can be set to the result of `GetCommandLineW`. Do not set this if you have to assemble it just for monitoring; use `process.command_args` instead.

func ProcessCreationTime ¶
func ProcessCreationTime(val string) attribute.KeyValue

ProcessCreationTime returns an attribute KeyValue conforming to the "process.creation.time" semantic conventions. It represents the date and time the process was created, in ISO 8601 format.

func ProcessExecutableName ¶
func ProcessExecutableName(val string) attribute.KeyValue

ProcessExecutableName returns an attribute KeyValue conforming to the "process.executable.name" semantic conventions. It represents the name of the process executable. On Linux based systems, can be set to the `Name` in `proc/[pid]/status`. On Windows, can be set to the base name of `GetProcessImageFileNameW`.

func ProcessExecutablePath ¶
func ProcessExecutablePath(val string) attribute.KeyValue

ProcessExecutablePath returns an attribute KeyValue conforming to the "process.executable.path" semantic conventions. It represents the full path to the process executable. On Linux based systems, can be set to the target of `proc/[pid]/exe`. On Windows, can be set to the result of `GetProcessImageFileNameW`.

func ProcessExitCode ¶
func ProcessExitCode(val int) attribute.KeyValue

ProcessExitCode returns an attribute KeyValue conforming to the "process.exit.code" semantic conventions. It represents the exit code of the process.

func ProcessExitTime ¶
func ProcessExitTime(val string) attribute.KeyValue

ProcessExitTime returns an attribute KeyValue conforming to the "process.exit.time" semantic conventions. It represents the date and time the process exited, in ISO 8601 format.

func ProcessGroupLeaderPID ¶
func ProcessGroupLeaderPID(val int) attribute.KeyValue

ProcessGroupLeaderPID returns an attribute KeyValue conforming to the "process.group_leader.pid" semantic conventions. It represents the PID of the process's group leader. This is also the process group ID (PGID) of the process.

func ProcessInteractive ¶
func ProcessInteractive(val bool) attribute.KeyValue

ProcessInteractive returns an attribute KeyValue conforming to the "process.interactive" semantic conventions. It represents the whether the process is connected to an interactive shell.

func ProcessOwner ¶
func ProcessOwner(val string) attribute.KeyValue

ProcessOwner returns an attribute KeyValue conforming to the "process.owner" semantic conventions. It represents the username of the user that owns the process.

func ProcessPID ¶
func ProcessPID(val int) attribute.KeyValue

ProcessPID returns an attribute KeyValue conforming to the "process.pid" semantic conventions. It represents the process identifier (PID).

func ProcessParentPID ¶
func ProcessParentPID(val int) attribute.KeyValue

ProcessParentPID returns an attribute KeyValue conforming to the "process.parent_pid" semantic conventions. It represents the parent Process identifier (PPID).

func ProcessRealUserID ¶
func ProcessRealUserID(val int) attribute.KeyValue

ProcessRealUserID returns an attribute KeyValue conforming to the "process.real_user.id" semantic conventions. It represents the real user ID (RUID) of the process.

func ProcessRealUserName ¶
func ProcessRealUserName(val string) attribute.KeyValue

ProcessRealUserName returns an attribute KeyValue conforming to the "process.real_user.name" semantic conventions. It represents the username of the real user of the process.

func ProcessRuntimeDescription ¶
func ProcessRuntimeDescription(val string) attribute.KeyValue

ProcessRuntimeDescription returns an attribute KeyValue conforming to the "process.runtime.description" semantic conventions. It represents an additional description about the runtime of the process, for example a specific vendor customization of the runtime environment.

func ProcessRuntimeName ¶
func ProcessRuntimeName(val string) attribute.KeyValue

ProcessRuntimeName returns an attribute KeyValue conforming to the "process.runtime.name" semantic conventions. It represents the name of the runtime of this process. For compiled native binaries, this SHOULD be the name of the compiler.

func ProcessRuntimeVersion ¶
func ProcessRuntimeVersion(val string) attribute.KeyValue

ProcessRuntimeVersion returns an attribute KeyValue conforming to the "process.runtime.version" semantic conventions. It represents the version of the runtime of this process, as returned by the runtime without modification.

func ProcessSavedUserID ¶
func ProcessSavedUserID(val int) attribute.KeyValue

ProcessSavedUserID returns an attribute KeyValue conforming to the "process.saved_user.id" semantic conventions. It represents the saved user ID (SUID) of the process.

func ProcessSavedUserName ¶
func ProcessSavedUserName(val string) attribute.KeyValue

ProcessSavedUserName returns an attribute KeyValue conforming to the "process.saved_user.name" semantic conventions. It represents the username of the saved user.

func ProcessSessionLeaderPID ¶
func ProcessSessionLeaderPID(val int) attribute.KeyValue

ProcessSessionLeaderPID returns an attribute KeyValue conforming to the "process.session_leader.pid" semantic conventions. It represents the PID of the process's session leader. This is also the session ID (SID) of the process.

func ProcessUserID ¶
func ProcessUserID(val int) attribute.KeyValue

ProcessUserID returns an attribute KeyValue conforming to the "process.user.id" semantic conventions. It represents the effective user ID (EUID) of the process.

func ProcessUserName ¶
func ProcessUserName(val string) attribute.KeyValue

ProcessUserName returns an attribute KeyValue conforming to the "process.user.name" semantic conventions. It represents the username of the effective user of the process.

func ProcessVpid ¶
func ProcessVpid(val int) attribute.KeyValue

ProcessVpid returns an attribute KeyValue conforming to the "process.vpid" semantic conventions. It represents the virtual process identifier.

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

RPCJsonrpcVersion returns an attribute KeyValue conforming to the "rpc.jsonrpc.version" semantic conventions. It represents the protocol version as in `jsonrpc` property of request/response. Since JSON-RPC 1.0 doesn't specify this, the value can be omitted.

func RPCMessageCompressedSize ¶
func RPCMessageCompressedSize(val int) attribute.KeyValue

RPCMessageCompressedSize returns an attribute KeyValue conforming to the "rpc.message.compressed_size" semantic conventions. It represents the compressed size of the message in bytes.

func RPCMessageID ¶
func RPCMessageID(val int) attribute.KeyValue

RPCMessageID returns an attribute KeyValue conforming to the "rpc.message.id" semantic conventions. It represents the mUST be calculated as two different counters starting from `1` one for sent messages and one for received message.

func RPCMessageUncompressedSize ¶
func RPCMessageUncompressedSize(val int) attribute.KeyValue

RPCMessageUncompressedSize returns an attribute KeyValue conforming to the "rpc.message.uncompressed_size" semantic conventions. It represents the uncompressed size of the message in bytes.

func RPCMethod ¶
func RPCMethod(val string) attribute.KeyValue

RPCMethod returns an attribute KeyValue conforming to the "rpc.method" semantic conventions. It represents the name of the (logical) method being called, must be equal to the $method part in the span name.

func RPCService ¶
func RPCService(val string) attribute.KeyValue

RPCService returns an attribute KeyValue conforming to the "rpc.service" semantic conventions. It represents the full (logical) name of the service being called, including its package name, if applicable.

func ServerAddress ¶
func ServerAddress(val string) attribute.KeyValue

ServerAddress returns an attribute KeyValue conforming to the "server.address" semantic conventions. It represents the server domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

func ServerPort ¶
func ServerPort(val int) attribute.KeyValue

ServerPort returns an attribute KeyValue conforming to the "server.port" semantic conventions. It represents the server port number.

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

func SessionID ¶
func SessionID(val string) attribute.KeyValue

SessionID returns an attribute KeyValue conforming to the "session.id" semantic conventions. It represents a unique id to identify a session.

func SessionPreviousID ¶
func SessionPreviousID(val string) attribute.KeyValue

SessionPreviousID returns an attribute KeyValue conforming to the "session.previous_id" semantic conventions. It represents the previous `session.id` for this user, when known.

func SourceAddress ¶
func SourceAddress(val string) attribute.KeyValue

SourceAddress returns an attribute KeyValue conforming to the "source.address" semantic conventions. It represents the source address - domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

func SourcePort ¶
func SourcePort(val int) attribute.KeyValue

SourcePort returns an attribute KeyValue conforming to the "source.port" semantic conventions. It represents the source port number

func SystemCPULogicalNumber ¶
func SystemCPULogicalNumber(val int) attribute.KeyValue

SystemCPULogicalNumber returns an attribute KeyValue conforming to the "system.cpu.logical_number" semantic conventions. It represents the logical CPU number [0..n-1]

func SystemDevice ¶
func SystemDevice(val string) attribute.KeyValue

SystemDevice returns an attribute KeyValue conforming to the "system.device" semantic conventions. It represents the device identifier

func SystemFilesystemMode ¶
func SystemFilesystemMode(val string) attribute.KeyValue

SystemFilesystemMode returns an attribute KeyValue conforming to the "system.filesystem.mode" semantic conventions. It represents the filesystem mode

func SystemFilesystemMountpoint ¶
func SystemFilesystemMountpoint(val string) attribute.KeyValue

SystemFilesystemMountpoint returns an attribute KeyValue conforming to the "system.filesystem.mountpoint" semantic conventions. It represents the filesystem mount path

func TLSCipher ¶
func TLSCipher(val string) attribute.KeyValue

TLSCipher returns an attribute KeyValue conforming to the "tls.cipher" semantic conventions. It represents the string indicating the [cipher](https://datatracker.ietf.org/doc/html/rfc5246#appendix-A.5) used during the current connection.

func TLSClientCertificate ¶
func TLSClientCertificate(val string) attribute.KeyValue

TLSClientCertificate returns an attribute KeyValue conforming to the "tls.client.certificate" semantic conventions. It represents the pEM-encoded stand-alone certificate offered by the client. This is usually mutually-exclusive of `client.certificate_chain` since this value also exists in that list.

func TLSClientCertificateChain ¶
func TLSClientCertificateChain(val ...string) attribute.KeyValue

TLSClientCertificateChain returns an attribute KeyValue conforming to the "tls.client.certificate_chain" semantic conventions. It represents the array of PEM-encoded certificates that make up the certificate chain offered by the client. This is usually mutually-exclusive of `client.certificate` since that value should be the first certificate in the chain.

func TLSClientHashMd5 ¶
func TLSClientHashMd5(val string) attribute.KeyValue

TLSClientHashMd5 returns an attribute KeyValue conforming to the "tls.client.hash.md5" semantic conventions. It represents the certificate fingerprint using the MD5 digest of DER-encoded version of certificate offered by the client. For consistency with other hash values, this value should be formatted as an uppercase hash.

func TLSClientHashSha1 ¶
func TLSClientHashSha1(val string) attribute.KeyValue

TLSClientHashSha1 returns an attribute KeyValue conforming to the "tls.client.hash.sha1" semantic conventions. It represents the certificate fingerprint using the SHA1 digest of DER-encoded version of certificate offered by the client. For consistency with other hash values, this value should be formatted as an uppercase hash.

func TLSClientHashSha256 ¶
func TLSClientHashSha256(val string) attribute.KeyValue

TLSClientHashSha256 returns an attribute KeyValue conforming to the "tls.client.hash.sha256" semantic conventions. It represents the certificate fingerprint using the SHA256 digest of DER-encoded version of certificate offered by the client. For consistency with other hash values, this value should be formatted as an uppercase hash.

func TLSClientIssuer ¶
func TLSClientIssuer(val string) attribute.KeyValue

TLSClientIssuer returns an attribute KeyValue conforming to the "tls.client.issuer" semantic conventions. It represents the distinguished name of [subject](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6) of the issuer of the x.509 certificate presented by the client.

func TLSClientJa3 ¶
func TLSClientJa3(val string) attribute.KeyValue

TLSClientJa3 returns an attribute KeyValue conforming to the "tls.client.ja3" semantic conventions. It represents a hash that identifies clients based on how they perform an SSL/TLS handshake.

func TLSClientNotAfter ¶
func TLSClientNotAfter(val string) attribute.KeyValue

TLSClientNotAfter returns an attribute KeyValue conforming to the "tls.client.not_after" semantic conventions. It represents the date/Time indicating when client certificate is no longer considered valid.

func TLSClientNotBefore ¶
func TLSClientNotBefore(val string) attribute.KeyValue

TLSClientNotBefore returns an attribute KeyValue conforming to the "tls.client.not_before" semantic conventions. It represents the date/Time indicating when client certificate is first considered valid.

func TLSClientServerName ¶
func TLSClientServerName(val string) attribute.KeyValue

TLSClientServerName returns an attribute KeyValue conforming to the "tls.client.server_name" semantic conventions. It represents the also called an SNI, this tells the server which hostname to which the client is attempting to connect to.

func TLSClientSubject ¶
func TLSClientSubject(val string) attribute.KeyValue

TLSClientSubject returns an attribute KeyValue conforming to the "tls.client.subject" semantic conventions. It represents the distinguished name of subject of the x.509 certificate presented by the client.

func TLSClientSupportedCiphers ¶
func TLSClientSupportedCiphers(val ...string) attribute.KeyValue

TLSClientSupportedCiphers returns an attribute KeyValue conforming to the "tls.client.supported_ciphers" semantic conventions. It represents the array of ciphers offered by the client during the client hello.

func TLSCurve ¶
func TLSCurve(val string) attribute.KeyValue

TLSCurve returns an attribute KeyValue conforming to the "tls.curve" semantic conventions. It represents the string indicating the curve used for the given cipher, when applicable

func TLSEstablished ¶
func TLSEstablished(val bool) attribute.KeyValue

TLSEstablished returns an attribute KeyValue conforming to the "tls.established" semantic conventions. It represents the boolean flag indicating if the TLS negotiation was successful and transitioned to an encrypted tunnel.

func TLSNextProtocol ¶
func TLSNextProtocol(val string) attribute.KeyValue

TLSNextProtocol returns an attribute KeyValue conforming to the "tls.next_protocol" semantic conventions. It represents the string indicating the protocol being tunneled. Per the values in the [IANA registry](https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids), this string should be lower case.

func TLSProtocolVersion ¶
func TLSProtocolVersion(val string) attribute.KeyValue

TLSProtocolVersion returns an attribute KeyValue conforming to the "tls.protocol.version" semantic conventions. It represents the numeric part of the version parsed from the original string of the negotiated [SSL/TLS protocol version](https://www.openssl.org/docs/man1.1.1/man3/SSL_get_version.html#RETURN-VALUES)

func TLSResumed ¶
func TLSResumed(val bool) attribute.KeyValue

TLSResumed returns an attribute KeyValue conforming to the "tls.resumed" semantic conventions. It represents the boolean flag indicating if this TLS connection was resumed from an existing TLS negotiation.

func TLSServerCertificate ¶
func TLSServerCertificate(val string) attribute.KeyValue

TLSServerCertificate returns an attribute KeyValue conforming to the "tls.server.certificate" semantic conventions. It represents the pEM-encoded stand-alone certificate offered by the server. This is usually mutually-exclusive of `server.certificate_chain` since this value also exists in that list.

func TLSServerCertificateChain ¶
func TLSServerCertificateChain(val ...string) attribute.KeyValue

TLSServerCertificateChain returns an attribute KeyValue conforming to the "tls.server.certificate_chain" semantic conventions. It represents the array of PEM-encoded certificates that make up the certificate chain offered by the server. This is usually mutually-exclusive of `server.certificate` since that value should be the first certificate in the chain.

func TLSServerHashMd5 ¶
func TLSServerHashMd5(val string) attribute.KeyValue

TLSServerHashMd5 returns an attribute KeyValue conforming to the "tls.server.hash.md5" semantic conventions. It represents the certificate fingerprint using the MD5 digest of DER-encoded version of certificate offered by the server. For consistency with other hash values, this value should be formatted as an uppercase hash.

func TLSServerHashSha1 ¶
func TLSServerHashSha1(val string) attribute.KeyValue

TLSServerHashSha1 returns an attribute KeyValue conforming to the "tls.server.hash.sha1" semantic conventions. It represents the certificate fingerprint using the SHA1 digest of DER-encoded version of certificate offered by the server. For consistency with other hash values, this value should be formatted as an uppercase hash.

func TLSServerHashSha256 ¶
func TLSServerHashSha256(val string) attribute.KeyValue

TLSServerHashSha256 returns an attribute KeyValue conforming to the "tls.server.hash.sha256" semantic conventions. It represents the certificate fingerprint using the SHA256 digest of DER-encoded version of certificate offered by the server. For consistency with other hash values, this value should be formatted as an uppercase hash.

func TLSServerIssuer ¶
func TLSServerIssuer(val string) attribute.KeyValue

TLSServerIssuer returns an attribute KeyValue conforming to the "tls.server.issuer" semantic conventions. It represents the distinguished name of [subject](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6) of the issuer of the x.509 certificate presented by the client.

func TLSServerJa3s ¶
func TLSServerJa3s(val string) attribute.KeyValue

TLSServerJa3s returns an attribute KeyValue conforming to the "tls.server.ja3s" semantic conventions. It represents a hash that identifies servers based on how they perform an SSL/TLS handshake.

func TLSServerNotAfter ¶
func TLSServerNotAfter(val string) attribute.KeyValue

TLSServerNotAfter returns an attribute KeyValue conforming to the "tls.server.not_after" semantic conventions. It represents the date/Time indicating when server certificate is no longer considered valid.

func TLSServerNotBefore ¶
func TLSServerNotBefore(val string) attribute.KeyValue

TLSServerNotBefore returns an attribute KeyValue conforming to the "tls.server.not_before" semantic conventions. It represents the date/Time indicating when server certificate is first considered valid.

func TLSServerSubject ¶
func TLSServerSubject(val string) attribute.KeyValue

TLSServerSubject returns an attribute KeyValue conforming to the "tls.server.subject" semantic conventions. It represents the distinguished name of subject of the x.509 certificate presented by the server.

func TelemetryDistroName ¶
func TelemetryDistroName(val string) attribute.KeyValue

TelemetryDistroName returns an attribute KeyValue conforming to the "telemetry.distro.name" semantic conventions. It represents the name of the auto instrumentation agent or distribution, if used.

func TelemetryDistroVersion ¶
func TelemetryDistroVersion(val string) attribute.KeyValue

TelemetryDistroVersion returns an attribute KeyValue conforming to the "telemetry.distro.version" semantic conventions. It represents the version string of the auto instrumentation agent or distribution, if used.

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

func URLDomain ¶
func URLDomain(val string) attribute.KeyValue

URLDomain returns an attribute KeyValue conforming to the "url.domain" semantic conventions. It represents the domain extracted from the `url.full`, such as "opentelemetry.io".

func URLExtension ¶
func URLExtension(val string) attribute.KeyValue

URLExtension returns an attribute KeyValue conforming to the "url.extension" semantic conventions. It represents the file extension extracted from the `url.full`, excluding the leading dot.

func URLFragment ¶
func URLFragment(val string) attribute.KeyValue

URLFragment returns an attribute KeyValue conforming to the "url.fragment" semantic conventions. It represents the [URI fragment](https://www.rfc-editor.org/rfc/rfc3986#section-3.5) component

func URLFull ¶
func URLFull(val string) attribute.KeyValue

URLFull returns an attribute KeyValue conforming to the "url.full" semantic conventions. It represents the absolute URL describing a network resource according to [RFC3986](https://www.rfc-editor.org/rfc/rfc3986)

func URLOriginal ¶
func URLOriginal(val string) attribute.KeyValue

URLOriginal returns an attribute KeyValue conforming to the "url.original" semantic conventions. It represents the unmodified original URL as seen in the event source.

func URLPath ¶
func URLPath(val string) attribute.KeyValue

URLPath returns an attribute KeyValue conforming to the "url.path" semantic conventions. It represents the [URI path](https://www.rfc-editor.org/rfc/rfc3986#section-3.3) component

func URLPort ¶
func URLPort(val int) attribute.KeyValue

URLPort returns an attribute KeyValue conforming to the "url.port" semantic conventions. It represents the port extracted from the `url.full`

func URLQuery ¶
func URLQuery(val string) attribute.KeyValue

URLQuery returns an attribute KeyValue conforming to the "url.query" semantic conventions. It represents the [URI query](https://www.rfc-editor.org/rfc/rfc3986#section-3.4) component

func URLRegisteredDomain ¶
func URLRegisteredDomain(val string) attribute.KeyValue

URLRegisteredDomain returns an attribute KeyValue conforming to the "url.registered_domain" semantic conventions. It represents the highest registered url domain, stripped of the subdomain.

func URLScheme ¶
func URLScheme(val string) attribute.KeyValue

URLScheme returns an attribute KeyValue conforming to the "url.scheme" semantic conventions. It represents the [URI scheme](https://www.rfc-editor.org/rfc/rfc3986#section-3.1) component identifying the used protocol.

func URLSubdomain ¶
func URLSubdomain(val string) attribute.KeyValue

URLSubdomain returns an attribute KeyValue conforming to the "url.subdomain" semantic conventions. It represents the subdomain portion of a fully qualified domain name includes all of the names except the host name under the registered_domain. In a partially qualified domain, or if the qualification level of the full name cannot be determined, subdomain contains all of the names below the registered domain.

func URLTemplate ¶
func URLTemplate(val string) attribute.KeyValue

URLTemplate returns an attribute KeyValue conforming to the "url.template" semantic conventions. It represents the low-cardinality template of an [absolute path reference](https://www.rfc-editor.org/rfc/rfc3986#section-4.2).

func URLTopLevelDomain ¶
func URLTopLevelDomain(val string) attribute.KeyValue

URLTopLevelDomain returns an attribute KeyValue conforming to the "url.top_level_domain" semantic conventions. It represents the effective top level domain (eTLD), also known as the domain suffix, is the last part of the domain name. For example, the top level domain for example.com is `com`.

func UserAgentName ¶
func UserAgentName(val string) attribute.KeyValue

UserAgentName returns an attribute KeyValue conforming to the "user_agent.name" semantic conventions. It represents the name of the user-agent extracted from original. Usually refers to the browser's name.

func UserAgentOriginal ¶
func UserAgentOriginal(val string) attribute.KeyValue

UserAgentOriginal returns an attribute KeyValue conforming to the "user_agent.original" semantic conventions. It represents the value of the [HTTP User-Agent](https://www.rfc-editor.org/rfc/rfc9110.html#field.user-agent) header sent by the client.

func UserAgentVersion ¶
func UserAgentVersion(val string) attribute.KeyValue

UserAgentVersion returns an attribute KeyValue conforming to the "user_agent.version" semantic conventions. It represents the version of the user-agent extracted from original. Usually refers to the browser's version

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
exception.go
metric.go
schema.go
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
