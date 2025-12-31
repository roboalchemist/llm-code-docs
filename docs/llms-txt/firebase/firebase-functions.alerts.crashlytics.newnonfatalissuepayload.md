# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md.txt

# alerts.crashlytics.NewNonfatalIssuePayload interface

The internal payload object for a new non-fatal issue. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface NewNonfatalIssuePayload 

## Properties

|                                                                                             Property                                                                                              |                                                                            Type                                                                            |                Description                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload%22@type%22) | "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsNewNonfatalIssuePayload"                                                          |                                            |
| [issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayloadissue)         | [Issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.issue.md#alertscrashlyticsissue_interface) | Basic information of the Crashlytics issue |

## alerts.crashlytics.NewNonfatalIssuePayload."@type"

**Signature:**  

```typescript

```

## alerts.crashlytics.NewNonfatalIssuePayload.issue

Basic information of the Crashlytics issue

**Signature:**  

    issue: Issue;