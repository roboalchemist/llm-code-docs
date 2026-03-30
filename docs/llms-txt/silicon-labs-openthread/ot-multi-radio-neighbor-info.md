# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-multi-radio-neighbor-info.md

Represents multi radio link information associated with a neighbor. 

## Public Attributes

### mSupportsIeee802154

```
bool otMultiRadioNeighborInfo::mSupportsIeee802154
```

**Description:** Neighbor supports IEEE 802.15.4 radio link.

### mSupportsTrelUdp6

```
bool otMultiRadioNeighborInfo::mSupportsTrelUdp6
```

**Description:** Neighbor supports Thread Radio Encapsulation Link (TREL) radio link.

### mIeee802154Info

```
otRadioLinkInfo otMultiRadioNeighborInfo::mIeee802154Info
```

**Description:** Additional info for 15.4 radio link (applicable when supported).

### mTrelUdp6Info

```
otRadioLinkInfo otMultiRadioNeighborInfo::mTrelUdp6Info
```

**Description:** Additional info for TREL radio link (applicable when supported).