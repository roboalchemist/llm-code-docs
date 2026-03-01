# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1

Title: grpc_channelz_v1 package - google.golang.org/grpc/channelz/grpc_channelz_v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1

Markdown Content:
*   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#pkg-constants)
*   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#pkg-variables)
*   [func RegisterChannelzServer(s grpc.ServiceRegistrar, srv ChannelzServer)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#RegisterChannelzServer)
*   [type Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)
*       *   [func (*Address) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.Descriptor)deprecated
    *   [func (x *Address) GetAddress() isAddress_Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.GetAddress)
    *   [func (x *Address) GetOtherAddress() *Address_OtherAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.GetOtherAddress)
    *   [func (x *Address) GetTcpipAddress() *Address_TcpIpAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.GetTcpipAddress)
    *   [func (x *Address) GetUdsAddress() *Address_UdsAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.GetUdsAddress)
    *   [func (*Address) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.ProtoMessage)
    *   [func (x *Address) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.ProtoReflect)
    *   [func (x *Address) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.Reset)
    *   [func (x *Address) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address.String)

*   [type Address_OtherAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress)
*       *   [func (*Address_OtherAddress) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress.Descriptor)deprecated
    *   [func (x *Address_OtherAddress) GetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress.GetName)
    *   [func (x *Address_OtherAddress) GetValue() *anypb.Any](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress.GetValue)
    *   [func (*Address_OtherAddress) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress.ProtoMessage)
    *   [func (x *Address_OtherAddress) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress.ProtoReflect)
    *   [func (x *Address_OtherAddress) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress.Reset)
    *   [func (x *Address_OtherAddress) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress.String)

*   [type Address_OtherAddress_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress_)
*   [type Address_TcpIpAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress)
*       *   [func (*Address_TcpIpAddress) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress.Descriptor)deprecated
    *   [func (x *Address_TcpIpAddress) GetIpAddress() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress.GetIpAddress)
    *   [func (x *Address_TcpIpAddress) GetPort() int32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress.GetPort)
    *   [func (*Address_TcpIpAddress) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress.ProtoMessage)
    *   [func (x *Address_TcpIpAddress) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress.ProtoReflect)
    *   [func (x *Address_TcpIpAddress) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress.Reset)
    *   [func (x *Address_TcpIpAddress) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress.String)

*   [type Address_TcpipAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpipAddress)
*   [type Address_UdsAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress)
*       *   [func (*Address_UdsAddress) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress.Descriptor)deprecated
    *   [func (x *Address_UdsAddress) GetFilename() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress.GetFilename)
    *   [func (*Address_UdsAddress) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress.ProtoMessage)
    *   [func (x *Address_UdsAddress) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress.ProtoReflect)
    *   [func (x *Address_UdsAddress) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress.Reset)
    *   [func (x *Address_UdsAddress) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress.String)

*   [type Address_UdsAddress_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress_)
*   [type Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)
*       *   [func (*Channel) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.Descriptor)deprecated
    *   [func (x *Channel) GetChannelRef() []*ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.GetChannelRef)
    *   [func (x *Channel) GetData() *ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.GetData)
    *   [func (x *Channel) GetRef() *ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.GetRef)
    *   [func (x *Channel) GetSocketRef() []*SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.GetSocketRef)
    *   [func (x *Channel) GetSubchannelRef() []*SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.GetSubchannelRef)
    *   [func (*Channel) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.ProtoMessage)
    *   [func (x *Channel) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.ProtoReflect)
    *   [func (x *Channel) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.Reset)
    *   [func (x *Channel) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel.String)

*   [type ChannelConnectivityState](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState)
*       *   [func (*ChannelConnectivityState) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState.Descriptor)deprecated
    *   [func (x *ChannelConnectivityState) GetState() ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState.GetState)
    *   [func (*ChannelConnectivityState) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState.ProtoMessage)
    *   [func (x *ChannelConnectivityState) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState.ProtoReflect)
    *   [func (x *ChannelConnectivityState) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState.Reset)
    *   [func (x *ChannelConnectivityState) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState.String)

*   [type ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State)
*       *   [func (ChannelConnectivityState_State) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State.Descriptor)
    *   [func (x ChannelConnectivityState_State) Enum() *ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State.Enum)
    *   [func (ChannelConnectivityState_State) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State.EnumDescriptor)deprecated
    *   [func (x ChannelConnectivityState_State) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State.Number)
    *   [func (x ChannelConnectivityState_State) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State.String)
    *   [func (ChannelConnectivityState_State) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State.Type)

*   [type ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)
*       *   [func (*ChannelData) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.Descriptor)deprecated
    *   [func (x *ChannelData) GetCallsFailed() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.GetCallsFailed)
    *   [func (x *ChannelData) GetCallsStarted() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.GetCallsStarted)
    *   [func (x *ChannelData) GetCallsSucceeded() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.GetCallsSucceeded)
    *   [func (x *ChannelData) GetLastCallStartedTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.GetLastCallStartedTimestamp)
    *   [func (x *ChannelData) GetState() *ChannelConnectivityState](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.GetState)
    *   [func (x *ChannelData) GetTarget() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.GetTarget)
    *   [func (x *ChannelData) GetTrace() *ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.GetTrace)
    *   [func (*ChannelData) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.ProtoMessage)
    *   [func (x *ChannelData) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.ProtoReflect)
    *   [func (x *ChannelData) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.Reset)
    *   [func (x *ChannelData) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData.String)

*   [type ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)
*       *   [func (*ChannelRef) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef.Descriptor)deprecated
    *   [func (x *ChannelRef) GetChannelId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef.GetChannelId)
    *   [func (x *ChannelRef) GetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef.GetName)
    *   [func (*ChannelRef) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef.ProtoMessage)
    *   [func (x *ChannelRef) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef.ProtoReflect)
    *   [func (x *ChannelRef) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef.Reset)
    *   [func (x *ChannelRef) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef.String)

*   [type ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace)
*       *   [func (*ChannelTrace) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.Descriptor)deprecated
    *   [func (x *ChannelTrace) GetCreationTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.GetCreationTimestamp)
    *   [func (x *ChannelTrace) GetEvents() []*ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.GetEvents)
    *   [func (x *ChannelTrace) GetNumEventsLogged() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.GetNumEventsLogged)
    *   [func (*ChannelTrace) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.ProtoMessage)
    *   [func (x *ChannelTrace) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.ProtoReflect)
    *   [func (x *ChannelTrace) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.Reset)
    *   [func (x *ChannelTrace) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace.String)

*   [type ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)
*       *   [func (*ChannelTraceEvent) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.Descriptor)deprecated
    *   [func (x *ChannelTraceEvent) GetChannelRef() *ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.GetChannelRef)
    *   [func (x *ChannelTraceEvent) GetChildRef() isChannelTraceEvent_ChildRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.GetChildRef)
    *   [func (x *ChannelTraceEvent) GetDescription() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.GetDescription)
    *   [func (x *ChannelTraceEvent) GetSeverity() ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.GetSeverity)
    *   [func (x *ChannelTraceEvent) GetSubchannelRef() *SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.GetSubchannelRef)
    *   [func (x *ChannelTraceEvent) GetTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.GetTimestamp)
    *   [func (*ChannelTraceEvent) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.ProtoMessage)
    *   [func (x *ChannelTraceEvent) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.ProtoReflect)
    *   [func (x *ChannelTraceEvent) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.Reset)
    *   [func (x *ChannelTraceEvent) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent.String)

*   [type ChannelTraceEvent_ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_ChannelRef)
*   [type ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity)
*       *   [func (ChannelTraceEvent_Severity) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity.Descriptor)
    *   [func (x ChannelTraceEvent_Severity) Enum() *ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity.Enum)
    *   [func (ChannelTraceEvent_Severity) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity.EnumDescriptor)deprecated
    *   [func (x ChannelTraceEvent_Severity) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity.Number)
    *   [func (x ChannelTraceEvent_Severity) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity.String)
    *   [func (ChannelTraceEvent_Severity) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity.Type)

*   [type ChannelTraceEvent_SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_SubchannelRef)
*   [type ChannelzClient](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelzClient)
*       *   [func NewChannelzClient(cc grpc.ClientConnInterface) ChannelzClient](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#NewChannelzClient)

*   [type ChannelzServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelzServer)
*   [type GetChannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest)
*       *   [func (*GetChannelRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest.Descriptor)deprecated
    *   [func (x *GetChannelRequest) GetChannelId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest.GetChannelId)
    *   [func (*GetChannelRequest) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest.ProtoMessage)
    *   [func (x *GetChannelRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest.ProtoReflect)
    *   [func (x *GetChannelRequest) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest.Reset)
    *   [func (x *GetChannelRequest) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest.String)

*   [type GetChannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse)
*       *   [func (*GetChannelResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse.Descriptor)deprecated
    *   [func (x *GetChannelResponse) GetChannel() *Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse.GetChannel)
    *   [func (*GetChannelResponse) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse.ProtoMessage)
    *   [func (x *GetChannelResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse.ProtoReflect)
    *   [func (x *GetChannelResponse) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse.Reset)
    *   [func (x *GetChannelResponse) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse.String)

*   [type GetServerRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest)
*       *   [func (*GetServerRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest.Descriptor)deprecated
    *   [func (x *GetServerRequest) GetServerId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest.GetServerId)
    *   [func (*GetServerRequest) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest.ProtoMessage)
    *   [func (x *GetServerRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest.ProtoReflect)
    *   [func (x *GetServerRequest) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest.Reset)
    *   [func (x *GetServerRequest) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest.String)

*   [type GetServerResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse)
*       *   [func (*GetServerResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse.Descriptor)deprecated
    *   [func (x *GetServerResponse) GetServer() *Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse.GetServer)
    *   [func (*GetServerResponse) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse.ProtoMessage)
    *   [func (x *GetServerResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse.ProtoReflect)
    *   [func (x *GetServerResponse) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse.Reset)
    *   [func (x *GetServerResponse) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse.String)

*   [type GetServerSocketsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest)
*       *   [func (*GetServerSocketsRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.Descriptor)deprecated
    *   [func (x *GetServerSocketsRequest) GetMaxResults() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.GetMaxResults)
    *   [func (x *GetServerSocketsRequest) GetServerId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.GetServerId)
    *   [func (x *GetServerSocketsRequest) GetStartSocketId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.GetStartSocketId)
    *   [func (*GetServerSocketsRequest) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.ProtoMessage)
    *   [func (x *GetServerSocketsRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.ProtoReflect)
    *   [func (x *GetServerSocketsRequest) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.Reset)
    *   [func (x *GetServerSocketsRequest) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest.String)

*   [type GetServerSocketsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse)
*       *   [func (*GetServerSocketsResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse.Descriptor)deprecated
    *   [func (x *GetServerSocketsResponse) GetEnd() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse.GetEnd)
    *   [func (x *GetServerSocketsResponse) GetSocketRef() []*SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse.GetSocketRef)
    *   [func (*GetServerSocketsResponse) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse.ProtoMessage)
    *   [func (x *GetServerSocketsResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse.ProtoReflect)
    *   [func (x *GetServerSocketsResponse) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse.Reset)
    *   [func (x *GetServerSocketsResponse) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse.String)

*   [type GetServersRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest)
*       *   [func (*GetServersRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest.Descriptor)deprecated
    *   [func (x *GetServersRequest) GetMaxResults() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest.GetMaxResults)
    *   [func (x *GetServersRequest) GetStartServerId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest.GetStartServerId)
    *   [func (*GetServersRequest) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest.ProtoMessage)
    *   [func (x *GetServersRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest.ProtoReflect)
    *   [func (x *GetServersRequest) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest.Reset)
    *   [func (x *GetServersRequest) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest.String)

*   [type GetServersResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse)
*       *   [func (*GetServersResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse.Descriptor)deprecated
    *   [func (x *GetServersResponse) GetEnd() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse.GetEnd)
    *   [func (x *GetServersResponse) GetServer() []*Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse.GetServer)
    *   [func (*GetServersResponse) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse.ProtoMessage)
    *   [func (x *GetServersResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse.ProtoReflect)
    *   [func (x *GetServersResponse) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse.Reset)
    *   [func (x *GetServersResponse) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse.String)

*   [type GetSocketRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest)
*       *   [func (*GetSocketRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest.Descriptor)deprecated
    *   [func (x *GetSocketRequest) GetSocketId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest.GetSocketId)
    *   [func (x *GetSocketRequest) GetSummary() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest.GetSummary)
    *   [func (*GetSocketRequest) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest.ProtoMessage)
    *   [func (x *GetSocketRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest.ProtoReflect)
    *   [func (x *GetSocketRequest) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest.Reset)
    *   [func (x *GetSocketRequest) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest.String)

*   [type GetSocketResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse)
*       *   [func (*GetSocketResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse.Descriptor)deprecated
    *   [func (x *GetSocketResponse) GetSocket() *Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse.GetSocket)
    *   [func (*GetSocketResponse) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse.ProtoMessage)
    *   [func (x *GetSocketResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse.ProtoReflect)
    *   [func (x *GetSocketResponse) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse.Reset)
    *   [func (x *GetSocketResponse) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse.String)

*   [type GetSubchannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest)
*       *   [func (*GetSubchannelRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest.Descriptor)deprecated
    *   [func (x *GetSubchannelRequest) GetSubchannelId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest.GetSubchannelId)
    *   [func (*GetSubchannelRequest) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest.ProtoMessage)
    *   [func (x *GetSubchannelRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest.ProtoReflect)
    *   [func (x *GetSubchannelRequest) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest.Reset)
    *   [func (x *GetSubchannelRequest) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest.String)

*   [type GetSubchannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse)
*       *   [func (*GetSubchannelResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse.Descriptor)deprecated
    *   [func (x *GetSubchannelResponse) GetSubchannel() *Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse.GetSubchannel)
    *   [func (*GetSubchannelResponse) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse.ProtoMessage)
    *   [func (x *GetSubchannelResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse.ProtoReflect)
    *   [func (x *GetSubchannelResponse) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse.Reset)
    *   [func (x *GetSubchannelResponse) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse.String)

*   [type GetTopChannelsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest)
*       *   [func (*GetTopChannelsRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest.Descriptor)deprecated
    *   [func (x *GetTopChannelsRequest) GetMaxResults() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest.GetMaxResults)
    *   [func (x *GetTopChannelsRequest) GetStartChannelId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest.GetStartChannelId)
    *   [func (*GetTopChannelsRequest) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest.ProtoMessage)
    *   [func (x *GetTopChannelsRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest.ProtoReflect)
    *   [func (x *GetTopChannelsRequest) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest.Reset)
    *   [func (x *GetTopChannelsRequest) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest.String)

*   [type GetTopChannelsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse)
*       *   [func (*GetTopChannelsResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse.Descriptor)deprecated
    *   [func (x *GetTopChannelsResponse) GetChannel() []*Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse.GetChannel)
    *   [func (x *GetTopChannelsResponse) GetEnd() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse.GetEnd)
    *   [func (*GetTopChannelsResponse) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse.ProtoMessage)
    *   [func (x *GetTopChannelsResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse.ProtoReflect)
    *   [func (x *GetTopChannelsResponse) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse.Reset)
    *   [func (x *GetTopChannelsResponse) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse.String)

*   [type Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security)
*       *   [func (*Security) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.Descriptor)deprecated
    *   [func (x *Security) GetModel() isSecurity_Model](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.GetModel)
    *   [func (x *Security) GetOther() *Security_OtherSecurity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.GetOther)
    *   [func (x *Security) GetTls() *Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.GetTls)
    *   [func (*Security) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.ProtoMessage)
    *   [func (x *Security) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.ProtoReflect)
    *   [func (x *Security) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.Reset)
    *   [func (x *Security) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security.String)

*   [type Security_Other](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Other)
*   [type Security_OtherSecurity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity)
*       *   [func (*Security_OtherSecurity) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity.Descriptor)deprecated
    *   [func (x *Security_OtherSecurity) GetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity.GetName)
    *   [func (x *Security_OtherSecurity) GetValue() *anypb.Any](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity.GetValue)
    *   [func (*Security_OtherSecurity) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity.ProtoMessage)
    *   [func (x *Security_OtherSecurity) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity.ProtoReflect)
    *   [func (x *Security_OtherSecurity) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity.Reset)
    *   [func (x *Security_OtherSecurity) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity.String)

*   [type Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls)
*       *   [func (*Security_Tls) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.Descriptor)deprecated
    *   [func (x *Security_Tls) GetCipherSuite() isSecurity_Tls_CipherSuite](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.GetCipherSuite)
    *   [func (x *Security_Tls) GetLocalCertificate() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.GetLocalCertificate)
    *   [func (x *Security_Tls) GetOtherName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.GetOtherName)
    *   [func (x *Security_Tls) GetRemoteCertificate() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.GetRemoteCertificate)
    *   [func (x *Security_Tls) GetStandardName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.GetStandardName)
    *   [func (*Security_Tls) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.ProtoMessage)
    *   [func (x *Security_Tls) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.ProtoReflect)
    *   [func (x *Security_Tls) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.Reset)
    *   [func (x *Security_Tls) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls.String)

*   [type Security_Tls_](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls_)
*   [type Security_Tls_OtherName](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls_OtherName)
*   [type Security_Tls_StandardName](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls_StandardName)
*   [type Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server)
*       *   [func (*Server) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.Descriptor)deprecated
    *   [func (x *Server) GetData() *ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.GetData)
    *   [func (x *Server) GetListenSocket() []*SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.GetListenSocket)
    *   [func (x *Server) GetRef() *ServerRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.GetRef)
    *   [func (*Server) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.ProtoMessage)
    *   [func (x *Server) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.ProtoReflect)
    *   [func (x *Server) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.Reset)
    *   [func (x *Server) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server.String)

*   [type ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)
*       *   [func (*ServerData) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.Descriptor)deprecated
    *   [func (x *ServerData) GetCallsFailed() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.GetCallsFailed)
    *   [func (x *ServerData) GetCallsStarted() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.GetCallsStarted)
    *   [func (x *ServerData) GetCallsSucceeded() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.GetCallsSucceeded)
    *   [func (x *ServerData) GetLastCallStartedTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.GetLastCallStartedTimestamp)
    *   [func (x *ServerData) GetTrace() *ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.GetTrace)
    *   [func (*ServerData) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.ProtoMessage)
    *   [func (x *ServerData) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.ProtoReflect)
    *   [func (x *ServerData) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.Reset)
    *   [func (x *ServerData) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData.String)

*   [type ServerRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef)
*       *   [func (*ServerRef) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef.Descriptor)deprecated
    *   [func (x *ServerRef) GetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef.GetName)
    *   [func (x *ServerRef) GetServerId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef.GetServerId)
    *   [func (*ServerRef) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef.ProtoMessage)
    *   [func (x *ServerRef) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef.ProtoReflect)
    *   [func (x *ServerRef) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef.Reset)
    *   [func (x *ServerRef) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef.String)

*   [type Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)
*       *   [func (*Socket) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.Descriptor)deprecated
    *   [func (x *Socket) GetData() *SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.GetData)
    *   [func (x *Socket) GetLocal() *Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.GetLocal)
    *   [func (x *Socket) GetRef() *SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.GetRef)
    *   [func (x *Socket) GetRemote() *Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.GetRemote)
    *   [func (x *Socket) GetRemoteName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.GetRemoteName)
    *   [func (x *Socket) GetSecurity() *Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.GetSecurity)
    *   [func (*Socket) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.ProtoMessage)
    *   [func (x *Socket) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.ProtoReflect)
    *   [func (x *Socket) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.Reset)
    *   [func (x *Socket) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket.String)

*   [type SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)
*       *   [func (*SocketData) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.Descriptor)deprecated
    *   [func (x *SocketData) GetKeepAlivesSent() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetKeepAlivesSent)
    *   [func (x *SocketData) GetLastLocalStreamCreatedTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetLastLocalStreamCreatedTimestamp)
    *   [func (x *SocketData) GetLastMessageReceivedTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetLastMessageReceivedTimestamp)
    *   [func (x *SocketData) GetLastMessageSentTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetLastMessageSentTimestamp)
    *   [func (x *SocketData) GetLastRemoteStreamCreatedTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetLastRemoteStreamCreatedTimestamp)
    *   [func (x *SocketData) GetLocalFlowControlWindow() *wrapperspb.Int64Value](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetLocalFlowControlWindow)
    *   [func (x *SocketData) GetMessagesReceived() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetMessagesReceived)
    *   [func (x *SocketData) GetMessagesSent() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetMessagesSent)
    *   [func (x *SocketData) GetOption() []*SocketOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetOption)
    *   [func (x *SocketData) GetRemoteFlowControlWindow() *wrapperspb.Int64Value](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetRemoteFlowControlWindow)
    *   [func (x *SocketData) GetStreamsFailed() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetStreamsFailed)
    *   [func (x *SocketData) GetStreamsStarted() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetStreamsStarted)
    *   [func (x *SocketData) GetStreamsSucceeded() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.GetStreamsSucceeded)
    *   [func (*SocketData) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.ProtoMessage)
    *   [func (x *SocketData) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.ProtoReflect)
    *   [func (x *SocketData) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.Reset)
    *   [func (x *SocketData) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData.String)

*   [type SocketOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption)
*       *   [func (*SocketOption) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.Descriptor)deprecated
    *   [func (x *SocketOption) GetAdditional() *anypb.Any](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.GetAdditional)
    *   [func (x *SocketOption) GetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.GetName)
    *   [func (x *SocketOption) GetValue() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.GetValue)
    *   [func (*SocketOption) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.ProtoMessage)
    *   [func (x *SocketOption) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.ProtoReflect)
    *   [func (x *SocketOption) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.Reset)
    *   [func (x *SocketOption) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption.String)

*   [type SocketOptionLinger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger)
*       *   [func (*SocketOptionLinger) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger.Descriptor)deprecated
    *   [func (x *SocketOptionLinger) GetActive() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger.GetActive)
    *   [func (x *SocketOptionLinger) GetDuration() *durationpb.Duration](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger.GetDuration)
    *   [func (*SocketOptionLinger) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger.ProtoMessage)
    *   [func (x *SocketOptionLinger) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger.ProtoReflect)
    *   [func (x *SocketOptionLinger) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger.Reset)
    *   [func (x *SocketOptionLinger) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger.String)

*   [type SocketOptionTcpInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo)
*       *   [func (*SocketOptionTcpInfo) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.Descriptor)deprecated
    *   [func (x *SocketOptionTcpInfo) GetTcpiAdvmss() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiAdvmss)
    *   [func (x *SocketOptionTcpInfo) GetTcpiAto() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiAto)
    *   [func (x *SocketOptionTcpInfo) GetTcpiBackoff() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiBackoff)
    *   [func (x *SocketOptionTcpInfo) GetTcpiCaState() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiCaState)
    *   [func (x *SocketOptionTcpInfo) GetTcpiFackets() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiFackets)
    *   [func (x *SocketOptionTcpInfo) GetTcpiLastAckRecv() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiLastAckRecv)
    *   [func (x *SocketOptionTcpInfo) GetTcpiLastAckSent() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiLastAckSent)
    *   [func (x *SocketOptionTcpInfo) GetTcpiLastDataRecv() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiLastDataRecv)
    *   [func (x *SocketOptionTcpInfo) GetTcpiLastDataSent() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiLastDataSent)
    *   [func (x *SocketOptionTcpInfo) GetTcpiLost() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiLost)
    *   [func (x *SocketOptionTcpInfo) GetTcpiOptions() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiOptions)
    *   [func (x *SocketOptionTcpInfo) GetTcpiPmtu() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiPmtu)
    *   [func (x *SocketOptionTcpInfo) GetTcpiProbes() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiProbes)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRcvMss() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRcvMss)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRcvSsthresh() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRcvSsthresh)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRcvWscale() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRcvWscale)
    *   [func (x *SocketOptionTcpInfo) GetTcpiReordering() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiReordering)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRetrans() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRetrans)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRetransmits() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRetransmits)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRto() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRto)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRtt() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRtt)
    *   [func (x *SocketOptionTcpInfo) GetTcpiRttvar() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiRttvar)
    *   [func (x *SocketOptionTcpInfo) GetTcpiSacked() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiSacked)
    *   [func (x *SocketOptionTcpInfo) GetTcpiSndCwnd() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiSndCwnd)
    *   [func (x *SocketOptionTcpInfo) GetTcpiSndMss() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiSndMss)
    *   [func (x *SocketOptionTcpInfo) GetTcpiSndSsthresh() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiSndSsthresh)
    *   [func (x *SocketOptionTcpInfo) GetTcpiSndWscale() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiSndWscale)
    *   [func (x *SocketOptionTcpInfo) GetTcpiState() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiState)
    *   [func (x *SocketOptionTcpInfo) GetTcpiUnacked() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.GetTcpiUnacked)
    *   [func (*SocketOptionTcpInfo) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.ProtoMessage)
    *   [func (x *SocketOptionTcpInfo) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.ProtoReflect)
    *   [func (x *SocketOptionTcpInfo) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.Reset)
    *   [func (x *SocketOptionTcpInfo) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo.String)

*   [type SocketOptionTimeout](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout)
*       *   [func (*SocketOptionTimeout) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout.Descriptor)deprecated
    *   [func (x *SocketOptionTimeout) GetDuration() *durationpb.Duration](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout.GetDuration)
    *   [func (*SocketOptionTimeout) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout.ProtoMessage)
    *   [func (x *SocketOptionTimeout) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout.ProtoReflect)
    *   [func (x *SocketOptionTimeout) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout.Reset)
    *   [func (x *SocketOptionTimeout) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout.String)

*   [type SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)
*       *   [func (*SocketRef) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef.Descriptor)deprecated
    *   [func (x *SocketRef) GetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef.GetName)
    *   [func (x *SocketRef) GetSocketId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef.GetSocketId)
    *   [func (*SocketRef) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef.ProtoMessage)
    *   [func (x *SocketRef) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef.ProtoReflect)
    *   [func (x *SocketRef) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef.Reset)
    *   [func (x *SocketRef) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef.String)

*   [type Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)
*       *   [func (*Subchannel) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.Descriptor)deprecated
    *   [func (x *Subchannel) GetChannelRef() []*ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.GetChannelRef)
    *   [func (x *Subchannel) GetData() *ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.GetData)
    *   [func (x *Subchannel) GetRef() *SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.GetRef)
    *   [func (x *Subchannel) GetSocketRef() []*SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.GetSocketRef)
    *   [func (x *Subchannel) GetSubchannelRef() []*SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.GetSubchannelRef)
    *   [func (*Subchannel) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.ProtoMessage)
    *   [func (x *Subchannel) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.ProtoReflect)
    *   [func (x *Subchannel) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.Reset)
    *   [func (x *Subchannel) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel.String)

*   [type SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)
*       *   [func (*SubchannelRef) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef.Descriptor)deprecated
    *   [func (x *SubchannelRef) GetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef.GetName)
    *   [func (x *SubchannelRef) GetSubchannelId() int64](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef.GetSubchannelId)
    *   [func (*SubchannelRef) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef.ProtoMessage)
    *   [func (x *SubchannelRef) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef.ProtoReflect)
    *   [func (x *SubchannelRef) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef.Reset)
    *   [func (x *SubchannelRef) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef.String)

*   [type UnimplementedChannelzServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer)
*       *   [func (UnimplementedChannelzServer) GetChannel(context.Context, *GetChannelRequest) (*GetChannelResponse, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer.GetChannel)
    *   [func (UnimplementedChannelzServer) GetServer(context.Context, *GetServerRequest) (*GetServerResponse, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer.GetServer)
    *   [func (UnimplementedChannelzServer) GetServerSockets(context.Context, *GetServerSocketsRequest) (*GetServerSocketsResponse, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer.GetServerSockets)
    *   [func (UnimplementedChannelzServer) GetServers(context.Context, *GetServersRequest) (*GetServersResponse, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer.GetServers)
    *   [func (UnimplementedChannelzServer) GetSocket(context.Context, *GetSocketRequest) (*GetSocketResponse, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer.GetSocket)
    *   [func (UnimplementedChannelzServer) GetSubchannel(context.Context, *GetSubchannelRequest) (*GetSubchannelResponse, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer.GetSubchannel)
    *   [func (UnimplementedChannelzServer) GetTopChannels(context.Context, *GetTopChannelsRequest) (*GetTopChannelsResponse, error)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnimplementedChannelzServer.GetTopChannels)

*   [type UnsafeChannelzServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#UnsafeChannelzServer)

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/channelz/grpc_channelz_v1/channelz_grpc.pb.go#L42)

const (
 Channelz_GetTopChannels_FullMethodName = "/grpc.channelz.v1.Channelz/GetTopChannels"  Channelz_GetServers_FullMethodName = "/grpc.channelz.v1.Channelz/GetServers"  Channelz_GetServer_FullMethodName = "/grpc.channelz.v1.Channelz/GetServer"  Channelz_GetServerSockets_FullMethodName = "/grpc.channelz.v1.Channelz/GetServerSockets"  Channelz_GetChannel_FullMethodName = "/grpc.channelz.v1.Channelz/GetChannel"  Channelz_GetSubchannel_FullMethodName = "/grpc.channelz.v1.Channelz/GetSubchannel"  Channelz_GetSocket_FullMethodName = "/grpc.channelz.v1.Channelz/GetSocket" )

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/channelz/grpc_channelz_v1/channelz.pb.go#L61)

var (
 ChannelConnectivityState_State_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "UNKNOWN",
		1: "IDLE",
		2: "CONNECTING",
		3: "READY",
		4: "TRANSIENT_FAILURE",
		5: "SHUTDOWN",
	}
 ChannelConnectivityState_State_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"UNKNOWN":           0,
		"IDLE":              1,
		"CONNECTING":        2,
		"READY":             3,
		"TRANSIENT_FAILURE": 4,
		"SHUTDOWN":          5,
	}
)

Enum value maps for ChannelConnectivityState_State.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/channelz/grpc_channelz_v1/channelz.pb.go#L118)

var (
 ChannelTraceEvent_Severity_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "CT_UNKNOWN",
		1: "CT_INFO",
		2: "CT_WARNING",
		3: "CT_ERROR",
	}
 ChannelTraceEvent_Severity_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"CT_UNKNOWN": 0,
		"CT_INFO":    1,
		"CT_WARNING": 2,
		"CT_ERROR":   3,
	}
)

Enum value maps for ChannelTraceEvent_Severity.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/channelz/grpc_channelz_v1/channelz_grpc.pb.go#L355)

var Channelz_ServiceDesc = [grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[ServiceDesc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#ServiceDesc){ 	ServiceName: "grpc.channelz.v1.Channelz",
	HandlerType: (*[ChannelzServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelzServer))([nil](https://pkg.go.dev/builtin#nil)),
	Methods: [][grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[MethodDesc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#MethodDesc){
		{
			MethodName: "GetTopChannels",
			Handler:    _Channelz_GetTopChannels_Handler,
		},
		{
			MethodName: "GetServers",
			Handler:    _Channelz_GetServers_Handler,
		},
		{
			MethodName: "GetServer",
			Handler:    _Channelz_GetServer_Handler,
		},
		{
			MethodName: "GetServerSockets",
			Handler:    _Channelz_GetServerSockets_Handler,
		},
		{
			MethodName: "GetChannel",
			Handler:    _Channelz_GetChannel_Handler,
		},
		{
			MethodName: "GetSubchannel",
			Handler:    _Channelz_GetSubchannel_Handler,
		},
		{
			MethodName: "GetSocket",
			Handler:    _Channelz_GetSocket_Handler,
		},
	},
	Streams:  [][grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[StreamDesc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#StreamDesc){},
	Metadata: "grpc/channelz/v1/channelz.proto",
}

Channelz_ServiceDesc is the grpc.ServiceDesc for Channelz service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

type Address struct {

	
	
	
	
	Address isAddress_Address `protobuf_oneof:"address"`
	
}

Address represents the address used to create the socket.

Deprecated: Use Address.ProtoReflect.Descriptor instead.

func (x *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)) GetAddress() isAddress_Address

func (x *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)) GetOtherAddress() *[Address_OtherAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress)

func (x *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)) GetTcpipAddress() *[Address_TcpIpAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress)

func (x *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)) GetUdsAddress() *[Address_UdsAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress)

func (*[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)) ProtoMessage()

func (x *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)) Reset()

type Address_OtherAddress struct {

	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Value *[anypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb).[Any](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb#Any) `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
	
}

An address type not included above.

Deprecated: Use Address_OtherAddress.ProtoReflect.Descriptor instead.

func (*[Address_OtherAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress)) ProtoMessage()

func (x *[Address_OtherAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress)) Reset()

type Address_OtherAddress_ struct {
 OtherAddress *[Address_OtherAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_OtherAddress) `protobuf:"bytes,3,opt,name=other_address,json=otherAddress,proto3,oneof"` }

type Address_TcpIpAddress struct {

	
	IpAddress [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,1,opt,name=ip_address,json=ipAddress,proto3" json:"ip_address,omitempty"`
	Port [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=port,proto3" json:"port,omitempty"`
	
}

Deprecated: Use Address_TcpIpAddress.ProtoReflect.Descriptor instead.

func (x *[Address_TcpIpAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress)) GetIpAddress() [][byte](https://pkg.go.dev/builtin#byte)

func (*[Address_TcpIpAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress)) ProtoMessage()

func (x *[Address_TcpIpAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress)) Reset()

type Address_TcpipAddress struct {
 TcpipAddress *[Address_TcpIpAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_TcpIpAddress) `protobuf:"bytes,1,opt,name=tcpip_address,json=tcpipAddress,proto3,oneof"` }

type Address_UdsAddress struct {
 Filename [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=filename,proto3" json:"filename,omitempty"` 	
}

A Unix Domain Socket address.

Deprecated: Use Address_UdsAddress.ProtoReflect.Descriptor instead.

func (*[Address_UdsAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress)) ProtoMessage()

func (x *[Address_UdsAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress)) Reset()

type Address_UdsAddress_ struct {
 UdsAddress *[Address_UdsAddress](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address_UdsAddress) `protobuf:"bytes,2,opt,name=uds_address,json=udsAddress,proto3,oneof"` }

type Channel struct {

	Ref *[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef) `protobuf:"bytes,1,opt,name=ref,proto3" json:"ref,omitempty"`
	Data *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData) `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"` 
	
	
	ChannelRef []*[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef) `protobuf:"bytes,3,rep,name=channel_ref,json=channelRef,proto3" json:"channel_ref,omitempty"`
	
	
	
	SubchannelRef []*[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef) `protobuf:"bytes,4,rep,name=subchannel_ref,json=subchannelRef,proto3" json:"subchannel_ref,omitempty"`
	SocketRef []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef) `protobuf:"bytes,5,rep,name=socket_ref,json=socketRef,proto3" json:"socket_ref,omitempty"`
	
}

Channel is a logical grouping of channels, subchannels, and sockets.

Deprecated: Use Channel.ProtoReflect.Descriptor instead.

func (x *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)) GetChannelRef() []*[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)

func (x *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)) GetData() *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)

func (x *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)) GetRef() *[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)

func (x *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)) GetSocketRef() []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)

func (x *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)) GetSubchannelRef() []*[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)

func (*[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)) ProtoMessage()

func (x *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)) Reset()

type ChannelConnectivityState_State [int32](https://pkg.go.dev/builtin#int32)

const (
 ChannelConnectivityState_UNKNOWN [ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State) = 0  ChannelConnectivityState_IDLE [ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State) = 1  ChannelConnectivityState_CONNECTING [ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State) = 2  ChannelConnectivityState_READY [ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State) = 3  ChannelConnectivityState_TRANSIENT_FAILURE [ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State) = 4  ChannelConnectivityState_SHUTDOWN [ChannelConnectivityState_State](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState_State) = 5 )

Deprecated: Use ChannelConnectivityState_State.Descriptor instead.

type ChannelData struct {

	
	State *[ChannelConnectivityState](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState) `protobuf:"bytes,1,opt,name=state,proto3" json:"state,omitempty"`
	Target [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=target,proto3" json:"target,omitempty"`
	Trace *[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace) `protobuf:"bytes,3,opt,name=trace,proto3" json:"trace,omitempty"`
	CallsStarted [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=calls_started,json=callsStarted,proto3" json:"calls_started,omitempty"`
	CallsSucceeded [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,5,opt,name=calls_succeeded,json=callsSucceeded,proto3" json:"calls_succeeded,omitempty"`
	CallsFailed [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,6,opt,name=calls_failed,json=callsFailed,proto3" json:"calls_failed,omitempty"`
	LastCallStartedTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `` 
	
}

Channel data is data related to a specific Channel or Subchannel.

Deprecated: Use ChannelData.ProtoReflect.Descriptor instead.

func (x *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)) GetCallsFailed() [int64](https://pkg.go.dev/builtin#int64)

func (x *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)) GetCallsStarted() [int64](https://pkg.go.dev/builtin#int64)

func (x *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)) GetCallsSucceeded() [int64](https://pkg.go.dev/builtin#int64)

func (x *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)) GetState() *[ChannelConnectivityState](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelConnectivityState)

func (x *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)) GetTrace() *[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace)

func (*[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)) ProtoMessage()

func (x *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)) Reset()

type ChannelRef struct {

	ChannelId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=channel_id,json=channelId,proto3" json:"channel_id,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	
}

ChannelRef is a reference to a Channel.

Deprecated: Use ChannelRef.ProtoReflect.Descriptor instead.

func (x *[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)) GetChannelId() [int64](https://pkg.go.dev/builtin#int64)

func (*[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)) ProtoMessage()

func (x *[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)) Reset()

type ChannelTrace struct {

	
	
	NumEventsLogged [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=num_events_logged,json=numEventsLogged,proto3" json:"num_events_logged,omitempty"`
	CreationTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `protobuf:"bytes,2,opt,name=creation_timestamp,json=creationTimestamp,proto3" json:"creation_timestamp,omitempty"`
	Events []*[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent) `protobuf:"bytes,3,rep,name=events,proto3" json:"events,omitempty"`
	
}

ChannelTrace represents the recent events that have occurred on the channel.

Deprecated: Use ChannelTrace.ProtoReflect.Descriptor instead.

func (x *[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace)) GetEvents() []*[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)

func (x *[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace)) GetNumEventsLogged() [int64](https://pkg.go.dev/builtin#int64)

func (*[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace)) ProtoMessage()

func (x *[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace)) Reset()

type ChannelTraceEvent struct {

	Description [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=description,proto3" json:"description,omitempty"`
	Severity [ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity) `protobuf:"varint,2,opt,name=severity,proto3,enum=grpc.channelz.v1.ChannelTraceEvent_Severity" json:"severity,omitempty"`
	Timestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `protobuf:"bytes,3,opt,name=timestamp,proto3" json:"timestamp,omitempty"`
	
	
	
	
	
	
	
	
	ChildRef isChannelTraceEvent_ChildRef `protobuf_oneof:"child_ref"`
	
}

A trace event is an interesting thing that happened to a channel or subchannel, such as creation, address resolution, subchannel creation, etc.

Deprecated: Use ChannelTraceEvent.ProtoReflect.Descriptor instead.

func (x *[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)) GetChannelRef() *[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)

func (x *[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)) GetChildRef() isChannelTraceEvent_ChildRef

func (x *[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)) GetSeverity() [ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity)

func (x *[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)) GetSubchannelRef() *[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)

func (*[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)) ProtoMessage()

func (x *[ChannelTraceEvent](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent)) Reset()

type ChannelTraceEvent_ChannelRef struct {
 ChannelRef *[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef) `protobuf:"bytes,4,opt,name=channel_ref,json=channelRef,proto3,oneof"` }

type ChannelTraceEvent_Severity [int32](https://pkg.go.dev/builtin#int32)

The supported severity levels of trace events.

const (
 ChannelTraceEvent_CT_UNKNOWN [ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity) = 0  ChannelTraceEvent_CT_INFO [ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity) = 1  ChannelTraceEvent_CT_WARNING [ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity) = 2  ChannelTraceEvent_CT_ERROR [ChannelTraceEvent_Severity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTraceEvent_Severity) = 3 )

Deprecated: Use ChannelTraceEvent_Severity.Descriptor instead.

type ChannelTraceEvent_SubchannelRef struct {
 SubchannelRef *[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef) `protobuf:"bytes,5,opt,name=subchannel_ref,json=subchannelRef,proto3,oneof"` }

type ChannelzClient interface {
	
	GetTopChannels(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), in *[GetTopChannelsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest), opts ...[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[CallOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#CallOption)) (*[GetTopChannelsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse), [error](https://pkg.go.dev/builtin#error))
	GetServers(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), in *[GetServersRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest), opts ...[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[CallOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#CallOption)) (*[GetServersResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse), [error](https://pkg.go.dev/builtin#error))
	GetServer(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), in *[GetServerRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest), opts ...[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[CallOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#CallOption)) (*[GetServerResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse), [error](https://pkg.go.dev/builtin#error))
	GetServerSockets(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), in *[GetServerSocketsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest), opts ...[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[CallOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#CallOption)) (*[GetServerSocketsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse), [error](https://pkg.go.dev/builtin#error))
	GetChannel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), in *[GetChannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest), opts ...[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[CallOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#CallOption)) (*[GetChannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse), [error](https://pkg.go.dev/builtin#error))
	GetSubchannel(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), in *[GetSubchannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest), opts ...[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[CallOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#CallOption)) (*[GetSubchannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse), [error](https://pkg.go.dev/builtin#error))
	GetSocket(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), in *[GetSocketRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest), opts ...[grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[CallOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#CallOption)) (*[GetSocketResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse), [error](https://pkg.go.dev/builtin#error))
}

ChannelzClient is the client API for Channelz service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to [https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream](https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream).

Channelz is a service exposed by gRPC servers that provides detailed debug information.

type ChannelzServer interface {
	
	GetTopChannels([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[GetTopChannelsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest)) (*[GetTopChannelsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse), [error](https://pkg.go.dev/builtin#error))
	GetServers([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[GetServersRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest)) (*[GetServersResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse), [error](https://pkg.go.dev/builtin#error))
	GetServer([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[GetServerRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest)) (*[GetServerResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse), [error](https://pkg.go.dev/builtin#error))
	GetServerSockets([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[GetServerSocketsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest)) (*[GetServerSocketsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse), [error](https://pkg.go.dev/builtin#error))
	GetChannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[GetChannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest)) (*[GetChannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse), [error](https://pkg.go.dev/builtin#error))
	GetSubchannel([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[GetSubchannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest)) (*[GetSubchannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse), [error](https://pkg.go.dev/builtin#error))
	GetSocket([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[GetSocketRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest)) (*[GetSocketResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse), [error](https://pkg.go.dev/builtin#error))
}

ChannelzServer is the server API for Channelz service. All implementations should embed UnimplementedChannelzServer for forward compatibility.

Channelz is a service exposed by gRPC servers that provides detailed debug information.

type GetChannelRequest struct {

	ChannelId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=channel_id,json=channelId,proto3" json:"channel_id,omitempty"`
	
}

Deprecated: Use GetChannelRequest.ProtoReflect.Descriptor instead.

func (*[GetChannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest)) ProtoMessage()

func (x *[GetChannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelRequest)) Reset()

type GetChannelResponse struct {

	
	Channel *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel) `protobuf:"bytes,1,opt,name=channel,proto3" json:"channel,omitempty"`
	
}

Deprecated: Use GetChannelResponse.ProtoReflect.Descriptor instead.

func (x *[GetChannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse)) GetChannel() *[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)

func (*[GetChannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse)) ProtoMessage()

func (x *[GetChannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetChannelResponse)) Reset()

type GetServerRequest struct {

	ServerId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=server_id,json=serverId,proto3" json:"server_id,omitempty"`
	
}

Deprecated: Use GetServerRequest.ProtoReflect.Descriptor instead.

func (*[GetServerRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest)) ProtoMessage()

func (x *[GetServerRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerRequest)) Reset()

type GetServerResponse struct {

	
	Server *[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server) `protobuf:"bytes,1,opt,name=server,proto3" json:"server,omitempty"`
	
}

Deprecated: Use GetServerResponse.ProtoReflect.Descriptor instead.

func (x *[GetServerResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse)) GetServer() *[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server)

func (*[GetServerResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse)) ProtoMessage()

func (x *[GetServerResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerResponse)) Reset()

type GetServerSocketsRequest struct {
 ServerId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=server_id,json=serverId,proto3" json:"server_id,omitempty"` 	
	
	
	
	StartSocketId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=start_socket_id,json=startSocketId,proto3" json:"start_socket_id,omitempty"`
	
	
	MaxResults [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=max_results,json=maxResults,proto3" json:"max_results,omitempty"`
	
}

Deprecated: Use GetServerSocketsRequest.ProtoReflect.Descriptor instead.

func (*[GetServerSocketsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest)) ProtoMessage()

func (x *[GetServerSocketsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsRequest)) Reset()

type GetServerSocketsResponse struct {

	
	
	SocketRef []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef) `protobuf:"bytes,1,rep,name=socket_ref,json=socketRef,proto3" json:"socket_ref,omitempty"`
	
	
	End [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=end,proto3" json:"end,omitempty"`
	
}

Deprecated: Use GetServerSocketsResponse.ProtoReflect.Descriptor instead.

func (x *[GetServerSocketsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse)) GetSocketRef() []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)

func (*[GetServerSocketsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse)) ProtoMessage()

func (x *[GetServerSocketsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServerSocketsResponse)) Reset()

type GetServersRequest struct {

	
	
	
	
	StartServerId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=start_server_id,json=startServerId,proto3" json:"start_server_id,omitempty"`
	
	
	MaxResults [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=max_results,json=maxResults,proto3" json:"max_results,omitempty"`
	
}

Deprecated: Use GetServersRequest.ProtoReflect.Descriptor instead.

func (x *[GetServersRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest)) GetStartServerId() [int64](https://pkg.go.dev/builtin#int64)

func (*[GetServersRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest)) ProtoMessage()

func (x *[GetServersRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersRequest)) Reset()

type GetServersResponse struct {

	
	
	Server []*[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server) `protobuf:"bytes,1,rep,name=server,proto3" json:"server,omitempty"`
	
	
	End [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=end,proto3" json:"end,omitempty"`
	
}

Deprecated: Use GetServersResponse.ProtoReflect.Descriptor instead.

func (x *[GetServersResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse)) GetServer() []*[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server)

func (*[GetServersResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse)) ProtoMessage()

func (x *[GetServersResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetServersResponse)) Reset()

type GetSocketRequest struct {

	SocketId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=socket_id,json=socketId,proto3" json:"socket_id,omitempty"`
	
	
	Summary [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=summary,proto3" json:"summary,omitempty"`
	
}

Deprecated: Use GetSocketRequest.ProtoReflect.Descriptor instead.

func (x *[GetSocketRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest)) GetSummary() [bool](https://pkg.go.dev/builtin#bool)

func (*[GetSocketRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest)) ProtoMessage()

func (x *[GetSocketRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketRequest)) Reset()

type GetSocketResponse struct {

	
	Socket *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket) `protobuf:"bytes,1,opt,name=socket,proto3" json:"socket,omitempty"`
	
}

Deprecated: Use GetSocketResponse.ProtoReflect.Descriptor instead.

func (x *[GetSocketResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse)) GetSocket() *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)

func (*[GetSocketResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse)) ProtoMessage()

func (x *[GetSocketResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSocketResponse)) Reset()

type GetSubchannelRequest struct {

	SubchannelId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=subchannel_id,json=subchannelId,proto3" json:"subchannel_id,omitempty"`
	
}

Deprecated: Use GetSubchannelRequest.ProtoReflect.Descriptor instead.

func (*[GetSubchannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest)) ProtoMessage()

func (x *[GetSubchannelRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelRequest)) Reset()

type GetSubchannelResponse struct {

	
	Subchannel *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel) `protobuf:"bytes,1,opt,name=subchannel,proto3" json:"subchannel,omitempty"`
	
}

Deprecated: Use GetSubchannelResponse.ProtoReflect.Descriptor instead.

func (x *[GetSubchannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse)) GetSubchannel() *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)

func (*[GetSubchannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse)) ProtoMessage()

func (x *[GetSubchannelResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetSubchannelResponse)) Reset()

type GetTopChannelsRequest struct {

	
	
	
	
	StartChannelId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=start_channel_id,json=startChannelId,proto3" json:"start_channel_id,omitempty"`
	
	
	MaxResults [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=max_results,json=maxResults,proto3" json:"max_results,omitempty"`
	
}

Deprecated: Use GetTopChannelsRequest.ProtoReflect.Descriptor instead.

func (x *[GetTopChannelsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest)) GetStartChannelId() [int64](https://pkg.go.dev/builtin#int64)

func (*[GetTopChannelsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest)) ProtoMessage()

func (x *[GetTopChannelsRequest](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsRequest)) Reset()

type GetTopChannelsResponse struct {

	
	
	Channel []*[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel) `protobuf:"bytes,1,rep,name=channel,proto3" json:"channel,omitempty"`
	
	
	End [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=end,proto3" json:"end,omitempty"`
	
}

Deprecated: Use GetTopChannelsResponse.ProtoReflect.Descriptor instead.

func (x *[GetTopChannelsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse)) GetChannel() []*[Channel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Channel)

func (*[GetTopChannelsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse)) ProtoMessage()

func (x *[GetTopChannelsResponse](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#GetTopChannelsResponse)) Reset()

type Security struct {

	
	
	
	Model isSecurity_Model `protobuf_oneof:"model"`
	
}

Security represents details about how secure the socket is.

Deprecated: Use Security.ProtoReflect.Descriptor instead.

func (x *[Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security)) GetModel() isSecurity_Model

func (x *[Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security)) GetOther() *[Security_OtherSecurity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity)

func (x *[Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security)) GetTls() *[Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls)

func (*[Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security)) ProtoMessage()

func (x *[Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security)) Reset()

type Security_Other struct {
 Other *[Security_OtherSecurity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity) `protobuf:"bytes,2,opt,name=other,proto3,oneof"` }

type Security_OtherSecurity struct {

	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Value *[anypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb).[Any](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb#Any) `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
	
}

Deprecated: Use Security_OtherSecurity.ProtoReflect.Descriptor instead.

func (*[Security_OtherSecurity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity)) ProtoMessage()

func (x *[Security_OtherSecurity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_OtherSecurity)) Reset()

type Security_Tls struct {

	
	
	
	CipherSuite isSecurity_Tls_CipherSuite `protobuf_oneof:"cipher_suite"`
	LocalCertificate [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,3,opt,name=local_certificate,json=localCertificate,proto3" json:"local_certificate,omitempty"`
	RemoteCertificate [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,4,opt,name=remote_certificate,json=remoteCertificate,proto3" json:"remote_certificate,omitempty"`
	
}

Deprecated: Use Security_Tls.ProtoReflect.Descriptor instead.

func (x *[Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls)) GetCipherSuite() isSecurity_Tls_CipherSuite

func (x *[Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls)) GetLocalCertificate() [][byte](https://pkg.go.dev/builtin#byte)

func (x *[Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls)) GetRemoteCertificate() [][byte](https://pkg.go.dev/builtin#byte)

func (*[Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls)) ProtoMessage()

func (x *[Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls)) Reset()

type Security_Tls_ struct {
 Tls *[Security_Tls](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls) `protobuf:"bytes,1,opt,name=tls,proto3,oneof"` }

type Security_Tls_OtherName struct {
	
	OtherName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=other_name,json=otherName,proto3,oneof"`
}

#### type [Security_Tls_StandardName](https://github.com/grpc/grpc-go/blob/v1.79.1/channelz/grpc_channelz_v1/channelz.pb.go#L2895)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security_Tls_StandardName "Go to Security_Tls_StandardName")

type Security_Tls_StandardName struct {
	
	StandardName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=standard_name,json=standardName,proto3,oneof"`
}

type Server struct {

	Ref *[ServerRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef) `protobuf:"bytes,1,opt,name=ref,proto3" json:"ref,omitempty"`
	Data *[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData) `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	
	ListenSocket []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef) `protobuf:"bytes,3,rep,name=listen_socket,json=listenSocket,proto3" json:"listen_socket,omitempty"`
	
}

Server represents a single server. There may be multiple servers in a single program.

Deprecated: Use Server.ProtoReflect.Descriptor instead.

func (x *[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server)) GetData() *[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)

func (x *[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server)) GetListenSocket() []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)

func (x *[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server)) GetRef() *[ServerRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef)

func (*[Server](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Server)) ProtoMessage()

type ServerData struct {

	Trace *[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace) `protobuf:"bytes,1,opt,name=trace,proto3" json:"trace,omitempty"`
	CallsStarted [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=calls_started,json=callsStarted,proto3" json:"calls_started,omitempty"`
	CallsSucceeded [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=calls_succeeded,json=callsSucceeded,proto3" json:"calls_succeeded,omitempty"`
	CallsFailed [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=calls_failed,json=callsFailed,proto3" json:"calls_failed,omitempty"`
	LastCallStartedTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `` 
	
}

ServerData is data for a specific Server.

Deprecated: Use ServerData.ProtoReflect.Descriptor instead.

func (x *[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)) GetCallsFailed() [int64](https://pkg.go.dev/builtin#int64)

func (x *[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)) GetCallsStarted() [int64](https://pkg.go.dev/builtin#int64)

func (x *[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)) GetCallsSucceeded() [int64](https://pkg.go.dev/builtin#int64)

func (x *[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)) GetTrace() *[ChannelTrace](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelTrace)

func (*[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)) ProtoMessage()

func (x *[ServerData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerData)) Reset()

type ServerRef struct {

	ServerId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,5,opt,name=server_id,json=serverId,proto3" json:"server_id,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=name,proto3" json:"name,omitempty"`
	
}

ServerRef is a reference to a Server.

Deprecated: Use ServerRef.ProtoReflect.Descriptor instead.

func (x *[ServerRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef)) GetServerId() [int64](https://pkg.go.dev/builtin#int64)

func (*[ServerRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef)) ProtoMessage()

func (x *[ServerRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ServerRef)) Reset()

type Socket struct {

	Ref *[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef) `protobuf:"bytes,1,opt,name=ref,proto3" json:"ref,omitempty"`
	Data *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData) `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"`
	Local *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address) `protobuf:"bytes,3,opt,name=local,proto3" json:"local,omitempty"`
	Remote *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address) `protobuf:"bytes,4,opt,name=remote,proto3" json:"remote,omitempty"`
	
	Security *[Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security) `protobuf:"bytes,5,opt,name=security,proto3" json:"security,omitempty"`
	
	RemoteName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=remote_name,json=remoteName,proto3" json:"remote_name,omitempty"`
	
}

Information about an actual connection. Pronounced "sock-ay".

Deprecated: Use Socket.ProtoReflect.Descriptor instead.

func (x *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)) GetData() *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)

func (x *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)) GetLocal() *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)

func (x *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)) GetRef() *[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)

func (x *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)) GetRemote() *[Address](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Address)

func (x *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)) GetRemoteName() [string](https://pkg.go.dev/builtin#string)

func (x *[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)) GetSecurity() *[Security](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Security)

func (*[Socket](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Socket)) ProtoMessage()

type SocketData struct {

	StreamsStarted [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,1,opt,name=streams_started,json=streamsStarted,proto3" json:"streams_started,omitempty"`
	
	
	StreamsSucceeded [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=streams_succeeded,json=streamsSucceeded,proto3" json:"streams_succeeded,omitempty"`
	
	
	StreamsFailed [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=streams_failed,json=streamsFailed,proto3" json:"streams_failed,omitempty"`
	MessagesSent [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,4,opt,name=messages_sent,json=messagesSent,proto3" json:"messages_sent,omitempty"`
	MessagesReceived [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,5,opt,name=messages_received,json=messagesReceived,proto3" json:"messages_received,omitempty"`
	
	KeepAlivesSent [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,6,opt,name=keep_alives_sent,json=keepAlivesSent,proto3" json:"keep_alives_sent,omitempty"`
	
	LastLocalStreamCreatedTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `` 
	
	LastRemoteStreamCreatedTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `` 
	LastMessageSentTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `` 
	LastMessageReceivedTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `` 
	
	
	LocalFlowControlWindow *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[Int64Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#Int64Value) `` 
	
	
	RemoteFlowControlWindow *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[Int64Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#Int64Value) `` 
	
	Option []*[SocketOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption) `protobuf:"bytes,13,rep,name=option,proto3" json:"option,omitempty"`
	
}

SocketData is data associated for a specific Socket. The fields present are specific to the implementation, so there may be minor differences in the semantics. (e.g. flow control windows)

Deprecated: Use SocketData.ProtoReflect.Descriptor instead.

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) GetKeepAlivesSent() [int64](https://pkg.go.dev/builtin#int64)

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) GetMessagesReceived() [int64](https://pkg.go.dev/builtin#int64)

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) GetMessagesSent() [int64](https://pkg.go.dev/builtin#int64)

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) GetOption() []*[SocketOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption)

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) GetStreamsFailed() [int64](https://pkg.go.dev/builtin#int64)

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) GetStreamsStarted() [int64](https://pkg.go.dev/builtin#int64)

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) GetStreamsSucceeded() [int64](https://pkg.go.dev/builtin#int64)

func (*[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) ProtoMessage()

func (x *[SocketData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketData)) Reset()

type SocketOption struct {

	
	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	
	Value [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=value,proto3" json:"value,omitempty"`
	
	Additional *[anypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb).[Any](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb#Any) `protobuf:"bytes,3,opt,name=additional,proto3" json:"additional,omitempty"`
	
}

SocketOption represents socket options for a socket. Specifically, these are the options returned by getsockopt().

Deprecated: Use SocketOption.ProtoReflect.Descriptor instead.

func (*[SocketOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption)) ProtoMessage()

func (x *[SocketOption](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOption)) Reset()

type SocketOptionLinger struct {

	Active [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=active,proto3" json:"active,omitempty"`
	Duration *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration) `protobuf:"bytes,2,opt,name=duration,proto3" json:"duration,omitempty"`
	
}

For use with SocketOption's additional field. This is primarily used for SO_LINGER.

Deprecated: Use SocketOptionLinger.ProtoReflect.Descriptor instead.

func (*[SocketOptionLinger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger)) ProtoMessage()

func (x *[SocketOptionLinger](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionLinger)) Reset()

type SocketOptionTcpInfo struct {
 TcpiState [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,1,opt,name=tcpi_state,json=tcpiState,proto3" json:"tcpi_state,omitempty"`  TcpiCaState [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,2,opt,name=tcpi_ca_state,json=tcpiCaState,proto3" json:"tcpi_ca_state,omitempty"`  TcpiRetransmits [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,3,opt,name=tcpi_retransmits,json=tcpiRetransmits,proto3" json:"tcpi_retransmits,omitempty"`  TcpiProbes [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,4,opt,name=tcpi_probes,json=tcpiProbes,proto3" json:"tcpi_probes,omitempty"`  TcpiBackoff [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,5,opt,name=tcpi_backoff,json=tcpiBackoff,proto3" json:"tcpi_backoff,omitempty"`  TcpiOptions [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,6,opt,name=tcpi_options,json=tcpiOptions,proto3" json:"tcpi_options,omitempty"`  TcpiSndWscale [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,7,opt,name=tcpi_snd_wscale,json=tcpiSndWscale,proto3" json:"tcpi_snd_wscale,omitempty"`  TcpiRcvWscale [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,8,opt,name=tcpi_rcv_wscale,json=tcpiRcvWscale,proto3" json:"tcpi_rcv_wscale,omitempty"`  TcpiRto [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,9,opt,name=tcpi_rto,json=tcpiRto,proto3" json:"tcpi_rto,omitempty"`  TcpiAto [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,10,opt,name=tcpi_ato,json=tcpiAto,proto3" json:"tcpi_ato,omitempty"`  TcpiSndMss [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,11,opt,name=tcpi_snd_mss,json=tcpiSndMss,proto3" json:"tcpi_snd_mss,omitempty"`  TcpiRcvMss [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,12,opt,name=tcpi_rcv_mss,json=tcpiRcvMss,proto3" json:"tcpi_rcv_mss,omitempty"`  TcpiUnacked [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,13,opt,name=tcpi_unacked,json=tcpiUnacked,proto3" json:"tcpi_unacked,omitempty"`  TcpiSacked [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,14,opt,name=tcpi_sacked,json=tcpiSacked,proto3" json:"tcpi_sacked,omitempty"`  TcpiLost [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,15,opt,name=tcpi_lost,json=tcpiLost,proto3" json:"tcpi_lost,omitempty"`  TcpiRetrans [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,16,opt,name=tcpi_retrans,json=tcpiRetrans,proto3" json:"tcpi_retrans,omitempty"`  TcpiFackets [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,17,opt,name=tcpi_fackets,json=tcpiFackets,proto3" json:"tcpi_fackets,omitempty"`  TcpiLastDataSent [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,18,opt,name=tcpi_last_data_sent,json=tcpiLastDataSent,proto3" json:"tcpi_last_data_sent,omitempty"`  TcpiLastAckSent [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,19,opt,name=tcpi_last_ack_sent,json=tcpiLastAckSent,proto3" json:"tcpi_last_ack_sent,omitempty"`  TcpiLastDataRecv [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,20,opt,name=tcpi_last_data_recv,json=tcpiLastDataRecv,proto3" json:"tcpi_last_data_recv,omitempty"`  TcpiLastAckRecv [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,21,opt,name=tcpi_last_ack_recv,json=tcpiLastAckRecv,proto3" json:"tcpi_last_ack_recv,omitempty"`  TcpiPmtu [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,22,opt,name=tcpi_pmtu,json=tcpiPmtu,proto3" json:"tcpi_pmtu,omitempty"`  TcpiRcvSsthresh [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,23,opt,name=tcpi_rcv_ssthresh,json=tcpiRcvSsthresh,proto3" json:"tcpi_rcv_ssthresh,omitempty"`  TcpiRtt [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,24,opt,name=tcpi_rtt,json=tcpiRtt,proto3" json:"tcpi_rtt,omitempty"`  TcpiRttvar [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,25,opt,name=tcpi_rttvar,json=tcpiRttvar,proto3" json:"tcpi_rttvar,omitempty"`  TcpiSndSsthresh [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,26,opt,name=tcpi_snd_ssthresh,json=tcpiSndSsthresh,proto3" json:"tcpi_snd_ssthresh,omitempty"`  TcpiSndCwnd [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,27,opt,name=tcpi_snd_cwnd,json=tcpiSndCwnd,proto3" json:"tcpi_snd_cwnd,omitempty"`  TcpiAdvmss [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,28,opt,name=tcpi_advmss,json=tcpiAdvmss,proto3" json:"tcpi_advmss,omitempty"`  TcpiReordering [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,29,opt,name=tcpi_reordering,json=tcpiReordering,proto3" json:"tcpi_reordering,omitempty"` 	
}

For use with SocketOption's additional field. Tcp info for SOL_TCP and TCP_INFO.

Deprecated: Use SocketOptionTcpInfo.ProtoReflect.Descriptor instead.

func (*[SocketOptionTcpInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo)) ProtoMessage()

func (x *[SocketOptionTcpInfo](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTcpInfo)) Reset()

type SocketOptionTimeout struct {
 Duration *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration) `protobuf:"bytes,1,opt,name=duration,proto3" json:"duration,omitempty"` 	
}

For use with SocketOption's additional field. This is primarily used for SO_RCVTIMEO and SO_SNDTIMEO

Deprecated: Use SocketOptionTimeout.ProtoReflect.Descriptor instead.

func (*[SocketOptionTimeout](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout)) ProtoMessage()

func (x *[SocketOptionTimeout](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketOptionTimeout)) Reset()

type SocketRef struct {

	SocketId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=socket_id,json=socketId,proto3" json:"socket_id,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=name,proto3" json:"name,omitempty"`
	
}

SocketRef is a reference to a Socket.

Deprecated: Use SocketRef.ProtoReflect.Descriptor instead.

func (x *[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)) GetSocketId() [int64](https://pkg.go.dev/builtin#int64)

func (*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)) ProtoMessage()

func (x *[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)) Reset()

type Subchannel struct {

	Ref *[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef) `protobuf:"bytes,1,opt,name=ref,proto3" json:"ref,omitempty"`
	Data *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData) `protobuf:"bytes,2,opt,name=data,proto3" json:"data,omitempty"` 
	
	
	ChannelRef []*[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef) `protobuf:"bytes,3,rep,name=channel_ref,json=channelRef,proto3" json:"channel_ref,omitempty"`
	
	
	
	SubchannelRef []*[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef) `protobuf:"bytes,4,rep,name=subchannel_ref,json=subchannelRef,proto3" json:"subchannel_ref,omitempty"`
	SocketRef []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef) `protobuf:"bytes,5,rep,name=socket_ref,json=socketRef,proto3" json:"socket_ref,omitempty"`
	
}

Subchannel is a logical grouping of channels, subchannels, and sockets. A subchannel is load balanced over by its ancestor

Deprecated: Use Subchannel.ProtoReflect.Descriptor instead.

func (x *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)) GetChannelRef() []*[ChannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelRef)

func (x *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)) GetData() *[ChannelData](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#ChannelData)

func (x *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)) GetRef() *[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)

func (x *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)) GetSocketRef() []*[SocketRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SocketRef)

func (x *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)) GetSubchannelRef() []*[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)

func (*[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)) ProtoMessage()

func (x *[Subchannel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#Subchannel)) Reset()

type SubchannelRef struct {

	SubchannelId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,7,opt,name=subchannel_id,json=subchannelId,proto3" json:"subchannel_id,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=name,proto3" json:"name,omitempty"`
	
}

SubchannelRef is a reference to a Subchannel.

Deprecated: Use SubchannelRef.ProtoReflect.Descriptor instead.

func (x *[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)) GetSubchannelId() [int64](https://pkg.go.dev/builtin#int64)

func (*[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)) ProtoMessage()

func (x *[SubchannelRef](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/channelz/grpc_channelz_v1#SubchannelRef)) Reset()

type UnimplementedChannelzServer struct{}

UnimplementedChannelzServer should be embedded to have forward compatible implementations.

NOTE: this should be embedded by value instead of pointer to avoid a nil pointer dereference when methods are called.

type UnsafeChannelzServer interface {
	
}

UnsafeChannelzServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to ChannelzServer will result in compilation errors.
