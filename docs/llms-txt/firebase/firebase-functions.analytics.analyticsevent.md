# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md.txt

# analytics.AnalyticsEvent class

Interface representing a Firebase Analytics event that was logged for a specific user.

**Signature:**  

    export declare class AnalyticsEvent 

## Constructors

|                                                                             Constructor                                                                             | Modifiers |                       Description                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------|
| [(constructor)(wireFormat)](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventconstructor) |           | Constructs a new instance of the `AnalyticsEvent` class |

## Properties

|                                                                           Property                                                                            | Modifiers |                                                                        Type                                                                         |                                                                                                                       Description                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [logTime](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventlogtime)                 |           | string                                                                                                                                              | UTC client time when the event happened.                                                                                                                                                                                                                 |
| [name](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventname)                       |           | string                                                                                                                                              | The name of the event.                                                                                                                                                                                                                                   |
| [params](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventparams)                   |           | { \[key: string\]: any; }                                                                                                                           | A map of parameters and their values associated with the event.Note: Values in this map are cast to the most appropriate type. Due to the nature of JavaScript's number handling, this might entail a loss of precision in cases of very large integers. |
| [previousLogTime](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventpreviouslogtime) |           | string                                                                                                                                              | UTC client time when the previous event happened.                                                                                                                                                                                                        |
| [reportingDate](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventreportingdate)     |           | string                                                                                                                                              | The date on which the event.was logged. (`YYYYMMDD` format in the registered timezone of your app).                                                                                                                                                      |
| [user](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventuser)                       |           | [UserDimensions](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensions_class) | User-related dimensions.                                                                                                                                                                                                                                 |
| [valueInUSD](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticseventvalueinusd)           |           | number                                                                                                                                              | Value parameter in USD.                                                                                                                                                                                                                                  |

## analytics.AnalyticsEvent.(constructor)

Constructs a new instance of the `AnalyticsEvent` class

**Signature:**  

    constructor(wireFormat: any);

### Parameters

| Parameter  | Type | Description |
|------------|------|-------------|
| wireFormat | any  |             |

## analytics.AnalyticsEvent.logTime

UTC client time when the event happened.

**Signature:**  

    logTime: string;

## analytics.AnalyticsEvent.name

The name of the event.

**Signature:**  

    name: string;

## analytics.AnalyticsEvent.params

A map of parameters and their values associated with the event.
| **Note:** Values in this map are cast to the most appropriate type. Due to the nature of JavaScript's number handling, this might entail a loss of precision in cases of very large integers.

**Signature:**  

    params: {
            [key: string]: any;
        };

## analytics.AnalyticsEvent.previousLogTime

UTC client time when the previous event happened.

**Signature:**  

    previousLogTime?: string;

## analytics.AnalyticsEvent.reportingDate

The date on which the event.was logged. (`YYYYMMDD` format in the registered timezone of your app).

**Signature:**  

    reportingDate: string;

## analytics.AnalyticsEvent.user

User-related dimensions.

**Signature:**  

    user?: UserDimensions;

## analytics.AnalyticsEvent.valueInUSD

Value parameter in USD.

**Signature:**  

    valueInUSD?: number;