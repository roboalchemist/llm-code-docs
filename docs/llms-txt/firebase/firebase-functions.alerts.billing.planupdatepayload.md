# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md.txt

# alerts.billing.PlanUpdatePayload interface

The internal payload object for billing plan updates. Payload is wrapped inside a `FirebaseAlertData` object.

**Signature:**  

    export interface PlanUpdatePayload 

## Properties

|                                                                                          Property                                                                                           |                                          Type                                           |                            Description                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| ["@type"](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayload%22@type%22)               | "type.googleapis.com/google.events.firebase.firebasealerts.v1.BillingPlanUpdatePayload" |                                                                    |
| [billingPlan](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayloadbillingplan)           | string                                                                                  | A Firebase billing plan.                                           |
| [notificationType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayloadnotificationtype) | string                                                                                  | The type of the notification, e.g. upgrade, downgrade              |
| [principalEmail](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.planupdatepayload.md#alertsbillingplanupdatepayloadprincipalemail)     | string                                                                                  | The email address of the person that triggered billing plan change |

## alerts.billing.PlanUpdatePayload."@type"

**Signature:**  

```typescript

```

## alerts.billing.PlanUpdatePayload.billingPlan

A Firebase billing plan.

**Signature:**  

    billingPlan: string;

## alerts.billing.PlanUpdatePayload.notificationType

The type of the notification, e.g. upgrade, downgrade

**Signature:**  

    notificationType: string;

## alerts.billing.PlanUpdatePayload.principalEmail

The email address of the person that triggered billing plan change

**Signature:**  

    principalEmail: string;