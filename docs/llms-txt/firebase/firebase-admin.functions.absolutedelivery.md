# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.absolutedelivery.md.txt

# AbsoluteDelivery interface

Interface representing task options with absolute delivery.

**Signature:**  

    export interface AbsoluteDelivery 

## Properties

|                                                                    Property                                                                     | Type |                           Description                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------|------|-----------------------------------------------------------------|
| [scheduleTime](https://firebase.google.com/docs/reference/admin/node/firebase-admin.functions.absolutedelivery.md#absolutedeliveryscheduletime) | Date | The time when the task is scheduled to be attempted or retried. |

## AbsoluteDelivery.scheduleTime

The time when the task is scheduled to be attempted or retried.

**Signature:**  

    scheduleTime?: Date;