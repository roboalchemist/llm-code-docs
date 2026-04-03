# Source: https://firebase.google.com/docs/admob.md.txt

# Use Firebase withGoogle AdMob

plat_iosplat_androidplat_cppplat_unity  
Google AdMobis an easy way to monetize mobile apps with targeted, in-app advertising.  
[Google AdMob](https://admob.google.com/home/?utm_source=firebase&utm_medium=et&utm_campaign=firebase-docs&utm_content=2017Q1)is a mobile advertising platform that you can use to generate revenue from your app. Using Firebase withAdMobprovides you with additional app usage data and analytics capabilities.

<br />

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/admob/ios/quick-start)[Android](https://firebase.google.com/docs/admob/android/quick-start)[Unity](https://firebase.google.com/docs/admob/unity/start)[C++](https://firebase.google.com/docs/admob/cpp/quick-start)

<br />

## Key capabilities

|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Earn more from in-app ads   | Show ads from millions of Google advertisers in real time or useAdMobmediation to earn from over 40 premium networks. Simplify your ad operations, improve competition, and earn more, for free. AdMobmediation has[ad network optimization](https://support.google.com/admob/answer/3379794)built in, which automatically adjusts the positions of your other ad networks in your mediation stack, which maximizes your revenue. |
| Improve user experience     | Native ads create a positive user experience as you monetize by matching the look and feel of your app. Choose from different ad templates, customize them, and experiment with different layout.                                                                                                                                                                                                                                 |
| Scale fast                  | When your app is a global or domestic hit, you can monetize users quickly withAdMob, by showing ads to users in more than 200 markets. Do you have more than one app? House ads fromAdMobis a free tool that enables you to cross-promote your apps to your user base, across your family of apps.                                                                                                                                |
| Access monetization reports | AdMobis the premier monetization platform for mobile. While generating ad revenue,AdMobalso produces its own monetization reports that you can use to make smarter decisions about product strategy.                                                                                                                                                                                                                              |

## How does it work?

[Google AdMob](https://www.google.com/admob/?utm_source=firebase&utm_medium=et&utm_campaign=firebase-docs&utm_content=2017Q1)helps you monetize your mobile app through in-app advertising. Ads can be displayed using various format options which are seamlessly added to platform native UI components. On Android, you can additionally display in-app purchase ads, allowing users to purchase advertised products from within your app.

|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Banner![](https://developers.google.com/admob/images/format-banner.svg) | Interstitial![](https://developers.google.com/admob/images/format-interstitial.svg) | Native![](https://developers.google.com/admob/images/format-native.svg) | Rewarded![](https://developers.google.com/admob/images/format-rewarded.svg) |

To display ads, you'll need anAdMob-registered app that integrates theGoogle Mobile AdsSDK ([iOS](https://firebase.google.com/docs/admob/ios/quick-start)\|[Android](https://firebase.google.com/docs/admob/android/quick-start)). You can then activate one or more Ad Unit IDs which are unique identifiers for the places in your app to display ads.

TheMobile AdsSDK helps you gain insights about your users, drive more in-app purchases, and maximize ad revenue. To do all this, the default integration of the SDK collects device information, publisher-provided location information, and general in-app purchase information (such as item purchase price and currency).

### User metrics, Firebase, andGoogle Analytics

To make informed decisions about optimizing your app's user experience and your ad revenue, you'll need metrics and data from your app. Working together,AdMob, Firebase, andGoogle Analyticsoffer additional levels of configuration to help you achieve your optimization goals.

1. **View user metrics in yourAdMobaccount**

   [Enable user metrics](https://support.google.com/admob/answer/9263723)in yourAdMobaccount to access new data and powerful reports, such as the[rewarded report](https://support.google.com/admob/answer/9005580), that may help inform your monetization strategy.
2. **Explore and work with your analytics data via Firebase**

   [Link yourAdMobapp to Firebase](https://support.google.com/admob/answer/6383165)to help you improve app monetization and user engagement. For example, you can build custom audiences and even use BigQuery with your analytics data.
3. **Access more customization features for your analytics data**

   [Add the Firebase SDK forGoogle Analytics](https://firebase.google.com/docs/admob/analytics-and-firebase)to implement more customized analytics (like custom events), view more complete user metrics in yourAdMobaccount, and start using other Firebase products.

Learn more about the[benefits](https://firebase.google.com/docs/admob/analytics-and-firebase)of these additional levels of configuration!

## Implementation path

|---|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Configure your app to use Firebase                    | Add Firebase to your new or existing app in theFirebaseconsole.                                                                                                                                                                                                   |
|   | Create anAdMobaccount and register your app           | [Sign up for anAdMobaccount](http://www.google.com/admob/?subid=WW-EN-ET-firebase-docs&utm_source=internal&utm_medium=et&utm_campaign=firebase-docs)and register your app as anAdMobapp. Before you publish, add to your app any Ad Unit IDs that you've created. |
|   | Enable user metrics and link yourAdMobapp to Firebase | *(Optional, but strongly recommended)* In yourAdMobaccount, enable user metrics to view curated metrics. Also, link yourAdMobapp to Firebase to explore and work with your analytics data via theFirebaseconsole.                                                 |
|   | Update project dependencies                           | Add theGoogle Mobile AdsSDK using CocoaPods on iOS or Gradle on Android.                                                                                                                                                                                          |
|   | Implement your first ad in your app                   | Use theMobile AdsSDK to create space in your app UI for a banner ad (a great place to start!). You can set the layout to just the way you like it or use smart banners that will resize depending on the device size and orientation.                             |

## Next steps

- Learn how to get started on[iOS](https://firebase.google.com/docs/admob/ios/quick-start)or[Android](https://firebase.google.com/docs/admob/android/quick-start).

- Follow the quickstart, a tutorial that guides you through setting upAdMobon[iOS](https://github.com/firebase/quickstart-ios/tree/master/admob/)and[Android](https://github.com/firebase/quickstart-android/tree/master/admob/).

- Optimize ad monetization for your app by trying out different ad formats or configurations with a small subset of users, and then making data driven decisions about implementing the ad for all your users. To learn more, check out the following tutorials:

  - *Test new ad format adoption* ([overview](https://firebase.google.com/docs/tutorials/admob_test-new-ad-format-adoption_solution-overview)\|[implementation](https://firebase.google.com/docs/tutorials/admob_test-new-ad-format-adoption_implementation-guide)).

  - *Optimize ad frequency* ([overview](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/solution-overview)\|[implementation](https://firebase.google.com/docs/tutorials/optimize-ad-frequency)).