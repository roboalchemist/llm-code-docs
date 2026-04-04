# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-ping-sender-reply.md

Represents a ping reply. 

## Public Attributes

### mSenderAddress

```
otIp6Address otPingSenderReply::mSenderAddress
```

**Description:** Sender IPv6 address (address from which ping reply was received).

### mRoundTripTime

```
uint16_t otPingSenderReply::mRoundTripTime
```

**Description:** Round trip time in msec.

### mSize

```
uint16_t otPingSenderReply::mSize
```

**Description:** Data size (number of bytes) in reply (excluding IPv6 and ICMP6 headers).

### mSequenceNumber

```
uint16_t otPingSenderReply::mSequenceNumber
```

**Description:** Sequence number.

### mHopLimit

```
uint8_t otPingSenderReply::mHopLimit
```

**Description:** Hop limit.