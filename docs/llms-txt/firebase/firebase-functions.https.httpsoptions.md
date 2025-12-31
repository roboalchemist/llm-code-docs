# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md.txt

# https.HttpsOptions interface

Options that can be set on an onRequest HTTPS function.

**Signature:**  

    export interface HttpsOptions extends Omit<GlobalOptions, "region" | "enforceAppCheck"> 

**Extends:** Omit\<[GlobalOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptions_interface), "region" \| "enforceAppCheck"\>

## Properties

|                                                                                       Property                                                                                       |                                                                                                                                                                                                                              Type                                                                                                                                                                                                                               |                                                                                                                                                                                                                            Description                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                                                                                                                                                                | Number of requests a function can serve at once.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [cors](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionscors)                                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\[\]\> \| boolean \| RegExp \| Array\<string \| RegExp\>                                                                            | If true, allows CORS on requests to this function. If this is a `string` or `RegExp`, allows requests from domains that match the provided value. If this is an `Array`, allows requests from domains matching at least one entry of the array. Defaults to true for [https.CallableFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablefunction.md#httpscallablefunction_interface) and false otherwise. |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                                                                                                                                                            | Fractional number of CPUs to allocate to a function.                                                                                                                                                                                                                                                                                                                                                                                                               |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                                                                                                                                                                  | Ingress settings which control where this function can be called from.                                                                                                                                                                                                                                                                                                                                                                                             |
| [invoker](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsinvoker)                                       | "public" \| "private" \| string \| string\[\]                                                                                                                                                                                                                                                                                                                                                                                                                   | Invoker to set access control on https functions.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                                                                                                                                                                        | User labels to set on the function.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                                                                                                                                                                | Max number of instances to be running in parallel.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                                          | Amount of memory to allocate to a function.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                                                                                                                                                                | Min number of actual instances to be running at a given time.                                                                                                                                                                                                                                                                                                                                                                                                      |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                                                                                                                                                            | If true, do not deploy or emulate this function.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsregion)                                         | [SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| Array\<[SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string\> \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | HTTP functions can override global options and can specify multiple regions to deploy to.                                                                                                                                                                                                                                                                                                                                                                          |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                                                                                                                                                                | Specific service account for the function to run as.                                                                                                                                                                                                                                                                                                                                                                                                               |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                                                                                                                                                                | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.                                                                                                                                                                                                                                                                                                                                                   |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                                                                                                                                                                | Connect cloud function to specified VPC connector.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.httpsoptions.md#httpshttpsoptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                                                                                                                                                              | Egress settings for VPC connector.                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## https.HttpsOptions.concurrency

Number of requests a function can serve at once.

Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## https.HttpsOptions.cors

If true, allows CORS on requests to this function. If this is a `string` or `RegExp`, allows requests from domains that match the provided value. If this is an `Array`, allows requests from domains matching at least one entry of the array. Defaults to true for [https.CallableFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.https.callablefunction.md#httpscallablefunction_interface) and false otherwise.

**Signature:**  

    cors?: string | Expression<string> | Expression<string[]> | boolean | RegExp | Array<string | RegExp>;

## https.HttpsOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## https.HttpsOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## https.HttpsOptions.invoker

Invoker to set access control on https functions.

**Signature:**  

    invoker?: "public" | "private" | string | string[];

## https.HttpsOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## https.HttpsOptions.maxInstances

Max number of instances to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## https.HttpsOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## https.HttpsOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## https.HttpsOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## https.HttpsOptions.region

HTTP functions can override global options and can specify multiple regions to deploy to.

**Signature:**  

    region?: SupportedRegion | string | Array<SupportedRegion | string> | Expression<string> | ResetValue;

## https.HttpsOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## https.HttpsOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## https.HttpsOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## https.HttpsOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## https.HttpsOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;