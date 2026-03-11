# Source: https://docs.buildnatively.com/guides/testing-and-submitting-your-app.md

# Testing & Submitting your app

* [Android](#android)
* [iOS](#ios)

## Android 🤖

### Testing on your device (APK)

You can simply [install](https://www.lifewire.com/install-apk-on-android-4177185) an APK file sent to your email after your app was successful build.

### Submitting the app to Google Play (AAB)

[How to submit your app to Google Play?](https://magecomp.com/blog/submit-app-to-google-play-store/)

**Note**: If you are submitting your app using a Personal Google Developer Account, [Google requires](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en) mandatory pre-launch testing.

* You must successfully pass a 14-day test period with a minimum of 12 testers in the Closed Test track before your app can be submitted for review.&#x20;

**Need Testers?**

If you require testers to fulfill this requirement, we can help. Please send your request to `help@buildnatively.com` from the email address associated with your Natively account.

## Privacy Policy Errors/Warnings

1. Advertising ID

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FGwIP8vXbxIIeT8WFrHdC%2FSCR-20230130-nmb.png?alt=media&#x26;token=a47da29b-2bc1-430e-af95-66808c3b3f0a" alt=""><figcaption></figcaption></figure>

To fix this warning, go to your Google Play Console, select the app which you are trying to upload, then on the left side, go to `Policy and programs -> App content` in there, fill the `Advertising ID form`.

### CAMERA/AUDIO etc. declaration

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FNvAEEvIQtfnSSSS5b6sm%2FSCR-20220802-omc.png?alt=media&#x26;token=12392f85-9003-4472-affc-c51a1717f10b" alt=""><figcaption></figcaption></figure>

To fix this error, go to your App Page in Google Play -> Policy -> App Contact -> (Under Privacy Policy), click Start

### App Bundle is signed with the wrong key

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fd2I6VY52MRIx1rTAMI3l%2Fimage.png?alt=media&#x26;token=84c3c0fc-7b0a-432a-92d3-a410494804cb" alt=""><figcaption></figcaption></figure>

It means that you've already uploaded an APK file of the app that was built not with Natively (Or previously created Natively app)&#x20;

To migrate your app on Natively please fill out this <https://tally.so/r/wLZexO> (And provide all requested data). If you don't have all this information, please get in touch with our support in a chat or at <help@buildnatively.com>

Migration request usually takes up to 24hrs. Be patient :)

##

## iOS 🍏

### Testflight

After you've successfully received your build in AppStoreConnect you need:

* Open your app in AppStoreConnect and go to the TestFlight tab.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-52fed76d401a17df16e6a2e26e339216257b2e92%2FSCR-20220530-us8.png?alt=media)

* Create a new **Internal Testing** group

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-678bac33be19e39db4d3913a143042ca0e5a426e%2FSCR-20220530-uxs.png?alt=media)

* Add **Testers** to this group

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-5fe2eafed1f57e9218155bfc0645bae10137a726%2FSCR-20220530-uy1.png?alt=media)

* You will receive an email from AppStoreConnect with an invite to TestFlight with a link to the app.

### App Store submission

{% embed url="<https://help.apple.com/app-store-connect/#/dev34e9bbb5a>" %}
How to publish your app?
{% endembed %}

After your build was successfully delivered to the App Store Connect and you test the app through [TestFlight](#testflight) it's to submit it to App Store.

Go to your app's page in App Store Connect, and select the **App Store** tab.

![](https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fgit-blob-fb571489d15ca3835772ad12527deb54f58e1158%2Fimage.png?alt=media)

You need to fill out all the required information on this page. Each field has a "(?)" button that contains a more detailed explanation. If you have any issues/questions, check out this [guide](https://blog.instabug.com/how-to-submit-app-to-app-store/).

Here are a few recommendations:

* If you have **In-App purchases** implemented, check a release [checklist](https://www.revenuecat.com/docs/launch-checklist) from RevenueCat.
* **Screenshots** - dimensions should be 1242x2688, 2688×1242, 1284×2778, or 2778×1284. Format PNG/JPEG. You can do it yourself or use such services like [this](https://www.appstorescreenshot.com/).
* **Social Login** - If your app has a login with social media (like Facebook, Google, Twitter, LinkedIn, etc.). Apple [requires](https://developer.apple.com/app-store/review/guidelines/#sign-in-with-apple) such apps to add Sign In with Apple. Of course, you can hide it during the review process, but you need to understand that it violates AppStore guidelines. All responsibility for such action is on your side.
* **App Privacy** - If you're using Push Notifications [this](https://documentation.onesignal.com/docs/apple-app-privacy-requirements) guide from One Signal team can be useful.
