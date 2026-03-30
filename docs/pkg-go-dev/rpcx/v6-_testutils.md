### Overview ¶

Package client is a generated protocol buffer package.

It is generated from these files:

```
arith_service.proto

```

It has these top-level messages:

```
ProtoArgs
ProtoReply

```

    
### Index ¶

- Variables

- 
          type ProtoArgs

- 

  - 
            func (*ProtoArgs) Descriptor() ([]byte, []int)

  - 
            func (m *ProtoArgs) GetA() int32

  - 
            func (m *ProtoArgs) GetB() int32

  - 
            func (m *ProtoArgs) Marshal() (dAtA []byte, err error)

  - 
            func (m *ProtoArgs) MarshalTo(dAtA []byte) (int, error)

  - 
            func (*ProtoArgs) ProtoMessage()

  - 
            func (m *ProtoArgs) Reset()

  - 
            func (m *ProtoArgs) Size() (n int)

  - 
            func (m *ProtoArgs) String() string

  - 
            func (m *ProtoArgs) Unmarshal(dAtA []byte) error

- 
          type ProtoReply

- 

  - 
            func (*ProtoReply) Descriptor() ([]byte, []int)

  - 
            func (m *ProtoReply) GetC() int32

  - 
            func (m *ProtoReply) Marshal() (dAtA []byte, err error)

  - 
            func (m *ProtoReply) MarshalTo(dAtA []byte) (int, error)

  - 
            func (*ProtoReply) ProtoMessage()

  - 
            func (m *ProtoReply) Reset()

  - 
            func (m *ProtoReply) Size() (n int)

  - 
            func (m *ProtoReply) String() string

  - 
            func (m *ProtoReply) Unmarshal(dAtA []byte) error

- 
          type ThriftArgs_

- 

  - 
            func NewThriftArgs_() *ThriftArgs_

- 

  - 
            func (p *ThriftArgs_) GetA() int32

  - 
            func (p *ThriftArgs_) GetB() int32

  - 
            func (p *ThriftArgs_) Read(iprot thrift.TProtocol) error

  - 
            func (p *ThriftArgs_) ReadField1(iprot thrift.TProtocol) error

  - 
            func (p *ThriftArgs_) ReadField2(iprot thrift.TProtocol) error

  - 
            func (p *ThriftArgs_) String() string

  - 
            func (p *ThriftArgs_) Write(oprot thrift.TProtocol) error

- 
          type ThriftReply

- 

  - 
            func NewThriftReply() *ThriftReply

- 

  - 
            func (p *ThriftReply) GetC() int32

  - 
            func (p *ThriftReply) Read(iprot thrift.TProtocol) error

  - 
            func (p *ThriftReply) ReadField1(iprot thrift.TProtocol) error

  - 
            func (p *ThriftReply) String() string

  - 
            func (p *ThriftReply) Write(oprot thrift.TProtocol) error

### Constants ¶

  

This section is empty.

  
### Variables ¶

  
    
      View Source
      

```
var (
	ErrInvalidLengthArithService = fmt.Errorf("proto: negative length found during unmarshaling")
	ErrIntOverflowArithService   = fmt.Errorf("proto: integer overflow")
)
```

    
  

    
      View Source
      

```
var GoUnusedProtection__ int
```

    
  

  
### Functions ¶

  

This section is empty.

  
### Types ¶

  
      
  
  
    
#### 
      type ProtoArgs ¶
  
    
  

    
    
      

```
type ProtoArgs struct {
	A int32 `protobuf:"varint,1,opt,name=A,proto3" json:"A,omitempty"`
	B int32 `protobuf:"varint,2,opt,name=B,proto3" json:"B,omitempty"`
}
```

    
  

    
  
  
    
#### 
      func (*ProtoArgs) Descriptor ¶
  
    
  

    
    
      

```
func (*ProtoArgs) Descriptor() ([]byte, []int)
```