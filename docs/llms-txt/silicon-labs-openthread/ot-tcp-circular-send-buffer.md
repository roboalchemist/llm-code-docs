# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-tcp-circular-send-buffer.md

Represents a circular send buffer for use with a TCP endpoint. 

Using a circular send buffer is optional. Applications can use a TCP endpoint to send data by managing otLinkedBuffers directly. However, some applications may find it more convenient to have a circular send buffer; such applications can call [otTcpCircularSendBufferWrite()](api-tcp-ext#ot-tcp-circular-send-buffer-write) to "attach" a circular send buffer to a TCP endpoint and send out data on that TCP endpoint, relying on the circular send buffer to manage the underlying otLinkedBuffers.

[otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) is implemented on top of the otLinkedBuffer-based API provided by an [otTcpEndpoint](ot-tcp-endpoint). Once attached to an [otTcpEndpoint](ot-tcp-endpoint), an [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) performs all the work of managing otLinkedBuffers for the connection. This means that, once an [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) is attached to an [otTcpEndpoint](ot-tcp-endpoint), the application should not call [otTcpSendByReference()](api-tcp#ot-tcp-send-by-reference) or [otTcpSendByExtension()](api-tcp#ot-tcp-send-by-extension) on that [otTcpEndpoint](ot-tcp-endpoint). Instead, the application should use [otTcpCircularSendBufferWrite()](api-tcp-ext#ot-tcp-circular-send-buffer-write) to add data to the send buffer.

The [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback is the intended way for users to learn when space becomes available in the circular send buffer. On an [otTcpEndpoint](ot-tcp-endpoint) to which an [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) is attached, the application MUST install an [otTcpForwardProgress()](api-tcp#ot-tcp-forward-progress) callback and call [otTcpCircularSendBufferHandleForwardProgress()](api-tcp-ext#ot-tcp-circular-send-buffer-handle-forward-progress) on the attached [otTcpCircularSendBuffer](ot-tcp-circular-send-buffer) at the start of the callback function. It is recommended that the user NOT install an [otTcpSendDone()](api-tcp#ot-tcp-send-done) callback, as all management of otLinkedBuffers is handled by the circular send buffer.

The application should not inspect the fields of this structure directly; it should only interact with it via the TCP Circular Send Buffer API functions whose signature are provided in this file. 

## Public Attributes

### mDataBuffer

```
uint8_t* otTcpCircularSendBuffer::mDataBuffer
```

**Description:** Pointer to data in the circular send buffer.

### mCapacity

```
size_t otTcpCircularSendBuffer::mCapacity
```

**Description:** Length of the circular send buffer.

### mStartIndex

```
size_t otTcpCircularSendBuffer::mStartIndex
```

**Description:** Index of the first valid byte in the send buffer.

### mCapacityUsed

```
size_t otTcpCircularSendBuffer::mCapacityUsed
```

**Description:** Number of bytes stored in the send buffer.

### mSendLinks

```
otLinkedBuffer otTcpCircularSendBuffer::mSendLinks[2]
```

### mFirstSendLinkIndex

```
uint8_t otTcpCircularSendBuffer::mFirstSendLinkIndex
```