# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-link-raw.md

# Raw Link

This module includes functions that control the raw link-layer configuration. 

## Typedefs

### otLinkRawReceiveDone

`typedef void(* otLinkRawReceiveDone) (otInstance *aInstance, otRadioFrame *aFrame, otError aError)`

**Description:**

Pointer on receipt of a IEEE 802.15.4 frame.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|A pointer to an OpenThread instance.|
||[in]|aFrame|A pointer to the received frame or NULL if the receive operation was aborted.|
||[in]|aError|OT_ERROR_NONE when successfully received a frame. OT_ERROR_ABORT when reception was aborted and a frame was not received.|

**Details:**

### otLinkRawTransmitDone

`typedef void(* otLinkRawTransmitDone) (otInstance *aInstance, otRadioFrame *aFrame, otRadioFrame *aAckFrame, otError aError)`

**Description:**

Pointer on receipt of a IEEE 802.15.4 frame.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|A pointer to an OpenThread instance.|
||[in]|aFrame|A pointer to the frame that was transmitted.|
||[in]|aAckFrame|A pointer to the ACK frame.|
||[in]|aError|OT_ERROR_NONE when the frame was transmitted. OT_ERROR_NO_ACK when the frame was transmitted but no ACK was received OT_ERROR_CHANNEL_ACCESS_FAILURE when the transmission could not take place due to activity on the channel. OT_ERROR_ABORT when transmission was aborted for other reasons.|

**Details:**

### otLinkRawEnergyScanDone

`typedef void(* otLinkRawEnergyScanDone) (otInstance *aInstance, int8_t aEnergyScanMaxRssi)`

**Description:**

Pointer on receipt of a IEEE 802.15.4 frame.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|A pointer to an OpenThread instance.|
||[in]|aEnergyScanMaxRssi|The maximum RSSI encountered on the scanned channel.|

**Details:**

## Functions

### otLinkRawSetReceiveDone

`otError otLinkRawSetReceiveDone(otInstance *aInstance, otLinkRawReceiveDone aCallback)`

**Description:** Enables/disables the raw link-layer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otLinkRawReceiveDone](api-link-raw#ot-link-raw-receive-done)|[in]|aCallback|A pointer to a function called on receipt of a IEEE 802.15.4 frame. NULL to disable the raw-link layer.|

### otLinkRawIsEnabled

`bool otLinkRawIsEnabled(otInstance *aInstance)`

**Description:** Indicates whether or not the raw link-layer is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkRawGetPromiscuous

`bool otLinkRawGetPromiscuous(otInstance *aInstance)`

**Description:** Gets the status of promiscuous mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkRawSetPromiscuous

`otError otLinkRawSetPromiscuous(otInstance *aInstance, bool aEnable)`

**Description:** Enables or disables promiscuous mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|A value to enable or disable promiscuous mode.|

### otLinkRawSetShortAddress

`otError otLinkRawSetShortAddress(otInstance *aInstance, uint16_t aShortAddress)`

**Description:** Set the Short Address for address filtering.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint16_t|[in]|aShortAddress|The IEEE 802.15.4 Short Address.|

### otLinkRawSetAlternateShortAddress

`otError otLinkRawSetAlternateShortAddress(otInstance *aInstance, otShortAddress aShortAddress)`

**Description:** Set the alternate short address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|
|[otShortAddress](radio-types#ot-short-address)|[in]|aShortAddress|The alternate short address. `OT_RADIO_INVALID_SHORT_ADDR` to clear.|

This is an optional API. Support for this is indicated by including the capability `OT_RADIO_CAPS_ALT_SHORT_ADDR` in `otLinkRawGetCaps()`.

When supported, the radio will accept received frames destined to the specified alternate short address in addition to the short address provided in `otLinkRawSetShortAddress()`.

The `aShortAddress` can be set to `OT_RADIO_INVALID_SHORT_ADDR` (0xfffe) to clear any previously set alternate short address.

### otLinkRawSleep

`otError otLinkRawSleep(otInstance *aInstance)`

**Description:** Transition the radio from Receive to Sleep.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Turn off the radio.

### otLinkRawReceive

`otError otLinkRawReceive(otInstance *aInstance)`

**Description:** Transitioning the radio from Sleep to Receive.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Turn on the radio.

### otLinkRawGetTransmitBuffer

`otRadioFrame * otLinkRawGetTransmitBuffer(otInstance *aInstance)`

**Description:** The radio transitions from Transmit to Receive.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Returns a pointer to the transmit buffer.

The caller forms the IEEE 802.15.4 frame in this buffer then calls [otLinkRawTransmit()](api-link-raw#ot-link-raw-transmit) to request transmission.

**Returns**

- A pointer to the transmit buffer or NULL if the raw link-layer isn't enabled.

### otLinkRawTransmit

`otError otLinkRawTransmit(otInstance *aInstance, otLinkRawTransmitDone aCallback)`

**Description:** Begins the transmit sequence on the radio.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otLinkRawTransmitDone](api-link-raw#ot-link-raw-transmit-done)|[in]|aCallback|A pointer to a function called on completion of the transmission.|

The caller must form the IEEE 802.15.4 frame in the buffer provided by [otLinkRawGetTransmitBuffer()](api-link-raw#ot-link-raw-get-transmit-buffer) before requesting transmission. The channel and transmit power are also included in the [otRadioFrame](ot-radio-frame) structure.

The transmit sequence consists of:

1. Transitioning the radio to Transmit from Receive.
2. Transmits the PSDU on the given channel and at the given transmit power.

### otLinkRawGetRssi

`int8_t otLinkRawGetRssi(otInstance *aInstance)`

**Description:** Get the most recent RSSI measurement.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- The RSSI in dBm when it is valid. 127 when RSSI is invalid.

### otLinkRawGetCaps

`otRadioCaps otLinkRawGetCaps(otInstance *aInstance)`

**Description:** Get the radio capabilities.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- The radio capability bit vector. The stack enables or disables some functions based on this value.

### otLinkRawEnergyScan

`otError otLinkRawEnergyScan(otInstance *aInstance, uint8_t aScanChannel, uint16_t aScanDuration, otLinkRawEnergyScanDone aCallback)`

**Description:** Begins the energy scan sequence on the radio.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aScanChannel|The channel to perform the energy scan on.|
|uint16_t|[in]|aScanDuration|The duration, in milliseconds, for the channel to be scanned.|
|[otLinkRawEnergyScanDone](api-link-raw#ot-link-raw-energy-scan-done)|[in]|aCallback|A pointer to a function called on completion of a scanned channel.|

### otLinkRawSrcMatchEnable

`otError otLinkRawSrcMatchEnable(otInstance *aInstance, bool aEnable)`

**Description:** Enable/Disable source match for frame pending.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|Enable/disable source match for frame pending.|

### otLinkRawSrcMatchAddShortEntry

`otError otLinkRawSrcMatchAddShortEntry(otInstance *aInstance, uint16_t aShortAddress)`

**Description:** Adding short address to the source match table.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint16_t|[in]|aShortAddress|The short address to be added.|

### otLinkRawSrcMatchAddExtEntry

`otError otLinkRawSrcMatchAddExtEntry(otInstance *aInstance, const otExtAddress *aExtAddress)`

**Description:** Adding extended address to the source match table.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|The extended address to be added.|

### otLinkRawSrcMatchClearShortEntry

`otError otLinkRawSrcMatchClearShortEntry(otInstance *aInstance, uint16_t aShortAddress)`

**Description:** Removing short address to the source match table.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint16_t|[in]|aShortAddress|The short address to be removed.|

### otLinkRawSrcMatchClearExtEntry

`otError otLinkRawSrcMatchClearExtEntry(otInstance *aInstance, const otExtAddress *aExtAddress)`

**Description:** Removing extended address to the source match table of the radio.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|The extended address to be removed.|

### otLinkRawSrcMatchClearShortEntries

`otError otLinkRawSrcMatchClearShortEntries(otInstance *aInstance)`

**Description:** Removing all the short addresses from the source match table.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkRawSrcMatchClearExtEntries

`otError otLinkRawSrcMatchClearExtEntries(otInstance *aInstance)`

**Description:** Removing all the extended addresses from the source match table.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkRawSetMacKey

`otError otLinkRawSetMacKey(otInstance *aInstance, uint8_t aKeyIdMode, uint8_t aKeyId, const otMacKey *aPrevKey, const otMacKey *aCurrKey, const otMacKey *aNextKey)`

**Description:** Update MAC keys and key index.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aKeyIdMode|The key ID mode.|
|uint8_t|[in]|aKeyId|The key index.|
|const [otMacKey](ot-mac-key) *|[in]|aPrevKey|The previous MAC key.|
|const [otMacKey](ot-mac-key) *|[in]|aCurrKey|The current MAC key.|
|const [otMacKey](ot-mac-key) *|[in]|aNextKey|The next MAC key.|

### otLinkRawSetMacFrameCounter

`otError otLinkRawSetMacFrameCounter(otInstance *aInstance, uint32_t aMacFrameCounter)`

**Description:** Sets the current MAC frame counter value.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aMacFrameCounter|The MAC frame counter value.|

Always sets the MAC counter to the new given value `aMacFrameCounter` independent of the current value.

### otLinkRawSetMacFrameCounterIfLarger

`otError otLinkRawSetMacFrameCounterIfLarger(otInstance *aInstance, uint32_t aMacFrameCounter)`

**Description:** Sets the current MAC frame counter value only if the new value is larger than the current one.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aMacFrameCounter|The MAC frame counter value.|

### otLinkRawGetRadioTime

`uint64_t otLinkRawGetRadioTime(otInstance *aInstance)`

**Description:** Get current platform time (64bits width) of the radio chip.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- The current radio time in microseconds.