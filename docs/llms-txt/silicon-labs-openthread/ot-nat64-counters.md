# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-nat64-counters.md

Represents the counters for NAT64. 

## Public Attributes

### m4To6Packets

```
uint64_t otNat64Counters::m4To6Packets
```

**Description:** Number of packets translated from IPv4 to IPv6.

### m4To6Bytes

```
uint64_t otNat64Counters::m4To6Bytes
```

**Description:** Sum of size of packets translated from IPv4 to IPv6.

### m6To4Packets

```
uint64_t otNat64Counters::m6To4Packets
```

**Description:** Number of packets translated from IPv6 to IPv4.

### m6To4Bytes

```
uint64_t otNat64Counters::m6To4Bytes
```

**Description:** Sum of size of packets translated from IPv6 to IPv4.