# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md.txt

# eventarc.EventarcTriggerOptions interface

Options that can be set on an Eventarc trigger.

**Signature:**  

    export interface EventarcTriggerOptions extends options.EventHandlerOptions 

**Extends:** [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                                                    Property                                                                                                    |                                                                                                                                                          Type                                                                                                                                                          |                                                                                                                                                                                                                                                                                    Description                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [channel](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionschannel)                                       | string                                                                                                                                                                                                                                                                                                                 | ID of the channel. Can be either: \* fully qualified channel resource name: `projects/{project}/locations/{location}/channels/{channel-id}` \* partial resource name with location and channel ID, in which case the runtime project ID of the function will be used: `locations/{location}/channels/{channel-id}` \* partial channel ID, in which case the runtime project ID of the function and `us-central1` as location will be used: `{channel-id}`If not specified, the default Firebase channel will be used: `projects/{project}/locations/us-central1/channels/firebase` |
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Number of requests a function can serve at once.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                   | Fractional number of CPUs to allocate to a function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [eventType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionseventtype)                                   | string                                                                                                                                                                                                                                                                                                                 | Type of the event to trigger on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [filters](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsfilters)                                       | Record\<string, string\>                                                                                                                                                                                                                                                                                               | Eventarc event exact match filter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                               | User labels to set on the function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Max number of instances to be running in parallel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Min number of actual instances to be running at a given time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                   | If true, do not deploy or emulate this function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsregion)                                         | [options.SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [retry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsretry)                                           | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\> \| ResetValue                                                                                                                                     | Whether failed executions should be delivered again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Specific service account for the function to run as.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Connect cloud function to specified VPC connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventarc.eventarctriggeroptions.md#eventarceventarctriggeroptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## eventarc.EventarcTriggerOptions.channel

ID of the channel. Can be either: \* fully qualified channel resource name: `projects/{project}/locations/{location}/channels/{channel-id}` \* partial resource name with location and channel ID, in which case the runtime project ID of the function will be used: `locations/{location}/channels/{channel-id}` \* partial channel ID, in which case the runtime project ID of the function and `us-central1` as location will be used: `{channel-id}`

If not specified, the default Firebase channel will be used: `projects/{project}/locations/us-central1/channels/firebase`

**Signature:**  

    channel?: string;

## eventarc.EventarcTriggerOptions.concurrency

Number of requests a function can serve at once.

Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## eventarc.EventarcTriggerOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## eventarc.EventarcTriggerOptions.eventType

Type of the event to trigger on.

**Signature:**  

    eventType: string;

## eventarc.EventarcTriggerOptions.filters

Eventarc event exact match filter.

**Signature:**  

    filters?: Record<string, string>;

## eventarc.EventarcTriggerOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## eventarc.EventarcTriggerOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## eventarc.EventarcTriggerOptions.maxInstances

Max number of instances to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## eventarc.EventarcTriggerOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## eventarc.EventarcTriggerOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## eventarc.EventarcTriggerOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## eventarc.EventarcTriggerOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: options.SupportedRegion | string | Expression<string> | ResetValue;

## eventarc.EventarcTriggerOptions.retry

Whether failed executions should be delivered again.

**Signature:**  

    retry?: boolean | Expression<boolean> | ResetValue;

## eventarc.EventarcTriggerOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## eventarc.EventarcTriggerOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## eventarc.EventarcTriggerOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## eventarc.EventarcTriggerOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## eventarc.EventarcTriggerOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;