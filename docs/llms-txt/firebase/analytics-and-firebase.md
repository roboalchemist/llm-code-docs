# Source: https://firebase.google.com/docs/admob/analytics-and-firebase.md.txt

<br />

iOS+Android  

<br />

| This page assumes that you've added theGoogle Mobile AdsSDK to your app*as well as* enabled user metrics in yourAdMobaccount and linkedAdMobto Firebase. But if you haven't, learn how in the[getting started guide](https://firebase.google.com/docs/admob/ios/quick-start).

After completing the basicAdMobsetup, you can also add the Firebase SDK forGoogle Analyticsto take advantage of other features fromGoogle Analyticsand Firebase. Learn how to[get started withGoogle Analytics](https://firebase.google.com/docs/admob/analytics-and-firebase#get-started-analytics)later on this page.

These increasing levels of configuration support features that can help you optimize your app's user experience and your ad revenue. Check out the following table of features and its links to learn more!

|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Feature**                                                                                                                                                                                                                         | **AddMobile AdsSDK + enable user metrics** | AddMobile AdsSDK + enable user metrics*and* **LinkAdMobto Firebase** | AddMobile AdsSDK + enable user metrics*and* LinkAdMobto Firebase*and* **[Add Firebase SDK forAnalytics](https://firebase.google.com/docs/admob/analytics-and-firebase#get-started-analytics)** |
| **View user metrics in yourAdMobaccount**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ||||
| Automatically collect analytics[events](https://support.google.com/admob/answer/9755157)and[user properties](https://support.google.com/admob/answer/9755590)from your app                                                          |                                            |                                                                      |                                                                                                                                                                                                |
| [View curated user metrics inAdMob](https://support.google.com/admob/answer/9281746)                                                                                                                                                |                                            |                                                                      |                                                                                                                                                                                                |
| **Explore and work with your analytics data via Firebase**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ||||
| [View key metrics in theFirebaseconsole](https://support.google.com/firebase/answer/6317517)                                                                                                                                        |                                            |                                                                      |                                                                                                                                                                                                |
| [Mark conversions for ad campaigns](https://support.google.com/analytics/answer/9267568)                                                                                                                                            |                                            |                                                                      |                                                                                                                                                                                                |
| [Build custom audiences](https://support.google.com/analytics/answer/9267572)                                                                                                                                                       |                                            |                                                                      |                                                                                                                                                                                                |
| [Export and analyze data in BigQuery](https://support.google.com/firebase/answer/7030014)                                                                                                                                           |                                            |                                                                      |                                                                                                                                                                                                |
| **Access more customization features for your analytics data**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ||||
| [Log custom events for analytics and models](https://firebase.google.com/docs/analytics/events)(like[logging ecommerce_purchase events](https://firebase.google.com/docs/admob/analytics-and-firebase#arpu-and-arppu)forandmetrics) |                                            |                                                                      |                                                                                                                                                                                                |
| [Configure custom conversions for ad campaigns](https://support.google.com/firebase/answer/6317518#custom)                                                                                                                          |                                            |                                                                      |                                                                                                                                                                                                |
| [Use other Firebase products](https://firebase.google.com/docs/admob/analytics-and-firebase#use-firebase-products) (likeRemote ConfigandA/B Testing)                                                                                |                                            |                                                                      |                                                                                                                                                                                                |

## Get started withGoogle Analytics

Google Analyticsis Firebase's analytics engine that gives you access to powerful insights into your data. Start usingGoogle Analyticsin your app by adding the Firebase SDK forGoogle Analytics.

<br />

Why add the Firebase SDK forGoogle Analytics?

<br />

With the[basicAdMobsetup](https://firebase.google.com/docs/admob/ios/quick-start), you can view aggregated statistics from automatically collected[events](https://support.google.com/admob/answer/9755157)and[user properties](https://support.google.com/admob/answer/9755590)in the*Analytics* dashboard of theFirebaseconsole without adding any additional code to your app.

However, if you want to collect additional*custom* event data or user properties, you'll need to use the Firebase SDK forGoogle Analytics. With this SDK, you can log up to 500 different analytics event types, and there's no limit on the total volume of events your app logs. An example use case for logging custom events is to include data in your revenue calculation from a custom event called`ecommerce_purchase`to help you[better representandmetrics](https://firebase.google.com/docs/admob/analytics-and-firebase#arpu-and-arppu).

By adding the Firebase SDK forGoogle Analytics, you can also[add custom conversions for ad campaigns](https://support.google.com/firebase/answer/6317518#custom)and enable the use of[other Firebase products](https://firebase.google.com/docs/admob/analytics-and-firebase#use-firebase-products).

<br />

<br />

The following steps describe how to start using the Firebase SDK forGoogle Analyticsin your app. After initializing the SDK, visit the[Analyticsdocumentation](https://firebase.google.com/docs/analytics/events)to learn how to start logging events in your app.

### **Step 1:**Add a configuration file to your app

If you registered your app with Firebase before creating anAdMoblink, then you already added a Firebase configuration file to your app. Check for a`GoogleService-Info.plist`file in the root of your Xcode project. Also make sure that the config file is added to all targets.

<br />

If you don't have this config file in your app, expand this section to learn how to add this file.

<br />

1. In the*Your apps* card of yoursettings\>[*Project settings*](https://console.firebase.google.com/project/_/settings/general), select the bundle ID of the app for which you need a config file.

2. Click**Download GoogleService-Info.plist** to obtain your Firebase iOS config file (`GoogleService-Info.plist`).

   - You can download your Firebase iOS config file again at any time from yoursettings\>*Project settings*.

   - Make sure the config file name isn't appended with additional characters, like`(2)`.

3. Move your config file into the root of your Xcode project. If prompted, select to add the config file to all targets.

If you have multiple bundle IDs in your project, you must associate each bundle ID with a registered app in theFirebaseconsole so that each app can have its own`GoogleService-Info.plist`file.
| **Note:** The Firebase config file contains unique, but non-secret identifiers for your project.  
| Visit[Understand Firebase Projects](https://firebase.google.com/docs/projects/learn-more#config-files-objects)to learn more about this config file.

<br />

<br />

### **Step 2:** Add the Firebase SDK forAnalyticsto your app

1. Add the dependency for the Firebase SDK forGoogle Analyticsto your Podfile:

       pod 'FirebaseAnalytics'

2. Run`pod install`, then open the created`.xcworkspace`file.

3. Import the`FirebaseCore`module in your`UIApplicationDelegate`, as well as any other[Firebase modules](https://firebase.google.com/docs/ios/setup#available-pods)your app delegate uses. For example, to useCloud FirestoreandAuthentication:  

   #### SwiftUI

   ```swift
   import SwiftUI
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Swift

   ```swift
   import FirebaseCore
   import FirebaseFirestore
   import FirebaseAuth
   // ...
         
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseCore;
   @import FirebaseFirestore;
   @import FirebaseAuth;
   // ...
         
   ```
4. Configure a[`FirebaseApp`](https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseApp)shared instance in your app delegate's`application(_:didFinishLaunchingWithOptions:)`method:  

   #### SwiftUI

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Swift

   ```swift
   // Use Firebase library to configure APIs
   FirebaseApp.configure()
   ```

   #### Objective-C

   ```objective-c
   // Use Firebase library to configure APIs
   [FIRApp configure];
   ```
5. If you're using SwiftUI, you must create an application delegate and attach it to your`App`struct via`UIApplicationDelegateAdaptor`or`NSApplicationDelegateAdaptor`. You must also disable app delegate swizzling. For more information, see the[SwiftUI instructions](https://firebase.google.com/docs/ios/learn-more#swiftui).  

   #### SwiftUI

   ```swift
   @main
   struct YourApp: App {
     // register app delegate for Firebase setup
     @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

     var body: some Scene {
       WindowGroup {
         NavigationView {
           ContentView()
         }
       }
     }
   }
         
   ```

| If you're tracking in-app purchases, you must initialize your transaction observer in`application:didFinishLaunchingWithOptions:`before initializing Firebase, or your observer may not receive all purchase notifications. See Apple's[In-App Purchase Best Practices](https://developer.apple.com/library/content/technotes/tn2387/_index.html)for more information.

## Implement custom event logging

This section shows an example of how to[implement custom event logging](https://firebase.google.com/docs/analytics/events)in your app. This specific example is for the custom event`ecommerce_purchase`which is a helpful event to log forAdMob-linked apps, especially for calculatingand.

<br />

Why is`ecommerce_purchase`important for ARPU and ARPPU?

<br />

A key metric for your app is[revenue by user](https://support.google.com/firebase/answer/6317517#revenue), which can be further segmented intoand. These two metrics display in the*User metrics* card of yourAdMobaccount and in the*Analytics* dashboard of theFirebaseconsole. Revenue, though, isn't directly measured; instead, it's the sum of your[estimatedAdMobearnings](https://support.google.com/admob/answer/6147072)and the following two analytics event values:

- [**`in_app_purchase`**](https://support.google.com/firebase/answer/6317485): when a user completes an in-app purchase that is processed by the App Store on iTunes, like an initial subscription, unlocking premium services, or buying in-game items

<!-- -->

- [**`ecommerce_purchase`**](https://support.google.com/firebase/answer/6317499): when a user completes a purchase, like online shopping, buying coupons or discount items, or buying movie tickets

Without any additional code in your app, theMobile AdsSDK automatically collects analytics data for`in_app_purchase`events. However, if you want to*also* include`ecommerce_purchase`event data in the revenue calculation, you'll need to implement custom logging via the Firebase SDK forGoogle Analytics.

<br />

<br />

Here's how to implement custom event logging in your app:

1. Make sure that you've completed the[Get started withGoogle Analytics](https://firebase.google.com/docs/admob/analytics-and-firebase#get-started-analytics)section of this page, which includes configuring your app to use Firebase, adding the Firebase SDK forGoogle Analytics, and initializing the SDK.

2. Log an`ecommerce_purchase`event ([Swift](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#analyticseventecommercepurchase)\|[Obj-C](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventEcommercePurchase)). Here's an example:

   ### Swift

   ```swift
   Analytics.logEvent(AnalyticsEventPurchase, parameters: [
     AnalyticsParameterCoupon: "SummerPromo",
     AnalyticsParameterCurrency: "JPY",
     AnalyticsParameterValue: 10000,
     AnalyticsParameterShipping: 500,
     AnalyticsParameterTransactionID: "192803301",
   ])
   ```

   ### Objective-C

   ```objective-c
   [FIRAnalytics logEventWithName:kFIREventPurchase
                       parameters:@{
     kFIRParameterCoupon: @"SummerPromo",
     kFIRParameterCurrency: @"JPY",
     kFIRParameterValue: @10000,
     kFIRParameterShipping: @500,
     kFIRParameterTransactionID: @"192803301",
   }];
   ```

To learn more about logging custom events in your app, visit the[Analyticsdocumentation](https://firebase.google.com/docs/analytics/events).

## Use other Firebase products in your app

After you add the Firebase SDK forGoogle Analytics, you can also start using other Firebase products, likeFirebase Remote ConfigandFirebase A/B Testing.

- [Remote Config](https://firebase.google.com/docs/remote-config)enables you to change the behavior and appearance of your app without publishing an app update, at no cost, for unlimited daily active users.

- [A/B Testing](https://firebase.google.com/docs/ab-testing)gives you the power to test changes to your app's UI, features, or engagement campaigns to learn if they make an impact on your key metrics (like revenue and retention) before rolling the changes out widely.

### Optimize ad monetization for your app

Try out different ad formats or configurations with a small subset of users, and then make data driven decisions about implementing the ad for all your users. To learn more, check out the following tutorials:

- *Test new ad format adoption* ([overview](https://firebase.google.com/docs/tutorials/admob_test-new-ad-format-adoption_solution-overview)\|[implementation](https://firebase.google.com/docs/tutorials/admob_test-new-ad-format-adoption_implementation-guide)).

- *Optimize ad frequency* ([overview](https://firebase.google.com/docs/tutorials/optimize-ad-frequency/solution-overview)\|[implementation](https://firebase.google.com/docs/tutorials/optimize-ad-frequency)).