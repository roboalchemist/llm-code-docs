# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event.md.txt

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

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ADD_PAYMENT_INFO](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_PAYMENT_INFO())` = "add_payment_info"` Add Payment Info event.                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ADD_SHIPPING_INFO](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_SHIPPING_INFO())` = "add_shipping_info"` Add Shipping Info event.                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ADD_TO_CART](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_CART())` = "add_to_cart"` E-Commerce Add To Cart event.                                                             |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ADD_TO_WISHLIST](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_WISHLIST())` = "add_to_wishlist"` E-Commerce Add To Wishlist event.                                             |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [AD_IMPRESSION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#AD_IMPRESSION())` = "ad_impression"` Ad Impression event.                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [APP_OPEN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#APP_OPEN())` = "app_open"` App Open event.                                                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [BEGIN_CHECKOUT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#BEGIN_CHECKOUT())` = "begin_checkout"` E-Commerce Begin Checkout event.                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS())` = "campaign_details"` Log this event to supply the referral details of a re-engagement campaign. |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [EARN_VIRTUAL_CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#EARN_VIRTUAL_CURRENCY())` = "earn_virtual_currency"` Earn Virtual Currency event.                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [GENERATE_LEAD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#GENERATE_LEAD())` = "generate_lead"` Generate Lead event.                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [JOIN_GROUP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#JOIN_GROUP())` = "join_group"` Join Group event.                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LEVEL_END](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LEVEL_END())` = "level_end"` Level End event.                                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LEVEL_START](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LEVEL_START())` = "level_start"` Level Start event.                                                                        |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LEVEL_UP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LEVEL_UP())` = "level_up"` Level Up event.                                                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LOGIN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#LOGIN())` = "login"` Login event.                                                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [POST_SCORE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#POST_SCORE())` = "post_score"` Post Score event.                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PURCHASE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE())` = "purchase"` E-Commerce Purchase event.                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [REFUND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#REFUND())` = "refund"` E-Commerce Refund event.                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [REMOVE_FROM_CART](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#REMOVE_FROM_CART())` = "remove_from_cart"` E-Commerce Remove from Cart event.                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SCREEN_VIEW](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SCREEN_VIEW())` = "screen_view"` Screen View event.                                                                        |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SEARCH](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SEARCH())` = "search"` Search event.                                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SELECT_CONTENT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_CONTENT())` = "select_content"` Select Content event.                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SELECT_ITEM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_ITEM())` = "select_item"` Select Item event.                                                                        |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SELECT_PROMOTION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SELECT_PROMOTION())` = "select_promotion"` Select promotion event.                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SHARE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SHARE())` = "share"` Share event.                                                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SIGN_UP](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SIGN_UP())` = "sign_up"` Sign Up event.                                                                                        |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SPEND_VIRTUAL_CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SPEND_VIRTUAL_CURRENCY())` = "spend_virtual_currency"` Spend Virtual Currency event.                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [TUTORIAL_BEGIN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_BEGIN())` = "tutorial_begin"` Tutorial Begin event.                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [TUTORIAL_COMPLETE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_COMPLETE())` = "tutorial_complete"` Tutorial End event.                                                     |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [UNLOCK_ACHIEVEMENT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#UNLOCK_ACHIEVEMENT())` = "unlock_achievement"` Unlock Achievement event.                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [VIEW_CART](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_CART())` = "view_cart"` E-commerce View Cart event.                                                                     |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [VIEW_ITEM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_ITEM())` = "view_item"` View Item event.                                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [VIEW_ITEM_LIST](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_ITEM_LIST())` = "view_item_list"` View Item List event.                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [VIEW_PROMOTION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_PROMOTION())` = "view_promotion"` View Promotion event.                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [VIEW_SEARCH_RESULTS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#VIEW_SEARCH_RESULTS())` = "view_search_results"` View Search Results event.                                        |

|                                                  ### Protected constructors                                                  |
|------------------------------------------------------------------------------------------------------------------------------|
| [Event](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#Event())`()` |

## Constants

### ADD_PAYMENT_INFO

```
constÂ valÂ ADD_PAYMENT_INFO = "add_payment_info":Â String!
```

Add Payment Info event. This event signifies that a user has submitted their payment information. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [COUPON](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()) (String) (optional)
- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [PAYMENT_TYPE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PAYMENT_TYPE()) (String) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### ADD_SHIPPING_INFO

```
constÂ valÂ ADD_SHIPPING_INFO = "add_shipping_info":Â String!
```

Add Shipping Info event. This event signifies that a user has submitted their shipping information. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [COUPON](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()) (String) (optional)
- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [SHIPPING_TIER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING_TIER()) (String) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### ADD_TO_CART

```
constÂ valÂ ADD_TO_CART = "add_to_cart":Â String!
```

E-Commerce Add To Cart event. This event signifies that an item(s) was added to a cart for purchase. Add this event to a funnel with [PURCHASE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE()) to gauge the effectiveness of your checkout process. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### ADD_TO_WISHLIST

```
constÂ valÂ ADD_TO_WISHLIST = "add_to_wishlist":Â String!
```

E-Commerce Add To Wishlist event. This event signifies that an item was added to a wishlist. Use this event to identify popular gift items. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### AD_IMPRESSION

```
constÂ valÂ AD_IMPRESSION = "ad_impression":Â String!
```

Ad Impression event. This event signifies when a user sees an ad impression. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [AD_PLATFORM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_PLATFORM()) (String) (optional)
- [AD_SOURCE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_SOURCE()) (String) (optional)
- [AD_FORMAT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_FORMAT()) (String) (optional)
- [AD_UNIT_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_UNIT_NAME()) (String) (optional)
- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### APP_OPEN

```
constÂ valÂ APP_OPEN = "app_open":Â String!
```

App Open event. By logging this event when an App is moved to the foreground, developers can understand how often users leave and return during the course of a Session. Although Sessions are automatically reported, this event can provide further clarification around the continuous engagement of app-users.  

### BEGIN_CHECKOUT

```
constÂ valÂ BEGIN_CHECKOUT = "begin_checkout":Â String!
```

E-Commerce Begin Checkout event. This event signifies that a user has begun the process of checking out. Add this event to a funnel with your [PURCHASE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE()) event to gauge the effectiveness of your checkout process. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [COUPON](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()) (String) (optional)
- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### CAMPAIGN_DETAILS

```
constÂ valÂ CAMPAIGN_DETAILS = "campaign_details":Â String!
```

Log this event to supply the referral details of a re-engagement campaign. Params:

- [SOURCE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE())
- [MEDIUM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MEDIUM())
- [CAMPAIGN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN())
- [TERM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TERM()) (optional)
- [CONTENT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT()) (optional)
- [ACLID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACLID()) (optional)
- [CP1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CP1()) (optional)
- [CAMPAIGN_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN_ID()) (optional)
- [SOURCE_PLATFORM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE_PLATFORM()) (optional)
- [CREATIVE_FORMAT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_FORMAT()) (optional)
- [MARKETING_TACTIC](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MARKETING_TACTIC()) (optional)  

### EARN_VIRTUAL_CURRENCY

```
constÂ valÂ EARN_VIRTUAL_CURRENCY = "earn_virtual_currency":Â String!
```

Earn Virtual Currency event. This event tracks the awarding of virtual currency in your app. Log this along with [SPEND_VIRTUAL_CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#SPEND_VIRTUAL_CURRENCY()) to better understand your virtual economy. Params:

- [VIRTUAL_CURRENCY_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VIRTUAL_CURRENCY_NAME()) (String)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (long or double)  

### GENERATE_LEAD

```
constÂ valÂ GENERATE_LEAD = "generate_lead":Â String!
```

Generate Lead event. Log this event when a lead has been generated in the app to understand the efficacy of your install and re-engagement campaigns. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### JOIN_GROUP

```
constÂ valÂ JOIN_GROUP = "join_group":Â String!
```

Join Group event. Log this event when a user joins a group such as a guild, team or family. Use this event to analyze how popular certain groups or social features are in your app. Params:

- [GROUP_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#GROUP_ID()) (String)  

### LEVEL_END

```
constÂ valÂ LEVEL_END = "level_end":Â String!
```

Level End event. Params:

- [LEVEL_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL_NAME()) (String)
- [SUCCESS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SUCCESS()) (String) (optional)  

### LEVEL_START

```
constÂ valÂ LEVEL_START = "level_start":Â String!
```

Level Start event. Params:

- [LEVEL_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL_NAME()) (String)  

### LEVEL_UP

```
constÂ valÂ LEVEL_UP = "level_up":Â String!
```

Level Up event. This event signifies that a player has leveled up in your gaming app. It can help you gauge the level distribution of your userbase and help you identify certain levels that are difficult to pass. Params:

- [LEVEL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL()) (long)
- [CHARACTER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CHARACTER()) (String) (optional)  

### LOGIN

```
constÂ valÂ LOGIN = "login":Â String!
```

Login event. Apps with a login feature can report this event to signify that a user has logged in. Params:

- [METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD()) (String)  

### POST_SCORE

```
constÂ valÂ POST_SCORE = "post_score":Â String!
```

Post Score event. Log this event when the user posts a score in your gaming app. This event can help you understand how users are actually performing in your game and it can help you correlate high scores with certain audiences or behaviors. Params:

- [SCORE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCORE()) (long)
- [LEVEL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL()) (long) (optional)
- [CHARACTER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CHARACTER()) (String) (optional)  

### PURCHASE

```
constÂ valÂ PURCHASE = "purchase":Â String!
```

E-Commerce Purchase event. This event signifies that an item(s) was purchased by a user. Note: This is different from the in-app purchase event, which is reported automatically for Google Play-based apps. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [AFFILIATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AFFILIATION()) (String) (optional)
- [COUPON](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()) (String) (optional)
- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [END_DATE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#END_DATE()) (String) (optional)
- [ITEM_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [SHIPPING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING()) (double) (optional)
- [START_DATE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#START_DATE()) (String) (optional)
- [TAX](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TAX()) (double) (optional)
- [TRANSACTION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRANSACTION_ID()) (String) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### REFUND

```
constÂ valÂ REFUND = "refund":Â String!
```

E-Commerce Refund event. This event signifies that a refund was issued. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [AFFILIATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AFFILIATION()) (String) (optional)
- [COUPON](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON()) (String) (optional)
- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [SHIPPING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING()) (double) (optional)
- [TAX](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TAX()) (double) (optional)
- [TRANSACTION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRANSACTION_ID()) (String) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### REMOVE_FROM_CART

```
constÂ valÂ REMOVE_FROM_CART = "remove_from_cart":Â String!
```

E-Commerce Remove from Cart event. This event signifies that an item(s) was removed from a cart. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the @[CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### SCREEN_VIEW

```
constÂ valÂ SCREEN_VIEW = "screen_view":Â String!
```

Screen View event. This event signifies a screen view. Use this when a screen transition occurs. This event can be logged irrespective of whether automatic screen tracking is enabled. Params:

- [SCREEN_CLASS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_CLASS()) (String) (optional)
- [SCREEN_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_NAME()) (String) (optional)  

### SEARCH

```
constÂ valÂ SEARCH = "search":Â String!
```

Search event. Apps that support search features can use this event to contextualize search operations by supplying the appropriate, corresponding parameters. This event can help you identify the most popular content in your app. Params:

- [SEARCH_TERM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SEARCH_TERM()) (String)
- [NUMBER_OF_NIGHTS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_NIGHTS()) (long) (optional) for hotel bookings
- [NUMBER_OF_ROOMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_ROOMS()) (long) (optional) for hotel bookings
- [NUMBER_OF_PASSENGERS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_PASSENGERS()) (long) (optional) for travel bookings
- [ORIGIN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ORIGIN()) (String) (optional) for travel bookings
- [DESTINATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#DESTINATION()) (String) (optional) for travel bookings
- [START_DATE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#START_DATE()) (String) (optional) for travel bookings
- [END_DATE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#END_DATE()) (String) (optional) for travel bookings
- [TRAVEL_CLASS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRAVEL_CLASS()) (String) (optional) for travel bookings  

### SELECT_CONTENT

```
constÂ valÂ SELECT_CONTENT = "select_content":Â String!
```

Select Content event. This general purpose event signifies that a user has selected some content of a certain type in an app. The content can be any object in your app. This event can help you identify popular content and categories of content in your app. Params:

- [CONTENT_TYPE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT_TYPE()) (String)
- [ITEM_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID()) (String)  

### SELECT_ITEM

```
constÂ valÂ SELECT_ITEM = "select_item":Â String!
```

Select Item event. This event signifies that an item was selected by a user from a list. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items selected. Params:

- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [ITEM_LIST_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_ID()) (String) (optional)
- [ITEM_LIST_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_NAME()) (String) (optional)  

### SELECT_PROMOTION

```
constÂ valÂ SELECT_PROMOTION = "select_promotion":Â String!
```

Select promotion event. This event signifies that a user has selected a promotion offer. Use the appropriate parameters to contextualize the event, such as the item(s) for which the promotion applies. Params:

- [CREATIVE_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_NAME()) (String) (optional)
- [CREATIVE_SLOT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_SLOT()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [LOCATION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION_ID()) (String) (optional)
- [PROMOTION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_ID()) (String) (optional)
- [PROMOTION_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_NAME()) (String) (optional)  

### SHARE

```
constÂ valÂ SHARE = "share":Â String!
```

Share event. Apps with social features can log the Share event to identify the most viral content. Params:

- [CONTENT_TYPE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT_TYPE()) (String)
- [ITEM_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID()) (String)
- [METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD()) (String)  

### SIGN_UP

```
constÂ valÂ SIGN_UP = "sign_up":Â String!
```

Sign Up event. This event indicates that a user has signed up for an account in your app. The parameter signifies the method by which the user signed up. Use this event to understand the different behaviors between logged in and logged out users. Params:

- [METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD()) (String)  

### SPEND_VIRTUAL_CURRENCY

```
constÂ valÂ SPEND_VIRTUAL_CURRENCY = "spend_virtual_currency":Â String!
```

Spend Virtual Currency event. This event tracks the sale of virtual goods in your app and can help you identify which virtual goods are the most popular objects of purchase. Params:

- [ITEM_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_NAME()) (String)
- [VIRTUAL_CURRENCY_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VIRTUAL_CURRENCY_NAME()) (String)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (long or double)  

### TUTORIAL_BEGIN

```
constÂ valÂ TUTORIAL_BEGIN = "tutorial_begin":Â String!
```

Tutorial Begin event. This event signifies the start of the on-boarding process in your app. Use this in a funnel with [TUTORIAL_COMPLETE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_COMPLETE()) to understand how many users complete this process and move on to the full app experience.  

### TUTORIAL_COMPLETE

```
constÂ valÂ TUTORIAL_COMPLETE = "tutorial_complete":Â String!
```

Tutorial End event. Use this event to signify the user's completion of your app's on-boarding process. Add this to a funnel with [TUTORIAL_BEGIN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#TUTORIAL_BEGIN()) to gauge the completion rate of your on-boarding process.  

### UNLOCK_ACHIEVEMENT

```
constÂ valÂ UNLOCK_ACHIEVEMENT = "unlock_achievement":Â String!
```

Unlock Achievement event. Log this event when the user has unlocked an achievement in your game. Since achievements generally represent the breadth of a gaming experience, this event can help you understand how many users are experiencing all that your game has to offer. Params:

- [ACHIEVEMENT_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACHIEVEMENT_ID()) (String)  

### VIEW_CART

```
constÂ valÂ VIEW_CART = "view_cart":Â String!
```

E-commerce View Cart event. This event signifies that a user has viewed their cart. Use this to analyze your purchase funnel. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### VIEW_ITEM

```
constÂ valÂ VIEW_ITEM = "view_item":Â String!
```

View Item event. This event signifies that a user has viewed an item. Use the appropriate parameters to contextualize the event. Use this event to discover the most popular items viewed in your app. Note: If you supply the [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) parameter, you must also supply the [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter so that revenue metrics can be computed accurately. Params:

- [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE()) (double) (optional)  

### VIEW_ITEM_LIST

```
constÂ valÂ VIEW_ITEM_LIST = "view_item_list":Â String!
```

View Item List event. Log this event when a user sees a list of items or offerings. Params:

- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [ITEM_LIST_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_ID()) (String) (optional)
- [ITEM_LIST_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_NAME()) (String) (optional)  

### VIEW_PROMOTION

```
constÂ valÂ VIEW_PROMOTION = "view_promotion":Â String!
```

View Promotion event. This event signifies that a promotion was shown to a user. Add this event to a funnel with the [ADD_TO_CART](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_CART()) and [PURCHASE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#PURCHASE()) to gauge your conversion process. Params:

- [CREATIVE_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_NAME()) (String) (optional)
- [CREATIVE_SLOT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_SLOT()) (String) (optional)
- [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS()) (Parcelable\[\]) (optional)
- [LOCATION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION_ID()) (String) (optional)
- [PROMOTION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_ID()) (String) (optional)
- [PROMOTION_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_NAME()) (String) (optional)  

### VIEW_SEARCH_RESULTS

```
constÂ valÂ VIEW_SEARCH_RESULTS = "view_search_results":Â String!
```

View Search Results event. Log this event when the user has been presented with the results of a search. Params:

- [SEARCH_TERM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SEARCH_TERM()) (String)  

## Protected constructors

### Event

```
protectedÂ Event()
```