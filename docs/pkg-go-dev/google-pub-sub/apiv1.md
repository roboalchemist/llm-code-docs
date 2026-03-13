### Overview ¶

  

      
- General documentation
      
- Example usage
      
- Using the Client
      
- Use of Context
  

Package pubsub is an auto-generated package for the
Cloud Pub/Sub API.

Provides reliable, many-to-many, asynchronous messaging between
applications.

#### General documentation ¶

For information that is relevant for all client libraries please reference
https://pkg.go.dev/cloud.google.com/go#pkg-overview. Some information on this
page includes:

  
- Authentication and Authorization
  
- Timeouts and Cancellation
  
- Testing against Client Libraries
  
- Debugging Client Libraries
  
- Inspecting errors

#### Example usage ¶

To get started with this package, create a client.

```
// go get cloud.google.com/go/pubsub/apiv1@latest
ctx := context.Background()
// This snippet has been automatically generated and should be regarded as a code template only.
// It will require modifications to work:
// - It may require correct/in-range values for request initialization.
// - It may require specifying regional endpoints when creating the service client as shown in:
//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
c, err := pubsub.NewSchemaClient(ctx)
if err != nil {
	// TODO: Handle error.
}
defer c.Close()

```

The client will use your default application credentials. Clients should be reused instead of created as needed.
The methods of Client are safe for concurrent use by multiple goroutines.
The returned client must be Closed when it is done being used.

#### Using the Client ¶

The following is an example of making an API call with the newly created client, mentioned above.

```
req := &pubsubpb.CommitSchemaRequest{
	// TODO: Fill request struct fields.
	// See https://pkg.go.dev/cloud.google.com/go/pubsub/apiv1/pubsubpb#CommitSchemaRequest.
}
resp, err := c.CommitSchema(ctx, req)
if err != nil {
	// TODO: Handle error.
}
// TODO: Use resp.
_ = resp

```

#### Use of Context ¶

The ctx passed to NewSchemaClient is used for authentication requests and
for creating the underlying connection, but is not used for subsequent calls.
Individual methods on the client use the ctx given to them.

To close the open connection, use the Close() method.

    
### Index ¶

- 
        func DefaultAuthScopes() []string

- 
        func PublisherProjectPath(project string) stringdeprecated

- 
        func PublisherTopicPath(project, topic string) stringdeprecated

- 
        func SubscriberProjectPath(project string) stringdeprecated

- 
        func SubscriberSnapshotPath(project, snapshot string) stringdeprecated

- 
        func SubscriberSubscriptionPath(project, subscription string) stringdeprecated

- 
        func SubscriberTopicPath(project, topic string) stringdeprecated

- 
          type PublisherCallOptions

- 
          type PublisherClient

- 

  - 
            func NewPublisherClient(ctx context.Context, opts ...option.ClientOption) (*PublisherClient, error)

  - 
            func NewPublisherRESTClient(ctx context.Context, opts ...option.ClientOption) (*PublisherClient, error)

- 

  - 
            func (c *PublisherClient) Close() error

  - 
            func (c *PublisherClient) Connection() *grpc.ClientConndeprecated

  - 
            func (c *PublisherClient) CreateTopic(ctx context.Context, req *pubsubpb.Topic, opts ...gax.CallOption) (*pubsubpb.Topic, error)

  - 
            func (c *PublisherClient) DeleteTopic(ctx context.Context, req *pubsubpb.DeleteTopicRequest, opts ...gax.CallOption) error

  - 
            func (c *PublisherClient) DetachSubscription(ctx context.Context, req *pubsubpb.DetachSubscriptionRequest, ...) (*pubsubpb.DetachSubscriptionResponse, error)

  - 
            func (c *PublisherClient) GetIamPolicy(ctx context.Context, req *iampb.GetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *PublisherClient) GetTopic(ctx context.Context, req *pubsubpb.GetTopicRequest, opts ...gax.CallOption) (*pubsubpb.Topic, error)

  - 
            func (c *PublisherClient) ListTopicSnapshots(ctx context.Context, req *pubsubpb.ListTopicSnapshotsRequest, ...) *StringIterator

  - 
            func (c *PublisherClient) ListTopicSubscriptions(ctx context.Context, req *pubsubpb.ListTopicSubscriptionsRequest, ...) *StringIterator

  - 
            func (c *PublisherClient) ListTopics(ctx context.Context, req *pubsubpb.ListTopicsRequest, opts ...gax.CallOption) *TopicIterator

  - 
            func (c *PublisherClient) Publish(ctx context.Context, req *pubsubpb.PublishRequest, opts ...gax.CallOption) (*pubsubpb.PublishResponse, error)

  - 
            func (pc *PublisherClient) SetGoogleClientInfo(keyval ...string)

  - 
            func (c *PublisherClient) SetIamPolicy(ctx context.Context, req *iampb.SetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *PublisherClient) SubscriptionIAM(subscription *pubsubpb.Subscription) *iam.Handle

  - 
            func (c *PublisherClient) TestIamPermissions(ctx context.Context, req *iampb.TestIamPermissionsRequest, ...) (*iampb.TestIamPermissionsResponse, error)

  - 
            func (c *PublisherClient) TopicIAM(topic *pubsubpb.Topic) *iam.Handle

  - 
            func (c *PublisherClient) UpdateTopic(ctx context.Context, req *pubsubpb.UpdateTopicRequest, opts ...gax.CallOption) (*pubsubpb.Topic, error)

- 
          type SchemaCallOptions

- 
          type SchemaClient

- 

  - 
            func NewSchemaClient(ctx context.Context, opts ...option.ClientOption) (*SchemaClient, error)

  - 
            func NewSchemaRESTClient(ctx context.Context, opts ...option.ClientOption) (*SchemaClient, error)

- 

  - 
            func (c *SchemaClient) Close() error

  - 
            func (c *SchemaClient) CommitSchema(ctx context.Context, req *pubsubpb.CommitSchemaRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)

  - 
            func (c *SchemaClient) Connection() *grpc.ClientConndeprecated

  - 
            func (c *SchemaClient) CreateSchema(ctx context.Context, req *pubsubpb.CreateSchemaRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)

  - 
            func (c *SchemaClient) DeleteSchema(ctx context.Context, req *pubsubpb.DeleteSchemaRequest, opts ...gax.CallOption) error

  - 
            func (c *SchemaClient) DeleteSchemaRevision(ctx context.Context, req *pubsubpb.DeleteSchemaRevisionRequest, ...) (*pubsubpb.Schema, error)

  - 
            func (c *SchemaClient) GetIamPolicy(ctx context.Context, req *iampb.GetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *SchemaClient) GetSchema(ctx context.Context, req *pubsubpb.GetSchemaRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)

  - 
            func (c *SchemaClient) ListSchemaRevisions(ctx context.Context, req *pubsubpb.ListSchemaRevisionsRequest, ...) *SchemaIterator

  - 
            func (c *SchemaClient) ListSchemas(ctx context.Context, req *pubsubpb.ListSchemasRequest, opts ...gax.CallOption) *SchemaIterator

  - 
            func (c *SchemaClient) RollbackSchema(ctx context.Context, req *pubsubpb.RollbackSchemaRequest, ...) (*pubsubpb.Schema, error)

  - 
            func (c *SchemaClient) SetIamPolicy(ctx context.Context, req *iampb.SetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *SchemaClient) TestIamPermissions(ctx context.Context, req *iampb.TestIamPermissionsRequest, ...) (*iampb.TestIamPermissionsResponse, error)

  - 
            func (c *SchemaClient) ValidateMessage(ctx context.Context, req *pubsubpb.ValidateMessageRequest, ...) (*pubsubpb.ValidateMessageResponse, error)

  - 
            func (c *SchemaClient) ValidateSchema(ctx context.Context, req *pubsubpb.ValidateSchemaRequest, ...) (*pubsubpb.ValidateSchemaResponse, error)

- 
          type SchemaIterator

- 

  - 
            func (it *SchemaIterator) All() iter.Seq2[*pubsubpb.Schema, error]

  - 
            func (it *SchemaIterator) Next() (*pubsubpb.Schema, error)

  - 
            func (it *SchemaIterator) PageInfo() *iterator.PageInfo

- 
          type SnapshotIterator

- 

  - 
            func (it *SnapshotIterator) All() iter.Seq2[*pubsubpb.Snapshot, error]

  - 
            func (it *SnapshotIterator) Next() (*pubsubpb.Snapshot, error)

  - 
            func (it *SnapshotIterator) PageInfo() *iterator.PageInfo

- 
          type StringIterator

- 

  - 
            func (it *StringIterator) All() iter.Seq2[string, error]

  - 
            func (it *StringIterator) Next() (string, error)

  - 
            func (it *StringIterator) PageInfo() *iterator.PageInfo

- 
          type SubscriberCallOptions

- 
          type SubscriberClient

- 

  - 
            func NewSubscriberClient(ctx context.Context, opts ...option.ClientOption) (*SubscriberClient, error)

  - 
            func NewSubscriberRESTClient(ctx context.Context, opts ...option.ClientOption) (*SubscriberClient, error)

- 

  - 
            func (c *SubscriberClient) Acknowledge(ctx context.Context, req *pubsubpb.AcknowledgeRequest, opts ...gax.CallOption) error

  - 
            func (c *SubscriberClient) Close() error

  - 
            func (c *SubscriberClient) Connection() *grpc.ClientConndeprecated

  - 
            func (c *SubscriberClient) CreateSnapshot(ctx context.Context, req *pubsubpb.CreateSnapshotRequest, ...) (*pubsubpb.Snapshot, error)

  - 
            func (c *SubscriberClient) CreateSubscription(ctx context.Context, req *pubsubpb.Subscription, opts ...gax.CallOption) (*pubsubpb.Subscription, error)

  - 
            func (c *SubscriberClient) DeleteSnapshot(ctx context.Context, req *pubsubpb.DeleteSnapshotRequest, ...) error

  - 
            func (c *SubscriberClient) DeleteSubscription(ctx context.Context, req *pubsubpb.DeleteSubscriptionRequest, ...) error

  - 
            func (c *SubscriberClient) GetIamPolicy(ctx context.Context, req *iampb.GetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *SubscriberClient) GetSnapshot(ctx context.Context, req *pubsubpb.GetSnapshotRequest, opts ...gax.CallOption) (*pubsubpb.Snapshot, error)

  - 
            func (c *SubscriberClient) GetSubscription(ctx context.Context, req *pubsubpb.GetSubscriptionRequest, ...) (*pubsubpb.Subscription, error)

  - 
            func (c *SubscriberClient) ListSnapshots(ctx context.Context, req *pubsubpb.ListSnapshotsRequest, ...) *SnapshotIterator

  - 
            func (c *SubscriberClient) ListSubscriptions(ctx context.Context, req *pubsubpb.ListSubscriptionsRequest, ...) *SubscriptionIterator

  - 
            func (c *SubscriberClient) ModifyAckDeadline(ctx context.Context, req *pubsubpb.ModifyAckDeadlineRequest, ...) error

  - 
            func (c *SubscriberClient) ModifyPushConfig(ctx context.Context, req *pubsubpb.ModifyPushConfigRequest, ...) error

  - 
            func (c *SubscriberClient) Pull(ctx context.Context, req *pubsubpb.PullRequest, opts ...gax.CallOption) (*pubsubpb.PullResponse, error)

  - 
            func (c *SubscriberClient) Seek(ctx context.Context, req *pubsubpb.SeekRequest, opts ...gax.CallOption) (*pubsubpb.SeekResponse, error)

  - 
            func (sc *SubscriberClient) SetGoogleClientInfo(keyval ...string)

  - 
            func (c *SubscriberClient) SetIamPolicy(ctx context.Context, req *iampb.SetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *SubscriberClient) StreamingPull(ctx context.Context, opts ...gax.CallOption) (pubsubpb.Subscriber_StreamingPullClient, error)

  - 
            func (c *SubscriberClient) SubscriptionIAM(subscription *pubsubpb.Subscription) *iam.Handle

  - 
            func (c *SubscriberClient) TestIamPermissions(ctx context.Context, req *iampb.TestIamPermissionsRequest, ...) (*iampb.TestIamPermissionsResponse, error)

  - 
            func (c *SubscriberClient) TopicIAM(topic *pubsubpb.Topic) *iam.Handle

  - 
            func (c *SubscriberClient) UpdateSnapshot(ctx context.Context, req *pubsubpb.UpdateSnapshotRequest, ...) (*pubsubpb.Snapshot, error)

  - 
            func (c *SubscriberClient) UpdateSubscription(ctx context.Context, req *pubsubpb.UpdateSubscriptionRequest, ...) (*pubsubpb.Subscription, error)

- 
          type SubscriptionIterator

- 

  - 
            func (it *SubscriptionIterator) All() iter.Seq2[*pubsubpb.Subscription, error]

  - 
            func (it *SubscriptionIterator) Next() (*pubsubpb.Subscription, error)

  - 
            func (it *SubscriptionIterator) PageInfo() *iterator.PageInfo

- 
          type TopicIterator

- 

  - 
            func (it *TopicIterator) All() iter.Seq2[*pubsubpb.Topic, error]

  - 
            func (it *TopicIterator) Next() (*pubsubpb.Topic, error)

  - 
            func (it *TopicIterator) PageInfo() *iterator.PageInfo

    
### Examples ¶

- NewPublisherClient

- NewPublisherRESTClient

- NewSchemaClient

- NewSchemaRESTClient

- NewSubscriberClient

- NewSubscriberRESTClient

- PublisherClient.CreateTopic

- PublisherClient.DeleteTopic

- PublisherClient.DetachSubscription

- PublisherClient.GetIamPolicy

- PublisherClient.GetTopic

- PublisherClient.ListTopicSnapshots

- PublisherClient.ListTopicSnapshots (All)

- PublisherClient.ListTopicSubscriptions

- PublisherClient.ListTopicSubscriptions (All)

- PublisherClient.ListTopics

- PublisherClient.ListTopics (All)

- PublisherClient.Publish

- PublisherClient.SetIamPolicy

- PublisherClient.TestIamPermissions

- PublisherClient.UpdateTopic

- SchemaClient.CommitSchema

- SchemaClient.CreateSchema

- SchemaClient.DeleteSchema

- SchemaClient.DeleteSchemaRevision

- SchemaClient.GetIamPolicy

- SchemaClient.GetSchema

- SchemaClient.ListSchemaRevisions

- SchemaClient.ListSchemaRevisions (All)

- SchemaClient.ListSchemas

- SchemaClient.ListSchemas (All)

- SchemaClient.RollbackSchema

- SchemaClient.SetIamPolicy

- SchemaClient.TestIamPermissions

- SchemaClient.ValidateMessage

- SchemaClient.ValidateSchema

- SubscriberClient.Acknowledge

- SubscriberClient.CreateSnapshot

- SubscriberClient.CreateSubscription

- SubscriberClient.DeleteSnapshot

- SubscriberClient.DeleteSubscription

- SubscriberClient.GetIamPolicy

- SubscriberClient.GetSnapshot

- SubscriberClient.GetSubscription

- SubscriberClient.ListSnapshots

- SubscriberClient.ListSnapshots (All)

- SubscriberClient.ListSubscriptions

- SubscriberClient.ListSubscriptions (All)

- SubscriberClient.ModifyAckDeadline

- SubscriberClient.ModifyPushConfig

- SubscriberClient.Pull

- SubscriberClient.Pull (LengthyClientProcessing)

- SubscriberClient.Seek

- SubscriberClient.SetIamPolicy

- SubscriberClient.StreamingPull

- SubscriberClient.TestIamPermissions

- SubscriberClient.UpdateSnapshot

- SubscriberClient.UpdateSubscription

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func DefaultAuthScopes ¶
  
    
  

    
    
      

```
func DefaultAuthScopes() []string
```

    
  

DefaultAuthScopes reports the default set of authentication scopes to use with this package.

  

        
	  
  
  
    
  

        
	  
  
  
    
  

        
	  
  
  
    
  

        
	  
  
  
    
  

        
	  
  
  
    
  

        
	  
  
  
    
  

        

  
### Types ¶

  
      
  
  
    
#### 
      type PublisherCallOptions ¶
  
    
  

    
    
      

```
type PublisherCallOptions struct {
	CreateTopic            []gax.CallOption
	UpdateTopic            []gax.CallOption
	Publish                []gax.CallOption
	GetTopic               []gax.CallOption
	ListTopics             []gax.CallOption
	ListTopicSubscriptions []gax.CallOption
	ListTopicSnapshots     []gax.CallOption
	DeleteTopic            []gax.CallOption
	DetachSubscription     []gax.CallOption
	GetIamPolicy           []gax.CallOption
	SetIamPolicy           []gax.CallOption
	TestIamPermissions     []gax.CallOption
}
```

    
  

PublisherCallOptions contains the retry settings for each method of PublisherClient.

  

    
      
  
  
    
#### 
      type PublisherClient ¶
  
    
  

    
    
      

```
type PublisherClient struct {

	// The call options for this service.
	CallOptions *PublisherCallOptions
	// contains filtered or unexported fields
}
```

    
  

PublisherClient is a client for interacting with Cloud Pub/Sub API.
Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

The service that an application uses to manipulate topics, and to send
messages to a topic.

    
  
  
    
#### 
      func NewPublisherClient ¶
  
    
  

    
    
      

```
func NewPublisherClient(ctx context.Context, opts ...option.ClientOption) (*PublisherClient, error)
```

    
  

NewPublisherClient creates a new publisher client based on gRPC.
The returned client must be Closed when it is done being used to clean up its underlying connections.

The service that an application uses to manipulate topics, and to send
messages to a topic.

  

  
    
  
  
    
#### 
      func NewPublisherRESTClient ¶
  
    
      added in
      v1.29.0
    
  

    
    
      

```
func NewPublisherRESTClient(ctx context.Context, opts ...option.ClientOption) (*PublisherClient, error)
```

    
  

NewPublisherRESTClient creates a new publisher rest client.

The service that an application uses to manipulate topics, and to send
messages to a topic.

  

  
    
  
  
    
#### 
      func (*PublisherClient) Close ¶
  
    
  

    
    
      

```
func (c *PublisherClient) Close() error
```

    
  

Close closes the connection to the API service. The user should invoke this when
the client is no longer required.

  

  
    
  
  
    
  

  
    
  
  
    
#### 
      func (*PublisherClient) CreateTopic ¶
  
    
  

    
    
      

```
func (c *PublisherClient) CreateTopic(ctx context.Context, req *pubsubpb.Topic, opts ...gax.CallOption) (*pubsubpb.Topic, error)
```

    
  

CreateTopic creates the given topic with the given name. See the [resource name rules]
(https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names (at https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names)).

  

  
    
  
  
    
#### 
      func (*PublisherClient) DeleteTopic ¶
  
    
  

    
    
      

```
func (c *PublisherClient) DeleteTopic(ctx context.Context, req *pubsubpb.DeleteTopicRequest, opts ...gax.CallOption) error
```

    
  

DeleteTopic deletes the topic with the given name. Returns NOT_FOUND if the topic
does not exist. After a topic is deleted, a new topic may be created with
the same name; this is an entirely new topic with none of the old
configuration or subscriptions. Existing subscriptions to this topic are
not deleted, but their topic field is set to _deleted-topic_.

  

  
    
  
  
    
#### 
      func (*PublisherClient) DetachSubscription ¶
  
    
      added in
      v1.4.0
    
  

    
    
      

```
func (c *PublisherClient) DetachSubscription(ctx context.Context, req *pubsubpb.DetachSubscriptionRequest, opts ...gax.CallOption) (*pubsubpb.DetachSubscriptionResponse, error)
```

    
  

DetachSubscription detaches a subscription from this topic. All messages retained in the
subscription are dropped. Subsequent Pull and StreamingPull requests
will return FAILED_PRECONDITION. If the subscription is a push
subscription, pushes to the endpoint will stop.

  

  
    
  
  
    
#### 
      func (*PublisherClient) GetIamPolicy ¶
  
    
      added in
      v1.12.0
    
  

    
    
      

```
func (c *PublisherClient) GetIamPolicy(ctx context.Context, req *iampb.GetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)
```

    
  

GetIamPolicy gets the access control policy for a resource. Returns an empty policy
if the resource exists and does not have a policy set.

  

  
    
  
  
    
#### 
      func (*PublisherClient) GetTopic ¶
  
    
  

    
    
      

```
func (c *PublisherClient) GetTopic(ctx context.Context, req *pubsubpb.GetTopicRequest, opts ...gax.CallOption) (*pubsubpb.Topic, error)
```

    
  

GetTopic gets the configuration of a topic.

  

  
    
  
  
    
#### 
      func (*PublisherClient) ListTopicSnapshots ¶
  
    
      added in
      v1.3.0
    
  

    
    
      

```
func (c *PublisherClient) ListTopicSnapshots(ctx context.Context, req *pubsubpb.ListTopicSnapshotsRequest, opts ...gax.CallOption) *StringIterator
```

    
  

ListTopicSnapshots lists the names of the snapshots on this topic. Snapshots are used in
Seek (at https://cloud.google.com/pubsub/docs/replay-overview) operations,
which allow you to manage message acknowledgments in bulk. That is, you can
set the acknowledgment state of messages in an existing subscription to the
state captured by a snapshot.

  

  
    
  
  
    
#### 
      func (*PublisherClient) ListTopicSubscriptions ¶
  
    
  

    
    
      

```
func (c *PublisherClient) ListTopicSubscriptions(ctx context.Context, req *pubsubpb.ListTopicSubscriptionsRequest, opts ...gax.CallOption) *StringIterator
```

    
  

ListTopicSubscriptions lists the names of the attached subscriptions on this topic.

  

  
    
  
  
    
#### 
      func (*PublisherClient) ListTopics ¶
  
    
  

    
    
      

```
func (c *PublisherClient) ListTopics(ctx context.Context, req *pubsubpb.ListTopicsRequest, opts ...gax.CallOption) *TopicIterator
```

    
  

ListTopics lists matching topics.

  

  
    
  
  
    
#### 
      func (*PublisherClient) Publish ¶
  
    
  

    
    
      

```
func (c *PublisherClient) Publish(ctx context.Context, req *pubsubpb.PublishRequest, opts ...gax.CallOption) (*pubsubpb.PublishResponse, error)
```

    
  

Publish adds one or more messages to the topic. Returns NOT_FOUND if the topic
does not exist.

  

  
    
  
  
    
#### 
      func (*PublisherClient) SetGoogleClientInfo ¶
  
    
  

    
    
      

```
func (pc *PublisherClient) SetGoogleClientInfo(keyval ...string)
```

    
  

SetGoogleClientInfo sets the name and version of the application in
the `x-goog-api-client` header passed on each request. Also passes any
provided key-value pairs. Intended for use by Google-written clients.

Internal use only.

  

  
    
  
  
    
#### 
      func (*PublisherClient) SetIamPolicy ¶
  
    
      added in
      v1.12.0
    
  

    
    
      

```
func (c *PublisherClient) SetIamPolicy(ctx context.Context, req *iampb.SetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)
```

    
  

SetIamPolicy sets the access control policy on the specified resource. Replaces
any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED
errors.

  

  
    
  
  
    
#### 
      func (*PublisherClient) SubscriptionIAM ¶
  
    
  

    
    
      

```
func (c *PublisherClient) SubscriptionIAM(subscription *pubsubpb.Subscription) *iam.Handle
```