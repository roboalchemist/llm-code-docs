# StreamPeerSocket

# StreamPeerSocket

Inherits:StreamPeer<RefCounted<Object
Inherited By:StreamPeerTCP,StreamPeerUDS
Abstract base class for interacting with socket streams.

## Description

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.

## Methods

| void | disconnect_from_host() |
|---|---|
| Status | get_status()const |
| Error | poll() |

void
disconnect_from_host()
Status
get_status()const
Error
poll()

## Enumerations

enumStatus:🔗
StatusSTATUS_NONE=0
The initial status of theStreamPeerSocket. This is also the status after disconnecting.
StatusSTATUS_CONNECTING=1
A status representing aStreamPeerSocketthat is connecting to a host.
StatusSTATUS_CONNECTED=2
A status representing aStreamPeerSocketthat is connected to a host.
StatusSTATUS_ERROR=3
A status representing aStreamPeerSocketin error state.

## Method Descriptions

voiddisconnect_from_host()🔗
Disconnects from host.
Statusget_status()const🔗
Returns the status of the connection.
Errorpoll()🔗
Polls the socket, updating its state. Seeget_status().

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
