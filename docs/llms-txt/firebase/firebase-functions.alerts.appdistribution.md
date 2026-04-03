# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md.txt

# alerts.appDistribution namespace

## Functions

|                                                                                                      Function                                                                                                      |                                   Description                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [onInAppFeedbackPublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md#alertsappdistributiononinappfeedbackpublished)                  | Declares a function that can handle receiving new in-app feedback from a tester. |
| [onInAppFeedbackPublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md#alertsappdistributiononinappfeedbackpublished)           | Declares a function that can handle receiving new in-app feedback from a tester. |
| [onInAppFeedbackPublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md#alertsappdistributiononinappfeedbackpublished)            | Declares a function that can handle receiving new in-app feedback from a tester. |
| [onNewTesterIosDevicePublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md#alertsappdistributiononnewtesteriosdevicepublished)        | Declares a function that can handle adding a new tester iOS device.              |
| [onNewTesterIosDevicePublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md#alertsappdistributiononnewtesteriosdevicepublished) | Declares a function that can handle adding a new tester iOS device.              |
| [onNewTesterIosDevicePublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.md#alertsappdistributiononnewtesteriosdevicepublished)  | Declares a function that can handle adding a new tester iOS device.              |

## Interfaces

|                                                                                                       Interface                                                                                                       |                                                               Description                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)       | A custom CloudEvent for Firebase Alerts (with custom extension attributes).                                                             |
| [AppDistributionOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptions_interface) | Configuration for app distribution functions.                                                                                           |
| [InAppFeedbackPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload_interface)       | The internal payload object for receiving in-app feedback from a tester. Payload is wrapped inside a `FirebaseAlertData` object.        |
| [NewTesterDevicePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload_interface) | The internal payload object for adding a new tester device to app distribution. Payload is wrapped inside a `FirebaseAlertData` object. |

## alerts.appDistribution.onInAppFeedbackPublished()

Declares a function that can handle receiving new in-app feedback from a tester.

**Signature:**  

    export declare function onInAppFeedbackPublished(handler: (event: AppDistributionEvent<InAppFeedbackPayload>) => any | Promise<any>): CloudFunction<AppDistributionEvent<InAppFeedbackPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                 Type                                                                                                                                                                                                                                  |                           Description                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| handler   | (event: [AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[InAppFeedbackPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time new feedback is received. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[InAppFeedbackPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload_interface)\>\>

A function that you can export and deploy.

## alerts.appDistribution.onInAppFeedbackPublished()

Declares a function that can handle receiving new in-app feedback from a tester.

**Signature:**  

    export declare function onInAppFeedbackPublished(appId: string, handler: (event: AppDistributionEvent<InAppFeedbackPayload>) => any | Promise<any>): CloudFunction<AppDistributionEvent<InAppFeedbackPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                 Type                                                                                                                                                                                                                                  |                           Description                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                                                                | A specific application the handler will trigger on.             |
| handler   | (event: [AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[InAppFeedbackPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time new feedback is received. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[InAppFeedbackPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload_interface)\>\>

A function that you can export and deploy.

## alerts.appDistribution.onInAppFeedbackPublished()

Declares a function that can handle receiving new in-app feedback from a tester.

**Signature:**  

    export declare function onInAppFeedbackPublished(opts: AppDistributionOptions, handler: (event: AppDistributionEvent<InAppFeedbackPayload>) => any | Promise<any>): CloudFunction<AppDistributionEvent<InAppFeedbackPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                 Type                                                                                                                                                                                                                                  |                           Description                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| opts      | [AppDistributionOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptions_interface)                                                                                                                                                                                                                                                 | Options that can be set on the function.                        |
| handler   | (event: [AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[InAppFeedbackPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time new feedback is received. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[InAppFeedbackPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.inappfeedbackpayload.md#alertsappdistributioninappfeedbackpayload_interface)\>\>

A function that you can export and deploy.

## alerts.appDistribution.onNewTesterIosDevicePublished()

Declares a function that can handle adding a new tester iOS device.

**Signature:**  

    export declare function onNewTesterIosDevicePublished(handler: (event: AppDistributionEvent<NewTesterDevicePayload>) => any | Promise<any>): CloudFunction<AppDistributionEvent<NewTesterDevicePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                    Type                                                                                                                                                                                                                                     |                               Description                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| handler   | (event: [AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[NewTesterDevicePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a new tester iOS device is added. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[NewTesterDevicePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload_interface)\>\>

A function that you can export and deploy.

## alerts.appDistribution.onNewTesterIosDevicePublished()

Declares a function that can handle adding a new tester iOS device.

**Signature:**  

    export declare function onNewTesterIosDevicePublished(appId: string, handler: (event: AppDistributionEvent<NewTesterDevicePayload>) => any | Promise<any>): CloudFunction<AppDistributionEvent<NewTesterDevicePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                    Type                                                                                                                                                                                                                                     |                               Description                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | A specific application the handler will trigger on.                     |
| handler   | (event: [AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[NewTesterDevicePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a new tester iOS device is added. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[NewTesterDevicePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload_interface)\>\>

A function that you can export and deploy.

## alerts.appDistribution.onNewTesterIosDevicePublished()

Declares a function that can handle adding a new tester iOS device.

**Signature:**  

    export declare function onNewTesterIosDevicePublished(opts: AppDistributionOptions, handler: (event: AppDistributionEvent<NewTesterDevicePayload>) => any | Promise<any>): CloudFunction<AppDistributionEvent<NewTesterDevicePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                                    Type                                                                                                                                                                                                                                     |                               Description                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| opts      | [AppDistributionOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionoptions.md#alertsappdistributionappdistributionoptions_interface)                                                                                                                                                                                                                                                       | Options that can be set on the function.                                |
| handler   | (event: [AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[NewTesterDevicePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload_interface)\>) =\> any \| Promise\<any\> | Event handler which is run every time a new tester iOS device is added. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AppDistributionEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.appdistributionevent.md#alertsappdistributionappdistributionevent_interface)\<[NewTesterDevicePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.appdistribution.newtesterdevicepayload.md#alertsappdistributionnewtesterdevicepayload_interface)\>\>

A function that you can export and deploy.