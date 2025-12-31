# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md.txt

# analytics.DeviceInfo interface

Interface representing the device that triggered these Firebase Analytics events.

**Signature:**  

    export interface DeviceInfo 

## Properties

|                                                                                   Property                                                                                    |  Type   |                                                                                                                       Description                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [deviceCategory](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfodevicecategory)                           | string  | Device category.Examples: "tablet" or "mobile".                                                                                                                                                                                                          |
| [deviceId](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfodeviceid)                                       | string  | Vendor specific device identifier. This is IDFV on iOS. Not used for Android.Example: '599F9C00-92DC-4B5C-9464-7971F01F8370'                                                                                                                             |
| [deviceModel](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfodevicemodel)                                 | string  | Device model, as read from the OS.Example: "iPhone9,1"                                                                                                                                                                                                   |
| [deviceTimeZoneOffsetSeconds](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfodevicetimezoneoffsetseconds) | number  | The time zone of the device when data was uploaded, as seconds skew from UTC. Use this to calculate the device's local time for \[`EventContext.timestamp`\](cloud_functions_eventcontext.html#timestamp).                                               |
| [limitedAdTracking](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfolimitedadtracking)                     | boolean | The device's Limit Ad Tracking setting. When `true`, you cannot use `resettableDeviceId` for remarketing, demographics or influencing ads serving behaviour. However, you can use `resettableDeviceId` for conversion tracking and campaign attribution. |
| [mobileBrandName](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfomobilebrandname)                         | string  | Device brand name.Examples: "Samsung", "HTC"                                                                                                                                                                                                             |
| [mobileMarketingName](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfomobilemarketingname)                 | string  | Device marketing name.Example: "Galaxy S4 Mini"                                                                                                                                                                                                          |
| [mobileModelName](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfomobilemodelname)                         | string  | Device model name in human-readable format.Example: "iPhone 7"                                                                                                                                                                                           |
| [platformVersion](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfoplatformversion)                         | string  | Device OS version when data capture ended.Example: "4.4.2"                                                                                                                                                                                               |
| [resettableDeviceId](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinforesettabledeviceid)                   | string  | The type of the \[`resettable_device_id`\](https://support.google.com/dfp_premium/answer/6238701?hl=en) is IDFA on iOS (when available) and AdId on Android.Example: "71683BF9-FA3B-4B0D-9535-A1F05188BAF3"                                              |
| [userDefaultLanguage](https://firebase.google.com/docs/reference/functions/firebase-functions.analytics.deviceinfo.md#analyticsdeviceinfouserdefaultlanguage)                 | string  | The user language in language-country format, where language is an ISO 639 value and country is an ISO 3166 value.Examples: "en-us", "en-za", "zh-tw", "jp"                                                                                              |

## analytics.DeviceInfo.deviceCategory

Device category.

Examples: "tablet" or "mobile".

**Signature:**  

    deviceCategory?: string;

## analytics.DeviceInfo.deviceId

Vendor specific device identifier. This is IDFV on iOS. Not used for Android.

Example: '599F9C00-92DC-4B5C-9464-7971F01F8370'

**Signature:**  

    deviceId?: string;

## analytics.DeviceInfo.deviceModel

Device model, as read from the OS.

Example: "iPhone9,1"

**Signature:**  

    deviceModel?: string;

## analytics.DeviceInfo.deviceTimeZoneOffsetSeconds

The time zone of the device when data was uploaded, as seconds skew from UTC. Use this to calculate the device's local time for \[`EventContext.timestamp`\](cloud_functions_eventcontext.html#timestamp).

**Signature:**  

    deviceTimeZoneOffsetSeconds: number;

## analytics.DeviceInfo.limitedAdTracking

The device's Limit Ad Tracking setting. When `true`, you cannot use `resettableDeviceId` for remarketing, demographics or influencing ads serving behaviour. However, you can use `resettableDeviceId` for conversion tracking and campaign attribution.

**Signature:**  

    limitedAdTracking: boolean;

## analytics.DeviceInfo.mobileBrandName

Device brand name.

Examples: "Samsung", "HTC"

**Signature:**  

    mobileBrandName?: string;

## analytics.DeviceInfo.mobileMarketingName

Device marketing name.

Example: "Galaxy S4 Mini"

**Signature:**  

    mobileMarketingName?: string;

## analytics.DeviceInfo.mobileModelName

Device model name in human-readable format.

Example: "iPhone 7"

**Signature:**  

    mobileModelName?: string;

## analytics.DeviceInfo.platformVersion

Device OS version when data capture ended.

Example: "4.4.2"

**Signature:**  

    platformVersion?: string;

## analytics.DeviceInfo.resettableDeviceId

The type of the \[`resettable_device_id`\](https://support.google.com/dfp_premium/answer/6238701?hl=en) is IDFA on iOS (when available) and AdId on Android.

Example: "71683BF9-FA3B-4B0D-9535-A1F05188BAF3"

**Signature:**  

    resettableDeviceId?: string;

## analytics.DeviceInfo.userDefaultLanguage

The user language in language-country format, where language is an ISO 639 value and country is an ISO 3166 value.

Examples: "en-us", "en-za", "zh-tw", "jp"

**Signature:**  

    userDefaultLanguage: string;