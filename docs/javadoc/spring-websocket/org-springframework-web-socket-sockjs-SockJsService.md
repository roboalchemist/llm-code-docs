# Interface SockJsService

All Known Implementing Classes:
`AbstractSockJsService, DefaultSockJsService, TransportHandlingSockJsService`

---

public interface SockJsService
The main entry point for processing HTTP requests from SockJS clients.

In a Servlet 3+ container, `SockJsHttpRequestHandler`
can be used to invoke this service. The processing servlet, as well as all filters involved,
must have asynchronous support enabled through the ServletContext API or by adding an
`<async-support>true</async-support>` element to servlet and filter declarations
in web.xml.

Since:
4.0
Author:
Rossen Stoyanchev
See Also:

- `SockJsHttpRequestHandler`

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`handleRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 @Nullable String sockJsPath,
 WebSocketHandler handler)`

Process a SockJS HTTP request.

- 

## Method Details

  - 

### handleRequest

void handleRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 @Nullable String sockJsPath,
 WebSocketHandler handler)
            throws SockJsException
Process a SockJS HTTP request.

See the "Base URL", "Static URLs", and "Session URLs" sections of the SockJS
protocol for details on the types of URLs expected.

Parameters:
`request` - the current request
`response` - the current response
`sockJsPath` - the remainder of the path within the SockJS service prefix
`handler` - the handler that will exchange messages with the SockJS client
Throws:
`SockJsException` - raised when request processing fails; generally, failed
attempts to send messages to clients automatically close the SockJS session
and raise `SockJsTransportFailureException`; failed attempts to read
messages from clients do not automatically close the session and may result
in `SockJsMessageDeliveryException` or `SockJsException`;
exceptions from the WebSocketHandler can be handled internally or through
`ExceptionWebSocketHandlerDecorator` or some alternative decorator.
The former is automatically added when using
`SockJsHttpRequestHandler`.