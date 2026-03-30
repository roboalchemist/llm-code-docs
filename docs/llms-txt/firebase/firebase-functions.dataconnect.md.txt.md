# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md.txt

# dataconnect namespace

## Functions

| Function | Description |
|---|---|
| [onMutationExecuted(mutation, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectonmutationexecuted) | Event handler that triggers when a mutation is executed in Firebase Data Connect. |
| [onMutationExecuted(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectonmutationexecuted) | Event handler that triggers when a mutation is executed in Firebase Data Connect. |

## Interfaces

| Interface | Description |
|---|---|
| [DataConnectEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnectevent_interface) |   |
| [GraphqlError](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.graphqlerror.md#dataconnectgraphqlerror_interface) |   |
| [GraphqlErrorExtensions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.graphqlerrorextensions.md#dataconnectgraphqlerrorextensions_interface) |   |
| [MutationEventData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.mutationeventdata.md#dataconnectmutationeventdata_interface) |   |
| [OperationOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.operationoptions.md#dataconnectoperationoptions_interface) | OperationOptions extend EventHandlerOptions with a provided service, connector, and operation. |
| [RawDataConnectEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawdataconnectevent.md#dataconnectrawdataconnectevent_interface) |   |
| [RawMutation](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.rawmutation.md#dataconnectrawmutation_interface) |   |
| [SourceLocation](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.sourcelocation.md#dataconnectsourcelocation_interface) |   |

## Type Aliases

| Type Alias | Description |
|---|---|
| [AuthType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectauthtype) | AuthType defines the possible values for the authType field in a Firebase Data Connect event. - app_user: an end user of an application.. - admin: an admin user of an application. In the context of impersonate endpoints used by the admin SDK, the impersonator. - unknown: a general type to capture all other principals not captured in the other auth types. |
| [DataConnectParams](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectdataconnectparams) |   |

## dataconnect.onMutationExecuted()

Event handler that triggers when a mutation is executed in Firebase Data Connect.

**Signature:**

    export declare function onMutationExecuted<Mutation extends string, Variables = unknown, ResponseData = unknown>(mutation: Mutation, handler: (event: DataConnectEvent<MutationEventData<Variables, ResponseData>, DataConnectParams<Mutation>>) => unknown | Promise<unknown>): CloudFunction<DataConnectEvent<MutationEventData<Variables, ResponseData>, DataConnectParams<Mutation>>>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| mutation | Mutation | The mutation path to trigger on. |
| handler | (event: [DataConnectEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnectevent_interface)\<[MutationEventData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.mutationeventdata.md#dataconnectmutationeventdata_interface)\<Variables, ResponseData\>, [DataConnectParams](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectdataconnectparams)\<Mutation\>\>) =\> unknown \| Promise\<unknown\> | Event handler which is run every time a mutation is executed. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DataConnectEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnectevent_interface)\<[MutationEventData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.mutationeventdata.md#dataconnectmutationeventdata_interface)\<Variables, ResponseData\>, [DataConnectParams](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectdataconnectparams)\<Mutation\>\>\>

## dataconnect.onMutationExecuted()

Event handler that triggers when a mutation is executed in Firebase Data Connect.

**Signature:**

    export declare function onMutationExecuted<Options extends OperationOptions, Variables = unknown, ResponseData = unknown>(opts: Options, handler: (event: DataConnectEvent<MutationEventData<Variables, ResponseData>, DataConnectParams<Options>>) => unknown | Promise<unknown>): CloudFunction<DataConnectEvent<MutationEventData<Variables, ResponseData>, DataConnectParams<Options>>>;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| opts | Options | Options that can be set on an individual event-handling function. |
| handler | (event: [DataConnectEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnectevent_interface)\<[MutationEventData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.mutationeventdata.md#dataconnectmutationeventdata_interface)\<Variables, ResponseData\>, [DataConnectParams](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectdataconnectparams)\<Options\>\>) =\> unknown \| Promise\<unknown\> | Event handler which is run every time a mutation is executed. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[DataConnectEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.dataconnectevent.md#dataconnectdataconnectevent_interface)\<[MutationEventData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.mutationeventdata.md#dataconnectmutationeventdata_interface)\<Variables, ResponseData\>, [DataConnectParams](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.md#dataconnectdataconnectparams)\<Options\>\>\>

## dataconnect.AuthType

AuthType defines the possible values for the authType field in a Firebase Data Connect event. - app_user: an end user of an application.. - admin: an admin user of an application. In the context of impersonate endpoints used by the admin SDK, the impersonator. - unknown: a general type to capture all other principals not captured in the other auth types.

**Signature:**

    export type AuthType = "app_user" | "admin" | "unknown";

## dataconnect.DataConnectParams

**Signature:**

    export type DataConnectParams<PathPatternOrOptions extends string | OperationOptions> = PathPatternOrOptions extends string ? ParamsOf<PathPatternOrOptions> : PathPatternOrOptions extends OperationOptions<infer Service extends string, infer Connector extends string, infer Operation extends string> ? Record<VarName<Service> | VarName<Connector> | VarName<Operation>, string> : never;