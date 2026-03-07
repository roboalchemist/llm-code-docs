# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-ping-sender-statistics.md

Represents statistics of a ping request. 

## Public Attributes

### mSentCount

```
uint16_t otPingSenderStatistics::mSentCount
```

**Description:** The number of ping requests already sent.

### mReceivedCount

```
uint16_t otPingSenderStatistics::mReceivedCount
```

**Description:** The number of ping replies received.

### mTotalRoundTripTime

```
uint32_t otPingSenderStatistics::mTotalRoundTripTime
```

**Description:** The total round trip time of ping requests.

### mMinRoundTripTime

```
uint16_t otPingSenderStatistics::mMinRoundTripTime
```

**Description:** The min round trip time among ping requests.

### mMaxRoundTripTime

```
uint16_t otPingSenderStatistics::mMaxRoundTripTime
```

**Description:** The max round trip time among ping requests.

### mIsMulticast

```
bool otPingSenderStatistics::mIsMulticast
```

**Description:** Whether this is a multicast ping request.