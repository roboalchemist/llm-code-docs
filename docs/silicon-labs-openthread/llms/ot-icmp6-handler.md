# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-icmp6-handler.md

Implements ICMPv6 message handler. 

## Public Attributes

### mReceiveCallback

```
otIcmp6ReceiveCallback otIcmp6Handler::mReceiveCallback
```

**Description:** The ICMPv6 received callback.

### mContext

```
void* otIcmp6Handler::mContext
```

**Description:** A pointer to arbitrary context information.

### mNext

```
struct otIcmp6Handler* otIcmp6Handler::mNext
```

**Description:** A pointer to the next handler in the list.