# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-ip6-address-info.md

Represents IPv6 address information. 

## Public Attributes

### mAddress

```
const otIp6Address* otIp6AddressInfo::mAddress
```

**Description:** A pointer to the IPv6 address.

### mPrefixLength

```
uint8_t otIp6AddressInfo::mPrefixLength
```

**Description:** The prefix length of mAddress if it is a unicast address.

### mScope

```
uint8_t otIp6AddressInfo::mScope
```

**Description:** The scope of this address.

### mPreferred

```
bool otIp6AddressInfo::mPreferred
```

**Description:** Whether this is a preferred address.

### mMeshLocal

```
bool otIp6AddressInfo::mMeshLocal
```

**Description:** Whether this is a mesh-local unicast/anycast address.