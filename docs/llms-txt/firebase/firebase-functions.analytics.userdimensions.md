# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md.txt

# analytics.UserDimensions class

Interface representing the user who triggered the events.

**Signature:**  

    export declare class UserDimensions 

## Constructors

|                                                                             Constructor                                                                             | Modifiers |                       Description                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------|
| [(constructor)(wireFormat)](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsconstructor) |           | Constructs a new instance of the `UserDimensions` class |

## Properties

|                                                                          Property                                                                           | Modifiers |                                                                                        Type                                                                                        |                                                                                                                                                                 Description                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [appInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsappinfo)               |           | [AppInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md#analyticsappinfo_interface)                                                 | App information.                                                                                                                                                                                                                                                                                                                            |
| [bundleInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsbundleinfo)         |           | [ExportBundleInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.exportbundleinfo.md#analyticsexportbundleinfo_class)                          | Information regarding the bundle in which these events were uploaded.                                                                                                                                                                                                                                                                       |
| [deviceInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsdeviceinfo)         |           | [DeviceInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfo_interface)                                        | Device information.                                                                                                                                                                                                                                                                                                                         |
| [firstOpenTime](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsfirstopentime)   |           | string                                                                                                                                                                             | The time (in UTC) at which the user first opened the app.                                                                                                                                                                                                                                                                                   |
| [geoInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsgeoinfo)               |           | [GeoInfo](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.geoinfo.md#analyticsgeoinfo_interface)                                                 | User's geographic information.                                                                                                                                                                                                                                                                                                              |
| [userId](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsuserid)                 |           | string                                                                                                                                                                             | The user ID set via the `setUserId` API. \[Android\](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.html#setUserId(java.lang.String)) \[iOS\](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setUserID) |
| [userProperties](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userdimensions.md#analyticsuserdimensionsuserproperties) |           | { \[key: string\]: [UserPropertyValue](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.userpropertyvalue.md#analyticsuserpropertyvalue_class); } | A map of user properties set with the \[`setUserProperty`\](https://firebase.google.com/docs/analytics/android/properties) API.All values are \[`UserPropertyValue`\](providers_analytics_.userpropertyvalue) objects.                                                                                                                      |

## analytics.UserDimensions.(constructor)

Constructs a new instance of the `UserDimensions` class

**Signature:**  

    constructor(wireFormat: any);

### Parameters

| Parameter  | Type | Description |
|------------|------|-------------|
| wireFormat | any  |             |

## analytics.UserDimensions.appInfo

App information.

**Signature:**  

    appInfo?: AppInfo;

## analytics.UserDimensions.bundleInfo

Information regarding the bundle in which these events were uploaded.

**Signature:**  

    bundleInfo: ExportBundleInfo;

## analytics.UserDimensions.deviceInfo

Device information.

**Signature:**  

    deviceInfo: DeviceInfo;

## analytics.UserDimensions.firstOpenTime

The time (in UTC) at which the user first opened the app.

**Signature:**  

    firstOpenTime?: string;

## analytics.UserDimensions.geoInfo

User's geographic information.

**Signature:**  

    geoInfo: GeoInfo;

## analytics.UserDimensions.userId

The user ID set via the `setUserId` API. \[Android\](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.html#setUserId(java.lang.String)) \[iOS\](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Classes/FIRAnalytics#/c:objc(cs)FIRAnalytics(cm)setUserID)

**Signature:**  

    userId?: string;

## analytics.UserDimensions.userProperties

A map of user properties set with the \[`setUserProperty`\](https://firebase.google.com/docs/analytics/android/properties) API.

All values are \[`UserPropertyValue`\](providers_analytics_.userpropertyvalue) objects.

**Signature:**  

    userProperties: {
            [key: string]: UserPropertyValue;
        };