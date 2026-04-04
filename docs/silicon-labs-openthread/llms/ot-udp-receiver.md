# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-udp-receiver.md

Represents a UDP receiver. 

## Public Attributes

### mNext

```
struct otUdpReceiver* otUdpReceiver::mNext
```

**Description:** A pointer to the next UDP receiver (internal use only).

### mHandler

```
otUdpHandler otUdpReceiver::mHandler
```

**Description:** A function pointer to the receiver callback.

### mContext

```
void* otUdpReceiver::mContext
```

**Description:** A pointer to application-specific context.