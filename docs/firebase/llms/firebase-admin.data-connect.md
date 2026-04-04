# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.md.txt

Firebase Data Connect service.

## Functions

|                                                                      Function                                                                       |                                                                                                                                                                                                                          Description                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getDataConnect(connectorConfig, app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.md#getdataconnect_3887e80) | Gets the[DataConnect](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnect_class)service with the provided connector configuration for the default app or a given app.`getDataConnect(connectorConfig)`can be called with no app argument to access the default app's`DataConnect`service or as`getDataConnect(connectorConfig, app)`to access the`DataConnect`service associated with a specific app. |

## Classes

|                                                               Class                                                               |                 Description                 |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| [DataConnect](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnect_class) | The Firebase`DataConnect`service interface. |

## Interfaces

|                                                                                     Interface                                                                                      |                                    Description                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [ConnectorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.connectorconfig.md#connectorconfig_interface)                                  | Interface representing a Data Connect connector configuration.                     |
| [ExecuteGraphqlResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executegraphqlresponse.md#executegraphqlresponse_interface)             | Interface representing ExecuteGraphQL response.                                    |
| [ExecuteOperationResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.executeoperationresponse.md#executeoperationresponse_interface)       | Interface representing ExecuteOperation response.                                  |
| [GraphqlOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.graphqloptions.md#graphqloptions_interface)                                     | Interface representing GraphQL options for executing arbitrary GraphQL operations. |
| [ImpersonateAuthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateauthenticated.md#impersonateauthenticated_interface)       | Interface representing the impersonation of an authenticated user.                 |
| [ImpersonateUnauthenticated](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.impersonateunauthenticated.md#impersonateunauthenticated_interface) | Interface representing the impersonation of an unauthenticated user.               |
| [OperationOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.operationoptions.md#operationoptions_interface)                               | Interface representing options for executing defined operations.                   |

## Type Aliases

|                                                  Type Alias                                                   |                                                 Description                                                  |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [AuthClaims](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.md#authclaims) | Type representing the partial claims of a Firebase Auth token used to evaluate the Data Connect auth policy. |

## getDataConnect(connectorConfig, app)

Gets the[DataConnect](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnect_class)service with the provided connector configuration for the default app or a given app.

`getDataConnect(connectorConfig)`can be called with no app argument to access the default app's`DataConnect`service or as`getDataConnect(connectorConfig, app)`to access the`DataConnect`service associated with a specific app.

**Signature:**  

    export declare function getDataConnect(connectorConfig: ConnectorConfig, app?: App): DataConnect;

### Parameters

|    Parameter    |                                                                       Type                                                                        |                                                       Description                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| connectorConfig | [ConnectorConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.connectorconfig.md#connectorconfig_interface) | Connector configuration for the`DataConnect`service.                                                                    |
| app             | App                                                                                                                                               | Optional app for which to return the`DataConnect`service. If not provided, the default`DataConnect`service is returned. |

**Returns:**

[DataConnect](https://firebase.google.com/docs/reference/admin/node/firebase-admin.data-connect.dataconnect.md#dataconnect_class)

The default`DataConnect`service with the provided connector configuration if no app is provided, or the`DataConnect`service associated with the provided app.

### Example 1

    const connectorConfig: ConnectorConfig = {
     location: 'us-west2',
     serviceId: 'my-service',
     connectorName: 'my-connector',
    };

    // Get the `DataConnect` service for the default app
    const defaultDataConnect = getDataConnect(connectorConfig);

### Example 2

    // Get the `DataConnect` service for a given app
    const otherDataConnect = getDataConnect(connectorConfig, otherApp);

## AuthClaims

Type representing the partial claims of a Firebase Auth token used to evaluate the Data Connect auth policy.

**Signature:**  

    export type AuthClaims = Partial<DecodedIdToken>;