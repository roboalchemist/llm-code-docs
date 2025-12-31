# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md.txt

# GlobalOptions interface

`GlobalOptions` are options that can be set across an entire project. These options are common to HTTPS and event handling functions.

**Signature:**  

    export interface GlobalOptions 

## Properties

|                                                                                  Property                                                                                   |                                                                                                                                                      Type                                                                                                                                                      |                                                   Description                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                               | Number of requests a function can serve at once.                                                                 |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                           | Fractional number of CPUs to allocate to a function.                                                             |
| [enforceAppCheck](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsenforceappcheck)                       | boolean                                                                                                                                                                                                                                                                                                        | Determines whether Firebase App Check is enforced. Defaults to false.                                            |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsingresssettings)                       | [IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from.                                           |
| [invoker](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsinvoker)                                       | "public" \| "private" \| string \| string\[\]                                                                                                                                                                                                                                                                  | Invoker to set access control on HTTPS functions.                                                                |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                       | User labels to set on the function.                                                                              |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                               | Max number of instances that can be running in parallel.                                                         |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsmemory)                                         | [MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function.                                                                      |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                               | Minimum number of actual instances to be running at a given time.                                                |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                           | If true, do not deploy or emulate this function.                                                                 |
| [preserveExternalChanges](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionspreserveexternalchanges)       | boolean                                                                                                                                                                                                                                                                                                        | Controls whether function configuration modified outside of function source is preserved. Defaults to false.     |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsregion)                                         | [SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                       |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                    |                                                                                                                  |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                               | Specific service account for the function to run as.                                                             |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                               | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout. |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                               | Connect a function to a specified VPC connector.                                                                 |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptionsvpcconnectoregresssettings) | [VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector.                                                                               |

## GlobalOptions.concurrency

Number of requests a function can serve at once.

Can be applied only to functions running on Cloud Functions (2nd gen)). A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## GlobalOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Cloud Functions (1st gen). To revert to the CPU amounts used in gcloud or in Cloud Functions (1st gen), set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## GlobalOptions.enforceAppCheck

Determines whether Firebase App Check is enforced. Defaults to false.

When true, requests with invalid tokens autorespond with a 401 (Unauthorized) error. When false, requests with invalid tokens set `event.app` to `undefined`.

**Signature:**  

    enforceAppCheck?: boolean;

## GlobalOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: IngressSetting | ResetValue;

## GlobalOptions.invoker

Invoker to set access control on HTTPS functions.

**Signature:**  

    invoker?: "public" | "private" | string | string[];

## GlobalOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## GlobalOptions.maxInstances

Max number of instances that can be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## GlobalOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: MemoryOption | Expression<number> | ResetValue;

## GlobalOptions.minInstances

Minimum number of actual instances to be running at a given time.

Instances are billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## GlobalOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## GlobalOptions.preserveExternalChanges

Controls whether function configuration modified outside of function source is preserved. Defaults to false.

When setting configuration available in an underlying platform that is not yet available in the Firebase SDK for Cloud Functions, we recommend setting `preserveExternalChanges` to `true`. Otherwise, when Google releases a new version of the SDK with support for the missing configuration, your function's manually configured setting may inadvertently be wiped out.

**Signature:**  

    preserveExternalChanges?: boolean;

## GlobalOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: SupportedRegion | string | Expression<string> | ResetValue;

## GlobalOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## GlobalOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## GlobalOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a 2nd gen function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes).

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## GlobalOptions.vpcConnector

Connect a function to a specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## GlobalOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: VpcEgressSetting | ResetValue;