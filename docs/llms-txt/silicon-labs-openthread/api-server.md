# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-server.md

# Server

This module includes functions to manage local network data with the OpenThread Server. 

## Functions

### otServerGetNetDataLocal

`otError otServerGetNetDataLocal(otInstance *aInstance, bool aStable, uint8_t *aData, uint8_t *aDataLength)`

**Description:** Provides a full or stable copy of the local Thread Network Data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aStable|TRUE when copying the stable version, FALSE when copying the full version.|
|uint8_t *|[out]|aData|A pointer to the data buffer.|
|uint8_t *|[inout]|aDataLength|On entry, size of the data buffer pointed to by `aData`. On exit, number of copied bytes.|

### otServerAddService

`otError otServerAddService(otInstance *aInstance, const otServiceConfig *aConfig)`

**Description:** Add a service configuration to the local network data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otServiceConfig](ot-service-config) *|[in]|aConfig|A pointer to the service configuration.|

**See Also**

- [otServerRemoveService](api-server#ot-server-remove-service)
- [otServerRegister](api-server#ot-server-register)

### otServerRemoveService

`otError otServerRemoveService(otInstance *aInstance, uint32_t aEnterpriseNumber, const uint8_t *aServiceData, uint8_t aServiceDataLength)`

**Description:** Remove a service configuration from the local network data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|uint32_t|[in]|aEnterpriseNumber|Enterprise Number of the service entry to be deleted.|
|const uint8_t *|[in]|aServiceData|A pointer to an Service Data to look for during deletion.|
|uint8_t|[in]|aServiceDataLength|The length of `aServiceData` in bytes.|

**See Also**

- [otServerAddService](api-server#ot-server-add-service)
- [otServerRegister](api-server#ot-server-register)

### otServerGetNextService

`otError otServerGetNextService(otInstance *aInstance, otNetworkDataIterator *aIterator, otServiceConfig *aConfig)`

**Description:** Gets the next service in the local Network Data.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|[otNetworkDataIterator](api-thread-general#ot-network-data-iterator) *|[inout]|aIterator|A pointer to the Network Data iterator context. To get the first service entry it should be set to OT_NETWORK_DATA_ITERATOR_INIT.|
|[otServiceConfig](ot-service-config) *|[out]|aConfig|A pointer to where the service information will be placed.|

### otServerRegister

`otError otServerRegister(otInstance *aInstance)`

**Description:** Immediately register the local network data with the Leader.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

**See Also**

- [otServerAddService](api-server#ot-server-add-service)
- [otServerRemoveService](api-server#ot-server-remove-service)