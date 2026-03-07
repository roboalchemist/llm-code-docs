# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-border-agent.md

# Border Agent

This module includes functions for the Thread Border Agent role. 

## Modules

[otBorderAgentId](ot-border-agent-id)

[otBorderAgentCounters](ot-border-agent-counters)

[otBorderAgentSessionInfo](ot-border-agent-session-info)

[otBorderAgentSessionIterator](ot-border-agent-session-iterator)

[otBorderAgentMeshCoPServiceTxtData](ot-border-agent-mesh-co-p-service-txt-data)

## Enumerations

### otBorderAgentEphemeralKeyState

```
enum otBorderAgentEphemeralKeyState {
    OT_BORDER_AGENT_STATE_DISABLED = 0
    OT_BORDER_AGENT_STATE_STOPPED = 1
    OT_BORDER_AGENT_STATE_STARTED = 2
    OT_BORDER_AGENT_STATE_CONNECTED = 3
    OT_BORDER_AGENT_STATE_ACCEPTED = 4
}
```

**Description:**

Represents Border Agent's Ephemeral Key Manager state.

**Enumerator:**

|   |   |
|---|---|
|OT_BORDER_AGENT_STATE_DISABLED|Ephemeral Key Manager is disabled.|
|OT_BORDER_AGENT_STATE_STOPPED|Enabled, but no ephemeral key is in use (not set or started).|
|OT_BORDER_AGENT_STATE_STARTED|Ephemeral key is set. Listening to accept secure connections.|
|OT_BORDER_AGENT_STATE_CONNECTED|Session is established with an external commissioner candidate.|
|OT_BORDER_AGENT_STATE_ACCEPTED|Session is established and candidate is accepted as full commissioner.|

## Typedefs

### otBorderAgentId

`typedef struct otBorderAgentId otBorderAgentId`

**Description:**

Represents a Border Agent Identifier.

### otBorderAgentCounters

`typedef struct otBorderAgentCounters otBorderAgentCounters`

**Description:**

Defines Border Agent counters.

**Details:**

The `mEpskc` related counters require `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`.

### otBorderAgentSessionInfo

`typedef struct otBorderAgentSessionInfo otBorderAgentSessionInfo`

**Description:**

Represents information about a Border Agent session.

**Details:**

This structure is populated by `otBorderAgentGetNextSessionInfo()` during iteration over the list of sessions using an `otBorderAgentSessionIterator`.

To ensure consistent `mLifetime` calculations, the iterator's initialization time is stored within the iterator, and each session's `mLifetime` is calculated relative to this time.

### otBorderAgentSessionIterator

`typedef struct otBorderAgentSessionIterator otBorderAgentSessionIterator`

**Description:**

Represents an iterator for Border Agent sessions.

**Details:**

The caller MUST NOT access or update the fields in this struct. It is intended for OpenThread internal use only.

### otBorderAgentMeshCoPServiceTxtData

`typedef struct otBorderAgentMeshCoPServiceTxtData otBorderAgentMeshCoPServiceTxtData`

**Description:**

Represents the Border Agent MeshCoP Service TXT data.

### otBorderAgentMeshCoPServiceChangedCallback

`typedef void(* otBorderAgentMeshCoPServiceChangedCallback) (void *aContext)`

**Description:**

This callback informs the application of the changes in the state of the MeshCoP service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

In specific, the 'state' includes the MeshCoP TXT data originated from the Thread network and whether the Border Agent is Active (which can be obtained by `otBorderAgentIsActive`).

### otBorderAgentEphemeralKeyState

`typedef enum otBorderAgentEphemeralKeyState otBorderAgentEphemeralKeyState`

**Description:**

Represents Border Agent's Ephemeral Key Manager state.

### otBorderAgentEphemeralKeyCallback

`typedef void(* otBorderAgentEphemeralKeyCallback) (void *aContext)`

**Description:**

Callback function pointer to signal state changes to the Border Agent's Ephemeral Key Manager.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to an arbitrary context (provided when callback is set).|

**Details:**

This callback is invoked whenever the `otBorderAgentEphemeralKeyGetState()` gets changed.

Any OpenThread API, including `otBorderAgent` APIs, can be safely called from this callback.

## Functions

### otBorderAgentSetEnabled

`void otBorderAgentSetEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Enables or disables the Border Agent service on the device.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|bool|[in]|aEnabled|A boolean to indicate whether to to enable (TRUE), or disable (FALSE).|

By default, the Border Agent service is enabled when the `OPENTHREAD_CONFIG_BORDER_AGENT_ENABLE` feature is used. This function allows higher-layer code to explicitly control its state. This can be useful in scenarios such as:

- The higher-layer code wishes to delay the start of the Border Agent service (and its mDNS advertisement of the `_meshcop._udp` service on the infrastructure link). This allows time to prepare or determine vendor-specific TXT data entries for inclusion.
- Unit tests or test scripts might disable the Border Agent service to prevent it from interfering with specific test steps. For example, tests validating mDNS or DNS-SD functionality may disable the Border Agent to prevent its registration of the MeshCoP service.

### otBorderAgentIsEnabled

`bool otBorderAgentIsEnabled(otInstance *aInstance)`

**Description:** Indicates whether or not the Border Agent service is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

### otBorderAgentIsActive

`bool otBorderAgentIsActive(otInstance *aInstance)`

**Description:** Indicates whether or not the Border Agent service is enabled and also active.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

While the Border Agent is active, external commissioner candidates can try to connect to and establish secure DTLS sessions with the Border Agent using PSKc. A connected commissioner can then petition to become a full commissioner.

If `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE` is enabled, independent and separate DTLS transport and sessions are used for the ephemeral key. Therefore, the ephemeral key and Border Agent service can be enabled and used in parallel.

### otBorderAgentGetUdpPort

`uint16_t otBorderAgentGetUdpPort(otInstance *aInstance)`

**Description:** Gets the UDP port of the Thread Border Agent service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- UDP port of the Border Agent.

### otBorderAgentSetMeshCoPServiceChangedCallback

`void otBorderAgentSetMeshCoPServiceChangedCallback(otInstance *aInstance, otBorderAgentMeshCoPServiceChangedCallback aCallback, void *aContext)`

**Description:** Sets the callback function used by the Border Agent to notify of any changes to the state of the MeshCoP service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBorderAgentMeshCoPServiceChangedCallback](api-border-agent#ot-border-agent-mesh-co-p-service-changed-callback)|[in]|aCallback|The callback to be invoked when there are any changes of the MeshCoP service.|
|void *|[in]|aContext|A pointer to application-specific context.|

The callback is invoked when the 'Is Active' state of the Border Agent or the MeshCoP service TXT data values change. For example, it is invoked when the network name or the extended PAN ID changes and passes the updated encoded TXT data to the application layer.

This callback is invoked once right after this API is called to provide initial states of the MeshCoP service.

### otBorderAgentGetMeshCoPServiceTxtData

`otError otBorderAgentGetMeshCoPServiceTxtData(otInstance *aInstance, otBorderAgentMeshCoPServiceTxtData *aTxtData)`

**Description:** Gets the MeshCoP service TXT data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBorderAgentMeshCoPServiceTxtData](ot-border-agent-mesh-co-p-service-txt-data) *|[out]|aTxtData|A pointer to a MeshCoP Service TXT data struct to get the data.|

The generated TXT data includes a subset of keys (depending on the device's current state and whether features are enabled) as specified in the documentation of the `OT_BORDER_AGENT_MESHCOP_SERVICE_TXT_DATA_MAX_LENGTH` constant. Notably, if `OPENTHREAD_CONFIG_BORDER_AGENT_MESHCOP_SERVICE_ENABLE` is enabled and `otBorderAgentSetVendorTxtData()` was used to set extra vendor-specific TXT data bytes, those vendor-specified TXT data bytes are NOT included in the TXT data returned by this function.

### otBorderAgentSetMeshCoPServiceBaseName

`otError otBorderAgentSetMeshCoPServiceBaseName(otInstance *aInstance, const char *aBaseName)`

**Description:** Sets the base name to construct the service instance name used when advertising the mDNS `_meshcop._udp` service by the Border Agent.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const char *|[in]|aBaseName|The base name to use (MUST not be NULL).|

Requires the `OPENTHREAD_CONFIG_BORDER_AGENT_MESHCOP_SERVICE_ENABLE` feature.

The name can also be configured using the `OPENTHREAD_CONFIG_BORDER_AGENT_MESHCOP_SERVICE_BASE_NAME` configuration option (which is the recommended way to specify this name). This API is provided for projects where the name needs to be set after device initialization and at run-time.

Per the Thread specification, the service instance should be a user-friendly name identifying the device model or product. A recommended format is "VendorName ProductName".

To construct the full name and ensure name uniqueness, the OpenThread Border Agent module will append the Extended Address of the device (as 16-character hex digits) to the given base name.

Note that the same name will be used for the ephemeral key service `_meshcop-e._udp` when the ephemeral key feature is enabled and used.

### otBorderAgentSetVendorTxtData

`void otBorderAgentSetVendorTxtData(otInstance *aInstance, const uint8_t *aVendorData, uint16_t aVendorDataLength)`

**Description:** Sets the vendor extra TXT data to be included when the Border Agent advertises the mDNS `_meshcop._udp` service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const uint8_t *|[in]|aVendorData|A pointer to the buffer containing the vendor TXT data.|
|uint16_t|[in]|aVendorDataLength|The length of `aVendorData` in bytes.|

Requires the `OPENTHREAD_CONFIG_BORDER_AGENT_MESHCOP_SERVICE_ENABLE` feature.

The provided `aVendorData` bytes are appended as they appear in the buffer to the end of the TXT data generated by the Border Agent itself, and are then included in the advertised mDNS `_meshcop._udp` service.

This function itself does not perform any validation of the format of the provided `aVendorData`. Therefore, the caller MUST ensure it is formatted properly. Per the Thread specification, vendor-specific Key-Value TXT data pairs use TXT keys starting with 'v'. For example, `vn` for vendor name and generally `v*`.

The OpenThread stack will create and retain its own copy of the bytes in `aVendorData`. So, the buffer passed to this function does not need to persist beyond the scope of the call.

The vendor TXT data can be set at any time while the Border Agent is in any state. If there is a change from the previously set value, it will trigger an update of the registered mDNS service to advertise the new TXT data.

### otBorderAgentGetId

`otError otBorderAgentGetId(otInstance *aInstance, otBorderAgentId *aId)`

**Description:** Gets the randomly generated Border Agent ID.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBorderAgentId](ot-border-agent-id) *|[out]|aId|A pointer to buffer to receive the ID.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_ID_ENABLE`.

The ID is saved in persistent storage and survives reboots. The typical use case of the ID is to be published in the MeshCoP mDNS service as the `id` TXT value for the client to identify this Border Router/Agent device.

**See Also**

- [otBorderAgentSetId](api-border-agent#ot-border-agent-set-id)

### otBorderAgentSetId

`otError otBorderAgentSetId(otInstance *aInstance, const otBorderAgentId *aId)`

**Description:** Sets the Border Agent ID.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otBorderAgentId](ot-border-agent-id) *|[out]|aId|A pointer to the Border Agent ID.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_ID_ENABLE`.

The Border Agent ID will be saved in persistent storage and survive reboots. It's required to set the ID only once after factory reset. If the ID has never been set by calling this function, a random ID will be generated and returned when `otBorderAgentGetId` is called.

**See Also**

- [otBorderAgentGetId](api-border-agent#ot-border-agent-get-id)

### otBorderAgentInitSessionIterator

`void otBorderAgentInitSessionIterator(otInstance *aInstance, otBorderAgentSessionIterator *aIterator)`

**Description:** Initializes a session iterator.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBorderAgentSessionIterator](ot-border-agent-session-iterator) *|[in]|aIterator|The iterator to initialize.|

An iterator MUST be initialized before being used in `otBorderAgentGetNextSessionInfo()`. A previously initialized iterator can be re-initialized to start from the beginning of the session list.

### otBorderAgentGetNextSessionInfo

`otError otBorderAgentGetNextSessionInfo(otBorderAgentSessionIterator *aIterator, otBorderAgentSessionInfo *aSessionInfo)`

**Description:** Retrieves the next Border Agent session information.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otBorderAgentSessionIterator](ot-border-agent-session-iterator) *|[in]|aIterator|The iterator to use.|
|[otBorderAgentSessionInfo](ot-border-agent-session-info) *|[out]|aSessionInfo|A pointer to an `otBorderAgentSessionInfo` to populate.|

### otBorderAgentGetCounters

`const otBorderAgentCounters * otBorderAgentGetCounters(otInstance *aInstance)`

**Description:** Gets the counters of the Thread Border Agent.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- A pointer to the Border Agent counters.

### otBorderAgentEphemeralKeyGetState

`otBorderAgentEphemeralKeyState otBorderAgentEphemeralKeyGetState(otInstance *aInstance)`

**Description:** Gets the state of Border Agent's Ephemeral Key Manager.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`.

**Returns**

- The current state of Ephemeral Key Manager.

### otBorderAgentEphemeralKeySetEnabled

`void otBorderAgentEphemeralKeySetEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Enables/disables the Border Agent's Ephemeral Key Manager.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|bool|[in]|aEnabled|Whether to enable or disable the Ephemeral Key Manager.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`.

If this function is called to disable, while an an ephemeral key is in use, the ephemeral key use will be stopped (as if `otBorderAgentEphemeralKeyStop()` is called).

### otBorderAgentEphemeralKeyStart

`otError otBorderAgentEphemeralKeyStart(otInstance *aInstance, const char *aKeyString, uint32_t aTimeout, uint16_t aUdpPort)`

**Description:** Starts using an ephemeral key for a given timeout duration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const char *|[in]|aKeyString|The ephemeral key.|
|uint32_t|[in]|aTimeout|The timeout duration, in milliseconds, to use the ephemeral key. If zero, the default `OT_BORDER_AGENT_DEFAULT_EPHEMERAL_KEY_TIMEOUT` value is used. If the timeout value is larger than `OT_BORDER_AGENT_MAX_EPHEMERAL_KEY_TIMEOUT`, the maximum value is used instead.|
|uint16_t|[in]|aUdpPort|The UDP port to use with the ephemeral key. If the UDP port is zero, an ephemeral port will be used. `otBorderAgentEphemeralKeyGetUdpPort()` returns the current UDP port being used.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`.

An ephemeral key can only be set when `otBorderAgentEphemeralKeyGetState()` is `OT_BORDER_AGENT_STATE_STOPPED`, i.e., enabled but not yet started. Otherwise, `OT_ERROR_INVALID_STATE` is returned. This means that setting the ephemeral key again while a previously set key is still in use will fail. Callers can stop the previous key by calling `otBorderAgentEphemeralKeyStop()` before starting with a new key.

The Ephemeral Key Manager and the Border Agent service (which uses PSKc) can be enabled and used in parallel, as they use independent and separate DTLS transport and sessions.

The given `aKeyString` is used directly as the ephemeral PSK (excluding the trailing null `\0` character). Its length must be between `OT_BORDER_AGENT_MIN_EPHEMERAL_KEY_LENGTH` and `OT_BORDER_AGENT_MAX_EPHEMERAL_KEY_LENGTH`, inclusive. Otherwise `OT_ERROR_INVALID_ARGS` is returned.

When successfully set, the ephemeral key can be used only once by an external commissioner candidate to establish a secure session. After the commissioner candidate disconnects, the use of the ephemeral key is stopped. If the timeout expires, the use of the ephemeral key is stopped, and any connected session using the key is immediately disconnected.

The Ephemeral Key Manager limits the number of failed DTLS connections to 10 attempts. After the 10th failed attempt, the use of the ephemeral key is automatically stopped (even if the timeout has not yet expired).

### otBorderAgentEphemeralKeyStop

`void otBorderAgentEphemeralKeyStop(otInstance *aInstance)`

**Description:** Stops the ephemeral key use and disconnects any session using it.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`.

If there is no ephemeral key in use, calling this function has no effect.

### otBorderAgentEphemeralKeyGetUdpPort

`uint16_t otBorderAgentEphemeralKeyGetUdpPort(otInstance *aInstance)`

**Description:** Gets the UDP port used by Border Agent's Ephemeral Key Manager.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`.

The port is applicable if an ephemeral key is in use, i.e., the state is not `OT_BORDER_AGENT_STATE_DISABLED` or `OT_BORDER_AGENT_STATE_STOPPED`.

**Returns**

- The UDP port being used by Border Agent's Ephemeral Key Manager (when active).

### otBorderAgentEphemeralKeySetCallback

`void otBorderAgentEphemeralKeySetCallback(otInstance *aInstance, otBorderAgentEphemeralKeyCallback aCallback, void *aContext)`

**Description:** Sets the callback function to notify state changes of Border Agent's Ephemeral Key Manager.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otBorderAgentEphemeralKeyCallback](api-border-agent#ot-border-agent-ephemeral-key-callback)|[in]|aCallback|The callback function pointer.|
|void *|[in]|aContext|The arbitrary context to use with callback.|

Requires `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`.

A subsequent call to this function will replace any previously set callback.

### otBorderAgentEphemeralKeyStateToString

`const char * otBorderAgentEphemeralKeyStateToString(otBorderAgentEphemeralKeyState aState)`

**Description:** Converts a given `otBorderAgentEphemeralKeyState` to a human-readable string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otBorderAgentEphemeralKeyState](api-border-agent#ot-border-agent-ephemeral-key-state)|[in]|aState|The state to convert.|

**Returns**

- Human-readable string corresponding to `aState`.

## Macros

`#define OT_BORDER_AGENT_ID_LENGTH (16)`

**Description**: The length of Border Agent/Router ID in bytes.

`#define OT_BORDER_AGENT_MESHCOP_SERVICE_TXT_DATA_MAX_LENGTH 256`

**Description**: Maximum length of the OT core generated MeshCoP Service TXT data.

`#define OT_BORDER_AGENT_MESHCOP_SERVICE_BASE_NAME_MAX_LENGTH (OT_DNS_MAX_LABEL_SIZE - 17)`

**Description**: Maximum string length of base name used in `otBorderAgentSetMeshCoPServiceBaseName()`.

`#define OT_BORDER_AGENT_MIN_EPHEMERAL_KEY_LENGTH (6)`

**Description**: Minimum length of the ephemeral key string.

`#define OT_BORDER_AGENT_MAX_EPHEMERAL_KEY_LENGTH (32)`

**Description**: Maximum length of the ephemeral key string.

`#define OT_BORDER_AGENT_DEFAULT_EPHEMERAL_KEY_TIMEOUT (2 * 60 * 1000u)`

**Description**: Default ephemeral key timeout interval in milliseconds.

`#define OT_BORDER_AGENT_MAX_EPHEMERAL_KEY_TIMEOUT (10 * 60 * 1000u)`

**Description**: Maximum ephemeral key timeout interval in milliseconds.