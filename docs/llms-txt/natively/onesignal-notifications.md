# Source: https://docs.buildnatively.com/natively-platform/features/notifications/onesignal-notifications.md

# OneSignal Notifications

{% hint style="warning" %}
This page is no longer being updated. Please refer to our [Push Notifications - OneSignal](https://docs.buildnatively.com/guides/integration/push-notifications-onesignal) for current configurations and support.
{% endhint %}

[Notifications](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/) can give people timely and important information, whether the device is locked or in use. For example, notifications can signal when a message arrives, an event is about to occur, or there’s a status change.

To configure your app to work with push notifications, you need to do the following steps:

1. [Setup OneSignal App](https://docs.buildnatively.com/guides/setup-one-signal-app)
2. Enable the Push Notification feature.&#x20;
3. Enter all relevant push notification information in the Natively dashboard.
   1. **(Only for iOS) Permission description** - The permission description text should explain to the user why your app needs that permission. Refer to [**Apple's guidelines** ](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/)to avoid potential **rejection**.
   2. **One Signal App Id** - App ID used by the One Signal service to send push notifications.
   3. **(Optional) Push Auto Register (v2.12.0) -** Automatically calls Push Notification permission on app launch
   4. **Custom Notification Sound** - can be used later to send push with custom sound.
4. **(Only for iOS)** Enable "Push Notification" capabilities for your App.
   1. Go to the [Apple Developer Identifiers](https://developer.apple.com/account/resources/identifiers/list) -> Find your app's Bundle ID. Click on it<br>

      <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FndgqqyPjbNL0ctHoni9s%2Fimage.png?alt=media&#x26;token=2395942f-0dae-4b31-b8ea-658a2c9b4b4a" alt=""><figcaption></figcaption></figure>
   2. &#x20;Scroll down and enable "Push Notifications". Click Save.<br>

      <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FzcVMfwH5Ve6UplsGFPFi%2Fimage.png?alt=media&#x26;token=9e2aeb31-475d-40b8-86fd-557c0c91c784" alt=""><figcaption></figcaption></figure>
5. Rebuild your application

{% hint style="warning" %}
If you have 2 apps (iOS and Android) for 1 website, you need **1** OneSignal application with 2 platforms enabled.
{% endhint %}

## How to use Push Notifications?

{% content-ref url="../../../guides/integration/push-notifications-onesignal" %}
[push-notifications-onesignal](https://docs.buildnatively.com/guides/integration/push-notifications-onesignal)
{% endcontent-ref %}
