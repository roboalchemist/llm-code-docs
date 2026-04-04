# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-icmp6-header.md

Represents an ICMPv6 header. 

## Modules

[otIcmp6Header::OT_TOOL_PACKED_FIELD](ot-icmp6-header-ot-tool-packed-field)

## Public Attributes

### mType

```
uint8_t otIcmp6Header::mType
```

**Description:** Type.

### mCode

```
uint8_t otIcmp6Header::mCode
```

**Description:** Code.

### mChecksum

```
uint16_t otIcmp6Header::mChecksum
```

**Description:** Checksum.

### mData

```
union otIcmp6Header::OT_TOOL_PACKED_FIELD otIcmp6Header::mData
```

**Description:** Message-specific data.