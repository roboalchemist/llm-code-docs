# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-backbone-router.md

# Backbone Router

This module includes functions for the OpenThread Backbone Router Service.

## Modules

[otBackboneRouterConfig](ot-backbone-router-config)

[otBackboneRouterMulticastListenerInfo](ot-backbone-router-multicast-listener-info)

[otBackboneRouterNdProxyInfo](ot-backbone-router-nd-proxy-info)

## Enumerations

### otBackboneRouterState

```c
enum otBackboneRouterState {
    OT_BACKBONE_ROUTER_STATE_DISABLED = 0
    OT_BACKBONE_ROUTER_STATE_SECONDARY = 1
    OT_BACKBONE_ROUTER_STATE_PRIMARY = 2
}
```

**Description:**

Represents the Backbone Router Status.

**Enumerator:**

|   |   |
|---|---|
|OT_BACKBONE_ROUTER_STATE_DISABLED|Backbone function is disabled.|
|OT_BACKBONE_ROUTER_STATE_SECONDARY|Secondary Backbone Router.|
|OT_BACKBONE_ROUTER_STATE_PRIMARY|The Primary Backbone Router.|

### otBackboneRouterMulticastListenerEvent

```c
enum otBackboneRouterMulticastListenerEvent {
    OT_BACKBONE_ROUTER_MULTICAST_LISTENER_ADDED = 0
    OT_BACKBONE_ROUTER_MULTICAST_LISTENER_REMOVED = 1
}
```

**Description:**

Represents the Multicast Listener events.

**Enumerator:**

|   |   |
|---|---|
|OT_BACKBONE_ROUTER_MULTICAST_LISTENER_ADDED|Multicast Listener was added.|
|OT_BACKBONE_ROUTER_MULTICAST_LISTENER_REMOVED|Multicast Listener was removed or expired.|

### otBackboneRouterNdProxyEvent

```c
enum otBackboneRouterNdProxyEvent {
    OT_BACKBONE_ROUTER_NDPROXY_ADDED = 0
    OT_BACKBONE_ROUTER_NDPROXY_REMOVED = 1
    OT_BACKBONE_ROUTER_NDPROXY_RENEWED = 2
    OT_BACKBONE_ROUTER_NDPROXY_CLEARED = 3
}
```

**Description:**

Represents the ND Proxy events.

**Enumerator:**

|   |   |
|---|---|
|OT_BACKBONE_ROUTER_NDPROXY_ADDED|ND Proxy was added.|
|OT_BACKBONE_ROUTER_NDPROXY_REMOVED|ND Proxy was removed.|
|OT_BACKBONE_ROUTER_NDPROXY_RENEWED|ND Proxy was renewed.|
|OT_BACKBONE_ROUTER_NDPROXY_CLEARED|All ND Proxies were cleared.|

### otBackboneRouterDomainPrefixEvent

```c
enum otBackboneRouterDomainPrefixEvent {
    OT_BACKBONE_ROUTER_DOMAIN_PREFIX_ADDED = 0
    OT_BACKBONE_ROUTER_DOMAIN_PREFIX_REMOVED = 1
    OT_BACKBONE_ROUTER_DOMAIN_PREFIX_CHANGED = 2
}
```

**Description:**

Represents the Domain Prefix events.

**Enumerator:**

|   |   |
|---|---|
|OT_BACKBONE_ROUTER_DOMAIN_PREFIX_ADDED|Domain Prefix was added.|
|OT_BACKBONE_ROUTER_DOMAIN_PREFIX_REMOVED|Domain Prefix was removed.|
|OT_BACKBONE_ROUTER_DOMAIN_PREFIX_CHANGED|Domain Prefix was changed.|

## Typedefs

### otBackboneRouterConfig

`typedef struct otBackboneRouterConfig otBackboneRouterConfig`

**Description:**

Represents Backbone Router configuration.

### otBackboneRouterMulticastListenerCallback

`typedef void(* otBackboneRouterMulticastListenerCallback) (void *aContext, otBackboneRouterMulticastListenerEvent aEvent, const otIp6Address *aAddress)`

**Description:**

Pointer is called whenever the Multicast Listeners change.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|The user context pointer.|
||[in]|aEvent|The Multicast Listener event.|
||[in]|aAddress|The IPv6 multicast address of the Multicast Listener.|

**Details:**

### otBackboneRouterMulticastListenerIterator

`typedef uint16_t otBackboneRouterMulticastListenerIterator`

**Description:**

Used to iterate through Multicast Listeners.

### otBackboneRouterMulticastListenerInfo

`typedef struct otBackboneRouterMulticastListenerInfo otBackboneRouterMulticastListenerInfo`

**Description:**

Represents a Backbone Router Multicast Listener info.

### otBackboneRouterNdProxyCallback

`typedef void(* otBackboneRouterNdProxyCallback) (void *aContext, otBackboneRouterNdProxyEvent aEvent, const otIp6Address *aDua)`

**Description:**

Pointer is called whenever the Nd Proxy changed.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|The user context pointer.|
||[in]|aEvent|The ND Proxy event.|
||[in]|aDua|The Domain Unicast Address of the ND Proxy, or NULL if `aEvent` is `OT_BACKBONE_ROUTER_NDPROXY_CLEARED`.|

**Details:**

### otBackboneRouterNdProxyInfo

`typedef struct otBackboneRouterNdProxyInfo otBackboneRouterNdProxyInfo`

**Description:**

Represents the Backbone Router ND Proxy info.

### otBackboneRouterDomainPrefixCallback

`typedef void(* otBackboneRouterDomainPrefixCallback) (void *aContext, otBackboneRouterDomainPrefixEvent aEvent, const otIp6Prefix *aDomainPrefix)`

**Description:**

Pointer is called whenever the Domain Prefix changed.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|The user context pointer.|
||[in]|aEvent|The Domain Prefix event.|
||[in]|aDomainPrefix|The new Domain Prefix if added or changed, NULL otherwise.|

**Details:**

## Functions

### otBackboneRouterGetPrimary

`otError otBackboneRouterGetPrimary(otInstance *aInstance, otBackboneRouterConfig *aConfig)`

**Description:** Gets the Primary Backbone Router information in the Thread Network.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBackboneRouterConfig](ot-backbone-router-config) *|[out]|aConfig|A pointer to where to put Primary Backbone Router information.|

### otBackboneRouterSetEnabled

`void otBackboneRouterSetEnabled(otInstance *aInstance, bool aEnable)`

**Description:** Enables or disables Backbone functionality.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|TRUE to enable Backbone functionality, FALSE otherwise.|

If enabled, a Server Data Request message `SRV_DATA.ntf` is triggered for the attached device if there is no Backbone Router Service in the Thread Network Data.

If disabled, `SRV_DATA.ntf` is triggered if the Backbone Router is in the Primary state.

Available when `OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE` is enabled.

#### See Also

- [otBackboneRouterGetState](api-backbone-router#ot-backbone-router-get-state)
- [otBackboneRouterGetConfig](api-backbone-router#ot-backbone-router-get-config)
- [otBackboneRouterSetConfig](api-backbone-router#ot-backbone-router-set-config)
- [otBackboneRouterRegister](api-backbone-router#ot-backbone-router-register)

### otBackboneRouterGetState

`otBackboneRouterState otBackboneRouterGetState(otInstance *aInstance)`

**Description:** Gets the Backbone Router [otBackboneRouterState](api-backbone-router#ot-backbone-router-state).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

#### See Also (otBackboneRouterGetState)

- [otBackboneRouterSetEnabled](api-backbone-router#ot-backbone-router-set-enabled)
- [otBackboneRouterGetConfig](api-backbone-router#ot-backbone-router-get-config)
- [otBackboneRouterSetConfig](api-backbone-router#ot-backbone-router-set-config)
- [otBackboneRouterRegister](api-backbone-router#ot-backbone-router-register)

### otBackboneRouterGetConfig

`void otBackboneRouterGetConfig(otInstance *aInstance, otBackboneRouterConfig *aConfig)`

**Description:** Gets the local Backbone Router configuration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBackboneRouterConfig](ot-backbone-router-config) *|[out]|aConfig|A pointer where to put local Backbone Router configuration.|

Available when `OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE` is enabled.

#### See Also (otBackboneRouterGetConfig)

- [otBackboneRouterSetEnabled](api-backbone-router#ot-backbone-router-set-enabled)
- [otBackboneRouterGetState](api-backbone-router#ot-backbone-router-get-state)
- [otBackboneRouterSetConfig](api-backbone-router#ot-backbone-router-set-config)
- [otBackboneRouterRegister](api-backbone-router#ot-backbone-router-register)

### otBackboneRouterSetConfig

`otError otBackboneRouterSetConfig(otInstance *aInstance, const otBackboneRouterConfig *aConfig)`

**Description:** Sets the local Backbone Router configuration [otBackboneRouterConfig](ot-backbone-router-config).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otBackboneRouterConfig](ot-backbone-router-config) *|[in]|aConfig|A pointer to the Backbone Router configuration to take effect.|

A Server Data Request message `SRV_DATA.ntf` is initiated automatically if BBR Dataset changes for Primary Backbone Router.

Available when `OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE` is enabled.

#### See Also (otBackboneRouterSetConfig)

- [otBackboneRouterSetEnabled](api-backbone-router#ot-backbone-router-set-enabled)
- [otBackboneRouterGetState](api-backbone-router#ot-backbone-router-get-state)
- [otBackboneRouterGetConfig](api-backbone-router#ot-backbone-router-get-config)
- [otBackboneRouterRegister](api-backbone-router#ot-backbone-router-register)

### otBackboneRouterRegister

`otError otBackboneRouterRegister(otInstance *aInstance)`

**Description:** Explicitly registers local Backbone Router configuration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

A Server Data Request message `SRV_DATA.ntf` is triggered for the attached device.

Available when `OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE` is enabled.

#### See Also (otBackboneRouterRegister)

- [otBackboneRouterSetEnabled](api-backbone-router#ot-backbone-router-set-enabled)
- [otBackboneRouterGetState](api-backbone-router#ot-backbone-router-get-state)
- [otBackboneRouterGetConfig](api-backbone-router#ot-backbone-router-get-config)
- [otBackboneRouterSetConfig](api-backbone-router#ot-backbone-router-set-config)

### otBackboneRouterGetRegistrationJitter

`uint8_t otBackboneRouterGetRegistrationJitter(otInstance *aInstance)`

**Description:** Returns the Backbone Router registration jitter value.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|N/A|aInstance||

#### Returns

- The Backbone Router registration jitter value.

##### See Also (Returns)

- [otBackboneRouterSetRegistrationJitter](api-backbone-router#ot-backbone-router-set-registration-jitter)

### otBackboneRouterSetRegistrationJitter

`void otBackboneRouterSetRegistrationJitter(otInstance *aInstance, uint8_t aJitter)`

**Description:** Sets the Backbone Router registration jitter value.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|the Backbone Router registration jitter value to set.|
|uint8_t|N/A|aJitter||

#### See Also (otBackboneRouterSetRegistrationJitter)

- [otBackboneRouterGetRegistrationJitter](api-backbone-router#ot-backbone-router-get-registration-jitter)

### otBackboneRouterGetDomainPrefix

`otError otBackboneRouterGetDomainPrefix(otInstance *aInstance, otBorderRouterConfig *aConfig)`

**Description:** Gets the local Domain Prefix configuration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBorderRouterConfig](ot-border-router-config) *|[out]|aConfig|A pointer to the Domain Prefix configuration.|

### otBackboneRouterConfigNextDuaRegistrationResponse

`void otBackboneRouterConfigNextDuaRegistrationResponse(otInstance *aInstance, const otIp6InterfaceIdentifier *aMlIid, uint8_t aStatus)`

**Description:** Configures response status for next DUA registration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6InterfaceIdentifier](ot-ip6-interface-identifier) *|[in]|aMlIid|A pointer to the Mesh Local IID. If NULL, respond with `aStatus` for any coming DUA.req, otherwise only respond the one with matching `aMlIid`.|
|uint8_t|[in]|aStatus|The status to respond.|

Note: available only when `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` is enabled. Only used for test and certification.

TODO: (DUA) support coap error code and corresponding process for certification purpose.

### otBackboneRouterConfigNextMulticastListenerRegistrationResponse

`void otBackboneRouterConfigNextMulticastListenerRegistrationResponse(otInstance *aInstance, uint8_t aStatus)`

**Description:** Configures the response status for the next Multicast Listener Registration.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint8_t|[in]|aStatus|The status to respond.|

Available when `OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE`, `OPENTHREAD_CONFIG_BACKBONE_ROUTER_MULTICAST_ROUTING_ENABLE`, and `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` are enabled.

### otBackboneRouterSetMulticastListenerCallback

`void otBackboneRouterSetMulticastListenerCallback(otInstance *aInstance, otBackboneRouterMulticastListenerCallback aCallback, void *aContext)`

**Description:** Sets the Backbone Router Multicast Listener callback.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBackboneRouterMulticastListenerCallback](api-backbone-router#ot-backbone-router-multicast-listener-callback)|[in]|aCallback|A pointer to the Multicast Listener callback.|
|void *|[in]|aContext|A user context pointer.|

### otBackboneRouterMulticastListenerClear

`void otBackboneRouterMulticastListenerClear(otInstance *aInstance)`

**Description:** Clears the Multicast Listeners.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

Available when `OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE`, `OPENTHREAD_CONFIG_BACKBONE_ROUTER_MULTICAST_ROUTING_ENABLE`, and `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` are enabled.

#### See Also (otBackboneRouterMulticastListenerClear)

- [otBackboneRouterMulticastListenerAdd](api-backbone-router#ot-backbone-router-multicast-listener-add)
- [otBackboneRouterMulticastListenerGetNext](api-backbone-router#ot-backbone-router-multicast-listener-get-next)

### otBackboneRouterMulticastListenerAdd

`otError otBackboneRouterMulticastListenerAdd(otInstance *aInstance, const otIp6Address *aAddress, uint32_t aTimeout)`

**Description:** Adds a Multicast Listener with a timeout value, in seconds.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aAddress|The Multicast Listener address.|
|uint32_t|[in]|aTimeout|The timeout (in seconds) of the Multicast Listener, or 0 to use the default MLR timeout.|

Pass `0` to use the default MLR timeout.

Available when `OPENTHREAD_CONFIG_BACKBONE_ROUTER_ENABLE`, `OPENTHREAD_CONFIG_BACKBONE_ROUTER_MULTICAST_ROUTING_ENABLE`, and `OPENTHREAD_CONFIG_REFERENCE_DEVICE_ENABLE` are enabled.

#### See Also (otBackboneRouterMulticastListenerAdd)

- [otBackboneRouterMulticastListenerClear](api-backbone-router#ot-backbone-router-multicast-listener-clear)
- [otBackboneRouterMulticastListenerGetNext](api-backbone-router#ot-backbone-router-multicast-listener-get-next)

### otBackboneRouterMulticastListenerGetNext

`otError otBackboneRouterMulticastListenerGetNext(otInstance *aInstance, otBackboneRouterMulticastListenerIterator *aIterator, otBackboneRouterMulticastListenerInfo *aListenerInfo)`

**Description:** Gets the next Multicast Listener info (using an iterator).

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBackboneRouterMulticastListenerIterator](api-backbone-router#ot-backbone-router-multicast-listener-iterator) *|[inout]|aIterator|A pointer to the iterator. On success the iterator will be updated to point to next Multicast Listener. To get the first entry the iterator should be set to OT_BACKBONE_ROUTER_MULTICAST_LISTENER_ITERATOR_INIT.|
|[otBackboneRouterMulticastListenerInfo](ot-backbone-router-multicast-listener-info) *|[out]|aListenerInfo|A pointer to an `otBackboneRouterMulticastListenerInfo` where information of next Multicast Listener is placed (on success).|

#### See Also (otBackboneRouterMulticastListenerGetNext)

- [otBackboneRouterMulticastListenerClear](api-backbone-router#ot-backbone-router-multicast-listener-clear)
- [otBackboneRouterMulticastListenerAdd](api-backbone-router#ot-backbone-router-multicast-listener-add)

### otBackboneRouterSetNdProxyCallback

`void otBackboneRouterSetNdProxyCallback(otInstance *aInstance, otBackboneRouterNdProxyCallback aCallback, void *aContext)`

**Description:** Sets the Backbone Router ND Proxy callback.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBackboneRouterNdProxyCallback](api-backbone-router#ot-backbone-router-nd-proxy-callback)|[in]|aCallback|A pointer to the ND Proxy callback.|
|void *|[in]|aContext|A user context pointer.|

### otBackboneRouterGetNdProxyInfo

`otError otBackboneRouterGetNdProxyInfo(otInstance *aInstance, const otIp6Address *aDua, otBackboneRouterNdProxyInfo *aNdProxyInfo)`

**Description:** Gets the Backbone Router ND Proxy info.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aDua|The Domain Unicast Address.|
|[otBackboneRouterNdProxyInfo](ot-backbone-router-nd-proxy-info) *|[out]|aNdProxyInfo|A pointer to the ND Proxy info.|

### otBackboneRouterSetDomainPrefixCallback

`void otBackboneRouterSetDomainPrefixCallback(otInstance *aInstance, otBackboneRouterDomainPrefixCallback aCallback, void *aContext)`

**Description:** Sets the Backbone Router Domain Prefix callback.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBackboneRouterDomainPrefixCallback](api-backbone-router#ot-backbone-router-domain-prefix-callback)|[in]|aCallback|A pointer to the Domain Prefix callback.|
|void *|[in]|aContext|A user context pointer.|

## Macros

`#define OT_BACKBONE_ROUTER_MULTICAST_LISTENER_ITERATOR_INIT     0`

**Description**: Initializer for otBackboneRouterMulticastListenerIterator.
