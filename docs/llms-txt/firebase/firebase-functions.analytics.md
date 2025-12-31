# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.md.txt

# analytics namespace

## Functions

|                                                             Function                                                             |                   Description                    |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [event(analyticsEventType)](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.md#analyticsevent) | Registers a function to handle analytics events. |

## Classes

|                                                                                  Class                                                                                   |                                       Description                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [AnalyticsEvent](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticsevent.md#analyticsanalyticsevent_class)                      | Interface representing a Firebase Analytics event that was logged for a specific user.   |
| [AnalyticsEventBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticseventbuilder.md#analyticsanalyticseventbuilder_class) | The Firebase Analytics event builder interface.Access via `functions.analytics.event()`. |
| [ExportBundleInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.exportbundleinfo.md#analyticsexportbundleinfo_class)                | Interface representing the bundle these events were uploaded to.                         |
| [UserDimensions](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensions_class)                      | Interface representing the user who triggered the events.                                |
| [UserPropertyValue](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userpropertyvalue.md#analyticsuserpropertyvalue_class)             | Predefined or custom properties stored on the client side.                               |

## Interfaces

|                                                                  Interface                                                                  |                                    Description                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [AppInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md#analyticsappinfo_interface)          | Interface representing the application that triggered these events.               |
| [DeviceInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfo_interface) | Interface representing the device that triggered these Firebase Analytics events. |
| [GeoInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.geoinfo.md#analyticsgeoinfo_interface)          | Interface representing the geographic origin of the events.                       |

## analytics.event()

Registers a function to handle analytics events.

**Signature:**  

    export declare function event(analyticsEventType: string): AnalyticsEventBuilder;

### Parameters

|     Parameter      |  Type  |                               Description                                |
|--------------------|--------|--------------------------------------------------------------------------|
| analyticsEventType | string | Name of the analytics event type to which this Cloud Function is scoped. |

**Returns:**

[AnalyticsEventBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.analyticseventbuilder.md#analyticsanalyticseventbuilder_class)

Analytics event builder interface.