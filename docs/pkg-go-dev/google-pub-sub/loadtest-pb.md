### Index ¶

- Constants

- Variables

- 
        func RegisterLoadtestWorkerServer(s grpc.ServiceRegistrar, srv LoadtestWorkerServer)

- 
          type CheckRequest

- 

  - 
            func (*CheckRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (*CheckRequest) ProtoMessage()

  - 
            func (x *CheckRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *CheckRequest) Reset()

  - 
            func (x *CheckRequest) String() string

- 
          type CheckResponse

- 

  - 
            func (*CheckResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *CheckResponse) GetBucketValues() []int64

  - 
            func (x *CheckResponse) GetFailed() int64

  - 
            func (x *CheckResponse) GetIsFinished() bool

  - 
            func (x *CheckResponse) GetReceivedMessages() []*MessageIdentifier

  - 
            func (x *CheckResponse) GetRunningDuration() *durationpb.Duration

  - 
            func (*CheckResponse) ProtoMessage()

  - 
            func (x *CheckResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *CheckResponse) Reset()

  - 
            func (x *CheckResponse) String() string

- 
          type LoadtestWorkerClient

- 

  - 
            func NewLoadtestWorkerClient(cc grpc.ClientConnInterface) LoadtestWorkerClient

- 
          type LoadtestWorkerServer

- 
          type MessageIdentifier

- 

  - 
            func (*MessageIdentifier) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *MessageIdentifier) GetPublisherClientId() int64

  - 
            func (x *MessageIdentifier) GetSequenceNumber() int32

  - 
            func (*MessageIdentifier) ProtoMessage()

  - 
            func (x *MessageIdentifier) ProtoReflect() protoreflect.Message

  - 
            func (x *MessageIdentifier) Reset()

  - 
            func (x *MessageIdentifier) String() string

- 
          type PublisherOptions

- 

  - 
            func (*PublisherOptions) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PublisherOptions) GetBatchDuration() *durationpb.Duration

  - 
            func (x *PublisherOptions) GetBatchSize() int32

  - 
            func (x *PublisherOptions) GetMessageSize() int32

  - 
            func (x *PublisherOptions) GetRate() float32

  - 
            func (*PublisherOptions) ProtoMessage()

  - 
            func (x *PublisherOptions) ProtoReflect() protoreflect.Message

  - 
            func (x *PublisherOptions) Reset()

  - 
            func (x *PublisherOptions) String() string

- 
          type PubsubOptions

- 

  - 
            func (*PubsubOptions) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PubsubOptions) GetSubscription() string

  - 
            func (*PubsubOptions) ProtoMessage()

  - 
            func (x *PubsubOptions) ProtoReflect() protoreflect.Message

  - 
            func (x *PubsubOptions) Reset()

  - 
            func (x *PubsubOptions) String() string

- 
          type StartRequest

- 

  - 
            func (*StartRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (m *StartRequest) GetClientOptions() isStartRequest_ClientOptions

  - 
            func (x *StartRequest) GetCpuScaling() int32

  - 
            func (x *StartRequest) GetIncludeIds() bool

  - 
            func (m *StartRequest) GetOptions() isStartRequest_Options

  - 
            func (x *StartRequest) GetProject() string

  - 
            func (x *StartRequest) GetPublisherOptions() *PublisherOptions

  - 
            func (x *StartRequest) GetPubsubOptions() *PubsubOptions

  - 
            func (x *StartRequest) GetStartTime() *timestamppb.Timestamp

  - 
            func (x *StartRequest) GetSubscriberOptions() *SubscriberOptions

  - 
            func (x *StartRequest) GetTestDuration() *durationpb.Duration

  - 
            func (x *StartRequest) GetTopic() string

  - 
            func (*StartRequest) ProtoMessage()

  - 
            func (x *StartRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *StartRequest) Reset()

  - 
            func (x *StartRequest) String() string

- 
          type StartRequest_PublisherOptions

- 
          type StartRequest_PubsubOptions

- 
          type StartRequest_SubscriberOptions

- 
          type StartResponse

- 

  - 
            func (*StartResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (*StartResponse) ProtoMessage()

  - 
            func (x *StartResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *StartResponse) Reset()

  - 
            func (x *StartResponse) String() string

- 
          type SubscriberOptions

- 

  - 
            func (*SubscriberOptions) Descriptor() ([]byte, []int)deprecated

  - 
            func (*SubscriberOptions) ProtoMessage()

  - 
            func (x *SubscriberOptions) ProtoReflect() protoreflect.Message

  - 
            func (x *SubscriberOptions) Reset()

  - 
            func (x *SubscriberOptions) String() string

- 
          type UnimplementedLoadtestWorkerServer

- 

  - 
            func (UnimplementedLoadtestWorkerServer) Check(context.Context, *CheckRequest) (*CheckResponse, error)

  - 
            func (UnimplementedLoadtestWorkerServer) Start(context.Context, *StartRequest) (*StartResponse, error)

- 
          type UnsafeLoadtestWorkerServer

### Constants ¶

  
    
      View Source
      

```
const (
	LoadtestWorker_Start_FullMethodName = "/google.pubsub.loadtest.LoadtestWorker/Start"
	LoadtestWorker_Check_FullMethodName = "/google.pubsub.loadtest.LoadtestWorker/Check"
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var File_loadtest_proto protoreflect.FileDescriptor
```

    
  

    
      View Source
      

```
var LoadtestWorker_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "google.pubsub.loadtest.LoadtestWorker",
	HandlerType: (*LoadtestWorkerServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Start",
			Handler:    _LoadtestWorker_Start_Handler,
		},
		{
			MethodName: "Check",
			Handler:    _LoadtestWorker_Check_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "loadtest.proto",
}
```

    
  

LoadtestWorker_ServiceDesc is the grpc.ServiceDesc for LoadtestWorker service.
It's only intended for direct use with grpc.RegisterService,
and not to be introspected or modified (even as a copy)

  
### Functions ¶

  
	  
  
  
    
#### 
      func RegisterLoadtestWorkerServer ¶
  
    
  

    
    
      

```
func RegisterLoadtestWorkerServer(s grpc.ServiceRegistrar, srv LoadtestWorkerServer)
```