# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-message.md

# Message

This module includes functions that manipulate OpenThread message buffers. 

## Modules

[otMessageSettings](ot-message-settings)

[otThreadLinkInfo](ot-thread-link-info)

[otMessageQueue](ot-message-queue)

[otMessageQueueInfo](ot-message-queue-info)

[otBufferInfo](ot-buffer-info)

## Enumerations

### otMessagePriority

```
enum otMessagePriority {
    OT_MESSAGE_PRIORITY_LOW = 0
    OT_MESSAGE_PRIORITY_NORMAL = 1
    OT_MESSAGE_PRIORITY_HIGH = 2
}
```

**Description:**

Defines the OpenThread message priority levels.

**Enumerator:**

|   |   |
|---|---|
|OT_MESSAGE_PRIORITY_LOW|Low priority level.|
|OT_MESSAGE_PRIORITY_NORMAL|Normal priority level.|
|OT_MESSAGE_PRIORITY_HIGH|High priority level.|

### otMessageOrigin

```
enum otMessageOrigin {
    OT_MESSAGE_ORIGIN_THREAD_NETIF = 0
    OT_MESSAGE_ORIGIN_HOST_TRUSTED = 1
    OT_MESSAGE_ORIGIN_HOST_UNTRUSTED = 2
}
```

**Description:**

Defines the OpenThread message origins.

**Enumerator:**

|   |   |
|---|---|
|OT_MESSAGE_ORIGIN_THREAD_NETIF|Message from Thread Netif.|
|OT_MESSAGE_ORIGIN_HOST_TRUSTED|Message from a trusted source on host.|
|OT_MESSAGE_ORIGIN_HOST_UNTRUSTED|Message from an untrusted source on host.|

## Typedefs

### otMessage

`typedef struct otMessage otMessage`

**Description:**

An opaque representation of an OpenThread message buffer.

### otMessagePriority

`typedef enum otMessagePriority otMessagePriority`

**Description:**

Defines the OpenThread message priority levels.

### otMessageOrigin

`typedef enum otMessageOrigin otMessageOrigin`

**Description:**

Defines the OpenThread message origins.

### otMessageSettings

`typedef struct otMessageSettings otMessageSettings`

**Description:**

Represents a message settings.

### otThreadLinkInfo

`typedef struct otThreadLinkInfo otThreadLinkInfo`

**Description:**

Represents link-specific information for messages received from the Thread radio.

### otMessageTxCallback

`typedef void(* otMessageTxCallback) (const otMessage *aMessage, otError aError, void *aContext)`

**Description:**

Represents the callback function pointer to notify the transmission outcome (success or failure) of a message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aMessage|A pointer to the message.|
||[in]|aError|The TX error when sending the message.|
||[in]|aContext|A pointer to the user-provided context when the callback was registered.|

**Details:**

The error indicates the transmission status of the IPv6 message from this device to an immediate neighbor (one-hop transmission). It doesn't indicate that the message is received by its final intended destination (multi-hop away).

For a unicast IPv6 message, an `OT_ERROR_NONE` error indicates that the message (all its corresponding fragment frames if the message is larger and requires fragmentation) was successfully delivered to the immediate neighbor, and a MAC layer acknowledgment was received for all fragments. This is reported regardless of whether the message is sent using direct TX or indirect TX (to a sleepy child using CSL or data poll triggered TX).

For a multicast message, an `OT_ERROR_NONE` status indicates that the message (all its fragment frames) was successfully broadcast. Note that no MAC-level acknowledgment is required for broadcast frame TX.

The OpenThread stack may alter the content of the message as it is prepared for transmission (e.g., IPv6 headers may be prepended, or additional metadata appended at the end). So, the content of `aMessage` when this callback is invoked may differ from its original content (e.g., when it was given as input in `otIp6Send()` for transmission).

### otMessageQueueInfo

`typedef struct otMessageQueueInfo otMessageQueueInfo`

**Description:**

Represents information about a message queue.

### otBufferInfo

`typedef struct otBufferInfo otBufferInfo`

**Description:**

Represents the message buffer information for different queues used by OpenThread stack.

## Functions

### otMessageGetInstance

`otInstance * otMessageGetInstance(const otMessage *aMessage)`

**Description:** Gets the `otInstance` associated with a given message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A message.|

**Returns**

- The `otInstance` associated with `aMessage`.

### otMessageFree

`void otMessageFree(otMessage *aMessage)`

**Description:** Free an allocated message buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|

**See Also**

- [otMessageAppend](api-message#ot-message-append)
- [otMessageGetLength](api-message#ot-message-get-length)
- [otMessageSetLength](api-message#ot-message-set-length)
- [otMessageGetOffset](api-message#ot-message-get-offset)
- [otMessageSetOffset](api-message#ot-message-set-offset)
- [otMessageRead](api-message#ot-message-read)
- [otMessageWrite](api-message#ot-message-write)

### otMessageGetLength

`uint16_t otMessageGetLength(const otMessage *aMessage)`

**Description:** Get the message length in bytes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|

**Returns**

- The message length in bytes.

**See Also**

- [otMessageFree](api-message#ot-message-free)
- [otMessageAppend](api-message#ot-message-append)
- [otMessageSetLength](api-message#ot-message-set-length)
- [otMessageGetOffset](api-message#ot-message-get-offset)
- [otMessageSetOffset](api-message#ot-message-set-offset)
- [otMessageRead](api-message#ot-message-read)
- [otMessageWrite](api-message#ot-message-write)
- [otMessageSetLength](api-message#ot-message-set-length)

### otMessageSetLength

`otError otMessageSetLength(otMessage *aMessage, uint16_t aLength)`

**Description:** Set the message length in bytes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|uint16_t|[in]|aLength|A length in bytes.|

**See Also**

- [otMessageFree](api-message#ot-message-free)
- [otMessageAppend](api-message#ot-message-append)
- [otMessageGetLength](api-message#ot-message-get-length)
- [otMessageGetOffset](api-message#ot-message-get-offset)
- [otMessageSetOffset](api-message#ot-message-set-offset)
- [otMessageRead](api-message#ot-message-read)
- [otMessageWrite](api-message#ot-message-write)

### otMessageGetOffset

`uint16_t otMessageGetOffset(const otMessage *aMessage)`

**Description:** Get the message offset in bytes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|

**Returns**

- The message offset value.

**See Also**

- [otMessageFree](api-message#ot-message-free)
- [otMessageAppend](api-message#ot-message-append)
- [otMessageGetLength](api-message#ot-message-get-length)
- [otMessageSetLength](api-message#ot-message-set-length)
- [otMessageSetOffset](api-message#ot-message-set-offset)
- [otMessageRead](api-message#ot-message-read)
- [otMessageWrite](api-message#ot-message-write)

### otMessageSetOffset

`void otMessageSetOffset(otMessage *aMessage, uint16_t aOffset)`

**Description:** Set the message offset in bytes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|uint16_t|[in]|aOffset|An offset in bytes.|

**See Also**

- [otMessageFree](api-message#ot-message-free)
- [otMessageAppend](api-message#ot-message-append)
- [otMessageGetLength](api-message#ot-message-get-length)
- [otMessageSetLength](api-message#ot-message-set-length)
- [otMessageGetOffset](api-message#ot-message-get-offset)
- [otMessageRead](api-message#ot-message-read)
- [otMessageWrite](api-message#ot-message-write)

### otMessageIsLinkSecurityEnabled

`bool otMessageIsLinkSecurityEnabled(const otMessage *aMessage)`

**Description:** Indicates whether or not link security is enabled for the message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|

### otMessageIsLoopbackToHostAllowed

`bool otMessageIsLoopbackToHostAllowed(const otMessage *aMessage)`

**Description:** Indicates whether or not the message is allowed to be looped back to host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|

### otMessageSetLoopbackToHostAllowed

`void otMessageSetLoopbackToHostAllowed(otMessage *aMessage, bool aAllowLoopbackToHost)`

**Description:** Sets whether or not the message is allowed to be looped back to host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|bool|[in]|aAllowLoopbackToHost|Whether to allow the message to be looped back to host.|

### otMessageIsMulticastLoopEnabled

`bool otMessageIsMulticastLoopEnabled(otMessage *aMessage)`

**Description:** Indicates whether the given message may be looped back in a case of a multicast destination address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to the message.|

If `aMessage` is used along with an `otMessageInfo`, the `mMulticastLoop` field from `otMessageInfo` structure takes precedence and will be used instead of the the value set on `aMessage`.

This API is mainly intended for use along with `otIp6Send()` which expects an already prepared IPv6 message.

### otMessageSetMulticastLoopEnabled

`void otMessageSetMulticastLoopEnabled(otMessage *aMessage, bool aEnabled)`

**Description:** Controls whether the given message may be looped back in a case of a multicast destination address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to the message.|
|bool|[in]|aEnabled|The configuration value.|

### otMessageGetOrigin

`otMessageOrigin otMessageGetOrigin(const otMessage *aMessage)`

**Description:** Gets the message origin.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|

**Returns**

- The message origin.

### otMessageSetOrigin

`void otMessageSetOrigin(otMessage *aMessage, otMessageOrigin aOrigin)`

**Description:** Sets the message origin.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|[otMessageOrigin](api-message#ot-message-origin)|[in]|aOrigin|The message origin.|

### otMessageSetDirectTransmission

`void otMessageSetDirectTransmission(otMessage *aMessage, bool aEnabled)`

**Description:** Sets/forces the message to be forwarded using direct transmission.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|bool|[in]|aEnabled|If `true`, the message is forced to use direct transmission. If `false`, the message follows the normal procedure.|

Default setting for a new message is `false`.

### otMessageGetRss

`int8_t otMessageGetRss(const otMessage *aMessage)`

**Description:** Returns the average RSS (received signal strength) associated with the message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|

**Returns**

- The average RSS value (in dBm) or OT_RADIO_RSSI_INVALID if no average RSS is available.

### otMessageGetThreadLinkInfo

`otError otMessageGetThreadLinkInfo(const otMessage *aMessage, otThreadLinkInfo *aLinkInfo)`

**Description:** Retrieves the link-specific information for a message received over Thread radio.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|The message from which to retrieve `otThreadLinkInfo`. @pram[out] aLinkInfo A pointer to an `otThreadLinkInfo` to populate.|
|[otThreadLinkInfo](ot-thread-link-info) *|N/A|aLinkInfo||

### otMessageRegisterTxCallback

`void otMessageRegisterTxCallback(otMessage *aMessage, otMessageTxCallback aCallback, void *aContext)`

**Description:** Registers a callback to be notified of a message's transmission outcome.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|The message to register the callback with.|
|[otMessageTxCallback](api-message#ot-message-tx-callback)|[in]|aCallback|The TX callback.|
|void *|[in]|aContext|A pointer to a user-provided arbitrary context for the callback.|

Calling this function again for the same message will replace any previously registered callback.

If the message is never actually sent (e.g., it's not passed to `otIp6Send()` or other send APIs), the callback will still be invoked when the message is freed. In this case, `OT_ERROR_DROP` will be passed as the error.

### otMessageAppend

`otError otMessageAppend(otMessage *aMessage, const void *aBuf, uint16_t aLength)`

**Description:** Append bytes to a message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|const void *|[in]|aBuf|A pointer to the data to append.|
|uint16_t|[in]|aLength|Number of bytes to append.|

**See Also**

- [otMessageFree](api-message#ot-message-free)
- [otMessageGetLength](api-message#ot-message-get-length)
- [otMessageSetLength](api-message#ot-message-set-length)
- [otMessageGetOffset](api-message#ot-message-get-offset)
- [otMessageSetOffset](api-message#ot-message-set-offset)
- [otMessageRead](api-message#ot-message-read)
- [otMessageWrite](api-message#ot-message-write)

### otMessageRead

`uint16_t otMessageRead(const otMessage *aMessage, uint16_t aOffset, void *aBuf, uint16_t aLength)`

**Description:** Read bytes from a message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|uint16_t|[in]|aOffset|An offset in bytes.|
|void *|[in]|aBuf|A pointer to a buffer that message bytes are read to.|
|uint16_t|[in]|aLength|Number of bytes to read.|

**Returns**

- The number of bytes read.

**See Also**

- [otMessageFree](api-message#ot-message-free)
- [otMessageAppend](api-message#ot-message-append)
- [otMessageGetLength](api-message#ot-message-get-length)
- [otMessageSetLength](api-message#ot-message-set-length)
- [otMessageGetOffset](api-message#ot-message-get-offset)
- [otMessageSetOffset](api-message#ot-message-set-offset)
- [otMessageWrite](api-message#ot-message-write)

### otMessageWrite

`int otMessageWrite(otMessage *aMessage, uint16_t aOffset, const void *aBuf, uint16_t aLength)`

**Description:** Write bytes to a message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to a message buffer.|
|uint16_t|[in]|aOffset|An offset in bytes.|
|const void *|[in]|aBuf|A pointer to a buffer that message bytes are written from.|
|uint16_t|[in]|aLength|Number of bytes to write.|

**Returns**

- The number of bytes written.

**See Also**

- [otMessageFree](api-message#ot-message-free)
- [otMessageAppend](api-message#ot-message-append)
- [otMessageGetLength](api-message#ot-message-get-length)
- [otMessageSetLength](api-message#ot-message-set-length)
- [otMessageGetOffset](api-message#ot-message-get-offset)
- [otMessageSetOffset](api-message#ot-message-set-offset)
- [otMessageRead](api-message#ot-message-read)

### otMessageQueueInit

`void otMessageQueueInit(otMessageQueue *aQueue)`

**Description:** Initialize the message queue.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessageQueue](ot-message-queue) *|[in]|aQueue|A pointer to a message queue.|

MUST be called once and only once for a `otMessageQueue` instance before any other `otMessageQueue` functions. The behavior is undefined if other queue APIs are used with an `otMessageQueue` before it being initialized or if it is initialized more than once.

### otMessageQueueEnqueue

`void otMessageQueueEnqueue(otMessageQueue *aQueue, otMessage *aMessage)`

**Description:** Adds a message to the end of the given message queue.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessageQueue](ot-message-queue) *|[in]|aQueue|A pointer to the message queue.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|The message to add.|

### otMessageQueueEnqueueAtHead

`void otMessageQueueEnqueueAtHead(otMessageQueue *aQueue, otMessage *aMessage)`

**Description:** Adds a message at the head/front of the given message queue.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessageQueue](ot-message-queue) *|[in]|aQueue|A pointer to the message queue.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|The message to add.|

### otMessageQueueDequeue

`void otMessageQueueDequeue(otMessageQueue *aQueue, otMessage *aMessage)`

**Description:** Removes a message from the given message queue.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessageQueue](ot-message-queue) *|[in]|aQueue|A pointer to the message queue.|
|[otMessage](api-message#ot-message) *|[in]|aMessage|The message to remove.|

### otMessageQueueGetHead

`otMessage * otMessageQueueGetHead(otMessageQueue *aQueue)`

**Description:** Returns a pointer to the message at the head of the queue.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessageQueue](ot-message-queue) *|[in]|aQueue|A pointer to a message queue.|

**Returns**

- A pointer to the message at the head of queue or NULL if queue is empty.

### otMessageQueueGetNext

`otMessage * otMessageQueueGetNext(otMessageQueue *aQueue, const otMessage *aMessage)`

**Description:** Returns a pointer to the next message in the queue by iterating forward (from head to tail).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otMessageQueue](ot-message-queue) *|[in]|aQueue|A pointer to a message queue.|
|const [otMessage](api-message#ot-message) *|[in]|aMessage|A pointer to current message buffer.|

**Returns**

- A pointer to the next message in the queue after `aMessage` or NULL if `aMessage is the tail of queue. NULL is returned if`aMessage`is not in the queue`aQueue`.

### otMessageGetBufferInfo

`void otMessageGetBufferInfo(otInstance *aInstance, otBufferInfo *aBufferInfo)`

**Description:** Get the Message Buffer information.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otBufferInfo](ot-buffer-info) *|[out]|aBufferInfo|A pointer where the message buffer information is written.|

### otMessageResetBufferInfo

`void otMessageResetBufferInfo(otInstance *aInstance)`

**Description:** Reset the Message Buffer information counter tracking the maximum number buffers in use at the same time.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

This resets `mMaxUsedBuffers` in `otBufferInfo`.