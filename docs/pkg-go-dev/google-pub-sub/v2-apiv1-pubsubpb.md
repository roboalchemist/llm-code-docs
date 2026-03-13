### Index ¶

- Constants

- Variables

- 
        func RegisterPublisherServer(s grpc.ServiceRegistrar, srv PublisherServer)

- 
        func RegisterSchemaServiceServer(s grpc.ServiceRegistrar, srv SchemaServiceServer)

- 
        func RegisterSubscriberServer(s grpc.ServiceRegistrar, srv SubscriberServer)

- 
          type AIInference

- 

  - 
            func (*AIInference) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *AIInference) GetEndpoint() string

  - 
            func (m *AIInference) GetInferenceMode() isAIInference_InferenceMode

  - 
            func (x *AIInference) GetServiceAccountEmail() string

  - 
            func (x *AIInference) GetUnstructuredInference() *AIInference_UnstructuredInference

  - 
            func (*AIInference) ProtoMessage()

  - 
            func (x *AIInference) ProtoReflect() protoreflect.Message

  - 
            func (x *AIInference) Reset()

  - 
            func (x *AIInference) String() string

- 
          type AIInference_UnstructuredInference

- 

  - 
            func (*AIInference_UnstructuredInference) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *AIInference_UnstructuredInference) GetParameters() *structpb.Struct

  - 
            func (*AIInference_UnstructuredInference) ProtoMessage()

  - 
            func (x *AIInference_UnstructuredInference) ProtoReflect() protoreflect.Message

  - 
            func (x *AIInference_UnstructuredInference) Reset()

  - 
            func (x *AIInference_UnstructuredInference) String() string

- 
          type AIInference_UnstructuredInference_

- 
          type AcknowledgeRequest

- 

  - 
            func (*AcknowledgeRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *AcknowledgeRequest) GetAckIds() []string

  - 
            func (x *AcknowledgeRequest) GetSubscription() string

  - 
            func (*AcknowledgeRequest) ProtoMessage()

  - 
            func (x *AcknowledgeRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *AcknowledgeRequest) Reset()

  - 
            func (x *AcknowledgeRequest) String() string

- 
          type BigQueryConfig

- 

  - 
            func (*BigQueryConfig) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *BigQueryConfig) GetDropUnknownFields() bool

  - 
            func (x *BigQueryConfig) GetServiceAccountEmail() string

  - 
            func (x *BigQueryConfig) GetState() BigQueryConfig_State

  - 
            func (x *BigQueryConfig) GetTable() string

  - 
            func (x *BigQueryConfig) GetUseTableSchema() bool

  - 
            func (x *BigQueryConfig) GetUseTopicSchema() bool

  - 
            func (x *BigQueryConfig) GetWriteMetadata() bool

  - 
            func (*BigQueryConfig) ProtoMessage()

  - 
            func (x *BigQueryConfig) ProtoReflect() protoreflect.Message

  - 
            func (x *BigQueryConfig) Reset()

  - 
            func (x *BigQueryConfig) String() string

- 
          type BigQueryConfig_State

- 

  - 
            func (BigQueryConfig_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x BigQueryConfig_State) Enum() *BigQueryConfig_State

  - 
            func (BigQueryConfig_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x BigQueryConfig_State) Number() protoreflect.EnumNumber

  - 
            func (x BigQueryConfig_State) String() string

  - 
            func (BigQueryConfig_State) Type() protoreflect.EnumType

- 
          type CloudStorageConfig

- 

  - 
            func (*CloudStorageConfig) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *CloudStorageConfig) GetAvroConfig() *CloudStorageConfig_AvroConfig

  - 
            func (x *CloudStorageConfig) GetBucket() string

  - 
            func (x *CloudStorageConfig) GetFilenameDatetimeFormat() string

  - 
            func (x *CloudStorageConfig) GetFilenamePrefix() string

  - 
            func (x *CloudStorageConfig) GetFilenameSuffix() string

  - 
            func (x *CloudStorageConfig) GetMaxBytes() int64

  - 
            func (x *CloudStorageConfig) GetMaxDuration() *durationpb.Duration

  - 
            func (x *CloudStorageConfig) GetMaxMessages() int64

  - 
            func (m *CloudStorageConfig) GetOutputFormat() isCloudStorageConfig_OutputFormat

  - 
            func (x *CloudStorageConfig) GetServiceAccountEmail() string

  - 
            func (x *CloudStorageConfig) GetState() CloudStorageConfig_State

  - 
            func (x *CloudStorageConfig) GetTextConfig() *CloudStorageConfig_TextConfig

  - 
            func (*CloudStorageConfig) ProtoMessage()

  - 
            func (x *CloudStorageConfig) ProtoReflect() protoreflect.Message

  - 
            func (x *CloudStorageConfig) Reset()

  - 
            func (x *CloudStorageConfig) String() string

- 
          type CloudStorageConfig_AvroConfig

- 

  - 
            func (*CloudStorageConfig_AvroConfig) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *CloudStorageConfig_AvroConfig) GetUseTopicSchema() bool

  - 
            func (x *CloudStorageConfig_AvroConfig) GetWriteMetadata() bool

  - 
            func (*CloudStorageConfig_AvroConfig) ProtoMessage()

  - 
            func (x *CloudStorageConfig_AvroConfig) ProtoReflect() protoreflect.Message

  - 
            func (x *CloudStorageConfig_AvroConfig) Reset()

  - 
            func (x *CloudStorageConfig_AvroConfig) String() string

- 
          type CloudStorageConfig_AvroConfig_

- 
          type CloudStorageConfig_State

- 

  - 
            func (CloudStorageConfig_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x CloudStorageConfig_State) Enum() *CloudStorageConfig_State

  - 
            func (CloudStorageConfig_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x CloudStorageConfig_State) Number() protoreflect.EnumNumber

  - 
            func (x CloudStorageConfig_State) String() string

  - 
            func (CloudStorageConfig_State) Type() protoreflect.EnumType

- 
          type CloudStorageConfig_TextConfig

- 

  - 
            func (*CloudStorageConfig_TextConfig) Descriptor() ([]byte, []int)deprecated

  - 
            func (*CloudStorageConfig_TextConfig) ProtoMessage()

  - 
            func (x *CloudStorageConfig_TextConfig) ProtoReflect() protoreflect.Message

  - 
            func (x *CloudStorageConfig_TextConfig) Reset()

  - 
            func (x *CloudStorageConfig_TextConfig) String() string

- 
          type CloudStorageConfig_TextConfig_

- 
          type CommitSchemaRequest

- 

  - 
            func (*CommitSchemaRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *CommitSchemaRequest) GetName() string

  - 
            func (x *CommitSchemaRequest) GetSchema() *Schema

  - 
            func (*CommitSchemaRequest) ProtoMessage()

  - 
            func (x *CommitSchemaRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *CommitSchemaRequest) Reset()

  - 
            func (x *CommitSchemaRequest) String() string

- 
          type CreateSchemaRequest

- 

  - 
            func (*CreateSchemaRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *CreateSchemaRequest) GetParent() string

  - 
            func (x *CreateSchemaRequest) GetSchema() *Schema

  - 
            func (x *CreateSchemaRequest) GetSchemaId() string

  - 
            func (*CreateSchemaRequest) ProtoMessage()

  - 
            func (x *CreateSchemaRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *CreateSchemaRequest) Reset()

  - 
            func (x *CreateSchemaRequest) String() string

- 
          type CreateSnapshotRequest

- 

  - 
            func (*CreateSnapshotRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *CreateSnapshotRequest) GetLabels() map[string]string

  - 
            func (x *CreateSnapshotRequest) GetName() string

  - 
            func (x *CreateSnapshotRequest) GetSubscription() string

  - 
            func (x *CreateSnapshotRequest) GetTags() map[string]string

  - 
            func (*CreateSnapshotRequest) ProtoMessage()

  - 
            func (x *CreateSnapshotRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *CreateSnapshotRequest) Reset()

  - 
            func (x *CreateSnapshotRequest) String() string

- 
          type DeadLetterPolicy

- 

  - 
            func (*DeadLetterPolicy) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *DeadLetterPolicy) GetDeadLetterTopic() string

  - 
            func (x *DeadLetterPolicy) GetMaxDeliveryAttempts() int32

  - 
            func (*DeadLetterPolicy) ProtoMessage()

  - 
            func (x *DeadLetterPolicy) ProtoReflect() protoreflect.Message

  - 
            func (x *DeadLetterPolicy) Reset()

  - 
            func (x *DeadLetterPolicy) String() string

- 
          type DeleteSchemaRequest

- 

  - 
            func (*DeleteSchemaRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *DeleteSchemaRequest) GetName() string

  - 
            func (*DeleteSchemaRequest) ProtoMessage()

  - 
            func (x *DeleteSchemaRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *DeleteSchemaRequest) Reset()

  - 
            func (x *DeleteSchemaRequest) String() string

- 
          type DeleteSchemaRevisionRequest

- 

  - 
            func (*DeleteSchemaRevisionRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *DeleteSchemaRevisionRequest) GetName() string

  - 
            func (x *DeleteSchemaRevisionRequest) GetRevisionId() stringdeprecated

  - 
            func (*DeleteSchemaRevisionRequest) ProtoMessage()

  - 
            func (x *DeleteSchemaRevisionRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *DeleteSchemaRevisionRequest) Reset()

  - 
            func (x *DeleteSchemaRevisionRequest) String() string

- 
          type DeleteSnapshotRequest

- 

  - 
            func (*DeleteSnapshotRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *DeleteSnapshotRequest) GetSnapshot() string

  - 
            func (*DeleteSnapshotRequest) ProtoMessage()

  - 
            func (x *DeleteSnapshotRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *DeleteSnapshotRequest) Reset()

  - 
            func (x *DeleteSnapshotRequest) String() string

- 
          type DeleteSubscriptionRequest

- 

  - 
            func (*DeleteSubscriptionRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *DeleteSubscriptionRequest) GetSubscription() string

  - 
            func (*DeleteSubscriptionRequest) ProtoMessage()

  - 
            func (x *DeleteSubscriptionRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *DeleteSubscriptionRequest) Reset()

  - 
            func (x *DeleteSubscriptionRequest) String() string

- 
          type DeleteTopicRequest

- 

  - 
            func (*DeleteTopicRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *DeleteTopicRequest) GetTopic() string

  - 
            func (*DeleteTopicRequest) ProtoMessage()

  - 
            func (x *DeleteTopicRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *DeleteTopicRequest) Reset()

  - 
            func (x *DeleteTopicRequest) String() string

- 
          type DetachSubscriptionRequest

- 

  - 
            func (*DetachSubscriptionRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *DetachSubscriptionRequest) GetSubscription() string

  - 
            func (*DetachSubscriptionRequest) ProtoMessage()

  - 
            func (x *DetachSubscriptionRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *DetachSubscriptionRequest) Reset()

  - 
            func (x *DetachSubscriptionRequest) String() string

- 
          type DetachSubscriptionResponse

- 

  - 
            func (*DetachSubscriptionResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (*DetachSubscriptionResponse) ProtoMessage()

  - 
            func (x *DetachSubscriptionResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *DetachSubscriptionResponse) Reset()

  - 
            func (x *DetachSubscriptionResponse) String() string

- 
          type Encoding

- 

  - 
            func (Encoding) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x Encoding) Enum() *Encoding

  - 
            func (Encoding) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x Encoding) Number() protoreflect.EnumNumber

  - 
            func (x Encoding) String() string

  - 
            func (Encoding) Type() protoreflect.EnumType

- 
          type ExpirationPolicy

- 

  - 
            func (*ExpirationPolicy) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ExpirationPolicy) GetTtl() *durationpb.Duration

  - 
            func (*ExpirationPolicy) ProtoMessage()

  - 
            func (x *ExpirationPolicy) ProtoReflect() protoreflect.Message

  - 
            func (x *ExpirationPolicy) Reset()

  - 
            func (x *ExpirationPolicy) String() string

- 
          type GetSchemaRequest

- 

  - 
            func (*GetSchemaRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *GetSchemaRequest) GetName() string

  - 
            func (x *GetSchemaRequest) GetView() SchemaView

  - 
            func (*GetSchemaRequest) ProtoMessage()

  - 
            func (x *GetSchemaRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *GetSchemaRequest) Reset()

  - 
            func (x *GetSchemaRequest) String() string

- 
          type GetSnapshotRequest

- 

  - 
            func (*GetSnapshotRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *GetSnapshotRequest) GetSnapshot() string

  - 
            func (*GetSnapshotRequest) ProtoMessage()

  - 
            func (x *GetSnapshotRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *GetSnapshotRequest) Reset()

  - 
            func (x *GetSnapshotRequest) String() string

- 
          type GetSubscriptionRequest

- 

  - 
            func (*GetSubscriptionRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *GetSubscriptionRequest) GetSubscription() string

  - 
            func (*GetSubscriptionRequest) ProtoMessage()

  - 
            func (x *GetSubscriptionRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *GetSubscriptionRequest) Reset()

  - 
            func (x *GetSubscriptionRequest) String() string

- 
          type GetTopicRequest

- 

  - 
            func (*GetTopicRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *GetTopicRequest) GetTopic() string

  - 
            func (*GetTopicRequest) ProtoMessage()

  - 
            func (x *GetTopicRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *GetTopicRequest) Reset()

  - 
            func (x *GetTopicRequest) String() string

- 
          type IngestionDataSourceSettings

- 

  - 
            func (*IngestionDataSourceSettings) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionDataSourceSettings) GetAwsKinesis() *IngestionDataSourceSettings_AwsKinesis

  - 
            func (x *IngestionDataSourceSettings) GetAwsMsk() *IngestionDataSourceSettings_AwsMsk

  - 
            func (x *IngestionDataSourceSettings) GetAzureEventHubs() *IngestionDataSourceSettings_AzureEventHubs

  - 
            func (x *IngestionDataSourceSettings) GetCloudStorage() *IngestionDataSourceSettings_CloudStorage

  - 
            func (x *IngestionDataSourceSettings) GetConfluentCloud() *IngestionDataSourceSettings_ConfluentCloud

  - 
            func (x *IngestionDataSourceSettings) GetPlatformLogsSettings() *PlatformLogsSettings

  - 
            func (m *IngestionDataSourceSettings) GetSource() isIngestionDataSourceSettings_Source

  - 
            func (*IngestionDataSourceSettings) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings) Reset()

  - 
            func (x *IngestionDataSourceSettings) String() string

- 
          type IngestionDataSourceSettings_AwsKinesis

- 

  - 
            func (*IngestionDataSourceSettings_AwsKinesis) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) GetAwsRoleArn() string

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) GetConsumerArn() string

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) GetGcpServiceAccount() string

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) GetState() IngestionDataSourceSettings_AwsKinesis_State

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) GetStreamArn() string

  - 
            func (*IngestionDataSourceSettings_AwsKinesis) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) Reset()

  - 
            func (x *IngestionDataSourceSettings_AwsKinesis) String() string

- 
          type IngestionDataSourceSettings_AwsKinesis_

- 
          type IngestionDataSourceSettings_AwsKinesis_State

- 

  - 
            func (IngestionDataSourceSettings_AwsKinesis_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x IngestionDataSourceSettings_AwsKinesis_State) Enum() *IngestionDataSourceSettings_AwsKinesis_State

  - 
            func (IngestionDataSourceSettings_AwsKinesis_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x IngestionDataSourceSettings_AwsKinesis_State) Number() protoreflect.EnumNumber

  - 
            func (x IngestionDataSourceSettings_AwsKinesis_State) String() string

  - 
            func (IngestionDataSourceSettings_AwsKinesis_State) Type() protoreflect.EnumType

- 
          type IngestionDataSourceSettings_AwsMsk

- 

  - 
            func (*IngestionDataSourceSettings_AwsMsk) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) GetAwsRoleArn() string

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) GetClusterArn() string

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) GetGcpServiceAccount() string

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) GetState() IngestionDataSourceSettings_AwsMsk_State

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) GetTopic() string

  - 
            func (*IngestionDataSourceSettings_AwsMsk) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) Reset()

  - 
            func (x *IngestionDataSourceSettings_AwsMsk) String() string

- 
          type IngestionDataSourceSettings_AwsMsk_

- 
          type IngestionDataSourceSettings_AwsMsk_State

- 

  - 
            func (IngestionDataSourceSettings_AwsMsk_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x IngestionDataSourceSettings_AwsMsk_State) Enum() *IngestionDataSourceSettings_AwsMsk_State

  - 
            func (IngestionDataSourceSettings_AwsMsk_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x IngestionDataSourceSettings_AwsMsk_State) Number() protoreflect.EnumNumber

  - 
            func (x IngestionDataSourceSettings_AwsMsk_State) String() string

  - 
            func (IngestionDataSourceSettings_AwsMsk_State) Type() protoreflect.EnumType

- 
          type IngestionDataSourceSettings_AzureEventHubs

- 

  - 
            func (*IngestionDataSourceSettings_AzureEventHubs) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetClientId() string

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetEventHub() string

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetGcpServiceAccount() string

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetNamespace() string

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetResourceGroup() string

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetState() IngestionDataSourceSettings_AzureEventHubs_State

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetSubscriptionId() string

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) GetTenantId() string

  - 
            func (*IngestionDataSourceSettings_AzureEventHubs) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) Reset()

  - 
            func (x *IngestionDataSourceSettings_AzureEventHubs) String() string

- 
          type IngestionDataSourceSettings_AzureEventHubs_

- 
          type IngestionDataSourceSettings_AzureEventHubs_State

- 

  - 
            func (IngestionDataSourceSettings_AzureEventHubs_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x IngestionDataSourceSettings_AzureEventHubs_State) Enum() *IngestionDataSourceSettings_AzureEventHubs_State

  - 
            func (IngestionDataSourceSettings_AzureEventHubs_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x IngestionDataSourceSettings_AzureEventHubs_State) Number() protoreflect.EnumNumber

  - 
            func (x IngestionDataSourceSettings_AzureEventHubs_State) String() string

  - 
            func (IngestionDataSourceSettings_AzureEventHubs_State) Type() protoreflect.EnumType

- 
          type IngestionDataSourceSettings_CloudStorage

- 

  - 
            func (*IngestionDataSourceSettings_CloudStorage) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) GetAvroFormat() *IngestionDataSourceSettings_CloudStorage_AvroFormat

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) GetBucket() string

  - 
            func (m *IngestionDataSourceSettings_CloudStorage) GetInputFormat() isIngestionDataSourceSettings_CloudStorage_InputFormat

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) GetMatchGlob() string

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) GetMinimumObjectCreateTime() *timestamppb.Timestamp

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) GetPubsubAvroFormat() *IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) GetState() IngestionDataSourceSettings_CloudStorage_State

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) GetTextFormat() *IngestionDataSourceSettings_CloudStorage_TextFormat

  - 
            func (*IngestionDataSourceSettings_CloudStorage) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) Reset()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage) String() string

- 
          type IngestionDataSourceSettings_CloudStorage_

- 
          type IngestionDataSourceSettings_CloudStorage_AvroFormat

- 

  - 
            func (*IngestionDataSourceSettings_CloudStorage_AvroFormat) Descriptor() ([]byte, []int)deprecated

  - 
            func (*IngestionDataSourceSettings_CloudStorage_AvroFormat) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_AvroFormat) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_AvroFormat) Reset()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_AvroFormat) String() string

- 
          type IngestionDataSourceSettings_CloudStorage_AvroFormat_

- 
          type IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat

- 

  - 
            func (*IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat) Descriptor() ([]byte, []int)deprecated

  - 
            func (*IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat) Reset()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_PubSubAvroFormat) String() string

- 
          type IngestionDataSourceSettings_CloudStorage_PubsubAvroFormat

- 
          type IngestionDataSourceSettings_CloudStorage_State

- 

  - 
            func (IngestionDataSourceSettings_CloudStorage_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x IngestionDataSourceSettings_CloudStorage_State) Enum() *IngestionDataSourceSettings_CloudStorage_State

  - 
            func (IngestionDataSourceSettings_CloudStorage_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x IngestionDataSourceSettings_CloudStorage_State) Number() protoreflect.EnumNumber

  - 
            func (x IngestionDataSourceSettings_CloudStorage_State) String() string

  - 
            func (IngestionDataSourceSettings_CloudStorage_State) Type() protoreflect.EnumType

- 
          type IngestionDataSourceSettings_CloudStorage_TextFormat

- 

  - 
            func (*IngestionDataSourceSettings_CloudStorage_TextFormat) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_TextFormat) GetDelimiter() string

  - 
            func (*IngestionDataSourceSettings_CloudStorage_TextFormat) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_TextFormat) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_TextFormat) Reset()

  - 
            func (x *IngestionDataSourceSettings_CloudStorage_TextFormat) String() string

- 
          type IngestionDataSourceSettings_CloudStorage_TextFormat_

- 
          type IngestionDataSourceSettings_ConfluentCloud

- 

  - 
            func (*IngestionDataSourceSettings_ConfluentCloud) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) GetBootstrapServer() string

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) GetClusterId() string

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) GetGcpServiceAccount() string

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) GetIdentityPoolId() string

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) GetState() IngestionDataSourceSettings_ConfluentCloud_State

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) GetTopic() string

  - 
            func (*IngestionDataSourceSettings_ConfluentCloud) ProtoMessage()

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) Reset()

  - 
            func (x *IngestionDataSourceSettings_ConfluentCloud) String() string

- 
          type IngestionDataSourceSettings_ConfluentCloud_

- 
          type IngestionDataSourceSettings_ConfluentCloud_State

- 

  - 
            func (IngestionDataSourceSettings_ConfluentCloud_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x IngestionDataSourceSettings_ConfluentCloud_State) Enum() *IngestionDataSourceSettings_ConfluentCloud_State

  - 
            func (IngestionDataSourceSettings_ConfluentCloud_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x IngestionDataSourceSettings_ConfluentCloud_State) Number() protoreflect.EnumNumber

  - 
            func (x IngestionDataSourceSettings_ConfluentCloud_State) String() string

  - 
            func (IngestionDataSourceSettings_ConfluentCloud_State) Type() protoreflect.EnumType

- 
          type IngestionFailureEvent

- 

  - 
            func (*IngestionFailureEvent) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionFailureEvent) GetAwsKinesisFailure() *IngestionFailureEvent_AwsKinesisFailureReason

  - 
            func (x *IngestionFailureEvent) GetAwsMskFailure() *IngestionFailureEvent_AwsMskFailureReason

  - 
            func (x *IngestionFailureEvent) GetAzureEventHubsFailure() *IngestionFailureEvent_AzureEventHubsFailureReason

  - 
            func (x *IngestionFailureEvent) GetCloudStorageFailure() *IngestionFailureEvent_CloudStorageFailure

  - 
            func (x *IngestionFailureEvent) GetConfluentCloudFailure() *IngestionFailureEvent_ConfluentCloudFailureReason

  - 
            func (x *IngestionFailureEvent) GetErrorMessage() string

  - 
            func (m *IngestionFailureEvent) GetFailure() isIngestionFailureEvent_Failure

  - 
            func (x *IngestionFailureEvent) GetTopic() string

  - 
            func (*IngestionFailureEvent) ProtoMessage()

  - 
            func (x *IngestionFailureEvent) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent) Reset()

  - 
            func (x *IngestionFailureEvent) String() string

- 
          type IngestionFailureEvent_ApiViolationReason

- 

  - 
            func (*IngestionFailureEvent_ApiViolationReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (*IngestionFailureEvent_ApiViolationReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_ApiViolationReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_ApiViolationReason) Reset()

  - 
            func (x *IngestionFailureEvent_ApiViolationReason) String() string

- 
          type IngestionFailureEvent_AvroFailureReason

- 

  - 
            func (*IngestionFailureEvent_AvroFailureReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (*IngestionFailureEvent_AvroFailureReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_AvroFailureReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_AvroFailureReason) Reset()

  - 
            func (x *IngestionFailureEvent_AvroFailureReason) String() string

- 
          type IngestionFailureEvent_AwsKinesisFailure

- 
          type IngestionFailureEvent_AwsKinesisFailureReason

- 

  - 
            func (*IngestionFailureEvent_AwsKinesisFailureReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) GetApiViolationReason() *IngestionFailureEvent_ApiViolationReason

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) GetMessageTransformationFailureReason() *IngestionFailureEvent_MessageTransformationFailureReason

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) GetPartitionKey() string

  - 
            func (m *IngestionFailureEvent_AwsKinesisFailureReason) GetReason() isIngestionFailureEvent_AwsKinesisFailureReason_Reason

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) GetSchemaViolationReason() *IngestionFailureEvent_SchemaViolationReason

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) GetSequenceNumber() string

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) GetStreamArn() string

  - 
            func (*IngestionFailureEvent_AwsKinesisFailureReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) Reset()

  - 
            func (x *IngestionFailureEvent_AwsKinesisFailureReason) String() string

- 
          type IngestionFailureEvent_AwsKinesisFailureReason_ApiViolationReason

- 
          type IngestionFailureEvent_AwsKinesisFailureReason_MessageTransformationFailureReason

- 
          type IngestionFailureEvent_AwsKinesisFailureReason_SchemaViolationReason

- 
          type IngestionFailureEvent_AwsMskFailure

- 
          type IngestionFailureEvent_AwsMskFailureReason

- 

  - 
            func (*IngestionFailureEvent_AwsMskFailureReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) GetApiViolationReason() *IngestionFailureEvent_ApiViolationReason

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) GetClusterArn() string

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) GetKafkaTopic() string

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) GetMessageTransformationFailureReason() *IngestionFailureEvent_MessageTransformationFailureReason

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) GetOffset() int64

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) GetPartitionId() int64

  - 
            func (m *IngestionFailureEvent_AwsMskFailureReason) GetReason() isIngestionFailureEvent_AwsMskFailureReason_Reason

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) GetSchemaViolationReason() *IngestionFailureEvent_SchemaViolationReason

  - 
            func (*IngestionFailureEvent_AwsMskFailureReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) Reset()

  - 
            func (x *IngestionFailureEvent_AwsMskFailureReason) String() string

- 
          type IngestionFailureEvent_AwsMskFailureReason_ApiViolationReason

- 
          type IngestionFailureEvent_AwsMskFailureReason_MessageTransformationFailureReason

- 
          type IngestionFailureEvent_AwsMskFailureReason_SchemaViolationReason

- 
          type IngestionFailureEvent_AzureEventHubsFailure

- 
          type IngestionFailureEvent_AzureEventHubsFailureReason

- 

  - 
            func (*IngestionFailureEvent_AzureEventHubsFailureReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) GetApiViolationReason() *IngestionFailureEvent_ApiViolationReason

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) GetEventHub() string

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) GetMessageTransformationFailureReason() *IngestionFailureEvent_MessageTransformationFailureReason

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) GetNamespace() string

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) GetOffset() int64

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) GetPartitionId() int64

  - 
            func (m *IngestionFailureEvent_AzureEventHubsFailureReason) GetReason() isIngestionFailureEvent_AzureEventHubsFailureReason_Reason

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) GetSchemaViolationReason() *IngestionFailureEvent_SchemaViolationReason

  - 
            func (*IngestionFailureEvent_AzureEventHubsFailureReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) Reset()

  - 
            func (x *IngestionFailureEvent_AzureEventHubsFailureReason) String() string

- 
          type IngestionFailureEvent_AzureEventHubsFailureReason_ApiViolationReason

- 
          type IngestionFailureEvent_AzureEventHubsFailureReason_MessageTransformationFailureReason

- 
          type IngestionFailureEvent_AzureEventHubsFailureReason_SchemaViolationReason

- 
          type IngestionFailureEvent_CloudStorageFailure

- 

  - 
            func (*IngestionFailureEvent_CloudStorageFailure) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) GetApiViolationReason() *IngestionFailureEvent_ApiViolationReason

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) GetAvroFailureReason() *IngestionFailureEvent_AvroFailureReason

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) GetBucket() string

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) GetMessageTransformationFailureReason() *IngestionFailureEvent_MessageTransformationFailureReason

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) GetObjectGeneration() int64

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) GetObjectName() string

  - 
            func (m *IngestionFailureEvent_CloudStorageFailure) GetReason() isIngestionFailureEvent_CloudStorageFailure_Reason

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) GetSchemaViolationReason() *IngestionFailureEvent_SchemaViolationReason

  - 
            func (*IngestionFailureEvent_CloudStorageFailure) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) Reset()

  - 
            func (x *IngestionFailureEvent_CloudStorageFailure) String() string

- 
          type IngestionFailureEvent_CloudStorageFailure_

- 
          type IngestionFailureEvent_CloudStorageFailure_ApiViolationReason

- 
          type IngestionFailureEvent_CloudStorageFailure_AvroFailureReason

- 
          type IngestionFailureEvent_CloudStorageFailure_MessageTransformationFailureReason

- 
          type IngestionFailureEvent_CloudStorageFailure_SchemaViolationReason

- 
          type IngestionFailureEvent_ConfluentCloudFailure

- 
          type IngestionFailureEvent_ConfluentCloudFailureReason

- 

  - 
            func (*IngestionFailureEvent_ConfluentCloudFailureReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) GetApiViolationReason() *IngestionFailureEvent_ApiViolationReason

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) GetClusterId() string

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) GetKafkaTopic() string

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) GetMessageTransformationFailureReason() *IngestionFailureEvent_MessageTransformationFailureReason

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) GetOffset() int64

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) GetPartitionId() int64

  - 
            func (m *IngestionFailureEvent_ConfluentCloudFailureReason) GetReason() isIngestionFailureEvent_ConfluentCloudFailureReason_Reason

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) GetSchemaViolationReason() *IngestionFailureEvent_SchemaViolationReason

  - 
            func (*IngestionFailureEvent_ConfluentCloudFailureReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) Reset()

  - 
            func (x *IngestionFailureEvent_ConfluentCloudFailureReason) String() string

- 
          type IngestionFailureEvent_ConfluentCloudFailureReason_ApiViolationReason

- 
          type IngestionFailureEvent_ConfluentCloudFailureReason_MessageTransformationFailureReason

- 
          type IngestionFailureEvent_ConfluentCloudFailureReason_SchemaViolationReason

- 
          type IngestionFailureEvent_MessageTransformationFailureReason

- 

  - 
            func (*IngestionFailureEvent_MessageTransformationFailureReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (*IngestionFailureEvent_MessageTransformationFailureReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_MessageTransformationFailureReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_MessageTransformationFailureReason) Reset()

  - 
            func (x *IngestionFailureEvent_MessageTransformationFailureReason) String() string

- 
          type IngestionFailureEvent_SchemaViolationReason

- 

  - 
            func (*IngestionFailureEvent_SchemaViolationReason) Descriptor() ([]byte, []int)deprecated

  - 
            func (*IngestionFailureEvent_SchemaViolationReason) ProtoMessage()

  - 
            func (x *IngestionFailureEvent_SchemaViolationReason) ProtoReflect() protoreflect.Message

  - 
            func (x *IngestionFailureEvent_SchemaViolationReason) Reset()

  - 
            func (x *IngestionFailureEvent_SchemaViolationReason) String() string

- 
          type JavaScriptUDF

- 

  - 
            func (*JavaScriptUDF) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *JavaScriptUDF) GetCode() string

  - 
            func (x *JavaScriptUDF) GetFunctionName() string

  - 
            func (*JavaScriptUDF) ProtoMessage()

  - 
            func (x *JavaScriptUDF) ProtoReflect() protoreflect.Message

  - 
            func (x *JavaScriptUDF) Reset()

  - 
            func (x *JavaScriptUDF) String() string

- 
          type ListSchemaRevisionsRequest

- 

  - 
            func (*ListSchemaRevisionsRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSchemaRevisionsRequest) GetName() string

  - 
            func (x *ListSchemaRevisionsRequest) GetPageSize() int32

  - 
            func (x *ListSchemaRevisionsRequest) GetPageToken() string

  - 
            func (x *ListSchemaRevisionsRequest) GetView() SchemaView

  - 
            func (*ListSchemaRevisionsRequest) ProtoMessage()

  - 
            func (x *ListSchemaRevisionsRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSchemaRevisionsRequest) Reset()

  - 
            func (x *ListSchemaRevisionsRequest) String() string

- 
          type ListSchemaRevisionsResponse

- 

  - 
            func (*ListSchemaRevisionsResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSchemaRevisionsResponse) GetNextPageToken() string

  - 
            func (x *ListSchemaRevisionsResponse) GetSchemas() []*Schema

  - 
            func (*ListSchemaRevisionsResponse) ProtoMessage()

  - 
            func (x *ListSchemaRevisionsResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSchemaRevisionsResponse) Reset()

  - 
            func (x *ListSchemaRevisionsResponse) String() string

- 
          type ListSchemasRequest

- 

  - 
            func (*ListSchemasRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSchemasRequest) GetPageSize() int32

  - 
            func (x *ListSchemasRequest) GetPageToken() string

  - 
            func (x *ListSchemasRequest) GetParent() string

  - 
            func (x *ListSchemasRequest) GetView() SchemaView

  - 
            func (*ListSchemasRequest) ProtoMessage()

  - 
            func (x *ListSchemasRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSchemasRequest) Reset()

  - 
            func (x *ListSchemasRequest) String() string

- 
          type ListSchemasResponse

- 

  - 
            func (*ListSchemasResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSchemasResponse) GetNextPageToken() string

  - 
            func (x *ListSchemasResponse) GetSchemas() []*Schema

  - 
            func (*ListSchemasResponse) ProtoMessage()

  - 
            func (x *ListSchemasResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSchemasResponse) Reset()

  - 
            func (x *ListSchemasResponse) String() string

- 
          type ListSnapshotsRequest

- 

  - 
            func (*ListSnapshotsRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSnapshotsRequest) GetPageSize() int32

  - 
            func (x *ListSnapshotsRequest) GetPageToken() string

  - 
            func (x *ListSnapshotsRequest) GetProject() string

  - 
            func (*ListSnapshotsRequest) ProtoMessage()

  - 
            func (x *ListSnapshotsRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSnapshotsRequest) Reset()

  - 
            func (x *ListSnapshotsRequest) String() string

- 
          type ListSnapshotsResponse

- 

  - 
            func (*ListSnapshotsResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSnapshotsResponse) GetNextPageToken() string

  - 
            func (x *ListSnapshotsResponse) GetSnapshots() []*Snapshot

  - 
            func (*ListSnapshotsResponse) ProtoMessage()

  - 
            func (x *ListSnapshotsResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSnapshotsResponse) Reset()

  - 
            func (x *ListSnapshotsResponse) String() string

- 
          type ListSubscriptionsRequest

- 

  - 
            func (*ListSubscriptionsRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSubscriptionsRequest) GetPageSize() int32

  - 
            func (x *ListSubscriptionsRequest) GetPageToken() string

  - 
            func (x *ListSubscriptionsRequest) GetProject() string

  - 
            func (*ListSubscriptionsRequest) ProtoMessage()

  - 
            func (x *ListSubscriptionsRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSubscriptionsRequest) Reset()

  - 
            func (x *ListSubscriptionsRequest) String() string

- 
          type ListSubscriptionsResponse

- 

  - 
            func (*ListSubscriptionsResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListSubscriptionsResponse) GetNextPageToken() string

  - 
            func (x *ListSubscriptionsResponse) GetSubscriptions() []*Subscription

  - 
            func (*ListSubscriptionsResponse) ProtoMessage()

  - 
            func (x *ListSubscriptionsResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ListSubscriptionsResponse) Reset()

  - 
            func (x *ListSubscriptionsResponse) String() string

- 
          type ListTopicSnapshotsRequest

- 

  - 
            func (*ListTopicSnapshotsRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListTopicSnapshotsRequest) GetPageSize() int32

  - 
            func (x *ListTopicSnapshotsRequest) GetPageToken() string

  - 
            func (x *ListTopicSnapshotsRequest) GetTopic() string

  - 
            func (*ListTopicSnapshotsRequest) ProtoMessage()

  - 
            func (x *ListTopicSnapshotsRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ListTopicSnapshotsRequest) Reset()

  - 
            func (x *ListTopicSnapshotsRequest) String() string

- 
          type ListTopicSnapshotsResponse

- 

  - 
            func (*ListTopicSnapshotsResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListTopicSnapshotsResponse) GetNextPageToken() string

  - 
            func (x *ListTopicSnapshotsResponse) GetSnapshots() []string

  - 
            func (*ListTopicSnapshotsResponse) ProtoMessage()

  - 
            func (x *ListTopicSnapshotsResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ListTopicSnapshotsResponse) Reset()

  - 
            func (x *ListTopicSnapshotsResponse) String() string

- 
          type ListTopicSubscriptionsRequest

- 

  - 
            func (*ListTopicSubscriptionsRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListTopicSubscriptionsRequest) GetPageSize() int32

  - 
            func (x *ListTopicSubscriptionsRequest) GetPageToken() string

  - 
            func (x *ListTopicSubscriptionsRequest) GetTopic() string

  - 
            func (*ListTopicSubscriptionsRequest) ProtoMessage()

  - 
            func (x *ListTopicSubscriptionsRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ListTopicSubscriptionsRequest) Reset()

  - 
            func (x *ListTopicSubscriptionsRequest) String() string

- 
          type ListTopicSubscriptionsResponse

- 

  - 
            func (*ListTopicSubscriptionsResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListTopicSubscriptionsResponse) GetNextPageToken() string

  - 
            func (x *ListTopicSubscriptionsResponse) GetSubscriptions() []string

  - 
            func (*ListTopicSubscriptionsResponse) ProtoMessage()

  - 
            func (x *ListTopicSubscriptionsResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ListTopicSubscriptionsResponse) Reset()

  - 
            func (x *ListTopicSubscriptionsResponse) String() string

- 
          type ListTopicsRequest

- 

  - 
            func (*ListTopicsRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListTopicsRequest) GetPageSize() int32

  - 
            func (x *ListTopicsRequest) GetPageToken() string

  - 
            func (x *ListTopicsRequest) GetProject() string

  - 
            func (*ListTopicsRequest) ProtoMessage()

  - 
            func (x *ListTopicsRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ListTopicsRequest) Reset()

  - 
            func (x *ListTopicsRequest) String() string

- 
          type ListTopicsResponse

- 

  - 
            func (*ListTopicsResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ListTopicsResponse) GetNextPageToken() string

  - 
            func (x *ListTopicsResponse) GetTopics() []*Topic

  - 
            func (*ListTopicsResponse) ProtoMessage()

  - 
            func (x *ListTopicsResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ListTopicsResponse) Reset()

  - 
            func (x *ListTopicsResponse) String() string

- 
          type MessageStoragePolicy

- 

  - 
            func (*MessageStoragePolicy) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *MessageStoragePolicy) GetAllowedPersistenceRegions() []string

  - 
            func (x *MessageStoragePolicy) GetEnforceInTransit() bool

  - 
            func (*MessageStoragePolicy) ProtoMessage()

  - 
            func (x *MessageStoragePolicy) ProtoReflect() protoreflect.Message

  - 
            func (x *MessageStoragePolicy) Reset()

  - 
            func (x *MessageStoragePolicy) String() string

- 
          type MessageTransform

- 

  - 
            func (*MessageTransform) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *MessageTransform) GetAiInference() *AIInference

  - 
            func (x *MessageTransform) GetDisabled() bool

  - 
            func (x *MessageTransform) GetEnabled() booldeprecated

  - 
            func (x *MessageTransform) GetJavascriptUdf() *JavaScriptUDF

  - 
            func (m *MessageTransform) GetTransform() isMessageTransform_Transform

  - 
            func (*MessageTransform) ProtoMessage()

  - 
            func (x *MessageTransform) ProtoReflect() protoreflect.Message

  - 
            func (x *MessageTransform) Reset()

  - 
            func (x *MessageTransform) String() string

- 
          type MessageTransform_AiInference

- 
          type MessageTransform_JavascriptUdf

- 
          type ModifyAckDeadlineRequest

- 

  - 
            func (*ModifyAckDeadlineRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ModifyAckDeadlineRequest) GetAckDeadlineSeconds() int32

  - 
            func (x *ModifyAckDeadlineRequest) GetAckIds() []string

  - 
            func (x *ModifyAckDeadlineRequest) GetSubscription() string

  - 
            func (*ModifyAckDeadlineRequest) ProtoMessage()

  - 
            func (x *ModifyAckDeadlineRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ModifyAckDeadlineRequest) Reset()

  - 
            func (x *ModifyAckDeadlineRequest) String() string

- 
          type ModifyPushConfigRequest

- 

  - 
            func (*ModifyPushConfigRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ModifyPushConfigRequest) GetPushConfig() *PushConfig

  - 
            func (x *ModifyPushConfigRequest) GetSubscription() string

  - 
            func (*ModifyPushConfigRequest) ProtoMessage()

  - 
            func (x *ModifyPushConfigRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ModifyPushConfigRequest) Reset()

  - 
            func (x *ModifyPushConfigRequest) String() string

- 
          type PlatformLogsSettings

- 

  - 
            func (*PlatformLogsSettings) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PlatformLogsSettings) GetSeverity() PlatformLogsSettings_Severity

  - 
            func (*PlatformLogsSettings) ProtoMessage()

  - 
            func (x *PlatformLogsSettings) ProtoReflect() protoreflect.Message

  - 
            func (x *PlatformLogsSettings) Reset()

  - 
            func (x *PlatformLogsSettings) String() string

- 
          type PlatformLogsSettings_Severity

- 

  - 
            func (PlatformLogsSettings_Severity) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x PlatformLogsSettings_Severity) Enum() *PlatformLogsSettings_Severity

  - 
            func (PlatformLogsSettings_Severity) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x PlatformLogsSettings_Severity) Number() protoreflect.EnumNumber

  - 
            func (x PlatformLogsSettings_Severity) String() string

  - 
            func (PlatformLogsSettings_Severity) Type() protoreflect.EnumType

- 
          type PublishRequest

- 

  - 
            func (*PublishRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PublishRequest) GetMessages() []*PubsubMessage

  - 
            func (x *PublishRequest) GetTopic() string

  - 
            func (*PublishRequest) ProtoMessage()

  - 
            func (x *PublishRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *PublishRequest) Reset()

  - 
            func (x *PublishRequest) String() string

- 
          type PublishResponse

- 

  - 
            func (*PublishResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PublishResponse) GetMessageIds() []string

  - 
            func (*PublishResponse) ProtoMessage()

  - 
            func (x *PublishResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *PublishResponse) Reset()

  - 
            func (x *PublishResponse) String() string

- 
          type PublisherClient

- 

  - 
            func NewPublisherClient(cc grpc.ClientConnInterface) PublisherClient

- 
          type PublisherServer

- 
          type PubsubMessage

- 

  - 
            func (*PubsubMessage) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PubsubMessage) GetAttributes() map[string]string

  - 
            func (x *PubsubMessage) GetData() []byte

  - 
            func (x *PubsubMessage) GetMessageId() string

  - 
            func (x *PubsubMessage) GetOrderingKey() string

  - 
            func (x *PubsubMessage) GetPublishTime() *timestamppb.Timestamp

  - 
            func (*PubsubMessage) ProtoMessage()

  - 
            func (x *PubsubMessage) ProtoReflect() protoreflect.Message

  - 
            func (x *PubsubMessage) Reset()

  - 
            func (x *PubsubMessage) String() string

- 
          type PullRequest

- 

  - 
            func (*PullRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PullRequest) GetMaxMessages() int32

  - 
            func (x *PullRequest) GetReturnImmediately() booldeprecated

  - 
            func (x *PullRequest) GetSubscription() string

  - 
            func (*PullRequest) ProtoMessage()

  - 
            func (x *PullRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *PullRequest) Reset()

  - 
            func (x *PullRequest) String() string

- 
          type PullResponse

- 

  - 
            func (*PullResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PullResponse) GetReceivedMessages() []*ReceivedMessage

  - 
            func (*PullResponse) ProtoMessage()

  - 
            func (x *PullResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *PullResponse) Reset()

  - 
            func (x *PullResponse) String() string

- 
          type PushConfig

- 

  - 
            func (*PushConfig) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PushConfig) GetAttributes() map[string]string

  - 
            func (m *PushConfig) GetAuthenticationMethod() isPushConfig_AuthenticationMethod

  - 
            func (x *PushConfig) GetNoWrapper() *PushConfig_NoWrapper

  - 
            func (x *PushConfig) GetOidcToken() *PushConfig_OidcToken

  - 
            func (x *PushConfig) GetPubsubWrapper() *PushConfig_PubsubWrapper

  - 
            func (x *PushConfig) GetPushEndpoint() string

  - 
            func (m *PushConfig) GetWrapper() isPushConfig_Wrapper

  - 
            func (*PushConfig) ProtoMessage()

  - 
            func (x *PushConfig) ProtoReflect() protoreflect.Message

  - 
            func (x *PushConfig) Reset()

  - 
            func (x *PushConfig) String() string

- 
          type PushConfig_NoWrapper

- 

  - 
            func (*PushConfig_NoWrapper) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PushConfig_NoWrapper) GetWriteMetadata() bool

  - 
            func (*PushConfig_NoWrapper) ProtoMessage()

  - 
            func (x *PushConfig_NoWrapper) ProtoReflect() protoreflect.Message

  - 
            func (x *PushConfig_NoWrapper) Reset()

  - 
            func (x *PushConfig_NoWrapper) String() string

- 
          type PushConfig_NoWrapper_

- 
          type PushConfig_OidcToken

- 

  - 
            func (*PushConfig_OidcToken) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PushConfig_OidcToken) GetAudience() string

  - 
            func (x *PushConfig_OidcToken) GetServiceAccountEmail() string

  - 
            func (*PushConfig_OidcToken) ProtoMessage()

  - 
            func (x *PushConfig_OidcToken) ProtoReflect() protoreflect.Message

  - 
            func (x *PushConfig_OidcToken) Reset()

  - 
            func (x *PushConfig_OidcToken) String() string

- 
          type PushConfig_OidcToken_

- 
          type PushConfig_PubsubWrapper

- 

  - 
            func (*PushConfig_PubsubWrapper) Descriptor() ([]byte, []int)deprecated

  - 
            func (*PushConfig_PubsubWrapper) ProtoMessage()

  - 
            func (x *PushConfig_PubsubWrapper) ProtoReflect() protoreflect.Message

  - 
            func (x *PushConfig_PubsubWrapper) Reset()

  - 
            func (x *PushConfig_PubsubWrapper) String() string

- 
          type PushConfig_PubsubWrapper_

- 
          type ReceivedMessage

- 

  - 
            func (*ReceivedMessage) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ReceivedMessage) GetAckId() string

  - 
            func (x *ReceivedMessage) GetDeliveryAttempt() int32

  - 
            func (x *ReceivedMessage) GetMessage() *PubsubMessage

  - 
            func (*ReceivedMessage) ProtoMessage()

  - 
            func (x *ReceivedMessage) ProtoReflect() protoreflect.Message

  - 
            func (x *ReceivedMessage) Reset()

  - 
            func (x *ReceivedMessage) String() string

- 
          type RetryPolicy

- 

  - 
            func (*RetryPolicy) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *RetryPolicy) GetMaximumBackoff() *durationpb.Duration

  - 
            func (x *RetryPolicy) GetMinimumBackoff() *durationpb.Duration

  - 
            func (*RetryPolicy) ProtoMessage()

  - 
            func (x *RetryPolicy) ProtoReflect() protoreflect.Message

  - 
            func (x *RetryPolicy) Reset()

  - 
            func (x *RetryPolicy) String() string

- 
          type RollbackSchemaRequest

- 

  - 
            func (*RollbackSchemaRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *RollbackSchemaRequest) GetName() string

  - 
            func (x *RollbackSchemaRequest) GetRevisionId() string

  - 
            func (*RollbackSchemaRequest) ProtoMessage()

  - 
            func (x *RollbackSchemaRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *RollbackSchemaRequest) Reset()

  - 
            func (x *RollbackSchemaRequest) String() string

- 
          type Schema

- 

  - 
            func (*Schema) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Schema) GetDefinition() string

  - 
            func (x *Schema) GetName() string

  - 
            func (x *Schema) GetRevisionCreateTime() *timestamppb.Timestamp

  - 
            func (x *Schema) GetRevisionId() string

  - 
            func (x *Schema) GetType() Schema_Type

  - 
            func (*Schema) ProtoMessage()

  - 
            func (x *Schema) ProtoReflect() protoreflect.Message

  - 
            func (x *Schema) Reset()

  - 
            func (x *Schema) String() string

- 
          type SchemaServiceClient

- 

  - 
            func NewSchemaServiceClient(cc grpc.ClientConnInterface) SchemaServiceClient

- 
          type SchemaServiceServer

- 
          type SchemaSettings

- 

  - 
            func (*SchemaSettings) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *SchemaSettings) GetEncoding() Encoding

  - 
            func (x *SchemaSettings) GetFirstRevisionId() string

  - 
            func (x *SchemaSettings) GetLastRevisionId() string

  - 
            func (x *SchemaSettings) GetSchema() string

  - 
            func (*SchemaSettings) ProtoMessage()

  - 
            func (x *SchemaSettings) ProtoReflect() protoreflect.Message

  - 
            func (x *SchemaSettings) Reset()

  - 
            func (x *SchemaSettings) String() string

- 
          type SchemaView

- 

  - 
            func (SchemaView) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x SchemaView) Enum() *SchemaView

  - 
            func (SchemaView) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x SchemaView) Number() protoreflect.EnumNumber

  - 
            func (x SchemaView) String() string

  - 
            func (SchemaView) Type() protoreflect.EnumType

- 
          type Schema_Type

- 

  - 
            func (Schema_Type) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x Schema_Type) Enum() *Schema_Type

  - 
            func (Schema_Type) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x Schema_Type) Number() protoreflect.EnumNumber

  - 
            func (x Schema_Type) String() string

  - 
            func (Schema_Type) Type() protoreflect.EnumType

- 
          type SeekRequest

- 

  - 
            func (*SeekRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *SeekRequest) GetSnapshot() string

  - 
            func (x *SeekRequest) GetSubscription() string

  - 
            func (m *SeekRequest) GetTarget() isSeekRequest_Target

  - 
            func (x *SeekRequest) GetTime() *timestamppb.Timestamp

  - 
            func (*SeekRequest) ProtoMessage()

  - 
            func (x *SeekRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *SeekRequest) Reset()

  - 
            func (x *SeekRequest) String() string

- 
          type SeekRequest_Snapshot

- 
          type SeekRequest_Time

- 
          type SeekResponse

- 

  - 
            func (*SeekResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (*SeekResponse) ProtoMessage()

  - 
            func (x *SeekResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *SeekResponse) Reset()

  - 
            func (x *SeekResponse) String() string

- 
          type Snapshot

- 

  - 
            func (*Snapshot) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Snapshot) GetExpireTime() *timestamppb.Timestamp

  - 
            func (x *Snapshot) GetLabels() map[string]string

  - 
            func (x *Snapshot) GetName() string

  - 
            func (x *Snapshot) GetTopic() string

  - 
            func (*Snapshot) ProtoMessage()

  - 
            func (x *Snapshot) ProtoReflect() protoreflect.Message

  - 
            func (x *Snapshot) Reset()

  - 
            func (x *Snapshot) String() string

- 
          type StreamingPullRequest

- 

  - 
            func (*StreamingPullRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *StreamingPullRequest) GetAckIds() []string

  - 
            func (x *StreamingPullRequest) GetClientId() string

  - 
            func (x *StreamingPullRequest) GetMaxOutstandingBytes() int64

  - 
            func (x *StreamingPullRequest) GetMaxOutstandingMessages() int64

  - 
            func (x *StreamingPullRequest) GetModifyDeadlineAckIds() []string

  - 
            func (x *StreamingPullRequest) GetModifyDeadlineSeconds() []int32

  - 
            func (x *StreamingPullRequest) GetProtocolVersion() int64

  - 
            func (x *StreamingPullRequest) GetStreamAckDeadlineSeconds() int32

  - 
            func (x *StreamingPullRequest) GetSubscription() string

  - 
            func (*StreamingPullRequest) ProtoMessage()

  - 
            func (x *StreamingPullRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *StreamingPullRequest) Reset()

  - 
            func (x *StreamingPullRequest) String() string

- 
          type StreamingPullResponse

- 

  - 
            func (*StreamingPullResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *StreamingPullResponse) GetAcknowledgeConfirmation() *StreamingPullResponse_AcknowledgeConfirmation

  - 
            func (x *StreamingPullResponse) GetModifyAckDeadlineConfirmation() *StreamingPullResponse_ModifyAckDeadlineConfirmation

  - 
            func (x *StreamingPullResponse) GetReceivedMessages() []*ReceivedMessage

  - 
            func (x *StreamingPullResponse) GetSubscriptionProperties() *StreamingPullResponse_SubscriptionProperties

  - 
            func (*StreamingPullResponse) ProtoMessage()

  - 
            func (x *StreamingPullResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *StreamingPullResponse) Reset()

  - 
            func (x *StreamingPullResponse) String() string

- 
          type StreamingPullResponse_AcknowledgeConfirmation

- 

  - 
            func (*StreamingPullResponse_AcknowledgeConfirmation) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *StreamingPullResponse_AcknowledgeConfirmation) GetAckIds() []string

  - 
            func (x *StreamingPullResponse_AcknowledgeConfirmation) GetInvalidAckIds() []string

  - 
            func (x *StreamingPullResponse_AcknowledgeConfirmation) GetTemporaryFailedAckIds() []string

  - 
            func (x *StreamingPullResponse_AcknowledgeConfirmation) GetUnorderedAckIds() []string

  - 
            func (*StreamingPullResponse_AcknowledgeConfirmation) ProtoMessage()

  - 
            func (x *StreamingPullResponse_AcknowledgeConfirmation) ProtoReflect() protoreflect.Message

  - 
            func (x *StreamingPullResponse_AcknowledgeConfirmation) Reset()

  - 
            func (x *StreamingPullResponse_AcknowledgeConfirmation) String() string

- 
          type StreamingPullResponse_ModifyAckDeadlineConfirmation

- 

  - 
            func (*StreamingPullResponse_ModifyAckDeadlineConfirmation) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *StreamingPullResponse_ModifyAckDeadlineConfirmation) GetAckIds() []string

  - 
            func (x *StreamingPullResponse_ModifyAckDeadlineConfirmation) GetInvalidAckIds() []string

  - 
            func (x *StreamingPullResponse_ModifyAckDeadlineConfirmation) GetTemporaryFailedAckIds() []string

  - 
            func (*StreamingPullResponse_ModifyAckDeadlineConfirmation) ProtoMessage()

  - 
            func (x *StreamingPullResponse_ModifyAckDeadlineConfirmation) ProtoReflect() protoreflect.Message

  - 
            func (x *StreamingPullResponse_ModifyAckDeadlineConfirmation) Reset()

  - 
            func (x *StreamingPullResponse_ModifyAckDeadlineConfirmation) String() string

- 
          type StreamingPullResponse_SubscriptionProperties

- 

  - 
            func (*StreamingPullResponse_SubscriptionProperties) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *StreamingPullResponse_SubscriptionProperties) GetExactlyOnceDeliveryEnabled() bool

  - 
            func (x *StreamingPullResponse_SubscriptionProperties) GetMessageOrderingEnabled() bool

  - 
            func (*StreamingPullResponse_SubscriptionProperties) ProtoMessage()

  - 
            func (x *StreamingPullResponse_SubscriptionProperties) ProtoReflect() protoreflect.Message

  - 
            func (x *StreamingPullResponse_SubscriptionProperties) Reset()

  - 
            func (x *StreamingPullResponse_SubscriptionProperties) String() string

- 
          type SubscriberClient

- 

  - 
            func NewSubscriberClient(cc grpc.ClientConnInterface) SubscriberClient

- 
          type SubscriberServer

- 
          type Subscriber_StreamingPullClient

- 
          type Subscriber_StreamingPullServer

- 
          type Subscription

- 

  - 
            func (*Subscription) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Subscription) GetAckDeadlineSeconds() int32

  - 
            func (x *Subscription) GetAnalyticsHubSubscriptionInfo() *Subscription_AnalyticsHubSubscriptionInfo

  - 
            func (x *Subscription) GetBigqueryConfig() *BigQueryConfig

  - 
            func (x *Subscription) GetCloudStorageConfig() *CloudStorageConfig

  - 
            func (x *Subscription) GetDeadLetterPolicy() *DeadLetterPolicy

  - 
            func (x *Subscription) GetDetached() bool

  - 
            func (x *Subscription) GetEnableExactlyOnceDelivery() bool

  - 
            func (x *Subscription) GetEnableMessageOrdering() bool

  - 
            func (x *Subscription) GetExpirationPolicy() *ExpirationPolicy

  - 
            func (x *Subscription) GetFilter() string

  - 
            func (x *Subscription) GetLabels() map[string]string

  - 
            func (x *Subscription) GetMessageRetentionDuration() *durationpb.Duration

  - 
            func (x *Subscription) GetMessageTransforms() []*MessageTransform

  - 
            func (x *Subscription) GetName() string

  - 
            func (x *Subscription) GetPushConfig() *PushConfig

  - 
            func (x *Subscription) GetRetainAckedMessages() bool

  - 
            func (x *Subscription) GetRetryPolicy() *RetryPolicy

  - 
            func (x *Subscription) GetState() Subscription_State

  - 
            func (x *Subscription) GetTags() map[string]string

  - 
            func (x *Subscription) GetTopic() string

  - 
            func (x *Subscription) GetTopicMessageRetentionDuration() *durationpb.Duration

  - 
            func (*Subscription) ProtoMessage()

  - 
            func (x *Subscription) ProtoReflect() protoreflect.Message

  - 
            func (x *Subscription) Reset()

  - 
            func (x *Subscription) String() string

- 
          type Subscription_AnalyticsHubSubscriptionInfo

- 

  - 
            func (*Subscription_AnalyticsHubSubscriptionInfo) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Subscription_AnalyticsHubSubscriptionInfo) GetListing() string

  - 
            func (x *Subscription_AnalyticsHubSubscriptionInfo) GetSubscription() string

  - 
            func (*Subscription_AnalyticsHubSubscriptionInfo) ProtoMessage()

  - 
            func (x *Subscription_AnalyticsHubSubscriptionInfo) ProtoReflect() protoreflect.Message

  - 
            func (x *Subscription_AnalyticsHubSubscriptionInfo) Reset()

  - 
            func (x *Subscription_AnalyticsHubSubscriptionInfo) String() string

- 
          type Subscription_State

- 

  - 
            func (Subscription_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x Subscription_State) Enum() *Subscription_State

  - 
            func (Subscription_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x Subscription_State) Number() protoreflect.EnumNumber

  - 
            func (x Subscription_State) String() string

  - 
            func (Subscription_State) Type() protoreflect.EnumType

- 
          type Topic

- 

  - 
            func (*Topic) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Topic) GetIngestionDataSourceSettings() *IngestionDataSourceSettings

  - 
            func (x *Topic) GetKmsKeyName() string

  - 
            func (x *Topic) GetLabels() map[string]string

  - 
            func (x *Topic) GetMessageRetentionDuration() *durationpb.Duration

  - 
            func (x *Topic) GetMessageStoragePolicy() *MessageStoragePolicy

  - 
            func (x *Topic) GetMessageTransforms() []*MessageTransform

  - 
            func (x *Topic) GetName() string

  - 
            func (x *Topic) GetSatisfiesPzs() bool

  - 
            func (x *Topic) GetSchemaSettings() *SchemaSettings

  - 
            func (x *Topic) GetState() Topic_State

  - 
            func (x *Topic) GetTags() map[string]string

  - 
            func (*Topic) ProtoMessage()

  - 
            func (x *Topic) ProtoReflect() protoreflect.Message

  - 
            func (x *Topic) Reset()

  - 
            func (x *Topic) String() string

- 
          type Topic_State

- 

  - 
            func (Topic_State) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x Topic_State) Enum() *Topic_State

  - 
            func (Topic_State) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x Topic_State) Number() protoreflect.EnumNumber

  - 
            func (x Topic_State) String() string

  - 
            func (Topic_State) Type() protoreflect.EnumType

- 
          type UnimplementedPublisherServer

- 

  - 
            func (UnimplementedPublisherServer) CreateTopic(context.Context, *Topic) (*Topic, error)

  - 
            func (UnimplementedPublisherServer) DeleteTopic(context.Context, *DeleteTopicRequest) (*emptypb.Empty, error)

  - 
            func (UnimplementedPublisherServer) DetachSubscription(context.Context, *DetachSubscriptionRequest) (*DetachSubscriptionResponse, error)

  - 
            func (UnimplementedPublisherServer) GetTopic(context.Context, *GetTopicRequest) (*Topic, error)

  - 
            func (UnimplementedPublisherServer) ListTopicSnapshots(context.Context, *ListTopicSnapshotsRequest) (*ListTopicSnapshotsResponse, error)

  - 
            func (UnimplementedPublisherServer) ListTopicSubscriptions(context.Context, *ListTopicSubscriptionsRequest) (*ListTopicSubscriptionsResponse, error)

  - 
            func (UnimplementedPublisherServer) ListTopics(context.Context, *ListTopicsRequest) (*ListTopicsResponse, error)

  - 
            func (UnimplementedPublisherServer) Publish(context.Context, *PublishRequest) (*PublishResponse, error)

  - 
            func (UnimplementedPublisherServer) UpdateTopic(context.Context, *UpdateTopicRequest) (*Topic, error)

- 
          type UnimplementedSchemaServiceServer

- 

  - 
            func (UnimplementedSchemaServiceServer) CommitSchema(context.Context, *CommitSchemaRequest) (*Schema, error)

  - 
            func (UnimplementedSchemaServiceServer) CreateSchema(context.Context, *CreateSchemaRequest) (*Schema, error)

  - 
            func (UnimplementedSchemaServiceServer) DeleteSchema(context.Context, *DeleteSchemaRequest) (*emptypb.Empty, error)

  - 
            func (UnimplementedSchemaServiceServer) DeleteSchemaRevision(context.Context, *DeleteSchemaRevisionRequest) (*Schema, error)

  - 
            func (UnimplementedSchemaServiceServer) GetSchema(context.Context, *GetSchemaRequest) (*Schema, error)

  - 
            func (UnimplementedSchemaServiceServer) ListSchemaRevisions(context.Context, *ListSchemaRevisionsRequest) (*ListSchemaRevisionsResponse, error)

  - 
            func (UnimplementedSchemaServiceServer) ListSchemas(context.Context, *ListSchemasRequest) (*ListSchemasResponse, error)

  - 
            func (UnimplementedSchemaServiceServer) RollbackSchema(context.Context, *RollbackSchemaRequest) (*Schema, error)

  - 
            func (UnimplementedSchemaServiceServer) ValidateMessage(context.Context, *ValidateMessageRequest) (*ValidateMessageResponse, error)

  - 
            func (UnimplementedSchemaServiceServer) ValidateSchema(context.Context, *ValidateSchemaRequest) (*ValidateSchemaResponse, error)

- 
          type UnimplementedSubscriberServer

- 

  - 
            func (UnimplementedSubscriberServer) Acknowledge(context.Context, *AcknowledgeRequest) (*emptypb.Empty, error)

  - 
            func (UnimplementedSubscriberServer) CreateSnapshot(context.Context, *CreateSnapshotRequest) (*Snapshot, error)

  - 
            func (UnimplementedSubscriberServer) CreateSubscription(context.Context, *Subscription) (*Subscription, error)

  - 
            func (UnimplementedSubscriberServer) DeleteSnapshot(context.Context, *DeleteSnapshotRequest) (*emptypb.Empty, error)

  - 
            func (UnimplementedSubscriberServer) DeleteSubscription(context.Context, *DeleteSubscriptionRequest) (*emptypb.Empty, error)

  - 
            func (UnimplementedSubscriberServer) GetSnapshot(context.Context, *GetSnapshotRequest) (*Snapshot, error)

  - 
            func (UnimplementedSubscriberServer) GetSubscription(context.Context, *GetSubscriptionRequest) (*Subscription, error)

  - 
            func (UnimplementedSubscriberServer) ListSnapshots(context.Context, *ListSnapshotsRequest) (*ListSnapshotsResponse, error)

  - 
            func (UnimplementedSubscriberServer) ListSubscriptions(context.Context, *ListSubscriptionsRequest) (*ListSubscriptionsResponse, error)

  - 
            func (UnimplementedSubscriberServer) ModifyAckDeadline(context.Context, *ModifyAckDeadlineRequest) (*emptypb.Empty, error)

  - 
            func (UnimplementedSubscriberServer) ModifyPushConfig(context.Context, *ModifyPushConfigRequest) (*emptypb.Empty, error)

  - 
            func (UnimplementedSubscriberServer) Pull(context.Context, *PullRequest) (*PullResponse, error)

  - 
            func (UnimplementedSubscriberServer) Seek(context.Context, *SeekRequest) (*SeekResponse, error)

  - 
            func (UnimplementedSubscriberServer) StreamingPull(Subscriber_StreamingPullServer) error

  - 
            func (UnimplementedSubscriberServer) UpdateSnapshot(context.Context, *UpdateSnapshotRequest) (*Snapshot, error)

  - 
            func (UnimplementedSubscriberServer) UpdateSubscription(context.Context, *UpdateSubscriptionRequest) (*Subscription, error)

- 
          type UnsafePublisherServer

- 
          type UnsafeSchemaServiceServer

- 
          type UnsafeSubscriberServer

- 
          type UpdateSnapshotRequest

- 

  - 
            func (*UpdateSnapshotRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *UpdateSnapshotRequest) GetSnapshot() *Snapshot

  - 
            func (x *UpdateSnapshotRequest) GetUpdateMask() *fieldmaskpb.FieldMask

  - 
            func (*UpdateSnapshotRequest) ProtoMessage()

  - 
            func (x *UpdateSnapshotRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *UpdateSnapshotRequest) Reset()

  - 
            func (x *UpdateSnapshotRequest) String() string

- 
          type UpdateSubscriptionRequest

- 

  - 
            func (*UpdateSubscriptionRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *UpdateSubscriptionRequest) GetSubscription() *Subscription

  - 
            func (x *UpdateSubscriptionRequest) GetUpdateMask() *fieldmaskpb.FieldMask

  - 
            func (*UpdateSubscriptionRequest) ProtoMessage()

  - 
            func (x *UpdateSubscriptionRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *UpdateSubscriptionRequest) Reset()

  - 
            func (x *UpdateSubscriptionRequest) String() string

- 
          type UpdateTopicRequest

- 

  - 
            func (*UpdateTopicRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *UpdateTopicRequest) GetTopic() *Topic

  - 
            func (x *UpdateTopicRequest) GetUpdateMask() *fieldmaskpb.FieldMask

  - 
            func (*UpdateTopicRequest) ProtoMessage()

  - 
            func (x *UpdateTopicRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *UpdateTopicRequest) Reset()

  - 
            func (x *UpdateTopicRequest) String() string

- 
          type ValidateMessageRequest

- 

  - 
            func (*ValidateMessageRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ValidateMessageRequest) GetEncoding() Encoding

  - 
            func (x *ValidateMessageRequest) GetMessage() []byte

  - 
            func (x *ValidateMessageRequest) GetName() string

  - 
            func (x *ValidateMessageRequest) GetParent() string

  - 
            func (x *ValidateMessageRequest) GetSchema() *Schema

  - 
            func (m *ValidateMessageRequest) GetSchemaSpec() isValidateMessageRequest_SchemaSpec

  - 
            func (*ValidateMessageRequest) ProtoMessage()

  - 
            func (x *ValidateMessageRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ValidateMessageRequest) Reset()

  - 
            func (x *ValidateMessageRequest) String() string

- 
          type ValidateMessageRequest_Name

- 
          type ValidateMessageRequest_Schema

- 
          type ValidateMessageResponse

- 

  - 
            func (*ValidateMessageResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (*ValidateMessageResponse) ProtoMessage()

  - 
            func (x *ValidateMessageResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ValidateMessageResponse) Reset()

  - 
            func (x *ValidateMessageResponse) String() string

- 
          type ValidateSchemaRequest

- 

  - 
            func (*ValidateSchemaRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *ValidateSchemaRequest) GetParent() string

  - 
            func (x *ValidateSchemaRequest) GetSchema() *Schema

  - 
            func (*ValidateSchemaRequest) ProtoMessage()

  - 
            func (x *ValidateSchemaRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *ValidateSchemaRequest) Reset()

  - 
            func (x *ValidateSchemaRequest) String() string

- 
          type ValidateSchemaResponse

- 

  - 
            func (*ValidateSchemaResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (*ValidateSchemaResponse) ProtoMessage()

  - 
            func (x *ValidateSchemaResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *ValidateSchemaResponse) Reset()

  - 
            func (x *ValidateSchemaResponse) String() string

### Constants ¶

  
    
      View Source
      

```
const (
	Publisher_CreateTopic_FullMethodName            = "/google.pubsub.v1.Publisher/CreateTopic"
	Publisher_UpdateTopic_FullMethodName            = "/google.pubsub.v1.Publisher/UpdateTopic"
	Publisher_Publish_FullMethodName                = "/google.pubsub.v1.Publisher/Publish"
	Publisher_GetTopic_FullMethodName               = "/google.pubsub.v1.Publisher/GetTopic"
	Publisher_ListTopics_FullMethodName             = "/google.pubsub.v1.Publisher/ListTopics"
	Publisher_ListTopicSubscriptions_FullMethodName = "/google.pubsub.v1.Publisher/ListTopicSubscriptions"
	Publisher_ListTopicSnapshots_FullMethodName     = "/google.pubsub.v1.Publisher/ListTopicSnapshots"
	Publisher_DeleteTopic_FullMethodName            = "/google.pubsub.v1.Publisher/DeleteTopic"
	Publisher_DetachSubscription_FullMethodName     = "/google.pubsub.v1.Publisher/DetachSubscription"
)
```

    
  

    
      View Source
      

```
const (
	Subscriber_CreateSubscription_FullMethodName = "/google.pubsub.v1.Subscriber/CreateSubscription"
	Subscriber_GetSubscription_FullMethodName    = "/google.pubsub.v1.Subscriber/GetSubscription"
	Subscriber_UpdateSubscription_FullMethodName = "/google.pubsub.v1.Subscriber/UpdateSubscription"
	Subscriber_ListSubscriptions_FullMethodName  = "/google.pubsub.v1.Subscriber/ListSubscriptions"
	Subscriber_DeleteSubscription_FullMethodName = "/google.pubsub.v1.Subscriber/DeleteSubscription"
	Subscriber_ModifyAckDeadline_FullMethodName  = "/google.pubsub.v1.Subscriber/ModifyAckDeadline"
	Subscriber_Acknowledge_FullMethodName        = "/google.pubsub.v1.Subscriber/Acknowledge"
	Subscriber_Pull_FullMethodName               = "/google.pubsub.v1.Subscriber/Pull"
	Subscriber_StreamingPull_FullMethodName      = "/google.pubsub.v1.Subscriber/StreamingPull"
	Subscriber_ModifyPushConfig_FullMethodName   = "/google.pubsub.v1.Subscriber/ModifyPushConfig"
	Subscriber_GetSnapshot_FullMethodName        = "/google.pubsub.v1.Subscriber/GetSnapshot"
	Subscriber_ListSnapshots_FullMethodName      = "/google.pubsub.v1.Subscriber/ListSnapshots"
	Subscriber_CreateSnapshot_FullMethodName     = "/google.pubsub.v1.Subscriber/CreateSnapshot"
	Subscriber_UpdateSnapshot_FullMethodName     = "/google.pubsub.v1.Subscriber/UpdateSnapshot"
	Subscriber_DeleteSnapshot_FullMethodName     = "/google.pubsub.v1.Subscriber/DeleteSnapshot"
	Subscriber_Seek_FullMethodName               = "/google.pubsub.v1.Subscriber/Seek"
)
```

    
  

    
      View Source
      

```
const (
	SchemaService_CreateSchema_FullMethodName         = "/google.pubsub.v1.SchemaService/CreateSchema"
	SchemaService_GetSchema_FullMethodName            = "/google.pubsub.v1.SchemaService/GetSchema"
	SchemaService_ListSchemas_FullMethodName          = "/google.pubsub.v1.SchemaService/ListSchemas"
	SchemaService_ListSchemaRevisions_FullMethodName  = "/google.pubsub.v1.SchemaService/ListSchemaRevisions"
	SchemaService_CommitSchema_FullMethodName         = "/google.pubsub.v1.SchemaService/CommitSchema"
	SchemaService_RollbackSchema_FullMethodName       = "/google.pubsub.v1.SchemaService/RollbackSchema"
	SchemaService_DeleteSchemaRevision_FullMethodName = "/google.pubsub.v1.SchemaService/DeleteSchemaRevision"
	SchemaService_DeleteSchema_FullMethodName         = "/google.pubsub.v1.SchemaService/DeleteSchema"
	SchemaService_ValidateSchema_FullMethodName       = "/google.pubsub.v1.SchemaService/ValidateSchema"
	SchemaService_ValidateMessage_FullMethodName      = "/google.pubsub.v1.SchemaService/ValidateMessage"
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var (
	IngestionDataSourceSettings_AwsKinesis_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "KINESIS_PERMISSION_DENIED",
		3: "PUBLISH_PERMISSION_DENIED",
		4: "STREAM_NOT_FOUND",
		5: "CONSUMER_NOT_FOUND",
	}
	IngestionDataSourceSettings_AwsKinesis_State_value = map[string]int32{
		"STATE_UNSPECIFIED":         0,
		"ACTIVE":                    1,
		"KINESIS_PERMISSION_DENIED": 2,
		"PUBLISH_PERMISSION_DENIED": 3,
		"STREAM_NOT_FOUND":          4,
		"CONSUMER_NOT_FOUND":        5,
	}
)
```

    
  

Enum value maps for IngestionDataSourceSettings_AwsKinesis_State.

    
      View Source
      

```
var (
	IngestionDataSourceSettings_CloudStorage_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "CLOUD_STORAGE_PERMISSION_DENIED",
		3: "PUBLISH_PERMISSION_DENIED",
		4: "BUCKET_NOT_FOUND",
		5: "TOO_MANY_OBJECTS",
	}
	IngestionDataSourceSettings_CloudStorage_State_value = map[string]int32{
		"STATE_UNSPECIFIED":               0,
		"ACTIVE":                          1,
		"CLOUD_STORAGE_PERMISSION_DENIED": 2,
		"PUBLISH_PERMISSION_DENIED":       3,
		"BUCKET_NOT_FOUND":                4,
		"TOO_MANY_OBJECTS":                5,
	}
)
```

    
  

Enum value maps for IngestionDataSourceSettings_CloudStorage_State.

    
      View Source
      

```
var (
	IngestionDataSourceSettings_AzureEventHubs_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "EVENT_HUBS_PERMISSION_DENIED",
		3: "PUBLISH_PERMISSION_DENIED",
		4: "NAMESPACE_NOT_FOUND",
		5: "EVENT_HUB_NOT_FOUND",
		6: "SUBSCRIPTION_NOT_FOUND",
		7: "RESOURCE_GROUP_NOT_FOUND",
	}
	IngestionDataSourceSettings_AzureEventHubs_State_value = map[string]int32{
		"STATE_UNSPECIFIED":            0,
		"ACTIVE":                       1,
		"EVENT_HUBS_PERMISSION_DENIED": 2,
		"PUBLISH_PERMISSION_DENIED":    3,
		"NAMESPACE_NOT_FOUND":          4,
		"EVENT_HUB_NOT_FOUND":          5,
		"SUBSCRIPTION_NOT_FOUND":       6,
		"RESOURCE_GROUP_NOT_FOUND":     7,
	}
)
```

    
  

Enum value maps for IngestionDataSourceSettings_AzureEventHubs_State.

    
      View Source
      

```
var (
	IngestionDataSourceSettings_AwsMsk_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "MSK_PERMISSION_DENIED",
		3: "PUBLISH_PERMISSION_DENIED",
		4: "CLUSTER_NOT_FOUND",
		5: "TOPIC_NOT_FOUND",
	}
	IngestionDataSourceSettings_AwsMsk_State_value = map[string]int32{
		"STATE_UNSPECIFIED":         0,
		"ACTIVE":                    1,
		"MSK_PERMISSION_DENIED":     2,
		"PUBLISH_PERMISSION_DENIED": 3,
		"CLUSTER_NOT_FOUND":         4,
		"TOPIC_NOT_FOUND":           5,
	}
)
```

    
  

Enum value maps for IngestionDataSourceSettings_AwsMsk_State.

    
      View Source
      

```
var (
	IngestionDataSourceSettings_ConfluentCloud_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "CONFLUENT_CLOUD_PERMISSION_DENIED",
		3: "PUBLISH_PERMISSION_DENIED",
		4: "UNREACHABLE_BOOTSTRAP_SERVER",
		5: "CLUSTER_NOT_FOUND",
		6: "TOPIC_NOT_FOUND",
	}
	IngestionDataSourceSettings_ConfluentCloud_State_value = map[string]int32{
		"STATE_UNSPECIFIED":                 0,
		"ACTIVE":                            1,
		"CONFLUENT_CLOUD_PERMISSION_DENIED": 2,
		"PUBLISH_PERMISSION_DENIED":         3,
		"UNREACHABLE_BOOTSTRAP_SERVER":      4,
		"CLUSTER_NOT_FOUND":                 5,
		"TOPIC_NOT_FOUND":                   6,
	}
)
```

    
  

Enum value maps for IngestionDataSourceSettings_ConfluentCloud_State.

    
      View Source
      

```
var (
	PlatformLogsSettings_Severity_name = map[int32]string{
		0: "SEVERITY_UNSPECIFIED",
		1: "DISABLED",
		2: "DEBUG",
		3: "INFO",
		4: "WARNING",
		5: "ERROR",
	}
	PlatformLogsSettings_Severity_value = map[string]int32{
		"SEVERITY_UNSPECIFIED": 0,
		"DISABLED":             1,
		"DEBUG":                2,
		"INFO":                 3,
		"WARNING":              4,
		"ERROR":                5,
	}
)
```

    
  

Enum value maps for PlatformLogsSettings_Severity.

    
      View Source
      

```
var (
	Topic_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "INGESTION_RESOURCE_ERROR",
	}
	Topic_State_value = map[string]int32{
		"STATE_UNSPECIFIED":        0,
		"ACTIVE":                   1,
		"INGESTION_RESOURCE_ERROR": 2,
	}
)
```

    
  

Enum value maps for Topic_State.

    
      View Source
      

```
var (
	Subscription_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "RESOURCE_ERROR",
	}
	Subscription_State_value = map[string]int32{
		"STATE_UNSPECIFIED": 0,
		"ACTIVE":            1,
		"RESOURCE_ERROR":    2,
	}
)
```

    
  

Enum value maps for Subscription_State.

    
      View Source
      

```
var (
	BigQueryConfig_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "PERMISSION_DENIED",
		3: "NOT_FOUND",
		4: "SCHEMA_MISMATCH",
		5: "IN_TRANSIT_LOCATION_RESTRICTION",
		6: "VERTEX_AI_LOCATION_RESTRICTION",
	}
	BigQueryConfig_State_value = map[string]int32{
		"STATE_UNSPECIFIED":               0,
		"ACTIVE":                          1,
		"PERMISSION_DENIED":               2,
		"NOT_FOUND":                       3,
		"SCHEMA_MISMATCH":                 4,
		"IN_TRANSIT_LOCATION_RESTRICTION": 5,
		"VERTEX_AI_LOCATION_RESTRICTION":  6,
	}
)
```

    
  

Enum value maps for BigQueryConfig_State.

    
      View Source
      

```
var (
	CloudStorageConfig_State_name = map[int32]string{
		0: "STATE_UNSPECIFIED",
		1: "ACTIVE",
		2: "PERMISSION_DENIED",
		3: "NOT_FOUND",
		4: "IN_TRANSIT_LOCATION_RESTRICTION",
		5: "SCHEMA_MISMATCH",
		6: "VERTEX_AI_LOCATION_RESTRICTION",
	}
	CloudStorageConfig_State_value = map[string]int32{
		"STATE_UNSPECIFIED":               0,
		"ACTIVE":                          1,
		"PERMISSION_DENIED":               2,
		"NOT_FOUND":                       3,
		"IN_TRANSIT_LOCATION_RESTRICTION": 4,
		"SCHEMA_MISMATCH":                 5,
		"VERTEX_AI_LOCATION_RESTRICTION":  6,
	}
)
```

    
  

Enum value maps for CloudStorageConfig_State.

    
      View Source
      

```
var (
	SchemaView_name = map[int32]string{
		0: "SCHEMA_VIEW_UNSPECIFIED",
		1: "BASIC",
		2: "FULL",
	}
	SchemaView_value = map[string]int32{
		"SCHEMA_VIEW_UNSPECIFIED": 0,
		"BASIC":                   1,
		"FULL":                    2,
	}
)
```

    
  

Enum value maps for SchemaView.

    
      View Source
      

```
var (
	Encoding_name = map[int32]string{
		0: "ENCODING_UNSPECIFIED",
		1: "JSON",
		2: "BINARY",
	}
	Encoding_value = map[string]int32{
		"ENCODING_UNSPECIFIED": 0,
		"JSON":                 1,
		"BINARY":               2,
	}
)
```

    
  

Enum value maps for Encoding.

    
      View Source
      

```
var (
	Schema_Type_name = map[int32]string{
		0: "TYPE_UNSPECIFIED",
		1: "PROTOCOL_BUFFER",
		2: "AVRO",
	}
	Schema_Type_value = map[string]int32{
		"TYPE_UNSPECIFIED": 0,
		"PROTOCOL_BUFFER":  1,
		"AVRO":             2,
	}
)
```

    
  

Enum value maps for Schema_Type.

    
      View Source
      

```
var File_google_pubsub_v1_pubsub_proto protoreflect.FileDescriptor
```

    
  

    
      View Source
      

```
var File_google_pubsub_v1_schema_proto protoreflect.FileDescriptor
```

    
  

    
      View Source
      

```
var Publisher_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "google.pubsub.v1.Publisher",
	HandlerType: (*PublisherServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateTopic",
			Handler:    _Publisher_CreateTopic_Handler,
		},
		{
			MethodName: "UpdateTopic",
			Handler:    _Publisher_UpdateTopic_Handler,
		},
		{
			MethodName: "Publish",
			Handler:    _Publisher_Publish_Handler,
		},
		{
			MethodName: "GetTopic",
			Handler:    _Publisher_GetTopic_Handler,
		},
		{
			MethodName: "ListTopics",
			Handler:    _Publisher_ListTopics_Handler,
		},
		{
			MethodName: "ListTopicSubscriptions",
			Handler:    _Publisher_ListTopicSubscriptions_Handler,
		},
		{
			MethodName: "ListTopicSnapshots",
			Handler:    _Publisher_ListTopicSnapshots_Handler,
		},
		{
			MethodName: "DeleteTopic",
			Handler:    _Publisher_DeleteTopic_Handler,
		},
		{
			MethodName: "DetachSubscription",
			Handler:    _Publisher_DetachSubscription_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "google/pubsub/v1/pubsub.proto",
}
```

    
  

Publisher_ServiceDesc is the grpc.ServiceDesc for Publisher service.
It's only intended for direct use with grpc.RegisterService,
and not to be introspected or modified (even as a copy)

    
      View Source
      

```
var SchemaService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "google.pubsub.v1.SchemaService",
	HandlerType: (*SchemaServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateSchema",
			Handler:    _SchemaService_CreateSchema_Handler,
		},
		{
			MethodName: "GetSchema",
			Handler:    _SchemaService_GetSchema_Handler,
		},
		{
			MethodName: "ListSchemas",
			Handler:    _SchemaService_ListSchemas_Handler,
		},
		{
			MethodName: "ListSchemaRevisions",
			Handler:    _SchemaService_ListSchemaRevisions_Handler,
		},
		{
			MethodName: "CommitSchema",
			Handler:    _SchemaService_CommitSchema_Handler,
		},
		{
			MethodName: "RollbackSchema",
			Handler:    _SchemaService_RollbackSchema_Handler,
		},
		{
			MethodName: "DeleteSchemaRevision",
			Handler:    _SchemaService_DeleteSchemaRevision_Handler,
		},
		{
			MethodName: "DeleteSchema",
			Handler:    _SchemaService_DeleteSchema_Handler,
		},
		{
			MethodName: "ValidateSchema",
			Handler:    _SchemaService_ValidateSchema_Handler,
		},
		{
			MethodName: "ValidateMessage",
			Handler:    _SchemaService_ValidateMessage_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "google/pubsub/v1/schema.proto",
}
```

    
  

SchemaService_ServiceDesc is the grpc.ServiceDesc for SchemaService service.
It's only intended for direct use with grpc.RegisterService,
and not to be introspected or modified (even as a copy)

    
      View Source
      

```
var Subscriber_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "google.pubsub.v1.Subscriber",
	HandlerType: (*SubscriberServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateSubscription",
			Handler:    _Subscriber_CreateSubscription_Handler,
		},
		{
			MethodName: "GetSubscription",
			Handler:    _Subscriber_GetSubscription_Handler,
		},
		{
			MethodName: "UpdateSubscription",
			Handler:    _Subscriber_UpdateSubscription_Handler,
		},
		{
			MethodName: "ListSubscriptions",
			Handler:    _Subscriber_ListSubscriptions_Handler,
		},
		{
			MethodName: "DeleteSubscription",
			Handler:    _Subscriber_DeleteSubscription_Handler,
		},
		{
			MethodName: "ModifyAckDeadline",
			Handler:    _Subscriber_ModifyAckDeadline_Handler,
		},
		{
			MethodName: "Acknowledge",
			Handler:    _Subscriber_Acknowledge_Handler,
		},
		{
			MethodName: "Pull",
			Handler:    _Subscriber_Pull_Handler,
		},
		{
			MethodName: "ModifyPushConfig",
			Handler:    _Subscriber_ModifyPushConfig_Handler,
		},
		{
			MethodName: "GetSnapshot",
			Handler:    _Subscriber_GetSnapshot_Handler,
		},
		{
			MethodName: "ListSnapshots",
			Handler:    _Subscriber_ListSnapshots_Handler,
		},
		{
			MethodName: "CreateSnapshot",
			Handler:    _Subscriber_CreateSnapshot_Handler,
		},
		{
			MethodName: "UpdateSnapshot",
			Handler:    _Subscriber_UpdateSnapshot_Handler,
		},
		{
			MethodName: "DeleteSnapshot",
			Handler:    _Subscriber_DeleteSnapshot_Handler,
		},
		{
			MethodName: "Seek",
			Handler:    _Subscriber_Seek_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "StreamingPull",
			Handler:       _Subscriber_StreamingPull_Handler,
			ServerStreams: true,
			ClientStreams: true,
		},
	},
	Metadata: "google/pubsub/v1/pubsub.proto",
}
```

    
  

Subscriber_ServiceDesc is the grpc.ServiceDesc for Subscriber service.
It's only intended for direct use with grpc.RegisterService,
and not to be introspected or modified (even as a copy)

  
### Functions ¶

  
	  
  
  
    
#### 
      func RegisterPublisherServer ¶
  
    
  

    
    
      

```
func RegisterPublisherServer(s grpc.ServiceRegistrar, srv PublisherServer)
```