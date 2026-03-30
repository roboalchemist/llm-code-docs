# Source: https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants.md.txt

# FirebaseAnalytics Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRConsentTypeAdStorage](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAdStorage)


  ` Enables storage (such as device identifiers) related to advertising.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType _Nonnull FIRConsentTypeAdStorage

- `


  ### [FIRConsentTypeAnalyticsStorage](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAnalyticsStorage)


  ` Enables storage (such as app identifiers) related to analytics, e.g. visit duration.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType _Nonnull FIRConsentTypeAnalyticsStorage

- `


  ### [FIRConsentTypeAdUserData](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAdUserData)


  ` Sets consent for sending user data to Google for advertising purposes.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType _Nonnull FIRConsentTypeAdUserData

- `


  ### [FIRConsentTypeAdPersonalization](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:@FIRConsentTypeAdPersonalization)


  ` Sets consent for personalized advertising.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentType _Nonnull FIRConsentTypeAdPersonalization

- `


  ### [FIRConsentStatusDenied](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:@FIRConsentStatusDenied)


  ` Consent status indicating consent is denied. For an overview of which data is sent when consent
  is denied, see [SDK behavior with consent
  mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#tag-behavior).

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentStatus _Nonnull FIRConsentStatusDenied

- `


  ### [FIRConsentStatusGranted](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:@FIRConsentStatusGranted)


  ` Consent status indicating consent is granted.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Type-Definitions#/c:FIRAnalytics+Consent.h@T@FIRConsentStatus _Nonnull FIRConsentStatusGranted

- `


  ### [kFIREventAdImpression](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAdImpression)


  ` Ad Impression event. This event signifies when a user sees an ad impression. Note: If you supply
  the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency`
  parameter so that revenue metrics can be computed accurately. Params:
  - `AnalyticsParameterAdPlatform` (String) (optional)
  - `AnalyticsParameterAdFormat` (String) (optional)
  - `AnalyticsParameterAdSource` (String) (optional)
  - `AnalyticsParameterAdUnitName` (String) (optional)
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventAdImpression = @"ad_impression"

- `


  ### [kFIREventAddPaymentInfo](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddPaymentInfo)


  ` Add Payment Info event. This event signifies that a user has submitted their payment
  information. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply
  the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `AnalyticsParameterCoupon` (String) (optional)
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterPaymentType` (String) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventAddPaymentInfo = @"add_payment_info"

- `


  ### [kFIREventAddShippingInfo](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddShippingInfo)


  ` Add Shipping Info event. This event signifies that a user has submitted their shipping
  information. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply
  the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `AnalyticsParameterCoupon` (String) (optional)
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterShippingTier` (String) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventAddShippingInfo = @"add_shipping_info"

- `


  ### [kFIREventAddToCart](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddToCart)


  ` E-Commerce Add To Cart event. This event signifies that an item(s) was added to a cart for
  purchase. Add this event to a funnel with `AnalyticsEventPurchase` to gauge the effectiveness
  of your checkout process. Note: If you supply the `AnalyticsParameterValue` parameter, you must
  also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed
  accurately. Params:
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventAddToCart = @"add_to_cart"

- `


  ### [kFIREventAddToWishlist](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAddToWishlist)


  ` E-Commerce Add To Wishlist event. This event signifies that an item was added to a wishlist. Use
  this event to identify popular gift items. Note: If you supply the `AnalyticsParameterValue`
  parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue
  metrics can be computed accurately. Params:
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventAddToWishlist = @"add_to_wishlist"

- `


  ### [kFIREventAppOpen](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventAppOpen)


  ` App Open event. By logging this event when an App becomes active, developers can understand how
  often users leave and return during the course of a Session. Although Sessions are automatically
  reported, this event can provide further clarification around the continuous engagement of
  app-users.

  #### Declaration

  Objective-C

      static NSString *const kFIREventAppOpen = @"app_open"

- `


  ### [kFIREventBeginCheckout](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventBeginCheckout)


  ` E-Commerce Begin Checkout event. This event signifies that a user has begun the process of
  checking out. Add this event to a funnel with your `AnalyticsEventPurchase` event to gauge the
  effectiveness of your checkout process. Note: If you supply the `AnalyticsParameterValue`
  parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue
  metrics can be computed accurately. Params:
  - `AnalyticsParameterCoupon` (String) (optional)
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventBeginCheckout = @"begin_checkout"

- `


  ### [kFIREventCampaignDetails](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventCampaignDetails)


  ` Campaign Detail event. Log this event to supply the referral details of a re-engagement
  campaign. Note: you must supply at least one of the required parameters
  AnalyticsParameterSource, AnalyticsParameterMedium or AnalyticsParameterCampaign. Params:
  - `AnalyticsParameterSource` (String)
  - `AnalyticsParameterMedium` (String)
  - `AnalyticsParameterCampaign` (String)
  - `AnalyticsParameterTerm` (String) (optional)
  - `AnalyticsParameterContent` (String) (optional)
  - `AnalyticsParameterAdNetworkClickID` (String) (optional)
  - `AnalyticsParameterCP1` (String) (optional)
  - `AnalyticsParameterCampaignID` (String) (optional)
  - `AnalyticsParameterCreativeFormat` (String) (optional)
  - `AnalyticsParameterMarketingTactic` (String) (optional)
  - `AnalyticsParameterSourcePlatform` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventCampaignDetails = @"campaign_details"

- `


  ### [kFIREventEarnVirtualCurrency](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventEarnVirtualCurrency)


  ` Earn Virtual Currency event. This event tracks the awarding of virtual currency in your app. Log
  this along with `AnalyticsEventSpendVirtualCurrency` to better understand your virtual economy.
  Params:
  - `AnalyticsParameterVirtualCurrencyName` (String)
  - `AnalyticsParameterValue` (Int or Double)

  #### Declaration

  Objective-C

      static NSString *const kFIREventEarnVirtualCurrency = @"earn_virtual_currency"

- `


  ### [kFIREventGenerateLead](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventGenerateLead)


  ` Generate Lead event. Log this event when a lead has been generated in the app to understand the
  efficacy of your install and re-engagement campaigns. Note: If you supply the
  `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency`
  parameter so that revenue metrics can be computed accurately. Params:
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventGenerateLead = @"generate_lead"

- `


  ### [kFIREventInAppPurchase](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventInAppPurchase)


  ` In-App Purchase event. This event signifies that extra content or a subscription was purchased
  by a user inside an app. Note: This is different from the ecommerce purchase event. Note: If you
  supply the `AnalyticsParameterValue` parameter, you must also supply the
  `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `AnalyticsParameterCurrency` (String)
  - `AnalyticsParameterFreeTrial` (Int) (optional)
  - `AnalyticsParameterPrice` (Double) (optional)
  - `AnalyticsParameterPriceIsDiscounted` (Int) (optional)
  - `AnalyticsParameterProductID` (String) (optional)
  - `AnalyticsParameterProductName` (String) (optional)
  - `AnalyticsParameterQuantity` (Int) (optional)
  - `AnalyticsParameterSubscription` (Int) (optional)
  - `AnalyticsParameterValue` (Double)

  #### Declaration

  Objective-C

      static NSString *const kFIREventInAppPurchase = @"in_app_purchase"

- `


  ### [kFIREventJoinGroup](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventJoinGroup)


  ` Join Group event. Log this event when a user joins a group such as a guild, team or family. Use
  this event to analyze how popular certain groups or social features are in your app. Params:
  - `AnalyticsParameterGroupID` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventJoinGroup = @"join_group"

- `


  ### [kFIREventLevelEnd](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLevelEnd)


  ` Level End event. Log this event when the user finishes a level. Params:
  - `AnalyticsParameterLevelName` (String)
  - `AnalyticsParameterSuccess` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventLevelEnd = @"level_end"

- `


  ### [kFIREventLevelStart](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLevelStart)


  ` Level Start event. Log this event when the user starts a new level. Params:
  - `AnalyticsParameterLevelName` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventLevelStart = @"level_start"

- `


  ### [kFIREventLevelUp](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLevelUp)


  ` Level Up event. This event signifies that a player has leveled up in your gaming app. It can
  help you gauge the level distribution of your userbase and help you identify certain levels that
  are difficult to pass. Params:
  - `AnalyticsParameterLevel` (Int)
  - `AnalyticsParameterCharacter` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventLevelUp = @"level_up"

- `


  ### [kFIREventLogin](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventLogin)


  ` Login event. Apps with a login feature can report this event to signify that a user has logged
  in.

  #### Declaration

  Objective-C

      static NSString *const kFIREventLogin = @"login"

- `


  ### [kFIREventPostScore](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventPostScore)


  ` Post Score event. Log this event when the user posts a score in your gaming app. This event can
  help you understand how users are actually performing in your game and it can help you correlate
  high scores with certain audiences or behaviors. Params:
  - `AnalyticsParameterScore` (Int)
  - `AnalyticsParameterLevel` (Int) (optional)
  - `AnalyticsParameterCharacter` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventPostScore = @"post_score"

- `


  ### [kFIREventPurchase](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventPurchase)


  ` E-Commerce Purchase event. This event signifies that an item(s) was purchased by a user. Note:
  This is different from the in-app purchase event, which is reported automatically for App
  Store-based apps. Note: If you supply the `AnalyticsParameterValue` parameter, you must also
  supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed
  accurately. Params:
  - `AnalyticsParameterAffiliation` (String) (optional)
  - `AnalyticsParameterCoupon` (String) (optional)
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterEndDate` (String) (optional)
  - `AnalyticsParameterItemID` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterShipping` (Double) (optional)
  - `AnalyticsParameterStartDate` (String) (optional)
  - `AnalyticsParameterTax` (Double) (optional)
  - `AnalyticsParameterTransactionID` (String) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventPurchase = @"purchase"

- `


  ### [kFIREventRefund](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventRefund)


  ` E-Commerce Refund event. This event signifies that a refund was issued. Note: If you supply the
  `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency`
  parameter so that revenue metrics can be computed accurately. Params:
  - `AnalyticsParameterAffiliation` (String) (optional)
  - `AnalyticsParameterCoupon` (String) (optional)
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterShipping` (Double) (optional)
  - `AnalyticsParameterTax` (Double) (optional)
  - `AnalyticsParameterTransactionID` (String) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventRefund = @"refund"

- `


  ### [kFIREventRemoveFromCart](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventRemoveFromCart)


  ` E-Commerce Remove from Cart event. This event signifies that an item(s) was removed from a cart.
  Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventRemoveFromCart = @"remove_from_cart"

- `


  ### [kFIREventScreenView](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventScreenView)


  ` Screen View event. This event signifies a screen view. Use this when a screen transition occurs.
  This event can be logged irrespective of whether automatic screen tracking is enabled. Params:
  - `AnalyticsParameterScreenClass` (String) (optional)
  - `AnalyticsParameterScreenName` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventScreenView = @"screen_view"

- `


  ### [kFIREventSearch](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSearch)


  ` Search event. Apps that support search features can use this event to contextualize search
  operations by supplying the appropriate, corresponding parameters. This event can help you
  identify the most popular content in your app. Params:
  - `AnalyticsParameterSearchTerm` (String)
  - `AnalyticsParameterStartDate` (String) (optional)
  - `AnalyticsParameterEndDate` (String) (optional)
  - `AnalyticsParameterNumberOfNights` (Int) (optional) for hotel bookings
  - `AnalyticsParameterNumberOfRooms` (Int) (optional) for hotel bookings
  - `AnalyticsParameterNumberOfPassengers` (Int) (optional) for travel bookings
  - `AnalyticsParameterOrigin` (String) (optional)
  - `AnalyticsParameterDestination` (String) (optional)
  - `AnalyticsParameterTravelClass` (String) (optional) for travel bookings

  #### Declaration

  Objective-C

      static NSString *const kFIREventSearch = @"search"

- `


  ### [kFIREventSelectContent](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSelectContent)


  ` Select Content event. This general purpose event signifies that a user has selected some content
  of a certain type in an app. The content can be any object in your app. This event can help you
  identify popular content and categories of content in your app. Params:
  - `AnalyticsParameterContentType` (String)
  - `AnalyticsParameterItemID` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventSelectContent = @"select_content"

- `


  ### [kFIREventSelectItem](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSelectItem)


  ` Select Item event. This event signifies that an item was selected by a user from a list. Use the
  appropriate parameters to contextualize the event. Use this event to discover the most popular
  items selected. Params:
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterItemListID` (String) (optional)
  - `AnalyticsParameterItemListName` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventSelectItem = @"select_item"

- `


  ### [kFIREventSelectPromotion](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSelectPromotion)


  ` Select promotion event. This event signifies that a user has selected a promotion offer. Use the
  appropriate parameters to contextualize the event, such as the item(s) for which the promotion
  applies. Params:
  - `AnalyticsParameterCreativeName` (String) (optional)
  - `AnalyticsParameterCreativeSlot` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterLocationID` (String) (optional)
  - `AnalyticsParameterPromotionID` (String) (optional)
  - `AnalyticsParameterPromotionName` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventSelectPromotion = @"select_promotion"

- `


  ### [kFIREventShare](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventShare)


  ` Share event. Apps with social features can log the Share event to identify the most viral
  content. Params:
  - `AnalyticsParameterContentType` (String)
  - `AnalyticsParameterItemID` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventShare = @"share"

- `


  ### [kFIREventSignUp](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSignUp)


  ` Sign Up event. This event indicates that a user has signed up for an account in your app. The
  parameter signifies the method by which the user signed up. Use this event to understand the
  different behaviors between logged in and logged out users. Params:
  - `AnalyticsParameterMethod` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventSignUp = @"sign_up"

- `


  ### [kFIREventSpendVirtualCurrency](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventSpendVirtualCurrency)


  ` Spend Virtual Currency event. This event tracks the sale of virtual goods in your app and can
  help you identify which virtual goods are the most popular objects of purchase. Params:
  - `AnalyticsParameterItemName` (String)
  - `AnalyticsParameterVirtualCurrencyName` (String)
  - `AnalyticsParameterValue` (Int or Double)

  #### Declaration

  Objective-C

      static NSString *const kFIREventSpendVirtualCurrency = @"spend_virtual_currency"

- `


  ### [kFIREventTutorialBegin](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventTutorialBegin)


  ` Tutorial Begin event. This event signifies the start of the on-boarding process in your app. Use
  this in a funnel with `AnalyticsEventTutorialComplete` to understand how many users complete
  this process and move on to the full app experience.

  #### Declaration

  Objective-C

      static NSString *const kFIREventTutorialBegin = @"tutorial_begin"

- `


  ### [kFIREventTutorialComplete](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventTutorialComplete)


  ` Tutorial End event. Use this event to signify the user's completion of your app's on-boarding
  process. Add this to a funnel with `AnalyticsEventTutorialBegin` to gauge the completion rate
  of your on-boarding process.

  #### Declaration

  Objective-C

      static NSString *const kFIREventTutorialComplete = @"tutorial_complete"

- `


  ### [kFIREventUnlockAchievement](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventUnlockAchievement)


  ` Unlock Achievement event. Log this event when the user has unlocked an achievement in your
  game. Since achievements generally represent the breadth of a gaming experience, this event can
  help you understand how many users are experiencing all that your game has to offer. Params:
  - `AnalyticsParameterAchievementID` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventUnlockAchievement = @"unlock_achievement"

- `


  ### [kFIREventViewCart](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewCart)


  ` E-commerce View Cart event. This event signifies that a user has viewed their cart. Use this to
  analyze your purchase funnel. Note: If you supply the `AnalyticsParameterValue` parameter, you
  must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be
  computed accurately. Params:
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventViewCart = @"view_cart"

- `


  ### [kFIREventViewItem](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewItem)


  ` View Item event. This event signifies that a user has viewed an item. Use the appropriate
  parameters to contextualize the event. Use this event to discover the most popular items viewed
  in your app. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply
  the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately.
  Params:
  - `AnalyticsParameterCurrency` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterValue` (Double) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventViewItem = @"view_item"

- `


  ### [kFIREventViewItemList](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewItemList)


  ` View Item List event. Log this event when a user sees a list of items or offerings. Params:
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterItemListID` (String) (optional)
  - `AnalyticsParameterItemListName` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventViewItemList = @"view_item_list"

- `


  ### [kFIREventViewPromotion](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewPromotion)


  ` View Promotion event. This event signifies that a promotion was shown to a user. Add this event
  to a funnel with the `AnalyticsEventAddToCart` and `AnalyticsEventPurchase` to gauge your
  conversion process. Params:
  - `AnalyticsParameterCreativeName` (String) (optional)
  - `AnalyticsParameterCreativeSlot` (String) (optional)
  - `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
  - `AnalyticsParameterLocationID` (String) (optional)
  - `AnalyticsParameterPromotionID` (String) (optional)
  - `AnalyticsParameterPromotionName` (String) (optional)

  #### Declaration

  Objective-C

      static NSString *const kFIREventViewPromotion = @"view_promotion"

- `


  ### [kFIREventViewSearchResults](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIREventNames.h@kFIREventViewSearchResults)


  ` View Search Results event. Log this event when the user has been presented with the results of a
  search. Params:
  - `AnalyticsParameterSearchTerm` (String)

  #### Declaration

  Objective-C

      static NSString *const kFIREventViewSearchResults = @"view_search_results"

- `


  ### [kFIRParameterAchievementID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAchievementID)


  ` Game achievement ID (String).

  ```
      let params = [
        AnalyticsParameterAchievementID : "10_matches_won",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterAchievementID = @"achievement_id"

- `


  ### [kFIRParameterAdFormat](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdFormat)


  ` The ad format (e.g. Banner, Interstitial, Rewarded, Native, Rewarded Interstitial, Instream).
  (String).

  ```
      let params = [
        AnalyticsParameterAdFormat : "Banner",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterAdFormat = @"ad_format"

- `


  ### [kFIRParameterAdNetworkClickID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdNetworkClickID)


  ` Ad Network Click ID (String). Used for network-specific click IDs which vary in format.

  ```
      let params = [
        AnalyticsParameterAdNetworkClickID : "1234567",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterAdNetworkClickID = @"aclid"

- `


  ### [kFIRParameterAdPlatform](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdPlatform)


  ` The ad platform (e.g. MoPub, IronSource) (String).

  ```
      let params = [
        AnalyticsParameterAdPlatform : "MoPub",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterAdPlatform = @"ad_platform"

- `


  ### [kFIRParameterAdSource](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdSource)


  ` The ad source (e.g. AdColony) (String).

  ```
      let params = [
        AnalyticsParameterAdSource : "AdColony",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterAdSource = @"ad_source"

- `


  ### [kFIRParameterAdUnitName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAdUnitName)


  ` The ad unit name (e.g. Banner_03) (String).

  ```
      let params = [
        AnalyticsParameterAdUnitName : "Banner_03",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterAdUnitName = @"ad_unit_name"

- `


  ### [kFIRParameterAffiliation](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterAffiliation)


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

  Objective-C

      static NSString *const kFIRParameterAffiliation = @"affiliation"

- `


  ### [kFIRParameterCP1](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCP1)


  ` Campaign custom parameter (String). Used as a method of capturing custom data in a campaign.
  Use varies by network.

  ```
      let params = [
        AnalyticsParameterCP1 : "custom_data",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCP1 = @"cp1"

- `


  ### [kFIRParameterCampaign](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCampaign)


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

  Objective-C

      static NSString *const kFIRParameterCampaign = @"campaign"

- `


  ### [kFIRParameterCampaignID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCampaignID)


  ` Campaign ID (String). Used for keyword analysis to identify a specific product promotion or
  strategic campaign. This is a required key for GA4 data import.

  ```
      let params = [
        AnalyticsParameterCampaignID : "7877652710",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCampaignID = @"campaign_id"

- `


  ### [kFIRParameterCharacter](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCharacter)


  ` Character used in game (String).

  ```
      let params = [
        AnalyticsParameterCharacter : "beat_boss",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCharacter = @"character"

- `


  ### [kFIRParameterContent](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterContent)


  ` Campaign content (String).

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterContent = @"content"

- `


  ### [kFIRParameterContentType](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterContentType)


  ` Type of content selected (String).

  ```
      let params = [
        AnalyticsParameterContentType : "news article",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterContentType = @"content_type"

- `


  ### [kFIRParameterCoupon](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCoupon)


  ` Coupon code used for a purchase (String).

  ```
      let params = [
        AnalyticsParameterCoupon : "SUMMER_FUN",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCoupon = @"coupon"

- `


  ### [kFIRParameterCreativeFormat](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeFormat)


  ` Creative Format (String). Used to identify the high-level classification of the type of ad
  served by a specific campaign.

  ```
      let params = [
        AnalyticsParameterCreativeFormat : "display",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCreativeFormat = @"creative_format"

- `


  ### [kFIRParameterCreativeName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeName)


  ` The name of a creative used in a promotional spot (String).

  ```
      let params = [
        AnalyticsParameterCreativeName : "Summer Sale",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCreativeName = @"creative_name"

- `


  ### [kFIRParameterCreativeSlot](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCreativeSlot)


  ` The name of a creative slot (String).

  ```
      let params = [
        AnalyticsParameterCreativeSlot : "summer_banner2",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCreativeSlot = @"creative_slot"

- `


  ### [kFIRParameterCurrency](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterCurrency)


  ` Currency of the purchase or items associated with the event, in 3-letter
  [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String).

  ```
      let params = [
        AnalyticsParameterCurrency : "USD",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterCurrency = @"currency"

- `


  ### [kFIRParameterDestination](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterDestination)


  ` Flight or Travel destination (String).

  ```
      let params = [
        AnalyticsParameterDestination : "Mountain View, CA",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterDestination = @"destination"

- `


  ### [kFIRParameterDiscount](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterDiscount)


  ` Monetary value of discount associated with a purchase (Double).

  ```
      let params = [
        AnalyticsParameterDiscount : 2.0,
        AnalyticsParameterCurrency : "USD",  // e.g. $2.00 USD
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterDiscount = @"discount"

- `


  ### [kFIRParameterEndDate](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterEndDate)


  ` The arrival date, check-out date or rental end date for the item. This should be in
  YYYY-MM-DD format (String).

  ```
      let params = [
        AnalyticsParameterEndDate : "2015-09-14",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterEndDate = @"end_date"

- `


  ### [kFIRParameterExtendSession](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterExtendSession)


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

  Objective-C

      static NSString *const kFIRParameterExtendSession = @"extend_session"

- `


  ### [kFIRParameterFlightNumber](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterFlightNumber)


  ` Flight number for travel events (String).

  ```
      let params = [
        AnalyticsParameterFlightNumber : "ZZ800",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterFlightNumber = @"flight_number"

- `


  ### [kFIRParameterFreeTrial](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterFreeTrial)


  ` Indicates if the user is on a free trial of a subscription. Specify 1 to indicate true and 0 to
  indicate false (Int).

  ```
      let params = [
        AnalyticsParameterFreeTrial : 1,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterFreeTrial = @"free_trial"

- `


  ### [kFIRParameterGroupID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterGroupID)


  ` Group/clan/guild ID (String).

  ```
      let params = [
        AnalyticsParameterGroupID : "g1",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterGroupID = @"group_id"

- `


  ### [kFIRParameterIndex](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterIndex)


  ` The index of the item in a list (Int).

  ```
      let params = [
        AnalyticsParameterIndex : 5,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterIndex = @"index"

- `


  ### [kFIRParameterItemBrand](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemBrand)


  ` Item brand (String).

  ```
      let params = [
        AnalyticsParameterItemBrand : "Google",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemBrand = @"item_brand"

- `


  ### [kFIRParameterItemCategory](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory)


  ` Item category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory : "pants",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemCategory = @"item_category"

- `


  ### [kFIRParameterItemCategory2](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory2)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory2 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemCategory2 = @"item_category2"

- `


  ### [kFIRParameterItemCategory3](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory3)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory3 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemCategory3 = @"item_category3"

- `


  ### [kFIRParameterItemCategory4](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory4)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory4 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemCategory4 = @"item_category4"

- `


  ### [kFIRParameterItemCategory5](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemCategory5)


  ` Item Category (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemCategory5 : "pants",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemCategory5 = @"item_category5"

- `


  ### [kFIRParameterItemID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemID)


  ` Item ID (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemID : "SKU_12345",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemID = @"item_id"

- `


  ### [kFIRParameterItemListID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListID)


  ` The ID of the list in which the item was presented to the user (String).

  ```
      let params = [
        AnalyticsParameterItemListID : "ABC123",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemListID = @"item_list_id"

- `


  ### [kFIRParameterItemListName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemListName)


  ` The name of the list in which the item was presented to the user (String).

  ```
      let params = [
        AnalyticsParameterItemListName : "Related products",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemListName = @"item_list_name"

- `


  ### [kFIRParameterItemName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemName)


  ` Item Name (context-specific) (String).

  ```
      let params = [
        AnalyticsParameterItemName : "jeggings",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemName = @"item_name"

- `


  ### [kFIRParameterItemVariant](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItemVariant)


  ` Item variant (String).

  ```
      let params = [
        AnalyticsParameterItemVariant : "Black",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterItemVariant = @"item_variant"

- `


  ### [kFIRParameterItems](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterItems)


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

  Objective-C

      static NSString *const kFIRParameterItems = @"items"

- `


  ### [kFIRParameterLevel](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevel)


  ` Level in game (Int).

  ```
      let params = [
        AnalyticsParameterLevel : 42,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterLevel = @"level"

- `


  ### [kFIRParameterLevelName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLevelName)


  ` The name of a level in a game (String).

  ```
      let params = [
        AnalyticsParameterLevelName : "room_1",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterLevelName = @"level_name"

- `


  ### [kFIRParameterLocation](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLocation)


  ` Location (String). The Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated event. Alternatively, you can supply your own custom
  Location ID.

  ```
      let params = [
        AnalyticsParameterLocation : "ChIJiyj437sx3YAR9kUWC8QkLzQ",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterLocation = @"location"

- `


  ### [kFIRParameterLocationID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterLocationID)


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

  Objective-C

      static NSString *const kFIRParameterLocationID = @"location_id"

- `


  ### [kFIRParameterMarketingTactic](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMarketingTactic)


  ` Marketing Tactic (String). Used to identify the targeting criteria applied to a specific
  campaign.

  ```
      let params = [
        AnalyticsParameterMarketingTactic : "Remarketing",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterMarketingTactic = @"marketing_tactic"

- `


  ### [kFIRParameterMedium](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMedium)


  ` The advertising or marketing medium, for example: cpc, banner, email, push. Highly recommended
  (String).

  ```
      let params = [
        AnalyticsParameterMedium : "email",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterMedium = @"medium"

- `


  ### [kFIRParameterMethod](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterMethod)


  ` A particular approach used in an operation; for example, "facebook" or "email" in the context
  of a sign_up or login event. (String).

  ```
      let params = [
        AnalyticsParameterMethod : "google",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterMethod = @"method"

- `


  ### [kFIRParameterNumberOfNights](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfNights)


  ` Number of nights staying at hotel (Int).

  ```
      let params = [
        AnalyticsParameterNumberOfNights : 3,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterNumberOfNights = @"number_of_nights"

- `


  ### [kFIRParameterNumberOfPassengers](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfPassengers)


  ` Number of passengers traveling (Int).

  ```
      let params = [
        AnalyticsParameterNumberOfPassengers : 11,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterNumberOfPassengers = @"number_of_passengers"

- `


  ### [kFIRParameterNumberOfRooms](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterNumberOfRooms)


  ` Number of rooms for travel events (Int).

  ```
      let params = [
        AnalyticsParameterNumberOfRooms : 2,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterNumberOfRooms = @"number_of_rooms"

- `


  ### [kFIRParameterOrigin](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterOrigin)


  ` Flight or Travel origin (String).

  ```
      let params = [
        AnalyticsParameterOrigin : "Mountain View, CA",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterOrigin = @"origin"

- `


  ### [kFIRParameterPaymentType](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPaymentType)


  ` The chosen method of payment (String).

  ```
      let params = [
        AnalyticsParameterPaymentType : "Visa",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterPaymentType = @"payment_type"

- `


  ### [kFIRParameterPrice](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPrice)


  ` Purchase price (Double).

  ```
      let params = [
        AnalyticsParameterPrice : 1.0,
        AnalyticsParameterCurrency : "USD",  // e.g. $1.00 USD
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterPrice = @"price"

- `


  ### [kFIRParameterPriceIsDiscounted](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPriceIsDiscounted)


  ` Indicates if an item's price is discounted. Specify 1 to indicate true and 0 to indicate false
  (Int).

  ```
      let params = [
        AnalyticsParameterPriceIsDiscounted : 1,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterPriceIsDiscounted = @"price_is_discounted"

- `


  ### [kFIRParameterProductID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterProductID)


  ` The ID of a product (String).

  ```
      let params = [
        AnalyticsParameterProductID : "PROD_12345",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterProductID = @"product_id"

- `


  ### [kFIRParameterProductName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterProductName)


  ` The name of a product (String).

  ```
      let params = [
        AnalyticsParameterProductName : "My Awesome Product",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterProductName = @"product_name"

- `


  ### [kFIRParameterPromotionID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionID)


  ` The ID of a product promotion (String).

  ```
      let params = [
        AnalyticsParameterPromotionID : "ABC123",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterPromotionID = @"promotion_id"

- `


  ### [kFIRParameterPromotionName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterPromotionName)


  ` The name of a product promotion (String).

  ```
      let params = [
        AnalyticsParameterPromotionName : "Summer Sale",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterPromotionName = @"promotion_name"

- `


  ### [kFIRParameterQuantity](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterQuantity)


  ` Purchase quantity (Int).

  ```
      let params = [
        AnalyticsParameterQuantity : 1,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterQuantity = @"quantity"

- `


  ### [kFIRParameterScore](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScore)


  ` Score in game (Int).

  ```
      let params = [
        AnalyticsParameterScore : 4200,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterScore = @"score"

- `


  ### [kFIRParameterScreenClass](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScreenClass)


  ` Current screen class, such as the class name of the UIViewController, logged with screen_view
  event and added to every event (String).

  ```
      let params = [
        AnalyticsParameterScreenClass : "LoginViewController",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterScreenClass = @"screen_class"

- `


  ### [kFIRParameterScreenName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterScreenName)


  ` Current screen name, such as the name of the UIViewController, logged with screen_view event and
  added to every event (String).

  ```
      let params = [
        AnalyticsParameterScreenName : "LoginView",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterScreenName = @"screen_name"

- `


  ### [kFIRParameterSearchTerm](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSearchTerm)


  ` The search string/keywords used (String).

  ```
      let params = [
        AnalyticsParameterSearchTerm : "periodic table",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterSearchTerm = @"search_term"

- `


  ### [kFIRParameterShipping](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterShipping)


  ` Shipping cost associated with a transaction (Double).

  ```
      let params = [
        AnalyticsParameterShipping : 5.99,
        AnalyticsParameterCurrency : "USD",  // e.g. $5.99 USD
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterShipping = @"shipping"

- `


  ### [kFIRParameterShippingTier](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterShippingTier)


  ` The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item
  (String).

  ```
      let params = [
        AnalyticsParameterShippingTier : "Ground",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterShippingTier = @"shipping_tier"

- `


  ### [kFIRParameterSource](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSource)


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

  Objective-C

      static NSString *const kFIRParameterSource = @"source"

- `


  ### [kFIRParameterSourcePlatform](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSourcePlatform)


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

  Objective-C

      static NSString *const kFIRParameterSourcePlatform = @"source_platform"

- `


  ### [kFIRParameterStartDate](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterStartDate)


  ` The departure date, check-in date or rental start date for the item. This should be in
  YYYY-MM-DD format (String).

  ```
      let params = [
        AnalyticsParameterStartDate : "2015-09-14",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterStartDate = @"start_date"

- `


  ### [kFIRParameterSubscription](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSubscription)


  ` Indicates if the purchase is a subscription. Specify 1 to indicate true and 0 to indicate false
  (Int).

  ```
      let params = [
        AnalyticsParameterSubscription : 1,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterSubscription = @"subscription"

- `


  ### [kFIRParameterSuccess](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterSuccess)


  ` The result of an operation. Specify 1 to indicate success and 0 to indicate failure (Int).

  ```
      let params = [
        AnalyticsParameterSuccess : 1,
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterSuccess = @"success"

- `


  ### [kFIRParameterTax](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTax)


  ` Tax cost associated with a transaction (Double).

  ```
      let params = [
        AnalyticsParameterTax : 2.43,
        AnalyticsParameterCurrency : "USD",  // e.g. $2.43 USD
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterTax = @"tax"

- `


  ### [kFIRParameterTerm](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTerm)


  ` If you're manually tagging keyword campaigns, you should use utm_term to specify the keyword
  (String).

  ```
      let params = [
        AnalyticsParameterTerm : "game",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterTerm = @"term"

- `


  ### [kFIRParameterTransactionID](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTransactionID)


  ` The unique identifier of a transaction (String).

  ```
      let params = [
        AnalyticsParameterTransactionID : "T12345",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterTransactionID = @"transaction_id"

- `


  ### [kFIRParameterTravelClass](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterTravelClass)


  ` Travel class (String).

  ```
      let params = [
        AnalyticsParameterTravelClass : "business",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterTravelClass = @"travel_class"

- `


  ### [kFIRParameterValue](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterValue)


  ` A context-specific numeric value which is accumulated automatically for each event type. This is
  a general purpose parameter that is useful for accumulating a key metric that pertains to an
  event. Examples include revenue, distance, time and points. Value should be specified as Int or
  Double.
  Notes: Values for pre-defined currency-related events (such as `AnalyticsEventAddToCart`)
  should be supplied using Double and must be accompanied by a `AnalyticsParameterCurrency`
  parameter. The valid range of accumulated values is
  \[-9,223,372,036,854.77, 9,223,372,036,854.77\]. Supplying a non-numeric value, omitting the
  corresponding `AnalyticsParameterCurrency` parameter, or supplying an invalid
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

  Objective-C

      static NSString *const kFIRParameterValue = @"value"

- `


  ### [kFIRParameterVirtualCurrencyName](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRParameterNames.h@kFIRParameterVirtualCurrencyName)


  ` Name of virtual currency type (String).

  ```
      let params = [
        AnalyticsParameterVirtualCurrencyName : "virtual_currency_name",
        // ...
      ]
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRParameterVirtualCurrencyName =
          @"virtual_currency_name"

- `


  ### [kFIRUserPropertyAllowAdPersonalizationSignals](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRUserPropertyNames.h@kFIRUserPropertyAllowAdPersonalizationSignals)


  ` Indicates whether events logged by Google Analytics can be used to personalize ads for the user.
  Set to "YES" to enable, or "NO" to disable. Default is enabled. See the
  [documentation](https://firebase.google.com/support/guides/disable-analytics) for
  more details and information about related settings.

  ```
      Analytics.setUserProperty("NO", forName: AnalyticsUserPropertyAllowAdPersonalizationSignals)
  ```

  #### Declaration

  Objective-C

      static NSString *const kFIRUserPropertyAllowAdPersonalizationSignals =
          @"allow_personalized_ads"

- `


  ### [kFIRUserPropertySignUpMethod](https://firebase.google.com/docs/reference/ios/firebaseanalytics/api/reference/Constants#/c:FIRUserPropertyNames.h@kFIRUserPropertySignUpMethod)


  ` The method used to sign in. For example, "google", "facebook" or "twitter".

  #### Declaration

  Objective-C

      static NSString *const kFIRUserPropertySignUpMethod = @"sign_up_method"