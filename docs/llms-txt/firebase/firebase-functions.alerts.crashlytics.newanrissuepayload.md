# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md.txt

# alerts.crashlytics.NewAnrIssuePayload interface

The internal payload object for a new Application Not Responding issue. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface NewAnrIssuePayload 

## Properties

|                                                                                        Property                                                                                         |                                                                            Type                                                                            |                Description                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload%22@type%22) | "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsNewAnrIssuePayload"                                                               |                                            |
| [issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayloadissue)         | [Issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.issue.md#alertscrashlyticsissue_interface) | Basic information of the Crashlytics issue |

## alerts.crashlytics.NewAnrIssuePayload."@type"

**Signature:**  

```typescript

```

## alerts.crashlytics.NewAnrIssuePayload.issue

Basic information of the Crashlytics issue

**Signature:**  

    issue: Issue;