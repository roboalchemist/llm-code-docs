# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md.txt

# alerts.appDistribution.AppDistributionEvent interface

A custom CloudEvent for Firebase Alerts (with custom extension attributes).

**Signature:**  

    export interface AppDistributionEvent<T> extends CloudEvent<FirebaseAlertData<T>> 

**Extends:** [CloudEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudevent.md#cloudevent_interface)\<[FirebaseAlertData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdata_interface)\<T\>\>

## Properties

|                                                                                              Property                                                                                               |  Type  |                      Description                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------|
| [alertType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributioneventalerttype) | string | The type of the alerts that got triggered.            |
| [appId](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributioneventappid)         | string | The Firebase App ID that's associated with the alert. |

## alerts.appDistribution.AppDistributionEvent.alertType

The type of the alerts that got triggered.

**Signature:**  

    alertType: string;

## alerts.appDistribution.AppDistributionEvent.appId

The Firebase App ID that's associated with the alert.

**Signature:**  

    appId: string;