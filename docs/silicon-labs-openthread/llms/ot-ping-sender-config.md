# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-ping-sender-config.md

Represents a ping request configuration. 

## Public Attributes

### mSource

```
otIp6Address otPingSenderConfig::mSource
```

**Description:** Source address of the ping.

### mDestination

```
otIp6Address otPingSenderConfig::mDestination
```

**Description:** Destination address to ping.

### mReplyCallback

```
otPingSenderReplyCallback otPingSenderConfig::mReplyCallback
```

**Description:** Callback function to report replies (can be NULL if not needed).

### mStatisticsCallback

```
otPingSenderStatisticsCallback otPingSenderConfig::mStatisticsCallback
```

**Description:** Callback function to report statistics (can be NULL if not needed).

### mCallbackContext

```
void* otPingSenderConfig::mCallbackContext
```

**Description:** A pointer to the callback application-specific context.

### mSize

```
uint16_t otPingSenderConfig::mSize
```

**Description:** Data size (# of bytes) excludes IPv6/ICMPv6 header. Zero for default.

### mCount

```
uint16_t otPingSenderConfig::mCount
```

**Description:** Number of ping messages to send. Zero to use default.

### mInterval

```
uint32_t otPingSenderConfig::mInterval
```

**Description:** Ping tx interval in milliseconds. Zero to use default.

### mTimeout

```
uint16_t otPingSenderConfig::mTimeout
```

**Description:** Time in milliseconds to wait for final reply after sending final request.

**Details:** Zero to use default.

### mHopLimit

```
uint8_t otPingSenderConfig::mHopLimit
```

**Description:** Hop limit (used if `mAllowZeroHopLimit` is false). Zero for default.

### mAllowZeroHopLimit

```
bool otPingSenderConfig::mAllowZeroHopLimit
```

**Description:** Indicates whether hop limit is zero.

### mMulticastLoop

```
bool otPingSenderConfig::mMulticastLoop
```

**Description:** Allow looping back pings to multicast address that device is subscribed to.