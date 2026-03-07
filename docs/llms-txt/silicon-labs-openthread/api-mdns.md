# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-mdns.md

# Multicast DNS

This module includes APIs for Multicast DNS (mDNS). 

The mDNS APIs are available when the mDNS support `OPENTHREAD_CONFIG_MULTICAST_DNS_ENABLE` is enabled and the `OPENTHREAD_CONFIG_MULTICAST_DNS_PUBLIC_API_ENABLE` is also enabled. 

## Modules

[otMdnsLocalHostAddress](ot-mdns-local-host-address)

[otMdnsCacheInfo](ot-mdns-cache-info)

## Enumerations

### otMdnsEntryState

```
enum otMdnsEntryState {
    OT_MDNS_ENTRY_STATE_PROBING
    OT_MDNS_ENTRY_STATE_REGISTERED
    OT_MDNS_ENTRY_STATE_CONFLICT
    OT_MDNS_ENTRY_STATE_REMOVING
}
```

**Description:**

Represents a host/service/key entry state.

**Enumerator:**

|   |   |
|---|---|
|OT_MDNS_ENTRY_STATE_PROBING|Probing to claim the name.|
|OT_MDNS_ENTRY_STATE_REGISTERED|Entry is successfully registered.|
|OT_MDNS_ENTRY_STATE_CONFLICT|Name conflict was detected.|
|OT_MDNS_ENTRY_STATE_REMOVING|Entry is being removed (sending "goodbye" announcements).|

## Typedefs

### otMdnsRequestId

`typedef otPlatDnssdRequestId otMdnsRequestId`

**Description:**

Represents a request ID (`uint32_t` value) for registering a host, a service, or a key service.

### otMdnsRegisterCallback

`typedef otPlatDnssdRegisterCallback otMdnsRegisterCallback`

**Description:**

Represents the callback function to report the outcome of a host, service, or key registration request.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|The OpenThread instance.|
||[in]|aRequestId|The request ID.|
||[in]|aError|Error indicating the outcome of request.|

**Details:**

The outcome of a registration request is reported back by invoking this callback with one of the following `aError` inputs:

- `OT_ERROR_NONE` indicates registration was successful.
- `OT_ERROR_DUPLICATED` indicates a name conflict while probing, i.e., name is claimed by another mDNS responder.

See `otMdnsRegisterHost()`, `otMdnsRegisterService()`, and `otMdnsRegisterKey()` for more details about when the callback will be invoked.

### otMdnsConflictCallback

`typedef void(* otMdnsConflictCallback) (otInstance *aInstance, const char *aName, const char *aServiceType)`

**Description:**

Represents the callback function to report a detected name conflict after successful registration of an entry.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aInstance|The OpenThread instance.|
||[in]|aName|The host name or the service instance label.|
||[in]|aServiceType|The service type (e.g., `_tst._udp`).|

**Details:**

If a conflict is detected while registering an entry, it is reported through the provided `otMdnsRegisterCallback`. The `otMdnsConflictCallback` is used only when a name conflict is detected after an entry has been successfully registered.

A non-NULL `aServiceType` indicates that conflict is for a service entry. In this case `aName` specifies the service instance label (treated as as a single DNS label and can potentially include dot `.` character).

A NULL `aServiceType` indicates that conflict is for a host entry. In this case `Name` specifies the host name. It does not include the domain name.

### otMdnsHost

`typedef otPlatDnssdHost otMdnsHost`

**Description:**

Represents an mDNS host.

**Details:**

This type is used to register or unregister a host (`otMdnsRegisterHost()` and `otMdnsUnregisterHost()`).

See the description of each function for more details on how different fields are used in each case.

### otMdnsService

`typedef otPlatDnssdService otMdnsService`

**Description:**

Represents an mDNS service.

**Details:**

This type is used to register or unregister a service (`otMdnsRegisterService()` and `otMdnsUnregisterService()`).

See the description of each function for more details on how different fields are used in each case.

### otMdnsKey

`typedef otPlatDnssdKey otMdnsKey`

**Description:**

Represents an mDNS key record.

**Details:**

See `otMdnsRegisterKey()`, `otMdnsUnregisterKey()` for more details about fields in each case.

### otMdnsIterator

`typedef struct otMdnsIterator otMdnsIterator`

**Description:**

Represents an mDNS entry iterator.

### otMdnsEntryState

`typedef enum otMdnsEntryState otMdnsEntryState`

**Description:**

Represents a host/service/key entry state.

### otMdnsLocalHostAddress

`typedef struct otMdnsLocalHostAddress otMdnsLocalHostAddress`

**Description:**

Represents a local host IPv4 or IPv6 address entry.

### otMdnsBrowser

`typedef otPlatDnssdBrowser otMdnsBrowser`

**Description:**

Represents a service browser.

**Details:**

Refer to `otPlatDnssdBrowser` for documentation of member fields and `otMdnsStartBrowser()` for how they are used.

### otMdnsBrowseCallback

`typedef otPlatDnssdBrowseCallback otMdnsBrowseCallback`

**Description:**

Represents the callback function pointer type used to report a browse result.

### otMdnsBrowseResult

`typedef otPlatDnssdBrowseResult otMdnsBrowseResult`

**Description:**

Represents a browse result.

### otMdnsSrvResolver

`typedef otPlatDnssdSrvResolver otMdnsSrvResolver`

**Description:**

Represents an SRV service resolver.

**Details:**

Refer to `otPlatDnssdSrvResolver` for documentation of member fields and `otMdnsStartSrvResolver()` for how they are used.

### otMdnsSrvCallback

`typedef otPlatDnssdSrvCallback otMdnsSrvCallback`

**Description:**

Represents the callback function pointer type used to report an SRV resolve result.

### otMdnsSrvResult

`typedef otPlatDnssdSrvResult otMdnsSrvResult`

**Description:**

Represents an SRV resolver result.

### otMdnsTxtResolver

`typedef otPlatDnssdTxtResolver otMdnsTxtResolver`

**Description:**

Represents a TXT service resolver.

**Details:**

Refer to `otPlatDnssdTxtResolver` for documentation of member fields and `otMdnsStartTxtResolver()` for how they are used.

### otMdnsTxtCallback

`typedef otPlatDnssdTxtCallback otMdnsTxtCallback`

**Description:**

Represents the callback function pointer type used to report a TXT resolve result.

### otMdnsTxtResult

`typedef otPlatDnssdTxtResult otMdnsTxtResult`

**Description:**

Represents a TXT resolver result.

### otMdnsAddressResolver

`typedef otPlatDnssdAddressResolver otMdnsAddressResolver`

**Description:**

Represents an address resolver.

**Details:**

Refer to `otPlatDnssdAddressResolver` for documentation of member fields and `otMdnsStartIp6AddressResolver()` or `otMdnsStartIp4AddressResolver()` for how they are used.

### otMdnsAddressCallback

`typedef otPlatDnssdAddressCallback otMdnsAddressCallback`

**Description:**

Represents the callback function pointer type use to report an IPv6/IPv4 address resolve result.

### otMdnsAddressAndTtl

`typedef otPlatDnssdAddressAndTtl otMdnsAddressAndTtl`

**Description:**

Represents a discovered host address and its TTL.

### otMdnsAddressResult

`typedef otPlatDnssdAddressResult otMdnsAddressResult`

**Description:**

Represents address resolver result.

### otMdnsRecordResult

`typedef otPlatDnssdRecordResult otMdnsRecordResult`

**Description:**

Represents a record query result.

### otMdnsRecordCallback

`typedef otPlatDnssdRecordCallback otMdnsRecordCallback`

**Description:**

Represents the callback function used to report a record querier result.

### otMdnsRecordQuerier

`typedef otPlatDnssdRecordQuerier otMdnsRecordQuerier`

**Description:**

Represents a record querier.

### otMdnsCacheInfo

`typedef struct otMdnsCacheInfo otMdnsCacheInfo`

**Description:**

Represents additional information about a browser/resolver and its cached results.

## Functions

### otMdnsSetEnabled

`otError otMdnsSetEnabled(otInstance *aInstance, bool aEnable, uint32_t aInfraIfIndex)`

**Description:** Enables or disables the mDNS module.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|bool|[in]|aEnable|Boolean to indicate whether to enable (on `TRUE`) or disable (on `FALSE`).|
|uint32_t|[in]|aInfraIfIndex|The network interface index for mDNS operation. Value is ignored when disabling|

The mDNS module should be enabled before registration any host, service, or key entries. Disabling mDNS will immediately stop all operations and any communication (multicast or unicast tx) and remove any previously registered entries without sending any "goodbye" announcements or invoking their callback. Once disabled, all currently active browsers and resolvers are stopped.

### otMdnsIsEnabled

`bool otMdnsIsEnabled(otInstance *aInstance)`

**Description:** Indicates whether the mDNS module is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

### otMdnsSetAutoEnableMode

`void otMdnsSetAutoEnableMode(otInstance *aInstance, bool aEnable)`

**Description:** Enables or disables the mDNS auto-enable mode.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|bool|[in]|aEnable|A boolean to enable or disable the auto-enable mode.|

Requires `OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE`.

When this mode is enabled, the mDNS module uses the same infrastructure network interface as the Border Routing manager. The mDNS module is then automatically enabled or disabled based on the operational state of that interface (see `otBorderRoutingInit()` and `otPlatInfraIfStateChanged()`).

It is recommended to use the auto-enable mode on Border Routers. The default state of this mode at initialization is controlled by the `OPENTHREAD_CONFIG_MULTICAST_DNS_AUTO_ENABLE_ON_INFRA_IF` configuration.

The auto-enable mode can be disabled by a call to `otMdnsSetAutoEnableMode(false)` or by an explicit call to `otMdnsSetEnabled()`. Deactivating the auto-enable mode with `otMdnsSetAutoEnableMode(false)` will not change the current operational state of the mDNS module (e.g., if it is currently enabled, it remains enabled).

### otMdnsGetAutoEnableMode

`bool otMdnsGetAutoEnableMode(otInstance *aInstance)`

**Description:** Indicates whether the auto-enable mode is enabled or disabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

Requires `OPENTHREAD_CONFIG_BORDER_ROUTING_ENABLE`.

### otMdnsSetQuestionUnicastAllowed

`void otMdnsSetQuestionUnicastAllowed(otInstance *aInstance, bool aAllow)`

**Description:** Sets whether the mDNS module is allowed to send questions requesting unicast responses referred to as "QU" questions.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|bool|[in]|aAllow|Indicates whether or not to allow "QU" questions.|

The "QU" questions request unicast responses, in contrast to "QM" questions which request multicast responses.

When allowed, the first probe will be sent as a "QU" question. This API can be used to address platform limitation where platform socket cannot accept unicast response received on mDNS port (due to it being already bound).

### otMdnsIsQuestionUnicastAllowed

`bool otMdnsIsQuestionUnicastAllowed(otInstance *aInstance)`

**Description:** Indicates whether mDNS module is allowed to send "QU" questions requesting unicast response.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

### otMdnsSetConflictCallback

`void otMdnsSetConflictCallback(otInstance *aInstance, otMdnsConflictCallback aCallback)`

**Description:** Sets the post-registration conflict callback.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsConflictCallback](api-mdns#ot-mdns-conflict-callback)|[in]|aCallback|The conflict callback.|

If a conflict is detected while registering an entry, it is reported through the provided `otMdnsRegisterCallback`. The `otMdnsConflictCallback` is used only when a name conflict is detected after an entry has been successfully registered.

`aCallback` can be set to `NULL` if not needed. Subsequent calls will replace any previously set callback.

### otMdnsGetLocalHostName

`const char * otMdnsGetLocalHostName(otInstance *aInstance)`

**Description:** Gets the local host name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

**Returns**

- The local host name.

### otMdnsSetLocalHostName

`otError otMdnsSetLocalHostName(otInstance *aInstance, const char *aName)`

**Description:** Sets the local host name.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const char *|[in]|aName|The local host name to use, can be to `NULL` to allow the mDNS module to choose the name.|

The local host name can be set only when the mDNS module is disabled. If not set the mDNS module itself will auto-generate the local host name.

### otMdnsRegisterHost

`otError otMdnsRegisterHost(otInstance *aInstance, const otMdnsHost *aHost, otMdnsRequestId aRequestId, otMdnsRegisterCallback aCallback)`

**Description:** Registers or updates a host on mDNS.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsHost](api-mdns#ot-mdns-host) *|[in]|aHost|Information about the host to register.|
|[otMdnsRequestId](api-mdns#ot-mdns-request-id)|[in]|aRequestId|The ID associated with this request.|
|[otMdnsRegisterCallback](api-mdns#ot-mdns-register-callback)|[in]|aCallback|The callback function pointer to report the outcome (can be NULL if not needed).|

The fields in `aHost` follow these rules:

- The `mHostName` field specifies the host name to register (e.g., "myhost"). MUST NOT contain the domain name.
- The `mAddresses` is array of IPv6 addresses to register with the host. `mAddressesLength` provides the number of entries in `mAddresses` array.
- The `mAddresses` array can be empty with zero `mAddressesLength`. In this case, mDNS will treat it as if host is unregistered and stops advertising any addresses for this the host name.
- The `mTtl` specifies the TTL if non-zero. If zero, the mDNS core will choose the default TTL of 120 seconds.
- Other fields in `aHost` structure are ignored in an `otMdnsRegisterHost()` call.

This function can be called again for the same `mHostName` to update a previously registered host entry, for example, to change the list of addresses of the host. In this case, the mDNS module will send "goodbye" announcements for any previously registered and now removed addresses and announce any newly added addresses.

The outcome of the registration request is reported back by invoking the provided `aCallback` with `aRequestId` as its input and one of the following `aError` inputs:

- `OT_ERROR_NONE` indicates registration was successful.
- `OT_ERROR_DULICATED` indicates a name conflict while probing, i.e., name is claimed by another mDNS responder.

For caller convenience, the OpenThread mDNS module guarantees that the callback will be invoked after this function returns, even in cases of immediate registration success. The `aCallback` can be `NULL` if caller does not want to be notified of the outcome.

### otMdnsUnregisterHost

`otError otMdnsUnregisterHost(otInstance *aInstance, const otMdnsHost *aHost)`

**Description:** Unregisters a host on mDNS.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsHost](api-mdns#ot-mdns-host) *|[in]|aHost|Information about the host to unregister.|

The fields in `aHost` follow these rules:

- The `mHostName` field specifies the host name to unregister (e.g., "myhost"). MUST NOT contain the domain name.
- Other fields in `aHost` structure are ignored in an `otMdnsUnregisterHost()` call.

If there is no previously registered host with the same name, no action is performed.

If there is a previously registered host with the same name, the mDNS module will send "goodbye" announcement for all previously advertised address records.

### otMdnsRegisterService

`otError otMdnsRegisterService(otInstance *aInstance, const otMdnsService *aService, otMdnsRequestId aRequestId, otMdnsRegisterCallback aCallback)`

**Description:** Registers or updates a service on mDNS.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsService](api-mdns#ot-mdns-service) *|[in]|aService|Information about the service to register.|
|[otMdnsRequestId](api-mdns#ot-mdns-request-id)|[in]|aRequestId|The ID associated with this request.|
|[otMdnsRegisterCallback](api-mdns#ot-mdns-register-callback)|[in]|aCallback|The callback function pointer to report the outcome (can be NULL if not needed).|

The fields in `aService` follow these rules:

- The `mServiceInstance` specifies the service instance label. It is treated as a single DNS name label. It may contain dot `.` character which is allowed in a service instance label.
- The `mServiceType` specifies the service type (e.g., "_tst._udp"). It is treated as multiple dot `.` separated labels. It MUST NOT contain the domain name.
- The `mHostName` field specifies the host name of the service if it is not NULL. Otherwise, if it is NULL, it indicates that this service is for the local host (this device itself).
- The `mSubTypeLabels` is an array of strings representing sub-types associated with the service. Each array entry is a sub-type label. The `mSubTypeLabels can be NULL if there is no sub-type. Otherwise, the array length is specified by`mSubTypeLabelsLength`.`
- `The`mTxtData`and`mTxtDataLength`specify the encoded TXT data. The`mTxtData`can be NULL or`mTxtDataLength` can be zero to specify an empty TXT data. In this case mDNS module will use a single zero byte`[ 0 ]` as the TXT data.
- The `mPort`, `mWeight`, and `mPriority` specify the service's parameters as specified in DNS SRV record.
- The `mTtl` specifies the TTL if non-zero. If zero, the mDNS module will use the default TTL of 120 seconds.
- Other fields in `aService` structure are ignored in an `otMdnsRegisterService()` call.

This function can be called again for the same `mServiceInstance` and `mServiceType` to update a previously registered service entry, for example, to change the sub-types list, or update any parameter such as port, weight, priority, TTL, or host name. The mDNS module will send announcements for any changed info, e.g., will send "goodbye" announcements for any removed sub-types and announce any newly added sub-types.

Regarding the invocation of the `aCallback`, this function behaves in the same way as described in `otMdnsRegisterHost()`.

### otMdnsUnregisterService

`otError otMdnsUnregisterService(otInstance *aInstance, const otMdnsService *aService)`

**Description:** Unregisters a service on mDNS module.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsService](api-mdns#ot-mdns-service) *|[in]|aService|Information about the service to unregister.|

The fields in `aService` follow these rules:

- The `mServiceInstance` specifies the service instance label. It is treated as a single DNS name label. It may contain dot `.` character which is allowed in a service instance label.
- The `mServiceType` specifies the service type (e.g., "_tst._udp"). It is treated as multiple dot `.` separated labels. It MUST NOT contain the domain name.
- Other fields in `aService` structure are ignored in an `otMdnsUnregisterService()` call.

If there is no previously registered service with the same name, no action is performed.

If there is a previously registered service with the same name, the mDNS module will send "goodbye" announcements for all related records.

### otMdnsRegisterKey

`otError otMdnsRegisterKey(otInstance *aInstance, const otMdnsKey *aKey, otMdnsRequestId aRequestId, otMdnsRegisterCallback aCallback)`

**Description:** Registers or updates a key record on mDNS module.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsKey](api-mdns#ot-mdns-key) *|[in]|aKey|Information about the key record to register.|
|[otMdnsRequestId](api-mdns#ot-mdns-request-id)|[in]|aRequestId|The ID associated with this request.|
|[otMdnsRegisterCallback](api-mdns#ot-mdns-register-callback)|[in]|aCallback|The callback function pointer to report the outcome (can be NULL if not needed).|

The fields in `aKey` follow these rules:

- If the key is associated with a host entry, the `mName` field specifies the host name and the `mServiceType` MUST be NULL.
- If the key is associated with a service entry, the `mName` filed specifies the service instance label (always treated as a single label) and the `mServiceType` filed specifies the service type (e.g., "_tst._udp"). In this case the DNS name for key record is `<mName>.<mServiceTye>`.
- The `mKeyData` field contains the key record's data with `mKeyDataLength` as its length in byes.
- The `mTtl` specifies the TTL if non-zero. If zero, the mDNS module will use the default TTL of 120 seconds.
- Other fields in `aKey` structure are ignored in an `otMdnsRegisterKey()` call.

This function can be called again for the same name to updated a previously registered key entry, for example, to change the key data or TTL.

Regarding the invocation of the `aCallback`, this function behaves in the same way as described in `otMdnsRegisterHost()`.

### otMdnsUnregisterKey

`otError otMdnsUnregisterKey(otInstance *aInstance, const otMdnsKey *aKey)`

**Description:** Unregisters a key record on mDNS.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsKey](api-mdns#ot-mdns-key) *|[in]|aKey|Information about the key to unregister.|

The fields in `aKey` follow these rules:

- If the key is associated with a host entry, the `mName` field specifies the host name and the `mServiceType` MUST be NULL.
- If the key is associated with a service entry, the `mName` filed specifies the service instance label (always treated as a single label) and the `mServiceType` filed specifies the service type (e.g., "_tst._udp"). In this case the DNS name for key record is `<mName>.<mServiceTye>`.
- Other fields in `aKey` structure are ignored in an `otMdnsUnregisterKey()` call.

If there is no previously registered key with the same name, no action is performed.

If there is a previously registered key with the same name, the mDNS module will send "goodbye" announcements for the key record.

### otMdnsAllocateIterator

`otMdnsIterator * otMdnsAllocateIterator(otInstance *aInstance)`

**Description:** Allocates a new iterator.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

An allocated iterator must be freed by the caller using `otMdnsFreeIterator()`.

**Returns**

- A pointer to the allocated iterator, or `NULL` if it fails to allocate.

### otMdnsFreeIterator

`void otMdnsFreeIterator(otInstance *aInstance, otMdnsIterator *aIterator)`

**Description:** Frees a previously allocated iterator.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|The iterator to free.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

### otMdnsGetNextHost

`otError otMdnsGetNextHost(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsHost *aHost, otMdnsEntryState *aState)`

**Description:** Iterates over registered host entries.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator.|
|[otMdnsHost](api-mdns#ot-mdns-host) *|[out]|aHost|Pointer to an `otMdnsHost` to return the information about the next host entry.|
|[otMdnsEntryState](api-mdns#ot-mdns-entry-state) *|[out]|aState|Pointer to an `otMdnsEntryState` to return the entry state.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aHost` is populated with information about the next host. Pointers within the `otMdnsHost` structure (like `mName`) remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextService

`otError otMdnsGetNextService(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsService *aService, otMdnsEntryState *aState)`

**Description:** Iterates over registered service entries.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator to use.|
|[otMdnsService](api-mdns#ot-mdns-service) *|[out]|aService|Pointer to an `otMdnsService` to return the information about the next service entry.|
|[otMdnsEntryState](api-mdns#ot-mdns-entry-state) *|[out]|aState|Pointer to an `otMdnsEntryState` to return the entry state.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aService` is populated with information about the next service . Pointers within the `otMdnsService` structure (like `mServiceType`, `mSubTypeLabels`) remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextKey

`otError otMdnsGetNextKey(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsKey *aKey, otMdnsEntryState *aState)`

**Description:** Iterates over registered key entries.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator to use.|
|[otMdnsKey](api-mdns#ot-mdns-key) *|[out]|aKey|Pointer to an `otMdnsKey` to return the information about the next key entry.|
|[otMdnsEntryState](api-mdns#ot-mdns-entry-state) *|[out]|aState|Pointer to an `otMdnsEntryState` to return the entry state.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aKey` is populated with information about the next key. Pointers within the `otMdnsKey` structure (like `mName`) remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextLocalHostAddress

`otError otMdnsGetNextLocalHostAddress(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsLocalHostAddress *aAddress)`

**Description:** Iterates over the local host IPv6 and IPv4 addresses tracked by OpenThread mDNS module.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[out]|aIterator|Pointer to the iterator to use.|
|[otMdnsLocalHostAddress](ot-mdns-local-host-address) *|[out]|aAddress|Pointer to an `otMdnsLocalHostAddress` to output the next address entry.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

The platform layer is responsible for monitoring and reporting all host IPv4 and IPv6 addresses to the OpenThread mDNS module, which then tracks the full address list (see `otPlatMdnsHandleHostAddressEvent()`). This function allows iteration through this tracked list, primarily intended for information and debugging purposes.

### otMdnsStartBrowser

`otError otMdnsStartBrowser(otInstance *aInstance, const otMdnsBrowser *aBrowser)`

**Description:** Starts a service browser.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsBrowser](api-mdns#ot-mdns-browser) *|[in]|aBrowser|The browser to be started.|

Initiates a continuous search for the specified `mServiceType` in `aBrowser`. For sub-type services, use `mSubTypeLabel` to define the sub-type, for base services, set `mSubTypeLabel` to NULL.

Discovered services are reported through the `mCallback` function in `aBrowser`. Services that have been removed are reported with a TTL value of zero. The callback may be invoked immediately with cached information (if available) and potentially before this function returns. When cached results are used, the reported TTL value will reflect the original TTL from the last received response.

Multiple browsers can be started for the same service, provided they use different callback functions.

### otMdnsStopBrowser

`otError otMdnsStopBrowser(otInstance *aInstance, const otMdnsBrowser *aBroswer)`

**Description:** Stops a service browser.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsBrowser](api-mdns#ot-mdns-browser) *|[in]|aBroswer|The browser to stop.|

No action is performed if no matching browser with the same service and callback is currently active.

### otMdnsStartSrvResolver

`otError otMdnsStartSrvResolver(otInstance *aInstance, const otMdnsSrvResolver *aResolver)`

**Description:** Starts an SRV record resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsSrvResolver](api-mdns#ot-mdns-srv-resolver) *|[in]|aResolver|The resolver to be started.|

Initiates a continuous SRV record resolver for the specified service in `aResolver`.

Discovered information is reported through the `mCallback` function in `aResolver`. When the service is removed it is reported with a TTL value of zero. In this case, `mHostName` may be NULL and other result fields (such as `mPort`) should be ignored.

The callback may be invoked immediately with cached information (if available) and potentially before this function returns. When cached result is used, the reported TTL value will reflect the original TTL from the last received response.

Multiple resolvers can be started for the same service, provided they use different callback functions.

### otMdnsStopSrvResolver

`otError otMdnsStopSrvResolver(otInstance *aInstance, const otMdnsSrvResolver *aResolver)`

**Description:** Stops an SRV record resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsSrvResolver](api-mdns#ot-mdns-srv-resolver) *|[in]|aResolver|The resolver to stop.|

No action is performed if no matching resolver with the same service and callback is currently active.

### otMdnsStartTxtResolver

`otError otMdnsStartTxtResolver(otInstance *aInstance, const otMdnsTxtResolver *aResolver)`

**Description:** Starts a TXT record resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsTxtResolver](api-mdns#ot-mdns-txt-resolver) *|[in]|aResolver|The resolver to be started.|

Initiates a continuous TXT record resolver for the specified service in `aResolver`.

Discovered information is reported through the `mCallback` function in `aResolver`. When the TXT record is removed it is reported with a TTL value of zero. In this case, `mTxtData` may be NULL, and other result fields (such as `mTxtDataLength`) should be ignored.

The callback may be invoked immediately with cached information (if available) and potentially before this function returns. When cached result is used, the reported TTL value will reflect the original TTL from the last received response.

Multiple resolvers can be started for the same service, provided they use different callback functions.

### otMdnsStopTxtResolver

`otError otMdnsStopTxtResolver(otInstance *aInstance, const otMdnsTxtResolver *aResolver)`

**Description:** Stops a TXT record resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsTxtResolver](api-mdns#ot-mdns-txt-resolver) *|[in]|aResolver|The resolver to stop.|

No action is performed if no matching resolver with the same service and callback is currently active.

### otMdnsStartIp6AddressResolver

`otError otMdnsStartIp6AddressResolver(otInstance *aInstance, const otMdnsAddressResolver *aResolver)`

**Description:** Starts an IPv6 address resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsAddressResolver](api-mdns#ot-mdns-address-resolver) *|[in]|aResolver|The resolver to be started.|

Initiates a continuous IPv6 address resolver for the specified host name in `aResolver`.

Discovered addresses are reported through the `mCallback` function in `aResolver`. The callback is invoked whenever addresses are added or removed, providing an updated list. If all addresses are removed, the callback is invoked with an empty list (`mAddresses` will be NULL, and `mAddressesLength` will be zero).

The callback may be invoked immediately with cached information (if available) and potentially before this function returns. When cached result is used, the reported TTL values will reflect the original TTL from the last received response.

Multiple resolvers can be started for the same host name, provided they use different callback functions.

### otMdnsStopIp6AddressResolver

`otError otMdnsStopIp6AddressResolver(otInstance *aInstance, const otMdnsAddressResolver *aResolver)`

**Description:** Stops an IPv6 address resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsAddressResolver](api-mdns#ot-mdns-address-resolver) *|[in]|aResolver|The resolver to stop.|

No action is performed if no matching resolver with the same host name and callback is currently active.

### otMdnsStartIp4AddressResolver

`otError otMdnsStartIp4AddressResolver(otInstance *aInstance, const otMdnsAddressResolver *aResolver)`

**Description:** Starts an IPv4 address resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsAddressResolver](api-mdns#ot-mdns-address-resolver) *|[in]|aResolver|The resolver to be started.|

Initiates a continuous IPv4 address resolver for the specified host name in `aResolver`.

Discovered addresses are reported through the `mCallback` function in `aResolver`. The IPv4 addresses are represented using the IPv4-mapped IPv6 address format in `mAddresses` array. The callback is invoked whenever addresses are added or removed, providing an updated list. If all addresses are removed, the callback is invoked with an empty list (`mAddresses` will be NULL, and `mAddressesLength` will be zero).

The callback may be invoked immediately with cached information (if available) and potentially before this function returns. When cached result is used, the reported TTL values will reflect the original TTL from the last received response.

Multiple resolvers can be started for the same host name, provided they use different callback functions.

### otMdnsStopIp4AddressResolver

`otError otMdnsStopIp4AddressResolver(otInstance *aInstance, const otMdnsAddressResolver *aResolver)`

**Description:** Stops an IPv4 address resolver.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsAddressResolver](api-mdns#ot-mdns-address-resolver) *|[in]|aResolver|The resolver to stop.|

No action is performed if no matching resolver with the same host name and callback is currently active.

### otMdnsStartRecordQuerier

`otError otMdnsStartRecordQuerier(otInstance *aInstance, const otMdnsRecordQuerier *aQuerier)`

**Description:** Starts a record querier.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsRecordQuerier](api-mdns#ot-mdns-record-querier) *|[in]|aQuerier|The record querier to be started.|

Initiates a continuous query for a given `mRecordType` as specified in `aQuerier`. The queried name is specified by the combination of `mFirstLabel` and `mNextLabels` (optional rest of the labels) in `aQuerier`. The `mFirstLabel` MUST be non-NULL but `mNextLabels` can be `NULL` if there are no other labels. The `mNextLabels` MUST NOT include the domain name. The reason for a separate first label is to allow it to include a dot `.` character (as allowed for service instance labels).

Discovered results are reported through the `mCallback` function in `aQuerier`, providing the record data bytes (RDATA). For NS, CNAME, SOA, PTR, MX, RP, AFSDB, RT, PX, SRV, KX, DNAME, and NSEC record types, the RDATA format contains one or more DNS names (which may use DNS name compression). For the above list, the reported record data bytes via `mCallback` will be decompressed to contain the full DNS name(s). For all other record types, the record data bytes are provided exactly as they appear in the received mDNS response. This aligns the implementation with RFC 6762 (section 18.14) regarding the use of name compression.

A removed record data is indicated with a TTL value of zero. The callback may be invoked immediately with cached information (if available) and potentially before this function returns. When cached results are used, the reported TTL value will reflect the original TTL from the last received response.

Multiple querier instances can be started for the same name, provided they use different callback functions.

The record querier MUST not be used for record types PTR, SRV, TXT, A, and AAAA. Otherwise, `OT_ERROR_INVALID_ARGS` will be returned. For these, browsers/resolvers can be used. This design is intentional to enable the implementation of an "opportunistic cache mechanism", where, depending on currently active service browsers/resolvers, the mDNS implementation will also monitor and cache related records (e.g., when a service is resolved, the address records associated with its host name are cached even if there is no active address resolver for this hostname).

The `aQuerier` and all its contained information (strings) are only valid during this call. The platform MUST save a copy of the information if it wants to retain the information after returning from this function.

### otMdnsStopRecordQuerier

`otError otMdnsStopRecordQuerier(otInstance *aInstance, const otMdnsRecordQuerier *aQuerier)`

**Description:** Stops a record querier.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|const [otMdnsRecordQuerier](api-mdns#ot-mdns-record-querier) *|[in]|aQuerier|The record querier to be stopped.|

No action is performed if no matching querier with the same name and callback is currently active.

The `aQuerier` and all its contained information (strings) are only valid during this call. The platform MUST save a copy of the information if it wants to retain the information after returning from this function.

### otMdnsGetNextBrowser

`otError otMdnsGetNextBrowser(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsBrowser *aBrowser, otMdnsCacheInfo *aInfo)`

**Description:** Iterates over browsers.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator.|
|[otMdnsBrowser](api-mdns#ot-mdns-browser) *|[out]|aBrowser|Pointer to an `otMdnsBrowser` to return the information about the next browser.|
|[otMdnsCacheInfo](ot-mdns-cache-info) *|[out]|aInfo|Pointer to an `otMdnsCacheInfo` to return additional information.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aBrowser` is populated with information about the next browser. The `mCallback` field is always set to `NULL` as there may be multiple active browsers with different callbacks. Other pointers within the `otMdnsBrowser` structure remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextSrvResolver

`otError otMdnsGetNextSrvResolver(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsSrvResolver *aResolver, otMdnsCacheInfo *aInfo)`

**Description:** Iterates over SRV resolvers.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator.|
|[otMdnsSrvResolver](api-mdns#ot-mdns-srv-resolver) *|[out]|aResolver|Pointer to an `otMdnsSrvResolver` to return the information about the next resolver.|
|[otMdnsCacheInfo](ot-mdns-cache-info) *|[out]|aInfo|Pointer to an `otMdnsCacheInfo` to return additional information.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aResolver` is populated with information about the next resolver. The `mCallback` field is always set to `NULL` as there may be multiple active resolvers with different callbacks. Other pointers within the `otMdnsSrvResolver` structure remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextTxtResolver

`otError otMdnsGetNextTxtResolver(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsTxtResolver *aResolver, otMdnsCacheInfo *aInfo)`

**Description:** Iterates over TXT resolvers.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator.|
|[otMdnsTxtResolver](api-mdns#ot-mdns-txt-resolver) *|[out]|aResolver|Pointer to an `otMdnsTxtResolver` to return the information about the next resolver.|
|[otMdnsCacheInfo](ot-mdns-cache-info) *|[out]|aInfo|Pointer to an `otMdnsCacheInfo` to return additional information.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aResolver` is populated with information about the next resolver. The `mCallback` field is always set to `NULL` as there may be multiple active resolvers with different callbacks. Other pointers within the `otMdnsTxtResolver` structure remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextIp6AddressResolver

`otError otMdnsGetNextIp6AddressResolver(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsAddressResolver *aResolver, otMdnsCacheInfo *aInfo)`

**Description:** Iterates over IPv6 address resolvers.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator.|
|[otMdnsAddressResolver](api-mdns#ot-mdns-address-resolver) *|[out]|aResolver|Pointer to an `otMdnsAddressResolver` to return the information about the next resolver.|
|[otMdnsCacheInfo](ot-mdns-cache-info) *|[out]|aInfo|Pointer to an `otMdnsCacheInfo` to return additional information.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aResolver` is populated with information about the next resolver. The `mCallback` field is always set to `NULL` as there may be multiple active resolvers with different callbacks. Other pointers within the `otMdnsAddressResolver` structure remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextIp4AddressResolver

`otError otMdnsGetNextIp4AddressResolver(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsAddressResolver *aResolver, otMdnsCacheInfo *aInfo)`

**Description:** Iterates over IPv4 address resolvers.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator.|
|[otMdnsAddressResolver](api-mdns#ot-mdns-address-resolver) *|[out]|aResolver|Pointer to an `otMdnsAddressResolver` to return the information about the next resolver.|
|[otMdnsCacheInfo](ot-mdns-cache-info) *|[out]|aInfo|Pointer to an `otMdnsCacheInfo` to return additional information.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aResolver` is populated with information about the next resolver. The `mCallback` field is always set to `NULL` as there may be multiple active resolvers with different callbacks. Other pointers within the `otMdnsAddressResolver` structure remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsGetNextRecordQuerier

`otError otMdnsGetNextRecordQuerier(otInstance *aInstance, otMdnsIterator *aIterator, otMdnsRecordQuerier *aQuerier, otMdnsCacheInfo *aInfo)`

**Description:** Iterates over record querier entries.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|The OpenThread instance.|
|[otMdnsIterator](api-mdns#ot-mdns-iterator) *|[in]|aIterator|Pointer to the iterator.|
|[otMdnsRecordQuerier](api-mdns#ot-mdns-record-querier) *|[out]|aQuerier|Pointer to an `otMdnsRecordQuerier` to return the information about the next one.|
|[otMdnsCacheInfo](ot-mdns-cache-info) *|[out]|aInfo|Pointer to an `otMdnsCacheInfo` to return additional information.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_ENTRY_ITERATION_API_ENABLE`.

On success, `aQuerier` is populated with information about the next querier . The `mCallback` field is always set to `NULL` as there may be multiple active querier with different callbacks. Other pointers within the `otMdnsRecordQuerier` structure remain valid until the next call to any OpenThread stack's public or platform API/callback.

### otMdnsSetVerboseLoggingEnabled

`void otMdnsSetVerboseLoggingEnabled(otInstance *aInstance, bool aEnable)`

**Description:** Enables or disables verbose logging for the mDNS module at run-time.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|TRUE to enable verbose logging, FALSE to disable.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_VERBOSE_LOGGING_ENABLE`.

The initial state of verbose logging (enabled or disabled at startup) is determined by the configuration `OPENTHREAD_CONFIG_MULTICAST_DEFAULT_DNS_VERBOSE_LOGGING_STATE`.

When enabled, the mDNS module emits verbose logs for every sent or received mDNS message, including the header and all question and resource records. These logs are generated regardless of the current log level configured on the device.

This feature can generate a large volume of logs, so its use is recommended only during development, integration, or debugging.

### otMdnsIsVerboseLoggingEnabled

`bool otMdnsIsVerboseLoggingEnabled(otInstance *aInstance)`

**Description:** Indicates whether verbose logging is enabled for the mDNS module.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Requires `OPENTHREAD_CONFIG_MULTICAST_DNS_VERBOSE_LOGGING_ENABLE`.