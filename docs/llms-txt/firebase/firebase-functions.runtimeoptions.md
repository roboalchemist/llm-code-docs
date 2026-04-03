# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md.txt

# RuntimeOptions interface

Configuration options for a function that applicable at runtime.

**Signature:**  

    export interface RuntimeOptions 

## Properties

|                                                                             Property                                                                             |                                                                                                                                                  Type                                                                                                                                                   |                                                 Description                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [consumeAppCheckToken](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsconsumeappchecktoken)             | boolean                                                                                                                                                                                                                                                                                                 | Determines whether Firebase App Check token is consumed on request. Defaults to false.                       |
| [enforceAppCheck](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsenforceappcheck)                       | boolean                                                                                                                                                                                                                                                                                                 | Determines whether Firebase AppCheck is enforced.                                                            |
| [failurePolicy](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsfailurepolicy)                           | [FailurePolicy](https://firebase.google.com/docs/reference/functions/firebase-functions.failurepolicy.md#failurepolicy_interface) \| boolean                                                                                                                                                            | Failure policy of the function, with boolean `true` being equivalent to providing an empty retry object.     |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsingresssettings)                       | (typeof [INGRESS_SETTINGS_OPTIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#ingress_settings_options))\[number\] \| ResetValue                                                                                                                                        | Ingress settings which control where this function can be called from.                                       |
| [invoker](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsinvoker)                                       | "public" \| "private" \| string \| string\[\]                                                                                                                                                                                                                                                           | Invoker to set access control on https functions.                                                            |
| [labels](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                | User labels to set on the function.                                                                          |
| [maxInstances](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                     | Max number of actual instances allowed to be running in parallel.                                            |
| [memory](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsmemory)                                         | (typeof [VALID_MEMORY_OPTIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#valid_memory_options))\[number\] \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue | Amount of memory to allocate to the function.                                                                |
| [minInstances](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                     | Min number of actual instances to be running at a given time.                                                |
| [preserveExternalChanges](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionspreserveexternalchanges)       | boolean                                                                                                                                                                                                                                                                                                 | Controls whether function configuration modified outside of function source is preserved. Defaults to false. |
| [secrets](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                             |                                                                                                              |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsserviceaccount)                         | "default" \| string \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                        | Specific service account for the function to run as.                                                         |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                     | Timeout for the function in seconds, possible values are 0 to 540.                                           |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                     | Connect cloud function to specified VPC connector.                                                           |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptionsvpcconnectoregresssettings) | (typeof [VPC_EGRESS_SETTINGS_OPTIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#vpc_egress_settings_options))\[number\] \| ResetValue                                                                                                                                  | Egress settings for VPC connector.                                                                           |

## RuntimeOptions.consumeAppCheckToken

Determines whether Firebase App Check token is consumed on request. Defaults to false.

Set this to true to enable the App Check replay protection feature by consuming the App Check token on callable request. Tokens that are found to be already consumed will have the `request.app.alreadyConsumed` property set to true.

Tokens are only considered to be consumed if it is sent to the App Check service by setting this option to true. Other uses of the token do not consume it.

This replay protection feature requires an additional network call to the App Check backend and forces the clients to obtain a fresh attestation from the chosen attestation providers. This can therefore negatively impact performance and can potentially deplete your attestation providers' quotas faster. Use this feature only for protecting low volume, security critical, or expensive operations.

This option does not affect the `enforceAppCheck` option. Setting the latter to true will cause the callable function to automatically respond with a 401 Unauthorized status code when the request includes an invalid App Check token. When the request includes valid but consumed App Check tokens, requests will not be automatically rejected. Instead, the `request.app.alreadyConsumed` property will be set to true and pass the execution to the handler code for making further decisions, such as requiring additional security checks or rejecting the request.

**Signature:**  

    consumeAppCheckToken?: boolean;

## RuntimeOptions.enforceAppCheck

Determines whether Firebase AppCheck is enforced.

When true, requests with invalid tokens autorespond with a 401 (Unauthorized) error. When false, requests with invalid tokens set context.app to undefiend.

**Signature:**  

    enforceAppCheck?: boolean;

## RuntimeOptions.failurePolicy

Failure policy of the function, with boolean `true` being equivalent to providing an empty retry object.

**Signature:**  

    failurePolicy?: FailurePolicy | boolean;

## RuntimeOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: (typeof INGRESS_SETTINGS_OPTIONS)[number] | ResetValue;

## RuntimeOptions.invoker

Invoker to set access control on https functions.

**Signature:**  

    invoker?: "public" | "private" | string | string[];

## RuntimeOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## RuntimeOptions.maxInstances

Max number of actual instances allowed to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## RuntimeOptions.memory

Amount of memory to allocate to the function.

**Signature:**  

    memory?: (typeof VALID_MEMORY_OPTIONS)[number] | Expression<number> | ResetValue;

## RuntimeOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## RuntimeOptions.preserveExternalChanges

Controls whether function configuration modified outside of function source is preserved. Defaults to false.

When setting configuration available in the underlying platform that is not yet available in the Firebase Functions SDK, we highly recommend setting `preserveExternalChanges` to `true`. Otherwise, when the Firebase Functions SDK releases a new version of the SDK with support for the missing configuration, your function's manually configured setting may inadvertently be wiped out.

**Signature:**  

    preserveExternalChanges?: boolean;

## RuntimeOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## RuntimeOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: "default" | string | Expression<string> | ResetValue;

## RuntimeOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540.

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## RuntimeOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## RuntimeOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: (typeof VPC_EGRESS_SETTINGS_OPTIONS)[number] | ResetValue;