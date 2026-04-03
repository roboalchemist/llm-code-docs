# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md.txt

# pubsub.PubSubOptions interface

PubSubOptions extend EventHandlerOptions but must include a topic.

**Signature:**  

    export interface PubSubOptions extends options.EventHandlerOptions 

**Extends:** [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                                         Property                                                                                         |                                                                                                                                                          Type                                                                                                                                                          |                                                   Description                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Number of requests a function can serve at once.                                                                 |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                   | Fractional number of CPUs to allocate to a function.                                                             |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from.                                           |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                               | User labels to set on the function.                                                                              |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Max number of instances to be running in parallel.                                                               |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function.                                                                      |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Min number of actual instances to be running at a given time.                                                    |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                   | If true, do not deploy or emulate this function.                                                                 |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsregion)                                         | [options.SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                       |
| [retry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsretry)                                           | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\> \| ResetValue                                                                                                                                     | Whether failed executions should be delivered again.                                                             |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                            |                                                                                                                  |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Specific service account for the function to run as.                                                             |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout. |
| [topic](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionstopic)                                           | string                                                                                                                                                                                                                                                                                                                 | The Pub/Sub topic to watch for message events                                                                    |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Connect cloud function to specified VPC connector.                                                               |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.pubsub.pubsuboptions.md#pubsubpubsuboptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector.                                                                               |

## pubsub.PubSubOptions.concurrency

Number of requests a function can serve at once.

Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## pubsub.PubSubOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## pubsub.PubSubOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## pubsub.PubSubOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## pubsub.PubSubOptions.maxInstances

Max number of instances to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## pubsub.PubSubOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## pubsub.PubSubOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## pubsub.PubSubOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## pubsub.PubSubOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: options.SupportedRegion | string | Expression<string> | ResetValue;

## pubsub.PubSubOptions.retry

Whether failed executions should be delivered again.

**Signature:**  

    retry?: boolean | Expression<boolean> | ResetValue;

## pubsub.PubSubOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## pubsub.PubSubOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## pubsub.PubSubOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## pubsub.PubSubOptions.topic

The Pub/Sub topic to watch for message events

**Signature:**  

    topic: string;

## pubsub.PubSubOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## pubsub.PubSubOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;