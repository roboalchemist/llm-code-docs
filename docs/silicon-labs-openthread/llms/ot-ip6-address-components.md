# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-ip6-address-components.md

Represents the components of an IPv6 address. 

## Public Attributes

### mNetworkPrefix

```
otIp6NetworkPrefix otIp6AddressComponents::mNetworkPrefix
```

**Description:** The Network Prefix (most significant 64 bits of the address)

### mIid

```
otIp6InterfaceIdentifier otIp6AddressComponents::mIid
```

**Description:** The Interface Identifier (least significant 64 bits of the address)