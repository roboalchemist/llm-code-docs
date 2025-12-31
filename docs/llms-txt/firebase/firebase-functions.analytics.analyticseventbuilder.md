# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticseventbuilder.md.txt

# analytics.AnalyticsEventBuilder class

The Firebase Analytics event builder interface.

Access via `functions.analytics.event()`.

**Signature:**  

    export declare class AnalyticsEventBuilder 

## Constructors

|                                                                                           Constructor                                                                                           | Modifiers |                          Description                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------|
| [(constructor)(triggerResource, options)](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticseventbuilder.md#analyticsanalyticseventbuilderconstructor) |           | Constructs a new instance of the `AnalyticsEventBuilder` class |

## Methods

|                                                                              Method                                                                              | Modifiers |                              Description                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------|
| [onLog(handler)](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticseventbuilder.md#analyticsanalyticseventbuilderonlog) |           | Event handler that fires every time a Firebase Analytics event occurs. |

## analytics.AnalyticsEventBuilder.(constructor)

Constructs a new instance of the `AnalyticsEventBuilder` class

**Signature:**  

    constructor(triggerResource: () => string, options: DeploymentOptions);

### Parameters

|    Parameter    |                                                                     Type                                                                      | Description |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| triggerResource | () =\> string                                                                                                                                 |             |
| options         | [DeploymentOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.deploymentoptions.md#deploymentoptions_interface) |             |

## analytics.AnalyticsEventBuilder.onLog()

Event handler that fires every time a Firebase Analytics event occurs.

**Signature:**  

    onLog(handler: (event: AnalyticsEvent, context: EventContext) => PromiseLike<any> | any): CloudFunction<AnalyticsEvent>;

### Parameters

| Parameter |                                                                                                                                                                Type                                                                                                                                                                 |                              Description                               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| handler   | (event: [AnalyticsEvent](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticsevent_class), context: [EventContext](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontext_interface)) =\> PromiseLike\<any\> \| any | Event handler that fires every time a Firebase Analytics event occurs. |

**Returns:**

[CloudFunction](https://firebase.google.com/docs/reference/functions/firebase-functions.cloudfunction.md#cloudfunction_interface)\<[AnalyticsEvent](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticsevent_class)\>

A function that you can export and deploy.