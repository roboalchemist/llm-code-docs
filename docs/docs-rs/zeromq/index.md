# Crate zeromq 
Source 
## Modules§
preludeRe-exports important traits. Consider glob-importing.util
## Structs§
DealerRecvHalfThe recv half of a `DealerSocket` produced by `DealerSocket::split`.DealerSendHalfThe send half of a `DealerSocket` produced by `DealerSocket::split`.DealerSocketPubSocketPullSocketPushSocketRepSocketReqSocketRouterRecvHalfThe recv half of a `RouterSocket` produced by `RouterSocket::split`.RouterSendHalfThe send half of a `RouterSocket` produced by `RouterSocket::split`.RouterSocketSocketOptionsSubSocketXPubSocketZmqEmptyMessageErrorZmqMessage
## Enums§
EndpointRepresents a ZMQ Endpoint.HostRepresents a host address. Does not include the port, and may be either an
ip address or a domain nameSocketEventSocketTypeSubBackendMsgTypeTransportThe type of transport used by a given endpointZmqError
## Traits§
CaptureSocketMarker trait that express the fact that only certain types of sockets might be used
in proxy function as a capture parameterMultiPeerBackendSocketSocketBackendSocketRecvSocketSendTryIntoEndpointRepresents a type that can be converted into an `Endpoint`.
## Functions§
proxy
## Type Aliases§
ZmqResult