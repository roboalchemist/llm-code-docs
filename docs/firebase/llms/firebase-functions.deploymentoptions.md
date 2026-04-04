# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md.txt

# DeploymentOptions interface

Configuration options for a function that applies during function deployment.

**Signature:**  

    export interface DeploymentOptions extends RuntimeOptions 

**Extends:** [RuntimeOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.runtimeoptions.md#runtimeoptions_interface)

## Properties

|                                                              Property                                                              |                                                                                                                                                         Type                                                                                                                                                         |                   Description                    |
|------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [omit](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptionsomit)         | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\>                                                                                                                                                              | If true, do not deploy or emulate this function. |
| [regions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptionsregions)   | Array\<(typeof [SUPPORTED_REGIONS](https://firebase.google.com/docs/reference/functions/firebase-functions.md#supported_regions))\[number\] \| string \| [Expression](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue\> | Regions where function should be deployed.       |
| [schedule](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptionsschedule) | [Schedule](https://firebase.google.com/docs/reference/functions/firebase-functions.schedule.md#schedule_interface)                                                                                                                                                                                                   | Schedule for the scheduled function.             |

## DeploymentOptions.omit

If true, do not deploy or emulate this function.

**Signature:**  

    omit?: boolean | Expression<boolean>;

## DeploymentOptions.regions

Regions where function should be deployed.

**Signature:**  

    regions?: Array<(typeof SUPPORTED_REGIONS)[number] | string | Expression<string> | ResetValue>;

## DeploymentOptions.schedule

Schedule for the scheduled function.

**Signature:**  

    schedule?: Schedule;