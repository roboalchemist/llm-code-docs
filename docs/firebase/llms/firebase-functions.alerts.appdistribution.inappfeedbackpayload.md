# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md.txt

# alerts.appDistribution.InAppFeedbackPayload interface

The internal payload object for receiving in-app feedback from a tester. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface InAppFeedbackPayload 

## Properties

|                                                                                                       Property                                                                                                        |                                             Type                                             |                                                            Description                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload%22@type%22)                   | "type.googleapis.com/google.events.firebase.firebasealerts.v1.AppDistroInAppFeedbackPayload" |                                                                                                                                   |
| [appVersion](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayloadappversion)                 | string                                                                                       | Version consisting of `versionName` and `versionCode` for Android and `CFBundleShortVersionString` and `CFBundleVersion` for iOS. |
| [feedbackConsoleUri](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayloadfeedbackconsoleuri) | string                                                                                       | Deep link back to the Firebase console.                                                                                           |
| [feedbackReport](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayloadfeedbackreport)         | string                                                                                       | Resource name. Format: `projects/{project_number}/apps/{app_id}/releases/{release_id}/feedbackReports/{feedback_id}`              |
| [screenshotUri](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayloadscreenshoturi)           | string                                                                                       | URI to download screenshot. This URI is fast expiring.                                                                            |
| [testerEmail](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayloadtesteremail)               | string                                                                                       | Email of the tester                                                                                                               |
| [testerName](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayloadtestername)                 | string                                                                                       | Name of the tester                                                                                                                |
| [text](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayloadtext)                             | string                                                                                       | Text entered by the tester                                                                                                        |

## alerts.appDistribution.InAppFeedbackPayload."@type"

**Signature:**  

```typescript

```

## alerts.appDistribution.InAppFeedbackPayload.appVersion

Version consisting of `versionName` and `versionCode` for Android and `CFBundleShortVersionString` and `CFBundleVersion` for iOS.

**Signature:**  

    appVersion: string;

## alerts.appDistribution.InAppFeedbackPayload.feedbackConsoleUri

Deep link back to the Firebase console.

**Signature:**  

    feedbackConsoleUri: string;

## alerts.appDistribution.InAppFeedbackPayload.feedbackReport

Resource name. Format: `projects/{project_number}/apps/{app_id}/releases/{release_id}/feedbackReports/{feedback_id}`

**Signature:**  

    feedbackReport: string;

## alerts.appDistribution.InAppFeedbackPayload.screenshotUri

URI to download screenshot. This URI is fast expiring.

**Signature:**  

    screenshotUri?: string;

## alerts.appDistribution.InAppFeedbackPayload.testerEmail

Email of the tester

**Signature:**  

    testerEmail: string;

## alerts.appDistribution.InAppFeedbackPayload.testerName

Name of the tester

**Signature:**  

    testerName?: string;

## alerts.appDistribution.InAppFeedbackPayload.text

Text entered by the tester

**Signature:**  

    text: string;