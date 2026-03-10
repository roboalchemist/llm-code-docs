# Source: https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/index-first-party.md.txt

# Tutorial: Use first-party data to measure Google Ads conversions from your iOS app campaigns

### **Solution tutorial**

Google's on-device conversion measurement improves the number of observable
conversions from your iOS app campaigns while keeping users' personal data
private. In this tutorial, you'll learn how the solution works and follow along
with the steps needed to implement it.

#### How does this work?

On-device conversion measurement helps measure app installs and in-app actions
from your iOS app campaigns. The Google Analytics for Firebase SDK
performs on-device attribution using a user's identity provided by your app's
sign-in experience. The user's identity is hidden through our on-device
conversion approach so that no personally identifiable information ever leaves
the user's device.

To use this technology, you need a consented, user-provided email address or
phone number. Through the `initiateOnDeviceConversionMeasurement()` API, the
email address or phone number is used by the Google Analytics for
Firebase SDK for attribution such that this personal data is never sent off the
device in a way that can identify the user or device. The feature works on apps
running iOS 12+.

You can use Firebase Authentication to allow users to sign in to your app using
one or more sign-in methods. Once integrated with Firebase Authentication, you can get
the signed-in user's email or phone number to send to the Google Analytics
for Firebase SDK.

## Products and features used in this tutorial

|---|---|
| Google Ads > [Google Ads](https://firebase.google.com/docs/ads) lets you drive installs, gain deep insights into ad conversions, and run targeted ad campaigns using Google Analytics audiences to engage your user base. Google Analytics > [Google Analytics](https://firebase.google.com/docs/analytics) gives you insight into user engagement, retention, and monetization metrics like total revenue, AdMob revenue, purchase revenue, and much more. It also allows you to create user audiences and segments. | Firebase Authentication > [Firebase Authentication](https://firebase.google.com/docs/auth) provides backend services, easy-to-use SDKs, and ready-made UI libraries to authenticate users to your app. It supports authentication using passwords, phone numbers, popular federated identity providers (like Google, Facebook, and Twitter), and more. |

<br />

## Tutorial overview

[Go
directly to the step-by-step tutorial](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-1)

1. [**Implement
   a sign-in experience**](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-1)

   1. Use Firebase Authentication to build a sign-in experience.

   2. Or, combine Firebase Authentication with your custom sign-in experience.

   3. In your sign-in interface, get the user's email address or phone number.

2. [**Integrate
   Google Analytics into your app**](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-2)

   1. Follow integration steps for Cocoapods, Swift Package Manager or manual
      installation.

   2. Optionally, enable debug mode in Xcode.

3. [**Initiate
   on-device conversion measurement**](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3)

   1. Call the on-device measurement API with the email or phone number you
      gathered.

   2. Verify API function with debug logs.

4. [**Troubleshoot and
   handle common issues**](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-4)

   1. If needed, troubleshoot with the help of support resources for
      Firebase Authentication and Google Analytics.

   2. Handle some commonly-encountered issues.

## What you'll need

- Your own app that can run on iOS 12 or higher

- Your app registered as a Firebase App that's linked to Google Analytics
  and Ads

- Your preferred IDE

<br />

*** ** * ** ***

<br />

[**Step 1** : Implement a sign-in experience](https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-1)

<br />

<br />

*** ** * ** ***