# Source: https://documentation.onesignal.com/docs/en/data-collected-by-the-onesignal-sdk.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Collected by the OneSignal SDK

> List of data collected by OneSignal SDK

The following are data fields that the OneSignal SDK collects automatically, manually, and/or through user permission. To customize which data is collected and how to manage user consent for data collection, please read our guide on [Handling Personal Data](./handling-personal-data). Most data can be [exported from the Dashboard or API](./exporting-data).

***

Data that can be used to target audiences by [Segments](./segmentation):

| Data                 | Description                                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| First Session Time   | The date & time the user first used the app / visited the website (UTC).                                                                        |
| Last Session Time    | The date & time the user most recently used the app / visited the website (UTC).                                                                |
| Session Count        | The number of times the user has used the app / visited the website.                                                                            |
| Total Usage Duration | The number of seconds the user has ever interacted with the app, as recorded whenever the app is in the foreground.                             |
| Device OS            | The operating system of the device / browser.                                                                                                   |
| Device Rooted        | **ANDROID** - Whether the user has a rooted device.**iOS** - Whether the user has a jailbroken device.                                          |
| Device Language      | The language the device / browser reports. Can also be set with the SDK language methods.                                                       |
| Timezone             | The most recent timezone the device / browser was in. Timezone is tracked based on [IANA TZ](https://en.wikipedia.org/wiki/Tz_database) format. |
| Country              | The most recent country the device / browser was in ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) format).                            |
| Push Status          | Whether the device / browser has push notifications enabled or disabled.                                                                        |
| App Version          | **MOBILE** - The version of the app the most recent session reported the user running.                                                          |
| In App Purchases     | **MOBILE** - Consumable Purchases made by the user in the app while our SDK was active.                                                         |

The following data the OneSignal SDK collects that is not able to be segmented:

| Data                        | Description                                                                                                                                                                                                           |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Your Application Identifier | **MOBILE** - The package name of your mobile application.                                                                                                                                                             |
| Cellular Carrier            | **MOBILE** - The name of the cellular carrier used by the device.                                                                                                                                                     |
| Device Model                | The model name of the device / browser.                                                                                                                                                                               |
| IP Address                  | The IP address the device / browser is visiting from. This is not stored on our servers if the user is in the EU. See [handing IP Address Tracking](./handling-personal-data#ip-address-collection) for more details. |
| web\_auth and web\_p256     | Web Push Subscription Tokens available for export from our [API CSV export](/reference/csv-export).                                                                                                                   |
| Push Tokens                 | Mobile App and Web Push Tokens added to the device by FCM or APNs.                                                                                                                                                    |

## Data OneSignal Automatically Collects that can be disabled client side

The following data the OneSignal SDK collects if your app asks for and receives permission from users:

| Data     | Description                                                                                                                                                                                           |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Location | **MOBILE** - GPS coordinates of the device. Location tracking must be turned on and accepted by the user. [Sending location to OneSignal can be disabled](./handling-personal-data#location-sharing). |

## Data Manually Sent to OneSignal

The following data you may manually send to OneSignal. See [Handling Personal Data](./handling-personal-data) for more details.

| Data         | Description                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------- |
| Email        | Our SDKs support sending us the user's email address if you wish to use OneSignal to deliver emails to users. |
| Phone Number | Our SDKs support sending us the user's phone number if you wish to use OneSignal to deliver SMS to users.     |
| Tags         | You can send any additional data to us about a user as a tag.                                                 |

## Web SDK Browser Storage

Identifiers, Purpose and Type of browser storage used:

| Identifier Name                                          | Purpose                                                                     | Type                                        |
| -------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------- |
| `ONE_SIGNAL_SDK_DB`                                      | Storing user preferences in connection with notification permission status. | IndexedDB dictionary, on customer’s domain. |
| `os_pageViews`,`isOptedOut`,`isPushNotificationsEnabled` | Prompting and subscription tracking                                         | Local Storage                               |
| `onesignal-pageview-count`,`ONESIGNAL_HTTP_PROMPT_SHOWN` | Prompting                                                                   | Session Storage                             |

***

Built with [Mintlify](https://mintlify.com).
