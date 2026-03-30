# Interface TransportHandler

All Known Implementing Classes:
`AbstractHttpReceivingTransportHandler, AbstractHttpSendingTransportHandler, AbstractTransportHandler, EventSourceTransportHandler, HtmlFileTransportHandler, WebSocketTransportHandler, XhrPollingTransportHandler, XhrReceivingTransportHandler, XhrStreamingTransportHandler`

---

public interface TransportHandler
Handle a SockJS session URL, i.e. transport-specific request.

Since:
4.0
Author:
Rossen Stoyanchev, Juergen Hoeller

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`checkSessionType(SockJsSession session)`

Check whether the type of the given session matches the transport type
of this `TransportHandler` where session id and the transport type
are extracted from the SockJS URL.

`TransportType`
`getTransportType()`

Return the transport type supported by this handler.

`void`
`handleRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 WebSocketHandler handler,
 SockJsSession session)`

Handle the given request and delegate messages to the provided
`WebSocketHandler`.

`void`
`initialize(SockJsServiceConfig serviceConfig)`

Initialize this handler with the given configuration.

- 

## Method Details

  - 

### initialize

void initialize(SockJsServiceConfig serviceConfig)
Initialize this handler with the given configuration.

Parameters:
`serviceConfig` - the configuration as defined by the containing
`SockJsService`

  - 

### getTransportType

TransportType getTransportType()
Return the transport type supported by this handler.

  - 

### checkSessionType

boolean checkSessionType(SockJsSession session)
Check whether the type of the given session matches the transport type
of this `TransportHandler` where session id and the transport type
are extracted from the SockJS URL.

Returns:
`true` if the session matches (and would therefore get
accepted by `handleRequest(ServerHttpRequest, ServerHttpResponse, WebSocketHandler, SockJsSession)`), or `false` otherwise
Since:
4.3.4

  - 

### handleRequest

void handleRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 WebSocketHandler handler,
 SockJsSession session)
            throws SockJsException
Handle the given request and delegate messages to the provided
`WebSocketHandler`.

Parameters:
`request` - the current request
`response` - the current response
`handler` - the target WebSocketHandler (never `null`)
`session` - the SockJS session (never `null`)
Throws:
`SockJsException` - raised when request processing fails as
explained in `SockJsService`