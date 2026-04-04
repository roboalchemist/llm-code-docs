# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-srp-client-host-info.md

Represents an SRP client host info. 

## Public Attributes

### mName

```
const char* otSrpClientHostInfo::mName
```

**Description:** Host name (label) string (NULL if not yet set).

### mAddresses

```
const otIp6Address* otSrpClientHostInfo::mAddresses
```

**Description:** Array of host IPv6 addresses (NULL if not set or auto address is enabled).

### mNumAddresses

```
uint8_t otSrpClientHostInfo::mNumAddresses
```

**Description:** Number of IPv6 addresses in `mAddresses` array.

### mAutoAddress

```
bool otSrpClientHostInfo::mAutoAddress
```

**Description:** Indicates whether auto address mode is enabled or not.

### mState

```
otSrpClientItemState otSrpClientHostInfo::mState
```

**Description:** Host info state.