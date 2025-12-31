# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md.txt

# alerts.crashlytics.StabilityDigestPayload interface

The internal payload object for a stability digest. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface StabilityDigestPayload 

## Properties

|                                                                                                 Property                                                                                                  |                                                                                                    Type                                                                                                     |                                               Description                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload%22@type%22)           | "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsStabilityDigestPayload"                                                                                                            |                                                                                                          |
| [digestDate](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayloaddigestdate)         | string                                                                                                                                                                                                      | The date that the digest gets created. Issues in the digest should have the same date as the digest date |
| [trendingIssues](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayloadtrendingissues) | [TrendingIssueDetails](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.trendingissuedetails.md#alertscrashlyticstrendingissuedetails_interface)\[\] | A stability digest containing several trending Crashlytics issues                                        |

## alerts.crashlytics.StabilityDigestPayload."@type"

**Signature:**  

```typescript

```

## alerts.crashlytics.StabilityDigestPayload.digestDate

The date that the digest gets created. Issues in the digest should have the same date as the digest date

**Signature:**  

    digestDate: string;

## alerts.crashlytics.StabilityDigestPayload.trendingIssues

A stability digest containing several trending Crashlytics issues

**Signature:**  

    trendingIssues: TrendingIssueDetails[];