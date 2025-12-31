# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md.txt

# identity.BlockingOptions interface

All function options plus idToken, accessToken, and refreshToken.

**Signature:**  

    export interface BlockingOptions 

## Properties

|                                                                                             Property                                                                                             |                                                                                                                                                          Type                                                                                                                                                          |                                                   Description                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [accessToken](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsaccesstoken)                               | boolean                                                                                                                                                                                                                                                                                                                | Pass the Access Token credential to the function.                                                                |
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Number of requests a function can serve at once.                                                                 |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                   | Fractional number of CPUs to allocate to a function.                                                             |
| [idToken](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsidtoken)                                       | boolean                                                                                                                                                                                                                                                                                                                | Pass the ID Token credential to the function.                                                                    |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from.                                           |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                               | User labels to set on the function.                                                                              |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Max number of instances to be running in parallel.                                                               |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function.                                                                      |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Min number of actual instances to be running at a given time.                                                    |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                   | If true, do not deploy or emulate this function.                                                                 |
| [refreshToken](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsrefreshtoken)                             | boolean                                                                                                                                                                                                                                                                                                                | Pass the Refresh Token credential to the function.                                                               |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsregion)                                         | [options.SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                       |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                            |                                                                                                                  |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Specific service account for the function to run as.                                                             |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout. |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Connect cloud function to specified VPC connector.                                                               |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.blockingoptions.md#identityblockingoptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector.                                                                               |

## identity.BlockingOptions.accessToken

Pass the Access Token credential to the function.

**Signature:**  

    accessToken?: boolean;

## identity.BlockingOptions.concurrency

Number of requests a function can serve at once.

Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## identity.BlockingOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## identity.BlockingOptions.idToken

Pass the ID Token credential to the function.

**Signature:**  

    idToken?: boolean;

## identity.BlockingOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## identity.BlockingOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## identity.BlockingOptions.maxInstances

Max number of instances to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## identity.BlockingOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## identity.BlockingOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## identity.BlockingOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## identity.BlockingOptions.refreshToken

Pass the Refresh Token credential to the function.

**Signature:**  

    refreshToken?: boolean;

## identity.BlockingOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: options.SupportedRegion | string | Expression<string> | ResetValue;

## identity.BlockingOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## identity.BlockingOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## identity.BlockingOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## identity.BlockingOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## identity.BlockingOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;