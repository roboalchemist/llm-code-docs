# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-netif-address.md

Represents an IPv6 network interface unicast address. 

## Public Attributes

### mAddress

```
otIp6Address otNetifAddress::mAddress
```

**Description:** The IPv6 unicast address.

### mPrefixLength

```
uint8_t otNetifAddress::mPrefixLength
```

**Description:** The Prefix length (in bits).

### mAddressOrigin

```
uint8_t otNetifAddress::mAddressOrigin
```

**Description:** The IPv6 address origin.

### mPreferred

```
bool otNetifAddress::mPreferred
```

**Description:** TRUE if the address is preferred, FALSE otherwise.

### mValid

```
bool otNetifAddress::mValid
```

**Description:** TRUE if the address is valid, FALSE otherwise.

### mScopeOverrideValid

```
bool otNetifAddress::mScopeOverrideValid
```

**Description:** TRUE if the mScopeOverride value is valid, FALSE otherwise.

### mScopeOverride

```
unsigned int otNetifAddress::mScopeOverride
```

**Description:** The IPv6 scope of this address.

### mRloc

```
bool otNetifAddress::mRloc
```

**Description:** TRUE if the address is an RLOC, FALSE otherwise.

### mMeshLocal

```
bool otNetifAddress::mMeshLocal
```

**Description:** TRUE if the address is mesh-local, FALSE otherwise.

### mSrpRegistered

```
bool otNetifAddress::mSrpRegistered
```

**Description:** Used by OT core only (indicates whether registered by SRP Client).

### mNext

```
const struct otNetifAddress* otNetifAddress::mNext
```

**Description:** A pointer to the next network interface address.