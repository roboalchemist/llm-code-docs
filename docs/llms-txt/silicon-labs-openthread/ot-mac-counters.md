# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-mac-counters.md

Represents the MAC layer counters. 

## Public Attributes

### mTxTotal

```
uint32_t otMacCounters::mTxTotal
```

**Description:** The total number of unique MAC frame transmission requests.

**Details:** Note that this counter is incremented for each MAC transmission request only by one, regardless of the amount of CCA failures, CSMA-CA attempts, or retransmissions.

This increment rule applies to the following counters:

- `mTxUnicast`
- `mTxBroadcast`
- `mTxAckRequested`
- `mTxNoAckRequested`
- `mTxData`
- `mTxDataPoll`
- `mTxBeacon`
- `mTxBeaconRequest`
- `mTxOther`
- `mTxErrAbort`
- `mTxErrBusyChannel`

The following equations are valid:

- `mTxTotal` = `mTxUnicast` + `mTxBroadcast`
- `mTxTotal` = `mTxAckRequested` + `mTxNoAckRequested`
- `mTxTotal` = `mTxData` + `mTxDataPoll` + `mTxBeacon` + `mTxBeaconRequest` + `mTxOther`

### mTxUnicast

```
uint32_t otMacCounters::mTxUnicast
```

**Description:** The total number of unique unicast MAC frame transmission requests.

### mTxBroadcast

```
uint32_t otMacCounters::mTxBroadcast
```

**Description:** The total number of unique broadcast MAC frame transmission requests.

### mTxAckRequested

```
uint32_t otMacCounters::mTxAckRequested
```

**Description:** The total number of unique MAC frame transmission requests with requested acknowledgment.

### mTxAcked

```
uint32_t otMacCounters::mTxAcked
```

**Description:** The total number of unique MAC frame transmission requests that were acked.

### mTxNoAckRequested

```
uint32_t otMacCounters::mTxNoAckRequested
```

**Description:** The total number of unique MAC frame transmission requests without requested acknowledgment.

### mTxData

```
uint32_t otMacCounters::mTxData
```

**Description:** The total number of unique MAC Data frame transmission requests.

### mTxDataPoll

```
uint32_t otMacCounters::mTxDataPoll
```

**Description:** The total number of unique MAC Data Poll frame transmission requests.

### mTxBeacon

```
uint32_t otMacCounters::mTxBeacon
```

**Description:** The total number of unique MAC Beacon frame transmission requests.

### mTxBeaconRequest

```
uint32_t otMacCounters::mTxBeaconRequest
```

**Description:** The total number of unique MAC Beacon Request frame transmission requests.

### mTxOther

```
uint32_t otMacCounters::mTxOther
```

**Description:** The total number of unique other MAC frame transmission requests.

**Details:** This counter is currently used for counting out-of-band frames.

### mTxRetry

```
uint32_t otMacCounters::mTxRetry
```

**Description:** The total number of MAC retransmission attempts.

**Details:** Note that this counter is incremented by one for each retransmission attempt that may be triggered by lack of acknowledgement, CSMA/CA failure, or other type of transmission error. The `mTxRetry` counter is incremented both for unicast and broadcast MAC frames.

Modify the following configuration parameters to control the amount of retransmissions in the system:

- OPENTHREAD_CONFIG_MAC_DEFAULT_MAX_FRAME_RETRIES_DIRECT
- OPENTHREAD_CONFIG_MAC_DEFAULT_MAX_FRAME_RETRIES_INDIRECT
- OPENTHREAD_CONFIG_MAC_TX_NUM_BCAST
- OPENTHREAD_CONFIG_MAC_MAX_CSMA_BACKOFFS_DIRECT
- OPENTHREAD_CONFIG_MAC_MAX_CSMA_BACKOFFS_INDIRECT

Currently, this counter is invalid if the platform's radio driver capability includes [OT_RADIO_CAPS_TRANSMIT_RETRIES](radio-types#ot-radio-caps-transmit-retries).

### mTxDirectMaxRetryExpiry

```
uint32_t otMacCounters::mTxDirectMaxRetryExpiry
```

**Description:** The total number of unique MAC transmission packets that meet maximal retry limit for direct packets.

### mTxIndirectMaxRetryExpiry

```
uint32_t otMacCounters::mTxIndirectMaxRetryExpiry
```

**Description:** The total number of unique MAC transmission packets that meet maximal retry limit for indirect packets.

### mTxErrCca

```
uint32_t otMacCounters::mTxErrCca
```

**Description:** The total number of CCA failures.

**Details:** The meaning of this counter can be different and it depends on the platform's radio driver capabilities.

If [OT_RADIO_CAPS_CSMA_BACKOFF](radio-types#ot-radio-caps-csma-backoff) is enabled, this counter represents the total number of full CSMA/CA failed attempts and it is incremented by one also for each retransmission (in case of a CSMA/CA fail).

If [OT_RADIO_CAPS_TRANSMIT_RETRIES](radio-types#ot-radio-caps-transmit-retries) is enabled, this counter represents the total number of full CSMA/CA failed attempts and it is incremented by one for each individual data frame request (regardless of the amount of retransmissions).

### mTxErrAbort

```
uint32_t otMacCounters::mTxErrAbort
```

**Description:** The total number of unique MAC transmission request failures cause by an abort error.

### mTxErrBusyChannel

```
uint32_t otMacCounters::mTxErrBusyChannel
```

**Description:** The total number of unique MAC transmission requests failures caused by a busy channel (a CSMA/CA fail).

### mRxTotal

```
uint32_t otMacCounters::mRxTotal
```

**Description:** The total number of received frames.

**Details:** This counter counts all frames reported by the platform's radio driver, including frames that were dropped, for example because of an FCS error.

### mRxUnicast

```
uint32_t otMacCounters::mRxUnicast
```

**Description:** The total number of unicast frames received.

### mRxBroadcast

```
uint32_t otMacCounters::mRxBroadcast
```

**Description:** The total number of broadcast frames received.

### mRxData

```
uint32_t otMacCounters::mRxData
```

**Description:** The total number of MAC Data frames received.

### mRxDataPoll

```
uint32_t otMacCounters::mRxDataPoll
```

**Description:** The total number of MAC Data Poll frames received.

### mRxBeacon

```
uint32_t otMacCounters::mRxBeacon
```

**Description:** The total number of MAC Beacon frames received.

### mRxBeaconRequest

```
uint32_t otMacCounters::mRxBeaconRequest
```

**Description:** The total number of MAC Beacon Request frames received.

### mRxOther

```
uint32_t otMacCounters::mRxOther
```

**Description:** The total number of other types of frames received.

### mRxAddressFiltered

```
uint32_t otMacCounters::mRxAddressFiltered
```

**Description:** The total number of frames dropped by MAC Filter module, for example received from denylisted node.

### mRxDestAddrFiltered

```
uint32_t otMacCounters::mRxDestAddrFiltered
```

**Description:** The total number of frames dropped by destination address check, for example received frame for other node.

### mRxDuplicated

```
uint32_t otMacCounters::mRxDuplicated
```

**Description:** The total number of frames dropped due to duplication, that is when the frame has been already received.

**Details:** This counter may be incremented, for example when ACK frame generated by the receiver hasn't reached transmitter node which performed retransmission.

### mRxErrNoFrame

```
uint32_t otMacCounters::mRxErrNoFrame
```

**Description:** The total number of frames dropped because of missing or malformed content.

### mRxErrUnknownNeighbor

```
uint32_t otMacCounters::mRxErrUnknownNeighbor
```

**Description:** The total number of frames dropped due to unknown neighbor.

### mRxErrInvalidSrcAddr

```
uint32_t otMacCounters::mRxErrInvalidSrcAddr
```

**Description:** The total number of frames dropped due to invalid source address.

### mRxErrSec

```
uint32_t otMacCounters::mRxErrSec
```

**Description:** The total number of frames dropped due to security error.

**Details:** This counter may be incremented, for example when lower than expected Frame Counter is used to encrypt the frame.

### mRxErrFcs

```
uint32_t otMacCounters::mRxErrFcs
```

**Description:** The total number of frames dropped due to invalid FCS.

### mRxErrOther

```
uint32_t otMacCounters::mRxErrOther
```

**Description:** The total number of frames dropped due to other error.