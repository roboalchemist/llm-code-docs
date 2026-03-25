### Overview ¶

Package pubsub aliases all exported identifiers in package
"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb".

Deprecated: Please use types in: cloud.google.com/go/pubsub/v2/apiv1/pubsubpb.

    
### Index ¶

- Constants

- Variables

- 
        func RegisterPublisherServer(s *grpc.Server, srv PublisherServer)deprecated

- 
        func RegisterSchemaServiceServer(s *grpc.Server, srv SchemaServiceServer)deprecated

- 
        func RegisterSubscriberServer(s *grpc.Server, srv SubscriberServer)deprecated

- 
          type AcknowledgeRequestdeprecated

- 
          type BigQueryConfigdeprecated

- 
          type BigQueryConfig_Statedeprecated

- 
          type CloudStorageConfigdeprecated

- 
          type CloudStorageConfig_AvroConfigdeprecated

- 
          type CloudStorageConfig_AvroConfig_

- 
          type CloudStorageConfig_Statedeprecated

- 
          type CloudStorageConfig_TextConfigdeprecated

- 
          type CloudStorageConfig_TextConfig_

- 
          type CommitSchemaRequestdeprecated

- 
          type CreateSchemaRequestdeprecated

- 
          type CreateSnapshotRequestdeprecated

- 
          type DeadLetterPolicydeprecated

- 
          type DeleteSchemaRequestdeprecated

- 
          type DeleteSchemaRevisionRequestdeprecated

- 
          type DeleteSnapshotRequestdeprecated

- 
          type DeleteSubscriptionRequestdeprecated

- 
          type DeleteTopicRequestdeprecated

- 
          type DetachSubscriptionRequestdeprecated

- 
          type DetachSubscriptionResponsedeprecated

- 
          type Encodingdeprecated

- 
          type ExpirationPolicydeprecated

- 
          type GetSchemaRequestdeprecated

- 
          type GetSnapshotRequestdeprecated

- 
          type GetSubscriptionRequestdeprecated

- 
          type GetTopicRequestdeprecated

- 
          type IngestionDataSourceSettingsdeprecated

- 
          type IngestionDataSourceSettings_AwsKinesisdeprecated

- 
          type IngestionDataSourceSettings_AwsKinesis_

- 
          type IngestionDataSourceSettings_AwsKinesis_Statedeprecated

- 
          type IngestionDataSourceSettings_AwsMskdeprecated

- 
          type IngestionDataSourceSettings_AwsMsk_

- 
          type IngestionDataSourceSettings_AwsMsk_Statedeprecated

- 
          type IngestionDataSourceSettings_AzureEventHubsdeprecated

- 
          type IngestionDataSourceSettings_AzureEventHubs_

- 
          type IngestionDataSourceSettings_AzureEventHubs_Statedeprecated

- 
          type IngestionDataSourceSettings_CloudStoragedeprecated

- 
          type IngestionDataSourceSettings_CloudStorage_

- 
          type IngestionDataSourceSettings_CloudStorage_AvroFormatdeprecated

- 
          type IngestionDataSourceSettings_CloudStorage_AvroFormat_

- 
          type IngestionDataSourceSettings_CloudStorage_PubSubAvroFormatdeprecated

- 
          type IngestionDataSourceSettings_CloudStorage_PubsubAvroFormat

- 
          type IngestionDataSourceSettings_CloudStorage_Statedeprecated

- 
          type IngestionDataSourceSettings_CloudStorage_TextFormatdeprecated

- 
          type IngestionDataSourceSettings_CloudStorage_TextFormat_

- 
          type IngestionDataSourceSettings_ConfluentClouddeprecated

- 
          type IngestionDataSourceSettings_ConfluentCloud_

- 
          type IngestionDataSourceSettings_ConfluentCloud_Statedeprecated

- 
          type IngestionFailureEventdeprecated

- 
          type IngestionFailureEvent_ApiViolationReasondeprecated

- 
          type IngestionFailureEvent_AvroFailureReasondeprecated

- 
          type IngestionFailureEvent_AwsMskFailure

- 
          type IngestionFailureEvent_AwsMskFailureReasondeprecated

- 
          type IngestionFailureEvent_AwsMskFailureReason_ApiViolationReason

- 
          type IngestionFailureEvent_AzureEventHubsFailure

- 
          type IngestionFailureEvent_AzureEventHubsFailureReasondeprecated

- 
          type IngestionFailureEvent_AzureEventHubsFailureReason_ApiViolationReason

- 
          type IngestionFailureEvent_CloudStorageFailuredeprecated

- 
          type IngestionFailureEvent_CloudStorageFailure_

- 
          type IngestionFailureEvent_CloudStorageFailure_ApiViolationReason

- 
          type IngestionFailureEvent_CloudStorageFailure_AvroFailureReason

- 
          type IngestionFailureEvent_ConfluentCloudFailure

- 
          type IngestionFailureEvent_ConfluentCloudFailureReasondeprecated

- 
          type IngestionFailureEvent_ConfluentCloudFailureReason_ApiViolationReason

- 
          type JavaScriptUDFdeprecated

- 
          type ListSchemaRevisionsRequestdeprecated

- 
          type ListSchemaRevisionsResponsedeprecated

- 
          type ListSchemasRequestdeprecated

- 
          type ListSchemasResponsedeprecated

- 
          type ListSnapshotsRequestdeprecated

- 
          type ListSnapshotsResponsedeprecated

- 
          type ListSubscriptionsRequestdeprecated

- 
          type ListSubscriptionsResponsedeprecated

- 
          type ListTopicSnapshotsRequestdeprecated

- 
          type ListTopicSnapshotsResponsedeprecated

- 
          type ListTopicSubscriptionsRequestdeprecated

- 
          type ListTopicSubscriptionsResponsedeprecated

- 
          type ListTopicsRequestdeprecated

- 
          type ListTopicsResponsedeprecated

- 
          type MessageStoragePolicydeprecated

- 
          type MessageTransformdeprecated

- 
          type MessageTransform_JavascriptUdf

- 
          type ModifyAckDeadlineRequestdeprecated

- 
          type ModifyPushConfigRequestdeprecated

- 
          type PlatformLogsSettingsdeprecated

- 
          type PlatformLogsSettings_Severitydeprecated

- 
          type PublishRequestdeprecated

- 
          type PublishResponsedeprecated

- 
          type PublisherClientdeprecated

- 

  - 
            func NewPublisherClient(cc grpc.ClientConnInterface) PublisherClientdeprecated

- 
          type PublisherServerdeprecated

- 
          type PubsubMessagedeprecated

- 
          type PullRequestdeprecated

- 
          type PullResponsedeprecated

- 
          type PushConfigdeprecated

- 
          type PushConfig_NoWrapperdeprecated

- 
          type PushConfig_NoWrapper_

- 
          type PushConfig_OidcTokendeprecated

- 
          type PushConfig_OidcToken_

- 
          type PushConfig_PubsubWrapperdeprecated

- 
          type PushConfig_PubsubWrapper_

- 
          type ReceivedMessagedeprecated

- 
          type RetryPolicydeprecated

- 
          type RollbackSchemaRequestdeprecated

- 
          type Schemadeprecated

- 
          type SchemaServiceClientdeprecated

- 

  - 
            func NewSchemaServiceClient(cc grpc.ClientConnInterface) SchemaServiceClientdeprecated

- 
          type SchemaServiceServerdeprecated

- 
          type SchemaSettingsdeprecated

- 
          type SchemaViewdeprecated

- 
          type Schema_Typedeprecated

- 
          type SeekRequestdeprecated

- 
          type SeekRequest_Snapshot

- 
          type SeekRequest_Time

- 
          type SeekResponsedeprecated

- 
          type Snapshotdeprecated

- 
          type StreamingPullRequestdeprecated

- 
          type StreamingPullResponsedeprecated

- 
          type StreamingPullResponse_AcknowledgeConfirmationdeprecated

- 
          type StreamingPullResponse_ModifyAckDeadlineConfirmationdeprecated

- 
          type StreamingPullResponse_SubscriptionPropertiesdeprecated

- 
          type SubscriberClientdeprecated

- 

  - 
            func NewSubscriberClient(cc grpc.ClientConnInterface) SubscriberClientdeprecated

- 
          type SubscriberServerdeprecated

- 
          type Subscriber_StreamingPullClient

- 
          type Subscriber_StreamingPullServer

- 
          type Subscriptiondeprecated

- 
          type Subscription_AnalyticsHubSubscriptionInfodeprecated

- 
          type Subscription_Statedeprecated

- 
          type Topicdeprecated

- 
          type Topic_Statedeprecated

- 
          type UnimplementedPublisherServerdeprecated

- 
          type UnimplementedSchemaServiceServerdeprecated

- 
          type UnimplementedSubscriberServerdeprecated

- 
          type UpdateSnapshotRequestdeprecated

- 
          type UpdateSubscriptionRequestdeprecated

- 
          type UpdateTopicRequestdeprecated

- 
          type ValidateMessageRequestdeprecated

- 
          type ValidateMessageRequest_Name

- 
          type ValidateMessageRequest_Schema

- 
          type ValidateMessageResponsedeprecated

- 
          type ValidateSchemaRequestdeprecated

- 
          type ValidateSchemaResponsedeprecated

### Constants ¶

  
    
      View Source
      

```
const (
	BigQueryConfig_ACTIVE                                                        = src.BigQueryConfig_ACTIVE
	BigQueryConfig_IN_TRANSIT_LOCATION_RESTRICTION                               = src.BigQueryConfig_IN_TRANSIT_LOCATION_RESTRICTION
	BigQueryConfig_NOT_FOUND                                                     = src.BigQueryConfig_NOT_FOUND
	BigQueryConfig_PERMISSION_DENIED                                             = src.BigQueryConfig_PERMISSION_DENIED
	BigQueryConfig_SCHEMA_MISMATCH                                               = src.BigQueryConfig_SCHEMA_MISMATCH
	BigQueryConfig_STATE_UNSPECIFIED                                             = src.BigQueryConfig_STATE_UNSPECIFIED
	CloudStorageConfig_ACTIVE                                                    = src.CloudStorageConfig_ACTIVE
	CloudStorageConfig_IN_TRANSIT_LOCATION_RESTRICTION                           = src.CloudStorageConfig_IN_TRANSIT_LOCATION_RESTRICTION
	CloudStorageConfig_NOT_FOUND                                                 = src.CloudStorageConfig_NOT_FOUND
	CloudStorageConfig_PERMISSION_DENIED                                         = src.CloudStorageConfig_PERMISSION_DENIED
	CloudStorageConfig_SCHEMA_MISMATCH                                           = src.CloudStorageConfig_SCHEMA_MISMATCH
	CloudStorageConfig_STATE_UNSPECIFIED                                         = src.CloudStorageConfig_STATE_UNSPECIFIED
	Encoding_BINARY                                                              = src.Encoding_BINARY
	Encoding_ENCODING_UNSPECIFIED                                                = src.Encoding_ENCODING_UNSPECIFIED
	Encoding_JSON                                                                = src.Encoding_JSON
	IngestionDataSourceSettings_AwsKinesis_ACTIVE                                = src.IngestionDataSourceSettings_AwsKinesis_ACTIVE
	IngestionDataSourceSettings_AwsKinesis_CONSUMER_NOT_FOUND                    = src.IngestionDataSourceSettings_AwsKinesis_CONSUMER_NOT_FOUND
	IngestionDataSourceSettings_AwsKinesis_KINESIS_PERMISSION_DENIED             = src.IngestionDataSourceSettings_AwsKinesis_KINESIS_PERMISSION_DENIED
	IngestionDataSourceSettings_AwsKinesis_PUBLISH_PERMISSION_DENIED             = src.IngestionDataSourceSettings_AwsKinesis_PUBLISH_PERMISSION_DENIED
	IngestionDataSourceSettings_AwsKinesis_STATE_UNSPECIFIED                     = src.IngestionDataSourceSettings_AwsKinesis_STATE_UNSPECIFIED
	IngestionDataSourceSettings_AwsKinesis_STREAM_NOT_FOUND                      = src.IngestionDataSourceSettings_AwsKinesis_STREAM_NOT_FOUND
	IngestionDataSourceSettings_AwsMsk_ACTIVE                                    = src.IngestionDataSourceSettings_AwsMsk_ACTIVE
	IngestionDataSourceSettings_AwsMsk_CLUSTER_NOT_FOUND                         = src.IngestionDataSourceSettings_AwsMsk_CLUSTER_NOT_FOUND
	IngestionDataSourceSettings_AwsMsk_MSK_PERMISSION_DENIED                     = src.IngestionDataSourceSettings_AwsMsk_MSK_PERMISSION_DENIED
	IngestionDataSourceSettings_AwsMsk_PUBLISH_PERMISSION_DENIED                 = src.IngestionDataSourceSettings_AwsMsk_PUBLISH_PERMISSION_DENIED
	IngestionDataSourceSettings_AwsMsk_STATE_UNSPECIFIED                         = src.IngestionDataSourceSettings_AwsMsk_STATE_UNSPECIFIED
	IngestionDataSourceSettings_AwsMsk_TOPIC_NOT_FOUND                           = src.IngestionDataSourceSettings_AwsMsk_TOPIC_NOT_FOUND
	IngestionDataSourceSettings_AzureEventHubs_ACTIVE                            = src.IngestionDataSourceSettings_AzureEventHubs_ACTIVE
	IngestionDataSourceSettings_AzureEventHubs_EVENT_HUBS_PERMISSION_DENIED      = src.IngestionDataSourceSettings_AzureEventHubs_EVENT_HUBS_PERMISSION_DENIED
	IngestionDataSourceSettings_AzureEventHubs_EVENT_HUB_NOT_FOUND               = src.IngestionDataSourceSettings_AzureEventHubs_EVENT_HUB_NOT_FOUND
	IngestionDataSourceSettings_AzureEventHubs_NAMESPACE_NOT_FOUND               = src.IngestionDataSourceSettings_AzureEventHubs_NAMESPACE_NOT_FOUND
	IngestionDataSourceSettings_AzureEventHubs_PUBLISH_PERMISSION_DENIED         = src.IngestionDataSourceSettings_AzureEventHubs_PUBLISH_PERMISSION_DENIED
	IngestionDataSourceSettings_AzureEventHubs_RESOURCE_GROUP_NOT_FOUND          = src.IngestionDataSourceSettings_AzureEventHubs_RESOURCE_GROUP_NOT_FOUND
	IngestionDataSourceSettings_AzureEventHubs_STATE_UNSPECIFIED                 = src.IngestionDataSourceSettings_AzureEventHubs_STATE_UNSPECIFIED
	IngestionDataSourceSettings_AzureEventHubs_SUBSCRIPTION_NOT_FOUND            = src.IngestionDataSourceSettings_AzureEventHubs_SUBSCRIPTION_NOT_FOUND
	IngestionDataSourceSettings_CloudStorage_ACTIVE                              = src.IngestionDataSourceSettings_CloudStorage_ACTIVE
	IngestionDataSourceSettings_CloudStorage_BUCKET_NOT_FOUND                    = src.IngestionDataSourceSettings_CloudStorage_BUCKET_NOT_FOUND
	IngestionDataSourceSettings_CloudStorage_CLOUD_STORAGE_PERMISSION_DENIED     = src.IngestionDataSourceSettings_CloudStorage_CLOUD_STORAGE_PERMISSION_DENIED
	IngestionDataSourceSettings_CloudStorage_PUBLISH_PERMISSION_DENIED           = src.IngestionDataSourceSettings_CloudStorage_PUBLISH_PERMISSION_DENIED
	IngestionDataSourceSettings_CloudStorage_STATE_UNSPECIFIED                   = src.IngestionDataSourceSettings_CloudStorage_STATE_UNSPECIFIED
	IngestionDataSourceSettings_CloudStorage_TOO_MANY_OBJECTS                    = src.IngestionDataSourceSettings_CloudStorage_TOO_MANY_OBJECTS
	IngestionDataSourceSettings_ConfluentCloud_ACTIVE                            = src.IngestionDataSourceSettings_ConfluentCloud_ACTIVE
	IngestionDataSourceSettings_ConfluentCloud_CLUSTER_NOT_FOUND                 = src.IngestionDataSourceSettings_ConfluentCloud_CLUSTER_NOT_FOUND
	IngestionDataSourceSettings_ConfluentCloud_CONFLUENT_CLOUD_PERMISSION_DENIED = src.IngestionDataSourceSettings_ConfluentCloud_CONFLUENT_CLOUD_PERMISSION_DENIED
	IngestionDataSourceSettings_ConfluentCloud_PUBLISH_PERMISSION_DENIED         = src.IngestionDataSourceSettings_ConfluentCloud_PUBLISH_PERMISSION_DENIED
	IngestionDataSourceSettings_ConfluentCloud_STATE_UNSPECIFIED                 = src.IngestionDataSourceSettings_ConfluentCloud_STATE_UNSPECIFIED
	IngestionDataSourceSettings_ConfluentCloud_TOPIC_NOT_FOUND                   = src.IngestionDataSourceSettings_ConfluentCloud_TOPIC_NOT_FOUND
	IngestionDataSourceSettings_ConfluentCloud_UNREACHABLE_BOOTSTRAP_SERVER      = src.IngestionDataSourceSettings_ConfluentCloud_UNREACHABLE_BOOTSTRAP_SERVER
	PlatformLogsSettings_DEBUG                                                   = src.PlatformLogsSettings_DEBUG
	PlatformLogsSettings_DISABLED                                                = src.PlatformLogsSettings_DISABLED
	PlatformLogsSettings_ERROR                                                   = src.PlatformLogsSettings_ERROR
	PlatformLogsSettings_INFO                                                    = src.PlatformLogsSettings_INFO
	PlatformLogsSettings_SEVERITY_UNSPECIFIED                                    = src.PlatformLogsSettings_SEVERITY_UNSPECIFIED
	PlatformLogsSettings_WARNING                                                 = src.PlatformLogsSettings_WARNING
	SchemaView_BASIC                                                             = src.SchemaView_BASIC
	SchemaView_FULL                                                              = src.SchemaView_FULL
	SchemaView_SCHEMA_VIEW_UNSPECIFIED                                           = src.SchemaView_SCHEMA_VIEW_UNSPECIFIED
	Schema_AVRO                                                                  = src.Schema_AVRO
	Schema_PROTOCOL_BUFFER                                                       = src.Schema_PROTOCOL_BUFFER
	Schema_TYPE_UNSPECIFIED                                                      = src.Schema_TYPE_UNSPECIFIED
	Subscription_ACTIVE                                                          = src.Subscription_ACTIVE
	Subscription_RESOURCE_ERROR                                                  = src.Subscription_RESOURCE_ERROR
	Subscription_STATE_UNSPECIFIED                                               = src.Subscription_STATE_UNSPECIFIED
	Topic_ACTIVE                                                                 = src.Topic_ACTIVE
	Topic_INGESTION_RESOURCE_ERROR                                               = src.Topic_INGESTION_RESOURCE_ERROR
	Topic_STATE_UNSPECIFIED                                                      = src.Topic_STATE_UNSPECIFIED
)
```

    
  

Deprecated: Please use consts in: cloud.google.com/go/pubsub/v2/apiv1/pubsubpb

  
### Variables ¶

  
    
      View Source
      

```
var (
	BigQueryConfig_State_name                              = src.BigQueryConfig_State_name
	BigQueryConfig_State_value                             = src.BigQueryConfig_State_value
	CloudStorageConfig_State_name                          = src.CloudStorageConfig_State_name
	CloudStorageConfig_State_value                         = src.CloudStorageConfig_State_value
	Encoding_name                                          = src.Encoding_name
	Encoding_value                                         = src.Encoding_value
	File_google_pubsub_v1_pubsub_proto                     = src.File_google_pubsub_v1_pubsub_proto
	File_google_pubsub_v1_schema_proto                     = src.File_google_pubsub_v1_schema_proto
	IngestionDataSourceSettings_AwsKinesis_State_name      = src.IngestionDataSourceSettings_AwsKinesis_State_name
	IngestionDataSourceSettings_AwsKinesis_State_value     = src.IngestionDataSourceSettings_AwsKinesis_State_value
	IngestionDataSourceSettings_AwsMsk_State_name          = src.IngestionDataSourceSettings_AwsMsk_State_name
	IngestionDataSourceSettings_AwsMsk_State_value         = src.IngestionDataSourceSettings_AwsMsk_State_value
	IngestionDataSourceSettings_AzureEventHubs_State_name  = src.IngestionDataSourceSettings_AzureEventHubs_State_name
	IngestionDataSourceSettings_AzureEventHubs_State_value = src.IngestionDataSourceSettings_AzureEventHubs_State_value
	IngestionDataSourceSettings_CloudStorage_State_name    = src.IngestionDataSourceSettings_CloudStorage_State_name
	IngestionDataSourceSettings_CloudStorage_State_value   = src.IngestionDataSourceSettings_CloudStorage_State_value
	IngestionDataSourceSettings_ConfluentCloud_State_name  = src.IngestionDataSourceSettings_ConfluentCloud_State_name
	IngestionDataSourceSettings_ConfluentCloud_State_value = src.IngestionDataSourceSettings_ConfluentCloud_State_value
	PlatformLogsSettings_Severity_name                     = src.PlatformLogsSettings_Severity_name
	PlatformLogsSettings_Severity_value                    = src.PlatformLogsSettings_Severity_value
	SchemaView_name                                        = src.SchemaView_name
	SchemaView_value                                       = src.SchemaView_value
	Schema_Type_name                                       = src.Schema_Type_name
	Schema_Type_value                                      = src.Schema_Type_value
	Subscription_State_name                                = src.Subscription_State_name
	Subscription_State_value                               = src.Subscription_State_value
	Topic_State_name                                       = src.Topic_State_name
	Topic_State_value                                      = src.Topic_State_value
)
```

    
  

Deprecated: Please use vars in: cloud.google.com/go/pubsub/v2/apiv1/pubsubpb

  
### Functions ¶

  
	  
  
  
    
  

        
	  
  
  
    
  

        
	  
  
  
    
  

        

  
### Types ¶

  
      
  
  
    
  

    
      
  
  
    
  

    
      
  
  
    
  

    
      
  
  
    
  

    
      
  
  
    
  

    
      
  
  
    
#### 
      type CloudStorageConfig_AvroConfig_ ¶
  
    
      added in
      v1.31.0
    
  

    
    
      

```
type CloudStorageConfig_AvroConfig_ = src.CloudStorageConfig_AvroConfig_
```