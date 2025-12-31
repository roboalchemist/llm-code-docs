# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md.txt

# alerts.crashlytics namespace

## Functions

|                                                                                                Function                                                                                                |                                             Description                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [onNewAnrIssuePublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewanrissuepublished)                  | Declares a function that can handle a new Application Not Responding issue published to Crashlytics. |
| [onNewAnrIssuePublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewanrissuepublished)           | Declares a function that can handle a new Application Not Responding issue published to Crashlytics. |
| [onNewAnrIssuePublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewanrissuepublished)            | Declares a function that can handle a new Application Not Responding issue published to Crashlytics. |
| [onNewFatalIssuePublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewfatalissuepublished)              | Declares a function that can handle a new fatal issue published to Crashlytics.                      |
| [onNewFatalIssuePublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewfatalissuepublished)       | Declares a function that can handle a new fatal issue published to Crashlytics.                      |
| [onNewFatalIssuePublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewfatalissuepublished)        | Declares a function that can handle a new fatal issue published to Crashlytics.                      |
| [onNewNonfatalIssuePublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewnonfatalissuepublished)        | Declares a function that can handle a new non-fatal issue published to Crashlytics.                  |
| [onNewNonfatalIssuePublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewnonfatalissuepublished) | Declares a function that can handle a new non-fatal issue published to Crashlytics.                  |
| [onNewNonfatalIssuePublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonnewnonfatalissuepublished)  | Declares a function that can handle a new non-fatal issue published to Crashlytics.                  |
| [onRegressionAlertPublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonregressionalertpublished)          | Declares a function that can handle a regression alert published to Crashlytics.                     |
| [onRegressionAlertPublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonregressionalertpublished)   | Declares a function that can handle a regression alert published to Crashlytics.                     |
| [onRegressionAlertPublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonregressionalertpublished)    | Declares a function that can handle a regression alert published to Crashlytics.                     |
| [onStabilityDigestPublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonstabilitydigestpublished)          | Declares a function that can handle a stability digest published to Crashlytics.                     |
| [onStabilityDigestPublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonstabilitydigestpublished)   | Declares a function that can handle a stability digest published to Crashlytics.                     |
| [onStabilityDigestPublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonstabilitydigestpublished)    | Declares a function that can handle a stability digest published to Crashlytics.                     |
| [onVelocityAlertPublished(handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonvelocityalertpublished)              | Declares a function that can handle a velocity alert published to Crashlytics.                       |
| [onVelocityAlertPublished(appId, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonvelocityalertpublished)       | Declares a function that can handle a velocity alert published to Crashlytics.                       |
| [onVelocityAlertPublished(opts, handler)](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.md#alertscrashlyticsonvelocityalertpublished)        | Declares a function that can handle a velocity alert published to Crashlytics.                       |

## Interfaces

|                                                                                                    Interface                                                                                                     |                                                           Description                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)                      | A custom CloudEvent for Firebase Alerts (with custom extension attributes).                                                     |
| [CrashlyticsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsoptions.md#alertscrashlyticscrashlyticsoptions_interface)                | Configuration for Crashlytics functions.                                                                                        |
| [Issue](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.issue.md#alertscrashlyticsissue_interface)                                                       | Generic Crashlytics issue interface                                                                                             |
| [NewAnrIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload_interface)                | The internal payload object for a new Application Not Responding issue. Payload is wrapped inside a `FirebaseAlertData` object. |
| [NewFatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload_interface)          | The internal payload object for a new fatal issue. Payload is wrapped inside a `FirebaseAlertData` object.                      |
| [NewNonfatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload_interface) | The internal payload object for a new non-fatal issue. Payload is wrapped inside a `FirebaseAlertData` object.                  |
| [RegressionAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload_interface)    | The internal payload object for a regression alert. Payload is wrapped inside a `FirebaseAlertData` object.                     |
| [StabilityDigestPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload_interface)    | The internal payload object for a stability digest. Payload is wrapped inside a `FirebaseAlertData` object.                     |
| [TrendingIssueDetails](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.trendingissuedetails.md#alertscrashlyticstrendingissuedetails_interface)          | Generic Crashlytics trending issue interface                                                                                    |
| [VelocityAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload_interface)          | The internal payload object for a velocity alert. Payload is wrapped inside a `FirebaseAlertData` object.                       |

## alerts.crashlytics.onNewAnrIssuePublished()

Declares a function that can handle a new Application Not Responding issue published to Crashlytics.

**Signature:**  

    export declare function onNewAnrIssuePublished(handler: (event: CrashlyticsEvent<NewAnrIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewAnrIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                Type                                                                                                                                                                                                                 |                                               Description                                                |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewAnrIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new Application Not Responding issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewAnrIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewAnrIssuePublished()

Declares a function that can handle a new Application Not Responding issue published to Crashlytics.

**Signature:**  

    export declare function onNewAnrIssuePublished(appId: string, handler: (event: CrashlyticsEvent<NewAnrIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewAnrIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                Type                                                                                                                                                                                                                 |                                               Description                                                |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                              | A specific application the handler will trigger on.                                                      |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewAnrIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new Application Not Responding issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewAnrIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewAnrIssuePublished()

Declares a function that can handle a new Application Not Responding issue published to Crashlytics.

**Signature:**  

    export declare function onNewAnrIssuePublished(opts: CrashlyticsOptions, handler: (event: CrashlyticsEvent<NewAnrIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewAnrIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                Type                                                                                                                                                                                                                 |                                               Description                                                |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| opts      | [CrashlyticsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsoptions.md#alertscrashlyticscrashlyticsoptions_interface)                                                                                                                                                                                                                                   | Options that can be set on the function.                                                                 |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewAnrIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new Application Not Responding issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewAnrIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newanrissuepayload.md#alertscrashlyticsnewanrissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewFatalIssuePublished()

Declares a function that can handle a new fatal issue published to Crashlytics.

**Signature:**  

    export declare function onNewFatalIssuePublished(handler: (event: CrashlyticsEvent<NewFatalIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewFatalIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                   Type                                                                                                                                                                                                                    |                                     Description                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewFatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new fatal issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewFatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewFatalIssuePublished()

Declares a function that can handle a new fatal issue published to Crashlytics.

**Signature:**  

    export declare function onNewFatalIssuePublished(appId: string, handler: (event: CrashlyticsEvent<NewFatalIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewFatalIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                   Type                                                                                                                                                                                                                    |                                     Description                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                                    | A specific application the handler will trigger on.                                 |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewFatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new fatal issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewFatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewFatalIssuePublished()

Declares a function that can handle a new fatal issue published to Crashlytics.

**Signature:**  

    export declare function onNewFatalIssuePublished(opts: CrashlyticsOptions, handler: (event: CrashlyticsEvent<NewFatalIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewFatalIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                   Type                                                                                                                                                                                                                    |                                     Description                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| opts      | [CrashlyticsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsoptions.md#alertscrashlyticscrashlyticsoptions_interface)                                                                                                                                                                                                                                         | Options that can be set on the function.                                            |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewFatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new fatal issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewFatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newfatalissuepayload.md#alertscrashlyticsnewfatalissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewNonfatalIssuePublished()

Declares a function that can handle a new non-fatal issue published to Crashlytics.

**Signature:**  

    export declare function onNewNonfatalIssuePublished(handler: (event: CrashlyticsEvent<NewNonfatalIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewNonfatalIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                        Type                                                                                                                                                                                                                        |                                     Description                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewNonfatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new fatal issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewNonfatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewNonfatalIssuePublished()

Declares a function that can handle a new non-fatal issue published to Crashlytics.

**Signature:**  

    export declare function onNewNonfatalIssuePublished(appId: string, handler: (event: CrashlyticsEvent<NewNonfatalIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewNonfatalIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                        Type                                                                                                                                                                                                                        |                                       Description                                       |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                                             | A specific application the handler will trigger on.                                     |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewNonfatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new non-fatal issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewNonfatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onNewNonfatalIssuePublished()

Declares a function that can handle a new non-fatal issue published to Crashlytics.

**Signature:**  

    export declare function onNewNonfatalIssuePublished(opts: CrashlyticsOptions, handler: (event: CrashlyticsEvent<NewNonfatalIssuePayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<NewNonfatalIssuePayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                        Type                                                                                                                                                                                                                        |                                       Description                                       |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| opts      | [CrashlyticsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsoptions.md#alertscrashlyticscrashlyticsoptions_interface)                                                                                                                                                                                                                                                  | Options that can be set on the function.                                                |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewNonfatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a new non-fatal issue is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[NewNonfatalIssuePayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.newnonfatalissuepayload.md#alertscrashlyticsnewnonfatalissuepayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onRegressionAlertPublished()

Declares a function that can handle a regression alert published to Crashlytics.

**Signature:**  

    export declare function onRegressionAlertPublished(handler: (event: CrashlyticsEvent<RegressionAlertPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<RegressionAlertPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                      Type                                                                                                                                                                                                                       |                                     Description                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[RegressionAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a regression alert is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[RegressionAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onRegressionAlertPublished()

Declares a function that can handle a regression alert published to Crashlytics.

**Signature:**  

    export declare function onRegressionAlertPublished(appId: string, handler: (event: CrashlyticsEvent<RegressionAlertPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<RegressionAlertPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                      Type                                                                                                                                                                                                                       |                                     Description                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                                          | A specific application the handler will trigger on.                                  |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[RegressionAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a regression alert is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[RegressionAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onRegressionAlertPublished()

Declares a function that can handle a regression alert published to Crashlytics.

**Signature:**  

    export declare function onRegressionAlertPublished(opts: CrashlyticsOptions, handler: (event: CrashlyticsEvent<RegressionAlertPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<RegressionAlertPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                      Type                                                                                                                                                                                                                       |                                     Description                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| opts      | [CrashlyticsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsoptions.md#alertscrashlyticscrashlyticsoptions_interface)                                                                                                                                                                                                                                               | Options that can be set on the function.                                             |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[RegressionAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a regression alert is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[RegressionAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.regressionalertpayload.md#alertscrashlyticsregressionalertpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onStabilityDigestPublished()

Declares a function that can handle a stability digest published to Crashlytics.

**Signature:**  

    export declare function onStabilityDigestPublished(handler: (event: CrashlyticsEvent<StabilityDigestPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<StabilityDigestPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                      Type                                                                                                                                                                                                                       |                                     Description                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[StabilityDigestPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a stability digest is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[StabilityDigestPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onStabilityDigestPublished()

Declares a function that can handle a stability digest published to Crashlytics.

**Signature:**  

    export declare function onStabilityDigestPublished(appId: string, handler: (event: CrashlyticsEvent<StabilityDigestPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<StabilityDigestPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                      Type                                                                                                                                                                                                                       |                                     Description                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                                          | A specific application the handler will trigger on.                                  |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[StabilityDigestPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a stability digest is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[StabilityDigestPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onStabilityDigestPublished()

Declares a function that can handle a stability digest published to Crashlytics.

**Signature:**  

    export declare function onStabilityDigestPublished(opts: CrashlyticsOptions, handler: (event: CrashlyticsEvent<StabilityDigestPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<StabilityDigestPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                      Type                                                                                                                                                                                                                       |                                     Description                                      |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| opts      | [CrashlyticsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsoptions.md#alertscrashlyticscrashlyticsoptions_interface)                                                                                                                                                                                                                                               | Options that can be set on the function.                                             |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[StabilityDigestPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a stability digest is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[StabilityDigestPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.stabilitydigestpayload.md#alertscrashlyticsstabilitydigestpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onVelocityAlertPublished()

Declares a function that can handle a velocity alert published to Crashlytics.

**Signature:**  

    export declare function onVelocityAlertPublished(handler: (event: CrashlyticsEvent<VelocityAlertPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<VelocityAlertPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                   Type                                                                                                                                                                                                                    |                                    Description                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[VelocityAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a velocity alert is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[VelocityAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onVelocityAlertPublished()

Declares a function that can handle a velocity alert published to Crashlytics.

**Signature:**  

    export declare function onVelocityAlertPublished(appId: string, handler: (event: CrashlyticsEvent<VelocityAlertPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<VelocityAlertPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                   Type                                                                                                                                                                                                                    |                                    Description                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| appId     | string                                                                                                                                                                                                                                                                                                                                                                                                                                    | A specific application the handler will trigger on.                                |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[VelocityAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a velocity alert is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[VelocityAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload_interface)\>\>

A function that you can export and deploy.

## alerts.crashlytics.onVelocityAlertPublished()

Declares a function that can handle a velocity alert published to Crashlytics.

**Signature:**  

    export declare function onVelocityAlertPublished(opts: CrashlyticsOptions, handler: (event: CrashlyticsEvent<VelocityAlertPayload>) => any | Promise<any>): CloudFunction<CrashlyticsEvent<VelocityAlertPayload>>;

### Parameters

| Parameter |                                                                                                                                                                                                                   Type                                                                                                                                                                                                                    |                                    Description                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| opts      | [CrashlyticsOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsoptions.md#alertscrashlyticscrashlyticsoptions_interface)                                                                                                                                                                                                                                         | Options that can be set on the function.                                           |
| handler   | (event: [CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[VelocityAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload_interface)\>) =\> any \| Promise\<any\> | Event handler that is triggered when a velocity alert is published to Crashlytics. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[CrashlyticsEvent](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.crashlyticsevent.md#alertscrashlyticscrashlyticsevent_interface)\<[VelocityAlertPayload](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.alerts.crashlytics.velocityalertpayload.md#alertscrashlyticsvelocityalertpayload_interface)\>\>

A function that you can export and deploy.