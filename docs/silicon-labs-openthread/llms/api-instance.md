# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-instance.md

# Instance

This module includes functions that control the OpenThread Instance.

## Typedefs

### otInstance

`typedef struct otInstance otInstance`

**Description:**

Represents the OpenThread instance structure.

### otChangedFlags

`typedef uint32_t otChangedFlags`

**Description:**

Represents a bit-field indicating specific state/configuration that has changed.

**Details:**

See `OT_CHANGED_*` definitions.

### otStateChangedCallback

`typedef void(* otStateChangedCallback) (otChangedFlags aFlags, void *aContext)`

**Description:**

Pointer is called to notify certain configuration or state changes within OpenThread.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aFlags|A bit-field indicating specific state that has changed. See `OT_CHANGED_*` definitions.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

## Functions

### otInstanceInit

`otInstance * otInstanceInit(void *aInstanceBuffer, size_t *aInstanceBufferSize)`

**Description:** Initializes the OpenThread library.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|void *|[in]|aInstanceBuffer|The buffer for OpenThread to use for allocating the otInstance structure.|
|size_t *|[inout]|aInstanceBufferSize|On input, the size of aInstanceBuffer. On output, if not enough space for otInstance, the number of bytes required for otInstance.|

Initializes OpenThread and prepares it for subsequent OpenThread API calls. This function must be called before any other calls to OpenThread.

Is available and can only be used when support for multiple OpenThread instances is enabled.

#### Returns

- A pointer to the new OpenThread instance.

##### See Also

- [otInstanceFinalize](api-instance#ot-instance-finalize)

### otInstanceInitSingle

`otInstance * otInstanceInitSingle(void)`

**Description:** Initializes the static single instance of the OpenThread library.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|void|N/A|undefined||

Initializes OpenThread and prepares it for subsequent OpenThread API calls. This function must be called before any other calls to OpenThread.

Is available and can only be used when support for multiple OpenThread instances is disabled.

#### Returns (otInstanceInitSingle)

- A pointer to the single OpenThread instance.

### otInstanceGetSingle

`otInstance * otInstanceGetSingle(void)`

**Description:** Gets the pointer to the single OpenThread instance when multiple instances are not in use.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|void|N/A|undefined||

Is available and can only be used when support for multiple OpenThread instances is disabled.

#### Returns (otInstanceGetSingle)

- A pointer to the single OpenThread instance.

### otInstanceInitMultiple

`otInstance * otInstanceInitMultiple(uint8_t aIdx)`

**Description:** Initializes the OpenThread instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|uint8_t|[in]|aIdx|The index of the OpenThread instance to initialize.|

This function initializes OpenThread and prepares it for subsequent OpenThread API calls. This function must be called before any other calls to OpenThread. This method utilizes static buffer to initialize the OpenThread instance.

This function is available and can only be used when support for multiple OpenThread static instances is enabled (`OPENTHREAD_CONFIG_MULTIPLE_STATIC_INSTANCE_ENABLE`)

#### Returns (otInstanceInitMultiple)

- A pointer to the new OpenThread instance.

### otInstanceGetInstance

`otInstance * otInstanceGetInstance(uint8_t aIdx)`

**Description:** Gets the pointer to an OpenThread instance with the provided index when multiple instances are in use.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|uint8_t|[in]|aIdx|The index of the OpenThread instance.|

This function is available when both `OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE` and `OPENTHREAD_CONFIG_MULTIPLE_STATIC_INSTANCE_ENABLE` are enabled.

#### Returns (otInstanceGetInstance)

- A pointer to the corresponding OpenThread instance, or `NULL` if `aIdx` is out of bounds.

### otInstanceGetIndex

`uint8_t otInstanceGetIndex(otInstance *aInstance)`

**Description:** Gets the index of the OpenThread instance when multiple instance is in use.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The reference of the OpenThread instance to get index.|

This function is available when both `OPENTHREAD_CONFIG_MULTIPLE_INSTANCE_ENABLE` and `OPENTHREAD_CONFIG_MULTIPLE_STATIC_INSTANCE_ENABLE` are enabled.

#### Returns (otInstanceGetIndex)

- The index of the OpenThread instance.

### otInstanceGetId

`uint32_t otInstanceGetId(otInstance *aInstance)`

**Description:** Gets the instance identifier.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

The instance identifier is set to a random value when the instance is constructed, and then its value will not change after initialization.

#### Returns (otInstanceGetId)

- The instance identifier.

### otInstanceIsInitialized

`bool otInstanceIsInitialized(otInstance *aInstance)`

**Description:** Indicates whether or not the instance is valid/initialized.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

The instance is considered valid if it is acquired and initialized using either `otInstanceInitSingle()` (in single instance case) or `otInstanceInit()` (in multi instance case). A subsequent call to `otInstanceFinalize()` causes the instance to be considered as uninitialized.

#### Returns (otInstanceIsInitialized)

- TRUE if the given instance is valid/initialized, FALSE otherwise.

### otInstanceFinalize

`void otInstanceFinalize(otInstance *aInstance)`

**Description:** Disables the OpenThread library.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Call this function when OpenThread is no longer in use.

### otInstanceGetUptime

`uint64_t otInstanceGetUptime(otInstance *aInstance)`

**Description:** Returns the current instance uptime (in msec).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_UPTIME_ENABLE` to be enabled.

The uptime is given as number of milliseconds since OpenThread instance was initialized.

#### Returns (otInstanceGetUptime)

- The uptime (number of milliseconds).

### otInstanceGetUptimeAsString

`void otInstanceGetUptimeAsString(otInstance *aInstance, char *aBuffer, uint16_t aSize)`

**Description:** Returns the current instance uptime as a human-readable string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|char *|[out]|aBuffer|A pointer to a char array to output the string.|
|uint16_t|[in]|aSize|The size of `aBuffer` (in bytes). Recommended to use `OT_UPTIME_STRING_SIZE`.|

Requires `OPENTHREAD_CONFIG_UPTIME_ENABLE` to be enabled.

The string follows the format "<hh>:<mm>:<ss>.<mmmm>" for hours, minutes, seconds and millisecond (if uptime is shorter than one day) or "<dd>d.<hh>:<mm>:<ss>.<mmmm>" (if longer than a day).

If the resulting string does not fit in `aBuffer` (within its `aSize` characters), the string will be truncated but the outputted string is always null-terminated.

### otSetStateChangedCallback

`otError otSetStateChangedCallback(otInstance *aInstance, otStateChangedCallback aCallback, void *aContext)`

**Description:** Registers a callback to indicate when certain configuration or state changes within OpenThread.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otStateChangedCallback](api-instance#ot-state-changed-callback)|[in]|aCallback|A pointer to a function that is called with certain configuration or state changes.|
|void *|[in]|aContext|A pointer to application-specific context.|

### otRemoveStateChangeCallback

`void otRemoveStateChangeCallback(otInstance *aInstance, otStateChangedCallback aCallback, void *aContext)`

**Description:** Removes a callback to indicate when certain configuration or state changes within OpenThread.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otStateChangedCallback](api-instance#ot-state-changed-callback)|[in]|aCallback|A pointer to a function that is called with certain configuration or state changes.|
|void *|[in]|aContext|A pointer to application-specific context.|

### otInstanceReset

`void otInstanceReset(otInstance *aInstance)`

**Description:** Triggers a platform reset.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

The reset process ensures that all the OpenThread state/info (stored in volatile memory) is erased. Note that the `otPlatformReset` does not erase any persistent state/info saved in non-volatile memory.

### otInstanceResetToBootloader

`otError otInstanceResetToBootloader(otInstance *aInstance)`

**Description:** Triggers a platform reset to bootloader mode, if supported.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_PLATFORM_BOOTLOADER_MODE_ENABLE`.

### otInstanceFactoryReset

`void otInstanceFactoryReset(otInstance *aInstance)`

**Description:** Deletes all the settings stored on non-volatile memory, and then triggers a platform reset.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otInstanceResetRadioStack

`void otInstanceResetRadioStack(otInstance *aInstance)`

**Description:** Resets the internal states of the OpenThread radio stack.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Callbacks and configurations are preserved.

This API is only available under radio builds (`OPENTHREAD_RADIO = 1`).

### otInstanceErasePersistentInfo

`otError otInstanceErasePersistentInfo(otInstance *aInstance)`

**Description:** Erases all the OpenThread persistent info (network settings) stored on non-volatile memory.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Erase is successful only if the device is in `disabled` state/role.

### otGetVersionString

`const char * otGetVersionString(void)`

**Description:** Gets the OpenThread version string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|void|N/A|undefined||

#### Returns (otGetVersionString)

- A pointer to the OpenThread version.

### otGetRadioVersionString

`const char * otGetRadioVersionString(otInstance *aInstance)`

**Description:** Gets the OpenThread radio version string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### Returns (otGetRadioVersionString)

- A pointer to the OpenThread radio version.

## Macros

`#define OT_UPTIME_STRING_SIZE 24`

**Description**: Recommended size for string representation of uptime.

`#define OT_CHANGED_IP6_ADDRESS_ADDED (1U << 0)`

**Description**: IPv6 address was added.

`#define OT_CHANGED_IP6_ADDRESS_REMOVED (1U << 1)`

**Description**: IPv6 address was removed.

`#define OT_CHANGED_THREAD_ROLE (1U << 2)`

**Description**: Role (disabled, detached, child, router, leader) changed.

`#define OT_CHANGED_THREAD_LL_ADDR (1U << 3)`

**Description**: The link-local address changed.

`#define OT_CHANGED_THREAD_ML_ADDR (1U << 4)`

**Description**: The mesh-local address changed.

`#define OT_CHANGED_THREAD_RLOC_ADDED (1U << 5)`

**Description**: RLOC was added.

`#define OT_CHANGED_THREAD_RLOC_REMOVED (1U << 6)`

**Description**: RLOC was removed.

`#define OT_CHANGED_THREAD_PARTITION_ID (1U << 7)`

**Description**: Partition ID changed.

`#define OT_CHANGED_THREAD_KEY_SEQUENCE_COUNTER (1U << 8)`

**Description**: Thread Key Sequence changed.

`#define OT_CHANGED_THREAD_NETDATA (1U << 9)`

**Description**: Thread Network Data changed.

`#define OT_CHANGED_THREAD_CHILD_ADDED (1U << 10)`

**Description**: Child was added.

`#define OT_CHANGED_THREAD_CHILD_REMOVED (1U << 11)`

**Description**: Child was removed.

`#define OT_CHANGED_IP6_MULTICAST_SUBSCRIBED (1U << 12)`

**Description**: Subscribed to a IPv6 multicast address.

`#define OT_CHANGED_IP6_MULTICAST_UNSUBSCRIBED (1U << 13)`

**Description**: Unsubscribed from a IPv6 multicast address.

`#define OT_CHANGED_THREAD_CHANNEL (1U << 14)`

**Description**: Thread network channel changed.

`#define OT_CHANGED_THREAD_PANID (1U << 15)`

**Description**: Thread network PAN Id changed.

`#define OT_CHANGED_THREAD_NETWORK_NAME (1U << 16)`

**Description**: Thread network name changed.

`#define OT_CHANGED_THREAD_EXT_PANID (1U << 17)`

**Description**: Thread network extended PAN ID changed.

`#define OT_CHANGED_NETWORK_KEY (1U << 18)`

**Description**: Network key changed.

`#define OT_CHANGED_PSKC (1U << 19)`

**Description**: PSKc changed.

`#define OT_CHANGED_SECURITY_POLICY (1U << 20)`

**Description**: Security Policy changed.

`#define OT_CHANGED_CHANNEL_MANAGER_NEW_CHANNEL (1U << 21)`

**Description**: Channel Manager new pending Thread channel changed.

`#define OT_CHANGED_SUPPORTED_CHANNEL_MASK (1U << 22)`

**Description**: Supported channel mask changed.

`#define OT_CHANGED_COMMISSIONER_STATE (1U << 23)`

**Description**: Commissioner state changed.

`#define OT_CHANGED_THREAD_NETIF_STATE (1U << 24)`

**Description**: Thread network interface state changed.

`#define OT_CHANGED_THREAD_BACKBONE_ROUTER_STATE (1U << 25)`

**Description**: Backbone Router state changed.

`#define OT_CHANGED_THREAD_BACKBONE_ROUTER_LOCAL (1U << 26)`

**Description**: Local Backbone Router configuration changed.

`#define OT_CHANGED_JOINER_STATE (1U << 27)`

**Description**: Joiner state changed.

`#define OT_CHANGED_ACTIVE_DATASET (1U << 28)`

**Description**: Active Operational Dataset changed.

`#define OT_CHANGED_PENDING_DATASET (1U << 29)`

**Description**: Pending Operational Dataset changed.

`#define OT_CHANGED_NAT64_TRANSLATOR_STATE (1U << 30)`

**Description**: The state of NAT64 translator changed.

`#define OT_CHANGED_PARENT_LINK_QUALITY (1U << 31)`

**Description**: Parent link quality changed.
