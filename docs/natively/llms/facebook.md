# Source: https://docs.buildnatively.com/natively-platform/features/analytics/facebook.md

# Facebook

Facebook Analytics is the data and tools you need to track your brand's performance on the world's most popular social network. Tracking Facebook analytics helps you understand your past performance and tweak your future strategy.

To configure your app to work with Facebook, you need to do the following steps:

1. Create a Facebook account (If you didn't have it before)
2. [Create](#how-to-create-a-facebook-app) a Facebook app.
3. [Set up](#how-to-setup-ios) the iOS app.
4. [Set up](#how-to-setup-android) the Android app.

{% embed url="<https://youtu.be/Opj836huIdM>" %}

## How to create a Facebook app?

Go to [My Apps](https://developers.facebook.com/apps/) page, and click "Create App" button (top right corner)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FMjZLZcLbdVPqsLaNpKjG%2Fimage.png?alt=media&#x26;token=4ee99539-378c-4589-a104-9a2c09b94f5e" alt=""><figcaption></figcaption></figure>

Select app type as "None"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FpAzxtjSHzderY6EGxLGY%2Fimage.png?alt=media&#x26;token=fd058f2d-bf86-49e8-b82b-ea2e94c081f5" alt=""><figcaption></figcaption></figure>

Fill out the app name and contact email

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FgoZ8HAJtJ7n4lJBenZ0j%2Fimage.png?alt=media&#x26;token=cb859df1-233b-4368-9d9d-085adc711906" alt=""><figcaption></figcaption></figure>

The first part is done, now we need to setup iOS and/or Android app(s)

### How to set up iOS?

Go to "Settings -> Basic" page

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fjyy69INNwsUU4AvehMVC%2Fimage.png?alt=media&#x26;token=fe18f08a-5761-4950-8270-551e3a48ba2e" alt=""><figcaption></figcaption></figure>

Scroll down and click "Add platform", select "iOS" and click "Next"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FofHMlGVlNkOnlgwCy5nE%2Fimage.png?alt=media&#x26;token=434f0f94-94d2-4fda-9f58-d48354995892" alt=""><figcaption></figcaption></figure>

Enter Bundle ID. It can be found on the Natively platform: Publish -> iOS Build -> Bundle Identifier

Enter iPhone/iPad Store ID. It can be found on the Natively platform: Publish -> iOS Build -> App Store App Id (This value is the same for iPhone and iPad apps if you have iPad support [enabled](https://docs.buildnatively.com/settings#ipad-support-only-for-ios))

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FYnPJjEPcFuDZT1TdS7u0%2Fimage.png?alt=media&#x26;token=5f1c45d8-37e7-4cc3-82d1-f78333d51dd4" alt=""><figcaption></figcaption></figure>

Click "Save changes"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FxDUxOW5RCdV8rfGltVzI%2Fimage.png?alt=media&#x26;token=13bba0e7-1b80-4554-81f5-1fb015554d47" alt=""><figcaption></figcaption></figure>

At the next step, we need to go to the Advanced settings, copy "Client token" and App ID

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FCBpcjI17owVixnaUZdrK%2Fimage.png?alt=media&#x26;token=300b88ec-0446-4e54-9a4c-8bed09713b1f" alt=""><figcaption></figcaption></figure>

Paste this value to the Natively platform. Also, do not forget to fill [Permission description](https://developer.apple.com/app-store/user-privacy-and-data-use) for iOS.

Click Save, and rebuild your iOS app after all changes!

{% hint style="danger" %}
Important, the App ID and Client Token are the same for iOS and Android. if you have both platforms you can enter it once. But you need to rebuild each app separately.
{% endhint %}

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FXyPklbBevAArK3WL8b9J%2Fimage.png?alt=media&#x26;token=32d0fd83-80d7-4879-85df-f6d1bcc62bd7" alt=""><figcaption></figcaption></figure>

### How to set up Android?

Go to "Settings -> Basic" page

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fjyy69INNwsUU4AvehMVC%2Fimage.png?alt=media&#x26;token=fe18f08a-5761-4950-8270-551e3a48ba2e" alt=""><figcaption></figcaption></figure>

Scroll down and click "Add platform", select "Android" and click "Next"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FLeEQqCpENS5tVecaT81n%2Fimage.png?alt=media&#x26;token=9eb5f267-2b8c-42e2-ba10-36f98bf6469c" alt=""><figcaption></figcaption></figure>

Select Google Play in a list of stores (Natively officially supports only Google Play, you can select other options on your own risk)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fvth0OJduQV2TGoSRFPxj%2Fimage.png?alt=media&#x26;token=9a08ae13-a3b4-4819-8f75-ef4505f43a70" alt=""><figcaption></figcaption></figure>

At that point, you need to enter a key hash. We will explain in next step how to get it.

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FONTACZDFsCWl6dbYgXQk%2Fimage.png?alt=media&#x26;token=dd33b375-96e7-43a3-9ef5-300b6f811cab" alt=""><figcaption></figcaption></figure>

To get a key hash value you need:&#x20;

1. Make sure you've already uploaded a first build to Google Play developer console.
2. Go to Google Play console and navigate to App Page -> Setup -> App Integrity
3. Scroll down and copy SHA-1 certificate fingerprint value (Upload & Publish keys certificates)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F0vvo5MKXX9ZeHudrgmhF%2FSCR-20240215-jla.png?alt=media&#x26;token=e254b345-1cda-4d34-b78c-297bd3068120" alt=""><figcaption></figcaption></figure>

1. Navigate to <https://base64.guru/converter/encode/hex>
2. Enter your SHA-1 value and click "Convert Hex to Base64"
3. Copy Base64 value

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F1K2mXCPhPD1R4yx9mmIF%2Fimage.png?alt=media&#x26;token=0a0542a5-4164-4b30-8d3e-5064e355ab4b" alt=""><figcaption></figcaption></figure>

**Do the same for 2nd ^**

Paste 2 values in the "Key hashes" field

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FBOTrQhnLxudx8sjfYTgW%2FSCR-20240215-jm3.png?alt=media&#x26;token=47edc14b-b026-4b5b-af96-74bfc5e040e2" alt=""><figcaption></figcaption></figure>

After that, on the same page, you need to enter your Package Name and Class Name

1. Package Name: Publish -> Android Build -> Bundle Identifier
2. Class Name: for Natively 2.0 "com.base.app.Core.JasonViewActivity" \
   or for Natively 3.0 "{your bundle id}.MainActivity" e.g: "com.AxdfrerA.natively.MainActivity"
3. Click "Save changes"

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FlHKSpHza9OCYAyTDClql%2Fimage.png?alt=media&#x26;token=eabe252d-6047-49ba-ad35-e520da0db721" alt=""><figcaption></figcaption></figure>

At the next step, we need to go to the Advanced settings, copy "Client token" and App ID

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FCBpcjI17owVixnaUZdrK%2Fimage.png?alt=media&#x26;token=300b88ec-0446-4e54-9a4c-8bed09713b1f" alt=""><figcaption></figcaption></figure>

Paste this value to the Natively platform.

{% hint style="danger" %}
Important, the App ID and Client Token are the same for iOS and Android. if you have both platforms you can enter it once. But you need to rebuild each app separately.
{% endhint %}

Click Save, and rebuild your Android app after all changes!

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FQ1XflTTZfkumjDzXHxvE%2Fimage.png?alt=media&#x26;token=fccd728a-4830-4237-9d04-c41065ee415e" alt=""><figcaption></figcaption></figure>
