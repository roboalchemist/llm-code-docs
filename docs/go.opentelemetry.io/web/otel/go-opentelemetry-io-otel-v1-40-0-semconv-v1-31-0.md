# Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.31.0

Title: semconv package - go.opentelemetry.io/otel/semconv/v1.31.0 - Go Packages

URL Source: https://pkg.go.dev/go.opentelemetry.io/otel@v1.40.0/semconv/v1.31.0

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
 
v1.31.0
semconv
package
Version: v1.40.0 Latest 
Published: Feb 2, 2026 
License: Apache-2.0, BSD-3-Clause 
Imports: 1 
Imported by: 1
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
Semconv v1.31.0
Documentation
Source Files
 README ¶
Semconv v1.31.0

 Documentation ¶
Overview ¶

Package semconv implements OpenTelemetry semantic conventions.

OpenTelemetry semantic conventions are agreed standardized naming patterns for OpenTelemetry things. This package represents the v1.31.0 version of the OpenTelemetry semantic conventions.

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
func AWSExtendedRequestID(val string) attribute.KeyValue
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
func ArtifactAttestationFilename(val string) attribute.KeyValue
func ArtifactAttestationHash(val string) attribute.KeyValue
func ArtifactAttestationID(val string) attribute.KeyValue
func ArtifactFilename(val string) attribute.KeyValue
func ArtifactHash(val string) attribute.KeyValue
func ArtifactPurl(val string) attribute.KeyValue
func ArtifactVersion(val string) attribute.KeyValue
func AzNamespace(val string) attribute.KeyValue
func AzServiceRequestID(val string) attribute.KeyValue
func AzureClientID(val string) attribute.KeyValue
func AzureCosmosDBOperationContactedRegions(val ...string) attribute.KeyValue
func AzureCosmosDBOperationRequestCharge(val float64) attribute.KeyValue
func AzureCosmosDBRequestBodySize(val int) attribute.KeyValue
func AzureCosmosDBResponseSubStatusCode(val int) attribute.KeyValue
func BrowserBrands(val ...string) attribute.KeyValue
func BrowserLanguage(val string) attribute.KeyValue
func BrowserMobile(val bool) attribute.KeyValue
func BrowserPlatform(val string) attribute.KeyValue
func CICDPipelineName(val string) attribute.KeyValue
func CICDPipelineRunID(val string) attribute.KeyValue
func CICDPipelineRunURLFull(val string) attribute.KeyValue
func CICDPipelineTaskName(val string) attribute.KeyValue
func CICDPipelineTaskRunID(val string) attribute.KeyValue
func CICDPipelineTaskRunURLFull(val string) attribute.KeyValue
func CICDSystemComponent(val string) attribute.KeyValue
func CPULogicalNumber(val int) attribute.KeyValue
func CassandraCoordinatorDC(val string) attribute.KeyValue
func CassandraCoordinatorID(val string) attribute.KeyValue
func CassandraPageSize(val int) attribute.KeyValue
func CassandraQueryIdempotent(val bool) attribute.KeyValue
func CassandraSpeculativeExecutionCount(val int) attribute.KeyValue
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
func CloudfoundryAppID(val string) attribute.KeyValue
func CloudfoundryAppInstanceID(val string) attribute.KeyValue
func CloudfoundryAppName(val string) attribute.KeyValue
func CloudfoundryOrgID(val string) attribute.KeyValue
func CloudfoundryOrgName(val string) attribute.KeyValue
func CloudfoundryProcessID(val string) attribute.KeyValue
func CloudfoundryProcessType(val string) attribute.KeyValue
func CloudfoundrySpaceID(val string) attribute.KeyValue
func CloudfoundrySpaceName(val string) attribute.KeyValue
func CloudfoundrySystemID(val string) attribute.KeyValue
func CloudfoundrySystemInstanceID(val string) attribute.KeyValue
func CodeColumnNumber(val int) attribute.KeyValue
func CodeFilePath(val string) attribute.KeyValue
func CodeFunctionName(val string) attribute.KeyValue
func CodeLineNumber(val int) attribute.KeyValue
func CodeStacktrace(val string) attribute.KeyValue
func ContainerCommand(val string) attribute.KeyValue
func ContainerCommandArgs(val ...string) attribute.KeyValue
func ContainerCommandLine(val string) attribute.KeyValue
func ContainerCsiPluginName(val string) attribute.KeyValue
func ContainerCsiVolumeID(val string) attribute.KeyValue
func ContainerID(val string) attribute.KeyValue
func ContainerImageID(val string) attribute.KeyValue
func ContainerImageName(val string) attribute.KeyValue
func ContainerImageRepoDigests(val ...string) attribute.KeyValue
func ContainerImageTags(val ...string) attribute.KeyValue
func ContainerName(val string) attribute.KeyValue
func ContainerRuntime(val string) attribute.KeyValue
func DBClientConnectionPoolName(val string) attribute.KeyValue
func DBCollectionName(val string) attribute.KeyValue
func DBNamespace(val string) attribute.KeyValue
func DBOperationBatchSize(val int) attribute.KeyValue
func DBOperationName(val string) attribute.KeyValue
func DBQuerySummary(val string) attribute.KeyValue
func DBQueryText(val string) attribute.KeyValue
func DBResponseReturnedRows(val int) attribute.KeyValue
func DBResponseStatusCode(val string) attribute.KeyValue
func DNSQuestionName(val string) attribute.KeyValue
func DeploymentEnvironmentName(val string) attribute.KeyValue
func DeploymentID(val string) attribute.KeyValue
func DeploymentName(val string) attribute.KeyValue
func DestinationAddress(val string) attribute.KeyValue
func DestinationPort(val int) attribute.KeyValue
func DeviceID(val string) attribute.KeyValue
func DeviceManufacturer(val string) attribute.KeyValue
func DeviceModelIdentifier(val string) attribute.KeyValue
func DeviceModelName(val string) attribute.KeyValue
func ElasticsearchNodeName(val string) attribute.KeyValue
func EnduserID(val string) attribute.KeyValue
func EnduserPseudoID(val string) attribute.KeyValue
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
func FeatureFlagContextID(val string) attribute.KeyValue
func FeatureFlagEvaluationErrorMessage(val string) attribute.KeyValue
func FeatureFlagKey(val string) attribute.KeyValue
func FeatureFlagProviderName(val string) attribute.KeyValue
func FeatureFlagSetID(val string) attribute.KeyValue
func FeatureFlagVariant(val string) attribute.KeyValue
func FeatureFlagVersion(val string) attribute.KeyValue
func FileAccessed(val string) attribute.KeyValue
func FileAttributes(val ...string) attribute.KeyValue
func FileChanged(val string) attribute.KeyValue
func FileCreated(val string) attribute.KeyValue
func FileDirectory(val string) attribute.KeyValue
func FileExtension(val string) attribute.KeyValue
func FileForkName(val string) attribute.KeyValue
func FileGroupID(val string) attribute.KeyValue
func FileGroupName(val string) attribute.KeyValue
func FileInode(val string) attribute.KeyValue
func FileMode(val string) attribute.KeyValue
func FileModified(val string) attribute.KeyValue
func FileName(val string) attribute.KeyValue
func FileOwnerID(val string) attribute.KeyValue
func FileOwnerName(val string) attribute.KeyValue
func FilePath(val string) attribute.KeyValue
func FileSize(val int) attribute.KeyValue
func FileSymbolicLinkTargetPath(val string) attribute.KeyValue
func GCPClientService(val string) attribute.KeyValue
func GCPCloudRunJobExecution(val string) attribute.KeyValue
func GCPCloudRunJobTaskIndex(val int) attribute.KeyValue
func GCPGceInstanceHostname(val string) attribute.KeyValue
func GCPGceInstanceName(val string) attribute.KeyValue
func GenAIAgentDescription(val string) attribute.KeyValue
func GenAIAgentID(val string) attribute.KeyValue
func GenAIAgentName(val string) attribute.KeyValue
func GenAIOpenaiResponseServiceTier(val string) attribute.KeyValue
func GenAIOpenaiResponseSystemFingerprint(val string) attribute.KeyValue
func GenAIRequestChoiceCount(val int) attribute.KeyValue
func GenAIRequestEncodingFormats(val ...string) attribute.KeyValue
func GenAIRequestFrequencyPenalty(val float64) attribute.KeyValue
func GenAIRequestMaxTokens(val int) attribute.KeyValue
func GenAIRequestModel(val string) attribute.KeyValue
func GenAIRequestPresencePenalty(val float64) attribute.KeyValue
func GenAIRequestSeed(val int) attribute.KeyValue
func GenAIRequestStopSequences(val ...string) attribute.KeyValue
func GenAIRequestTemperature(val float64) attribute.KeyValue
func GenAIRequestTopK(val float64) attribute.KeyValue
func GenAIRequestTopP(val float64) attribute.KeyValue
func GenAIResponseFinishReasons(val ...string) attribute.KeyValue
func GenAIResponseID(val string) attribute.KeyValue
func GenAIResponseModel(val string) attribute.KeyValue
func GenAIToolCallID(val string) attribute.KeyValue
func GenAIToolName(val string) attribute.KeyValue
func GenAIToolType(val string) attribute.KeyValue
func GenAIUsageInputTokens(val int) attribute.KeyValue
func GenAIUsageOutputTokens(val int) attribute.KeyValue
func GeoCountryIsoCode(val string) attribute.KeyValue
func GeoLocalityName(val string) attribute.KeyValue
func GeoLocationLat(val float64) attribute.KeyValue
func GeoLocationLon(val float64) attribute.KeyValue
func GeoPostalCode(val string) attribute.KeyValue
func GeoRegionIsoCode(val string) attribute.KeyValue
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
func HwID(val string) attribute.KeyValue
func HwName(val string) attribute.KeyValue
func HwParent(val string) attribute.KeyValue
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
func K8SHpaName(val string) attribute.KeyValue
func K8SHpaUID(val string) attribute.KeyValue
func K8SJobName(val string) attribute.KeyValue
func K8SJobUID(val string) attribute.KeyValue
func K8SNamespaceName(val string) attribute.KeyValue
func K8SNodeName(val string) attribute.KeyValue
func K8SNodeUID(val string) attribute.KeyValue
func K8SPodName(val string) attribute.KeyValue
func K8SPodUID(val string) attribute.KeyValue
func K8SReplicaSetName(val string) attribute.KeyValue
func K8SReplicaSetUID(val string) attribute.KeyValue
func K8SReplicationControllerName(val string) attribute.KeyValue
func K8SReplicationControllerUID(val string) attribute.KeyValue
func K8SResourceQuotaName(val string) attribute.KeyValue
func K8SResourceQuotaUID(val string) attribute.KeyValue
func K8SStatefulSetName(val string) attribute.KeyValue
func K8SStatefulSetUID(val string) attribute.KeyValue
func K8SVolumeName(val string) attribute.KeyValue
func LogFileName(val string) attribute.KeyValue
func LogFileNameResolved(val string) attribute.KeyValue
func LogFilePath(val string) attribute.KeyValue
func LogFilePathResolved(val string) attribute.KeyValue
func LogRecordOriginal(val string) attribute.KeyValue
func LogRecordUID(val string) attribute.KeyValue
func MessagingBatchMessageCount(val int) attribute.KeyValue
func MessagingClientID(val string) attribute.KeyValue
func MessagingConsumerGroupName(val string) attribute.KeyValue
func MessagingDestinationAnonymous(val bool) attribute.KeyValue
func MessagingDestinationName(val string) attribute.KeyValue
func MessagingDestinationPartitionID(val string) attribute.KeyValue
func MessagingDestinationSubscriptionName(val string) attribute.KeyValue
func MessagingDestinationTemplate(val string) attribute.KeyValue
func MessagingDestinationTemporary(val bool) attribute.KeyValue
func MessagingEventhubsMessageEnqueuedTime(val int) attribute.KeyValue
func MessagingGCPPubsubMessageAckDeadline(val int) attribute.KeyValue
func MessagingGCPPubsubMessageAckID(val string) attribute.KeyValue
func MessagingGCPPubsubMessageDeliveryAttempt(val int) attribute.KeyValue
func MessagingGCPPubsubMessageOrderingKey(val string) attribute.KeyValue
func MessagingKafkaMessageKey(val string) attribute.KeyValue
func MessagingKafkaMessageTombstone(val bool) attribute.KeyValue
func MessagingKafkaOffset(val int) attribute.KeyValue
func MessagingMessageBodySize(val int) attribute.KeyValue
func MessagingMessageConversationID(val string) attribute.KeyValue
func MessagingMessageEnvelopeSize(val int) attribute.KeyValue
func MessagingMessageID(val string) attribute.KeyValue
func MessagingOperationName(val string) attribute.KeyValue
func MessagingRabbitmqDestinationRoutingKey(val string) attribute.KeyValue
func MessagingRabbitmqMessageDeliveryTag(val int) attribute.KeyValue
func MessagingRocketmqMessageDelayTimeLevel(val int) attribute.KeyValue
func MessagingRocketmqMessageDeliveryTimestamp(val int) attribute.KeyValue
func MessagingRocketmqMessageGroup(val string) attribute.KeyValue
func MessagingRocketmqMessageKeys(val ...string) attribute.KeyValue
func MessagingRocketmqMessageTag(val string) attribute.KeyValue
func MessagingRocketmqNamespace(val string) attribute.KeyValue
func MessagingServicebusMessageDeliveryCount(val int) attribute.KeyValue
func MessagingServicebusMessageEnqueuedTime(val int) attribute.KeyValue
func NetworkCarrierIcc(val string) attribute.KeyValue
func NetworkCarrierMcc(val string) attribute.KeyValue
func NetworkCarrierMnc(val string) attribute.KeyValue
func NetworkCarrierName(val string) attribute.KeyValue
func NetworkInterfaceName(val string) attribute.KeyValue
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
func OTelComponentName(val string) attribute.KeyValue
func OTelScopeName(val string) attribute.KeyValue
func OTelScopeVersion(val string) attribute.KeyValue
func OTelStatusDescription(val string) attribute.KeyValue
func OciManifestDigest(val string) attribute.KeyValue
func PeerService(val string) attribute.KeyValue
func ProcessArgsCount(val int) attribute.KeyValue
func ProcessCommand(val string) attribute.KeyValue
func ProcessCommandArgs(val ...string) attribute.KeyValue
func ProcessCommandLine(val string) attribute.KeyValue
func ProcessCreationTime(val string) attribute.KeyValue
func ProcessExecutableBuildIDGnu(val string) attribute.KeyValue
func ProcessExecutableBuildIDGo(val string) attribute.KeyValue
func ProcessExecutableBuildIDHtlhash(val string) attribute.KeyValue
func ProcessExecutableName(val string) attribute.KeyValue
func ProcessExecutablePath(val string) attribute.KeyValue
func ProcessExitCode(val int) attribute.KeyValue
func ProcessExitTime(val string) attribute.KeyValue
func ProcessGroupLeaderPID(val int) attribute.KeyValue
func ProcessInteractive(val bool) attribute.KeyValue
func ProcessLinuxCgroup(val string) attribute.KeyValue
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
func ProcessTitle(val string) attribute.KeyValue
func ProcessUserID(val int) attribute.KeyValue
func ProcessUserName(val string) attribute.KeyValue
func ProcessVpid(val int) attribute.KeyValue
func ProcessWorkingDirectory(val string) attribute.KeyValue
func RPCJsonrpcErrorCode(val int) attribute.KeyValue
func RPCJsonrpcErrorMessage(val string) attribute.KeyValue
func RPCJsonrpcRequestID(val string) attribute.KeyValue
func RPCJsonrpcVersion(val string) attribute.KeyValue
func RPCMessageCompressedSize(val int) attribute.KeyValue
func RPCMessageID(val int) attribute.KeyValue
func RPCMessageUncompressedSize(val int) attribute.KeyValue
func RPCMethod(val string) attribute.KeyValue
func RPCService(val string) attribute.KeyValue
func SecurityRuleCategory(val string) attribute.KeyValue
func SecurityRuleDescription(val string) attribute.KeyValue
func SecurityRuleLicense(val string) attribute.KeyValue
func SecurityRuleName(val string) attribute.KeyValue
func SecurityRuleReference(val string) attribute.KeyValue
func SecurityRuleRulesetName(val string) attribute.KeyValue
func SecurityRuleUUID(val string) attribute.KeyValue
func SecurityRuleVersion(val string) attribute.KeyValue
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
func TestCaseName(val string) attribute.KeyValue
func TestSuiteName(val string) attribute.KeyValue
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
func UserAgentOSName(val string) attribute.KeyValue
func UserAgentOSVersion(val string) attribute.KeyValue
func UserAgentOriginal(val string) attribute.KeyValue
func UserAgentVersion(val string) attribute.KeyValue
func UserEmail(val string) attribute.KeyValue
func UserFullName(val string) attribute.KeyValue
func UserHash(val string) attribute.KeyValue
func UserID(val string) attribute.KeyValue
func UserName(val string) attribute.KeyValue
func UserRoles(val ...string) attribute.KeyValue
func VCSChangeID(val string) attribute.KeyValue
func VCSChangeTitle(val string) attribute.KeyValue
func VCSRefBaseName(val string) attribute.KeyValue
func VCSRefBaseRevision(val string) attribute.KeyValue
func VCSRefHeadName(val string) attribute.KeyValue
func VCSRefHeadRevision(val string) attribute.KeyValue
func VCSRepositoryName(val string) attribute.KeyValue
func VCSRepositoryURLFull(val string) attribute.KeyValue
func WebEngineDescription(val string) attribute.KeyValue
func WebEngineName(val string) attribute.KeyValue
func WebEngineVersion(val string) attribute.KeyValue
Constants ¶
View Source
const (
	// AndroidAppStateKey is the attribute Key conforming to the "android.app.state"
	// semantic conventions. It represents the this attribute represents the state
	// of the application.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "created"
	// Note: The Android lifecycle states are defined in
	// [Activity lifecycle callbacks], and from which the `OS identifiers` are
	// derived.
	//
	// [Activity lifecycle callbacks]: https://developer.android.com/guide/components/activities/activity-lifecycle#lc
	AndroidAppStateKey = attribute.Key("android.app.state")

	// AndroidOSAPILevelKey is the attribute Key conforming to the
	// "android.os.api_level" semantic conventions. It represents the uniquely
	// identifies the framework API revision offered by a version (`os.version`) of
	// the android operating system. More information can be found [here].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "33", "32"
	//
	// [here]: https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels
	AndroidOSAPILevelKey = attribute.Key("android.os.api_level")
)

Namespace: android

View Source
const (
	// ArtifactAttestationFilenameKey is the attribute Key conforming to the
	// "artifact.attestation.filename" semantic conventions. It represents the
	// provenance filename of the built attestation which directly relates to the
	// build artifact filename. This filename SHOULD accompany the artifact at
	// publish time. See the [SLSA Relationship] specification for more information.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "golang-binary-amd64-v0.1.0.attestation",
	// "docker-image-amd64-v0.1.0.intoto.json1", "release-1.tar.gz.attestation",
	// "file-name-package.tar.gz.intoto.json1"
	//
	// [SLSA Relationship]: https://slsa.dev/spec/v1.0/distributing-provenance#relationship-between-artifacts-and-attestations
	ArtifactAttestationFilenameKey = attribute.Key("artifact.attestation.filename")

	// ArtifactAttestationHashKey is the attribute Key conforming to the
	// "artifact.attestation.hash" semantic conventions. It represents the full
	// [hash value (see glossary)], of the built attestation. Some envelopes in the
	// [software attestation space] also refer to this as the **digest**.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1b31dfcd5b7f9267bf2ff47651df1cfb9147b9e4df1f335accf65b4cda498408"
	//
	// [hash value (see glossary)]: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf
	// [software attestation space]: https://github.com/in-toto/attestation/tree/main/spec
	ArtifactAttestationHashKey = attribute.Key("artifact.attestation.hash")

	// ArtifactAttestationIDKey is the attribute Key conforming to the
	// "artifact.attestation.id" semantic conventions. It represents the id of the
	// build [software attestation].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "123"
	//
	// [software attestation]: https://slsa.dev/attestation-model
	ArtifactAttestationIDKey = attribute.Key("artifact.attestation.id")

	// ArtifactFilenameKey is the attribute Key conforming to the
	// "artifact.filename" semantic conventions. It represents the human readable
	// file name of the artifact, typically generated during build and release
	// processes. Often includes the package name and version in the file name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "golang-binary-amd64-v0.1.0", "docker-image-amd64-v0.1.0",
	// "release-1.tar.gz", "file-name-package.tar.gz"
	// Note: This file name can also act as the [Package Name]
	// in cases where the package ecosystem maps accordingly.
	// Additionally, the artifact [can be published]
	// for others, but that is not a guarantee.
	//
	// [Package Name]: https://slsa.dev/spec/v1.0/terminology#package-model
	// [can be published]: https://slsa.dev/spec/v1.0/terminology#software-supply-chain
	ArtifactFilenameKey = attribute.Key("artifact.filename")

	// ArtifactHashKey is the attribute Key conforming to the "artifact.hash"
	// semantic conventions. It represents the full [hash value (see glossary)],
	// often found in checksum.txt on a release of the artifact and used to verify
	// package integrity.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "9ff4c52759e2c4ac70b7d517bc7fcdc1cda631ca0045271ddd1b192544f8a3e9"
	// Note: The specific algorithm used to create the cryptographic hash value is
	// not defined. In situations where an artifact has multiple
	// cryptographic hashes, it is up to the implementer to choose which
	// hash value to set here; this should be the most secure hash algorithm
	// that is suitable for the situation and consistent with the
	// corresponding attestation. The implementer can then provide the other
	// hash values through an additional set of attribute extensions as they
	// deem necessary.
	//
	// [hash value (see glossary)]: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf
	ArtifactHashKey = attribute.Key("artifact.hash")

	// ArtifactPurlKey is the attribute Key conforming to the "artifact.purl"
	// semantic conventions. It represents the [Package URL] of the
	// [package artifact] provides a standard way to identify and locate the
	// packaged artifact.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "pkg:github/package-url/purl-spec@1209109710924",
	// "pkg:npm/foo@12.12.3"
	//
	// [Package URL]: https://github.com/package-url/purl-spec
	// [package artifact]: https://slsa.dev/spec/v1.0/terminology#package-model
	ArtifactPurlKey = attribute.Key("artifact.purl")

	// ArtifactVersionKey is the attribute Key conforming to the "artifact.version"
	// semantic conventions. It represents the version of the artifact.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "v0.1.0", "1.2.1", "122691-build"
	ArtifactVersionKey = attribute.Key("artifact.version")
)

Namespace: artifact

View Source
const (
	// AWSDynamoDBAttributeDefinitionsKey is the attribute Key conforming to the
	// "aws.dynamodb.attribute_definitions" semantic conventions. It represents the
	// JSON-serialized value of each item in the `AttributeDefinitions` request
	// field.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "{ "AttributeName": "string", "AttributeType": "string" }"
	AWSDynamoDBAttributeDefinitionsKey = attribute.Key("aws.dynamodb.attribute_definitions")

	// AWSDynamoDBAttributesToGetKey is the attribute Key conforming to the
	// "aws.dynamodb.attributes_to_get" semantic conventions. It represents the
	// value of the `AttributesToGet` request parameter.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "lives", "id"
	AWSDynamoDBAttributesToGetKey = attribute.Key("aws.dynamodb.attributes_to_get")

	// AWSDynamoDBConsistentReadKey is the attribute Key conforming to the
	// "aws.dynamodb.consistent_read" semantic conventions. It represents the value
	// of the `ConsistentRead` request parameter.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	AWSDynamoDBConsistentReadKey = attribute.Key("aws.dynamodb.consistent_read")

	// AWSDynamoDBConsumedCapacityKey is the attribute Key conforming to the
	// "aws.dynamodb.consumed_capacity" semantic conventions. It represents the
	// JSON-serialized value of each item in the `ConsumedCapacity` response field.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "{ "CapacityUnits": number, "GlobalSecondaryIndexes": { "string" :
	// { "CapacityUnits": number, "ReadCapacityUnits": number, "WriteCapacityUnits":
	// number } }, "LocalSecondaryIndexes": { "string" : { "CapacityUnits": number,
	// "ReadCapacityUnits": number, "WriteCapacityUnits": number } },
	// "ReadCapacityUnits": number, "Table": { "CapacityUnits": number,
	// "ReadCapacityUnits": number, "WriteCapacityUnits": number }, "TableName":
	// "string", "WriteCapacityUnits": number }"
	AWSDynamoDBConsumedCapacityKey = attribute.Key("aws.dynamodb.consumed_capacity")

	// AWSDynamoDBCountKey is the attribute Key conforming to the
	// "aws.dynamodb.count" semantic conventions. It represents the value of the
	// `Count` response parameter.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 10
	AWSDynamoDBCountKey = attribute.Key("aws.dynamodb.count")

	// AWSDynamoDBExclusiveStartTableKey is the attribute Key conforming to the
	// "aws.dynamodb.exclusive_start_table" semantic conventions. It represents the
	// value of the `ExclusiveStartTableName` request parameter.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Users", "CatsTable"
	AWSDynamoDBExclusiveStartTableKey = attribute.Key("aws.dynamodb.exclusive_start_table")

	// AWSDynamoDBGlobalSecondaryIndexUpdatesKey is the attribute Key conforming to
	// the "aws.dynamodb.global_secondary_index_updates" semantic conventions. It
	// represents the JSON-serialized value of each item in the
	// `GlobalSecondaryIndexUpdates` request field.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "{ "Create": { "IndexName": "string", "KeySchema": [ {
	// "AttributeName": "string", "KeyType": "string" } ], "Projection": {
	// "NonKeyAttributes": [ "string" ], "ProjectionType": "string" },
	// "ProvisionedThroughput": { "ReadCapacityUnits": number, "WriteCapacityUnits":
	// number } }"
	AWSDynamoDBGlobalSecondaryIndexUpdatesKey = attribute.Key("aws.dynamodb.global_secondary_index_updates")

	// AWSDynamoDBGlobalSecondaryIndexesKey is the attribute Key conforming to the
	// "aws.dynamodb.global_secondary_indexes" semantic conventions. It represents
	// the JSON-serialized value of each item of the `GlobalSecondaryIndexes`
	// request field.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "{ "IndexName": "string", "KeySchema": [ { "AttributeName":
	// "string", "KeyType": "string" } ], "Projection": { "NonKeyAttributes": [
	// "string" ], "ProjectionType": "string" }, "ProvisionedThroughput": {
	// "ReadCapacityUnits": number, "WriteCapacityUnits": number } }"
	AWSDynamoDBGlobalSecondaryIndexesKey = attribute.Key("aws.dynamodb.global_secondary_indexes")

	// AWSDynamoDBIndexNameKey is the attribute Key conforming to the
	// "aws.dynamodb.index_name" semantic conventions. It represents the value of
	// the `IndexName` request parameter.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "name_to_group"
	AWSDynamoDBIndexNameKey = attribute.Key("aws.dynamodb.index_name")

	// AWSDynamoDBItemCollectionMetricsKey is the attribute Key conforming to the
	// "aws.dynamodb.item_collection_metrics" semantic conventions. It represents
	// the JSON-serialized value of the `ItemCollectionMetrics` response field.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "{ "string" : [ { "ItemCollectionKey": { "string" : { "B": blob,
	// "BOOL": boolean, "BS": [ blob ], "L": [ "AttributeValue" ], "M": { "string" :
	// "AttributeValue" }, "N": "string", "NS": [ "string" ], "NULL": boolean, "S":
	// "string", "SS": [ "string" ] } }, "SizeEstimateRangeGB": [ number ] } ] }"
	AWSDynamoDBItemCollectionMetricsKey = attribute.Key("aws.dynamodb.item_collection_metrics")

	// AWSDynamoDBLimitKey is the attribute Key conforming to the
	// "aws.dynamodb.limit" semantic conventions. It represents the value of the
	// `Limit` request parameter.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 10
	AWSDynamoDBLimitKey = attribute.Key("aws.dynamodb.limit")

	// AWSDynamoDBLocalSecondaryIndexesKey is the attribute Key conforming to the
	// "aws.dynamodb.local_secondary_indexes" semantic conventions. It represents
	// the JSON-serialized value of each item of the `LocalSecondaryIndexes` request
	// field.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "{ "IndexArn": "string", "IndexName": "string", "IndexSizeBytes":
	// number, "ItemCount": number, "KeySchema": [ { "AttributeName": "string",
	// "KeyType": "string" } ], "Projection": { "NonKeyAttributes": [ "string" ],
	// "ProjectionType": "string" } }"
	AWSDynamoDBLocalSecondaryIndexesKey = attribute.Key("aws.dynamodb.local_secondary_indexes")

	// AWSDynamoDBProjectionKey is the attribute Key conforming to the
	// "aws.dynamodb.projection" semantic conventions. It represents the value of
	// the `ProjectionExpression` request parameter.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Title", "Title, Price, Color", "Title, Description, RelatedItems,
	// ProductReviews"
	AWSDynamoDBProjectionKey = attribute.Key("aws.dynamodb.projection")

	// AWSDynamoDBProvisionedReadCapacityKey is the attribute Key conforming to the
	// "aws.dynamodb.provisioned_read_capacity" semantic conventions. It represents
	// the value of the `ProvisionedThroughput.ReadCapacityUnits` request parameter.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1.0, 2.0
	AWSDynamoDBProvisionedReadCapacityKey = attribute.Key("aws.dynamodb.provisioned_read_capacity")

	// AWSDynamoDBProvisionedWriteCapacityKey is the attribute Key conforming to the
	// "aws.dynamodb.provisioned_write_capacity" semantic conventions. It represents
	// the value of the `ProvisionedThroughput.WriteCapacityUnits` request
	// parameter.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1.0, 2.0
	AWSDynamoDBProvisionedWriteCapacityKey = attribute.Key("aws.dynamodb.provisioned_write_capacity")

	// AWSDynamoDBScanForwardKey is the attribute Key conforming to the
	// "aws.dynamodb.scan_forward" semantic conventions. It represents the value of
	// the `ScanIndexForward` request parameter.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	AWSDynamoDBScanForwardKey = attribute.Key("aws.dynamodb.scan_forward")

	// AWSDynamoDBScannedCountKey is the attribute Key conforming to the
	// "aws.dynamodb.scanned_count" semantic conventions. It represents the value of
	// the `ScannedCount` response parameter.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 50
	AWSDynamoDBScannedCountKey = attribute.Key("aws.dynamodb.scanned_count")

	// AWSDynamoDBSegmentKey is the attribute Key conforming to the
	// "aws.dynamodb.segment" semantic conventions. It represents the value of the
	// `Segment` request parameter.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 10
	AWSDynamoDBSegmentKey = attribute.Key("aws.dynamodb.segment")

	// AWSDynamoDBSelectKey is the attribute Key conforming to the
	// "aws.dynamodb.select" semantic conventions. It represents the value of the
	// `Select` request parameter.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "ALL_ATTRIBUTES", "COUNT"
	AWSDynamoDBSelectKey = attribute.Key("aws.dynamodb.select")

	// AWSDynamoDBTableCountKey is the attribute Key conforming to the
	// "aws.dynamodb.table_count" semantic conventions. It represents the number of
	// items in the `TableNames` response parameter.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 20
	AWSDynamoDBTableCountKey = attribute.Key("aws.dynamodb.table_count")

	// AWSDynamoDBTableNamesKey is the attribute Key conforming to the
	// "aws.dynamodb.table_names" semantic conventions. It represents the keys in
	// the `RequestItems` object field.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Users", "Cats"
	AWSDynamoDBTableNamesKey = attribute.Key("aws.dynamodb.table_names")

	// AWSDynamoDBTotalSegmentsKey is the attribute Key conforming to the
	// "aws.dynamodb.total_segments" semantic conventions. It represents the value
	// of the `TotalSegments` request parameter.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 100
	AWSDynamoDBTotalSegmentsKey = attribute.Key("aws.dynamodb.total_segments")

	// AWSECSClusterARNKey is the attribute Key conforming to the
	// "aws.ecs.cluster.arn" semantic conventions. It represents the ARN of an
	// [ECS cluster].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "arn:aws:ecs:us-west-2:123456789123:cluster/my-cluster"
	//
	// [ECS cluster]: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html
	AWSECSClusterARNKey = attribute.Key("aws.ecs.cluster.arn")

	// AWSECSContainerARNKey is the attribute Key conforming to the
	// "aws.ecs.container.arn" semantic conventions. It represents the Amazon
	// Resource Name (ARN) of an [ECS container instance].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "arn:aws:ecs:us-west-1:123456789123:container/32624152-9086-4f0e-acae-1a75b14fe4d9"
	//
	// [ECS container instance]: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html
	AWSECSContainerARNKey = attribute.Key("aws.ecs.container.arn")

	// AWSECSLaunchtypeKey is the attribute Key conforming to the
	// "aws.ecs.launchtype" semantic conventions. It represents the [launch type]
	// for an ECS task.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	//
	// [launch type]: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html
	AWSECSLaunchtypeKey = attribute.Key("aws.ecs.launchtype")

	// AWSECSTaskARNKey is the attribute Key conforming to the "aws.ecs.task.arn"
	// semantic conventions. It represents the ARN of a running [ECS task].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "arn:aws:ecs:us-west-1:123456789123:task/10838bed-421f-43ef-870a-f43feacbbb5b",
	// "arn:aws:ecs:us-west-1:123456789123:task/my-cluster/task-id/23ebb8ac-c18f-46c6-8bbe-d55d0e37cfbd"
	//
	// [ECS task]: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids
	AWSECSTaskARNKey = attribute.Key("aws.ecs.task.arn")

	// AWSECSTaskFamilyKey is the attribute Key conforming to the
	// "aws.ecs.task.family" semantic conventions. It represents the family name of
	// the [ECS task definition] used to create the ECS task.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry-family"
	//
	// [ECS task definition]: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html
	AWSECSTaskFamilyKey = attribute.Key("aws.ecs.task.family")

	// AWSECSTaskIDKey is the attribute Key conforming to the "aws.ecs.task.id"
	// semantic conventions. It represents the ID of a running ECS task. The ID MUST
	// be extracted from `task.arn`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "10838bed-421f-43ef-870a-f43feacbbb5b",
	// "23ebb8ac-c18f-46c6-8bbe-d55d0e37cfbd"
	AWSECSTaskIDKey = attribute.Key("aws.ecs.task.id")

	// AWSECSTaskRevisionKey is the attribute Key conforming to the
	// "aws.ecs.task.revision" semantic conventions. It represents the revision for
	// the task definition used to create the ECS task.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "8", "26"
	AWSECSTaskRevisionKey = attribute.Key("aws.ecs.task.revision")

	// AWSEKSClusterARNKey is the attribute Key conforming to the
	// "aws.eks.cluster.arn" semantic conventions. It represents the ARN of an EKS
	// cluster.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "arn:aws:ecs:us-west-2:123456789123:cluster/my-cluster"
	AWSEKSClusterARNKey = attribute.Key("aws.eks.cluster.arn")

	// AWSExtendedRequestIDKey is the attribute Key conforming to the
	// "aws.extended_request_id" semantic conventions. It represents the AWS
	// extended request ID as returned in the response header `x-amz-id-2`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "wzHcyEWfmOGDIE5QOhTAqFDoDWP3y8IUvpNINCwL9N4TEHbUw0/gZJ+VZTmCNCWR7fezEN3eCiQ="
	AWSExtendedRequestIDKey = attribute.Key("aws.extended_request_id")

	// AWSLambdaInvokedARNKey is the attribute Key conforming to the
	// "aws.lambda.invoked_arn" semantic conventions. It represents the full invoked
	// ARN as provided on the `Context` passed to the function (
	// `Lambda-Runtime-Invoked-Function-Arn` header on the
	// `/runtime/invocation/next` applicable).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "arn:aws:lambda:us-east-1:123456:function:myfunction:myalias"
	// Note: This may be different from `cloud.resource_id` if an alias is involved.
	AWSLambdaInvokedARNKey = attribute.Key("aws.lambda.invoked_arn")

	// AWSLogGroupARNsKey is the attribute Key conforming to the
	// "aws.log.group.arns" semantic conventions. It represents the Amazon Resource
	// Name(s) (ARN) of the AWS log group(s).
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "arn:aws:logs:us-west-1:123456789012:log-group:/aws/my/group:*"
	// Note: See the [log group ARN format documentation].
	//
	// [log group ARN format documentation]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html#CWL_ARN_Format
	AWSLogGroupARNsKey = attribute.Key("aws.log.group.arns")

	// AWSLogGroupNamesKey is the attribute Key conforming to the
	// "aws.log.group.names" semantic conventions. It represents the name(s) of the
	// AWS log group(s) an application is writing to.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/aws/lambda/my-function", "opentelemetry-service"
	// Note: Multiple log groups must be supported for cases like multi-container
	// applications, where a single application has sidecar containers, and each
	// write to their own log group.
	AWSLogGroupNamesKey = attribute.Key("aws.log.group.names")

	// AWSLogStreamARNsKey is the attribute Key conforming to the
	// "aws.log.stream.arns" semantic conventions. It represents the ARN(s) of the
	// AWS log stream(s).
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "arn:aws:logs:us-west-1:123456789012:log-group:/aws/my/group:log-stream:logs/main/10838bed-421f-43ef-870a-f43feacbbb5b"
	// Note: See the [log stream ARN format documentation]. One log group can
	// contain several log streams, so these ARNs necessarily identify both a log
	// group and a log stream.
	//
	// [log stream ARN format documentation]: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html#CWL_ARN_Format
	AWSLogStreamARNsKey = attribute.Key("aws.log.stream.arns")

	// AWSLogStreamNamesKey is the attribute Key conforming to the
	// "aws.log.stream.names" semantic conventions. It represents the name(s) of the
	// AWS log stream(s) an application is writing to.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "logs/main/10838bed-421f-43ef-870a-f43feacbbb5b"
	AWSLogStreamNamesKey = attribute.Key("aws.log.stream.names")

	// AWSRequestIDKey is the attribute Key conforming to the "aws.request_id"
	// semantic conventions. It represents the AWS request ID as returned in the
	// response headers `x-amzn-requestid`, `x-amzn-request-id` or
	// `x-amz-request-id`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "79b9da39-b7ae-508a-a6bc-864b2829c622", "C9ER4AJX75574TDJ"
	AWSRequestIDKey = attribute.Key("aws.request_id")

	// AWSS3BucketKey is the attribute Key conforming to the "aws.s3.bucket"
	// semantic conventions. It represents the S3 bucket name the request refers to.
	// Corresponds to the `--bucket` parameter of the [S3 API] operations.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "some-bucket-name"
	// Note: The `bucket` attribute is applicable to all S3 operations that
	// reference a bucket, i.e. that require the bucket name as a mandatory
	// parameter.
	// This applies to almost all S3 operations except `list-buckets`.
	//
	// [S3 API]: https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html
	AWSS3BucketKey = attribute.Key("aws.s3.bucket")

	// AWSS3CopySourceKey is the attribute Key conforming to the
	// "aws.s3.copy_source" semantic conventions. It represents the source object
	// (in the form `bucket`/`key`) for the copy operation.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "someFile.yml"
	// Note: The `copy_source` attribute applies to S3 copy operations and
	// corresponds to the `--copy-source` parameter
	// of the [copy-object operation within the S3 API].
	// This applies in particular to the following operations:
	//
	//   - [copy-object]
	//   - [upload-part-copy]
	//
	//
	// [copy-object operation within the S3 API]: https://docs.aws.amazon.com/cli/latest/reference/s3api/copy-object.html
	// [copy-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/copy-object.html
	// [upload-part-copy]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html
	AWSS3CopySourceKey = attribute.Key("aws.s3.copy_source")

	// AWSS3DeleteKey is the attribute Key conforming to the "aws.s3.delete"
	// semantic conventions. It represents the delete request container that
	// specifies the objects to be deleted.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "Objects=[{Key=string,VersionId=string},{Key=string,VersionId=string}],Quiet=boolean"
	// Note: The `delete` attribute is only applicable to the [delete-object]
	// operation.
	// The `delete` attribute corresponds to the `--delete` parameter of the
	// [delete-objects operation within the S3 API].
	//
	// [delete-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html
	// [delete-objects operation within the S3 API]: https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-objects.html
	AWSS3DeleteKey = attribute.Key("aws.s3.delete")

	// AWSS3KeyKey is the attribute Key conforming to the "aws.s3.key" semantic
	// conventions. It represents the S3 object key the request refers to.
	// Corresponds to the `--key` parameter of the [S3 API] operations.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "someFile.yml"
	// Note: The `key` attribute is applicable to all object-related S3 operations,
	// i.e. that require the object key as a mandatory parameter.
	// This applies in particular to the following operations:
	//
	//   - [copy-object]
	//   - [delete-object]
	//   - [get-object]
	//   - [head-object]
	//   - [put-object]
	//   - [restore-object]
	//   - [select-object-content]
	//   - [abort-multipart-upload]
	//   - [complete-multipart-upload]
	//   - [create-multipart-upload]
	//   - [list-parts]
	//   - [upload-part]
	//   - [upload-part-copy]
	//
	//
	// [S3 API]: https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html
	// [copy-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/copy-object.html
	// [delete-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html
	// [get-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html
	// [head-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/head-object.html
	// [put-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html
	// [restore-object]: https://docs.aws.amazon.com/cli/latest/reference/s3api/restore-object.html
	// [select-object-content]: https://docs.aws.amazon.com/cli/latest/reference/s3api/select-object-content.html
	// [abort-multipart-upload]: https://docs.aws.amazon.com/cli/latest/reference/s3api/abort-multipart-upload.html
	// [complete-multipart-upload]: https://docs.aws.amazon.com/cli/latest/reference/s3api/complete-multipart-upload.html
	// [create-multipart-upload]: https://docs.aws.amazon.com/cli/latest/reference/s3api/create-multipart-upload.html
	// [list-parts]: https://docs.aws.amazon.com/cli/latest/reference/s3api/list-parts.html
	// [upload-part]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html
	// [upload-part-copy]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html
	AWSS3KeyKey = attribute.Key("aws.s3.key")

	// AWSS3PartNumberKey is the attribute Key conforming to the
	// "aws.s3.part_number" semantic conventions. It represents the part number of
	// the part being uploaded in a multipart-upload operation. This is a positive
	// integer between 1 and 10,000.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 3456
	// Note: The `part_number` attribute is only applicable to the [upload-part]
	// and [upload-part-copy] operations.
	// The `part_number` attribute corresponds to the `--part-number` parameter of
	// the
	// [upload-part operation within the S3 API].
	//
	// [upload-part]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html
	// [upload-part-copy]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html
	// [upload-part operation within the S3 API]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html
	AWSS3PartNumberKey = attribute.Key("aws.s3.part_number")

	// AWSS3UploadIDKey is the attribute Key conforming to the "aws.s3.upload_id"
	// semantic conventions. It represents the upload ID that identifies the
	// multipart upload.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "dfRtDYWFbkRONycy.Yxwh66Yjlx.cph0gtNBtJ"
	// Note: The `upload_id` attribute applies to S3 multipart-upload operations and
	// corresponds to the `--upload-id` parameter
	// of the [S3 API] multipart operations.
	// This applies in particular to the following operations:
	//
	//   - [abort-multipart-upload]
	//   - [complete-multipart-upload]
	//   - [list-parts]
	//   - [upload-part]
	//   - [upload-part-copy]
	//
	//
	// [S3 API]: https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html
	// [abort-multipart-upload]: https://docs.aws.amazon.com/cli/latest/reference/s3api/abort-multipart-upload.html
	// [complete-multipart-upload]: https://docs.aws.amazon.com/cli/latest/reference/s3api/complete-multipart-upload.html
	// [list-parts]: https://docs.aws.amazon.com/cli/latest/reference/s3api/list-parts.html
	// [upload-part]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part.html
	// [upload-part-copy]: https://docs.aws.amazon.com/cli/latest/reference/s3api/upload-part-copy.html
	AWSS3UploadIDKey = attribute.Key("aws.s3.upload_id")
)

Namespace: aws

View Source
const (
	// AzNamespaceKey is the attribute Key conforming to the "az.namespace" semantic
	// conventions. It represents the [Azure Resource Provider Namespace] as
	// recognized by the client.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Microsoft.Storage", "Microsoft.KeyVault", "Microsoft.ServiceBus"
	//
	// [Azure Resource Provider Namespace]: https://learn.microsoft.com/azure/azure-resource-manager/management/azure-services-resource-providers
	AzNamespaceKey = attribute.Key("az.namespace")

	// AzServiceRequestIDKey is the attribute Key conforming to the
	// "az.service_request_id" semantic conventions. It represents the unique
	// identifier of the service request. It's generated by the Azure service and
	// returned with the response.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "00000000-0000-0000-0000-000000000000"
	AzServiceRequestIDKey = attribute.Key("az.service_request_id")
)

Namespace: az

View Source
const (
	// AzureClientIDKey is the attribute Key conforming to the "azure.client.id"
	// semantic conventions. It represents the unique identifier of the client
	// instance.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "3ba4827d-4422-483f-b59f-85b74211c11d", "storage-client-1"
	AzureClientIDKey = attribute.Key("azure.client.id")

	// AzureCosmosDBConnectionModeKey is the attribute Key conforming to the
	// "azure.cosmosdb.connection.mode" semantic conventions. It represents the
	// cosmos client connection mode.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	AzureCosmosDBConnectionModeKey = attribute.Key("azure.cosmosdb.connection.mode")

	// AzureCosmosDBConsistencyLevelKey is the attribute Key conforming to the
	// "azure.cosmosdb.consistency.level" semantic conventions. It represents the
	// account or request [consistency level].
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Eventual", "ConsistentPrefix", "BoundedStaleness", "Strong",
	// "Session"
	//
	// [consistency level]: https://learn.microsoft.com/azure/cosmos-db/consistency-levels
	AzureCosmosDBConsistencyLevelKey = attribute.Key("azure.cosmosdb.consistency.level")

	// AzureCosmosDBOperationContactedRegionsKey is the attribute Key conforming to
	// the "azure.cosmosdb.operation.contacted_regions" semantic conventions. It
	// represents the list of regions contacted during operation in the order that
	// they were contacted. If there is more than one region listed, it indicates
	// that the operation was performed on multiple regions i.e. cross-regional
	// call.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "North Central US", "Australia East", "Australia Southeast"
	// Note: Region name matches the format of `displayName` in [Azure Location API]
	//
	// [Azure Location API]: https://learn.microsoft.com/rest/api/subscription/subscriptions/list-locations?view=rest-subscription-2021-10-01&tabs=HTTP#location
	AzureCosmosDBOperationContactedRegionsKey = attribute.Key("azure.cosmosdb.operation.contacted_regions")

	// AzureCosmosDBOperationRequestChargeKey is the attribute Key conforming to the
	// "azure.cosmosdb.operation.request_charge" semantic conventions. It represents
	// the number of request units consumed by the operation.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 46.18, 1.0
	AzureCosmosDBOperationRequestChargeKey = attribute.Key("azure.cosmosdb.operation.request_charge")

	// AzureCosmosDBRequestBodySizeKey is the attribute Key conforming to the
	// "azure.cosmosdb.request.body.size" semantic conventions. It represents the
	// request payload size in bytes.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	AzureCosmosDBRequestBodySizeKey = attribute.Key("azure.cosmosdb.request.body.size")

	// AzureCosmosDBResponseSubStatusCodeKey is the attribute Key conforming to the
	// "azure.cosmosdb.response.sub_status_code" semantic conventions. It represents
	// the cosmos DB sub status code.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1000, 1002
	AzureCosmosDBResponseSubStatusCodeKey = attribute.Key("azure.cosmosdb.response.sub_status_code")
)

Namespace: azure

View Source
const (
	// BrowserBrandsKey is the attribute Key conforming to the "browser.brands"
	// semantic conventions. It represents the array of brand name and version
	// separated by a space.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: " Not A;Brand 99", "Chromium 99", "Chrome 99"
	// Note: This value is intended to be taken from the [UA client hints API] (
	// `navigator.userAgentData.brands`).
	//
	// [UA client hints API]: https://wicg.github.io/ua-client-hints/#interface
	BrowserBrandsKey = attribute.Key("browser.brands")

	// BrowserLanguageKey is the attribute Key conforming to the "browser.language"
	// semantic conventions. It represents the preferred language of the user using
	// the browser.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "en", "en-US", "fr", "fr-FR"
	// Note: This value is intended to be taken from the Navigator API
	// `navigator.language`.
	BrowserLanguageKey = attribute.Key("browser.language")

	// BrowserMobileKey is the attribute Key conforming to the "browser.mobile"
	// semantic conventions. It represents a boolean that is true if the browser is
	// running on a mobile device.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: This value is intended to be taken from the [UA client hints API] (
	// `navigator.userAgentData.mobile`). If unavailable, this attribute SHOULD be
	// left unset.
	//
	// [UA client hints API]: https://wicg.github.io/ua-client-hints/#interface
	BrowserMobileKey = attribute.Key("browser.mobile")

	// BrowserPlatformKey is the attribute Key conforming to the "browser.platform"
	// semantic conventions. It represents the platform on which the browser is
	// running.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Windows", "macOS", "Android"
	// Note: This value is intended to be taken from the [UA client hints API] (
	// `navigator.userAgentData.platform`). If unavailable, the legacy
	// `navigator.platform` API SHOULD NOT be used instead and this attribute SHOULD
	// be left unset in order for the values to be consistent.
	// The list of possible values is defined in the
	// [W3C User-Agent Client Hints specification]. Note that some (but not all) of
	// these values can overlap with values in the
	// [`os.type` and `os.name` attributes]. However, for consistency, the values in
	// the `browser.platform` attribute should capture the exact value that the user
	// agent provides.
	//
	// [UA client hints API]: https://wicg.github.io/ua-client-hints/#interface
	// [W3C User-Agent Client Hints specification]: https://wicg.github.io/ua-client-hints/#sec-ch-ua-platform
	// [`os.type` and `os.name` attributes]: ./os.md
	BrowserPlatformKey = attribute.Key("browser.platform")
)

Namespace: browser

View Source
const (
	// CassandraConsistencyLevelKey is the attribute Key conforming to the
	// "cassandra.consistency.level" semantic conventions. It represents the
	// consistency level of the query. Based on consistency values from [CQL].
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	//
	// [CQL]: https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/dml/dmlConfigConsistency.html
	CassandraConsistencyLevelKey = attribute.Key("cassandra.consistency.level")

	// CassandraCoordinatorDCKey is the attribute Key conforming to the
	// "cassandra.coordinator.dc" semantic conventions. It represents the data
	// center of the coordinating node for a query.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: us-west-2
	CassandraCoordinatorDCKey = attribute.Key("cassandra.coordinator.dc")

	// CassandraCoordinatorIDKey is the attribute Key conforming to the
	// "cassandra.coordinator.id" semantic conventions. It represents the ID of the
	// coordinating node for a query.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: be13faa2-8574-4d71-926d-27f16cf8a7af
	CassandraCoordinatorIDKey = attribute.Key("cassandra.coordinator.id")

	// CassandraPageSizeKey is the attribute Key conforming to the
	// "cassandra.page.size" semantic conventions. It represents the fetch size used
	// for paging, i.e. how many rows will be returned at once.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 5000
	CassandraPageSizeKey = attribute.Key("cassandra.page.size")

	// CassandraQueryIdempotentKey is the attribute Key conforming to the
	// "cassandra.query.idempotent" semantic conventions. It represents the whether
	// or not the query is idempotent.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	CassandraQueryIdempotentKey = attribute.Key("cassandra.query.idempotent")

	// CassandraSpeculativeExecutionCountKey is the attribute Key conforming to the
	// "cassandra.speculative_execution.count" semantic conventions. It represents
	// the number of times a query was speculatively executed. Not set or `0` if the
	// query was not executed speculatively.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 0, 2
	CassandraSpeculativeExecutionCountKey = attribute.Key("cassandra.speculative_execution.count")
)

Namespace: cassandra

View Source
const (
	// CICDPipelineNameKey is the attribute Key conforming to the
	// "cicd.pipeline.name" semantic conventions. It represents the human readable
	// name of the pipeline within a CI/CD system.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Build and Test", "Lint", "Deploy Go Project",
	// "deploy_to_environment"
	CICDPipelineNameKey = attribute.Key("cicd.pipeline.name")

	// CICDPipelineResultKey is the attribute Key conforming to the
	// "cicd.pipeline.result" semantic conventions. It represents the result of a
	// pipeline run.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "success", "failure", "timeout", "skipped"
	CICDPipelineResultKey = attribute.Key("cicd.pipeline.result")

	// CICDPipelineRunIDKey is the attribute Key conforming to the
	// "cicd.pipeline.run.id" semantic conventions. It represents the unique
	// identifier of a pipeline run within a CI/CD system.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "120912"
	CICDPipelineRunIDKey = attribute.Key("cicd.pipeline.run.id")

	// CICDPipelineRunStateKey is the attribute Key conforming to the
	// "cicd.pipeline.run.state" semantic conventions. It represents the pipeline
	// run goes through these states during its lifecycle.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "pending", "executing", "finalizing"
	CICDPipelineRunStateKey = attribute.Key("cicd.pipeline.run.state")

	// CICDPipelineRunURLFullKey is the attribute Key conforming to the
	// "cicd.pipeline.run.url.full" semantic conventions. It represents the [URL] of
	// the pipeline run, providing the complete address in order to locate and
	// identify the pipeline run.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "https://github.com/open-telemetry/semantic-conventions/actions/runs/9753949763?pr=1075"
	//
	// [URL]: https://wikipedia.org/wiki/URL
	CICDPipelineRunURLFullKey = attribute.Key("cicd.pipeline.run.url.full")

	// CICDPipelineTaskNameKey is the attribute Key conforming to the
	// "cicd.pipeline.task.name" semantic conventions. It represents the human
	// readable name of a task within a pipeline. Task here most closely aligns with
	// a [computing process] in a pipeline. Other terms for tasks include commands,
	// steps, and procedures.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Run GoLang Linter", "Go Build", "go-test", "deploy_binary"
	//
	// [computing process]: https://wikipedia.org/wiki/Pipeline_(computing)
	CICDPipelineTaskNameKey = attribute.Key("cicd.pipeline.task.name")

	// CICDPipelineTaskRunIDKey is the attribute Key conforming to the
	// "cicd.pipeline.task.run.id" semantic conventions. It represents the unique
	// identifier of a task run within a pipeline.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "12097"
	CICDPipelineTaskRunIDKey = attribute.Key("cicd.pipeline.task.run.id")

	// CICDPipelineTaskRunURLFullKey is the attribute Key conforming to the
	// "cicd.pipeline.task.run.url.full" semantic conventions. It represents the
	// [URL] of the pipeline task run, providing the complete address in order to
	// locate and identify the pipeline task run.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "https://github.com/open-telemetry/semantic-conventions/actions/runs/9753949763/job/26920038674?pr=1075"
	//
	// [URL]: https://wikipedia.org/wiki/URL
	CICDPipelineTaskRunURLFullKey = attribute.Key("cicd.pipeline.task.run.url.full")

	// CICDPipelineTaskTypeKey is the attribute Key conforming to the
	// "cicd.pipeline.task.type" semantic conventions. It represents the type of the
	// task within a pipeline.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "build", "test", "deploy"
	CICDPipelineTaskTypeKey = attribute.Key("cicd.pipeline.task.type")

	// CICDSystemComponentKey is the attribute Key conforming to the
	// "cicd.system.component" semantic conventions. It represents the name of a
	// component of the CICD system.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "controller", "scheduler", "agent"
	CICDSystemComponentKey = attribute.Key("cicd.system.component")

	// CICDWorkerStateKey is the attribute Key conforming to the "cicd.worker.state"
	// semantic conventions. It represents the state of a CICD worker / agent.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "idle", "busy", "down"
	CICDWorkerStateKey = attribute.Key("cicd.worker.state")
)

Namespace: cicd

View Source
const (
	// ClientAddressKey is the attribute Key conforming to the "client.address"
	// semantic conventions. It represents the client address - domain name if
	// available without reverse DNS lookup; otherwise, IP address or Unix domain
	// socket name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "client.example.com", "10.1.2.80", "/tmp/my.sock"
	// Note: When observed from the server side, and when communicating through an
	// intermediary, `client.address` SHOULD represent the client address behind any
	// intermediaries, for example proxies, if it's available.
	ClientAddressKey = attribute.Key("client.address")

	// ClientPortKey is the attribute Key conforming to the "client.port" semantic
	// conventions. It represents the client port number.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: 65123
	// Note: When observed from the server side, and when communicating through an
	// intermediary, `client.port` SHOULD represent the client port behind any
	// intermediaries, for example proxies, if it's available.
	ClientPortKey = attribute.Key("client.port")
)

Namespace: client

View Source
const (
	// CloudAccountIDKey is the attribute Key conforming to the "cloud.account.id"
	// semantic conventions. It represents the cloud account ID the resource is
	// assigned to.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "111111111111", "opentelemetry"
	CloudAccountIDKey = attribute.Key("cloud.account.id")

	// CloudAvailabilityZoneKey is the attribute Key conforming to the
	// "cloud.availability_zone" semantic conventions. It represents the cloud
	// regions often have multiple, isolated locations known as zones to increase
	// availability. Availability zone represents the zone where the resource is
	// running.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "us-east-1c"
	// Note: Availability zones are called "zones" on Alibaba Cloud and Google
	// Cloud.
	CloudAvailabilityZoneKey = attribute.Key("cloud.availability_zone")

	// CloudPlatformKey is the attribute Key conforming to the "cloud.platform"
	// semantic conventions. It represents the cloud platform in use.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: The prefix of the service SHOULD match the one specified in
	// `cloud.provider`.
	CloudPlatformKey = attribute.Key("cloud.platform")

	// CloudProviderKey is the attribute Key conforming to the "cloud.provider"
	// semantic conventions. It represents the name of the cloud provider.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	CloudProviderKey = attribute.Key("cloud.provider")

	// CloudRegionKey is the attribute Key conforming to the "cloud.region" semantic
	// conventions. It represents the geographical region the resource is running.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "us-central1", "us-east-1"
	// Note: Refer to your provider's docs to see the available regions, for example
	// [Alibaba Cloud regions], [AWS regions], [Azure regions],
	// [Google Cloud regions], or [Tencent Cloud regions].
	//
	// [Alibaba Cloud regions]: https://www.alibabacloud.com/help/doc-detail/40654.htm
	// [AWS regions]: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
	// [Azure regions]: https://azure.microsoft.com/global-infrastructure/geographies/
	// [Google Cloud regions]: https://cloud.google.com/about/locations
	// [Tencent Cloud regions]: https://www.tencentcloud.com/document/product/213/6091
	CloudRegionKey = attribute.Key("cloud.region")

	// CloudResourceIDKey is the attribute Key conforming to the "cloud.resource_id"
	// semantic conventions. It represents the cloud provider-specific native
	// identifier of the monitored cloud resource (e.g. an [ARN] on AWS, a
	// [fully qualified resource ID] on Azure, a [full resource name] on GCP).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "arn:aws:lambda:REGION:ACCOUNT_ID:function:my-function",
	// "//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID",
	// "/subscriptions/<SUBSCRIPTION_GUID>/resourceGroups/<RG>
	// /providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>"
	// Note: On some cloud providers, it may not be possible to determine the full
	// ID at startup,
	// so it may be necessary to set `cloud.resource_id` as a span attribute
	// instead.
	//
	// The exact value to use for `cloud.resource_id` depends on the cloud provider.
	// The following well-known definitions MUST be used if you set this attribute
	// and they apply:
	//
	//   - **AWS Lambda:** The function [ARN].
	//     Take care not to use the "invoked ARN" directly but replace any
	//     [alias suffix]
	//     with the resolved function version, as the same runtime instance may be
	//     invocable with
	//     multiple different aliases.
	//   - **GCP:** The [URI of the resource]
	//   - **Azure:** The [Fully Qualified Resource ID] of the invoked function,
	//     *not* the function app, having the form
	//
	//     `/subscriptions/<SUBSCRIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>`
	//     .
	//     This means that a span attribute MUST be used, as an Azure function app
	//     can host multiple functions that would usually share
	//     a TracerProvider.
	//
	//
	// [ARN]: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
	// [fully qualified resource ID]: https://learn.microsoft.com/rest/api/resources/resources/get-by-id
	// [full resource name]: https://google.aip.dev/122#full-resource-names
	// [ARN]: https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
	// [alias suffix]: https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html
	// [URI of the resource]: https://cloud.google.com/iam/docs/full-resource-names
	// [Fully Qualified Resource ID]: https://docs.microsoft.com/rest/api/resources/resources/get-by-id
	CloudResourceIDKey = attribute.Key("cloud.resource_id")
)

Namespace: cloud

View Source
const (
	// CloudeventsEventIDKey is the attribute Key conforming to the
	// "cloudevents.event_id" semantic conventions. It represents the [event_id]
	// uniquely identifies the event.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "123e4567-e89b-12d3-a456-426614174000", "0001"
	//
	// [event_id]: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#id
	CloudeventsEventIDKey = attribute.Key("cloudevents.event_id")

	// CloudeventsEventSourceKey is the attribute Key conforming to the
	// "cloudevents.event_source" semantic conventions. It represents the [source]
	// identifies the context in which an event happened.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "https://github.com/cloudevents", "/cloudevents/spec/pull/123",
	// "my-service"
	//
	// [source]: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#source-1
	CloudeventsEventSourceKey = attribute.Key("cloudevents.event_source")

	// CloudeventsEventSpecVersionKey is the attribute Key conforming to the
	// "cloudevents.event_spec_version" semantic conventions. It represents the
	// [version of the CloudEvents specification] which the event uses.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1.0
	//
	// [version of the CloudEvents specification]: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#specversion
	CloudeventsEventSpecVersionKey = attribute.Key("cloudevents.event_spec_version")

	// CloudeventsEventSubjectKey is the attribute Key conforming to the
	// "cloudevents.event_subject" semantic conventions. It represents the [subject]
	//  of the event in the context of the event producer (identified by source).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: mynewfile.jpg
	//
	// [subject]: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#subject
	CloudeventsEventSubjectKey = attribute.Key("cloudevents.event_subject")

	// CloudeventsEventTypeKey is the attribute Key conforming to the
	// "cloudevents.event_type" semantic conventions. It represents the [event_type]
	//  contains a value describing the type of event related to the originating
	// occurrence.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "com.github.pull_request.opened", "com.example.object.deleted.v2"
	//
	// [event_type]: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md#type
	CloudeventsEventTypeKey = attribute.Key("cloudevents.event_type")
)

Namespace: cloudevents

View Source
const (
	// CloudfoundryAppIDKey is the attribute Key conforming to the
	// "cloudfoundry.app.id" semantic conventions. It represents the guid of the
	// application.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "218fc5a9-a5f1-4b54-aa05-46717d0ab26d"
	// Note: Application instrumentation should use the value from environment
	// variable `VCAP_APPLICATION.application_id`. This is the same value as
	// reported by `cf app <app-name> --guid`.
	CloudfoundryAppIDKey = attribute.Key("cloudfoundry.app.id")

	// CloudfoundryAppInstanceIDKey is the attribute Key conforming to the
	// "cloudfoundry.app.instance.id" semantic conventions. It represents the index
	// of the application instance. 0 when just one instance is active.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "0", "1"
	// Note: CloudFoundry defines the `instance_id` in the [Loggregator v2 envelope]
	// .
	// It is used for logs and metrics emitted by CloudFoundry. It is
	// supposed to contain the application instance index for applications
	// deployed on the runtime.
	//
	// Application instrumentation should use the value from environment
	// variable `CF_INSTANCE_INDEX`.
	//
	// [Loggregator v2 envelope]: https://github.com/cloudfoundry/loggregator-api#v2-envelope
	CloudfoundryAppInstanceIDKey = attribute.Key("cloudfoundry.app.instance.id")

	// CloudfoundryAppNameKey is the attribute Key conforming to the
	// "cloudfoundry.app.name" semantic conventions. It represents the name of the
	// application.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-app-name"
	// Note: Application instrumentation should use the value from environment
	// variable `VCAP_APPLICATION.application_name`. This is the same value
	// as reported by `cf apps`.
	CloudfoundryAppNameKey = attribute.Key("cloudfoundry.app.name")

	// CloudfoundryOrgIDKey is the attribute Key conforming to the
	// "cloudfoundry.org.id" semantic conventions. It represents the guid of the
	// CloudFoundry org the application is running in.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "218fc5a9-a5f1-4b54-aa05-46717d0ab26d"
	// Note: Application instrumentation should use the value from environment
	// variable `VCAP_APPLICATION.org_id`. This is the same value as
	// reported by `cf org <org-name> --guid`.
	CloudfoundryOrgIDKey = attribute.Key("cloudfoundry.org.id")

	// CloudfoundryOrgNameKey is the attribute Key conforming to the
	// "cloudfoundry.org.name" semantic conventions. It represents the name of the
	// CloudFoundry organization the app is running in.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-org-name"
	// Note: Application instrumentation should use the value from environment
	// variable `VCAP_APPLICATION.org_name`. This is the same value as
	// reported by `cf orgs`.
	CloudfoundryOrgNameKey = attribute.Key("cloudfoundry.org.name")

	// CloudfoundryProcessIDKey is the attribute Key conforming to the
	// "cloudfoundry.process.id" semantic conventions. It represents the UID
	// identifying the process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "218fc5a9-a5f1-4b54-aa05-46717d0ab26d"
	// Note: Application instrumentation should use the value from environment
	// variable `VCAP_APPLICATION.process_id`. It is supposed to be equal to
	// `VCAP_APPLICATION.app_id` for applications deployed to the runtime.
	// For system components, this could be the actual PID.
	CloudfoundryProcessIDKey = attribute.Key("cloudfoundry.process.id")

	// CloudfoundryProcessTypeKey is the attribute Key conforming to the
	// "cloudfoundry.process.type" semantic conventions. It represents the type of
	// process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "web"
	// Note: CloudFoundry applications can consist of multiple jobs. Usually the
	// main process will be of type `web`. There can be additional background
	// tasks or side-cars with different process types.
	CloudfoundryProcessTypeKey = attribute.Key("cloudfoundry.process.type")

	// CloudfoundrySpaceIDKey is the attribute Key conforming to the
	// "cloudfoundry.space.id" semantic conventions. It represents the guid of the
	// CloudFoundry space the application is running in.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "218fc5a9-a5f1-4b54-aa05-46717d0ab26d"
	// Note: Application instrumentation should use the value from environment
	// variable `VCAP_APPLICATION.space_id`. This is the same value as
	// reported by `cf space <space-name> --guid`.
	CloudfoundrySpaceIDKey = attribute.Key("cloudfoundry.space.id")

	// CloudfoundrySpaceNameKey is the attribute Key conforming to the
	// "cloudfoundry.space.name" semantic conventions. It represents the name of the
	// CloudFoundry space the application is running in.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-space-name"
	// Note: Application instrumentation should use the value from environment
	// variable `VCAP_APPLICATION.space_name`. This is the same value as
	// reported by `cf spaces`.
	CloudfoundrySpaceNameKey = attribute.Key("cloudfoundry.space.name")

	// CloudfoundrySystemIDKey is the attribute Key conforming to the
	// "cloudfoundry.system.id" semantic conventions. It represents a guid or
	// another name describing the event source.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "cf/gorouter"
	// Note: CloudFoundry defines the `source_id` in the [Loggregator v2 envelope].
	// It is used for logs and metrics emitted by CloudFoundry. It is
	// supposed to contain the component name, e.g. "gorouter", for
	// CloudFoundry components.
	//
	// When system components are instrumented, values from the
	// [Bosh spec]
	// should be used. The `system.id` should be set to
	// `spec.deployment/spec.name`.
	//
	// [Loggregator v2 envelope]: https://github.com/cloudfoundry/loggregator-api#v2-envelope
	// [Bosh spec]: https://bosh.io/docs/jobs/#properties-spec
	CloudfoundrySystemIDKey = attribute.Key("cloudfoundry.system.id")

	// CloudfoundrySystemInstanceIDKey is the attribute Key conforming to the
	// "cloudfoundry.system.instance.id" semantic conventions. It represents a guid
	// describing the concrete instance of the event source.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "218fc5a9-a5f1-4b54-aa05-46717d0ab26d"
	// Note: CloudFoundry defines the `instance_id` in the [Loggregator v2 envelope]
	// .
	// It is used for logs and metrics emitted by CloudFoundry. It is
	// supposed to contain the vm id for CloudFoundry components.
	//
	// When system components are instrumented, values from the
	// [Bosh spec]
	// should be used. The `system.instance.id` should be set to `spec.id`.
	//
	// [Loggregator v2 envelope]: https://github.com/cloudfoundry/loggregator-api#v2-envelope
	// [Bosh spec]: https://bosh.io/docs/jobs/#properties-spec
	CloudfoundrySystemInstanceIDKey = attribute.Key("cloudfoundry.system.instance.id")
)

Namespace: cloudfoundry

View Source
const (
	// CodeColumnNumberKey is the attribute Key conforming to the
	// "code.column.number" semantic conventions. It represents the column number in
	// `code.file.path` best representing the operation. It SHOULD point within the
	// code unit named in `code.function.name`.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	CodeColumnNumberKey = attribute.Key("code.column.number")

	// CodeFilePathKey is the attribute Key conforming to the "code.file.path"
	// semantic conventions. It represents the source code file name that identifies
	// the code unit as uniquely as possible (preferably an absolute file path).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: /usr/local/MyApplication/content_root/app/index.php
	CodeFilePathKey = attribute.Key("code.file.path")

	// CodeFunctionNameKey is the attribute Key conforming to the
	// "code.function.name" semantic conventions. It represents the method or
	// function fully-qualified name without arguments. The value should fit the
	// natural representation of the language runtime, which is also likely the same
	// used within `code.stacktrace` attribute value.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: "com.example.MyHttpService.serveRequest",
	// "GuzzleHttp\Client::transfer", "fopen"
	// Note: Values and format depends on each language runtime, thus it is
	// impossible to provide an exhaustive list of examples.
	// The values are usually the same (or prefixes of) the ones found in native
	// stack trace representation stored in
	// `code.stacktrace` without information on arguments.
	//
	// Examples:
	//
	//   - Java method: `com.example.MyHttpService.serveRequest`
	//   - Java anonymous class method: `com.mycompany.Main$1.myMethod`
	//   - Java lambda method:
	//     `com.mycompany.Main$$Lambda/0x0000748ae4149c00.myMethod`
	//   - PHP function: `GuzzleHttp\Client::transfer
	//   - Go function: `github.com/my/repo/pkg.foo.func5`
	//   - Elixir: `OpenTelemetry.Ctx.new`
	//   - Erlang: `opentelemetry_ctx:new`
	//   - Rust: `playground::my_module::my_cool_func`
	//   - C function: `fopen`
	CodeFunctionNameKey = attribute.Key("code.function.name")

	// CodeLineNumberKey is the attribute Key conforming to the "code.line.number"
	// semantic conventions. It represents the line number in `code.file.path` best
	// representing the operation. It SHOULD point within the code unit named in
	// `code.function.name`.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	CodeLineNumberKey = attribute.Key("code.line.number")

	// CodeStacktraceKey is the attribute Key conforming to the "code.stacktrace"
	// semantic conventions. It represents a stacktrace as a string in the natural
	// representation for the language runtime. The representation is identical to
	// [`exception.stacktrace`].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: at com.example.GenerateTrace.methodB(GenerateTrace.java:13)\n at
	// com.example.GenerateTrace.methodA(GenerateTrace.java:9)\n at
	// com.example.GenerateTrace.main(GenerateTrace.java:5)
	//
	// [`exception.stacktrace`]: /docs/exceptions/exceptions-spans.md#stacktrace-representation
	CodeStacktraceKey = attribute.Key("code.stacktrace")
)

Namespace: code

View Source
const (
	// ContainerCommandKey is the attribute Key conforming to the
	// "container.command" semantic conventions. It represents the command used to
	// run the container (i.e. the command name).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "otelcontribcol"
	// Note: If using embedded credentials or sensitive data, it is recommended to
	// remove them to prevent potential leakage.
	ContainerCommandKey = attribute.Key("container.command")

	// ContainerCommandArgsKey is the attribute Key conforming to the
	// "container.command_args" semantic conventions. It represents the all the
	// command arguments (including the command/executable itself) run by the
	// container.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "otelcontribcol", "--config", "config.yaml"
	ContainerCommandArgsKey = attribute.Key("container.command_args")

	// ContainerCommandLineKey is the attribute Key conforming to the
	// "container.command_line" semantic conventions. It represents the full command
	// run by the container as a single string representing the full command.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "otelcontribcol --config config.yaml"
	ContainerCommandLineKey = attribute.Key("container.command_line")

	// ContainerCsiPluginNameKey is the attribute Key conforming to the
	// "container.csi.plugin.name" semantic conventions. It represents the name of
	// the CSI ([Container Storage Interface]) plugin used by the volume.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "pd.csi.storage.gke.io"
	// Note: This can sometimes be referred to as a "driver" in CSI implementations.
	// This should represent the `name` field of the GetPluginInfo RPC.
	//
	// [Container Storage Interface]: https://github.com/container-storage-interface/spec
	ContainerCsiPluginNameKey = attribute.Key("container.csi.plugin.name")

	// ContainerCsiVolumeIDKey is the attribute Key conforming to the
	// "container.csi.volume.id" semantic conventions. It represents the unique
	// volume ID returned by the CSI ([Container Storage Interface]) plugin.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "projects/my-gcp-project/zones/my-gcp-zone/disks/my-gcp-disk"
	// Note: This can sometimes be referred to as a "volume handle" in CSI
	// implementations. This should represent the `Volume.volume_id` field in CSI
	// spec.
	//
	// [Container Storage Interface]: https://github.com/container-storage-interface/spec
	ContainerCsiVolumeIDKey = attribute.Key("container.csi.volume.id")

	// ContainerIDKey is the attribute Key conforming to the "container.id" semantic
	// conventions. It represents the container ID. Usually a UUID, as for example
	// used to [identify Docker containers]. The UUID might be abbreviated.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "a3bf90e006b2"
	//
	// [identify Docker containers]: https://docs.docker.com/engine/containers/run/#container-identification
	ContainerIDKey = attribute.Key("container.id")

	// ContainerImageIDKey is the attribute Key conforming to the
	// "container.image.id" semantic conventions. It represents the runtime specific
	// image identifier. Usually a hash algorithm followed by a UUID.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "sha256:19c92d0a00d1b66d897bceaa7319bee0dd38a10a851c60bcec9474aa3f01e50f"
	// Note: Docker defines a sha256 of the image id; `container.image.id`
	// corresponds to the `Image` field from the Docker container inspect [API]
	// endpoint.
	// K8s defines a link to the container registry repository with digest
	// `"imageID": "registry.azurecr.io /namespace/service/dockerfile@sha256:bdeabd40c3a8a492eaf9e8e44d0ebbb84bac7ee25ac0cf8a7159d25f62555625"`
	// .
	// The ID is assigned by the container runtime and can vary in different
	// environments. Consider using `oci.manifest.digest` if it is important to
	// identify the same image in different environments/runtimes.
	//
	// [API]: https://docs.docker.com/engine/api/v1.43/#tag/Container/operation/ContainerInspect
	ContainerImageIDKey = attribute.Key("container.image.id")

	// ContainerImageNameKey is the attribute Key conforming to the
	// "container.image.name" semantic conventions. It represents the name of the
	// image the container was built on.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "gcr.io/opentelemetry/operator"
	ContainerImageNameKey = attribute.Key("container.image.name")

	// ContainerImageRepoDigestsKey is the attribute Key conforming to the
	// "container.image.repo_digests" semantic conventions. It represents the repo
	// digests of the container image as provided by the container runtime.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "example@sha256:afcc7f1ac1b49db317a7196c902e61c6c3c4607d63599ee1a82d702d249a0ccb",
	// "internal.registry.example.com:5000/example@sha256:b69959407d21e8a062e0416bf13405bb2b71ed7a84dde4158ebafacfa06f5578"
	// Note: [Docker] and [CRI] report those under the `RepoDigests` field.
	//
	// [Docker]: https://docs.docker.com/engine/api/v1.43/#tag/Image/operation/ImageInspect
	// [CRI]: https://github.com/kubernetes/cri-api/blob/c75ef5b473bbe2d0a4fc92f82235efd665ea8e9f/pkg/apis/runtime/v1/api.proto#L1237-L1238
	ContainerImageRepoDigestsKey = attribute.Key("container.image.repo_digests")

	// ContainerImageTagsKey is the attribute Key conforming to the
	// "container.image.tags" semantic conventions. It represents the container
	// image tags. An example can be found in [Docker Image Inspect]. Should be only
	// the `<tag>` section of the full name for example from
	// `registry.example.com/my-org/my-image:<tag>`.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "v1.27.1", "3.5.7-0"
	//
	// [Docker Image Inspect]: https://docs.docker.com/engine/api/v1.43/#tag/Image/operation/ImageInspect
	ContainerImageTagsKey = attribute.Key("container.image.tags")

	// ContainerNameKey is the attribute Key conforming to the "container.name"
	// semantic conventions. It represents the container name used by container
	// runtime.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry-autoconf"
	ContainerNameKey = attribute.Key("container.name")

	// ContainerRuntimeKey is the attribute Key conforming to the
	// "container.runtime" semantic conventions. It represents the container runtime
	// managing this container.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "docker", "containerd", "rkt"
	ContainerRuntimeKey = attribute.Key("container.runtime")
)

Namespace: container

View Source
const (
	// CPULogicalNumberKey is the attribute Key conforming to the
	// "cpu.logical_number" semantic conventions. It represents the logical CPU
	// number [0..n-1].
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1
	CPULogicalNumberKey = attribute.Key("cpu.logical_number")

	// CPUModeKey is the attribute Key conforming to the "cpu.mode" semantic
	// conventions. It represents the mode of the CPU.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "user", "system"
	CPUModeKey = attribute.Key("cpu.mode")
)

Namespace: cpu

View Source
const (
	// DBClientConnectionPoolNameKey is the attribute Key conforming to the
	// "db.client.connection.pool.name" semantic conventions. It represents the name
	// of the connection pool; unique within the instrumented application. In case
	// the connection pool implementation doesn't provide a name, instrumentation
	// SHOULD use a combination of parameters that would make the name unique, for
	// example, combining attributes `server.address`, `server.port`, and
	// `db.namespace`, formatted as `server.address:server.port/db.namespace`.
	// Instrumentations that generate connection pool name following different
	// patterns SHOULD document it.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "myDataSource"
	DBClientConnectionPoolNameKey = attribute.Key("db.client.connection.pool.name")

	// DBClientConnectionStateKey is the attribute Key conforming to the
	// "db.client.connection.state" semantic conventions. It represents the state of
	// a connection in the pool.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "idle"
	DBClientConnectionStateKey = attribute.Key("db.client.connection.state")

	// DBCollectionNameKey is the attribute Key conforming to the
	// "db.collection.name" semantic conventions. It represents the name of a
	// collection (table, container) within the database.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: "public.users", "customers"
	// Note: It is RECOMMENDED to capture the value as provided by the application
	// without attempting to do any case normalization.
	//
	// The collection name SHOULD NOT be extracted from `db.query.text`,
	// when the database system supports cross-table queries in non-batch
	// operations.
	//
	// For batch operations, if the individual operations are known to have the same
	// collection name then that collection name SHOULD be used.
	DBCollectionNameKey = attribute.Key("db.collection.name")

	// DBNamespaceKey is the attribute Key conforming to the "db.namespace" semantic
	// conventions. It represents the name of the database, fully qualified within
	// the server address and port.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: "customers", "test.users"
	// Note: If a database system has multiple namespace components, they SHOULD be
	// concatenated (potentially using database system specific conventions) from
	// most general to most specific namespace component, and more specific
	// namespaces SHOULD NOT be captured without the more general namespaces, to
	// ensure that "startswith" queries for the more general namespaces will be
	// valid.
	// Semantic conventions for individual database systems SHOULD document what
	// `db.namespace` means in the context of that system.
	// It is RECOMMENDED to capture the value as provided by the application without
	// attempting to do any case normalization.
	DBNamespaceKey = attribute.Key("db.namespace")

	// DBOperationBatchSizeKey is the attribute Key conforming to the
	// "db.operation.batch.size" semantic conventions. It represents the number of
	// queries included in a batch operation.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: 2, 3, 4
	// Note: Operations are only considered batches when they contain two or more
	// operations, and so `db.operation.batch.size` SHOULD never be `1`.
	DBOperationBatchSizeKey = attribute.Key("db.operation.batch.size")

	// DBOperationNameKey is the attribute Key conforming to the "db.operation.name"
	// semantic conventions. It represents the name of the operation or command
	// being executed.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: "findAndModify", "HMSET", "SELECT"
	// Note: It is RECOMMENDED to capture the value as provided by the application
	// without attempting to do any case normalization.
	//
	// The operation name SHOULD NOT be extracted from `db.query.text`,
	// when the database system supports cross-table queries in non-batch
	// operations.
	//
	// For batch operations, if the individual operations are known to have the same
	// operation name
	// then that operation name SHOULD be used prepended by `BATCH `,
	// otherwise `db.operation.name` SHOULD be `BATCH` or some other database
	// system specific term if more applicable.
	DBOperationNameKey = attribute.Key("db.operation.name")

	// DBQuerySummaryKey is the attribute Key conforming to the "db.query.summary"
	// semantic conventions. It represents the low cardinality representation of a
	// database query text.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: "SELECT wuser_table", "INSERT shipping_details SELECT orders", "get
	// user by id"
	// Note: `db.query.summary` provides static summary of the query text. It
	// describes a class of database queries and is useful as a grouping key,
	// especially when analyzing telemetry for database calls involving complex
	// queries.
	// Summary may be available to the instrumentation through instrumentation hooks
	// or other means. If it is not available, instrumentations that support query
	// parsing SHOULD generate a summary following [Generating query summary]
	// section.
	//
	// [Generating query summary]: ../database/database-spans.md#generating-a-summary-of-the-query-text
	DBQuerySummaryKey = attribute.Key("db.query.summary")

	// DBQueryTextKey is the attribute Key conforming to the "db.query.text"
	// semantic conventions. It represents the database query being executed.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: "SELECT * FROM wuser_table where username = ?", "SET mykey ?"
	// Note: For sanitization see [Sanitization of `db.query.text`].
	// For batch operations, if the individual operations are known to have the same
	// query text then that query text SHOULD be used, otherwise all of the
	// individual query texts SHOULD be concatenated with separator `; ` or some
	// other database system specific separator if more applicable.
	// Even though parameterized query text can potentially have sensitive data, by
	// using a parameterized query the user is giving a strong signal that any
	// sensitive data will be passed as parameter values, and the benefit to
	// observability of capturing the static part of the query text by default
	// outweighs the risk.
	//
	// [Sanitization of `db.query.text`]: ../database/database-spans.md#sanitization-of-dbquerytext
	DBQueryTextKey = attribute.Key("db.query.text")

	// DBResponseReturnedRowsKey is the attribute Key conforming to the
	// "db.response.returned_rows" semantic conventions. It represents the number of
	// rows returned by the operation.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 10, 30, 1000
	DBResponseReturnedRowsKey = attribute.Key("db.response.returned_rows")

	// DBResponseStatusCodeKey is the attribute Key conforming to the
	// "db.response.status_code" semantic conventions. It represents the database
	// response status code.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples: "102", "ORA-17002", "08P01", "404"
	// Note: The status code returned by the database. Usually it represents an
	// error code, but may also represent partial success, warning, or differentiate
	// between various types of successful outcomes.
	// Semantic conventions for individual database systems SHOULD document what
	// `db.response.status_code` means in the context of that system.
	DBResponseStatusCodeKey = attribute.Key("db.response.status_code")

	// DBSystemNameKey is the attribute Key conforming to the "db.system.name"
	// semantic conventions. It represents the database management system (DBMS)
	// product as identified by the client instrumentation.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Release_Candidate
	//
	// Examples:
	// Note: The actual DBMS may differ from the one identified by the client. For
	// example, when using PostgreSQL client libraries to connect to a CockroachDB,
	// the `db.system.name` is set to `postgresql` based on the instrumentation's
	// best knowledge.
	DBSystemNameKey = attribute.Key("db.system.name")
)

Namespace: db

View Source
const (
	// DeploymentEnvironmentNameKey is the attribute Key conforming to the
	// "deployment.environment.name" semantic conventions. It represents the name of
	// the [deployment environment] (aka deployment tier).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "staging", "production"
	// Note: `deployment.environment.name` does not affect the uniqueness
	// constraints defined through
	// the `service.namespace`, `service.name` and `service.instance.id` resource
	// attributes.
	// This implies that resources carrying the following attribute combinations
	// MUST be
	// considered to be identifying the same service:
	//
	//   - `service.name=frontend`, `deployment.environment.name=production`
	//   - `service.name=frontend`, `deployment.environment.name=staging`.
	//
	//
	// [deployment environment]: https://wikipedia.org/wiki/Deployment_environment
	DeploymentEnvironmentNameKey = attribute.Key("deployment.environment.name")

	// DeploymentIDKey is the attribute Key conforming to the "deployment.id"
	// semantic conventions. It represents the id of the deployment.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1208"
	DeploymentIDKey = attribute.Key("deployment.id")

	// DeploymentNameKey is the attribute Key conforming to the "deployment.name"
	// semantic conventions. It represents the name of the deployment.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "deploy my app", "deploy-frontend"
	DeploymentNameKey = attribute.Key("deployment.name")

	// DeploymentStatusKey is the attribute Key conforming to the
	// "deployment.status" semantic conventions. It represents the status of the
	// deployment.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	DeploymentStatusKey = attribute.Key("deployment.status")
)

Namespace: deployment

View Source
const (
	// DestinationAddressKey is the attribute Key conforming to the
	// "destination.address" semantic conventions. It represents the destination
	// address - domain name if available without reverse DNS lookup; otherwise, IP
	// address or Unix domain socket name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "destination.example.com", "10.1.2.80", "/tmp/my.sock"
	// Note: When observed from the source side, and when communicating through an
	// intermediary, `destination.address` SHOULD represent the destination address
	// behind any intermediaries, for example proxies, if it's available.
	DestinationAddressKey = attribute.Key("destination.address")

	// DestinationPortKey is the attribute Key conforming to the "destination.port"
	// semantic conventions. It represents the destination port number.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 3389, 2888
	DestinationPortKey = attribute.Key("destination.port")
)

Namespace: destination

View Source
const (
	// DeviceIDKey is the attribute Key conforming to the "device.id" semantic
	// conventions. It represents a unique identifier representing the device.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2ab2916d-a51f-4ac8-80ee-45ac31a28092"
	// Note: The device identifier MUST only be defined using the values outlined
	// below. This value is not an advertising identifier and MUST NOT be used as
	// such. On iOS (Swift or Objective-C), this value MUST be equal to the
	// [vendor identifier]. On Android (Java or Kotlin), this value MUST be equal to
	// the Firebase Installation ID or a globally unique UUID which is persisted
	// across sessions in your application. More information can be found [here] on
	// best practices and exact implementation details. Caution should be taken when
	// storing personal data or anything which can identify a user. GDPR and data
	// protection laws may apply, ensure you do your own due diligence.
	//
	// [vendor identifier]: https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor
	// [here]: https://developer.android.com/training/articles/user-data-ids
	DeviceIDKey = attribute.Key("device.id")

	// DeviceManufacturerKey is the attribute Key conforming to the
	// "device.manufacturer" semantic conventions. It represents the name of the
	// device manufacturer.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Apple", "Samsung"
	// Note: The Android OS provides this field via [Build]. iOS apps SHOULD
	// hardcode the value `Apple`.
	//
	// [Build]: https://developer.android.com/reference/android/os/Build#MANUFACTURER
	DeviceManufacturerKey = attribute.Key("device.manufacturer")

	// DeviceModelIdentifierKey is the attribute Key conforming to the
	// "device.model.identifier" semantic conventions. It represents the model
	// identifier for the device.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "iPhone3,4", "SM-G920F"
	// Note: It's recommended this value represents a machine-readable version of
	// the model identifier rather than the market or consumer-friendly name of the
	// device.
	DeviceModelIdentifierKey = attribute.Key("device.model.identifier")

	// DeviceModelNameKey is the attribute Key conforming to the "device.model.name"
	// semantic conventions. It represents the marketing name for the device model.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "iPhone 6s Plus", "Samsung Galaxy S6"
	// Note: It's recommended this value represents a human-readable version of the
	// device model rather than a machine-readable alternative.
	DeviceModelNameKey = attribute.Key("device.model.name")
)

Namespace: device

View Source
const (
	// EnduserIDKey is the attribute Key conforming to the "enduser.id" semantic
	// conventions. It represents the unique identifier of an end user in the
	// system. It maybe a username, email address, or other identifier.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "username"
	// Note: Unique identifier of an end user in the system.
	//
	// > [!Warning]
	// > This field contains sensitive (PII) information.
	EnduserIDKey = attribute.Key("enduser.id")

	// EnduserPseudoIDKey is the attribute Key conforming to the "enduser.pseudo.id"
	// semantic conventions. It represents the pseudonymous identifier of an end
	// user. This identifier should be a random value that is not directly linked or
	// associated with the end user's actual identity.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "QdH5CAWJgqVT4rOr0qtumf"
	// Note: Pseudonymous identifier of an end user.
	//
	// > [!Warning]
	// > This field contains sensitive (linkable PII) information.
	EnduserPseudoIDKey = attribute.Key("enduser.pseudo.id")
)

Namespace: enduser

View Source
const (
	// ExceptionMessageKey is the attribute Key conforming to the
	// "exception.message" semantic conventions. It represents the exception
	// message.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "Division by zero", "Can't convert 'int' object to str implicitly"
	ExceptionMessageKey = attribute.Key("exception.message")

	// ExceptionStacktraceKey is the attribute Key conforming to the
	// "exception.stacktrace" semantic conventions. It represents a stacktrace as a
	// string in the natural representation for the language runtime. The
	// representation is to be determined and documented by each language SIG.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: Exception in thread "main" java.lang.RuntimeException: Test
	// exception\n at com.example.GenerateTrace.methodB(GenerateTrace.java:13)\n at
	// com.example.GenerateTrace.methodA(GenerateTrace.java:9)\n at
	// com.example.GenerateTrace.main(GenerateTrace.java:5)
	ExceptionStacktraceKey = attribute.Key("exception.stacktrace")

	// ExceptionTypeKey is the attribute Key conforming to the "exception.type"
	// semantic conventions. It represents the type of the exception (its
	// fully-qualified class name, if applicable). The dynamic type of the exception
	// should be preferred over the static type in languages that support it.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "java.net.ConnectException", "OSError"
	ExceptionTypeKey = attribute.Key("exception.type")
)

Namespace: exception

View Source
const (
	// FaaSColdstartKey is the attribute Key conforming to the "faas.coldstart"
	// semantic conventions. It represents a boolean that is true if the serverless
	// function is executed for the first time (aka cold-start).
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	FaaSColdstartKey = attribute.Key("faas.coldstart")

	// FaaSCronKey is the attribute Key conforming to the "faas.cron" semantic
	// conventions. It represents a string containing the schedule period as
	// [Cron Expression].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 0/5 * * * ? *
	//
	// [Cron Expression]: https://docs.oracle.com/cd/E12058_01/doc/doc.1014/e12030/cron_expressions.htm
	FaaSCronKey = attribute.Key("faas.cron")

	// FaaSDocumentCollectionKey is the attribute Key conforming to the
	// "faas.document.collection" semantic conventions. It represents the name of
	// the source on which the triggering operation was performed. For example, in
	// Cloud Storage or S3 corresponds to the bucket name, and in Cosmos DB to the
	// database name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "myBucketName", "myDbName"
	FaaSDocumentCollectionKey = attribute.Key("faas.document.collection")

	// FaaSDocumentNameKey is the attribute Key conforming to the
	// "faas.document.name" semantic conventions. It represents the document
	// name/table subjected to the operation. For example, in Cloud Storage or S3 is
	// the name of the file, and in Cosmos DB the table name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "myFile.txt", "myTableName"
	FaaSDocumentNameKey = attribute.Key("faas.document.name")

	// FaaSDocumentOperationKey is the attribute Key conforming to the
	// "faas.document.operation" semantic conventions. It represents the describes
	// the type of the operation that was performed on the data.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	FaaSDocumentOperationKey = attribute.Key("faas.document.operation")

	// FaaSDocumentTimeKey is the attribute Key conforming to the
	// "faas.document.time" semantic conventions. It represents a string containing
	// the time when the data was accessed in the [ISO 8601] format expressed in
	// [UTC].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 2020-01-23T13:47:06Z
	//
	// [ISO 8601]: https://www.iso.org/iso-8601-date-and-time-format.html
	// [UTC]: https://www.w3.org/TR/NOTE-datetime
	FaaSDocumentTimeKey = attribute.Key("faas.document.time")

	// FaaSInstanceKey is the attribute Key conforming to the "faas.instance"
	// semantic conventions. It represents the execution environment ID as a string,
	// that will be potentially reused for other invocations to the same
	// function/function version.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2021/06/28/[$LATEST]2f399eb14537447da05ab2a2e39309de"
	// Note: - **AWS Lambda:** Use the (full) log stream name.
	FaaSInstanceKey = attribute.Key("faas.instance")

	// FaaSInvocationIDKey is the attribute Key conforming to the
	// "faas.invocation_id" semantic conventions. It represents the invocation ID of
	// the current function invocation.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: af9d5aa4-a685-4c5f-a22b-444f80b3cc28
	FaaSInvocationIDKey = attribute.Key("faas.invocation_id")

	// FaaSInvokedNameKey is the attribute Key conforming to the "faas.invoked_name"
	// semantic conventions. It represents the name of the invoked function.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: my-function
	// Note: SHOULD be equal to the `faas.name` resource attribute of the invoked
	// function.
	FaaSInvokedNameKey = attribute.Key("faas.invoked_name")

	// FaaSInvokedProviderKey is the attribute Key conforming to the
	// "faas.invoked_provider" semantic conventions. It represents the cloud
	// provider of the invoked function.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: SHOULD be equal to the `cloud.provider` resource attribute of the
	// invoked function.
	FaaSInvokedProviderKey = attribute.Key("faas.invoked_provider")

	// FaaSInvokedRegionKey is the attribute Key conforming to the
	// "faas.invoked_region" semantic conventions. It represents the cloud region of
	// the invoked function.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: eu-central-1
	// Note: SHOULD be equal to the `cloud.region` resource attribute of the invoked
	// function.
	FaaSInvokedRegionKey = attribute.Key("faas.invoked_region")

	// FaaSMaxMemoryKey is the attribute Key conforming to the "faas.max_memory"
	// semantic conventions. It represents the amount of memory available to the
	// serverless function converted to Bytes.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Note: It's recommended to set this attribute since e.g. too little memory can
	// easily stop a Java AWS Lambda function from working correctly. On AWS Lambda,
	// the environment variable `AWS_LAMBDA_FUNCTION_MEMORY_SIZE` provides this
	// information (which must be multiplied by 1,048,576).
	FaaSMaxMemoryKey = attribute.Key("faas.max_memory")

	// FaaSNameKey is the attribute Key conforming to the "faas.name" semantic
	// conventions. It represents the name of the single function that this runtime
	// instance executes.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-function", "myazurefunctionapp/some-function-name"
	// Note: This is the name of the function as configured/deployed on the FaaS
	// platform and is usually different from the name of the callback
	// function (which may be stored in the
	// [`code.namespace`/`code.function.name`]
	// span attributes).
	//
	// For some cloud providers, the above definition is ambiguous. The following
	// definition of function name MUST be used for this attribute
	// (and consequently the span name) for the listed cloud providers/products:
	//
	//   - **Azure:** The full name `<FUNCAPP>/<FUNC>`, i.e., function app name
	//     followed by a forward slash followed by the function name (this form
	//     can also be seen in the resource JSON for the function).
	//     This means that a span attribute MUST be used, as an Azure function
	//     app can host multiple functions that would usually share
	//     a TracerProvider (see also the `cloud.resource_id` attribute).
	//
	//
	// [`code.namespace`/`code.function.name`]: /docs/general/attributes.md#source-code-attributes
	FaaSNameKey = attribute.Key("faas.name")

	// FaaSTimeKey is the attribute Key conforming to the "faas.time" semantic
	// conventions. It represents a string containing the function invocation time
	// in the [ISO 8601] format expressed in [UTC].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 2020-01-23T13:47:06Z
	//
	// [ISO 8601]: https://www.iso.org/iso-8601-date-and-time-format.html
	// [UTC]: https://www.w3.org/TR/NOTE-datetime
	FaaSTimeKey = attribute.Key("faas.time")

	// FaaSTriggerKey is the attribute Key conforming to the "faas.trigger" semantic
	// conventions. It represents the type of the trigger which caused this function
	// invocation.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	FaaSTriggerKey = attribute.Key("faas.trigger")

	// FaaSVersionKey is the attribute Key conforming to the "faas.version" semantic
	// conventions. It represents the immutable version of the function being
	// executed.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "26", "pinkfroid-00002"
	// Note: Depending on the cloud provider and platform, use:
	//
	//   - **AWS Lambda:** The [function version]
	//     (an integer represented as a decimal string).
	//   - **Google Cloud Run (Services):** The [revision]
	//     (i.e., the function name plus the revision suffix).
	//   - **Google Cloud Functions:** The value of the
	//     [`K_REVISION` environment variable].
	//   - **Azure Functions:** Not applicable. Do not set this attribute.
	//
	//
	// [function version]: https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html
	// [revision]: https://cloud.google.com/run/docs/managing/revisions
	// [`K_REVISION` environment variable]: https://cloud.google.com/functions/docs/env-var#runtime_environment_variables_set_automatically
	FaaSVersionKey = attribute.Key("faas.version")
)

Namespace: faas

View Source
const (
	// FeatureFlagContextIDKey is the attribute Key conforming to the
	// "feature_flag.context.id" semantic conventions. It represents the unique
	// identifier for the flag evaluation context. For example, the targeting key.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "5157782b-2203-4c80-a857-dbbd5e7761db"
	FeatureFlagContextIDKey = attribute.Key("feature_flag.context.id")

	// FeatureFlagEvaluationErrorMessageKey is the attribute Key conforming to the
	// "feature_flag.evaluation.error.message" semantic conventions. It represents a
	// message explaining the nature of an error occurring during flag evaluation.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Flag `header-color` expected type `string` but found type `number`
	// "
	FeatureFlagEvaluationErrorMessageKey = attribute.Key("feature_flag.evaluation.error.message")

	// FeatureFlagEvaluationReasonKey is the attribute Key conforming to the
	// "feature_flag.evaluation.reason" semantic conventions. It represents the
	// reason code which shows how a feature flag value was determined.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "static", "targeting_match", "error", "default"
	FeatureFlagEvaluationReasonKey = attribute.Key("feature_flag.evaluation.reason")

	// FeatureFlagKeyKey is the attribute Key conforming to the "feature_flag.key"
	// semantic conventions. It represents the lookup key of the feature flag.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "logo-color"
	FeatureFlagKeyKey = attribute.Key("feature_flag.key")

	// FeatureFlagProviderNameKey is the attribute Key conforming to the
	// "feature_flag.provider_name" semantic conventions. It represents the
	// identifies the feature flag provider.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Flag Manager"
	FeatureFlagProviderNameKey = attribute.Key("feature_flag.provider_name")

	// FeatureFlagSetIDKey is the attribute Key conforming to the
	// "feature_flag.set.id" semantic conventions. It represents the identifier of
	// the [flag set] to which the feature flag belongs.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "proj-1", "ab98sgs", "service1/dev"
	//
	// [flag set]: https://openfeature.dev/specification/glossary/#flag-set
	FeatureFlagSetIDKey = attribute.Key("feature_flag.set.id")

	// FeatureFlagVariantKey is the attribute Key conforming to the
	// "feature_flag.variant" semantic conventions. It represents a semantic
	// identifier for an evaluated flag value.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "red", "true", "on"
	// Note: A semantic identifier, commonly referred to as a variant, provides a
	// means
	// for referring to a value without including the value itself. This can
	// provide additional context for understanding the meaning behind a value.
	// For example, the variant `red` maybe be used for the value `#c05543`.
	FeatureFlagVariantKey = attribute.Key("feature_flag.variant")

	// FeatureFlagVersionKey is the attribute Key conforming to the
	// "feature_flag.version" semantic conventions. It represents the version of the
	// ruleset used during the evaluation. This may be any stable value which
	// uniquely identifies the ruleset.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1", "01ABCDEF"
	FeatureFlagVersionKey = attribute.Key("feature_flag.version")
)

Namespace: feature_flag

View Source
const (
	// FileAccessedKey is the attribute Key conforming to the "file.accessed"
	// semantic conventions. It represents the time when the file was last accessed,
	// in ISO 8601 format.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2021-01-01T12:00:00Z"
	// Note: This attribute might not be supported by some file systems — NFS,
	// FAT32, in embedded OS, etc.
	FileAccessedKey = attribute.Key("file.accessed")

	// FileAttributesKey is the attribute Key conforming to the "file.attributes"
	// semantic conventions. It represents the array of file attributes.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "readonly", "hidden"
	// Note: Attributes names depend on the OS or file system. Here’s a
	// non-exhaustive list of values expected for this attribute: `archive`,
	// `compressed`, `directory`, `encrypted`, `execute`, `hidden`, `immutable`,
	// `journaled`, `read`, `readonly`, `symbolic link`, `system`, `temporary`,
	// `write`.
	FileAttributesKey = attribute.Key("file.attributes")

	// FileChangedKey is the attribute Key conforming to the "file.changed" semantic
	// conventions. It represents the time when the file attributes or metadata was
	// last changed, in ISO 8601 format.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2021-01-01T12:00:00Z"
	// Note: `file.changed` captures the time when any of the file's properties or
	// attributes (including the content) are changed, while `file.modified`
	// captures the timestamp when the file content is modified.
	FileChangedKey = attribute.Key("file.changed")

	// FileCreatedKey is the attribute Key conforming to the "file.created" semantic
	// conventions. It represents the time when the file was created, in ISO 8601
	// format.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2021-01-01T12:00:00Z"
	// Note: This attribute might not be supported by some file systems — NFS,
	// FAT32, in embedded OS, etc.
	FileCreatedKey = attribute.Key("file.created")

	// FileDirectoryKey is the attribute Key conforming to the "file.directory"
	// semantic conventions. It represents the directory where the file is located.
	// It should include the drive letter, when appropriate.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/home/user", "C:\Program Files\MyApp"
	FileDirectoryKey = attribute.Key("file.directory")

	// FileExtensionKey is the attribute Key conforming to the "file.extension"
	// semantic conventions. It represents the file extension, excluding the leading
	// dot.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "png", "gz"
	// Note: When the file name has multiple extensions (example.tar.gz), only the
	// last one should be captured ("gz", not "tar.gz").
	FileExtensionKey = attribute.Key("file.extension")

	// FileForkNameKey is the attribute Key conforming to the "file.fork_name"
	// semantic conventions. It represents the name of the fork. A fork is
	// additional data associated with a filesystem object.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Zone.Identifer"
	// Note: On Linux, a resource fork is used to store additional data with a
	// filesystem object. A file always has at least one fork for the data portion,
	// and additional forks may exist.
	// On NTFS, this is analogous to an Alternate Data Stream (ADS), and the default
	// data stream for a file is just called $DATA. Zone.Identifier is commonly used
	// by Windows to track contents downloaded from the Internet. An ADS is
	// typically of the form: C:\path\to\filename.extension:some_fork_name, and
	// some_fork_name is the value that should populate `fork_name`.
	// `filename.extension` should populate `file.name`, and `extension` should
	// populate `file.extension`. The full path, `file.path`, will include the fork
	// name.
	FileForkNameKey = attribute.Key("file.fork_name")

	// FileGroupIDKey is the attribute Key conforming to the "file.group.id"
	// semantic conventions. It represents the primary Group ID (GID) of the file.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1000"
	FileGroupIDKey = attribute.Key("file.group.id")

	// FileGroupNameKey is the attribute Key conforming to the "file.group.name"
	// semantic conventions. It represents the primary group name of the file.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "users"
	FileGroupNameKey = attribute.Key("file.group.name")

	// FileInodeKey is the attribute Key conforming to the "file.inode" semantic
	// conventions. It represents the inode representing the file in the filesystem.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "256383"
	FileInodeKey = attribute.Key("file.inode")

	// FileModeKey is the attribute Key conforming to the "file.mode" semantic
	// conventions. It represents the mode of the file in octal representation.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "0640"
	FileModeKey = attribute.Key("file.mode")

	// FileModifiedKey is the attribute Key conforming to the "file.modified"
	// semantic conventions. It represents the time when the file content was last
	// modified, in ISO 8601 format.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2021-01-01T12:00:00Z"
	FileModifiedKey = attribute.Key("file.modified")

	// FileNameKey is the attribute Key conforming to the "file.name" semantic
	// conventions. It represents the name of the file including the extension,
	// without the directory.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "example.png"
	FileNameKey = attribute.Key("file.name")

	// FileOwnerIDKey is the attribute Key conforming to the "file.owner.id"
	// semantic conventions. It represents the user ID (UID) or security identifier
	// (SID) of the file owner.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1000"
	FileOwnerIDKey = attribute.Key("file.owner.id")

	// FileOwnerNameKey is the attribute Key conforming to the "file.owner.name"
	// semantic conventions. It represents the username of the file owner.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "root"
	FileOwnerNameKey = attribute.Key("file.owner.name")

	// FilePathKey is the attribute Key conforming to the "file.path" semantic
	// conventions. It represents the full path to the file, including the file
	// name. It should include the drive letter, when appropriate.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/home/alice/example.png", "C:\Program Files\MyApp\myapp.exe"
	FilePathKey = attribute.Key("file.path")

	// FileSizeKey is the attribute Key conforming to the "file.size" semantic
	// conventions. It represents the file size in bytes.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	FileSizeKey = attribute.Key("file.size")

	// FileSymbolicLinkTargetPathKey is the attribute Key conforming to the
	// "file.symbolic_link.target_path" semantic conventions. It represents the path
	// to the target of a symbolic link.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/usr/bin/python3"
	// Note: This attribute is only applicable to symbolic links.
	FileSymbolicLinkTargetPathKey = attribute.Key("file.symbolic_link.target_path")
)

Namespace: file

View Source
const (
	// GCPClientServiceKey is the attribute Key conforming to the
	// "gcp.client.service" semantic conventions. It represents the identifies the
	// Google Cloud service for which the official client library is intended.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "appengine", "run", "firestore", "alloydb", "spanner"
	// Note: Intended to be a stable identifier for Google Cloud client libraries
	// that is uniform across implementation languages. The value should be derived
	// from the canonical service domain for the service; for example,
	// 'foo.googleapis.com' should result in a value of 'foo'.
	GCPClientServiceKey = attribute.Key("gcp.client.service")

	// GCPCloudRunJobExecutionKey is the attribute Key conforming to the
	// "gcp.cloud_run.job.execution" semantic conventions. It represents the name of
	// the Cloud Run [execution] being run for the Job, as set by the
	// [`CLOUD_RUN_EXECUTION`] environment variable.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "job-name-xxxx", "sample-job-mdw84"
	//
	// [execution]: https://cloud.google.com/run/docs/managing/job-executions
	// [`CLOUD_RUN_EXECUTION`]: https://cloud.google.com/run/docs/container-contract#jobs-env-vars
	GCPCloudRunJobExecutionKey = attribute.Key("gcp.cloud_run.job.execution")

	// GCPCloudRunJobTaskIndexKey is the attribute Key conforming to the
	// "gcp.cloud_run.job.task_index" semantic conventions. It represents the index
	// for a task within an execution as provided by the [`CLOUD_RUN_TASK_INDEX`]
	// environment variable.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 0, 1
	//
	// [`CLOUD_RUN_TASK_INDEX`]: https://cloud.google.com/run/docs/container-contract#jobs-env-vars
	GCPCloudRunJobTaskIndexKey = attribute.Key("gcp.cloud_run.job.task_index")

	// GCPGceInstanceHostnameKey is the attribute Key conforming to the
	// "gcp.gce.instance.hostname" semantic conventions. It represents the hostname
	// of a GCE instance. This is the full value of the default or [custom hostname]
	// .
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-host1234.example.com",
	// "sample-vm.us-west1-b.c.my-project.internal"
	//
	// [custom hostname]: https://cloud.google.com/compute/docs/instances/custom-hostname-vm
	GCPGceInstanceHostnameKey = attribute.Key("gcp.gce.instance.hostname")

	// GCPGceInstanceNameKey is the attribute Key conforming to the
	// "gcp.gce.instance.name" semantic conventions. It represents the instance name
	// of a GCE instance. This is the value provided by `host.name`, the visible
	// name of the instance in the Cloud Console UI, and the prefix for the default
	// hostname of the instance as defined by the [default internal DNS name].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "instance-1", "my-vm-name"
	//
	// [default internal DNS name]: https://cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names
	GCPGceInstanceNameKey = attribute.Key("gcp.gce.instance.name")
)

Namespace: gcp

View Source
const (
	// GenAIAgentDescriptionKey is the attribute Key conforming to the
	// "gen_ai.agent.description" semantic conventions. It represents the free-form
	// description of the GenAI agent provided by the application.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Helps with math problems", "Generates fiction stories"
	GenAIAgentDescriptionKey = attribute.Key("gen_ai.agent.description")

	// GenAIAgentIDKey is the attribute Key conforming to the "gen_ai.agent.id"
	// semantic conventions. It represents the unique identifier of the GenAI agent.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "asst_5j66UpCpwteGg4YSxUnt7lPY"
	GenAIAgentIDKey = attribute.Key("gen_ai.agent.id")

	// GenAIAgentNameKey is the attribute Key conforming to the "gen_ai.agent.name"
	// semantic conventions. It represents the human-readable name of the GenAI
	// agent provided by the application.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Math Tutor", "Fiction Writer"
	GenAIAgentNameKey = attribute.Key("gen_ai.agent.name")

	// GenAIOpenaiRequestServiceTierKey is the attribute Key conforming to the
	// "gen_ai.openai.request.service_tier" semantic conventions. It represents the
	// service tier requested. May be a specific tier, default, or auto.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "auto", "default"
	GenAIOpenaiRequestServiceTierKey = attribute.Key("gen_ai.openai.request.service_tier")

	// GenAIOpenaiResponseServiceTierKey is the attribute Key conforming to the
	// "gen_ai.openai.response.service_tier" semantic conventions. It represents the
	// service tier used for the response.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "scale", "default"
	GenAIOpenaiResponseServiceTierKey = attribute.Key("gen_ai.openai.response.service_tier")

	// GenAIOpenaiResponseSystemFingerprintKey is the attribute Key conforming to
	// the "gen_ai.openai.response.system_fingerprint" semantic conventions. It
	// represents a fingerprint to track any eventual change in the Generative AI
	// environment.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "fp_44709d6fcb"
	GenAIOpenaiResponseSystemFingerprintKey = attribute.Key("gen_ai.openai.response.system_fingerprint")

	// GenAIOperationNameKey is the attribute Key conforming to the
	// "gen_ai.operation.name" semantic conventions. It represents the name of the
	// operation being performed.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: If one of the predefined values applies, but specific system uses a
	// different name it's RECOMMENDED to document it in the semantic conventions
	// for specific GenAI system and use system-specific name in the
	// instrumentation. If a different name is not documented, instrumentation
	// libraries SHOULD use applicable predefined value.
	GenAIOperationNameKey = attribute.Key("gen_ai.operation.name")

	// GenAIOutputTypeKey is the attribute Key conforming to the
	// "gen_ai.output.type" semantic conventions. It represents the represents the
	// content type requested by the client.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: This attribute SHOULD be used when the client requests output of a
	// specific type. The model may return zero or more outputs of this type.
	// This attribute specifies the output modality and not the actual output
	// format. For example, if an image is requested, the actual output could be a
	// URL pointing to an image file.
	// Additional output format details may be recorded in the future in the
	// `gen_ai.output.{type}.*` attributes.
	GenAIOutputTypeKey = attribute.Key("gen_ai.output.type")

	// GenAIRequestChoiceCountKey is the attribute Key conforming to the
	// "gen_ai.request.choice.count" semantic conventions. It represents the target
	// number of candidate completions to return.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 3
	GenAIRequestChoiceCountKey = attribute.Key("gen_ai.request.choice.count")

	// GenAIRequestEncodingFormatsKey is the attribute Key conforming to the
	// "gen_ai.request.encoding_formats" semantic conventions. It represents the
	// encoding formats requested in an embeddings operation, if specified.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "base64"], ["float", "binary"
	// Note: In some GenAI systems the encoding formats are called embedding types.
	// Also, some GenAI systems only accept a single format per request.
	GenAIRequestEncodingFormatsKey = attribute.Key("gen_ai.request.encoding_formats")

	// GenAIRequestFrequencyPenaltyKey is the attribute Key conforming to the
	// "gen_ai.request.frequency_penalty" semantic conventions. It represents the
	// frequency penalty setting for the GenAI request.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 0.1
	GenAIRequestFrequencyPenaltyKey = attribute.Key("gen_ai.request.frequency_penalty")

	// GenAIRequestMaxTokensKey is the attribute Key conforming to the
	// "gen_ai.request.max_tokens" semantic conventions. It represents the maximum
	// number of tokens the model generates for a request.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 100
	GenAIRequestMaxTokensKey = attribute.Key("gen_ai.request.max_tokens")

	// GenAIRequestModelKey is the attribute Key conforming to the
	// "gen_ai.request.model" semantic conventions. It represents the name of the
	// GenAI model a request is being made to.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: gpt-4
	GenAIRequestModelKey = attribute.Key("gen_ai.request.model")

	// GenAIRequestPresencePenaltyKey is the attribute Key conforming to the
	// "gen_ai.request.presence_penalty" semantic conventions. It represents the
	// presence penalty setting for the GenAI request.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 0.1
	GenAIRequestPresencePenaltyKey = attribute.Key("gen_ai.request.presence_penalty")

	// GenAIRequestSeedKey is the attribute Key conforming to the
	// "gen_ai.request.seed" semantic conventions. It represents the requests with
	// same seed value more likely to return same result.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 100
	GenAIRequestSeedKey = attribute.Key("gen_ai.request.seed")

	// GenAIRequestStopSequencesKey is the attribute Key conforming to the
	// "gen_ai.request.stop_sequences" semantic conventions. It represents the list
	// of sequences that the model will use to stop generating further tokens.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "forest", "lived"
	GenAIRequestStopSequencesKey = attribute.Key("gen_ai.request.stop_sequences")

	// GenAIRequestTemperatureKey is the attribute Key conforming to the
	// "gen_ai.request.temperature" semantic conventions. It represents the
	// temperature setting for the GenAI request.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 0.0
	GenAIRequestTemperatureKey = attribute.Key("gen_ai.request.temperature")

	// GenAIRequestTopKKey is the attribute Key conforming to the
	// "gen_ai.request.top_k" semantic conventions. It represents the top_k sampling
	// setting for the GenAI request.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1.0
	GenAIRequestTopKKey = attribute.Key("gen_ai.request.top_k")

	// GenAIRequestTopPKey is the attribute Key conforming to the
	// "gen_ai.request.top_p" semantic conventions. It represents the top_p sampling
	// setting for the GenAI request.
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1.0
	GenAIRequestTopPKey = attribute.Key("gen_ai.request.top_p")

	// GenAIResponseFinishReasonsKey is the attribute Key conforming to the
	// "gen_ai.response.finish_reasons" semantic conventions. It represents the
	// array of reasons the model stopped generating tokens, corresponding to each
	// generation received.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "stop"], ["stop", "length"
	GenAIResponseFinishReasonsKey = attribute.Key("gen_ai.response.finish_reasons")

	// GenAIResponseIDKey is the attribute Key conforming to the
	// "gen_ai.response.id" semantic conventions. It represents the unique
	// identifier for the completion.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "chatcmpl-123"
	GenAIResponseIDKey = attribute.Key("gen_ai.response.id")

	// GenAIResponseModelKey is the attribute Key conforming to the
	// "gen_ai.response.model" semantic conventions. It represents the name of the
	// model that generated the response.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "gpt-4-0613"
	GenAIResponseModelKey = attribute.Key("gen_ai.response.model")

	// GenAISystemKey is the attribute Key conforming to the "gen_ai.system"
	// semantic conventions. It represents the Generative AI product as identified
	// by the client or server instrumentation.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: openai
	// Note: The `gen_ai.system` describes a family of GenAI models with specific
	// model identified
	// by `gen_ai.request.model` and `gen_ai.response.model` attributes.
	//
	// The actual GenAI product may differ from the one identified by the client.
	// Multiple systems, including Azure OpenAI and Gemini, are accessible by OpenAI
	// client
	// libraries. In such cases, the `gen_ai.system` is set to `openai` based on the
	// instrumentation's best knowledge, instead of the actual system. The
	// `server.address`
	// attribute may help identify the actual system in use for `openai`.
	//
	// For custom model, a custom friendly name SHOULD be used.
	// If none of these options apply, the `gen_ai.system` SHOULD be set to `_OTHER`
	// .
	GenAISystemKey = attribute.Key("gen_ai.system")

	// GenAITokenTypeKey is the attribute Key conforming to the "gen_ai.token.type"
	// semantic conventions. It represents the type of token being counted.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "input", "output"
	GenAITokenTypeKey = attribute.Key("gen_ai.token.type")

	// GenAIToolCallIDKey is the attribute Key conforming to the
	// "gen_ai.tool.call.id" semantic conventions. It represents the tool call
	// identifier.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "call_mszuSIzqtI65i1wAUOE8w5H4"
	GenAIToolCallIDKey = attribute.Key("gen_ai.tool.call.id")

	// GenAIToolNameKey is the attribute Key conforming to the "gen_ai.tool.name"
	// semantic conventions. It represents the name of the tool utilized by the
	// agent.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Flights"
	GenAIToolNameKey = attribute.Key("gen_ai.tool.name")

	// GenAIToolTypeKey is the attribute Key conforming to the "gen_ai.tool.type"
	// semantic conventions. It represents the type of the tool utilized by the
	// agent.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "function", "extension", "datastore"
	// Note: Extension: A tool executed on the agent-side to directly call external
	// APIs, bridging the gap between the agent and real-world systems.
	// Agent-side operations involve actions that are performed by the agent on the
	// server or within the agent's controlled environment.
	// Function: A tool executed on the client-side, where the agent generates
	// parameters for a predefined function, and the client executes the logic.
	// Client-side operations are actions taken on the user's end or within the
	// client application.
	// Datastore: A tool used by the agent to access and query structured or
	// unstructured external data for retrieval-augmented tasks or knowledge
	// updates.
	GenAIToolTypeKey = attribute.Key("gen_ai.tool.type")

	// GenAIUsageInputTokensKey is the attribute Key conforming to the
	// "gen_ai.usage.input_tokens" semantic conventions. It represents the number of
	// tokens used in the GenAI input (prompt).
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 100
	GenAIUsageInputTokensKey = attribute.Key("gen_ai.usage.input_tokens")

	// GenAIUsageOutputTokensKey is the attribute Key conforming to the
	// "gen_ai.usage.output_tokens" semantic conventions. It represents the number
	// of tokens used in the GenAI response (completion).
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 180
	GenAIUsageOutputTokensKey = attribute.Key("gen_ai.usage.output_tokens")
)

Namespace: gen_ai

View Source
const (
	// GeoContinentCodeKey is the attribute Key conforming to the
	// "geo.continent.code" semantic conventions. It represents the two-letter code
	// representing continent’s name.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	GeoContinentCodeKey = attribute.Key("geo.continent.code")

	// GeoCountryIsoCodeKey is the attribute Key conforming to the
	// "geo.country.iso_code" semantic conventions. It represents the two-letter ISO
	// Country Code ([ISO 3166-1 alpha2]).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "CA"
	//
	// [ISO 3166-1 alpha2]: https://wikipedia.org/wiki/ISO_3166-1#Codes
	GeoCountryIsoCodeKey = attribute.Key("geo.country.iso_code")

	// GeoLocalityNameKey is the attribute Key conforming to the "geo.locality.name"
	// semantic conventions. It represents the locality name. Represents the name of
	// a city, town, village, or similar populated place.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Montreal", "Berlin"
	GeoLocalityNameKey = attribute.Key("geo.locality.name")

	// GeoLocationLatKey is the attribute Key conforming to the "geo.location.lat"
	// semantic conventions. It represents the latitude of the geo location in
	// [WGS84].
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 45.505918
	//
	// [WGS84]: https://wikipedia.org/wiki/World_Geodetic_System#WGS84
	GeoLocationLatKey = attribute.Key("geo.location.lat")

	// GeoLocationLonKey is the attribute Key conforming to the "geo.location.lon"
	// semantic conventions. It represents the longitude of the geo location in
	// [WGS84].
	//
	// Type: double
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: -73.61483
	//
	// [WGS84]: https://wikipedia.org/wiki/World_Geodetic_System#WGS84
	GeoLocationLonKey = attribute.Key("geo.location.lon")

	// GeoPostalCodeKey is the attribute Key conforming to the "geo.postal_code"
	// semantic conventions. It represents the postal code associated with the
	// location. Values appropriate for this field may also be known as a postcode
	// or ZIP code and will vary widely from country to country.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "94040"
	GeoPostalCodeKey = attribute.Key("geo.postal_code")

	// GeoRegionIsoCodeKey is the attribute Key conforming to the
	// "geo.region.iso_code" semantic conventions. It represents the region ISO code
	// ([ISO 3166-2]).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "CA-QC"
	//
	// [ISO 3166-2]: https://wikipedia.org/wiki/ISO_3166-2
	GeoRegionIsoCodeKey = attribute.Key("geo.region.iso_code")
)

Namespace: geo

View Source
const (
	// GraphqlDocumentKey is the attribute Key conforming to the "graphql.document"
	// semantic conventions. It represents the GraphQL document being executed.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: query findBookById { bookById(id: ?) { name } }
	// Note: The value may be sanitized to exclude sensitive information.
	GraphqlDocumentKey = attribute.Key("graphql.document")

	// GraphqlOperationNameKey is the attribute Key conforming to the
	// "graphql.operation.name" semantic conventions. It represents the name of the
	// operation being executed.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: findBookById
	GraphqlOperationNameKey = attribute.Key("graphql.operation.name")

	// GraphqlOperationTypeKey is the attribute Key conforming to the
	// "graphql.operation.type" semantic conventions. It represents the type of the
	// operation being executed.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "query", "mutation", "subscription"
	GraphqlOperationTypeKey = attribute.Key("graphql.operation.type")
)

Namespace: graphql

View Source
const (
	// HerokuAppIDKey is the attribute Key conforming to the "heroku.app.id"
	// semantic conventions. It represents the unique identifier for the
	// application.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2daa2797-e42b-4624-9322-ec3f968df4da"
	HerokuAppIDKey = attribute.Key("heroku.app.id")

	// HerokuReleaseCommitKey is the attribute Key conforming to the
	// "heroku.release.commit" semantic conventions. It represents the commit hash
	// for the current release.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "e6134959463efd8966b20e75b913cafe3f5ec"
	HerokuReleaseCommitKey = attribute.Key("heroku.release.commit")

	// HerokuReleaseCreationTimestampKey is the attribute Key conforming to the
	// "heroku.release.creation_timestamp" semantic conventions. It represents the
	// time and date the release was created.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2022-10-23T18:00:42Z"
	HerokuReleaseCreationTimestampKey = attribute.Key("heroku.release.creation_timestamp")
)

Namespace: heroku

View Source
const (
	// HostArchKey is the attribute Key conforming to the "host.arch" semantic
	// conventions. It represents the CPU architecture the host system is running
	// on.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	HostArchKey = attribute.Key("host.arch")

	// HostCPUCacheL2SizeKey is the attribute Key conforming to the
	// "host.cpu.cache.l2.size" semantic conventions. It represents the amount of
	// level 2 memory cache available to the processor (in Bytes).
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 12288000
	HostCPUCacheL2SizeKey = attribute.Key("host.cpu.cache.l2.size")

	// HostCPUFamilyKey is the attribute Key conforming to the "host.cpu.family"
	// semantic conventions. It represents the family or generation of the CPU.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "6", "PA-RISC 1.1e"
	HostCPUFamilyKey = attribute.Key("host.cpu.family")

	// HostCPUModelIDKey is the attribute Key conforming to the "host.cpu.model.id"
	// semantic conventions. It represents the model identifier. It provides more
	// granular information about the CPU, distinguishing it from other CPUs within
	// the same family.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "6", "9000/778/B180L"
	HostCPUModelIDKey = attribute.Key("host.cpu.model.id")

	// HostCPUModelNameKey is the attribute Key conforming to the
	// "host.cpu.model.name" semantic conventions. It represents the model
	// designation of the processor.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz"
	HostCPUModelNameKey = attribute.Key("host.cpu.model.name")

	// HostCPUSteppingKey is the attribute Key conforming to the "host.cpu.stepping"
	// semantic conventions. It represents the stepping or core revisions.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1", "r1p1"
	HostCPUSteppingKey = attribute.Key("host.cpu.stepping")

	// HostCPUVendorIDKey is the attribute Key conforming to the
	// "host.cpu.vendor.id" semantic conventions. It represents the processor
	// manufacturer identifier. A maximum 12-character string.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "GenuineIntel"
	// Note: [CPUID] command returns the vendor ID string in EBX, EDX and ECX
	// registers. Writing these to memory in this order results in a 12-character
	// string.
	//
	// [CPUID]: https://wiki.osdev.org/CPUID
	HostCPUVendorIDKey = attribute.Key("host.cpu.vendor.id")

	// HostIDKey is the attribute Key conforming to the "host.id" semantic
	// conventions. It represents the unique host ID. For Cloud, this must be the
	// instance_id assigned by the cloud provider. For non-containerized systems,
	// this should be the `machine-id`. See the table below for the sources to use
	// to determine the `machine-id` based on operating system.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "fdbf79e8af94cb7f9e8df36789187052"
	HostIDKey = attribute.Key("host.id")

	// HostImageIDKey is the attribute Key conforming to the "host.image.id"
	// semantic conventions. It represents the VM image ID or host OS image ID. For
	// Cloud, this value is from the provider.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "ami-07b06b442921831e5"
	HostImageIDKey = attribute.Key("host.image.id")

	// HostImageNameKey is the attribute Key conforming to the "host.image.name"
	// semantic conventions. It represents the name of the VM image or OS install
	// the host was instantiated from.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "infra-ami-eks-worker-node-7d4ec78312", "CentOS-8-x86_64-1905"
	HostImageNameKey = attribute.Key("host.image.name")

	// HostImageVersionKey is the attribute Key conforming to the
	// "host.image.version" semantic conventions. It represents the version string
	// of the VM image or host OS as defined in [Version Attributes].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "0.1"
	//
	// [Version Attributes]: /docs/resource/README.md#version-attributes
	HostImageVersionKey = attribute.Key("host.image.version")

	// HostIPKey is the attribute Key conforming to the "host.ip" semantic
	// conventions. It represents the available IP addresses of the host, excluding
	// loopback interfaces.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "192.168.1.140", "fe80::abc2:4a28:737a:609e"
	// Note: IPv4 Addresses MUST be specified in dotted-quad notation. IPv6
	// addresses MUST be specified in the [RFC 5952] format.
	//
	// [RFC 5952]: https://www.rfc-editor.org/rfc/rfc5952.html
	HostIPKey = attribute.Key("host.ip")

	// HostMacKey is the attribute Key conforming to the "host.mac" semantic
	// conventions. It represents the available MAC addresses of the host, excluding
	// loopback interfaces.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "AC-DE-48-23-45-67", "AC-DE-48-23-45-67-01-9F"
	// Note: MAC Addresses MUST be represented in [IEEE RA hexadecimal form]: as
	// hyphen-separated octets in uppercase hexadecimal form from most to least
	// significant.
	//
	// [IEEE RA hexadecimal form]: https://standards.ieee.org/wp-content/uploads/import/documents/tutorials/eui.pdf
	HostMacKey = attribute.Key("host.mac")

	// HostNameKey is the attribute Key conforming to the "host.name" semantic
	// conventions. It represents the name of the host. On Unix systems, it may
	// contain what the hostname command returns, or the fully qualified hostname,
	// or another name specified by the user.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry-test"
	HostNameKey = attribute.Key("host.name")

	// HostTypeKey is the attribute Key conforming to the "host.type" semantic
	// conventions. It represents the type of host. For Cloud, this must be the
	// machine type.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "n1-standard-1"
	HostTypeKey = attribute.Key("host.type")
)

Namespace: host

View Source
const (
	// HTTPConnectionStateKey is the attribute Key conforming to the
	// "http.connection.state" semantic conventions. It represents the state of the
	// HTTP connection in the HTTP connection pool.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "active", "idle"
	HTTPConnectionStateKey = attribute.Key("http.connection.state")

	// HTTPRequestBodySizeKey is the attribute Key conforming to the
	// "http.request.body.size" semantic conventions. It represents the size of the
	// request payload body in bytes. This is the number of bytes transferred
	// excluding headers and is often, but not always, present as the
	// [Content-Length] header. For requests using transport encoding, this should
	// be the compressed size.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// [Content-Length]: https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length
	HTTPRequestBodySizeKey = attribute.Key("http.request.body.size")

	// HTTPRequestMethodKey is the attribute Key conforming to the
	// "http.request.method" semantic conventions. It represents the HTTP request
	// method.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "GET", "POST", "HEAD"
	// Note: HTTP request method value SHOULD be "known" to the instrumentation.
	// By default, this convention defines "known" methods as the ones listed in
	// [RFC9110]
	// and the PATCH method defined in [RFC5789].
	//
	// If the HTTP request method is not known to instrumentation, it MUST set the
	// `http.request.method` attribute to `_OTHER`.
	//
	// If the HTTP instrumentation could end up converting valid HTTP request
	// methods to `_OTHER`, then it MUST provide a way to override
	// the list of known HTTP methods. If this override is done via environment
	// variable, then the environment variable MUST be named
	// OTEL_INSTRUMENTATION_HTTP_KNOWN_METHODS and support a comma-separated list of
	// case-sensitive known HTTP methods
	// (this list MUST be a full override of the default known method, it is not a
	// list of known methods in addition to the defaults).
	//
	// HTTP method names are case-sensitive and `http.request.method` attribute
	// value MUST match a known HTTP method name exactly.
	// Instrumentations for specific web frameworks that consider HTTP methods to be
	// case insensitive, SHOULD populate a canonical equivalent.
	// Tracing instrumentations that do so, MUST also set
	// `http.request.method_original` to the original value.
	//
	// [RFC9110]: https://www.rfc-editor.org/rfc/rfc9110.html#name-methods
	// [RFC5789]: https://www.rfc-editor.org/rfc/rfc5789.html
	HTTPRequestMethodKey = attribute.Key("http.request.method")

	// HTTPRequestMethodOriginalKey is the attribute Key conforming to the
	// "http.request.method_original" semantic conventions. It represents the
	// original HTTP method sent by the client in the request line.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "GeT", "ACL", "foo"
	HTTPRequestMethodOriginalKey = attribute.Key("http.request.method_original")

	// HTTPRequestResendCountKey is the attribute Key conforming to the
	// "http.request.resend_count" semantic conventions. It represents the ordinal
	// number of request resending attempt (for any reason, including redirects).
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Note: The resend count SHOULD be updated each time an HTTP request gets
	// resent by the client, regardless of what was the cause of the resending (e.g.
	// redirection, authorization failure, 503 Server Unavailable, network issues,
	// or any other).
	HTTPRequestResendCountKey = attribute.Key("http.request.resend_count")

	// HTTPRequestSizeKey is the attribute Key conforming to the "http.request.size"
	// semantic conventions. It represents the total size of the request in bytes.
	// This should be the total number of bytes sent over the wire, including the
	// request line (HTTP/1.1), framing (HTTP/2 and HTTP/3), headers, and request
	// body if any.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	HTTPRequestSizeKey = attribute.Key("http.request.size")

	// HTTPResponseBodySizeKey is the attribute Key conforming to the
	// "http.response.body.size" semantic conventions. It represents the size of the
	// response payload body in bytes. This is the number of bytes transferred
	// excluding headers and is often, but not always, present as the
	// [Content-Length] header. For requests using transport encoding, this should
	// be the compressed size.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// [Content-Length]: https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length
	HTTPResponseBodySizeKey = attribute.Key("http.response.body.size")

	// HTTPResponseSizeKey is the attribute Key conforming to the
	// "http.response.size" semantic conventions. It represents the total size of
	// the response in bytes. This should be the total number of bytes sent over the
	// wire, including the status line (HTTP/1.1), framing (HTTP/2 and HTTP/3),
	// headers, and response body and trailers if any.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	HTTPResponseSizeKey = attribute.Key("http.response.size")

	// HTTPResponseStatusCodeKey is the attribute Key conforming to the
	// "http.response.status_code" semantic conventions. It represents the
	// [HTTP response status code].
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: 200
	//
	// [HTTP response status code]: https://tools.ietf.org/html/rfc7231#section-6
	HTTPResponseStatusCodeKey = attribute.Key("http.response.status_code")

	// HTTPRouteKey is the attribute Key conforming to the "http.route" semantic
	// conventions. It represents the matched route, that is, the path template in
	// the format used by the respective server framework.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "/users/:userID?", "{controller}/{action}/{id?}"
	// Note: MUST NOT be populated when this is not supported by the HTTP server
	// framework as the route attribute should have low-cardinality and the URI path
	// can NOT substitute it.
	// SHOULD include the [application root] if there is one.
	//
	// [application root]: /docs/http/http-spans.md#http-server-definitions
	HTTPRouteKey = attribute.Key("http.route")
)

Namespace: http

View Source
const (
	// HwIDKey is the attribute Key conforming to the "hw.id" semantic conventions.
	// It represents an identifier for the hardware component, unique within the
	// monitored host.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "win32battery_battery_testsysa33_1"
	HwIDKey = attribute.Key("hw.id")

	// HwNameKey is the attribute Key conforming to the "hw.name" semantic
	// conventions. It represents an easily-recognizable name for the hardware
	// component.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "eth0"
	HwNameKey = attribute.Key("hw.name")

	// HwParentKey is the attribute Key conforming to the "hw.parent" semantic
	// conventions. It represents the unique identifier of the parent component
	// (typically the `hw.id` attribute of the enclosure, or disk controller).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "dellStorage_perc_0"
	HwParentKey = attribute.Key("hw.parent")

	// HwStateKey is the attribute Key conforming to the "hw.state" semantic
	// conventions. It represents the current state of the component.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	HwStateKey = attribute.Key("hw.state")

	// HwTypeKey is the attribute Key conforming to the "hw.type" semantic
	// conventions. It represents the type of the component.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: Describes the category of the hardware component for which `hw.state`
	// is being reported. For example, `hw.type=temperature` along with
	// `hw.state=degraded` would indicate that the temperature of the hardware
	// component has been reported as `degraded`.
	HwTypeKey = attribute.Key("hw.type")
)

Namespace: hw

View Source
const (
	// K8SClusterNameKey is the attribute Key conforming to the "k8s.cluster.name"
	// semantic conventions. It represents the name of the cluster.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry-cluster"
	K8SClusterNameKey = attribute.Key("k8s.cluster.name")

	// K8SClusterUIDKey is the attribute Key conforming to the "k8s.cluster.uid"
	// semantic conventions. It represents a pseudo-ID for the cluster, set to the
	// UID of the `kube-system` namespace.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "218fc5a9-a5f1-4b54-aa05-46717d0ab26d"
	// Note: K8s doesn't have support for obtaining a cluster ID. If this is ever
	// added, we will recommend collecting the `k8s.cluster.uid` through the
	// official APIs. In the meantime, we are able to use the `uid` of the
	// `kube-system` namespace as a proxy for cluster ID. Read on for the
	// rationale.
	//
	// Every object created in a K8s cluster is assigned a distinct UID. The
	// `kube-system` namespace is used by Kubernetes itself and will exist
	// for the lifetime of the cluster. Using the `uid` of the `kube-system`
	// namespace is a reasonable proxy for the K8s ClusterID as it will only
	// change if the cluster is rebuilt. Furthermore, Kubernetes UIDs are
	// UUIDs as standardized by
	// [ISO/IEC 9834-8 and ITU-T X.667].
	// Which states:
	//
	// > If generated according to one of the mechanisms defined in Rec.
	// > ITU-T X.667 | ISO/IEC 9834-8, a UUID is either guaranteed to be
	// > different from all other UUIDs generated before 3603 A.D., or is
	// > extremely likely to be different (depending on the mechanism chosen).
	//
	// Therefore, UIDs between clusters should be extremely unlikely to
	// conflict.
	//
	// [ISO/IEC 9834-8 and ITU-T X.667]: https://www.itu.int/ITU-T/studygroups/com17/oid.html
	K8SClusterUIDKey = attribute.Key("k8s.cluster.uid")

	// K8SContainerNameKey is the attribute Key conforming to the
	// "k8s.container.name" semantic conventions. It represents the name of the
	// Container from Pod specification, must be unique within a Pod. Container
	// runtime usually uses different globally unique name (`container.name`).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "redis"
	K8SContainerNameKey = attribute.Key("k8s.container.name")

	// K8SContainerRestartCountKey is the attribute Key conforming to the
	// "k8s.container.restart_count" semantic conventions. It represents the number
	// of times the container was restarted. This attribute can be used to identify
	// a particular container (running or stopped) within a container spec.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	K8SContainerRestartCountKey = attribute.Key("k8s.container.restart_count")

	// K8SContainerStatusLastTerminatedReasonKey is the attribute Key conforming to
	// the "k8s.container.status.last_terminated_reason" semantic conventions. It
	// represents the last terminated reason of the Container.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Evicted", "Error"
	K8SContainerStatusLastTerminatedReasonKey = attribute.Key("k8s.container.status.last_terminated_reason")

	// K8SCronJobNameKey is the attribute Key conforming to the "k8s.cronjob.name"
	// semantic conventions. It represents the name of the CronJob.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SCronJobNameKey = attribute.Key("k8s.cronjob.name")

	// K8SCronJobUIDKey is the attribute Key conforming to the "k8s.cronjob.uid"
	// semantic conventions. It represents the UID of the CronJob.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SCronJobUIDKey = attribute.Key("k8s.cronjob.uid")

	// K8SDaemonSetNameKey is the attribute Key conforming to the
	// "k8s.daemonset.name" semantic conventions. It represents the name of the
	// DaemonSet.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SDaemonSetNameKey = attribute.Key("k8s.daemonset.name")

	// K8SDaemonSetUIDKey is the attribute Key conforming to the "k8s.daemonset.uid"
	// semantic conventions. It represents the UID of the DaemonSet.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SDaemonSetUIDKey = attribute.Key("k8s.daemonset.uid")

	// K8SDeploymentNameKey is the attribute Key conforming to the
	// "k8s.deployment.name" semantic conventions. It represents the name of the
	// Deployment.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SDeploymentNameKey = attribute.Key("k8s.deployment.name")

	// K8SDeploymentUIDKey is the attribute Key conforming to the
	// "k8s.deployment.uid" semantic conventions. It represents the UID of the
	// Deployment.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SDeploymentUIDKey = attribute.Key("k8s.deployment.uid")

	// K8SHpaNameKey is the attribute Key conforming to the "k8s.hpa.name" semantic
	// conventions. It represents the name of the horizontal pod autoscaler.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SHpaNameKey = attribute.Key("k8s.hpa.name")

	// K8SHpaUIDKey is the attribute Key conforming to the "k8s.hpa.uid" semantic
	// conventions. It represents the UID of the horizontal pod autoscaler.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SHpaUIDKey = attribute.Key("k8s.hpa.uid")

	// K8SJobNameKey is the attribute Key conforming to the "k8s.job.name" semantic
	// conventions. It represents the name of the Job.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SJobNameKey = attribute.Key("k8s.job.name")

	// K8SJobUIDKey is the attribute Key conforming to the "k8s.job.uid" semantic
	// conventions. It represents the UID of the Job.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SJobUIDKey = attribute.Key("k8s.job.uid")

	// K8SNamespaceNameKey is the attribute Key conforming to the
	// "k8s.namespace.name" semantic conventions. It represents the name of the
	// namespace that the pod is running in.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "default"
	K8SNamespaceNameKey = attribute.Key("k8s.namespace.name")

	// K8SNamespacePhaseKey is the attribute Key conforming to the
	// "k8s.namespace.phase" semantic conventions. It represents the phase of the
	// K8s namespace.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "active", "terminating"
	// Note: This attribute aligns with the `phase` field of the
	// [K8s NamespaceStatus]
	//
	// [K8s NamespaceStatus]: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#namespacestatus-v1-core
	K8SNamespacePhaseKey = attribute.Key("k8s.namespace.phase")

	// K8SNodeNameKey is the attribute Key conforming to the "k8s.node.name"
	// semantic conventions. It represents the name of the Node.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "node-1"
	K8SNodeNameKey = attribute.Key("k8s.node.name")

	// K8SNodeUIDKey is the attribute Key conforming to the "k8s.node.uid" semantic
	// conventions. It represents the UID of the Node.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1eb3a0c6-0477-4080-a9cb-0cb7db65c6a2"
	K8SNodeUIDKey = attribute.Key("k8s.node.uid")

	// K8SPodNameKey is the attribute Key conforming to the "k8s.pod.name" semantic
	// conventions. It represents the name of the Pod.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry-pod-autoconf"
	K8SPodNameKey = attribute.Key("k8s.pod.name")

	// K8SPodUIDKey is the attribute Key conforming to the "k8s.pod.uid" semantic
	// conventions. It represents the UID of the Pod.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SPodUIDKey = attribute.Key("k8s.pod.uid")

	// K8SReplicaSetNameKey is the attribute Key conforming to the
	// "k8s.replicaset.name" semantic conventions. It represents the name of the
	// ReplicaSet.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SReplicaSetNameKey = attribute.Key("k8s.replicaset.name")

	// K8SReplicaSetUIDKey is the attribute Key conforming to the
	// "k8s.replicaset.uid" semantic conventions. It represents the UID of the
	// ReplicaSet.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SReplicaSetUIDKey = attribute.Key("k8s.replicaset.uid")

	// K8SReplicationControllerNameKey is the attribute Key conforming to the
	// "k8s.replicationcontroller.name" semantic conventions. It represents the name
	// of the replication controller.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SReplicationControllerNameKey = attribute.Key("k8s.replicationcontroller.name")

	// K8SReplicationControllerUIDKey is the attribute Key conforming to the
	// "k8s.replicationcontroller.uid" semantic conventions. It represents the UID
	// of the replication controller.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SReplicationControllerUIDKey = attribute.Key("k8s.replicationcontroller.uid")

	// K8SResourceQuotaNameKey is the attribute Key conforming to the
	// "k8s.resourcequota.name" semantic conventions. It represents the name of the
	// resource quota.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SResourceQuotaNameKey = attribute.Key("k8s.resourcequota.name")

	// K8SResourceQuotaUIDKey is the attribute Key conforming to the
	// "k8s.resourcequota.uid" semantic conventions. It represents the UID of the
	// resource quota.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SResourceQuotaUIDKey = attribute.Key("k8s.resourcequota.uid")

	// K8SStatefulSetNameKey is the attribute Key conforming to the
	// "k8s.statefulset.name" semantic conventions. It represents the name of the
	// StatefulSet.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "opentelemetry"
	K8SStatefulSetNameKey = attribute.Key("k8s.statefulset.name")

	// K8SStatefulSetUIDKey is the attribute Key conforming to the
	// "k8s.statefulset.uid" semantic conventions. It represents the UID of the
	// StatefulSet.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "275ecb36-5aa8-4c2a-9c47-d8bb681b9aff"
	K8SStatefulSetUIDKey = attribute.Key("k8s.statefulset.uid")

	// K8SVolumeNameKey is the attribute Key conforming to the "k8s.volume.name"
	// semantic conventions. It represents the name of the K8s volume.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "volume0"
	K8SVolumeNameKey = attribute.Key("k8s.volume.name")

	// K8SVolumeTypeKey is the attribute Key conforming to the "k8s.volume.type"
	// semantic conventions. It represents the type of the K8s volume.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "emptyDir", "persistentVolumeClaim"
	K8SVolumeTypeKey = attribute.Key("k8s.volume.type")
)

Namespace: k8s

View Source
const (
	// LogFileNameKey is the attribute Key conforming to the "log.file.name"
	// semantic conventions. It represents the basename of the file.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "audit.log"
	LogFileNameKey = attribute.Key("log.file.name")

	// LogFileNameResolvedKey is the attribute Key conforming to the
	// "log.file.name_resolved" semantic conventions. It represents the basename of
	// the file, with symlinks resolved.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "uuid.log"
	LogFileNameResolvedKey = attribute.Key("log.file.name_resolved")

	// LogFilePathKey is the attribute Key conforming to the "log.file.path"
	// semantic conventions. It represents the full path to the file.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/var/log/mysql/audit.log"
	LogFilePathKey = attribute.Key("log.file.path")

	// LogFilePathResolvedKey is the attribute Key conforming to the
	// "log.file.path_resolved" semantic conventions. It represents the full path to
	// the file, with symlinks resolved.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/var/lib/docker/uuid.log"
	LogFilePathResolvedKey = attribute.Key("log.file.path_resolved")

	// LogIostreamKey is the attribute Key conforming to the "log.iostream" semantic
	// conventions. It represents the stream associated with the log. See below for
	// a list of well-known values.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	LogIostreamKey = attribute.Key("log.iostream")

	// LogRecordOriginalKey is the attribute Key conforming to the
	// "log.record.original" semantic conventions. It represents the complete
	// original Log Record.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "77 <86>1 2015-08-06T21:58:59.694Z 192.168.2.133 inactive - - -
	// Something happened", "[INFO] 8/3/24 12:34:56 Something happened"
	// Note: This value MAY be added when processing a Log Record which was
	// originally transmitted as a string or equivalent data type AND the Body field
	// of the Log Record does not contain the same value. (e.g. a syslog or a log
	// record read from a file.)
	LogRecordOriginalKey = attribute.Key("log.record.original")

	// LogRecordUIDKey is the attribute Key conforming to the "log.record.uid"
	// semantic conventions. It represents a unique identifier for the Log Record.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "01ARZ3NDEKTSV4RRFFQ69G5FAV"
	// Note: If an id is provided, other log records with the same id will be
	// considered duplicates and can be removed safely. This means, that two
	// distinguishable log records MUST have different values.
	// The id MAY be an
	// [Universally Unique Lexicographically Sortable Identifier (ULID)], but other
	// identifiers (e.g. UUID) may be used as needed.
	//
	// [Universally Unique Lexicographically Sortable Identifier (ULID)]: https://github.com/ulid/spec
	LogRecordUIDKey = attribute.Key("log.record.uid")
)

Namespace: log

View Source
const (
	// MessagingBatchMessageCountKey is the attribute Key conforming to the
	// "messaging.batch.message_count" semantic conventions. It represents the
	// number of messages sent, received, or processed in the scope of the batching
	// operation.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 0, 1, 2
	// Note: Instrumentations SHOULD NOT set `messaging.batch.message_count` on
	// spans that operate with a single message. When a messaging client library
	// supports both batch and single-message API for the same operation,
	// instrumentations SHOULD use `messaging.batch.message_count` for batching APIs
	// and SHOULD NOT use it for single-message APIs.
	MessagingBatchMessageCountKey = attribute.Key("messaging.batch.message_count")

	// MessagingClientIDKey is the attribute Key conforming to the
	// "messaging.client.id" semantic conventions. It represents a unique identifier
	// for the client that consumes or produces a message.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "client-5", "myhost@8742@s8083jm"
	MessagingClientIDKey = attribute.Key("messaging.client.id")

	// MessagingConsumerGroupNameKey is the attribute Key conforming to the
	// "messaging.consumer.group.name" semantic conventions. It represents the name
	// of the consumer group with which a consumer is associated.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-group", "indexer"
	// Note: Semantic conventions for individual messaging systems SHOULD document
	// whether `messaging.consumer.group.name` is applicable and what it means in
	// the context of that system.
	MessagingConsumerGroupNameKey = attribute.Key("messaging.consumer.group.name")

	// MessagingDestinationAnonymousKey is the attribute Key conforming to the
	// "messaging.destination.anonymous" semantic conventions. It represents a
	// boolean that is true if the message destination is anonymous (could be
	// unnamed or have auto-generated name).
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	MessagingDestinationAnonymousKey = attribute.Key("messaging.destination.anonymous")

	// MessagingDestinationNameKey is the attribute Key conforming to the
	// "messaging.destination.name" semantic conventions. It represents the message
	// destination name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "MyQueue", "MyTopic"
	// Note: Destination name SHOULD uniquely identify a specific queue, topic or
	// other entity within the broker. If
	// the broker doesn't have such notion, the destination name SHOULD uniquely
	// identify the broker.
	MessagingDestinationNameKey = attribute.Key("messaging.destination.name")

	// MessagingDestinationPartitionIDKey is the attribute Key conforming to the
	// "messaging.destination.partition.id" semantic conventions. It represents the
	// identifier of the partition messages are sent to or received from, unique
	// within the `messaging.destination.name`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1
	MessagingDestinationPartitionIDKey = attribute.Key("messaging.destination.partition.id")

	// MessagingDestinationSubscriptionNameKey is the attribute Key conforming to
	// the "messaging.destination.subscription.name" semantic conventions. It
	// represents the name of the destination subscription from which a message is
	// consumed.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "subscription-a"
	// Note: Semantic conventions for individual messaging systems SHOULD document
	// whether `messaging.destination.subscription.name` is applicable and what it
	// means in the context of that system.
	MessagingDestinationSubscriptionNameKey = attribute.Key("messaging.destination.subscription.name")

	// MessagingDestinationTemplateKey is the attribute Key conforming to the
	// "messaging.destination.template" semantic conventions. It represents the low
	// cardinality representation of the messaging destination name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/customers/{customerId}"
	// Note: Destination names could be constructed from templates. An example would
	// be a destination name involving a user name or product id. Although the
	// destination name in this case is of high cardinality, the underlying template
	// is of low cardinality and can be effectively used for grouping and
	// aggregation.
	MessagingDestinationTemplateKey = attribute.Key("messaging.destination.template")

	// MessagingDestinationTemporaryKey is the attribute Key conforming to the
	// "messaging.destination.temporary" semantic conventions. It represents a
	// boolean that is true if the message destination is temporary and might not
	// exist anymore after messages are processed.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	MessagingDestinationTemporaryKey = attribute.Key("messaging.destination.temporary")

	// MessagingEventhubsMessageEnqueuedTimeKey is the attribute Key conforming to
	// the "messaging.eventhubs.message.enqueued_time" semantic conventions. It
	// represents the UTC epoch seconds at which the message has been accepted and
	// stored in the entity.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingEventhubsMessageEnqueuedTimeKey = attribute.Key("messaging.eventhubs.message.enqueued_time")

	// MessagingGCPPubsubMessageAckDeadlineKey is the attribute Key conforming to
	// the "messaging.gcp_pubsub.message.ack_deadline" semantic conventions. It
	// represents the ack deadline in seconds set for the modify ack deadline
	// request.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingGCPPubsubMessageAckDeadlineKey = attribute.Key("messaging.gcp_pubsub.message.ack_deadline")

	// MessagingGCPPubsubMessageAckIDKey is the attribute Key conforming to the
	// "messaging.gcp_pubsub.message.ack_id" semantic conventions. It represents the
	// ack id for a given message.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: ack_id
	MessagingGCPPubsubMessageAckIDKey = attribute.Key("messaging.gcp_pubsub.message.ack_id")

	// MessagingGCPPubsubMessageDeliveryAttemptKey is the attribute Key conforming
	// to the "messaging.gcp_pubsub.message.delivery_attempt" semantic conventions.
	// It represents the delivery attempt for a given message.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingGCPPubsubMessageDeliveryAttemptKey = attribute.Key("messaging.gcp_pubsub.message.delivery_attempt")

	// MessagingGCPPubsubMessageOrderingKeyKey is the attribute Key conforming to
	// the "messaging.gcp_pubsub.message.ordering_key" semantic conventions. It
	// represents the ordering key for a given message. If the attribute is not
	// present, the message does not have an ordering key.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: ordering_key
	MessagingGCPPubsubMessageOrderingKeyKey = attribute.Key("messaging.gcp_pubsub.message.ordering_key")

	// MessagingKafkaMessageKeyKey is the attribute Key conforming to the
	// "messaging.kafka.message.key" semantic conventions. It represents the message
	// keys in Kafka are used for grouping alike messages to ensure they're
	// processed on the same partition. They differ from `messaging.message.id` in
	// that they're not unique. If the key is `null`, the attribute MUST NOT be set.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: myKey
	// Note: If the key type is not string, it's string representation has to be
	// supplied for the attribute. If the key has no unambiguous, canonical string
	// form, don't include its value.
	MessagingKafkaMessageKeyKey = attribute.Key("messaging.kafka.message.key")

	// MessagingKafkaMessageTombstoneKey is the attribute Key conforming to the
	// "messaging.kafka.message.tombstone" semantic conventions. It represents a
	// boolean that is true if the message is a tombstone.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	MessagingKafkaMessageTombstoneKey = attribute.Key("messaging.kafka.message.tombstone")

	// MessagingKafkaOffsetKey is the attribute Key conforming to the
	// "messaging.kafka.offset" semantic conventions. It represents the offset of a
	// record in the corresponding Kafka partition.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingKafkaOffsetKey = attribute.Key("messaging.kafka.offset")

	// MessagingMessageBodySizeKey is the attribute Key conforming to the
	// "messaging.message.body.size" semantic conventions. It represents the size of
	// the message body in bytes.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Note: This can refer to both the compressed or uncompressed body size. If
	// both sizes are known, the uncompressed
	// body size should be used.
	MessagingMessageBodySizeKey = attribute.Key("messaging.message.body.size")

	// MessagingMessageConversationIDKey is the attribute Key conforming to the
	// "messaging.message.conversation_id" semantic conventions. It represents the
	// conversation ID identifying the conversation to which the message belongs,
	// represented as a string. Sometimes called "Correlation ID".
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: MyConversationId
	MessagingMessageConversationIDKey = attribute.Key("messaging.message.conversation_id")

	// MessagingMessageEnvelopeSizeKey is the attribute Key conforming to the
	// "messaging.message.envelope.size" semantic conventions. It represents the
	// size of the message body and metadata in bytes.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Note: This can refer to both the compressed or uncompressed size. If both
	// sizes are known, the uncompressed
	// size should be used.
	MessagingMessageEnvelopeSizeKey = attribute.Key("messaging.message.envelope.size")

	// MessagingMessageIDKey is the attribute Key conforming to the
	// "messaging.message.id" semantic conventions. It represents a value used by
	// the messaging system as an identifier for the message, represented as a
	// string.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 452a7c7c7c7048c2f887f61572b18fc2
	MessagingMessageIDKey = attribute.Key("messaging.message.id")

	// MessagingOperationNameKey is the attribute Key conforming to the
	// "messaging.operation.name" semantic conventions. It represents the
	// system-specific name of the messaging operation.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "ack", "nack", "send"
	MessagingOperationNameKey = attribute.Key("messaging.operation.name")

	// MessagingOperationTypeKey is the attribute Key conforming to the
	// "messaging.operation.type" semantic conventions. It represents a string
	// identifying the type of the messaging operation.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: If a custom value is used, it MUST be of low cardinality.
	MessagingOperationTypeKey = attribute.Key("messaging.operation.type")

	// MessagingRabbitmqDestinationRoutingKeyKey is the attribute Key conforming to
	// the "messaging.rabbitmq.destination.routing_key" semantic conventions. It
	// represents the rabbitMQ message routing key.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: myKey
	MessagingRabbitmqDestinationRoutingKeyKey = attribute.Key("messaging.rabbitmq.destination.routing_key")

	// MessagingRabbitmqMessageDeliveryTagKey is the attribute Key conforming to the
	// "messaging.rabbitmq.message.delivery_tag" semantic conventions. It represents
	// the rabbitMQ message delivery tag.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingRabbitmqMessageDeliveryTagKey = attribute.Key("messaging.rabbitmq.message.delivery_tag")

	// MessagingRocketmqConsumptionModelKey is the attribute Key conforming to the
	// "messaging.rocketmq.consumption_model" semantic conventions. It represents
	// the model of message consumption. This only applies to consumer spans.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	MessagingRocketmqConsumptionModelKey = attribute.Key("messaging.rocketmq.consumption_model")

	// MessagingRocketmqMessageDelayTimeLevelKey is the attribute Key conforming to
	// the "messaging.rocketmq.message.delay_time_level" semantic conventions. It
	// represents the delay time level for delay message, which determines the
	// message delay time.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingRocketmqMessageDelayTimeLevelKey = attribute.Key("messaging.rocketmq.message.delay_time_level")

	// MessagingRocketmqMessageDeliveryTimestampKey is the attribute Key conforming
	// to the "messaging.rocketmq.message.delivery_timestamp" semantic conventions.
	// It represents the timestamp in milliseconds that the delay message is
	// expected to be delivered to consumer.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingRocketmqMessageDeliveryTimestampKey = attribute.Key("messaging.rocketmq.message.delivery_timestamp")

	// MessagingRocketmqMessageGroupKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.group" semantic conventions. It represents the it
	// is essential for FIFO message. Messages that belong to the same message group
	// are always processed one by one within the same consumer group.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: myMessageGroup
	MessagingRocketmqMessageGroupKey = attribute.Key("messaging.rocketmq.message.group")

	// MessagingRocketmqMessageKeysKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.keys" semantic conventions. It represents the
	// key(s) of message, another way to mark message besides message id.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "keyA", "keyB"
	MessagingRocketmqMessageKeysKey = attribute.Key("messaging.rocketmq.message.keys")

	// MessagingRocketmqMessageTagKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.tag" semantic conventions. It represents the
	// secondary classifier of message besides topic.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: tagA
	MessagingRocketmqMessageTagKey = attribute.Key("messaging.rocketmq.message.tag")

	// MessagingRocketmqMessageTypeKey is the attribute Key conforming to the
	// "messaging.rocketmq.message.type" semantic conventions. It represents the
	// type of message.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	MessagingRocketmqMessageTypeKey = attribute.Key("messaging.rocketmq.message.type")

	// MessagingRocketmqNamespaceKey is the attribute Key conforming to the
	// "messaging.rocketmq.namespace" semantic conventions. It represents the
	// namespace of RocketMQ resources, resources in different namespaces are
	// individual.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: myNamespace
	MessagingRocketmqNamespaceKey = attribute.Key("messaging.rocketmq.namespace")

	// MessagingServicebusDispositionStatusKey is the attribute Key conforming to
	// the "messaging.servicebus.disposition_status" semantic conventions. It
	// represents the describes the [settlement type].
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	//
	// [settlement type]: https://learn.microsoft.com/azure/service-bus-messaging/message-transfers-locks-settlement#peeklock
	MessagingServicebusDispositionStatusKey = attribute.Key("messaging.servicebus.disposition_status")

	// MessagingServicebusMessageDeliveryCountKey is the attribute Key conforming to
	// the "messaging.servicebus.message.delivery_count" semantic conventions. It
	// represents the number of deliveries that have been attempted for this
	// message.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingServicebusMessageDeliveryCountKey = attribute.Key("messaging.servicebus.message.delivery_count")

	// MessagingServicebusMessageEnqueuedTimeKey is the attribute Key conforming to
	// the "messaging.servicebus.message.enqueued_time" semantic conventions. It
	// represents the UTC epoch seconds at which the message has been accepted and
	// stored in the entity.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	MessagingServicebusMessageEnqueuedTimeKey = attribute.Key("messaging.servicebus.message.enqueued_time")

	// MessagingSystemKey is the attribute Key conforming to the "messaging.system"
	// semantic conventions. It represents the messaging system as identified by the
	// client instrumentation.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: The actual messaging system may differ from the one known by the
	// client. For example, when using Kafka client libraries to communicate with
	// Azure Event Hubs, the `messaging.system` is set to `kafka` based on the
	// instrumentation's best knowledge.
	MessagingSystemKey = attribute.Key("messaging.system")
)

Namespace: messaging

View Source
const (
	// NetworkCarrierIccKey is the attribute Key conforming to the
	// "network.carrier.icc" semantic conventions. It represents the ISO 3166-1
	// alpha-2 2-character country code associated with the mobile carrier network.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: DE
	NetworkCarrierIccKey = attribute.Key("network.carrier.icc")

	// NetworkCarrierMccKey is the attribute Key conforming to the
	// "network.carrier.mcc" semantic conventions. It represents the mobile carrier
	// country code.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 310
	NetworkCarrierMccKey = attribute.Key("network.carrier.mcc")

	// NetworkCarrierMncKey is the attribute Key conforming to the
	// "network.carrier.mnc" semantic conventions. It represents the mobile carrier
	// network code.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 001
	NetworkCarrierMncKey = attribute.Key("network.carrier.mnc")

	// NetworkCarrierNameKey is the attribute Key conforming to the
	// "network.carrier.name" semantic conventions. It represents the name of the
	// mobile carrier.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: sprint
	NetworkCarrierNameKey = attribute.Key("network.carrier.name")

	// NetworkConnectionStateKey is the attribute Key conforming to the
	// "network.connection.state" semantic conventions. It represents the state of
	// network connection.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "close_wait"
	// Note: Connection states are defined as part of the [rfc9293]
	//
	// [rfc9293]: https://datatracker.ietf.org/doc/html/rfc9293#section-3.3.2
	NetworkConnectionStateKey = attribute.Key("network.connection.state")

	// NetworkConnectionSubtypeKey is the attribute Key conforming to the
	// "network.connection.subtype" semantic conventions. It represents the this
	// describes more details regarding the connection.type. It may be the type of
	// cell technology connection, but it could be used for describing details about
	// a wifi connection.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: LTE
	NetworkConnectionSubtypeKey = attribute.Key("network.connection.subtype")

	// NetworkConnectionTypeKey is the attribute Key conforming to the
	// "network.connection.type" semantic conventions. It represents the internet
	// connection type.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: wifi
	NetworkConnectionTypeKey = attribute.Key("network.connection.type")

	// NetworkInterfaceNameKey is the attribute Key conforming to the
	// "network.interface.name" semantic conventions. It represents the network
	// interface name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "lo", "eth0"
	NetworkInterfaceNameKey = attribute.Key("network.interface.name")

	// NetworkIoDirectionKey is the attribute Key conforming to the
	// "network.io.direction" semantic conventions. It represents the network IO
	// operation direction.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "transmit"
	NetworkIoDirectionKey = attribute.Key("network.io.direction")

	// NetworkLocalAddressKey is the attribute Key conforming to the
	// "network.local.address" semantic conventions. It represents the local address
	// of the network connection - IP address or Unix domain socket name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "10.1.2.80", "/tmp/my.sock"
	NetworkLocalAddressKey = attribute.Key("network.local.address")

	// NetworkLocalPortKey is the attribute Key conforming to the
	// "network.local.port" semantic conventions. It represents the local port
	// number of the network connection.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: 65123
	NetworkLocalPortKey = attribute.Key("network.local.port")

	// NetworkPeerAddressKey is the attribute Key conforming to the
	// "network.peer.address" semantic conventions. It represents the peer address
	// of the network connection - IP address or Unix domain socket name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "10.1.2.80", "/tmp/my.sock"
	NetworkPeerAddressKey = attribute.Key("network.peer.address")

	// NetworkPeerPortKey is the attribute Key conforming to the "network.peer.port"
	// semantic conventions. It represents the peer port number of the network
	// connection.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: 65123
	NetworkPeerPortKey = attribute.Key("network.peer.port")

	// NetworkProtocolNameKey is the attribute Key conforming to the
	// "network.protocol.name" semantic conventions. It represents the
	// [OSI application layer] or non-OSI equivalent.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "amqp", "http", "mqtt"
	// Note: The value SHOULD be normalized to lowercase.
	//
	// [OSI application layer]: https://wikipedia.org/wiki/Application_layer
	NetworkProtocolNameKey = attribute.Key("network.protocol.name")

	// NetworkProtocolVersionKey is the attribute Key conforming to the
	// "network.protocol.version" semantic conventions. It represents the actual
	// version of the protocol used for network communication.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "1.1", "2"
	// Note: If protocol version is subject to negotiation (for example using [ALPN]
	// ), this attribute SHOULD be set to the negotiated version. If the actual
	// protocol version is not known, this attribute SHOULD NOT be set.
	//
	// [ALPN]: https://www.rfc-editor.org/rfc/rfc7301.html
	NetworkProtocolVersionKey = attribute.Key("network.protocol.version")

	// NetworkTransportKey is the attribute Key conforming to the
	// "network.transport" semantic conventions. It represents the
	// [OSI transport layer] or [inter-process communication method].
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "tcp", "udp"
	// Note: The value SHOULD be normalized to lowercase.
	//
	// Consider always setting the transport when setting a port number, since
	// a port number is ambiguous without knowing the transport. For example
	// different processes could be listening on TCP port 12345 and UDP port 12345.
	//
	// [OSI transport layer]: https://wikipedia.org/wiki/Transport_layer
	// [inter-process communication method]: https://wikipedia.org/wiki/Inter-process_communication
	NetworkTransportKey = attribute.Key("network.transport")

	// NetworkTypeKey is the attribute Key conforming to the "network.type" semantic
	// conventions. It represents the [OSI network layer] or non-OSI equivalent.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "ipv4", "ipv6"
	// Note: The value SHOULD be normalized to lowercase.
	//
	// [OSI network layer]: https://wikipedia.org/wiki/Network_layer
	NetworkTypeKey = attribute.Key("network.type")
)

Namespace: network

View Source
const (
	// OSBuildIDKey is the attribute Key conforming to the "os.build_id" semantic
	// conventions. It represents the unique identifier for a particular build or
	// compilation of the operating system.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "TQ3C.230805.001.B2", "20E247", "22621"
	OSBuildIDKey = attribute.Key("os.build_id")

	// OSDescriptionKey is the attribute Key conforming to the "os.description"
	// semantic conventions. It represents the human readable (not intended to be
	// parsed) OS version information, like e.g. reported by `ver` or
	// `lsb_release -a` commands.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Microsoft Windows [Version 10.0.18363.778]", "Ubuntu 18.04.1 LTS"
	OSDescriptionKey = attribute.Key("os.description")

	// OSNameKey is the attribute Key conforming to the "os.name" semantic
	// conventions. It represents the human readable operating system name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "iOS", "Android", "Ubuntu"
	OSNameKey = attribute.Key("os.name")

	// OSTypeKey is the attribute Key conforming to the "os.type" semantic
	// conventions. It represents the operating system type.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	OSTypeKey = attribute.Key("os.type")

	// OSVersionKey is the attribute Key conforming to the "os.version" semantic
	// conventions. It represents the version string of the operating system as
	// defined in [Version Attributes].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "14.2.1", "18.04.1"
	//
	// [Version Attributes]: /docs/resource/README.md#version-attributes
	OSVersionKey = attribute.Key("os.version")
)

Namespace: os

View Source
const (
	// OTelComponentNameKey is the attribute Key conforming to the
	// "otel.component.name" semantic conventions. It represents a name uniquely
	// identifying the instance of the OpenTelemetry component within its containing
	// SDK instance.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "otlp_grpc_span_exporter/0", "custom-name"
	// Note: Implementations SHOULD ensure a low cardinality for this attribute,
	// even across application or SDK restarts.
	// E.g. implementations MUST NOT use UUIDs as values for this attribute.
	//
	// Implementations MAY achieve these goals by following a
	// `<otel.component.type>/<instance-counter>` pattern, e.g.
	// `batching_span_processor/0`.
	// Hereby `otel.component.type` refers to the corresponding attribute value of
	// the component.
	//
	// The value of `instance-counter` MAY be automatically assigned by the
	// component and uniqueness within the enclosing SDK instance MUST be
	// guaranteed.
	// For example, `<instance-counter>` MAY be implemented by using a monotonically
	// increasing counter (starting with `0`), which is incremented every time an
	// instance of the given component type is started.
	//
	// With this implementation, for example the first Batching Span Processor would
	// have `batching_span_processor/0`
	// as `otel.component.name`, the second one `batching_span_processor/1` and so
	// on.
	// These values will therefore be reused in the case of an application restart.
	OTelComponentNameKey = attribute.Key("otel.component.name")

	// OTelComponentTypeKey is the attribute Key conforming to the
	// "otel.component.type" semantic conventions. It represents a name identifying
	// the type of the OpenTelemetry component.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "batching_span_processor", "com.example.MySpanExporter"
	// Note: If none of the standardized values apply, implementations SHOULD use
	// the language-defined name of the type.
	// E.g. for Java the fully qualified classname SHOULD be used in this case.
	OTelComponentTypeKey = attribute.Key("otel.component.type")

	// OTelScopeNameKey is the attribute Key conforming to the "otel.scope.name"
	// semantic conventions. It represents the name of the instrumentation scope - (
	// `InstrumentationScope.Name` in OTLP).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "io.opentelemetry.contrib.mongodb"
	OTelScopeNameKey = attribute.Key("otel.scope.name")

	// OTelScopeVersionKey is the attribute Key conforming to the
	// "otel.scope.version" semantic conventions. It represents the version of the
	// instrumentation scope - (`InstrumentationScope.Version` in OTLP).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "1.0.0"
	OTelScopeVersionKey = attribute.Key("otel.scope.version")

	// OTelSpanSamplingResultKey is the attribute Key conforming to the
	// "otel.span.sampling_result" semantic conventions. It represents the result
	// value of the sampler for this span.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	OTelSpanSamplingResultKey = attribute.Key("otel.span.sampling_result")

	// OTelStatusCodeKey is the attribute Key conforming to the "otel.status_code"
	// semantic conventions. It represents the name of the code, either "OK" or
	// "ERROR". MUST NOT be set if the status code is UNSET.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples:
	OTelStatusCodeKey = attribute.Key("otel.status_code")

	// OTelStatusDescriptionKey is the attribute Key conforming to the
	// "otel.status_description" semantic conventions. It represents the description
	// of the Status if it has a value, otherwise not set.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "resource not found"
	OTelStatusDescriptionKey = attribute.Key("otel.status_description")
)

Namespace: otel

View Source
const (
	// ProcessArgsCountKey is the attribute Key conforming to the
	// "process.args_count" semantic conventions. It represents the length of the
	// process.command_args array.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 4
	// Note: This field can be useful for querying or performing bucket analysis on
	// how many arguments were provided to start a process. More arguments may be an
	// indication of suspicious activity.
	ProcessArgsCountKey = attribute.Key("process.args_count")

	// ProcessCommandKey is the attribute Key conforming to the "process.command"
	// semantic conventions. It represents the command used to launch the process
	// (i.e. the command name). On Linux based systems, can be set to the zeroth
	// string in `proc/[pid]/cmdline`. On Windows, can be set to the first parameter
	// extracted from `GetCommandLineW`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "cmd/otelcol"
	ProcessCommandKey = attribute.Key("process.command")

	// ProcessCommandArgsKey is the attribute Key conforming to the
	// "process.command_args" semantic conventions. It represents the all the
	// command arguments (including the command/executable itself) as received by
	// the process. On Linux-based systems (and some other Unixoid systems
	// supporting procfs), can be set according to the list of null-delimited
	// strings extracted from `proc/[pid]/cmdline`. For libc-based executables, this
	// would be the full argv vector passed to `main`.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "cmd/otecol", "--config=config.yaml"
	ProcessCommandArgsKey = attribute.Key("process.command_args")

	// ProcessCommandLineKey is the attribute Key conforming to the
	// "process.command_line" semantic conventions. It represents the full command
	// used to launch the process as a single string representing the full command.
	// On Windows, can be set to the result of `GetCommandLineW`. Do not set this if
	// you have to assemble it just for monitoring; use `process.command_args`
	// instead.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "C:\cmd\otecol --config="my directory\config.yaml""
	ProcessCommandLineKey = attribute.Key("process.command_line")

	// ProcessContextSwitchTypeKey is the attribute Key conforming to the
	// "process.context_switch_type" semantic conventions. It represents the
	// specifies whether the context switches for this data point were voluntary or
	// involuntary.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	ProcessContextSwitchTypeKey = attribute.Key("process.context_switch_type")

	// ProcessCreationTimeKey is the attribute Key conforming to the
	// "process.creation.time" semantic conventions. It represents the date and time
	// the process was created, in ISO 8601 format.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2023-11-21T09:25:34.853Z"
	ProcessCreationTimeKey = attribute.Key("process.creation.time")

	// ProcessExecutableBuildIDGnuKey is the attribute Key conforming to the
	// "process.executable.build_id.gnu" semantic conventions. It represents the GNU
	// build ID as found in the `.note.gnu.build-id` ELF section (hex string).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "c89b11207f6479603b0d49bf291c092c2b719293"
	ProcessExecutableBuildIDGnuKey = attribute.Key("process.executable.build_id.gnu")

	// ProcessExecutableBuildIDGoKey is the attribute Key conforming to the
	// "process.executable.build_id.go" semantic conventions. It represents the Go
	// build ID as retrieved by `go tool buildid <go executable>`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "foh3mEXu7BLZjsN9pOwG/kATcXlYVCDEFouRMQed_/WwRFB1hPo9LBkekthSPG/x8hMC8emW2cCjXD0_1aY"
	ProcessExecutableBuildIDGoKey = attribute.Key("process.executable.build_id.go")

	// ProcessExecutableBuildIDHtlhashKey is the attribute Key conforming to the
	// "process.executable.build_id.htlhash" semantic conventions. It represents the
	// profiling specific build ID for executables. See the OTel specification for
	// Profiles for more information.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "600DCAFE4A110000F2BF38C493F5FB92"
	ProcessExecutableBuildIDHtlhashKey = attribute.Key("process.executable.build_id.htlhash")

	// ProcessExecutableNameKey is the attribute Key conforming to the
	// "process.executable.name" semantic conventions. It represents the name of the
	// process executable. On Linux based systems, this SHOULD be set to the base
	// name of the target of `/proc/[pid]/exe`. On Windows, this SHOULD be set to
	// the base name of `GetProcessImageFileNameW`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "otelcol"
	ProcessExecutableNameKey = attribute.Key("process.executable.name")

	// ProcessExecutablePathKey is the attribute Key conforming to the
	// "process.executable.path" semantic conventions. It represents the full path
	// to the process executable. On Linux based systems, can be set to the target
	// of `proc/[pid]/exe`. On Windows, can be set to the result of
	// `GetProcessImageFileNameW`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/usr/bin/cmd/otelcol"
	ProcessExecutablePathKey = attribute.Key("process.executable.path")

	// ProcessExitCodeKey is the attribute Key conforming to the "process.exit.code"
	// semantic conventions. It represents the exit code of the process.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 127
	ProcessExitCodeKey = attribute.Key("process.exit.code")

	// ProcessExitTimeKey is the attribute Key conforming to the "process.exit.time"
	// semantic conventions. It represents the date and time the process exited, in
	// ISO 8601 format.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2023-11-21T09:26:12.315Z"
	ProcessExitTimeKey = attribute.Key("process.exit.time")

	// ProcessGroupLeaderPIDKey is the attribute Key conforming to the
	// "process.group_leader.pid" semantic conventions. It represents the PID of the
	// process's group leader. This is also the process group ID (PGID) of the
	// process.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 23
	ProcessGroupLeaderPIDKey = attribute.Key("process.group_leader.pid")

	// ProcessInteractiveKey is the attribute Key conforming to the
	// "process.interactive" semantic conventions. It represents the whether the
	// process is connected to an interactive shell.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	ProcessInteractiveKey = attribute.Key("process.interactive")

	// ProcessLinuxCgroupKey is the attribute Key conforming to the
	// "process.linux.cgroup" semantic conventions. It represents the control group
	// associated with the process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1:name=systemd:/user.slice/user-1000.slice/session-3.scope",
	// "0::/user.slice/user-1000.slice/user@1000.service/tmux-spawn-0267755b-4639-4a27-90ed-f19f88e53748.scope"
	// Note: Control groups (cgroups) are a kernel feature used to organize and
	// manage process resources. This attribute provides the path(s) to the
	// cgroup(s) associated with the process, which should match the contents of the
	// [/proc/[PID]/cgroup] file.
	//
	// [/proc/[PID]/cgroup]: https://man7.org/linux/man-pages/man7/cgroups.7.html
	ProcessLinuxCgroupKey = attribute.Key("process.linux.cgroup")

	// ProcessOwnerKey is the attribute Key conforming to the "process.owner"
	// semantic conventions. It represents the username of the user that owns the
	// process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "root"
	ProcessOwnerKey = attribute.Key("process.owner")

	// ProcessPagingFaultTypeKey is the attribute Key conforming to the
	// "process.paging.fault_type" semantic conventions. It represents the type of
	// page fault for this data point. Type `major` is for major/hard page faults,
	// and `minor` is for minor/soft page faults.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	ProcessPagingFaultTypeKey = attribute.Key("process.paging.fault_type")

	// ProcessParentPIDKey is the attribute Key conforming to the
	// "process.parent_pid" semantic conventions. It represents the parent Process
	// identifier (PPID).
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 111
	ProcessParentPIDKey = attribute.Key("process.parent_pid")

	// ProcessPIDKey is the attribute Key conforming to the "process.pid" semantic
	// conventions. It represents the process identifier (PID).
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1234
	ProcessPIDKey = attribute.Key("process.pid")

	// ProcessRealUserIDKey is the attribute Key conforming to the
	// "process.real_user.id" semantic conventions. It represents the real user ID
	// (RUID) of the process.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1000
	ProcessRealUserIDKey = attribute.Key("process.real_user.id")

	// ProcessRealUserNameKey is the attribute Key conforming to the
	// "process.real_user.name" semantic conventions. It represents the username of
	// the real user of the process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "operator"
	ProcessRealUserNameKey = attribute.Key("process.real_user.name")

	// ProcessRuntimeDescriptionKey is the attribute Key conforming to the
	// "process.runtime.description" semantic conventions. It represents an
	// additional description about the runtime of the process, for example a
	// specific vendor customization of the runtime environment.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: Eclipse OpenJ9 Eclipse OpenJ9 VM openj9-0.21.0
	ProcessRuntimeDescriptionKey = attribute.Key("process.runtime.description")

	// ProcessRuntimeNameKey is the attribute Key conforming to the
	// "process.runtime.name" semantic conventions. It represents the name of the
	// runtime of this process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "OpenJDK Runtime Environment"
	ProcessRuntimeNameKey = attribute.Key("process.runtime.name")

	// ProcessRuntimeVersionKey is the attribute Key conforming to the
	// "process.runtime.version" semantic conventions. It represents the version of
	// the runtime of this process, as returned by the runtime without modification.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 14.0.2
	ProcessRuntimeVersionKey = attribute.Key("process.runtime.version")

	// ProcessSavedUserIDKey is the attribute Key conforming to the
	// "process.saved_user.id" semantic conventions. It represents the saved user ID
	// (SUID) of the process.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1002
	ProcessSavedUserIDKey = attribute.Key("process.saved_user.id")

	// ProcessSavedUserNameKey is the attribute Key conforming to the
	// "process.saved_user.name" semantic conventions. It represents the username of
	// the saved user.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "operator"
	ProcessSavedUserNameKey = attribute.Key("process.saved_user.name")

	// ProcessSessionLeaderPIDKey is the attribute Key conforming to the
	// "process.session_leader.pid" semantic conventions. It represents the PID of
	// the process's session leader. This is also the session ID (SID) of the
	// process.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 14
	ProcessSessionLeaderPIDKey = attribute.Key("process.session_leader.pid")

	// ProcessTitleKey is the attribute Key conforming to the "process.title"
	// semantic conventions. It represents the process title (proctitle).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "cat /etc/hostname", "xfce4-session", "bash"
	// Note: In many Unix-like systems, process title (proctitle), is the string
	// that represents the name or command line of a running process, displayed by
	// system monitoring tools like ps, top, and htop.
	ProcessTitleKey = attribute.Key("process.title")

	// ProcessUserIDKey is the attribute Key conforming to the "process.user.id"
	// semantic conventions. It represents the effective user ID (EUID) of the
	// process.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1001
	ProcessUserIDKey = attribute.Key("process.user.id")

	// ProcessUserNameKey is the attribute Key conforming to the "process.user.name"
	// semantic conventions. It represents the username of the effective user of the
	// process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "root"
	ProcessUserNameKey = attribute.Key("process.user.name")

	// ProcessVpidKey is the attribute Key conforming to the "process.vpid" semantic
	// conventions. It represents the virtual process identifier.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 12
	// Note: The process ID within a PID namespace. This is not necessarily unique
	// across all processes on the host but it is unique within the process
	// namespace that the process exists within.
	ProcessVpidKey = attribute.Key("process.vpid")

	// ProcessWorkingDirectoryKey is the attribute Key conforming to the
	// "process.working_directory" semantic conventions. It represents the working
	// directory of the process.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/root"
	ProcessWorkingDirectoryKey = attribute.Key("process.working_directory")
)

Namespace: process

View Source
const (
	// RPCConnectRPCErrorCodeKey is the attribute Key conforming to the
	// "rpc.connect_rpc.error_code" semantic conventions. It represents the
	// [error codes] of the Connect request. Error codes are always string values.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	//
	// [error codes]: https://connectrpc.com//docs/protocol/#error-codes
	RPCConnectRPCErrorCodeKey = attribute.Key("rpc.connect_rpc.error_code")

	// RPCGRPCStatusCodeKey is the attribute Key conforming to the
	// "rpc.grpc.status_code" semantic conventions. It represents the
	// [numeric status code] of the gRPC request.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	//
	// [numeric status code]: https://github.com/grpc/grpc/blob/v1.33.2/doc/statuscodes.md
	RPCGRPCStatusCodeKey = attribute.Key("rpc.grpc.status_code")

	// RPCJsonrpcErrorCodeKey is the attribute Key conforming to the
	// "rpc.jsonrpc.error_code" semantic conventions. It represents the `error.code`
	//  property of response if it is an error response.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: -32700, 100
	RPCJsonrpcErrorCodeKey = attribute.Key("rpc.jsonrpc.error_code")

	// RPCJsonrpcErrorMessageKey is the attribute Key conforming to the
	// "rpc.jsonrpc.error_message" semantic conventions. It represents the
	// `error.message` property of response if it is an error response.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Parse error", "User already exists"
	RPCJsonrpcErrorMessageKey = attribute.Key("rpc.jsonrpc.error_message")

	// RPCJsonrpcRequestIDKey is the attribute Key conforming to the
	// "rpc.jsonrpc.request_id" semantic conventions. It represents the `id`
	// property of request or response. Since protocol allows id to be int, string,
	// `null` or missing (for notifications), value is expected to be cast to string
	// for simplicity. Use empty string in case of `null` value. Omit entirely if
	// this is a notification.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "10", "request-7", ""
	RPCJsonrpcRequestIDKey = attribute.Key("rpc.jsonrpc.request_id")

	// RPCJsonrpcVersionKey is the attribute Key conforming to the
	// "rpc.jsonrpc.version" semantic conventions. It represents the protocol
	// version as in `jsonrpc` property of request/response. Since JSON-RPC 1.0
	// doesn't specify this, the value can be omitted.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2.0", "1.0"
	RPCJsonrpcVersionKey = attribute.Key("rpc.jsonrpc.version")

	// RPCMessageCompressedSizeKey is the attribute Key conforming to the
	// "rpc.message.compressed_size" semantic conventions. It represents the
	// compressed size of the message in bytes.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	RPCMessageCompressedSizeKey = attribute.Key("rpc.message.compressed_size")

	// RPCMessageIDKey is the attribute Key conforming to the "rpc.message.id"
	// semantic conventions. It MUST be calculated as two different counters
	// starting from `1` one for sent messages and one for received message.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: This way we guarantee that the values will be consistent between
	// different implementations.
	RPCMessageIDKey = attribute.Key("rpc.message.id")

	// RPCMessageTypeKey is the attribute Key conforming to the "rpc.message.type"
	// semantic conventions. It represents the whether this is a received or sent
	// message.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	RPCMessageTypeKey = attribute.Key("rpc.message.type")

	// RPCMessageUncompressedSizeKey is the attribute Key conforming to the
	// "rpc.message.uncompressed_size" semantic conventions. It represents the
	// uncompressed size of the message in bytes.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	RPCMessageUncompressedSizeKey = attribute.Key("rpc.message.uncompressed_size")

	// RPCMethodKey is the attribute Key conforming to the "rpc.method" semantic
	// conventions. It represents the name of the (logical) method being called,
	// must be equal to the $method part in the span name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: exampleMethod
	// Note: This is the logical name of the method from the RPC interface
	// perspective, which can be different from the name of any implementing
	// method/function. The `code.function.name` attribute may be used to store the
	// latter (e.g., method actually executing the call on the server side, RPC
	// client stub method on the client side).
	RPCMethodKey = attribute.Key("rpc.method")

	// RPCServiceKey is the attribute Key conforming to the "rpc.service" semantic
	// conventions. It represents the full (logical) name of the service being
	// called, including its package name, if applicable.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: myservice.EchoService
	// Note: This is the logical name of the service from the RPC interface
	// perspective, which can be different from the name of any implementing class.
	// The `code.namespace` attribute may be used to store the latter (despite the
	// attribute name, it may include a class name; e.g., class with method actually
	// executing the call on the server side, RPC client stub class on the client
	// side).
	RPCServiceKey = attribute.Key("rpc.service")

	// RPCSystemKey is the attribute Key conforming to the "rpc.system" semantic
	// conventions. It represents a string identifying the remoting system. See
	// below for a list of well-known identifiers.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	RPCSystemKey = attribute.Key("rpc.system")
)

Namespace: rpc

View Source
const (
	// SecurityRuleCategoryKey is the attribute Key conforming to the
	// "security_rule.category" semantic conventions. It represents a categorization
	// value keyword used by the entity using the rule for detection of this event.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Attempted Information Leak"
	SecurityRuleCategoryKey = attribute.Key("security_rule.category")

	// SecurityRuleDescriptionKey is the attribute Key conforming to the
	// "security_rule.description" semantic conventions. It represents the
	// description of the rule generating the event.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Block requests to public DNS over HTTPS / TLS protocols"
	SecurityRuleDescriptionKey = attribute.Key("security_rule.description")

	// SecurityRuleLicenseKey is the attribute Key conforming to the
	// "security_rule.license" semantic conventions. It represents the name of the
	// license under which the rule used to generate this event is made available.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Apache 2.0"
	SecurityRuleLicenseKey = attribute.Key("security_rule.license")

	// SecurityRuleNameKey is the attribute Key conforming to the
	// "security_rule.name" semantic conventions. It represents the name of the rule
	// or signature generating the event.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "BLOCK_DNS_over_TLS"
	SecurityRuleNameKey = attribute.Key("security_rule.name")

	// SecurityRuleReferenceKey is the attribute Key conforming to the
	// "security_rule.reference" semantic conventions. It represents the reference
	// URL to additional information about the rule used to generate this event.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "https://en.wikipedia.org/wiki/DNS_over_TLS"
	// Note: The URL can point to the vendor’s documentation about the rule. If
	// that’s not available, it can also be a link to a more general page
	// describing this type of alert.
	SecurityRuleReferenceKey = attribute.Key("security_rule.reference")

	// SecurityRuleRulesetNameKey is the attribute Key conforming to the
	// "security_rule.ruleset.name" semantic conventions. It represents the name of
	// the ruleset, policy, group, or parent category in which the rule used to
	// generate this event is a member.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Standard_Protocol_Filters"
	SecurityRuleRulesetNameKey = attribute.Key("security_rule.ruleset.name")

	// SecurityRuleUUIDKey is the attribute Key conforming to the
	// "security_rule.uuid" semantic conventions. It represents a rule ID that is
	// unique within the scope of a set or group of agents, observers, or other
	// entities using the rule for detection of this event.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "550e8400-e29b-41d4-a716-446655440000", "1100110011"
	SecurityRuleUUIDKey = attribute.Key("security_rule.uuid")

	// SecurityRuleVersionKey is the attribute Key conforming to the
	// "security_rule.version" semantic conventions. It represents the version /
	// revision of the rule being used for analysis.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1.0.0"
	SecurityRuleVersionKey = attribute.Key("security_rule.version")
)

Namespace: security_rule

View Source
const (
	// ServerAddressKey is the attribute Key conforming to the "server.address"
	// semantic conventions. It represents the server domain name if available
	// without reverse DNS lookup; otherwise, IP address or Unix domain socket name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "example.com", "10.1.2.80", "/tmp/my.sock"
	// Note: When observed from the client side, and when communicating through an
	// intermediary, `server.address` SHOULD represent the server address behind any
	// intermediaries, for example proxies, if it's available.
	ServerAddressKey = attribute.Key("server.address")

	// ServerPortKey is the attribute Key conforming to the "server.port" semantic
	// conventions. It represents the server port number.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: 80, 8080, 443
	// Note: When observed from the client side, and when communicating through an
	// intermediary, `server.port` SHOULD represent the server port behind any
	// intermediaries, for example proxies, if it's available.
	ServerPortKey = attribute.Key("server.port")
)

Namespace: server

View Source
const (
	// ServiceInstanceIDKey is the attribute Key conforming to the
	// "service.instance.id" semantic conventions. It represents the string ID of
	// the service instance.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "627cc493-f310-47de-96bd-71410b7dec09"
	// Note: MUST be unique for each instance of the same
	// `service.namespace,service.name` pair (in other words
	// `service.namespace,service.name,service.instance.id` triplet MUST be globally
	// unique). The ID helps to
	// distinguish instances of the same service that exist at the same time (e.g.
	// instances of a horizontally scaled
	// service).
	//
	// Implementations, such as SDKs, are recommended to generate a random Version 1
	// or Version 4 [RFC
	// 4122] UUID, but are free to use an inherent unique ID as
	// the source of
	// this value if stability is desirable. In that case, the ID SHOULD be used as
	// source of a UUID Version 5 and
	// SHOULD use the following UUID as the namespace:
	// `4d63009a-8d0f-11ee-aad7-4c796ed8e320`.
	//
	// UUIDs are typically recommended, as only an opaque value for the purposes of
	// identifying a service instance is
	// needed. Similar to what can be seen in the man page for the
	// [`/etc/machine-id`] file, the underlying
	// data, such as pod name and namespace should be treated as confidential, being
	// the user's choice to expose it
	// or not via another resource attribute.
	//
	// For applications running behind an application server (like unicorn), we do
	// not recommend using one identifier
	// for all processes participating in the application. Instead, it's recommended
	// each division (e.g. a worker
	// thread in unicorn) to have its own instance.id.
	//
	// It's not recommended for a Collector to set `service.instance.id` if it can't
	// unambiguously determine the
	// service instance that is generating that telemetry. For instance, creating an
	// UUID based on `pod.name` will
	// likely be wrong, as the Collector might not know from which container within
	// that pod the telemetry originated.
	// However, Collectors can set the `service.instance.id` if they can
	// unambiguously determine the service instance
	// for that telemetry. This is typically the case for scraping receivers, as
	// they know the target address and
	// port.
	//
	// [RFC
	// 4122]: https://www.ietf.org/rfc/rfc4122.txt
	// [`/etc/machine-id`]: https://www.freedesktop.org/software/systemd/man/latest/machine-id.html
	ServiceInstanceIDKey = attribute.Key("service.instance.id")

	// ServiceNameKey is the attribute Key conforming to the "service.name" semantic
	// conventions. It represents the logical name of the service.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "shoppingcart"
	// Note: MUST be the same for all instances of horizontally scaled services. If
	// the value was not specified, SDKs MUST fallback to `unknown_service:`
	// concatenated with [`process.executable.name`], e.g. `unknown_service:bash`.
	// If `process.executable.name` is not available, the value MUST be set to
	// `unknown_service`.
	//
	// [`process.executable.name`]: process.md
	ServiceNameKey = attribute.Key("service.name")

	// ServiceNamespaceKey is the attribute Key conforming to the
	// "service.namespace" semantic conventions. It represents a namespace for
	// `service.name`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Shop"
	// Note: A string value having a meaning that helps to distinguish a group of
	// services, for example the team name that owns a group of services.
	// `service.name` is expected to be unique within the same namespace. If
	// `service.namespace` is not specified in the Resource then `service.name` is
	// expected to be unique for all services that have no explicit namespace
	// defined (so the empty/unspecified namespace is simply one more valid
	// namespace). Zero-length namespace string is assumed equal to unspecified
	// namespace.
	ServiceNamespaceKey = attribute.Key("service.namespace")

	// ServiceVersionKey is the attribute Key conforming to the "service.version"
	// semantic conventions. It represents the version string of the service API or
	// implementation. The format is not defined by these conventions.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "2.0.0", "a01dbef8a"
	ServiceVersionKey = attribute.Key("service.version")
)

Namespace: service

View Source
const (
	// SessionIDKey is the attribute Key conforming to the "session.id" semantic
	// conventions. It represents a unique id to identify a session.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 00112233-4455-6677-8899-aabbccddeeff
	SessionIDKey = attribute.Key("session.id")

	// SessionPreviousIDKey is the attribute Key conforming to the
	// "session.previous_id" semantic conventions. It represents the previous
	// `session.id` for this user, when known.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 00112233-4455-6677-8899-aabbccddeeff
	SessionPreviousIDKey = attribute.Key("session.previous_id")
)

Namespace: session

View Source
const (
	// SignalrConnectionStatusKey is the attribute Key conforming to the
	// "signalr.connection.status" semantic conventions. It represents the signalR
	// HTTP connection closure status.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "app_shutdown", "timeout"
	SignalrConnectionStatusKey = attribute.Key("signalr.connection.status")

	// SignalrTransportKey is the attribute Key conforming to the
	// "signalr.transport" semantic conventions. It represents the
	// [SignalR transport type].
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "web_sockets", "long_polling"
	//
	// [SignalR transport type]: https://github.com/dotnet/aspnetcore/blob/main/src/SignalR/docs/specs/TransportProtocols.md
	SignalrTransportKey = attribute.Key("signalr.transport")
)

Namespace: signalr

View Source
const (
	// SourceAddressKey is the attribute Key conforming to the "source.address"
	// semantic conventions. It represents the source address - domain name if
	// available without reverse DNS lookup; otherwise, IP address or Unix domain
	// socket name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "source.example.com", "10.1.2.80", "/tmp/my.sock"
	// Note: When observed from the destination side, and when communicating through
	// an intermediary, `source.address` SHOULD represent the source address behind
	// any intermediaries, for example proxies, if it's available.
	SourceAddressKey = attribute.Key("source.address")

	// SourcePortKey is the attribute Key conforming to the "source.port" semantic
	// conventions. It represents the source port number.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 3389, 2888
	SourcePortKey = attribute.Key("source.port")
)

Namespace: source

View Source
const (
	// SystemCPULogicalNumberKey is the attribute Key conforming to the
	// "system.cpu.logical_number" semantic conventions. It represents the
	// deprecated, use `cpu.logical_number` instead.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 1
	SystemCPULogicalNumberKey = attribute.Key("system.cpu.logical_number")

	// SystemDeviceKey is the attribute Key conforming to the "system.device"
	// semantic conventions. It represents the device identifier.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "(identifier)"
	SystemDeviceKey = attribute.Key("system.device")

	// SystemFilesystemModeKey is the attribute Key conforming to the
	// "system.filesystem.mode" semantic conventions. It represents the filesystem
	// mode.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "rw, ro"
	SystemFilesystemModeKey = attribute.Key("system.filesystem.mode")

	// SystemFilesystemMountpointKey is the attribute Key conforming to the
	// "system.filesystem.mountpoint" semantic conventions. It represents the
	// filesystem mount path.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/mnt/data"
	SystemFilesystemMountpointKey = attribute.Key("system.filesystem.mountpoint")

	// SystemFilesystemStateKey is the attribute Key conforming to the
	// "system.filesystem.state" semantic conventions. It represents the filesystem
	// state.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "used"
	SystemFilesystemStateKey = attribute.Key("system.filesystem.state")

	// SystemFilesystemTypeKey is the attribute Key conforming to the
	// "system.filesystem.type" semantic conventions. It represents the filesystem
	// type.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "ext4"
	SystemFilesystemTypeKey = attribute.Key("system.filesystem.type")

	// SystemMemoryStateKey is the attribute Key conforming to the
	// "system.memory.state" semantic conventions. It represents the memory state.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "free", "cached"
	SystemMemoryStateKey = attribute.Key("system.memory.state")

	// SystemPagingDirectionKey is the attribute Key conforming to the
	// "system.paging.direction" semantic conventions. It represents the paging
	// access direction.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "in"
	SystemPagingDirectionKey = attribute.Key("system.paging.direction")

	// SystemPagingStateKey is the attribute Key conforming to the
	// "system.paging.state" semantic conventions. It represents the memory paging
	// state.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "free"
	SystemPagingStateKey = attribute.Key("system.paging.state")

	// SystemPagingTypeKey is the attribute Key conforming to the
	// "system.paging.type" semantic conventions. It represents the memory paging
	// type.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "minor"
	SystemPagingTypeKey = attribute.Key("system.paging.type")

	// SystemProcessStatusKey is the attribute Key conforming to the
	// "system.process.status" semantic conventions. It represents the process
	// state, e.g., [Linux Process State Codes].
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "running"
	//
	// [Linux Process State Codes]: https://man7.org/linux/man-pages/man1/ps.1.html#PROCESS_STATE_CODES
	SystemProcessStatusKey = attribute.Key("system.process.status")
)

Namespace: system

View Source
const (
	// TelemetryDistroNameKey is the attribute Key conforming to the
	// "telemetry.distro.name" semantic conventions. It represents the name of the
	// auto instrumentation agent or distribution, if used.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "parts-unlimited-java"
	// Note: Official auto instrumentation agents and distributions SHOULD set the
	// `telemetry.distro.name` attribute to
	// a string starting with `opentelemetry-`, e.g.
	// `opentelemetry-java-instrumentation`.
	TelemetryDistroNameKey = attribute.Key("telemetry.distro.name")

	// TelemetryDistroVersionKey is the attribute Key conforming to the
	// "telemetry.distro.version" semantic conventions. It represents the version
	// string of the auto instrumentation agent or distribution, if used.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1.2.3"
	TelemetryDistroVersionKey = attribute.Key("telemetry.distro.version")

	// TelemetrySDKLanguageKey is the attribute Key conforming to the
	// "telemetry.sdk.language" semantic conventions. It represents the language of
	// the telemetry SDK.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples:
	TelemetrySDKLanguageKey = attribute.Key("telemetry.sdk.language")

	// TelemetrySDKNameKey is the attribute Key conforming to the
	// "telemetry.sdk.name" semantic conventions. It represents the name of the
	// telemetry SDK as defined above.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "opentelemetry"
	// Note: The OpenTelemetry SDK MUST set the `telemetry.sdk.name` attribute to
	// `opentelemetry`.
	// If another SDK, like a fork or a vendor-provided implementation, is used,
	// this SDK MUST set the
	// `telemetry.sdk.name` attribute to the fully-qualified class or module name of
	// this SDK's main entry point
	// or another suitable identifier depending on the language.
	// The identifier `opentelemetry` is reserved and MUST NOT be used in this case.
	// All custom identifiers SHOULD be stable across different versions of an
	// implementation.
	TelemetrySDKNameKey = attribute.Key("telemetry.sdk.name")

	// TelemetrySDKVersionKey is the attribute Key conforming to the
	// "telemetry.sdk.version" semantic conventions. It represents the version
	// string of the telemetry SDK.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "1.2.3"
	TelemetrySDKVersionKey = attribute.Key("telemetry.sdk.version")
)

Namespace: telemetry

View Source
const (
	// TestCaseNameKey is the attribute Key conforming to the "test.case.name"
	// semantic conventions. It represents the fully qualified human readable name
	// of the [test case].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "org.example.TestCase1.test1", "example/tests/TestCase1.test1",
	// "ExampleTestCase1_test1"
	//
	// [test case]: https://wikipedia.org/wiki/Test_case
	TestCaseNameKey = attribute.Key("test.case.name")

	// TestCaseResultStatusKey is the attribute Key conforming to the
	// "test.case.result.status" semantic conventions. It represents the status of
	// the actual test case result from test execution.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "pass", "fail"
	TestCaseResultStatusKey = attribute.Key("test.case.result.status")

	// TestSuiteNameKey is the attribute Key conforming to the "test.suite.name"
	// semantic conventions. It represents the human readable name of a [test suite]
	// .
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "TestSuite1"
	//
	// [test suite]: https://wikipedia.org/wiki/Test_suite
	TestSuiteNameKey = attribute.Key("test.suite.name")

	// TestSuiteRunStatusKey is the attribute Key conforming to the
	// "test.suite.run.status" semantic conventions. It represents the status of the
	// test suite run.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "success", "failure", "skipped", "aborted", "timed_out",
	// "in_progress"
	TestSuiteRunStatusKey = attribute.Key("test.suite.run.status")
)

Namespace: test

View Source
const (
	// ThreadIDKey is the attribute Key conforming to the "thread.id" semantic
	// conventions. It represents the current "managed" thread ID (as opposed to OS
	// thread ID).
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	ThreadIDKey = attribute.Key("thread.id")

	// ThreadNameKey is the attribute Key conforming to the "thread.name" semantic
	// conventions. It represents the current thread name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: main
	ThreadNameKey = attribute.Key("thread.name")
)

Namespace: thread

View Source
const (
	// TLSCipherKey is the attribute Key conforming to the "tls.cipher" semantic
	// conventions. It represents the string indicating the [cipher] used during the
	// current connection.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "TLS_RSA_WITH_3DES_EDE_CBC_SHA",
	// "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
	// Note: The values allowed for `tls.cipher` MUST be one of the `Descriptions`
	// of the [registered TLS Cipher Suits].
	//
	// [cipher]: https://datatracker.ietf.org/doc/html/rfc5246#appendix-A.5
	// [registered TLS Cipher Suits]: https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml#table-tls-parameters-4
	TLSCipherKey = attribute.Key("tls.cipher")

	// TLSClientCertificateKey is the attribute Key conforming to the
	// "tls.client.certificate" semantic conventions. It represents the PEM-encoded
	// stand-alone certificate offered by the client. This is usually
	// mutually-exclusive of `client.certificate_chain` since this value also exists
	// in that list.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "MII..."
	TLSClientCertificateKey = attribute.Key("tls.client.certificate")

	// TLSClientCertificateChainKey is the attribute Key conforming to the
	// "tls.client.certificate_chain" semantic conventions. It represents the array
	// of PEM-encoded certificates that make up the certificate chain offered by the
	// client. This is usually mutually-exclusive of `client.certificate` since that
	// value should be the first certificate in the chain.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "MII...", "MI..."
	TLSClientCertificateChainKey = attribute.Key("tls.client.certificate_chain")

	// TLSClientHashMd5Key is the attribute Key conforming to the
	// "tls.client.hash.md5" semantic conventions. It represents the certificate
	// fingerprint using the MD5 digest of DER-encoded version of certificate
	// offered by the client. For consistency with other hash values, this value
	// should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "0F76C7F2C55BFD7D8E8B8F4BFBF0C9EC"
	TLSClientHashMd5Key = attribute.Key("tls.client.hash.md5")

	// TLSClientHashSha1Key is the attribute Key conforming to the
	// "tls.client.hash.sha1" semantic conventions. It represents the certificate
	// fingerprint using the SHA1 digest of DER-encoded version of certificate
	// offered by the client. For consistency with other hash values, this value
	// should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "9E393D93138888D288266C2D915214D1D1CCEB2A"
	TLSClientHashSha1Key = attribute.Key("tls.client.hash.sha1")

	// TLSClientHashSha256Key is the attribute Key conforming to the
	// "tls.client.hash.sha256" semantic conventions. It represents the certificate
	// fingerprint using the SHA256 digest of DER-encoded version of certificate
	// offered by the client. For consistency with other hash values, this value
	// should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "0687F666A054EF17A08E2F2162EAB4CBC0D265E1D7875BE74BF3C712CA92DAF0"
	TLSClientHashSha256Key = attribute.Key("tls.client.hash.sha256")

	// TLSClientIssuerKey is the attribute Key conforming to the "tls.client.issuer"
	// semantic conventions. It represents the distinguished name of [subject] of
	// the issuer of the x.509 certificate presented by the client.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "CN=Example Root CA, OU=Infrastructure Team, DC=example, DC=com"
	//
	// [subject]: https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6
	TLSClientIssuerKey = attribute.Key("tls.client.issuer")

	// TLSClientJa3Key is the attribute Key conforming to the "tls.client.ja3"
	// semantic conventions. It represents a hash that identifies clients based on
	// how they perform an SSL/TLS handshake.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "d4e5b18d6b55c71272893221c96ba240"
	TLSClientJa3Key = attribute.Key("tls.client.ja3")

	// TLSClientNotAfterKey is the attribute Key conforming to the
	// "tls.client.not_after" semantic conventions. It represents the date/Time
	// indicating when client certificate is no longer considered valid.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2021-01-01T00:00:00.000Z"
	TLSClientNotAfterKey = attribute.Key("tls.client.not_after")

	// TLSClientNotBeforeKey is the attribute Key conforming to the
	// "tls.client.not_before" semantic conventions. It represents the date/Time
	// indicating when client certificate is first considered valid.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1970-01-01T00:00:00.000Z"
	TLSClientNotBeforeKey = attribute.Key("tls.client.not_before")

	// TLSClientSubjectKey is the attribute Key conforming to the
	// "tls.client.subject" semantic conventions. It represents the distinguished
	// name of subject of the x.509 certificate presented by the client.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "CN=myclient, OU=Documentation Team, DC=example, DC=com"
	TLSClientSubjectKey = attribute.Key("tls.client.subject")

	// TLSClientSupportedCiphersKey is the attribute Key conforming to the
	// "tls.client.supported_ciphers" semantic conventions. It represents the array
	// of ciphers offered by the client during the client hello.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
	// "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
	TLSClientSupportedCiphersKey = attribute.Key("tls.client.supported_ciphers")

	// TLSCurveKey is the attribute Key conforming to the "tls.curve" semantic
	// conventions. It represents the string indicating the curve used for the given
	// cipher, when applicable.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "secp256r1"
	TLSCurveKey = attribute.Key("tls.curve")

	// TLSEstablishedKey is the attribute Key conforming to the "tls.established"
	// semantic conventions. It represents the boolean flag indicating if the TLS
	// negotiation was successful and transitioned to an encrypted tunnel.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: true
	TLSEstablishedKey = attribute.Key("tls.established")

	// TLSNextProtocolKey is the attribute Key conforming to the "tls.next_protocol"
	// semantic conventions. It represents the string indicating the protocol being
	// tunneled. Per the values in the [IANA registry], this string should be lower
	// case.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "http/1.1"
	//
	// [IANA registry]: https://www.iana.org/assignments/tls-extensiontype-values/tls-extensiontype-values.xhtml#alpn-protocol-ids
	TLSNextProtocolKey = attribute.Key("tls.next_protocol")

	// TLSProtocolNameKey is the attribute Key conforming to the "tls.protocol.name"
	// semantic conventions. It represents the normalized lowercase protocol name
	// parsed from original string of the negotiated [SSL/TLS protocol version].
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	//
	// [SSL/TLS protocol version]: https://docs.openssl.org/1.1.1/man3/SSL_get_version/#return-values
	TLSProtocolNameKey = attribute.Key("tls.protocol.name")

	// TLSProtocolVersionKey is the attribute Key conforming to the
	// "tls.protocol.version" semantic conventions. It represents the numeric part
	// of the version parsed from the original string of the negotiated
	// [SSL/TLS protocol version].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1.2", "3"
	//
	// [SSL/TLS protocol version]: https://docs.openssl.org/1.1.1/man3/SSL_get_version/#return-values
	TLSProtocolVersionKey = attribute.Key("tls.protocol.version")

	// TLSResumedKey is the attribute Key conforming to the "tls.resumed" semantic
	// conventions. It represents the boolean flag indicating if this TLS connection
	// was resumed from an existing TLS negotiation.
	//
	// Type: boolean
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: true
	TLSResumedKey = attribute.Key("tls.resumed")

	// TLSServerCertificateKey is the attribute Key conforming to the
	// "tls.server.certificate" semantic conventions. It represents the PEM-encoded
	// stand-alone certificate offered by the server. This is usually
	// mutually-exclusive of `server.certificate_chain` since this value also exists
	// in that list.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "MII..."
	TLSServerCertificateKey = attribute.Key("tls.server.certificate")

	// TLSServerCertificateChainKey is the attribute Key conforming to the
	// "tls.server.certificate_chain" semantic conventions. It represents the array
	// of PEM-encoded certificates that make up the certificate chain offered by the
	// server. This is usually mutually-exclusive of `server.certificate` since that
	// value should be the first certificate in the chain.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "MII...", "MI..."
	TLSServerCertificateChainKey = attribute.Key("tls.server.certificate_chain")

	// TLSServerHashMd5Key is the attribute Key conforming to the
	// "tls.server.hash.md5" semantic conventions. It represents the certificate
	// fingerprint using the MD5 digest of DER-encoded version of certificate
	// offered by the server. For consistency with other hash values, this value
	// should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "0F76C7F2C55BFD7D8E8B8F4BFBF0C9EC"
	TLSServerHashMd5Key = attribute.Key("tls.server.hash.md5")

	// TLSServerHashSha1Key is the attribute Key conforming to the
	// "tls.server.hash.sha1" semantic conventions. It represents the certificate
	// fingerprint using the SHA1 digest of DER-encoded version of certificate
	// offered by the server. For consistency with other hash values, this value
	// should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "9E393D93138888D288266C2D915214D1D1CCEB2A"
	TLSServerHashSha1Key = attribute.Key("tls.server.hash.sha1")

	// TLSServerHashSha256Key is the attribute Key conforming to the
	// "tls.server.hash.sha256" semantic conventions. It represents the certificate
	// fingerprint using the SHA256 digest of DER-encoded version of certificate
	// offered by the server. For consistency with other hash values, this value
	// should be formatted as an uppercase hash.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "0687F666A054EF17A08E2F2162EAB4CBC0D265E1D7875BE74BF3C712CA92DAF0"
	TLSServerHashSha256Key = attribute.Key("tls.server.hash.sha256")

	// TLSServerIssuerKey is the attribute Key conforming to the "tls.server.issuer"
	// semantic conventions. It represents the distinguished name of [subject] of
	// the issuer of the x.509 certificate presented by the client.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "CN=Example Root CA, OU=Infrastructure Team, DC=example, DC=com"
	//
	// [subject]: https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6
	TLSServerIssuerKey = attribute.Key("tls.server.issuer")

	// TLSServerJa3sKey is the attribute Key conforming to the "tls.server.ja3s"
	// semantic conventions. It represents a hash that identifies servers based on
	// how they perform an SSL/TLS handshake.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "d4e5b18d6b55c71272893221c96ba240"
	TLSServerJa3sKey = attribute.Key("tls.server.ja3s")

	// TLSServerNotAfterKey is the attribute Key conforming to the
	// "tls.server.not_after" semantic conventions. It represents the date/Time
	// indicating when server certificate is no longer considered valid.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "2021-01-01T00:00:00.000Z"
	TLSServerNotAfterKey = attribute.Key("tls.server.not_after")

	// TLSServerNotBeforeKey is the attribute Key conforming to the
	// "tls.server.not_before" semantic conventions. It represents the date/Time
	// indicating when server certificate is first considered valid.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "1970-01-01T00:00:00.000Z"
	TLSServerNotBeforeKey = attribute.Key("tls.server.not_before")

	// TLSServerSubjectKey is the attribute Key conforming to the
	// "tls.server.subject" semantic conventions. It represents the distinguished
	// name of subject of the x.509 certificate presented by the server.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "CN=myserver, OU=Documentation Team, DC=example, DC=com"
	TLSServerSubjectKey = attribute.Key("tls.server.subject")
)

Namespace: tls

View Source
const (
	// URLDomainKey is the attribute Key conforming to the "url.domain" semantic
	// conventions. It represents the domain extracted from the `url.full`, such as
	// "opentelemetry.io".
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "www.foo.bar", "opentelemetry.io", "3.12.167.2",
	// "[1080:0:0:0:8:800:200C:417A]"
	// Note: In some cases a URL may refer to an IP and/or port directly, without a
	// domain name. In this case, the IP address would go to the domain field. If
	// the URL contains a [literal IPv6 address] enclosed by `[` and `]`, the `[`
	// and `]` characters should also be captured in the domain field.
	//
	// [literal IPv6 address]: https://www.rfc-editor.org/rfc/rfc2732#section-2
	URLDomainKey = attribute.Key("url.domain")

	// URLExtensionKey is the attribute Key conforming to the "url.extension"
	// semantic conventions. It represents the file extension extracted from the
	// `url.full`, excluding the leading dot.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "png", "gz"
	// Note: The file extension is only set if it exists, as not every url has a
	// file extension. When the file name has multiple extensions `example.tar.gz`,
	// only the last one should be captured `gz`, not `tar.gz`.
	URLExtensionKey = attribute.Key("url.extension")

	// URLFragmentKey is the attribute Key conforming to the "url.fragment" semantic
	// conventions. It represents the [URI fragment] component.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "SemConv"
	//
	// [URI fragment]: https://www.rfc-editor.org/rfc/rfc3986#section-3.5
	URLFragmentKey = attribute.Key("url.fragment")

	// URLFullKey is the attribute Key conforming to the "url.full" semantic
	// conventions. It represents the absolute URL describing a network resource
	// according to [RFC3986].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "https://www.foo.bar/search?q=OpenTelemetry#SemConv", "//localhost"
	// Note: For network calls, URL usually has
	// `scheme://host[:port][path][?query][#fragment]` format, where the fragment
	// is not transmitted over HTTP, but if it is known, it SHOULD be included
	// nevertheless.
	//
	// `url.full` MUST NOT contain credentials passed via URL in form of
	// `https://username:password@www.example.com/`.
	// In such case username and password SHOULD be redacted and attribute's value
	// SHOULD be `https://REDACTED:REDACTED@www.example.com/`.
	//
	// `url.full` SHOULD capture the absolute URL when it is available (or can be
	// reconstructed).
	//
	// Sensitive content provided in `url.full` SHOULD be scrubbed when
	// instrumentations can identify it.
	//
	//
	// Query string values for the following keys SHOULD be redacted by default and
	// replaced by the
	// value `REDACTED`:
	//
	//   - [`AWSAccessKeyId`]
	//   - [`Signature`]
	//   - [`sig`]
	//   - [`X-Goog-Signature`]
	//
	// This list is subject to change over time.
	//
	// When a query string value is redacted, the query string key SHOULD still be
	// preserved, e.g.
	// `https://www.example.com/path?color=blue&sig=REDACTED`.
	//
	// [RFC3986]: https://www.rfc-editor.org/rfc/rfc3986
	// [`AWSAccessKeyId`]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html#RESTAuthenticationQueryStringAuth
	// [`Signature`]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html#RESTAuthenticationQueryStringAuth
	// [`sig`]: https://learn.microsoft.com/azure/storage/common/storage-sas-overview#sas-token
	// [`X-Goog-Signature`]: https://cloud.google.com/storage/docs/access-control/signed-urls
	URLFullKey = attribute.Key("url.full")

	// URLOriginalKey is the attribute Key conforming to the "url.original" semantic
	// conventions. It represents the unmodified original URL as seen in the event
	// source.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "https://www.foo.bar/search?q=OpenTelemetry#SemConv",
	// "search?q=OpenTelemetry"
	// Note: In network monitoring, the observed URL may be a full URL, whereas in
	// access logs, the URL is often just represented as a path. This field is meant
	// to represent the URL as it was observed, complete or not.
	// `url.original` might contain credentials passed via URL in form of
	// `https://username:password@www.example.com/`. In such case password and
	// username SHOULD NOT be redacted and attribute's value SHOULD remain the same.
	URLOriginalKey = attribute.Key("url.original")

	// URLPathKey is the attribute Key conforming to the "url.path" semantic
	// conventions. It represents the [URI path] component.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "/search"
	// Note: Sensitive content provided in `url.path` SHOULD be scrubbed when
	// instrumentations can identify it.
	//
	// [URI path]: https://www.rfc-editor.org/rfc/rfc3986#section-3.3
	URLPathKey = attribute.Key("url.path")

	// URLPortKey is the attribute Key conforming to the "url.port" semantic
	// conventions. It represents the port extracted from the `url.full`.
	//
	// Type: int
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: 443
	URLPortKey = attribute.Key("url.port")

	// URLQueryKey is the attribute Key conforming to the "url.query" semantic
	// conventions. It represents the [URI query] component.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "q=OpenTelemetry"
	// Note: Sensitive content provided in `url.query` SHOULD be scrubbed when
	// instrumentations can identify it.
	//
	//
	// Query string values for the following keys SHOULD be redacted by default and
	// replaced by the value `REDACTED`:
	//
	//   - [`AWSAccessKeyId`]
	//   - [`Signature`]
	//   - [`sig`]
	//   - [`X-Goog-Signature`]
	//
	// This list is subject to change over time.
	//
	// When a query string value is redacted, the query string key SHOULD still be
	// preserved, e.g.
	// `q=OpenTelemetry&sig=REDACTED`.
	//
	// [URI query]: https://www.rfc-editor.org/rfc/rfc3986#section-3.4
	// [`AWSAccessKeyId`]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html#RESTAuthenticationQueryStringAuth
	// [`Signature`]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html#RESTAuthenticationQueryStringAuth
	// [`sig`]: https://learn.microsoft.com/azure/storage/common/storage-sas-overview#sas-token
	// [`X-Goog-Signature`]: https://cloud.google.com/storage/docs/access-control/signed-urls
	URLQueryKey = attribute.Key("url.query")

	// URLRegisteredDomainKey is the attribute Key conforming to the
	// "url.registered_domain" semantic conventions. It represents the highest
	// registered url domain, stripped of the subdomain.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "example.com", "foo.co.uk"
	// Note: This value can be determined precisely with the [public suffix list].
	// For example, the registered domain for `foo.example.com` is `example.com`.
	// Trying to approximate this by simply taking the last two labels will not work
	// well for TLDs such as `co.uk`.
	//
	// [public suffix list]: https://publicsuffix.org/
	URLRegisteredDomainKey = attribute.Key("url.registered_domain")

	// URLSchemeKey is the attribute Key conforming to the "url.scheme" semantic
	// conventions. It represents the [URI scheme] component identifying the used
	// protocol.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "https", "ftp", "telnet"
	//
	// [URI scheme]: https://www.rfc-editor.org/rfc/rfc3986#section-3.1
	URLSchemeKey = attribute.Key("url.scheme")

	// URLSubdomainKey is the attribute Key conforming to the "url.subdomain"
	// semantic conventions. It represents the subdomain portion of a fully
	// qualified domain name includes all of the names except the host name under
	// the registered_domain. In a partially qualified domain, or if the
	// qualification level of the full name cannot be determined, subdomain contains
	// all of the names below the registered domain.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "east", "sub2.sub1"
	// Note: The subdomain portion of `www.east.mydomain.co.uk` is `east`. If the
	// domain has multiple levels of subdomain, such as `sub2.sub1.example.com`, the
	// subdomain field should contain `sub2.sub1`, with no trailing period.
	URLSubdomainKey = attribute.Key("url.subdomain")

	// URLTemplateKey is the attribute Key conforming to the "url.template" semantic
	// conventions. It represents the low-cardinality template of an
	// [absolute path reference].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "/users/{id}", "/users/:id", "/users?id={id}"
	//
	// [absolute path reference]: https://www.rfc-editor.org/rfc/rfc3986#section-4.2
	URLTemplateKey = attribute.Key("url.template")

	// URLTopLevelDomainKey is the attribute Key conforming to the
	// "url.top_level_domain" semantic conventions. It represents the effective top
	// level domain (eTLD), also known as the domain suffix, is the last part of the
	// domain name. For example, the top level domain for example.com is `com`.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "com", "co.uk"
	// Note: This value can be determined precisely with the [public suffix list].
	//
	// [public suffix list]: https://publicsuffix.org/
	URLTopLevelDomainKey = attribute.Key("url.top_level_domain")
)

Namespace: url

View Source
const (
	// UserEmailKey is the attribute Key conforming to the "user.email" semantic
	// conventions. It represents the user email address.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "a.einstein@example.com"
	UserEmailKey = attribute.Key("user.email")

	// UserFullNameKey is the attribute Key conforming to the "user.full_name"
	// semantic conventions. It represents the user's full name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Albert Einstein"
	UserFullNameKey = attribute.Key("user.full_name")

	// UserHashKey is the attribute Key conforming to the "user.hash" semantic
	// conventions. It represents the unique user hash to correlate information for
	// a user in anonymized form.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "364fc68eaf4c8acec74a4e52d7d1feaa"
	// Note: Useful if `user.id` or `user.name` contain confidential information and
	// cannot be used.
	UserHashKey = attribute.Key("user.hash")

	// UserIDKey is the attribute Key conforming to the "user.id" semantic
	// conventions. It represents the unique identifier of the user.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "S-1-5-21-202424912787-2692429404-2351956786-1000"
	UserIDKey = attribute.Key("user.id")

	// UserNameKey is the attribute Key conforming to the "user.name" semantic
	// conventions. It represents the short name or login/username of the user.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "a.einstein"
	UserNameKey = attribute.Key("user.name")

	// UserRolesKey is the attribute Key conforming to the "user.roles" semantic
	// conventions. It represents the array of user roles at the time of the event.
	//
	// Type: string[]
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "admin", "reporting_user"
	UserRolesKey = attribute.Key("user.roles")
)

Namespace: user

View Source
const (
	// UserAgentNameKey is the attribute Key conforming to the "user_agent.name"
	// semantic conventions. It represents the name of the user-agent extracted from
	// original. Usually refers to the browser's name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Safari", "YourApp"
	// Note: [Example] of extracting browser's name from original string. In the
	// case of using a user-agent for non-browser products, such as microservices
	// with multiple names/versions inside the `user_agent.original`, the most
	// significant name SHOULD be selected. In such a scenario it should align with
	// `user_agent.version`
	//
	// [Example]: https://www.whatsmyua.info
	UserAgentNameKey = attribute.Key("user_agent.name")

	// UserAgentOriginalKey is the attribute Key conforming to the
	// "user_agent.original" semantic conventions. It represents the value of the
	// [HTTP User-Agent] header sent by the client.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "CERN-LineMode/2.15 libwww/2.17b3", "Mozilla/5.0 (iPhone; CPU
	// iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)
	// Version/14.1.2 Mobile/15E148 Safari/604.1", "YourApp/1.0.0
	// grpc-java-okhttp/1.27.2"
	//
	// [HTTP User-Agent]: https://www.rfc-editor.org/rfc/rfc9110.html#field.user-agent
	UserAgentOriginalKey = attribute.Key("user_agent.original")

	// UserAgentOSNameKey is the attribute Key conforming to the
	// "user_agent.os.name" semantic conventions. It represents the human readable
	// operating system name.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "iOS", "Android", "Ubuntu"
	// Note: For mapping user agent strings to OS names, libraries such as
	// [ua-parser] can be utilized.
	//
	// [ua-parser]: https://github.com/ua-parser
	UserAgentOSNameKey = attribute.Key("user_agent.os.name")

	// UserAgentOSVersionKey is the attribute Key conforming to the
	// "user_agent.os.version" semantic conventions. It represents the version
	// string of the operating system as defined in [Version Attributes].
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "14.2.1", "18.04.1"
	// Note: For mapping user agent strings to OS versions, libraries such as
	// [ua-parser] can be utilized.
	//
	// [Version Attributes]: /docs/resource/README.md#version-attributes
	// [ua-parser]: https://github.com/ua-parser
	UserAgentOSVersionKey = attribute.Key("user_agent.os.version")

	// UserAgentSyntheticTypeKey is the attribute Key conforming to the
	// "user_agent.synthetic.type" semantic conventions. It represents the specifies
	// the category of synthetic traffic, such as tests or bots.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: This attribute MAY be derived from the contents of the
	// `user_agent.original` attribute. Components that populate the attribute are
	// responsible for determining what they consider to be synthetic bot or test
	// traffic. This attribute can either be set for self-identification purposes,
	// or on telemetry detected to be generated as a result of a synthetic request.
	// This attribute is useful for distinguishing between genuine client traffic
	// and synthetic traffic generated by bots or tests.
	UserAgentSyntheticTypeKey = attribute.Key("user_agent.synthetic.type")

	// UserAgentVersionKey is the attribute Key conforming to the
	// "user_agent.version" semantic conventions. It represents the version of the
	// user-agent extracted from original. Usually refers to the browser's version.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "14.1.2", "1.0.0"
	// Note: [Example] of extracting browser's version from original string. In the
	// case of using a user-agent for non-browser products, such as microservices
	// with multiple names/versions inside the `user_agent.original`, the most
	// significant version SHOULD be selected. In such a scenario it should align
	// with `user_agent.name`
	//
	// [Example]: https://www.whatsmyua.info
	UserAgentVersionKey = attribute.Key("user_agent.version")
)

Namespace: user_agent

View Source
const (
	// VCSChangeIDKey is the attribute Key conforming to the "vcs.change.id"
	// semantic conventions. It represents the ID of the change (pull request/merge
	// request/changelist) if applicable. This is usually a unique (within
	// repository) identifier generated by the VCS system.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "123"
	VCSChangeIDKey = attribute.Key("vcs.change.id")

	// VCSChangeStateKey is the attribute Key conforming to the "vcs.change.state"
	// semantic conventions. It represents the state of the change (pull
	// request/merge request/changelist).
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "open", "closed", "merged"
	VCSChangeStateKey = attribute.Key("vcs.change.state")

	// VCSChangeTitleKey is the attribute Key conforming to the "vcs.change.title"
	// semantic conventions. It represents the human readable title of the change
	// (pull request/merge request/changelist). This title is often a brief summary
	// of the change and may get merged in to a ref as the commit summary.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "Fixes broken thing", "feat: add my new feature", "[chore] update
	// dependency"
	VCSChangeTitleKey = attribute.Key("vcs.change.title")

	// VCSLineChangeTypeKey is the attribute Key conforming to the
	// "vcs.line_change.type" semantic conventions. It represents the type of line
	// change being measured on a branch or change.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "added", "removed"
	VCSLineChangeTypeKey = attribute.Key("vcs.line_change.type")

	// VCSRefBaseNameKey is the attribute Key conforming to the "vcs.ref.base.name"
	// semantic conventions. It represents the name of the [reference] such as
	// **branch** or **tag** in the repository.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-feature-branch", "tag-1-test"
	// Note: `base` refers to the starting point of a change. For example, `main`
	// would be the base reference of type branch if you've created a new
	// reference of type branch from it and created new commits.
	//
	// [reference]: https://git-scm.com/docs/gitglossary#def_ref
	VCSRefBaseNameKey = attribute.Key("vcs.ref.base.name")

	// VCSRefBaseRevisionKey is the attribute Key conforming to the
	// "vcs.ref.base.revision" semantic conventions. It represents the revision,
	// literally [revised version], The revision most often refers to a commit
	// object in Git, or a revision number in SVN.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "9d59409acf479dfa0df1aa568182e43e43df8bbe28d60fcf2bc52e30068802cc",
	// "main", "123", "HEAD"
	// Note: `base` refers to the starting point of a change. For example, `main`
	// would be the base reference of type branch if you've created a new
	// reference of type branch from it and created new commits. The
	// revision can be a full [hash value (see
	// glossary)],
	// of the recorded change to a ref within a repository pointing to a
	// commit [commit] object. It does
	// not necessarily have to be a hash; it can simply define a [revision
	// number]
	// which is an integer that is monotonically increasing. In cases where
	// it is identical to the `ref.base.name`, it SHOULD still be included.
	// It is up to the implementer to decide which value to set as the
	// revision based on the VCS system and situational context.
	//
	// [revised version]: https://www.merriam-webster.com/dictionary/revision
	// [hash value (see
	// glossary)]: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf
	// [commit]: https://git-scm.com/docs/git-commit
	// [revision
	// number]: https://svnbook.red-bean.com/en/1.7/svn.tour.revs.specifiers.html
	VCSRefBaseRevisionKey = attribute.Key("vcs.ref.base.revision")

	// VCSRefBaseTypeKey is the attribute Key conforming to the "vcs.ref.base.type"
	// semantic conventions. It represents the type of the [reference] in the
	// repository.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "branch", "tag"
	// Note: `base` refers to the starting point of a change. For example, `main`
	// would be the base reference of type branch if you've created a new
	// reference of type branch from it and created new commits.
	//
	// [reference]: https://git-scm.com/docs/gitglossary#def_ref
	VCSRefBaseTypeKey = attribute.Key("vcs.ref.base.type")

	// VCSRefHeadNameKey is the attribute Key conforming to the "vcs.ref.head.name"
	// semantic conventions. It represents the name of the [reference] such as
	// **branch** or **tag** in the repository.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "my-feature-branch", "tag-1-test"
	// Note: `head` refers to where you are right now; the current reference at a
	// given time.
	//
	// [reference]: https://git-scm.com/docs/gitglossary#def_ref
	VCSRefHeadNameKey = attribute.Key("vcs.ref.head.name")

	// VCSRefHeadRevisionKey is the attribute Key conforming to the
	// "vcs.ref.head.revision" semantic conventions. It represents the revision,
	// literally [revised version], The revision most often refers to a commit
	// object in Git, or a revision number in SVN.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "9d59409acf479dfa0df1aa568182e43e43df8bbe28d60fcf2bc52e30068802cc",
	// "main", "123", "HEAD"
	// Note: `head` refers to where you are right now; the current reference at a
	// given time.The revision can be a full [hash value (see
	// glossary)],
	// of the recorded change to a ref within a repository pointing to a
	// commit [commit] object. It does
	// not necessarily have to be a hash; it can simply define a [revision
	// number]
	// which is an integer that is monotonically increasing. In cases where
	// it is identical to the `ref.head.name`, it SHOULD still be included.
	// It is up to the implementer to decide which value to set as the
	// revision based on the VCS system and situational context.
	//
	// [revised version]: https://www.merriam-webster.com/dictionary/revision
	// [hash value (see
	// glossary)]: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf
	// [commit]: https://git-scm.com/docs/git-commit
	// [revision
	// number]: https://svnbook.red-bean.com/en/1.7/svn.tour.revs.specifiers.html
	VCSRefHeadRevisionKey = attribute.Key("vcs.ref.head.revision")

	// VCSRefHeadTypeKey is the attribute Key conforming to the "vcs.ref.head.type"
	// semantic conventions. It represents the type of the [reference] in the
	// repository.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "branch", "tag"
	// Note: `head` refers to where you are right now; the current reference at a
	// given time.
	//
	// [reference]: https://git-scm.com/docs/gitglossary#def_ref
	VCSRefHeadTypeKey = attribute.Key("vcs.ref.head.type")

	// VCSRefTypeKey is the attribute Key conforming to the "vcs.ref.type" semantic
	// conventions. It represents the type of the [reference] in the repository.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "branch", "tag"
	//
	// [reference]: https://git-scm.com/docs/gitglossary#def_ref
	VCSRefTypeKey = attribute.Key("vcs.ref.type")

	// VCSRepositoryNameKey is the attribute Key conforming to the
	// "vcs.repository.name" semantic conventions. It represents the human readable
	// name of the repository. It SHOULD NOT include any additional identifier like
	// Group/SubGroup in GitLab or organization in GitHub.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "semantic-conventions", "my-cool-repo"
	// Note: Due to it only being the name, it can clash with forks of the same
	// repository if collecting telemetry across multiple orgs or groups in
	// the same backends.
	VCSRepositoryNameKey = attribute.Key("vcs.repository.name")

	// VCSRepositoryURLFullKey is the attribute Key conforming to the
	// "vcs.repository.url.full" semantic conventions. It represents the
	// [canonical URL] of the repository providing the complete HTTP(S) address in
	// order to locate and identify the repository through a browser.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "https://github.com/opentelemetry/open-telemetry-collector-contrib",
	// "https://gitlab.com/my-org/my-project/my-projects-project/repo"
	// Note: In Git Version Control Systems, the canonical URL SHOULD NOT include
	// the `.git` extension.
	//
	// [canonical URL]: https://support.google.com/webmasters/answer/10347851?hl=en#:~:text=A%20canonical%20URL%20is%20the,Google%20chooses%20one%20as%20canonical.
	VCSRepositoryURLFullKey = attribute.Key("vcs.repository.url.full")

	// VCSRevisionDeltaDirectionKey is the attribute Key conforming to the
	// "vcs.revision_delta.direction" semantic conventions. It represents the type
	// of revision comparison.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "ahead", "behind"
	VCSRevisionDeltaDirectionKey = attribute.Key("vcs.revision_delta.direction")
)

Namespace: vcs

View Source
const (
	// WebEngineDescriptionKey is the attribute Key conforming to the
	// "webengine.description" semantic conventions. It represents the additional
	// description of the web engine (e.g. detailed version and edition
	// information).
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "WildFly Full 21.0.0.Final (WildFly Core 13.0.1.Final) -
	// 2.2.2.Final"
	WebEngineDescriptionKey = attribute.Key("webengine.description")

	// WebEngineNameKey is the attribute Key conforming to the "webengine.name"
	// semantic conventions. It represents the name of the web engine.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "WildFly"
	WebEngineNameKey = attribute.Key("webengine.name")

	// WebEngineVersionKey is the attribute Key conforming to the
	// "webengine.version" semantic conventions. It represents the version of the
	// web engine.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "21.0.0"
	WebEngineVersionKey = attribute.Key("webengine.version")
)

Namespace: webengine

View Source
const (
	// AzureCosmosDBClientActiveInstanceCount is the metric conforming to the
	// "azure.cosmosdb.client.active_instance.count" semantic conventions. It
	// represents the number of active client instances.
	// Instrument: updowncounter
	// Unit: {instance}
	// Stability: development
	AzureCosmosDBClientActiveInstanceCountName        = "azure.cosmosdb.client.active_instance.count"
	AzureCosmosDBClientActiveInstanceCountUnit        = "{instance}"
	AzureCosmosDBClientActiveInstanceCountDescription = "Number of active client instances"
	// AzureCosmosDBClientOperationRequestCharge is the metric conforming to the
	// "azure.cosmosdb.client.operation.request_charge" semantic conventions. It
	// represents the [Request units] consumed by the operation.
	//
	// [Request units]: https://learn.microsoft.com/azure/cosmos-db/request-units
	// Instrument: histogram
	// Unit: {request_unit}
	// Stability: development
	AzureCosmosDBClientOperationRequestChargeName        = "azure.cosmosdb.client.operation.request_charge"
	AzureCosmosDBClientOperationRequestChargeUnit        = "{request_unit}"
	AzureCosmosDBClientOperationRequestChargeDescription = "[Request units](https://learn.microsoft.com/azure/cosmos-db/request-units) consumed by the operation"
	// CICDPipelineRunActive is the metric conforming to the
	// "cicd.pipeline.run.active" semantic conventions. It represents the number of
	// pipeline runs currently active in the system by state.
	// Instrument: updowncounter
	// Unit: {run}
	// Stability: development
	CICDPipelineRunActiveName        = "cicd.pipeline.run.active"
	CICDPipelineRunActiveUnit        = "{run}"
	CICDPipelineRunActiveDescription = "The number of pipeline runs currently active in the system by state."
	// CICDPipelineRunDuration is the metric conforming to the
	// "cicd.pipeline.run.duration" semantic conventions. It represents the
	// duration of a pipeline run grouped by pipeline, state and result.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	CICDPipelineRunDurationName        = "cicd.pipeline.run.duration"
	CICDPipelineRunDurationUnit        = "s"
	CICDPipelineRunDurationDescription = "Duration of a pipeline run grouped by pipeline, state and result."
	// CICDPipelineRunErrors is the metric conforming to the
	// "cicd.pipeline.run.errors" semantic conventions. It represents the number of
	// errors encountered in pipeline runs (eg. compile, test failures).
	// Instrument: counter
	// Unit: {error}
	// Stability: development
	CICDPipelineRunErrorsName        = "cicd.pipeline.run.errors"
	CICDPipelineRunErrorsUnit        = "{error}"
	CICDPipelineRunErrorsDescription = "The number of errors encountered in pipeline runs (eg. compile, test failures)."
	// CICDSystemErrors is the metric conforming to the "cicd.system.errors"
	// semantic conventions. It represents the number of errors in a component of
	// the CICD system (eg. controller, scheduler, agent).
	// Instrument: counter
	// Unit: {error}
	// Stability: development
	CICDSystemErrorsName        = "cicd.system.errors"
	CICDSystemErrorsUnit        = "{error}"
	CICDSystemErrorsDescription = "The number of errors in a component of the CICD system (eg. controller, scheduler, agent)."
	// CICDWorkerCount is the metric conforming to the "cicd.worker.count" semantic
	// conventions. It represents the number of workers on the CICD system by
	// state.
	// Instrument: updowncounter
	// Unit: {count}
	// Stability: development
	CICDWorkerCountName        = "cicd.worker.count"
	CICDWorkerCountUnit        = "{count}"
	CICDWorkerCountDescription = "The number of workers on the CICD system by state."
	// ContainerCPUTime is the metric conforming to the "container.cpu.time"
	// semantic conventions. It represents the total CPU time consumed.
	// Instrument: counter
	// Unit: s
	// Stability: development
	ContainerCPUTimeName        = "container.cpu.time"
	ContainerCPUTimeUnit        = "s"
	ContainerCPUTimeDescription = "Total CPU time consumed"
	// ContainerCPUUsage is the metric conforming to the "container.cpu.usage"
	// semantic conventions. It represents the container's CPU usage, measured in
	// cpus. Range from 0 to the number of allocatable CPUs.
	// Instrument: gauge
	// Unit: {cpu}
	// Stability: development
	ContainerCPUUsageName        = "container.cpu.usage"
	ContainerCPUUsageUnit        = "{cpu}"
	ContainerCPUUsageDescription = "Container's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs"
	// ContainerDiskIo is the metric conforming to the "container.disk.io" semantic
	// conventions. It represents the disk bytes for the container.
	// Instrument: counter
	// Unit: By
	// Stability: development
	ContainerDiskIoName        = "container.disk.io"
	ContainerDiskIoUnit        = "By"
	ContainerDiskIoDescription = "Disk bytes for the container."
	// ContainerMemoryUsage is the metric conforming to the
	// "container.memory.usage" semantic conventions. It represents the memory
	// usage of the container.
	// Instrument: counter
	// Unit: By
	// Stability: development
	ContainerMemoryUsageName        = "container.memory.usage"
	ContainerMemoryUsageUnit        = "By"
	ContainerMemoryUsageDescription = "Memory usage of the container."
	// ContainerNetworkIo is the metric conforming to the "container.network.io"
	// semantic conventions. It represents the network bytes for the container.
	// Instrument: counter
	// Unit: By
	// Stability: development
	ContainerNetworkIoName        = "container.network.io"
	ContainerNetworkIoUnit        = "By"
	ContainerNetworkIoDescription = "Network bytes for the container."
	// ContainerUptime is the metric conforming to the "container.uptime" semantic
	// conventions. It represents the time the container has been running.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	ContainerUptimeName        = "container.uptime"
	ContainerUptimeUnit        = "s"
	ContainerUptimeDescription = "The time the container has been running"
	// CPUFrequency is the metric conforming to the "cpu.frequency" semantic
	// conventions. It represents the operating frequency of the logical CPU in
	// Hertz.
	// Instrument: gauge
	// Unit: Hz
	// Stability: development
	CPUFrequencyName        = "cpu.frequency"
	CPUFrequencyUnit        = "Hz"
	CPUFrequencyDescription = "Operating frequency of the logical CPU in Hertz."
	// CPUTime is the metric conforming to the "cpu.time" semantic conventions. It
	// represents the seconds each logical CPU spent on each mode.
	// Instrument: counter
	// Unit: s
	// Stability: development
	CPUTimeName        = "cpu.time"
	CPUTimeUnit        = "s"
	CPUTimeDescription = "Seconds each logical CPU spent on each mode"
	// CPUUtilization is the metric conforming to the "cpu.utilization" semantic
	// conventions. It represents the for each logical CPU, the utilization is
	// calculated as the change in cumulative CPU time (cpu.time) over a
	// measurement interval, divided by the elapsed time.
	// Instrument: gauge
	// Unit: 1
	// Stability: development
	CPUUtilizationName        = "cpu.utilization"
	CPUUtilizationUnit        = "1"
	CPUUtilizationDescription = "" /* 157-byte string literal not displayed */
	// DBClientConnectionCount is the metric conforming to the
	// "db.client.connection.count" semantic conventions. It represents the number
	// of connections that are currently in state described by the `state`
	// attribute.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: development
	DBClientConnectionCountName        = "db.client.connection.count"
	DBClientConnectionCountUnit        = "{connection}"
	DBClientConnectionCountDescription = "The number of connections that are currently in state described by the `state` attribute"
	// DBClientConnectionCreateTime is the metric conforming to the
	// "db.client.connection.create_time" semantic conventions. It represents the
	// time it took to create a new connection.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	DBClientConnectionCreateTimeName        = "db.client.connection.create_time"
	DBClientConnectionCreateTimeUnit        = "s"
	DBClientConnectionCreateTimeDescription = "The time it took to create a new connection"
	// DBClientConnectionIdleMax is the metric conforming to the
	// "db.client.connection.idle.max" semantic conventions. It represents the
	// maximum number of idle open connections allowed.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: development
	DBClientConnectionIdleMaxName        = "db.client.connection.idle.max"
	DBClientConnectionIdleMaxUnit        = "{connection}"
	DBClientConnectionIdleMaxDescription = "The maximum number of idle open connections allowed"
	// DBClientConnectionIdleMin is the metric conforming to the
	// "db.client.connection.idle.min" semantic conventions. It represents the
	// minimum number of idle open connections allowed.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: development
	DBClientConnectionIdleMinName        = "db.client.connection.idle.min"
	DBClientConnectionIdleMinUnit        = "{connection}"
	DBClientConnectionIdleMinDescription = "The minimum number of idle open connections allowed"
	// DBClientConnectionMax is the metric conforming to the
	// "db.client.connection.max" semantic conventions. It represents the maximum
	// number of open connections allowed.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: development
	DBClientConnectionMaxName        = "db.client.connection.max"
	DBClientConnectionMaxUnit        = "{connection}"
	DBClientConnectionMaxDescription = "The maximum number of open connections allowed"
	// DBClientConnectionPendingRequests is the metric conforming to the
	// "db.client.connection.pending_requests" semantic conventions. It represents
	// the number of current pending requests for an open connection.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: development
	DBClientConnectionPendingRequestsName        = "db.client.connection.pending_requests"
	DBClientConnectionPendingRequestsUnit        = "{request}"
	DBClientConnectionPendingRequestsDescription = "The number of current pending requests for an open connection"
	// DBClientConnectionTimeouts is the metric conforming to the
	// "db.client.connection.timeouts" semantic conventions. It represents the
	// number of connection timeouts that have occurred trying to obtain a
	// connection from the pool.
	// Instrument: counter
	// Unit: {timeout}
	// Stability: development
	DBClientConnectionTimeoutsName        = "db.client.connection.timeouts"
	DBClientConnectionTimeoutsUnit        = "{timeout}"
	DBClientConnectionTimeoutsDescription = "The number of connection timeouts that have occurred trying to obtain a connection from the pool"
	// DBClientConnectionUseTime is the metric conforming to the
	// "db.client.connection.use_time" semantic conventions. It represents the time
	// between borrowing a connection and returning it to the pool.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	DBClientConnectionUseTimeName        = "db.client.connection.use_time"
	DBClientConnectionUseTimeUnit        = "s"
	DBClientConnectionUseTimeDescription = "The time between borrowing a connection and returning it to the pool"
	// DBClientConnectionWaitTime is the metric conforming to the
	// "db.client.connection.wait_time" semantic conventions. It represents the
	// time it took to obtain an open connection from the pool.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	DBClientConnectionWaitTimeName        = "db.client.connection.wait_time"
	DBClientConnectionWaitTimeUnit        = "s"
	DBClientConnectionWaitTimeDescription = "The time it took to obtain an open connection from the pool"
	// DBClientOperationDuration is the metric conforming to the
	// "db.client.operation.duration" semantic conventions. It represents the
	// duration of database client operations.
	// Instrument: histogram
	// Unit: s
	// Stability: release_candidate
	DBClientOperationDurationName        = "db.client.operation.duration"
	DBClientOperationDurationUnit        = "s"
	DBClientOperationDurationDescription = "Duration of database client operations."
	// DBClientResponseReturnedRows is the metric conforming to the
	// "db.client.response.returned_rows" semantic conventions. It represents the
	// actual number of records returned by the database operation.
	// Instrument: histogram
	// Unit: {row}
	// Stability: development
	DBClientResponseReturnedRowsName        = "db.client.response.returned_rows"
	DBClientResponseReturnedRowsUnit        = "{row}"
	DBClientResponseReturnedRowsDescription = "The actual number of records returned by the database operation."
	// DNSLookupDuration is the metric conforming to the "dns.lookup.duration"
	// semantic conventions. It represents the measures the time taken to perform a
	// DNS lookup.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	DNSLookupDurationName        = "dns.lookup.duration"
	DNSLookupDurationUnit        = "s"
	DNSLookupDurationDescription = "Measures the time taken to perform a DNS lookup."
	// FaaSColdstarts is the metric conforming to the "faas.coldstarts" semantic
	// conventions. It represents the number of invocation cold starts.
	// Instrument: counter
	// Unit: {coldstart}
	// Stability: development
	FaaSColdstartsName        = "faas.coldstarts"
	FaaSColdstartsUnit        = "{coldstart}"
	FaaSColdstartsDescription = "Number of invocation cold starts"
	// FaaSCPUUsage is the metric conforming to the "faas.cpu_usage" semantic
	// conventions. It represents the distribution of CPU usage per invocation.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	FaaSCPUUsageName        = "faas.cpu_usage"
	FaaSCPUUsageUnit        = "s"
	FaaSCPUUsageDescription = "Distribution of CPU usage per invocation"
	// FaaSErrors is the metric conforming to the "faas.errors" semantic
	// conventions. It represents the number of invocation errors.
	// Instrument: counter
	// Unit: {error}
	// Stability: development
	FaaSErrorsName        = "faas.errors"
	FaaSErrorsUnit        = "{error}"
	FaaSErrorsDescription = "Number of invocation errors"
	// FaaSInitDuration is the metric conforming to the "faas.init_duration"
	// semantic conventions. It represents the measures the duration of the
	// function's initialization, such as a cold start.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	FaaSInitDurationName        = "faas.init_duration"
	FaaSInitDurationUnit        = "s"
	FaaSInitDurationDescription = "Measures the duration of the function's initialization, such as a cold start"
	// FaaSInvocations is the metric conforming to the "faas.invocations" semantic
	// conventions. It represents the number of successful invocations.
	// Instrument: counter
	// Unit: {invocation}
	// Stability: development
	FaaSInvocationsName        = "faas.invocations"
	FaaSInvocationsUnit        = "{invocation}"
	FaaSInvocationsDescription = "Number of successful invocations"
	// FaaSInvokeDuration is the metric conforming to the "faas.invoke_duration"
	// semantic conventions. It represents the measures the duration of the
	// function's logic execution.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	FaaSInvokeDurationName        = "faas.invoke_duration"
	FaaSInvokeDurationUnit        = "s"
	FaaSInvokeDurationDescription = "Measures the duration of the function's logic execution"
	// FaaSMemUsage is the metric conforming to the "faas.mem_usage" semantic
	// conventions. It represents the distribution of max memory usage per
	// invocation.
	// Instrument: histogram
	// Unit: By
	// Stability: development
	FaaSMemUsageName        = "faas.mem_usage"
	FaaSMemUsageUnit        = "By"
	FaaSMemUsageDescription = "Distribution of max memory usage per invocation"
	// FaaSNetIo is the metric conforming to the "faas.net_io" semantic
	// conventions. It represents the distribution of net I/O usage per invocation.
	// Instrument: histogram
	// Unit: By
	// Stability: development
	FaaSNetIoName        = "faas.net_io"
	FaaSNetIoUnit        = "By"
	FaaSNetIoDescription = "Distribution of net I/O usage per invocation"
	// FaaSTimeouts is the metric conforming to the "faas.timeouts" semantic
	// conventions. It represents the number of invocation timeouts.
	// Instrument: counter
	// Unit: {timeout}
	// Stability: development
	FaaSTimeoutsName        = "faas.timeouts"
	FaaSTimeoutsUnit        = "{timeout}"
	FaaSTimeoutsDescription = "Number of invocation timeouts"
	// GenAIClientOperationDuration is the metric conforming to the
	// "gen_ai.client.operation.duration" semantic conventions. It represents the
	// genAI operation duration.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	GenAIClientOperationDurationName        = "gen_ai.client.operation.duration"
	GenAIClientOperationDurationUnit        = "s"
	GenAIClientOperationDurationDescription = "GenAI operation duration"
	// GenAIClientTokenUsage is the metric conforming to the
	// "gen_ai.client.token.usage" semantic conventions. It represents the measures
	// number of input and output tokens used.
	// Instrument: histogram
	// Unit: {token}
	// Stability: development
	GenAIClientTokenUsageName        = "gen_ai.client.token.usage"
	GenAIClientTokenUsageUnit        = "{token}"
	GenAIClientTokenUsageDescription = "Measures number of input and output tokens used"
	// GenAIServerRequestDuration is the metric conforming to the
	// "gen_ai.server.request.duration" semantic conventions. It represents the
	// generative AI server request duration such as time-to-last byte or last
	// output token.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	GenAIServerRequestDurationName        = "gen_ai.server.request.duration"
	GenAIServerRequestDurationUnit        = "s"
	GenAIServerRequestDurationDescription = "Generative AI server request duration such as time-to-last byte or last output token"
	// GenAIServerTimePerOutputToken is the metric conforming to the
	// "gen_ai.server.time_per_output_token" semantic conventions. It represents
	// the time per output token generated after the first token for successful
	// responses.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	GenAIServerTimePerOutputTokenName        = "gen_ai.server.time_per_output_token"
	GenAIServerTimePerOutputTokenUnit        = "s"
	GenAIServerTimePerOutputTokenDescription = "Time per output token generated after the first token for successful responses"
	// GenAIServerTimeToFirstToken is the metric conforming to the
	// "gen_ai.server.time_to_first_token" semantic conventions. It represents the
	// time to generate first token for successful responses.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	GenAIServerTimeToFirstTokenName        = "gen_ai.server.time_to_first_token"
	GenAIServerTimeToFirstTokenUnit        = "s"
	GenAIServerTimeToFirstTokenDescription = "Time to generate first token for successful responses"
	// GoConfigGogc is the metric conforming to the "go.config.gogc" semantic
	// conventions. It represents the heap size target percentage configured by the
	// user, otherwise 100.
	// Instrument: updowncounter
	// Unit: %
	// Stability: development
	GoConfigGogcName        = "go.config.gogc"
	GoConfigGogcUnit        = "%"
	GoConfigGogcDescription = "Heap size target percentage configured by the user, otherwise 100."
	// GoGoroutineCount is the metric conforming to the "go.goroutine.count"
	// semantic conventions. It represents the count of live goroutines.
	// Instrument: updowncounter
	// Unit: {goroutine}
	// Stability: development
	GoGoroutineCountName        = "go.goroutine.count"
	GoGoroutineCountUnit        = "{goroutine}"
	GoGoroutineCountDescription = "Count of live goroutines."
	// GoMemoryAllocated is the metric conforming to the "go.memory.allocated"
	// semantic conventions. It represents the memory allocated to the heap by the
	// application.
	// Instrument: counter
	// Unit: By
	// Stability: development
	GoMemoryAllocatedName        = "go.memory.allocated"
	GoMemoryAllocatedUnit        = "By"
	GoMemoryAllocatedDescription = "Memory allocated to the heap by the application."
	// GoMemoryAllocations is the metric conforming to the "go.memory.allocations"
	// semantic conventions. It represents the count of allocations to the heap by
	// the application.
	// Instrument: counter
	// Unit: {allocation}
	// Stability: development
	GoMemoryAllocationsName        = "go.memory.allocations"
	GoMemoryAllocationsUnit        = "{allocation}"
	GoMemoryAllocationsDescription = "Count of allocations to the heap by the application."
	// GoMemoryGCGoal is the metric conforming to the "go.memory.gc.goal" semantic
	// conventions. It represents the heap size target for the end of the GC cycle.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	GoMemoryGCGoalName        = "go.memory.gc.goal"
	GoMemoryGCGoalUnit        = "By"
	GoMemoryGCGoalDescription = "Heap size target for the end of the GC cycle."
	// GoMemoryLimit is the metric conforming to the "go.memory.limit" semantic
	// conventions. It represents the go runtime memory limit configured by the
	// user, if a limit exists.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	GoMemoryLimitName        = "go.memory.limit"
	GoMemoryLimitUnit        = "By"
	GoMemoryLimitDescription = "Go runtime memory limit configured by the user, if a limit exists."
	// GoMemoryUsed is the metric conforming to the "go.memory.used" semantic
	// conventions. It represents the memory used by the Go runtime.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	GoMemoryUsedName        = "go.memory.used"
	GoMemoryUsedUnit        = "By"
	GoMemoryUsedDescription = "Memory used by the Go runtime."
	// GoProcessorLimit is the metric conforming to the "go.processor.limit"
	// semantic conventions. It represents the number of OS threads that can
	// execute user-level Go code simultaneously.
	// Instrument: updowncounter
	// Unit: {thread}
	// Stability: development
	GoProcessorLimitName        = "go.processor.limit"
	GoProcessorLimitUnit        = "{thread}"
	GoProcessorLimitDescription = "The number of OS threads that can execute user-level Go code simultaneously."
	// GoScheduleDuration is the metric conforming to the "go.schedule.duration"
	// semantic conventions. It represents the time goroutines have spent in the
	// scheduler in a runnable state before actually running.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	GoScheduleDurationName        = "go.schedule.duration"
	GoScheduleDurationUnit        = "s"
	GoScheduleDurationDescription = "The time goroutines have spent in the scheduler in a runnable state before actually running."
	// HTTPClientActiveRequests is the metric conforming to the
	// "http.client.active_requests" semantic conventions. It represents the number
	// of active HTTP requests.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: development
	HTTPClientActiveRequestsName        = "http.client.active_requests"
	HTTPClientActiveRequestsUnit        = "{request}"
	HTTPClientActiveRequestsDescription = "Number of active HTTP requests."
	// HTTPClientConnectionDuration is the metric conforming to the
	// "http.client.connection.duration" semantic conventions. It represents the
	// duration of the successfully established outbound HTTP connections.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	HTTPClientConnectionDurationName        = "http.client.connection.duration"
	HTTPClientConnectionDurationUnit        = "s"
	HTTPClientConnectionDurationDescription = "The duration of the successfully established outbound HTTP connections."
	// HTTPClientOpenConnections is the metric conforming to the
	// "http.client.open_connections" semantic conventions. It represents the
	// number of outbound HTTP connections that are currently active or idle on the
	// client.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: development
	HTTPClientOpenConnectionsName        = "http.client.open_connections"
	HTTPClientOpenConnectionsUnit        = "{connection}"
	HTTPClientOpenConnectionsDescription = "Number of outbound HTTP connections that are currently active or idle on the client."
	// HTTPClientRequestBodySize is the metric conforming to the
	// "http.client.request.body.size" semantic conventions. It represents the size
	// of HTTP client request bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: development
	HTTPClientRequestBodySizeName        = "http.client.request.body.size"
	HTTPClientRequestBodySizeUnit        = "By"
	HTTPClientRequestBodySizeDescription = "Size of HTTP client request bodies."
	// HTTPClientRequestDuration is the metric conforming to the
	// "http.client.request.duration" semantic conventions. It represents the
	// duration of HTTP client requests.
	// Instrument: histogram
	// Unit: s
	// Stability: stable
	HTTPClientRequestDurationName        = "http.client.request.duration"
	HTTPClientRequestDurationUnit        = "s"
	HTTPClientRequestDurationDescription = "Duration of HTTP client requests."
	// HTTPClientResponseBodySize is the metric conforming to the
	// "http.client.response.body.size" semantic conventions. It represents the
	// size of HTTP client response bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: development
	HTTPClientResponseBodySizeName        = "http.client.response.body.size"
	HTTPClientResponseBodySizeUnit        = "By"
	HTTPClientResponseBodySizeDescription = "Size of HTTP client response bodies."
	// HTTPServerActiveRequests is the metric conforming to the
	// "http.server.active_requests" semantic conventions. It represents the number
	// of active HTTP server requests.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: development
	HTTPServerActiveRequestsName        = "http.server.active_requests"
	HTTPServerActiveRequestsUnit        = "{request}"
	HTTPServerActiveRequestsDescription = "Number of active HTTP server requests."
	// HTTPServerRequestBodySize is the metric conforming to the
	// "http.server.request.body.size" semantic conventions. It represents the size
	// of HTTP server request bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: development
	HTTPServerRequestBodySizeName        = "http.server.request.body.size"
	HTTPServerRequestBodySizeUnit        = "By"
	HTTPServerRequestBodySizeDescription = "Size of HTTP server request bodies."
	// HTTPServerRequestDuration is the metric conforming to the
	// "http.server.request.duration" semantic conventions. It represents the
	// duration of HTTP server requests.
	// Instrument: histogram
	// Unit: s
	// Stability: stable
	HTTPServerRequestDurationName        = "http.server.request.duration"
	HTTPServerRequestDurationUnit        = "s"
	HTTPServerRequestDurationDescription = "Duration of HTTP server requests."
	// HTTPServerResponseBodySize is the metric conforming to the
	// "http.server.response.body.size" semantic conventions. It represents the
	// size of HTTP server response bodies.
	// Instrument: histogram
	// Unit: By
	// Stability: development
	HTTPServerResponseBodySizeName        = "http.server.response.body.size"
	HTTPServerResponseBodySizeUnit        = "By"
	HTTPServerResponseBodySizeDescription = "Size of HTTP server response bodies."
	// HwEnergy is the metric conforming to the "hw.energy" semantic conventions.
	// It represents the energy consumed by the component.
	// Instrument: counter
	// Unit: J
	// Stability: development
	HwEnergyName        = "hw.energy"
	HwEnergyUnit        = "J"
	HwEnergyDescription = "Energy consumed by the component"
	// HwErrors is the metric conforming to the "hw.errors" semantic conventions.
	// It represents the number of errors encountered by the component.
	// Instrument: counter
	// Unit: {error}
	// Stability: development
	HwErrorsName        = "hw.errors"
	HwErrorsUnit        = "{error}"
	HwErrorsDescription = "Number of errors encountered by the component"
	// HwHostAmbientTemperature is the metric conforming to the
	// "hw.host.ambient_temperature" semantic conventions. It represents the
	// ambient (external) temperature of the physical host.
	// Instrument: gauge
	// Unit: Cel
	// Stability: development
	HwHostAmbientTemperatureName        = "hw.host.ambient_temperature"
	HwHostAmbientTemperatureUnit        = "Cel"
	HwHostAmbientTemperatureDescription = "Ambient (external) temperature of the physical host"
	// HwHostEnergy is the metric conforming to the "hw.host.energy" semantic
	// conventions. It represents the total energy consumed by the entire physical
	// host, in joules.
	// Instrument: counter
	// Unit: J
	// Stability: development
	HwHostEnergyName        = "hw.host.energy"
	HwHostEnergyUnit        = "J"
	HwHostEnergyDescription = "Total energy consumed by the entire physical host, in joules"
	// HwHostHeatingMargin is the metric conforming to the "hw.host.heating_margin"
	// semantic conventions. It represents the by how many degrees Celsius the
	// temperature of the physical host can be increased, before reaching a warning
	// threshold on one of the internal sensors.
	// Instrument: gauge
	// Unit: Cel
	// Stability: development
	HwHostHeatingMarginName        = "hw.host.heating_margin"
	HwHostHeatingMarginUnit        = "Cel"
	HwHostHeatingMarginDescription = "" /* 149-byte string literal not displayed */
	// HwHostPower is the metric conforming to the "hw.host.power" semantic
	// conventions. It represents the instantaneous power consumed by the entire
	// physical host in Watts (`hw.host.energy` is preferred).
	// Instrument: gauge
	// Unit: W
	// Stability: development
	HwHostPowerName        = "hw.host.power"
	HwHostPowerUnit        = "W"
	HwHostPowerDescription = "Instantaneous power consumed by the entire physical host in Watts (`hw.host.energy` is preferred)"
	// HwPower is the metric conforming to the "hw.power" semantic conventions. It
	// represents the instantaneous power consumed by the component.
	// Instrument: gauge
	// Unit: W
	// Stability: development
	HwPowerName        = "hw.power"
	HwPowerUnit        = "W"
	HwPowerDescription = "Instantaneous power consumed by the component"
	// HwStatus is the metric conforming to the "hw.status" semantic conventions.
	// It represents the operational status: `1` (true) or `0` (false) for each of
	// the possible states.
	// Instrument: updowncounter
	// Unit: 1
	// Stability: development
	HwStatusName        = "hw.status"
	HwStatusUnit        = "1"
	HwStatusDescription = "Operational status: `1` (true) or `0` (false) for each of the possible states"
	// K8SCronJobActiveJobs is the metric conforming to the
	// "k8s.cronjob.active_jobs" semantic conventions. It represents the number of
	// actively running jobs for a cronjob.
	// Instrument: updowncounter
	// Unit: {job}
	// Stability: development
	K8SCronJobActiveJobsName        = "k8s.cronjob.active_jobs"
	K8SCronJobActiveJobsUnit        = "{job}"
	K8SCronJobActiveJobsDescription = "The number of actively running jobs for a cronjob"
	// K8SDaemonSetCurrentScheduledNodes is the metric conforming to the
	// "k8s.daemonset.current_scheduled_nodes" semantic conventions. It represents
	// the number of nodes that are running at least 1 daemon pod and are supposed
	// to run the daemon pod.
	// Instrument: updowncounter
	// Unit: {node}
	// Stability: development
	K8SDaemonSetCurrentScheduledNodesName        = "k8s.daemonset.current_scheduled_nodes"
	K8SDaemonSetCurrentScheduledNodesUnit        = "{node}"
	K8SDaemonSetCurrentScheduledNodesDescription = "Number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod"
	// K8SDaemonSetDesiredScheduledNodes is the metric conforming to the
	// "k8s.daemonset.desired_scheduled_nodes" semantic conventions. It represents
	// the number of nodes that should be running the daemon pod (including nodes
	// currently running the daemon pod).
	// Instrument: updowncounter
	// Unit: {node}
	// Stability: development
	K8SDaemonSetDesiredScheduledNodesName        = "k8s.daemonset.desired_scheduled_nodes"
	K8SDaemonSetDesiredScheduledNodesUnit        = "{node}"
	K8SDaemonSetDesiredScheduledNodesDescription = "Number of nodes that should be running the daemon pod (including nodes currently running the daemon pod)"
	// K8SDaemonSetMisscheduledNodes is the metric conforming to the
	// "k8s.daemonset.misscheduled_nodes" semantic conventions. It represents the
	// number of nodes that are running the daemon pod, but are not supposed to run
	// the daemon pod.
	// Instrument: updowncounter
	// Unit: {node}
	// Stability: development
	K8SDaemonSetMisscheduledNodesName        = "k8s.daemonset.misscheduled_nodes"
	K8SDaemonSetMisscheduledNodesUnit        = "{node}"
	K8SDaemonSetMisscheduledNodesDescription = "Number of nodes that are running the daemon pod, but are not supposed to run the daemon pod"
	// K8SDaemonSetReadyNodes is the metric conforming to the
	// "k8s.daemonset.ready_nodes" semantic conventions. It represents the number
	// of nodes that should be running the daemon pod and have one or more of the
	// daemon pod running and ready.
	// Instrument: updowncounter
	// Unit: {node}
	// Stability: development
	K8SDaemonSetReadyNodesName        = "k8s.daemonset.ready_nodes"
	K8SDaemonSetReadyNodesUnit        = "{node}"
	K8SDaemonSetReadyNodesDescription = "Number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready"
	// K8SDeploymentAvailablePods is the metric conforming to the
	// "k8s.deployment.available_pods" semantic conventions. It represents the
	// total number of available replica pods (ready for at least minReadySeconds)
	// targeted by this deployment.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SDeploymentAvailablePodsName        = "k8s.deployment.available_pods"
	K8SDeploymentAvailablePodsUnit        = "{pod}"
	K8SDeploymentAvailablePodsDescription = "Total number of available replica pods (ready for at least minReadySeconds) targeted by this deployment"
	// K8SDeploymentDesiredPods is the metric conforming to the
	// "k8s.deployment.desired_pods" semantic conventions. It represents the number
	// of desired replica pods in this deployment.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SDeploymentDesiredPodsName        = "k8s.deployment.desired_pods"
	K8SDeploymentDesiredPodsUnit        = "{pod}"
	K8SDeploymentDesiredPodsDescription = "Number of desired replica pods in this deployment"
	// K8SHpaCurrentPods is the metric conforming to the "k8s.hpa.current_pods"
	// semantic conventions. It represents the current number of replica pods
	// managed by this horizontal pod autoscaler, as last seen by the autoscaler.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SHpaCurrentPodsName        = "k8s.hpa.current_pods"
	K8SHpaCurrentPodsUnit        = "{pod}"
	K8SHpaCurrentPodsDescription = "Current number of replica pods managed by this horizontal pod autoscaler, as last seen by the autoscaler"
	// K8SHpaDesiredPods is the metric conforming to the "k8s.hpa.desired_pods"
	// semantic conventions. It represents the desired number of replica pods
	// managed by this horizontal pod autoscaler, as last calculated by the
	// autoscaler.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SHpaDesiredPodsName        = "k8s.hpa.desired_pods"
	K8SHpaDesiredPodsUnit        = "{pod}"
	K8SHpaDesiredPodsDescription = "Desired number of replica pods managed by this horizontal pod autoscaler, as last calculated by the autoscaler"
	// K8SHpaMaxPods is the metric conforming to the "k8s.hpa.max_pods" semantic
	// conventions. It represents the upper limit for the number of replica pods to
	// which the autoscaler can scale up.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SHpaMaxPodsName        = "k8s.hpa.max_pods"
	K8SHpaMaxPodsUnit        = "{pod}"
	K8SHpaMaxPodsDescription = "The upper limit for the number of replica pods to which the autoscaler can scale up"
	// K8SHpaMinPods is the metric conforming to the "k8s.hpa.min_pods" semantic
	// conventions. It represents the lower limit for the number of replica pods to
	// which the autoscaler can scale down.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SHpaMinPodsName        = "k8s.hpa.min_pods"
	K8SHpaMinPodsUnit        = "{pod}"
	K8SHpaMinPodsDescription = "The lower limit for the number of replica pods to which the autoscaler can scale down"
	// K8SJobActivePods is the metric conforming to the "k8s.job.active_pods"
	// semantic conventions. It represents the number of pending and actively
	// running pods for a job.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SJobActivePodsName        = "k8s.job.active_pods"
	K8SJobActivePodsUnit        = "{pod}"
	K8SJobActivePodsDescription = "The number of pending and actively running pods for a job"
	// K8SJobDesiredSuccessfulPods is the metric conforming to the
	// "k8s.job.desired_successful_pods" semantic conventions. It represents the
	// desired number of successfully finished pods the job should be run with.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SJobDesiredSuccessfulPodsName        = "k8s.job.desired_successful_pods"
	K8SJobDesiredSuccessfulPodsUnit        = "{pod}"
	K8SJobDesiredSuccessfulPodsDescription = "The desired number of successfully finished pods the job should be run with"
	// K8SJobFailedPods is the metric conforming to the "k8s.job.failed_pods"
	// semantic conventions. It represents the number of pods which reached phase
	// Failed for a job.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SJobFailedPodsName        = "k8s.job.failed_pods"
	K8SJobFailedPodsUnit        = "{pod}"
	K8SJobFailedPodsDescription = "The number of pods which reached phase Failed for a job"
	// K8SJobMaxParallelPods is the metric conforming to the
	// "k8s.job.max_parallel_pods" semantic conventions. It represents the max
	// desired number of pods the job should run at any given time.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SJobMaxParallelPodsName        = "k8s.job.max_parallel_pods"
	K8SJobMaxParallelPodsUnit        = "{pod}"
	K8SJobMaxParallelPodsDescription = "The max desired number of pods the job should run at any given time"
	// K8SJobSuccessfulPods is the metric conforming to the
	// "k8s.job.successful_pods" semantic conventions. It represents the number of
	// pods which reached phase Succeeded for a job.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SJobSuccessfulPodsName        = "k8s.job.successful_pods"
	K8SJobSuccessfulPodsUnit        = "{pod}"
	K8SJobSuccessfulPodsDescription = "The number of pods which reached phase Succeeded for a job"
	// K8SNamespacePhase is the metric conforming to the "k8s.namespace.phase"
	// semantic conventions. It represents the describes number of K8s namespaces
	// that are currently in a given phase.
	// Instrument: updowncounter
	// Unit: {namespace}
	// Stability: development
	K8SNamespacePhaseName        = "k8s.namespace.phase"
	K8SNamespacePhaseUnit        = "{namespace}"
	K8SNamespacePhaseDescription = "Describes number of K8s namespaces that are currently in a given phase."
	// K8SNodeCPUTime is the metric conforming to the "k8s.node.cpu.time" semantic
	// conventions. It represents the total CPU time consumed.
	// Instrument: counter
	// Unit: s
	// Stability: development
	K8SNodeCPUTimeName        = "k8s.node.cpu.time"
	K8SNodeCPUTimeUnit        = "s"
	K8SNodeCPUTimeDescription = "Total CPU time consumed"
	// K8SNodeCPUUsage is the metric conforming to the "k8s.node.cpu.usage"
	// semantic conventions. It represents the node's CPU usage, measured in cpus.
	// Range from 0 to the number of allocatable CPUs.
	// Instrument: gauge
	// Unit: {cpu}
	// Stability: development
	K8SNodeCPUUsageName        = "k8s.node.cpu.usage"
	K8SNodeCPUUsageUnit        = "{cpu}"
	K8SNodeCPUUsageDescription = "Node's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs"
	// K8SNodeMemoryUsage is the metric conforming to the "k8s.node.memory.usage"
	// semantic conventions. It represents the memory usage of the Node.
	// Instrument: gauge
	// Unit: By
	// Stability: development
	K8SNodeMemoryUsageName        = "k8s.node.memory.usage"
	K8SNodeMemoryUsageUnit        = "By"
	K8SNodeMemoryUsageDescription = "Memory usage of the Node"
	// K8SNodeNetworkErrors is the metric conforming to the
	// "k8s.node.network.errors" semantic conventions. It represents the node
	// network errors.
	// Instrument: counter
	// Unit: {error}
	// Stability: development
	K8SNodeNetworkErrorsName        = "k8s.node.network.errors"
	K8SNodeNetworkErrorsUnit        = "{error}"
	K8SNodeNetworkErrorsDescription = "Node network errors"
	// K8SNodeNetworkIo is the metric conforming to the "k8s.node.network.io"
	// semantic conventions. It represents the network bytes for the Node.
	// Instrument: counter
	// Unit: By
	// Stability: development
	K8SNodeNetworkIoName        = "k8s.node.network.io"
	K8SNodeNetworkIoUnit        = "By"
	K8SNodeNetworkIoDescription = "Network bytes for the Node"
	// K8SNodeUptime is the metric conforming to the "k8s.node.uptime" semantic
	// conventions. It represents the time the Node has been running.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	K8SNodeUptimeName        = "k8s.node.uptime"
	K8SNodeUptimeUnit        = "s"
	K8SNodeUptimeDescription = "The time the Node has been running"
	// K8SPodCPUTime is the metric conforming to the "k8s.pod.cpu.time" semantic
	// conventions. It represents the total CPU time consumed.
	// Instrument: counter
	// Unit: s
	// Stability: development
	K8SPodCPUTimeName        = "k8s.pod.cpu.time"
	K8SPodCPUTimeUnit        = "s"
	K8SPodCPUTimeDescription = "Total CPU time consumed"
	// K8SPodCPUUsage is the metric conforming to the "k8s.pod.cpu.usage" semantic
	// conventions. It represents the pod's CPU usage, measured in cpus. Range from
	// 0 to the number of allocatable CPUs.
	// Instrument: gauge
	// Unit: {cpu}
	// Stability: development
	K8SPodCPUUsageName        = "k8s.pod.cpu.usage"
	K8SPodCPUUsageUnit        = "{cpu}"
	K8SPodCPUUsageDescription = "Pod's CPU usage, measured in cpus. Range from 0 to the number of allocatable CPUs"
	// K8SPodMemoryUsage is the metric conforming to the "k8s.pod.memory.usage"
	// semantic conventions. It represents the memory usage of the Pod.
	// Instrument: gauge
	// Unit: By
	// Stability: development
	K8SPodMemoryUsageName        = "k8s.pod.memory.usage"
	K8SPodMemoryUsageUnit        = "By"
	K8SPodMemoryUsageDescription = "Memory usage of the Pod"
	// K8SPodNetworkErrors is the metric conforming to the "k8s.pod.network.errors"
	// semantic conventions. It represents the pod network errors.
	// Instrument: counter
	// Unit: {error}
	// Stability: development
	K8SPodNetworkErrorsName        = "k8s.pod.network.errors"
	K8SPodNetworkErrorsUnit        = "{error}"
	K8SPodNetworkErrorsDescription = "Pod network errors"
	// K8SPodNetworkIo is the metric conforming to the "k8s.pod.network.io"
	// semantic conventions. It represents the network bytes for the Pod.
	// Instrument: counter
	// Unit: By
	// Stability: development
	K8SPodNetworkIoName        = "k8s.pod.network.io"
	K8SPodNetworkIoUnit        = "By"
	K8SPodNetworkIoDescription = "Network bytes for the Pod"
	// K8SPodUptime is the metric conforming to the "k8s.pod.uptime" semantic
	// conventions. It represents the time the Pod has been running.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	K8SPodUptimeName        = "k8s.pod.uptime"
	K8SPodUptimeUnit        = "s"
	K8SPodUptimeDescription = "The time the Pod has been running"
	// K8SReplicaSetAvailablePods is the metric conforming to the
	// "k8s.replicaset.available_pods" semantic conventions. It represents the
	// total number of available replica pods (ready for at least minReadySeconds)
	// targeted by this replicaset.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SReplicaSetAvailablePodsName        = "k8s.replicaset.available_pods"
	K8SReplicaSetAvailablePodsUnit        = "{pod}"
	K8SReplicaSetAvailablePodsDescription = "Total number of available replica pods (ready for at least minReadySeconds) targeted by this replicaset"
	// K8SReplicaSetDesiredPods is the metric conforming to the
	// "k8s.replicaset.desired_pods" semantic conventions. It represents the number
	// of desired replica pods in this replicaset.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SReplicaSetDesiredPodsName        = "k8s.replicaset.desired_pods"
	K8SReplicaSetDesiredPodsUnit        = "{pod}"
	K8SReplicaSetDesiredPodsDescription = "Number of desired replica pods in this replicaset"
	// K8SReplicationControllerAvailablePods is the metric conforming to the
	// "k8s.replicationcontroller.available_pods" semantic conventions. It
	// represents the total number of available replica pods (ready for at least
	// minReadySeconds) targeted by this replication controller.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SReplicationControllerAvailablePodsName        = "k8s.replicationcontroller.available_pods"
	K8SReplicationControllerAvailablePodsUnit        = "{pod}"
	K8SReplicationControllerAvailablePodsDescription = "Total number of available replica pods (ready for at least minReadySeconds) targeted by this replication controller"
	// K8SReplicationControllerDesiredPods is the metric conforming to the
	// "k8s.replicationcontroller.desired_pods" semantic conventions. It represents
	// the number of desired replica pods in this replication controller.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SReplicationControllerDesiredPodsName        = "k8s.replicationcontroller.desired_pods"
	K8SReplicationControllerDesiredPodsUnit        = "{pod}"
	K8SReplicationControllerDesiredPodsDescription = "Number of desired replica pods in this replication controller"
	// K8SStatefulSetCurrentPods is the metric conforming to the
	// "k8s.statefulset.current_pods" semantic conventions. It represents the
	// number of replica pods created by the statefulset controller from the
	// statefulset version indicated by currentRevision.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SStatefulSetCurrentPodsName        = "k8s.statefulset.current_pods"
	K8SStatefulSetCurrentPodsUnit        = "{pod}"
	K8SStatefulSetCurrentPodsDescription = "The number of replica pods created by the statefulset controller from the statefulset version indicated by currentRevision"
	// K8SStatefulSetDesiredPods is the metric conforming to the
	// "k8s.statefulset.desired_pods" semantic conventions. It represents the
	// number of desired replica pods in this statefulset.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SStatefulSetDesiredPodsName        = "k8s.statefulset.desired_pods"
	K8SStatefulSetDesiredPodsUnit        = "{pod}"
	K8SStatefulSetDesiredPodsDescription = "Number of desired replica pods in this statefulset"
	// K8SStatefulSetReadyPods is the metric conforming to the
	// "k8s.statefulset.ready_pods" semantic conventions. It represents the number
	// of replica pods created for this statefulset with a Ready Condition.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SStatefulSetReadyPodsName        = "k8s.statefulset.ready_pods"
	K8SStatefulSetReadyPodsUnit        = "{pod}"
	K8SStatefulSetReadyPodsDescription = "The number of replica pods created for this statefulset with a Ready Condition"
	// K8SStatefulSetUpdatedPods is the metric conforming to the
	// "k8s.statefulset.updated_pods" semantic conventions. It represents the
	// number of replica pods created by the statefulset controller from the
	// statefulset version indicated by updateRevision.
	// Instrument: updowncounter
	// Unit: {pod}
	// Stability: development
	K8SStatefulSetUpdatedPodsName        = "k8s.statefulset.updated_pods"
	K8SStatefulSetUpdatedPodsUnit        = "{pod}"
	K8SStatefulSetUpdatedPodsDescription = "Number of replica pods created by the statefulset controller from the statefulset version indicated by updateRevision"
	// KestrelActiveConnections is the metric conforming to the
	// "kestrel.active_connections" semantic conventions. It represents the number
	// of connections that are currently active on the server.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: stable
	KestrelActiveConnectionsName        = "kestrel.active_connections"
	KestrelActiveConnectionsUnit        = "{connection}"
	KestrelActiveConnectionsDescription = "Number of connections that are currently active on the server."
	// KestrelActiveTLSHandshakes is the metric conforming to the
	// "kestrel.active_tls_handshakes" semantic conventions. It represents the
	// number of TLS handshakes that are currently in progress on the server.
	// Instrument: updowncounter
	// Unit: {handshake}
	// Stability: stable
	KestrelActiveTLSHandshakesName        = "kestrel.active_tls_handshakes"
	KestrelActiveTLSHandshakesUnit        = "{handshake}"
	KestrelActiveTLSHandshakesDescription = "Number of TLS handshakes that are currently in progress on the server."
	// KestrelConnectionDuration is the metric conforming to the
	// "kestrel.connection.duration" semantic conventions. It represents the
	// duration of connections on the server.
	// Instrument: histogram
	// Unit: s
	// Stability: stable
	KestrelConnectionDurationName        = "kestrel.connection.duration"
	KestrelConnectionDurationUnit        = "s"
	KestrelConnectionDurationDescription = "The duration of connections on the server."
	// KestrelQueuedConnections is the metric conforming to the
	// "kestrel.queued_connections" semantic conventions. It represents the number
	// of connections that are currently queued and are waiting to start.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: stable
	KestrelQueuedConnectionsName        = "kestrel.queued_connections"
	KestrelQueuedConnectionsUnit        = "{connection}"
	KestrelQueuedConnectionsDescription = "Number of connections that are currently queued and are waiting to start."
	// KestrelQueuedRequests is the metric conforming to the
	// "kestrel.queued_requests" semantic conventions. It represents the number of
	// HTTP requests on multiplexed connections (HTTP/2 and HTTP/3) that are
	// currently queued and are waiting to start.
	// Instrument: updowncounter
	// Unit: {request}
	// Stability: stable
	KestrelQueuedRequestsName        = "kestrel.queued_requests"
	KestrelQueuedRequestsUnit        = "{request}"
	KestrelQueuedRequestsDescription = "Number of HTTP requests on multiplexed connections (HTTP/2 and HTTP/3) that are currently queued and are waiting to start."
	// KestrelRejectedConnections is the metric conforming to the
	// "kestrel.rejected_connections" semantic conventions. It represents the
	// number of connections rejected by the server.
	// Instrument: counter
	// Unit: {connection}
	// Stability: stable
	KestrelRejectedConnectionsName        = "kestrel.rejected_connections"
	KestrelRejectedConnectionsUnit        = "{connection}"
	KestrelRejectedConnectionsDescription = "Number of connections rejected by the server."
	// KestrelTLSHandshakeDuration is the metric conforming to the
	// "kestrel.tls_handshake.duration" semantic conventions. It represents the
	// duration of TLS handshakes on the server.
	// Instrument: histogram
	// Unit: s
	// Stability: stable
	KestrelTLSHandshakeDurationName        = "kestrel.tls_handshake.duration"
	KestrelTLSHandshakeDurationUnit        = "s"
	KestrelTLSHandshakeDurationDescription = "The duration of TLS handshakes on the server."
	// KestrelUpgradedConnections is the metric conforming to the
	// "kestrel.upgraded_connections" semantic conventions. It represents the
	// number of connections that are currently upgraded (WebSockets). .
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: stable
	KestrelUpgradedConnectionsName        = "kestrel.upgraded_connections"
	KestrelUpgradedConnectionsUnit        = "{connection}"
	KestrelUpgradedConnectionsDescription = "Number of connections that are currently upgraded (WebSockets). ."
	// MessagingClientConsumedMessages is the metric conforming to the
	// "messaging.client.consumed.messages" semantic conventions. It represents the
	// number of messages that were delivered to the application.
	// Instrument: counter
	// Unit: {message}
	// Stability: development
	MessagingClientConsumedMessagesName        = "messaging.client.consumed.messages"
	MessagingClientConsumedMessagesUnit        = "{message}"
	MessagingClientConsumedMessagesDescription = "Number of messages that were delivered to the application."
	// MessagingClientOperationDuration is the metric conforming to the
	// "messaging.client.operation.duration" semantic conventions. It represents
	// the duration of messaging operation initiated by a producer or consumer
	// client.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	MessagingClientOperationDurationName        = "messaging.client.operation.duration"
	MessagingClientOperationDurationUnit        = "s"
	MessagingClientOperationDurationDescription = "Duration of messaging operation initiated by a producer or consumer client."
	// MessagingClientSentMessages is the metric conforming to the
	// "messaging.client.sent.messages" semantic conventions. It represents the
	// number of messages producer attempted to send to the broker.
	// Instrument: counter
	// Unit: {message}
	// Stability: development
	MessagingClientSentMessagesName        = "messaging.client.sent.messages"
	MessagingClientSentMessagesUnit        = "{message}"
	MessagingClientSentMessagesDescription = "Number of messages producer attempted to send to the broker."
	// MessagingProcessDuration is the metric conforming to the
	// "messaging.process.duration" semantic conventions. It represents the
	// duration of processing operation.
	// Instrument: histogram
	// Unit: s
	// Stability: development
	MessagingProcessDurationName        = "messaging.process.duration"
	MessagingProcessDurationUnit        = "s"
	MessagingProcessDurationDescription = "Duration of processing operation."
	// OTelSDKExporterSpanExportedCount is the metric conforming to the
	// "otel.sdk.exporter.span.exported.count" semantic conventions. It represents
	// the number of spans for which the export has finished, either successful or
	// failed.
	// Instrument: counter
	// Unit: {span}
	// Stability: development
	OTelSDKExporterSpanExportedCountName        = "otel.sdk.exporter.span.exported.count"
	OTelSDKExporterSpanExportedCountUnit        = "{span}"
	OTelSDKExporterSpanExportedCountDescription = "The number of spans for which the export has finished, either successful or failed"
	// OTelSDKExporterSpanInflightCount is the metric conforming to the
	// "otel.sdk.exporter.span.inflight.count" semantic conventions. It represents
	// the number of spans which were passed to the exporter, but that have not
	// been exported yet (neither successful, nor failed).
	// Instrument: updowncounter
	// Unit: {span}
	// Stability: development
	OTelSDKExporterSpanInflightCountName        = "otel.sdk.exporter.span.inflight.count"
	OTelSDKExporterSpanInflightCountUnit        = "{span}"
	OTelSDKExporterSpanInflightCountDescription = "The number of spans which were passed to the exporter, but that have not been exported yet (neither successful, nor failed)"
	// OTelSDKProcessorSpanProcessedCount is the metric conforming to the
	// "otel.sdk.processor.span.processed.count" semantic conventions. It
	// represents the number of spans for which the processing has finished, either
	// successful or failed.
	// Instrument: counter
	// Unit: {span}
	// Stability: development
	OTelSDKProcessorSpanProcessedCountName        = "otel.sdk.processor.span.processed.count"
	OTelSDKProcessorSpanProcessedCountUnit        = "{span}"
	OTelSDKProcessorSpanProcessedCountDescription = "The number of spans for which the processing has finished, either successful or failed"
	// OTelSDKProcessorSpanQueueCapacity is the metric conforming to the
	// "otel.sdk.processor.span.queue.capacity" semantic conventions. It represents
	// the maximum number of spans the queue of a given instance of an SDK span
	// processor can hold.
	// Instrument: updowncounter
	// Unit: {span}
	// Stability: development
	OTelSDKProcessorSpanQueueCapacityName        = "otel.sdk.processor.span.queue.capacity"
	OTelSDKProcessorSpanQueueCapacityUnit        = "{span}"
	OTelSDKProcessorSpanQueueCapacityDescription = "The maximum number of spans the queue of a given instance of an SDK span processor can hold"
	// OTelSDKProcessorSpanQueueSize is the metric conforming to the
	// "otel.sdk.processor.span.queue.size" semantic conventions. It represents the
	// number of spans in the queue of a given instance of an SDK span processor.
	// Instrument: updowncounter
	// Unit: {span}
	// Stability: development
	OTelSDKProcessorSpanQueueSizeName        = "otel.sdk.processor.span.queue.size"
	OTelSDKProcessorSpanQueueSizeUnit        = "{span}"
	OTelSDKProcessorSpanQueueSizeDescription = "The number of spans in the queue of a given instance of an SDK span processor"
	// OTelSDKSpanEndedCount is the metric conforming to the
	// "otel.sdk.span.ended.count" semantic conventions. It represents the number
	// of created spans for which the end operation was called.
	// Instrument: counter
	// Unit: {span}
	// Stability: development
	OTelSDKSpanEndedCountName        = "otel.sdk.span.ended.count"
	OTelSDKSpanEndedCountUnit        = "{span}"
	OTelSDKSpanEndedCountDescription = "The number of created spans for which the end operation was called"
	// OTelSDKSpanLiveCount is the metric conforming to the
	// "otel.sdk.span.live.count" semantic conventions. It represents the number of
	// created spans for which the end operation has not been called yet.
	// Instrument: updowncounter
	// Unit: {span}
	// Stability: development
	OTelSDKSpanLiveCountName        = "otel.sdk.span.live.count"
	OTelSDKSpanLiveCountUnit        = "{span}"
	OTelSDKSpanLiveCountDescription = "The number of created spans for which the end operation has not been called yet"
	// ProcessContextSwitches is the metric conforming to the
	// "process.context_switches" semantic conventions. It represents the number of
	// times the process has been context switched.
	// Instrument: counter
	// Unit: {context_switch}
	// Stability: development
	ProcessContextSwitchesName        = "process.context_switches"
	ProcessContextSwitchesUnit        = "{context_switch}"
	ProcessContextSwitchesDescription = "Number of times the process has been context switched."
	// ProcessCPUTime is the metric conforming to the "process.cpu.time" semantic
	// conventions. It represents the total CPU seconds broken down by different
	// states.
	// Instrument: counter
	// Unit: s
	// Stability: development
	ProcessCPUTimeName        = "process.cpu.time"
	ProcessCPUTimeUnit        = "s"
	ProcessCPUTimeDescription = "Total CPU seconds broken down by different states."
	// ProcessCPUUtilization is the metric conforming to the
	// "process.cpu.utilization" semantic conventions. It represents the difference
	// in process.cpu.time since the last measurement, divided by the elapsed time
	// and number of CPUs available to the process.
	// Instrument: gauge
	// Unit: 1
	// Stability: development
	ProcessCPUUtilizationName        = "process.cpu.utilization"
	ProcessCPUUtilizationUnit        = "1"
	ProcessCPUUtilizationDescription = "" /* 131-byte string literal not displayed */
	// ProcessDiskIo is the metric conforming to the "process.disk.io" semantic
	// conventions. It represents the disk bytes transferred.
	// Instrument: counter
	// Unit: By
	// Stability: development
	ProcessDiskIoName        = "process.disk.io"
	ProcessDiskIoUnit        = "By"
	ProcessDiskIoDescription = "Disk bytes transferred."
	// ProcessMemoryUsage is the metric conforming to the "process.memory.usage"
	// semantic conventions. It represents the amount of physical memory in use.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	ProcessMemoryUsageName        = "process.memory.usage"
	ProcessMemoryUsageUnit        = "By"
	ProcessMemoryUsageDescription = "The amount of physical memory in use."
	// ProcessMemoryVirtual is the metric conforming to the
	// "process.memory.virtual" semantic conventions. It represents the amount of
	// committed virtual memory.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	ProcessMemoryVirtualName        = "process.memory.virtual"
	ProcessMemoryVirtualUnit        = "By"
	ProcessMemoryVirtualDescription = "The amount of committed virtual memory."
	// ProcessNetworkIo is the metric conforming to the "process.network.io"
	// semantic conventions. It represents the network bytes transferred.
	// Instrument: counter
	// Unit: By
	// Stability: development
	ProcessNetworkIoName        = "process.network.io"
	ProcessNetworkIoUnit        = "By"
	ProcessNetworkIoDescription = "Network bytes transferred."
	// ProcessOpenFileDescriptorCount is the metric conforming to the
	// "process.open_file_descriptor.count" semantic conventions. It represents the
	// number of file descriptors in use by the process.
	// Instrument: updowncounter
	// Unit: {file_descriptor}
	// Stability: development
	ProcessOpenFileDescriptorCountName        = "process.open_file_descriptor.count"
	ProcessOpenFileDescriptorCountUnit        = "{file_descriptor}"
	ProcessOpenFileDescriptorCountDescription = "Number of file descriptors in use by the process."
	// ProcessPagingFaults is the metric conforming to the "process.paging.faults"
	// semantic conventions. It represents the number of page faults the process
	// has made.
	// Instrument: counter
	// Unit: {fault}
	// Stability: development
	ProcessPagingFaultsName        = "process.paging.faults"
	ProcessPagingFaultsUnit        = "{fault}"
	ProcessPagingFaultsDescription = "Number of page faults the process has made."
	// ProcessThreadCount is the metric conforming to the "process.thread.count"
	// semantic conventions. It represents the process threads count.
	// Instrument: updowncounter
	// Unit: {thread}
	// Stability: development
	ProcessThreadCountName        = "process.thread.count"
	ProcessThreadCountUnit        = "{thread}"
	ProcessThreadCountDescription = "Process threads count."
	// ProcessUptime is the metric conforming to the "process.uptime" semantic
	// conventions. It represents the time the process has been running.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	ProcessUptimeName        = "process.uptime"
	ProcessUptimeUnit        = "s"
	ProcessUptimeDescription = "The time the process has been running."
	// RPCClientDuration is the metric conforming to the "rpc.client.duration"
	// semantic conventions. It represents the measures the duration of outbound
	// RPC.
	// Instrument: histogram
	// Unit: ms
	// Stability: development
	RPCClientDurationName        = "rpc.client.duration"
	RPCClientDurationUnit        = "ms"
	RPCClientDurationDescription = "Measures the duration of outbound RPC."
	// RPCClientRequestSize is the metric conforming to the
	// "rpc.client.request.size" semantic conventions. It represents the measures
	// the size of RPC request messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: development
	RPCClientRequestSizeName        = "rpc.client.request.size"
	RPCClientRequestSizeUnit        = "By"
	RPCClientRequestSizeDescription = "Measures the size of RPC request messages (uncompressed)."
	// RPCClientRequestsPerRPC is the metric conforming to the
	// "rpc.client.requests_per_rpc" semantic conventions. It represents the
	// measures the number of messages received per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: development
	RPCClientRequestsPerRPCName        = "rpc.client.requests_per_rpc"
	RPCClientRequestsPerRPCUnit        = "{count}"
	RPCClientRequestsPerRPCDescription = "Measures the number of messages received per RPC."
	// RPCClientResponseSize is the metric conforming to the
	// "rpc.client.response.size" semantic conventions. It represents the measures
	// the size of RPC response messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: development
	RPCClientResponseSizeName        = "rpc.client.response.size"
	RPCClientResponseSizeUnit        = "By"
	RPCClientResponseSizeDescription = "Measures the size of RPC response messages (uncompressed)."
	// RPCClientResponsesPerRPC is the metric conforming to the
	// "rpc.client.responses_per_rpc" semantic conventions. It represents the
	// measures the number of messages sent per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: development
	RPCClientResponsesPerRPCName        = "rpc.client.responses_per_rpc"
	RPCClientResponsesPerRPCUnit        = "{count}"
	RPCClientResponsesPerRPCDescription = "Measures the number of messages sent per RPC."
	// RPCServerDuration is the metric conforming to the "rpc.server.duration"
	// semantic conventions. It represents the measures the duration of inbound
	// RPC.
	// Instrument: histogram
	// Unit: ms
	// Stability: development
	RPCServerDurationName        = "rpc.server.duration"
	RPCServerDurationUnit        = "ms"
	RPCServerDurationDescription = "Measures the duration of inbound RPC."
	// RPCServerRequestSize is the metric conforming to the
	// "rpc.server.request.size" semantic conventions. It represents the measures
	// the size of RPC request messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: development
	RPCServerRequestSizeName        = "rpc.server.request.size"
	RPCServerRequestSizeUnit        = "By"
	RPCServerRequestSizeDescription = "Measures the size of RPC request messages (uncompressed)."
	// RPCServerRequestsPerRPC is the metric conforming to the
	// "rpc.server.requests_per_rpc" semantic conventions. It represents the
	// measures the number of messages received per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: development
	RPCServerRequestsPerRPCName        = "rpc.server.requests_per_rpc"
	RPCServerRequestsPerRPCUnit        = "{count}"
	RPCServerRequestsPerRPCDescription = "Measures the number of messages received per RPC."
	// RPCServerResponseSize is the metric conforming to the
	// "rpc.server.response.size" semantic conventions. It represents the measures
	// the size of RPC response messages (uncompressed).
	// Instrument: histogram
	// Unit: By
	// Stability: development
	RPCServerResponseSizeName        = "rpc.server.response.size"
	RPCServerResponseSizeUnit        = "By"
	RPCServerResponseSizeDescription = "Measures the size of RPC response messages (uncompressed)."
	// RPCServerResponsesPerRPC is the metric conforming to the
	// "rpc.server.responses_per_rpc" semantic conventions. It represents the
	// measures the number of messages sent per RPC.
	// Instrument: histogram
	// Unit: {count}
	// Stability: development
	RPCServerResponsesPerRPCName        = "rpc.server.responses_per_rpc"
	RPCServerResponsesPerRPCUnit        = "{count}"
	RPCServerResponsesPerRPCDescription = "Measures the number of messages sent per RPC."
	// SignalrServerActiveConnections is the metric conforming to the
	// "signalr.server.active_connections" semantic conventions. It represents the
	// number of connections that are currently active on the server.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: stable
	SignalrServerActiveConnectionsName        = "signalr.server.active_connections"
	SignalrServerActiveConnectionsUnit        = "{connection}"
	SignalrServerActiveConnectionsDescription = "Number of connections that are currently active on the server."
	// SignalrServerConnectionDuration is the metric conforming to the
	// "signalr.server.connection.duration" semantic conventions. It represents the
	// duration of connections on the server.
	// Instrument: histogram
	// Unit: s
	// Stability: stable
	SignalrServerConnectionDurationName        = "signalr.server.connection.duration"
	SignalrServerConnectionDurationUnit        = "s"
	SignalrServerConnectionDurationDescription = "The duration of connections on the server."
	// SystemCPULogicalCount is the metric conforming to the
	// "system.cpu.logical.count" semantic conventions. It represents the reports
	// the number of logical (virtual) processor cores created by the operating
	// system to manage multitasking.
	// Instrument: updowncounter
	// Unit: {cpu}
	// Stability: development
	SystemCPULogicalCountName        = "system.cpu.logical.count"
	SystemCPULogicalCountUnit        = "{cpu}"
	SystemCPULogicalCountDescription = "Reports the number of logical (virtual) processor cores created by the operating system to manage multitasking"
	// SystemCPUPhysicalCount is the metric conforming to the
	// "system.cpu.physical.count" semantic conventions. It represents the reports
	// the number of actual physical processor cores on the hardware.
	// Instrument: updowncounter
	// Unit: {cpu}
	// Stability: development
	SystemCPUPhysicalCountName        = "system.cpu.physical.count"
	SystemCPUPhysicalCountUnit        = "{cpu}"
	SystemCPUPhysicalCountDescription = "Reports the number of actual physical processor cores on the hardware"
	// SystemDiskIo is the metric conforming to the "system.disk.io" semantic
	// conventions.
	// Instrument: counter
	// Unit: By
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemDiskIoName = "system.disk.io"
	SystemDiskIoUnit = "By"
	// SystemDiskIoTime is the metric conforming to the "system.disk.io_time"
	// semantic conventions. It represents the time disk spent activated.
	// Instrument: counter
	// Unit: s
	// Stability: development
	SystemDiskIoTimeName        = "system.disk.io_time"
	SystemDiskIoTimeUnit        = "s"
	SystemDiskIoTimeDescription = "Time disk spent activated"
	// SystemDiskLimit is the metric conforming to the "system.disk.limit" semantic
	// conventions. It represents the total storage capacity of the disk.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemDiskLimitName        = "system.disk.limit"
	SystemDiskLimitUnit        = "By"
	SystemDiskLimitDescription = "The total storage capacity of the disk"
	// SystemDiskMerged is the metric conforming to the "system.disk.merged"
	// semantic conventions.
	// Instrument: counter
	// Unit: {operation}
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemDiskMergedName = "system.disk.merged"
	SystemDiskMergedUnit = "{operation}"
	// SystemDiskOperationTime is the metric conforming to the
	// "system.disk.operation_time" semantic conventions. It represents the sum of
	// the time each operation took to complete.
	// Instrument: counter
	// Unit: s
	// Stability: development
	SystemDiskOperationTimeName        = "system.disk.operation_time"
	SystemDiskOperationTimeUnit        = "s"
	SystemDiskOperationTimeDescription = "Sum of the time each operation took to complete"
	// SystemDiskOperations is the metric conforming to the
	// "system.disk.operations" semantic conventions.
	// Instrument: counter
	// Unit: {operation}
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemDiskOperationsName = "system.disk.operations"
	SystemDiskOperationsUnit = "{operation}"
	// SystemFilesystemLimit is the metric conforming to the
	// "system.filesystem.limit" semantic conventions. It represents the total
	// storage capacity of the filesystem.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemFilesystemLimitName        = "system.filesystem.limit"
	SystemFilesystemLimitUnit        = "By"
	SystemFilesystemLimitDescription = "The total storage capacity of the filesystem"
	// SystemFilesystemUsage is the metric conforming to the
	// "system.filesystem.usage" semantic conventions. It represents the reports a
	// filesystem's space usage across different states.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemFilesystemUsageName        = "system.filesystem.usage"
	SystemFilesystemUsageUnit        = "By"
	SystemFilesystemUsageDescription = "Reports a filesystem's space usage across different states."
	// SystemFilesystemUtilization is the metric conforming to the
	// "system.filesystem.utilization" semantic conventions.
	// Instrument: gauge
	// Unit: 1
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemFilesystemUtilizationName = "system.filesystem.utilization"
	SystemFilesystemUtilizationUnit = "1"
	// SystemLinuxMemoryAvailable is the metric conforming to the
	// "system.linux.memory.available" semantic conventions. It represents an
	// estimate of how much memory is available for starting new applications,
	// without causing swapping.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemLinuxMemoryAvailableName        = "system.linux.memory.available"
	SystemLinuxMemoryAvailableUnit        = "By"
	SystemLinuxMemoryAvailableDescription = "An estimate of how much memory is available for starting new applications, without causing swapping"
	// SystemLinuxMemorySlabUsage is the metric conforming to the
	// "system.linux.memory.slab.usage" semantic conventions. It represents the
	// reports the memory used by the Linux kernel for managing caches of
	// frequently used objects.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemLinuxMemorySlabUsageName        = "system.linux.memory.slab.usage"
	SystemLinuxMemorySlabUsageUnit        = "By"
	SystemLinuxMemorySlabUsageDescription = "Reports the memory used by the Linux kernel for managing caches of frequently used objects."
	// SystemMemoryLimit is the metric conforming to the "system.memory.limit"
	// semantic conventions. It represents the total memory available in the
	// system.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemMemoryLimitName        = "system.memory.limit"
	SystemMemoryLimitUnit        = "By"
	SystemMemoryLimitDescription = "Total memory available in the system."
	// SystemMemoryShared is the metric conforming to the "system.memory.shared"
	// semantic conventions. It represents the shared memory used (mostly by
	// tmpfs).
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemMemorySharedName        = "system.memory.shared"
	SystemMemorySharedUnit        = "By"
	SystemMemorySharedDescription = "Shared memory used (mostly by tmpfs)."
	// SystemMemoryUsage is the metric conforming to the "system.memory.usage"
	// semantic conventions. It represents the reports memory in use by state.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemMemoryUsageName        = "system.memory.usage"
	SystemMemoryUsageUnit        = "By"
	SystemMemoryUsageDescription = "Reports memory in use by state."
	// SystemMemoryUtilization is the metric conforming to the
	// "system.memory.utilization" semantic conventions.
	// Instrument: gauge
	// Unit: 1
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemMemoryUtilizationName = "system.memory.utilization"
	SystemMemoryUtilizationUnit = "1"
	// SystemNetworkConnections is the metric conforming to the
	// "system.network.connections" semantic conventions.
	// Instrument: updowncounter
	// Unit: {connection}
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemNetworkConnectionsName = "system.network.connections"
	SystemNetworkConnectionsUnit = "{connection}"
	// SystemNetworkDropped is the metric conforming to the
	// "system.network.dropped" semantic conventions. It represents the count of
	// packets that are dropped or discarded even though there was no error.
	// Instrument: counter
	// Unit: {packet}
	// Stability: development
	SystemNetworkDroppedName        = "system.network.dropped"
	SystemNetworkDroppedUnit        = "{packet}"
	SystemNetworkDroppedDescription = "Count of packets that are dropped or discarded even though there was no error"
	// SystemNetworkErrors is the metric conforming to the "system.network.errors"
	// semantic conventions. It represents the count of network errors detected.
	// Instrument: counter
	// Unit: {error}
	// Stability: development
	SystemNetworkErrorsName        = "system.network.errors"
	SystemNetworkErrorsUnit        = "{error}"
	SystemNetworkErrorsDescription = "Count of network errors detected"
	// SystemNetworkIo is the metric conforming to the "system.network.io" semantic
	// conventions.
	// Instrument: counter
	// Unit: By
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemNetworkIoName = "system.network.io"
	SystemNetworkIoUnit = "By"
	// SystemNetworkPackets is the metric conforming to the
	// "system.network.packets" semantic conventions.
	// Instrument: counter
	// Unit: {packet}
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemNetworkPacketsName = "system.network.packets"
	SystemNetworkPacketsUnit = "{packet}"
	// SystemPagingFaults is the metric conforming to the "system.paging.faults"
	// semantic conventions.
	// Instrument: counter
	// Unit: {fault}
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemPagingFaultsName = "system.paging.faults"
	SystemPagingFaultsUnit = "{fault}"
	// SystemPagingOperations is the metric conforming to the
	// "system.paging.operations" semantic conventions.
	// Instrument: counter
	// Unit: {operation}
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemPagingOperationsName = "system.paging.operations"
	SystemPagingOperationsUnit = "{operation}"
	// SystemPagingUsage is the metric conforming to the "system.paging.usage"
	// semantic conventions. It represents the unix swap or windows pagefile usage.
	// Instrument: updowncounter
	// Unit: By
	// Stability: development
	SystemPagingUsageName        = "system.paging.usage"
	SystemPagingUsageUnit        = "By"
	SystemPagingUsageDescription = "Unix swap or windows pagefile usage"
	// SystemPagingUtilization is the metric conforming to the
	// "system.paging.utilization" semantic conventions.
	// Instrument: gauge
	// Unit: 1
	// Stability: development
	// NOTE: The description (brief) for this metric is not defined in the semantic-conventions repository.
	SystemPagingUtilizationName = "system.paging.utilization"
	SystemPagingUtilizationUnit = "1"
	// SystemProcessCount is the metric conforming to the "system.process.count"
	// semantic conventions. It represents the total number of processes in each
	// state.
	// Instrument: updowncounter
	// Unit: {process}
	// Stability: development
	SystemProcessCountName        = "system.process.count"
	SystemProcessCountUnit        = "{process}"
	SystemProcessCountDescription = "Total number of processes in each state"
	// SystemProcessCreated is the metric conforming to the
	// "system.process.created" semantic conventions. It represents the total
	// number of processes created over uptime of the host.
	// Instrument: counter
	// Unit: {process}
	// Stability: development
	SystemProcessCreatedName        = "system.process.created"
	SystemProcessCreatedUnit        = "{process}"
	SystemProcessCreatedDescription = "Total number of processes created over uptime of the host"
	// SystemUptime is the metric conforming to the "system.uptime" semantic
	// conventions. It represents the time the system has been running.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	SystemUptimeName        = "system.uptime"
	SystemUptimeUnit        = "s"
	SystemUptimeDescription = "The time the system has been running"
	// VCSChangeCount is the metric conforming to the "vcs.change.count" semantic
	// conventions. It represents the number of changes (pull requests/merge
	// requests/changelists) in a repository, categorized by their state (e.g. open
	// or merged).
	// Instrument: updowncounter
	// Unit: {change}
	// Stability: development
	VCSChangeCountName        = "vcs.change.count"
	VCSChangeCountUnit        = "{change}"
	VCSChangeCountDescription = "" /* 130-byte string literal not displayed */
	// VCSChangeDuration is the metric conforming to the "vcs.change.duration"
	// semantic conventions. It represents the time duration a change (pull
	// request/merge request/changelist) has been in a given state.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	VCSChangeDurationName        = "vcs.change.duration"
	VCSChangeDurationUnit        = "s"
	VCSChangeDurationDescription = "The time duration a change (pull request/merge request/changelist) has been in a given state."
	// VCSChangeTimeToApproval is the metric conforming to the
	// "vcs.change.time_to_approval" semantic conventions. It represents the amount
	// of time since its creation it took a change (pull request/merge
	// request/changelist) to get the first approval.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	VCSChangeTimeToApprovalName        = "vcs.change.time_to_approval"
	VCSChangeTimeToApprovalUnit        = "s"
	VCSChangeTimeToApprovalDescription = "The amount of time since its creation it took a change (pull request/merge request/changelist) to get the first approval."
	// VCSChangeTimeToMerge is the metric conforming to the
	// "vcs.change.time_to_merge" semantic conventions. It represents the amount of
	// time since its creation it took a change (pull request/merge
	// request/changelist) to get merged into the target(base) ref.
	// Instrument: gauge
	// Unit: s
	// Stability: development
	VCSChangeTimeToMergeName        = "vcs.change.time_to_merge"
	VCSChangeTimeToMergeUnit        = "s"
	VCSChangeTimeToMergeDescription = "" /* 135-byte string literal not displayed */
	// VCSContributorCount is the metric conforming to the "vcs.contributor.count"
	// semantic conventions. It represents the number of unique contributors to a
	// repository.
	// Instrument: gauge
	// Unit: {contributor}
	// Stability: development
	VCSContributorCountName        = "vcs.contributor.count"
	VCSContributorCountUnit        = "{contributor}"
	VCSContributorCountDescription = "The number of unique contributors to a repository"
	// VCSRefCount is the metric conforming to the "vcs.ref.count" semantic
	// conventions. It represents the number of refs of type branch or tag in a
	// repository.
	// Instrument: updowncounter
	// Unit: {ref}
	// Stability: development
	VCSRefCountName        = "vcs.ref.count"
	VCSRefCountUnit        = "{ref}"
	VCSRefCountDescription = "The number of refs of type branch or tag in a repository."
	// VCSRefLinesDelta is the metric conforming to the "vcs.ref.lines_delta"
	// semantic conventions. It represents the number of lines added/removed in a
	// ref (branch) relative to the ref from the `vcs.ref.base.name` attribute.
	// Instrument: gauge
	// Unit: {line}
	// Stability: development
	VCSRefLinesDeltaName        = "vcs.ref.lines_delta"
	VCSRefLinesDeltaUnit        = "{line}"
	VCSRefLinesDeltaDescription = "The number of lines added/removed in a ref (branch) relative to the ref from the `vcs.ref.base.name` attribute."
	// VCSRefRevisionsDelta is the metric conforming to the
	// "vcs.ref.revisions_delta" semantic conventions. It represents the number of
	// revisions (commits) a ref (branch) is ahead/behind the branch from the
	// `vcs.ref.base.name` attribute.
	// Instrument: gauge
	// Unit: {revision}
	// Stability: development
	VCSRefRevisionsDeltaName        = "vcs.ref.revisions_delta"
	VCSRefRevisionsDeltaUnit        = "{revision}"
	VCSRefRevisionsDeltaDescription = "The number of revisions (commits) a ref (branch) is ahead/behind the branch from the `vcs.ref.base.name` attribute"
	// VCSRefTime is the metric conforming to the "vcs.ref.time" semantic
	// conventions. It represents the time a ref (branch) created from the default
	// branch (trunk) has existed. The `ref.type` attribute will always be `branch`
	// .
	// Instrument: gauge
	// Unit: s
	// Stability: development
	VCSRefTimeName        = "vcs.ref.time"
	VCSRefTimeUnit        = "s"
	VCSRefTimeDescription = "Time a ref (branch) created from the default branch (trunk) has existed. The `ref.type` attribute will always be `branch`"
	// VCSRepositoryCount is the metric conforming to the "vcs.repository.count"
	// semantic conventions. It represents the number of repositories in an
	// organization.
	// Instrument: updowncounter
	// Unit: {repository}
	// Stability: development
	VCSRepositoryCountName        = "vcs.repository.count"
	VCSRepositoryCountUnit        = "{repository}"
	VCSRepositoryCountDescription = "The number of repositories in an organization."
)
View Source
const (
	// DNSQuestionNameKey is the attribute Key conforming to the "dns.question.name"
	// semantic conventions. It represents the name being queried.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "www.example.com", "opentelemetry.io"
	// Note: If the name field contains non-printable characters (below 32 or above
	// 126), those characters should be represented as escaped base 10 integers
	// (\DDD). Back slashes and quotes should be escaped. Tabs, carriage returns,
	// and line feeds should be converted to \t, \r, and \n respectively.
	DNSQuestionNameKey = attribute.Key("dns.question.name")
)

Namespace: dns

View Source
const (
	// DiskIoDirectionKey is the attribute Key conforming to the "disk.io.direction"
	// semantic conventions. It represents the disk IO operation direction.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "read"
	DiskIoDirectionKey = attribute.Key("disk.io.direction")
)

Namespace: disk

View Source
const (
	// ElasticsearchNodeNameKey is the attribute Key conforming to the
	// "elasticsearch.node.name" semantic conventions. It represents the represents
	// the human-readable identifier of the node/instance to which a request was
	// routed.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "instance-0000000001"
	ElasticsearchNodeNameKey = attribute.Key("elasticsearch.node.name")
)

Namespace: elasticsearch

View Source
const (
	// ErrorTypeKey is the attribute Key conforming to the "error.type" semantic
	// conventions. It represents the describes a class of error the operation ended
	// with.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Stable
	//
	// Examples: "timeout", "java.net.UnknownHostException",
	// "server_certificate_invalid", "500"
	// Note: The `error.type` SHOULD be predictable, and SHOULD have low
	// cardinality.
	//
	// When `error.type` is set to a type (e.g., an exception type), its
	// canonical class name identifying the type within the artifact SHOULD be used.
	//
	// Instrumentations SHOULD document the list of errors they report.
	//
	// The cardinality of `error.type` within one instrumentation library SHOULD be
	// low.
	// Telemetry consumers that aggregate data from multiple instrumentation
	// libraries and applications
	// should be prepared for `error.type` to have high cardinality at query time
	// when no
	// additional filters are applied.
	//
	// If the operation has completed successfully, instrumentations SHOULD NOT set
	// `error.type`.
	//
	// If a specific domain defines its own set of error identifiers (such as HTTP
	// or gRPC status codes),
	// it's RECOMMENDED to:
	//
	//   - Use a domain-specific attribute
	//   - Set `error.type` to capture all errors, regardless of whether they are
	//     defined within the domain-specific set or not.
	ErrorTypeKey = attribute.Key("error.type")
)

Namespace: error

View Source
const (
	// ExceptionEventName is the name of the Span event representing an exception.
	ExceptionEventName = "exception"
)
View Source
const (
	// GoMemoryTypeKey is the attribute Key conforming to the "go.memory.type"
	// semantic conventions. It represents the type of memory.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "other", "stack"
	GoMemoryTypeKey = attribute.Key("go.memory.type")
)

Namespace: go

View Source
const (
	// IosAppStateKey is the attribute Key conforming to the "ios.app.state"
	// semantic conventions. It represents the this attribute represents the state
	// of the application.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: The iOS lifecycle states are defined in the
	// [UIApplicationDelegate documentation], and from which the `OS terminology`
	// column values are derived.
	//
	// [UIApplicationDelegate documentation]: https://developer.apple.com/documentation/uikit/uiapplicationdelegate
	IosAppStateKey = attribute.Key("ios.app.state")
)

Namespace: ios

View Source
const (
	// LinuxMemorySlabStateKey is the attribute Key conforming to the
	// "linux.memory.slab.state" semantic conventions. It represents the Linux Slab
	// memory state.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "reclaimable", "unreclaimable"
	LinuxMemorySlabStateKey = attribute.Key("linux.memory.slab.state")
)

Namespace: linux

View Source
const (
	// OciManifestDigestKey is the attribute Key conforming to the
	// "oci.manifest.digest" semantic conventions. It represents the digest of the
	// OCI image manifest. For container images specifically is the digest by which
	// the container image is known.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// "sha256:e4ca62c0d62f3e886e684806dfe9d4e0cda60d54986898173c1083856cfda0f4"
	// Note: Follows [OCI Image Manifest Specification], and specifically the
	// [Digest property].
	// An example can be found in [Example Image Manifest].
	//
	// [OCI Image Manifest Specification]: https://github.com/opencontainers/image-spec/blob/main/manifest.md
	// [Digest property]: https://github.com/opencontainers/image-spec/blob/main/descriptor.md#digests
	// [Example Image Manifest]: https://github.com/opencontainers/image-spec/blob/main/manifest.md#example-image-manifest
	OciManifestDigestKey = attribute.Key("oci.manifest.digest")
)

Namespace: oci

View Source
const (
	// OpentracingRefTypeKey is the attribute Key conforming to the
	// "opentracing.ref_type" semantic conventions. It represents the parent-child
	// Reference type.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples:
	// Note: The causal relationship between a child Span and a parent Span.
	OpentracingRefTypeKey = attribute.Key("opentracing.ref_type")
)

Namespace: opentracing

View Source
const (
	// PeerServiceKey is the attribute Key conforming to the "peer.service" semantic
	// conventions. It represents the [`service.name`] of the remote service. SHOULD
	// be equal to the actual `service.name` resource attribute of the remote
	// service if any.
	//
	// Type: string
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: AuthTokenCache
	//
	// [`service.name`]: /docs/resource/README.md#service
	PeerServiceKey = attribute.Key("peer.service")
)

Namespace: peer

View Source
const (
	// ProfileFrameTypeKey is the attribute Key conforming to the
	// "profile.frame.type" semantic conventions. It represents the describes the
	// interpreter or compiler of a single frame.
	//
	// Type: Enum
	// RequirementLevel: Recommended
	// Stability: Development
	//
	// Examples: "cpython"
	ProfileFrameTypeKey = attribute.Key("profile.frame.type")
)

Namespace: profile

View Source
const SchemaURL = "https://opentelemetry.io/schemas/1.31.0"

SchemaURL is the schema URL that matches the version of the semantic conventions that this package defines. Semconv packages starting from v1.4.0 must declare non-empty schema URL in the form https://opentelemetry.io/schemas/<version>

Variables ¶
View Source
var (
	// Any time before Activity.onResume() or, if the app has no Activity,
	// Context.startService() has been called in the app for the first time.
	//
	// Stability: development
	AndroidAppStateCreated = AndroidAppStateKey.String("created")
	// Any time after Activity.onPause() or, if the app has no Activity,
	// Context.stopService() has been called when the app was in the foreground
	// state.
	//
	// Stability: development
	AndroidAppStateBackground = AndroidAppStateKey.String("background")
	// Any time after Activity.onResume() or, if the app has no Activity,
	// Context.startService() has been called when the app was in either the created
	// or background states.
	//
	// Stability: development
	AndroidAppStateForeground = AndroidAppStateKey.String("foreground")
)

Enum values for android.app.state

View Source
var (
	// ec2
	// Stability: development
	AWSECSLaunchtypeEC2 = AWSECSLaunchtypeKey.String("ec2")
	// fargate
	// Stability: development
	AWSECSLaunchtypeFargate = AWSECSLaunchtypeKey.String("fargate")
)

Enum values for aws.ecs.launchtype

View Source
var (
	// Gateway (HTTP) connection.
	// Stability: development
	AzureCosmosDBConnectionModeGateway = AzureCosmosDBConnectionModeKey.String("gateway")
	// Direct connection.
	// Stability: development
	AzureCosmosDBConnectionModeDirect = AzureCosmosDBConnectionModeKey.String("direct")
)

Enum values for azure.cosmosdb.connection.mode

View Source
var (
	// strong
	// Stability: development
	AzureCosmosDBConsistencyLevelStrong = AzureCosmosDBConsistencyLevelKey.String("Strong")
	// bounded_staleness
	// Stability: development
	AzureCosmosDBConsistencyLevelBoundedStaleness = AzureCosmosDBConsistencyLevelKey.String("BoundedStaleness")
	// session
	// Stability: development
	AzureCosmosDBConsistencyLevelSession = AzureCosmosDBConsistencyLevelKey.String("Session")
	// eventual
	// Stability: development
	AzureCosmosDBConsistencyLevelEventual = AzureCosmosDBConsistencyLevelKey.String("Eventual")
	// consistent_prefix
	// Stability: development
	AzureCosmosDBConsistencyLevelConsistentPrefix = AzureCosmosDBConsistencyLevelKey.String("ConsistentPrefix")
)

Enum values for azure.cosmosdb.consistency.level

View Source
var (
	// all
	// Stability: development
	CassandraConsistencyLevelAll = CassandraConsistencyLevelKey.String("all")
	// each_quorum
	// Stability: development
	CassandraConsistencyLevelEachQuorum = CassandraConsistencyLevelKey.String("each_quorum")
	// quorum
	// Stability: development
	CassandraConsistencyLevelQuorum = CassandraConsistencyLevelKey.String("quorum")
	// local_quorum
	// Stability: development
	CassandraConsistencyLevelLocalQuorum = CassandraConsistencyLevelKey.String("local_quorum")
	// one
	// Stability: development
	CassandraConsistencyLevelOne = CassandraConsistencyLevelKey.String("one")
	// two
	// Stability: development
	CassandraConsistencyLevelTwo = CassandraConsistencyLevelKey.String("two")
	// three
	// Stability: development
	CassandraConsistencyLevelThree = CassandraConsistencyLevelKey.String("three")
	// local_one
	// Stability: development
	CassandraConsistencyLevelLocalOne = CassandraConsistencyLevelKey.String("local_one")
	// any
	// Stability: development
	CassandraConsistencyLevelAny = CassandraConsistencyLevelKey.String("any")
	// serial
	// Stability: development
	CassandraConsistencyLevelSerial = CassandraConsistencyLevelKey.String("serial")
	// local_serial
	// Stability: development
	CassandraConsistencyLevelLocalSerial = CassandraConsistencyLevelKey.String("local_serial")
)

Enum values for cassandra.consistency.level

View Source
var (
	// The pipeline run finished successfully.
	// Stability: development
	CICDPipelineResultSuccess = CICDPipelineResultKey.String("success")
	// The pipeline run did not finish successfully, eg. due to a compile error or a
	// failing test. Such failures are usually detected by non-zero exit codes of
	// the tools executed in the pipeline run.
	// Stability: development
	CICDPipelineResultFailure = CICDPipelineResultKey.String("failure")
	// The pipeline run failed due to an error in the CICD system, eg. due to the
	// worker being killed.
	// Stability: development
	CICDPipelineResultError = CICDPipelineResultKey.String("error")
	// A timeout caused the pipeline run to be interrupted.
	// Stability: development
	CICDPipelineResultTimeout = CICDPipelineResultKey.String("timeout")
	// The pipeline run was cancelled, eg. by a user manually cancelling the
	// pipeline run.
	// Stability: development
	CICDPipelineResultCancellation = CICDPipelineResultKey.String("cancellation")
	// The pipeline run was skipped, eg. due to a precondition not being met.
	// Stability: development
	CICDPipelineResultSkip = CICDPipelineResultKey.String("skip")
)

Enum values for cicd.pipeline.result

View Source
var (
	// The run pending state spans from the event triggering the pipeline run until
	// the execution of the run starts (eg. time spent in a queue, provisioning
	// agents, creating run resources).
	//
	// Stability: development
	CICDPipelineRunStatePending = CICDPipelineRunStateKey.String("pending")
	// The executing state spans the execution of any run tasks (eg. build, test).
	// Stability: development
	CICDPipelineRunStateExecuting = CICDPipelineRunStateKey.String("executing")
	// The finalizing state spans from when the run has finished executing (eg.
	// cleanup of run resources).
	// Stability: development
	CICDPipelineRunStateFinalizing = CICDPipelineRunStateKey.String("finalizing")
)

Enum values for cicd.pipeline.run.state

View Source
var (
	// build
	// Stability: development
	CICDPipelineTaskTypeBuild = CICDPipelineTaskTypeKey.String("build")
	// test
	// Stability: development
	CICDPipelineTaskTypeTest = CICDPipelineTaskTypeKey.String("test")
	// deploy
	// Stability: development
	CICDPipelineTaskTypeDeploy = CICDPipelineTaskTypeKey.String("deploy")
)

Enum values for cicd.pipeline.task.type

View Source
var (
	// The worker is not performing work for the CICD system. It is available to the
	// CICD system to perform work on (online / idle).
	// Stability: development
	CICDWorkerStateAvailable = CICDWorkerStateKey.String("available")
	// The worker is performing work for the CICD system.
	// Stability: development
	CICDWorkerStateBusy = CICDWorkerStateKey.String("busy")
	// The worker is not available to the CICD system (disconnected / down).
	// Stability: development
	CICDWorkerStateOffline = CICDWorkerStateKey.String("offline")
)

Enum values for cicd.worker.state

View Source
var (
	// Alibaba Cloud Elastic Compute Service
	// Stability: development
	CloudPlatformAlibabaCloudECS = CloudPlatformKey.String("alibaba_cloud_ecs")
	// Alibaba Cloud Function Compute
	// Stability: development
	CloudPlatformAlibabaCloudFc = CloudPlatformKey.String("alibaba_cloud_fc")
	// Red Hat OpenShift on Alibaba Cloud
	// Stability: development
	CloudPlatformAlibabaCloudOpenshift = CloudPlatformKey.String("alibaba_cloud_openshift")
	// AWS Elastic Compute Cloud
	// Stability: development
	CloudPlatformAWSEC2 = CloudPlatformKey.String("aws_ec2")
	// AWS Elastic Container Service
	// Stability: development
	CloudPlatformAWSECS = CloudPlatformKey.String("aws_ecs")
	// AWS Elastic Kubernetes Service
	// Stability: development
	CloudPlatformAWSEKS = CloudPlatformKey.String("aws_eks")
	// AWS Lambda
	// Stability: development
	CloudPlatformAWSLambda = CloudPlatformKey.String("aws_lambda")
	// AWS Elastic Beanstalk
	// Stability: development
	CloudPlatformAWSElasticBeanstalk = CloudPlatformKey.String("aws_elastic_beanstalk")
	// AWS App Runner
	// Stability: development
	CloudPlatformAWSAppRunner = CloudPlatformKey.String("aws_app_runner")
	// Red Hat OpenShift on AWS (ROSA)
	// Stability: development
	CloudPlatformAWSOpenshift = CloudPlatformKey.String("aws_openshift")
	// Azure Virtual Machines
	// Stability: development
	CloudPlatformAzureVM = CloudPlatformKey.String("azure_vm")
	// Azure Container Apps
	// Stability: development
	CloudPlatformAzureContainerApps = CloudPlatformKey.String("azure_container_apps")
	// Azure Container Instances
	// Stability: development
	CloudPlatformAzureContainerInstances = CloudPlatformKey.String("azure_container_instances")
	// Azure Kubernetes Service
	// Stability: development
	CloudPlatformAzureAKS = CloudPlatformKey.String("azure_aks")
	// Azure Functions
	// Stability: development
	CloudPlatformAzureFunctions = CloudPlatformKey.String("azure_functions")
	// Azure App Service
	// Stability: development
	CloudPlatformAzureAppService = CloudPlatformKey.String("azure_app_service")
	// Azure Red Hat OpenShift
	// Stability: development
	CloudPlatformAzureOpenshift = CloudPlatformKey.String("azure_openshift")
	// Google Bare Metal Solution (BMS)
	// Stability: development
	CloudPlatformGCPBareMetalSolution = CloudPlatformKey.String("gcp_bare_metal_solution")
	// Google Cloud Compute Engine (GCE)
	// Stability: development
	CloudPlatformGCPComputeEngine = CloudPlatformKey.String("gcp_compute_engine")
	// Google Cloud Run
	// Stability: development
	CloudPlatformGCPCloudRun = CloudPlatformKey.String("gcp_cloud_run")
	// Google Cloud Kubernetes Engine (GKE)
	// Stability: development
	CloudPlatformGCPKubernetesEngine = CloudPlatformKey.String("gcp_kubernetes_engine")
	// Google Cloud Functions (GCF)
	// Stability: development
	CloudPlatformGCPCloudFunctions = CloudPlatformKey.String("gcp_cloud_functions")
	// Google Cloud App Engine (GAE)
	// Stability: development
	CloudPlatformGCPAppEngine = CloudPlatformKey.String("gcp_app_engine")
	// Red Hat OpenShift on Google Cloud
	// Stability: development
	CloudPlatformGCPOpenshift = CloudPlatformKey.String("gcp_openshift")
	// Red Hat OpenShift on IBM Cloud
	// Stability: development
	CloudPlatformIbmCloudOpenshift = CloudPlatformKey.String("ibm_cloud_openshift")
	// Compute on Oracle Cloud Infrastructure (OCI)
	// Stability: development
	CloudPlatformOracleCloudCompute = CloudPlatformKey.String("oracle_cloud_compute")
	// Kubernetes Engine (OKE) on Oracle Cloud Infrastructure (OCI)
	// Stability: development
	CloudPlatformOracleCloudOke = CloudPlatformKey.String("oracle_cloud_oke")
	// Tencent Cloud Cloud Virtual Machine (CVM)
	// Stability: development
	CloudPlatformTencentCloudCvm = CloudPlatformKey.String("tencent_cloud_cvm")
	// Tencent Cloud Elastic Kubernetes Service (EKS)
	// Stability: development
	CloudPlatformTencentCloudEKS = CloudPlatformKey.String("tencent_cloud_eks")
	// Tencent Cloud Serverless Cloud Function (SCF)
	// Stability: development
	CloudPlatformTencentCloudScf = CloudPlatformKey.String("tencent_cloud_scf")
)

Enum values for cloud.platform

View Source
var (
	// Alibaba Cloud
	// Stability: development
	CloudProviderAlibabaCloud = CloudProviderKey.String("alibaba_cloud")
	// Amazon Web Services
	// Stability: development
	CloudProviderAWS = CloudProviderKey.String("aws")
	// Microsoft Azure
	// Stability: development
	CloudProviderAzure = CloudProviderKey.String("azure")
	// Google Cloud Platform
	// Stability: development
	CloudProviderGCP = CloudProviderKey.String("gcp")
	// Heroku Platform as a Service
	// Stability: development
	CloudProviderHeroku = CloudProviderKey.String("heroku")
	// IBM Cloud
	// Stability: development
	CloudProviderIbmCloud = CloudProviderKey.String("ibm_cloud")
	// Oracle Cloud Infrastructure (OCI)
	// Stability: development
	CloudProviderOracleCloud = CloudProviderKey.String("oracle_cloud")
	// Tencent Cloud
	// Stability: development
	CloudProviderTencentCloud = CloudProviderKey.String("tencent_cloud")
)

Enum values for cloud.provider

View Source
var (
	// user
	// Stability: development
	CPUModeUser = CPUModeKey.String("user")
	// system
	// Stability: development
	CPUModeSystem = CPUModeKey.String("system")
	// nice
	// Stability: development
	CPUModeNice = CPUModeKey.String("nice")
	// idle
	// Stability: development
	CPUModeIdle = CPUModeKey.String("idle")
	// iowait
	// Stability: development
	CPUModeIowait = CPUModeKey.String("iowait")
	// interrupt
	// Stability: development
	CPUModeInterrupt = CPUModeKey.String("interrupt")
	// steal
	// Stability: development
	CPUModeSteal = CPUModeKey.String("steal")
	// kernel
	// Stability: development
	CPUModeKernel = CPUModeKey.String("kernel")
)

Enum values for cpu.mode

View Source
var (
	// idle
	// Stability: development
	DBClientConnectionStateIdle = DBClientConnectionStateKey.String("idle")
	// used
	// Stability: development
	DBClientConnectionStateUsed = DBClientConnectionStateKey.String("used")
)

Enum values for db.client.connection.state

View Source
var (
	// Some other SQL database. Fallback only.
	// Stability: development
	DBSystemNameOtherSQL = DBSystemNameKey.String("other_sql")
	// [Adabas (Adaptable Database System)]
	// Stability: development
	//
	// [Adabas (Adaptable Database System)]: https://documentation.softwareag.com/?pf=adabas
	DBSystemNameSoftwareagAdabas = DBSystemNameKey.String("softwareag.adabas")
	// [Actian Ingres]
	// Stability: development
	//
	// [Actian Ingres]: https://www.actian.com/databases/ingres/
	DBSystemNameActianIngres = DBSystemNameKey.String("actian.ingres")
	// [Amazon DynamoDB]
	// Stability: development
	//
	// [Amazon DynamoDB]: https://aws.amazon.com/pm/dynamodb/
	DBSystemNameAWSDynamoDB = DBSystemNameKey.String("aws.dynamodb")
	// [Amazon Redshift]
	// Stability: development
	//
	// [Amazon Redshift]: https://aws.amazon.com/redshift/
	DBSystemNameAWSRedshift = DBSystemNameKey.String("aws.redshift")
	// [Azure Cosmos DB]
	// Stability: development
	//
	// [Azure Cosmos DB]: https://learn.microsoft.com/azure/cosmos-db
	DBSystemNameAzureCosmosDB = DBSystemNameKey.String("azure.cosmosdb")
	// [InterSystems Caché]
	// Stability: development
	//
	// [InterSystems Caché]: https://www.intersystems.com/products/cache/
	DBSystemNameIntersystemsCache = DBSystemNameKey.String("intersystems.cache")
	// [Apache Cassandra]
	// Stability: development
	//
	// [Apache Cassandra]: https://cassandra.apache.org/
	DBSystemNameCassandra = DBSystemNameKey.String("cassandra")
	// [ClickHouse]
	// Stability: development
	//
	// [ClickHouse]: https://clickhouse.com/
	DBSystemNameClickhouse = DBSystemNameKey.String("clickhouse")
	// [CockroachDB]
	// Stability: development
	//
	// [CockroachDB]: https://www.cockroachlabs.com/
	DBSystemNameCockroachdb = DBSystemNameKey.String("cockroachdb")
	// [Couchbase]
	// Stability: development
	//
	// [Couchbase]: https://www.couchbase.com/
	DBSystemNameCouchbase = DBSystemNameKey.String("couchbase")
	// [Apache CouchDB]
	// Stability: development
	//
	// [Apache CouchDB]: https://couchdb.apache.org/
	DBSystemNameCouchDB = DBSystemNameKey.String("couchdb")
	// [Apache Derby]
	// Stability: development
	//
	// [Apache Derby]: https://db.apache.org/derby/
	DBSystemNameDerby = DBSystemNameKey.String("derby")
	// [Elasticsearch]
	// Stability: development
	//
	// [Elasticsearch]: https://www.elastic.co/elasticsearch
	DBSystemNameElasticsearch = DBSystemNameKey.String("elasticsearch")
	// [Firebird]
	// Stability: development
	//
	// [Firebird]: https://www.firebirdsql.org/
	DBSystemNameFirebirdsql = DBSystemNameKey.String("firebirdsql")
	// [Google Cloud Spanner]
	// Stability: development
	//
	// [Google Cloud Spanner]: https://cloud.google.com/spanner
	DBSystemNameGCPSpanner = DBSystemNameKey.String("gcp.spanner")
	// [Apache Geode]
	// Stability: development
	//
	// [Apache Geode]: https://geode.apache.org/
	DBSystemNameGeode = DBSystemNameKey.String("geode")
	// [H2 Database]
	// Stability: development
	//
	// [H2 Database]: https://h2database.com/
	DBSystemNameH2database = DBSystemNameKey.String("h2database")
	// [Apache HBase]
	// Stability: development
	//
	// [Apache HBase]: https://hbase.apache.org/
	DBSystemNameHBase = DBSystemNameKey.String("hbase")
	// [Apache Hive]
	// Stability: development
	//
	// [Apache Hive]: https://hive.apache.org/
	DBSystemNameHive = DBSystemNameKey.String("hive")
	// [HyperSQL Database]
	// Stability: development
	//
	// [HyperSQL Database]: https://hsqldb.org/
	DBSystemNameHSQLDB = DBSystemNameKey.String("hsqldb")
	// [IBM Db2]
	// Stability: development
	//
	// [IBM Db2]: https://www.ibm.com/db2
	DBSystemNameIbmDb2 = DBSystemNameKey.String("ibm.db2")
	// [IBM Informix]
	// Stability: development
	//
	// [IBM Informix]: https://www.ibm.com/products/informix
	DBSystemNameIbmInformix = DBSystemNameKey.String("ibm.informix")
	// [IBM Netezza]
	// Stability: development
	//
	// [IBM Netezza]: https://www.ibm.com/products/netezza
	DBSystemNameIbmNetezza = DBSystemNameKey.String("ibm.netezza")
	// [InfluxDB]
	// Stability: development
	//
	// [InfluxDB]: https://www.influxdata.com/
	DBSystemNameInfluxdb = DBSystemNameKey.String("influxdb")
	// [Instant]
	// Stability: development
	//
	// [Instant]: https://www.instantdb.com/
	DBSystemNameInstantDB = DBSystemNameKey.String("instantdb")
	// [MariaDB]
	// Stability: release_candidate
	//
	// [MariaDB]: https://mariadb.org/
	DBSystemNameMariaDB = DBSystemNameKey.String("mariadb")
	// [Memcached]
	// Stability: development
	//
	// [Memcached]: https://memcached.org/
	DBSystemNameMemcached = DBSystemNameKey.String("memcached")
	// [MongoDB]
	// Stability: development
	//
	// [MongoDB]: https://www.mongodb.com/
	DBSystemNameMongoDB = DBSystemNameKey.String("mongodb")
	// [Microsoft SQL Server]
	// Stability: release_candidate
	//
	// [Microsoft SQL Server]: https://www.microsoft.com/sql-server
	DBSystemNameMicrosoftSQLServer = DBSystemNameKey.String("microsoft.sql_server")
	// [MySQL]
	// Stability: release_candidate
	//
	// [MySQL]: https://www.mysql.com/
	DBSystemNameMySQL = DBSystemNameKey.String("mysql")
	// [Neo4j]
	// Stability: development
	//
	// [Neo4j]: https://neo4j.com/
	DBSystemNameNeo4j = DBSystemNameKey.String("neo4j")
	// [OpenSearch]
	// Stability: development
	//
	// [OpenSearch]: https://opensearch.org/
	DBSystemNameOpensearch = DBSystemNameKey.String("opensearch")
	// [Oracle Database]
	// Stability: development
	//
	// [Oracle Database]: https://www.oracle.com/database/
	DBSystemNameOracleDB = DBSystemNameKey.String("oracle.db")
	// [PostgreSQL]
	// Stability: release_candidate
	//
	// [PostgreSQL]: https://www.postgresql.org/
	DBSystemNamePostgreSQL = DBSystemNameKey.String("postgresql")
	// [Redis]
	// Stability: development
	//
	// [Redis]: https://redis.io/
	DBSystemNameRedis = DBSystemNameKey.String("redis")
	// [SAP HANA]
	// Stability: development
	//
	// [SAP HANA]: https://www.sap.com/products/technology-platform/hana/what-is-sap-hana.html
	DBSystemNameSapHana = DBSystemNameKey.String("sap.hana")
	// [SAP MaxDB]
	// Stability: development
	//
	// [SAP MaxDB]: https://maxdb.sap.com/
	DBSystemNameSapMaxDB = DBSystemNameKey.String("sap.maxdb")
	// [SQLite]
	// Stability: development
	//
	// [SQLite]: https://www.sqlite.org/
	DBSystemNameSqlite = DBSystemNameKey.String("sqlite")
	// [Teradata]
	// Stability: development
	//
	// [Teradata]: https://www.teradata.com/
	DBSystemNameTeradata = DBSystemNameKey.String("teradata")
	// [Trino]
	// Stability: development
	//
	// [Trino]: https://trino.io/
	DBSystemNameTrino = DBSystemNameKey.String("trino")
)

Enum values for db.system.name

View Source
var (
	// failed
	// Stability: development
	DeploymentStatusFailed = DeploymentStatusKey.String("failed")
	// succeeded
	// Stability: development
	DeploymentStatusSucceeded = DeploymentStatusKey.String("succeeded")
)

Enum values for deployment.status

View Source
var (
	// read
	// Stability: development
	DiskIoDirectionRead = DiskIoDirectionKey.String("read")
	// write
	// Stability: development
	DiskIoDirectionWrite = DiskIoDirectionKey.String("write")
)

Enum values for disk.io.direction

View Source
var (
	// When a new object is created.
	// Stability: development
	FaaSDocumentOperationInsert = FaaSDocumentOperationKey.String("insert")
	// When an object is modified.
	// Stability: development
	FaaSDocumentOperationEdit = FaaSDocumentOperationKey.String("edit")
	// When an object is deleted.
	// Stability: development
	FaaSDocumentOperationDelete = FaaSDocumentOperationKey.String("delete")
)

Enum values for faas.document.operation

View Source
var (
	// Alibaba Cloud
	// Stability: development
	FaaSInvokedProviderAlibabaCloud = FaaSInvokedProviderKey.String("alibaba_cloud")
	// Amazon Web Services
	// Stability: development
	FaaSInvokedProviderAWS = FaaSInvokedProviderKey.String("aws")
	// Microsoft Azure
	// Stability: development
	FaaSInvokedProviderAzure = FaaSInvokedProviderKey.String("azure")
	// Google Cloud Platform
	// Stability: development
	FaaSInvokedProviderGCP = FaaSInvokedProviderKey.String("gcp")
	// Tencent Cloud
	// Stability: development
	FaaSInvokedProviderTencentCloud = FaaSInvokedProviderKey.String("tencent_cloud")
)

Enum values for faas.invoked_provider

View Source
var (
	// A response to some data source operation such as a database or filesystem
	// read/write
	// Stability: development
	FaaSTriggerDatasource = FaaSTriggerKey.String("datasource")
	// To provide an answer to an inbound HTTP request
	// Stability: development
	FaaSTriggerHTTP = FaaSTriggerKey.String("http")
	// A function is set to be executed when messages are sent to a messaging system
	// Stability: development
	FaaSTriggerPubsub = FaaSTriggerKey.String("pubsub")
	// A function is scheduled to be executed regularly
	// Stability: development
	FaaSTriggerTimer = FaaSTriggerKey.String("timer")
	// If none of the others apply
	// Stability: development
	FaaSTriggerOther = FaaSTriggerKey.String("other")
)

Enum values for faas.trigger

View Source
var (
	// The resolved value is static (no dynamic evaluation).
	// Stability: development
	FeatureFlagEvaluationReasonStatic = FeatureFlagEvaluationReasonKey.String("static")
	// The resolved value fell back to a pre-configured value (no dynamic evaluation
	// occurred or dynamic evaluation yielded no result).
	// Stability: development
	FeatureFlagEvaluationReasonDefault = FeatureFlagEvaluationReasonKey.String("default")
	// The resolved value was the result of a dynamic evaluation, such as a rule or
	// specific user-targeting.
	// Stability: development
	FeatureFlagEvaluationReasonTargetingMatch = FeatureFlagEvaluationReasonKey.String("targeting_match")
	// The resolved value was the result of pseudorandom assignment.
	// Stability: development
	FeatureFlagEvaluationReasonSplit = FeatureFlagEvaluationReasonKey.String("split")
	// The resolved value was retrieved from cache.
	// Stability: development
	FeatureFlagEvaluationReasonCached = FeatureFlagEvaluationReasonKey.String("cached")
	// The resolved value was the result of the flag being disabled in the
	// management system.
	// Stability: development
	FeatureFlagEvaluationReasonDisabled = FeatureFlagEvaluationReasonKey.String("disabled")
	// The reason for the resolved value could not be determined.
	// Stability: development
	FeatureFlagEvaluationReasonUnknown = FeatureFlagEvaluationReasonKey.String("unknown")
	// The resolved value is non-authoritative or possibly out of date
	// Stability: development
	FeatureFlagEvaluationReasonStale = FeatureFlagEvaluationReasonKey.String("stale")
	// The resolved value was the result of an error.
	// Stability: development
	FeatureFlagEvaluationReasonError = FeatureFlagEvaluationReasonKey.String("error")
)

Enum values for feature_flag.evaluation.reason

View Source
var (
	// The system will utilize scale tier credits until they are exhausted.
	// Stability: development
	GenAIOpenaiRequestServiceTierAuto = GenAIOpenaiRequestServiceTierKey.String("auto")
	// The system will utilize the default scale tier.
	// Stability: development
	GenAIOpenaiRequestServiceTierDefault = GenAIOpenaiRequestServiceTierKey.String("default")
)

Enum values for gen_ai.openai.request.service_tier

View Source
var (
	// Chat completion operation such as [OpenAI Chat API]
	// Stability: development
	//
	// [OpenAI Chat API]: https://platform.openai.com/docs/api-reference/chat
	GenAIOperationNameChat = GenAIOperationNameKey.String("chat")
	// Text completions operation such as [OpenAI Completions API (Legacy)]
	// Stability: development
	//
	// [OpenAI Completions API (Legacy)]: https://platform.openai.com/docs/api-reference/completions
	GenAIOperationNameTextCompletion = GenAIOperationNameKey.String("text_completion")
	// Embeddings operation such as [OpenAI Create embeddings API]
	// Stability: development
	//
	// [OpenAI Create embeddings API]: https://platform.openai.com/docs/api-reference/embeddings/create
	GenAIOperationNameEmbeddings = GenAIOperationNameKey.String("embeddings")
	// Create GenAI agent
	// Stability: development
	GenAIOperationNameCreateAgent = GenAIOperationNameKey.String("create_agent")
	// Execute a tool
	// Stability: development
	GenAIOperationNameExecuteTool = GenAIOperationNameKey.String("execute_tool")
)

Enum values for gen_ai.operation.name

View Source
var (
	// Plain text
	// Stability: development
	GenAIOutputTypeText = GenAIOutputTypeKey.String("text")
	// JSON object with known or unknown schema
	// Stability: development
	GenAIOutputTypeJSON = GenAIOutputTypeKey.String("json")
	// Image
	// Stability: development
	GenAIOutputTypeImage = GenAIOutputTypeKey.String("image")
	// Speech
	// Stability: development
	GenAIOutputTypeSpeech = GenAIOutputTypeKey.String("speech")
)

Enum values for gen_ai.output.type

View Source
var (
	// OpenAI
	// Stability: development
	GenAISystemOpenai = GenAISystemKey.String("openai")
	// Vertex AI
	// Stability: development
	GenAISystemVertexAI = GenAISystemKey.String("vertex_ai")
	// Gemini
	// Stability: development
	GenAISystemGemini = GenAISystemKey.String("gemini")
	// Anthropic
	// Stability: development
	GenAISystemAnthropic = GenAISystemKey.String("anthropic")
	// Cohere
	// Stability: development
	GenAISystemCohere = GenAISystemKey.String("cohere")
	// Azure AI Inference
	// Stability: development
	GenAISystemAzAIInference = GenAISystemKey.String("az.ai.inference")
	// Azure OpenAI
	// Stability: development
	GenAISystemAzAIOpenai = GenAISystemKey.String("az.ai.openai")
	// IBM Watsonx AI
	// Stability: development
	GenAISystemIbmWatsonxAI = GenAISystemKey.String("ibm.watsonx.ai")
	// AWS Bedrock
	// Stability: development
	GenAISystemAWSBedrock = GenAISystemKey.String("aws.bedrock")
	// Perplexity
	// Stability: development
	GenAISystemPerplexity = GenAISystemKey.String("perplexity")
	// xAI
	// Stability: development
	GenAISystemXai = GenAISystemKey.String("xai")
	// DeepSeek
	// Stability: development
	GenAISystemDeepseek = GenAISystemKey.String("deepseek")
	// Groq
	// Stability: development
	GenAISystemGroq = GenAISystemKey.String("groq")
	// Mistral AI
	// Stability: development
	GenAISystemMistralAI = GenAISystemKey.String("mistral_ai")
)

Enum values for gen_ai.system

View Source
var (
	// Input tokens (prompt, input, etc.)
	// Stability: development
	GenAITokenTypeInput = GenAITokenTypeKey.String("input")
	// Deprecated: Replaced by `output`.
	GenAITokenTypeCompletion = GenAITokenTypeKey.String("output")
	// Output tokens (completion, response, etc.)
	// Stability: development
	GenAITokenTypeOutput = GenAITokenTypeKey.String("output")
)

Enum values for gen_ai.token.type

View Source
var (
	// Africa
	// Stability: development
	GeoContinentCodeAf = GeoContinentCodeKey.String("AF")
	// Antarctica
	// Stability: development
	GeoContinentCodeAn = GeoContinentCodeKey.String("AN")
	// Asia
	// Stability: development
	GeoContinentCodeAs = GeoContinentCodeKey.String("AS")
	// Europe
	// Stability: development
	GeoContinentCodeEu = GeoContinentCodeKey.String("EU")
	// North America
	// Stability: development
	GeoContinentCodeNa = GeoContinentCodeKey.String("NA")
	// Oceania
	// Stability: development
	GeoContinentCodeOc = GeoContinentCodeKey.String("OC")
	// South America
	// Stability: development
	GeoContinentCodeSa = GeoContinentCodeKey.String("SA")
)

Enum values for geo.continent.code

View Source
var (
	// Memory allocated from the heap that is reserved for stack space, whether or
	// not it is currently in-use.
	// Stability: development
	GoMemoryTypeStack = GoMemoryTypeKey.String("stack")
	// Memory used by the Go runtime, excluding other categories of memory usage
	// described in this enumeration.
	// Stability: development
	GoMemoryTypeOther = GoMemoryTypeKey.String("other")
)

Enum values for go.memory.type

View Source
var (
	// GraphQL query
	// Stability: development
	GraphqlOperationTypeQuery = GraphqlOperationTypeKey.String("query")
	// GraphQL mutation
	// Stability: development
	GraphqlOperationTypeMutation = GraphqlOperationTypeKey.String("mutation")
	// GraphQL subscription
	// Stability: development
	GraphqlOperationTypeSubscription = GraphqlOperationTypeKey.String("subscription")
)

Enum values for graphql.operation.type

View Source
var (
	// AMD64
	// Stability: development
	HostArchAMD64 = HostArchKey.String("amd64")
	// ARM32
	// Stability: development
	HostArchARM32 = HostArchKey.String("arm32")
	// ARM64
	// Stability: development
	HostArchARM64 = HostArchKey.String("arm64")
	// Itanium
	// Stability: development
	HostArchIA64 = HostArchKey.String("ia64")
	// 32-bit PowerPC
	// Stability: development
	HostArchPPC32 = HostArchKey.String("ppc32")
	// 64-bit PowerPC
	// Stability: development
	HostArchPPC64 = HostArchKey.String("ppc64")
	// IBM z/Architecture
	// Stability: development
	HostArchS390x = HostArchKey.String("s390x")
	// 32-bit x86
	// Stability: development
	HostArchX86 = HostArchKey.String("x86")
)

Enum values for host.arch

View Source
var (
	// active state.
	// Stability: development
	HTTPConnectionStateActive = HTTPConnectionStateKey.String("active")
	// idle state.
	// Stability: development
	HTTPConnectionStateIdle = HTTPConnectionStateKey.String("idle")
)

Enum values for http.connection.state

View Source
var (
	// CONNECT method.
	// Stability: stable
	HTTPRequestMethodConnect = HTTPRequestMethodKey.String("CONNECT")
	// DELETE method.
	// Stability: stable
	HTTPRequestMethodDelete = HTTPRequestMethodKey.String("DELETE")
	// GET method.
	// Stability: stable
	HTTPRequestMethodGet = HTTPRequestMethodKey.String("GET")
	// HEAD method.
	// Stability: stable
	HTTPRequestMethodHead = HTTPRequestMethodKey.String("HEAD")
	// OPTIONS method.
	// Stability: stable
	HTTPRequestMethodOptions = HTTPRequestMethodKey.String("OPTIONS")
	// PATCH method.
	// Stability: stable
	HTTPRequestMethodPatch = HTTPRequestMethodKey.String("PATCH")
	// POST method.
	// Stability: stable
	HTTPRequestMethodPost = HTTPRequestMethodKey.String("POST")
	// PUT method.
	// Stability: stable
	HTTPRequestMethodPut = HTTPRequestMethodKey.String("PUT")
	// TRACE method.
	// Stability: stable
	HTTPRequestMethodTrace = HTTPRequestMethodKey.String("TRACE")
	// Any HTTP method that the instrumentation has no prior knowledge of.
	// Stability: stable
	HTTPRequestMethodOther = HTTPRequestMethodKey.String("_OTHER")
)

Enum values for http.request.method

View Source
var (
	// Ok
	// Stability: development
	HwStateOk = HwStateKey.String("ok")
	// Degraded
	// Stability: development
	HwStateDegraded = HwStateKey.String("degraded")
	// Failed
	// Stability: development
	HwStateFailed = HwStateKey.String("failed")
)

Enum values for hw.state

View Source
var (
	// Battery
	// Stability: development
	HwTypeBattery = HwTypeKey.String("battery")
	// CPU
	// Stability: development
	HwTypeCPU = HwTypeKey.String("cpu")
	// Disk controller
	// Stability: development
	HwTypeDiskController = HwTypeKey.String("disk_controller")
	// Enclosure
	// Stability: development
	HwTypeEnclosure = HwTypeKey.String("enclosure")
	// Fan
	// Stability: development
	HwTypeFan = HwTypeKey.String("fan")
	// GPU
	// Stability: development
	HwTypeGpu = HwTypeKey.String("gpu")
	// Logical disk
	// Stability: development
	HwTypeLogicalDisk = HwTypeKey.String("logical_disk")
	// Memory
	// Stability: development
	HwTypeMemory = HwTypeKey.String("memory")
	// Network
	// Stability: development
	HwTypeNetwork = HwTypeKey.String("network")
	// Physical disk
	// Stability: development
	HwTypePhysicalDisk = HwTypeKey.String("physical_disk")
	// Power supply
	// Stability: development
	HwTypePowerSupply = HwTypeKey.String("power_supply")
	// Tape drive
	// Stability: development
	HwTypeTapeDrive = HwTypeKey.String("tape_drive")
	// Temperature
	// Stability: development
	HwTypeTemperature = HwTypeKey.String("temperature")
	// Voltage
	// Stability: development
	HwTypeVoltage = HwTypeKey.String("voltage")
)

Enum values for hw.type

View Source
var (
	// The app has become `active`. Associated with UIKit notification
	// `applicationDidBecomeActive`.
	//
	// Stability: development
	IosAppStateActive = IosAppStateKey.String("active")
	// The app is now `inactive`. Associated with UIKit notification
	// `applicationWillResignActive`.
	//
	// Stability: development
	IosAppStateInactive = IosAppStateKey.String("inactive")
	// The app is now in the background. This value is associated with UIKit
	// notification `applicationDidEnterBackground`.
	//
	// Stability: development
	IosAppStateBackground = IosAppStateKey.String("background")
	// The app is now in the foreground. This value is associated with UIKit
	// notification `applicationWillEnterForeground`.
	//
	// Stability: development
	IosAppStateForeground = IosAppStateKey.String("foreground")
	// The app is about to terminate. Associated with UIKit notification
	// `applicationWillTerminate`.
	//
	// Stability: development
	IosAppStateTerminate = IosAppStateKey.String("terminate")
)

Enum values for ios.app.state

View Source
var (
	// Active namespace phase as described by [K8s API]
	// Stability: development
	//
	// [K8s API]: https://pkg.go.dev/k8s.io/api@v0.31.3/core/v1#NamespacePhase
	K8SNamespacePhaseActive = K8SNamespacePhaseKey.String("active")
	// Terminating namespace phase as described by [K8s API]
	// Stability: development
	//
	// [K8s API]: https://pkg.go.dev/k8s.io/api@v0.31.3/core/v1#NamespacePhase
	K8SNamespacePhaseTerminating = K8SNamespacePhaseKey.String("terminating")
)

Enum values for k8s.namespace.phase

View Source
var (
	// A [persistentVolumeClaim] volume
	// Stability: development
	//
	// [persistentVolumeClaim]: https://v1-30.docs.kubernetes.io/docs/concepts/storage/volumes/#persistentvolumeclaim
	K8SVolumeTypePersistentVolumeClaim = K8SVolumeTypeKey.String("persistentVolumeClaim")
	// A [configMap] volume
	// Stability: development
	//
	// [configMap]: https://v1-30.docs.kubernetes.io/docs/concepts/storage/volumes/#configmap
	K8SVolumeTypeConfigMap = K8SVolumeTypeKey.String("configMap")
	// A [downwardAPI] volume
	// Stability: development
	//
	// [downwardAPI]: https://v1-30.docs.kubernetes.io/docs/concepts/storage/volumes/#downwardapi
	K8SVolumeTypeDownwardAPI = K8SVolumeTypeKey.String("downwardAPI")
	// An [emptyDir] volume
	// Stability: development
	//
	// [emptyDir]: https://v1-30.docs.kubernetes.io/docs/concepts/storage/volumes/#emptydir
	K8SVolumeTypeEmptyDir = K8SVolumeTypeKey.String("emptyDir")
	// A [secret] volume
	// Stability: development
	//
	// [secret]: https://v1-30.docs.kubernetes.io/docs/concepts/storage/volumes/#secret
	K8SVolumeTypeSecret = K8SVolumeTypeKey.String("secret")
	// A [local] volume
	// Stability: development
	//
	// [local]: https://v1-30.docs.kubernetes.io/docs/concepts/storage/volumes/#local
	K8SVolumeTypeLocal = K8SVolumeTypeKey.String("local")
)

Enum values for k8s.volume.type

View Source
var (
	// reclaimable
	// Stability: development
	LinuxMemorySlabStateReclaimable = LinuxMemorySlabStateKey.String("reclaimable")
	// unreclaimable
	// Stability: development
	LinuxMemorySlabStateUnreclaimable = LinuxMemorySlabStateKey.String("unreclaimable")
)

Enum values for linux.memory.slab.state

View Source
var (
	// Logs from stdout stream
	// Stability: development
	LogIostreamStdout = LogIostreamKey.String("stdout")
	// Events from stderr stream
	// Stability: development
	LogIostreamStderr = LogIostreamKey.String("stderr")
)

Enum values for log.iostream

View Source
var (
	// A message is created. "Create" spans always refer to a single message and are
	// used to provide a unique creation context for messages in batch sending
	// scenarios.
	//
	// Stability: development
	MessagingOperationTypeCreate = MessagingOperationTypeKey.String("create")
	// One or more messages are provided for sending to an intermediary. If a single
	// message is sent, the context of the "Send" span can be used as the creation
	// context and no "Create" span needs to be created.
	//
	// Stability: development
	MessagingOperationTypeSend = MessagingOperationTypeKey.String("send")
	// One or more messages are requested by a consumer. This operation refers to
	// pull-based scenarios, where consumers explicitly call methods of messaging
	// SDKs to receive messages.
	//
	// Stability: development
	MessagingOperationTypeReceive = MessagingOperationTypeKey.String("receive")
	// One or more messages are processed by a consumer.
	//
	// Stability: development
	MessagingOperationTypeProcess = MessagingOperationTypeKey.String("process")
	// One or more messages are settled.
	//
	// Stability: development
	MessagingOperationTypeSettle = MessagingOperationTypeKey.String("settle")
	// Deprecated: Replaced by `process`.
	MessagingOperationTypeDeliver = MessagingOperationTypeKey.String("deliver")
	// Deprecated: Replaced by `send`.
	MessagingOperationTypePublish = MessagingOperationTypeKey.String("publish")
)

Enum values for messaging.operation.type

View Source
var (
	// Clustering consumption model
	// Stability: development
	MessagingRocketmqConsumptionModelClustering = MessagingRocketmqConsumptionModelKey.String("clustering")
	// Broadcasting consumption model
	// Stability: development
	MessagingRocketmqConsumptionModelBroadcasting = MessagingRocketmqConsumptionModelKey.String("broadcasting")
)

Enum values for messaging.rocketmq.consumption_model

View Source
var (
	// Normal message
	// Stability: development
	MessagingRocketmqMessageTypeNormal = MessagingRocketmqMessageTypeKey.String("normal")
	// FIFO message
	// Stability: development
	MessagingRocketmqMessageTypeFifo = MessagingRocketmqMessageTypeKey.String("fifo")
	// Delay message
	// Stability: development
	MessagingRocketmqMessageTypeDelay = MessagingRocketmqMessageTypeKey.String("delay")
	// Transaction message
	// Stability: development
	MessagingRocketmqMessageTypeTransaction = MessagingRocketmqMessageTypeKey.String("transaction")
)

Enum values for messaging.rocketmq.message.type

View Source
var (
	// Message is completed
	// Stability: development
	MessagingServicebusDispositionStatusComplete = MessagingServicebusDispositionStatusKey.String("complete")
	// Message is abandoned
	// Stability: development
	MessagingServicebusDispositionStatusAbandon = MessagingServicebusDispositionStatusKey.String("abandon")
	// Message is sent to dead letter queue
	// Stability: development
	MessagingServicebusDispositionStatusDeadLetter = MessagingServicebusDispositionStatusKey.String("dead_letter")
	// Message is deferred
	// Stability: development
	MessagingServicebusDispositionStatusDefer = MessagingServicebusDispositionStatusKey.String("defer")
)

Enum values for messaging.servicebus.disposition_status

View Source
var (
	// Apache ActiveMQ
	// Stability: development
	MessagingSystemActivemq = MessagingSystemKey.String("activemq")
	// Amazon Simple Queue Service (SQS)
	// Stability: development
	MessagingSystemAWSSqs = MessagingSystemKey.String("aws_sqs")
	// Azure Event Grid
	// Stability: development
	MessagingSystemEventgrid = MessagingSystemKey.String("eventgrid")
	// Azure Event Hubs
	// Stability: development
	MessagingSystemEventhubs = MessagingSystemKey.String("eventhubs")
	// Azure Service Bus
	// Stability: development
	MessagingSystemServicebus = MessagingSystemKey.String("servicebus")
	// Google Cloud Pub/Sub
	// Stability: development
	MessagingSystemGCPPubsub = MessagingSystemKey.String("gcp_pubsub")
	// Java Message Service
	// Stability: development
	MessagingSystemJms = MessagingSystemKey.String("jms")
	// Apache Kafka
	// Stability: development
	MessagingSystemKafka = MessagingSystemKey.String("kafka")
	// RabbitMQ
	// Stability: development
	MessagingSystemRabbitmq = MessagingSystemKey.String("rabbitmq")
	// Apache RocketMQ
	// Stability: development
	MessagingSystemRocketmq = MessagingSystemKey.String("rocketmq")
	// Apache Pulsar
	// Stability: development
	MessagingSystemPulsar = MessagingSystemKey.String("pulsar")
)

Enum values for messaging.system

View Source
var (
	// closed
	// Stability: development
	NetworkConnectionStateClosed = NetworkConnectionStateKey.String("closed")
	// close_wait
	// Stability: development
	NetworkConnectionStateCloseWait = NetworkConnectionStateKey.String("close_wait")
	// closing
	// Stability: development
	NetworkConnectionStateClosing = NetworkConnectionStateKey.String("closing")
	// established
	// Stability: development
	NetworkConnectionStateEstablished = NetworkConnectionStateKey.String("established")
	// fin_wait_1
	// Stability: development
	NetworkConnectionStateFinWait1 = NetworkConnectionStateKey.String("fin_wait_1")
	// fin_wait_2
	// Stability: development
	NetworkConnectionStateFinWait2 = NetworkConnectionStateKey.String("fin_wait_2")
	// last_ack
	// Stability: development
	NetworkConnectionStateLastAck = NetworkConnectionStateKey.String("last_ack")
	// listen
	// Stability: development
	NetworkConnectionStateListen = NetworkConnectionStateKey.String("listen")
	// syn_received
	// Stability: development
	NetworkConnectionStateSynReceived = NetworkConnectionStateKey.String("syn_received")
	// syn_sent
	// Stability: development
	NetworkConnectionStateSynSent = NetworkConnectionStateKey.String("syn_sent")
	// time_wait
	// Stability: development
	NetworkConnectionStateTimeWait = NetworkConnectionStateKey.String("time_wait")
)

Enum values for network.connection.state

View Source
var (
	// GPRS
	// Stability: development
	NetworkConnectionSubtypeGprs = NetworkConnectionSubtypeKey.String("gprs")
	// EDGE
	// Stability: development
	NetworkConnectionSubtypeEdge = NetworkConnectionSubtypeKey.String("edge")
	// UMTS
	// Stability: development
	NetworkConnectionSubtypeUmts = NetworkConnectionSubtypeKey.String("umts")
	// CDMA
	// Stability: development
	NetworkConnectionSubtypeCdma = NetworkConnectionSubtypeKey.String("cdma")
	// EVDO Rel. 0
	// Stability: development
	NetworkConnectionSubtypeEvdo0 = NetworkConnectionSubtypeKey.String("evdo_0")
	// EVDO Rev. A
	// Stability: development
	NetworkConnectionSubtypeEvdoA = NetworkConnectionSubtypeKey.String("evdo_a")
	// CDMA2000 1XRTT
	// Stability: development
	NetworkConnectionSubtypeCdma20001xrtt = NetworkConnectionSubtypeKey.String("cdma2000_1xrtt")
	// HSDPA
	// Stability: development
	NetworkConnectionSubtypeHsdpa = NetworkConnectionSubtypeKey.String("hsdpa")
	// HSUPA
	// Stability: development
	NetworkConnectionSubtypeHsupa = NetworkConnectionSubtypeKey.String("hsupa")
	// HSPA
	// Stability: development
	NetworkConnectionSubtypeHspa = NetworkConnectionSubtypeKey.String("hspa")
	// IDEN
	// Stability: development
	NetworkConnectionSubtypeIden = NetworkConnectionSubtypeKey.String("iden")
	// EVDO Rev. B
	// Stability: development
	NetworkConnectionSubtypeEvdoB = NetworkConnectionSubtypeKey.String("evdo_b")
	// LTE
	// Stability: development
	NetworkConnectionSubtypeLte = NetworkConnectionSubtypeKey.String("lte")
	// EHRPD
	// Stability: development
	NetworkConnectionSubtypeEhrpd = NetworkConnectionSubtypeKey.String("ehrpd")
	// HSPAP
	// Stability: development
	NetworkConnectionSubtypeHspap = NetworkConnectionSubtypeKey.String("hspap")
	// GSM
	// Stability: development
	NetworkConnectionSubtypeGsm = NetworkConnectionSubtypeKey.String("gsm")
	// TD-SCDMA
	// Stability: development
	NetworkConnectionSubtypeTdScdma = NetworkConnectionSubtypeKey.String("td_scdma")
	// IWLAN
	// Stability: development
	NetworkConnectionSubtypeIwlan = NetworkConnectionSubtypeKey.String("iwlan")
	// 5G NR (New Radio)
	// Stability: development
	NetworkConnectionSubtypeNr = NetworkConnectionSubtypeKey.String("nr")
	// 5G NRNSA (New Radio Non-Standalone)
	// Stability: development
	NetworkConnectionSubtypeNrnsa = NetworkConnectionSubtypeKey.String("nrnsa")
	// LTE CA
	// Stability: development
	NetworkConnectionSubtypeLteCa = NetworkConnectionSubtypeKey.String("lte_ca")
)

Enum values for network.connection.subtype

View Source
var (
	// wifi
	// Stability: development
	NetworkConnectionTypeWifi = NetworkConnectionTypeKey.String("wifi")
	// wired
	// Stability: development
	NetworkConnectionTypeWired = NetworkConnectionTypeKey.String("wired")
	// cell
	// Stability: development
	NetworkConnectionTypeCell = NetworkConnectionTypeKey.String("cell")
	// unavailable
	// Stability: development
	NetworkConnectionTypeUnavailable = NetworkConnectionTypeKey.String("unavailable")
	// unknown
	// Stability: development
	NetworkConnectionTypeUnknown = NetworkConnectionTypeKey.String("unknown")
)

Enum values for network.connection.type

View Source
var (
	// transmit
	// Stability: development
	NetworkIoDirectionTransmit = NetworkIoDirectionKey.String("transmit")
	// receive
	// Stability: development
	NetworkIoDirectionReceive = NetworkIoDirectionKey.String("receive")
)

Enum values for network.io.direction

View Source
var (
	// TCP
	// Stability: stable
	NetworkTransportTCP = NetworkTransportKey.String("tcp")
	// UDP
	// Stability: stable
	NetworkTransportUDP = NetworkTransportKey.String("udp")
	// Named or anonymous pipe.
	// Stability: stable
	NetworkTransportPipe = NetworkTransportKey.String("pipe")
	// Unix domain socket
	// Stability: stable
	NetworkTransportUnix = NetworkTransportKey.String("unix")
	// QUIC
	// Stability: development
	NetworkTransportQUIC = NetworkTransportKey.String("quic")
)

Enum values for network.transport

View Source
var (
	// IPv4
	// Stability: stable
	NetworkTypeIpv4 = NetworkTypeKey.String("ipv4")
	// IPv6
	// Stability: stable
	NetworkTypeIpv6 = NetworkTypeKey.String("ipv6")
)

Enum values for network.type

View Source
var (
	// The parent Span depends on the child Span in some capacity
	// Stability: development
	OpentracingRefTypeChildOf = OpentracingRefTypeKey.String("child_of")
	// The parent Span doesn't depend in any way on the result of the child Span
	// Stability: development
	OpentracingRefTypeFollowsFrom = OpentracingRefTypeKey.String("follows_from")
)

Enum values for opentracing.ref_type

View Source
var (
	// Microsoft Windows
	// Stability: development
	OSTypeWindows = OSTypeKey.String("windows")
	// Linux
	// Stability: development
	OSTypeLinux = OSTypeKey.String("linux")
	// Apple Darwin
	// Stability: development
	OSTypeDarwin = OSTypeKey.String("darwin")
	// FreeBSD
	// Stability: development
	OSTypeFreeBSD = OSTypeKey.String("freebsd")
	// NetBSD
	// Stability: development
	OSTypeNetBSD = OSTypeKey.String("netbsd")
	// OpenBSD
	// Stability: development
	OSTypeOpenBSD = OSTypeKey.String("openbsd")
	// DragonFly BSD
	// Stability: development
	OSTypeDragonflyBSD = OSTypeKey.String("dragonflybsd")
	// HP-UX (Hewlett Packard Unix)
	// Stability: development
	OSTypeHPUX = OSTypeKey.String("hpux")
	// AIX (Advanced Interactive eXecutive)
	// Stability: development
	OSTypeAIX = OSTypeKey.String("aix")
	// SunOS, Oracle Solaris
	// Stability: development
	OSTypeSolaris = OSTypeKey.String("solaris")
	// IBM z/OS
	// Stability: development
	OSTypeZOS = OSTypeKey.String("z_os")
)

Enum values for os.type

View Source
var (
	// The builtin SDK Batching Span Processor
	//
	// Stability: development
	OTelComponentTypeBatchingSpanProcessor = OTelComponentTypeKey.String("batching_span_processor")
	// The builtin SDK Simple Span Processor
	//
	// Stability: development
	OTelComponentTypeSimpleSpanProcessor = OTelComponentTypeKey.String("simple_span_processor")
	// OTLP span exporter over gRPC with protobuf serialization
	//
	// Stability: development
	OTelComponentTypeOtlpGRPCSpanExporter = OTelComponentTypeKey.String("otlp_grpc_span_exporter")
	// OTLP span exporter over HTTP with protobuf serialization
	//
	// Stability: development
	OTelComponentTypeOtlpHTTPSpanExporter = OTelComponentTypeKey.String("otlp_http_span_exporter")
	// OTLP span exporter over HTTP with JSON serialization
	//
	// Stability: development
	OTelComponentTypeOtlpHTTPJSONSpanExporter = OTelComponentTypeKey.String("otlp_http_json_span_exporter")
)

Enum values for otel.component.type

View Source
var (
	// The span is not sampled and not recording
	// Stability: development
	OTelSpanSamplingResultDrop = OTelSpanSamplingResultKey.String("DROP")
	// The span is not sampled, but recording
	// Stability: development
	OTelSpanSamplingResultRecordOnly = OTelSpanSamplingResultKey.String("RECORD_ONLY")
	// The span is sampled and recording
	// Stability: development
	OTelSpanSamplingResultRecordAndSample = OTelSpanSamplingResultKey.String("RECORD_AND_SAMPLE")
)

Enum values for otel.span.sampling_result

View Source
var (
	// The operation has been validated by an Application developer or Operator to
	// have completed successfully.
	// Stability: stable
	OTelStatusCodeOk = OTelStatusCodeKey.String("OK")
	// The operation contains an error.
	// Stability: stable
	OTelStatusCodeError = OTelStatusCodeKey.String("ERROR")
)

Enum values for otel.status_code

View Source
var (
	// voluntary
	// Stability: development
	ProcessContextSwitchTypeVoluntary = ProcessContextSwitchTypeKey.String("voluntary")
	// involuntary
	// Stability: development
	ProcessContextSwitchTypeInvoluntary = ProcessContextSwitchTypeKey.String("involuntary")
)

Enum values for process.context_switch_type

View Source
var (
	// major
	// Stability: development
	ProcessPagingFaultTypeMajor = ProcessPagingFaultTypeKey.String("major")
	// minor
	// Stability: development
	ProcessPagingFaultTypeMinor = ProcessPagingFaultTypeKey.String("minor")
)

Enum values for process.paging.fault_type

View Source
var (
	// [.NET]
	//
	// Stability: development
	//
	// [.NET]: https://wikipedia.org/wiki/.NET
	ProfileFrameTypeDotnet = ProfileFrameTypeKey.String("dotnet")
	// [JVM]
	//
	// Stability: development
	//
	// [JVM]: https://wikipedia.org/wiki/Java_virtual_machine
	ProfileFrameTypeJVM = ProfileFrameTypeKey.String("jvm")
	// [Kernel]
	//
	// Stability: development
	//
	// [Kernel]: https://wikipedia.org/wiki/Kernel_(operating_system)
	ProfileFrameTypeKernel = ProfileFrameTypeKey.String("kernel")
	// [C], [C++], [Go], [Rust]
	//
	// Stability: development
	//
	// [C]: https://wikipedia.org/wiki/C_(programming_language)
	// [C++]: https://wikipedia.org/wiki/C%2B%2B
	// [Go]: https://wikipedia.org/wiki/Go_(programming_language)
	// [Rust]: https://wikipedia.org/wiki/Rust_(programming_language)
	ProfileFrameTypeNative = ProfileFrameTypeKey.String("native")
	// [Perl]
	//
	// Stability: development
	//
	// [Perl]: https://wikipedia.org/wiki/Perl
	ProfileFrameTypePerl = ProfileFrameTypeKey.String("perl")
	// [PHP]
	//
	// Stability: development
	//
	// [PHP]: https://wikipedia.org/wiki/PHP
	ProfileFrameTypePHP = ProfileFrameTypeKey.String("php")
	// [Python]
	//
	// Stability: development
	//
	// [Python]: https://wikipedia.org/wiki/Python_(programming_language)
	ProfileFrameTypeCpython = ProfileFrameTypeKey.String("cpython")
	// [Ruby]
	//
	// Stability: development
	//
	// [Ruby]: https://wikipedia.org/wiki/Ruby_(programming_language)
	ProfileFrameTypeRuby = ProfileFrameTypeKey.String("ruby")
	// [V8JS]
	//
	// Stability: development
	//
	// [V8JS]: https://wikipedia.org/wiki/V8_(JavaScript_engine)
	ProfileFrameTypeV8JS = ProfileFrameTypeKey.String("v8js")
	// [Erlang]
	//
	// Stability: development
	//
	// [Erlang]: https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine)
	ProfileFrameTypeBeam = ProfileFrameTypeKey.String("beam")
)

Enum values for profile.frame.type

View Source
var (
	// cancelled
	// Stability: development
	RPCConnectRPCErrorCodeCancelled = RPCConnectRPCErrorCodeKey.String("cancelled")
	// unknown
	// Stability: development
	RPCConnectRPCErrorCodeUnknown = RPCConnectRPCErrorCodeKey.String("unknown")
	// invalid_argument
	// Stability: development
	RPCConnectRPCErrorCodeInvalidArgument = RPCConnectRPCErrorCodeKey.String("invalid_argument")
	// deadline_exceeded
	// Stability: development
	RPCConnectRPCErrorCodeDeadlineExceeded = RPCConnectRPCErrorCodeKey.String("deadline_exceeded")
	// not_found
	// Stability: development
	RPCConnectRPCErrorCodeNotFound = RPCConnectRPCErrorCodeKey.String("not_found")
	// already_exists
	// Stability: development
	RPCConnectRPCErrorCodeAlreadyExists = RPCConnectRPCErrorCodeKey.String("already_exists")
	// permission_denied
	// Stability: development
	RPCConnectRPCErrorCodePermissionDenied = RPCConnectRPCErrorCodeKey.String("permission_denied")
	// resource_exhausted
	// Stability: development
	RPCConnectRPCErrorCodeResourceExhausted = RPCConnectRPCErrorCodeKey.String("resource_exhausted")
	// failed_precondition
	// Stability: development
	RPCConnectRPCErrorCodeFailedPrecondition = RPCConnectRPCErrorCodeKey.String("failed_precondition")
	// aborted
	// Stability: development
	RPCConnectRPCErrorCodeAborted = RPCConnectRPCErrorCodeKey.String("aborted")
	// out_of_range
	// Stability: development
	RPCConnectRPCErrorCodeOutOfRange = RPCConnectRPCErrorCodeKey.String("out_of_range")
	// unimplemented
	// Stability: development
	RPCConnectRPCErrorCodeUnimplemented = RPCConnectRPCErrorCodeKey.String("unimplemented")
	// internal
	// Stability: development
	RPCConnectRPCErrorCodeInternal = RPCConnectRPCErrorCodeKey.String("internal")
	// unavailable
	// Stability: development
	RPCConnectRPCErrorCodeUnavailable = RPCConnectRPCErrorCodeKey.String("unavailable")
	// data_loss
	// Stability: development
	RPCConnectRPCErrorCodeDataLoss = RPCConnectRPCErrorCodeKey.String("data_loss")
	// unauthenticated
	// Stability: development
	RPCConnectRPCErrorCodeUnauthenticated = RPCConnectRPCErrorCodeKey.String("unauthenticated")
)

Enum values for rpc.connect_rpc.error_code

View Source
var (
	// OK
	// Stability: development
	RPCGRPCStatusCodeOk = RPCGRPCStatusCodeKey.Int(0)
	// CANCELLED
	// Stability: development
	RPCGRPCStatusCodeCancelled = RPCGRPCStatusCodeKey.Int(1)
	// UNKNOWN
	// Stability: development
	RPCGRPCStatusCodeUnknown = RPCGRPCStatusCodeKey.Int(2)
	// INVALID_ARGUMENT
	// Stability: development
	RPCGRPCStatusCodeInvalidArgument = RPCGRPCStatusCodeKey.Int(3)
	// DEADLINE_EXCEEDED
	// Stability: development
	RPCGRPCStatusCodeDeadlineExceeded = RPCGRPCStatusCodeKey.Int(4)
	// NOT_FOUND
	// Stability: development
	RPCGRPCStatusCodeNotFound = RPCGRPCStatusCodeKey.Int(5)
	// ALREADY_EXISTS
	// Stability: development
	RPCGRPCStatusCodeAlreadyExists = RPCGRPCStatusCodeKey.Int(6)
	// PERMISSION_DENIED
	// Stability: development
	RPCGRPCStatusCodePermissionDenied = RPCGRPCStatusCodeKey.Int(7)
	// RESOURCE_EXHAUSTED
	// Stability: development
	RPCGRPCStatusCodeResourceExhausted = RPCGRPCStatusCodeKey.Int(8)
	// FAILED_PRECONDITION
	// Stability: development
	RPCGRPCStatusCodeFailedPrecondition = RPCGRPCStatusCodeKey.Int(9)
	// ABORTED
	// Stability: development
	RPCGRPCStatusCodeAborted = RPCGRPCStatusCodeKey.Int(10)
	// OUT_OF_RANGE
	// Stability: development
	RPCGRPCStatusCodeOutOfRange = RPCGRPCStatusCodeKey.Int(11)
	// UNIMPLEMENTED
	// Stability: development
	RPCGRPCStatusCodeUnimplemented = RPCGRPCStatusCodeKey.Int(12)
	// INTERNAL
	// Stability: development
	RPCGRPCStatusCodeInternal = RPCGRPCStatusCodeKey.Int(13)
	// UNAVAILABLE
	// Stability: development
	RPCGRPCStatusCodeUnavailable = RPCGRPCStatusCodeKey.Int(14)
	// DATA_LOSS
	// Stability: development
	RPCGRPCStatusCodeDataLoss = RPCGRPCStatusCodeKey.Int(15)
	// UNAUTHENTICATED
	// Stability: development
	RPCGRPCStatusCodeUnauthenticated = RPCGRPCStatusCodeKey.Int(16)
)

Enum values for rpc.grpc.status_code

View Source
var (
	// sent
	// Stability: development
	RPCMessageTypeSent = RPCMessageTypeKey.String("SENT")
	// received
	// Stability: development
	RPCMessageTypeReceived = RPCMessageTypeKey.String("RECEIVED")
)

Enum values for rpc.message.type

View Source
var (
	// gRPC
	// Stability: development
	RPCSystemGRPC = RPCSystemKey.String("grpc")
	// Java RMI
	// Stability: development
	RPCSystemJavaRmi = RPCSystemKey.String("java_rmi")
	// .NET WCF
	// Stability: development
	RPCSystemDotnetWcf = RPCSystemKey.String("dotnet_wcf")
	// Apache Dubbo
	// Stability: development
	RPCSystemApacheDubbo = RPCSystemKey.String("apache_dubbo")
	// Connect RPC
	// Stability: development
	RPCSystemConnectRPC = RPCSystemKey.String("connect_rpc")
)

Enum values for rpc.system

View Source
var (
	// The connection was closed normally.
	// Stability: stable
	SignalrConnectionStatusNormalClosure = SignalrConnectionStatusKey.String("normal_closure")
	// The connection was closed due to a timeout.
	// Stability: stable
	SignalrConnectionStatusTimeout = SignalrConnectionStatusKey.String("timeout")
	// The connection was closed because the app is shutting down.
	// Stability: stable
	SignalrConnectionStatusAppShutdown = SignalrConnectionStatusKey.String("app_shutdown")
)

Enum values for signalr.connection.status

View Source
var (
	// ServerSentEvents protocol
	// Stability: stable
	SignalrTransportServerSentEvents = SignalrTransportKey.String("server_sent_events")
	// LongPolling protocol
	// Stability: stable
	SignalrTransportLongPolling = SignalrTransportKey.String("long_polling")
	// WebSockets protocol
	// Stability: stable
	SignalrTransportWebSockets = SignalrTransportKey.String("web_sockets")
)

Enum values for signalr.transport

View Source
var (
	// used
	// Stability: development
	SystemFilesystemStateUsed = SystemFilesystemStateKey.String("used")
	// free
	// Stability: development
	SystemFilesystemStateFree = SystemFilesystemStateKey.String("free")
	// reserved
	// Stability: development
	SystemFilesystemStateReserved = SystemFilesystemStateKey.String("reserved")
)

Enum values for system.filesystem.state

View Source
var (
	// fat32
	// Stability: development
	SystemFilesystemTypeFat32 = SystemFilesystemTypeKey.String("fat32")
	// exfat
	// Stability: development
	SystemFilesystemTypeExfat = SystemFilesystemTypeKey.String("exfat")
	// ntfs
	// Stability: development
	SystemFilesystemTypeNtfs = SystemFilesystemTypeKey.String("ntfs")
	// refs
	// Stability: development
	SystemFilesystemTypeRefs = SystemFilesystemTypeKey.String("refs")
	// hfsplus
	// Stability: development
	SystemFilesystemTypeHfsplus = SystemFilesystemTypeKey.String("hfsplus")
	// ext4
	// Stability: development
	SystemFilesystemTypeExt4 = SystemFilesystemTypeKey.String("ext4")
)

Enum values for system.filesystem.type

View Source
var (
	// used
	// Stability: development
	SystemMemoryStateUsed = SystemMemoryStateKey.String("used")
	// free
	// Stability: development
	SystemMemoryStateFree = SystemMemoryStateKey.String("free")
	// Deprecated: Removed, report shared memory usage with
	// `metric.system.memory.shared` metric.
	SystemMemoryStateShared = SystemMemoryStateKey.String("shared")
	// buffers
	// Stability: development
	SystemMemoryStateBuffers = SystemMemoryStateKey.String("buffers")
	// cached
	// Stability: development
	SystemMemoryStateCached = SystemMemoryStateKey.String("cached")
)

Enum values for system.memory.state

View Source
var (
	// in
	// Stability: development
	SystemPagingDirectionIn = SystemPagingDirectionKey.String("in")
	// out
	// Stability: development
	SystemPagingDirectionOut = SystemPagingDirectionKey.String("out")
)

Enum values for system.paging.direction

View Source
var (
	// used
	// Stability: development
	SystemPagingStateUsed = SystemPagingStateKey.String("used")
	// free
	// Stability: development
	SystemPagingStateFree = SystemPagingStateKey.String("free")
)

Enum values for system.paging.state

View Source
var (
	// major
	// Stability: development
	SystemPagingTypeMajor = SystemPagingTypeKey.String("major")
	// minor
	// Stability: development
	SystemPagingTypeMinor = SystemPagingTypeKey.String("minor")
)

Enum values for system.paging.type

View Source
var (
	// running
	// Stability: development
	SystemProcessStatusRunning = SystemProcessStatusKey.String("running")
	// sleeping
	// Stability: development
	SystemProcessStatusSleeping = SystemProcessStatusKey.String("sleeping")
	// stopped
	// Stability: development
	SystemProcessStatusStopped = SystemProcessStatusKey.String("stopped")
	// defunct
	// Stability: development
	SystemProcessStatusDefunct = SystemProcessStatusKey.String("defunct")
)

Enum values for system.process.status

View Source
var (
	// cpp
	// Stability: stable
	TelemetrySDKLanguageCPP = TelemetrySDKLanguageKey.String("cpp")
	// dotnet
	// Stability: stable
	TelemetrySDKLanguageDotnet = TelemetrySDKLanguageKey.String("dotnet")
	// erlang
	// Stability: stable
	TelemetrySDKLanguageErlang = TelemetrySDKLanguageKey.String("erlang")
	// go
	// Stability: stable
	TelemetrySDKLanguageGo = TelemetrySDKLanguageKey.String("go")
	// java
	// Stability: stable
	TelemetrySDKLanguageJava = TelemetrySDKLanguageKey.String("java")
	// nodejs
	// Stability: stable
	TelemetrySDKLanguageNodejs = TelemetrySDKLanguageKey.String("nodejs")
	// php
	// Stability: stable
	TelemetrySDKLanguagePHP = TelemetrySDKLanguageKey.String("php")
	// python
	// Stability: stable
	TelemetrySDKLanguagePython = TelemetrySDKLanguageKey.String("python")
	// ruby
	// Stability: stable
	TelemetrySDKLanguageRuby = TelemetrySDKLanguageKey.String("ruby")
	// rust
	// Stability: stable
	TelemetrySDKLanguageRust = TelemetrySDKLanguageKey.String("rust")
	// swift
	// Stability: stable
	TelemetrySDKLanguageSwift = TelemetrySDKLanguageKey.String("swift")
	// webjs
	// Stability: stable
	TelemetrySDKLanguageWebjs = TelemetrySDKLanguageKey.String("webjs")
)

Enum values for telemetry.sdk.language

View Source
var (
	// pass
	// Stability: development
	TestCaseResultStatusPass = TestCaseResultStatusKey.String("pass")
	// fail
	// Stability: development
	TestCaseResultStatusFail = TestCaseResultStatusKey.String("fail")
)

Enum values for test.case.result.status

View Source
var (
	// success
	// Stability: development
	TestSuiteRunStatusSuccess = TestSuiteRunStatusKey.String("success")
	// failure
	// Stability: development
	TestSuiteRunStatusFailure = TestSuiteRunStatusKey.String("failure")
	// skipped
	// Stability: development
	TestSuiteRunStatusSkipped = TestSuiteRunStatusKey.String("skipped")
	// aborted
	// Stability: development
	TestSuiteRunStatusAborted = TestSuiteRunStatusKey.String("aborted")
	// timed_out
	// Stability: development
	TestSuiteRunStatusTimedOut = TestSuiteRunStatusKey.String("timed_out")
	// in_progress
	// Stability: development
	TestSuiteRunStatusInProgress = TestSuiteRunStatusKey.String("in_progress")
)

Enum values for test.suite.run.status

View Source
var (
	// ssl
	// Stability: development
	TLSProtocolNameSsl = TLSProtocolNameKey.String("ssl")
	// tls
	// Stability: development
	TLSProtocolNameTLS = TLSProtocolNameKey.String("tls")
)

Enum values for tls.protocol.name

View Source
var (
	// Bot source.
	// Stability: development
	UserAgentSyntheticTypeBot = UserAgentSyntheticTypeKey.String("bot")
	// Synthetic test source.
	// Stability: development
	UserAgentSyntheticTypeTest = UserAgentSyntheticTypeKey.String("test")
)

Enum values for user_agent.synthetic.type

View Source
var (
	// Open means the change is currently active and under review. It hasn't been
	// merged into the target branch yet, and it's still possible to make changes or
	// add comments.
	// Stability: development
	VCSChangeStateOpen = VCSChangeStateKey.String("open")
	// WIP (work-in-progress, draft) means the change is still in progress and not
	// yet ready for a full review. It might still undergo significant changes.
	// Stability: development
	VCSChangeStateWip = VCSChangeStateKey.String("wip")
	// Closed means the merge request has been closed without merging. This can
	// happen for various reasons, such as the changes being deemed unnecessary, the
	// issue being resolved in another way, or the author deciding to withdraw the
	// request.
	// Stability: development
	VCSChangeStateClosed = VCSChangeStateKey.String("closed")
	// Merged indicates that the change has been successfully integrated into the
	// target codebase.
	// Stability: development
	VCSChangeStateMerged = VCSChangeStateKey.String("merged")
)

Enum values for vcs.change.state

View Source
var (
	// How many lines were added.
	// Stability: development
	VCSLineChangeTypeAdded = VCSLineChangeTypeKey.String("added")
	// How many lines were removed.
	// Stability: development
	VCSLineChangeTypeRemoved = VCSLineChangeTypeKey.String("removed")
)

Enum values for vcs.line_change.type

View Source
var (
	// [branch]
	// Stability: development
	//
	// [branch]: https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefbranchabranch
	VCSRefBaseTypeBranch = VCSRefBaseTypeKey.String("branch")
	// [tag]
	// Stability: development
	//
	// [tag]: https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddeftagatag
	VCSRefBaseTypeTag = VCSRefBaseTypeKey.String("tag")
)

Enum values for vcs.ref.base.type

View Source
var (
	// [branch]
	// Stability: development
	//
	// [branch]: https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefbranchabranch
	VCSRefHeadTypeBranch = VCSRefHeadTypeKey.String("branch")
	// [tag]
	// Stability: development
	//
	// [tag]: https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddeftagatag
	VCSRefHeadTypeTag = VCSRefHeadTypeKey.String("tag")
)

Enum values for vcs.ref.head.type

View Source
var (
	// [branch]
	// Stability: development
	//
	// [branch]: https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefbranchabranch
	VCSRefTypeBranch = VCSRefTypeKey.String("branch")
	// [tag]
	// Stability: development
	//
	// [tag]: https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddeftagatag
	VCSRefTypeTag = VCSRefTypeKey.String("tag")
)

Enum values for vcs.ref.type

View Source
var (
	// How many revisions the change is behind the target ref.
	// Stability: development
	VCSRevisionDeltaDirectionBehind = VCSRevisionDeltaDirectionKey.String("behind")
	// How many revisions the change is ahead of the target ref.
	// Stability: development
	VCSRevisionDeltaDirectionAhead = VCSRevisionDeltaDirectionKey.String("ahead")
)

Enum values for vcs.revision_delta.direction

View Source
var (
	// A fallback error value to be used when the instrumentation doesn't define a
	// custom value.
	//
	// Stability: stable
	ErrorTypeOther = ErrorTypeKey.String("_OTHER")
)

Enum values for error.type

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

AWSDynamoDBGlobalSecondaryIndexes returns an attribute KeyValue conforming to the "aws.dynamodb.global_secondary_indexes" semantic conventions. It represents the JSON-serialized value of each item of the `GlobalSecondaryIndexes` request field.

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

AWSECSClusterARN returns an attribute KeyValue conforming to the "aws.ecs.cluster.arn" semantic conventions. It represents the ARN of an ECS cluster.

func AWSECSContainerARN ¶
func AWSECSContainerARN(val string) attribute.KeyValue

AWSECSContainerARN returns an attribute KeyValue conforming to the "aws.ecs.container.arn" semantic conventions. It represents the Amazon Resource Name (ARN) of an ECS container instance.

func AWSECSTaskARN ¶
func AWSECSTaskARN(val string) attribute.KeyValue

AWSECSTaskARN returns an attribute KeyValue conforming to the "aws.ecs.task.arn" semantic conventions. It represents the ARN of a running ECS task.

func AWSECSTaskFamily ¶
func AWSECSTaskFamily(val string) attribute.KeyValue

AWSECSTaskFamily returns an attribute KeyValue conforming to the "aws.ecs.task.family" semantic conventions. It represents the family name of the ECS task definition used to create the ECS task.

func AWSECSTaskID ¶
func AWSECSTaskID(val string) attribute.KeyValue

AWSECSTaskID returns an attribute KeyValue conforming to the "aws.ecs.task.id" semantic conventions. It represents the ID of a running ECS task. The ID MUST be extracted from `task.arn`.

func AWSECSTaskRevision ¶
func AWSECSTaskRevision(val string) attribute.KeyValue

AWSECSTaskRevision returns an attribute KeyValue conforming to the "aws.ecs.task.revision" semantic conventions. It represents the revision for the task definition used to create the ECS task.

func AWSEKSClusterARN ¶
func AWSEKSClusterARN(val string) attribute.KeyValue

AWSEKSClusterARN returns an attribute KeyValue conforming to the "aws.eks.cluster.arn" semantic conventions. It represents the ARN of an EKS cluster.

func AWSExtendedRequestID ¶
func AWSExtendedRequestID(val string) attribute.KeyValue

AWSExtendedRequestID returns an attribute KeyValue conforming to the "aws.extended_request_id" semantic conventions. It represents the AWS extended request ID as returned in the response header `x-amz-id-2`.

func AWSLambdaInvokedARN ¶
func AWSLambdaInvokedARN(val string) attribute.KeyValue

AWSLambdaInvokedARN returns an attribute KeyValue conforming to the "aws.lambda.invoked_arn" semantic conventions. It represents the full invoked ARN as provided on the `Context` passed to the function ( `Lambda-Runtime-Invoked-Function-Arn` header on the `/runtime/invocation/next`

applicable).

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

AWSRequestID returns an attribute KeyValue conforming to the "aws.request_id" semantic conventions. It represents the AWS request ID as returned in the response headers `x-amzn-requestid`, `x-amzn-request-id` or `x-amz-request-id` .

func AWSS3Bucket ¶
func AWSS3Bucket(val string) attribute.KeyValue

AWSS3Bucket returns an attribute KeyValue conforming to the "aws.s3.bucket" semantic conventions. It represents the S3 bucket name the request refers to. Corresponds to the `--bucket` parameter of the S3 API operations.

func AWSS3CopySource ¶
func AWSS3CopySource(val string) attribute.KeyValue

AWSS3CopySource returns an attribute KeyValue conforming to the "aws.s3.copy_source" semantic conventions. It represents the source object (in the form `bucket`/`key`) for the copy operation.

func AWSS3Delete ¶
func AWSS3Delete(val string) attribute.KeyValue

AWSS3Delete returns an attribute KeyValue conforming to the "aws.s3.delete" semantic conventions. It represents the delete request container that specifies the objects to be deleted.

func AWSS3Key ¶
func AWSS3Key(val string) attribute.KeyValue

AWSS3Key returns an attribute KeyValue conforming to the "aws.s3.key" semantic conventions. It represents the S3 object key the request refers to. Corresponds to the `--key` parameter of the S3 API operations.

func AWSS3PartNumber ¶
func AWSS3PartNumber(val int) attribute.KeyValue

AWSS3PartNumber returns an attribute KeyValue conforming to the "aws.s3.part_number" semantic conventions. It represents the part number of the part being uploaded in a multipart-upload operation. This is a positive integer between 1 and 10,000.

func AWSS3UploadID ¶
func AWSS3UploadID(val string) attribute.KeyValue

AWSS3UploadID returns an attribute KeyValue conforming to the "aws.s3.upload_id" semantic conventions. It represents the upload ID that identifies the multipart upload.

func AndroidOSAPILevel ¶
func AndroidOSAPILevel(val string) attribute.KeyValue

AndroidOSAPILevel returns an attribute KeyValue conforming to the "android.os.api_level" semantic conventions. It represents the uniquely identifies the framework API revision offered by a version (`os.version`) of the android operating system. More information can be found here.

func ArtifactAttestationFilename ¶
func ArtifactAttestationFilename(val string) attribute.KeyValue

ArtifactAttestationFilename returns an attribute KeyValue conforming to the "artifact.attestation.filename" semantic conventions. It represents the provenance filename of the built attestation which directly relates to the build artifact filename. This filename SHOULD accompany the artifact at publish time. See the SLSA Relationship specification for more information.

func ArtifactAttestationHash ¶
func ArtifactAttestationHash(val string) attribute.KeyValue

ArtifactAttestationHash returns an attribute KeyValue conforming to the "artifact.attestation.hash" semantic conventions. It represents the full hash value (see glossary), of the built attestation. Some envelopes in the software attestation space also refer to this as the **digest**.

func ArtifactAttestationID ¶
func ArtifactAttestationID(val string) attribute.KeyValue

ArtifactAttestationID returns an attribute KeyValue conforming to the "artifact.attestation.id" semantic conventions. It represents the id of the build software attestation.

func ArtifactFilename ¶
func ArtifactFilename(val string) attribute.KeyValue

ArtifactFilename returns an attribute KeyValue conforming to the "artifact.filename" semantic conventions. It represents the human readable file name of the artifact, typically generated during build and release processes. Often includes the package name and version in the file name.

func ArtifactHash ¶
func ArtifactHash(val string) attribute.KeyValue

ArtifactHash returns an attribute KeyValue conforming to the "artifact.hash" semantic conventions. It represents the full hash value (see glossary), often found in checksum.txt on a release of the artifact and used to verify package integrity.

func ArtifactPurl ¶
func ArtifactPurl(val string) attribute.KeyValue

ArtifactPurl returns an attribute KeyValue conforming to the "artifact.purl" semantic conventions. It represents the Package URL of the package artifact provides a standard way to identify and locate the packaged artifact.

func ArtifactVersion ¶
func ArtifactVersion(val string) attribute.KeyValue

ArtifactVersion returns an attribute KeyValue conforming to the "artifact.version" semantic conventions. It represents the version of the artifact.

func AzNamespace ¶
func AzNamespace(val string) attribute.KeyValue

AzNamespace returns an attribute KeyValue conforming to the "az.namespace" semantic conventions. It represents the Azure Resource Provider Namespace as recognized by the client.

func AzServiceRequestID ¶
func AzServiceRequestID(val string) attribute.KeyValue

AzServiceRequestID returns an attribute KeyValue conforming to the "az.service_request_id" semantic conventions. It represents the unique identifier of the service request. It's generated by the Azure service and returned with the response.

func AzureClientID ¶
func AzureClientID(val string) attribute.KeyValue

AzureClientID returns an attribute KeyValue conforming to the "azure.client.id" semantic conventions. It represents the unique identifier of the client instance.

func AzureCosmosDBOperationContactedRegions ¶
func AzureCosmosDBOperationContactedRegions(val ...string) attribute.KeyValue

AzureCosmosDBOperationContactedRegions returns an attribute KeyValue conforming to the "azure.cosmosdb.operation.contacted_regions" semantic conventions. It represents the list of regions contacted during operation in the order that they were contacted. If there is more than one region listed, it indicates that the operation was performed on multiple regions i.e. cross-regional call.

func AzureCosmosDBOperationRequestCharge ¶
func AzureCosmosDBOperationRequestCharge(val float64) attribute.KeyValue

AzureCosmosDBOperationRequestCharge returns an attribute KeyValue conforming to the "azure.cosmosdb.operation.request_charge" semantic conventions. It represents the number of request units consumed by the operation.

func AzureCosmosDBRequestBodySize ¶
func AzureCosmosDBRequestBodySize(val int) attribute.KeyValue

AzureCosmosDBRequestBodySize returns an attribute KeyValue conforming to the "azure.cosmosdb.request.body.size" semantic conventions. It represents the request payload size in bytes.

func AzureCosmosDBResponseSubStatusCode ¶
func AzureCosmosDBResponseSubStatusCode(val int) attribute.KeyValue

AzureCosmosDBResponseSubStatusCode returns an attribute KeyValue conforming to the "azure.cosmosdb.response.sub_status_code" semantic conventions. It represents the cosmos DB sub status code.

func BrowserBrands ¶
func BrowserBrands(val ...string) attribute.KeyValue

BrowserBrands returns an attribute KeyValue conforming to the "browser.brands" semantic conventions. It represents the array of brand name and version separated by a space.

func BrowserLanguage ¶
func BrowserLanguage(val string) attribute.KeyValue

BrowserLanguage returns an attribute KeyValue conforming to the "browser.language" semantic conventions. It represents the preferred language of the user using the browser.

func BrowserMobile ¶
func BrowserMobile(val bool) attribute.KeyValue

BrowserMobile returns an attribute KeyValue conforming to the "browser.mobile" semantic conventions. It represents a boolean that is true if the browser is running on a mobile device.

func BrowserPlatform ¶
func BrowserPlatform(val string) attribute.KeyValue

BrowserPlatform returns an attribute KeyValue conforming to the "browser.platform" semantic conventions. It represents the platform on which the browser is running.

func CICDPipelineName ¶
func CICDPipelineName(val string) attribute.KeyValue

CICDPipelineName returns an attribute KeyValue conforming to the "cicd.pipeline.name" semantic conventions. It represents the human readable name of the pipeline within a CI/CD system.

func CICDPipelineRunID ¶
func CICDPipelineRunID(val string) attribute.KeyValue

CICDPipelineRunID returns an attribute KeyValue conforming to the "cicd.pipeline.run.id" semantic conventions. It represents the unique identifier of a pipeline run within a CI/CD system.

func CICDPipelineRunURLFull ¶
func CICDPipelineRunURLFull(val string) attribute.KeyValue

CICDPipelineRunURLFull returns an attribute KeyValue conforming to the "cicd.pipeline.run.url.full" semantic conventions. It represents the URL of the pipeline run, providing the complete address in order to locate and identify the pipeline run.

func CICDPipelineTaskName ¶
func CICDPipelineTaskName(val string) attribute.KeyValue

CICDPipelineTaskName returns an attribute KeyValue conforming to the "cicd.pipeline.task.name" semantic conventions. It represents the human readable name of a task within a pipeline. Task here most closely aligns with a computing process in a pipeline. Other terms for tasks include commands, steps, and procedures.

func CICDPipelineTaskRunID ¶
func CICDPipelineTaskRunID(val string) attribute.KeyValue

CICDPipelineTaskRunID returns an attribute KeyValue conforming to the "cicd.pipeline.task.run.id" semantic conventions. It represents the unique identifier of a task run within a pipeline.

func CICDPipelineTaskRunURLFull ¶
func CICDPipelineTaskRunURLFull(val string) attribute.KeyValue

CICDPipelineTaskRunURLFull returns an attribute KeyValue conforming to the "cicd.pipeline.task.run.url.full" semantic conventions. It represents the URL of the pipeline task run, providing the complete address in order to locate and identify the pipeline task run.

func CICDSystemComponent ¶
func CICDSystemComponent(val string) attribute.KeyValue

CICDSystemComponent returns an attribute KeyValue conforming to the "cicd.system.component" semantic conventions. It represents the name of a component of the CICD system.

func CPULogicalNumber ¶
func CPULogicalNumber(val int) attribute.KeyValue

CPULogicalNumber returns an attribute KeyValue conforming to the "cpu.logical_number" semantic conventions. It represents the logical CPU number [0..n-1].

func CassandraCoordinatorDC ¶
func CassandraCoordinatorDC(val string) attribute.KeyValue

CassandraCoordinatorDC returns an attribute KeyValue conforming to the "cassandra.coordinator.dc" semantic conventions. It represents the data center of the coordinating node for a query.

func CassandraCoordinatorID ¶
func CassandraCoordinatorID(val string) attribute.KeyValue

CassandraCoordinatorID returns an attribute KeyValue conforming to the "cassandra.coordinator.id" semantic conventions. It represents the ID of the coordinating node for a query.

func CassandraPageSize ¶
func CassandraPageSize(val int) attribute.KeyValue

CassandraPageSize returns an attribute KeyValue conforming to the "cassandra.page.size" semantic conventions. It represents the fetch size used for paging, i.e. how many rows will be returned at once.

func CassandraQueryIdempotent ¶
func CassandraQueryIdempotent(val bool) attribute.KeyValue

CassandraQueryIdempotent returns an attribute KeyValue conforming to the "cassandra.query.idempotent" semantic conventions. It represents the whether or not the query is idempotent.

func CassandraSpeculativeExecutionCount ¶
func CassandraSpeculativeExecutionCount(val int) attribute.KeyValue

CassandraSpeculativeExecutionCount returns an attribute KeyValue conforming to the "cassandra.speculative_execution.count" semantic conventions. It represents the number of times a query was speculatively executed. Not set or `0` if the query was not executed speculatively.

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

CloudResourceID returns an attribute KeyValue conforming to the "cloud.resource_id" semantic conventions. It represents the cloud provider-specific native identifier of the monitored cloud resource (e.g. an ARN on AWS, a fully qualified resource ID on Azure, a full resource name

on GCP).

func CloudeventsEventID ¶
func CloudeventsEventID(val string) attribute.KeyValue

CloudeventsEventID returns an attribute KeyValue conforming to the "cloudevents.event_id" semantic conventions. It represents the event_id uniquely identifies the event.

func CloudeventsEventSource ¶
func CloudeventsEventSource(val string) attribute.KeyValue

CloudeventsEventSource returns an attribute KeyValue conforming to the "cloudevents.event_source" semantic conventions. It represents the source identifies the context in which an event happened.

func CloudeventsEventSpecVersion ¶
func CloudeventsEventSpecVersion(val string) attribute.KeyValue

CloudeventsEventSpecVersion returns an attribute KeyValue conforming to the "cloudevents.event_spec_version" semantic conventions. It represents the version of the CloudEvents specification which the event uses.

func CloudeventsEventSubject ¶
func CloudeventsEventSubject(val string) attribute.KeyValue

CloudeventsEventSubject returns an attribute KeyValue conforming to the "cloudevents.event_subject" semantic conventions. It represents the subject of the event in the context of the event producer (identified by source).

func CloudeventsEventType ¶
func CloudeventsEventType(val string) attribute.KeyValue

CloudeventsEventType returns an attribute KeyValue conforming to the "cloudevents.event_type" semantic conventions. It represents the event_type contains a value describing the type of event related to the originating occurrence.

func CloudfoundryAppID ¶
func CloudfoundryAppID(val string) attribute.KeyValue

CloudfoundryAppID returns an attribute KeyValue conforming to the "cloudfoundry.app.id" semantic conventions. It represents the guid of the application.

func CloudfoundryAppInstanceID ¶
func CloudfoundryAppInstanceID(val string) attribute.KeyValue

CloudfoundryAppInstanceID returns an attribute KeyValue conforming to the "cloudfoundry.app.instance.id" semantic conventions. It represents the index of the application instance. 0 when just one instance is active.

func CloudfoundryAppName ¶
func CloudfoundryAppName(val string) attribute.KeyValue

CloudfoundryAppName returns an attribute KeyValue conforming to the "cloudfoundry.app.name" semantic conventions. It represents the name of the application.

func CloudfoundryOrgID ¶
func CloudfoundryOrgID(val string) attribute.KeyValue

CloudfoundryOrgID returns an attribute KeyValue conforming to the "cloudfoundry.org.id" semantic conventions. It represents the guid of the CloudFoundry org the application is running in.

func CloudfoundryOrgName ¶
func CloudfoundryOrgName(val string) attribute.KeyValue

CloudfoundryOrgName returns an attribute KeyValue conforming to the "cloudfoundry.org.name" semantic conventions. It represents the name of the CloudFoundry organization the app is running in.

func CloudfoundryProcessID ¶
func CloudfoundryProcessID(val string) attribute.KeyValue

CloudfoundryProcessID returns an attribute KeyValue conforming to the "cloudfoundry.process.id" semantic conventions. It represents the UID identifying the process.

func CloudfoundryProcessType ¶
func CloudfoundryProcessType(val string) attribute.KeyValue

CloudfoundryProcessType returns an attribute KeyValue conforming to the "cloudfoundry.process.type" semantic conventions. It represents the type of process.

func CloudfoundrySpaceID ¶
func CloudfoundrySpaceID(val string) attribute.KeyValue

CloudfoundrySpaceID returns an attribute KeyValue conforming to the "cloudfoundry.space.id" semantic conventions. It represents the guid of the CloudFoundry space the application is running in.

func CloudfoundrySpaceName ¶
func CloudfoundrySpaceName(val string) attribute.KeyValue

CloudfoundrySpaceName returns an attribute KeyValue conforming to the "cloudfoundry.space.name" semantic conventions. It represents the name of the CloudFoundry space the application is running in.

func CloudfoundrySystemID ¶
func CloudfoundrySystemID(val string) attribute.KeyValue

CloudfoundrySystemID returns an attribute KeyValue conforming to the "cloudfoundry.system.id" semantic conventions. It represents a guid or another name describing the event source.

func CloudfoundrySystemInstanceID ¶
func CloudfoundrySystemInstanceID(val string) attribute.KeyValue

CloudfoundrySystemInstanceID returns an attribute KeyValue conforming to the "cloudfoundry.system.instance.id" semantic conventions. It represents a guid describing the concrete instance of the event source.

func CodeColumnNumber ¶
func CodeColumnNumber(val int) attribute.KeyValue

CodeColumnNumber returns an attribute KeyValue conforming to the "code.column.number" semantic conventions. It represents the column number in `code.file.path` best representing the operation. It SHOULD point within the code unit named in `code.function.name`.

func CodeFilePath ¶
func CodeFilePath(val string) attribute.KeyValue

CodeFilePath returns an attribute KeyValue conforming to the "code.file.path" semantic conventions. It represents the source code file name that identifies the code unit as uniquely as possible (preferably an absolute file path).

func CodeFunctionName ¶
func CodeFunctionName(val string) attribute.KeyValue

CodeFunctionName returns an attribute KeyValue conforming to the "code.function.name" semantic conventions. It represents the method or function fully-qualified name without arguments. The value should fit the natural representation of the language runtime, which is also likely the same used within `code.stacktrace` attribute value.

func CodeLineNumber ¶
func CodeLineNumber(val int) attribute.KeyValue

CodeLineNumber returns an attribute KeyValue conforming to the "code.line.number" semantic conventions. It represents the line number in `code.file.path` best representing the operation. It SHOULD point within the code unit named in `code.function.name`.

func CodeStacktrace ¶
func CodeStacktrace(val string) attribute.KeyValue

CodeStacktrace returns an attribute KeyValue conforming to the "code.stacktrace" semantic conventions. It represents a stacktrace as a string in the natural representation for the language runtime. The representation is identical to [`exception.stacktrace`].

[`exception.stacktrace`]: /docs/exceptions/exceptions-spans.md#stacktrace-representation

func ContainerCommand ¶
func ContainerCommand(val string) attribute.KeyValue

ContainerCommand returns an attribute KeyValue conforming to the "container.command" semantic conventions. It represents the command used to run the container (i.e. the command name).

func ContainerCommandArgs ¶
func ContainerCommandArgs(val ...string) attribute.KeyValue

ContainerCommandArgs returns an attribute KeyValue conforming to the "container.command_args" semantic conventions. It represents the all the command arguments (including the command/executable itself) run by the container.

func ContainerCommandLine ¶
func ContainerCommandLine(val string) attribute.KeyValue

ContainerCommandLine returns an attribute KeyValue conforming to the "container.command_line" semantic conventions. It represents the full command run by the container as a single string representing the full command.

func ContainerCsiPluginName ¶
func ContainerCsiPluginName(val string) attribute.KeyValue

ContainerCsiPluginName returns an attribute KeyValue conforming to the "container.csi.plugin.name" semantic conventions. It represents the name of the CSI (Container Storage Interface) plugin used by the volume.

func ContainerCsiVolumeID ¶
func ContainerCsiVolumeID(val string) attribute.KeyValue

ContainerCsiVolumeID returns an attribute KeyValue conforming to the "container.csi.volume.id" semantic conventions. It represents the unique volume ID returned by the CSI (Container Storage Interface) plugin.

func ContainerID ¶
func ContainerID(val string) attribute.KeyValue

ContainerID returns an attribute KeyValue conforming to the "container.id" semantic conventions. It represents the container ID. Usually a UUID, as for example used to identify Docker containers. The UUID might be abbreviated.

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

ContainerImageTags returns an attribute KeyValue conforming to the "container.image.tags" semantic conventions. It represents the container image tags. An example can be found in Docker Image Inspect. Should be only the `<tag>` section of the full name for example from `registry.example.com/my-org/my-image:<tag>`.

func ContainerName ¶
func ContainerName(val string) attribute.KeyValue

ContainerName returns an attribute KeyValue conforming to the "container.name" semantic conventions. It represents the container name used by container runtime.

func ContainerRuntime ¶
func ContainerRuntime(val string) attribute.KeyValue

ContainerRuntime returns an attribute KeyValue conforming to the "container.runtime" semantic conventions. It represents the container runtime managing this container.

func DBClientConnectionPoolName ¶
func DBClientConnectionPoolName(val string) attribute.KeyValue

DBClientConnectionPoolName returns an attribute KeyValue conforming to the "db.client.connection.pool.name" semantic conventions. It represents the name of the connection pool; unique within the instrumented application. In case the connection pool implementation doesn't provide a name, instrumentation SHOULD use a combination of parameters that would make the name unique, for example, combining attributes `server.address`, `server.port`, and `db.namespace`, formatted as `server.address:server.port/db.namespace`. Instrumentations that generate connection pool name following different patterns SHOULD document it.

func DBCollectionName ¶
func DBCollectionName(val string) attribute.KeyValue

DBCollectionName returns an attribute KeyValue conforming to the "db.collection.name" semantic conventions. It represents the name of a collection (table, container) within the database.

func DBNamespace ¶
func DBNamespace(val string) attribute.KeyValue

DBNamespace returns an attribute KeyValue conforming to the "db.namespace" semantic conventions. It represents the name of the database, fully qualified within the server address and port.

func DBOperationBatchSize ¶
func DBOperationBatchSize(val int) attribute.KeyValue

DBOperationBatchSize returns an attribute KeyValue conforming to the "db.operation.batch.size" semantic conventions. It represents the number of queries included in a batch operation.

func DBOperationName ¶
func DBOperationName(val string) attribute.KeyValue

DBOperationName returns an attribute KeyValue conforming to the "db.operation.name" semantic conventions. It represents the name of the operation or command being executed.

func DBQuerySummary ¶
func DBQuerySummary(val string) attribute.KeyValue

DBQuerySummary returns an attribute KeyValue conforming to the "db.query.summary" semantic conventions. It represents the low cardinality representation of a database query text.

func DBQueryText ¶
func DBQueryText(val string) attribute.KeyValue

DBQueryText returns an attribute KeyValue conforming to the "db.query.text" semantic conventions. It represents the database query being executed.

func DBResponseReturnedRows ¶
func DBResponseReturnedRows(val int) attribute.KeyValue

DBResponseReturnedRows returns an attribute KeyValue conforming to the "db.response.returned_rows" semantic conventions. It represents the number of rows returned by the operation.

func DBResponseStatusCode ¶
func DBResponseStatusCode(val string) attribute.KeyValue

DBResponseStatusCode returns an attribute KeyValue conforming to the "db.response.status_code" semantic conventions. It represents the database response status code.

func DNSQuestionName ¶
func DNSQuestionName(val string) attribute.KeyValue

DNSQuestionName returns an attribute KeyValue conforming to the "dns.question.name" semantic conventions. It represents the name being queried.

func DeploymentEnvironmentName ¶
func DeploymentEnvironmentName(val string) attribute.KeyValue

DeploymentEnvironmentName returns an attribute KeyValue conforming to the "deployment.environment.name" semantic conventions. It represents the name of the deployment environment (aka deployment tier).

func DeploymentID ¶
func DeploymentID(val string) attribute.KeyValue

DeploymentID returns an attribute KeyValue conforming to the "deployment.id" semantic conventions. It represents the id of the deployment.

func DeploymentName ¶
func DeploymentName(val string) attribute.KeyValue

DeploymentName returns an attribute KeyValue conforming to the "deployment.name" semantic conventions. It represents the name of the deployment.

func DestinationAddress ¶
func DestinationAddress(val string) attribute.KeyValue

DestinationAddress returns an attribute KeyValue conforming to the "destination.address" semantic conventions. It represents the destination address - domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name.

func DestinationPort ¶
func DestinationPort(val int) attribute.KeyValue

DestinationPort returns an attribute KeyValue conforming to the "destination.port" semantic conventions. It represents the destination port number.

func DeviceID ¶
func DeviceID(val string) attribute.KeyValue

DeviceID returns an attribute KeyValue conforming to the "device.id" semantic conventions. It represents a unique identifier representing the device.

func DeviceManufacturer ¶
func DeviceManufacturer(val string) attribute.KeyValue

DeviceManufacturer returns an attribute KeyValue conforming to the "device.manufacturer" semantic conventions. It represents the name of the device manufacturer.

func DeviceModelIdentifier ¶
func DeviceModelIdentifier(val string) attribute.KeyValue

DeviceModelIdentifier returns an attribute KeyValue conforming to the "device.model.identifier" semantic conventions. It represents the model identifier for the device.

func DeviceModelName ¶
func DeviceModelName(val string) attribute.KeyValue

DeviceModelName returns an attribute KeyValue conforming to the "device.model.name" semantic conventions. It represents the marketing name for the device model.

func ElasticsearchNodeName ¶
func ElasticsearchNodeName(val string) attribute.KeyValue

ElasticsearchNodeName returns an attribute KeyValue conforming to the "elasticsearch.node.name" semantic conventions. It represents the represents the human-readable identifier of the node/instance to which a request was routed.

func EnduserID ¶
func EnduserID(val string) attribute.KeyValue

EnduserID returns an attribute KeyValue conforming to the "enduser.id" semantic conventions. It represents the unique identifier of an end user in the system. It maybe a username, email address, or other identifier.

func EnduserPseudoID ¶
func EnduserPseudoID(val string) attribute.KeyValue

EnduserPseudoID returns an attribute KeyValue conforming to the "enduser.pseudo.id" semantic conventions. It represents the pseudonymous identifier of an end user. This identifier should be a random value that is not directly linked or associated with the end user's actual identity.

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

FaaSCron returns an attribute KeyValue conforming to the "faas.cron" semantic conventions. It represents a string containing the schedule period as Cron Expression.

func FaaSDocumentCollection ¶
func FaaSDocumentCollection(val string) attribute.KeyValue

FaaSDocumentCollection returns an attribute KeyValue conforming to the "faas.document.collection" semantic conventions. It represents the name of the source on which the triggering operation was performed. For example, in Cloud Storage or S3 corresponds to the bucket name, and in Cosmos DB to the database name.

func FaaSDocumentName ¶
func FaaSDocumentName(val string) attribute.KeyValue

FaaSDocumentName returns an attribute KeyValue conforming to the "faas.document.name" semantic conventions. It represents the document name/table subjected to the operation. For example, in Cloud Storage or S3 is the name of the file, and in Cosmos DB the table name.

func FaaSDocumentTime ¶
func FaaSDocumentTime(val string) attribute.KeyValue

FaaSDocumentTime returns an attribute KeyValue conforming to the "faas.document.time" semantic conventions. It represents a string containing the time when the data was accessed in the ISO 8601 format expressed in UTC.

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

FaaSTime returns an attribute KeyValue conforming to the "faas.time" semantic conventions. It represents a string containing the function invocation time in the ISO 8601 format expressed in UTC.

func FaaSVersion ¶
func FaaSVersion(val string) attribute.KeyValue

FaaSVersion returns an attribute KeyValue conforming to the "faas.version" semantic conventions. It represents the immutable version of the function being executed.

func FeatureFlagContextID ¶
func FeatureFlagContextID(val string) attribute.KeyValue

FeatureFlagContextID returns an attribute KeyValue conforming to the "feature_flag.context.id" semantic conventions. It represents the unique identifier for the flag evaluation context. For example, the targeting key.

func FeatureFlagEvaluationErrorMessage ¶
func FeatureFlagEvaluationErrorMessage(val string) attribute.KeyValue

FeatureFlagEvaluationErrorMessage returns an attribute KeyValue conforming to the "feature_flag.evaluation.error.message" semantic conventions. It represents a message explaining the nature of an error occurring during flag evaluation.

func FeatureFlagKey ¶
func FeatureFlagKey(val string) attribute.KeyValue

FeatureFlagKey returns an attribute KeyValue conforming to the "feature_flag.key" semantic conventions. It represents the lookup key of the feature flag.

func FeatureFlagProviderName ¶
func FeatureFlagProviderName(val string) attribute.KeyValue

FeatureFlagProviderName returns an attribute KeyValue conforming to the "feature_flag.provider_name" semantic conventions. It represents the identifies the feature flag provider.

func FeatureFlagSetID ¶
func FeatureFlagSetID(val string) attribute.KeyValue

FeatureFlagSetID returns an attribute KeyValue conforming to the "feature_flag.set.id" semantic conventions. It represents the identifier of the flag set to which the feature flag belongs.

func FeatureFlagVariant ¶
func FeatureFlagVariant(val string) attribute.KeyValue

FeatureFlagVariant returns an attribute KeyValue conforming to the "feature_flag.variant" semantic conventions. It represents a semantic identifier for an evaluated flag value.

func FeatureFlagVersion ¶
func FeatureFlagVersion(val string) attribute.KeyValue

FeatureFlagVersion returns an attribute KeyValue conforming to the "feature_flag.version" semantic conventions. It represents the version of the ruleset used during the evaluation. This may be any stable value which uniquely identifies the ruleset.

func FileAccessed ¶
func FileAccessed(val string) attribute.KeyValue

FileAccessed returns an attribute KeyValue conforming to the "file.accessed" semantic conventions. It represents the time when the file was last accessed, in ISO 8601 format.

func FileAttributes ¶
func FileAttributes(val ...string) attribute.KeyValue

FileAttributes returns an attribute KeyValue conforming to the "file.attributes" semantic conventions. It represents the array of file attributes.

func FileChanged ¶
func FileChanged(val string) attribute.KeyValue

FileChanged returns an attribute KeyValue conforming to the "file.changed" semantic conventions. It represents the time when the file attributes or metadata was last changed, in ISO 8601 format.

func FileCreated ¶
func FileCreated(val string) attribute.KeyValue

FileCreated returns an attribute KeyValue conforming to the "file.created" semantic conventions. It represents the time when the file was created, in ISO 8601 format.

func FileDirectory ¶
func FileDirectory(val string) attribute.KeyValue

FileDirectory returns an attribute KeyValue conforming to the "file.directory" semantic conventions. It represents the directory where the file is located. It should include the drive letter, when appropriate.

func FileExtension ¶
func FileExtension(val string) attribute.KeyValue

FileExtension returns an attribute KeyValue conforming to the "file.extension" semantic conventions. It represents the file extension, excluding the leading dot.

func FileForkName ¶
func FileForkName(val string) attribute.KeyValue

FileForkName returns an attribute KeyValue conforming to the "file.fork_name" semantic conventions. It represents the name of the fork. A fork is additional data associated with a filesystem object.

func FileGroupID ¶
func FileGroupID(val string) attribute.KeyValue

FileGroupID returns an attribute KeyValue conforming to the "file.group.id" semantic conventions. It represents the primary Group ID (GID) of the file.

func FileGroupName ¶
func FileGroupName(val string) attribute.KeyValue

FileGroupName returns an attribute KeyValue conforming to the "file.group.name" semantic conventions. It represents the primary group name of the file.

func FileInode ¶
func FileInode(val string) attribute.KeyValue

FileInode returns an attribute KeyValue conforming to the "file.inode" semantic conventions. It represents the inode representing the file in the filesystem.

func FileMode ¶
func FileMode(val string) attribute.KeyValue

FileMode returns an attribute KeyValue conforming to the "file.mode" semantic conventions. It represents the mode of the file in octal representation.

func FileModified ¶
func FileModified(val string) attribute.KeyValue

FileModified returns an attribute KeyValue conforming to the "file.modified" semantic conventions. It represents the time when the file content was last modified, in ISO 8601 format.

func FileName ¶
func FileName(val string) attribute.KeyValue

FileName returns an attribute KeyValue conforming to the "file.name" semantic conventions. It represents the name of the file including the extension, without the directory.

func FileOwnerID ¶
func FileOwnerID(val string) attribute.KeyValue

FileOwnerID returns an attribute KeyValue conforming to the "file.owner.id" semantic conventions. It represents the user ID (UID) or security identifier (SID) of the file owner.

func FileOwnerName ¶
func FileOwnerName(val string) attribute.KeyValue

FileOwnerName returns an attribute KeyValue conforming to the "file.owner.name" semantic conventions. It represents the username of the file owner.

func FilePath ¶
func FilePath(val string) attribute.KeyValue

FilePath returns an attribute KeyValue conforming to the "file.path" semantic conventions. It represents the full path to the file, including the file name. It should include the drive letter, when appropriate.

func FileSize ¶
func FileSize(val int) attribute.KeyValue

FileSize returns an attribute KeyValue conforming to the "file.size" semantic conventions. It represents the file size in bytes.

func FileSymbolicLinkTargetPath ¶
func FileSymbolicLinkTargetPath(val string) attribute.KeyValue

FileSymbolicLinkTargetPath returns an attribute KeyValue conforming to the "file.symbolic_link.target_path" semantic conventions. It represents the path to the target of a symbolic link.

func GCPClientService ¶
func GCPClientService(val string) attribute.KeyValue

GCPClientService returns an attribute KeyValue conforming to the "gcp.client.service" semantic conventions. It represents the identifies the Google Cloud service for which the official client library is intended.

func GCPCloudRunJobExecution ¶
func GCPCloudRunJobExecution(val string) attribute.KeyValue

GCPCloudRunJobExecution returns an attribute KeyValue conforming to the "gcp.cloud_run.job.execution" semantic conventions. It represents the name of the Cloud Run execution being run for the Job, as set by the `CLOUD_RUN_EXECUTION` environment variable.

func GCPCloudRunJobTaskIndex ¶
func GCPCloudRunJobTaskIndex(val int) attribute.KeyValue

GCPCloudRunJobTaskIndex returns an attribute KeyValue conforming to the "gcp.cloud_run.job.task_index" semantic conventions. It represents the index for a task within an execution as provided by the `CLOUD_RUN_TASK_INDEX` environment variable.

func GCPGceInstanceHostname ¶
func GCPGceInstanceHostname(val string) attribute.KeyValue

GCPGceInstanceHostname returns an attribute KeyValue conforming to the "gcp.gce.instance.hostname" semantic conventions. It represents the hostname of a GCE instance. This is the full value of the default or custom hostname .

func GCPGceInstanceName ¶
func GCPGceInstanceName(val string) attribute.KeyValue

GCPGceInstanceName returns an attribute KeyValue conforming to the "gcp.gce.instance.name" semantic conventions. It represents the instance name of a GCE instance. This is the value provided by `host.name`, the visible name of the instance in the Cloud Console UI, and the prefix for the default hostname of the instance as defined by the default internal DNS name.

func GenAIAgentDescription ¶
func GenAIAgentDescription(val string) attribute.KeyValue

GenAIAgentDescription returns an attribute KeyValue conforming to the "gen_ai.agent.description" semantic conventions. It represents the free-form description of the GenAI agent provided by the application.

func GenAIAgentID ¶
func GenAIAgentID(val string) attribute.KeyValue

GenAIAgentID returns an attribute KeyValue conforming to the "gen_ai.agent.id" semantic conventions. It represents the unique identifier of the GenAI agent.

func GenAIAgentName ¶
func GenAIAgentName(val string) attribute.KeyValue

GenAIAgentName returns an attribute KeyValue conforming to the "gen_ai.agent.name" semantic conventions. It represents the human-readable name of the GenAI agent provided by the application.

func GenAIOpenaiResponseServiceTier ¶
func GenAIOpenaiResponseServiceTier(val string) attribute.KeyValue

GenAIOpenaiResponseServiceTier returns an attribute KeyValue conforming to the "gen_ai.openai.response.service_tier" semantic conventions. It represents the service tier used for the response.

func GenAIOpenaiResponseSystemFingerprint ¶
func GenAIOpenaiResponseSystemFingerprint(val string) attribute.KeyValue

GenAIOpenaiResponseSystemFingerprint returns an attribute KeyValue conforming to the "gen_ai.openai.response.system_fingerprint" semantic conventions. It represents a fingerprint to track any eventual change in the Generative AI environment.

func GenAIRequestChoiceCount ¶
func GenAIRequestChoiceCount(val int) attribute.KeyValue

GenAIRequestChoiceCount returns an attribute KeyValue conforming to the "gen_ai.request.choice.count" semantic conventions. It represents the target number of candidate completions to return.

func GenAIRequestEncodingFormats ¶
func GenAIRequestEncodingFormats(val ...string) attribute.KeyValue

GenAIRequestEncodingFormats returns an attribute KeyValue conforming to the "gen_ai.request.encoding_formats" semantic conventions. It represents the encoding formats requested in an embeddings operation, if specified.

func GenAIRequestFrequencyPenalty ¶
func GenAIRequestFrequencyPenalty(val float64) attribute.KeyValue

GenAIRequestFrequencyPenalty returns an attribute KeyValue conforming to the "gen_ai.request.frequency_penalty" semantic conventions. It represents the frequency penalty setting for the GenAI request.

func GenAIRequestMaxTokens ¶
func GenAIRequestMaxTokens(val int) attribute.KeyValue

GenAIRequestMaxTokens returns an attribute KeyValue conforming to the "gen_ai.request.max_tokens" semantic conventions. It represents the maximum number of tokens the model generates for a request.

func GenAIRequestModel ¶
func GenAIRequestModel(val string) attribute.KeyValue

GenAIRequestModel returns an attribute KeyValue conforming to the "gen_ai.request.model" semantic conventions. It represents the name of the GenAI model a request is being made to.

func GenAIRequestPresencePenalty ¶
func GenAIRequestPresencePenalty(val float64) attribute.KeyValue

GenAIRequestPresencePenalty returns an attribute KeyValue conforming to the "gen_ai.request.presence_penalty" semantic conventions. It represents the presence penalty setting for the GenAI request.

func GenAIRequestSeed ¶
func GenAIRequestSeed(val int) attribute.KeyValue

GenAIRequestSeed returns an attribute KeyValue conforming to the "gen_ai.request.seed" semantic conventions. It represents the requests with same seed value more likely to return same result.

func GenAIRequestStopSequences ¶
func GenAIRequestStopSequences(val ...string) attribute.KeyValue

GenAIRequestStopSequences returns an attribute KeyValue conforming to the "gen_ai.request.stop_sequences" semantic conventions. It represents the list of sequences that the model will use to stop generating further tokens.

func GenAIRequestTemperature ¶
func GenAIRequestTemperature(val float64) attribute.KeyValue

GenAIRequestTemperature returns an attribute KeyValue conforming to the "gen_ai.request.temperature" semantic conventions. It represents the temperature setting for the GenAI request.

func GenAIRequestTopK ¶
func GenAIRequestTopK(val float64) attribute.KeyValue

GenAIRequestTopK returns an attribute KeyValue conforming to the "gen_ai.request.top_k" semantic conventions. It represents the top_k sampling setting for the GenAI request.

func GenAIRequestTopP ¶
func GenAIRequestTopP(val float64) attribute.KeyValue

GenAIRequestTopP returns an attribute KeyValue conforming to the "gen_ai.request.top_p" semantic conventions. It represents the top_p sampling setting for the GenAI request.

func GenAIResponseFinishReasons ¶
func GenAIResponseFinishReasons(val ...string) attribute.KeyValue

GenAIResponseFinishReasons returns an attribute KeyValue conforming to the "gen_ai.response.finish_reasons" semantic conventions. It represents the array of reasons the model stopped generating tokens, corresponding to each generation received.

func GenAIResponseID ¶
func GenAIResponseID(val string) attribute.KeyValue

GenAIResponseID returns an attribute KeyValue conforming to the "gen_ai.response.id" semantic conventions. It represents the unique identifier for the completion.

func GenAIResponseModel ¶
func GenAIResponseModel(val string) attribute.KeyValue

GenAIResponseModel returns an attribute KeyValue conforming to the "gen_ai.response.model" semantic conventions. It represents the name of the model that generated the response.

func GenAIToolCallID ¶
func GenAIToolCallID(val string) attribute.KeyValue

GenAIToolCallID returns an attribute KeyValue conforming to the "gen_ai.tool.call.id" semantic conventions. It represents the tool call identifier.

func GenAIToolName ¶
func GenAIToolName(val string) attribute.KeyValue

GenAIToolName returns an attribute KeyValue conforming to the "gen_ai.tool.name" semantic conventions. It represents the name of the tool utilized by the agent.

func GenAIToolType ¶
func GenAIToolType(val string) attribute.KeyValue

GenAIToolType returns an attribute KeyValue conforming to the "gen_ai.tool.type" semantic conventions. It represents the type of the tool utilized by the agent.

func GenAIUsageInputTokens ¶
func GenAIUsageInputTokens(val int) attribute.KeyValue

GenAIUsageInputTokens returns an attribute KeyValue conforming to the "gen_ai.usage.input_tokens" semantic conventions. It represents the number of tokens used in the GenAI input (prompt).

func GenAIUsageOutputTokens ¶
func GenAIUsageOutputTokens(val int) attribute.KeyValue

GenAIUsageOutputTokens returns an attribute KeyValue conforming to the "gen_ai.usage.output_tokens" semantic conventions. It represents the number of tokens used in the GenAI response (completion).

func GeoCountryIsoCode ¶
func GeoCountryIsoCode(val string) attribute.KeyValue

GeoCountryIsoCode returns an attribute KeyValue conforming to the "geo.country.iso_code" semantic conventions. It represents the two-letter ISO Country Code (ISO 3166-1 alpha2).

func GeoLocalityName ¶
func GeoLocalityName(val string) attribute.KeyValue

GeoLocalityName returns an attribute KeyValue conforming to the "geo.locality.name" semantic conventions. It represents the locality name. Represents the name of a city, town, village, or similar populated place.

func GeoLocationLat ¶
func GeoLocationLat(val float64) attribute.KeyValue

GeoLocationLat returns an attribute KeyValue conforming to the "geo.location.lat" semantic conventions. It represents the latitude of the geo location in WGS84.

func GeoLocationLon ¶
func GeoLocationLon(val float64) attribute.KeyValue

GeoLocationLon returns an attribute KeyValue conforming to the "geo.location.lon" semantic conventions. It represents the longitude of the geo location in WGS84.

func GeoPostalCode ¶
func GeoPostalCode(val string) attribute.KeyValue

GeoPostalCode returns an attribute KeyValue conforming to the "geo.postal_code" semantic conventions. It represents the postal code associated with the location. Values appropriate for this field may also be known as a postcode or ZIP code and will vary widely from country to country.

func GeoRegionIsoCode ¶
func GeoRegionIsoCode(val string) attribute.KeyValue

GeoRegionIsoCode returns an attribute KeyValue conforming to the "geo.region.iso_code" semantic conventions. It represents the region ISO code (ISO 3166-2).

func GraphqlDocument ¶
func GraphqlDocument(val string) attribute.KeyValue

GraphqlDocument returns an attribute KeyValue conforming to the "graphql.document" semantic conventions. It represents the GraphQL document being executed.

func GraphqlOperationName ¶
func GraphqlOperationName(val string) attribute.KeyValue

GraphqlOperationName returns an attribute KeyValue conforming to the "graphql.operation.name" semantic conventions. It represents the name of the operation being executed.

func HTTPRequestBodySize ¶
func HTTPRequestBodySize(val int) attribute.KeyValue

HTTPRequestBodySize returns an attribute KeyValue conforming to the "http.request.body.size" semantic conventions. It represents the size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header. For requests using transport encoding, this should be the compressed size.

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

HTTPResponseBodySize returns an attribute KeyValue conforming to the "http.response.body.size" semantic conventions. It represents the size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the Content-Length header. For requests using transport encoding, this should be the compressed size.

func HTTPResponseSize ¶
func HTTPResponseSize(val int) attribute.KeyValue

HTTPResponseSize returns an attribute KeyValue conforming to the "http.response.size" semantic conventions. It represents the total size of the response in bytes. This should be the total number of bytes sent over the wire, including the status line (HTTP/1.1), framing (HTTP/2 and HTTP/3), headers, and response body and trailers if any.

func HTTPResponseStatusCode ¶
func HTTPResponseStatusCode(val int) attribute.KeyValue

HTTPResponseStatusCode returns an attribute KeyValue conforming to the "http.response.status_code" semantic conventions. It represents the HTTP response status code.

func HTTPRoute ¶
func HTTPRoute(val string) attribute.KeyValue

HTTPRoute returns an attribute KeyValue conforming to the "http.route" semantic conventions. It represents the matched route, that is, the path template in the format used by the respective server framework.

func HerokuAppID ¶
func HerokuAppID(val string) attribute.KeyValue

HerokuAppID returns an attribute KeyValue conforming to the "heroku.app.id" semantic conventions. It represents the unique identifier for the application.

func HerokuReleaseCommit ¶
func HerokuReleaseCommit(val string) attribute.KeyValue

HerokuReleaseCommit returns an attribute KeyValue conforming to the "heroku.release.commit" semantic conventions. It represents the commit hash for the current release.

func HerokuReleaseCreationTimestamp ¶
func HerokuReleaseCreationTimestamp(val string) attribute.KeyValue

HerokuReleaseCreationTimestamp returns an attribute KeyValue conforming to the "heroku.release.creation_timestamp" semantic conventions. It represents the time and date the release was created.

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

HostImageID returns an attribute KeyValue conforming to the "host.image.id" semantic conventions. It represents the VM image ID or host OS image ID. For Cloud, this value is from the provider.

func HostImageName ¶
func HostImageName(val string) attribute.KeyValue

HostImageName returns an attribute KeyValue conforming to the "host.image.name" semantic conventions. It represents the name of the VM image or OS install the host was instantiated from.

func HostImageVersion ¶
func HostImageVersion(val string) attribute.KeyValue

HostImageVersion returns an attribute KeyValue conforming to the "host.image.version" semantic conventions. It represents the version string of the VM image or host OS as defined in [Version Attributes].

[Version Attributes]: /docs/resource/README.md#version-attributes

func HostMac ¶
func HostMac(val ...string) attribute.KeyValue

HostMac returns an attribute KeyValue conforming to the "host.mac" semantic conventions. It represents the available MAC addresses of the host, excluding loopback interfaces.

func HostName ¶
func HostName(val string) attribute.KeyValue

HostName returns an attribute KeyValue conforming to the "host.name" semantic conventions. It represents the name of the host. On Unix systems, it may contain what the hostname command returns, or the fully qualified hostname, or another name specified by the user.

func HostType ¶
func HostType(val string) attribute.KeyValue

HostType returns an attribute KeyValue conforming to the "host.type" semantic conventions. It represents the type of host. For Cloud, this must be the machine type.

func HwID ¶
func HwID(val string) attribute.KeyValue

HwID returns an attribute KeyValue conforming to the "hw.id" semantic conventions. It represents an identifier for the hardware component, unique within the monitored host.

func HwName ¶
func HwName(val string) attribute.KeyValue

HwName returns an attribute KeyValue conforming to the "hw.name" semantic conventions. It represents an easily-recognizable name for the hardware component.

func HwParent ¶
func HwParent(val string) attribute.KeyValue

HwParent returns an attribute KeyValue conforming to the "hw.parent" semantic conventions. It represents the unique identifier of the parent component (typically the `hw.id` attribute of the enclosure, or disk controller).

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

func K8SHpaName ¶
func K8SHpaName(val string) attribute.KeyValue

K8SHpaName returns an attribute KeyValue conforming to the "k8s.hpa.name" semantic conventions. It represents the name of the horizontal pod autoscaler.

func K8SHpaUID ¶
func K8SHpaUID(val string) attribute.KeyValue

K8SHpaUID returns an attribute KeyValue conforming to the "k8s.hpa.uid" semantic conventions. It represents the UID of the horizontal pod autoscaler.

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

func K8SReplicationControllerName ¶
func K8SReplicationControllerName(val string) attribute.KeyValue

K8SReplicationControllerName returns an attribute KeyValue conforming to the "k8s.replicationcontroller.name" semantic conventions. It represents the name of the replication controller.

func K8SReplicationControllerUID ¶
func K8SReplicationControllerUID(val string) attribute.KeyValue

K8SReplicationControllerUID returns an attribute KeyValue conforming to the "k8s.replicationcontroller.uid" semantic conventions. It represents the UID of the replication controller.

func K8SResourceQuotaName ¶
func K8SResourceQuotaName(val string) attribute.KeyValue

K8SResourceQuotaName returns an attribute KeyValue conforming to the "k8s.resourcequota.name" semantic conventions. It represents the name of the resource quota.

func K8SResourceQuotaUID ¶
func K8SResourceQuotaUID(val string) attribute.KeyValue

K8SResourceQuotaUID returns an attribute KeyValue conforming to the "k8s.resourcequota.uid" semantic conventions. It represents the UID of the resource quota.

func K8SStatefulSetName ¶
func K8SStatefulSetName(val string) attribute.KeyValue

K8SStatefulSetName returns an attribute KeyValue conforming to the "k8s.statefulset.name" semantic conventions. It represents the name of the StatefulSet.

func K8SStatefulSetUID ¶
func K8SStatefulSetUID(val string) attribute.KeyValue

K8SStatefulSetUID returns an attribute KeyValue conforming to the "k8s.statefulset.uid" semantic conventions. It represents the UID of the StatefulSet.

func K8SVolumeName ¶
func K8SVolumeName(val string) attribute.KeyValue

K8SVolumeName returns an attribute KeyValue conforming to the "k8s.volume.name" semantic conventions. It represents the name of the K8s volume.

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

func LogRecordOriginal ¶
func LogRecordOriginal(val string) attribute.KeyValue

LogRecordOriginal returns an attribute KeyValue conforming to the "log.record.original" semantic conventions. It represents the complete original Log Record.

func LogRecordUID ¶
func LogRecordUID(val string) attribute.KeyValue

LogRecordUID returns an attribute KeyValue conforming to the "log.record.uid" semantic conventions. It represents a unique identifier for the Log Record.

func MessagingBatchMessageCount ¶
func MessagingBatchMessageCount(val int) attribute.KeyValue

MessagingBatchMessageCount returns an attribute KeyValue conforming to the "messaging.batch.message_count" semantic conventions. It represents the number of messages sent, received, or processed in the scope of the batching operation.

func MessagingClientID ¶
func MessagingClientID(val string) attribute.KeyValue

MessagingClientID returns an attribute KeyValue conforming to the "messaging.client.id" semantic conventions. It represents a unique identifier for the client that consumes or produces a message.

func MessagingConsumerGroupName ¶
func MessagingConsumerGroupName(val string) attribute.KeyValue

MessagingConsumerGroupName returns an attribute KeyValue conforming to the "messaging.consumer.group.name" semantic conventions. It represents the name of the consumer group with which a consumer is associated.

func MessagingDestinationAnonymous ¶
func MessagingDestinationAnonymous(val bool) attribute.KeyValue

MessagingDestinationAnonymous returns an attribute KeyValue conforming to the "messaging.destination.anonymous" semantic conventions. It represents a boolean that is true if the message destination is anonymous (could be unnamed or have auto-generated name).

func MessagingDestinationName ¶
func MessagingDestinationName(val string) attribute.KeyValue

MessagingDestinationName returns an attribute KeyValue conforming to the "messaging.destination.name" semantic conventions. It represents the message destination name.

func MessagingDestinationPartitionID ¶
func MessagingDestinationPartitionID(val string) attribute.KeyValue

MessagingDestinationPartitionID returns an attribute KeyValue conforming to the "messaging.destination.partition.id" semantic conventions. It represents the identifier of the partition messages are sent to or received from, unique within the `messaging.destination.name`.

func MessagingDestinationSubscriptionName ¶
func MessagingDestinationSubscriptionName(val string) attribute.KeyValue

MessagingDestinationSubscriptionName returns an attribute KeyValue conforming to the "messaging.destination.subscription.name" semantic conventions. It represents the name of the destination subscription from which a message is consumed.

func MessagingDestinationTemplate ¶
func MessagingDestinationTemplate(val string) attribute.KeyValue

MessagingDestinationTemplate returns an attribute KeyValue conforming to the "messaging.destination.template" semantic conventions. It represents the low cardinality representation of the messaging destination name.

func MessagingDestinationTemporary ¶
func MessagingDestinationTemporary(val bool) attribute.KeyValue

MessagingDestinationTemporary returns an attribute KeyValue conforming to the "messaging.destination.temporary" semantic conventions. It represents a boolean that is true if the message destination is temporary and might not exist anymore after messages are processed.

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

func MessagingKafkaMessageKey ¶
func MessagingKafkaMessageKey(val string) attribute.KeyValue

MessagingKafkaMessageKey returns an attribute KeyValue conforming to the "messaging.kafka.message.key" semantic conventions. It represents the message keys in Kafka are used for grouping alike messages to ensure they're processed on the same partition. They differ from `messaging.message.id` in that they're not unique. If the key is `null`, the attribute MUST NOT be set.

func MessagingKafkaMessageTombstone ¶
func MessagingKafkaMessageTombstone(val bool) attribute.KeyValue

MessagingKafkaMessageTombstone returns an attribute KeyValue conforming to the "messaging.kafka.message.tombstone" semantic conventions. It represents a boolean that is true if the message is a tombstone.

func MessagingKafkaOffset ¶
func MessagingKafkaOffset(val int) attribute.KeyValue

MessagingKafkaOffset returns an attribute KeyValue conforming to the "messaging.kafka.offset" semantic conventions. It represents the offset of a record in the corresponding Kafka partition.

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

MessagingRabbitmqMessageDeliveryTag returns an attribute KeyValue conforming to the "messaging.rabbitmq.message.delivery_tag" semantic conventions. It represents the rabbitMQ message delivery tag.

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

func NetworkInterfaceName ¶
func NetworkInterfaceName(val string) attribute.KeyValue

NetworkInterfaceName returns an attribute KeyValue conforming to the "network.interface.name" semantic conventions. It represents the network interface name.

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

NetworkProtocolName returns an attribute KeyValue conforming to the "network.protocol.name" semantic conventions. It represents the OSI application layer or non-OSI equivalent.

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

OSVersion returns an attribute KeyValue conforming to the "os.version" semantic conventions. It represents the version string of the operating system as defined in [Version Attributes].

[Version Attributes]: /docs/resource/README.md#version-attributes

func OTelComponentName ¶
func OTelComponentName(val string) attribute.KeyValue

OTelComponentName returns an attribute KeyValue conforming to the "otel.component.name" semantic conventions. It represents a name uniquely identifying the instance of the OpenTelemetry component within its containing SDK instance.

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

PeerService returns an attribute KeyValue conforming to the "peer.service" semantic conventions. It represents the [`service.name`] of the remote service. SHOULD be equal to the actual `service.name` resource attribute of the remote service if any.

[`service.name`]: /docs/resource/README.md#service

func ProcessArgsCount ¶
func ProcessArgsCount(val int) attribute.KeyValue

ProcessArgsCount returns an attribute KeyValue conforming to the "process.args_count" semantic conventions. It represents the length of the process.command_args array.

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

func ProcessExecutableBuildIDGnu ¶
func ProcessExecutableBuildIDGnu(val string) attribute.KeyValue

ProcessExecutableBuildIDGnu returns an attribute KeyValue conforming to the "process.executable.build_id.gnu" semantic conventions. It represents the GNU build ID as found in the `.note.gnu.build-id` ELF section (hex string).

func ProcessExecutableBuildIDGo ¶
func ProcessExecutableBuildIDGo(val string) attribute.KeyValue

ProcessExecutableBuildIDGo returns an attribute KeyValue conforming to the "process.executable.build_id.go" semantic conventions. It represents the Go build ID as retrieved by `go tool buildid <go executable>`.

func ProcessExecutableBuildIDHtlhash ¶
func ProcessExecutableBuildIDHtlhash(val string) attribute.KeyValue

ProcessExecutableBuildIDHtlhash returns an attribute KeyValue conforming to the "process.executable.build_id.htlhash" semantic conventions. It represents the profiling specific build ID for executables. See the OTel specification for Profiles for more information.

func ProcessExecutableName ¶
func ProcessExecutableName(val string) attribute.KeyValue

ProcessExecutableName returns an attribute KeyValue conforming to the "process.executable.name" semantic conventions. It represents the name of the process executable. On Linux based systems, this SHOULD be set to the base name of the target of `/proc/[pid]/exe`. On Windows, this SHOULD be set to the base name of `GetProcessImageFileNameW`.

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

func ProcessLinuxCgroup ¶
func ProcessLinuxCgroup(val string) attribute.KeyValue

ProcessLinuxCgroup returns an attribute KeyValue conforming to the "process.linux.cgroup" semantic conventions. It represents the control group associated with the process.

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

ProcessRuntimeName returns an attribute KeyValue conforming to the "process.runtime.name" semantic conventions. It represents the name of the runtime of this process.

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

func ProcessTitle ¶
func ProcessTitle(val string) attribute.KeyValue

ProcessTitle returns an attribute KeyValue conforming to the "process.title" semantic conventions. It represents the process title (proctitle).

func ProcessUserID ¶
func ProcessUserID(val int) attribute.KeyValue

ProcessUserID returns an attribute KeyValue conforming to the "process.user.id" semantic conventions. It represents the effective user ID (EUID) of the process.

func ProcessUserName ¶
func ProcessUserName(val string) attribute.KeyValue

ProcessUserName returns an attribute KeyValue conforming to the "process.user.name" semantic conventions. It represents the username of the effective user of the process.

func ProcessVpid ¶
func ProcessVpid(val int) attribute.KeyValue

ProcessVpid returns an attribute KeyValue conforming to the "process.vpid" semantic conventions. It represents the virtual process identifier.

func ProcessWorkingDirectory ¶
func ProcessWorkingDirectory(val string) attribute.KeyValue

ProcessWorkingDirectory returns an attribute KeyValue conforming to the "process.working_directory" semantic conventions. It represents the working directory of the process.

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

RPCMessageID returns an attribute KeyValue conforming to the "rpc.message.id" semantic conventions. It MUST be calculated as two different counters starting from `1` one for sent messages and one for received message.

func RPCMessageUncompressedSize ¶
func RPCMessageUncompressedSize(val int) attribute.KeyValue

RPCMessageUncompressedSize returns an attribute KeyValue conforming to the "rpc.message.uncompressed_size" semantic conventions. It represents the uncompressed size of the message in bytes.

func RPCMethod ¶
func RPCMethod(val string) attribute.KeyValue

RPCMethod returns an attribute KeyValue conforming to the "rpc.method" semantic conventions. It represents the name of the (logical) method being called, must be equal to the $method part in the span name.

func RPCService ¶
func RPCService(val string) attribute.KeyValue

RPCService returns an attribute KeyValue conforming to the "rpc.service" semantic conventions. It represents the full (logical) name of the service being called, including its package name, if applicable.

func SecurityRuleCategory ¶
func SecurityRuleCategory(val string) attribute.KeyValue

SecurityRuleCategory returns an attribute KeyValue conforming to the "security_rule.category" semantic conventions. It represents a categorization value keyword used by the entity using the rule for detection of this event.

func SecurityRuleDescription ¶
func SecurityRuleDescription(val string) attribute.KeyValue

SecurityRuleDescription returns an attribute KeyValue conforming to the "security_rule.description" semantic conventions. It represents the description of the rule generating the event.

func SecurityRuleLicense ¶
func SecurityRuleLicense(val string) attribute.KeyValue

SecurityRuleLicense returns an attribute KeyValue conforming to the "security_rule.license" semantic conventions. It represents the name of the license under which the rule used to generate this event is made available.

func SecurityRuleName ¶
func SecurityRuleName(val string) attribute.KeyValue

SecurityRuleName returns an attribute KeyValue conforming to the "security_rule.name" semantic conventions. It represents the name of the rule or signature generating the event.

func SecurityRuleReference ¶
func SecurityRuleReference(val string) attribute.KeyValue

SecurityRuleReference returns an attribute KeyValue conforming to the "security_rule.reference" semantic conventions. It represents the reference URL to additional information about the rule used to generate this event.

func SecurityRuleRulesetName ¶
func SecurityRuleRulesetName(val string) attribute.KeyValue

SecurityRuleRulesetName returns an attribute KeyValue conforming to the "security_rule.ruleset.name" semantic conventions. It represents the name of the ruleset, policy, group, or parent category in which the rule used to generate this event is a member.

func SecurityRuleUUID ¶
func SecurityRuleUUID(val string) attribute.KeyValue

SecurityRuleUUID returns an attribute KeyValue conforming to the "security_rule.uuid" semantic conventions. It represents a rule ID that is unique within the scope of a set or group of agents, observers, or other entities using the rule for detection of this event.

func SecurityRuleVersion ¶
func SecurityRuleVersion(val string) attribute.KeyValue

SecurityRuleVersion returns an attribute KeyValue conforming to the "security_rule.version" semantic conventions. It represents the version / revision of the rule being used for analysis.

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

SourcePort returns an attribute KeyValue conforming to the "source.port" semantic conventions. It represents the source port number.

func SystemCPULogicalNumber ¶
func SystemCPULogicalNumber(val int) attribute.KeyValue

SystemCPULogicalNumber returns an attribute KeyValue conforming to the "system.cpu.logical_number" semantic conventions. It represents the deprecated, use `cpu.logical_number` instead.

func SystemDevice ¶
func SystemDevice(val string) attribute.KeyValue

SystemDevice returns an attribute KeyValue conforming to the "system.device" semantic conventions. It represents the device identifier.

func SystemFilesystemMode ¶
func SystemFilesystemMode(val string) attribute.KeyValue

SystemFilesystemMode returns an attribute KeyValue conforming to the "system.filesystem.mode" semantic conventions. It represents the filesystem mode.

func SystemFilesystemMountpoint ¶
func SystemFilesystemMountpoint(val string) attribute.KeyValue

SystemFilesystemMountpoint returns an attribute KeyValue conforming to the "system.filesystem.mountpoint" semantic conventions. It represents the filesystem mount path.

func TLSCipher ¶
func TLSCipher(val string) attribute.KeyValue

TLSCipher returns an attribute KeyValue conforming to the "tls.cipher" semantic conventions. It represents the string indicating the cipher used during the current connection.

func TLSClientCertificate ¶
func TLSClientCertificate(val string) attribute.KeyValue

TLSClientCertificate returns an attribute KeyValue conforming to the "tls.client.certificate" semantic conventions. It represents the PEM-encoded stand-alone certificate offered by the client. This is usually mutually-exclusive of `client.certificate_chain` since this value also exists in that list.

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

TLSClientIssuer returns an attribute KeyValue conforming to the "tls.client.issuer" semantic conventions. It represents the distinguished name of subject of the issuer of the x.509 certificate presented by the client.

func TLSClientJa3 ¶
func TLSClientJa3(val string) attribute.KeyValue

TLSClientJa3 returns an attribute KeyValue conforming to the "tls.client.ja3" semantic conventions. It represents a hash that identifies clients based on how they perform an SSL/TLS handshake.

func TLSClientNotAfter ¶
func TLSClientNotAfter(val string) attribute.KeyValue

TLSClientNotAfter returns an attribute KeyValue conforming to the "tls.client.not_after" semantic conventions. It represents the date/Time indicating when client certificate is no longer considered valid.

func TLSClientNotBefore ¶
func TLSClientNotBefore(val string) attribute.KeyValue

TLSClientNotBefore returns an attribute KeyValue conforming to the "tls.client.not_before" semantic conventions. It represents the date/Time indicating when client certificate is first considered valid.

func TLSClientSubject ¶
func TLSClientSubject(val string) attribute.KeyValue

TLSClientSubject returns an attribute KeyValue conforming to the "tls.client.subject" semantic conventions. It represents the distinguished name of subject of the x.509 certificate presented by the client.

func TLSClientSupportedCiphers ¶
func TLSClientSupportedCiphers(val ...string) attribute.KeyValue

TLSClientSupportedCiphers returns an attribute KeyValue conforming to the "tls.client.supported_ciphers" semantic conventions. It represents the array of ciphers offered by the client during the client hello.

func TLSCurve ¶
func TLSCurve(val string) attribute.KeyValue

TLSCurve returns an attribute KeyValue conforming to the "tls.curve" semantic conventions. It represents the string indicating the curve used for the given cipher, when applicable.

func TLSEstablished ¶
func TLSEstablished(val bool) attribute.KeyValue

TLSEstablished returns an attribute KeyValue conforming to the "tls.established" semantic conventions. It represents the boolean flag indicating if the TLS negotiation was successful and transitioned to an encrypted tunnel.

func TLSNextProtocol ¶
func TLSNextProtocol(val string) attribute.KeyValue

TLSNextProtocol returns an attribute KeyValue conforming to the "tls.next_protocol" semantic conventions. It represents the string indicating the protocol being tunneled. Per the values in the IANA registry, this string should be lower case.

func TLSProtocolVersion ¶
func TLSProtocolVersion(val string) attribute.KeyValue

TLSProtocolVersion returns an attribute KeyValue conforming to the "tls.protocol.version" semantic conventions. It represents the numeric part of the version parsed from the original string of the negotiated SSL/TLS protocol version.

func TLSResumed ¶
func TLSResumed(val bool) attribute.KeyValue

TLSResumed returns an attribute KeyValue conforming to the "tls.resumed" semantic conventions. It represents the boolean flag indicating if this TLS connection was resumed from an existing TLS negotiation.

func TLSServerCertificate ¶
func TLSServerCertificate(val string) attribute.KeyValue

TLSServerCertificate returns an attribute KeyValue conforming to the "tls.server.certificate" semantic conventions. It represents the PEM-encoded stand-alone certificate offered by the server. This is usually mutually-exclusive of `server.certificate_chain` since this value also exists in that list.

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

TLSServerIssuer returns an attribute KeyValue conforming to the "tls.server.issuer" semantic conventions. It represents the distinguished name of subject of the issuer of the x.509 certificate presented by the client.

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

func TestCaseName ¶
func TestCaseName(val string) attribute.KeyValue

TestCaseName returns an attribute KeyValue conforming to the "test.case.name" semantic conventions. It represents the fully qualified human readable name of the test case.

func TestSuiteName ¶
func TestSuiteName(val string) attribute.KeyValue

TestSuiteName returns an attribute KeyValue conforming to the "test.suite.name" semantic conventions. It represents the human readable name of a test suite.

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

URLFragment returns an attribute KeyValue conforming to the "url.fragment" semantic conventions. It represents the URI fragment component.

func URLFull ¶
func URLFull(val string) attribute.KeyValue

URLFull returns an attribute KeyValue conforming to the "url.full" semantic conventions. It represents the absolute URL describing a network resource according to RFC3986.

func URLOriginal ¶
func URLOriginal(val string) attribute.KeyValue

URLOriginal returns an attribute KeyValue conforming to the "url.original" semantic conventions. It represents the unmodified original URL as seen in the event source.

func URLPath ¶
func URLPath(val string) attribute.KeyValue

URLPath returns an attribute KeyValue conforming to the "url.path" semantic conventions. It represents the URI path component.

func URLPort ¶
func URLPort(val int) attribute.KeyValue

URLPort returns an attribute KeyValue conforming to the "url.port" semantic conventions. It represents the port extracted from the `url.full`.

func URLQuery ¶
func URLQuery(val string) attribute.KeyValue

URLQuery returns an attribute KeyValue conforming to the "url.query" semantic conventions. It represents the URI query component.

func URLRegisteredDomain ¶
func URLRegisteredDomain(val string) attribute.KeyValue

URLRegisteredDomain returns an attribute KeyValue conforming to the "url.registered_domain" semantic conventions. It represents the highest registered url domain, stripped of the subdomain.

func URLScheme ¶
func URLScheme(val string) attribute.KeyValue

URLScheme returns an attribute KeyValue conforming to the "url.scheme" semantic conventions. It represents the URI scheme component identifying the used protocol.

func URLSubdomain ¶
func URLSubdomain(val string) attribute.KeyValue

URLSubdomain returns an attribute KeyValue conforming to the "url.subdomain" semantic conventions. It represents the subdomain portion of a fully qualified domain name includes all of the names except the host name under the registered_domain. In a partially qualified domain, or if the qualification level of the full name cannot be determined, subdomain contains all of the names below the registered domain.

func URLTemplate ¶
func URLTemplate(val string) attribute.KeyValue

URLTemplate returns an attribute KeyValue conforming to the "url.template" semantic conventions. It represents the low-cardinality template of an absolute path reference.

func URLTopLevelDomain ¶
func URLTopLevelDomain(val string) attribute.KeyValue

URLTopLevelDomain returns an attribute KeyValue conforming to the "url.top_level_domain" semantic conventions. It represents the effective top level domain (eTLD), also known as the domain suffix, is the last part of the domain name. For example, the top level domain for example.com is `com`.

func UserAgentName ¶
func UserAgentName(val string) attribute.KeyValue

UserAgentName returns an attribute KeyValue conforming to the "user_agent.name" semantic conventions. It represents the name of the user-agent extracted from original. Usually refers to the browser's name.

func UserAgentOSName ¶
func UserAgentOSName(val string) attribute.KeyValue

UserAgentOSName returns an attribute KeyValue conforming to the "user_agent.os.name" semantic conventions. It represents the human readable operating system name.

func UserAgentOSVersion ¶
func UserAgentOSVersion(val string) attribute.KeyValue

UserAgentOSVersion returns an attribute KeyValue conforming to the "user_agent.os.version" semantic conventions. It represents the version string of the operating system as defined in [Version Attributes].

[Version Attributes]: /docs/resource/README.md#version-attributes

func UserAgentOriginal ¶
func UserAgentOriginal(val string) attribute.KeyValue

UserAgentOriginal returns an attribute KeyValue conforming to the "user_agent.original" semantic conventions. It represents the value of the HTTP User-Agent header sent by the client.

func UserAgentVersion ¶
func UserAgentVersion(val string) attribute.KeyValue

UserAgentVersion returns an attribute KeyValue conforming to the "user_agent.version" semantic conventions. It represents the version of the user-agent extracted from original. Usually refers to the browser's version.

func UserEmail ¶
func UserEmail(val string) attribute.KeyValue

UserEmail returns an attribute KeyValue conforming to the "user.email" semantic conventions. It represents the user email address.

func UserFullName ¶
func UserFullName(val string) attribute.KeyValue

UserFullName returns an attribute KeyValue conforming to the "user.full_name" semantic conventions. It represents the user's full name.

func UserHash ¶
func UserHash(val string) attribute.KeyValue

UserHash returns an attribute KeyValue conforming to the "user.hash" semantic conventions. It represents the unique user hash to correlate information for a user in anonymized form.

func UserID ¶
func UserID(val string) attribute.KeyValue

UserID returns an attribute KeyValue conforming to the "user.id" semantic conventions. It represents the unique identifier of the user.

func UserName ¶
func UserName(val string) attribute.KeyValue

UserName returns an attribute KeyValue conforming to the "user.name" semantic conventions. It represents the short name or login/username of the user.

func UserRoles ¶
func UserRoles(val ...string) attribute.KeyValue

UserRoles returns an attribute KeyValue conforming to the "user.roles" semantic conventions. It represents the array of user roles at the time of the event.

func VCSChangeID ¶
func VCSChangeID(val string) attribute.KeyValue

VCSChangeID returns an attribute KeyValue conforming to the "vcs.change.id" semantic conventions. It represents the ID of the change (pull request/merge request/changelist) if applicable. This is usually a unique (within repository) identifier generated by the VCS system.

func VCSChangeTitle ¶
func VCSChangeTitle(val string) attribute.KeyValue

VCSChangeTitle returns an attribute KeyValue conforming to the "vcs.change.title" semantic conventions. It represents the human readable title of the change (pull request/merge request/changelist). This title is often a brief summary of the change and may get merged in to a ref as the commit summary.

func VCSRefBaseName ¶
func VCSRefBaseName(val string) attribute.KeyValue

VCSRefBaseName returns an attribute KeyValue conforming to the "vcs.ref.base.name" semantic conventions. It represents the name of the reference such as **branch** or **tag** in the repository.

func VCSRefBaseRevision ¶
func VCSRefBaseRevision(val string) attribute.KeyValue

VCSRefBaseRevision returns an attribute KeyValue conforming to the "vcs.ref.base.revision" semantic conventions. It represents the revision, literally revised version, The revision most often refers to a commit object in Git, or a revision number in SVN.

func VCSRefHeadName ¶
func VCSRefHeadName(val string) attribute.KeyValue

VCSRefHeadName returns an attribute KeyValue conforming to the "vcs.ref.head.name" semantic conventions. It represents the name of the reference such as **branch** or **tag** in the repository.

func VCSRefHeadRevision ¶
func VCSRefHeadRevision(val string) attribute.KeyValue

VCSRefHeadRevision returns an attribute KeyValue conforming to the "vcs.ref.head.revision" semantic conventions. It represents the revision, literally revised version, The revision most often refers to a commit object in Git, or a revision number in SVN.

func VCSRepositoryName ¶
func VCSRepositoryName(val string) attribute.KeyValue

VCSRepositoryName returns an attribute KeyValue conforming to the "vcs.repository.name" semantic conventions. It represents the human readable name of the repository. It SHOULD NOT include any additional identifier like Group/SubGroup in GitLab or organization in GitHub.

func VCSRepositoryURLFull ¶
func VCSRepositoryURLFull(val string) attribute.KeyValue

VCSRepositoryURLFull returns an attribute KeyValue conforming to the "vcs.repository.url.full" semantic conventions. It represents the canonical URL of the repository providing the complete HTTP(S) address in order to locate and identify the repository through a browser.

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
