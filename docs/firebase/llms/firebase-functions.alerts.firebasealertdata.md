# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md.txt

# alerts.FirebaseAlertData interface

The CloudEvent data emitted by Firebase Alerts.

**Signature:**  

    export interface FirebaseAlertData<T = any> 

## Properties

|                                                                             Property                                                                             |  Type  |                                Description                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------|
| [createTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdatacreatetime) | string | Time that the event has created.                                          |
| [endTime](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdataendtime)       | string | Time that the event has ended. Optional, only present for ongoing alerts. |
| [payload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdatapayload)       | T      | Payload of the event, which includes the details of the specific alert.   |

## alerts.FirebaseAlertData.createTime

Time that the event has created.

**Signature:**  

    createTime: string;

## alerts.FirebaseAlertData.endTime

Time that the event has ended. Optional, only present for ongoing alerts.

**Signature:**  

    endTime: string;

## alerts.FirebaseAlertData.payload

Payload of the event, which includes the details of the specific alert.

**Signature:**  

    payload: T;