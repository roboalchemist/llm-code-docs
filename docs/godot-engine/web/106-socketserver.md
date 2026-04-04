# SocketServer

# SocketServer

Inherits:RefCounted<Object
Inherited By:TCPServer,UDSServer
An abstract class for servers based on sockets.

## Description

A socket server.

## Methods

| bool | is_connection_available()const |
|---|---|
| bool | is_listening()const |
| void | stop() |
| StreamPeerSocket | take_socket_connection() |

bool
is_connection_available()const
bool
is_listening()const
void
stop()
StreamPeerSocket
take_socket_connection()

## Method Descriptions

boolis_connection_available()const🔗
Returnstrueif a connection is available for taking.
boolis_listening()const🔗
Returnstrueif the server is currently listening for connections.
voidstop()🔗
Stops listening.
StreamPeerSockettake_socket_connection()🔗
If a connection is available, returns a StreamPeerSocket with the connection.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
