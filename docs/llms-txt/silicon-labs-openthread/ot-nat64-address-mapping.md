# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-nat64-address-mapping.md

Represents an address mapping record for NAT64. 

**Note**

- The counters will be reset for each mapping session even for the same address pair. Applications can use `mId` to identify different sessions to calculate the packets correctly.

## Public Attributes

### mId

```
uint64_t otNat64AddressMapping::mId
```

**Description:** The unique id for a mapping session.

### mIp4

```
otIp4Address otNat64AddressMapping::mIp4
```

**Description:** The IPv4 address of the mapping.

### mIp6

```
otIp6Address otNat64AddressMapping::mIp6
```

**Description:** The IPv6 address of the mapping.

### mSrcPortOrId

```
uint16_t otNat64AddressMapping::mSrcPortOrId
```

**Description:** The source port or ICMP ID of the mapping.

**Details:** Used when OPENTHREAD_CONFIG_NAT64_PORT_TRANSLATION_ENABLE is true.

### mTranslatedPortOrId

```
uint16_t otNat64AddressMapping::mTranslatedPortOrId
```

**Description:** The translated port or ICMP ID of the mapping.

**Details:** Used when OPENTHREAD_CONFIG_NAT64_PORT_TRANSLATION_ENABLE is true.

### mRemainingTimeMs

```
uint32_t otNat64AddressMapping::mRemainingTimeMs
```

**Description:** Remaining time in milliseconds before the entry expires.

**Details:** The remaining time is relative to the initialization of the `otNat64AddressMappingIterator`, i.e., when `otNat64InitAddressMappingIterator()` was called.

### mCounters

```
otNat64ProtocolCounters otNat64AddressMapping::mCounters
```

**Description:** Counters.