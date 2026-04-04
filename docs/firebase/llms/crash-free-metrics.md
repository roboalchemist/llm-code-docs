# Source: https://firebase.google.com/docs/crashlytics/crash-free-metrics.md.txt

<br />

For each of your apps,Crashlyticsautomatically calculates and displays crash-free metrics, specifically the percentage of**crash-free*users*** and the percentage of**crash-free*sessions***. These metrics can help you quickly understand the stability of your app.

You can find charts of these crash-free metrics at the top of the[Crashlyticsdashboard](https://console.firebase.google.com/project/_/crashlytics), and you can filter these charts by a variety of dimensions, like time range, build, and (for Android apps) byGoogle Playtrack.

Note that crash-free metrics are only calculated for*fatal*events (and uncaught exceptions reported as fatals for Unity and Flutter).
| **Important:** To get the most accurate calculations for crash-free metrics and to access the latest features inCrashlytics(like crash-free sessions),**make sure your app uses*at minimum* the following versions of theCrashlyticsSDK:**   
| Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

## Get crash-free metrics

For most apps, crash-free metrics are automatically calculated when you integrate theCrashlyticsSDK in your app. However, there are certain situations whereCrashlyticsdoesn't receive the necessary data to calculate crash-free metrics:

- Builds of your app that use an old version of theCrashlyticsSDK (learn about the minimum supported versions below)

- Builds of your app that disable automaticCrashlyticsdata collection and reporting (learn more in the["Impact of data collection settings on metrics quality"](https://firebase.google.com/docs/crashlytics/crash-free-metrics#impact-of-data-collection-settings)section of this page)

### SDK versions that support crash-free metrics

To get crash-free metrics, you must update your app to use aCrashlyticsSDK version that supports them. The following are the*minimum* supported versions of theCrashlyticsSDK that can power crash-free metrics:

- Apple platforms: v10.8.0+
- Android: v18.6.0+ (BoMv32.6.0+)
- Flutter: v3.4.5+
- Unity: 11.7.0+

You should automatically get crash-free metrics for the builds of your app that use an updated SDK version.

## What are the crash-free metrics?

Crash-free metrics include[crash-free*users*](https://firebase.google.com/docs/crashlytics/crash-free-metrics#crash-free-users)and[crash-free*sessions*](https://firebase.google.com/docs/crashlytics/crash-free-metrics#crash-free-sessions).

Crash-free metrics depend on two concepts: users and sessions. To get crash-free metrics for your app, you need to use aCrashlyticsSDK version that can send data about both of these concepts. Here's howCrashlyticsdifferentiates a user from a session:

- A**user** is an individual installation of your app on a device. For example, if a person has your app installed on several different devices, thenCrashlyticswill count each installation as a different and unique user.

- A**session**is a continuous period of time when a user is engaged with an application. A new session starts when the app is cold-started or the app is foregrounded after at least 30 minutes of backgrounding.

Also, crash-free metrics are only calculated for*fatal*events (and uncaught exceptions reported as fatals for Unity and Flutter).
| **Note:** Since crash-free metrics are only calculated for fatal events, if you filter the*Event type*in the console to only non-fatals or ANRs, then the charts for crash-free metrics will be blank.

### What is the crash-free*users*metric?

The**crash-free*users***metric is the percentage of users who engaged with your app during a selected time period but did not have a crash. This metric reflects the experience that your app delivers to a single user. It's frequently tracked as the key health metric for the entire app, when the goal is the overall user experience.

This metric may be specifically applicable to the following types of apps:

- **Apps with long and casual sessions**such as on-demand streaming apps, social media apps, or casual games, where the user can continue where they left off. Because users typically engage with these apps in longer, often multi-session experiences, maximizing the total number of crash-free users takes precedence over ensuring each individual session is flawless.

- **Apps with established user bases**such as well-established work apps or large-scale online platforms, where habit and need for these platforms outweigh the inconvenience of a crash.

### What is the crash-free*sessions*metric?

The**crash-free*sessions***metric is the percentage of sessions that happened during a selected time period and did not end in a crash. Sessions without crashes indicate overall reliability of an app and build user confidence. Tracking crash-free sessions is especially important in the early stages of a new release, when a crash during a user's first interaction could result in immediate frustration to the point of abandonment.

This metric is frequently the preferred metric for the following types of apps:

- **Apps with short and intense usage patterns**such as real-time gaming or time-sensitive streaming apps, where a crash in the middle of a critical moment can devastate the user.

- **Apps with significant consequences**such as financial apps or navigational apps, where the emphasis is on the end state of the experience. A crash in one of these apps can lead to significant problems, resulting in loss of trust in the app.

| **Note:** Crash-free sessions are only available for builds that use the following versions of theCrashlyticsSDK:  
| Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+

## Calculation of crash-free metrics

### How are crash-free*users*calculated?

The crash-free users value represents the percentage of users who engaged with your app but did***not***have a crash over a selected time period.

Here is the formula for calculating the crash-free users percentage. Its input values are provided by theCrashlyticsSDK, and they're based on the time period that you've selected from the drop-down menu in the upper-right of theCrashlyticsdashboard.

`CRASH_FREE_USERS_PERCENTAGE = 1 - (`<var translate="no">CRASHED_USERS</var>` / `<var translate="no">ALL_USERS</var>`)`

- <var translate="no">CRASHED_USERS</var>represents the total number of unique users who experienced a crash over the selected time period.

- <var translate="no">ALL_USERS</var>represents the total number of users who engaged with your app over the selected time period.

The crash-free users percentage is an**aggregation over time**, not an average.
| **Note** : If your app uses any of the following versions of theCrashlyticsSDK, thenCrashlyticsno longer usesGoogle Analyticsfor data to calculate crash-free users for builds that use these versions.  
| Apple platforms: v10.8.0+ \| Android: v18.6.0+ (BoMv32.6.0+) \| Flutter: v3.4.5+ \| Unity: 11.7.0+
|
| If your app uses an older version of theCrashlyticsSDK and thus depends onGoogle Analyticsfor the crash-free users calculation, then we strongly recommend that you update to use the latest version of theCrashlyticsSDK instead.

<br />

**View an example calculation**

<br />

For example, imagine your app has three users; we'll call them User A, User B, and User C. The following table shows which users engaged with your app each day and which of those users had a crash that day:

|                                 | Monday  | Tuesday | Wednesday |
|---------------------------------|---------|---------|-----------|
| Users who engaged with your app | A, B, C | A, B, C | A, B      |
| User that had a crash           | C       | B       | A         |

- On Wednesday, your crash-free users percentage is 50% (1 out of 2 users was crash-free).  
  *Two of your users engaged with your app on Wednesday, but only one of them (User B) had no crashes.*

- For the past 2 days, your crash-free users percentage is 33.3% (1 out of 3 users was crash-free).  
  *Three of your users engaged with your app over the past two days, but only one of them (User C) had no crashes.*

- For the past 3 days, your crash-free users percentage is 0% (0 out of 3 users were crash-free).  
  *Three of your users engaged with your app over the past three days, but zero of them had no crashes.*

<br />

<br />

The crash-free users value shouldn't be compared over different time periods. The probability of a single user experiencing a crash grows the more times they use your app, so the crash-free users value is likely to be smaller for longer time periods.

### How are crash-free*sessions*calculated?

The crash-free sessions value represents the percentage of sessions that happened in your app but did***not***have a crash over a selected time period.

Here is the formula for calculating the crash-free sessions percentage. Its input values are provided by theCrashlyticsSDK, and they're based on the time period that you've selected from the drop-down menu in the upper-right of theCrashlyticsdashboard.

`CRASH_FREE_SESSIONS_PERCENTAGE = 1 - (`<var translate="no">CRASHED_SESSIONS</var>` / `<var translate="no">ALL_SESSIONS</var>`)`

- <var translate="no">CRASHED_SESSIONS</var>represents the number of sessions that ended in a crash over the selected time period.

- <var translate="no">ALL_SESSIONS</var>represents the total number of sessions that happened in your app over the selected time period.

The crash-free sessions percentage is an**aggregation over time**, not an average.

## Impact of data collection settings on metrics quality

Depending on your data collection settings, your crash-free metrics may show low or zero values. Here are two common scenarios that can cause unreliable crash-free metrics:

<br />

- If you[enable opt-in reporting](https://firebase.google.com/docs/crashlytics/customize-crash-reports#enable-reporting)by disabling automatic crash reporting, crash information can only be sent toCrashlyticsfrom users who have explicitly opted into data collection. Thus, the accuracy of crash-free metrics will be affected sinceCrashlyticsonly has crash information from these opted-in users (rather than*all*your users). This means that your crash-free metrics may be less reliable and less reflective of the overall stability of your app.

- If you have automatic data collection disabled, you can use`sendUnsentReports`to send on-device cached reports toCrashlytics. Using this method will send*crash* data toCrashlytics, but not*sessions*data which causes the console charts to show low or zero values for crash-free metrics.