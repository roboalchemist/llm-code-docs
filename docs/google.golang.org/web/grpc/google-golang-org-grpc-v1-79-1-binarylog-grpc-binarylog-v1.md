# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1

Title: grpc_binarylog_v1 package - google.golang.org/grpc/binarylog/grpc_binarylog_v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1

Markdown Content:
*   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#pkg-variables)
*   [type Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address)
*       *   [func (*Address) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.Descriptor)deprecated
    *   [func (x *Address) GetAddress() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.GetAddress)
    *   [func (x *Address) GetIpPort() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.GetIpPort)
    *   [func (x *Address) GetType() Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.GetType)
    *   [func (*Address) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.ProtoMessage)
    *   [func (x *Address) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.ProtoReflect)
    *   [func (x *Address) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.Reset)
    *   [func (x *Address) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address.String)

*   [type Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type)
*       *   [func (Address_Type) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type.Descriptor)
    *   [func (x Address_Type) Enum() *Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type.Enum)
    *   [func (Address_Type) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type.EnumDescriptor)deprecated
    *   [func (x Address_Type) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type.Number)
    *   [func (x Address_Type) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type.String)
    *   [func (Address_Type) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type.Type)

*   [type ClientHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader)
*       *   [func (*ClientHeader) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.Descriptor)deprecated
    *   [func (x *ClientHeader) GetAuthority() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.GetAuthority)
    *   [func (x *ClientHeader) GetMetadata() *Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.GetMetadata)
    *   [func (x *ClientHeader) GetMethodName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.GetMethodName)
    *   [func (x *ClientHeader) GetTimeout() *durationpb.Duration](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.GetTimeout)
    *   [func (*ClientHeader) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.ProtoMessage)
    *   [func (x *ClientHeader) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.ProtoReflect)
    *   [func (x *ClientHeader) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.Reset)
    *   [func (x *ClientHeader) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader.String)

*   [type GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)
*       *   [func (*GrpcLogEntry) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.Descriptor)deprecated
    *   [func (x *GrpcLogEntry) GetCallId() uint64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetCallId)
    *   [func (x *GrpcLogEntry) GetClientHeader() *ClientHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetClientHeader)
    *   [func (x *GrpcLogEntry) GetLogger() GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetLogger)
    *   [func (x *GrpcLogEntry) GetMessage() *Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetMessage)
    *   [func (x *GrpcLogEntry) GetPayload() isGrpcLogEntry_Payload](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetPayload)
    *   [func (x *GrpcLogEntry) GetPayloadTruncated() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetPayloadTruncated)
    *   [func (x *GrpcLogEntry) GetPeer() *Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetPeer)
    *   [func (x *GrpcLogEntry) GetSequenceIdWithinCall() uint64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetSequenceIdWithinCall)
    *   [func (x *GrpcLogEntry) GetServerHeader() *ServerHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetServerHeader)
    *   [func (x *GrpcLogEntry) GetTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetTimestamp)
    *   [func (x *GrpcLogEntry) GetTrailer() *Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetTrailer)
    *   [func (x *GrpcLogEntry) GetType() GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.GetType)
    *   [func (*GrpcLogEntry) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.ProtoMessage)
    *   [func (x *GrpcLogEntry) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.ProtoReflect)
    *   [func (x *GrpcLogEntry) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.Reset)
    *   [func (x *GrpcLogEntry) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry.String)

*   [type GrpcLogEntry_ClientHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_ClientHeader)
*   [type GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType)
*       *   [func (GrpcLogEntry_EventType) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType.Descriptor)
    *   [func (x GrpcLogEntry_EventType) Enum() *GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType.Enum)
    *   [func (GrpcLogEntry_EventType) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType.EnumDescriptor)deprecated
    *   [func (x GrpcLogEntry_EventType) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType.Number)
    *   [func (x GrpcLogEntry_EventType) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType.String)
    *   [func (GrpcLogEntry_EventType) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType.Type)

*   [type GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger)
*       *   [func (GrpcLogEntry_Logger) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger.Descriptor)
    *   [func (x GrpcLogEntry_Logger) Enum() *GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger.Enum)
    *   [func (GrpcLogEntry_Logger) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger.EnumDescriptor)deprecated
    *   [func (x GrpcLogEntry_Logger) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger.Number)
    *   [func (x GrpcLogEntry_Logger) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger.String)
    *   [func (GrpcLogEntry_Logger) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger.Type)

*   [type GrpcLogEntry_Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Message)
*   [type GrpcLogEntry_ServerHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_ServerHeader)
*   [type GrpcLogEntry_Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Trailer)
*   [type Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message)
*       *   [func (*Message) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message.Descriptor)deprecated
    *   [func (x *Message) GetData() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message.GetData)
    *   [func (x *Message) GetLength() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message.GetLength)
    *   [func (*Message) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message.ProtoMessage)
    *   [func (x *Message) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message.ProtoReflect)
    *   [func (x *Message) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message.Reset)
    *   [func (x *Message) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message.String)

*   [type Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata)
*       *   [func (*Metadata) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata.Descriptor)deprecated
    *   [func (x *Metadata) GetEntry() []*MetadataEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata.GetEntry)
    *   [func (*Metadata) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata.ProtoMessage)
    *   [func (x *Metadata) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata.ProtoReflect)
    *   [func (x *Metadata) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata.Reset)
    *   [func (x *Metadata) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata.String)

*   [type MetadataEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry)
*       *   [func (*MetadataEntry) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry.Descriptor)deprecated
    *   [func (x *MetadataEntry) GetKey() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry.GetKey)
    *   [func (x *MetadataEntry) GetValue() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry.GetValue)
    *   [func (*MetadataEntry) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry.ProtoMessage)
    *   [func (x *MetadataEntry) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry.ProtoReflect)
    *   [func (x *MetadataEntry) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry.Reset)
    *   [func (x *MetadataEntry) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry.String)

*   [type ServerHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader)
*       *   [func (*ServerHeader) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader.Descriptor)deprecated
    *   [func (x *ServerHeader) GetMetadata() *Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader.GetMetadata)
    *   [func (*ServerHeader) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader.ProtoMessage)
    *   [func (x *ServerHeader) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader.ProtoReflect)
    *   [func (x *ServerHeader) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader.Reset)
    *   [func (x *ServerHeader) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader.String)

*   [type Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer)
*       *   [func (*Trailer) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.Descriptor)deprecated
    *   [func (x *Trailer) GetMetadata() *Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.GetMetadata)
    *   [func (x *Trailer) GetStatusCode() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.GetStatusCode)
    *   [func (x *Trailer) GetStatusDetails() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.GetStatusDetails)
    *   [func (x *Trailer) GetStatusMessage() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.GetStatusMessage)
    *   [func (*Trailer) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.ProtoMessage)
    *   [func (x *Trailer) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.ProtoReflect)
    *   [func (x *Trailer) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.Reset)
    *   [func (x *Trailer) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer.String)

This section is empty.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/binarylog/grpc_binarylog_v1/binarylog.pb.go#L79)

var (
 GrpcLogEntry_EventType_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "EVENT_TYPE_UNKNOWN",
		1: "EVENT_TYPE_CLIENT_HEADER",
		2: "EVENT_TYPE_SERVER_HEADER",
		3: "EVENT_TYPE_CLIENT_MESSAGE",
		4: "EVENT_TYPE_SERVER_MESSAGE",
		5: "EVENT_TYPE_CLIENT_HALF_CLOSE",
		6: "EVENT_TYPE_SERVER_TRAILER",
		7: "EVENT_TYPE_CANCEL",
	}
 GrpcLogEntry_EventType_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"EVENT_TYPE_UNKNOWN":           0,
		"EVENT_TYPE_CLIENT_HEADER":     1,
		"EVENT_TYPE_SERVER_HEADER":     2,
		"EVENT_TYPE_CLIENT_MESSAGE":    3,
		"EVENT_TYPE_SERVER_MESSAGE":    4,
		"EVENT_TYPE_CLIENT_HALF_CLOSE": 5,
		"EVENT_TYPE_SERVER_TRAILER":    6,
		"EVENT_TYPE_CANCEL":            7,
	}
)

Enum value maps for GrpcLogEntry_EventType.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/binarylog/grpc_binarylog_v1/binarylog.pb.go#L139)

var (
 GrpcLogEntry_Logger_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "LOGGER_UNKNOWN",
		1: "LOGGER_CLIENT",
		2: "LOGGER_SERVER",
	}
 GrpcLogEntry_Logger_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"LOGGER_UNKNOWN": 0,
		"LOGGER_CLIENT":  1,
		"LOGGER_SERVER":  2,
	}
)

Enum value maps for GrpcLogEntry_Logger.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/binarylog/grpc_binarylog_v1/binarylog.pb.go#L193)

var (
 Address_Type_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "TYPE_UNKNOWN",
		1: "TYPE_IPV4",
		2: "TYPE_IPV6",
		3: "TYPE_UNIX",
	}
 Address_Type_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"TYPE_UNKNOWN": 0,
		"TYPE_IPV4":    1,
		"TYPE_IPV6":    2,
		"TYPE_UNIX":    3,
	}
)

Enum value maps for Address_Type.

This section is empty.

type Address struct {
 Type [Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type) `protobuf:"varint,1,opt,name=type,proto3,enum=grpc.binarylog.v1.Address_Type" json:"type,omitempty"`  Address [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=address,proto3" json:"address,omitempty"` 	IpPort [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,3,opt,name=ip_port,json=ipPort,proto3" json:"ip_port,omitempty"`
	
}

Address information

Deprecated: Use Address.ProtoReflect.Descriptor instead.

func (x *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address)) GetType() [Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type)

func (*[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address)) ProtoMessage()

func (x *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address)) Reset()

const (
 Address_TYPE_UNKNOWN [Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type) = 0 	Address_TYPE_IPV4 [Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type) = 1
	
	Address_TYPE_IPV6 [Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type) = 2
	Address_TYPE_UNIX [Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type) = 3
)

func (x [Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type)) Enum() *[Address_Type](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address_Type)

Deprecated: Use Address_Type.Descriptor instead.

type ClientHeader struct {

	Metadata *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata) `protobuf:"bytes,1,opt,name=metadata,proto3" json:"metadata,omitempty"`
	
	
	MethodName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=method_name,json=methodName,proto3" json:"method_name,omitempty"`
	
	
	
	
	Authority [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=authority,proto3" json:"authority,omitempty"`
	Timeout *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration) `protobuf:"bytes,4,opt,name=timeout,proto3" json:"timeout,omitempty"`
	
}

Deprecated: Use ClientHeader.ProtoReflect.Descriptor instead.

func (x *[ClientHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader)) GetMetadata() *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata)

func (*[ClientHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader)) ProtoMessage()

func (x *[ClientHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader)) Reset()

type GrpcLogEntry struct {

	Timestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `protobuf:"bytes,1,opt,name=timestamp,proto3" json:"timestamp,omitempty"`
	
	
	
	
	CallId [uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,2,opt,name=call_id,json=callId,proto3" json:"call_id,omitempty"`
	
	
	
	
 SequenceIdWithinCall [uint64](https://pkg.go.dev/builtin#uint64) ``  Type [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) `protobuf:"varint,4,opt,name=type,proto3,enum=grpc.binarylog.v1.GrpcLogEntry_EventType" json:"type,omitempty"`  Logger [GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger) `protobuf:"varint,5,opt,name=logger,proto3,enum=grpc.binarylog.v1.GrpcLogEntry_Logger" json:"logger,omitempty"` 	
	
	
	
	
	
	
	
	Payload isGrpcLogEntry_Payload `protobuf_oneof:"payload"`
	PayloadTruncated [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,10,opt,name=payload_truncated,json=payloadTruncated,proto3" json:"payload_truncated,omitempty"`
	
	
	
	
	Peer *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address) `protobuf:"bytes,11,opt,name=peer,proto3" json:"peer,omitempty"`
	
}

Log entry we store in binary logs

Deprecated: Use GrpcLogEntry.ProtoReflect.Descriptor instead.

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetClientHeader() *[ClientHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ClientHeader)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetLogger() [GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetMessage() *[Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetPayload() isGrpcLogEntry_Payload

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetPayloadTruncated() [bool](https://pkg.go.dev/builtin#bool)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetPeer() *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Address)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetSequenceIdWithinCall() [uint64](https://pkg.go.dev/builtin#uint64)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetServerHeader() *[ServerHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetTrailer() *[Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer)

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) GetType() [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType)

func (*[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) ProtoMessage()

func (x *[GrpcLogEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry)) Reset()

type GrpcLogEntry_ClientHeader struct {
}

type GrpcLogEntry_EventType [int32](https://pkg.go.dev/builtin#int32)

Enumerates the type of event Note the terminology is different from the RPC semantics definition, but the same meaning is expressed here.

const (
 GrpcLogEntry_EVENT_TYPE_UNKNOWN [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 0 	GrpcLogEntry_EVENT_TYPE_CLIENT_HEADER [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 1
	GrpcLogEntry_EVENT_TYPE_SERVER_HEADER [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 2
	GrpcLogEntry_EVENT_TYPE_CLIENT_MESSAGE [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 3
	GrpcLogEntry_EVENT_TYPE_SERVER_MESSAGE [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 4
	GrpcLogEntry_EVENT_TYPE_CLIENT_HALF_CLOSE [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 5
	
	
	
	
	
	
	GrpcLogEntry_EVENT_TYPE_SERVER_TRAILER [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 6
	
	
	
	
	
	GrpcLogEntry_EVENT_TYPE_CANCEL [GrpcLogEntry_EventType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_EventType) = 7
)

Deprecated: Use GrpcLogEntry_EventType.Descriptor instead.

type GrpcLogEntry_Logger [int32](https://pkg.go.dev/builtin#int32)

Enumerates the entity that generates the log entry

const (
 GrpcLogEntry_LOGGER_UNKNOWN [GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger) = 0  GrpcLogEntry_LOGGER_CLIENT [GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger) = 1  GrpcLogEntry_LOGGER_SERVER [GrpcLogEntry_Logger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#GrpcLogEntry_Logger) = 2 )

Deprecated: Use GrpcLogEntry_Logger.Descriptor instead.

type GrpcLogEntry_Message struct {
	Message *[Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message) `protobuf:"bytes,8,opt,name=message,proto3,oneof"`
}

type GrpcLogEntry_ServerHeader struct {
}

type GrpcLogEntry_Trailer struct {
 Trailer *[Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer) `protobuf:"bytes,9,opt,name=trailer,proto3,oneof"` }

type Message struct {

	
	Length [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,1,opt,name=length,proto3" json:"length,omitempty"`
	Data [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	
}

Message payload, used by CLIENT_MESSAGE and SERVER_MESSAGE

Deprecated: Use Message.ProtoReflect.Descriptor instead.

func (x *[Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message)) GetData() [][byte](https://pkg.go.dev/builtin#byte)

func (*[Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message)) ProtoMessage()

func (x *[Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Message)) Reset()

type Metadata struct {
 Entry []*[MetadataEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry) `protobuf:"bytes,1,rep,name=entry,proto3" json:"entry,omitempty"` 	
}

A list of metadata pairs, used in the payload of client header, server header, and server trailer. Implementations may omit some entries to honor the header limits of GRPC_BINARY_LOG_CONFIG.

Header keys added by gRPC are omitted. To be more specific, implementations will not log the following entries, and this is not to be treated as a truncation:

*   entries handled by grpc that are not user visible, such as those that begin with 'grpc-' (with exception of grpc-trace-bin) or keys like 'lb-token'
*   transport specific entries, including but not limited to: ':path', ':authority', 'content-encoding', 'user-agent', 'te', etc
*   entries added for call credentials

Implementations must always log grpc-trace-bin if it is present. Practically speaking it will only be visible on server side because grpc-trace-bin is managed by low level client side mechanisms inaccessible from the application level. On server side, the header is just a normal metadata key. The pair will not count towards the size limit.

Deprecated: Use Metadata.ProtoReflect.Descriptor instead.

func (x *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata)) GetEntry() []*[MetadataEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry)

func (*[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata)) ProtoMessage()

func (x *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata)) Reset()

type MetadataEntry struct {
 Key [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=key,proto3" json:"key,omitempty"`  Value [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"` 	
}

A metadata key value pair

Deprecated: Use MetadataEntry.ProtoReflect.Descriptor instead.

func (x *[MetadataEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry)) GetValue() [][byte](https://pkg.go.dev/builtin#byte)

func (*[MetadataEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry)) ProtoMessage()

func (x *[MetadataEntry](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#MetadataEntry)) Reset()

type ServerHeader struct {

	Metadata *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata) `protobuf:"bytes,1,opt,name=metadata,proto3" json:"metadata,omitempty"`
	
}

Deprecated: Use ServerHeader.ProtoReflect.Descriptor instead.

func (x *[ServerHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader)) GetMetadata() *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata)

func (*[ServerHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader)) ProtoMessage()

func (x *[ServerHeader](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#ServerHeader)) Reset()

type Trailer struct {

	Metadata *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata) `protobuf:"bytes,1,opt,name=metadata,proto3" json:"metadata,omitempty"`
	StatusCode [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,2,opt,name=status_code,json=statusCode,proto3" json:"status_code,omitempty"`
	
	StatusMessage [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=status_message,json=statusMessage,proto3" json:"status_message,omitempty"`
	
	StatusDetails [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,4,opt,name=status_details,json=statusDetails,proto3" json:"status_details,omitempty"`
	
}

Deprecated: Use Trailer.ProtoReflect.Descriptor instead.

func (x *[Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer)) GetMetadata() *[Metadata](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Metadata)

func (x *[Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer)) GetStatusDetails() [][byte](https://pkg.go.dev/builtin#byte)

func (x *[Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer)) GetStatusMessage() [string](https://pkg.go.dev/builtin#string)

func (*[Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer)) ProtoMessage()

func (x *[Trailer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/binarylog/grpc_binarylog_v1#Trailer)) Reset()
