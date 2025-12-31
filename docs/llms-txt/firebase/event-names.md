# Source: https://firebase.google.com/docs/reference/cpp/group/event-names.md.txt

# Source: https://firebase.google.com/docs/reference/unity/group/event-names.md.txt

# Analytics Events

Predefined event names.

## Summary

An Event is an important occurrence in your app that you want to measure. You can report up to 500 different types of Events per app and you can associate up to 25 unique parameters with each Event type. Some common events are suggested below, but you may also choose to specify custom Event types that are associated with your specific app. Each event type is identified by a unique name. Event names can be up to 40 characters long, may only contain alphanumeric characters and underscores ("_"), and must start with an alphabetic character. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used.

|                                                                                                           ### Variables                                                                                                           ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| [EventAdImpression](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaf2085a1d3cb08e9f6db2bcbaab1a26d4)` = "ad_impression"`                  | `string` Ad Impression event.               |
| [EventAddPaymentInfo](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaf528d748fa6ba3697a39e890e20ff5b6)` = "add_payment_info"`             | `string` Add Payment Info event.            |
| [EventAddShippingInfo](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga38f1b76e1897cf5074c19191ffef0c5f)` = "add_shipping_info"`           | `string` Add Shipping Info event.           |
| [EventAddToCart](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga780291db2d1875e682a131b0e7822664)` = "add_to_cart"`                       | `string` E-Commerce Add To Cart event.      |
| [EventAddToWishlist](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gab9d7a471d25b43c9701d25877effcccd)` = "add_to_wishlist"`               | `string` E-Commerce Add To Wishlist event.  |
| [EventAppOpen](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaa0116dbd120d6181e3328b726d776312)` = "app_open"`                            | `string` App Open event.                    |
| [EventBeginCheckout](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga46ed426c3c79cbb8b88b294da64e677d)` = "begin_checkout"`                | `string` E-Commerce Begin Checkout event.   |
| [EventCampaignDetails](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga13eaeee5a2539f864f07126bce8011f5)` = "campaign_details"`            | `string` Campaign Detail event.             |
| [EventEarnVirtualCurrency](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gabc9792def19d804d84cb847a837063ab)` = "earn_virtual_currency"`   | `string` Earn Virtual Currency event.       |
| [EventGenerateLead](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gae09776188902a499aee2c2b49c72655b)` = "generate_lead"`                  | `string` Generate Lead event.               |
| [EventInAppPurchase](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga45ba4cdcdad82825840bec002201c1d6)` = "in_app_purchase"`               | `string` In-App Purchase event.             |
| [EventJoinGroup](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaa7812a4e7c555dc1a3be98b47c77356a)` = "join_group"`                        | `string` Join Group event.                  |
| [EventLevelEnd](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga06d0c36e04e2253ef6efcd1e5087cd52)` = "level_end"`                          | `string` Level End event.                   |
| [EventLevelStart](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga74f7261b7ce9da5d4eb90421045be246)` = "level_start"`                      | `string` Level Start event.                 |
| [EventLevelUp](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gafd7f594b096c2a785ffd791677f6c51d)` = "level_up"`                            | `string` Level Up event.                    |
| [EventLogin](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga4777f25dec0d444ce981565aac37a5d9)` = "login"`                                 | `string` Login event.                       |
| [EventPostScore](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gae6c7bae26bf168725550d92fde85686b)` = "post_score"`                        | `string` Post Score event.                  |
| [EventPurchase](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga28a024454ff4a4be16fd705a986135e1)` = "purchase"`                           | `string` E-Commerce Purchase event.         |
| [EventRefund](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gac2ad39117f0d330ebb8f665a13fb0f9b)` = "refund"`                               | `string` E-Commerce Refund event.           |
| [EventRemoveFromCart](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga7332a67a09a87fd5213053dd81781208)` = "remove_from_cart"`             | `string` E-Commerce Remove from Cart event. |
| [EventScreenView](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaa0dac3af8c39a1002c07e0a65727c4dc)` = "screen_view"`                      | `string` Screen View event.                 |
| [EventSearch](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gadb7a4258a2712c9f28d60b1579421d56)` = "search"`                               | `string` Search event.                      |
| [EventSelectContent](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga53ea47346994ec8c2c13ea8a4396e78e)` = "select_content"`                | `string` Select Content event.              |
| [EventSelectItem](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gae1ded6912cc85dd90e566f3c698f67dd)` = "select_item"`                      | `string` Select Item event.                 |
| [EventSelectPromotion](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gae7f7055b6ef082137e6860ecb9d4b6d7)` = "select_promotion"`            | `string` Select promotion event.            |
| [EventShare](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaa5873d3d44141caaebb64236effe4260)` = "share"`                                 | `string` Share event.                       |
| [EventSignUp](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga02eab2ba8ebebbdb1e8b78fdfb289a2a)` = "sign_up"`                              | `string` Sign Up event.                     |
| [EventSpendVirtualCurrency](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gad7ad7c48cb9e4cddefced2165c5df7d3)` = "spend_virtual_currency"` | `string` Spend Virtual Currency event.      |
| [EventTutorialBegin](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaae32163dc826f78f45c3dbe687d5b495)` = "tutorial_begin"`                | `string` Tutorial Begin event.              |
| [EventTutorialComplete](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gabf4a2a738c35d247c2833a6106b542d5)` = "tutorial_complete"`          | `string` Tutorial End event.                |
| [EventUnlockAchievement](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga3bf9935c3379ea13dc5bdf1f5992da08)` = "unlock_achievement"`        | `string` Unlock Achievement event.          |
| [EventViewCart](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga85e2fdaae405a8d2962195d00f72c9ef)` = "view_cart"`                          | `string` E-commerce View Cart event.        |
| [EventViewItem](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1ga96f6867734efe261a80c669d260726a2)` = "view_item"`                          | `string` View Item event.                   |
| [EventViewItemList](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gac2672eae72ea0c741d228c39f676ae20)` = "view_item_list"`                 | `string` View Item List event.              |
| [EventViewPromotion](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaab70fd81164d1a394ee23923ff4cf7de)` = "view_promotion"`                | `string` View Promotion event.              |
| [EventViewSearchResults](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gaf5304788628f1096bf6818c275ca1daa)` = "view_search_results"`       | `string` View Search Results event.         |

## Variables

### EventAdImpression

```c#
string EventAdImpression =
    "ad_impression"
```  
Ad Impression event.

This event signifies when a user sees an ad impression. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterAdPlatform`(String) (optional)
- `AnalyticsParameterAdFormat`(String) (optional)
- `AnalyticsParameterAdSource`(String) (optional)
- `AnalyticsParameterAdUnitName`(String) (optional)
- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventAddPaymentInfo

```c#
string EventAddPaymentInfo =
    "add_payment_info"
```  
Add Payment Info event.

This event signifies that a user has submitted their payment information. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCoupon`(String) (optional)
- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterPaymentType`(String) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventAddShippingInfo

```c#
string EventAddShippingInfo =
    "add_shipping_info"
```  
Add Shipping Info event.

This event signifies that a user has submitted their shipping information. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCoupon`(String) (optional)
- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterShippingTier`(String) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventAddToCart

```c#
string EventAddToCart = "add_to_cart"
```  
E-Commerce Add To Cart event.

This event signifies that an item(s) was added to a cart for purchase. Add this event to a funnel with`AnalyticsEventPurchase`to gauge the effectiveness of your checParameter(kout, If you supply the`AnalyticsParameterValue`parameter), you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventAddToWishlist

```c#
string EventAddToWishlist =
    "add_to_wishlist"
```  
E-Commerce Add To Wishlist event.

This event signifies that an item was added to a wishlist. Use this event to identify popular gift items. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventAppOpen

```c#
string EventAppOpen = "app_open"
```  
App Open event.

By logging this event when an App becomes active, developers can understand how often users leave and return during the course of a Session. Although Sessions are automatically reported, this event can provide further clarification around the continuous engagement of app-users.  

### EventBeginCheckout

```c#
string EventBeginCheckout =
    "begin_checkout"
```  
E-Commerce Begin Checkout event.

This event signifies that a user has begun the process of checking out. Add this event to a funnel with your`AnalyticsEventPurchase`event to gauge the effectiveness of your checkout process. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCoupon`(String) (optional)
- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventCampaignDetails

```c#
string EventCampaignDetails =
    "campaign_details"
```  
Campaign Detail event.

Log this event to supply the referral details of a re-engagement campaign. Note: you must supply at least one of the required parameters AnalyticsParameterSource, AnalyticsParameterMedium or AnalyticsParameterCampaign. Params:

<br />

- `AnalyticsParameterSource`(String)
- `AnalyticsParameterMedium`(String)
- `AnalyticsParameterCampaign`(String)
- `AnalyticsParameterTerm`(String) (optional)
- `AnalyticsParameterContent`(String) (optional)
- `AnalyticsParameterAdNetworkClickID`(String) (optional)
- `AnalyticsParameterCP1`(String) (optional)
- `AnalyticsParameterCampaignID`(String) (optional)
- `AnalyticsParameterCreativeFormat`(String) (optional)
- `AnalyticsParameterMarketingTactic`(String) (optional)
- `AnalyticsParameterSourcePlatform`(String) (optional)

<br />

### EventEarnVirtualCurrency

```c#
string EventEarnVirtualCurrency = "earn_virtual_currency"
```  
Earn Virtual Currency event.

This event tracks the awarding of virtual currency in your app. Log this along with`AnalyticsEventSpendVirtualCurrency`to better understand your virtual economy. Params:

<br />

- `AnalyticsParameterVirtualCurrencyName`(String)
- `AnalyticsParameterValue`(Int or Double)

<br />

### EventGenerateLead

```c#
string EventGenerateLead =
    "generate_lead"
```  
Generate Lead event.

Log this event when a lead has been generated in the app to understand the efficacy of your install and re-engagement campaigns. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventInAppPurchase

```c#
string EventInAppPurchase =
     "in_app_purchase"
```  
In-App Purchase event.

This event signifies that extra content or a subscription was purchased by a user inside an app. Note: This is different from the ecommerce purchase event. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCurrency`(String)
- `AnalyticsParameterFreeTrial`(Int) (optional)
- `AnalyticsParameterPrice`(Double) (optional)
- `AnalyticsParameterPriceIsDiscounted`(Int) (optional)
- `AnalyticsParameterProductID`(String) (optional)
- `AnalyticsParameterProductName`(String) (optional)
- `AnalyticsParameterQuantity`(Int) (optional)
- `AnalyticsParameterSubscription`(Int) (optional)
- `AnalyticsParameterValue`(Double)

<br />

### EventJoinGroup

```c#
string EventJoinGroup = "join_group"
```  
Join Group event.

Log this event when a user joins a group such as a guild, team or family. Use this event to analyze how popular certain groups or social features are in your app. Params:

<br />

- `AnalyticsParameterGroupID`(String)

<br />

### EventLevelEnd

```c#
string EventLevelEnd = "level_end"
```  
Level End event.

Log this event when the user finishes a level. Params:

<br />

- `AnalyticsParameterLevelName`(String)
- `AnalyticsParameterSuccess`(String)

<br />

### EventLevelStart

```c#
string EventLevelStart = "level_start"
```  
Level Start event.

Log this event when the user starts a new level. Params:

<br />

- `AnalyticsParameterLevelName`(String)

<br />

### EventLevelUp

```c#
string EventLevelUp = "level_up"
```  
Level Up event.

This event signifies that a player has leveled up in your gaming app. It can help you gauge the level distribution of your userbase and help you identify certain levels that are difficult to pass. Params:

<br />

- `AnalyticsParameterLevel`(Int)
- `AnalyticsParameterCharacter`(String) (optional)

<br />

### EventLogin

```c#
string EventLogin = "login"
```  
Login event.

Apps with a login feature can report this event to signify that a user has logged in.  

### EventPostScore

```c#
string EventPostScore = "post_score"
```  
Post Score event.

Log this event when the user posts a score in your gaming app. This event can help you understand how users are actually performing in your game and it can help you correlate high scores with certain audiences or behaviors. Params:

<br />

- `AnalyticsParameterScore`(Int)
- `AnalyticsParameterLevel`(Int) (optional)
- `AnalyticsParameterCharacter`(String) (optional)

<br />

### EventPurchase

```c#
string EventPurchase = "purchase"
```  
E-Commerce Purchase event.

This event signifies that an item(s) was purchased by a user. Note: This is different from the in-app purchase event, which is reported automatically for App Store-based apps. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterAffiliation`(String) (optional)
- `AnalyticsParameterCoupon`(String) (optional)
- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterEndDate`(String) (optional)
- `AnalyticsParameterItemID`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterShipping`(Double) (optional)
- `AnalyticsParameterStartDate`(String) (optional)
- `AnalyticsParameterTax`(Double) (optional)
- `AnalyticsParameterTransactionID`(String) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventRefund

```c#
string EventRefund = "refund"
```  
E-Commerce Refund event.

This event signifies that a refund was issued. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterAffiliation`(String) (optional)
- `AnalyticsParameterCoupon`(String) (optional)
- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterShipping`(Double) (optional)
- `AnalyticsParameterTax`(Double) (optional)
- `AnalyticsParameterTransactionID`(String) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventRemoveFromCart

```c#
string EventRemoveFromCart =
    "remove_from_cart"
```  
E-Commerce Remove from Cart event.

This event signifies that an item(s) was removed from a cart. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventScreenView

```c#
string EventScreenView = "screen_view"
```  
Screen View event.

This event signifies a screen view. Use this when a screen transition occurs. This event can be logged irrespective of whether automatic screen tracking is enabled. Params:

<br />

- `AnalyticsParameterScreenClass`(String) (optional)
- `AnalyticsParameterScreenName`(String) (optional)

<br />

### EventSearch

```c#
string EventSearch = "search"
```  
Search event.

Apps that support search features can use this event to contextualize search operations by supplying the appropriate, corresponding parameters. This event can help you identify the most popular content in your app. Params:

<br />

- `AnalyticsParameterSearchTerm`(String)
- `AnalyticsParameterStartDate`(String) (optional)
- `AnalyticsParameterEndDate`(String) (optional)
- `AnalyticsParameterNumberOfNights`(Int) (optional) for hotel bookings
- `AnalyticsParameterNumberOfRooms`(Int) (optional) for hotel bookings
- `AnalyticsParameterNumberOfPassengers`(Int) (optional) for travel bookings
- `AnalyticsParameterOrigin`(String) (optional)
- `AnalyticsParameterDestination`(String) (optional)
- `AnalyticsParameterTravelClass`(String) (optional) for travel bookings

<br />

### EventSelectContent

```c#
string EventSelectContent =
    "select_content"
```  
Select Content event.

This general purpose event signifies that a user has selected some content of a certain type in an app. The content can be any object in your app. This event can help you identify popular content and categories of content in your app. Params:

<br />

- `AnalyticsParameterContentType`(String)
- `AnalyticsParameterItemID`(String)

<br />

### EventSelectItem

```c#
string EventSelectItem = "select_item"
```  
Select Item event.

This event signifies that an item was selected by a user from a list. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items selected. Params:

<br />

- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterItemListID`(String) (optional)
- `AnalyticsParameterItemListName`(String) (optional)

<br />

### EventSelectPromotion

```c#
string EventSelectPromotion =
    "select_promotion"
```  
Select promotion event.

This event signifies that a user has selected a promotion offer. Use the appropriate parameters to contextualize the event, such as the item(s) for which the promotion applies. Params:

<br />

- `AnalyticsParameterCreativeName`(String) (optional)
- `AnalyticsParameterCreativeSlot`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterLocationID`(String) (optional)
- `AnalyticsParameterPromotionID`(String) (optional)
- `AnalyticsParameterPromotionName`(String) (optional)

<br />

### EventShare

```c#
string EventShare = "share"
```  
Share event.

Apps with social features can log the Share event to identify the most viral content. Params:

<br />

- `AnalyticsParameterContentType`(String)
- `AnalyticsParameterItemID`(String)

<br />

### EventSignUp

```c#
string EventSignUp = "sign_up"
```  
Sign Up event.

This event indicates that a user has signed up for an account in your app. The parameter signifies the method by which the user signed up. Use this event to understand the different behaviors between logged in and logged out users. Params:

<br />

- `AnalyticsParameterMethod`(String)

<br />

### EventSpendVirtualCurrency

```c#
string EventSpendVirtualCurrency = "spend_virtual_currency"
```  
Spend Virtual Currency event.

This event tracks the sale of virtual goods in your app and can help you identify which virtual goods are the most popular objects of purchase. Params:

<br />

- `AnalyticsParameterItemName`(String)
- `AnalyticsParameterVirtualCurrencyName`(String)
- `AnalyticsParameterValue`(Int or Double)

<br />

### EventTutorialBegin

```c#
string EventTutorialBegin =
    "tutorial_begin"
```  
Tutorial Begin event.

This event signifies the start of the on-boarding process in your app. Use this in a funnel with`AnalyticsEventTutorialComplete`to understand how many users complete this process and move on to the full app experience.  

### EventTutorialComplete

```c#
string EventTutorialComplete =
    "tutorial_complete"
```  
Tutorial End event.

Use this event to signify the user's completion of your app's on-boarding process. Add this to a funnel with`AnalyticsEventTutorialBegin`to gauge the completion rate of your on-boarding process.  

### EventUnlockAchievement

```c#
string EventUnlockAchievement =
    "unlock_achievement"
```  
Unlock Achievement event.

Log this event when the user has unlocked an achievement in your game. Since achievements generally represent the breadth of a gaming experience, this event can help you understand how many users are experiencing all that your game has to offer. Params:

<br />

- `AnalyticsParameterAchievementID`(String)

<br />

### EventViewCart

```c#
string EventViewCart = "view_cart"
```  
E-commerce View Cart event.

This event signifies that a user has viewed their cart. Use this to analyze your purchase funnel. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventViewItem

```c#
string EventViewItem = "view_item"
```  
View Item event.

This event signifies that a user has viewed an item. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items viewed in your app. Note: If you supply the`AnalyticsParameterValue`parameter, you must also supply the`AnalyticsParameterCurrency`parameter so that revenue metrics can be computed accurately. Params:

<br />

- `AnalyticsParameterCurrency`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue`(Double) (optional)

<br />

### EventViewItemList

```c#
string EventViewItemList =
    "view_item_list"
```  
View Item List event.

Log this event when a user sees a list of items or offerings. Params:

<br />

- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterItemListID`(String) (optional)
- `AnalyticsParameterItemListName`(String) (optional)

<br />

### EventViewPromotion

```c#
string EventViewPromotion =
    "view_promotion"
```  
View Promotion event.

This event signifies that a promotion was shown to a user. Add this event to a funnel with the`AnalyticsEventAddToCart`and`AnalyticsEventPurchase`to gauge your conversion process. Params:

<br />

- `AnalyticsParameterCreativeName`(String) (optional)
- `AnalyticsParameterCreativeSlot`(String) (optional)
- `AnalyticsParameterItems`(\[\[String: Any\]\]) (optional)
- `AnalyticsParameterLocationID`(String) (optional)
- `AnalyticsParameterPromotionID`(String) (optional)
- `AnalyticsParameterPromotionName`(String) (optional)

<br />

### EventViewSearchResults

```c#
string EventViewSearchResults =
    "view_search_results"
```  
View Search Results event.

Log this event when the user has been presented with the results of a search. Params:

<br />

- `AnalyticsParameterSearchTerm`(String)

<br />