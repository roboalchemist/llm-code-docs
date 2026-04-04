# Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp

Title: grpc_gcp package - google.golang.org/grpc/credentials/alts/internal/proto/grpc_gcp - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp

Markdown Content:
*   [Constants](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#pkg-constants)
*   [Variables](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#pkg-variables)
*   [func RegisterHandshakerServiceServer(s grpc.ServiceRegistrar, srv HandshakerServiceServer)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RegisterHandshakerServiceServer)
*   [type AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)
*       *   [func (*AltsContext) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.Descriptor)deprecated
    *   [func (x *AltsContext) GetApplicationProtocol() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.GetApplicationProtocol)
    *   [func (x *AltsContext) GetLocalServiceAccount() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.GetLocalServiceAccount)
    *   [func (x *AltsContext) GetPeerAttributes() map[string]string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.GetPeerAttributes)
    *   [func (x *AltsContext) GetPeerRpcVersions() *RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.GetPeerRpcVersions)
    *   [func (x *AltsContext) GetPeerServiceAccount() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.GetPeerServiceAccount)
    *   [func (x *AltsContext) GetRecordProtocol() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.GetRecordProtocol)
    *   [func (x *AltsContext) GetSecurityLevel() SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.GetSecurityLevel)
    *   [func (*AltsContext) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.ProtoMessage)
    *   [func (x *AltsContext) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.ProtoReflect)
    *   [func (x *AltsContext) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.Reset)
    *   [func (x *AltsContext) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext.String)

*   [type Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint)
*       *   [func (*Endpoint) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.Descriptor)deprecated
    *   [func (x *Endpoint) GetIpAddress() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.GetIpAddress)
    *   [func (x *Endpoint) GetPort() int32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.GetPort)
    *   [func (x *Endpoint) GetProtocol() NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.GetProtocol)
    *   [func (*Endpoint) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.ProtoMessage)
    *   [func (x *Endpoint) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.ProtoReflect)
    *   [func (x *Endpoint) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.Reset)
    *   [func (x *Endpoint) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint.String)

*   [type HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol)
*       *   [func (HandshakeProtocol) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Descriptor)
    *   [func (x HandshakeProtocol) Enum() *HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Enum)
    *   [func (HandshakeProtocol) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.EnumDescriptor)deprecated
    *   [func (x HandshakeProtocol) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Number)
    *   [func (x HandshakeProtocol) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.String)
    *   [func (HandshakeProtocol) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Type)

*   [type HandshakerReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq)
*       *   [func (*HandshakerReq) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.Descriptor)deprecated
    *   [func (x *HandshakerReq) GetClientStart() *StartClientHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.GetClientStart)
    *   [func (x *HandshakerReq) GetNext() *NextHandshakeMessageReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.GetNext)
    *   [func (x *HandshakerReq) GetReqOneof() isHandshakerReq_ReqOneof](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.GetReqOneof)
    *   [func (x *HandshakerReq) GetServerStart() *StartServerHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.GetServerStart)
    *   [func (*HandshakerReq) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.ProtoMessage)
    *   [func (x *HandshakerReq) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.ProtoReflect)
    *   [func (x *HandshakerReq) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.Reset)
    *   [func (x *HandshakerReq) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.String)

*   [type HandshakerReq_ClientStart](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq_ClientStart)
*   [type HandshakerReq_Next](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq_Next)
*   [type HandshakerReq_ServerStart](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq_ServerStart)
*   [type HandshakerResp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp)
*       *   [func (*HandshakerResp) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.Descriptor)deprecated
    *   [func (x *HandshakerResp) GetBytesConsumed() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.GetBytesConsumed)
    *   [func (x *HandshakerResp) GetOutFrames() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.GetOutFrames)
    *   [func (x *HandshakerResp) GetResult() *HandshakerResult](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.GetResult)
    *   [func (x *HandshakerResp) GetStatus() *HandshakerStatus](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.GetStatus)
    *   [func (*HandshakerResp) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.ProtoMessage)
    *   [func (x *HandshakerResp) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.ProtoReflect)
    *   [func (x *HandshakerResp) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.Reset)
    *   [func (x *HandshakerResp) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.String)

*   [type HandshakerResult](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult)
*       *   [func (*HandshakerResult) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.Descriptor)deprecated
    *   [func (x *HandshakerResult) GetApplicationProtocol() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetApplicationProtocol)
    *   [func (x *HandshakerResult) GetKeepChannelOpen() bool](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetKeepChannelOpen)
    *   [func (x *HandshakerResult) GetKeyData() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetKeyData)
    *   [func (x *HandshakerResult) GetLocalIdentity() *Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetLocalIdentity)
    *   [func (x *HandshakerResult) GetMaxFrameSize() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetMaxFrameSize)
    *   [func (x *HandshakerResult) GetPeerIdentity() *Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetPeerIdentity)
    *   [func (x *HandshakerResult) GetPeerRpcVersions() *RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetPeerRpcVersions)
    *   [func (x *HandshakerResult) GetRecordProtocol() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetRecordProtocol)
    *   [func (x *HandshakerResult) GetTransportProtocol() *NegotiatedTransportProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.GetTransportProtocol)
    *   [func (*HandshakerResult) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.ProtoMessage)
    *   [func (x *HandshakerResult) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.ProtoReflect)
    *   [func (x *HandshakerResult) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.Reset)
    *   [func (x *HandshakerResult) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.String)

*   [type HandshakerServiceClient](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerServiceClient)
*       *   [func NewHandshakerServiceClient(cc grpc.ClientConnInterface) HandshakerServiceClient](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NewHandshakerServiceClient)

*   [type HandshakerServiceServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerServiceServer)
*   [type HandshakerService_DoHandshakeClient](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerService_DoHandshakeClient)
*   [type HandshakerService_DoHandshakeServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerService_DoHandshakeServer)
*   [type HandshakerStatus](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus)
*       *   [func (*HandshakerStatus) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.Descriptor)deprecated
    *   [func (x *HandshakerStatus) GetCode() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.GetCode)
    *   [func (x *HandshakerStatus) GetDetails() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.GetDetails)
    *   [func (*HandshakerStatus) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.ProtoMessage)
    *   [func (x *HandshakerStatus) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.ProtoReflect)
    *   [func (x *HandshakerStatus) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.Reset)
    *   [func (x *HandshakerStatus) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.String)

*   [type Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity)
*       *   [func (*Identity) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.Descriptor)deprecated
    *   [func (x *Identity) GetAttributes() map[string]string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.GetAttributes)
    *   [func (x *Identity) GetHostname() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.GetHostname)
    *   [func (x *Identity) GetIdentityOneof() isIdentity_IdentityOneof](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.GetIdentityOneof)
    *   [func (x *Identity) GetServiceAccount() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.GetServiceAccount)
    *   [func (*Identity) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.ProtoMessage)
    *   [func (x *Identity) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.ProtoReflect)
    *   [func (x *Identity) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.Reset)
    *   [func (x *Identity) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity.String)

*   [type Identity_Hostname](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity_Hostname)
*   [type Identity_ServiceAccount](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity_ServiceAccount)
*   [type NegotiatedTransportProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol)
*       *   [func (*NegotiatedTransportProtocol) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol.Descriptor)deprecated
    *   [func (x *NegotiatedTransportProtocol) GetTransportProtocol() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol.GetTransportProtocol)
    *   [func (*NegotiatedTransportProtocol) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol.ProtoMessage)
    *   [func (x *NegotiatedTransportProtocol) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol.ProtoReflect)
    *   [func (x *NegotiatedTransportProtocol) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol.Reset)
    *   [func (x *NegotiatedTransportProtocol) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol.String)

*   [type NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol)
*       *   [func (NetworkProtocol) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol.Descriptor)
    *   [func (x NetworkProtocol) Enum() *NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol.Enum)
    *   [func (NetworkProtocol) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol.EnumDescriptor)deprecated
    *   [func (x NetworkProtocol) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol.Number)
    *   [func (x NetworkProtocol) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol.String)
    *   [func (NetworkProtocol) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol.Type)

*   [type NextHandshakeMessageReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq)
*       *   [func (*NextHandshakeMessageReq) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.Descriptor)deprecated
    *   [func (x *NextHandshakeMessageReq) GetInBytes() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.GetInBytes)
    *   [func (x *NextHandshakeMessageReq) GetNetworkLatencyMs() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.GetNetworkLatencyMs)
    *   [func (*NextHandshakeMessageReq) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.ProtoMessage)
    *   [func (x *NextHandshakeMessageReq) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.ProtoReflect)
    *   [func (x *NextHandshakeMessageReq) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.Reset)
    *   [func (x *NextHandshakeMessageReq) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.String)

*   [type RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)
*       *   [func (*RpcProtocolVersions) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions.Descriptor)deprecated
    *   [func (x *RpcProtocolVersions) GetMaxRpcVersion() *RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions.GetMaxRpcVersion)
    *   [func (x *RpcProtocolVersions) GetMinRpcVersion() *RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions.GetMinRpcVersion)
    *   [func (*RpcProtocolVersions) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions.ProtoMessage)
    *   [func (x *RpcProtocolVersions) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions.ProtoReflect)
    *   [func (x *RpcProtocolVersions) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions.Reset)
    *   [func (x *RpcProtocolVersions) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions.String)

*   [type RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version)
*       *   [func (*RpcProtocolVersions_Version) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version.Descriptor)deprecated
    *   [func (x *RpcProtocolVersions_Version) GetMajor() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version.GetMajor)
    *   [func (x *RpcProtocolVersions_Version) GetMinor() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version.GetMinor)
    *   [func (*RpcProtocolVersions_Version) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version.ProtoMessage)
    *   [func (x *RpcProtocolVersions_Version) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version.ProtoReflect)
    *   [func (x *RpcProtocolVersions_Version) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version.Reset)
    *   [func (x *RpcProtocolVersions_Version) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version.String)

*   [type SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel)
*       *   [func (SecurityLevel) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel.Descriptor)
    *   [func (x SecurityLevel) Enum() *SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel.Enum)
    *   [func (SecurityLevel) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel.EnumDescriptor)deprecated
    *   [func (x SecurityLevel) Number() protoreflect.EnumNumber](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel.Number)
    *   [func (x SecurityLevel) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel.String)
    *   [func (SecurityLevel) Type() protoreflect.EnumType](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel.Type)

*   [type ServerHandshakeParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters)
*       *   [func (*ServerHandshakeParameters) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.Descriptor)deprecated
    *   [func (x *ServerHandshakeParameters) GetLocalIdentities() []*Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.GetLocalIdentities)
    *   [func (x *ServerHandshakeParameters) GetRecordProtocols() []string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.GetRecordProtocols)
    *   [func (x *ServerHandshakeParameters) GetToken() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.GetToken)
    *   [func (*ServerHandshakeParameters) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.ProtoMessage)
    *   [func (x *ServerHandshakeParameters) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.ProtoReflect)
    *   [func (x *ServerHandshakeParameters) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.Reset)
    *   [func (x *ServerHandshakeParameters) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.String)

*   [type StartClientHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq)
*       *   [func (*StartClientHandshakeReq) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.Descriptor)deprecated
    *   [func (x *StartClientHandshakeReq) GetAccessToken() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetAccessToken)
    *   [func (x *StartClientHandshakeReq) GetApplicationProtocols() []string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetApplicationProtocols)
    *   [func (x *StartClientHandshakeReq) GetHandshakeSecurityProtocol() HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetHandshakeSecurityProtocol)
    *   [func (x *StartClientHandshakeReq) GetLocalEndpoint() *Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetLocalEndpoint)
    *   [func (x *StartClientHandshakeReq) GetLocalIdentity() *Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetLocalIdentity)
    *   [func (x *StartClientHandshakeReq) GetMaxFrameSize() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetMaxFrameSize)
    *   [func (x *StartClientHandshakeReq) GetRecordProtocols() []string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetRecordProtocols)
    *   [func (x *StartClientHandshakeReq) GetRemoteEndpoint() *Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetRemoteEndpoint)
    *   [func (x *StartClientHandshakeReq) GetRpcVersions() *RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetRpcVersions)
    *   [func (x *StartClientHandshakeReq) GetTargetIdentities() []*Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetTargetIdentities)
    *   [func (x *StartClientHandshakeReq) GetTargetName() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetTargetName)
    *   [func (x *StartClientHandshakeReq) GetTransportProtocolPreferences() *TransportProtocolPreferences](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.GetTransportProtocolPreferences)
    *   [func (*StartClientHandshakeReq) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.ProtoMessage)
    *   [func (x *StartClientHandshakeReq) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.ProtoReflect)
    *   [func (x *StartClientHandshakeReq) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.Reset)
    *   [func (x *StartClientHandshakeReq) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.String)

*   [type StartServerHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq)
*       *   [func (*StartServerHandshakeReq) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.Descriptor)deprecated
    *   [func (x *StartServerHandshakeReq) GetApplicationProtocols() []string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetApplicationProtocols)
    *   [func (x *StartServerHandshakeReq) GetHandshakeParameters() map[int32]*ServerHandshakeParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetHandshakeParameters)
    *   [func (x *StartServerHandshakeReq) GetInBytes() []byte](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetInBytes)
    *   [func (x *StartServerHandshakeReq) GetLocalEndpoint() *Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetLocalEndpoint)
    *   [func (x *StartServerHandshakeReq) GetMaxFrameSize() uint32](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetMaxFrameSize)
    *   [func (x *StartServerHandshakeReq) GetRemoteEndpoint() *Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetRemoteEndpoint)
    *   [func (x *StartServerHandshakeReq) GetRpcVersions() *RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetRpcVersions)
    *   [func (x *StartServerHandshakeReq) GetTransportProtocolPreferences() *TransportProtocolPreferences](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.GetTransportProtocolPreferences)
    *   [func (*StartServerHandshakeReq) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.ProtoMessage)
    *   [func (x *StartServerHandshakeReq) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.ProtoReflect)
    *   [func (x *StartServerHandshakeReq) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.Reset)
    *   [func (x *StartServerHandshakeReq) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.String)

*   [type TransportProtocolPreferences](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences)
*       *   [func (*TransportProtocolPreferences) Descriptor() ([]byte, []int)](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences.Descriptor)deprecated
    *   [func (x *TransportProtocolPreferences) GetTransportProtocol() []string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences.GetTransportProtocol)
    *   [func (*TransportProtocolPreferences) ProtoMessage()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences.ProtoMessage)
    *   [func (x *TransportProtocolPreferences) ProtoReflect() protoreflect.Message](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences.ProtoReflect)
    *   [func (x *TransportProtocolPreferences) Reset()](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences.Reset)
    *   [func (x *TransportProtocolPreferences) String() string](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences.String)

*   [type UnimplementedHandshakerServiceServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#UnimplementedHandshakerServiceServer)
*       *   [func (UnimplementedHandshakerServiceServer) DoHandshake(grpc.BidiStreamingServer[HandshakerReq, HandshakerResp]) error](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#UnimplementedHandshakerServiceServer.DoHandshake)

*   [type UnsafeHandshakerServiceServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#UnsafeHandshakerServiceServer)

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker_grpc.pb.go#L38)

const (
 HandshakerService_DoHandshake_FullMethodName = "/grpc.gcp.HandshakerService/DoHandshake" )

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L53)

var (
 HandshakeProtocol_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "HANDSHAKE_PROTOCOL_UNSPECIFIED",
		1: "TLS",
		2: "ALTS",
	}
 HandshakeProtocol_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"HANDSHAKE_PROTOCOL_UNSPECIFIED": 0,
		"TLS":                            1,
		"ALTS":                           2,
	}
)

Enum value maps for HandshakeProtocol.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L102)

var (
 NetworkProtocol_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "NETWORK_PROTOCOL_UNSPECIFIED",
		1: "TCP",
		2: "UDP",
	}
 NetworkProtocol_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"NETWORK_PROTOCOL_UNSPECIFIED": 0,
		"TCP":                          1,
		"UDP":                          2,
	}
)

Enum value maps for NetworkProtocol.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/transport_security_common.pb.go#L52)

var (
 SecurityLevel_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "SECURITY_NONE",
		1: "INTEGRITY_ONLY",
		2: "INTEGRITY_AND_PRIVACY",
	}
 SecurityLevel_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"SECURITY_NONE":         0,
		"INTEGRITY_ONLY":        1,
		"INTEGRITY_AND_PRIVACY": 2,
	}
)

Enum value maps for SecurityLevel.

[View Source](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker_grpc.pb.go#L131)

var HandshakerService_ServiceDesc = [grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[ServiceDesc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#ServiceDesc){ 	ServiceName: "grpc.gcp.HandshakerService",
	HandlerType: (*[HandshakerServiceServer](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerServiceServer))([nil](https://pkg.go.dev/builtin#nil)),
	Methods:     [][grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[MethodDesc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#MethodDesc){},
	Streams: [][grpc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1).[StreamDesc](https://pkg.go.dev/google.golang.org/grpc@v1.79.1#StreamDesc){
		{
			StreamName:    "DoHandshake",
			Handler:       _HandshakerService_DoHandshake_Handler,
			ServerStreams: [true](https://pkg.go.dev/builtin#true),
			ClientStreams: [true](https://pkg.go.dev/builtin#true),
		},
	},
	Metadata: "grpc/gcp/handshaker.proto",
}

HandshakerService_ServiceDesc is the grpc.ServiceDesc for HandshakerService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

type AltsContext struct {

	ApplicationProtocol [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=application_protocol,json=applicationProtocol,proto3" json:"application_protocol,omitempty"`
	RecordProtocol [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=record_protocol,json=recordProtocol,proto3" json:"record_protocol,omitempty"`
	SecurityLevel [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel) `` 
	PeerServiceAccount [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=peer_service_account,json=peerServiceAccount,proto3" json:"peer_service_account,omitempty"`
	LocalServiceAccount [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=local_service_account,json=localServiceAccount,proto3" json:"local_service_account,omitempty"`
	PeerRpcVersions *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions) `protobuf:"bytes,6,opt,name=peer_rpc_versions,json=peerRpcVersions,proto3" json:"peer_rpc_versions,omitempty"`
	PeerAttributes map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `` 
	
}

Deprecated: Use AltsContext.ProtoReflect.Descriptor instead.

func (x *[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) GetApplicationProtocol() [string](https://pkg.go.dev/builtin#string)

func (x *[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) GetLocalServiceAccount() [string](https://pkg.go.dev/builtin#string)

func (x *[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) GetPeerRpcVersions() *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)

func (x *[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) GetPeerServiceAccount() [string](https://pkg.go.dev/builtin#string)

func (x *[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) GetRecordProtocol() [string](https://pkg.go.dev/builtin#string)

func (x *[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) GetSecurityLevel() [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel)

func (*[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) ProtoMessage()

func (x *[AltsContext](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#AltsContext)) Reset()

type Endpoint struct {

	
	IpAddress [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=ip_address,json=ipAddress,proto3" json:"ip_address,omitempty"`
	Port [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=port,proto3" json:"port,omitempty"`
	Protocol [NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol) `protobuf:"varint,3,opt,name=protocol,proto3,enum=grpc.gcp.NetworkProtocol" json:"protocol,omitempty"`
	
}

Deprecated: Use Endpoint.ProtoReflect.Descriptor instead.

func (x *[Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint)) GetProtocol() [NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol)

func (*[Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint)) ProtoMessage()

func (x *[Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint)) Reset()

#### type [HandshakeProtocol](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L41)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol "Go to HandshakeProtocol")

type HandshakeProtocol [int32](https://pkg.go.dev/builtin#int32)

const (
	HandshakeProtocol_HANDSHAKE_PROTOCOL_UNSPECIFIED [HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol) = 0
	HandshakeProtocol_TLS [HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol) = 1
	HandshakeProtocol_ALTS [HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol) = 2
)

#### func (HandshakeProtocol) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L76)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Descriptor "Go to HandshakeProtocol.Descriptor")added in v1.33.2

#### func (HandshakeProtocol) [Enum](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L66)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Enum "Go to HandshakeProtocol.Enum")added in v1.33.2

func (x [HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol)) Enum() *[HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol)

#### func (HandshakeProtocol) [EnumDescriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L89)deprecated

Deprecated: Use HandshakeProtocol.Descriptor instead.

#### func (HandshakeProtocol) [Number](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L84)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Number "Go to HandshakeProtocol.Number")added in v1.33.2

#### func (HandshakeProtocol) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L72)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.String "Go to HandshakeProtocol.String")

#### func (HandshakeProtocol) [Type](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L80)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol.Type "Go to HandshakeProtocol.Type")added in v1.33.2

#### type [HandshakerReq](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L697)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq "Go to HandshakerReq")

type HandshakerReq struct {

	
	
	
	
	ReqOneof isHandshakerReq_ReqOneof `protobuf_oneof:"req_oneof"`
	
}

#### func (*HandshakerReq) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L735)deprecated

Deprecated: Use HandshakerReq.ProtoReflect.Descriptor instead.

#### func (*HandshakerReq) [GetReqOneof](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L739)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.GetReqOneof "Go to HandshakerReq.GetReqOneof")

func (x *[HandshakerReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq)) GetReqOneof() isHandshakerReq_ReqOneof

#### func (*HandshakerReq) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L709)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq.Reset "Go to HandshakerReq.Reset")

func (x *[HandshakerReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq)) Reset()

#### type [HandshakerReq_ClientStart](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L777)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq_ClientStart "Go to HandshakerReq_ClientStart")

type HandshakerReq_ClientStart struct {
	ClientStart *[StartClientHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq) `protobuf:"bytes,1,opt,name=client_start,json=clientStart,proto3,oneof"`
}

#### type [HandshakerReq_Next](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L787)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq_Next "Go to HandshakerReq_Next")

type HandshakerReq_Next struct {
	Next *[NextHandshakeMessageReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq) `protobuf:"bytes,3,opt,name=next,proto3,oneof"`
}

#### type [HandshakerReq_ServerStart](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L782)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerReq_ServerStart "Go to HandshakerReq_ServerStart")

type HandshakerReq_ServerStart struct {
	ServerStart *[StartServerHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq) `protobuf:"bytes,2,opt,name=server_start,json=serverStart,proto3,oneof"`
}

#### type [HandshakerResp](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L973)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp "Go to HandshakerResp")

type HandshakerResp struct {

	
	
	
	
	OutFrames [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,1,opt,name=out_frames,json=outFrames,proto3" json:"out_frames,omitempty"`
	
	
	BytesConsumed [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,2,opt,name=bytes_consumed,json=bytesConsumed,proto3" json:"bytes_consumed,omitempty"`
	
	Result *[HandshakerResult](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult) `protobuf:"bytes,3,opt,name=result,proto3" json:"result,omitempty"`
	Status *[HandshakerStatus](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus) `protobuf:"bytes,4,opt,name=status,proto3" json:"status,omitempty"`
	
}

#### func (*HandshakerResp) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L1020)deprecated

Deprecated: Use HandshakerResp.ProtoReflect.Descriptor instead.

#### func (*HandshakerResp) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L994)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp.Reset "Go to HandshakerResp.Reset")

func (x *[HandshakerResp](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResp)) Reset()

#### type [HandshakerResult](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L798)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult "Go to HandshakerResult")

type HandshakerResult struct {

	ApplicationProtocol [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=application_protocol,json=applicationProtocol,proto3" json:"application_protocol,omitempty"`
	RecordProtocol [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=record_protocol,json=recordProtocol,proto3" json:"record_protocol,omitempty"`
	
	
	KeyData [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,3,opt,name=key_data,json=keyData,proto3" json:"key_data,omitempty"`
	PeerIdentity *[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity) `protobuf:"bytes,4,opt,name=peer_identity,json=peerIdentity,proto3" json:"peer_identity,omitempty"`
	LocalIdentity *[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity) `protobuf:"bytes,5,opt,name=local_identity,json=localIdentity,proto3" json:"local_identity,omitempty"`
	
	
	KeepChannelOpen [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=keep_channel_open,json=keepChannelOpen,proto3" json:"keep_channel_open,omitempty"`
	PeerRpcVersions *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions) `protobuf:"bytes,7,opt,name=peer_rpc_versions,json=peerRpcVersions,proto3" json:"peer_rpc_versions,omitempty"`
	MaxFrameSize [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,8,opt,name=max_frame_size,json=maxFrameSize,proto3" json:"max_frame_size,omitempty"`
	TransportProtocol *[NegotiatedTransportProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol) `protobuf:"bytes,9,opt,name=transport_protocol,json=transportProtocol,proto3" json:"transport_protocol,omitempty"`
	
}

#### func (*HandshakerResult) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L852)deprecated

Deprecated: Use HandshakerResult.ProtoReflect.Descriptor instead.

#### func (*HandshakerResult) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L826)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.Reset "Go to HandshakerResult.Reset")

func (x *[HandshakerResult](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult)) Reset()

#### func (*HandshakerResult) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L833)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerResult.String "Go to HandshakerResult.String")

#### type [HandshakerServiceServer](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker_grpc.pb.go#L79)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerServiceServer "Go to HandshakerServiceServer")

HandshakerServiceServer is the server API for HandshakerService service. All implementations must embed UnimplementedHandshakerServiceServer for forward compatibility.

#### type [HandshakerStatus](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L919)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus "Go to HandshakerStatus")

type HandshakerStatus struct {

	Code [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,1,opt,name=code,proto3" json:"code,omitempty"`
	Details [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=details,proto3" json:"details,omitempty"`
	
}

#### func (*HandshakerStatus) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L955)deprecated

Deprecated: Use HandshakerStatus.ProtoReflect.Descriptor instead.

#### func (*HandshakerStatus) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L929)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.Reset "Go to HandshakerStatus.Reset")

func (x *[HandshakerStatus](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus)) Reset()

#### func (*HandshakerStatus) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L936)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakerStatus.String "Go to HandshakerStatus.String")

type Identity struct {

	
	
	
	IdentityOneof isIdentity_IdentityOneof `protobuf_oneof:"identity_oneof"`
	Attributes map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `` 
	
}

Deprecated: Use Identity.ProtoReflect.Descriptor instead.

func (x *[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity)) GetIdentityOneof() isIdentity_IdentityOneof

func (x *[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity)) GetServiceAccount() [string](https://pkg.go.dev/builtin#string)

func (*[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity)) ProtoMessage()

func (x *[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity)) Reset()

type Identity_Hostname struct {
	Hostname [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=hostname,proto3,oneof"`
}

type Identity_ServiceAccount struct {
	ServiceAccount [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=service_account,json=serviceAccount,proto3,oneof"`
}

type NegotiatedTransportProtocol struct {
 TransportProtocol [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=transport_protocol,json=transportProtocol,proto3" json:"transport_protocol,omitempty"` 	
}

The negotiated transport protocol.

Deprecated: Use NegotiatedTransportProtocol.ProtoReflect.Descriptor instead.

func (*[NegotiatedTransportProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol)) ProtoMessage()

func (x *[NegotiatedTransportProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NegotiatedTransportProtocol)) Reset()

type NetworkProtocol [int32](https://pkg.go.dev/builtin#int32)

const (
 NetworkProtocol_NETWORK_PROTOCOL_UNSPECIFIED [NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol) = 0  NetworkProtocol_TCP [NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol) = 1  NetworkProtocol_UDP [NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol) = 2 )

func (x [NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol)) Enum() *[NetworkProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NetworkProtocol)

Deprecated: Use NetworkProtocol.Descriptor instead.

#### type [NextHandshakeMessageReq](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L639)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq "Go to NextHandshakeMessageReq")

type NextHandshakeMessageReq struct {

	
	
	InBytes [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,1,opt,name=in_bytes,json=inBytes,proto3" json:"in_bytes,omitempty"`
	
	
	NetworkLatencyMs [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,2,opt,name=network_latency_ms,json=networkLatencyMs,proto3" json:"network_latency_ms,omitempty"`
	
}

#### func (*NextHandshakeMessageReq) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L679)deprecated

Deprecated: Use NextHandshakeMessageReq.ProtoReflect.Descriptor instead.

#### func (*NextHandshakeMessageReq) [ProtoReflect](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L666)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.ProtoReflect "Go to NextHandshakeMessageReq.ProtoReflect")added in v1.33.2

#### func (*NextHandshakeMessageReq) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L653)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.Reset "Go to NextHandshakeMessageReq.Reset")

func (x *[NextHandshakeMessageReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq)) Reset()

#### func (*NextHandshakeMessageReq) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L660)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#NextHandshakeMessageReq.String "Go to NextHandshakeMessageReq.String")

type RpcProtocolVersions struct {

	MaxRpcVersion *[RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version) `protobuf:"bytes,1,opt,name=max_rpc_version,json=maxRpcVersion,proto3" json:"max_rpc_version,omitempty"`
	MinRpcVersion *[RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version) `protobuf:"bytes,2,opt,name=min_rpc_version,json=minRpcVersion,proto3" json:"min_rpc_version,omitempty"`
	
}

Max and min supported RPC protocol versions.

Deprecated: Use RpcProtocolVersions.ProtoReflect.Descriptor instead.

func (x *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)) GetMaxRpcVersion() *[RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version)

func (x *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)) GetMinRpcVersion() *[RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version)

func (*[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)) ProtoMessage()

func (x *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions)) Reset()

type RpcProtocolVersions_Version struct {
 Major [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,1,opt,name=major,proto3" json:"major,omitempty"`  Minor [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,2,opt,name=minor,proto3" json:"minor,omitempty"` 	
}

RPC version contains a major version and a minor version.

Deprecated: Use RpcProtocolVersions_Version.ProtoReflect.Descriptor instead.

func (*[RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version)) ProtoMessage()

func (x *[RpcProtocolVersions_Version](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions_Version)) Reset()

The security level of the created channel. The list is sorted in increasing level of security. This order must always be maintained.

const (
 SecurityLevel_SECURITY_NONE [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel) = 0  SecurityLevel_INTEGRITY_ONLY [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel) = 1  SecurityLevel_INTEGRITY_AND_PRIVACY [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel) = 2 )

func (x [SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel)) Enum() *[SecurityLevel](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#SecurityLevel)

Deprecated: Use SecurityLevel.Descriptor instead.

#### type [ServerHandshakeParameters](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L455)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters "Go to ServerHandshakeParameters")

type ServerHandshakeParameters struct {

	
	RecordProtocols [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=record_protocols,json=recordProtocols,proto3" json:"record_protocols,omitempty"`
	
	LocalIdentities []*[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity) `protobuf:"bytes,2,rep,name=local_identities,json=localIdentities,proto3" json:"local_identities,omitempty"`
	
	
	
	Token *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=token,proto3,oneof" json:"token,omitempty"`
	
}

#### func (*ServerHandshakeParameters) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L498)deprecated

Deprecated: Use ServerHandshakeParameters.ProtoReflect.Descriptor instead.

#### func (*ServerHandshakeParameters) [GetToken](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L516)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.GetToken "Go to ServerHandshakeParameters.GetToken")added in v1.64.0

#### func (*ServerHandshakeParameters) [ProtoReflect](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L485)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.ProtoReflect "Go to ServerHandshakeParameters.ProtoReflect")added in v1.33.2

#### func (*ServerHandshakeParameters) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L472)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.Reset "Go to ServerHandshakeParameters.Reset")

func (x *[ServerHandshakeParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters)) Reset()

#### func (*ServerHandshakeParameters) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L479)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters.String "Go to ServerHandshakeParameters.String")

#### type [StartClientHandshakeReq](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L299)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq "Go to StartClientHandshakeReq")

type StartClientHandshakeReq struct {

	HandshakeSecurityProtocol [HandshakeProtocol](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#HandshakeProtocol) `` 
	
	ApplicationProtocols [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,rep,name=application_protocols,json=applicationProtocols,proto3" json:"application_protocols,omitempty"`
	
	RecordProtocols [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,rep,name=record_protocols,json=recordProtocols,proto3" json:"record_protocols,omitempty"`
	
	
	TargetIdentities []*[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity) `protobuf:"bytes,4,rep,name=target_identities,json=targetIdentities,proto3" json:"target_identities,omitempty"`
	
	LocalIdentity *[Identity](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Identity) `protobuf:"bytes,5,opt,name=local_identity,json=localIdentity,proto3" json:"local_identity,omitempty"`
	
	LocalEndpoint *[Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint) `protobuf:"bytes,6,opt,name=local_endpoint,json=localEndpoint,proto3" json:"local_endpoint,omitempty"`
	
	RemoteEndpoint *[Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint) `protobuf:"bytes,7,opt,name=remote_endpoint,json=remoteEndpoint,proto3" json:"remote_endpoint,omitempty"`
	
	
	TargetName [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,opt,name=target_name,json=targetName,proto3" json:"target_name,omitempty"`
	RpcVersions *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions) `protobuf:"bytes,9,opt,name=rpc_versions,json=rpcVersions,proto3" json:"rpc_versions,omitempty"`
	MaxFrameSize [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,10,opt,name=max_frame_size,json=maxFrameSize,proto3" json:"max_frame_size,omitempty"`
	
	
	
	AccessToken [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=access_token,json=accessToken,proto3" json:"access_token,omitempty"`
	TransportProtocolPreferences *[TransportProtocolPreferences](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences) `` 
	
}

#### func (*StartClientHandshakeReq) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L367)deprecated

Deprecated: Use StartClientHandshakeReq.ProtoReflect.Descriptor instead.

#### func (*StartClientHandshakeReq) [ProtoReflect](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L354)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.ProtoReflect "Go to StartClientHandshakeReq.ProtoReflect")added in v1.33.2

#### func (*StartClientHandshakeReq) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L341)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.Reset "Go to StartClientHandshakeReq.Reset")

func (x *[StartClientHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq)) Reset()

#### func (*StartClientHandshakeReq) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L348)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartClientHandshakeReq.String "Go to StartClientHandshakeReq.String")

#### type [StartServerHandshakeReq](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L523)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq "Go to StartServerHandshakeReq")

type StartServerHandshakeReq struct {

	
	ApplicationProtocols [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=application_protocols,json=applicationProtocols,proto3" json:"application_protocols,omitempty"`
	
	
	
	
	HandshakeParameters map[[int32](https://pkg.go.dev/builtin#int32)]*[ServerHandshakeParameters](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#ServerHandshakeParameters) `` 
	
	InBytes [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,3,opt,name=in_bytes,json=inBytes,proto3" json:"in_bytes,omitempty"`
	
	LocalEndpoint *[Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint) `protobuf:"bytes,4,opt,name=local_endpoint,json=localEndpoint,proto3" json:"local_endpoint,omitempty"`
	
	RemoteEndpoint *[Endpoint](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#Endpoint) `protobuf:"bytes,5,opt,name=remote_endpoint,json=remoteEndpoint,proto3" json:"remote_endpoint,omitempty"`
	RpcVersions *[RpcProtocolVersions](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#RpcProtocolVersions) `protobuf:"bytes,6,opt,name=rpc_versions,json=rpcVersions,proto3" json:"rpc_versions,omitempty"`
	MaxFrameSize [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,7,opt,name=max_frame_size,json=maxFrameSize,proto3" json:"max_frame_size,omitempty"`
	TransportProtocolPreferences *[TransportProtocolPreferences](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences) `` 
	
}

#### func (*StartServerHandshakeReq) [Descriptor](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L579)deprecated

Deprecated: Use StartServerHandshakeReq.ProtoReflect.Descriptor instead.

#### func (*StartServerHandshakeReq) [ProtoReflect](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L566)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.ProtoReflect "Go to StartServerHandshakeReq.ProtoReflect")added in v1.33.2

#### func (*StartServerHandshakeReq) [Reset](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L553)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.Reset "Go to StartServerHandshakeReq.Reset")

func (x *[StartServerHandshakeReq](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq)) Reset()

#### func (*StartServerHandshakeReq) [String](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker.pb.go#L560)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#StartServerHandshakeReq.String "Go to StartServerHandshakeReq.String")

type TransportProtocolPreferences struct {
 TransportProtocol [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=transport_protocol,json=transportProtocol,proto3" json:"transport_protocol,omitempty"` 	
}

The ordered list of protocols that the client wishes to use, or the set that the server supports.

Deprecated: Use TransportProtocolPreferences.ProtoReflect.Descriptor instead.

func (*[TransportProtocolPreferences](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences)) ProtoMessage()

func (x *[TransportProtocolPreferences](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#TransportProtocolPreferences)) Reset()

#### type [UnimplementedHandshakerServiceServer](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker_grpc.pb.go#L95)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#UnimplementedHandshakerServiceServer "Go to UnimplementedHandshakerServiceServer")added in v1.24.0

type UnimplementedHandshakerServiceServer struct{}

UnimplementedHandshakerServiceServer must be embedded to have forward compatible implementations.

NOTE: this should be embedded by value instead of pointer to avoid a nil pointer dereference when methods are called.

#### func (UnimplementedHandshakerServiceServer) [DoHandshake](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker_grpc.pb.go#L97)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#UnimplementedHandshakerServiceServer.DoHandshake "Go to UnimplementedHandshakerServiceServer.DoHandshake")added in v1.24.0

#### type [UnsafeHandshakerServiceServer](https://github.com/grpc/grpc-go/blob/v1.79.1/credentials/alts/internal/proto/grpc_gcp/handshaker_grpc.pb.go#L106)[¶](https://pkg.go.dev/google.golang.org/grpc@v1.79.1/credentials/alts/internal/proto/grpc_gcp#UnsafeHandshakerServiceServer "Go to UnsafeHandshakerServiceServer")added in v1.33.0

type UnsafeHandshakerServiceServer interface {
	
}

UnsafeHandshakerServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to HandshakerServiceServer will result in compilation errors.
