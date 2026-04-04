# Source: https://documentation.onesignal.com/docs/en/google-play-data-safety-requirements.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Play Data Safety Requirements

> Learn how to accurately complete the Google Play Data Safety form when using OneSignal. Understand what data is collected, how to disclose it, and ensure compliance with Google's privacy policies.

To publish or update your app on Google Play, you must complete the **Data safety** section in the **App Privacy** tab in the [Google Play Console](https://play.google.com/console/app/app-content/summary).

As OneSignal is a third-party service, you are responsible for disclosing how you handle user data when using OneSignal. Google's official guidance can be found [here](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#in_play_console).

By default, OneSignal collects:

* **In-app purchases**
* **App interactions** (e.g., session counts, durations, and notification clicks)

If you use OneSignal to collect emails, phone numbers, or additional custom data (via [Tags](./add-user-data-tags)),you must disclose those data types as well.

For details on handling user data, see [Handling Personal Data](./handling-personal-data).

## Data types and OneSignal behavior

✅ = Collected when using OneSignal
💡 = May be collected depending on your OneSignal usage
❌ = Not collected by OneSignal

| Category                     | Data Type                      | OneSignal Collection Behavior                                                                            |
| ---------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Location**                 | Approximate location           | ❌ Not collected                                                                                          |
|                              | Precise location               | 💡 Only if your app collects it and sends it to OneSignal                                                |
| **Personal info**            | Name                           | 💡 If collected via Tags or Outcomes                                                                     |
|                              | Email address                  | 💡 If added to OneSignal                                                                                 |
|                              | User IDs                       | 💡 If collected via Tags or Outcomes                                                                     |
|                              | Address                        | ❌ Not collected                                                                                          |
|                              | Phone number                   | 💡 If added to OneSignal                                                                                 |
|                              | Race and ethnicity             | ❌ Not collected                                                                                          |
|                              | Political or religious beliefs | ❌ Not collected                                                                                          |
|                              | Sexual orientation             | ❌ Not collected                                                                                          |
|                              | Other info                     | 💡 If collected via Tags or Outcomes                                                                     |
| **Financial info**           | User payment info              | ❌ Not collected                                                                                          |
|                              | Purchase history               | ✅ Collected if your app has in-app purchases                                                             |
|                              | Credit score                   | ❌ Not collected                                                                                          |
|                              | Other financial info           | ❌ Not collected                                                                                          |
| **Health and fitness**       | Health info                    | ❌ Not collected                                                                                          |
|                              | Fitness info                   | ❌ Not collected                                                                                          |
| **Messages**                 | Emails                         | ❌ Not collected                                                                                          |
|                              | SMS or MMS                     | ❌ Not collected                                                                                          |
|                              | Other in-app messages          | ❌ Not collected                                                                                          |
| **Photos and videos**        | Photos                         | ❌ Not collected                                                                                          |
|                              | Videos                         | ❌ Not collected                                                                                          |
| **Audio files**              | Voice or sound recordings      | ❌ Not collected                                                                                          |
|                              | Music files                    | ❌ Not collected                                                                                          |
|                              | Other audio files              | ❌ Not collected                                                                                          |
| **Files and docs**           | Files and docs                 | ❌ Not collected                                                                                          |
| **Calendar**                 | Calendar events                | ❌ Not collected                                                                                          |
| **Contacts**                 | Contacts                       | ❌ Not collected                                                                                          |
| **App activity**             | App interactions               | ✅ Collected: includes sessions and notification clicks                                                   |
|                              | In-app search history          | ❌ Not collected                                                                                          |
|                              | Installed apps                 | ❌ Not collected                                                                                          |
|                              | Other user-generated content   | 💡 If collected via Tags or Outcomes                                                                     |
|                              | Other actions                  | 💡 If collected via Tags or Outcomes                                                                     |
| **Web browsing**             | Web browsing history           | ❌ Not collected                                                                                          |
| **App info and performance** | Crash logs                     | ❌ Not collected                                                                                          |
|                              | Diagnostics                    | ❌ Not collected                                                                                          |
|                              | Other performance data         | ❌ Not collected                                                                                          |
| **Device or other IDs**      | Device or other IDs            | ❌ Does not collect GAID by default<br />💡 Collected if you use [Aliases](./aliases) to link identifiers |

## Required data types for OneSignal

You **must disclose** the following if you use OneSignal:

### Purchase history

If your app includes in-app purchases, disclose collection of **Purchase history** under **Financial info**.

<Frame caption="Data types: Purchase history">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2ba7aa4-purchase-type-financial-info.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=62f12ef7f7eac83abb9461d1da2aecd3" width="1527" height="522" data-path="images/docs/2ba7aa4-purchase-type-financial-info.png" />
</Frame>

<Frame caption="Collected and shared settings">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1acbea7-purchase-type-history-collected-shared.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=040dfdfc9a6695f2289987d94e453753" width="1527" height="522" data-path="images/docs/1acbea7-purchase-type-history-collected-shared.png" />
</Frame>

<Frame caption="Data processing settings">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/a1623fc-purchase-type-history-processing-data.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=761e1ea3aef6ac2a10c0fe6ff9d6d027" width="1527" height="777" data-path="images/docs/a1623fc-purchase-type-history-processing-data.png" />
</Frame>

<Frame caption="Analytics usage">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d5c78cf-required-data-types-purchase-history-analytics.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=dc8a3fcaaa05927431d87299e0a6ea25" width="1527" height="980" data-path="images/docs/d5c78cf-required-data-types-purchase-history-analytics.png" />
</Frame>

<Info>
  At a minimum, select “Analytics” for OneSignal. If you use OneSignal for other use cases, you must select those as well.
</Info>

### App interactions

Disclose collection of **App interactions** under the **App activity** section.

<Frame caption="Data types: App interactions">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/ed8b775-purchase-type-app-interactions.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=4ae4f74b1521e77bfd58b1bc39831941" width="1527" height="522" data-path="images/docs/ed8b775-purchase-type-app-interactions.png" />
</Frame>

<Frame caption="Collected and shared settings">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/017c88f-app-interactions-data-collected.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=bb2e55ed24cc56d7efcdb10b6544d490" width="1527" height="507" data-path="images/docs/017c88f-app-interactions-data-collected.png" />
</Frame>

<Frame caption="Data processing settings">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/8bf269a-app-interactions-data-processed-ephemerally.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=fa22d2d55358cfd90ae2291fe4242863" width="1527" height="777" data-path="images/docs/8bf269a-app-interactions-data-processed-ephemerally.png" />
</Frame>

<Frame caption="Analytics and developer communications">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/4144305-required-data-types-app-interactions-analytics-developer-communications.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=d3486477986ab608c1bf6b141d85f93d" width="1527" height="980" data-path="images/docs/4144305-required-data-types-app-interactions-analytics-developer-communications.png" />
</Frame>

<Info>
  Select both “Analytics” and “Developer communications” at a minimum. If additional data is collected through OneSignal, disclose it as well.
</Info>

## Preview of store listing

After completing your privacy selections, Google will generate a preview. If you've disclosed **Purchase history** and **App interactions**, your listing should look like this:

<Frame caption="Store listing preview">
  <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6be1a35-preview-data-safety.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=60d9eca04e934722981255032c87fa34" width="1527" height="1361" data-path="images/docs/6be1a35-preview-data-safety.png" />
</Frame>

## Keep your disclosure up to date

If your data collection practices change, revisit the **Data safety** section in the Play Console and update your disclosures.

***

Built with [Mintlify](https://mintlify.com).
