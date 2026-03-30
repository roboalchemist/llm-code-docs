# Source: https://firebase.google.com/docs/reference/cpp/group/event-names.md.txt

# Analytics Events

# Analytics Events

Predefined event names.

## Summary

An Event is an important occurrence in your app that you want to measure. You can report up to 500 different types of Events per app and you can associate up to 25 unique parameters with each Event type. Some common events are suggested below, but you may also choose to specify custom Event types that are associated with your specific app. Each event type is identified by a unique name. Event names can be up to 40 characters long, may only contain alphanumeric characters and underscores ("_"), and must start with an alphabetic character. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used.

| ### Variables ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga9e36c790cdfbc729fc92d96ce3b58e00 = "ad_impression"` | `const char *const` Ad Impression event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaef9cda17e92365cc965b83daf7b753ce = "add_payment_info"` | `const char *const` Add Payment Info event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga0a53f07d6efbbbe3aa48a48596ff8c8b = "add_shipping_info"` | `const char *const` Add Shipping Info event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga7f6119a5d4c687f4b33c2672e41526a8 = "add_to_cart"` | `const char *const` E-Commerce Add To Cart event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaad30af9fe4bdf8ded2455bec922e8246 = "add_to_wishlist"` | `const char *const` E-Commerce Add To Wishlist event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga8b0adfcfda4d882d897bb250eec188ae = "app_open"` | `const char *const` [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Open event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga91900ee2595a936ecff7f6fffcfb6456 = "begin_checkout"` | `const char *const` E-Commerce Begin Checkout event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gafb57501cd5491fdd321590b2f522e36b = "campaign_details"` | `const char *const` Campaign Detail event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaedc04823e7798672ffec4214072b16c8 = "earn_virtual_currency"` | `const char *const` Earn Virtual Currency event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gab056485cdcf6ca2d14974847f811a714 = "generate_lead"` | `const char *const` Generate Lead event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gab884b744d69444f1af61b97be2209289 = "in_app_purchase"` | `const char *const` In-App Purchase event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga5a49785c11b2f422ffb2b4893ed40480 = "join_group"` | `const char *const` Join Group event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gac54f9dbb711b270ebc4087ec98112e8f = "level_end"` | `const char *const` Level End event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga06a59a92243e5845e2db014ca0eee663 = "level_start"` | `const char *const` Level Start event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaeebb9647c405acc7e8a6c09052beac86 = "level_up"` | `const char *const` Level Up event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaecaeadd193279c625cd30fac90380ec7 = "login"` | `const char *const` Login event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaed08729d28824e6a7c0fcf4ee8a40112 = "post_score"` | `const char *const` Post Score event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga8f07f269a5678bfddfb7489932667ab7 = "purchase"` | `const char *const` E-Commerce Purchase event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga3782cf3daccb7e55514ad88dd3961aa5 = "refund"` | `const char *const` E-Commerce Refund event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga72f1626522cdd2c25c90eef9c90d56c4 = "remove_from_cart"` | `const char *const` E-Commerce Remove from Cart event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga44c7e13ca539a532af72ea6654b5104f = "screen_view"` | `const char *const` Screen View event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gab9504e187b6a1e70253949f3636ae72a = "search"` | `const char *const` Search event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gabdca2ea4590e2e3fb35bf315cac0e083 = "select_content"` | `const char *const` Select Content event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga31ac5c69dc2553c3f1ba9cf32c7873ad = "select_item"` | `const char *const` Select Item event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga2a259238755b2828fac433342a70a6d7 = "select_promotion"` | `const char *const` Select promotion event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gac33436f65d31b24bca522ce471d5e18d = "share"` | `const char *const` Share event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaf0ba6dd9991ef30ae2155e4946ddf1c7 = "sign_up"` | `const char *const` Sign Up event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga2a623b4ca85c67959041bee1cc45b97d = "spend_virtual_currency"` | `const char *const` Spend Virtual Currency event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga95c5f47b99b77218aebd666e2fcea38f = "tutorial_begin"` | `const char *const` Tutorial Begin event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gad0fdfc2f96c176ab29dd244032ad21b5 = "tutorial_complete"` | `const char *const` Tutorial End event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga7a3cf45eb5b10d7bded16f0c6cc7b353 = "unlock_achievement"` | `const char *const` Unlock Achievement event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gae1ceb7764e2ae646a1fcd504962fbed4 = "view_cart"` | `const char *const` E-commerce View Cart event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga8746cf7d6084f59b2b5e5c32bf69e51a = "view_item"` | `const char *const` View Item event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gaf8336b7c9f27db01db6a2539b7884f90 = "view_item_list"` | `const char *const` View Item List event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1gafe5f14597b78b8316bfc6bcf265d0ff3 = "view_promotion"` | `const char *const` View Promotion event. |
| `https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names_1ga83e066eb51879656344e56b866241918 = "view_search_results"` | `const char *const` View Search Results event. |

## Variables

### kEventAdImpression

```c++
const char *const kEventAdImpression =
    "ad_impression"
```
Ad Impression event.

This event signifies when a user sees an ad impression. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterAdPlatform` (String) (optional)
- `AnalyticsParameterAdFormat` (String) (optional)
- `AnalyticsParameterAdSource` (String) (optional)
- `AnalyticsParameterAdUnitName` (String) (optional)
- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventAddPaymentInfo

```c++
const char *const kEventAddPaymentInfo =
    "add_payment_info"
```
Add Payment Info event.

This event signifies that a user has submitted their payment information. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCoupon` (String) (optional)
- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterPaymentType` (String) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventAddShippingInfo

```c++
const char *const kEventAddShippingInfo =
    "add_shipping_info"
```
Add Shipping Info event.

This event signifies that a user has submitted their shipping information. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCoupon` (String) (optional)
- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterShippingTier` (String) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventAddToCart

```c++
const char *const kEventAddToCart = "add_to_cart"
```
E-Commerce Add To Cart event.

This event signifies that an item(s) was added to a cart for purchase. Add this event to a funnel with `AnalyticsEventPurchase` to gauge the effectiveness of your checParameter(kout, If you supply the `AnalyticsParameterValue` parameter), you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventAddToWishlist

```c++
const char *const kEventAddToWishlist =
    "add_to_wishlist"
```
E-Commerce Add To Wishlist event.

This event signifies that an item was added to a wishlist. Use this event to identify popular gift items. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventAppOpen

```c++
const char *const kEventAppOpen = "app_open"
```
[App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Open event.

By logging this event when an [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) becomes active, developers can understand how often users leave and return during the course of a Session. Although Sessions are automatically reported, this event can provide further clarification around the continuous engagement of app-users.

### kEventBeginCheckout

```c++
const char *const kEventBeginCheckout =
    "begin_checkout"
```
E-Commerce Begin Checkout event.

This event signifies that a user has begun the process of checking out. Add this event to a funnel with your `AnalyticsEventPurchase` event to gauge the effectiveness of your checkout process. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCoupon` (String) (optional)
- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventCampaignDetails

```c++
const char *const kEventCampaignDetails =
    "campaign_details"
```
Campaign Detail event.

Log this event to supply the referral details of a re-engagement campaign. Note: you must supply at least one of the required parameters AnalyticsParameterSource, AnalyticsParameterMedium or AnalyticsParameterCampaign. Params:


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

<br />

### kEventEarnVirtualCurrency

```c++
const char *const kEventEarnVirtualCurrency = "earn_virtual_currency"
```
Earn Virtual Currency event.

This event tracks the awarding of virtual currency in your app. Log this along with `AnalyticsEventSpendVirtualCurrency` to better understand your virtual economy. Params:


- `AnalyticsParameterVirtualCurrencyName` (String)
- `AnalyticsParameterValue` (Int or Double)

<br />

### kEventGenerateLead

```c++
const char *const kEventGenerateLead =
    "generate_lead"
```
Generate Lead event.

Log this event when a lead has been generated in the app to understand the efficacy of your install and re-engagement campaigns. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventInAppPurchase

```c++
const char *const kEventInAppPurchase =
     "in_app_purchase"
```
In-App Purchase event.

This event signifies that extra content or a subscription was purchased by a user inside an app. Note: This is different from the ecommerce purchase event. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCurrency` (String)
- `AnalyticsParameterFreeTrial` (Int) (optional)
- `AnalyticsParameterPrice` (Double) (optional)
- `AnalyticsParameterPriceIsDiscounted` (Int) (optional)
- `AnalyticsParameterProductID` (String) (optional)
- `AnalyticsParameterProductName` (String) (optional)
- `AnalyticsParameterQuantity` (Int) (optional)
- `AnalyticsParameterSubscription` (Int) (optional)
- `AnalyticsParameterValue` (Double)

<br />

### kEventJoinGroup

```c++
const char *const kEventJoinGroup = "join_group"
```
Join Group event.

Log this event when a user joins a group such as a guild, team or family. Use this event to analyze how popular certain groups or social features are in your app. Params:


- `AnalyticsParameterGroupID` (String)

<br />

### kEventLevelEnd

```c++
const char *const kEventLevelEnd = "level_end"
```
Level End event.

Log this event when the user finishes a level. Params:


- `AnalyticsParameterLevelName` (String)
- `AnalyticsParameterSuccess` (String)

<br />

### kEventLevelStart

```c++
const char *const kEventLevelStart = "level_start"
```
Level Start event.

Log this event when the user starts a new level. Params:


- `AnalyticsParameterLevelName` (String)

<br />

### kEventLevelUp

```c++
const char *const kEventLevelUp = "level_up"
```
Level Up event.

This event signifies that a player has leveled up in your gaming app. It can help you gauge the level distribution of your userbase and help you identify certain levels that are difficult to pass. Params:


- `AnalyticsParameterLevel` (Int)
- `AnalyticsParameterCharacter` (String) (optional)

<br />

### kEventLogin

```c++
const char *const kEventLogin = "login"
```
Login event.

Apps with a login feature can report this event to signify that a user has logged in.

### kEventPostScore

```c++
const char *const kEventPostScore = "post_score"
```
Post Score event.

Log this event when the user posts a score in your gaming app. This event can help you understand how users are actually performing in your game and it can help you correlate high scores with certain audiences or behaviors. Params:


- `AnalyticsParameterScore` (Int)
- `AnalyticsParameterLevel` (Int) (optional)
- `AnalyticsParameterCharacter` (String) (optional)

<br />

### kEventPurchase

```c++
const char *const kEventPurchase = "purchase"
```
E-Commerce Purchase event.

This event signifies that an item(s) was purchased by a user. Note: This is different from the in-app purchase event, which is reported automatically for [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) Store-based apps. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


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

<br />

### kEventRefund

```c++
const char *const kEventRefund = "refund"
```
E-Commerce Refund event.

This event signifies that a refund was issued. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterAffiliation` (String) (optional)
- `AnalyticsParameterCoupon` (String) (optional)
- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterShipping` (Double) (optional)
- `AnalyticsParameterTax` (Double) (optional)
- `AnalyticsParameterTransactionID` (String) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventRemoveFromCart

```c++
const char *const kEventRemoveFromCart =
    "remove_from_cart"
```
E-Commerce Remove from Cart event.

This event signifies that an item(s) was removed from a cart. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventScreenView

```c++
const char *const kEventScreenView = "screen_view"
```
Screen View event.

This event signifies a screen view. Use this when a screen transition occurs. This event can be logged irrespective of whether automatic screen tracking is enabled. Params:


- `AnalyticsParameterScreenClass` (String) (optional)
- `AnalyticsParameterScreenName` (String) (optional)

<br />

### kEventSearch

```c++
const char *const kEventSearch = "search"
```
Search event.

Apps that support search features can use this event to contextualize search operations by supplying the appropriate, corresponding parameters. This event can help you identify the most popular content in your app. Params:


- `AnalyticsParameterSearchTerm` (String)
- `AnalyticsParameterStartDate` (String) (optional)
- `AnalyticsParameterEndDate` (String) (optional)
- `AnalyticsParameterNumberOfNights` (Int) (optional) for hotel bookings
- `AnalyticsParameterNumberOfRooms` (Int) (optional) for hotel bookings
- `AnalyticsParameterNumberOfPassengers` (Int) (optional) for travel bookings
- `AnalyticsParameterOrigin` (String) (optional)
- `AnalyticsParameterDestination` (String) (optional)
- `AnalyticsParameterTravelClass` (String) (optional) for travel bookings

<br />

### kEventSelectContent

```c++
const char *const kEventSelectContent =
    "select_content"
```
Select Content event.

This general purpose event signifies that a user has selected some content of a certain type in an app. The content can be any object in your app. This event can help you identify popular content and categories of content in your app. Params:


- `AnalyticsParameterContentType` (String)
- `AnalyticsParameterItemID` (String)

<br />

### kEventSelectItem

```c++
const char *const kEventSelectItem = "select_item"
```
Select Item event.

This event signifies that an item was selected by a user from a list. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items selected. Params:


- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterItemListID` (String) (optional)
- `AnalyticsParameterItemListName` (String) (optional)

<br />

### kEventSelectPromotion

```c++
const char *const kEventSelectPromotion =
    "select_promotion"
```
Select promotion event.

This event signifies that a user has selected a promotion offer. Use the appropriate parameters to contextualize the event, such as the item(s) for which the promotion applies. Params:


- `AnalyticsParameterCreativeName` (String) (optional)
- `AnalyticsParameterCreativeSlot` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterLocationID` (String) (optional)
- `AnalyticsParameterPromotionID` (String) (optional)
- `AnalyticsParameterPromotionName` (String) (optional)

<br />

### kEventShare

```c++
const char *const kEventShare = "share"
```
Share event.

Apps with social features can log the Share event to identify the most viral content. Params:


- `AnalyticsParameterContentType` (String)
- `AnalyticsParameterItemID` (String)

<br />

### kEventSignUp

```c++
const char *const kEventSignUp = "sign_up"
```
Sign Up event.

This event indicates that a user has signed up for an account in your app. The parameter signifies the method by which the user signed up. Use this event to understand the different behaviors between logged in and logged out users. Params:


- `AnalyticsParameterMethod` (String)

<br />

### kEventSpendVirtualCurrency

```c++
const char *const kEventSpendVirtualCurrency = "spend_virtual_currency"
```
Spend Virtual Currency event.

This event tracks the sale of virtual goods in your app and can help you identify which virtual goods are the most popular objects of purchase. Params:


- `AnalyticsParameterItemName` (String)
- `AnalyticsParameterVirtualCurrencyName` (String)
- `AnalyticsParameterValue` (Int or Double)

<br />

### kEventTutorialBegin

```c++
const char *const kEventTutorialBegin =
    "tutorial_begin"
```
Tutorial Begin event.

This event signifies the start of the on-boarding process in your app. Use this in a funnel with `AnalyticsEventTutorialComplete` to understand how many users complete this process and move on to the full app experience.

### kEventTutorialComplete

```c++
const char *const kEventTutorialComplete =
    "tutorial_complete"
```
Tutorial End event.

Use this event to signify the user's completion of your app's on-boarding process. Add this to a funnel with `AnalyticsEventTutorialBegin` to gauge the completion rate of your on-boarding process.

### kEventUnlockAchievement

```c++
const char *const kEventUnlockAchievement =
    "unlock_achievement"
```
Unlock Achievement event.

Log this event when the user has unlocked an achievement in your game. Since achievements generally represent the breadth of a gaming experience, this event can help you understand how many users are experiencing all that your game has to offer. Params:


- `AnalyticsParameterAchievementID` (String)

<br />

### kEventViewCart

```c++
const char *const kEventViewCart = "view_cart"
```
E-commerce View Cart event.

This event signifies that a user has viewed their cart. Use this to analyze your purchase funnel. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventViewItem

```c++
const char *const kEventViewItem = "view_item"
```
View Item event.

This event signifies that a user has viewed an item. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items viewed in your app. Note: If you supply the `AnalyticsParameterValue` parameter, you must also supply the `AnalyticsParameterCurrency` parameter so that revenue metrics can be computed accurately. Params:


- `AnalyticsParameterCurrency` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterValue` (Double) (optional)

<br />

### kEventViewItemList

```c++
const char *const kEventViewItemList =
    "view_item_list"
```
View Item List event.

Log this event when a user sees a list of items or offerings. Params:


- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterItemListID` (String) (optional)
- `AnalyticsParameterItemListName` (String) (optional)

<br />

### kEventViewPromotion

```c++
const char *const kEventViewPromotion =
    "view_promotion"
```
View Promotion event.

This event signifies that a promotion was shown to a user. Add this event to a funnel with the `AnalyticsEventAddToCart` and `AnalyticsEventPurchase` to gauge your conversion process. Params:


- `AnalyticsParameterCreativeName` (String) (optional)
- `AnalyticsParameterCreativeSlot` (String) (optional)
- `AnalyticsParameterItems` (\[\[String: Any\]\]) (optional)
- `AnalyticsParameterLocationID` (String) (optional)
- `AnalyticsParameterPromotionID` (String) (optional)
- `AnalyticsParameterPromotionName` (String) (optional)

<br />

### kEventViewSearchResults

```c++
const char *const kEventViewSearchResults =
    "view_search_results"
```
View Search Results event.

Log this event when the user has been presented with the results of a search. Params:


- `AnalyticsParameterSearchTerm` (String)

<br />