# Source: https://documentation.onesignal.com/docs/en/authorize-onesignal-to-send-huawei-push.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Huawei authorization

> Step-by-step guide to connect your Huawei app to OneSignal for push notifications, including PushKit setup, API key configuration, and Huawei's optional message self-classification for apps with users in China.

## Requirements

To enable push notifications on Huawei Android devices using OneSignal, you'll need:

* A [Huawei Developer Account](https://developer.huawei.com/consumer/en/console)
* An Android mobile app registered in [Huawei's AppGallery Connect](https://developer.huawei.com/consumer/en/doc/distribution/app/agc-create_app)
* A [OneSignal Account](https://onesignal.com/)
* (Optional) [Huawei Self-Classification Rights](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1653845862216) if targeting users in China and needing more precise message categorization via the `Huawei_category` API field

***

## Setup

### 1. Enable PushKit

See [Huawei's docs on Push Kit](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html#0).

### 2. Get your Huawei Push credentials

Open [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html) and select your app/project.

<Frame caption="Navigate to your App in AppGallery Connect">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/f36e4ff-Huawei_AppGallery_Connect_LandingPage_With_Myapps_highlight.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=b30a9076c3775da810a8d90cb0648f16" width="1269" height="805" data-path="images/docs/f36e4ff-Huawei_AppGallery_Connect_LandingPage_With_Myapps_highlight.png" />
</Frame>

Go to **In-App Purchases** under **All services > Earn**. Copy the following:

* **Package Name**
* **Client ID**
* **Client Secret**

<Frame caption="Copy your Package Name, Client ID, and Client Secret">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/fc70624-huawei.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=ebbbda6c47d3b6d968a05bc285d20f5f" width="1847" height="849" data-path="images/docs/fc70624-huawei.png" />
</Frame>

### 3. Add credentials to OneSignal

In the OneSignal dashboard, go to your app **Settings > Push & In-App > Huawei Android (HMS)**.

<Frame caption="Select Huawei Android in OneSignal">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/huawei-android-settings.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=9176643dd1ce25e5fc083be7346c2249" width="2420" height="1770" data-path="images/docs/huawei-android-settings.png" />
</Frame>

Click **Activate** and paste your credentials:

* **Package Name**
* **Client ID** (into **App ID** field)
* **Client Secret** (into **App Secret** field)

Then click **Next**.

<Frame caption="Enter Huawei Push credentials in OneSignal">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/huawei-configuration.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=362d6263e48199ba542fbcb72d30e0a8" width="2420" height="1770" data-path="images/docs/huawei-configuration.png" />
</Frame>

### 4. (Optional) Apply for Huawei’s Self-Classification Rights

Huawei requires AppGallery apps sending notifications to **users in China** to categorize messages. They offer **automatic classification**, but **self-classification** gives more control and higher send limits for critical message types.

#### How to apply

1. Follow Huawei’s [Self-Classification application guide](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-classification-0000001149358835#section1653845862216).
2. Once approved, use the `Huawei_category` field in the OneSignal API to classify your messages.

#### Supported `Huawei_category` values

| Category          | Description                        |
| ----------------- | ---------------------------------- |
| `IM`              | Instant messaging                  |
| `VOIP`            | Voice-over-IP services             |
| `SUBSCRIPTION`    | Subscribed content notifications   |
| `TRAVEL`          | Travel info (e.g., ticket updates) |
| `HEALTH`          | Health and wellness updates        |
| `WORK`            | Work-related reminders             |
| `ACCOUNT`         | Account activity alerts            |
| `EXPRESS`         | Logistics/delivery updates         |
| `FINANCE`         | Financial/banking alerts           |
| `DEVICE_REMINDER` | Device-level system reminders      |
| `MAIL`            | Email client messages              |
| `MARKETING`       | Marketing or promotional content   |

<Note>
  Default category is `MARKETING`, which is limited to 2–5 sends/day depending on [third-level classifications](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/message-restriction-description-0000001361648361#section199311418515).

  **Important:** [Classification violations](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/volation-classification-violation-penalty-criteria-0000001356540133) may lead to penalties or delivery restrictions.
</Note>

***

## Huawei badges

OneSignal supports setting app icon badge counts on Huawei devices via the API and dashboard. Use the `huawei_badge_class`, `huawei_badge_set_num`, and `huawei_badge_add_num` parameters when creating push notifications.

See [Badges](./badges#huawei-badges) for full details and examples.

***

<Check>
  You're now authorized to send Huawei push notifications using OneSignal!
  Next steps:

* [Integrate the OneSignal SDK](./mobile-sdk-setup)
</Check>

***

Built with [Mintlify](https://mintlify.com).
