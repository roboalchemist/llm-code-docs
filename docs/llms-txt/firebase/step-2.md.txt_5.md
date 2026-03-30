# Source: https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2.md.txt

# Tutorial: Optimize hybrid monetization using AdMob, Google Analytics, and Firebase

## Step 2: Set up Google Analytics

<br />

|---|
| Introduction: [Optimize hybrid monetization using AdMob, Google Analytics, and Firebase](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization) |
| Step 1: Use AdMob to create new ad units for display |
| **Step 2: [Set up Google Analytics](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2)** <br /> |
| Step 3: [Set up Firebase Remote Config to show specific ads experiences](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3) |

<br />

Google Analytics collects and analyzes information about your users, which can
help you target specific groups of users with more customized app experiences ---
in this case, their in-app ads experience.

### **Add the Google Analytics for Firebase SDK to your app**

To use Google Analytics with AdMob and Firebase, you need to add the
Google Analytics for Firebase SDK to your app's codebase.

This SDK will automatically log certain events and user dimensions; you don't
need to add any code to enable them. Google Analytics will use this data to
segment your users into audiences.

Note that your app should already have the Google Mobile Ads (AdMob) SDK from
the previous step of this tutorial.

### Swift

Add and install the Google Analytics for Firebase pod in your podfile:

    pod 'Firebase/Analytics'

### Android

Add the Google Analytics for Firebase library dependency to your
`build.gradle` file:

    implementation 'com.google.firebase:firebase-analytics:23.0.0'

### Flutter

From the root of your Flutter project, run the following command to install
the Google Analytics for Firebase plugin:

    flutter pub add firebase_analytics

### Unity

Download and install the latest
[Firebase Unity SDK](https://firebase.google.com/download/unity), and then add
the Google Analytics for Firebase package to your project:  

`FirebaseAnalytics.unitypackage`

### **Understand Google Analytics audiences**

Using Google Analytics, you can segment your users into **audiences**, which are
groups of users who share the same attributes. All the users in a given audience
have exhibited the same behavior in your app (for example, added an item to
cart) and/or share demographic or other descriptive data (for example, age
range).

Google Analytics automatically provides a "Purchasers" default audience that's
common for most apps. Any user who has made an in-app purchase or an ecommerce
purchase will be placed in this audience.

When using a hybrid monetization strategy, you do **not** want to show in-app
ads to users who have made a purchase. So you can leverage this Google Analytics
audience of "Purchasers" when you set up Firebase Remote Config.

Here are some Google Analytics resources to learn more about audiences:

- [Introduction to audiences in Google Analytics](https://support.google.com/analytics/answer/12799087)

- [Examples of audiences in Google Analytics and how to create them](https://support.google.com/analytics/answer/12799863)

In the next step of this tutorial, you'll leverage the "Purchasers" audience in
setting up Firebase Remote Config.

<br />

*** ** * ** ***

<br />

[**Step 1** : Use AdMob to create new ad units for display](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization)
[**Step 3** : Set up Remote Config to show specific ads experiences](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3)

<br />

*** ** * ** ***