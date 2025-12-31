# Source: https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization.md.txt

### **Solution tutorial**

Oftentimes, the initial focus for app monetization is in-app purchases, but the market shows that in-app advertising is a top revenue stream for apps.

In fact, according to some reports, in-app advertising is projected to grow nearly 50%, whereas in-app purchase revenue is projected to grow only by about 30%. In addition, only about 5% of users make purchases, which means that for the*majority of your user base*, you need to implement a monetization strategy --- like in-app advertising.

A hybrid approach to monetization can capture all your user segments. However, optimizing that strategy is complicated, but Google offers tooling and products to help.

- Use**Google AdMob** to create and implement ad units to display in your app, and thenAdMobtakes care of connecting advertisers to that ad space.

- Set up**Google Analytics**to dynamically segment your users into categories (like "Purchasers"), which you can then leverage to implement hybrid monetization.

- Use**Firebase Remote Config**to dynamically serve an in-app ads experience in your app based on whether a user is in that "Purchaser" audience or not.

## What you'll learn

In this multistep tutorial, you'll learn how to useGoogle AdMob, Google Analytics audiences, and Firebase to implement and optimize a hybrid monetization strategy. It uses an[interstitial](https://support.google.com/admob/answer/7311435)ad format as the example test case, but you can extrapolate and use these same steps if you want to use a[different ad format](https://support.google.com/admob/answer/6128738).

Note that this tutorial assumes that you have a basic understanding ofGoogle AdMoband the Firebase platform and that you'd like to learn how to optimize your in-app advertising monetization using Google Analytics andFirebase Remote Config.
| **Tip:** If there's a term that you're not familiar with, check out the[glossary](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization#glossary)at the bottom of this page.

## Products and features used in this tutorial

|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Google AdMob > [Google AdMob](https://firebase.google.com/docs/admob)enables you to create ad units that will be served within your app. When you linkAdMobwith Firebase,AdMobsends ad revenue information to Firebase to improve ad strategy optimization. Google Analytics > [Google Analytics](https://firebase.google.com/docs/analytics)gives you insight into user engagement, retention, and monetization metrics like total revenue,AdMobrevenue, purchase revenue, and much more. It also allows you to create user audiences and segments. | Firebase Remote Config > [Firebase Remote Config](https://firebase.google.com/docs/remote-config)enables you to dynamically change and customize the behavior and appearance of your app for desired user segments ---*all without publishing a new version of your app* . In this tutorial, you'll useRemote Configparameters to control whether a new ad unit is shown to your users based on their placement in a Google Analytics audience. |

## Tutorial overview

[Go directly to the step-by-step tutorial](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-1)

1. [**UseAdMobto to create new ad units for display**](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-1)

   1. Create an ad unit in yourAdMobaccount.

   2. Implement the ad unit in your app's codebase.

2. [**Set up Google Analytics**](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-2)

   1. Add the Google Analytics for Firebase SDK to your app's codebase.

   2. Understand Google Analytics audiences.

3. [**Set upFirebase Remote Configto show specific ads experiences**](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-3)

   1. Set upRemote Configparameters and conditions in theFirebaseconsole.

   2. Add theRemote ConfigSDK to your app's codebase.

   3. Configure theRemote Configinstance.

   4. Fetch and activateRemote Config.

   5. Use theRemote Configparameter value.

   6. Release your app.

## What you'll need

- Your own app (iOS, Android, Flutter, or Unity project)

- Your app registered as a Firebase App that's linked to anAdMobApp ([learn more](https://support.google.com/admob/answer/6383165)).  
  This means the following are also done:

  - You've enabled Google Analytics in your Firebase project (meaning you've linked your Firebase project to a Google Analytics property).

  - You've added the applicable Firebase configuration to your app's codebase.

- *(Android apps or apps targeting Android)* [Link your Firebase App toGoogle Play](https://support.google.com/firebase/answer/6392038)(required to get in-app purchase event data)

- Access to your app's associatedAdMobaccount, with permissions to create new ad units

- Access to your app's associated Firebase project, with permissions to create and manageFirebase Remote Config

- Access to the Google Analytics property linked to your Firebase project, with permissions to create audiences (at least Editor role)

- Your preferred IDE

## Glossary

<br />

View a list of common terms for this solution

<br />

- **Google Analytics[events](https://support.google.com/firebase/answer/6317485)**: Actions that users take in your app, like making an in-app purchase, clicking an ad, signing into your app, etc.

- **Google Analytics[audience](https://support.google.com/analytics/answer/9267572)**: A segment of your user base who share the same attributes. All the users in a given audience have exhibited the same behavior in your app (for example, added an item to cart) and/or share demographic or other descriptive data (for example, age range).

- **Remote Configparameter**: The configurable parameter (key-value pair) used to control whether the app shows ads or not. In the basic implementation of this guide, it will have a boolean value.

- **Remote Configcondition**: A condition is used to target a group of app instances. Conditions are made up of one or more rules that must all evaluate to true for the condition to evaluate to true for a given app instance.

<br />

<br />

<br />

*** ** * ** ***

<br />

[**Step 1** : UseAdMobto create new ad units for displayarrow_forward_ios](https://firebase.google.com/docs/tutorials/optimize-hybrid-monetization/step-1)

<br />

<br />

*** ** * ** ***