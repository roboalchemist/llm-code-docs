# Source: https://docs.buildnatively.com/guides/setup-one-signal-app.md

# Setup One Signal App

{% hint style="warning" %}
This page is no longer being updated. Please refer to our [Push Notifications - OneSignal](https://docs.buildnatively.com/guides/integration/push-notifications-onesignal) for current configurations and support.
{% endhint %}

{% hint style="warning" %}
If you have 2 apps (iOS and Android) for 1 website, you need 1 OneSignal application with 2 platforms enabled.
{% endhint %}

## Android 🤖

### Prerequisites

* A [Firebase account](https://firebase.google.com/)
* A [OneSignal Account](https://onesignal.com/), if you do not already have one.

### Push Notification Setup for Android

1. [Generate a Google Server API Key](https://documentation.onesignal.com/docs/generate-a-google-server-api-key)
2. [Add Android to the OneSignal app target SDK](https://documentation.onesignal.com/docs/mobile-sdk-setup#android)
3. Add *OneSignal App Id* to the [Push Notification](https://documentation.onesignal.com/docs/mobile-sdk-setup#android) section on the Native Feature step

## iOS 🍏

### Prerequisites

* **Apple .p8 Auth Key + Key ID + Team ID + Bundle ID.** \
  Please use the [following guide](https://docs.buildnatively.com/guides/generate-ios-push-key) to do that.
* Create [One Signal Account](https://dashboard.onesignal.com/signup).

### Create App (App ID)

* Open One Signal's [**Apps Dashboard**](https://app.onesignal.com/apps)
* Click **New App/Website**
* Enter the name of your app in **Name of your app or website** field
* Select **Apple iOS (APNs)**
* Click **Next**
* **Select .p8 Auth Key**

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FH7PaX0gPGeSnJN97yuLc%2Fimage.png?alt=media&#x26;token=9e2fef9a-56c1-4a25-8de6-1514481847c0" alt=""><figcaption></figcaption></figure>

* Upload the .p8 key you've created, and enter a [Team ID, Key ID, and Bundle ID](https://docs.buildnatively.com/generate-ios-push-key#gather-all-required-data).&#x20;
* Click **Save & Continue**
* Select target SDK **Native iOS** and click **Save & Continue**
* Copy your **App ID** and click **Done**

{% hint style="warning" %}
IMPORTANT For iOS. We don't support p12 files anymore! Please use p8 key instead!
{% endhint %}
