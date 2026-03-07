# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-active-scan-result.md

Represents a received IEEE 802.15.4 Beacon. 

## Public Attributes

### mExtAddress

```
otExtAddress otActiveScanResult::mExtAddress
```

**Description:** IEEE 802.15.4 Extended Address.

### mNetworkName

```
otNetworkName otActiveScanResult::mNetworkName
```

**Description:** Thread Network Name.

### mExtendedPanId

```
otExtendedPanId otActiveScanResult::mExtendedPanId
```

**Description:** Thread Extended PAN ID.

### mSteeringData

```
otSteeringData otActiveScanResult::mSteeringData
```

**Description:** Steering Data.

### mPanId

```
uint16_t otActiveScanResult::mPanId
```

**Description:** IEEE 802.15.4 PAN ID.

### mJoinerUdpPort

```
uint16_t otActiveScanResult::mJoinerUdpPort
```

**Description:** Joiner UDP Port.

### mChannel

```
uint8_t otActiveScanResult::mChannel
```

**Description:** IEEE 802.15.4 Channel.

### mRssi

```
int8_t otActiveScanResult::mRssi
```

**Description:** RSSI (dBm)

### mLqi

```
uint8_t otActiveScanResult::mLqi
```

**Description:** LQI.

### mVersion

```
unsigned int otActiveScanResult::mVersion
```

**Description:** Version.

### mIsNative

```
bool otActiveScanResult::mIsNative
```

**Description:** Native Commissioner flag.

### mDiscover

```
bool otActiveScanResult::mDiscover
```

**Description:** Result from MLE Discovery.

### mIsJoinable

```
bool otActiveScanResult::mIsJoinable
```

**Description:** Joining Permitted flag.