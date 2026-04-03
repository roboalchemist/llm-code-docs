# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md.txt

# alerts.AlertEvent interface

A custom CloudEvent for Firebase Alerts (with custom extension attributes).

**Signature:**  

    export interface AlertEvent<T> extends CloudEvent<FirebaseAlertData<T>> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[FirebaseAlertData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdata_interface)\<T\>\>

## Properties

|                                                                     Property                                                                     |                                                                                     Type                                                                                     |                                                                   Description                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [alertType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalerteventalerttype) | string                                                                                                                                                                       | The type of the alerts that got triggered.                                                                                                       |
| [appId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalerteventappid)         | string                                                                                                                                                                       | The Firebase App ID that's associated with the alert. This is optional, and only present when the alert is targeting at a specific Firebase App. |
| [data](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalerteventdata)           | [FirebaseAlertData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdata_interface)\<T\> | Data for an `AlertEvent` is a `FirebaseAlertData` object with a given payload.                                                                   |

## alerts.AlertEvent.alertType

The type of the alerts that got triggered.

**Signature:**  

    alertType: string;

## alerts.AlertEvent.appId

The Firebase App ID that's associated with the alert. This is optional, and only present when the alert is targeting at a specific Firebase App.

**Signature:**  

    appId?: string;

## alerts.AlertEvent.data

Data for an `AlertEvent` is a `FirebaseAlertData` object with a given payload.

**Signature:**  

    data: FirebaseAlertData<T>;