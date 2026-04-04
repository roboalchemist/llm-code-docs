# Source: https://docs.buildnatively.com/natively-platform/features/analytics/appsflyer.md

# AppsFlyer

AppsFlyer is a cloud-based mobile attribution and marketing analytics platform which assists app marketers with campaign management and conversion tracking. Its key features include customer journey mapping, attribution modeling, audience segmentation, social media metrics, and retention tracking.

{% hint style="danger" %}
If you have In-App Purchases enabled for your app, AppsFlyer will automatically track them (You can't disable this)
{% endhint %}

{% embed url="<https://youtu.be/LY_CzWvTEvs>" %}

To configure your app to work with AppsFlyer, you need to do the following steps:

1. Create an AppsFlyer account [here](https://www.appsflyer.com/start/)
2. [Create and set up](#how-to-set-up-an-ios-app-in-appsflyer) the AppsFlyer iOS app.
3. [Create and set up](#how-to-set-up-an-android-app-in-appsflyer) the AppsFlyer Android app.
4. [Test](https://support.appsflyer.com/hc/en-us/articles/360001559405-Testing-the-SDK-integration-for-marketers) your integration

## How to set up an iOS app in AppsFlyer?

Go to [My Apps](https://hq1.appsflyer.com/apps/myapps) page, and click "Add app" button (top right corner)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FhBcHhxwR551NnbJXIZgF%2Fimage.png?alt=media&#x26;token=977cd6a2-8d3c-4cc0-805e-13f805ed30d7" alt=""><figcaption></figcaption></figure>

Then Select "iOS, tvOS, MacOS" platform. Also, you need to provide information about your App Store status. If you've already published the app select the "In Store" option. Otherwise, "Pending approval/not published.

After that, Select the store country and enter your App ID (It can be found on Natively platform "Publish -> iOS Build -> App Store App Id" or in your's AppStoreConnect account)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FI3khHo05CNVBgXDHZqyp%2Fimage.png?alt=media&#x26;token=5320437b-2537-4f02-8ae8-5b049f221f93" alt=""><figcaption></figcaption></figure>

In the next step, select a relevant currency and if your app is targeted to a kids audience.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F8pxOYcA11ZhQvxLYi7yX%2Fimage.png?alt=media&#x26;token=1b890bd4-d9e3-42d7-9d46-893683cbb1fd" alt=""><figcaption></figcaption></figure>

After that, you will see a Success screen and a Dev Key value, copy it&#x20;

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FndmnYjKWn7TGsv4PH77r%2Fimage.png?alt=media&#x26;token=4e60745a-4c7a-4266-aa04-c94c78a113b0" alt=""><figcaption></figcaption></figure>

Go back to the Natively platform and paste this value. Also, do not forget to fill [Permission description](https://developer.apple.com/app-store/user-privacy-and-data-use) for iOS.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FimxrWITQgrajqYx1WHdT%2Fimage.png?alt=media&#x26;token=7a378b77-4e6c-4e59-96ef-cecdf349c1cb" alt=""><figcaption></figcaption></figure>

Click Save, and do not forget to rebuild your app after all changes!

{% hint style="danger" %}
Important, the dev key is the same for iOS and Android. if you have both platforms you can just enter it once. But you need to rebuild each app separately.
{% endhint %}

## How to set up an Android app in AppsFlyer?

Go to [My Apps](https://hq1.appsflyer.com/apps/myapps) page, and click "Add app" button (top right corner)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FhBcHhxwR551NnbJXIZgF%2Fimage.png?alt=media&#x26;token=977cd6a2-8d3c-4cc0-805e-13f805ed30d7" alt=""><figcaption></figcaption></figure>

Then Select "Android, AndroidTV, Fire" platform. Also, you need to provide information about your Google Play status. If you've already published the app select the "In Store" option. Otherwise, "Pending approval/not published.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FPcigCsUSOzD9DGSTy1hB%2Fimage.png?alt=media&#x26;token=071a3d0b-9188-4227-a9c0-3970dc60dd3d" alt=""><figcaption></figcaption></figure>

If you've selected "In store" option on previous step, you need to enter your app URL

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FofddpVrYoWq1TJ0RojcV%2Fimage.png?alt=media&#x26;token=5007199b-fed1-4014-9af1-e6dea2a1511d" alt=""><figcaption></figcaption></figure>

Otherwise, enter a package id, that can be found on the Natively platform "Publish -> Android Build -> Bundle Identifier"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FxalBaXwLwwSWuj3x2jKE%2Fimage.png?alt=media&#x26;token=b55809d7-1baa-437f-b206-5573f622794b" alt=""><figcaption></figcaption></figure>

In the next step, select a relevant currency and if your app is targeted to a kids audience.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FXxokgM6dUF1XIqqc3LW5%2Fimage.png?alt=media&#x26;token=d5f27baf-a73b-4fef-afa1-46b09e4e21ba" alt=""><figcaption></figcaption></figure>

After that, you will see a Success screen and a Dev Key value, copy it&#x20;

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FndmnYjKWn7TGsv4PH77r%2Fimage.png?alt=media&#x26;token=4e60745a-4c7a-4266-aa04-c94c78a113b0" alt=""><figcaption></figcaption></figure>

Go back to the Natively platform and paste this value.

{% hint style="danger" %}
Important, the dev key is the same for iOS and Android. if you have both platforms you can just enter it once. But you need to rebuild each app separately.
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FOFlteDQqq4hdYs1ANPZP%2Fimage.png?alt=media&#x26;token=e4e5afd1-fe05-4599-8c4b-ec902a6441e5" alt=""><figcaption></figcaption></figure>

Click Save, and do not forget to rebuild your app after all changes!
