# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md.txt

# alerts.billing.BillingEvent interface

A custom CloudEvent for billing Firebase Alerts (with custom extension attributes).

**Signature:**  

    export interface BillingEvent<T> extends CloudEvent<FirebaseAlertData<T>> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[FirebaseAlertData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdata_interface)\<T\>\>

## Properties

|                                                                              Property                                                                               |  Type  |                Description                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------|
| [alertType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.billingevent.md#alertsbillingbillingeventalerttype) | string | The type of the alerts that got triggered. |

## alerts.billing.BillingEvent.alertType

The type of the alerts that got triggered.

**Signature:**  

    alertType: string;