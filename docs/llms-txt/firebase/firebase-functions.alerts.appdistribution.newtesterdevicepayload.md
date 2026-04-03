# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md.txt

# alerts.appDistribution.NewTesterDevicePayload interface

The internal payload object for adding a new tester device to app distribution. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface NewTesterDevicePayload 

## Properties

|                                                                                                             Property                                                                                                              |                                               Type                                                |      Description      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload%22@type%22)                           | "type.googleapis.com/google.events.firebase.firebasealerts.v1.AppDistroNewTesterIosDevicePayload" |                       |
| [testerDeviceIdentifier](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayloadtesterdeviceidentifier) | string                                                                                            | The device ID         |
| [testerDeviceModelName](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayloadtesterdevicemodelname)   | string                                                                                            | The device model name |
| [testerEmail](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayloadtesteremail)                       | string                                                                                            | Email of the tester   |
| [testerName](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayloadtestername)                         | string                                                                                            | Name of the tester    |

## alerts.appDistribution.NewTesterDevicePayload."@type"

**Signature:**  

```typescript

```

## alerts.appDistribution.NewTesterDevicePayload.testerDeviceIdentifier

The device ID

**Signature:**  

    testerDeviceIdentifier: string;

## alerts.appDistribution.NewTesterDevicePayload.testerDeviceModelName

The device model name

**Signature:**  

    testerDeviceModelName: string;

## alerts.appDistribution.NewTesterDevicePayload.testerEmail

Email of the tester

**Signature:**  

    testerEmail: string;

## alerts.appDistribution.NewTesterDevicePayload.testerName

Name of the tester

**Signature:**  

    testerName: string;