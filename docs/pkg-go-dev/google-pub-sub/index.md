### Overview ¶

  

      
- Publishing
      
- Receiving
      
- Streams Management
      
- Ack Deadlines
      
- Slow Message Processing
      
- Emulator
  

Package pubsub provides an easy way to publish and receive Google Cloud Pub/Sub
messages, hiding the details of the underlying server RPCs.
Pub/Sub is a many-to-many, asynchronous messaging system that decouples senders
and receivers.

More information about Pub/Sub is available at
https://cloud.google.com/pubsub/docs

See https://godoc.org/cloud.google.com/go for authentication, timeouts,
connection pooling and similar aspects of this package.

#### Publishing ¶

Pub/Sub messages are published to topics. A Topic may be created
using Client.CreateTopic like so:

```
topic, err := pubsubClient.CreateTopic(context.Background(), "topic-name")

```

Messages may then be published to a Topic:

```
res := topic.Publish(ctx, &pubsub.Message{Data: []byte("payload")})

```

Topic.Publish queues the message for publishing and returns immediately. When enough
messages have accumulated, or enough time has elapsed, the batch of messages is
sent to the Pub/Sub service.

Topic.Publish returns a PublishResult, which behaves like a future: its Get method
blocks until the message has been sent to the service.

The first time you call Topic.Publish on a Topic, goroutines are started in the
background. To clean up these goroutines, call Topic.Stop:

```
topic.Stop()

```

#### Receiving ¶

To receive messages published to a Topic, clients create a Subscription
for the topic. There may be more than one subscription per topic ; each message
that is published to the topic will be delivered to all associated subscriptions.

A Subscription may be created like so:

```
 sub, err := pubsubClient.CreateSubscription(context.Background(), "sub-name",
	pubsub.SubscriptionConfig{Topic: topic})

```

Messages are then consumed from a Subscription via callback.

```
 err := sub.Receive(context.Background(), func(ctx context.Context, m *Message) {
	log.Printf("Got message: %s", m.Data)
	m.Ack()
 })
 if err != nil && !errors.Is(err, context.Canceled) {
	// Handle error.
 }

```

The callback is invoked concurrently by multiple goroutines, maximizing
throughput. To terminate a call to Subscription.Receive, cancel its context.

Once client code has processed the Message, it must call Message.Ack or
Message.Nack; otherwise the Message will eventually be redelivered. Ack/Nack
MUST be called within the Subscription.Receive handler function, and not from a goroutine.
Otherwise, flow control (e.g. ReceiveSettings.MaxOutstandingMessages) will
not be respected, and messages can get orphaned when cancelling Receive.

If the client cannot or doesn't want to process the message, it can call Message.Nack
to speed redelivery. For more information and configuration options, see
Ack Deadlines below.

Note: It is possible for a Message to be redelivered even if Message.Ack has
been called. Client code must be robust to multiple deliveries of messages.

Note: This uses pubsub's streaming pull feature. This feature has properties that
may be surprising. Please take a look at https://cloud.google.com/pubsub/docs/pull#streamingpull
for more details on how streaming pull behaves compared to the synchronous
pull method.

#### Streams Management ¶

The number of StreamingPull connections can be configured by setting NumGoroutines in ReceiveSettings.
The default value of 10 means the client library will maintain 10 StreamingPull connections.
This is more than sufficient for most use cases, as StreamingPull connections can handle up to
10 MB/s https://cloud.google.com/pubsub/quotas#resource_limits. In some cases, using too many streams
can lead to client library behaving poorly as the application becomes I/O bound.

By default, the number of connections in the gRPC conn pool is min(4,GOMAXPROCS). Each connection supports
up to 100 streams. Thus, if you have 4 or more CPU cores, the default setting allows a maximum of 400 streams
which is already excessive for most use cases.
If you want to change the limits on the number of streams, you can change the number of connections
in the gRPC connection pool as shown below:

```
 opts := []option.ClientOption{
	option.WithGRPCConnectionPool(2),
 }
 client, err := pubsub.NewClient(ctx, projID, opts...)

```

#### Ack Deadlines ¶

The default pubsub deadlines are suitable for most use cases, but may be
overridden. This section describes the tradeoffs that should be considered
when overriding the defaults.

Behind the scenes, each message returned by the Pub/Sub server has an
associated lease, known as an "ack deadline". Unless a message is
acknowledged within the ack deadline, or the client requests that
the ack deadline be extended, the message will become eligible for redelivery.

As a convenience, the pubsub client will automatically extend deadlines until
either:

  
- Message.Ack or Message.Nack is called, or
  
- The "MaxExtension" duration elapses from the time the message is fetched from
the server. This defaults to 60m.

Ack deadlines are extended periodically by the client. The period between extensions,
as well as the length of the extension, automatically adjusts based on the time it takes the
subscriber application to ack messages (based on the 99th percentile of ack latency).
By default, this extension period is capped at 10m, but this limit can be configured
by the "MaxExtensionPeriod" setting. This has the effect that subscribers that process
messages quickly have their message ack deadlines extended for a short amount, whereas
subscribers that process message slowly have their message ack deadlines extended
for a large amount. The net effect is fewer RPCs sent from the client library.

For example, consider a subscriber that takes 3 minutes to process each message.
Since the library has already recorded several 3-minute "ack latencies"s in a
percentile distribution, future message extensions are sent with a value of 3
minutes, every 3 minutes. Suppose the application crashes 5 seconds after the
library sends such an extension: the Pub/Sub server would wait the remaining
2m55s before re-sending the messages out to other subscribers.

Please note that by default, the client library does not use the subscription's
AckDeadline for the MaxExtension value.

#### Slow Message Processing ¶

For use cases where message processing exceeds 30 minutes, we recommend using
the base client in a pull model, since long-lived streams are periodically killed
by firewalls. See the example at https://godoc.org/cloud.google.com/go/pubsub/apiv1#example-SubscriberClient-Pull-LengthyClientProcessing

#### Emulator ¶

To use an emulator with this library, you can set the PUBSUB_EMULATOR_HOST
environment variable to the address at which your emulator is running. This will
send requests to that address instead of to Pub/Sub. You can then create
and use a client as usual:

```
// Set PUBSUB_EMULATOR_HOST environment variable.
err := os.Setenv("PUBSUB_EMULATOR_HOST", "localhost:9000")
if err != nil {
	// TODO: Handle error.
}
// Create client as usual.
client, err := pubsub.NewClient(ctx, "my-project-id")
if err != nil {
	// TODO: Handle error.
}
defer client.Close()

```

Deprecated: Please use cloud.google.com/go/pubsub/v2.

    
### Index ¶

- Constants

- Variables

- 
        func NewMessageCarrierFromPB(msg *pb.PubsubMessage) propagation.TextMapCarrier

- 
          type AWSKinesisState

- 
          type AckResult

- 
          type AcknowledgeStatus

- 
          type AmazonMSKState

- 
          type AuthenticationMethod

- 
          type BigQueryConfig

- 
          type BigQueryConfigState

- 
          type Client

- 

  - 
            func NewClient(ctx context.Context, projectID string, opts ...option.ClientOption) (c *Client, err error)

  - 
            func NewClientWithConfig(ctx context.Context, projectID string, config *ClientConfig, ...) (*Client, error)

- 

  - 
            func (c *Client) Close() error

  - 
            func (c *Client) CreateSubscription(ctx context.Context, id string, cfg SubscriptionConfig) (*Subscription, error)

  - 
            func (c *Client) CreateTopic(ctx context.Context, topicID string) (*Topic, error)

  - 
            func (c *Client) CreateTopicWithConfig(ctx context.Context, topicID string, tc *TopicConfig) (*Topic, error)

  - 
            func (c *Client) DetachSubscription(ctx context.Context, sub string) (*DetachSubscriptionResult, error)

  - 
            func (c *Client) Project() string

  - 
            func (c *Client) Snapshot(id string) *Snapshot

  - 
            func (c *Client) Snapshots(ctx context.Context) *SnapshotConfigIterator

  - 
            func (c *Client) Subscription(id string) *Subscription

  - 
            func (c *Client) SubscriptionInProject(id, projectID string) *Subscription

  - 
            func (c *Client) Subscriptions(ctx context.Context) *SubscriptionIterator

  - 
            func (c *Client) Topic(id string) *Topic

  - 
            func (c *Client) TopicInProject(id, projectID string) *Topic

  - 
            func (c *Client) Topics(ctx context.Context) *TopicIterator

- 
          type ClientConfig

- 
          type CloudStorageConfig

- 
          type CloudStorageConfigState

- 
          type CloudStorageIngestionState

- 
          type CloudStorageOutputFormatAvroConfig

- 
          type CloudStorageOutputFormatTextConfig

- 
          type ConfluentCloudState

- 
          type DeadLetterPolicy

- 
          type DetachSubscriptionResult

- 
          type ErrPublishingPaused

- 

  - 
            func (e ErrPublishingPaused) Error() string

- 
          type EventHubsState

- 
          type FlowControlSettings

- 
          type IngestionDataSource

- 
          type IngestionDataSourceAWSKinesis

- 
          type IngestionDataSourceAmazonMSK

- 
          type IngestionDataSourceAzureEventHubs

- 
          type IngestionDataSourceCloudStorage

- 
          type IngestionDataSourceCloudStorageAvroFormat

- 
          type IngestionDataSourceCloudStoragePubSubAvroFormat

- 
          type IngestionDataSourceCloudStorageTextFormat

- 
          type IngestionDataSourceConfluentCloud

- 
          type IngestionDataSourceSettings

- 
          type JavaScriptUDF

- 
          type LimitExceededBehavior

- 
          type Message

- 
          type MessageStoragePolicy

- 
          type MessageTransform

- 
          type NoWrapper

- 
          type OIDCToken

- 
          type PlatformLogsSettings

- 
          type PlatformLogsSeverity

- 
          type PublishResult

- 
          type PublishSettings

- 
          type PubsubWrapper

- 
          type PushConfig

- 
          type ReceiveSettings

- 
          type RetryPolicy

- 
          type SchemaClient

- 

  - 
            func NewSchemaClient(ctx context.Context, projectID string, opts ...option.ClientOption) (*SchemaClient, error)

- 

  - 
            func (s *SchemaClient) Close() error

  - 
            func (c *SchemaClient) CommitSchema(ctx context.Context, schemaID string, s SchemaConfig) (*SchemaConfig, error)

  - 
            func (c *SchemaClient) CreateSchema(ctx context.Context, schemaID string, s SchemaConfig) (*SchemaConfig, error)

  - 
            func (c *SchemaClient) DeleteSchema(ctx context.Context, schemaID string) error

  - 
            func (c *SchemaClient) DeleteSchemaRevision(ctx context.Context, schemaID, revisionID string) (*SchemaConfig, error)

  - 
            func (c *SchemaClient) ListSchemaRevisions(ctx context.Context, schemaID string, view SchemaView) *SchemaIterator

  - 
            func (c *SchemaClient) RollbackSchema(ctx context.Context, schemaID, revisionID string) (*SchemaConfig, error)

  - 
            func (c *SchemaClient) Schema(ctx context.Context, schemaID string, view SchemaView) (*SchemaConfig, error)

  - 
            func (c *SchemaClient) Schemas(ctx context.Context, view SchemaView) *SchemaIterator

  - 
            func (c *SchemaClient) ValidateMessageWithConfig(ctx context.Context, msg []byte, encoding SchemaEncoding, config SchemaConfig) (*ValidateMessageResult, error)

  - 
            func (c *SchemaClient) ValidateMessageWithID(ctx context.Context, msg []byte, encoding SchemaEncoding, schemaID string) (*ValidateMessageResult, error)

  - 
            func (c *SchemaClient) ValidateSchema(ctx context.Context, schema SchemaConfig) (*ValidateSchemaResult, error)

- 
          type SchemaConfig

- 
          type SchemaEncoding

- 
          type SchemaIterator

- 

  - 
            func (s *SchemaIterator) Next() (*SchemaConfig, error)

- 
          type SchemaSettings

- 
          type SchemaType

- 
          type SchemaView

- 
          type Snapshot

- 

  - 
            func (s *Snapshot) Delete(ctx context.Context) error

  - 
            func (s *Snapshot) ID() string

  - 
            func (s *Snapshot) SetLabels(ctx context.Context, label map[string]string) (*SnapshotConfig, error)

- 
          type SnapshotConfig

- 
          type SnapshotConfigIterator

- 

  - 
            func (snaps *SnapshotConfigIterator) Next() (*SnapshotConfig, error)

- 
          type Subscription

- 

  - 
            func (s *Subscription) Config(ctx context.Context) (SubscriptionConfig, error)

  - 
            func (s *Subscription) CreateSnapshot(ctx context.Context, name string) (*SnapshotConfig, error)

  - 
            func (s *Subscription) Delete(ctx context.Context) error

  - 
            func (s *Subscription) Exists(ctx context.Context) (bool, error)

  - 
            func (s *Subscription) IAM() *iam.Handle

  - 
            func (s *Subscription) ID() string

  - 
            func (s *Subscription) Receive(ctx context.Context, f func(context.Context, *Message)) error

  - 
            func (s *Subscription) SeekToSnapshot(ctx context.Context, snap *Snapshot) error

  - 
            func (s *Subscription) SeekToTime(ctx context.Context, t time.Time) error

  - 
            func (s *Subscription) String() string

  - 
            func (s *Subscription) Update(ctx context.Context, cfg SubscriptionConfigToUpdate) (SubscriptionConfig, error)

- 
          type SubscriptionConfig

- 

  - 
            func (s *SubscriptionConfig) ID() string

  - 
            func (s *SubscriptionConfig) String() string

- 
          type SubscriptionConfigToUpdate

- 
          type SubscriptionIterator

- 

  - 
            func (subs *SubscriptionIterator) Next() (*Subscription, error)

  - 
            func (subs *SubscriptionIterator) NextConfig() (*SubscriptionConfig, error)

- 
          type SubscriptionState

- 
          type Topic

- 

  - 
            func (t *Topic) Config(ctx context.Context) (TopicConfig, error)

  - 
            func (t *Topic) Delete(ctx context.Context) error

  - 
            func (t *Topic) Exists(ctx context.Context) (bool, error)

  - 
            func (t *Topic) Flush()

  - 
            func (t *Topic) IAM() *iam.Handle

  - 
            func (t *Topic) ID() string

  - 
            func (t *Topic) Publish(ctx context.Context, msg *Message) *PublishResult

  - 
            func (t *Topic) ResumePublish(orderingKey string)

  - 
            func (t *Topic) Stop()

  - 
            func (t *Topic) String() string

  - 
            func (t *Topic) Subscriptions(ctx context.Context) *SubscriptionIterator

  - 
            func (t *Topic) Update(ctx context.Context, cfg TopicConfigToUpdate) (TopicConfig, error)

- 
          type TopicConfig

- 

  - 
            func (t *TopicConfig) ID() string

  - 
            func (t *TopicConfig) String() string

- 
          type TopicConfigToUpdate

- 
          type TopicIterator

- 

  - 
            func (tps *TopicIterator) Next() (*Topic, error)

  - 
            func (t *TopicIterator) NextConfig() (*TopicConfig, error)

- 
          type TopicState

- 
          type Transform

- 
          type ValidateMessageResult

- 
          type ValidateSchemaResult

- 
          type Wrapper

    
### Examples ¶

- Client.CreateSubscription

- Client.CreateSubscription (NeverExpire)

- Client.CreateTopic

- Client.CreateTopicWithConfig

- Client.Snapshots

- Client.Subscriptions

- Client.TopicInProject

- Client.Topics

- NewClient

- Snapshot.Delete

- SnapshotConfigIterator.Next

- Subscription.Config

- Subscription.CreateSnapshot

- Subscription.Delete

- Subscription.Exists

- Subscription.Receive

- Subscription.Receive (MaxExtension)

- Subscription.Receive (MaxOutstanding)

- Subscription.SeekToSnapshot

- Subscription.SeekToTime

- Subscription.Update

- Subscription.Update (PushConfigAuthenticationMethod)

- SubscriptionIterator.Next

- Topic.Delete

- Topic.Exists

- Topic.Publish

- Topic.Subscriptions

- Topic.Update

- Topic.Update (ResetMessageStoragePolicy)

- TopicIterator.Next

### Constants ¶

  
    
      View Source
      

```
const (
	// ScopePubSub grants permissions to view and manage Pub/Sub
	// topics and subscriptions.
	ScopePubSub = "https://www.googleapis.com/auth/pubsub"

	// ScopeCloudPlatform grants permissions to view and manage your data
	// across Google Cloud Platform services.
	ScopeCloudPlatform = "https://www.googleapis.com/auth/cloud-platform"
)
```

    
  

    
      View Source
      

```
const (
	// BigQueryConfigStateUnspecified is the default value. This value is unused.
	BigQueryConfigStateUnspecified = iota

	// BigQueryConfigActive means the subscription can actively send messages to BigQuery.
	BigQueryConfigActive

	// BigQueryConfigPermissionDenied means the subscription cannot write to the BigQuery table because of permission denied errors.
	BigQueryConfigPermissionDenied

	// BigQueryConfigNotFound means the subscription cannot write to the BigQuery table because it does not exist.
	BigQueryConfigNotFound

	// BigQueryConfigSchemaMismatch means the subscription cannot write to the BigQuery table due to a schema mismatch.
	BigQueryConfigSchemaMismatch
)
```

    
  

    
      View Source
      

```
const (
	// CloudStorageConfigStateUnspecified is the default value. This value is unused.
	CloudStorageConfigStateUnspecified = iota

	// CloudStorageConfigActive means the subscription can actively send messages to Cloud Storage.
	CloudStorageConfigActive

	// CloudStorageConfigPermissionDenied means the subscription cannot write to the Cloud storage bucket because of permission denied errors.
	CloudStorageConfigPermissionDenied

	// CloudStorageConfigNotFound means the subscription cannot write to the Cloud Storage bucket because it does not exist.
	CloudStorageConfigNotFound
)
```

    
  

    
      View Source
      

```
const (
	// SubscriptionStateUnspecified is the default value. This value is unused.
	SubscriptionStateUnspecified = iota

	// SubscriptionStateActive means the subscription can actively send messages to BigQuery.
	SubscriptionStateActive

	// SubscriptionStateResourceError means the subscription receive messages because of an
	// error with the resource to which it pushes messages.
	// See the more detailed error state in the corresponding configuration.
	SubscriptionStateResourceError
)
```

    
  

    
      View Source
      

```
const (
	// MaxPublishRequestCount is the maximum number of messages that can be in
	// a single publish request, as defined by the PubSub service.
	MaxPublishRequestCount = 1000

	// MaxPublishRequestBytes is the maximum size of a single publish request
	// in bytes, as defined by the PubSub service.
	MaxPublishRequestBytes = 1e7
)
```

    
  

    
      View Source
      

```
const (
	// TopicStateUnspecified is the default value. This value is unused.
	TopicStateUnspecified = iota

	// TopicStateActive means the topic does not have any persistent errors.
	TopicStateActive

	// TopicStateIngestionResourceError means ingestion from the data source
	// has encountered a permanent error.
	// See the more detailed error state in the corresponding ingestion
	// source configuration.
	TopicStateIngestionResourceError
)
```

    
  

    
      View Source
      

```
const (
	// AWSKinesisStateUnspecified is the default value. This value is unused.
	AWSKinesisStateUnspecified = iota

	// AWSKinesisStateActive means ingestion is active.
	AWSKinesisStateActive

	// AWSKinesisStatePermissionDenied means encountering an error while consumign data from Kinesis.
	// This can happen if:
	//   - The provided `aws_role_arn` does not exist or does not have the
	//     appropriate permissions attached.
	//   - The provided `aws_role_arn` is not set up properly for Identity
	//     Federation using `gcp_service_account`.
	//   - The Pub/Sub SA is not granted the
	//     `iam.serviceAccounts.getOpenIdToken` permission on
	//     `gcp_service_account`.
	AWSKinesisStatePermissionDenied

	// AWSKinesisStatePublishPermissionDenied means permission denied encountered while publishing to the topic.
	// This can happen due to Pub/Sub SA has not been granted the appropriate publish
	// permissions https://cloud.google.com/pubsub/docs/access-control#pubsub.publisher
	AWSKinesisStatePublishPermissionDenied

	// AWSKinesisStateStreamNotFound means the Kinesis stream does not exist.
	AWSKinesisStateStreamNotFound

	// AWSKinesisStateConsumerNotFound means the Kinesis consumer does not exist.
	AWSKinesisStateConsumerNotFound
)
```

    
  

    
      View Source
      

```
const (
	// CloudStorageIngestionStateUnspecified is the default value. This value is unused.
	CloudStorageIngestionStateUnspecified = iota

	// CloudStorageIngestionStateActive means ingestion is active.
	CloudStorageIngestionStateActive

	// CloudStorageIngestionPermissionDenied means encountering an error while calling the Cloud Storage API.
	// This can happen if the Pub/Sub SA has not been granted the
	// [appropriate permissions](https://cloud.google.com/storage/docs/access-control/iam-permissions):
	// - storage.objects.list: to list the objects in a bucket.
	// - storage.objects.get: to read the objects in a bucket.
	// - storage.buckets.get: to verify the bucket exists.
	CloudStorageIngestionPermissionDenied

	// CloudStorageIngestionPublishPermissionDenied means encountering an error when publishing to the topic.
	// This can happen if the Pub/Sub SA has not been granted the [appropriate publish
	// permissions](https://cloud.google.com/pubsub/docs/access-control#pubsub.publisher)
	CloudStorageIngestionPublishPermissionDenied

	// CloudStorageIngestionBucketNotFound means the provided bucket doesn't exist.
	CloudStorageIngestionBucketNotFound

	// CloudStorageIngestionTooManyObjects means the bucket has too many objects, ingestion will be paused.
	CloudStorageIngestionTooManyObjects
)
```

    
  

    
      View Source
      

```
const (
	// EventHubsStateUnspecified is the default value. This value is unused.
	EventHubsStateUnspecified = iota

	// EventHubsStateActive means the state is active.
	EventHubsStateActive

	// EventHubsStatePermissionDenied indicates encountered permission denied error
	// while consuming data from Event Hubs.
	// This can happen when `client_id`, or `tenant_id` are invalid. Or the
	// right permissions haven't been granted.
	EventHubsStatePermissionDenied

	// EventHubsStatePublishPermissionDenied indicates permission denied encountered
	// while publishing to the topic.
	EventHubsStatePublishPermissionDenied

	// EventHubsStateNamespaceNotFound indicates the provided Event Hubs namespace couldn't be found.
	EventHubsStateNamespaceNotFound

	// EventHubsStateNotFound indicates the provided Event Hub couldn't be found.
	EventHubsStateNotFound

	// EventHubsStateSubscriptionNotFound indicates the provided Event Hubs subscription couldn't be found.
	EventHubsStateSubscriptionNotFound

	// EventHubsStateResourceGroupNotFound indicates the provided Event Hubs resource group couldn't be found.
	EventHubsStateResourceGroupNotFound
)
```

    
  

    
      View Source
      

```
const (
	// AmazonMSKStateUnspecified is the default value. This value is unused.
	AmazonMSKStateUnspecified = iota

	// AmazonMSKActive indicates MSK topic is active.
	AmazonMSKActive

	// AmazonMSKPermissionDenied indicates permission denied encountered while consuming data from Amazon MSK.
	AmazonMSKPermissionDenied

	// AmazonMSKPublishPermissionDenied indicates permission denied encountered while publishing to the topic.
	AmazonMSKPublishPermissionDenied

	// AmazonMSKClusterNotFound indicates the provided Msk cluster wasn't found.
	AmazonMSKClusterNotFound

	// AmazonMSKTopicNotFound indicates the provided topic wasn't found.
	AmazonMSKTopicNotFound
)
```

    
  

    
      View Source
      

```
const (
	// ConfluentCloudStateUnspecified is the default value. This value is unused.
	ConfluentCloudStateUnspecified = iota

	// ConfluentCloudActive indicates the state is active.
	ConfluentCloudActive = 1

	// ConfluentCloudPermissionDenied indicates permission denied encountered
	// while consuming data from Confluent Cloud.
	ConfluentCloudPermissionDenied = 2

	// ConfluentCloudPublishPermissionDenied indicates permission denied encountered
	// while publishing to the topic.
	ConfluentCloudPublishPermissionDenied = 3

	// ConfluentCloudUnreachableBootstrapServer indicates the provided bootstrap
	// server address is unreachable.
	ConfluentCloudUnreachableBootstrapServer = 4

	// ConfluentCloudClusterNotFound indicates the provided cluster wasn't found.
	ConfluentCloudClusterNotFound = 5

	// ConfluentCloudTopicNotFound indicates the provided topic wasn't found.
	ConfluentCloudTopicNotFound = 6
)
```

    
  

    
      View Source
      

```
const DetectProjectID = "*detect-project-id*"
```

    
  

DetectProjectID is a sentinel value that instructs NewClient to detect the
project ID. It is given in place of the projectID argument. NewClient will
use the project ID from the given credentials or the default credentials
(https://developers.google.com/accounts/docs/application-default-credentials)
if no credentials were provided. When providing credentials, not all
options will allow NewClient to extract the project ID. Specifically a JWT
does not have the project ID encoded.

  
### Variables ¶

  
    
      View Source
      

```
var (
	// ErrFlowControllerMaxOutstandingMessages indicates that outstanding messages exceeds MaxOutstandingMessages.
	ErrFlowControllerMaxOutstandingMessages = errors.New("pubsub: MaxOutstandingMessages flow controller limit exceeded")

	// ErrFlowControllerMaxOutstandingBytes indicates that outstanding bytes of messages exceeds MaxOutstandingBytes.
	ErrFlowControllerMaxOutstandingBytes = errors.New("pubsub: MaxOutstandingBytes flow control limit exceeded")
)
```

    
  

    
      View Source
      

```
var (
	// PublishedMessages is a measure of the number of messages published, which may include errors.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublishedMessages = stats.Int64(statsPrefix+"published_messages", "Number of PubSub message published", stats.UnitDimensionless)

	// PublishLatency is a measure of the number of milliseconds it took to publish a bundle,
	// which may consist of one or more messages.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublishLatency = stats.Float64(statsPrefix+"publish_roundtrip_latency", "The latency in milliseconds per publish batch", stats.UnitMilliseconds)

	// PullCount is a measure of the number of messages pulled.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PullCount = stats.Int64(statsPrefix+"pull_count", "Number of PubSub messages pulled", stats.UnitDimensionless)

	// AckCount is a measure of the number of messages acked.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	AckCount = stats.Int64(statsPrefix+"ack_count", "Number of PubSub messages acked", stats.UnitDimensionless)

	// NackCount is a measure of the number of messages nacked.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	NackCount = stats.Int64(statsPrefix+"nack_count", "Number of PubSub messages nacked", stats.UnitDimensionless)

	// ModAckCount is a measure of the number of messages whose ack-deadline was modified.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	ModAckCount = stats.Int64(statsPrefix+"mod_ack_count", "Number of ack-deadlines modified", stats.UnitDimensionless)

	// ModAckTimeoutCount is a measure of the number ModifyAckDeadline RPCs that timed out.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	ModAckTimeoutCount = stats.Int64(statsPrefix+"mod_ack_timeout_count", "Number of ModifyAckDeadline RPCs that timed out", stats.UnitDimensionless)

	// StreamOpenCount is a measure of the number of times a streaming-pull stream was opened.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamOpenCount = stats.Int64(statsPrefix+"stream_open_count", "Number of calls opening a new streaming pull", stats.UnitDimensionless)

	// StreamRetryCount is a measure of the number of times a streaming-pull operation was retried.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamRetryCount = stats.Int64(statsPrefix+"stream_retry_count", "Number of retries of a stream send or receive", stats.UnitDimensionless)

	// StreamRequestCount is a measure of the number of requests sent on a streaming-pull stream.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamRequestCount = stats.Int64(statsPrefix+"stream_request_count", "Number gRPC StreamingPull request messages sent", stats.UnitDimensionless)

	// StreamResponseCount is a measure of the number of responses received on a streaming-pull stream.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamResponseCount = stats.Int64(statsPrefix+"stream_response_count", "Number of gRPC StreamingPull response messages received", stats.UnitDimensionless)

	// OutstandingMessages is a measure of the number of outstanding messages held by the client before they are processed.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	OutstandingMessages = stats.Int64(statsPrefix+"outstanding_messages", "Number of outstanding Pub/Sub messages", stats.UnitDimensionless)

	// OutstandingBytes is a measure of the number of bytes all outstanding messages held by the client take up.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	OutstandingBytes = stats.Int64(statsPrefix+"outstanding_bytes", "Number of outstanding bytes", stats.UnitDimensionless)

	// PublisherOutstandingMessages is a measure of the number of published outstanding messages held by the client before they are processed.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublisherOutstandingMessages = stats.Int64(statsPrefix+"publisher_outstanding_messages", "Number of outstanding publish messages", stats.UnitDimensionless)

	// PublisherOutstandingBytes is a measure of the number of bytes all outstanding publish messages held by the client take up.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublisherOutstandingBytes = stats.Int64(statsPrefix+"publisher_outstanding_bytes", "Number of outstanding publish bytes", stats.UnitDimensionless)
)
```

    
  

The following are measures recorded in publish/subscribe flows.

    
      View Source
      

```
var (
	// PublishedMessagesView is a cumulative sum of PublishedMessages.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublishedMessagesView *view.View

	// PublishLatencyView is a distribution of PublishLatency.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublishLatencyView *view.View

	// PullCountView is a cumulative sum of PullCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PullCountView *view.View

	// AckCountView is a cumulative sum of AckCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	AckCountView *view.View

	// NackCountView is a cumulative sum of NackCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	NackCountView *view.View

	// ModAckCountView is a cumulative sum of ModAckCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	ModAckCountView *view.View

	// ModAckTimeoutCountView is a cumulative sum of ModAckTimeoutCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	ModAckTimeoutCountView *view.View

	// StreamOpenCountView is a cumulative sum of StreamOpenCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamOpenCountView *view.View

	// StreamRetryCountView is a cumulative sum of StreamRetryCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamRetryCountView *view.View

	// StreamRequestCountView is a cumulative sum of StreamRequestCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamRequestCountView *view.View

	// StreamResponseCountView is a cumulative sum of StreamResponseCount.
	// It is EXPERIMENTAL and subject to change or removal without notice.
	StreamResponseCountView *view.View

	// OutstandingMessagesView is the last value of OutstandingMessages
	// It is EXPERIMENTAL and subject to change or removal without notice.
	OutstandingMessagesView *view.View

	// OutstandingBytesView is the last value of OutstandingBytes
	// It is EXPERIMENTAL and subject to change or removal without notice.
	OutstandingBytesView *view.View

	// PublisherOutstandingMessagesView is the last value of OutstandingMessages
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublisherOutstandingMessagesView *view.View

	// PublisherOutstandingBytesView is the last value of OutstandingBytes
	// It is EXPERIMENTAL and subject to change or removal without notice.
	PublisherOutstandingBytesView *view.View
)
```

    
  

    
      View Source
      

```
var (
	DefaultPublishViews   []*view.View
	DefaultSubscribeViews []*view.View
)
```

    
  

These arrays hold the default OpenCensus views that keep track of publish/subscribe operations.
It is EXPERIMENTAL and subject to change or removal without notice.

    
      View Source
      

```
var DefaultPublishSettings = PublishSettings{
	DelayThreshold: 10 * time.Millisecond,
	CountThreshold: 100,
	ByteThreshold:  1e6,
	Timeout:        60 * time.Second,

	BufferedByteLimit: 10 * MaxPublishRequestBytes,
	FlowControlSettings: FlowControlSettings{
		MaxOutstandingMessages: 1000,
		MaxOutstandingBytes:    -1,
		LimitExceededBehavior:  FlowControlIgnore,
	},

	EnableCompression:         false,
	CompressionBytesThreshold: 240,
}
```

    
  

DefaultPublishSettings holds the default values for topics' PublishSettings.

    
      View Source
      

```
var DefaultReceiveSettings = ReceiveSettings{
	MaxExtension:           60 * time.Minute,
	MaxExtensionPeriod:     0,
	MinExtensionPeriod:     0,
	MaxOutstandingMessages: 1000,
	MaxOutstandingBytes:    1e9,
	NumGoroutines:          10,
}
```

    
  

DefaultReceiveSettings holds the default values for ReceiveSettings.

    
      View Source
      

```
var ErrEmptyProjectID = errors.New("pubsub: projectID string is empty")
```

    
  

ErrEmptyProjectID denotes that the project string passed into NewClient was empty.
Please provide a valid project ID or use the DetectProjectID sentinel value to detect
project ID from well defined sources.

    
      View Source
      

```
var ErrOversizedMessage = bundler.ErrOversizedItem
```

    
  

ErrOversizedMessage indicates that a message's size exceeds MaxPublishRequestBytes.

    
      View Source
      

```
var ErrTopicStopped = errors.New("pubsub: Stop has been called for this topic")
```

    
  

ErrTopicStopped indicates that topic has been stopped and further publishing will fail.

  
### Functions ¶

  
	  
  
  
    
#### 
      func NewMessageCarrierFromPB ¶
  
    
      added in
      v1.43.0
    
  

    
    
      

```
func NewMessageCarrierFromPB(msg *pb.PubsubMessage) propagation.TextMapCarrier
```

    
  

NewMessageCarrierFromPB creates a propagation.TextMapCarrier that can be used to extract the trace
context from a protobuf PubsubMessage.

Example:
ctx = propagation.TraceContext{}.Extract(ctx, pubsub.NewMessageCarrierFromPB(msg))

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type AWSKinesisState ¶
  
    
      added in
      v1.37.0
    
  

    
    
      

```
type AWSKinesisState int
```

    
  

AWSKinesisState denotes the possible states for ingestion from Amazon Kinesis Data Streams.

  

    
      
  
  
    
#### 
      type AckResult ¶
  
    
      added in
      v1.25.0
    
  

    
    
      

```
type AckResult = ipubsub.AckResult
```

    
  

AckResult holds the result from a call to Ack or Nack.

Call Get to obtain the result of the Ack/NackWithResult call. Example:

```
// Get blocks until Ack/NackWithResult completes or ctx is done.
ackStatus, err := r.Get(ctx)
if err != nil {
    // TODO: Handle error.
}

```

  

    
      
  
  
    
#### 
      type AcknowledgeStatus ¶
  
    
      added in
      v1.25.0
    
  

    
    
      

```
type AcknowledgeStatus = ipubsub.AcknowledgeStatus
```

    
  

AcknowledgeStatus represents the status of an Ack or Nack request.

    
      

```
const (
	// AcknowledgeStatusSuccess indicates the request was a success.
	AcknowledgeStatusSuccess AcknowledgeStatus = iota
	// AcknowledgeStatusPermissionDenied indicates the caller does not have sufficient permissions.
	AcknowledgeStatusPermissionDenied
	// AcknowledgeStatusFailedPrecondition indicates the request encountered a FailedPrecondition error.
	AcknowledgeStatusFailedPrecondition
	// AcknowledgeStatusInvalidAckID indicates one or more of the ack IDs sent were invalid.
	AcknowledgeStatusInvalidAckID
	// AcknowledgeStatusOther indicates another unknown error was returned.
	AcknowledgeStatusOther
)
```