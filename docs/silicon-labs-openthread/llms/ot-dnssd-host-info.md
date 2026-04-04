# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-dnssd-host-info.md

Represents information of a discovered host for a DNS-SD query. 

## Public Attributes

### mAddressNum

```
uint8_t otDnssdHostInfo::mAddressNum
```

**Description:** Number of host IPv6 addresses.

### mAddresses

```
const otIp6Address* otDnssdHostInfo::mAddresses
```

**Description:** Host IPv6 addresses.

### mTtl

```
uint32_t otDnssdHostInfo::mTtl
```

**Description:** Service TTL (in seconds).