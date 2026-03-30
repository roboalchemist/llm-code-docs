# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-udp-socket.md

Represents a UDP socket. 

## Public Attributes

### mSockName

```
otSockAddr otUdpSocket::mSockName
```

**Description:** The local IPv6 socket address.

### mPeerName

```
otSockAddr otUdpSocket::mPeerName
```

**Description:** The peer IPv6 socket address.

### mHandler

```
otUdpReceive otUdpSocket::mHandler
```

**Description:** A function pointer to the application callback.

### mContext

```
void* otUdpSocket::mContext
```

**Description:** A pointer to application-specific context.

### mHandle

```
void* otUdpSocket::mHandle
```

**Description:** A handle to platform's UDP.

### mNext

```
struct otUdpSocket* otUdpSocket::mNext
```

**Description:** A pointer to the next UDP socket (internal use only).

### mNetifId

```
otNetifIdentifier otUdpSocket::mNetifId
```

**Description:** The network interface identifier.