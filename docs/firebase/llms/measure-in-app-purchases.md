# Source: https://firebase.google.com/docs/analytics/measure-in-app-purchases.md.txt

In-app purchases (IAP) are digital content or features that you can sell in a mobile app throughGoogle Playor the Apple App Store so your app doesn't have to process financial transactions. Examples of in-app purchases include subscription-based content or special game pieces.

Analyticsshows IAP events in the[In-app purchases report](https://support.google.com/analytics/answer/12923440).

For Android apps, theAnalyticsSDK integrates withGoogle Play. For Apple platform apps, the SDK integrates with the Apple App Store using the StoreKit 1 and StoreKit 2 APIs from Apple.

In most cases, theAnalyticsSDK automatically collects IAP events without requiring API calls in your app. On iOS, you can also[log IAP events manually in a WebView](https://firebase.google.com/docs/analytics/webview?platform=ios#log_in_app_purchase_events_manually_in_a_webview_on_iOS)in addition to the automatically collected IAP events. This guide explains how to set up your project for automatic tracking, and describes some special cases that require a few lines of code to implement.

## Before you begin

- Set up your Firebase project and your app's codebase as described in[Get Started withGoogle Analytics](https://firebase.google.com/docs/analytics/get-started).

- [Link your Firebase project to a Google Analytics 4 property.](https://support.google.com/firebase/answer/9289399)

### Android apps

- Make sure that your app is using theAnalyticsSDK v17.3.0+ (orFirebase Android BoMv25.2.0+).

- [Link your Firebase apps toGoogle Play](https://support.google.com/firebase/answer/6392038).

  | **Note:** For Android apps, you can measure IAP events as soon as you link toGoogle Play. The remainder of this guide is focused on Apple platform apps.

### Apple platform apps

- Make sure that you're using the latest SDK:

  - For***automatic***in-app purchase tracking: Make sure that your app is using the Analytics SDK v6.20.0+.

  - For***manual***in-app purchase tracking: Make sure that your app is using the Analytics SDK v12.5.0+.

- Make sure you're familiar with the Apple StoreKit 1 and StoreKit 2 in-app purchase APIs by reviewing the[Apple documentation](https://developer.apple.com/documentation/storekit/in-app_purchase).

## Implementation

In most cases, the Analytics SDK automatically logs IAP events without requiring additional code.

### Implementation in Android apps

For Android apps, you can measure IAP events as soon as you[link to Google Play](https://support.google.com/analytics/answer/11548051).

### Implementation in Apple platform apps

For iOS apps, if you're using StoreKit 1, the Analytics SDK automatically logs IAP events. If you're using StoreKit 2, you can log verified in-app purchase events using the code snippet below.

Alternatively, if you have a need to track in-app purchases made outside of the App Store, you can[log IAP events manually in a WebView](https://firebase.google.com/docs/analytics/webview?platform=ios#log_in-app_purchase_events_manually_in_a_webview_on_ios). Note that the SDK will continue to automatically log in-app purchases where possible, and won't de-duplicate any manually logged in-app purchase events. Make sure that you're using the Analytics SDK v12.5.0+ when manually tracking in-app purchases.  

### Swift

If you're using StoreKit 1, theAnalyticsSDK automatically logs IAP events.

If you're using StoreKit 2, use the following code to log IAP events.  

```swift
import StoreKit
import FirebaseAnalytics

// A user tapped a button to purchase an item.
func userTappedPurchaseUpgradeButton() {
  let product = ...
  purchaseSomeProduct(product)
}

func purchaseSomeProduct(_ product: Product) {
  // Purchase a Product. This is mostly standard boilerplate StoreKit 2
  // code, except for the Analytics.logTransaction() call.
  let result = try await product.purchase()
  switch result {
  case .success(let verification):
      let transaction = try checkVerified(verification)

      // Call this Firebase API to log the in-app purchase event.
      Analytics.logTransaction(transaction)

      await transaction.finish()
  ...
}
```

### Objective-C

If you're using StoreKit 1, theAnalyticsSDK automatically logs IAP events.

StoreKit 2 is Swift-only, so an Objective-C implementation is not supported.