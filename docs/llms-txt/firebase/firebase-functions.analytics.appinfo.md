# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md.txt

# analytics.AppInfo interface

Interface representing the application that triggered these events.

**Signature:**  

    export interface AppInfo 

## Properties

|                                                                  Property                                                                   |  Type  |                                                                Description                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [appId](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md#analyticsappinfoappid)                 | string | Unique application identifier within an app store.                                                                                        |
| [appInstanceId](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md#analyticsappinfoappinstanceid) | string | Unique ID for this instance of the app.Example: "71683BF9FA3B4B0D9535A1F05188BAF3".                                                       |
| [appPlatform](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md#analyticsappinfoappplatform)     | string | The app platform.Examples: "ANDROID", "IOS".                                                                                              |
| [appStore](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md#analyticsappinfoappstore)           | string | The identifier of the store that installed the app.Examples: "com.sec.android.app.samsungapps", "com.amazon.venezia", "com.nokia.nstore". |
| [appVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.appinfo.md#analyticsappinfoappversion)       | string | The app's version name.Examples: "1.0", "4.3.1.1.213361", "2.3 (1824253)", "v1.8b22p6".                                                   |

## analytics.AppInfo.appId

Unique application identifier within an app store.

**Signature:**  

    appId?: string;

## analytics.AppInfo.appInstanceId

Unique ID for this instance of the app.

Example: "71683BF9FA3B4B0D9535A1F05188BAF3".

**Signature:**  

    appInstanceId: string;

## analytics.AppInfo.appPlatform

The app platform.

Examples: "ANDROID", "IOS".

**Signature:**  

    appPlatform: string;

## analytics.AppInfo.appStore

The identifier of the store that installed the app.

Examples: "com.sec.android.app.samsungapps", "com.amazon.venezia", "com.nokia.nstore".

**Signature:**  

    appStore?: string;

## analytics.AppInfo.appVersion

The app's version name.

Examples: "1.0", "4.3.1.1.213361", "2.3 (1824253)", "v1.8b22p6".

**Signature:**  

    appVersion?: string;