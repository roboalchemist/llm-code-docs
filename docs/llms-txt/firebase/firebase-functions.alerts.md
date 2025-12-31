# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.md.txt

# alerts namespace

## Functions

|                                                                           Function                                                                            |                              Description                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [onAlertPublished(alertType, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.md#alertsonalertpublished) | Declares a function that can handle Firebase Alerts from CloudEvents. |
| [onAlertPublished(options, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.md#alertsonalertpublished)   | Declares a function that can handle Firebase Alerts from CloudEvents. |

## Interfaces

|                                                                                    Interface                                                                                     |                                 Description                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [AlertEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalertevent_interface)                               | A custom CloudEvent for Firebase Alerts (with custom extension attributes). |
| [FirebaseAlertData](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertdata.md#alertsfirebasealertdata_interface)          | The CloudEvent data emitted by Firebase Alerts.                             |
| [FirebaseAlertOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptions_interface) | Configuration for Firebase Alert functions.                                 |

## Namespaces

|                                                                             Namespace                                                                             | Description |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [appDistribution](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md#alertsappdistribution_namespace) |             |
| [billing](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.billing.md#alertsbilling_namespace)                         |             |
| [crashlytics](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlytics_namespace)             |             |
| [performance](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.performance.md#alertsperformance_namespace)             |             |

## Type Aliases

|                                                         Type Alias                                                          |                        Description                         |
|-----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [AlertType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.md#alertsalerttype) | The underlying alert type of the Firebase Alerts provider. |

## alerts.onAlertPublished()

Declares a function that can handle Firebase Alerts from CloudEvents.

**Signature:**  

    export declare function onAlertPublished<T extends {
        ["@type"]: string;
    } = any>(alertType: AlertType, handler: (event: AlertEvent<T>) => any | Promise<any>): CloudFunction<AlertEvent<T>>;

### Parameters

| Parameter |                                                                                            Type                                                                                            |                            Description                             |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| alertType | [AlertType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.md#alertsalerttype)                                                                | the alert type or Firebase Alert function configuration.           |
| handler   | (event: [AlertEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalertevent_interface)\<T\>) =\> any \| Promise\<any\> | a function that can handle the Firebase Alert inside a CloudEvent. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AlertEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalertevent_interface)\<T\>\>

A function that you can export and deploy.

## alerts.onAlertPublished()

Declares a function that can handle Firebase Alerts from CloudEvents.

**Signature:**  

    export declare function onAlertPublished<T extends {
        ["@type"]: string;
    } = any>(options: FirebaseAlertOptions, handler: (event: AlertEvent<T>) => any | Promise<any>): CloudFunction<AlertEvent<T>>;

### Parameters

| Parameter |                                                                                            Type                                                                                            |                            Description                             |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| options   | [FirebaseAlertOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.firebasealertoptions.md#alertsfirebasealertoptions_interface)           | the alert type and other options for this cloud function.          |
| handler   | (event: [AlertEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalertevent_interface)\<T\>) =\> any \| Promise\<any\> | a function that can handle the Firebase Alert inside a CloudEvent. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AlertEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.alertevent.md#alertsalertevent_interface)\<T\>\>

## alerts.AlertType

The underlying alert type of the Firebase Alerts provider.

**Signature:**  

    export type AlertType = "crashlytics.newFatalIssue" | "crashlytics.newNonfatalIssue" | "crashlytics.regression" | "crashlytics.stabilityDigest" | "crashlytics.velocity" | "crashlytics.newAnrIssue" | "billing.planUpdate" | "billing.planAutomatedUpdate" | "appDistribution.newTesterIosDevice" | "appDistribution.inAppFeedback" | "performance.threshold" | string;