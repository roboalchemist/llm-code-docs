### Index ¶

- Constants

- Variables

- 
        func RegisterPubsubBenchWrapperServer(s grpc.ServiceRegistrar, srv PubsubBenchWrapperServer)

- 
          type EmptyResponse

- 

  - 
            func (*EmptyResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (*EmptyResponse) ProtoMessage()

  - 
            func (x *EmptyResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *EmptyResponse) Reset()

  - 
            func (x *EmptyResponse) String() string

- 
          type PubsubBenchWrapperClient

- 

  - 
            func NewPubsubBenchWrapperClient(cc grpc.ClientConnInterface) PubsubBenchWrapperClient

- 
          type PubsubBenchWrapperServer

- 
          type PubsubRecv

- 

  - 
            func (*PubsubRecv) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *PubsubRecv) GetSubName() string

  - 
            func (*PubsubRecv) ProtoMessage()

  - 
            func (x *PubsubRecv) ProtoReflect() protoreflect.Message

  - 
            func (x *PubsubRecv) Reset()

  - 
            func (x *PubsubRecv) String() string

- 
          type UnimplementedPubsubBenchWrapperServer

- 

  - 
            func (UnimplementedPubsubBenchWrapperServer) Recv(context.Context, *PubsubRecv) (*EmptyResponse, error)

- 
          type UnsafePubsubBenchWrapperServer

### Constants ¶

  
    
      View Source
      

```
const (
	PubsubBenchWrapper_Recv_FullMethodName = "/pubsub_bench.PubsubBenchWrapper/Recv"
)
```

    
  

  
### Variables ¶

  
    
      View Source
      

```
var File_pubsub_proto protoreflect.FileDescriptor
```

    
  

    
      View Source
      

```
var PubsubBenchWrapper_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "pubsub_bench.PubsubBenchWrapper",
	HandlerType: (*PubsubBenchWrapperServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Recv",
			Handler:    _PubsubBenchWrapper_Recv_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "pubsub.proto",
}
```

    
  

PubsubBenchWrapper_ServiceDesc is the grpc.ServiceDesc for PubsubBenchWrapper service.
It's only intended for direct use with grpc.RegisterService,
and not to be introspected or modified (even as a copy)

  
### Functions ¶

  
	  
  
  
    
#### 
      func RegisterPubsubBenchWrapperServer ¶
  
    
  

    
    
      

```
func RegisterPubsubBenchWrapperServer(s grpc.ServiceRegistrar, srv PubsubBenchWrapperServer)
```