# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskqueueoptions.md.txt

# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md.txt

# tasks.TaskQueueOptions interface

**Signature:**  

    export interface TaskQueueOptions extends options.EventHandlerOptions 

**Extends:** [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                                           Property                                                                                           |                                                                                                                                                          Type                                                                                                                                                          |                                                                                     Description                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Number of requests a function can serve at once.                                                                                                                                     |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                   | Fractional number of CPUs to allocate to a function.                                                                                                                                 |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from.                                                                                                               |
| [invoker](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsinvoker)                                       | "private" \| string \| string\[\]                                                                                                                                                                                                                                                                                      | Who can enqueue tasks for this function. If left unspecified, only service accounts which have `roles/cloudtasks.enqueuer` and `roles/cloudfunctions.invoker` will have permissions. |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                               | User labels to set on the function.                                                                                                                                                  |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Max number of instances to be running in parallel.                                                                                                                                   |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function.                                                                                                                                          |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Min number of actual instances to be running at a given time.                                                                                                                        |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                   | If true, do not deploy or emulate this function.                                                                                                                                     |
| [rateLimits](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsratelimits)                                 | [RateLimits](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.ratelimits.md#tasksratelimits_interface)                                                                                                                                                                       | How congestion control should be applied to the function.                                                                                                                            |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsregion)                                         | [options.SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                                                                                           |
| [retry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsretry)                                           | boolean                                                                                                                                                                                                                                                                                                                | Whether failed executions should be delivered again.                                                                                                                                 |
| [retryConfig](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsretryconfig)                               | [RetryConfig](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.retryconfig.md#tasksretryconfig_interface)                                                                                                                                                                    | How a task should be retried in the event of a non-2xx return.                                                                                                                       |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                      |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Specific service account for the function to run as.                                                                                                                                 |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.                                                                     |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Connect cloud function to specified VPC connector.                                                                                                                                   |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.tasks.taskqueueoptions.md#taskstaskqueueoptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector.                                                                                                                                                   |

## tasks.TaskQueueOptions.concurrency

Number of requests a function can serve at once.

Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## tasks.TaskQueueOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## tasks.TaskQueueOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## tasks.TaskQueueOptions.invoker

Who can enqueue tasks for this function.

If left unspecified, only service accounts which have `roles/cloudtasks.enqueuer` and `roles/cloudfunctions.invoker` will have permissions.

**Signature:**  

    invoker?: "private" | string | string[];

## tasks.TaskQueueOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## tasks.TaskQueueOptions.maxInstances

Max number of instances to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## tasks.TaskQueueOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## tasks.TaskQueueOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## tasks.TaskQueueOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## tasks.TaskQueueOptions.rateLimits

How congestion control should be applied to the function.

**Signature:**  

    rateLimits?: RateLimits;

## tasks.TaskQueueOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: options.SupportedRegion | string | Expression<string> | ResetValue;

## tasks.TaskQueueOptions.retry

Whether failed executions should be delivered again.

**Signature:**  

    retry?: boolean;

## tasks.TaskQueueOptions.retryConfig

How a task should be retried in the event of a non-2xx return.

**Signature:**  

    retryConfig?: RetryConfig;

## tasks.TaskQueueOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## tasks.TaskQueueOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## tasks.TaskQueueOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## tasks.TaskQueueOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## tasks.TaskQueueOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;