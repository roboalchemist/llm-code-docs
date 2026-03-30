# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md.txt

# alerts.crashlytics.NewFatalIssuePayload interface

The internal payload object for a new fatal issue. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**

    export interface NewFatalIssuePayload 

## Properties

| Property | Type | Description |
|---|---|---|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload%22@type%22) | "type.googleapis.com/google.events.firebase.firebasealerts.v1.CrashlyticsNewFatalIssuePayload" |   |
| [issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayloadissue) | [Issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.issue.md#alertscrashlyticsissue_interface) | Basic information of the Crashlytics issue |

## alerts.crashlytics.NewFatalIssuePayload."@type"

**Signature:**

```typescript

```

## alerts.crashlytics.NewFatalIssuePayload.issue

Basic information of the Crashlytics issue

**Signature:**

    issue: Issue;