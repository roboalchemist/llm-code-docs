# Source: https://docs.buildnatively.com/natively-platform/features/notifications/firebase-notifications-advanced.md

# Firebase Notifications (Advanced)

Create a new Firebase Project

* Go to <https://console.firebase.google.com/>
* Click New Project, enter the project name

{% hint style="info" %}
You can use the same one for Push notifications or for Firebase Deep Links.
{% endhint %}

## **Ensure Firebase Cloud Messaging API (V1) is enabled**

In your project, click the **Gear icon** next to "Project Overview" in the top left of the left-hand menu and select **Project settings**. Select the **Cloud Messaging** tab.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FMotk4rRrlm1zweGjgfFi%2Ffirebase%20project%20settings.png?alt=media&#x26;token=2fec72d7-1a48-4f94-996f-08a6fe5e2ef1" alt=""><figcaption></figcaption></figure>

\
If **Firebase Cloud Messaging API (V1)** is disabled, then click the kebab menu icon on the top right corner and open the link.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FwXiR4wptkg68uA7kReYv%2Ffirebase%20enable%20fcm.png?alt=media&#x26;token=31dd898d-e894-4195-b6fb-3864386e1230" alt=""><figcaption></figcaption></figure>

\
On the subsequent page, click **Enable**. You may need to wait a few minutes for the action to propagate to Firebase systems.

{% hint style="info" %}
You can skip this step if you have already set up the [Notifications](https://docs.buildnatively.com/natively-platform/features/notifications/onesignal-notifications) feature.
{% endhint %}

## **(Only for iOS) Ensure the** "Push Notification" capabilities are enabled for your App.

1. Go to the [Apple Developer Identifiers](https://developer.apple.com/account/resources/identifiers/list) -> Find your app's Bundle ID. Click on it

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fl6cGh6eVnk7nvCJEChkt%2Fimage.avif?alt=media&#x26;token=423b5b65-d7f4-4884-b111-6c739e5a6d5a" alt=""><figcaption></figcaption></figure>

2. Scroll down and enable "Push Notifications". Click Save.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FVfRhYySPHvpeFoOxuIAc%2Fimage%20(1).avif?alt=media&#x26;token=41ce8d2b-ecc3-47ef-8cd1-431c35145dfd" alt=""><figcaption></figcaption></figure>

## **Add Android & iOS apps**

Please follow this guide: [Add Android & iOS apps](https://docs.buildnatively.com/natively-platform/features/deeplinks/firebase#add-android-and-ios-apps)

Download the GoogleService-Info.plist and the google-services.json files on this step.

{% hint style="info" %}
You can skip this step if you have already set up the [Firebase Deep Links](https://docs.buildnatively.com/natively-platform/features/deeplinks/firebase)
{% endhint %}

## Upload your APNs authentication key (iOS) <a href="#upload_your_apns_authentication_key" id="upload_your_apns_authentication_key"></a>

Please use the [following guide](https://docs.buildnatively.com/guides/generate-ios-push-key) to generate the authentication key is you do not already have one.

1. Inside your project in the Firebase console, select the gear icon, select **Project Settings**, and then select the **Cloud Messaging** tab.
2. In **APNs authentication key** under **iOS app configuration**, click the **Upload** button.
3. Browse to the location where you saved your key, select it, and click **Open**. Add the key ID for the key and click **Upload**.

## Enable Firebase Push notifications on the Natively platform

* Turn the switcher on
* Upload the iOS Config file (GoogleService-Info.plist)
* Upload the Android Config file (google-services.json)
* Click the 'Save' button to save your changes

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FpzUXIN5Zv6GaFWPes1fV%2Ffirebase%20push%20notifications.png?alt=media&#x26;token=b4cdab1e-53c1-4f92-975d-95972433d16e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you have already enabled the [Firebase Deep Links](https://docs.buildnatively.com/natively-platform/features/deeplinks/firebase) feature for your app, you may see the iOS Config file and the Android Config file uploaded. That's because these files are the same for the Firebase Notifications feature.
{% endhint %}
