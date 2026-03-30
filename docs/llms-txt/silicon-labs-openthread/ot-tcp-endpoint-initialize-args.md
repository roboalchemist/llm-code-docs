# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-tcp-endpoint-initialize-args.md

Contains arguments to the [otTcpEndpointInitialize()](api-tcp#ot-tcp-endpoint-initialize) function. 

## Public Attributes

### mContext

```
void* otTcpEndpointInitializeArgs::mContext
```

**Description:** Pointer to application-specific context.

### mEstablishedCallback

```
otTcpEstablished otTcpEndpointInitializeArgs::mEstablishedCallback
```

**Description:** "Established" callback function

### mSendDoneCallback

```
otTcpSendDone otTcpEndpointInitializeArgs::mSendDoneCallback
```

**Description:** "Send done" callback function

### mForwardProgressCallback

```
otTcpForwardProgress otTcpEndpointInitializeArgs::mForwardProgressCallback
```

**Description:** "Forward progress" callback function

### mReceiveAvailableCallback

```
otTcpReceiveAvailable otTcpEndpointInitializeArgs::mReceiveAvailableCallback
```

**Description:** "Receive available" callback function

### mDisconnectedCallback

```
otTcpDisconnected otTcpEndpointInitializeArgs::mDisconnectedCallback
```

**Description:** "Disconnected" callback function

### mReceiveBuffer

```
void* otTcpEndpointInitializeArgs::mReceiveBuffer
```

**Description:** Pointer to memory provided to the system for the TCP receive buffer.

### mReceiveBufferSize

```
size_t otTcpEndpointInitializeArgs::mReceiveBufferSize
```

**Description:** Size of memory provided to the system for the TCP receive buffer.