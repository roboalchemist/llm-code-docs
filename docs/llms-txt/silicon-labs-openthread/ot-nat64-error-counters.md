# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-nat64-error-counters.md

Represents the counters of dropped packets due to errors when handling NAT64 packets. 

## Public Attributes

### mCount4To6

```
uint64_t otNat64ErrorCounters::mCount4To6[OT_NAT64_DROP_REASON_COUNT]
```

**Description:** Errors translating IPv4 packets.

### mCount6To4

```
uint64_t otNat64ErrorCounters::mCount6To4[OT_NAT64_DROP_REASON_COUNT]
```

**Description:** Errors translating IPv6 packets.