# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.performanceoptions.md.txt

# alerts.performance.PerformanceOptions interface

Configuration for app distribution functions.

**Signature:**  

    export interface PerformanceOptions extends EventHandlerOptions 

**Extends:** [EventHandlerOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptions_interface)

## Properties

|                                                                                    Property                                                                                     |  Type  |                       Description                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------------------------------------------------|
| [appId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.performanceoptions.md#alertsperformanceperformanceoptionsappid) | string | Scope the function to trigger on a specific application. |

## alerts.performance.PerformanceOptions.appId

Scope the function to trigger on a specific application.

**Signature:**  

    appId?: string;