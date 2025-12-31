# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md.txt

# alerts.appDistribution.AppDistributionOptions interface

Configuration for app distribution functions.

**Signature:**  

    export interface AppDistributionOptions extends options.EventHandlerOptions 

**Extends:** [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                                                                 Property                                                                                                                  |                                                                                                                                                          Type                                                                                                                                                          |                                                   Description                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [appId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsappid)                                           | string                                                                                                                                                                                                                                                                                                                 | Scope the function to trigger on a specific application.                                                         |
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Number of requests a function can serve at once.                                                                 |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                   | Fractional number of CPUs to allocate to a function.                                                             |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from.                                           |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                               | User labels to set on the function.                                                                              |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Max number of instances to be running in parallel.                                                               |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function.                                                                      |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Min number of actual instances to be running at a given time.                                                    |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                   | If true, do not deploy or emulate this function.                                                                 |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsregion)                                         | [options.SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                       |
| [retry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsretry)                                           | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\> \| ResetValue                                                                                                                                     | Whether failed executions should be delivered again.                                                             |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                            |                                                                                                                  |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Specific service account for the function to run as.                                                             |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout. |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Connect cloud function to specified VPC connector.                                                               |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector.                                                                               |

## alerts.appDistribution.AppDistributionOptions.appId

Scope the function to trigger on a specific application.

**Signature:**  

    appId?: string;

## alerts.appDistribution.AppDistributionOptions.concurrency

Number of requests a function can serve at once.

Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.cpu

Fractional number of CPUs to allocate to a function.

Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## alerts.appDistribution.AppDistributionOptions.ingressSettings

Ingress settings which control where this function can be called from.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## alerts.appDistribution.AppDistributionOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## alerts.appDistribution.AppDistributionOptions.maxInstances

Max number of instances to be running in parallel.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.memory

Amount of memory to allocate to a function.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.minInstances

Min number of actual instances to be running at a given time.

Instances will be billed for memory allocation and 10% of CPU allocation while idle.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## alerts.appDistribution.AppDistributionOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: options.SupportedRegion | string | Expression<string> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.retry

Whether failed executions should be delivered again.

**Signature:**  

    retry?: boolean | Expression<boolean> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## alerts.appDistribution.AppDistributionOptions.serviceAccount

Specific service account for the function to run as.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout.

The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.vpcConnector

Connect cloud function to specified VPC connector.

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## alerts.appDistribution.AppDistributionOptions.vpcConnectorEgressSettings

Egress settings for VPC connector.

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;