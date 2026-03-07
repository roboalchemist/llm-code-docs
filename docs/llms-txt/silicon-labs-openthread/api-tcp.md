# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-tcp.md

# TCP

This module includes functions that control TCP communication. 

## Modules

[otLinkedBuffer](ot-linked-buffer)

[otTcpEndpoint](ot-tcp-endpoint)

[otTcpEndpointInitializeArgs](ot-tcp-endpoint-initialize-args)

[otTcpListener](ot-tcp-listener)

[otTcpListenerInitializeArgs](ot-tcp-listener-initialize-args)

## Enumerations

### otTcpDisconnectedReason

```
enum otTcpDisconnectedReason {
    OT_TCP_DISCONNECTED_REASON_NORMAL
    OT_TCP_DISCONNECTED_REASON_REFUSED
    OT_TCP_DISCONNECTED_REASON_RESET
    OT_TCP_DISCONNECTED_REASON_TIME_WAIT
    OT_TCP_DISCONNECTED_REASON_TIMED_OUT
}
```

**Enumerator:**

|   |   |
|---|---|
|OT_TCP_DISCONNECTED_REASON_NORMAL||
|OT_TCP_DISCONNECTED_REASON_REFUSED||
|OT_TCP_DISCONNECTED_REASON_RESET||
|OT_TCP_DISCONNECTED_REASON_TIME_WAIT||
|OT_TCP_DISCONNECTED_REASON_TIMED_OUT||

### @19

```
enum @19 {
    OT_TCP_CONNECT_NO_FAST_OPEN = 1 << 0
}
```

**Description:**

Defines flags passed to [otTcpConnect()](api-tcp#ot-tcp-connect).

**Enumerator:**

|   |   |
|---|---|
|OT_TCP_CONNECT_NO_FAST_OPEN||

### @20

```
enum @20 {
    OT_TCP_SEND_MORE_TO_COME = 1 << 0
}
```

**Description:**

Defines flags passed to `otTcpSendByReference`.

**Enumerator:**

|   |   |
|---|---|
|OT_TCP_SEND_MORE_TO_COME||

### otTcpIncomingConnectionAction

```
enum otTcpIncomingConnectionAction {
    OT_TCP_INCOMING_CONNECTION_ACTION_ACCEPT
    OT_TCP_INCOMING_CONNECTION_ACTION_DEFER
    OT_TCP_INCOMING_CONNECTION_ACTION_REFUSE
}
```

**Description:**

Defines incoming connection actions.

**Details:**

This is used in [otTcpAcceptReady()](api-tcp#ot-tcp-accept-ready) callback.

**Enumerator:**

|   |   |
|---|---|
|OT_TCP_INCOMING_CONNECTION_ACTION_ACCEPT|Accept the incoming connection.|
|OT_TCP_INCOMING_CONNECTION_ACTION_DEFER|Defer (silently ignore) the incoming connection.|
|OT_TCP_INCOMING_CONNECTION_ACTION_REFUSE|Refuse the incoming connection.|

## Typedefs

### otLinkedBuffer

`typedef struct otLinkedBuffer otLinkedBuffer`

**Description:**

A linked buffer structure for use with TCP.

**Details:**

A single [otLinkedBuffer](ot-linked-buffer) structure references an array of bytes in memory, via mData and mLength. The mNext field is used to form a chain of [otLinkedBuffer](ot-linked-buffer) structures.

### otTcpEndpoint

`typedef struct otTcpEndpoint otTcpEndpoint`

### otTcpEstablished

`typedef void(* otTcpEstablished) (otTcpEndpoint *aEndpoint)`

**Description:**

This callback informs the application that the TCP 3-way handshake is complete and that the connection is now established.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aEndpoint|The TCP endpoint whose connection is now established.|

**Details:**

### otTcpSendDone

`typedef void(* otTcpSendDone) (otTcpEndpoint *aEndpoint, otLinkedBuffer *aData)`

**Description:**

This callback informs the application that data in the provided `aData` have been acknowledged by the connection peer and that `aData` and the data it contains can be reclaimed by the application.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aEndpoint|The TCP endpoint for the connection.|
||[in]|aData|A pointer to the [otLinkedBuffer](ot-linked-buffer) that can be reclaimed.|

**Details:**

The `aData` are guaranteed to be identical to those passed in to TCP via [otTcpSendByReference()](api-tcp#ot-tcp-send-by-reference), including any extensions effected via [otTcpSendByExtension()](api-tcp#ot-tcp-send-by-extension).

### otTcpForwardProgress

`typedef void(* otTcpForwardProgress) (otTcpEndpoint *aEndpoint, size_t aInSendBuffer, size_t aBacklog)`

**Description:**

This callback informs the application if forward progress has been made in transferring data from the send buffer to the recipient.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aEndpoint|The TCP endpoint for the connection.|
||[in]|aInSendBuffer|The number of bytes in the send buffer (sum of "in-flight" and "backlog" regions).|
||[in]|aBacklog|The number of bytes that are queued for sending but have not yet been sent (the "backlog" region).|

**Details:**

This callback is not necessary for correct TCP operation. Most applications can just rely on the [otTcpSendDone()](api-tcp#ot-tcp-send-done) callback to reclaim linked buffers once the TCP stack is done using them. The purpose of this callback is to support advanced applications that benefit from finer-grained information about how the the connection is making forward progress in transferring data to the connection peer.

This callback's operation is closely tied to TCP's send buffer. The send buffer can be understood as having two regions. First, there is the "in-flight" region at the head (front) of the send buffer. It corresponds to data which has been sent to the recipient, but is not yet acknowledged. Second, there is the "backlog" region, which consists of all data in the send buffer that is not in the "in-flight" region. The "backlog" region corresponds to data that is queued for sending, but has not yet been sent.

The callback is invoked in response to two types of events. First, the "in-flight" region of the send buffer may shrink (e.g., when the recipient acknowledges data that we sent earlier). Second, the "backlog" region of the send buffer may shrink (e.g., new data was sent out). These two conditions often occur at the same time, in response to an ACK segment from the connection peer, which is why they are combined in a single callback.

The TCP stack only uses the `aInSendBuffer` bytes at the tail of the send buffer; when `aInSendBuffer` decreases by an amount x, it means that x additional bytes that were formerly at the head of the send buffer are no longer part of the send buffer and can now be reclaimed (i.e., overwritten) by the application. Note that the [otLinkedBuffer](ot-linked-buffer) structure itself can only be reclaimed once all bytes that it references are no longer part of the send buffer.

This callback subsumes [otTcpSendDone()](api-tcp#ot-tcp-send-done), in the following sense: applications can determine when linked buffers can be reclaimed by comparing `aInSendBuffer` with how many bytes are in each linked buffer. However, we expect [otTcpSendDone()](api-tcp#ot-tcp-send-done), which directly conveys which otLinkedBuffers can be reclaimed, to be much simpler to use. If both callbacks are registered and are triggered by the same event (e.g., the same ACK segment received), then the [otTcpSendDone()](api-tcp#ot-tcp-send-done) callback will be triggered first, followed by this callback.

Additionally, this callback provides `aBacklog`, which indicates how many bytes of data in the send buffer are not yet in flight. For applications that only want to add data to the send buffer when there is an assurance that it will be sent out soon, it may be desirable to only send out data when `aBacklog` is suitably small (0 or close to 0). For example, an application may use `aBacklog` so that it can react to queue buildup by dropping or aggregating data to avoid creating a backlog of data.

After a call to [otTcpSendByReference()](api-tcp#ot-tcp-send-by-reference) or [otTcpSendByExtension()](api-tcp#ot-tcp-send-by-extension) with a positive number of bytes, the [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback is guaranteed to be called, to indicate when the bytes that were added to the send buffer are sent out. The call to [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) may be made immediately after the bytes are added to the send buffer (if some of those bytes are immediately sent out, reducing the backlog), or sometime in the future (once the connection sends out some or all of the data, reducing the backlog). By "immediately," we mean that the callback is immediately scheduled for execution in a tasklet; to avoid reentrancy-related complexity, the [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback is never directly called from the [otTcpSendByReference()](api-tcp#ot-tcp-send-by-reference) or [otTcpSendByExtension()](api-tcp#ot-tcp-send-by-extension) functions.

### otTcpReceiveAvailable

`typedef void(* otTcpReceiveAvailable) (otTcpEndpoint *aEndpoint, size_t aBytesAvailable, bool aEndOfStream, size_t aBytesRemaining)`

**Description:**

This callback indicates the number of bytes available for consumption from the receive buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aEndpoint|The TCP endpoint for the connection.|
||[in]|aBytesAvailable|The number of bytes in the connection's receive buffer.|
||[in]|aEndOfStream|Indicates if additional data, beyond what is already in the connection's receive buffer, can be received.|
||[in]|aBytesRemaining|The number of additional bytes that can be received before the receive buffer becomes full.|

**Details:**

It is called whenever bytes are added to the receive buffer and when the end of stream is reached. If the end of the stream has been reached (i.e., if no more data will become available to read because the connection peer has closed their end of the connection for writing), then `aEndOfStream` is true. Finally, `aBytesRemaining` indicates how much capacity is left in the receive buffer to hold additional data that arrives.

### otTcpDisconnectedReason

`typedef enum otTcpDisconnectedReason otTcpDisconnectedReason`

### otTcpDisconnected

`typedef void(* otTcpDisconnected) (otTcpEndpoint *aEndpoint, otTcpDisconnectedReason aReason)`

**Description:**

This callback indicates that the connection was broken and should no longer be used, or that a connection has entered the TIME-WAIT state.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aEndpoint|The TCP endpoint whose connection has been lost.|
||[in]|aReason|The reason why the connection was lost.|

**Details:**

It can occur if a connection establishment attempt (initiated by calling [otTcpConnect()](api-tcp#ot-tcp-connect)) fails, or any point thereafter (e.g., if the connection times out or an RST segment is received from the connection peer). Once this callback fires, all resources that the application provided for this connection (i.e., any `otLinkedBuffers` and memory they reference, but not the TCP endpoint itself or space for the receive buffers) can be reclaimed. In the case of a connection entering the TIME-WAIT state, this callback is called twice, once upon entry into the TIME-WAIT state (with OT_TCP_DISCONNECTED_REASON_TIME_WAIT, and again when the TIME-WAIT state expires (with OT_TCP_DISCONNECTED_REASON_NORMAL).

### otTcpEndpointInitializeArgs

`typedef struct otTcpEndpointInitializeArgs otTcpEndpointInitializeArgs`

**Description:**

Contains arguments to the [otTcpEndpointInitialize()](api-tcp#ot-tcp-endpoint-initialize) function.

### otTcpListener

`typedef struct otTcpListener otTcpListener`

### otTcpIncomingConnectionAction

`typedef enum otTcpIncomingConnectionAction otTcpIncomingConnectionAction`

**Description:**

Defines incoming connection actions.

**Details:**

This is used in [otTcpAcceptReady()](api-tcp#ot-tcp-accept-ready) callback.

### otTcpAcceptReady

`typedef otTcpIncomingConnectionAction(* otTcpAcceptReady) (otTcpListener *aListener, const otSockAddr *aPeer, otTcpEndpoint **aAcceptInto)`

**Description:**

This callback indicates that an incoming connection that matches this TCP listener has arrived.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aListener|The TCP listener that matches the incoming connection.|
||[in]|aPeer|The host and port from which the incoming connection originates.|
||[out]|aAcceptInto|The TCP endpoint into which to accept the incoming connection.|

**Details:**

The typical response is for the application to accept the incoming connection. It does so by populating `aAcceptInto` with a pointer to the [otTcpEndpoint](ot-tcp-endpoint) into which to accept the incoming connection. This [otTcpEndpoint](ot-tcp-endpoint) must already be initialized using [otTcpEndpointInitialize()](api-tcp#ot-tcp-endpoint-initialize). Then, the application returns OT_TCP_INCOMING_CONNECTION_ACTION_ACCEPT.

Alternatively, the application can decline to accept the incoming connection. There are two ways for the application to do this. First, if the application returns OT_TCP_INCOMING_CONNECTION_ACTION_DEFER, then OpenThread silently ignores the connection establishment request; the connection peer will likely retransmit the request, at which point the callback will be called again. This is valuable if resources are not presently available to accept the connection, but they may be available when the connection peer retransmits its connection establishment attempt. Second, if the application returns OT_TCP_INCOMING_CONNECTION_ACTION_REFUSE, then OpenThread sends a "connection refused" message to the host that attempted to establish a connection. If the application declines the incoming connection, it is not required to populate `aAcceptInto`.

**Returns**

- Description of how to handle the incoming connection.

### otTcpAcceptDone

`typedef void(* otTcpAcceptDone) (otTcpListener *aListener, otTcpEndpoint *aEndpoint, const otSockAddr *aPeer)`

**Description:**

This callback indicates that the TCP connection is now ready for two-way communication.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aListener|The TCP listener that matches the incoming connection.|
||[in]|aEndpoint|The TCP endpoint into which the incoming connection was accepted.|
||[in]|aPeer|the host and port from which the incoming connection originated.|

**Details:**

In the case of TCP Fast Open, this may be before the TCP connection handshake has actually completed. The application is provided with the context pointers both for the TCP listener that accepted the connection and the TCP endpoint into which it was accepted. The provided context is the one associated with the TCP listener.

### otTcpListenerInitializeArgs

`typedef struct otTcpListenerInitializeArgs otTcpListenerInitializeArgs`

**Description:**

Contains arguments to the [otTcpListenerInitialize()](api-tcp#ot-tcp-listener-initialize) function.

## Functions

### otTcpEndpointInitialize

`otError otTcpEndpointInitialize(otInstance *aInstance, otTcpEndpoint *aEndpoint, const otTcpEndpointInitializeArgs *aArgs)`

**Description:** Initializes a TCP endpoint.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to a TCP endpoint structure.|
|const [otTcpEndpointInitializeArgs](ot-tcp-endpoint-initialize-args) *|[in]|aArgs|A pointer to a structure of arguments.|

Calling this function causes OpenThread to keep track of the TCP endpoint and store and retrieve TCP data inside the `aEndpoint`. The application should refrain from directly accessing or modifying the fields in `aEndpoint`. If the application needs to reclaim the memory backing `aEndpoint`, it should call [otTcpEndpointDeinitialize()](api-tcp#ot-tcp-endpoint-deinitialize).

### otTcpEndpointGetInstance

`otInstance * otTcpEndpointGetInstance(otTcpEndpoint *aEndpoint)`

**Description:** Obtains the otInstance that was associated with `aEndpoint` upon initialization.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|The TCP endpoint whose instance to obtain.|

**Returns**

- The otInstance pointer associated with `aEndpoint`.

### otTcpEndpointGetContext

`void * otTcpEndpointGetContext(otTcpEndpoint *aEndpoint)`

**Description:** Obtains the context pointer that was associated with `aEndpoint` upon initialization.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|The TCP endpoint whose context to obtain.|

**Returns**

- The context pointer associated with `aEndpoint`.

### otTcpGetLocalAddress

`const otSockAddr * otTcpGetLocalAddress(const otTcpEndpoint *aEndpoint)`

**Description:** Obtains a pointer to a TCP endpoint's local host and port.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|The TCP endpoint whose local host and port to obtain.|

The contents of the host and port may be stale if this socket is not in a connected state and has not been bound after it was last disconnected.

**Returns**

- The local host and port of `aEndpoint`.

### otTcpGetPeerAddress

`const otSockAddr * otTcpGetPeerAddress(const otTcpEndpoint *aEndpoint)`

**Description:** Obtains a pointer to a TCP endpoint's peer's host and port.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|The TCP endpoint whose peer's host and port to obtain.|

The contents of the host and port may be stale if this socket is not in a connected state.

**Returns**

- The host and port of the connection peer of `aEndpoint`.

### otTcpBind

`otError otTcpBind(otTcpEndpoint *aEndpoint, const otSockAddr *aSockName)`

**Description:** Binds the TCP endpoint to an IP address and port.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure to bind.|
|const [otSockAddr](ot-sock-addr) *|[in]|aSockName|The address and port to which to bind this TCP endpoint.|

### otTcpConnect

`otError otTcpConnect(otTcpEndpoint *aEndpoint, const otSockAddr *aSockName, uint32_t aFlags)`

**Description:** Records the remote host and port for this connection.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure to connect.|
|const [otSockAddr](ot-sock-addr) *|[in]|aSockName|The IP address and port of the host to which to connect.|
|uint32_t|[in]|aFlags|Flags specifying options for this operation (see enumeration above).|

TCP Fast Open must be enabled or disabled using `aFlags`. If it is disabled, then the TCP connection establishment handshake is initiated immediately. If it is enabled, then this function merely records the the remote host and port, and the TCP connection establishment handshake only happens on the first call to `otTcpSendByReference()`.

If TCP Fast Open is disabled, then the caller must wait for the `otTcpEstablished` callback indicating that TCP connection establishment handshake is done before it can start sending data e.g., by calling `otTcpSendByReference()`.

### otTcpSendByReference

`otError otTcpSendByReference(otTcpEndpoint *aEndpoint, otLinkedBuffer *aBuffer, uint32_t aFlags)`

**Description:** Adds data referenced by the linked buffer pointed to by `aBuffer` to the send buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure representing the TCP endpoint on which to send data.|
|[otLinkedBuffer](ot-linked-buffer) *|[in]|aBuffer|A pointer to the linked buffer chain referencing data to add to the send buffer.|
|uint32_t|[in]|aFlags|Flags specifying options for this operation (see enumeration above).|

Upon a successful call to this function, the linked buffer and data it references are owned by the TCP stack; they should not be modified by the application until a "send done" callback returns ownership of those objects to the application. It is acceptable to call this function to add another linked buffer to the send queue, even if the "send done" callback for a previous invocation of this function has not yet fired.

Note that `aBuffer` should not be chained; its mNext field should be NULL. If additional data will be added right after this call, then the OT_TCP_SEND_MORE_TO_COME flag should be used as a hint to the TCP implementation.

### otTcpSendByExtension

`otError otTcpSendByExtension(otTcpEndpoint *aEndpoint, size_t aNumBytes, uint32_t aFlags)`

**Description:** Adds data to the send buffer by extending the length of the final [otLinkedBuffer](ot-linked-buffer) in the send buffer by the specified amount.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure representing the TCP endpoint on which to send data.|
|size_t|[in]|aNumBytes|The number of bytes by which to extend the length of the final linked buffer.|
|uint32_t|[in]|aFlags|Flags specifying options for this operation (see enumeration above).|

If the send buffer is empty, then the operation fails.

### otTcpReceiveByReference

`otError otTcpReceiveByReference(otTcpEndpoint *aEndpoint, const otLinkedBuffer **aBuffer)`

**Description:** Provides the application with a linked buffer chain referencing data currently in the TCP receive buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure representing the TCP endpoint on which to receive data.|
|const [otLinkedBuffer](ot-linked-buffer) **|[out]|aBuffer|A pointer to the linked buffer chain referencing data currently in the receive buffer.|

The linked buffer chain is valid until the "receive ready" callback is next invoked, or until the next call to [otTcpReceiveContiguify()](api-tcp#ot-tcp-receive-contiguify) or [otTcpCommitReceive()](api-tcp#ot-tcp-commit-receive).

### otTcpReceiveContiguify

`otError otTcpReceiveContiguify(otTcpEndpoint *aEndpoint)`

**Description:** Reorganizes the receive buffer to be entirely contiguous in memory.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint whose receive buffer to reorganize.|

This is optional; an application can simply traverse the linked buffer chain obtained by calling `otTcpReceiveByReference`. Some applications may wish to call this function to make the receive buffer contiguous to simplify their data processing, but this comes at the expense of CPU time to reorganize the data in the receive buffer.

### otTcpCommitReceive

`otError otTcpCommitReceive(otTcpEndpoint *aEndpoint, size_t aNumBytes, uint32_t aFlags)`

**Description:** Informs the TCP stack that the application has finished processing `aNumBytes` bytes of data at the start of the receive buffer and that the TCP stack need not continue maintaining those bytes in the receive buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure representing the TCP endpoint on which to receive data.|
|size_t|[in]|aNumBytes|The number of bytes consumed.|
|uint32_t|[in]|aFlags|Flags specifying options for this operation (none yet).|

### otTcpSendEndOfStream

`otError otTcpSendEndOfStream(otTcpEndpoint *aEndpoint)`

**Description:** Informs the connection peer that this TCP endpoint will not send more data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure representing the TCP endpoint to shut down.|

This should be used when the application has no more data to send to the connection peer. For this connection, future reads on the connection peer will result in the "end of stream" condition, and future writes on this connection endpoint will fail.

The "end of stream" condition only applies after any data previously provided to the TCP stack to send out has been received by the connection peer.

### otTcpAbort

`otError otTcpAbort(otTcpEndpoint *aEndpoint)`

**Description:** Forcibly ends the TCP connection associated with this TCP endpoint.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure representing the TCP endpoint to abort.|

This immediately makes the TCP endpoint free for use for another connection and empties the send and receive buffers, transferring ownership of any data provided by the application in [otTcpSendByReference()](api-tcp#ot-tcp-send-by-reference) and [otTcpSendByExtension()](api-tcp#ot-tcp-send-by-extension) calls back to the application. The TCP endpoint's callbacks and memory for the receive buffer remain associated with the TCP endpoint.

### otTcpEndpointDeinitialize

`otError otTcpEndpointDeinitialize(otTcpEndpoint *aEndpoint)`

**Description:** Deinitializes this TCP endpoint.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|A pointer to the TCP endpoint structure to deinitialize.|

This means that OpenThread no longer keeps track of this TCP endpoint and deallocates all resources it has internally allocated for this TCP endpoint. The application can reuse the memory backing the TCP endpoint as it sees fit.

If it corresponds to a live TCP connection, the connection is terminated unceremoniously (as in [otTcpAbort()](api-tcp#ot-tcp-abort)). All resources the application has provided for this TCP endpoint (linked buffers for the send buffer, memory for the receive buffer, the `aEndpoint` structure itself, etc.) are immediately returned to the application.

### otTcpListenerInitialize

`otError otTcpListenerInitialize(otInstance *aInstance, otTcpListener *aListener, const otTcpListenerInitializeArgs *aArgs)`

**Description:** Initializes a TCP listener.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otTcpListener](ot-tcp-listener) *|[in]|aListener|A pointer to a TCP listener structure.|
|const [otTcpListenerInitializeArgs](ot-tcp-listener-initialize-args) *|[in]|aArgs|A pointer to a structure of arguments.|

Calling this function causes OpenThread to keep track of the TCP listener and store and retrieve TCP data inside `aListener`. The application should refrain from directly accessing or modifying the fields in `aListener`. If the application needs to reclaim the memory backing `aListener`, it should call [otTcpListenerDeinitialize()](api-tcp#ot-tcp-listener-deinitialize).

### otTcpListenerGetInstance

`otInstance * otTcpListenerGetInstance(otTcpListener *aListener)`

**Description:** Obtains the otInstance that was associated with `aListener` upon initialization.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpListener](ot-tcp-listener) *|[in]|aListener|The TCP listener whose instance to obtain.|

**Returns**

- The otInstance pointer associated with `aListener`.

### otTcpListenerGetContext

`void * otTcpListenerGetContext(otTcpListener *aListener)`

**Description:** Obtains the context pointer that was associated with `aListener` upon initialization.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpListener](ot-tcp-listener) *|[in]|aListener|The TCP listener whose context to obtain.|

**Returns**

- The context pointer associated with `aListener`.

### otTcpListen

`otError otTcpListen(otTcpListener *aListener, const otSockAddr *aSockName)`

**Description:** Causes incoming TCP connections that match the specified IP address and port to trigger this TCP listener's callbacks.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpListener](ot-tcp-listener) *|[in]|aListener|A pointer to the TCP listener structure that should begin listening.|
|const [otSockAddr](ot-sock-addr) *|[in]|aSockName|The address and port on which to listen for incoming connections.|

### otTcpStopListening

`otError otTcpStopListening(otTcpListener *aListener)`

**Description:** Causes this TCP listener to stop listening for incoming connections.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpListener](ot-tcp-listener) *|[in]|aListener|A pointer to the TCP listener structure that should stop listening.|

### otTcpListenerDeinitialize

`otError otTcpListenerDeinitialize(otTcpListener *aListener)`

**Description:** Deinitializes this TCP listener.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpListener](ot-tcp-listener) *|[in]|aListener|A pointer to the TCP listener structure to deinitialize.|

This means that OpenThread no longer keeps track of this TCP listener and deallocates all resources it has internally allocated for this TCP listener. The application can reuse the memory backing the TCP listener as it sees fit.

If the TCP listener is currently listening, it stops listening.

## Macros

`#define OT_TCP_ENDPOINT_TCB_SIZE_BASE 392`

**Description**: OT_TCP_ENDPOINT_TCB_SIZE_BASE and OT_TCP_ENDPOINT_TCB_NUM_POINTERS are chosen such that the mTcb field of [otTcpEndpoint](ot-tcp-endpoint) has the same size as struct tcpcb in TCPlp.

`#define OT_TCP_ENDPOINT_TCB_NUM_PTR 36`

`#define OT_TCP_RECEIVE_BUFFER_SIZE_FEW_HOPS 2598`

**Description**: Recommended buffer size for TCP connections that traverse about 3 wireless hops or fewer.

`#define OT_TCP_RECEIVE_BUFFER_SIZE_MANY_HOPS 4157`

**Description**: Recommended buffer size for TCP connections that traverse many wireless hops.

`#define OT_TCP_LISTENER_TCB_SIZE_BASE 16`

**Description**: OT_TCP_LISTENER_TCB_SIZE_BASE and OT_TCP_LISTENER_TCB_NUM_POINTERS are chosen such that the mTcbListener field of [otTcpListener](ot-tcp-listener) has the same size as struct tcpcb_listen in TCPlp.

`#define OT_TCP_LISTENER_TCB_NUM_PTR 3`