# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-trel.md

# TREL - Thread Stack

This module defines Thread Radio Encapsulation Link (TREL) APIs for Thread Over Infrastructure.

The functions in this module require `OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE` to be enabled.

## Modules

[otTrelPeer](ot-trel-peer)

## Typedefs

### otTrelPeer

`typedef struct otTrelPeer otTrelPeer`

**Description**:

Represents a TREL peer.

### otTrelPeerIterator

`typedef const void* otTrelPeerIterator`

**Description**:

Represents an iterator for iterating over TREL peer table entries.

### otTrelCounters

`typedef otPlatTrelCounters otTrelCounters`

**Description**:

Represents a group of TREL related counters.

### otTrelStateChangeCallback

`typedef void(* otTrelStateChangeCallback) (void *aContext)`

**Description**:

Callback function pointer to signal state changes to the TREL.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to an arbitrary context (provided when callback is set).|

**Details**:

This callback is invoked whenever the `otTrelGetEnabled()` or `otTrelGetUdpPort()` gets changed.

Any OpenThread API, including `otTrel` APIs, can be safely called from this callback.

## Functions

### otTrelSetEnabled

`void otTrelSetEnabled(otInstance *aInstance, bool aEnable)`

**Description:** Sets the user's preference to enable or disable the TREL operation.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|A boolean to enable/disable the TREL operation.|

The TREL interface's operational state is determined by two factors: the user's preference (set by this function) and the OpenThread stack's internal state. The TREL interface is enabled only when both the user and the OpenThread stack have it enabled. Otherwise, it is disabled.

Upon OpenThread initialization, the user's preference is set to enabled by default. This allows the stack to control the TREL interface state automatically (e.g., enabling it when radio links are enabled and disabling it when radio links are disabled).

If the user explicitly disables the TREL operation by calling this function with `aEnable` as `false`, it will remain disabled until the user explicitly re-enables it by calling this function with `aEnable` as `true`. This ensures the user's 'disable' request persists across other OpenThread stack state changes (which may trigger disabling/enabling of all radio links, including the TREL link).

### otTrelIsEnabled

`bool otTrelIsEnabled(otInstance *aInstance)`

**Description:** Indicates whether the TREL operation is enabled.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

The TREL operation is enabled if and only if it is enabled by both the user (see `otTrelSetEnabled()`) and the OpenThread stack.

### otTrelInitPeerIterator

`void otTrelInitPeerIterator(otInstance *aInstance, otTrelPeerIterator *aIterator)`

**Description:** Initializes a peer table iterator.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otTrelPeerIterator](api-trel#ot-trel-peer-iterator) *|[in]|aIterator|The iterator to initialize.|

### otTrelGetNextPeer

`const otTrelPeer * otTrelGetNextPeer(otInstance *aInstance, otTrelPeerIterator *aIterator)`

**Description:** Iterates over the peer table entries and get the next entry from the table.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otTrelPeerIterator](api-trel#ot-trel-peer-iterator) *|[in]|aIterator|The iterator. MUST be initialized.|

**Returns:**

- A pointer to the next `otTrelPeer` entry or `NULL` if no more entries in the table.

### otTrelGetNumberOfPeers

`uint16_t otTrelGetNumberOfPeers(otInstance *aInstance)`

**Description:** Returns the number of TREL peers.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns:**

- The number of TREL peers.

### otTrelSetFilterEnabled

`void otTrelSetFilterEnabled(otInstance *aInstance, bool aEnable)`

**Description:** Sets the filter mode (enables/disables filtering).

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|bool|[in]|aEnable|TRUE to enable filter mode, FALSE to disable filter mode.|

When filter mode is enabled, any rx and tx traffic through TREL interface is silently dropped. This is mainly intended for use during testing.

Unlike `otTrel{Enable/Disable}()` which fully starts/stops the TREL operation, when filter mode is enabled the TREL interface continues to be enabled.

### otTrelIsFilterEnabled

`bool otTrelIsFilterEnabled(otInstance *aInstance)`

**Description:** Indicates whether or not the filter mode is enabled.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

### otTrelGetCounters

`const otTrelCounters * otTrelGetCounters(otInstance *aInstance)`

**Description:** Gets the TREL counters.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns:**

- A pointer to the TREL counters.

### otTrelResetCounters

`void otTrelResetCounters(otInstance *aInstance)`

**Description:** Resets the TREL counters.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otTrelGetUdpPort

`uint16_t otTrelGetUdpPort(otInstance *aInstance)`

**Description:** Gets the UDP port of the TREL interface.

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns:**

- UDP port of the TREL interface.

### otTrelSetStateChangeCallback

`void otTrelSetStateChangeCallback(otInstance *aInstance, otTrelStateChangeCallback aCallback, void *aContext)`

**Parameters**:

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||
|[otTrelStateChangeCallback](api-trel#ot-trel-state-change-callback)|N/A|aCallback||
|void *|N/A|aContext||
