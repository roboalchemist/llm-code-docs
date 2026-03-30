# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-udp.md

# UDP

This module includes functions that control UDP communication.

## Modules

[otUdpReceiver](ot-udp-receiver)

[otUdpSocket](ot-udp-socket)

## Enumerations

### otNetifIdentifier

```c

enum otNetifIdentifier {
    OT_NETIF_UNSPECIFIED = 0
    OT_NETIF_THREAD_HOST
    OT_NETIF_THREAD_INTERNAL
    OT_NETIF_BACKBONE
}

```

**Description**:

Defines the OpenThread network interface identifiers.

**Enumerator**:

|   |   |
|---|---|
|OT_NETIF_UNSPECIFIED|Unspecified network interface.|
|OT_NETIF_THREAD_HOST|The host Thread interface - allow use of platform UDP.|
|OT_NETIF_THREAD_INTERNAL|The internal Thread interface (within OpenThread) - do not use platform UDP.|
|OT_NETIF_BACKBONE|The Backbone interface.|

## Typedefs

### otUdpHandler

`typedef bool(* otUdpHandler) (void *aContext, const otMessage *aMessage, const otMessageInfo *aMessageInfo)`

**Description**:

This callback allows OpenThread to provide specific handlers for certain UDP messages.

**Details**:

### otUdpReceiver

`typedef struct otUdpReceiver otUdpReceiver`

**Description**:

Represents a UDP receiver.

### otUdpReceive

`typedef void(* otUdpReceive) (void *aContext, otMessage *aMessage, const otMessageInfo *aMessageInfo)`

**Description**:

This callback allows OpenThread to inform the application of a received UDP message.

### otNetifIdentifier (Typedef)

`typedef enum otNetifIdentifier otNetifIdentifier`

**Description**:

Defines the OpenThread network interface identifiers.

### otUdpSocket

`typedef struct otUdpSocket otUdpSocket`

**Description**:

Represents a UDP socket.

## Functions

### otUdpAddReceiver

`otError otUdpAddReceiver(otInstance *aInstance, otUdpReceiver *aUdpReceiver)`

**Description:** Adds a UDP receiver.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpReceiver](ot-udp-receiver) *|[in]|aUdpReceiver|A pointer to the UDP receiver.|

### otUdpRemoveReceiver

`otError otUdpRemoveReceiver(otInstance *aInstance, otUdpReceiver *aUdpReceiver)`

**Description:** Removes a UDP receiver.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpReceiver](ot-udp-receiver) *|[in]|aUdpReceiver|A pointer to the UDP receiver.|

### otUdpSendDatagram

`otError otUdpSendDatagram(otInstance *aInstance, otMessage *aMessage, otMessageInfo *aMessageInfo)`

**Description:** Sends a UDP message without socket.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message without UDP header.|
|[otMessageInfo](ot-message-info) *|[in]|aMessageInfo|A pointer to a message info associated with `aMessage`.|

### otUdpNewMessage

`otMessage * otUdpNewMessage(otInstance *aInstance, const otMessageSettings *aSettings)`

**Description:** Allocate a new message buffer for sending a UDP message.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otMessageSettings](ot-message-settings) *|[in]|aSettings|A pointer to the message settings or NULL to use default settings.|

**Note:**

- If `aSettings` is 'NULL', the link layer security is enabled and the message priority is set to OT_MESSAGE_PRIORITY_NORMAL by default.

**Returns:**

- A pointer to the message buffer or NULL if no message buffers are available or parameters are invalid.

**See Also:**

- [otMessageFree](api-message#ot-message-free)

### otUdpOpen

`otError otUdpOpen(otInstance *aInstance, otUdpSocket *aSocket, otUdpReceive aCallback, void *aContext)`

**Description:** Open a UDP/IPv6 socket.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpSocket](ot-udp-socket) *|[in]|aSocket|A pointer to a UDP socket structure.|
|[otUdpReceive](api-udp#ot-udp-receive)|[in]|aCallback|A pointer to the application callback function.|
|void *|[in]|aContext|A pointer to application-specific context.|

### otUdpIsOpen

`bool otUdpIsOpen(otInstance *aInstance, const otUdpSocket *aSocket)`

**Description:** Check if a UDP socket is open.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otUdpSocket](ot-udp-socket) *|[in]|aSocket|A pointer to a UDP socket structure.|

**Returns:**

- Whether the UDP socket is open.

### otUdpClose

`otError otUdpClose(otInstance *aInstance, otUdpSocket *aSocket)`

**Description:** Close a UDP/IPv6 socket.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpSocket](ot-udp-socket) *|[in]|aSocket|A pointer to a UDP socket structure.|

### otUdpBind

`otError otUdpBind(otInstance *aInstance, otUdpSocket *aSocket, const otSockAddr *aSockName, otNetifIdentifier aNetif)`

**Description:** Bind a UDP/IPv6 socket.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpSocket](ot-udp-socket) *|[in]|aSocket|A pointer to a UDP socket structure.|
|const [otSockAddr](ot-sock-addr) *|[in]|aSockName|A pointer to an IPv6 socket address structure.|
|[otNetifIdentifier](api-udp#ot-netif-identifier)|[in]|aNetif|The network interface to bind.|

### otUdpConnect

`otError otUdpConnect(otInstance *aInstance, otUdpSocket *aSocket, const otSockAddr *aSockName)`

**Description:** Connect a UDP/IPv6 socket.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpSocket](ot-udp-socket) *|[in]|aSocket|A pointer to a UDP socket structure.|
|const [otSockAddr](ot-sock-addr) *|[in]|aSockName|A pointer to an IPv6 socket address structure.|

### otUdpSend

`otError otUdpSend(otInstance *aInstance, otUdpSocket *aSocket, otMessage *aMessage, const otMessageInfo *aMessageInfo)`

**Description:** Send a UDP/IPv6 message.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otUdpSocket](ot-udp-socket) *|[in]|aSocket|A pointer to a UDP socket structure.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|const [otMessageInfo](ot-message-info) *|[in]|aMessageInfo|A pointer to a message info structure.|

If the return value is OT_ERROR_NONE, OpenThread takes ownership of `aMessage`, and the caller should no longer reference `aMessage`. If the return value is not OT_ERROR_NONE, the caller retains ownership of `aMessage`, including freeing `aMessage` if the message buffer is no longer needed.

### otUdpGetSockets

`otUdpSocket * otUdpGetSockets(otInstance *aInstance)`

**Description:** Gets the head of linked list of UDP Sockets.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns:**

- A pointer to the head of UDP Socket linked list.
