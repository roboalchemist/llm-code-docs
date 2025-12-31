# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md.txt

# alerts.crashlytics.RegressionAlertPayload interface

The internal payload object for a regression alert. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface RegressionAlertPayload 

## Properties

|                                                                                              Property                                                                                               |                                                                            Type                                                                            |                                         Description                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload%22@type%22)     | "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsRegressionAlertPayload"                                                           |                                                                                             |
| [issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayloadissue)             | [Issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.issue.md#alertscrashlyticsissue_interface) | Basic information of the Crashlytics issue                                                  |
| [resolveTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayloadresolvetime) | string                                                                                                                                                     | The time that the Crashlytics issues was most recently resolved before it began to reoccur. |
| [type](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayloadtype)               | string                                                                                                                                                     | The type of the Crashlytics issue, e.g. new fatal, new nonfatal, ANR                        |

## alerts.crashlytics.RegressionAlertPayload."@type"

**Signature:**  

```typescript

```

## alerts.crashlytics.RegressionAlertPayload.issue

Basic information of the Crashlytics issue

**Signature:**  

    issue: Issue;

## alerts.crashlytics.RegressionAlertPayload.resolveTime

The time that the Crashlytics issues was most recently resolved before it began to reoccur.

**Signature:**  

    resolveTime: string;

## alerts.crashlytics.RegressionAlertPayload.type

The type of the Crashlytics issue, e.g. new fatal, new nonfatal, ANR

**Signature:**  

    type: string;