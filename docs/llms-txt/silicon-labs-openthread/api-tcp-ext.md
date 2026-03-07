# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-tcp-ext.md

# TCP Abstractions

This module includes easy-to-use abstractions on top of the base TCP API. 

## Modules

[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer)

[otTcpEndpointAndCircularSendBuffer](ot-tcp-endpoint-and-circular-send-buffer)

## Enumerations

### @23

```
enum @23 {
    OT_TCP_CIRCULAR_SEND_BUFFER_WRITE_MORE_TO_COME = 1 << 0
}
```

**Description:**

Defines flags passed to `otTcpCircularSendBufferWrite`.

**Enumerator:**

|   |   |
|---|---|
|OT_TCP_CIRCULAR_SEND_BUFFER_WRITE_MORE_TO_COME||

## Typedefs

### otTcpCircularSendBuffer

`typedef struct otTcpCircularSendBuffer otTcpCircularSendBuffer`

**Description:**

Represents a circular send buffer for use with a TCP endpoint.

**Details:**

Using a circular send buffer is optional. Applications can use a TCP endpoint to send data by managing otLinkedBuffers directly. However, some applications may find it more convenient to have a circular send buffer; such applications can call [otTcpCircularSendBufferWrite()](api-tcp-ext#ot-tcp-circular-send-buffer-write) to "attach" a circular send buffer to a TCP endpoint and send out data on that TCP endpoint, relying on the circular send buffer to manage the underlying otLinkedBuffers.

[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) is implemented on top of the otLinkedBuffer-based API provided by an [otTcpEndpoint](ot-tcp-endpoint). Once attached to an [otTcpEndpoint](ot-tcp-endpoint), an [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) performs all the work of managing otLinkedBuffers for the connection. This means that, once an [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) is attached to an [otTcpEndpoint](ot-tcp-endpoint), the application should not call [otTcpSendByReference()](api-tcp#ot-tcp-send-by-reference) or [otTcpSendByExtension()](api-tcp#ot-tcp-send-by-extension) on that [otTcpEndpoint](ot-tcp-endpoint). Instead, the application should use [otTcpCircularSendBufferWrite()](api-tcp-ext#ot-tcp-circular-send-buffer-write) to add data to the send buffer.

The [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback is the intended way for users to learn when space becomes available in the circular send buffer. On an [otTcpEndpoint](ot-tcp-endpoint) to which an [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) is attached, the application MUST install an [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback and call [otTcpCircularSendBufferHandleForwardProgress()](api-tcp-ext#ot-tcp-circular-send-buffer-handle-forward-progress) on the attached [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) at the start of the callback function. It is recommended that the user NOT install an [otTcpSendDone()](api-tcp#ot-tcp-send-done) callback, as all management of otLinkedBuffers is handled by the circular send buffer.

The application should not inspect the fields of this structure directly; it should only interact with it via the TCP Circular Send Buffer API functions whose signature are provided in this file.

### otTcpEndpointAndCircularSendBuffer

`typedef struct otTcpEndpointAndCircularSendBuffer otTcpEndpointAndCircularSendBuffer`

**Description:**

Context structure to use with mbedtls_ssl_set_bio.

## Functions

### otTcpCircularSendBufferInitialize

`void otTcpCircularSendBufferInitialize(otTcpCircularSendBuffer *aSendBuffer, void *aDataBuffer, size_t aCapacity)`

**Description:** Initializes a TCP circular send buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) *|[in]|aSendBuffer|A pointer to the TCP circular send buffer to initialize.|
|void *|[in]|aDataBuffer|A pointer to memory to use to store data in the TCP circular send buffer.|
|size_t|[in]|aCapacity|The capacity, in bytes, of the TCP circular send buffer, which must equal the size of the memory pointed to by `aDataBuffer` .|

### otTcpCircularSendBufferWrite

`otError otTcpCircularSendBufferWrite(otTcpEndpoint *aEndpoint, otTcpCircularSendBuffer *aSendBuffer, const void *aData, size_t aLength, size_t *aWritten, uint32_t aFlags)`

**Description:** Sends out data on a TCP endpoint, using the provided TCP circular send buffer to manage buffering.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpEndpoint](ot-tcp-endpoint) *|[in]|aEndpoint|The TCP endpoint on which to send out data.|
|[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) *|[in]|aSendBuffer|The TCP circular send buffer into which to copy data.|
|const void *|[in]|aData|A pointer to data to copy into the TCP circular send buffer.|
|size_t|[in]|aLength|The length of the data pointed to by `aData` to copy into the TCP circular send buffer.|
|size_t *|[out]|aWritten|Populated with the amount of data copied into the send buffer, which might be less than `aLength` if the send buffer reaches capacity.|
|uint32_t|[in]|aFlags|Flags specifying options for this operation (see enumeration above).|

Once this function is called, `aSendBuffer` and `aEndpoint` are considered "attached" to each other. While they are attached, ALL send operations for `aEndpoint` must be made using `aSendBuffer` and ALL operations on `aSendBuffer` must be associated with `aEndpoint` .

The only way to "detach" a TCP circular send buffer and a TCP endpoint is to wait for the send buffer to become completely empty. This can happen in two ways: (1) all data in the send buffer is sent and acknowledged in the normal course of TCP protocol operation, or (2) the connection is terminated.

The recommended usage pattern is to use a single TCP circular send buffer with a TCP endpoint, and to send data on that TCP endpoint only via its associated TCP circular buffer. This recommended usage pattern sidesteps the issues described above by always using a TCP endpoint and TCP circular send buffer together.

If the circular send buffer reaches capacity, only a prefix of the provided data is copied into the circular send buffer.

### otTcpCircularSendBufferHandleForwardProgress

`void otTcpCircularSendBufferHandleForwardProgress(otTcpCircularSendBuffer *aSendBuffer, size_t aInSendBuffer)`

**Description:** Performs circular-send-buffer-specific handling in the otTcpForwardProgress callback.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) *|[in]|aSendBuffer|A pointer to the TCP circular send buffer for the endpoint for which [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) was invoked.|
|size_t|[in]|aInSendBuffer|Value of `aInSendBuffer` passed to the [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback.|

The application is expected to install an [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback on the [otTcpEndpoint](ot-tcp-endpoint), and call this function at the start of the callback function for circular-send-buffer-specific processing.

In the callback function, the application can determine the amount of free space in the circular send buffer by calling otTcpCircularSendBufferFreeSpace(), or by comparing `aInSendBuffer` with the send buffer's capacity, chosen by the user when calling [otTcpCircularSendBufferInitialize()](api-tcp-ext#ot-tcp-circular-send-buffer-initialize).

### otTcpCircularSendBufferGetFreeSpace

`size_t otTcpCircularSendBufferGetFreeSpace(const otTcpCircularSendBuffer *aSendBuffer)`

**Description:** Returns the amount of free space in the TCP circular send buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) *|[in]|aSendBuffer|A pointer to the TCP circular send buffer whose amount of free space to return.|

This operation will always succeed.

**Returns**

- The amount of free space in the send buffer.

### otTcpCircularSendBufferForceDiscardAll

`void otTcpCircularSendBufferForceDiscardAll(otTcpCircularSendBuffer *aSendBuffer)`

**Description:** Forcibly discards all data in the circular send buffer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) *|[in]|aSendBuffer|The TCP circular send buffer whose data to discard.|

The application is expected to call this function when a TCP connection is terminated unceremoniously (e.g., if the application calls otTcpEndpointAbort() or is informed of a reset connection via the otTcpConnectionLost() callback).

Calling this function on a nonempty TCP circular send buffer attached to a TCP endpoint results in undefined behavior.

### otTcpCircularSendBufferDeinitialize

`otError otTcpCircularSendBufferDeinitialize(otTcpCircularSendBuffer *aSendBuffer)`

**Description:** Deinitializes a TCP circular send buffer, detaching it if attached.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) *|[in]|aSendBuffer|The TCP circular send buffer to deinitialize.|

If the TCP circular send buffer is not empty, then this operation will fail.

### otTcpMbedTlsSslSendCallback

`int otTcpMbedTlsSslSendCallback(void *aCtx, const unsigned char *aBuf, size_t aLen)`

**Description:** Non-blocking send callback to pass to mbedtls_ssl_set_bio.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|void *|[in]|aCtx|A pointer to an [otTcpEndpointAndCircularSendBuffer](ot-tcp-endpoint-and-circular-send-buffer).|
|const unsigned char *|[in]|aBuf|The data to add to the send buffer.|
|size_t|[in]|aLen|The amount of data to add to the send buffer.|

**Returns**

- The number of bytes sent, or an mbedtls error code.

### otTcpMbedTlsSslRecvCallback

`int otTcpMbedTlsSslRecvCallback(void *aCtx, unsigned char *aBuf, size_t aLen)`

**Description:** Non-blocking receive callback to pass to mbedtls_ssl_set_bio.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|void *|[in]|aCtx|A pointer to an [otTcpEndpointAndCircularSendBuffer](ot-tcp-endpoint-and-circular-send-buffer).|
|unsigned char *|[out]|aBuf|The buffer into which to receive data.|
|size_t|[in]|aLen|The maximum amount of data that can be received.|

**Returns**

- The number of bytes received, or an mbedtls error code.