# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event.md.txt

# FirebaseAnalytics.Event

# FirebaseAnalytics.Event


```
class FirebaseAnalytics.Event
```

<br />

*** ** * ** ***

An Event is an important occurrence in your app that you want to measure. You can report up to 500 different types of Events per app and you can associate up to 25 unique parameters with each Event type. Some common events are suggested below, but you may also choose to specify custom Event types that are associated with your specific app. Each event type is identified by a unique name. Event names can be up to 40 characters long, may only contain [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-) characters and underscores ("_"), and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-) character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used.

The following event names are reserved and cannot be used:

- ad_activeview
- ad_click
- ad_exposure
- ad_query
- ad_reward
- adunit_exposure
- app_background
- app_clear_data
- app_exception
- app_remove
- app_store_refund
- app_store_subscription_cancel
- app_store_subscription_convert
- app_store_subscription_renew
- app_update
- app_upgrade
- dynamic_link_app_open
- dynamic_link_app_update
- dynamic_link_first_open
- error
- first_open
- first_visit
- in_app_purchase
- notification_dismiss
- notification_foreground
- notification_open
- notification_receive
- os_update
- session_start
- session_start_with_rollout
- user_engagement

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_PAYMENT_INFO() = "add_payment_info"` Add Payment Info event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_SHIPPING_INFO() = "add_shipping_info"` Add Shipping Info event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_CART() = "add_to_cart"` E-Commerce Add To Cart event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_WISHLIST() = "add_to_wishlist"` E-Commerce Add To Wishlist event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#AD_IMPRESSION() = "ad_impression"` Ad Impression event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#APP_OPEN() = "app_open"` App Open event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#BEGIN_CHECKOUT() = "begin_checkout"` E-Commerce Begin Checkout event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS() = "campaign_details"` Log this event to supply the referral details of a re-engagement campaign. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#EARN_VIRTUAL_CURRENCY() = "earn_virtual_currency"` Earn Virtual Currency event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#GENERATE_LEAD() = "generate_lead"` Generate Lead event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#JOIN_GROUP() = "join_group"` Join Group event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LEVEL_END() = "level_end"` Level End event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LEVEL_START() = "level_start"` Level Start event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LEVEL_UP() = "level_up"` Level Up event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LOGIN() = "login"` Login event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#POST_SCORE() = "post_score"` Post Score event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE() = "purchase"` E-Commerce Purchase event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#REFUND() = "refund"` E-Commerce Refund event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#REMOVE_FROM_CART() = "remove_from_cart"` E-Commerce Remove from Cart event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SCREEN_VIEW() = "screen_view"` Screen View event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SEARCH() = "search"` Search event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_CONTENT() = "select_content"` Select Content event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_ITEM() = "select_item"` Select Item event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_PROMOTION() = "select_promotion"` Select promotion event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SHARE() = "share"` Share event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SIGN_UP() = "sign_up"` Sign Up event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SPEND_VIRTUAL_CURRENCY() = "spend_virtual_currency"` Spend Virtual Currency event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_BEGIN() = "tutorial_begin"` Tutorial Begin event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_COMPLETE() = "tutorial_complete"` Tutorial End event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#UNLOCK_ACHIEVEMENT() = "unlock_achievement"` Unlock Achievement event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_CART() = "view_cart"` E-commerce View Cart event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_ITEM() = "view_item"` View Item event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_ITEM_LIST() = "view_item_list"` View Item List event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_PROMOTION() = "view_promotion"` View Promotion event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_SEARCH_RESULTS() = "view_search_results"` View Search Results event. |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#Event()()` |

## Constants

### ADD_PAYMENT_INFO

```
const val ADD_PAYMENT_INFO = "add_payment_info": String!
```

Add Payment Info event. This event signifies that a user has submitted their payment information. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PAYMENT_TYPE()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### ADD_SHIPPING_INFO

```
const val ADD_SHIPPING_INFO = "add_shipping_info": String!
```

Add Shipping Info event. This event signifies that a user has submitted their shipping information. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING_TIER()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### ADD_TO_CART

```
const val ADD_TO_CART = "add_to_cart": String!
```

E-Commerce Add To Cart event. This event signifies that an item(s) was added to a cart for purchase. Add this event to a funnel with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE()` to gauge the effectiveness of your checkout process. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### ADD_TO_WISHLIST

```
const val ADD_TO_WISHLIST = "add_to_wishlist": String!
```

E-Commerce Add To Wishlist event. This event signifies that an item was added to a wishlist. Use this event to identify popular gift items. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### AD_IMPRESSION

```
const val AD_IMPRESSION = "ad_impression": String!
```

Ad Impression event. This event signifies when a user sees an ad impression. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_PLATFORM()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_SOURCE()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_FORMAT()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_UNIT_NAME()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### APP_OPEN

```
const val APP_OPEN = "app_open": String!
```

App Open event. By logging this event when an App is moved to the foreground, developers can understand how often users leave and return during the course of a Session. Although Sessions are automatically reported, this event can provide further clarification around the continuous engagement of app-users.

### BEGIN_CHECKOUT

```
const val BEGIN_CHECKOUT = "begin_checkout": String!
```

E-Commerce Begin Checkout event. This event signifies that a user has begun the process of checking out. Add this event to a funnel with your `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE()` event to gauge the effectiveness of your checkout process. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### CAMPAIGN_DETAILS

```
const val CAMPAIGN_DETAILS = "campaign_details": String!
```

Log this event to supply the referral details of a re-engagement campaign. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE()`
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MEDIUM()`
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN()`
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TERM()` (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT()` (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACLID()` (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CP1()` (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN_ID()` (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE_PLATFORM()` (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_FORMAT()` (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MARKETING_TACTIC()` (optional)

### EARN_VIRTUAL_CURRENCY

```
const val EARN_VIRTUAL_CURRENCY = "earn_virtual_currency": String!
```

Earn Virtual Currency event. This event tracks the awarding of virtual currency in your app. Log this along with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SPEND_VIRTUAL_CURRENCY()` to better understand your virtual economy. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VIRTUAL_CURRENCY_NAME()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (long or double)

### GENERATE_LEAD

```
const val GENERATE_LEAD = "generate_lead": String!
```

Generate Lead event. Log this event when a lead has been generated in the app to understand the efficacy of your install and re-engagement campaigns. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### JOIN_GROUP

```
const val JOIN_GROUP = "join_group": String!
```

Join Group event. Log this event when a user joins a group such as a guild, team or family. Use this event to analyze how popular certain groups or social features are in your app. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#GROUP_ID()` (String)

### LEVEL_END

```
const val LEVEL_END = "level_end": String!
```

Level End event. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL_NAME()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SUCCESS()` (String) (optional)

### LEVEL_START

```
const val LEVEL_START = "level_start": String!
```

Level Start event. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL_NAME()` (String)

### LEVEL_UP

```
const val LEVEL_UP = "level_up": String!
```

Level Up event. This event signifies that a player has leveled up in your gaming app. It can help you gauge the level distribution of your userbase and help you identify certain levels that are difficult to pass. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL()` (long)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CHARACTER()` (String) (optional)

### LOGIN

```
const val LOGIN = "login": String!
```

Login event. Apps with a login feature can report this event to signify that a user has logged in. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD()` (String)

### POST_SCORE

```
const val POST_SCORE = "post_score": String!
```

Post Score event. Log this event when the user posts a score in your gaming app. This event can help you understand how users are actually performing in your game and it can help you correlate high scores with certain audiences or behaviors. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCORE()` (long)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL()` (long) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CHARACTER()` (String) (optional)

### PURCHASE

```
const val PURCHASE = "purchase": String!
```

E-Commerce Purchase event. This event signifies that an item(s) was purchased by a user. Note: This is different from the in-app purchase event, which is reported automatically for Google Play-based apps. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AFFILIATION()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#END_DATE()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING()` (double) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#START_DATE()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TAX()` (double) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRANSACTION_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### REFUND

```
const val REFUND = "refund": String!
```

E-Commerce Refund event. This event signifies that a refund was issued. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AFFILIATION()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING()` (double) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TAX()` (double) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRANSACTION_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### REMOVE_FROM_CART

```
const val REMOVE_FROM_CART = "remove_from_cart": String!
```

E-Commerce Remove from Cart event. This event signifies that an item(s) was removed from a cart. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the @`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### SCREEN_VIEW

```
const val SCREEN_VIEW = "screen_view": String!
```

Screen View event. This event signifies a screen view. Use this when a screen transition occurs. This event can be logged irrespective of whether automatic screen tracking is enabled. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_CLASS()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_NAME()` (String) (optional)

### SEARCH

```
const val SEARCH = "search": String!
```

Search event. Apps that support search features can use this event to contextualize search operations by supplying the appropriate, corresponding parameters. This event can help you identify the most popular content in your app. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SEARCH_TERM()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_NIGHTS()` (long) (optional) for hotel bookings
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_ROOMS()` (long) (optional) for hotel bookings
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_PASSENGERS()` (long) (optional) for travel bookings
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ORIGIN()` (String) (optional) for travel bookings
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#DESTINATION()` (String) (optional) for travel bookings
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#START_DATE()` (String) (optional) for travel bookings
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#END_DATE()` (String) (optional) for travel bookings
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRAVEL_CLASS()` (String) (optional) for travel bookings

### SELECT_CONTENT

```
const val SELECT_CONTENT = "select_content": String!
```

Select Content event. This general purpose event signifies that a user has selected some content of a certain type in an app. The content can be any object in your app. This event can help you identify popular content and categories of content in your app. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT_TYPE()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID()` (String)

### SELECT_ITEM

```
const val SELECT_ITEM = "select_item": String!
```

Select Item event. This event signifies that an item was selected by a user from a list. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items selected. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_NAME()` (String) (optional)

### SELECT_PROMOTION

```
const val SELECT_PROMOTION = "select_promotion": String!
```

Select promotion event. This event signifies that a user has selected a promotion offer. Use the appropriate parameters to contextualize the event, such as the item(s) for which the promotion applies. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_NAME()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_SLOT()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_NAME()` (String) (optional)

### SHARE

```
const val SHARE = "share": String!
```

Share event. Apps with social features can log the Share event to identify the most viral content. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT_TYPE()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD()` (String)

### SIGN_UP

```
const val SIGN_UP = "sign_up": String!
```

Sign Up event. This event indicates that a user has signed up for an account in your app. The parameter signifies the method by which the user signed up. Use this event to understand the different behaviors between logged in and logged out users. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD()` (String)

### SPEND_VIRTUAL_CURRENCY

```
const val SPEND_VIRTUAL_CURRENCY = "spend_virtual_currency": String!
```

Spend Virtual Currency event. This event tracks the sale of virtual goods in your app and can help you identify which virtual goods are the most popular objects of purchase. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_NAME()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VIRTUAL_CURRENCY_NAME()` (String)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (long or double)

### TUTORIAL_BEGIN

```
const val TUTORIAL_BEGIN = "tutorial_begin": String!
```

Tutorial Begin event. This event signifies the start of the on-boarding process in your app. Use this in a funnel with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_COMPLETE()` to understand how many users complete this process and move on to the full app experience.

### TUTORIAL_COMPLETE

```
const val TUTORIAL_COMPLETE = "tutorial_complete": String!
```

Tutorial End event. Use this event to signify the user's completion of your app's on-boarding process. Add this to a funnel with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_BEGIN()` to gauge the completion rate of your on-boarding process.

### UNLOCK_ACHIEVEMENT

```
const val UNLOCK_ACHIEVEMENT = "unlock_achievement": String!
```

Unlock Achievement event. Log this event when the user has unlocked an achievement in your game. Since achievements generally represent the breadth of a gaming experience, this event can help you understand how many users are experiencing all that your game has to offer. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACHIEVEMENT_ID()` (String)

### VIEW_CART

```
const val VIEW_CART = "view_cart": String!
```

E-commerce View Cart event. This event signifies that a user has viewed their cart. Use this to analyze your purchase funnel. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### VIEW_ITEM

```
const val VIEW_ITEM = "view_item": String!
```

View Item event. This event signifies that a user has viewed an item. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items viewed in your app. Note: If you supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` parameter, you must also supply the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter so that revenue metrics can be computed accurately. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()` (double) (optional)

### VIEW_ITEM_LIST

```
const val VIEW_ITEM_LIST = "view_item_list": String!
```

View Item List event. Log this event when a user sees a list of items or offerings. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_NAME()` (String) (optional)

### VIEW_PROMOTION

```
const val VIEW_PROMOTION = "view_promotion": String!
```

View Promotion event. This event signifies that a promotion was shown to a user. Add this event to a funnel with the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_CART()` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE()` to gauge your conversion process. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_NAME()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_SLOT()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()` (Parcelable\[\]) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_ID()` (String) (optional)
- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_NAME()` (String) (optional)

### VIEW_SEARCH_RESULTS

```
const val VIEW_SEARCH_RESULTS = "view_search_results": String!
```

View Search Results event. Log this event when the user has been presented with the results of a search. Params:

- `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SEARCH_TERM()` (String)

## Protected constructors

### Event

```
protected Event()
```