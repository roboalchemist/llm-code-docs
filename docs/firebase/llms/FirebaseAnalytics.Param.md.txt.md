# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param.md.txt

# FirebaseAnalytics.Param

# FirebaseAnalytics.Param


```
public class FirebaseAnalytics.Param
```

<br />

*** ** * ** ***

Params supply information that contextualize Events. You can associate up to 25 unique Params with each Event type. Some Params are suggested below for certain common Events, but you are not limited to these. You may supply extra Params for suggested Events or custom Params for Custom events. Param names can be up to 40 characters long, may only contain [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-) characters and underscores ("_"), and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-) character. Param values can be up to 100 characters long. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ACHIEVEMENT_ID() = "achievement_id"` Game achievement ID (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ACLID() = "aclid"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` click ID. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_FORMAT() = "ad_format"` The ad format (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_PLATFORM() = "ad_platform"` The ad platform (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_SOURCE() = "ad_source"` The ad source (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_UNIT_NAME() = "ad_unit_name"` The ad unit name (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#AFFILIATION() = "affiliation"` A product affiliation to designate a supplying company or brick and mortar store location (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN() = "campaign"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` name; used for keyword analysis to identify a specific product promotion or strategic campaign. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN_ID() = "campaign_id"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Campaign ID. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CHARACTER() = "character"` Character used in game (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT() = "content"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` content; used for A/B testing and content-targeted ads to differentiate ads or links that point to the same URL. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT_TYPE() = "content_type"` Type of content selected (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON() = "coupon"` Coupon code used for a purchase (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CP1() = "cp1"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` custom parameter. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_FORMAT() = "creative_format"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Creative format. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_NAME() = "creative_name"` The name of a creative used in a promotional spot (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_SLOT() = "creative_slot"` The name of a creative slot (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY() = "currency"` Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#DESTINATION() = "destination"` Flight or Travel destination (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#DISCOUNT() = "discount"` Monetary value of discount associated with a purchase(double). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#END_DATE() = "end_date"` The arrival date, check-out date, or rental end date for the item (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#EXTEND_SESSION() = "extend_session"` Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#FLIGHT_NUMBER() = "flight_number"` Flight number for travel events (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#GROUP_ID() = "group_id"` Group/clan/guild id (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#INDEX() = "index"` The index of the item in a list. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS() = "items"` The list of items involved in the transaction. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_BRAND() = "item_brand"` Item brand. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY() = "item_category"` Item category (context-specific) (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY2() = "item_category2"` Item category (context-specific) (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY3() = "item_category3"` Item category (context-specific) (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY4() = "item_category4"` Item category (context-specific) (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY5() = "item_category5"` Item category (context-specific) (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID() = "item_id"` Item ID (context-specific) (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_ID() = "item_list_id"` The ID of the list in which the item was presented to the user (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_NAME() = "item_list_name"` The name of the list in which the item was presented to the user (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_NAME() = "item_name"` Item Name (context-specific) (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_VARIANT() = "item_variant"` Item variant. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL() = "level"` Level in game (long). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL_NAME() = "level_name"` The name of a level in a game (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION() = "location"` Location (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION_ID() = "location_id"` The location associated with the event. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#MARKETING_TACTIC() = "marketing_tactic"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Marketing tactic. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#MEDIUM() = "medium"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` medium; used to identify a medium such as email or cost-per-click (cpc). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD() = "method"` A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_NIGHTS() = "number_of_nights"` Number of nights staying at hotel (long). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_PASSENGERS() = "number_of_passengers"` Number of passengers traveling (long). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_ROOMS() = "number_of_rooms"` Number of rooms for travel events (long). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#ORIGIN() = "origin"` Flight or Travel origin (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#PAYMENT_TYPE() = "payment_type"` The chosen method of payment (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#PRICE() = "price"` Purchase price (double). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_ID() = "promotion_id"` The ID of a product promotion (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_NAME() = "promotion_name"` The name of a product promotion (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#QUANTITY() = "quantity"` Purchase quantity (long). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SCORE() = "score"` Score in game (long). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_CLASS() = "screen_class"` Current screen class, such as the class name of the Activity, logged with screen_view event and added to every event. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_NAME() = "screen_name"` Current screen name, such as the name of the Activity, logged with screen_view event and added to every event. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SEARCH_TERM() = "search_term"` The search string/keywords used (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING() = "shipping"` Shipping cost associated with a transaction (double). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING_TIER() = "shipping_tier"` The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE() = "source"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` source; used to identify a search engine, newsletter, or other source. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE_PLATFORM() = "source_platform"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Source platform. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#START_DATE() = "start_date"` The departure date, check-in date, or rental start date for the item (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#SUCCESS() = "success"` The result of an operation (long). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#TAX() = "tax"` Tax cost associated with a transaction (double). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#TERM() = "term"` `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` term; used with paid search to supply the keywords for ads. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#TRANSACTION_ID() = "transaction_id"` The unique identifier of a transaction (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#TRAVEL_CLASS() = "travel_class"` Travel class (String). |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE() = "value"` A context-specific numeric value which is accumulated automatically for each event type. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#VIRTUAL_CURRENCY_NAME() = "virtual_currency_name"` Name of virtual currency type (String). |

| ### Protected constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#Param()()` |

## Constants

### ACHIEVEMENT_ID

```
public static final String ACHIEVEMENT_ID = "achievement_id"
```

Game achievement ID (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ACHIEVEMENT_ID, "10_matches_won");
```

### ACLID

```
public static final String ACLID = "aclid"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` click ID.

### AD_FORMAT

```
public static final String AD_FORMAT = "ad_format"
```

The ad format (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.AD_FORMAT, "Banner");
```

### AD_PLATFORM

```
public static final String AD_PLATFORM = "ad_platform"
```

The ad platform (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.AD_PLATFORM, "MoPub");
```

### AD_SOURCE

```
public static final String AD_SOURCE = "ad_source"
```

The ad source (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.AD_SOURCE, "AdColony");
```

### AD_UNIT_NAME

```
public static final String AD_UNIT_NAME = "ad_unit_name"
```

The ad unit name (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.AD_UNIT_NAME, "Banner_03");
```

### AFFILIATION

```
public static final String AFFILIATION = "affiliation"
```

A product affiliation to designate a supplying company or brick and mortar store location (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.AFFILIATION, "Google Store");
```

### CAMPAIGN

```
public static final String CAMPAIGN = "campaign"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` name; used for keyword analysis to identify a specific product promotion or strategic campaign.

### CAMPAIGN_ID

```
public static final String CAMPAIGN_ID = "campaign_id"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Campaign ID.

### CHARACTER

```
public static final String CHARACTER = "character"
```

Character used in game (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.CHARACTER, "beat_boss");
```

### CONTENT

```
public static final String CONTENT = "content"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` content; used for A/B testing and content-targeted ads to differentiate ads or links that point to the same URL.

### CONTENT_TYPE

```
public static final String CONTENT_TYPE = "content_type"
```

Type of content selected (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.CONTENT_TYPE, "news article");
```

### COUPON

```
public static final String COUPON = "coupon"
```

Coupon code used for a purchase (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.COUPON, "SUMMER_FUN");
```

### CP1

```
public static final String CP1 = "cp1"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` custom parameter.

### CREATIVE_FORMAT

```
public static final String CREATIVE_FORMAT = "creative_format"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Creative format.

### CREATIVE_NAME

```
public static final String CREATIVE_NAME = "creative_name"
```

The name of a creative used in a promotional spot (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.CREATIVE_NAME, "Summer Sale");
```

### CREATIVE_SLOT

```
public static final String CREATIVE_SLOT = "creative_slot"
```

The name of a creative slot (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.CREATIVE_SLOT, "summer_banner2");
```

### CURRENCY

```
public static final String CURRENCY = "currency"
```

Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.CURRENCY, "USD");
```

### DESTINATION

```
public static final String DESTINATION = "destination"
```

Flight or Travel destination (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.DESTINATION, "Mountain View, CA");
```

### DISCOUNT

```
public static final String DISCOUNT = "discount"
```

Monetary value of discount associated with a purchase(double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```
    Bundle params = new Bundle();
    params.putDouble(Param.DISCOUNT, 2.0);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $2.00 USD
```

### END_DATE

```
public static final String END_DATE = "end_date"
```

The arrival date, check-out date, or rental end date for the item (String). The parameter expects a date formatted as YYYY-MM-DD and set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.END_DATE, "2015-09-14");
```

### EXTEND_SESSION

```
public static final String EXTEND_SESSION = "extend_session"
```

Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged. Specify 1 to extend the current session or to start a new session; any other long value will not extend or start a session.

```
    Bundle params = new Bundle();
    params.putLong(Param.EXTEND_SESSION, 1);
```

### FLIGHT_NUMBER

```
public static final String FLIGHT_NUMBER = "flight_number"
```

Flight number for travel events (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.FLIGHT_NUMBER, "ZZ800");
```

### GROUP_ID

```
public static final String GROUP_ID = "group_id"
```

Group/clan/guild id (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.GROUP_ID, "g1");
```

### INDEX

```
public static final String INDEX = "index"
```

The index of the item in a list. The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.INDEX, 5);
```

### ITEMS

```
public static final String ITEMS = "items"
```

The list of items involved in the transaction. (Parcelable\[\]). The parameter expects a Parcelable Array set with putParcelableArray:

```
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
public static final String ITEM_BRAND = "item_brand"
```

Item brand. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_BRAND, "Google");
```

### ITEM_CATEGORY

```
public static final String ITEM_CATEGORY = "item_category"
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY, "pants");
```

### ITEM_CATEGORY2

```
public static final String ITEM_CATEGORY2 = "item_category2"
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY2, "pants");
```

### ITEM_CATEGORY3

```
public static final String ITEM_CATEGORY3 = "item_category3"
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY3, "pants");
```

### ITEM_CATEGORY4

```
public static final String ITEM_CATEGORY4 = "item_category4"
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY4, "pants");
```

### ITEM_CATEGORY5

```
public static final String ITEM_CATEGORY5 = "item_category5"
```

Item category (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY5, "pants");
```

### ITEM_ID

```
public static final String ITEM_ID = "item_id"
```

Item ID (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_ID, "SKU_12345");
```

### ITEM_LIST_ID

```
public static final String ITEM_LIST_ID = "item_list_id"
```

The ID of the list in which the item was presented to the user (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_LIST_ID, "ABC123");
```

### ITEM_LIST_NAME

```
public static final String ITEM_LIST_NAME = "item_list_name"
```

The name of the list in which the item was presented to the user (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_LIST_NAME, "Related products");
```

### ITEM_NAME

```
public static final String ITEM_NAME = "item_name"
```

Item Name (context-specific) (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_NAME, "jeggings");
```

### ITEM_VARIANT

```
public static final String ITEM_VARIANT = "item_variant"
```

Item variant. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ITEM_VARIANT, "Black");
```

### LEVEL

```
public static final String LEVEL = "level"
```

Level in game (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.LEVEL, 42);
```

### LEVEL_NAME

```
public static final String LEVEL_NAME = "level_name"
```

The name of a level in a game (String). The parameter expects a String value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.LEVEL_NAME, "room_1");
```

### LOCATION

```
public static final String LOCATION = "location"
```

Location (String). The Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated event. Alternatively, you can supply your own custom Location ID. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.LOCATION, "Mountain View, CA");
```

### LOCATION_ID

```
public static final String LOCATION_ID = "location_id"
```

The location associated with the event. Preferred to be the Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated item but could be overridden to a custom location ID string. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.LOCATION_ID, "ChIJiyj437sx3YAR9kUWC8QkLzQ");
```

### MARKETING_TACTIC

```
public static final String MARKETING_TACTIC = "marketing_tactic"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Marketing tactic.

### MEDIUM

```
public static final String MEDIUM = "medium"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` medium; used to identify a medium such as email or cost-per-click (cpc).

### METHOD

```
public static final String METHOD = "method"
```

A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.METHOD, "google");
```

### NUMBER_OF_NIGHTS

```
public static final String NUMBER_OF_NIGHTS = "number_of_nights"
```

Number of nights staying at hotel (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_NIGHTS, 3);
```

### NUMBER_OF_PASSENGERS

```
public static final String NUMBER_OF_PASSENGERS = "number_of_passengers"
```

Number of passengers traveling (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_PASSENGERS, 11);
```

### NUMBER_OF_ROOMS

```
public static final String NUMBER_OF_ROOMS = "number_of_rooms"
```

Number of rooms for travel events (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_ROOMS, 2);
```

### ORIGIN

```
public static final String ORIGIN = "origin"
```

Flight or Travel origin (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.ORIGIN, "Mountain View, CA");
```

### PAYMENT_TYPE

```
public static final String PAYMENT_TYPE = "payment_type"
```

The chosen method of payment (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.PAYMENT_TYPE, "Visa");
```

### PRICE

```
public static final String PRICE = "price"
```

Purchase price (double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```
    Bundle params = new Bundle();
    params.putDouble(Param.PRICE, 1.0);
    params.putString(Param.CURRENCY, "USD"); // e.g. $1.00 USD
```

### PROMOTION_ID

```
public static final String PROMOTION_ID = "promotion_id"
```

The ID of a product promotion (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.PROMOTION_ID, "ABC123");
```

### PROMOTION_NAME

```
public static final String PROMOTION_NAME = "promotion_name"
```

The name of a product promotion (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.PROMOTION_NAME, "Summer Sale");
```

### QUANTITY

```
public static final String QUANTITY = "quantity"
```

Purchase quantity (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.QUANTITY, 1);
```

### SCORE

```
public static final String SCORE = "score"
```

Score in game (long). The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.SCORE, 4200);
```

### SCREEN_CLASS

```
public static final String SCREEN_CLASS = "screen_class"
```

Current screen class, such as the class name of the Activity, logged with screen_view event and added to every event. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.SCREEN_CLASS, "MainActivity");
```

### SCREEN_NAME

```
public static final String SCREEN_NAME = "screen_name"
```

Current screen name, such as the name of the Activity, logged with screen_view event and added to every event. The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.SCREEN_NAME, "Splash Screen");
```

### SEARCH_TERM

```
public static final String SEARCH_TERM = "search_term"
```

The search string/keywords used (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.SEARCH_TERM, "periodic table");
```

### SHIPPING

```
public static final String SHIPPING = "shipping"
```

Shipping cost associated with a transaction (double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```
    Bundle params = new Bundle();
    params.putDouble(Param.SHIPPING, 5.99);
    params.putString(Param.CURRENCY, "USD"); // e.g. $5.99 USD
```

### SHIPPING_TIER

```
public static final String SHIPPING_TIER = "shipping_tier"
```

The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.SHIPPING_TIER, "Ground");
```

### SOURCE

```
public static final String SOURCE = "source"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` source; used to identify a search engine, newsletter, or other source.

### SOURCE_PLATFORM

```
public static final String SOURCE_PLATFORM = "source_platform"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` Source platform.

### START_DATE

```
public static final String START_DATE = "start_date"
```

The departure date, check-in date, or rental start date for the item (String). The parameter expects a date formatted as YYYY-MM-DD and set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.START_DATE, "2015-09-14");
```

### SUCCESS

```
public static final String SUCCESS = "success"
```

The result of an operation (long). Specify 1 to indicate success and 0 to indicate failure. The parameter expects a long value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)`:

```
    Bundle params = new Bundle();
    params.putLong(Param.SUCCESS, 1);
```

### TAX

```
public static final String TAX = "tax"
```

Tax cost associated with a transaction (double). Expecting a double value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`:

```
    Bundle params = new Bundle();
    params.putDouble(Param.TAX, 2.43);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $2.43 USD
```

### TERM

```
public static final String TERM = "term"
```

`https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()` term; used with paid search to supply the keywords for ads.

### TRANSACTION_ID

```
public static final String TRANSACTION_ID = "transaction_id"
```

The unique identifier of a transaction (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.TRANSACTION_ID, "T12345");
```

### TRAVEL_CLASS

```
public static final String TRAVEL_CLASS = "travel_class"
```

Travel class (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.TRAVEL_CLASS, "business");
```

### VALUE

```
public static final String VALUE = "value"
```

A context-specific numeric value which is accumulated automatically for each event type. Value should be specified with `https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)` or `https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)`. This is a general purpose parameter that is useful for accumulating a key metric that pertains to an event. Examples include revenue, distance, time, and points. Notes: Values for pre-defined currency-related events (such as `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_CART()`) should be accompanied by a `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` param. The valid range of accumulated values is \[-9,223,372,036,854.77, 9,223,372,036,854.77\]. Supplying a non-numeric value, omitting the corresponding `https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()` parameter, or supplying an invalid [currency code](https://goo.gl/qqX3J2) for conversion events will cause that conversion to be omitted from reporting.

```
    Bundle params = new Bundle();
    params.putDouble(Param.VALUE, 3.99);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $3.99 USD
```

### VIRTUAL_CURRENCY_NAME

```
public static final String VIRTUAL_CURRENCY_NAME = "virtual_currency_name"
```

Name of virtual currency type (String). The parameter expects a string value set with `https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)`:

```
    Bundle params = new Bundle();
    params.putString(Param.VIRTUAL_CURRENCY_NAME, "gems");
```

## Protected constructors

### Param

```
protected Param()
```