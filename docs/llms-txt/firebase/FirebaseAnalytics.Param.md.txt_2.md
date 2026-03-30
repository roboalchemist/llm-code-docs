# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param.md.txt

# FirebaseAnalytics.Param

# FirebaseAnalytics.Param


```
class FirebaseAnalytics.Param
```

<br />

*** ** * ** ***

Params supply information that contextualize Events. You can associate up to 25 unique Params with each Event type. Some Params are suggested below for certain common Events, but you are not limited to these. You may supply extra Params for suggested Events or custom Params for Custom events. Param names can be up to 40 characters long, may only contain [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-) characters and underscores ("_"), and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-) character. Param values can be up to 100 characters long. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACHIEVEMENT_ID() = "achievement_id"` Game achievement ID (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACLID() = "aclid"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` click ID. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_FORMAT() = "ad_format"` The ad format (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_PLATFORM() = "ad_platform"` The ad platform (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_SOURCE() = "ad_source"` The ad source (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_UNIT_NAME() = "ad_unit_name"` The ad unit name (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AFFILIATION() = "affiliation"` A product affiliation to designate a supplying company or brick and mortar store location (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN() = "campaign"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` name; used for keyword analysis to identify a specific product promotion or strategic campaign. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN_ID() = "campaign_id"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Campaign ID. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CHARACTER() = "character"` Character used in game (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT() = "content"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` content; used for A/B testing and content-targeted ads to differentiate ads or links that point to the same URL. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT_TYPE() = "content_type"` Type of content selected (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON() = "coupon"` Coupon code used for a purchase (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CP1() = "cp1"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` custom parameter. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_FORMAT() = "creative_format"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Creative format. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_NAME() = "creative_name"` The name of a creative used in a promotional spot (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_SLOT() = "creative_slot"` The name of a creative slot (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY() = "currency"` Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#DESTINATION() = "destination"` Flight or Travel destination (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#DISCOUNT() = "discount"` Monetary value of discount associated with a purchase(double). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#END_DATE() = "end_date"` The arrival date, check-out date, or rental end date for the item (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#EXTEND_SESSION() = "extend_session"` Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#FLIGHT_NUMBER() = "flight_number"` Flight number for travel events (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#GROUP_ID() = "group_id"` Group/clan/guild id (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#INDEX() = "index"` The index of the item in a list. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS() = "items"` The list of items involved in the transaction. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_BRAND() = "item_brand"` Item brand. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY() = "item_category"` Item category (context-specific) (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY2() = "item_category2"` Item category (context-specific) (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY3() = "item_category3"` Item category (context-specific) (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY4() = "item_category4"` Item category (context-specific) (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY5() = "item_category5"` Item category (context-specific) (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID() = "item_id"` Item ID (context-specific) (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_ID() = "item_list_id"` The ID of the list in which the item was presented to the user (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_NAME() = "item_list_name"` The name of the list in which the item was presented to the user (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_NAME() = "item_name"` Item Name (context-specific) (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_VARIANT() = "item_variant"` Item variant. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL() = "level"` Level in game (long). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL_NAME() = "level_name"` The name of a level in a game (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION() = "location"` Location (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION_ID() = "location_id"` The location associated with the event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MARKETING_TACTIC() = "marketing_tactic"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Marketing tactic. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MEDIUM() = "medium"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` medium; used to identify a medium such as email or cost-per-click (cpc). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD() = "method"` A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_NIGHTS() = "number_of_nights"` Number of nights staying at hotel (long). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_PASSENGERS() = "number_of_passengers"` Number of passengers traveling (long). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_ROOMS() = "number_of_rooms"` Number of rooms for travel events (long). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ORIGIN() = "origin"` Flight or Travel origin (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PAYMENT_TYPE() = "payment_type"` The chosen method of payment (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PRICE() = "price"` Purchase price (double). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_ID() = "promotion_id"` The ID of a product promotion (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_NAME() = "promotion_name"` The name of a product promotion (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#QUANTITY() = "quantity"` Purchase quantity (long). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCORE() = "score"` Score in game (long). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_CLASS() = "screen_class"` Current screen class, such as the class name of the Activity, logged with screen_view event and added to every event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_NAME() = "screen_name"` Current screen name, such as the name of the Activity, logged with screen_view event and added to every event. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SEARCH_TERM() = "search_term"` The search string/keywords used (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING() = "shipping"` Shipping cost associated with a transaction (double). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING_TIER() = "shipping_tier"` The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE() = "source"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` source; used to identify a search engine, newsletter, or other source. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE_PLATFORM() = "source_platform"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Source platform. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#START_DATE() = "start_date"` The departure date, check-in date, or rental start date for the item (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SUCCESS() = "success"` The result of an operation (long). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TAX() = "tax"` Tax cost associated with a transaction (double). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TERM() = "term"` `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` term; used with paid search to supply the keywords for ads. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRANSACTION_ID() = "transaction_id"` The unique identifier of a transaction (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRAVEL_CLASS() = "travel_class"` Travel class (String). |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE() = "value"` A context-specific numeric value which is accumulated automatically for each event type. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VIRTUAL_CURRENCY_NAME() = "virtual_currency_name"` Name of virtual currency type (String). |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#Param()()` |

## Constants

### ACHIEVEMENT_ID

```
const val ACHIEVEMENT_ID = "achievement_id": String!
```

Game achievement ID (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ACHIEVEMENT_ID, "10_matches_won");
```

### ACLID

```
const val ACLID = "aclid": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` click ID.

### AD_FORMAT

```
const val AD_FORMAT = "ad_format": String!
```

The ad format (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_FORMAT, "Banner");
```

### AD_PLATFORM

```
const val AD_PLATFORM = "ad_platform": String!
```

The ad platform (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_PLATFORM, "MoPub");
```

### AD_SOURCE

```
const val AD_SOURCE = "ad_source": String!
```

The ad source (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_SOURCE, "AdColony");
```

### AD_UNIT_NAME

```
const val AD_UNIT_NAME = "ad_unit_name": String!
```

The ad unit name (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_UNIT_NAME, "Banner_03");
```

### AFFILIATION

```
const val AFFILIATION = "affiliation": String!
```

A product affiliation to designate a supplying company or brick and mortar store location (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AFFILIATION, "Google Store");
```

### CAMPAIGN

```
const val CAMPAIGN = "campaign": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` name; used for keyword analysis to identify a specific product promotion or strategic campaign.

### CAMPAIGN_ID

```
const val CAMPAIGN_ID = "campaign_id": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Campaign ID.

### CHARACTER

```
const val CHARACTER = "character": String!
```

Character used in game (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CHARACTER, "beat_boss");
```

### CONTENT

```
const val CONTENT = "content": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` content; used for A/B testing and content-targeted ads to differentiate ads or links that point to the same URL.

### CONTENT_TYPE

```
const val CONTENT_TYPE = "content_type": String!
```

Type of content selected (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CONTENT_TYPE, "news article");
```

### COUPON

```
const val COUPON = "coupon": String!
```

Coupon code used for a purchase (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.COUPON, "SUMMER_FUN");
```

### CP1

```
const val CP1 = "cp1": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` custom parameter.

### CREATIVE_FORMAT

```
const val CREATIVE_FORMAT = "creative_format": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Creative format.

### CREATIVE_NAME

```
const val CREATIVE_NAME = "creative_name": String!
```

The name of a creative used in a promotional spot (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CREATIVE_NAME, "Summer Sale");
```

### CREATIVE_SLOT

```
const val CREATIVE_SLOT = "creative_slot": String!
```

The name of a creative slot (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CREATIVE_SLOT, "summer_banner2");
```

### CURRENCY

```
const val CURRENCY = "currency": String!
```

Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CURRENCY, "USD");
```

### DESTINATION

```
const val DESTINATION = "destination": String!
```

Flight or Travel destination (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.DESTINATION, "Mountain View, CA");
```

### DISCOUNT

```
const val DISCOUNT = "discount": String!
```

Monetary value of discount associated with a purchase(double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.DISCOUNT, 2.0);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $2.00 USD
```

### END_DATE

```
const val END_DATE = "end_date": String!
```

The arrival date, check-out date, or rental end date for the item (String). The parameter expects a date formatted as YYYY-MM-DD and set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.END_DATE, "2015-09-14");
```

### EXTEND_SESSION

```
const val EXTEND_SESSION = "extend_session": String!
```

Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged. Specify 1 to extend the current session or to start a new session; any other long value will not extend or start a session.

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.EXTEND_SESSION, 1);
```

### FLIGHT_NUMBER

```
const val FLIGHT_NUMBER = "flight_number": String!
```

Flight number for travel events (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.FLIGHT_NUMBER, "ZZ800");
```

### GROUP_ID

```
const val GROUP_ID = "group_id": String!
```

Group/clan/guild id (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.GROUP_ID, "g1");
```

### INDEX

```
const val INDEX = "index": String!
```

The index of the item in a list. The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.INDEX, 5);
```

### ITEMS

```
const val ITEMS = "items": String!
```

The list of items involved in the transaction. (Parcelable\[\]). The parameter expects a Parcelable Array set with putParcelableArray:

```kotlin
    Bundle item1 = new Bundle();
    item1.putString(Param.ITEM_NAME, "jeggings");
    item1.putString(Param.ITEM_CATEGORY, "pants");
    Bundle item2 = new Bundle();
    item2.putString(Param.ITEM_NAME, "boots");
    item2.putString(Param.ITEM_CATEGORY, "shoes");
    Bundle params = new Bundle();
    params.putParcelableArray(Param.ITEMS, new Bundle[] {item1, item2});
```

### ITEM_BRAND

```
const val ITEM_BRAND = "item_brand": String!
```

Item brand. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_BRAND, "Google");
```

### ITEM_CATEGORY

```
const val ITEM_CATEGORY = "item_category": String!
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY, "pants");
```

### ITEM_CATEGORY2

```
const val ITEM_CATEGORY2 = "item_category2": String!
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY2, "pants");
```

### ITEM_CATEGORY3

```
const val ITEM_CATEGORY3 = "item_category3": String!
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY3, "pants");
```

### ITEM_CATEGORY4

```
const val ITEM_CATEGORY4 = "item_category4": String!
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY4, "pants");
```

### ITEM_CATEGORY5

```
const val ITEM_CATEGORY5 = "item_category5": String!
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY5, "pants");
```

### ITEM_ID

```
const val ITEM_ID = "item_id": String!
```

Item ID (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_ID, "SKU_12345");
```

### ITEM_LIST_ID

```
const val ITEM_LIST_ID = "item_list_id": String!
```

The ID of the list in which the item was presented to the user (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_LIST_ID, "ABC123");
```

### ITEM_LIST_NAME

```
const val ITEM_LIST_NAME = "item_list_name": String!
```

The name of the list in which the item was presented to the user (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_LIST_NAME, "Related products");
```

### ITEM_NAME

```
const val ITEM_NAME = "item_name": String!
```

Item Name (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_NAME, "jeggings");
```

### ITEM_VARIANT

```
const val ITEM_VARIANT = "item_variant": String!
```

Item variant. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_VARIANT, "Black");
```

### LEVEL

```
const val LEVEL = "level": String!
```

Level in game (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.LEVEL, 42);
```

### LEVEL_NAME

```
const val LEVEL_NAME = "level_name": String!
```

The name of a level in a game (String). The parameter expects a String value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.LEVEL_NAME, "room_1");
```

### LOCATION

```
const val LOCATION = "location": String!
```

Location (String). The Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated event. Alternatively, you can supply your own custom Location ID. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.LOCATION, "Mountain View, CA");
```

### LOCATION_ID

```
const val LOCATION_ID = "location_id": String!
```

The location associated with the event. Preferred to be the Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated item but could be overridden to a custom location ID string. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.LOCATION_ID, "ChIJiyj437sx3YAR9kUWC8QkLzQ");
```

### MARKETING_TACTIC

```
const val MARKETING_TACTIC = "marketing_tactic": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Marketing tactic.

### MEDIUM

```
const val MEDIUM = "medium": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` medium; used to identify a medium such as email or cost-per-click (cpc).

### METHOD

```
const val METHOD = "method": String!
```

A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.METHOD, "google");
```

### NUMBER_OF_NIGHTS

```
const val NUMBER_OF_NIGHTS = "number_of_nights": String!
```

Number of nights staying at hotel (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_NIGHTS, 3);
```

### NUMBER_OF_PASSENGERS

```
const val NUMBER_OF_PASSENGERS = "number_of_passengers": String!
```

Number of passengers traveling (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_PASSENGERS, 11);
```

### NUMBER_OF_ROOMS

```
const val NUMBER_OF_ROOMS = "number_of_rooms": String!
```

Number of rooms for travel events (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_ROOMS, 2);
```

### ORIGIN

```
const val ORIGIN = "origin": String!
```

Flight or Travel origin (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ORIGIN, "Mountain View, CA");
```

### PAYMENT_TYPE

```
const val PAYMENT_TYPE = "payment_type": String!
```

The chosen method of payment (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.PAYMENT_TYPE, "Visa");
```

### PRICE

```
const val PRICE = "price": String!
```

Purchase price (double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.PRICE, 1.0);
    params.putString(Param.CURRENCY, "USD"); // e.g. $1.00 USD
```

### PROMOTION_ID

```
const val PROMOTION_ID = "promotion_id": String!
```

The ID of a product promotion (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.PROMOTION_ID, "ABC123");
```

### PROMOTION_NAME

```
const val PROMOTION_NAME = "promotion_name": String!
```

The name of a product promotion (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.PROMOTION_NAME, "Summer Sale");
```

### QUANTITY

```
const val QUANTITY = "quantity": String!
```

Purchase quantity (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.QUANTITY, 1);
```

### SCORE

```
const val SCORE = "score": String!
```

Score in game (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.SCORE, 4200);
```

### SCREEN_CLASS

```
const val SCREEN_CLASS = "screen_class": String!
```

Current screen class, such as the class name of the Activity, logged with screen_view event and added to every event. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SCREEN_CLASS, "MainActivity");
```

### SCREEN_NAME

```
const val SCREEN_NAME = "screen_name": String!
```

Current screen name, such as the name of the Activity, logged with screen_view event and added to every event. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SCREEN_NAME, "Splash Screen");
```

### SEARCH_TERM

```
const val SEARCH_TERM = "search_term": String!
```

The search string/keywords used (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SEARCH_TERM, "periodic table");
```

### SHIPPING

```
const val SHIPPING = "shipping": String!
```

Shipping cost associated with a transaction (double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.SHIPPING, 5.99);
    params.putString(Param.CURRENCY, "USD"); // e.g. $5.99 USD
```

### SHIPPING_TIER

```
const val SHIPPING_TIER = "shipping_tier": String!
```

The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SHIPPING_TIER, "Ground");
```

### SOURCE

```
const val SOURCE = "source": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` source; used to identify a search engine, newsletter, or other source.

### SOURCE_PLATFORM

```
const val SOURCE_PLATFORM = "source_platform": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Source platform.

### START_DATE

```
const val START_DATE = "start_date": String!
```

The departure date, check-in date, or rental start date for the item (String). The parameter expects a date formatted as YYYY-MM-DD and set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.START_DATE, "2015-09-14");
```

### SUCCESS

```
const val SUCCESS = "success": String!
```

The result of an operation (long). Specify 1 to indicate success and 0 to indicate failure. The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.SUCCESS, 1);
```

### TAX

```
const val TAX = "tax": String!
```

Tax cost associated with a transaction (double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.TAX, 2.43);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $2.43 USD
```

### TERM

```
const val TERM = "term": String!
```

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` term; used with paid search to supply the keywords for ads.

### TRANSACTION_ID

```
const val TRANSACTION_ID = "transaction_id": String!
```

The unique identifier of a transaction (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.TRANSACTION_ID, "T12345");
```

### TRAVEL_CLASS

```
const val TRAVEL_CLASS = "travel_class": String!
```

Travel class (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.TRAVEL_CLASS, "business");
```

### VALUE

```
const val VALUE = "value": String!
```

A context-specific numeric value which is accumulated automatically for each event type. Value should be specified with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)` or `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`. This is a general purpose parameter that is useful for accumulating a key metric that pertains to an event. Examples include revenue, distance, time, and points. Notes: Values for pre-defined currency-related events (such as `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_CART()`) should be accompanied by a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` param. The valid range of accumulated values is \[-9,223,372,036,854.77, 9,223,372,036,854.77\]. Supplying a non-numeric value, omitting the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter, or supplying an invalid [currency code](https://goo.gl/qqX3J2) for conversion events will cause that conversion to be omitted from reporting.

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.VALUE, 3.99);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $3.99 USD
```

### VIRTUAL_CURRENCY_NAME

```
const val VIRTUAL_CURRENCY_NAME = "virtual_currency_name": String!
```

Name of virtual currency type (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.VIRTUAL_CURRENCY_NAME, "gems");
```

## Protected constructors

### Param

```
protected Param()
```