# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-multi-radio.md

# Multi Radio Link

This module includes definitions and functions for multi radio link.

## Modules

[otRadioLinkInfo](ot-radio-link-info)

[otMultiRadioNeighborInfo](ot-multi-radio-neighbor-info)

## Typedefs

### otRadioLinkInfo

`typedef struct otRadioLinkInfo otRadioLinkInfo`

**Description**:

Represents information associated with a radio link.

### otMultiRadioNeighborInfo

`typedef struct otMultiRadioNeighborInfo otMultiRadioNeighborInfo`

**Description**:

Represents multi radio link information associated with a neighbor.

## Functions

### otMultiRadioGetNeighborInfo

`otError otMultiRadioGetNeighborInfo(otInstance *aInstance, const otExtAddress *aExtAddress, otMultiRadioNeighborInfo *aNeighborInfo)`

**Description:** Gets the multi radio link information associated with a neighbor with a given Extended Address.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|The Extended Address of neighbor.|
|[otMultiRadioNeighborInfo](ot-multi-radio-neighbor-info) *|[out]|aNeighborInfo|A pointer to `otMultiRadioNeighborInfo` to output the neighbor info (on success).|

`OPENTHREAD_CONFIG_MULTI_RADIO` must be enabled.
