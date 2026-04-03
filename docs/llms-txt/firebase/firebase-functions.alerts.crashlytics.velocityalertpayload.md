# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md.txt

# alerts.crashlytics.VelocityAlertPayload interface

The internal payload object for a velocity alert. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface VelocityAlertPayload 

## Properties

|                                                                                                Property                                                                                                 |                                                                            Type                                                                            |                                                                     Description                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload%22@type%22)             | "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsVelocityAlertPayload"                                                             |                                                                                                                                                     |
| [crashCount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayloadcrashcount)           | number                                                                                                                                                     | The number of user sessions for the given app version that had this specific crash issue in the time period used to trigger the velocity alert.     |
| [crashPercentage](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayloadcrashpercentage) | number                                                                                                                                                     | The percentage of user sessions for the given app version that had this specific crash issue in the time period used to trigger the velocity alert. |
| [createTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayloadcreatetime)           | string                                                                                                                                                     | The time that the Crashlytics issue gets created                                                                                                    |
| [firstVersion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayloadfirstversion)       | string                                                                                                                                                     | The first app version where this issue was seen, and not necessarily the version that has triggered the alert.                                      |
| [issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayloadissue)                     | [Issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.issue.md#alertscrashlyticsissue_interface) | Basic information of the Crashlytics issue                                                                                                          |

## alerts.crashlytics.VelocityAlertPayload."@type"

**Signature:**  

```typescript

```

## alerts.crashlytics.VelocityAlertPayload.crashCount

The number of user sessions for the given app version that had this specific crash issue in the time period used to trigger the velocity alert.

**Signature:**  

    crashCount: number;

## alerts.crashlytics.VelocityAlertPayload.crashPercentage

The percentage of user sessions for the given app version that had this specific crash issue in the time period used to trigger the velocity alert.

**Signature:**  

    crashPercentage: number;

## alerts.crashlytics.VelocityAlertPayload.createTime

The time that the Crashlytics issue gets created

**Signature:**  

    createTime: string;

## alerts.crashlytics.VelocityAlertPayload.firstVersion

The first app version where this issue was seen, and not necessarily the version that has triggered the alert.

**Signature:**  

    firstVersion: string;

## alerts.crashlytics.VelocityAlertPayload.issue

Basic information of the Crashlytics issue

**Signature:**  

    issue: Issue;