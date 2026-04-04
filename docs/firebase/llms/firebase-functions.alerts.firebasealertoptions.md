# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md.txt

# alerts.FirebaseAlertOptions interface

Configuration for Firebase Alert functions.

**Signature:**  

    export interface FirebaseAlertOptions extends options.EventHandlerOptions 

**Extends:** [options.EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                                                Property                                                                                                |                                                                                                                                                          Type                                                                                                                                                          |                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [alertType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsalerttype)                                   | [AlertType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.md#alertsalerttype)                                                                                                                                                                                            | Scope the handler to trigger on an alert type.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [appId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsappid)                                           | string                                                                                                                                                                                                                                                                                                                 | Scope the function to trigger on a specific application.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [concurrency](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsconcurrency)                               | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Number of requests a function can serve at once. Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.                                                                                                                                                                     |
| [cpu](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionscpu)                                               | number \| "gcf_gen1"                                                                                                                                                                                                                                                                                                   | Fractional number of CPUs to allocate to a function. Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"                                                                              |
| [ingressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsingresssettings)                       | [options.IngressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#ingresssetting) \| ResetValue                                                                                                                                                                         | Ingress settings which control where this function can be called from. A value of null turns off ingress settings.                                                                                                                                                                                                                                                                                                                                                                               |
| [labels](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionslabels)                                         | Record\<string, string\>                                                                                                                                                                                                                                                                                               | User labels to set on the function.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [maxInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsmaxinstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Max number of instances to be running in parallel. A value of null restores the default max instances.                                                                                                                                                                                                                                                                                                                                                                                           |
| [memory](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsmemory)                                         | [options.MemoryOption](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#memoryoption) \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                 | Amount of memory to allocate to a function. A value of null restores the defaults of 256MB.                                                                                                                                                                                                                                                                                                                                                                                                      |
| [minInstances](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsmininstances)                             | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Min number of actual instances to be running at a given time. Instances will be billed for memory allocation and 10% of CPU allocation while idle. A value of null restores the default min instances.                                                                                                                                                                                                                                                                                           |
| [omit](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsomit)                                             | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                   | If true, do not deploy or emulate this function.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsregion)                                         | [options.SupportedRegion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#supportedregion) \| string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue | Region where functions should be deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [retry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsretry)                                           | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\> \| ResetValue                                                                                                                                     | Whether failed executions should be delivered again.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [secrets](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionssecrets)                                       | (string \| SecretParam)\[\]                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsserviceaccount)                         | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Specific service account for the function to run as. A value of null restores the default service account.                                                                                                                                                                                                                                                                                                                                                                                       |
| [timeoutSeconds](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionstimeoutseconds)                         | number \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<number\> \| ResetValue                                                                                                                                       | Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout. A value of null restores the default of 60s The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes) |
| [vpcConnector](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsvpcconnector)                             | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue                                                                                                                                       | Connect cloud function to specified VPC connector. A value of null removes the VPC connector                                                                                                                                                                                                                                                                                                                                                                                                     |
| [vpcConnectorEgressSettings](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptionsvpcconnectoregresssettings) | [options.VpcEgressSetting](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.md#vpcegresssetting) \| ResetValue                                                                                                                                                                     | Egress settings for VPC connector. A value of null turns off VPC connector egress settings                                                                                                                                                                                                                                                                                                                                                                                                       |

## alerts.FirebaseAlertOptions.alertType

Scope the handler to trigger on an alert type.

**Signature:**  

    alertType: AlertType;

## alerts.FirebaseAlertOptions.appId

Scope the function to trigger on a specific application.

**Signature:**  

    appId?: string;

## alerts.FirebaseAlertOptions.concurrency

Number of requests a function can serve at once. Can only be applied to functions running on Cloud Functions v2. A value of null restores the default concurrency (80 when CPU \>= 1, 1 otherwise). Concurrency cannot be set to any value other than 1 if `cpu` is less than 1. The maximum value for concurrency is 1,000.

**Signature:**  

    concurrency?: number | Expression<number> | ResetValue;

## alerts.FirebaseAlertOptions.cpu

Fractional number of CPUs to allocate to a function. Defaults to 1 for functions with \<= 2GB RAM and increases for larger memory sizes. This is different from the defaults when using the gcloud utility and is different from the fixed amount assigned in Google Cloud Functions generation 1. To revert to the CPU amounts used in gcloud or in Cloud Functions generation 1, set this to the value "gcf_gen1"

**Signature:**  

    cpu?: number | "gcf_gen1";

## alerts.FirebaseAlertOptions.ingressSettings

Ingress settings which control where this function can be called from. A value of null turns off ingress settings.

**Signature:**  

    ingressSettings?: options.IngressSetting | ResetValue;

## alerts.FirebaseAlertOptions.labels

User labels to set on the function.

**Signature:**  

    labels?: Record<string, string>;

## alerts.FirebaseAlertOptions.maxInstances

Max number of instances to be running in parallel. A value of null restores the default max instances.

**Signature:**  

    maxInstances?: number | Expression<number> | ResetValue;

## alerts.FirebaseAlertOptions.memory

Amount of memory to allocate to a function. A value of null restores the defaults of 256MB.

**Signature:**  

    memory?: options.MemoryOption | Expression<number> | ResetValue;

## alerts.FirebaseAlertOptions.minInstances

Min number of actual instances to be running at a given time. Instances will be billed for memory allocation and 10% of CPU allocation while idle. A value of null restores the default min instances.

**Signature:**  

    minInstances?: number | Expression<number> | ResetValue;

## alerts.FirebaseAlertOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## alerts.FirebaseAlertOptions.region

Region where functions should be deployed.

**Signature:**  

    region?: options.SupportedRegion | string | Expression<string> | ResetValue;

## alerts.FirebaseAlertOptions.retry

Whether failed executions should be delivered again.

**Signature:**  

    retry?: boolean | Expression<boolean> | ResetValue;

## alerts.FirebaseAlertOptions.secrets

**Signature:**  

    secrets?: (string | SecretParam)[];

## alerts.FirebaseAlertOptions.serviceAccount

Specific service account for the function to run as. A value of null restores the default service account.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;

## alerts.FirebaseAlertOptions.timeoutSeconds

Timeout for the function in seconds, possible values are 0 to 540. HTTPS functions can specify a higher timeout. A value of null restores the default of 60s The minimum timeout for a gen 2 function is 1s. The maximum timeout for a function depends on the type of function: Event handling functions have a maximum timeout of 540s (9 minutes). HTTPS and callable functions have a maximum timeout of 3,600s (1 hour). Task queue functions have a maximum timeout of 1,800s (30 minutes)

**Signature:**  

    timeoutSeconds?: number | Expression<number> | ResetValue;

## alerts.FirebaseAlertOptions.vpcConnector

Connect cloud function to specified VPC connector. A value of null removes the VPC connector

**Signature:**  

    vpcConnector?: string | Expression<string> | ResetValue;

## alerts.FirebaseAlertOptions.vpcConnectorEgressSettings

Egress settings for VPC connector. A value of null turns off VPC connector egress settings

**Signature:**  

    vpcConnectorEgressSettings?: options.VpcEgressSetting | ResetValue;