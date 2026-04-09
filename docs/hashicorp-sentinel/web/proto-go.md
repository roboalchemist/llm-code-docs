### Overview ¶

Package proto contains the Go generated files for the protocol buffer files.

    
### Index ¶

- Variables

- 
        func RegisterPluginServer(s *grpc.Server, srv PluginServer)

- 
          type Close

- 

  - 
            func (*Close) Descriptor() ([]byte, []int)deprecated

  - 
            func (*Close) ProtoMessage()

  - 
            func (x *Close) ProtoReflect() protoreflect.Message

  - 
            func (x *Close) Reset()

  - 
            func (x *Close) String() string

- 
          type Close_Request

- 

  - 
            func (*Close_Request) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Close_Request) GetInstanceId() uint64

  - 
            func (*Close_Request) ProtoMessage()

  - 
            func (x *Close_Request) ProtoReflect() protoreflect.Message

  - 
            func (x *Close_Request) Reset()

  - 
            func (x *Close_Request) String() string

- 
          type Configure

- 

  - 
            func (*Configure) Descriptor() ([]byte, []int)deprecated

  - 
            func (*Configure) ProtoMessage()

  - 
            func (x *Configure) ProtoReflect() protoreflect.Message

  - 
            func (x *Configure) Reset()

  - 
            func (x *Configure) String() string

- 
          type Configure_Request

- 

  - 
            func (*Configure_Request) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Configure_Request) GetConfig() *Value

  - 
            func (*Configure_Request) ProtoMessage()

  - 
            func (x *Configure_Request) ProtoReflect() protoreflect.Message

  - 
            func (x *Configure_Request) Reset()

  - 
            func (x *Configure_Request) String() string

- 
          type Configure_Response

- 

  - 
            func (*Configure_Response) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Configure_Response) GetInstanceId() uint64

  - 
            func (*Configure_Response) ProtoMessage()

  - 
            func (x *Configure_Response) ProtoReflect() protoreflect.Message

  - 
            func (x *Configure_Response) Reset()

  - 
            func (x *Configure_Response) String() string

- 
          type Empty

- 

  - 
            func (*Empty) Descriptor() ([]byte, []int)deprecated

  - 
            func (*Empty) ProtoMessage()

  - 
            func (x *Empty) ProtoReflect() protoreflect.Message

  - 
            func (x *Empty) Reset()

  - 
            func (x *Empty) String() string

- 
          type Get

- 

  - 
            func (*Get) Descriptor() ([]byte, []int)deprecated

  - 
            func (*Get) ProtoMessage()

  - 
            func (x *Get) ProtoReflect() protoreflect.Message

  - 
            func (x *Get) Reset()

  - 
            func (x *Get) String() string

- 
          type Get_MultiRequest

- 

  - 
            func (*Get_MultiRequest) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Get_MultiRequest) GetRequests() []*Get_Request

  - 
            func (*Get_MultiRequest) ProtoMessage()

  - 
            func (x *Get_MultiRequest) ProtoReflect() protoreflect.Message

  - 
            func (x *Get_MultiRequest) Reset()

  - 
            func (x *Get_MultiRequest) String() string

- 
          type Get_MultiResponse

- 

  - 
            func (*Get_MultiResponse) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Get_MultiResponse) GetResponses() []*Get_Response

  - 
            func (*Get_MultiResponse) ProtoMessage()

  - 
            func (x *Get_MultiResponse) ProtoReflect() protoreflect.Message

  - 
            func (x *Get_MultiResponse) Reset()

  - 
            func (x *Get_MultiResponse) String() string

- 
          type Get_Request

- 

  - 
            func (*Get_Request) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Get_Request) GetContext() map[string]*Value

  - 
            func (x *Get_Request) GetExecDeadline() uint64

  - 
            func (x *Get_Request) GetExecId() uint64

  - 
            func (x *Get_Request) GetInstanceId() uint64

  - 
            func (x *Get_Request) GetKeyId() uint64

  - 
            func (x *Get_Request) GetKeys() []*Get_Request_Key

  - 
            func (*Get_Request) ProtoMessage()

  - 
            func (x *Get_Request) ProtoReflect() protoreflect.Message

  - 
            func (x *Get_Request) Reset()

  - 
            func (x *Get_Request) String() string

- 
          type Get_Request_Key

- 

  - 
            func (*Get_Request_Key) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Get_Request_Key) GetArgs() []*Value

  - 
            func (x *Get_Request_Key) GetCall() bool

  - 
            func (x *Get_Request_Key) GetKey() string

  - 
            func (*Get_Request_Key) ProtoMessage()

  - 
            func (x *Get_Request_Key) ProtoReflect() protoreflect.Message

  - 
            func (x *Get_Request_Key) Reset()

  - 
            func (x *Get_Request_Key) String() string

- 
          type Get_Response

- 

  - 
            func (*Get_Response) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Get_Response) GetCallable() bool

  - 
            func (x *Get_Response) GetContext() map[string]*Value

  - 
            func (x *Get_Response) GetInstanceId() uint64

  - 
            func (x *Get_Response) GetKeyId() uint64

  - 
            func (x *Get_Response) GetKeys() []string

  - 
            func (x *Get_Response) GetValue() *Value

  - 
            func (*Get_Response) ProtoMessage()

  - 
            func (x *Get_Response) ProtoReflect() protoreflect.Message

  - 
            func (x *Get_Response) Reset()

  - 
            func (x *Get_Response) String() string

- 
          type PluginClient

- 

  - 
            func NewPluginClient(cc grpc.ClientConnInterface) PluginClient

- 
          type PluginServer

- 
          type UnimplementedPluginServer

- 

  - 
            func (*UnimplementedPluginServer) Close(context.Context, *Close_Request) (*Empty, error)

  - 
            func (*UnimplementedPluginServer) Configure(context.Context, *Configure_Request) (*Configure_Response, error)

  - 
            func (*UnimplementedPluginServer) Get(context.Context, *Get_MultiRequest) (*Get_MultiResponse, error)

- 
          type Value

- 

  - 
            func (*Value) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Value) GetType() Value_Type

  - 
            func (m *Value) GetValue() isValue_Value

  - 
            func (x *Value) GetValueBool() bool

  - 
            func (x *Value) GetValueFloat() float64

  - 
            func (x *Value) GetValueInt() int64

  - 
            func (x *Value) GetValueList() *Value_List

  - 
            func (x *Value) GetValueMap() *Value_Map

  - 
            func (x *Value) GetValueString() string

  - 
            func (*Value) ProtoMessage()

  - 
            func (x *Value) ProtoReflect() protoreflect.Message

  - 
            func (x *Value) Reset()

  - 
            func (x *Value) String() string

- 
          type Value_KV

- 

  - 
            func (*Value_KV) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Value_KV) GetKey() *Value

  - 
            func (x *Value_KV) GetValue() *Value

  - 
            func (*Value_KV) ProtoMessage()

  - 
            func (x *Value_KV) ProtoReflect() protoreflect.Message

  - 
            func (x *Value_KV) Reset()

  - 
            func (x *Value_KV) String() string

- 
          type Value_List

- 

  - 
            func (*Value_List) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Value_List) GetElems() []*Value

  - 
            func (*Value_List) ProtoMessage()

  - 
            func (x *Value_List) ProtoReflect() protoreflect.Message

  - 
            func (x *Value_List) Reset()

  - 
            func (x *Value_List) String() string

- 
          type Value_Map

- 

  - 
            func (*Value_Map) Descriptor() ([]byte, []int)deprecated

  - 
            func (x *Value_Map) GetElems() []*Value_KV

  - 
            func (*Value_Map) ProtoMessage()

  - 
            func (x *Value_Map) ProtoReflect() protoreflect.Message

  - 
            func (x *Value_Map) Reset()

  - 
            func (x *Value_Map) String() string

- 
          type Value_Type

- 

  - 
            func (Value_Type) Descriptor() protoreflect.EnumDescriptor

  - 
            func (x Value_Type) Enum() *Value_Type

  - 
            func (Value_Type) EnumDescriptor() ([]byte, []int)deprecated

  - 
            func (x Value_Type) Number() protoreflect.EnumNumber

  - 
            func (x Value_Type) String() string

  - 
            func (Value_Type) Type() protoreflect.EnumType

- 
          type Value_ValueBool

- 
          type Value_ValueFloat

- 
          type Value_ValueInt

- 
          type Value_ValueList

- 
          type Value_ValueMap

- 
          type Value_ValueString

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var (
	Value_Type_name = map[int32]string{
		0: "INVALID",
		1: "UNDEFINED",
		2: "NULL",
		3: "BOOL",
		4: "INT",
		5: "FLOAT",
		6: "STRING",
		7: "LIST",
		8: "MAP",
	}
	Value_Type_value = map[string]int32{
		"INVALID":   0,
		"UNDEFINED": 1,
		"NULL":      2,
		"BOOL":      3,
		"INT":       4,
		"FLOAT":     5,
		"STRING":    6,
		"LIST":      7,
		"MAP":       8,
	}
)
```

    
  

Enum value maps for Value_Type.

    
      View Source
      

```
var File_plugin_proto protoreflect.FileDescriptor
```

    
  

  
### Functions ¶

  
	  
  
  
    
#### 
      func RegisterPluginServer ¶
  
    
      added in
      v0.4.0
    
  

    
    
      

```
func RegisterPluginServer(s *grpc.Server, srv PluginServer)
```