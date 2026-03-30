# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.operationoptions.md.txt

# dataconnect.OperationOptions interface

OperationOptions extend EventHandlerOptions with a provided service, connector, and operation.

**Signature:**

    export interface OperationOptions<Service extends string = string, Connector extends string = string, Operation extends string = string> extends EventHandlerOptions 

**Extends:** [EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

| Property | Type | Description |
|---|---|---|
| [connector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.operationoptions.md#dataconnectoperationoptionsconnector) | Connector | Firebase Data Connect connector ID |
| [operation](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.operationoptions.md#dataconnectoperationoptionsoperation) | Operation | Name of the operation |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.operationoptions.md#dataconnectoperationoptionsregion) | [SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed. Defaults to us-central1. |
| [service](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.dataconnect.operationoptions.md#dataconnectoperationoptionsservice) | Service | Firebase Data Connect service ID |

## dataconnect.OperationOptions.connector

Firebase Data Connect connector ID

**Signature:**

    connector?: Connector;

## dataconnect.OperationOptions.operation

Name of the operation

**Signature:**

    operation?: Operation;

## dataconnect.OperationOptions.region

Region where functions should be deployed. Defaults to us-central1.

**Signature:**

    region?: SupportedRegion | string | Expression<string> | ResetValue;

## dataconnect.OperationOptions.service

Firebase Data Connect service ID

**Signature:**

    service?: Service;