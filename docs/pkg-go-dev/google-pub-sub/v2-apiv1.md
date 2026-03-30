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
// go get cloud.google.com/go/pubsub/v2/apiv1@latest
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
	// See https://pkg.go.dev/cloud.google.com/go/pubsub/v2/apiv1/pubsubpb#CommitSchemaRequest.
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
          type SubscriptionAdminCallOptions

- 
          type SubscriptionAdminClient

- 

  - 
            func NewSubscriptionAdminClient(ctx context.Context, opts ...option.ClientOption) (*SubscriptionAdminClient, error)

  - 
            func NewSubscriptionAdminRESTClient(ctx context.Context, opts ...option.ClientOption) (*SubscriptionAdminClient, error)

- 

  - 
            func (c *SubscriptionAdminClient) Acknowledge(ctx context.Context, req *pubsubpb.AcknowledgeRequest, opts ...gax.CallOption) error

  - 
            func (c *SubscriptionAdminClient) Close() error

  - 
            func (c *SubscriptionAdminClient) Connection() *grpc.ClientConndeprecated

  - 
            func (c *SubscriptionAdminClient) CreateSnapshot(ctx context.Context, req *pubsubpb.CreateSnapshotRequest, ...) (*pubsubpb.Snapshot, error)

  - 
            func (c *SubscriptionAdminClient) CreateSubscription(ctx context.Context, req *pubsubpb.Subscription, opts ...gax.CallOption) (*pubsubpb.Subscription, error)

  - 
            func (c *SubscriptionAdminClient) DeleteSnapshot(ctx context.Context, req *pubsubpb.DeleteSnapshotRequest, ...) error

  - 
            func (c *SubscriptionAdminClient) DeleteSubscription(ctx context.Context, req *pubsubpb.DeleteSubscriptionRequest, ...) error

  - 
            func (c *SubscriptionAdminClient) GetIamPolicy(ctx context.Context, req *iampb.GetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *SubscriptionAdminClient) GetSnapshot(ctx context.Context, req *pubsubpb.GetSnapshotRequest, opts ...gax.CallOption) (*pubsubpb.Snapshot, error)

  - 
            func (c *SubscriptionAdminClient) GetSubscription(ctx context.Context, req *pubsubpb.GetSubscriptionRequest, ...) (*pubsubpb.Subscription, error)

  - 
            func (c *SubscriptionAdminClient) ListSnapshots(ctx context.Context, req *pubsubpb.ListSnapshotsRequest, ...) *SnapshotIterator

  - 
            func (c *SubscriptionAdminClient) ListSubscriptions(ctx context.Context, req *pubsubpb.ListSubscriptionsRequest, ...) *SubscriptionIterator

  - 
            func (c *SubscriptionAdminClient) ModifyAckDeadline(ctx context.Context, req *pubsubpb.ModifyAckDeadlineRequest, ...) error

  - 
            func (c *SubscriptionAdminClient) ModifyPushConfig(ctx context.Context, req *pubsubpb.ModifyPushConfigRequest, ...) error

  - 
            func (c *SubscriptionAdminClient) Pull(ctx context.Context, req *pubsubpb.PullRequest, opts ...gax.CallOption) (*pubsubpb.PullResponse, error)

  - 
            func (c *SubscriptionAdminClient) Seek(ctx context.Context, req *pubsubpb.SeekRequest, opts ...gax.CallOption) (*pubsubpb.SeekResponse, error)

  - 
            func (sc *SubscriptionAdminClient) SetGoogleClientInfo(keyval ...string)

  - 
            func (c *SubscriptionAdminClient) SetIamPolicy(ctx context.Context, req *iampb.SetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *SubscriptionAdminClient) StreamingPull(ctx context.Context, opts ...gax.CallOption) (pubsubpb.Subscriber_StreamingPullClient, error)

  - 
            func (c *SubscriptionAdminClient) TestIamPermissions(ctx context.Context, req *iampb.TestIamPermissionsRequest, ...) (*iampb.TestIamPermissionsResponse, error)

  - 
            func (c *SubscriptionAdminClient) UpdateSnapshot(ctx context.Context, req *pubsubpb.UpdateSnapshotRequest, ...) (*pubsubpb.Snapshot, error)

  - 
            func (c *SubscriptionAdminClient) UpdateSubscription(ctx context.Context, req *pubsubpb.UpdateSubscriptionRequest, ...) (*pubsubpb.Subscription, error)

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
          type TopicAdminCallOptions

- 
          type TopicAdminClient

- 

  - 
            func NewTopicAdminClient(ctx context.Context, opts ...option.ClientOption) (*TopicAdminClient, error)

  - 
            func NewTopicAdminRESTClient(ctx context.Context, opts ...option.ClientOption) (*TopicAdminClient, error)

- 

  - 
            func (c *TopicAdminClient) Close() error

  - 
            func (c *TopicAdminClient) Connection() *grpc.ClientConndeprecated

  - 
            func (c *TopicAdminClient) CreateTopic(ctx context.Context, req *pubsubpb.Topic, opts ...gax.CallOption) (*pubsubpb.Topic, error)

  - 
            func (c *TopicAdminClient) DeleteTopic(ctx context.Context, req *pubsubpb.DeleteTopicRequest, opts ...gax.CallOption) error

  - 
            func (c *TopicAdminClient) DetachSubscription(ctx context.Context, req *pubsubpb.DetachSubscriptionRequest, ...) (*pubsubpb.DetachSubscriptionResponse, error)

  - 
            func (c *TopicAdminClient) GetIamPolicy(ctx context.Context, req *iampb.GetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *TopicAdminClient) GetTopic(ctx context.Context, req *pubsubpb.GetTopicRequest, opts ...gax.CallOption) (*pubsubpb.Topic, error)

  - 
            func (c *TopicAdminClient) ListTopicSnapshots(ctx context.Context, req *pubsubpb.ListTopicSnapshotsRequest, ...) *StringIterator

  - 
            func (c *TopicAdminClient) ListTopicSubscriptions(ctx context.Context, req *pubsubpb.ListTopicSubscriptionsRequest, ...) *StringIterator

  - 
            func (c *TopicAdminClient) ListTopics(ctx context.Context, req *pubsubpb.ListTopicsRequest, opts ...gax.CallOption) *TopicIterator

  - 
            func (c *TopicAdminClient) Publish(ctx context.Context, req *pubsubpb.PublishRequest, opts ...gax.CallOption) (*pubsubpb.PublishResponse, error)

  - 
            func (tc *TopicAdminClient) SetGoogleClientInfo(keyval ...string)

  - 
            func (c *TopicAdminClient) SetIamPolicy(ctx context.Context, req *iampb.SetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)

  - 
            func (c *TopicAdminClient) TestIamPermissions(ctx context.Context, req *iampb.TestIamPermissionsRequest, ...) (*iampb.TestIamPermissionsResponse, error)

  - 
            func (c *TopicAdminClient) UpdateTopic(ctx context.Context, req *pubsubpb.UpdateTopicRequest, opts ...gax.CallOption) (*pubsubpb.Topic, error)

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

- NewSchemaClient

- NewSchemaRESTClient

- NewSubscriptionAdminClient

- NewSubscriptionAdminRESTClient

- NewTopicAdminClient

- NewTopicAdminRESTClient

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

- SubscriptionAdminClient.Acknowledge

- SubscriptionAdminClient.CreateSnapshot

- SubscriptionAdminClient.CreateSubscription

- SubscriptionAdminClient.DeleteSnapshot

- SubscriptionAdminClient.DeleteSubscription

- SubscriptionAdminClient.GetIamPolicy

- SubscriptionAdminClient.GetSnapshot

- SubscriptionAdminClient.GetSubscription

- SubscriptionAdminClient.ListSnapshots

- SubscriptionAdminClient.ListSnapshots (All)

- SubscriptionAdminClient.ListSubscriptions

- SubscriptionAdminClient.ListSubscriptions (All)

- SubscriptionAdminClient.ModifyAckDeadline

- SubscriptionAdminClient.ModifyPushConfig

- SubscriptionAdminClient.Pull

- SubscriptionAdminClient.Seek

- SubscriptionAdminClient.SetIamPolicy

- SubscriptionAdminClient.StreamingPull

- SubscriptionAdminClient.TestIamPermissions

- SubscriptionAdminClient.UpdateSnapshot

- SubscriptionAdminClient.UpdateSubscription

- TopicAdminClient.CreateTopic

- TopicAdminClient.DeleteTopic

- TopicAdminClient.DetachSubscription

- TopicAdminClient.GetIamPolicy

- TopicAdminClient.GetTopic

- TopicAdminClient.ListTopicSnapshots

- TopicAdminClient.ListTopicSnapshots (All)

- TopicAdminClient.ListTopicSubscriptions

- TopicAdminClient.ListTopicSubscriptions (All)

- TopicAdminClient.ListTopics

- TopicAdminClient.ListTopics (All)

- TopicAdminClient.Publish

- TopicAdminClient.SetIamPolicy

- TopicAdminClient.TestIamPermissions

- TopicAdminClient.UpdateTopic

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
      type SchemaCallOptions ¶
  
    
  

    
    
      

```
type SchemaCallOptions struct {
	CreateSchema         []gax.CallOption
	GetSchema            []gax.CallOption
	ListSchemas          []gax.CallOption
	ListSchemaRevisions  []gax.CallOption
	CommitSchema         []gax.CallOption
	RollbackSchema       []gax.CallOption
	DeleteSchemaRevision []gax.CallOption
	DeleteSchema         []gax.CallOption
	ValidateSchema       []gax.CallOption
	ValidateMessage      []gax.CallOption
	GetIamPolicy         []gax.CallOption
	SetIamPolicy         []gax.CallOption
	TestIamPermissions   []gax.CallOption
}
```

    
  

SchemaCallOptions contains the retry settings for each method of SchemaClient.

  

    
      
  
  
    
#### 
      type SchemaClient ¶
  
    
  

    
    
      

```
type SchemaClient struct {

	// The call options for this service.
	CallOptions *SchemaCallOptions
	// contains filtered or unexported fields
}
```

    
  

SchemaClient is a client for interacting with Cloud Pub/Sub API.
Methods, except Close, may be called concurrently. However, fields must not be modified concurrently with method calls.

Service for doing schema-related operations.

    
  
  
    
#### 
      func NewSchemaClient ¶
  
    
  

    
    
      

```
func NewSchemaClient(ctx context.Context, opts ...option.ClientOption) (*SchemaClient, error)
```

    
  

NewSchemaClient creates a new schema service client based on gRPC.
The returned client must be Closed when it is done being used to clean up its underlying connections.

Service for doing schema-related operations.

  

  
    
  
  
    
#### 
      func NewSchemaRESTClient ¶
  
    
  

    
    
      

```
func NewSchemaRESTClient(ctx context.Context, opts ...option.ClientOption) (*SchemaClient, error)
```

    
  

NewSchemaRESTClient creates a new schema service rest client.

Service for doing schema-related operations.

  

  
    
  
  
    
#### 
      func (*SchemaClient) Close ¶
  
    
  

    
    
      

```
func (c *SchemaClient) Close() error
```

    
  

Close closes the connection to the API service. The user should invoke this when
the client is no longer required.

  

  
    
  
  
    
#### 
      func (*SchemaClient) CommitSchema ¶
  
    
  

    
    
      

```
func (c *SchemaClient) CommitSchema(ctx context.Context, req *pubsubpb.CommitSchemaRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)
```

    
  

CommitSchema commits a new schema revision to an existing schema.

  

  
    
  
  
    
  

  
    
  
  
    
#### 
      func (*SchemaClient) CreateSchema ¶
  
    
  

    
    
      

```
func (c *SchemaClient) CreateSchema(ctx context.Context, req *pubsubpb.CreateSchemaRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)
```

    
  

CreateSchema creates a schema.

  

  
    
  
  
    
#### 
      func (*SchemaClient) DeleteSchema ¶
  
    
  

    
    
      

```
func (c *SchemaClient) DeleteSchema(ctx context.Context, req *pubsubpb.DeleteSchemaRequest, opts ...gax.CallOption) error
```

    
  

DeleteSchema deletes a schema.

  

  
    
  
  
    
#### 
      func (*SchemaClient) DeleteSchemaRevision ¶
  
    
  

    
    
      

```
func (c *SchemaClient) DeleteSchemaRevision(ctx context.Context, req *pubsubpb.DeleteSchemaRevisionRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)
```

    
  

DeleteSchemaRevision deletes a specific schema revision.

  

  
    
  
  
    
#### 
      func (*SchemaClient) GetIamPolicy ¶
  
    
  

    
    
      

```
func (c *SchemaClient) GetIamPolicy(ctx context.Context, req *iampb.GetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)
```

    
  

GetIamPolicy gets the access control policy for a resource. Returns an empty policy
if the resource exists and does not have a policy set.

  

  
    
  
  
    
#### 
      func (*SchemaClient) GetSchema ¶
  
    
  

    
    
      

```
func (c *SchemaClient) GetSchema(ctx context.Context, req *pubsubpb.GetSchemaRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)
```

    
  

GetSchema gets a schema.

  

  
    
  
  
    
#### 
      func (*SchemaClient) ListSchemaRevisions ¶
  
    
  

    
    
      

```
func (c *SchemaClient) ListSchemaRevisions(ctx context.Context, req *pubsubpb.ListSchemaRevisionsRequest, opts ...gax.CallOption) *SchemaIterator
```

    
  

ListSchemaRevisions lists all schema revisions for the named schema.

  

  
    
  
  
    
#### 
      func (*SchemaClient) ListSchemas ¶
  
    
  

    
    
      

```
func (c *SchemaClient) ListSchemas(ctx context.Context, req *pubsubpb.ListSchemasRequest, opts ...gax.CallOption) *SchemaIterator
```

    
  

ListSchemas lists schemas in a project.

  

  
    
  
  
    
#### 
      func (*SchemaClient) RollbackSchema ¶
  
    
  

    
    
      

```
func (c *SchemaClient) RollbackSchema(ctx context.Context, req *pubsubpb.RollbackSchemaRequest, opts ...gax.CallOption) (*pubsubpb.Schema, error)
```

    
  

RollbackSchema creates a new schema revision that is a copy of the provided revision_id.

  

  
    
  
  
    
#### 
      func (*SchemaClient) SetIamPolicy ¶
  
    
  

    
    
      

```
func (c *SchemaClient) SetIamPolicy(ctx context.Context, req *iampb.SetIamPolicyRequest, opts ...gax.CallOption) (*iampb.Policy, error)
```

    
  

SetIamPolicy sets the access control policy on the specified resource. Replaces
any existing policy.

Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED
errors.

  

  
    
  
  
    
#### 
      func (*SchemaClient) TestIamPermissions ¶
  
    
  

    
    
      

```
func (c *SchemaClient) TestIamPermissions(ctx context.Context, req *iampb.TestIamPermissionsRequest, opts ...gax.CallOption) (*iampb.TestIamPermissionsResponse, error)
```

    
  

TestIamPermissions returns permissions that a caller has on the specified resource. If the
resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building
permission-aware UIs and command-line tools, not for authorization
checking. This operation may “fail open” without warning.

  

  
    
  
  
    
#### 
      func (*SchemaClient) ValidateMessage ¶
  
    
  

    
    
      

```
func (c *SchemaClient) ValidateMessage(ctx context.Context, req *pubsubpb.ValidateMessageRequest, opts ...gax.CallOption) (*pubsubpb.ValidateMessageResponse, error)
```

    
  

ValidateMessage validates a message against a schema.

  

  
    
  
  
    
#### 
      func (*SchemaClient) ValidateSchema ¶
  
    
  

    
    
      

```
func (c *SchemaClient) ValidateSchema(ctx context.Context, req *pubsubpb.ValidateSchemaRequest, opts ...gax.CallOption) (*pubsubpb.ValidateSchemaResponse, error)
```

    
  

ValidateSchema validates a schema.