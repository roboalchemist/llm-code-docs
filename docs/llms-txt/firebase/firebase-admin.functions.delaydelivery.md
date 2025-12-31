# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.delaydelivery.md.txt

# DelayDelivery interface

Interface representing task options with delayed delivery.

**Signature:**  

    export interface DelayDelivery 

## Properties

|                                                                         Property                                                                          |  Type  |                                                            Description                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------|
| [scheduleDelaySeconds](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.delaydelivery.md#delaydeliveryscheduledelayseconds) | number | The duration of delay of the time when the task is scheduled to be attempted or retried. This delay is added to the current time. |

## DelayDelivery.scheduleDelaySeconds

The duration of delay of the time when the task is scheduled to be attempted or retried. This delay is added to the current time.

**Signature:**  

    scheduleDelaySeconds?: number;