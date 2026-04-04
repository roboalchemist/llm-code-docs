# Source: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants.md.txt

# FirebaseAnalytics Framework Reference

# Constants

The following constants are available globally.
- `


  ### [adStorage](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAdStorage)


  ` Enables storage (such as device identifiers) related to advertising.

  #### Declaration

  Swift

      static let adStorage: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType

- `


  ### [analyticsStorage](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAnalyticsStorage)


  ` Enables storage (such as app identifiers) related to analytics, e.g. visit duration.

  #### Declaration

  Swift

      static let analyticsStorage: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType

- `


  ### [adUserData](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAdUserData)


  ` Sets consent for sending user data to Google for advertising purposes.

  #### Declaration

  Swift

      static let adUserData: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType

- `


  ### [adPersonalization](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAdPersonalization)


  ` Sets consent for personalized advertising.

  #### Declaration

  Swift

      static let adPersonalization: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType

- `


  ### [denied](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:@FIRConsentStatusDenied)


  ` Consent status indicating consent is denied. For an overview of which data is sent when consent
  is denied, see [SDK behavior with consent
  mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#tag-behavior).

  #### Declaration

  Swift

      static let denied: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentStatus

- `


  ### [granted](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:@FIRConsentStatusGranted)


  ` Consent status indicating consent is granted.

  #### Declaration

  Swift

      static let granted: https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentStatus

- `


  ### [AnalyticsEventAdImpression](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAdImpression)


  ` Ad Impression event. This event signifies when a user sees an ad impression. Note: If you supply
  the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency`
  parameter so that revenue metrics can be computed accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdPlatform` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdFormat` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdSource` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdUnitName` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventAdImpression: String

- `


  ### [AnalyticsEventAddPaymentInfo](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddPaymentInfo)


  ` Add Payment Info event. This event signifies that a user has submitted their payment
  information. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply
  the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCoupon` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPaymentType` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventAddPaymentInfo: String

- `


  ### [AnalyticsEventAddShippingInfo](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddShippingInfo)


  ` Add Shipping Info event. This event signifies that a user has submitted their shipping
  information. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply
  the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCoupon` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterShippingTier` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventAddShippingInfo: String

- `


  ### [AnalyticsEventAddToCart](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddToCart)


  ` E-Commerce Add To Cart event. This event signifies that an item(s) was added to a cart for
  purchase. Add this event to a funnel with `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventPurchase` to gauge the effectiveness
  of your checkout process. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must
  also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be computed
  accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventAddToCart: String

- `


  ### [AnalyticsEventAddToWishlist](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddToWishlist)


  ` E-Commerce Add To Wishlist event. This event signifies that an item was added to a wishlist. Use
  this event to identify popular gift items. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue`
  parameter, you must also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue
  metrics can be computed accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventAddToWishlist: String

- `


  ### [AnalyticsEventAppOpen](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAppOpen)


  ` App Open event. By logging this event when an App becomes active, developers can understand how
  often users leave and return during the course of a Session. Although Sessions are automatically
  reported, this event can provide further clarification around the continuous engagement of
  app-users.

  #### Declaration

  Swift

      let AnalyticsEventAppOpen: String

- `


  ### [AnalyticsEventBeginCheckout](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventBeginCheckout)


  ` E-Commerce Begin Checkout event. This event signifies that a user has begun the process of
  checking out. Add this event to a funnel with your `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventPurchase` event to gauge the
  effectiveness of your checkout process. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue`
  parameter, you must also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue
  metrics can be computed accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCoupon` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventBeginCheckout: String

- `


  ### [AnalyticsEventCampaignDetails](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventCampaignDetails)


  ` Campaign Detail event. Log this event to supply the referral details of a re-engagement
  campaign. Note: you must supply at least one of the required parameters
  AnalyticsParameterSource, AnalyticsParameterMedium or AnalyticsParameterCampaign. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSource` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMedium` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCampaign` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTerm` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterContent` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdNetworkClickID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCP1` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCampaignID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeFormat` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMarketingTactic` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSourcePlatform` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventCampaignDetails: String

- `


  ### [AnalyticsEventEarnVirtualCurrency](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventEarnVirtualCurrency)


  ` Earn Virtual Currency event. This event tracks the awarding of virtual currency in your app. Log
  this along with `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSpendVirtualCurrency` to better understand your virtual economy.
  Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterVirtualCurrencyName` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Int or Double)

  #### Declaration

  Swift

      let AnalyticsEventEarnVirtualCurrency: String

- `


  ### [AnalyticsEventGenerateLead](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventGenerateLead)


  ` Generate Lead event. Log this event when a lead has been generated in the app to understand the
  efficacy of your install and re-engagement campaigns. Note: If you supply the
  `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency`
  parameter so that revenue metrics can be computed accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventGenerateLead: String

- `


  ### [AnalyticsEventInAppPurchase](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventInAppPurchase)


  ` In-App Purchase event. This event signifies that extra content or a subscription was purchased
  by a user inside an app. Note: This is different from the ecommerce purchase event. Note: If you
  supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply the
  `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterFreeTrial` (Int) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPrice` (Double) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPriceIsDiscounted` (Int) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterProductID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterProductName` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterQuantity` (Int) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSubscription` (Int) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double)

  #### Declaration

  Swift

      let AnalyticsEventInAppPurchase: String

- `


  ### [AnalyticsEventJoinGroup](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventJoinGroup)


  ` Join Group event. Log this event when a user joins a group such as a guild, team or family. Use
  this event to analyze how popular certain groups or social features are in your app. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterGroupID` (String)

  #### Declaration

  Swift

      let AnalyticsEventJoinGroup: String

- `


  ### [AnalyticsEventLevelEnd](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLevelEnd)


  ` Level End event. Log this event when the user finishes a level. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevelName` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSuccess` (String)

  #### Declaration

  Swift

      let AnalyticsEventLevelEnd: String

- `


  ### [AnalyticsEventLevelStart](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLevelStart)


  ` Level Start event. Log this event when the user starts a new level. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevelName` (String)

  #### Declaration

  Swift

      let AnalyticsEventLevelStart: String

- `


  ### [AnalyticsEventLevelUp](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLevelUp)


  ` Level Up event. This event signifies that a player has leveled up in your gaming app. It can
  help you gauge the level distribution of your userbase and help you identify certain levels that
  are difficult to pass. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevel` (Int)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCharacter` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventLevelUp: String

- `


  ### [AnalyticsEventLogin](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLogin)


  ` Login event. Apps with a login feature can report this event to signify that a user has logged
  in.

  #### Declaration

  Swift

      let AnalyticsEventLogin: String

- `


  ### [AnalyticsEventPostScore](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventPostScore)


  ` Post Score event. Log this event when the user posts a score in your gaming app. This event can
  help you understand how users are actually performing in your game and it can help you correlate
  high scores with certain audiences or behaviors. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScore` (Int)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevel` (Int) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCharacter` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventPostScore: String

- `


  ### [AnalyticsEventPurchase](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventPurchase)


  ` E-Commerce Purchase event. This event signifies that an item(s) was purchased by a user. Note:
  This is different from the in-app purchase event, which is reported automatically for App
  Store-based apps. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also
  supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be computed
  accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAffiliation` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCoupon` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterEndDate` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterShipping` (Double) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterStartDate` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTax` (Double) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTransactionID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventPurchase: String

- `


  ### [AnalyticsEventRefund](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventRefund)


  ` E-Commerce Refund event. This event signifies that a refund was issued. Note: If you supply the
  `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency`
  parameter so that revenue metrics can be computed accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAffiliation` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCoupon` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterShipping` (Double) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTax` (Double) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTransactionID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventRefund: String

- `


  ### [AnalyticsEventRemoveFromCart](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventRemoveFromCart)


  ` E-Commerce Remove from Cart event. This event signifies that an item(s) was removed from a cart.
  Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventRemoveFromCart: String

- `


  ### [AnalyticsEventScreenView](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventScreenView)


  ` Screen View event. This event signifies a screen view. Use this when a screen transition occurs.
  This event can be logged irrespective of whether automatic screen tracking is enabled. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScreenClass` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScreenName` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventScreenView: String

- `


  ### [AnalyticsEventSearch](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSearch)


  ` Search event. Apps that support search features can use this event to contextualize search
  operations by supplying the appropriate, corresponding parameters. This event can help you
  identify the most popular content in your app. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSearchTerm` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterStartDate` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterEndDate` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfNights` (Int) (optional) for hotel bookings
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfRooms` (Int) (optional) for hotel bookings
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfPassengers` (Int) (optional) for travel bookings
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterOrigin` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterDestination` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTravelClass` (String) (optional) for travel bookings

  #### Declaration

  Swift

      let AnalyticsEventSearch: String

- `


  ### [AnalyticsEventSelectContent](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSelectContent)


  ` Select Content event. This general purpose event signifies that a user has selected some content
  of a certain type in an app. The content can be any object in your app. This event can help you
  identify popular content and categories of content in your app. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterContentType` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemID` (String)

  #### Declaration

  Swift

      let AnalyticsEventSelectContent: String

- `


  ### [AnalyticsEventSelectItem](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSelectItem)


  ` Select Item event. This event signifies that an item was selected by a user from a list. Use the
  appropriate parameters to contextualize the event. Use this event to discover the most popular
  items selected. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListName` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventSelectItem: String

- `


  ### [AnalyticsEventSelectPromotion](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSelectPromotion)


  ` Select promotion event. This event signifies that a user has selected a promotion offer. Use the
  appropriate parameters to contextualize the event, such as the item(s) for which the promotion
  applies. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeName` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeSlot` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLocationID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionName` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventSelectPromotion: String

- `


  ### [AnalyticsEventShare](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventShare)


  ` Share event. Apps with social features can log the Share event to identify the most viral
  content. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterContentType` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemID` (String)

  #### Declaration

  Swift

      let AnalyticsEventShare: String

- `


  ### [AnalyticsEventSignUp](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSignUp)


  ` Sign Up event. This event indicates that a user has signed up for an account in your app. The
  parameter signifies the method by which the user signed up. Use this event to understand the
  different behaviors between logged in and logged out users. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMethod` (String)

  #### Declaration

  Swift

      let AnalyticsEventSignUp: String

- `


  ### [AnalyticsEventSpendVirtualCurrency](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSpendVirtualCurrency)


  ` Spend Virtual Currency event. This event tracks the sale of virtual goods in your app and can
  help you identify which virtual goods are the most popular objects of purchase. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemName` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterVirtualCurrencyName` (String)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Int or Double)

  #### Declaration

  Swift

      let AnalyticsEventSpendVirtualCurrency: String

- `


  ### [AnalyticsEventTutorialBegin](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventTutorialBegin)


  ` Tutorial Begin event. This event signifies the start of the on-boarding process in your app. Use
  this in a funnel with `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventTutorialComplete` to understand how many users complete
  this process and move on to the full app experience.

  #### Declaration

  Swift

      let AnalyticsEventTutorialBegin: String

- `


  ### [AnalyticsEventTutorialComplete](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventTutorialComplete)


  ` Tutorial End event. Use this event to signify the user's completion of your app's on-boarding
  process. Add this to a funnel with `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventTutorialBegin` to gauge the completion rate
  of your on-boarding process.

  #### Declaration

  Swift

      let AnalyticsEventTutorialComplete: String

- `


  ### [AnalyticsEventUnlockAchievement](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventUnlockAchievement)


  ` Unlock Achievement event. Log this event when the user has unlocked an achievement in your
  game. Since achievements generally represent the breadth of a gaming experience, this event can
  help you understand how many users are experiencing all that your game has to offer. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAchievementID` (String)

  #### Declaration

  Swift

      let AnalyticsEventUnlockAchievement: String

- `


  ### [AnalyticsEventViewCart](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewCart)


  ` E-commerce View Cart event. This event signifies that a user has viewed their cart. Use this to
  analyze your purchase funnel. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you
  must also supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be
  computed accurately. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventViewCart: String

- `


  ### [AnalyticsEventViewItem](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewItem)


  ` View Item event. This event signifies that a user has viewed an item. Use the appropriate
  parameters to contextualize the event. Use this event to discover the most popular items viewed
  in your app. Note: If you supply the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` parameter, you must also supply
  the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue` (Double) (optional)

  #### Declaration

  Swift

      let AnalyticsEventViewItem: String

- `


  ### [AnalyticsEventViewItemList](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewItemList)


  ` View Item List event. Log this event when a user sees a list of items or offerings. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListName` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventViewItemList: String

- `


  ### [AnalyticsEventViewPromotion](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewPromotion)


  ` View Promotion event. This event signifies that a promotion was shown to a user. Add this event
  to a funnel with the `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddToCart` and `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventPurchase` to gauge your
  conversion process. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeName` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeSlot` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems` (\[\[String: Any\]\]) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLocationID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionID` (String) (optional)
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionName` (String) (optional)

  #### Declaration

  Swift

      let AnalyticsEventViewPromotion: String

- `


  ### [AnalyticsEventViewSearchResults](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewSearchResults)


  ` View Search Results event. Log this event when the user has been presented with the results of a
  search. Params:
  - `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSearchTerm` (String)

  #### Declaration

  Swift

      let AnalyticsEventViewSearchResults: String

- `


  ### [AnalyticsParameterAchievementID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAchievementID)


  ` Game achievement ID (String).

  ```
      let params = [
        AnalyticsParameterAchievementID : "10_matches_won",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterAchievementID: String

- `


  ### [AnalyticsParameterAdFormat](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdFormat)


  ` The ad format (e.g. Banner, Interstitial, Rewarded, Native, Rewarded Interstitial, Instream).
  (String).

  ```
      let params = [
        AnalyticsParameterAdFormat : "Banner",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterAdFormat: String

- `


  ### [AnalyticsParameterAdNetworkClickID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdNetworkClickID)


  ` Ad Network Click ID (String). Used for network-specific click IDs which vary in format.

  ```
      let params = [
        AnalyticsParameterAdNetworkClickID : "1234567",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterAdNetworkClickID: String

- `


  ### [AnalyticsParameterAdPlatform](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdPlatform)


  ` The ad platform (e.g. MoPub, IronSource) (String).

  ```
      let params = [
        AnalyticsParameterAdPlatform : "MoPub",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterAdPlatform: String

- `


  ### [AnalyticsParameterAdSource](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdSource)


  ` The ad source (e.g. AdColony) (String).

  ```
      let params = [
        AnalyticsParameterAdSource : "AdColony",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterAdSource: String

- `


  ### [AnalyticsParameterAdUnitName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdUnitName)


  ` The ad unit name (e.g. Banner_03) (String).

  ```
      let params = [
        AnalyticsParameterAdUnitName : "Banner_03",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterAdUnitName: String

- `


  ### [AnalyticsParameterAffiliation](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAffiliation)


  ` A product affiliation to designate a supplying company or brick and mortar store location
  (String).

  ```
      let params = [
        AnalyticsParameterAffiliation : "Google Store",
        // ...
      ]
  ```

  <br />

  #### Declaration

  Swift

      let AnalyticsParameterAffiliation: String

- `


  ### [AnalyticsParameterCP1](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCP1)


  ` Campaign custom parameter (String). Used as a method of capturing custom data in a campaign.
  Use varies by network.

  ```
      let params = [
        AnalyticsParameterCP1 : "custom_data",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCP1: String

- `


  ### [AnalyticsParameterCampaign](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCampaign)


  ` The individual campaign name, slogan, promo code, etc. Some networks have pre-defined macro to
  capture campaign information, otherwise can be populated by developer. Highly Recommended
  (String).

  ```
      let params = [
        AnalyticsParameterCampaign : "winter_promotion",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCampaign: String

- `


  ### [AnalyticsParameterCampaignID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCampaignID)


  ` Campaign ID (String). Used for keyword analysis to identify a specific product promotion or
  strategic campaign. This is a required key for GA4 data import.

  ```
      let params = [
        AnalyticsParameterCampaignID : "7877652710",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCampaignID: String

- `


  ### [AnalyticsParameterCharacter](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCharacter)


  ` Character used in game (String).

  ```
      let params = [
        AnalyticsParameterCharacter : "beat_boss",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCharacter: String

- `


  ### [AnalyticsParameterContent](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterContent)


  ` Campaign content (String).

  #### Declaration

  Swift

      let AnalyticsParameterContent: String

- `


  ### [AnalyticsParameterContentType](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterContentType)


  ` Type of content selected (String).

  ```
      let params = [
        AnalyticsParameterContentType : "news article",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterContentType: String

- `


  ### [AnalyticsParameterCoupon](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCoupon)


  ` Coupon code used for a purchase (String).

  ```
      let params = [
        AnalyticsParameterCoupon : "SUMMER_FUN",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCoupon: String

- `


  ### [AnalyticsParameterCreativeFormat](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeFormat)


  ` Creative Format (String). Used to identify the high-level classification of the type of ad
  served by a specific campaign.

  ```
      let params = [
        AnalyticsParameterCreativeFormat : "display",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCreativeFormat: String

- `


  ### [AnalyticsParameterCreativeName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeName)


  ` The name of a creative used in a promotional spot (String).

  ```
      let params = [
        AnalyticsParameterCreativeName : "Summer Sale",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCreativeName: String

- `


  ### [AnalyticsParameterCreativeSlot](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeSlot)


  ` The name of a creative slot (String).

  ```
      let params = [
        AnalyticsParameterCreativeSlot : "summer_banner2",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCreativeSlot: String

- `


  ### [AnalyticsParameterCurrency](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency)


  ` Currency of the purchase or items associated with the event, in 3-letter
  [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String).

  ```
      let params = [
        AnalyticsParameterCurrency : "USD",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterCurrency: String

- `


  ### [AnalyticsParameterDestination](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterDestination)


  ` Flight or Travel destination (String).

  ```
      let params = [
        AnalyticsParameterDestination : "Mountain View, CA",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterDestination: String

- `


  ### [AnalyticsParameterDiscount](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterDiscount)


  ` Monetary value of discount associated with a purchase (Double).

  ```
      let params = [
        AnalyticsParameterDiscount : 2.0,
        AnalyticsParameterCurrency : "USD",  // e.g. $2.00 USD
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterDiscount: String

- `


  ### [AnalyticsParameterEndDate](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterEndDate)


  ` The arrival date, check-out date or rental end date for the item. This should be in
  YYYY-MM-DD format (String).

  ```
      let params = [
        AnalyticsParameterEndDate : "2015-09-14",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterEndDate: String

- `


  ### [AnalyticsParameterExtendSession](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterExtendSession)


  ` Indicates that the associated event should either extend the current session or start a new
  session if no session was active when the event was logged. Specify 1 to extend the current
  session or to start a new session; any other value will not extend or start a session.

  ```
      let params = [
        AnalyticsParameterExtendSession : 1,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterExtendSession: String

- `


  ### [AnalyticsParameterFlightNumber](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterFlightNumber)


  ` Flight number for travel events (String).

  ```
      let params = [
        AnalyticsParameterFlightNumber : "ZZ800",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterFlightNumber: String

- `


  ### [AnalyticsParameterFreeTrial](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterFreeTrial)


  ` Indicates if the user is on a free trial of a subscription. Specify 1 to indicate true and 0 to
  indicate false (Int).

  ```
      let params = [
        AnalyticsParameterFreeTrial : 1,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterFreeTrial: String

- `


  ### [AnalyticsParameterGroupID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterGroupID)


  ` Group/clan/guild ID (String).

  ```
      let params = [
        AnalyticsParameterGroupID : "g1",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterGroupID: String

- `


  ### [AnalyticsParameterIndex](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterIndex)


  ` The index of the item in a list (Int).

  ```
      let params = [
        AnalyticsParameterIndex : 5,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterIndex: String

- `


  ### [AnalyticsParameterItemBrand](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemBrand)


  ` Item brand (String).

  ```
      let params = [
        AnalyticsParameterItemBrand : "Google",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemBrand: String

- `


  ### [AnalyticsParameterItemCategory](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory)


  ` Item category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory : "pants",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemCategory: String

- `


  ### [AnalyticsParameterItemCategory2](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory2)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory2 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemCategory2: String

- `


  ### [AnalyticsParameterItemCategory3](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory3)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory3 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemCategory3: String

- `


  ### [AnalyticsParameterItemCategory4](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory4)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory4 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemCategory4: String

- `


  ### [AnalyticsParameterItemCategory5](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory5)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory5 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemCategory5: String

- `


  ### [AnalyticsParameterItemID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemID)


  ` Item ID (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemID : "SKU_12345",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemID: String

- `


  ### [AnalyticsParameterItemListID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListID)


  ` The ID of the list in which the item was presented to the user (String).

  ```
      let params = [
        AnalyticsParameterItemListID : "ABC123",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemListID: String

- `


  ### [AnalyticsParameterItemListName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListName)


  ` The name of the list in which the item was presented to the user (String).

  ```
      let params = [
        AnalyticsParameterItemListName : "Related products",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemListName: String

- `


  ### [AnalyticsParameterItemName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemName)


  ` Item Name (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemName : "jeggings",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemName: String

- `


  ### [AnalyticsParameterItemVariant](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemVariant)


  ` Item variant (String).

  ```
      let params = [
        AnalyticsParameterItemVariant : "Black",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItemVariant: String

- `


  ### [AnalyticsParameterItems](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems)


  ` The list of items involved in the transaction expressed as `[[String: Any]]`.

  ```
      let params = [
        AnalyticsParameterItems : [
          [AnalyticsParameterItemName : "jeggings", AnalyticsParameterItemCategory : "pants"],
          [AnalyticsParameterItemName : "boots", AnalyticsParameterItemCategory : "shoes"],
        ],
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterItems: String

- `


  ### [AnalyticsParameterLevel](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevel)


  ` Level in game (Int).

  ```
      let params = [
        AnalyticsParameterLevel : 42,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterLevel: String

- `


  ### [AnalyticsParameterLevelName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevelName)


  ` The name of a level in a game (String).

  ```
      let params = [
        AnalyticsParameterLevelName : "room_1",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterLevelName: String

- `


  ### [AnalyticsParameterLocation](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLocation)


  ` Location (String). The Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated event. Alternatively, you can supply your own custom
  Location ID.

  ```
      let params = [
        AnalyticsParameterLocation : "ChIJiyj437sx3YAR9kUWC8QkLzQ",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterLocation: String

- `


  ### [AnalyticsParameterLocationID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLocationID)


  ` The location associated with the event. Preferred to be the Google
  [Place ID](https://developers.google.com/places/place-id) that corresponds to the
  associated item but could be overridden to a custom location ID string.(String).

  ```
      let params = [
        AnalyticsParameterLocationID : "ChIJiyj437sx3YAR9kUWC8QkLzQ",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterLocationID: String

- `


  ### [AnalyticsParameterMarketingTactic](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMarketingTactic)


  ` Marketing Tactic (String). Used to identify the targeting criteria applied to a specific
  campaign.

  ```
      let params = [
        AnalyticsParameterMarketingTactic : "Remarketing",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterMarketingTactic: String

- `


  ### [AnalyticsParameterMedium](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMedium)


  ` The advertising or marketing medium, for example: cpc, banner, email, push. Highly recommended
  (String).

  ```
      let params = [
        AnalyticsParameterMedium : "email",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterMedium: String

- `


  ### [AnalyticsParameterMethod](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMethod)


  ` A particular approach used in an operation; for example, "facebook" or "email" in the context
  of a sign_up or login event. (String).

  ```
      let params = [
        AnalyticsParameterMethod : "google",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterMethod: String

- `


  ### [AnalyticsParameterNumberOfNights](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfNights)


  ` Number of nights staying at hotel (Int).

  ```
      let params = [
        AnalyticsParameterNumberOfNights : 3,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterNumberOfNights: String

- `


  ### [AnalyticsParameterNumberOfPassengers](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfPassengers)


  ` Number of passengers traveling (Int).

  ```
      let params = [
        AnalyticsParameterNumberOfPassengers : 11,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterNumberOfPassengers: String

- `


  ### [AnalyticsParameterNumberOfRooms](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfRooms)


  ` Number of rooms for travel events (Int).

  ```
      let params = [
        AnalyticsParameterNumberOfRooms : 2,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterNumberOfRooms: String

- `


  ### [AnalyticsParameterOrigin](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterOrigin)


  ` Flight or Travel origin (String).

  ```
      let params = [
        AnalyticsParameterOrigin : "Mountain View, CA",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterOrigin: String

- `


  ### [AnalyticsParameterPaymentType](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPaymentType)


  ` The chosen method of payment (String).

  ```
      let params = [
        AnalyticsParameterPaymentType : "Visa",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterPaymentType: String

- `


  ### [AnalyticsParameterPrice](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPrice)


  ` Purchase price (Double).

  ```
      let params = [
        AnalyticsParameterPrice : 1.0,
        AnalyticsParameterCurrency : "USD",  // e.g. $1.00 USD
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterPrice: String

- `


  ### [AnalyticsParameterPriceIsDiscounted](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPriceIsDiscounted)


  ` Indicates if an item's price is discounted. Specify 1 to indicate true and 0 to indicate false
  (Int).

  ```
      let params = [
        AnalyticsParameterPriceIsDiscounted : 1,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterPriceIsDiscounted: String

- `


  ### [AnalyticsParameterProductID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterProductID)


  ` The ID of a product (String).

  ```
      let params = [
        AnalyticsParameterProductID : "PROD_12345",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterProductID: String

- `


  ### [AnalyticsParameterProductName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterProductName)


  ` The name of a product (String).

  ```
      let params = [
        AnalyticsParameterProductName : "My Awesome Product",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterProductName: String

- `


  ### [AnalyticsParameterPromotionID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionID)


  ` The ID of a product promotion (String).

  ```
      let params = [
        AnalyticsParameterPromotionID : "ABC123",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterPromotionID: String

- `


  ### [AnalyticsParameterPromotionName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionName)


  ` The name of a product promotion (String).

  ```
      let params = [
        AnalyticsParameterPromotionName : "Summer Sale",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterPromotionName: String

- `


  ### [AnalyticsParameterQuantity](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterQuantity)


  ` Purchase quantity (Int).

  ```
      let params = [
        AnalyticsParameterQuantity : 1,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterQuantity: String

- `


  ### [AnalyticsParameterScore](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScore)


  ` Score in game (Int).

  ```
      let params = [
        AnalyticsParameterScore : 4200,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterScore: String

- `


  ### [AnalyticsParameterScreenClass](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScreenClass)


  ` Current screen class, such as the class name of the UIViewController, logged with screen_view
  event and added to every event (String).

  ```
      let params = [
        AnalyticsParameterScreenClass : "LoginViewController",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterScreenClass: String

- `


  ### [AnalyticsParameterScreenName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScreenName)


  ` Current screen name, such as the name of the UIViewController, logged with screen_view event and
  added to every event (String).

  ```
      let params = [
        AnalyticsParameterScreenName : "LoginView",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterScreenName: String

- `


  ### [AnalyticsParameterSearchTerm](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSearchTerm)


  ` The search string/keywords used (String).

  ```
      let params = [
        AnalyticsParameterSearchTerm : "periodic table",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterSearchTerm: String

- `


  ### [AnalyticsParameterShipping](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterShipping)


  ` Shipping cost associated with a transaction (Double).

  ```
      let params = [
        AnalyticsParameterShipping : 5.99,
        AnalyticsParameterCurrency : "USD",  // e.g. $5.99 USD
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterShipping: String

- `


  ### [AnalyticsParameterShippingTier](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterShippingTier)


  ` The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item
  (String).

  ```
      let params = [
        AnalyticsParameterShippingTier : "Ground",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterShippingTier: String

- `


  ### [AnalyticsParameterSource](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSource)


  ` The origin of your traffic, such as an Ad network (for example, google) or partner (urban
  airship). Identify the advertiser, site, publication, etc. that is sending traffic to your
  property. Highly recommended (String).

  ```
      let params = [
        AnalyticsParameterSource : "InMobi",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterSource: String

- `


  ### [AnalyticsParameterSourcePlatform](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSourcePlatform)


  ` Source Platform (String). Used to identify the platform responsible for directing traffic to a
  given Analytics property (e.g., a buying platform where budgets, targeting criteria, etc. are
  set, a platform for managing organic traffic data, etc.).

  ```
      let params = [
        AnalyticsParameterSourcePlatform : "sa360",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterSourcePlatform: String

- `


  ### [AnalyticsParameterStartDate](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterStartDate)


  ` The departure date, check-in date or rental start date for the item. This should be in
  YYYY-MM-DD format (String).

  ```
      let params = [
        AnalyticsParameterStartDate : "2015-09-14",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterStartDate: String

- `


  ### [AnalyticsParameterSubscription](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSubscription)


  ` Indicates if the purchase is a subscription. Specify 1 to indicate true and 0 to indicate false
  (Int).

  ```
      let params = [
        AnalyticsParameterSubscription : 1,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterSubscription: String

- `


  ### [AnalyticsParameterSuccess](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSuccess)


  ` The result of an operation. Specify 1 to indicate success and 0 to indicate failure (Int).

  ```
      let params = [
        AnalyticsParameterSuccess : 1,
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterSuccess: String

- `


  ### [AnalyticsParameterTax](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTax)


  ` Tax cost associated with a transaction (Double).

  ```
      let params = [
        AnalyticsParameterTax : 2.43,
        AnalyticsParameterCurrency : "USD",  // e.g. $2.43 USD
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterTax: String

- `


  ### [AnalyticsParameterTerm](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTerm)


  ` If you're manually tagging keyword campaigns, you should use utm_term to specify the keyword
  (String).

  ```
      let params = [
        AnalyticsParameterTerm : "game",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterTerm: String

- `


  ### [AnalyticsParameterTransactionID](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTransactionID)


  ` The unique identifier of a transaction (String).

  ```
      let params = [
        AnalyticsParameterTransactionID : "T12345",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterTransactionID: String

- `


  ### [AnalyticsParameterTravelClass](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTravelClass)


  ` Travel class (String).

  ```
      let params = [
        AnalyticsParameterTravelClass : "business",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterTravelClass: String

- `


  ### [AnalyticsParameterValue](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue)


  ` A context-specific numeric value which is accumulated automatically for each event type. This is
  a general purpose parameter that is useful for accumulating a key metric that pertains to an
  event. Examples include revenue, distance, time and points. Value should be specified as Int or
  Double.
  Notes: Values for pre-defined currency-related events (such as `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddToCart`)
  should be supplied using Double and must be accompanied by a `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency`
  parameter. The valid range of accumulated values is
  \[-9,223,372,036,854.77, 9,223,372,036,854.77\]. Supplying a non-numeric value, omitting the
  corresponding `https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency` parameter, or supplying an invalid
  [currency code](https://goo.gl/qqX3J2) for conversion events will cause that
  conversion to be omitted from reporting.

  ```
      let params = [
        AnalyticsParameterValue : 3.99,
        AnalyticsParameterCurrency : "USD",  // e.g. $3.99 USD
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterValue: String

- `


  ### [AnalyticsParameterVirtualCurrencyName](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterVirtualCurrencyName)


  ` Name of virtual currency type (String).

  ```
      let params = [
        AnalyticsParameterVirtualCurrencyName : "virtual_currency_name",
        // ...
      ]
  ```

  #### Declaration

  Swift

      let AnalyticsParameterVirtualCurrencyName: String

- `


  ### [AnalyticsUserPropertyAllowAdPersonalizationSignals](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRUserPropertyNames.h@kFIRUserPropertyAllowAdPersonalizationSignals)


  ` Indicates whether events logged by Google Analytics can be used to personalize ads for the user.
  Set to "YES" to enable, or "NO" to disable. Default is enabled. See the
  [documentation](https://firebase.google.com/support/guides/disable-analytics) for
  more details and information about related settings.

  ```
      Analytics.setUserProperty("NO", forName: AnalyticsUserPropertyAllowAdPersonalizationSignals)
  ```

  #### Declaration

  Swift

      let AnalyticsUserPropertyAllowAdPersonalizationSignals: String

- `


  ### [AnalyticsUserPropertySignUpMethod](https://firebase.google.com/docs/reference/swift/firebaseanalytics/api/reference/Constants#/c:FIRUserPropertyNames.h@kFIRUserPropertySignUpMethod)


  ` The method used to sign in. For example, "google", "facebook" or "twitter".

  #### Declaration

  Swift

      let AnalyticsUserPropertySignUpMethod: String