# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-link-link.md

# Link

This module includes functions that control link-layer configuration.

## Modules

[otMacFilterEntry](ot-mac-filter-entry)

[otMacCounters](ot-mac-counters)

[otActiveScanResult](ot-active-scan-result)

[otEnergyScanResult](ot-energy-scan-result)

## Enumerations

### otMacFilterAddressMode

```c
enum otMacFilterAddressMode {
    OT_MAC_FILTER_ADDRESS_MODE_DISABLED
    OT_MAC_FILTER_ADDRESS_MODE_ALLOWLIST
    OT_MAC_FILTER_ADDRESS_MODE_DENYLIST
}
```

**Description:**

Defines address mode of the mac filter.

**Enumerator:**

|   |   |
|---|---|
|OT_MAC_FILTER_ADDRESS_MODE_DISABLED|Address filter is disabled.|
|OT_MAC_FILTER_ADDRESS_MODE_ALLOWLIST|Allowlist address filter mode is enabled.|
|OT_MAC_FILTER_ADDRESS_MODE_DENYLIST|Denylist address filter mode is enabled.|

## Typedefs

### otMacFilterIterator

`typedef uint8_t otMacFilterIterator`

**Description:**

Used to iterate through mac filter entries.

### otMacFilterAddressMode (Typedefs)

`typedef enum otMacFilterAddressMode otMacFilterAddressMode`

**Description:**

Defines address mode of the mac filter.

### otMacFilterEntry

`typedef struct otMacFilterEntry otMacFilterEntry`

**Description:**

Represents a Mac Filter entry.

### otMacCounters

`typedef struct otMacCounters otMacCounters`

**Description:**

Represents the MAC layer counters.

### otActiveScanResult

`typedef struct otActiveScanResult otActiveScanResult`

**Description:**

Represents a received IEEE 802.15.4 Beacon.

### otEnergyScanResult

`typedef struct otEnergyScanResult otEnergyScanResult`

**Description:**

Represents an energy scan result.

### otHandleActiveScanResult

`typedef void(* otHandleActiveScanResult) (otActiveScanResult *aResult, void *aContext)`

**Description:**

Pointer is called during an IEEE 802.15.4 Active Scan when an IEEE 802.15.4 Beacon is received or the scan completes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aResult|A valid pointer to the beacon information or NULL when the active scan completes.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otHandleEnergyScanResult

`typedef void(* otHandleEnergyScanResult) (otEnergyScanResult *aResult, void *aContext)`

**Description:**

Pointer is called during an IEEE 802.15.4 Energy Scan when the result for a channel is ready or the scan completes.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aResult|A valid pointer to the energy scan result information or NULL when the energy scan completes.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otLinkPcapCallback

`typedef void(* otLinkPcapCallback) (const otRadioFrame *aFrame, bool aIsTx, void *aContext)`

**Description:**

Pointer is called when an IEEE 802.15.4 frame is received.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aFrame|A pointer to the received IEEE 802.15.4 frame.|
||[in]|aIsTx|Whether this frame is transmitted, not received.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

#### Note

- This callback is called after FCS processing and `aFrame` may not contain the actual FCS that was received.
- This callback is called before IEEE 802.15.4 security processing.

## Functions

### otLinkActiveScan

`otError otLinkActiveScan(otInstance *aInstance, uint32_t aScanChannels, uint16_t aScanDuration, otHandleActiveScanResult aCallback, void *aCallbackContext)`

**Description:** Starts an IEEE 802.15.4 Active Scan.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aScanChannels|A bit vector indicating which channels to scan (e.g. OT_CHANNEL_11_MASK).|
|uint16_t|[in]|aScanDuration|The time in milliseconds to spend scanning each channel.|
|[otHandleActiveScanResult](api-link-link#ot-handle-active-scan-result)|[in]|aCallback|A pointer to a function called on receiving a beacon or scan completes.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|

### otLinkIsActiveScanInProgress

`bool otLinkIsActiveScanInProgress(otInstance *aInstance)`

**Description:** Indicates whether or not an IEEE 802.15.4 Active Scan is currently in progress.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns

- true if an IEEE 802.15.4 Active Scan is in progress, false otherwise.

### otLinkEnergyScan

`otError otLinkEnergyScan(otInstance *aInstance, uint32_t aScanChannels, uint16_t aScanDuration, otHandleEnergyScanResult aCallback, void *aCallbackContext)`

**Description:** Starts an IEEE 802.15.4 Energy Scan.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aScanChannels|A bit vector indicating on which channels to perform energy scan.|
|uint16_t|[in]|aScanDuration|The time in milliseconds to spend scanning each channel.|
|[otHandleEnergyScanResult](api-link-link#ot-handle-energy-scan-result)|[in]|aCallback|A pointer to a function called to pass on scan result on indicate scan completion.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|

### otLinkIsEnergyScanInProgress

`bool otLinkIsEnergyScanInProgress(otInstance *aInstance)`

**Description:** Indicates whether or not an IEEE 802.15.4 Energy Scan is currently in progress.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkIsEnergyScanInProgress)

- true if an IEEE 802.15.4 Energy Scan is in progress, false otherwise.

### otLinkSendDataRequest

`otError otLinkSendDataRequest(otInstance *aInstance)`

**Description:** Enqueues an IEEE 802.15.4 Data Request message for transmission.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkIsInTransmitState

`bool otLinkIsInTransmitState(otInstance *aInstance)`

**Description:** Indicates whether or not an IEEE 802.15.4 MAC is in the transmit state.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

MAC module is in the transmit state during CSMA/CA procedure, CCA, Data, Beacon or Data Request frame transmission and receiving an ACK of a transmitted frame. MAC module is not in the transmit state during transmission of an ACK frame or a Beacon Request frame.

#### Returns (otLinkIsInTransmitState)

- true if an IEEE 802.15.4 MAC is in the transmit state, false otherwise.

### otLinkGetChannel

`uint8_t otLinkGetChannel(otInstance *aInstance)`

**Description:** Get the IEEE 802.15.4 channel.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetChannel)

- The IEEE 802.15.4 channel.

##### See Also

- [otLinkSetChannel](api-link-link#ot-link-set-channel)

### otLinkSetChannel

`otError otLinkSetChannel(otInstance *aInstance, uint8_t aChannel)`

**Description:** Set the IEEE 802.15.4 channel.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aChannel|The IEEE 802.15.4 channel.|

Succeeds only when Thread protocols are disabled. A successful call to this function invalidates the Active and Pending Operational Datasets in non-volatile memory.

#### See Also (otLinkSetChannel)

- [otLinkGetChannel](api-link-link#ot-link-get-channel)

### otLinkGetSupportedChannelMask

`uint32_t otLinkGetSupportedChannelMask(otInstance *aInstance)`

**Description:** Get the supported channel mask of MAC layer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetSupportedChannelMask)

- The supported channel mask as `uint32_t` with bit 0 (lsb) mapping to channel 0, bit 1 to channel 1, so on.

### otLinkSetSupportedChannelMask

`otError otLinkSetSupportedChannelMask(otInstance *aInstance, uint32_t aChannelMask)`

**Description:** Set the supported channel mask of MAC layer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aChannelMask|The supported channel mask (bit 0 or lsb mapping to channel 0, and so on).|

Succeeds only when Thread protocols are disabled.

### otLinkGetExtendedAddress

`const otExtAddress * otLinkGetExtendedAddress(otInstance *aInstance)`

**Description:** Gets the IEEE 802.15.4 Extended Address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetExtendedAddress)

- A pointer to the IEEE 802.15.4 Extended Address.

### otLinkSetExtendedAddress

`otError otLinkSetExtendedAddress(otInstance *aInstance, const otExtAddress *aExtAddress)`

**Description:** Sets the IEEE 802.15.4 Extended Address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|A pointer to the IEEE 802.15.4 Extended Address.|

#### Note (otLinkSetExtendedAddress)

- Only succeeds when Thread protocols are disabled.

### otLinkGetFactoryAssignedIeeeEui64

`void otLinkGetFactoryAssignedIeeeEui64(otInstance *aInstance, otExtAddress *aEui64)`

**Description:** Get the factory-assigned IEEE EUI-64.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otExtAddress](ot-ext-address) *|[out]|aEui64|A pointer to where the factory-assigned IEEE EUI-64 is placed.|

### otLinkGetPanId

`otPanId otLinkGetPanId(otInstance *aInstance)`

**Description:** Get the IEEE 802.15.4 PAN ID.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetPanId)

- The IEEE 802.15.4 PAN ID.

##### See Also (Returns)

- [otLinkSetPanId](api-link-link#ot-link-set-pan-id)

### otLinkSetPanId

`otError otLinkSetPanId(otInstance *aInstance, otPanId aPanId)`

**Description:** Set the IEEE 802.15.4 PAN ID.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otPanId](radio-types#ot-pan-id)|[in]|aPanId|The IEEE 802.15.4 PAN ID.|

Succeeds only when Thread protocols are disabled. A successful call to this function also invalidates the Active and Pending Operational Datasets in non-volatile memory.

#### See Also (otLinkSetPanId)

- [otLinkGetPanId](api-link-link#ot-link-get-pan-id)

### otLinkGetPollPeriod

`uint32_t otLinkGetPollPeriod(otInstance *aInstance)`

**Description:** Get the data poll period of sleepy end device.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetPollPeriod)

- The data poll period of sleepy end device in milliseconds.

##### See Also (otLinkGetPollPeriod)

- [otLinkSetPollPeriod](api-link-link#ot-link-set-poll-period)

### otLinkSetPollPeriod

`otError otLinkSetPollPeriod(otInstance *aInstance, uint32_t aPollPeriod)`

**Description:** Set/clear user-specified/external data poll period for sleepy end device.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aPollPeriod|data poll period in milliseconds.|

#### Note (otLinkSetPollPeriod)

- This function updates only poll period of sleepy end device. To update child timeout the function `otThreadSetChildTimeout()` shall be called.
- Minimal non-zero value should be `OPENTHREAD_CONFIG_MAC_MINIMUM_POLL_PERIOD` (10ms). Or zero to clear user-specified poll period.
- User-specified value should be no more than the maximal value 0x3FFFFFF ((1 << 26) - 1) allowed, otherwise it would be clipped by the maximal value.

##### See Also (Note)

- [otLinkGetPollPeriod](api-link-link#ot-link-get-poll-period)

### otLinkGetShortAddress

`otShortAddress otLinkGetShortAddress(otInstance *aInstance)`

**Description:** Get the IEEE 802.15.4 Short Address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetShortAddress)

- The IEEE 802.15.4 Short Address.

### otLinkGetAlternateShortAddress

`otShortAddress otLinkGetAlternateShortAddress(otInstance *aInstance)`

**Description:** Get the IEEE 802.15.4 alternate short address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetAlternateShortAddress)

- The alternate short address, or `OT_RADIO_INVALID_SHORT_ADDR` (0xfffe) if there is no alternate address.

### otLinkGetMaxFrameRetriesDirect

`uint8_t otLinkGetMaxFrameRetriesDirect(otInstance *aInstance)`

**Description:** Returns the maximum number of frame retries during direct transmission.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetMaxFrameRetriesDirect)

- The maximum number of retries during direct transmission.

### otLinkSetMaxFrameRetriesDirect

`void otLinkSetMaxFrameRetriesDirect(otInstance *aInstance, uint8_t aMaxFrameRetriesDirect)`

**Description:** Sets the maximum number of frame retries during direct transmission.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aMaxFrameRetriesDirect|The maximum number of retries during direct transmission.|

### otLinkGetMaxFrameRetriesIndirect

`uint8_t otLinkGetMaxFrameRetriesIndirect(otInstance *aInstance)`

**Description:** Returns the maximum number of frame retries during indirect transmission.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetMaxFrameRetriesIndirect)

- The maximum number of retries during indirect transmission.

### otLinkSetMaxFrameRetriesIndirect

`void otLinkSetMaxFrameRetriesIndirect(otInstance *aInstance, uint8_t aMaxFrameRetriesIndirect)`

**Description:** Sets the maximum number of frame retries during indirect transmission.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aMaxFrameRetriesIndirect|The maximum number of retries during indirect transmission.|

### otLinkGetFrameCounter

`uint32_t otLinkGetFrameCounter(otInstance *aInstance)`

**Description:** Gets the current MAC frame counter value.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

#### Returns (otLinkGetFrameCounter)

- The current MAC frame counter value.

### otLinkFilterGetAddressMode

`otMacFilterAddressMode otLinkFilterGetAddressMode(otInstance *aInstance)`

**Description:** Gets the address mode of MAC filter.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

#### Returns (otLinkFilterGetAddressMode)

- the address mode.

### otLinkFilterSetAddressMode

`void otLinkFilterSetAddressMode(otInstance *aInstance, otMacFilterAddressMode aMode)`

**Description:** Sets the address mode of MAC filter.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMacFilterAddressMode](api-link-link#ot-mac-filter-address-mode)|[in]|aMode|The address mode to set.|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkFilterAddAddress

`otError otLinkFilterAddAddress(otInstance *aInstance, const otExtAddress *aExtAddress)`

**Description:** Adds an Extended Address to MAC filter.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|A pointer to the Extended Address (MUST NOT be NULL).|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkFilterRemoveAddress

`void otLinkFilterRemoveAddress(otInstance *aInstance, const otExtAddress *aExtAddress)`

**Description:** Removes an Extended Address from MAC filter.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|A pointer to the Extended Address (MUST NOT be NULL).|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

No action is performed if there is no existing entry in Filter matching the given Extended Address.

### otLinkFilterClearAddresses

`void otLinkFilterClearAddresses(otInstance *aInstance)`

**Description:** Clears all the Extended Addresses from MAC filter.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkFilterGetNextAddress

`otError otLinkFilterGetNextAddress(otInstance *aInstance, otMacFilterIterator *aIterator, otMacFilterEntry *aEntry)`

**Description:** Gets an in-use address filter entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMacFilterIterator](api-link-link#ot-mac-filter-iterator) *|[inout]|aIterator|A pointer to the MAC filter iterator context. To get the first in-use address filter entry, it should be set to OT_MAC_FILTER_ITERATOR_INIT. MUST NOT be NULL.|
|[otMacFilterEntry](ot-mac-filter-entry) *|[out]|aEntry|A pointer to where the information is placed. MUST NOT be NULL.|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkFilterAddRssIn

`otError otLinkFilterAddRssIn(otInstance *aInstance, const otExtAddress *aExtAddress, int8_t aRss)`

**Description:** Adds the specified Extended Address to the `RssIn` list (or modifies an existing address in the `RssIn` list) and sets the received signal strength (in dBm) entry for messages from that address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|A pointer to the IEEE 802.15.4 Extended Address. MUST NOT be NULL.|
|int8_t|[in]|aRss|A received signal strength (in dBm).|

The Extended Address does not necessarily have to be in the `address allowlist/denylist` filter to set the `rss`. **Note**

- The `RssIn` list contains Extended Addresses whose `rss` or link quality indicator (`lqi`) values have been set to be different from the defaults.

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkFilterRemoveRssIn

`void otLinkFilterRemoveRssIn(otInstance *aInstance, const otExtAddress *aExtAddress)`

**Description:** Removes the specified Extended Address from the `RssIn` list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|A pointer to the IEEE 802.15.4 Extended Address. MUST NOT be NULL.|

Once removed from the `RssIn` list, this MAC address will instead use the default `rss` and `lqi` settings, assuming defaults have been set. (If no defaults have been set, the over-air signal is used.)

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

No action is performed if there is no existing entry in the `RssIn` list matching the specified Extended Address.

### otLinkFilterSetDefaultRssIn

`void otLinkFilterSetDefaultRssIn(otInstance *aInstance, int8_t aRss)`

**Description:** Sets the default received signal strength (in dBm) on MAC Filter.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|int8_t|[in]|aRss|The default received signal strength (in dBm) to set.|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

The default RSS value is used for all received frames from addresses for which there is no explicit RSS-IN entry in the Filter list (added using `otLinkFilterAddRssIn()`).

### otLinkFilterClearDefaultRssIn

`void otLinkFilterClearDefaultRssIn(otInstance *aInstance)`

**Description:** Clears any previously set default received signal strength (in dBm) on MAC Filter.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkFilterClearAllRssIn

`void otLinkFilterClearAllRssIn(otInstance *aInstance)`

**Description:** Clears all the received signal strength (`rss`) and link quality indicator (`lqi`) entries (including defaults) from the `RssIn` list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Performing this action means that all Extended Addresses will use the on-air signal.

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkFilterGetNextRssIn

`otError otLinkFilterGetNextRssIn(otInstance *aInstance, otMacFilterIterator *aIterator, otMacFilterEntry *aEntry)`

**Description:** Gets an in-use RssIn filter entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otMacFilterIterator](api-link-link#ot-mac-filter-iterator) *|[inout]|aIterator|A pointer to the MAC filter iterator context. MUST NOT be NULL. To get the first entry, it should be set to OT_MAC_FILTER_ITERATOR_INIT.|
|[otMacFilterEntry](ot-mac-filter-entry) *|[out]|aEntry|A pointer to where the information is placed. The last entry would have the extended address as all 0xff to indicate the default received signal strength if it was set. `aEntry` MUST NOT be NULL.|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkSetRadioFilterEnabled

`void otLinkSetRadioFilterEnabled(otInstance *aInstance, bool aFilterEnabled)`

**Description:** Enables/disables IEEE 802.15.4 radio filter mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aFilterEnabled|TRUE to enable radio filter, FALSE to disable|

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

The radio filter is mainly intended for testing. It can be used to temporarily block all tx/rx on the 802.15.4 radio. When radio filter is enabled, radio is put to sleep instead of receive (to ensure device does not receive any frame and/or potentially send ack). Also the frame transmission requests return immediately without sending the frame over the air (return "no ack" error if ack is requested, otherwise return success).

### otLinkIsRadioFilterEnabled

`bool otLinkIsRadioFilterEnabled(otInstance *aInstance)`

**Description:** Indicates whether the IEEE 802.15.4 radio filter is enabled or not.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

Is available when `OPENTHREAD_CONFIG_MAC_FILTER_ENABLE` configuration is enabled.

### otLinkConvertRssToLinkQuality

`uint8_t otLinkConvertRssToLinkQuality(otInstance *aInstance, int8_t aRss)`

**Description:** Converts received signal strength to link quality.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|int8_t|[in]|aRss|The received signal strength value to be converted.|

#### Returns (otLinkConvertRssToLinkQuality)

- Link quality value mapping to `aRss`.

### otLinkConvertLinkQualityToRss

`int8_t otLinkConvertLinkQualityToRss(otInstance *aInstance, uint8_t aLinkQuality)`

**Description:** Converts link quality to typical received signal strength.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aLinkQuality|LinkQuality value, should be in range [0,3].|

#### Returns (otLinkConvertLinkQualityToRss)

- Typical platform received signal strength mapping to `aLinkQuality`.

### otLinkGetTxDirectRetrySuccessHistogram

`const uint32_t * otLinkGetTxDirectRetrySuccessHistogram(otInstance *aInstance, uint8_t *aNumberOfEntries)`

**Description:** Gets histogram of retries for a single direct packet until success.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t *|[out]|aNumberOfEntries|A pointer to where the size of returned histogram array is placed.|

Is valid when OPENTHREAD_CONFIG_MAC_RETRY_SUCCESS_HISTOGRAM_ENABLE configuration is enabled.

#### Returns (otLinkGetTxDirectRetrySuccessHistogram)

- A pointer to the histogram of retries (in a form of an array). The n-th element indicates that the packet has been sent with n-th retry.

### otLinkGetTxIndirectRetrySuccessHistogram

`const uint32_t * otLinkGetTxIndirectRetrySuccessHistogram(otInstance *aInstance, uint8_t *aNumberOfEntries)`

**Description:** Gets histogram of retries for a single indirect packet until success.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t *|[out]|aNumberOfEntries|A pointer to where the size of returned histogram array is placed.|

Is valid when OPENTHREAD_CONFIG_MAC_RETRY_SUCCESS_HISTOGRAM_ENABLE configuration is enabled.

#### Returns (otLinkGetTxIndirectRetrySuccessHistogram)

- A pointer to the histogram of retries (in a form of an array). The n-th element indicates that the packet has been sent with n-th retry.

### otLinkResetTxRetrySuccessHistogram

`void otLinkResetTxRetrySuccessHistogram(otInstance *aInstance)`

**Description:** Clears histogram statistics for direct and indirect transmissions.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Is valid when OPENTHREAD_CONFIG_MAC_RETRY_SUCCESS_HISTOGRAM_ENABLE configuration is enabled.

### otLinkGetCounters

`const otMacCounters * otLinkGetCounters(otInstance *aInstance)`

**Description:** Get the MAC layer counters.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetCounters)

- A pointer to the MAC layer counters.

### otLinkResetCounters

`void otLinkResetCounters(otInstance *aInstance)`

**Description:** Resets the MAC layer counters.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkSetPcapCallback

`void otLinkSetPcapCallback(otInstance *aInstance, otLinkPcapCallback aPcapCallback, void *aCallbackContext)`

**Description:** Registers a callback to provide received raw IEEE 802.15.4 frames.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otLinkPcapCallback](api-link-link#ot-link-pcap-callback)|[in]|aPcapCallback|A pointer to a function that is called when receiving an IEEE 802.15.4 link frame or NULL to disable the callback.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|

### otLinkIsPromiscuous

`bool otLinkIsPromiscuous(otInstance *aInstance)`

**Description:** Indicates whether or not promiscuous mode is enabled at the link layer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkSetPromiscuous

`otError otLinkSetPromiscuous(otInstance *aInstance, bool aPromiscuous)`

**Description:** Enables or disables the link layer promiscuous mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aPromiscuous|true to enable promiscuous mode, or false otherwise.|

#### Note (otLinkSetPromiscuous)

- Promiscuous mode may only be enabled when the Thread interface is disabled.

### otLinkGetCslChannel

`uint8_t otLinkGetCslChannel(otInstance *aInstance)`

**Description:** Gets the CSL channel.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetCslChannel)

- The CSL channel.

### otLinkSetCslChannel

`otError otLinkSetCslChannel(otInstance *aInstance, uint8_t aChannel)`

**Description:** Sets the CSL channel.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aChannel|The CSL sample channel. Channel value should be `0` (Set CSL Channel unspecified) or within the range [1, 10] (if 915-MHz supported) and [11, 26] (if 2.4 GHz supported).|

### otLinkGetCslPeriod

`uint32_t otLinkGetCslPeriod(otInstance *aInstance)`

**Description:** Gets the CSL period in microseconds.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetCslPeriod)

- The CSL period in microseconds.

### otLinkSetCslPeriod

`otError otLinkSetCslPeriod(otInstance *aInstance, uint32_t aPeriod)`

**Description:** Sets the CSL period in microseconds.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aPeriod|The CSL period in microseconds.|

Disable CSL by setting this parameter to `0`.

The CSL period MUST be a multiple of `OT_LINK_CSL_PERIOD_TEN_SYMBOLS_UNIT_IN_USEC`, otherwise `OT_ERROR_INVALID_ARGS` is returned.

### otLinkGetCslTimeout

`uint32_t otLinkGetCslTimeout(otInstance *aInstance)`

**Description:** Gets the CSL timeout.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otLinkGetCslTimeout)

- The CSL timeout in seconds.

### otLinkSetCslTimeout

`otError otLinkSetCslTimeout(otInstance *aInstance, uint32_t aTimeout)`

**Description:** Sets the CSL timeout in seconds.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aTimeout|The CSL timeout in seconds.|

### otLinkGetCcaFailureRate

`uint16_t otLinkGetCcaFailureRate(otInstance *aInstance)`

**Description:** Returns the current CCA (Clear Channel Assessment) failure rate.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

The rate is maintained over a window of (roughly) last `OPENTHREAD_CONFIG_CCA_FAILURE_RATE_AVERAGING_WINDOW` frame transmissions.

#### Returns (otLinkGetCcaFailureRate)

- The CCA failure rate with maximum value `0xffff` corresponding to 100% failure rate.

### otLinkSetEnabled

`otError otLinkSetEnabled(otInstance *aInstance, bool aEnable)`

**Description:** Enables or disables the link layer.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|true to enable the link layer, or false otherwise.|

#### Note (otLinkSetEnabled)

- The link layer may only be enabled / disabled when the Thread Interface is disabled.

### otLinkIsEnabled

`bool otLinkIsEnabled(otInstance *aInstance)`

**Description:** Indicates whether or not the link layer is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkIsCslEnabled

`bool otLinkIsCslEnabled(otInstance *aInstance)`

**Description:** Indicates whether or not CSL is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkIsCslSupported

`bool otLinkIsCslSupported(otInstance *aInstance)`

**Description:** Indicates whether the device is connected to a parent which supports CSL.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

### otLinkSendEmptyData

`otError otLinkSendEmptyData(otInstance *aInstance)`

**Description:** Instructs the device to send an empty IEEE 802.15.4 data frame.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Is only supported on an Rx-Off-When-Idle device to send an empty data frame to its parent. Note: available only when `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` is enabled.

### otLinkSetRegion

`otError otLinkSetRegion(otInstance *aInstance, uint16_t aRegionCode)`

**Description:** Sets the region code.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|
|uint16_t|[in]|aRegionCode|The radio region code. The `aRegionCode >> 8` is first ascii char and the `aRegionCode & 0xff` is the second ascii char.|

The radio region format is the 2-bytes ascii representation of the ISO 3166 alpha-2 code.

### otLinkGetRegion

`otError otLinkGetRegion(otInstance *aInstance, uint16_t *aRegionCode)`

**Description:** Get the region code.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance structure.|
|uint16_t *|[out]|aRegionCode|The radio region code. The `aRegionCode >> 8` is first ascii char and the `aRegionCode & 0xff` is the second ascii char.|

The radio region format is the 2-bytes ascii representation of the ISO 3166 alpha-2 code.

### otLinkGetWakeupChannel

`uint8_t otLinkGetWakeupChannel(otInstance *aInstance)`

**Description:** Gets the Wake-up channel.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_WAKEUP_COORDINATOR_ENABLE` or `OPENTHREAD_CONFIG_WAKEUP_END_DEVICE_ENABLE`.

#### Returns (otLinkGetWakeupChannel)

- The Wake-up channel.

### otLinkSetWakeupChannel

`otError otLinkSetWakeupChannel(otInstance *aInstance, uint8_t aChannel)`

**Description:** Sets the Wake-up channel.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aChannel|The Wake-up sample channel. Channel value should be `0` (Set Wake-up Channel unspecified, which means the device will use the PAN channel) or within the range [1, 10] (if 915-MHz supported) and [11, 26] (if 2.4 GHz supported).|

Requires `OPENTHREAD_CONFIG_WAKEUP_COORDINATOR_ENABLE` or `OPENTHREAD_CONFIG_WAKEUP_END_DEVICE_ENABLE`.

### otLinkSetWakeUpListenEnabled

`otError otLinkSetWakeUpListenEnabled(otInstance *aInstance, bool aEnable)`

**Description:** Enables or disables listening for wake-up frames.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|true to enable listening for wake-up frames, or false otherwise.|

Requires `OPENTHREAD_CONFIG_WAKEUP_END_DEVICE_ENABLE`.

### otLinkIsWakeupListenEnabled

`bool otLinkIsWakeupListenEnabled(otInstance *aInstance)`

**Description:** Returns whether listening for wake-up frames is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_WAKEUP_END_DEVICE_ENABLE`.

### otLinkGetWakeupListenParameters

`void otLinkGetWakeupListenParameters(otInstance *aInstance, uint32_t *aInterval, uint32_t *aDuration)`

**Description:** Get the wake-up listen parameters.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t *|[out]|aInterval|A pointer to return the wake-up listen interval in microseconds.|
|uint32_t *|[out]|aDuration|A pointer to return the wake-up listen duration in microseconds.|

Requires `OPENTHREAD_CONFIG_WAKEUP_END_DEVICE_ENABLE`.

### otLinkSetWakeupListenParameters

`otError otLinkSetWakeupListenParameters(otInstance *aInstance, uint32_t aInterval, uint32_t aDuration)`

**Description:** Set the wake-up listen parameters.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aInterval|The wake-up listen interval in microseconds.|
|uint32_t|[in]|aDuration|The wake-up listen duration in microseconds.|

The listen interval must be greater than the listen duration. The listen duration must be greater or equal than the minimum supported.

Requires `OPENTHREAD_CONFIG_WAKEUP_END_DEVICE_ENABLE`.

### otLinkSetRxOnWhenIdle

`otError otLinkSetRxOnWhenIdle(otInstance *aInstance, bool aRxOnWhenIdle)`

**Description:** Sets the rx-on-when-idle state.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aRxOnWhenIdle|TRUE to keep radio in Receive state, FALSE to put to Sleep state during idle periods.|

## Macros

`#define OT_US_PER_TEN_SYMBOLS OT_RADIO_TEN_SYMBOLS_TIME`

**Description**: Time for 10 symbols in units of microseconds.

`#define OT_MAC_FILTER_FIXED_RSS_DISABLED 127`

**Description**: Used to indicate no fixed received signal strength was set.

`#define OT_MAC_FILTER_ITERATOR_INIT 0`

**Description**: Initializer for otMacFilterIterator.

`#define OT_LINK_CSL_PERIOD_TEN_SYMBOLS_UNIT_IN_USEC (160)`

**Description**: Represents CSL period ten symbols unit in microseconds.
