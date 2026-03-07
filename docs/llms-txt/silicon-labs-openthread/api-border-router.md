# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-border-router.md

# Border Router

This module includes functions to manage local network data with the OpenThread Border Router. 

## Typedefs

### otBorderRouterNetDataFullCallback

`typedef void(* otBorderRouterNetDataFullCallback) (void *aContext)`

**Description:**

Function pointer callback which is invoked when Network Data (local or leader) gets full.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aContext|A pointer to arbitrary context information.|

**Details:**

## Functions

### otBorderRouterGetNetData

`otError otBorderRouterGetNetData(otInstance *aInstance, bool aStable, uint8_t *aData, uint8_t *aDataLength)`

**Description:** Provides a full or stable copy of the local Thread Network Data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aStable|TRUE when copying the stable version, FALSE when copying the full version.|
|uint8_t *|[out]|aData|A pointer to the data buffer.|
|uint8_t *|[inout]|aDataLength|On entry, size of the data buffer pointed to by `aData`. On exit, number of copied bytes.|

### otBorderRouterAddOnMeshPrefix

`otError otBorderRouterAddOnMeshPrefix(otInstance *aInstance, const otBorderRouterConfig *aConfig)`

**Description:** Add a border router configuration to the local network data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otBorderRouterConfig](ot-border-router-config) *|[in]|aConfig|A pointer to the border router configuration.|

**See Also**

- [otBorderRouterRemoveOnMeshPrefix](api-border-router#ot-border-router-remove-on-mesh-prefix)
- [otBorderRouterRegister](api-border-router#ot-border-router-register)

### otBorderRouterRemoveOnMeshPrefix

`otError otBorderRouterRemoveOnMeshPrefix(otInstance *aInstance, const otIp6Prefix *aPrefix)`

**Description:** Remove a border router configuration from the local network data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Prefix](ot-ip6-prefix) *|[in]|aPrefix|A pointer to an IPv6 prefix.|

**See Also**

- [otBorderRouterAddOnMeshPrefix](api-border-router#ot-border-router-add-on-mesh-prefix)
- [otBorderRouterRegister](api-border-router#ot-border-router-register)

### otBorderRouterGetNextOnMeshPrefix

`otError otBorderRouterGetNextOnMeshPrefix(otInstance *aInstance, otNetworkDataIterator *aIterator, otBorderRouterConfig *aConfig)`

**Description:** Gets the next On Mesh Prefix in the local Network Data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otNetworkDataIterator](api-thread-general#ot-network-data-iterator) *|[inout]|aIterator|A pointer to the Network Data iterator context. To get the first on-mesh entry it should be set to OT_NETWORK_DATA_ITERATOR_INIT.|
|[otBorderRouterConfig](ot-border-router-config) *|[out]|aConfig|A pointer to the On Mesh Prefix information.|

### otBorderRouterAddRoute

`otError otBorderRouterAddRoute(otInstance *aInstance, const otExternalRouteConfig *aConfig)`

**Description:** Add an external route configuration to the local network data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExternalRouteConfig](ot-external-route-config) *|[in]|aConfig|A pointer to the external route configuration.|

**See Also**

- [otBorderRouterRemoveRoute](api-border-router#ot-border-router-remove-route)
- [otBorderRouterRegister](api-border-router#ot-border-router-register)

### otBorderRouterRemoveRoute

`otError otBorderRouterRemoveRoute(otInstance *aInstance, const otIp6Prefix *aPrefix)`

**Description:** Remove an external route configuration from the local network data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Prefix](ot-ip6-prefix) *|[in]|aPrefix|A pointer to an IPv6 prefix.|

**See Also**

- [otBorderRouterAddRoute](api-border-router#ot-border-router-add-route)
- [otBorderRouterRegister](api-border-router#ot-border-router-register)

### otBorderRouterGetNextRoute

`otError otBorderRouterGetNextRoute(otInstance *aInstance, otNetworkDataIterator *aIterator, otExternalRouteConfig *aConfig)`

**Description:** Gets the next external route in the local Network Data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otNetworkDataIterator](api-thread-general#ot-network-data-iterator) *|[inout]|aIterator|A pointer to the Network Data iterator context. To get the first external route entry it should be set to OT_NETWORK_DATA_ITERATOR_INIT.|
|[otExternalRouteConfig](ot-external-route-config) *|[out]|aConfig|A pointer to the External Route information.|

### otBorderRouterRegister

`otError otBorderRouterRegister(otInstance *aInstance)`

**Description:** Immediately register the local network data with the Leader.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**See Also**

- [otBorderRouterAddOnMeshPrefix](api-border-router#ot-border-router-add-on-mesh-prefix)
- [otBorderRouterRemoveOnMeshPrefix](api-border-router#ot-border-router-remove-on-mesh-prefix)
- [otBorderRouterAddRoute](api-border-router#ot-border-router-add-route)
- [otBorderRouterRemoveRoute](api-border-router#ot-border-router-remove-route)

### otBorderRouterSetNetDataFullCallback

`void otBorderRouterSetNetDataFullCallback(otInstance *aInstance, otBorderRouterNetDataFullCallback aCallback, void *aContext)`

**Description:** Sets the callback to indicate when Network Data gets full.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otBorderRouterNetDataFullCallback](api-border-router#ot-border-router-net-data-full-callback)|[in]|aCallback|The callback.|
|void *|[in]|aContext|A pointer to arbitrary context information used with `aCallback`.|

Requires `OPENTHREAD_CONFIG_BORDER_ROUTER_SIGNAL_NETWORK_DATA_FULL`.

The callback is invoked whenever:

- The device is acting as a leader and receives a Network Data registration from a Border Router (BR) that it cannot add to Network Data (running out of space).
- The device is acting as a BR and new entries cannot be added to its local Network Data.
- The device is acting as a BR and tries to register its local Network Data entries with the leader, but determines that its local entries will not fit.