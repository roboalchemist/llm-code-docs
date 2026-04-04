# Source: https://docs.buildnatively.com/guides/setup-admob-app.md

# Setup Admob App

{% hint style="info" %}
This page is no longer being updated. Please refer to our [admob-integration-guide](https://docs.buildnatively.com/guides/integration/admob-integration-guide "mention") for current configurations and support.
{% endhint %}

[Google AdMob](https://admob.google.com) makes it easy for developers to earn money from their mobile apps with high-quality ads. AdMob maximizes the value of every impression by combining global advertiser demand, innovative ad formats, and advanced app monetization technology.

## Prerequisites

If you are new to Admob, it's recommended you read this first: [What is Admob?](https://admob.google.com/home/resources/what-is-admob/)

## Admob Integration

Integrating the Admob in your app comprises of the following steps:

### **1. Admob initial setup**

Follow the guide by the Admob team to create and configure your app.

{% embed url="<https://support.google.com/admob/answer/9989980?hl=en>" %}

Or follow this short tutorial:

1. Create your app by clicking the "ADD YOUR FIRST APP" button.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FbghTM56fRnog5GP5VizP%2F1.png?alt=media&#x26;token=12006427-c50d-47cd-a92f-12691e0adb87" alt=""><figcaption></figcaption></figure>

2. Select Platform (iOS/Android) and if your app is already listed in GooglePlay or AppStore.\
   (If you have Android and iOS, you will need to add each app separately to Admob)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FFn1vu5cdBZEzUBh7rQ4z%2F2.png?alt=media&#x26;token=974e9819-acc6-41d7-ae08-b1443dcbf3bb" alt=""><figcaption></figcaption></figure>

2. (1) If your app is already published, enter it's Bundle ID and click "ADD"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FfCZ7rEfHsdu26KXqdQkW%2F3.png?alt=media&#x26;token=35263e8b-4701-40f2-9a67-d9737093a603" alt=""><figcaption></figcaption></figure>

Make sure to link the correct app and click "ADD APP"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FnZZC7RmxDzL3IkoU1CEc%2F4.png?alt=media&#x26;token=ca2118ae-9e95-4644-ab2d-d4165e062521" alt=""><figcaption></figcaption></figure>

2. (2) Otherwise, if your app is not published, enter the App name and click "ADD APP".

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F971PF2yUTe2LLwda6wYJ%2F3-1.png?alt=media&#x26;token=cf1c7836-e896-493e-94bd-595a322563c4" alt=""><figcaption></figcaption></figure>

3. Copy the App ID and go back to the Natively dashboard.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FN5UUXc2kAcBXfHr9DcxK%2F5.png?alt=media&#x26;token=3b76dd72-0439-4f6b-a4f0-8cba4c834481" alt=""><figcaption></figcaption></figure>

### 2. Connect Admob Apps with your Natively App

After successfully creating an Android or iOS app in the Admob, you need to link it with the Natively. To do that, follow these steps:

1. Open your Natively's app dashboard from the desktop
2. Go to **Features -> Admob** and enable it.
3. Enter your **App ID** (that you've copied in Admob) to relevant fields in the Natively dashboard.&#x20;

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F93CuJle5VqsePzj8Dx7H%2F5.png?alt=media&#x26;token=a559d47e-3d04-4e5f-ae9a-220fce2a1a55" alt=""><figcaption></figcaption></figure>

And finally, order a new build. We will inject the following keys into your app bundle.

### 3. Add payment info

### 4. Development

{% content-ref url="integration/admob" %}
[admob](https://docs.buildnatively.com/guides/integration/admob)
{% endcontent-ref %}

### 5. Testing

First, you need to add the test device. Go to "Settings" -> "Test devices" and click "ADD TEST DEVICE"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FPbHn3rdwJJ1XuQsfqQ18%2Ftesting-1.png?alt=media&#x26;token=0ac51312-5567-4b8c-8bbe-a225a4f69cd3" alt=""><figcaption></figcaption></figure>

Fill in the device name, platform, and IDFA.&#x20;

To get your device ID/IDFA you can download the AppsFlyer app for [Android](https://play.google.com/store/apps/details?id=com.appsflyer.android.deviceid\&hl=en\&gl=US) and [iOS](https://apps.apple.com/us/app/my-device-id-by-appsflyer/id1192323960)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FJScTyUEhmY8Cf1lBS3Y8%2Ftesting-2.png?alt=media&#x26;token=91770901-c594-41c3-ab02-6390c32de47d" alt=""><figcaption></figcaption></figure>

Next, you can start testing your app. Please read the Admob testing guides:

* [Testing Android app](https://developers.google.com/admob/android/test-ads)
* [Testing iOS app](https://developers.google.com/admob/ios/test-ads)

### 6. Release

Make sure to replace testing Unit IDs and create your own:

{% embed url="<https://support.google.com/admob/answer/6128738?hl=en&sjid=11000667129848669269-EU>" %}

After finishing development, you will need to submit your app to AppStore / GooglePlay get it approved, and then click "Add Store". It will take \~1 day for the Admob team to review your app.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FClJBqizoXseptHyMr1uM%2Fimage.png?alt=media&#x26;token=f22d9adc-3baa-4ba7-9e56-aaa22e5bcead" alt=""><figcaption></figcaption></figure>

If you have more questions, please read the Admob FAQ page:&#x20;

{% embed url="<https://support.google.com/admob/?hl=en&sjid=11000667129848669269-EU#topic=7384409>" %}
