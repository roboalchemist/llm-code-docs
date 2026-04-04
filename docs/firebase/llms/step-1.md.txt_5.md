# Source: https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-1.md.txt

# Tutorial: Optimize hybrid monetization using AdMob, Google Analytics, and Firebase

## Step 1: Use AdMob to create new ad units for display

<br />

|---|
| Introduction: [Optimize hybrid monetization using AdMob, Google Analytics, and Firebase](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization) |
| **Step 1: Use AdMob to create new ad units for display** <br /> |
| Step 2: [Set up Google Analytics](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2) |
| Step 3: [Set up Firebase Remote Config to show specific ads experiences](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3) |

<br />

To get started, you first need to create a new ad unit and then implement the ad
in your app's code.

This tutorial uses the
[interstitial](https://support.google.com/admob/answer/7311435) ad
format as the new format being tested for adoption. When reading this tutorial,
though, keep in mind that you could follow similar steps to implement and test
any other ad format.

<br />

**Make sure you have the prerequisites for this tutorial**

<br />

- Your own app (iOS, Android, Flutter, or Unity project)

- Your app registered as a Firebase App that's linked to an AdMob App
  ([learn more](https://support.google.com/admob/answer/6383165)).  

  This means the following are also done:

  - You've enabled Google Analytics in your Firebase project (meaning you've
    linked your Firebase project to a Google Analytics property).

  - You've added the applicable Firebase configuration to your app's codebase.

- *(Android apps or apps targeting Android)*
  [Link your Firebase App to Google Play](https://support.google.com/firebase/answer/6392038)
  (required to get in-app purchase event data)

- Access to your app's associated AdMob account, with permissions to create
  new ad units

- Access to your app's associated Firebase project, with permissions to create
  and manage Firebase Remote Config

- Access to the Google Analytics property linked to your Firebase project, with
  permissions to create audiences (at least Editor role)

- Your preferred IDE

<br />

<br />

### **Create an ad unit in your AdMob account**

In your
[AdMob account](https://apps.admob.com), follow the on-screen
prompts to create an *Interstitial* ad unit that you will display in your app.

The other ad unit settings aren't important for this particular tutorial, so
select settings that are appropriate for your app.

> [!IMPORTANT]
> **Important:** For Flutter projects and Unity projects, you need to create a separate interstitial ad unit in each of your AdMob Apps; one for each platform that you target (that is, Android and iOS).

### **Implement the ad unit in your app's codebase**

After you create an ad unit, AdMob provides you with a unique **ad unit ID**
for the ad unit. Remember where to find this ad unit ID in your AdMob
account as you'll need it to implement the ad into your app. If you created more
than one ad unit, then you'll need the ad unit ID for *each* ad unit.

Follow the on-screen instructions (or go to the links below) to integrate the
Google Mobile Ads (AdMob) SDK (if you haven't already) and to implement the
new ad unit into your app.

### Swift

1. [Get started with AdMob in an iOS app](https://developers.google.com/admob/ios/quick-start)
2. [Implement interstitial ads in an iOS app](https://developers.google.com/admob/ios/interstitial)

### Kotlin

1. [Get started with AdMob in an Android app](https://developers.google.com/admob/android/quick-start)
2. [Implement interstitial ads in an Android app](https://developers.google.com/admob/android/interstitial)

### Java

1. [Get started with AdMob in an Android app](https://developers.google.com/admob/android/quick-start)
2. [Implement interstitial ads in an Android app](https://developers.google.com/admob/android/interstitial)

### Flutter

1. [Get started with AdMob in a Flutter app](https://developers.google.com/admob/flutter/quick-start)
2. [Implement interstitial ads in a Flutter app](https://developers.google.com/admob/flutter/interstitial)

### Unity

1. [Get started with AdMob in a Unity app](https://developers.google.com/admob/unity/quick-start)
2. [Implement interstitial ads in a Unity app](https://developers.google.com/admob/unity/interstitial)

In the next steps of this tutorial, you'll configure Firebase Remote Config
to display this ad unit based on whether a user is part of the Google Analytics
audience of "Purchasers".

<br />

*** ** * ** ***

<br />

[**Introduction**](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization)
[**Step 2** : Set up Google Analytics](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2)

<br />

*** ** * ** ***