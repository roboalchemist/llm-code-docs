# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-thread-link-info.md

Represents link-specific information for messages received from the Thread radio. 

## Public Attributes

### mPanId

```
uint16_t otThreadLinkInfo::mPanId
```

**Description:** Source PAN ID.

### mChannel

```
uint8_t otThreadLinkInfo::mChannel
```

**Description:** 802.15.4 Channel

### mRss

```
int8_t otThreadLinkInfo::mRss
```

**Description:** Received Signal Strength in dBm (averaged over fragments)

### mLqi

```
uint8_t otThreadLinkInfo::mLqi
```

**Description:** Average Link Quality Indicator (averaged over fragments)

### mLinkSecurity

```
bool otThreadLinkInfo::mLinkSecurity
```

**Description:** Indicates whether or not link security is enabled.

### mIsDstPanIdBroadcast

```
bool otThreadLinkInfo::mIsDstPanIdBroadcast
```

**Description:** Indicates whether or not destination PAN ID is broadcast.

### mTimeSyncSeq

```
uint8_t otThreadLinkInfo::mTimeSyncSeq
```

**Description:** The time sync sequence.

### mNetworkTimeOffset

```
int64_t otThreadLinkInfo::mNetworkTimeOffset
```

**Description:** The time offset to the Thread network time, in microseconds.

### mRadioType

```
uint8_t otThreadLinkInfo::mRadioType
```

**Description:** Radio link type.