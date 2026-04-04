# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-message-info.md

Represents the local and peer IPv6 socket addresses. 

## Public Attributes

### mSockAddr

```
otIp6Address otMessageInfo::mSockAddr
```

**Description:** The local IPv6 address.

### mPeerAddr

```
otIp6Address otMessageInfo::mPeerAddr
```

**Description:** The peer IPv6 address.

### mSockPort

```
uint16_t otMessageInfo::mSockPort
```

**Description:** The local transport-layer port.

### mPeerPort

```
uint16_t otMessageInfo::mPeerPort
```

**Description:** The peer transport-layer port.

### mHopLimit

```
uint8_t otMessageInfo::mHopLimit
```

**Description:** The IPv6 Hop Limit value.

**Details:** Only applies if `mAllowZeroHopLimit` is FALSE. If `0`, IPv6 Hop Limit is default value `OPENTHREAD_CONFIG_IP6_HOP_LIMIT_DEFAULT`. Otherwise, specifies the IPv6 Hop Limit.

### mEcn

```
uint8_t otMessageInfo::mEcn
```

**Description:** The ECN status of the packet, represented as in the IPv6 header.

### mIsHostInterface

```
bool otMessageInfo::mIsHostInterface
```

**Description:** TRUE if packets sent/received via host interface, FALSE otherwise.

### mAllowZeroHopLimit

```
bool otMessageInfo::mAllowZeroHopLimit
```

**Description:** TRUE to allow IPv6 Hop Limit 0 in `mHopLimit`, FALSE otherwise.

### mMulticastLoop

```
bool otMessageInfo::mMulticastLoop
```

**Description:** TRUE to allow looping back multicast, FALSE otherwise.