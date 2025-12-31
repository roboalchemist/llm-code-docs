# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param.md.txt

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

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ACHIEVEMENT_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACHIEVEMENT_ID())` = "achievement_id"` Game achievement ID (String).                                                                                                                                                                                                              |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ACLID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ACLID())` = "aclid"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) click ID.                                                                                                              |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [AD_FORMAT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_FORMAT())` = "ad_format"` The ad format (String).                                                                                                                                                                                                                                   |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [AD_PLATFORM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_PLATFORM())` = "ad_platform"` The ad platform (String).                                                                                                                                                                                                                           |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [AD_SOURCE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_SOURCE())` = "ad_source"` The ad source (String).                                                                                                                                                                                                                                   |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [AD_UNIT_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AD_UNIT_NAME())` = "ad_unit_name"` The ad unit name (String).                                                                                                                                                                                                                       |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [AFFILIATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#AFFILIATION())` = "affiliation"` A product affiliation to designate a supplying company or brick and mortar store location (String).                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CAMPAIGN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN())` = "campaign"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) name; used for keyword analysis to identify a specific product promotion or strategic campaign.               |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CAMPAIGN_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CAMPAIGN_ID())` = "campaign_id"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Campaign ID.                                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CHARACTER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CHARACTER())` = "character"` Character used in game (String).                                                                                                                                                                                                                          |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CONTENT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT())` = "content"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) content; used for A/B testing and content-targeted ads to differentiate ads or links that point to the same URL. |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CONTENT_TYPE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CONTENT_TYPE())` = "content_type"` Type of content selected (String).                                                                                                                                                                                                               |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [COUPON](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#COUPON())` = "coupon"` Coupon code used for a purchase (String).                                                                                                                                                                                                                          |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CP1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CP1())` = "cp1"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) custom parameter.                                                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CREATIVE_FORMAT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_FORMAT())` = "creative_format"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Creative format.                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CREATIVE_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_NAME())` = "creative_name"` The name of a creative used in a promotional spot (String).                                                                                                                                                                                   |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CREATIVE_SLOT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CREATIVE_SLOT())` = "creative_slot"` The name of a creative slot (String).                                                                                                                                                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY())` = "currency"` Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String).                                                                                                     |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [DESTINATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#DESTINATION())` = "destination"` Flight or Travel destination (String).                                                                                                                                                                                                              |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [DISCOUNT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#DISCOUNT())` = "discount"` Monetary value of discount associated with a purchase(double).                                                                                                                                                                                               |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [END_DATE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#END_DATE())` = "end_date"` The arrival date, check-out date, or rental end date for the item (String).                                                                                                                                                                                  |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [EXTEND_SESSION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#EXTEND_SESSION())` = "extend_session"` Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged.                                                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [FLIGHT_NUMBER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#FLIGHT_NUMBER())` = "flight_number"` Flight number for travel events (String).                                                                                                                                                                                                     |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [GROUP_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#GROUP_ID())` = "group_id"` Group/clan/guild id (String).                                                                                                                                                                                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [INDEX](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#INDEX())` = "index"` The index of the item in a list.                                                                                                                                                                                                                                      |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEMS())` = "items"` The list of items involved in the transaction.                                                                                                                                                                                                                        |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_BRAND](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_BRAND())` = "item_brand"` Item brand.                                                                                                                                                                                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_CATEGORY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY())` = "item_category"` Item category (context-specific) (String).                                                                                                                                                                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_CATEGORY2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY2())` = "item_category2"` Item category (context-specific) (String).                                                                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_CATEGORY3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY3())` = "item_category3"` Item category (context-specific) (String).                                                                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_CATEGORY4](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY4())` = "item_category4"` Item category (context-specific) (String).                                                                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_CATEGORY5](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_CATEGORY5())` = "item_category5"` Item category (context-specific) (String).                                                                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_ID())` = "item_id"` Item ID (context-specific) (String).                                                                                                                                                                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_LIST_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_ID())` = "item_list_id"` The ID of the list in which the item was presented to the user (String).                                                                                                                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_LIST_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_LIST_NAME())` = "item_list_name"` The name of the list in which the item was presented to the user (String).                                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_NAME())` = "item_name"` Item Name (context-specific) (String).                                                                                                                                                                                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ITEM_VARIANT](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ITEM_VARIANT())` = "item_variant"` Item variant.                                                                                                                                                                                                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LEVEL](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL())` = "level"` Level in game (long).                                                                                                                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LEVEL_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LEVEL_NAME())` = "level_name"` The name of a level in a game (String).                                                                                                                                                                                                                |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LOCATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION())` = "location"` Location (String).                                                                                                                                                                                                                                           |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [LOCATION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#LOCATION_ID())` = "location_id"` The location associated with the event.                                                                                                                                                                                                             |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [MARKETING_TACTIC](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MARKETING_TACTIC())` = "marketing_tactic"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Marketing tactic.                                                                     |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [MEDIUM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#MEDIUM())` = "medium"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) medium; used to identify a medium such as email or cost-per-click (cpc).                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#METHOD())` = "method"` A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event.                                                                                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [NUMBER_OF_NIGHTS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_NIGHTS())` = "number_of_nights"` Number of nights staying at hotel (long).                                                                                                                                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [NUMBER_OF_PASSENGERS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_PASSENGERS())` = "number_of_passengers"` Number of passengers traveling (long).                                                                                                                                                                                   |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [NUMBER_OF_ROOMS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#NUMBER_OF_ROOMS())` = "number_of_rooms"` Number of rooms for travel events (long).                                                                                                                                                                                               |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [ORIGIN](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#ORIGIN())` = "origin"` Flight or Travel origin (String).                                                                                                                                                                                                                                  |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PAYMENT_TYPE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PAYMENT_TYPE())` = "payment_type"` The chosen method of payment (String).                                                                                                                                                                                                           |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PRICE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PRICE())` = "price"` Purchase price (double).                                                                                                                                                                                                                                              |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PROMOTION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_ID())` = "promotion_id"` The ID of a product promotion (String).                                                                                                                                                                                                          |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PROMOTION_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#PROMOTION_NAME())` = "promotion_name"` The name of a product promotion (String).                                                                                                                                                                                                  |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [QUANTITY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#QUANTITY())` = "quantity"` Purchase quantity (long).                                                                                                                                                                                                                                    |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SCORE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCORE())` = "score"` Score in game (long).                                                                                                                                                                                                                                                 |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SCREEN_CLASS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_CLASS())` = "screen_class"` Current screen class, such as the class name of the Activity, logged with screen_view event and added to every event.                                                                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SCREEN_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SCREEN_NAME())` = "screen_name"` Current screen name, such as the name of the Activity, logged with screen_view event and added to every event.                                                                                                                                      |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SEARCH_TERM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SEARCH_TERM())` = "search_term"` The search string/keywords used (String).                                                                                                                                                                                                           |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SHIPPING](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING())` = "shipping"` Shipping cost associated with a transaction (double).                                                                                                                                                                                                        |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SHIPPING_TIER](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SHIPPING_TIER())` = "shipping_tier"` The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item (String).                                                                                                                                          |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SOURCE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE())` = "source"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) source; used to identify a search engine, newsletter, or other source.                                              |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SOURCE_PLATFORM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SOURCE_PLATFORM())` = "source_platform"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Source platform.                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [START_DATE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#START_DATE())` = "start_date"` The departure date, check-in date, or rental start date for the item (String).                                                                                                                                                                         |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [SUCCESS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#SUCCESS())` = "success"` The result of an operation (long).                                                                                                                                                                                                                              |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [TAX](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TAX())` = "tax"` Tax cost associated with a transaction (double).                                                                                                                                                                                                                            |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [TERM](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TERM())` = "term"` [CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) term; used with paid search to supply the keywords for ads.                                                               |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [TRANSACTION_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRANSACTION_ID())` = "transaction_id"` The unique identifier of a transaction (String).                                                                                                                                                                                           |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [TRAVEL_CLASS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#TRAVEL_CLASS())` = "travel_class"` Travel class (String).                                                                                                                                                                                                                           |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [VALUE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VALUE())` = "value"` A context-specific numeric value which is accumulated automatically for each event type.                                                                                                                                                                              |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [VIRTUAL_CURRENCY_NAME](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#VIRTUAL_CURRENCY_NAME())` = "virtual_currency_name"` Name of virtual currency type (String).                                                                                                                                                                               |

|                                                  ### Protected constructors                                                  |
|------------------------------------------------------------------------------------------------------------------------------|
| [Param](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#Param())`()` |

## Constants

### ACHIEVEMENT_ID

```
constÂ valÂ ACHIEVEMENT_ID = "achievement_id":Â String!
```

Game achievement ID (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ACHIEVEMENT_ID, "10_matches_won");
```  

### ACLID

```
constÂ valÂ ACLID = "aclid":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) click ID.  

### AD_FORMAT

```
constÂ valÂ AD_FORMAT = "ad_format":Â String!
```

The ad format (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_FORMAT, "Banner");
```  

### AD_PLATFORM

```
constÂ valÂ AD_PLATFORM = "ad_platform":Â String!
```

The ad platform (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_PLATFORM, "MoPub");
```  

### AD_SOURCE

```
constÂ valÂ AD_SOURCE = "ad_source":Â String!
```

The ad source (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_SOURCE, "AdColony");
```  

### AD_UNIT_NAME

```
constÂ valÂ AD_UNIT_NAME = "ad_unit_name":Â String!
```

The ad unit name (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AD_UNIT_NAME, "Banner_03");
```  

### AFFILIATION

```
constÂ valÂ AFFILIATION = "affiliation":Â String!
```

A product affiliation to designate a supplying company or brick and mortar store location (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.AFFILIATION, "Google Store");
```  

### CAMPAIGN

```
constÂ valÂ CAMPAIGN = "campaign":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) name; used for keyword analysis to identify a specific product promotion or strategic campaign.  

### CAMPAIGN_ID

```
constÂ valÂ CAMPAIGN_ID = "campaign_id":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Campaign ID.  

### CHARACTER

```
constÂ valÂ CHARACTER = "character":Â String!
```

Character used in game (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CHARACTER, "beat_boss");
```  

### CONTENT

```
constÂ valÂ CONTENT = "content":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) content; used for A/B testing and content-targeted ads to differentiate ads or links that point to the same URL.  

### CONTENT_TYPE

```
constÂ valÂ CONTENT_TYPE = "content_type":Â String!
```

Type of content selected (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CONTENT_TYPE, "news article");
```  

### COUPON

```
constÂ valÂ COUPON = "coupon":Â String!
```

Coupon code used for a purchase (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.COUPON, "SUMMER_FUN");
```  

### CP1

```
constÂ valÂ CP1 = "cp1":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) custom parameter.  

### CREATIVE_FORMAT

```
constÂ valÂ CREATIVE_FORMAT = "creative_format":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Creative format.  

### CREATIVE_NAME

```
constÂ valÂ CREATIVE_NAME = "creative_name":Â String!
```

The name of a creative used in a promotional spot (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CREATIVE_NAME, "Summer Sale");
```  

### CREATIVE_SLOT

```
constÂ valÂ CREATIVE_SLOT = "creative_slot":Â String!
```

The name of a creative slot (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CREATIVE_SLOT, "summer_banner2");
```  

### CURRENCY

```
constÂ valÂ CURRENCY = "currency":Â String!
```

Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.CURRENCY, "USD");
```  

### DESTINATION

```
constÂ valÂ DESTINATION = "destination":Â String!
```

Flight or Travel destination (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.DESTINATION, "Mountain View, CA");
```  

### DISCOUNT

```
constÂ valÂ DISCOUNT = "discount":Â String!
```

Monetary value of discount associated with a purchase(double). Expecting a double value set with [putDouble](https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)):  

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.DISCOUNT, 2.0);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $2.00 USD
```  

### END_DATE

```
constÂ valÂ END_DATE = "end_date":Â String!
```

The arrival date, check-out date, or rental end date for the item (String). The parameter expects a date formatted as YYYY-MM-DD and set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.END_DATE, "2015-09-14");
```  

### EXTEND_SESSION

```
constÂ valÂ EXTEND_SESSION = "extend_session":Â String!
```

Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged. Specify 1 to extend the current session or to start a new session; any other long value will not extend or start a session.  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.EXTEND_SESSION, 1);
```  

### FLIGHT_NUMBER

```
constÂ valÂ FLIGHT_NUMBER = "flight_number":Â String!
```

Flight number for travel events (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.FLIGHT_NUMBER, "ZZ800");
```  

### GROUP_ID

```
constÂ valÂ GROUP_ID = "group_id":Â String!
```

Group/clan/guild id (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.GROUP_ID, "g1");
```  

### INDEX

```
constÂ valÂ INDEX = "index":Â String!
```

The index of the item in a list. The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.INDEX, 5);
```  

### ITEMS

```
constÂ valÂ ITEMS = "items":Â String!
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
constÂ valÂ ITEM_BRAND = "item_brand":Â String!
```

Item brand. The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_BRAND, "Google");
```  

### ITEM_CATEGORY

```
constÂ valÂ ITEM_CATEGORY = "item_category":Â String!
```

Item category (context-specific) (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY, "pants");
```  

### ITEM_CATEGORY2

```
constÂ valÂ ITEM_CATEGORY2 = "item_category2":Â String!
```

Item category (context-specific) (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY2, "pants");
```  

### ITEM_CATEGORY3

```
constÂ valÂ ITEM_CATEGORY3 = "item_category3":Â String!
```

Item category (context-specific) (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY3, "pants");
```  

### ITEM_CATEGORY4

```
constÂ valÂ ITEM_CATEGORY4 = "item_category4":Â String!
```

Item category (context-specific) (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY4, "pants");
```  

### ITEM_CATEGORY5

```
constÂ valÂ ITEM_CATEGORY5 = "item_category5":Â String!
```

Item category (context-specific) (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_CATEGORY5, "pants");
```  

### ITEM_ID

```
constÂ valÂ ITEM_ID = "item_id":Â String!
```

Item ID (context-specific) (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_ID, "SKU_12345");
```  

### ITEM_LIST_ID

```
constÂ valÂ ITEM_LIST_ID = "item_list_id":Â String!
```

The ID of the list in which the item was presented to the user (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_LIST_ID, "ABC123");
```  

### ITEM_LIST_NAME

```
constÂ valÂ ITEM_LIST_NAME = "item_list_name":Â String!
```

The name of the list in which the item was presented to the user (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_LIST_NAME, "Related products");
```  

### ITEM_NAME

```
constÂ valÂ ITEM_NAME = "item_name":Â String!
```

Item Name (context-specific) (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_NAME, "jeggings");
```  

### ITEM_VARIANT

```
constÂ valÂ ITEM_VARIANT = "item_variant":Â String!
```

Item variant. The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ITEM_VARIANT, "Black");
```  

### LEVEL

```
constÂ valÂ LEVEL = "level":Â String!
```

Level in game (long). The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.LEVEL, 42);
```  

### LEVEL_NAME

```
constÂ valÂ LEVEL_NAME = "level_name":Â String!
```

The name of a level in a game (String). The parameter expects a String value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.LEVEL_NAME, "room_1");
```  

### LOCATION

```
constÂ valÂ LOCATION = "location":Â String!
```

Location (String). The Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated event. Alternatively, you can supply your own custom Location ID. The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.LOCATION, "Mountain View, CA");
```  

### LOCATION_ID

```
constÂ valÂ LOCATION_ID = "location_id":Â String!
```

The location associated with the event. Preferred to be the Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated item but could be overridden to a custom location ID string. The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.LOCATION_ID, "ChIJiyj437sx3YAR9kUWC8QkLzQ");
```  

### MARKETING_TACTIC

```
constÂ valÂ MARKETING_TACTIC = "marketing_tactic":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Marketing tactic.  

### MEDIUM

```
constÂ valÂ MEDIUM = "medium":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) medium; used to identify a medium such as email or cost-per-click (cpc).  

### METHOD

```
constÂ valÂ METHOD = "method":Â String!
```

A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event. The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.METHOD, "google");
```  

### NUMBER_OF_NIGHTS

```
constÂ valÂ NUMBER_OF_NIGHTS = "number_of_nights":Â String!
```

Number of nights staying at hotel (long). The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_NIGHTS, 3);
```  

### NUMBER_OF_PASSENGERS

```
constÂ valÂ NUMBER_OF_PASSENGERS = "number_of_passengers":Â String!
```

Number of passengers traveling (long). The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_PASSENGERS, 11);
```  

### NUMBER_OF_ROOMS

```
constÂ valÂ NUMBER_OF_ROOMS = "number_of_rooms":Â String!
```

Number of rooms for travel events (long). The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.NUMBER_OF_ROOMS, 2);
```  

### ORIGIN

```
constÂ valÂ ORIGIN = "origin":Â String!
```

Flight or Travel origin (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.ORIGIN, "Mountain View, CA");
```  

### PAYMENT_TYPE

```
constÂ valÂ PAYMENT_TYPE = "payment_type":Â String!
```

The chosen method of payment (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.PAYMENT_TYPE, "Visa");
```  

### PRICE

```
constÂ valÂ PRICE = "price":Â String!
```

Purchase price (double). Expecting a double value set with [putDouble](https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)):  

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.PRICE, 1.0);
    params.putString(Param.CURRENCY, "USD"); // e.g. $1.00 USD
```  

### PROMOTION_ID

```
constÂ valÂ PROMOTION_ID = "promotion_id":Â String!
```

The ID of a product promotion (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.PROMOTION_ID, "ABC123");
```  

### PROMOTION_NAME

```
constÂ valÂ PROMOTION_NAME = "promotion_name":Â String!
```

The name of a product promotion (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.PROMOTION_NAME, "Summer Sale");
```  

### QUANTITY

```
constÂ valÂ QUANTITY = "quantity":Â String!
```

Purchase quantity (long). The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.QUANTITY, 1);
```  

### SCORE

```
constÂ valÂ SCORE = "score":Â String!
```

Score in game (long). The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.SCORE, 4200);
```  

### SCREEN_CLASS

```
constÂ valÂ SCREEN_CLASS = "screen_class":Â String!
```

Current screen class, such as the class name of the Activity, logged with screen_view event and added to every event. The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SCREEN_CLASS, "MainActivity");
```  

### SCREEN_NAME

```
constÂ valÂ SCREEN_NAME = "screen_name":Â String!
```

Current screen name, such as the name of the Activity, logged with screen_view event and added to every event. The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SCREEN_NAME, "Splash Screen");
```  

### SEARCH_TERM

```
constÂ valÂ SEARCH_TERM = "search_term":Â String!
```

The search string/keywords used (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SEARCH_TERM, "periodic table");
```  

### SHIPPING

```
constÂ valÂ SHIPPING = "shipping":Â String!
```

Shipping cost associated with a transaction (double). Expecting a double value set with [putDouble](https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)):  

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.SHIPPING, 5.99);
    params.putString(Param.CURRENCY, "USD"); // e.g. $5.99 USD
```  

### SHIPPING_TIER

```
constÂ valÂ SHIPPING_TIER = "shipping_tier":Â String!
```

The shipping tier (e.g. Ground, Air, Next-day) selected for delivery of the purchased item (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.SHIPPING_TIER, "Ground");
```  

### SOURCE

```
constÂ valÂ SOURCE = "source":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) source; used to identify a search engine, newsletter, or other source.  

### SOURCE_PLATFORM

```
constÂ valÂ SOURCE_PLATFORM = "source_platform":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) Source platform.  

### START_DATE

```
constÂ valÂ START_DATE = "start_date":Â String!
```

The departure date, check-in date, or rental start date for the item (String). The parameter expects a date formatted as YYYY-MM-DD and set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.START_DATE, "2015-09-14");
```  

### SUCCESS

```
constÂ valÂ SUCCESS = "success":Â String!
```

The result of an operation (long). Specify 1 to indicate success and 0 to indicate failure. The parameter expects a long value set with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)):  

```kotlin
    Bundle params = new Bundle();
    params.putLong(Param.SUCCESS, 1);
```  

### TAX

```
constÂ valÂ TAX = "tax":Â String!
```

Tax cost associated with a transaction (double). Expecting a double value set with [putDouble](https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)):  

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.TAX, 2.43);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $2.43 USD
```  

### TERM

```
constÂ valÂ TERM = "term":Â String!
```

[CAMPAIGN_DETAILS](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#CAMPAIGN_DETAILS()) term; used with paid search to supply the keywords for ads.  

### TRANSACTION_ID

```
constÂ valÂ TRANSACTION_ID = "transaction_id":Â String!
```

The unique identifier of a transaction (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.TRANSACTION_ID, "T12345");
```  

### TRAVEL_CLASS

```
constÂ valÂ TRAVEL_CLASS = "travel_class":Â String!
```

Travel class (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.TRAVEL_CLASS, "business");
```  

### VALUE

```
constÂ valÂ VALUE = "value":Â String!
```

A context-specific numeric value which is accumulated automatically for each event type. Value should be specified with [putLong](https://developer.android.com/reference/android/os/BaseBundle.html#putLong(java.lang.String, long)) or [putDouble](https://developer.android.com/reference/android/os/BaseBundle.html#putDouble(java.lang.String, double)). This is a general purpose parameter that is useful for accumulating a key metric that pertains to an event. Examples include revenue, distance, time, and points. Notes: Values for pre-defined currency-related events (such as [ADD_TO_CART](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Event#ADD_TO_CART())) should be accompanied by a [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) param. The valid range of accumulated values is \[-9,223,372,036,854.77, 9,223,372,036,854.77\]. Supplying a non-numeric value, omitting the corresponding [CURRENCY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.Param#CURRENCY()) parameter, or supplying an invalid [currency code](https://goo.gl/qqX3J2) for conversion events will cause that conversion to be omitted from reporting.  

```kotlin
    Bundle params = new Bundle();
    params.putDouble(Param.VALUE, 3.99);
    params.putString(Param.CURRENCY, "USD" );  // e.g. $3.99 USD
```  

### VIRTUAL_CURRENCY_NAME

```
constÂ valÂ VIRTUAL_CURRENCY_NAME = "virtual_currency_name":Â String!
```

Name of virtual currency type (String). The parameter expects a string value set with [putString](https://developer.android.com/reference/android/os/BaseBundle.html#putString(java.lang.String, java.lang.String)):  

```kotlin
    Bundle params = new Bundle();
    params.putString(Param.VIRTUAL_CURRENCY_NAME, "gems");
```  

## Protected constructors

### Param

```
protectedÂ Param()
```