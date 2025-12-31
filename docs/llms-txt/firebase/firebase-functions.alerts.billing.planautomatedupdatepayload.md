# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md.txt

# alerts.billing.PlanAutomatedUpdatePayload interface

The internal payload object for billing plan automated updates. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface PlanAutomatedUpdatePayload 

## Properties

|                                                                                                   Property                                                                                                    |                                               Type                                               |                      Description                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayload%22@type%22)               | "type.googleapis.com/google.events.firebase.firebasealerts.v1.BillingPlanAutomatedUpdatePayload" |                                                       |
| [billingPlan](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayloadbillingplan)           | string                                                                                           | A Firebase billing plan.                              |
| [notificationType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planautomatedupdatepayload.md#alertsbillingplanautomatedupdatepayloadnotificationtype) | string                                                                                           | The type of the notification, e.g. upgrade, downgrade |

## alerts.billing.PlanAutomatedUpdatePayload."@type"

**Signature:**  

```typescript

```

## alerts.billing.PlanAutomatedUpdatePayload.billingPlan

A Firebase billing plan.

**Signature:**  

    billingPlan: string;

## alerts.billing.PlanAutomatedUpdatePayload.notificationType

The type of the notification, e.g. upgrade, downgrade

**Signature:**  

    notificationType: string;