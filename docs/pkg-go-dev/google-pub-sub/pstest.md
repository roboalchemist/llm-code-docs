### Overview ¶

Package pstest provides a fake Cloud PubSub service for testing. It implements a
simplified form of the service, suitable for unit tests. It may behave
differently from the actual service in ways in which the service is
non-deterministic or unspecified: timing, delivery order, etc.

This package is EXPERIMENTAL and is subject to change without notice.

See the example for usage.

    
### Index ¶

- 
        func ResetMinAckDeadline()

- 
        func SetMinAckDeadline(n time.Duration)

- 
        func ValidateFilter(filter string) error

- 
          type GServer

- 

  - 
            func (s *GServer) Acknowledge(_ context.Context, req *pb.AcknowledgeRequest) (*emptypb.Empty, error)

  - 
            func (s *GServer) CommitSchema(_ context.Context, req *pb.CommitSchemaRequest) (*pb.Schema, error)

  - 
            func (s *GServer) CreateSchema(_ context.Context, req *pb.CreateSchemaRequest) (*pb.Schema, error)

  - 
            func (s *GServer) CreateSubscription(_ context.Context, ps *pb.Subscription) (*pb.Subscription, error)

  - 
            func (s *GServer) CreateTopic(_ context.Context, t *pb.Topic) (*pb.Topic, error)

  - 
            func (s *GServer) DeleteSchema(_ context.Context, req *pb.DeleteSchemaRequest) (*emptypb.Empty, error)

  - 
            func (s *GServer) DeleteSchemaRevision(_ context.Context, req *pb.DeleteSchemaRevisionRequest) (*pb.Schema, error)

  - 
            func (s *GServer) DeleteSubscription(_ context.Context, req *pb.DeleteSubscriptionRequest) (*emptypb.Empty, error)

  - 
            func (s *GServer) DeleteTopic(_ context.Context, req *pb.DeleteTopicRequest) (*emptypb.Empty, error)

  - 
            func (s *GServer) DetachSubscription(_ context.Context, req *pb.DetachSubscriptionRequest) (*pb.DetachSubscriptionResponse, error)

  - 
            func (s *GServer) GetSchema(_ context.Context, req *pb.GetSchemaRequest) (*pb.Schema, error)

  - 
            func (s *GServer) GetSubscription(_ context.Context, req *pb.GetSubscriptionRequest) (*pb.Subscription, error)

  - 
            func (s *GServer) GetTopic(_ context.Context, req *pb.GetTopicRequest) (*pb.Topic, error)

  - 
            func (s *GServer) ListSchemaRevisions(_ context.Context, req *pb.ListSchemaRevisionsRequest) (*pb.ListSchemaRevisionsResponse, error)

  - 
            func (s *GServer) ListSchemas(_ context.Context, req *pb.ListSchemasRequest) (*pb.ListSchemasResponse, error)

  - 
            func (s *GServer) ListSubscriptions(_ context.Context, req *pb.ListSubscriptionsRequest) (*pb.ListSubscriptionsResponse, error)

  - 
            func (s *GServer) ListTopicSubscriptions(_ context.Context, req *pb.ListTopicSubscriptionsRequest) (*pb.ListTopicSubscriptionsResponse, error)

  - 
            func (s *GServer) ListTopics(_ context.Context, req *pb.ListTopicsRequest) (*pb.ListTopicsResponse, error)

  - 
            func (s *GServer) ModifyAckDeadline(_ context.Context, req *pb.ModifyAckDeadlineRequest) (*emptypb.Empty, error)

  - 
            func (s *GServer) Publish(_ context.Context, req *pb.PublishRequest) (*pb.PublishResponse, error)

  - 
            func (s *GServer) Pull(ctx context.Context, req *pb.PullRequest) (*pb.PullResponse, error)

  - 
            func (s *GServer) RollbackSchema(_ context.Context, req *pb.RollbackSchemaRequest) (*pb.Schema, error)

  - 
            func (s *GServer) Seek(ctx context.Context, req *pb.SeekRequest) (*pb.SeekResponse, error)

  - 
            func (s *GServer) StreamingPull(sps pb.Subscriber_StreamingPullServer) error

  - 
            func (s *GServer) UpdateSubscription(_ context.Context, req *pb.UpdateSubscriptionRequest) (*pb.Subscription, error)

  - 
            func (s *GServer) UpdateTopic(_ context.Context, req *pb.UpdateTopicRequest) (*pb.Topic, error)

  - 
            func (s *GServer) ValidateMessage(_ context.Context, req *pb.ValidateMessageRequest) (*pb.ValidateMessageResponse, error)

  - 
            func (s *GServer) ValidateSchema(_ context.Context, req *pb.ValidateSchemaRequest) (*pb.ValidateSchemaResponse, error)

- 
          type Message

- 
          type Modack

- 
          type Reactor

- 
          type ReactorOptions

- 
          type Server

- 

  - 
            func NewServer(opts ...ServerReactorOption) *Server

  - 
            func NewServerWithAddress(address string, opts ...ServerReactorOption) *Server

  - 
            func NewServerWithCallback(port int, callback func(*grpc.Server), opts ...ServerReactorOption) *Server

  - 
            func NewServerWithPort(port int, opts ...ServerReactorOption) *Server

- 

  - 
            func (s *Server) AddPublishResponse(pbr *pb.PublishResponse, err error)

  - 
            func (s *Server) ClearMessages()

  - 
            func (s *Server) Close() error

  - 
            func (s *Server) Message(id string) *Message

  - 
            func (s *Server) Messages() []*Message

  - 
            func (s *Server) Publish(topic string, data []byte, attrs map[string]string) string

  - 
            func (s *Server) PublishOrdered(topic string, data []byte, attrs map[string]string, orderingKey string) string

  - 
            func (s *Server) ResetPublishResponses(size int)

  - 
            func (s *Server) SetAutoPublishResponse(autoPublishResponse bool)

  - 
            func (s *Server) SetStreamTimeout(d time.Duration)

  - 
            func (s *Server) SetTimeNowFunc(f func() time.Time)

  - 
            func (s *Server) Wait()

- 
          type ServerReactorOption

- 

  - 
            func WithErrorInjection(funcName string, code codes.Code, msg string) ServerReactorOption

    
### Examples ¶

- NewServer

- NewServerWithPort

### Constants ¶

  

This section is empty.

  
### Variables ¶

  

This section is empty.

  
### Functions ¶

  
	  
  
  
    
#### 
      func ResetMinAckDeadline ¶
  
    
  

    
    
      

```
func ResetMinAckDeadline()
```

    
  

ResetMinAckDeadline resets the minack deadline to the default.

  

        
	  
  
  
    
#### 
      func SetMinAckDeadline ¶
  
    
  

    
    
      

```
func SetMinAckDeadline(n time.Duration)
```

    
  

SetMinAckDeadline changes the minack deadline to n. Must be
greater than or equal to 1 second. Remember to reset this value
to the default after your test changes it. Example usage:

```
pstest.SetMinAckDeadlineSecs(1)
defer pstest.ResetMinAckDeadlineSecs()

```

  

        
	  
  
  
    
#### 
      func ValidateFilter ¶
  
    
      added in
      v1.35.0
    
  

    
    
      

```
func ValidateFilter(filter string) error
```

    
  

ValidateFilter validates if the filter string is parsable.

  

        

  
### Types ¶

  
      
  
  
    
#### 
      type GServer ¶
  
    
  

    
    
      

```
type GServer struct {
	pb.UnimplementedPublisherServer
	pb.UnimplementedSubscriberServer
	pb.UnimplementedSchemaServiceServer
	// contains filtered or unexported fields
}
```

    
  

GServer is the underlying service implementor. It is not intended to be used
directly.

    
  
  
    
#### 
      func (*GServer) Acknowledge ¶
  
    
  

    
    
      

```
func (s *GServer) Acknowledge(_ context.Context, req *pb.AcknowledgeRequest) (*emptypb.Empty, error)
```

    
  

Acknowledge marks the message as acknowleged.

  

  
    
  
  
    
#### 
      func (*GServer) CommitSchema ¶
  
    
      added in
      v1.29.0
    
  

    
    
      

```
func (s *GServer) CommitSchema(_ context.Context, req *pb.CommitSchemaRequest) (*pb.Schema, error)
```

    
  

CommitSchema commits a new schema revision.

  

  
    
  
  
    
#### 
      func (*GServer) CreateSchema ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func (s *GServer) CreateSchema(_ context.Context, req *pb.CreateSchemaRequest) (*pb.Schema, error)
```

    
  

CreateSchema creates a new schema.

  

  
    
  
  
    
#### 
      func (*GServer) CreateSubscription ¶
  
    
  

    
    
      

```
func (s *GServer) CreateSubscription(_ context.Context, ps *pb.Subscription) (*pb.Subscription, error)
```

    
  

CreateSubscription creates a Pub/Sub subscription.

  

  
    
  
  
    
#### 
      func (*GServer) CreateTopic ¶
  
    
  

    
    
      

```
func (s *GServer) CreateTopic(_ context.Context, t *pb.Topic) (*pb.Topic, error)
```

    
  

CreateTopic creates a topic.

  

  
    
  
  
    
#### 
      func (*GServer) DeleteSchema ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func (s *GServer) DeleteSchema(_ context.Context, req *pb.DeleteSchemaRequest) (*emptypb.Empty, error)
```

    
  

DeleteSchema deletes an existing schema.

  

  
    
  
  
    
#### 
      func (*GServer) DeleteSchemaRevision ¶
  
    
      added in
      v1.29.0
    
  

    
    
      

```
func (s *GServer) DeleteSchemaRevision(_ context.Context, req *pb.DeleteSchemaRevisionRequest) (*pb.Schema, error)
```

    
  

DeleteSchemaRevision deletes a schema revision.

  

  
    
  
  
    
#### 
      func (*GServer) DeleteSubscription ¶
  
    
  

    
    
      

```
func (s *GServer) DeleteSubscription(_ context.Context, req *pb.DeleteSubscriptionRequest) (*emptypb.Empty, error)
```

    
  

DeleteSubscription deletes the Pub/Sub subscription.

  

  
    
  
  
    
#### 
      func (*GServer) DeleteTopic ¶
  
    
  

    
    
      

```
func (s *GServer) DeleteTopic(_ context.Context, req *pb.DeleteTopicRequest) (*emptypb.Empty, error)
```

    
  

DeleteTopic deletes the topic.

  

  
    
  
  
    
#### 
      func (*GServer) DetachSubscription ¶
  
    
      added in
      v1.5.0
    
  

    
    
      

```
func (s *GServer) DetachSubscription(_ context.Context, req *pb.DetachSubscriptionRequest) (*pb.DetachSubscriptionResponse, error)
```

    
  

DetachSubscription detaches the subscription from the topic.

  

  
    
  
  
    
#### 
      func (*GServer) GetSchema ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func (s *GServer) GetSchema(_ context.Context, req *pb.GetSchemaRequest) (*pb.Schema, error)
```

    
  

GetSchema gets an existing schema details.

  

  
    
  
  
    
#### 
      func (*GServer) GetSubscription ¶
  
    
  

    
    
      

```
func (s *GServer) GetSubscription(_ context.Context, req *pb.GetSubscriptionRequest) (*pb.Subscription, error)
```

    
  

GetSubscription fetches an existing Pub/Sub subscription details.

  

  
    
  
  
    
#### 
      func (*GServer) GetTopic ¶
  
    
  

    
    
      

```
func (s *GServer) GetTopic(_ context.Context, req *pb.GetTopicRequest) (*pb.Topic, error)
```

    
  

GetTopic gets a Pub/Sub topic.

  

  
    
  
  
    
#### 
      func (*GServer) ListSchemaRevisions ¶
  
    
      added in
      v1.29.0
    
  

    
    
      

```
func (s *GServer) ListSchemaRevisions(_ context.Context, req *pb.ListSchemaRevisionsRequest) (*pb.ListSchemaRevisionsResponse, error)
```

    
  

ListSchemaRevisions lists the schema revisions.

  

  
    
  
  
    
#### 
      func (*GServer) ListSchemas ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func (s *GServer) ListSchemas(_ context.Context, req *pb.ListSchemasRequest) (*pb.ListSchemasResponse, error)
```

    
  

ListSchemas lists the available schemas in this server.

  

  
    
  
  
    
#### 
      func (*GServer) ListSubscriptions ¶
  
    
  

    
    
      

```
func (s *GServer) ListSubscriptions(_ context.Context, req *pb.ListSubscriptionsRequest) (*pb.ListSubscriptionsResponse, error)
```

    
  

ListSubscriptions lists the Pub/Sub subscriptions in this server.

  

  
    
  
  
    
#### 
      func (*GServer) ListTopicSubscriptions ¶
  
    
  

    
    
      

```
func (s *GServer) ListTopicSubscriptions(_ context.Context, req *pb.ListTopicSubscriptionsRequest) (*pb.ListTopicSubscriptionsResponse, error)
```

    
  

ListTopicSubscriptions lists the subscriptions associated with a topic.

  

  
    
  
  
    
#### 
      func (*GServer) ListTopics ¶
  
    
  

    
    
      

```
func (s *GServer) ListTopics(_ context.Context, req *pb.ListTopicsRequest) (*pb.ListTopicsResponse, error)
```

    
  

ListTopics lists the topics in this server.

  

  
    
  
  
    
#### 
      func (*GServer) ModifyAckDeadline ¶
  
    
  

    
    
      

```
func (s *GServer) ModifyAckDeadline(_ context.Context, req *pb.ModifyAckDeadlineRequest) (*emptypb.Empty, error)
```

    
  

ModifyAckDeadline modifies the ack deadline of the message.

  

  
    
  
  
    
#### 
      func (*GServer) Publish ¶
  
    
  

    
    
      

```
func (s *GServer) Publish(_ context.Context, req *pb.PublishRequest) (*pb.PublishResponse, error)
```

    
  

Publish sends a message to the topic.

  

  
    
  
  
    
#### 
      func (*GServer) Pull ¶
  
    
  

    
    
      

```
func (s *GServer) Pull(ctx context.Context, req *pb.PullRequest) (*pb.PullResponse, error)
```

    
  

Pull returns a list of unacknowledged messages from a subscription.

  

  
    
  
  
    
#### 
      func (*GServer) RollbackSchema ¶
  
    
      added in
      v1.29.0
    
  

    
    
      

```
func (s *GServer) RollbackSchema(_ context.Context, req *pb.RollbackSchemaRequest) (*pb.Schema, error)
```

    
  

RollbackSchema rolls back the current schema to a previous revision by copying and creating a new revision.

  

  
    
  
  
    
#### 
      func (*GServer) Seek ¶
  
    
  

    
    
      

```
func (s *GServer) Seek(ctx context.Context, req *pb.SeekRequest) (*pb.SeekResponse, error)
```

    
  

Seek updates a subscription to a specific point in time or snapshot.

  

  
    
  
  
    
#### 
      func (*GServer) StreamingPull ¶
  
    
  

    
    
      

```
func (s *GServer) StreamingPull(sps pb.Subscriber_StreamingPullServer) error
```

    
  

StreamingPull return a stream to pull messages from a subscription.

  

  
    
  
  
    
#### 
      func (*GServer) UpdateSubscription ¶
  
    
  

    
    
      

```
func (s *GServer) UpdateSubscription(_ context.Context, req *pb.UpdateSubscriptionRequest) (*pb.Subscription, error)
```

    
  

UpdateSubscription updates an existing Pub/Sub subscription.

  

  
    
  
  
    
#### 
      func (*GServer) UpdateTopic ¶
  
    
  

    
    
      

```
func (s *GServer) UpdateTopic(_ context.Context, req *pb.UpdateTopicRequest) (*pb.Topic, error)
```

    
  

UpdateTopic updates the Pub/Sub topic.

  

  
    
  
  
    
#### 
      func (*GServer) ValidateMessage ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func (s *GServer) ValidateMessage(_ context.Context, req *pb.ValidateMessageRequest) (*pb.ValidateMessageResponse, error)
```

    
  

ValidateMessage mocks the ValidateMessage call but only checks that the schema definition to validate the
message against is not empty.

  

  
    
  
  
    
#### 
      func (*GServer) ValidateSchema ¶
  
    
      added in
      v1.15.0
    
  

    
    
      

```
func (s *GServer) ValidateSchema(_ context.Context, req *pb.ValidateSchemaRequest) (*pb.ValidateSchemaResponse, error)
```

    
  

ValidateSchema mocks the ValidateSchema call but only checks that the schema definition is not empty.