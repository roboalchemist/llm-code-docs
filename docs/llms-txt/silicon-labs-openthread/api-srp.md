# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-srp.md

# SRP

This module includes functions that control SRP client behavior. 

This module includes functions of the Service Registration Protocol.

This module includes functions for SRP client buffers and service pool.

Functions in this module are only available when feature OPENTHREAD_CONFIG_SRP_CLIENT_BUFFERS_ENABLE is enabled. 

## Modules

[otSrpClientHostInfo](ot-srp-client-host-info)

[otSrpClientService](ot-srp-client-service)

[otSrpClientBuffersServiceEntry](ot-srp-client-buffers-service-entry)

[otSrpServerTtlConfig](ot-srp-server-ttl-config)

[otSrpServerLeaseConfig](ot-srp-server-lease-config)

[otSrpServerLeaseInfo](ot-srp-server-lease-info)

[otSrpServerResponseCounters](ot-srp-server-response-counters)

## Enumerations

### otSrpClientItemState

```
enum otSrpClientItemState {
    OT_SRP_CLIENT_ITEM_STATE_TO_ADD
    OT_SRP_CLIENT_ITEM_STATE_ADDING
    OT_SRP_CLIENT_ITEM_STATE_TO_REFRESH
    OT_SRP_CLIENT_ITEM_STATE_REFRESHING
    OT_SRP_CLIENT_ITEM_STATE_TO_REMOVE
    OT_SRP_CLIENT_ITEM_STATE_REMOVING
    OT_SRP_CLIENT_ITEM_STATE_REGISTERED
    OT_SRP_CLIENT_ITEM_STATE_REMOVED
}
```

**Description:**

Specifies an SRP client item (service or host info) state.

**Enumerator:**

|   |   |
|---|---|
|OT_SRP_CLIENT_ITEM_STATE_TO_ADD|Item to be added/registered.|
|OT_SRP_CLIENT_ITEM_STATE_ADDING|Item is being added/registered.|
|OT_SRP_CLIENT_ITEM_STATE_TO_REFRESH|Item to be refreshed (re-register to renew lease).|
|OT_SRP_CLIENT_ITEM_STATE_REFRESHING|Item is being refreshed.|
|OT_SRP_CLIENT_ITEM_STATE_TO_REMOVE|Item to be removed.|
|OT_SRP_CLIENT_ITEM_STATE_REMOVING|Item is being removed.|
|OT_SRP_CLIENT_ITEM_STATE_REGISTERED|Item is registered with server.|
|OT_SRP_CLIENT_ITEM_STATE_REMOVED|Item is removed.|

### otSrpServerState

```
enum otSrpServerState {
    OT_SRP_SERVER_STATE_DISABLED = 0
    OT_SRP_SERVER_STATE_RUNNING = 1
    OT_SRP_SERVER_STATE_STOPPED = 2
}
```

**Description:**

Represents the state of the SRP server.

**Enumerator:**

|   |   |
|---|---|
|OT_SRP_SERVER_STATE_DISABLED|The SRP server is disabled.|
|OT_SRP_SERVER_STATE_RUNNING|The SRP server is enabled and running.|
|OT_SRP_SERVER_STATE_STOPPED|The SRP server is enabled but stopped.|

### otSrpServerAddressMode

```
enum otSrpServerAddressMode {
    OT_SRP_SERVER_ADDRESS_MODE_UNICAST = 0
    OT_SRP_SERVER_ADDRESS_MODE_ANYCAST = 1
    OT_SRP_SERVER_ADDRESS_MODE_UNICAST_FORCE_ADD = 2
}
```

**Description:**

Represents the address mode used by the SRP server.

**Details:**

Address mode specifies how the address and port number are determined by the SRP server and how this info is published in the Thread Network Data.

**Warnings**

- Using the `OT_SRP_SERVER_ADDRESS_MODE_UNICAST_FORCE_ADD` option will make the implementation non-compliant with the Thread specification. This option is intended for testing and specific use-cases. When selected, the SRP server, upon being enabled, will bypass the Network Data publisher and always add the "SRP/DNS unicast" entry directly to the Network Data, regardless of how many other similar entries are present.

**Enumerator:**

|   |   |
|---|---|
|OT_SRP_SERVER_ADDRESS_MODE_UNICAST|Unicast address mode. Use Network Data publisher.|
|OT_SRP_SERVER_ADDRESS_MODE_ANYCAST|Anycast address mode. Use Network Data publisher.|
|OT_SRP_SERVER_ADDRESS_MODE_UNICAST_FORCE_ADD|Unicast address mode. Immediately force add to Network Data.|

## Typedefs

### otSrpClientHostInfo

`typedef struct otSrpClientHostInfo otSrpClientHostInfo`

**Description:**

Represents an SRP client host info.

### otSrpClientService

`typedef struct otSrpClientService otSrpClientService`

**Description:**

Represents an SRP client service.

**Details:**

The values in this structure, including the string buffers for the names and the TXT record entries, MUST persist and stay constant after an instance of this structure is passed to OpenThread from `otSrpClientAddService()` or `otSrpClientRemoveService()`.

The `mState`, `mData`, `mNext` fields are used/managed by OT core only. Their value is ignored when an instance of `otSrpClientService` is passed in `otSrpClientAddService()` or `otSrpClientRemoveService()` or other functions. The caller does not need to set these fields.

The `mLease` and `mKeyLease` fields specify the desired lease and key lease intervals for this service. Zero value indicates that the interval is unspecified and then the default lease or key lease intervals from `otSrpClientGetLeaseInterval()` and `otSrpClientGetKeyLeaseInterval()` are used for this service. If the key lease interval (whether set explicitly or determined from the default) is shorter than the lease interval for a service, SRP client will re-use the lease interval value for key lease interval as well. For example, if in service `mLease` is explicitly set to 2 days and `mKeyLease` is set to zero and default key lease is set to 1 day, then when registering this service, the requested key lease for this service is also set to 2 days.

### otSrpClientCallback

`typedef void(* otSrpClientCallback) (otError aError, const otSrpClientHostInfo *aHostInfo, const otSrpClientService *aServices, const otSrpClientService *aRemovedServices, void *aContext)`

**Description:**

Pointer type defines the callback used by SRP client to notify user of changes/events/errors.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aError|The error (see above).|
||[in]|aHostInfo|A pointer to host info.|
||[in]|aServices|The head of linked-list containing all services (excluding the ones removed). NULL if the list is empty.|
||[in]|aRemovedServices|The head of linked-list containing all removed services. NULL if the list is empty.|
||[in]|aContext|A pointer to an arbitrary context (provided when callback was registered).|

**Details:**

This callback is invoked on a successful registration of an update (i.e., add/remove of host-info and/or some service(s)) with the SRP server, or if there is a failure or error (e.g., server rejects a update request or client times out waiting for response, etc).

In case of a successful reregistration of an update, `aError` parameter would be `OT_ERROR_NONE` and the host info and the full list of services is provided as input parameters to the callback. Note that host info and services each track its own state in the corresponding `mState` member variable of the related data structure (the state indicating whether the host-info/service is registered or removed or still being added/removed, etc).

The list of removed services is passed as its own linked-list `aRemovedServices` in the callback. Note that when the callback is invoked, the SRP client (OpenThread implementation) is done with the removed service instances listed in `aRemovedServices` and no longer tracks/stores them (i.e., if from the callback we call `otSrpClientGetServices()` the removed services will not be present in the returned list). Providing a separate list of removed services in the callback helps indicate to user which items are now removed and allow user to re-claim/reuse the instances.

If the server rejects an SRP update request, the DNS response code (RFC 2136) is mapped to the following errors:

- (0) NOERROR Success (no error condition) -> OT_ERROR_NONE
- (1) FORMERR Server unable to interpret due to format error -> OT_ERROR_PARSE
- (2) SERVFAIL Server encountered an internal failure -> OT_ERROR_FAILED
- (3) NXDOMAIN Name that ought to exist, does not exist -> OT_ERROR_NOT_FOUND
- (4) NOTIMP Server does not support the query type (OpCode) -> OT_ERROR_NOT_IMPLEMENTED
- (5) REFUSED Server refused for policy/security reasons -> OT_ERROR_SECURITY
- (6) YXDOMAIN Some name that ought not to exist, does exist -> OT_ERROR_DUPLICATED
- (7) YXRRSET Some RRset that ought not to exist, does exist -> OT_ERROR_DUPLICATED
- (8) NXRRSET Some RRset that ought to exist, does not exist -> OT_ERROR_NOT_FOUND
- (9) NOTAUTH Service is not authoritative for zone -> OT_ERROR_SECURITY
- (10) NOTZONE A name is not in the zone -> OT_ERROR_PARSE
- (20) BADNAME Bad name -> OT_ERROR_PARSE
- (21) BADALG Bad algorithm -> OT_ERROR_SECURITY
- (22) BADTRUN Bad truncation -> OT_ERROR_PARSE
- Other response codes -> OT_ERROR_FAILED

The following errors are also possible:

- OT_ERROR_RESPONSE_TIMEOUT : Timed out waiting for response from server (client would continue to retry).
- OT_ERROR_INVALID_ARGS : The provided service structure is invalid (e.g., bad service name or `otDnsTxtEntry`).
- OT_ERROR_NO_BUFS : Insufficient buffer to prepare or send the update message.

Note that in case of any failure, the client continues the operation, i.e. it prepares and (re)transmits the SRP update message to the server, after some wait interval. The retry wait interval starts from the minimum value and is increased by the growth factor every failure up to the max value (please see configuration parameter `OPENTHREAD_CONFIG_SRP_CLIENT_MIN_RETRY_WAIT_INTERVAL` and the related ones for more details).

### otSrpClientAutoStartCallback

`typedef void(* otSrpClientAutoStartCallback) (const otSockAddr *aServerSockAddr, void *aContext)`

**Description:**

Pointer type defines the callback used by SRP client to notify user when it is auto-started or stopped.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aServerSockAddr|A non-NULL pointer indicates SRP server was started and pointer will give the selected server socket address. A NULL pointer indicates SRP server was stopped.|
||[in]|aContext|A pointer to an arbitrary context (provided when callback was registered).|

**Details:**

This is only used when auto-start feature `OPENTHREAD_CONFIG_SRP_CLIENT_AUTO_START_API_ENABLE` is enabled.

This callback is invoked when auto-start mode is enabled and the SRP client is either automatically started or stopped.

### otSrpClientBuffersServiceEntry

`typedef struct otSrpClientBuffersServiceEntry otSrpClientBuffersServiceEntry`

**Description:**

Represents a SRP client service pool entry.

### otSrpServerHost

`typedef struct otSrpServerHost otSrpServerHost`

**Description:**

This opaque type represents a SRP service host.

### otSrpServerService

`typedef struct otSrpServerService otSrpServerService`

**Description:**

This opaque type represents a SRP service.

### otSrpServerServiceUpdateId

`typedef uint32_t otSrpServerServiceUpdateId`

**Description:**

The ID of a SRP service update transaction on the SRP Server.

### otSrpServerAddressMode

`typedef enum otSrpServerAddressMode otSrpServerAddressMode`

**Description:**

Represents the address mode used by the SRP server.

**Details:**

Address mode specifies how the address and port number are determined by the SRP server and how this info is published in the Thread Network Data.

**Warnings**

- Using the `OT_SRP_SERVER_ADDRESS_MODE_UNICAST_FORCE_ADD` option will make the implementation non-compliant with the Thread specification. This option is intended for testing and specific use-cases. When selected, the SRP server, upon being enabled, will bypass the Network Data publisher and always add the "SRP/DNS unicast" entry directly to the Network Data, regardless of how many other similar entries are present.

### otSrpServerTtlConfig

`typedef struct otSrpServerTtlConfig otSrpServerTtlConfig`

**Description:**

Includes SRP server TTL configurations.

### otSrpServerLeaseConfig

`typedef struct otSrpServerLeaseConfig otSrpServerLeaseConfig`

**Description:**

Includes SRP server LEASE and KEY-LEASE configurations.

### otSrpServerLeaseInfo

`typedef struct otSrpServerLeaseInfo otSrpServerLeaseInfo`

**Description:**

Includes SRP server lease information of a host/service.

### otSrpServerResponseCounters

`typedef struct otSrpServerResponseCounters otSrpServerResponseCounters`

**Description:**

Includes the statistics of SRP server responses.

### otSrpServerServiceUpdateHandler

`typedef void(* otSrpServerServiceUpdateHandler) (otSrpServerServiceUpdateId aId, const otSrpServerHost *aHost, uint32_t aTimeout, void *aContext)`

**Description:**

Handles SRP service updates.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aId|The service update transaction ID. This ID must be passed back with `otSrpServerHandleServiceUpdateResult`.|
||[in]|aHost|A pointer to the otSrpServerHost object which contains the SRP updates. The handler should publish/un-publish the host and each service points to this host with below rules:<br/><br/>1. If the host is not deleted (indicated by `otSrpServerHostIsDeleted`), then it should be published or updated with mDNS. Otherwise, the host should be un-published (remove AAAA RRs).<br/>2. For each service points to this host, it must be un-published if the host is to be un-published. Otherwise, the handler should publish or update the service when it is not deleted (indicated by `otSrpServerServiceIsDeleted`) and un-publish it when deleted.|
||[in]|aTimeout|The maximum time in milliseconds for the handler to process the service event.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

Is called by the SRP server to notify that a SRP host and possibly SRP services are being updated. It is important that the SRP updates are not committed until the handler returns the result by calling otSrpServerHandleServiceUpdateResult or times out after `aTimeout`.

A SRP service observer should always call otSrpServerHandleServiceUpdateResult with error code OT_ERROR_NONE immediately after receiving the update events.

A more generic handler may perform validations on the SRP host/services and rejects the SRP updates if any validation fails. For example, an Advertising Proxy should advertise (or remove) the host and services on a multicast-capable link and returns specific error code if any failure occurs.

**See Also**

- [otSrpServerSetServiceUpdateHandler](api-srp#ot-srp-server-set-service-update-handler)
- [otSrpServerHandleServiceUpdateResult](api-srp#ot-srp-server-handle-service-update-result)

## Functions

### otSrpClientStart

`otError otSrpClientStart(otInstance *aInstance, const otSockAddr *aServerSockAddr)`

**Description:** Starts the SRP client operation.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|const [otSockAddr](ot-sock-addr) *|[in]|aServerSockAddr|The socket address (IPv6 address and port number) of the SRP server.|

SRP client will prepare and send "SRP Update" message to the SRP server once all the following conditions are met:

- The SRP client is started - `otSrpClientStart()` is called.
- Host name is set - `otSrpClientSetHostName()` is called.
- At least one host IPv6 address is set - `otSrpClientSetHostAddresses()` is called.
- At least one service is added - `otSrpClientAddService()` is called.

It does not matter in which order these functions are called. When all conditions are met, the SRP client will wait for a short delay before preparing an "SRP Update" message and sending it to server. This delay allows for user to add multiple services and/or IPv6 addresses before the first SRP Update message is sent (ensuring a single SRP Update is sent containing all the info). The config `OPENTHREAD_CONFIG_SRP_CLIENT_UPDATE_TX_DELAY` specifies the delay interval.

### otSrpClientStop

`void otSrpClientStop(otInstance *aInstance)`

**Description:** Stops the SRP client operation.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

Stops any further interactions with the SRP server. Note that it does not remove or clear host info and/or list of services. It marks all services to be added/removed again once the client is (re)started.

### otSrpClientIsRunning

`bool otSrpClientIsRunning(otInstance *aInstance)`

**Description:** Indicates whether the SRP client is running or not.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

**Returns**

- TRUE if the SRP client is running, FALSE otherwise.

### otSrpClientGetServerAddress

`const otSockAddr * otSrpClientGetServerAddress(otInstance *aInstance)`

**Description:** Gets the socket address (IPv6 address and port number) of the SRP server which is being used by SRP client.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

If the client is not running, the address is unspecified (all zero) with zero port number.

**Returns**

- A pointer to the SRP server's socket address (is always non-NULL).

### otSrpClientSetCallback

`void otSrpClientSetCallback(otInstance *aInstance, otSrpClientCallback aCallback, void *aContext)`

**Description:** Sets the callback to notify caller of events/changes from SRP client.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otSrpClientCallback](api-srp#ot-srp-client-callback)|[in]|aCallback|The callback to notify of events and changes. Can be NULL if not needed.|
|void *|[in]|aContext|An arbitrary context used with `aCallback`.|

The SRP client allows a single callback to be registered. So consecutive calls to this function will overwrite any previously set callback functions.

### otSrpClientEnableAutoStartMode

`void otSrpClientEnableAutoStartMode(otInstance *aInstance, otSrpClientAutoStartCallback aCallback, void *aContext)`

**Description:** Enables the auto-start mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otSrpClientAutoStartCallback](api-srp#ot-srp-client-auto-start-callback)|[in]|aCallback|A callback to notify when client is auto-started/stopped. Can be NULL if not needed.|
|void *|[in]|aContext|A context to be passed when invoking `aCallback`.|

This is only available when auto-start feature `OPENTHREAD_CONFIG_SRP_CLIENT_AUTO_START_API_ENABLE` is enabled.

Config option `OPENTHREAD_CONFIG_SRP_CLIENT_AUTO_START_DEFAULT_MODE` specifies the default auto-start mode (whether it is enabled or disabled at the start of OT stack).

When auto-start is enabled, the SRP client will monitor the Thread Network Data to discover SRP servers and select the preferred server and automatically start and stop the client when an SRP server is detected.

There are three categories of Network Data entries indicating presence of SRP sever. They are preferred in the following order:

1) Preferred unicast entries where server address is included in the service data. If there are multiple options, the one with numerically lowest IPv6 address is preferred.

2) Anycast entries each having a seq number. A larger sequence number in the sense specified by Serial Number Arithmetic logic in RFC-1982 is considered more recent and therefore preferred. The largest seq number using serial number arithmetic is preferred if it is well-defined (i.e., the seq number is larger than all other seq numbers). If it is not well-defined, then the numerically largest seq number is preferred.

3) Unicast entries where the server address info is included in server data. If there are multiple options, the one with numerically lowest IPv6 address is preferred.

When there is a change in the Network Data entries, client will check that the currently selected server is still present in the Network Data and is still the preferred one. Otherwise the client will switch to the new preferred server or stop if there is none.

When the SRP client is explicitly started through a successful call to `otSrpClientStart()`, the given SRP server address in `otSrpClientStart()` will continue to be used regardless of the state of auto-start mode and whether the same SRP server address is discovered or not in the Thread Network Data. In this case, only an explicit `otSrpClientStop()` call will stop the client.

### otSrpClientDisableAutoStartMode

`void otSrpClientDisableAutoStartMode(otInstance *aInstance)`

**Description:** Disables the auto-start mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

This is only available when auto-start feature `OPENTHREAD_CONFIG_SRP_CLIENT_AUTO_START_API_ENABLE` is enabled.

Disabling the auto-start mode will not stop the client if it is already running but the client stops monitoring the Thread Network Data to verify that the selected SRP server is still present in it.

Note that a call to `otSrpClientStop()` will also disable the auto-start mode.

### otSrpClientIsAutoStartModeEnabled

`bool otSrpClientIsAutoStartModeEnabled(otInstance *aInstance)`

**Description:** Indicates the current state of auto-start mode (enabled or disabled).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

This is only available when auto-start feature `OPENTHREAD_CONFIG_SRP_CLIENT_AUTO_START_API_ENABLE` is enabled.

**Returns**

- TRUE if the auto-start mode is enabled, FALSE otherwise.

### otSrpClientGetTtl

`uint32_t otSrpClientGetTtl(otInstance *aInstance)`

**Description:** Gets the TTL value in every record included in SRP update requests.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

Note that this is the TTL requested by the SRP client. The server may choose to accept a different TTL.

By default, the TTL will equal the lease interval. Passing 0 or a value larger than the lease interval via `otSrpClientSetTtl()` will also cause the TTL to equal the lease interval.

**Returns**

- The TTL (in seconds).

### otSrpClientSetTtl

`void otSrpClientSetTtl(otInstance *aInstance, uint32_t aTtl)`

**Description:** Sets the TTL value in every record included in SRP update requests.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|uint32_t|[in]|aTtl|The TTL (in seconds). If value is zero or greater than lease interval, the TTL is set to the lease interval.|

Changing the TTL does not impact the TTL of already registered services/host-info. It only affects future SRP update messages (i.e., adding new services and/or refreshes of the existing services).

### otSrpClientGetLeaseInterval

`uint32_t otSrpClientGetLeaseInterval(otInstance *aInstance)`

**Description:** Gets the default lease interval used in SRP update requests.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

The default interval is used only for `otSrpClientService` instances with `mLease` set to zero.

Note that this is the lease duration requested by the SRP client. The server may choose to accept a different lease interval.

**Returns**

- The lease interval (in seconds).

### otSrpClientSetLeaseInterval

`void otSrpClientSetLeaseInterval(otInstance *aInstance, uint32_t aInterval)`

**Description:** Sets the default lease interval used in SRP update requests.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|uint32_t|[in]|aInterval|The lease interval (in seconds). If zero, the default value specified by `OPENTHREAD_CONFIG_SRP_CLIENT_DEFAULT_LEASE` would be used.|

The default interval is used only for `otSrpClientService` instances with `mLease` set to zero.

Changing the lease interval does not impact the accepted lease interval of already registered services/host-info. It only affects any future SRP update messages (i.e., adding new services and/or refreshes of the existing services).

### otSrpClientGetKeyLeaseInterval

`uint32_t otSrpClientGetKeyLeaseInterval(otInstance *aInstance)`

**Description:** Gets the default key lease interval used in SRP update requests.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

The default interval is used only for `otSrpClientService` instances with `mKeyLease` set to zero.

Note that this is the lease duration requested by the SRP client. The server may choose to accept a different lease interval.

**Returns**

- The key lease interval (in seconds).

### otSrpClientSetKeyLeaseInterval

`void otSrpClientSetKeyLeaseInterval(otInstance *aInstance, uint32_t aInterval)`

**Description:** Sets the default key lease interval used in SRP update requests.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|uint32_t|[in]|aInterval|The key lease interval (in seconds). If zero, the default value specified by `OPENTHREAD_CONFIG_SRP_CLIENT_DEFAULT_KEY_LEASE` would be used.|

The default interval is used only for `otSrpClientService` instances with `mKeyLease` set to zero.

Changing the lease interval does not impact the accepted lease interval of already registered services/host-info. It only affects any future SRP update messages (i.e., adding new services and/or refreshes of existing services).

### otSrpClientGetHostInfo

`const otSrpClientHostInfo * otSrpClientGetHostInfo(otInstance *aInstance)`

**Description:** Gets the host info.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

**Returns**

- A pointer to host info structure.

### otSrpClientSetHostName

`otError otSrpClientSetHostName(otInstance *aInstance, const char *aName)`

**Description:** Sets the host name label.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|const char *|[in]|aName|A pointer to host name label string (MUST NOT be NULL). Pointer to the string buffer MUST persist and remain valid and constant after return from this function.|

After a successful call to this function, `otSrpClientCallback` will be called to report the status of host info registration with SRP server.

The name string buffer pointed to by `aName` MUST persist and stay unchanged after returning from this function. OpenThread will keep the pointer to the string.

The host name can be set before client is started or after start but before host info is registered with server (host info should be in either `STATE_TO_ADD` or `STATE_REMOVED`).

### otSrpClientEnableAutoHostAddress

`otError otSrpClientEnableAutoHostAddress(otInstance *aInstance)`

**Description:** Enables auto host address mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

When enabled host IPv6 addresses are automatically set by SRP client using all the preferred unicast addresses on Thread netif excluding all link-local and mesh-local addresses. If there is no preferred address, then Mesh Local EID address is added. The SRP client will automatically re-register when/if addresses on Thread netif are updated (new addresses are added or existing addresses are removed or marked as non-preferred).

The auto host address mode can be enabled before start or during operation of SRP client except when the host info is being removed (client is busy handling a remove request from an call to `otSrpClientRemoveHostAndServices()` and host info still being in either `STATE_TO_REMOVE` or `STATE_REMOVING` states).

After auto host address mode is enabled, it can be disabled by a call to `otSrpClientSetHostAddresses()` which then explicitly sets the host addresses.

### otSrpClientSetHostAddresses

`otError otSrpClientSetHostAddresses(otInstance *aInstance, const otIp6Address *aIp6Addresses, uint8_t aNumAddresses)`

**Description:** Sets/updates the list of host IPv6 address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aIp6Addresses|A pointer to the an array containing the host IPv6 addresses.|
|uint8_t|[in]|aNumAddresses|The number of addresses in the `aIp6Addresses` array.|

Host IPv6 addresses can be set/changed before start or during operation of SRP client (e.g. to add/remove or change a previously registered host address), except when the host info is being removed (client is busy handling a remove request from an earlier call to `otSrpClientRemoveHostAndServices()` and host info still being in either `STATE_TO_REMOVE` or `STATE_REMOVING` states).

The host IPv6 address array pointed to by `aIp6Addresses` MUST persist and remain unchanged after returning from this function (with `OT_ERROR_NONE`). OpenThread will save the pointer to the array.

After a successful call to this function, `otSrpClientCallback` will be called to report the status of the address registration with SRP server.

Calling this function disables auto host address mode if it was previously enabled from a successful call to `otSrpClientEnableAutoHostAddress()`.

### otSrpClientAddService

`otError otSrpClientAddService(otInstance *aInstance, otSrpClientService *aService)`

**Description:** Adds a service to be registered with server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otSrpClientService](ot-srp-client-service) *|[in]|aService|A pointer to a `otSrpClientService` instance to add.|

After a successful call to this function, `otSrpClientCallback` will be called to report the status of the service addition/registration with SRP server.

The `otSrpClientService` instance being pointed to by `aService` MUST persist and remain unchanged after returning from this function (with `OT_ERROR_NONE`). OpenThread will save the pointer to the service instance.

The `otSrpClientService` instance is not longer tracked by OpenThread and can be reclaimed only when

- It is removed explicitly by a call to `otSrpClientRemoveService()` or removed along with other services by a call to `otSrpClientRemoveHostAndServices() and only after the`otSrpClientCallback` is called indicating the service was removed. Or,
- A call to `otSrpClientClearHostAndServices()` which removes the host and all related services immediately.

### otSrpClientRemoveService

`otError otSrpClientRemoveService(otInstance *aInstance, otSrpClientService *aService)`

**Description:** Requests a service to be unregistered with server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otSrpClientService](ot-srp-client-service) *|[in]|aService|A pointer to a `otSrpClientService` instance to remove.|

After a successful call to this function, `otSrpClientCallback` will be called to report the status of remove request with SRP server.

The `otSrpClientService` instance being pointed to by `aService` MUST persist and remain unchanged after returning from this function (with `OT_ERROR_NONE`). OpenThread will keep the service instance during the remove process. Only after the `otSrpClientCallback` is called indicating the service instance is removed from SRP client service list and can be be freed/reused.

### otSrpClientClearService

`otError otSrpClientClearService(otInstance *aInstance, otSrpClientService *aService)`

**Description:** Clears a service, immediately removing it from the client service list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otSrpClientService](ot-srp-client-service) *|[in]|aService|A pointer to a `otSrpClientService` instance to delete.|

Unlike `otSrpClientRemoveService()` which sends an update message to the server to remove the service, this function clears the service from the client's service list without any interaction with the server. On a successful call to this function, the `otSrpClientCallback` will NOT be called and the `aService` entry can be reclaimed and re-used by the caller immediately.

Can be used along with a subsequent call to `otSrpClientAddService()` (potentially reusing the same `aService` entry with the same service and instance names) to update some of the parameters in an existing service.

### otSrpClientGetServices

`const otSrpClientService * otSrpClientGetServices(otInstance *aInstance)`

**Description:** Gets the list of services being managed by client.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

**Returns**

- A pointer to the head of linked-list of all services or NULL if the list is empty.

### otSrpClientRemoveHostAndServices

`otError otSrpClientRemoveHostAndServices(otInstance *aInstance, bool aRemoveKeyLease, bool aSendUnregToServer)`

**Description:** Starts the remove process of the host info and all services.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|bool|[in]|aRemoveKeyLease|A boolean indicating whether or not the host key lease should also be removed.|
|bool|[in]|aSendUnregToServer|A boolean indicating whether to send update to server when host info is not registered.|

After returning from this function, `otSrpClientCallback` will be called to report the status of remove request with SRP server.

If the host info is to be permanently removed from server, `aRemoveKeyLease` should be set to `true` which removes the key lease associated with host on server. Otherwise, the key lease record is kept as before, which ensures that the server holds the host name in reserve for when the client is once again able to provide and register its service(s).

The `aSendUnregToServer` determines the behavior when the host info is not yet registered with the server. If `aSendUnregToServer` is set to `false` (which is the default/expected value) then the SRP client will immediately remove the host info and services without sending an update message to server (no need to update the server if nothing is yet registered with it). If `aSendUnregToServer` is set to `true` then the SRP client will send an update message to the server. Note that if the host info is registered then the value of `aSendUnregToServer` does not matter and the SRP client will always send an update message to server requesting removal of all info.

One situation where `aSendUnregToServer` can be useful is on a device reset/reboot, caller may want to remove any previously registered services with the server. In this case, caller can `otSrpClientSetHostName()` and then request `otSrpClientRemoveHostAndServices()` with `aSendUnregToServer` as `true`.

### otSrpClientClearHostAndServices

`void otSrpClientClearHostAndServices(otInstance *aInstance)`

**Description:** Clears all host info and all the services.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

Unlike `otSrpClientRemoveHostAndServices()` which sends an update message to the server to remove all the info, this function clears all the info immediately without any interaction with the server.

### otSrpClientGetDomainName

`const char * otSrpClientGetDomainName(otInstance *aInstance)`

**Description:** Gets the domain name being used by SRP client.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

Requires `OPENTHREAD_CONFIG_SRP_CLIENT_DOMAIN_NAME_API_ENABLE` to be enabled.

If domain name is not set, "default.service.arpa" will be used.

**Returns**

- The domain name string.

### otSrpClientSetDomainName

`otError otSrpClientSetDomainName(otInstance *aInstance, const char *aName)`

**Description:** Sets the domain name to be used by SRP client.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|const char *|[in]|aName|A pointer to the domain name string. If NULL sets it to default "default.service.arpa".|

Requires `OPENTHREAD_CONFIG_SRP_CLIENT_DOMAIN_NAME_API_ENABLE` to be enabled.

If not set "default.service.arpa" will be used.

The name string buffer pointed to by `aName` MUST persist and stay unchanged after returning from this function. OpenThread will keep the pointer to the string.

The domain name can be set before client is started or after start but before host info is registered with server (host info should be in either `STATE_TO_ADD` or `STATE_TO_REMOVE`).

### otSrpClientItemStateToString

`const char * otSrpClientItemStateToString(otSrpClientItemState aItemState)`

**Description:** Converts a `otSrpClientItemState` to a string.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otSrpClientItemState](api-srp#ot-srp-client-item-state)|[in]|aItemState|An item state.|

**Returns**

- A string representation of `aItemState`.

### otSrpClientSetServiceKeyRecordEnabled

`void otSrpClientSetServiceKeyRecordEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Enables/disables "service key record inclusion" mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|bool|[in]|aEnabled|TRUE to enable, FALSE to disable the "service key record inclusion" mode.|

When enabled, SRP client will include KEY record in Service Description Instructions in the SRP update messages that it sends.

Is available when `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` configuration is enabled.

**Note**

- KEY record is optional in Service Description Instruction (it is required and always included in the Host Description Instruction). The default behavior of SRP client is to not include it. This function is intended to override the default behavior for testing only.

### otSrpClientIsServiceKeyRecordEnabled

`bool otSrpClientIsServiceKeyRecordEnabled(otInstance *aInstance)`

**Description:** Indicates whether the "service key record inclusion" mode is enabled or disabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

Is available when `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` configuration is enabled.

**Returns**

- TRUE if "service key record inclusion" mode is enabled, FALSE otherwise.

### otSrpClientBuffersGetHostNameString

`char * otSrpClientBuffersGetHostNameString(otInstance *aInstance, uint16_t *aSize)`

**Description:** Gets the string buffer to use for SRP client host name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|uint16_t *|[out]|aSize|Pointer to a variable to return the size (number of bytes) of the string buffer (MUST NOT be NULL).|

**Returns**

- A pointer to char buffer to use for SRP client host name.

### otSrpClientBuffersGetHostAddressesArray

`otIp6Address * otSrpClientBuffersGetHostAddressesArray(otInstance *aInstance, uint8_t *aArrayLength)`

**Description:** Gets the array of IPv6 address entries to use as SRP client host address list.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|uint8_t *|[out]|aArrayLength|Pointer to a variable to return the array length i.e., number of IPv6 address entries in the array (MUST NOT be NULL).|

**Returns**

- A pointer to an array of `otIp6Address` entries (number of entries is returned in `aArrayLength`).

### otSrpClientBuffersAllocateService

`otSrpClientBuffersServiceEntry * otSrpClientBuffersAllocateService(otInstance *aInstance)`

**Description:** Allocates a new service entry from the pool.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

The returned service entry instance will be initialized as follows:

- `mService.mName` will point to an allocated string buffer which can be retrieved using the function `otSrpClientBuffersGetServiceEntryServiceNameString()`.
- `mService.mInstanceName` will point to an allocated string buffer which can be retrieved using the function `otSrpClientBuffersGetServiceEntryInstanceNameString()`.
- `mService.mSubTypeLabels` points to an array that is returned from `otSrpClientBuffersGetSubTypeLabelsArray()`.
- `mService.mTxtEntries` will point to `mTxtEntry`.
- `mService.mNumTxtEntries` will be set to one.
- Other `mService` fields (port, priority, weight) are set to zero.
- `mTxtEntry.mKey` is set to NULL (value is treated as already encoded).
- `mTxtEntry.mValue` will point to an allocated buffer which can be retrieved using the function `otSrpClientBuffersGetServiceEntryTxtBuffer()`.
- `mTxtEntry.mValueLength` is set to zero.
- All related data/string buffers and arrays are cleared to all zero.

**Returns**

- A pointer to the newly allocated service entry or NULL if not more entry available in the pool.

### otSrpClientBuffersFreeService

`void otSrpClientBuffersFreeService(otInstance *aInstance, otSrpClientBuffersServiceEntry *aService)`

**Description:** Frees a previously allocated service entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|
|[otSrpClientBuffersServiceEntry](ot-srp-client-buffers-service-entry) *|[in]|aService|A pointer to the service entry to free (MUST NOT be NULL).|

The `aService` MUST be previously allocated using `otSrpClientBuffersAllocateService()` and not yet freed. Otherwise the behavior of this function is undefined.

### otSrpClientBuffersFreeAllServices

`void otSrpClientBuffersFreeAllServices(otInstance *aInstance)`

**Description:** Frees all previously allocated service entries.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

### otSrpClientBuffersGetServiceEntryServiceNameString

`char * otSrpClientBuffersGetServiceEntryServiceNameString(otSrpClientBuffersServiceEntry *aEntry, uint16_t *aSize)`

**Description:** Gets the string buffer for service name from a service entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otSrpClientBuffersServiceEntry](ot-srp-client-buffers-service-entry) *|[in]|aEntry|A pointer to a previously allocated service entry (MUST NOT be NULL).|
|uint16_t *|[out]|aSize|A pointer to a variable to return the size (number of bytes) of the string buffer (MUST NOT be NULL).|

**Returns**

- A pointer to the string buffer.

### otSrpClientBuffersGetServiceEntryInstanceNameString

`char * otSrpClientBuffersGetServiceEntryInstanceNameString(otSrpClientBuffersServiceEntry *aEntry, uint16_t *aSize)`

**Description:** Gets the string buffer for service instance name from a service entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otSrpClientBuffersServiceEntry](ot-srp-client-buffers-service-entry) *|[in]|aEntry|A pointer to a previously allocated service entry (MUST NOT be NULL).|
|uint16_t *|[out]|aSize|A pointer to a variable to return the size (number of bytes) of the string buffer (MUST NOT be NULL).|

**Returns**

- A pointer to the string buffer.

### otSrpClientBuffersGetServiceEntryTxtBuffer

`uint8_t * otSrpClientBuffersGetServiceEntryTxtBuffer(otSrpClientBuffersServiceEntry *aEntry, uint16_t *aSize)`

**Description:** Gets the buffer for TXT record from a service entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otSrpClientBuffersServiceEntry](ot-srp-client-buffers-service-entry) *|[in]|aEntry|A pointer to a previously allocated service entry (MUST NOT be NULL).|
|uint16_t *|[out]|aSize|A pointer to a variable to return the size (number of bytes) of the buffer (MUST NOT be NULL).|

**Returns**

- A pointer to the buffer.

### otSrpClientBuffersGetSubTypeLabelsArray

`const char ** otSrpClientBuffersGetSubTypeLabelsArray(otSrpClientBuffersServiceEntry *aEntry, uint16_t *aArrayLength)`

**Description:** Gets the array for service subtype labels from the service entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otSrpClientBuffersServiceEntry](ot-srp-client-buffers-service-entry) *|[in]|aEntry|A pointer to a previously allocated service entry (MUST NOT be NULL).|
|uint16_t *|[out]|aArrayLength|A pointer to a variable to return the array length (MUST NOT be NULL).|

**Returns**

- A pointer to the array.

### otSrpServerGetDomain

`const char * otSrpServerGetDomain(otInstance *aInstance)`

**Description:** Returns the domain authorized to the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

If the domain if not set by SetDomain, "default.service.arpa." will be returned. A trailing dot is always appended even if the domain is set without it.

**Returns**

- A pointer to the dot-joined domain string.

### otSrpServerSetDomain

`otError otSrpServerSetDomain(otInstance *aInstance, const char *aDomain)`

**Description:** Sets the domain on the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const char *|[in]|aDomain|The domain to be set. MUST NOT be NULL.|

A trailing dot will be appended to `aDomain` if it is not already there. Should only be called before the SRP server is enabled.

### otSrpServerGetState

`otSrpServerState otSrpServerGetState(otInstance *aInstance)`

**Description:** Returns the state of the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- The current state of the SRP server.

### otSrpServerGetPort

`uint16_t otSrpServerGetPort(otInstance *aInstance)`

**Description:** Returns the port the SRP server is listening to.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- The port of the SRP server. It returns 0 if the server is not running.

### otSrpServerGetAddressMode

`otSrpServerAddressMode otSrpServerGetAddressMode(otInstance *aInstance)`

**Description:** Returns the address mode being used by the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- The SRP server's address mode.

### otSrpServerSetAddressMode

`otError otSrpServerSetAddressMode(otInstance *aInstance, otSrpServerAddressMode aMode)`

**Description:** Sets the address mode to be used by the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otSrpServerAddressMode](api-srp#ot-srp-server-address-mode)|[in]|aMode|The address mode to use.|

### otSrpServerGetAnycastModeSequenceNumber

`uint8_t otSrpServerGetAnycastModeSequenceNumber(otInstance *aInstance)`

**Description:** Returns the sequence number used with anycast address mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

The sequence number is included in "DNS/SRP Service Anycast Address" entry published in the Network Data.

**Returns**

- The anycast sequence number.

### otSrpServerSetAnycastModeSequenceNumber

`otError otSrpServerSetAnycastModeSequenceNumber(otInstance *aInstance, uint8_t aSequenceNumber)`

**Description:** Sets the sequence number used with anycast address mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aSequenceNumber|The sequence number to use.|

### otSrpServerSetEnabled

`void otSrpServerSetEnabled(otInstance *aInstance, bool aEnabled)`

**Description:** Enables/disables the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnabled|A boolean to enable/disable the SRP server.|

On a Border Router, it is recommended to use `otSrpServerSetAutoEnableMode()` instead.

### otSrpServerSetAutoEnableMode

`void otSrpServerSetAutoEnableMode(otInstance *aInstance, bool aEnabled)`

**Description:** Enables/disables the auto-enable mode on SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnabled|A boolean to enable/disable the auto-enable mode.|

Requires `OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE` feature.

When this mode is enabled, the Border Routing Manager controls if/when to enable or disable the SRP server. SRP sever is auto-enabled if/when Border Routing is started and it is done with the initial prefix and route configurations (when the OMR and on-link prefixes are determined, advertised in emitted Router Advertisement message on infrastructure side and published in the Thread Network Data). The SRP server is auto-disabled if/when BR is stopped (e.g., if the infrastructure network interface is brought down or if BR gets detached).

This mode can be disabled by a `otSrpServerSetAutoEnableMode()` call with `aEnabled` set to `false` or if the SRP server is explicitly enabled or disabled by a call to `otSrpServerSetEnabled()` function. Disabling auto-enable mode using `otSrpServerSetAutoEnableMode(false)` will not change the current state of SRP sever (e.g., if it is enabled it stays enabled).

### otSrpServerIsAutoEnableMode

`bool otSrpServerIsAutoEnableMode(otInstance *aInstance)`

**Description:** Indicates whether the auto-enable mode is enabled or disabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE` feature.

### otSrpServerEnableFastStartMode

`otError otSrpServerEnableFastStartMode(otInstance *aInstance)`

**Description:** Enables the "Fast Start Mode" on the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to the OpenThread instance.|

Requires the `OPENTHREAD_CONFIG_SRP_SERVER_FAST_START_MODE_ENABLE` feature to be enabled.

The Fast Start Mode is designed for scenarios where a device, often a mobile device, needs to act as a provisional SRP server (e.g., functioning as a temporary Border Router). The SRP server function is enabled only if no other Border Routers (BRs) are already providing the SRP service within the Thread network. A common use case is a mobile device joining a Thread network where it may be the first, or only, BR. Importantly, Fast Start Mode allows the device to quickly start its SRP server functionality upon joining the network, allowing other Thread devices to quickly connect and register their services without the typical delays associated with standard Border Router initialization (and SRP server startup).

When Fast Start Mode is enabled, the SRP server manages when to start or stop based on the presence of other BRs, following this process:

- Upon initial attachment to the Thread network, the device immediately inspects the received Network Data for any existing "SRP/DNS" entries. These entries indicate the presence of other active BRs providing SRP server service:  
  - If no "SRP/DNS" entries from other BRs are found, the device immediately enables its own SRP server. This activation uses `OT_SRP_SERVER_ADDRESS_MODE_UNICAST_FORCE_ADD`, which bypasses the usual delay associated with the standard Network Data publisher, directly adding its own "SRP/DNS unicast" entry to the Network Data.  
  - If "SRP/DNS" entries from other BRs are detected, the device will not enable its SRP server, deferring to the existing ones.
- After starting its SRP server in Fast Start Mode, the device continuously monitors the Network Data. If, at any point, new "SRP/DNS" entries appear (indicating that another BR has become active), the device automatically disables its own SRP server functionality, relinquishing the role to the newly available BR.

The Fast Start Mode can be enabled when the device is in the detached or disabled state, the SRP server is currently disabled, and "auto-enable mode" is not in use (i.e., `otSrpServerIsAutoEnableMode()` returns `false`).

After successfully enabling Fast Start Mode, it can be disabled either by a call to `otSrpServerSetEnabled()`, explicitly enabling or disabling the SRP server, or by a call to `otSrpServerSetAutoEnableMode()`, enabling or disabling the auto-enable mode. If the Fast Start Mode (while active) enables the SRP server, upon disabling Fast Start Mode (regardless of how it is done), the SRP server will also be stopped, and the use of the `OT_SRP_SERVER_ADDRESS_MODE_UNICAST_FORCE_ADD` address mode will be stopped, and the address mode will be automatically reverted back to its previous setting before Fast Start Mode was enabled.

### otSrpServerIsFastStartModeEnabled

`bool otSrpServerIsFastStartModeEnabled(otInstance *aInstance)`

**Description:** Indicates whether the Fast Start Mode is enabled or disabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_SRP_SERVER_FAST_START_MODE_ENABLE` feature to be enabled.

### otSrpServerGetTtlConfig

`void otSrpServerGetTtlConfig(otInstance *aInstance, otSrpServerTtlConfig *aTtlConfig)`

**Description:** Returns SRP server TTL configuration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otSrpServerTtlConfig](ot-srp-server-ttl-config) *|[out]|aTtlConfig|A pointer to an `otSrpServerTtlConfig` instance.|

### otSrpServerSetTtlConfig

`otError otSrpServerSetTtlConfig(otInstance *aInstance, const otSrpServerTtlConfig *aTtlConfig)`

**Description:** Sets SRP server TTL configuration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otSrpServerTtlConfig](ot-srp-server-ttl-config) *|[in]|aTtlConfig|A pointer to an `otSrpServerTtlConfig` instance.|

The granted TTL will always be no greater than the max lease interval configured via `otSrpServerSetLeaseConfig()`, regardless of the minimum and maximum TTL configuration.

### otSrpServerGetLeaseConfig

`void otSrpServerGetLeaseConfig(otInstance *aInstance, otSrpServerLeaseConfig *aLeaseConfig)`

**Description:** Returns SRP server LEASE and KEY-LEASE configurations.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otSrpServerLeaseConfig](ot-srp-server-lease-config) *|[out]|aLeaseConfig|A pointer to an `otSrpServerLeaseConfig` instance.|

### otSrpServerSetLeaseConfig

`otError otSrpServerSetLeaseConfig(otInstance *aInstance, const otSrpServerLeaseConfig *aLeaseConfig)`

**Description:** Sets SRP server LEASE and KEY-LEASE configurations.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otSrpServerLeaseConfig](ot-srp-server-lease-config) *|[in]|aLeaseConfig|A pointer to an `otSrpServerLeaseConfig` instance.|

When a non-zero LEASE time is requested from a client, the granted value will be limited in range [aMinLease, aMaxLease]; and a non-zero KEY-LEASE will be granted in range [aMinKeyLease, aMaxKeyLease]. For zero LEASE or KEY-LEASE time, zero will be granted.

### otSrpServerSetServiceUpdateHandler

`void otSrpServerSetServiceUpdateHandler(otInstance *aInstance, otSrpServerServiceUpdateHandler aServiceHandler, void *aContext)`

**Description:** Sets the SRP service updates handler on SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otSrpServerServiceUpdateHandler](api-srp#ot-srp-server-service-update-handler)|[in]|aServiceHandler|A pointer to a service handler. Use NULL to remove the handler.|
|void *|[in]|aContext|A pointer to arbitrary context information. May be NULL if not used.|

### otSrpServerHandleServiceUpdateResult

`void otSrpServerHandleServiceUpdateResult(otInstance *aInstance, otSrpServerServiceUpdateId aId, otError aError)`

**Description:** Reports the result of processing a SRP update to the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otSrpServerServiceUpdateId](api-srp#ot-srp-server-service-update-id)|[in]|aId|The service update transaction ID. This should be the same ID provided via `otSrpServerServiceUpdateHandler`.|
|[otError](api-error#ot-error)|[in]|aError|An error to be returned to the SRP server. Use OT_ERROR_DUPLICATED to represent DNS name conflicts.|

The Service Update Handler should call this function to return the result of its processing of a SRP update.

### otSrpServerGetNextHost

`const otSrpServerHost * otSrpServerGetNextHost(otInstance *aInstance, const otSrpServerHost *aHost)`

**Description:** Returns the next registered host on the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otSrpServerHost](api-srp#ot-srp-server-host) *|[in]|aHost|A pointer to current host; use NULL to get the first host.|

**Returns**

- A pointer to the registered host. NULL, if no more hosts can be found.

### otSrpServerGetResponseCounters

`const otSrpServerResponseCounters * otSrpServerGetResponseCounters(otInstance *aInstance)`

**Description:** Returns the response counters of the SRP server.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**Returns**

- A pointer to the response counters of the SRP server.

### otSrpServerHostIsDeleted

`bool otSrpServerHostIsDeleted(const otSrpServerHost *aHost)`

**Description:** Tells if the SRP service host has been deleted.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerHost](api-srp#ot-srp-server-host) *|[in]|aHost|A pointer to the SRP service host.|

A SRP service host can be deleted but retains its name for future uses. In this case, the host instance is not removed from the SRP server/registry.

**Returns**

- TRUE if the host has been deleted, FALSE if not.

### otSrpServerHostGetFullName

`const char * otSrpServerHostGetFullName(const otSrpServerHost *aHost)`

**Description:** Returns the full name of the host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerHost](api-srp#ot-srp-server-host) *|[in]|aHost|A pointer to the SRP service host.|

**Returns**

- A pointer to the null-terminated host name string.

### otSrpServerHostMatchesFullName

`bool otSrpServerHostMatchesFullName(const otSrpServerHost *aHost, const char *aFullName)`

**Description:** Indicates whether the host matches a given host name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerHost](api-srp#ot-srp-server-host) *|[in]|aHost|A pointer to the SRP service host.|
|const char *|[in]|aFullName|A full host name.|

DNS name matches are performed using a case-insensitive string comparison (i.e., "Abc" and "aBc" are considered to be the same).

### otSrpServerHostGetAddresses

`const otIp6Address * otSrpServerHostGetAddresses(const otSrpServerHost *aHost, uint8_t *aAddressesNum)`

**Description:** Returns the addresses of given host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerHost](api-srp#ot-srp-server-host) *|[in]|aHost|A pointer to the SRP service host.|
|uint8_t *|[out]|aAddressesNum|A pointer to where we should output the number of the addresses to.|

**Returns**

- A pointer to the array of IPv6 Address.

### otSrpServerHostGetLeaseInfo

`void otSrpServerHostGetLeaseInfo(const otSrpServerHost *aHost, otSrpServerLeaseInfo *aLeaseInfo)`

**Description:** Returns the LEASE and KEY-LEASE information of a given host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerHost](api-srp#ot-srp-server-host) *|[in]|aHost|A pointer to the SRP server host.|
|[otSrpServerLeaseInfo](ot-srp-server-lease-info) *|[out]|aLeaseInfo|A pointer to where to output the LEASE and KEY-LEASE information.|

### otSrpServerHostGetNextService

`const otSrpServerService * otSrpServerHostGetNextService(const otSrpServerHost *aHost, const otSrpServerService *aService)`

**Description:** Returns the next service of given host.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerHost](api-srp#ot-srp-server-host) *|[in]|aHost|A pointer to the SRP service host.|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to current SRP service instance; use NULL to get the first service.|

**Returns**

- A pointer to the next service or NULL if there is no more services.

### otSrpServerServiceIsDeleted

`bool otSrpServerServiceIsDeleted(const otSrpServerService *aService)`

**Description:** Indicates whether or not the SRP service has been deleted.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

A SRP service can be deleted but retains its name for future uses. In this case, the service instance is not removed from the SRP server/registry. It is guaranteed that all services are deleted if the host is deleted.

**Returns**

- TRUE if the service has been deleted, FALSE if not.

### otSrpServerServiceGetInstanceName

`const char * otSrpServerServiceGetInstanceName(const otSrpServerService *aService)`

**Description:** Returns the full service instance name of the service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- A pointer to the null-terminated service instance name string.

### otSrpServerServiceMatchesInstanceName

`bool otSrpServerServiceMatchesInstanceName(const otSrpServerService *aService, const char *aInstanceName)`

**Description:** Indicates whether this service matches a given service instance name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|
|const char *|[in]|aInstanceName|The service instance name.|

DNS name matches are performed using a case-insensitive string comparison (i.e., "Abc" and "aBc" are considered to be the same).

### otSrpServerServiceGetInstanceLabel

`const char * otSrpServerServiceGetInstanceLabel(const otSrpServerService *aService)`

**Description:** Returns the service instance label (first label in instance name) of the service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- A pointer to the null-terminated service instance label string..

### otSrpServerServiceGetServiceName

`const char * otSrpServerServiceGetServiceName(const otSrpServerService *aService)`

**Description:** Returns the full service name of the service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- A pointer to the null-terminated service name string.

### otSrpServerServiceMatchesServiceName

`bool otSrpServerServiceMatchesServiceName(const otSrpServerService *aService, const char *aServiceName)`

**Description:** Indicates whether this service matches a given service name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|
|const char *|[in]|aServiceName|The service name.|

DNS name matches are performed using a case-insensitive string comparison (i.e., "Abc" and "aBc" are considered to be the same).

### otSrpServerServiceGetNumberOfSubTypes

`uint16_t otSrpServerServiceGetNumberOfSubTypes(const otSrpServerService *aService)`

**Description:** Gets the number of sub-types of the service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- The number of sub-types of `aService`.

### otSrpServerServiceGetSubTypeServiceNameAt

`const char * otSrpServerServiceGetSubTypeServiceNameAt(const otSrpServerService *aService, uint16_t aIndex)`

**Description:** Gets the sub-type service name (full name) of the service at a given index.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|
|uint16_t|[in]|aIndex|The index to get.|

The full service name for a sub-type service follows "<sub-label>._sub.<service-labels>.<domain>.".

**Returns**

- A pointer to sub-type service name at `aIndex`, or `NULL` if no sub-type at this index.

### otSrpServerServiceHasSubTypeServiceName

`bool otSrpServerServiceHasSubTypeServiceName(const otSrpServerService *aService, const char *aSubTypeServiceName)`

**Description:** Indicates whether or not the service has a given sub-type.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|
|const char *|[in]|aSubTypeServiceName|The sub-type service name (full name) to check.|

DNS name matches are performed using a case-insensitive string comparison (i.e., "Abc" and "aBc" are considered to be the same).

### otSrpServerParseSubTypeServiceName

`otError otSrpServerParseSubTypeServiceName(const char *aSubTypeServiceName, char *aLabel, uint8_t aLabelSize)`

**Description:** Parses a sub-type service name (full name) and extracts the sub-type label.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const char *|[in]|aSubTypeServiceName|A sub-type service name (full name).|
|char *|[out]|aLabel|A pointer to a buffer to copy the extracted sub-type label.|
|uint8_t|[in]|aLabelSize|Maximum size of `aLabel` buffer.|

The full service name for a sub-type service follows "<sub-label>._sub.<service-labels>.<domain>.".

### otSrpServerServiceGetPort

`uint16_t otSrpServerServiceGetPort(const otSrpServerService *aService)`

**Description:** Returns the port of the service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- The port of the service.

### otSrpServerServiceGetWeight

`uint16_t otSrpServerServiceGetWeight(const otSrpServerService *aService)`

**Description:** Returns the weight of the service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- The weight of the service.

### otSrpServerServiceGetPriority

`uint16_t otSrpServerServiceGetPriority(const otSrpServerService *aService)`

**Description:** Returns the priority of the service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- The priority of the service.

### otSrpServerServiceGetTtl

`uint32_t otSrpServerServiceGetTtl(const otSrpServerService *aService)`

**Description:** Returns the TTL of the service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- The TTL of the service instance..

### otSrpServerServiceGetTxtData

`const uint8_t * otSrpServerServiceGetTxtData(const otSrpServerService *aService, uint16_t *aDataLength)`

**Description:** Returns the TXT record data of the service instance.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|
|uint16_t *|[out]|aDataLength|A pointer to return the TXT record data length. MUST NOT be NULL.|

**Returns**

- A pointer to the buffer containing the TXT record data (the TXT data length is returned in `aDataLength`).

### otSrpServerServiceGetHost

`const otSrpServerHost * otSrpServerServiceGetHost(const otSrpServerService *aService)`

**Description:** Returns the host which the service instance reside on.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP service.|

**Returns**

- A pointer to the host instance.

### otSrpServerServiceGetLeaseInfo

`void otSrpServerServiceGetLeaseInfo(const otSrpServerService *aService, otSrpServerLeaseInfo *aLeaseInfo)`

**Description:** Returns the LEASE and KEY-LEASE information of a given service.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|const [otSrpServerService](api-srp#ot-srp-server-service) *|[in]|aService|A pointer to the SRP server service.|
|[otSrpServerLeaseInfo](ot-srp-server-lease-info) *|[out]|aLeaseInfo|A pointer to where to output the LEASE and KEY-LEASE information.|