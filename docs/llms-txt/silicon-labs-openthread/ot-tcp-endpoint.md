# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-tcp-endpoint.md

Represents a TCP endpoint. 

A TCP endpoint acts an endpoint of TCP connection. It can be used to initiate TCP connections, and, once a TCP connection is established, send data to and receive data from the connection peer.

The application should not inspect the fields of this structure directly; it should only interact with it via the TCP API functions whose signatures are provided in this file. 

## Public Attributes

### mSize

```
uint8_t otTcpEndpoint::mSize[OT_TCP_ENDPOINT_TCB_SIZE_BASE+OT_TCP_ENDPOINT_TCB_NUM_PTR *sizeof(void *)]
```

### mAlign

```
uint64_t otTcpEndpoint::mAlign
```

### mTcb

```
union otTcpEndpoint::@21 otTcpEndpoint::mTcb
```

### mNext

```
struct otTcpEndpoint* otTcpEndpoint::mNext
```

**Description:** A pointer to the next TCP endpoint (internal use only)

### mContext

```
void* otTcpEndpoint::mContext
```

**Description:** A pointer to application-specific context.

### mEstablishedCallback

```
otTcpEstablished otTcpEndpoint::mEstablishedCallback
```

**Description:** "Established" callback function

### mSendDoneCallback

```
otTcpSendDone otTcpEndpoint::mSendDoneCallback
```

**Description:** "Send done" callback function

### mForwardProgressCallback

```
otTcpForwardProgress otTcpEndpoint::mForwardProgressCallback
```

**Description:** "Forward progress" callback function

### mReceiveAvailableCallback

```
otTcpReceiveAvailable otTcpEndpoint::mReceiveAvailableCallback
```

**Description:** "Receive available" callback function

### mDisconnectedCallback

```
otTcpDisconnected otTcpEndpoint::mDisconnectedCallback
```

**Description:** "Disconnected" callback function

### mTimers

```
uint32_t otTcpEndpoint::mTimers[4]
```

### mReceiveLinks

```
otLinkedBuffer otTcpEndpoint::mReceiveLinks[2]
```

### mSockAddr

```
otSockAddr otTcpEndpoint::mSockAddr
```

### mPendingCallbacks

```
uint8_t otTcpEndpoint::mPendingCallbacks
```