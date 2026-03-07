# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-mdns-local-host-address.md

Represents a local host IPv4 or IPv6 address entry. 

## Public Attributes

### mIsIp6

```
bool otMdnsLocalHostAddress::mIsIp6
```

**Description:** Indicates whether the address is IPv6 (`true`) or IPv4 (`false`).

### mInfraIfIndex

```
uint32_t otMdnsLocalHostAddress::mInfraIfIndex
```

**Description:** The infrastructure network interface index.

### mIp6

```
otIp6Address otMdnsLocalHostAddress::mIp6
```

**Description:** The IPv6 address (valid when `mIsIp6` is true).

### mIp4

```
otIp4Address otMdnsLocalHostAddress::mIp4
```

**Description:** The IPv4 address (valid when `mIsIp6` is false).

### mAddress

```
union otMdnsLocalHostAddress::@5 otMdnsLocalHostAddress::mAddress
```

**Description:** The address.