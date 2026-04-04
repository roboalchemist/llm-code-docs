# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md.txt

# database.ReferenceOptions interface

ReferenceOptions extend EventHandlerOptions with provided ref and optional instance

**Signature:**  

    export interface ReferenceOptions<Ref extends string = string> extends options.EventHandlerOptions 

**Extends:** [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                                              Property                                                                                              |                                                                                                                                                          Type                                                                                                                                                          |                                                                                                            Description                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Number of requests a function can serve at once.                                                                                                                                                                                   |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                   | Fractional number of CPUs to allocate to a function.                                                                                                                                                                               |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from.                                                                                                                                                             |
| [instance](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsinstance)                                     | string                                                                                                                                                                                                                                                                                                                 | Specify the handler to trigger on a database instance(s). If present, this value can either be a single instance or a pattern. Examples: 'my-instance-1', 'my-instance-\*' Note: The capture syntax cannot be used for 'instance'. |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                               | User labels to set on the function.                                                                                                                                                                                                |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Max number of instances to be running in parallel.                                                                                                                                                                                 |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function.                                                                                                                                                                                        |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Min number of actual instances to be running at a given time.                                                                                                                                                                      |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                   | If true, do not deploy or emulate this function.                                                                                                                                                                                   |
| [ref](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsref)                                               | Ref                                                                                                                                                                                                                                                                                                                    | Specify the handler to trigger on a database reference(s). This value can either be a single reference or a pattern. Examples: '/foo/bar', '/foo/{bar}'                                                                            |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsregion)                                         | [options.SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                                                                                                                                         |
| [retry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsretry)                                           | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\> \| ResetValue                                                                                                                                     | Whether failed executions should be delivered again.                                                                                                                                                                               |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                    |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Specific service account for the function to run as.                                                                                                                                                                               |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.                                                                                                                   |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Connect cloud function to specified VPC connector.                                                                                                                                                                                 |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.database.referenceoptions.md#databasereferenceoptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector.                                                                                                                                                                                                 |

## database.ReferenceOptions.concurrency

Number of requests a function can serve at once.

Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## database.ReferenceOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## database.ReferenceOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## database.ReferenceOptions.instance

Specify the handler to trigger on a database instance(s). If present, this value can either be a single instance or a pattern. Examples: 'my-instance-1', 'my-instance-\*' Note: The capture syntax cannot be used for 'instance'.

**Signature:**  

    instance?: string;

## database.ReferenceOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## database.ReferenceOptions.maxInstances

Max number of instances to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## database.ReferenceOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## database.ReferenceOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## database.ReferenceOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## database.ReferenceOptions.ref

Specify the handler to trigger on a database reference(s). This value can either be a single reference or a pattern. Examples: '/foo/bar', '/foo/{bar}'

**Signature:**  

    ref: Ref;

## database.ReferenceOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: options.SupportedRegion | string | Expression<string> | ResetValue;

## database.ReferenceOptions.retry

Whether failed executions should be delivered again.

**Signature:**  

    retry?: boolean | Expression<boolean> | ResetValue;

## database.ReferenceOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## database.ReferenceOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## database.ReferenceOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## database.ReferenceOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## database.ReferenceOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;