# Source: https://firebase.google.com/docs/reference/cpp/group/parameter-names.md.txt

# Analytics Parameters

# Analytics Parameters

Predefined event parameter names.

## Summary

Params supply information that contextualize Events. You can associate up to 25 unique Params with each Event type. Some Params are suggested below for certain common Events, but you are not limited to these. You may supply extra Params for suggested Events or custom Params for Custom events. Param names can be up to 40 characters long, may only contain alphanumeric characters and underscores ("_"), and must start with an alphabetic character. Param values can be up to 100 characters long for standard Google Analytics properties and up to 500 characters long for Google Analytics 360 properties. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used.

| ### Variables ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gab8e8281c0b893e05131c33e6c832ec8e = "achievement_id"` | `const char *const` Game achievement ID (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gaac15fa899184e62a64242b7c84553575 = "ad_format"` | `const char *const` The ad format (e.g. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gac927d3dc2bd173b2e32bf8cc38e9f255 = "aclid"` | `const char *const` Ad Network Click ID (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga3c35f99563eca3301a93ff00f4e8dca5 = "ad_platform"` | `const char *const` The ad platform (e.g. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga143c0123216322aa063c94eaf73d3895 = "ad_source"` | `const char *const` The ad source (e.g. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga6def3ddad7794cc67d3668098cfe376c = "ad_unit_name"` | `const char *const` The ad unit name (e.g. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gac23c98bd6093ddd5ea17c946682464af = "affiliation"` | `const char *const` A product affiliation to designate a supplying company or brick and mortar store location (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga4e29459e866c6159237cac6cd9f08e0b = "cp1"` | `const char *const` Campaign custom parameter (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga1e2ba8b7c6b351308f25d164dd3bd400 = "campaign"` | `const char *const` The individual campaign name, slogan, promo code, etc. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga012d6436a23fa8d8fe694b00e1cc9da2 = "campaign_id"` | `const char *const` Campaign ID (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga6bee93cf62048b8f2f49a7e66128881e = "character"` | `const char *const` Character used in game (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga40acfe37fc6eafd12410bb4db79f4f2c = "content"` | `const char *const` Campaign content (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga210e023067955536eb52b537a3bc2f8d = "content_type"` | `const char *const` Type of content selected (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga7f9e905b26189e20fe0a0c5c96687df5 = "coupon"` | `const char *const` Coupon code used for a purchase (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga4ca46e8d54c6d60a5067ae718d403e64 = "creative_format"` | `const char *const` Creative Format (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga6c48c976a65eece77e1e19692c58e4b1 = "creative_name"` | `const char *const` The name of a creative used in a promotional spot (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga946751c8ba9dc64d97112dc02aad153d = "creative_slot"` | `const char *const` The name of a creative slot (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gabfcda4403cd012ef3f51c01d8db394fb = "currency"` | `const char *const` Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga7e0ab6989e5bc6f3ec408adacee2e93a = "destination"` | `const char *const` Flight or Travel destination (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga6c8ad004ce59fdeb914d4f612db07be0 = "discount"` | `const char *const` Monetary value of discount associated with a purchase (Double). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga12550e2018da51c70e7cae79272052bb = "end_date"` | `const char *const` The arrival date, check-out date or rental end date for the item. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga387b075bbe4a5cb13f7e69487ae3d200 = "extend_session"` | `const char *const` Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga3eab1f802585028dd689ce7009315ade = "flight_number"` | `const char *const` Flight number for travel events (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga050060cbe2ee4d6a586f2783c48b5e32 = "free_trial"` | `const char *const` Indicates if the user is on a free trial of a subscription. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gacd0cdb9c1accb51c982490bdc2cee8fd = "group_id"` | `const char *const` Group/clan/guild ID (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gaf9bf0c13e11e71879cd79023c5b22d63 = "index"` | `const char *const` The index of the item in a list (Int). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gaece40be5bdbd31c9010a48c9c057d472 = "item_brand"` | `const char *const` Item brand (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga8aebb6b8a56a906f76cab8aa71f57d17 = "item_category"` | `const char *const` Item category (context-specific) (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gae474702372e837331cbe94699d47b885 = "item_category2"` | `const char *const` Item Category (context-specific) (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga7478feb65ad299f5a38c3cb105c493ff = "item_category3"` | `const char *const` Item Category (context-specific) (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga921dfdf2c11ca1c6edd58335df1813f1 = "item_category4"` | `const char *const` Item Category (context-specific) (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga422870c48a37f06db065b8d24229fe92 = "item_category5"` | `const char *const` Item Category (context-specific) (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga58457392841b4c4b36448ec6e70a1fdd = "item_id"` | `const char *const` Item ID (context-specific) (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga2317a88bab265bae4c64d0af3f4e15ab = "item_list_id"` | `const char *const` The ID of the list in which the item was presented to the user (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gae12be4181a849683d8228be2b11d4ebc = "item_list_name"` | `const char *const` The name of the list in which the item was presented to the user (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gaf241070f04d25b39c4122b31d0aa4590 = "item_name"` | `const char *const` Item Name (context-specific) (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga8f5ba81117a69ecfdee2f96f86615fd0 = "item_variant"` | `const char *const` Item variant (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gae206265f291389b09798a1a11afc1cb5 = "items"` | `const char *const` The list of items involved in the transaction expressed as `[[String: Any]]`. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gad5e2cb9d4c91afea5a8e5314ae8d9b9f = "level"` | `const char *const` Level in game (Int). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga5eaf0ab74002b82a0d6efd84496720fb = "level_name"` | `const char *const` The name of a level in a game (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gae578917dae34301ce5726ef54ea5f807 = "location"` | `const char *const` Location (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga579b93655f660e7f2168f66a800687ae = "location_id"` | `const char *const` The location associated with the event. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga81bbbc53fd828e904caa6927f86d162a = "marketing_tactic"` | `const char *const` Marketing Tactic (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga6ce1a7485d7adbd23d21c1b62e24feef = "medium"` | `const char *const` The advertising or marParameter(keting, cpc, banner, email), push. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga10e9e410b57da93060817dcd479d9452 = "method"` | `const char *const` A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga6f32e4529fbaec902e0ee8f227e4894c = "number_of_nights"` | `const char *const` Number of nights staying at hotel (Int). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gad744fec6316ff1aa025179c63a51a569 = "number_of_passengers"` | `const char *const` Number of passengers traveling (Int). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga6d28e50401051046066a90e4779b3959 = "number_of_rooms"` | `const char *const` Number of rooms for travel events (Int). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gadfd58375e1f70cd50110c795b8c8dceb = "origin"` | `const char *const` Flight or Travel origin (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga3d6b63bc032c972a7ec9fd41727b7940 = "payment_type"` | `const char *const` The chosen method of payment (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga2f9022310179ff9f3e92014d0a2637d0 = "price"` | `const char *const` Purchase price (Double). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga86cfd18063e59d4dc8c4742a61c2bd31 = "price_is_discounted"` | `const char *const` Indicates if an item's price is discounted. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga1e482ff9a400f0d34ba04a4d7e69e7bc = "product_id"` | `const char *const` The ID of a product (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gaf04225da73493ac13a2b7a21f6fc4a3f = "product_name"` | `const char *const` The name of a product (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga2f49b86a3e93797e277c6e45437aba1b = "promotion_id"` | `const char *const` The ID of a product promotion (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga276907602a4a99b7a12121ca6c95afcc = "promotion_name"` | `const char *const` The name of a product promotion (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga4a6de5b9ffa9cda2d92f4443f8f05896 = "quantity"` | `const char *const` Purchase quantity (Int). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga95658395aa1bbdba009b0ec12202e320 = "score"` | `const char *const` Score in game (Int). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga5e48cd9a2d43d1f1ec2b9408be14dee4 = "screen_class"` | `const char *const` Current screen class, such as the class name of the UIViewController, logged with screen_view event and added to every event (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga8764b450cefcb22eb97ed49d099215aa = "screen_name"` | `const char *const` Current screen name, such as the name of the UIViewController, logged with screen_view event and added to every event (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga514604d88fc7722d9765918485231c28 = "search_term"` | `const char *const` The search string/keywords used (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga5675f476c4f49a4f4ab31d95a6a1e5a2 = "shipping"` | `const char *const` Shipping cost associated with a transaction (Double). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gab23feded276b97f96b6bbfb84bb9b815 = "shipping_tier"` | `const char *const` The shipping tier (e.g. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gac6692c120cd5f8bef3236a7b3adb29cc = "source"` | `const char *const` The origin of your traffic, such as an Ad network (for example, google) or partner (urban airship). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gae2363c13a160fde54a114518f2d6be26 = "source_platform"` | `const char *const` Source Platform (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga5bfba1e4ea1d69daabd2f9e0dbd31eb6 = "start_date"` | `const char *const` The departure date, check-in date or rental start date for the item. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga300483c7dcd7d2d9bb1b0bcd0a4d57c9 = "subscription"` | `const char *const` Indicates if the purchase is a subscription. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gafd6190bee20f622b20f88d66dbc356c0 = "success"` | `const char *const` The result of an operation. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga71cb2d643b5e27aaa84e489aa769d2a0 = "tax"` | `const char *const` Tax cost associated with a transaction (Double). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga3662836733c5ec45bc7f3f13ae119eac = "term"` | `const char *const` If you're manually tagging keyword campaigns, you should use utm_term to specify the keyword (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga559918d80a905913a59c97f35d3b125c = "transaction_id"` | `const char *const` The unique identifier of a transaction (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1gaadc505211e00567038d97bd309c9d54b = "travel_class"` | `const char *const` Travel class (String). |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga891958841005e91eea6aeb0b5d4c08b9 = "value"` | `const char *const` A context-specific numeric value which is accumulated automatically for each event type. |
| `https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names_1ga03bd854eb3acf45361870759353e1fee = "virtual_currency_name"` | `const char *const` Name of virtual currency type (String). |

## Variables

### kParameterAchievementID

```c++
const char *const kParameterAchievementID =
    "achievement_id"
```
Game achievement ID (String).


```c++
let params = [
  AnalyticsParameterAchievementID : "10_matches_won",
  // ...
]
```

<br />

### kParameterAdFormat

```c++
const char *const kParameterAdFormat =
    "ad_format"
```
The ad format (e.g.

Banner, Interstitial, Rewarded, Native, Rewarded Interstitial, Instream). (String).

```c++
let params = [
  AnalyticsParameterAdFormat : "Banner",
  // ...
]
```

<br />

### kParameterAdNetworkClickID

```c++
const char *const kParameterAdNetworkClickID = "aclid"
```
Ad Network Click ID (String).

Used for network-specific click IDs which vary in format.

```c++
let params = [
  AnalyticsParameterAdNetworParameter(kClickID, "1234567"),
  // ...
]
```

<br />

### kParameterAdPlatform

```c++
const char *const kParameterAdPlatform =
    "ad_platform"
```
The ad platform (e.g.

MoPub, IronSource) (String).

```c++
let params = [
  AnalyticsParameterAdPlatform : "MoPub",
  // ...
]
```

<br />

### kParameterAdSource

```c++
const char *const kParameterAdSource =
    "ad_source"
```
The ad source (e.g.

AdColony) (String).

```c++
let params = [
  AnalyticsParameterAdSource : "AdColony",
  // ...
]
```

<br />

### kParameterAdUnitName

```c++
const char *const kParameterAdUnitName =
    "ad_unit_name"
```
The ad unit name (e.g.

Banner_03) (String).

```c++
let params = [
  AnalyticsParameterAdUnitName : "Banner_03",
  // ...
]
```

<br />

### kParameterAffiliation

```c++
const char *const kParameterAffiliation =
    "affiliation"
```
A product affiliation to designate a supplying company or brick and mortar store location (String).


```c++
let params = [
  AnalyticsParameterAffiliation : "Google Store",
  // ...
]
```

<br />

### kParameterCP1

```c++
const char *const kParameterCP1 = "cp1"
```
Campaign custom parameter (String).

Used as a method of capturing custom data in a campaign. Use varies by network.

```c++
let params = [
  AnalyticsParameterCP1 : "custom_data",
  // ...
]
```

<br />

### kParameterCampaign

```c++
const char *const kParameterCampaign =
    "campaign"
```
The individual campaign name, slogan, promo code, etc.

Some networks have pre-defined macro to capture campaign information, otherwise can be populated by developer. Highly Recommended (String).

```c++
let params = [
  AnalyticsParameterCampaign : "winter_promotion",
  // ...
]
```

<br />

### kParameterCampaignID

```c++
const char *const kParameterCampaignID =
    "campaign_id"
```
Campaign ID (String).

Used for keyword analysis to identify a specific product promotion or strategic campaign. This is a required key for GA4 data import.

```c++
let params = [
  AnalyticsParameterCampaignID : "7877652710",
  // ...
]
```

<br />

### kParameterCharacter

```c++
const char *const kParameterCharacter =
    "character"
```
Character used in game (String).


```c++
let params = [
  AnalyticsParameterCharacter : "beat_boss",
  // ...
]
```

<br />

### kParameterContent

```c++
const char *const kParameterContent = "content"
```
Campaign content (String).

### kParameterContentType

```c++
const char *const kParameterContentType =
    "content_type"
```
Type of content selected (String).


```c++
let params = [
  AnalyticsParameterContentType : "news article",
  // ...
]
```

<br />

### kParameterCoupon

```c++
const char *const kParameterCoupon = "coupon"
```
Coupon code used for a purchase (String).


```c++
let params = [
  AnalyticsParameterCoupon : "SUMMER_FUN",
  // ...
]
```

<br />

### kParameterCreativeFormat

```c++
const char *const kParameterCreativeFormat =
    "creative_format"
```
Creative Format (String).

Used to identify the high-level classification of the type of ad served by a specific campaign.

```c++
let params = [
  AnalyticsParameterCreativeFormat : "display",
  // ...
]
```

<br />

### kParameterCreativeName

```c++
const char *const kParameterCreativeName =
    "creative_name"
```
The name of a creative used in a promotional spot (String).


```c++
let params = [
  AnalyticsParameterCreativeName : "Summer Sale",
  // ...
]
```

<br />

### kParameterCreativeSlot

```c++
const char *const kParameterCreativeSlot =
    "creative_slot"
```
The name of a creative slot (String).


```c++
let params = [
  AnalyticsParameterCreativeSlot : "summer_banner2",
  // ...
]
```

<br />

### kParameterCurrency

```c++
const char *const kParameterCurrency =
    "currency"
```
Currency of the purchase or items associated with the event, in 3-letter [ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes) format (String).


```c++
let params = [
  AnalyticsParameterCurrency : "USD",
  // ...
]
```

<br />

### kParameterDestination

```c++
const char *const kParameterDestination =
    "destination"
```
Flight or Travel destination (String).


```c++
let params = [
  AnalyticsParameterDestination : "Mountain View, CA",
  // ...
]
```

<br />

### kParameterDiscount

```c++
const char *const kParameterDiscount =
    "discount"
```
Monetary value of discount associated with a purchase (Double).


```c++
let params = [
  AnalyticsParameterDiscount : 2.0,
  AnalyticsParameterCurrency : "USD",  // e.g. $2.00 USD
  // ...
]
```

<br />

### kParameterEndDate

```c++
const char *const kParameterEndDate = "end_date"
```
The arrival date, check-out date or rental end date for the item.

This should be in YYYY-MM-DD format (String).

```c++
let params = [
  AnalyticsParameterEndDate : "2015-09-14",
  // ...
]
```

<br />

### kParameterExtendSession

```c++
const char *const kParameterExtendSession =
    "extend_session"
```
Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged.

Specify 1 to extend the current session or to start a new session; any other value will not extend or start a session.

```c++
let params = [
  AnalyticsParameterExtendSession : 1,
  // ...
]
```

<br />

### kParameterFlightNumber

```c++
const char *const kParameterFlightNumber =
    "flight_number"
```
Flight number for travel events (String).


```c++
let params = [
  AnalyticsParameterFlightNumber : "ZZ800",
  // ...
]
```

<br />

### kParameterFreeTrial

```c++
const char *const kParameterFreeTrial =
    "free_trial"
```
Indicates if the user is on a free trial of a subscription.

Specify 1 to indicate true and 0 to indicate false (Int).

```c++
let params = [
  AnalyticsParameterFreeTrial : 1,
  // ...
]
```

<br />

### kParameterGroupID

```c++
const char *const kParameterGroupID = "group_id"
```
Group/clan/guild ID (String).


```c++
let params = [
  AnalyticsParameterGroupID : "g1",
  // ...
]
```

<br />

### kParameterIndex

```c++
const char *const kParameterIndex = "index"
```
The index of the item in a list (Int).


```c++
let params = [
  AnalyticsParameterIndex : 5,
  // ...
]
```

<br />

### kParameterItemBrand

```c++
const char *const kParameterItemBrand =
    "item_brand"
```
Item brand (String).


```c++
let params = [
  AnalyticsParameterItemBrand : "Google",
  // ...
]
```

<br />

### kParameterItemCategory

```c++
const char *const kParameterItemCategory =
    "item_category"
```
Item category (context-specific) (String).


```c++
let params = [
  AnalyticsParameterItemCategory : "pants",
  // ...
]
```

<br />

### kParameterItemCategory2

```c++
const char *const kParameterItemCategory2 =
    "item_category2"
```
Item Category (context-specific) (String).


```c++
let params = [
  AnalyticsParameterItemCategory2 : "pants",
  // ...
]
```

<br />

### kParameterItemCategory3

```c++
const char *const kParameterItemCategory3 =
    "item_category3"
```
Item Category (context-specific) (String).


```c++
let params = [
  AnalyticsParameterItemCategory3 : "pants",
  // ...
]
```

<br />

### kParameterItemCategory4

```c++
const char *const kParameterItemCategory4 =
    "item_category4"
```
Item Category (context-specific) (String).


```c++
let params = [
  AnalyticsParameterItemCategory4 : "pants",
  // ...
]
```

<br />

### kParameterItemCategory5

```c++
const char *const kParameterItemCategory5 =
    "item_category5"
```
Item Category (context-specific) (String).


```c++
let params = [
  AnalyticsParameterItemCategory5 : "pants",
  // ...
]
```

<br />

### kParameterItemID

```c++
const char *const kParameterItemID = "item_id"
```
Item ID (context-specific) (String).


```c++
let params = [
  AnalyticsParameterItemID : "SKU_12345",
  // ...
]
```

<br />

### kParameterItemListID

```c++
const char *const kParameterItemListID =
    "item_list_id"
```
The ID of the list in which the item was presented to the user (String).


```c++
let params = [
  AnalyticsParameterItemListID : "ABC123",
  // ...
]
```

<br />

### kParameterItemListName

```c++
const char *const kParameterItemListName =
    "item_list_name"
```
The name of the list in which the item was presented to the user (String).


```c++
let params = [
  AnalyticsParameterItemListName : "Related products",
  // ...
]
```

<br />

### kParameterItemName

```c++
const char *const kParameterItemName =
    "item_name"
```
Item Name (context-specific) (String).


```c++
let params = [
  AnalyticsParameterItemName : "jeggings",
  // ...
]
```

<br />

### kParameterItemVariant

```c++
const char *const kParameterItemVariant =
    "item_variant"
```
Item variant (String).


```c++
let params = [
  AnalyticsParameterItemVariant : "Black",
  // ...
]
```

<br />

### kParameterItems

```c++
const char *const kParameterItems = "items"
```
The list of items involved in the transaction expressed as `[[String: Any]]`.


```c++
let params = [
  AnalyticsParameterItems : [
    [AnalyticsParameterItemName : "jeggings", AnalyticsParameterItemCategory : "pants"],
    [AnalyticsParameterItemName : "boots", AnalyticsParameterItemCategory : "shoes"],
  ],
]
```

<br />

### kParameterLevel

```c++
const char *const kParameterLevel = "level"
```
Level in game (Int).


```c++
let params = [
  AnalyticsParameterLevel : 42,
  // ...
]
```

<br />

### kParameterLevelName

```c++
const char *const kParameterLevelName =
    "level_name"
```
The name of a level in a game (String).


```c++
let params = [
  AnalyticsParameterLevelName : "room_1",
  // ...
]
```

<br />

### kParameterLocation

```c++
const char *const kParameterLocation =
    "location"
```
Location (String).

The Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated event. Alternatively, you can supply your own custom Location ID.

```c++
let params = [
  AnalyticsParameterLocation : "ChIJiyj437sx3YAR9kUWC8QkLzQ",
  // ...
]
```

<br />

### kParameterLocationID

```c++
const char *const kParameterLocationID =
    "location_id"
```
The location associated with the event.

Preferred to be the Google [Place ID](https://developers.google.com/places/place-id) that corresponds to the associated item but could be overridden to a custom location ID string.(String).

```c++
let params = [
  AnalyticsParameterLocationID : "ChIJiyj437sx3YAR9kUWC8QkLzQ",
  // ...
]
```

<br />

### kParameterMarketingTactic

```c++
const char *const kParameterMarketingTactic = "marketing_tactic"
```
Marketing Tactic (String).

Used to identify the targeting criteria applied to a specific campaign.

```c++
let params = [
  AnalyticsParameterMarParameter(ketingTactic, "Remarketing"),
  // ...
]
```

<br />

### kParameterMedium

```c++
const char *const kParameterMedium = "medium"
```
The advertising or marParameter(keting, cpc, banner, email), push.

Highly recommended (String).

```c++
let params = [
  AnalyticsParameterMedium : "email",
  // ...
]
```

<br />

### kParameterMethod

```c++
const char *const kParameterMethod = "method"
```
A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event.

(String).

```c++
let params = [
  AnalyticsParameterMethod : "google",
  // ...
]
```

<br />

### kParameterNumberOfNights

```c++
const char *const kParameterNumberOfNights = "number_of_nights"
```
Number of nights staying at hotel (Int).


```c++
let params = [
  AnalyticsParameterNumberOfNights : 3,
  // ...
]
```

<br />

### kParameterNumberOfPassengers

```c++
const char *const kParameterNumberOfPassengers = "number_of_passengers"
```
Number of passengers traveling (Int).


```c++
let params = [
  AnalyticsParameterNumberOfPassengers : 11,
  // ...
]
```

<br />

### kParameterNumberOfRooms

```c++
const char *const kParameterNumberOfRooms =
    "number_of_rooms"
```
Number of rooms for travel events (Int).


```c++
let params = [
  AnalyticsParameterNumberOfRooms : 2,
  // ...
]
```

<br />

### kParameterOrigin

```c++
const char *const kParameterOrigin = "origin"
```
Flight or Travel origin (String).


```c++
let params = [
  AnalyticsParameterOrigin : "Mountain View, CA",
  // ...
]
```

<br />

### kParameterPaymentType

```c++
const char *const kParameterPaymentType =
    "payment_type"
```
The chosen method of payment (String).


```c++
let params = [
  AnalyticsParameterPaymentType : "Visa",
  // ...
]
```

<br />

### kParameterPrice

```c++
const char *const kParameterPrice = "price"
```
Purchase price (Double).


```c++
let params = [
  AnalyticsParameterPrice : 1.0,
  AnalyticsParameterCurrency : "USD",  // e.g. $1.00 USD
  // ...
]
```

<br />

### kParameterPriceIsDiscounted

```c++
const char *const kParameterPriceIsDiscounted = "price_is_discounted"
```
Indicates if an item's price is discounted.

Specify 1 to indicate true and 0 to indicate false (Int).

```c++
let params = [
  AnalyticsParameterPriceIsDiscounted : 1,
  // ...
]
```

<br />

### kParameterProductID

```c++
const char *const kParameterProductID =
    "product_id"
```
The ID of a product (String).


```c++
let params = [
  AnalyticsParameterProductID : "PROD_12345",
  // ...
]
```

<br />

### kParameterProductName

```c++
const char *const kParameterProductName =
    "product_name"
```
The name of a product (String).


```c++
let params = [
  AnalyticsParameterProductName : "My Awesome Product",
  // ...
]
```

<br />

### kParameterPromotionID

```c++
const char *const kParameterPromotionID =
    "promotion_id"
```
The ID of a product promotion (String).


```c++
let params = [
  AnalyticsParameterPromotionID : "ABC123",
  // ...
]
```

<br />

### kParameterPromotionName

```c++
const char *const kParameterPromotionName =
    "promotion_name"
```
The name of a product promotion (String).


```c++
let params = [
  AnalyticsParameterPromotionName : "Summer Sale",
  // ...
]
```

<br />

### kParameterQuantity

```c++
const char *const kParameterQuantity =
    "quantity"
```
Purchase quantity (Int).


```c++
let params = [
  AnalyticsParameterQuantity : 1,
  // ...
]
```

<br />

### kParameterScore

```c++
const char *const kParameterScore = "score"
```
Score in game (Int).


```c++
let params = [
  AnalyticsParameterScore : 4200,
  // ...
]
```

<br />

### kParameterScreenClass

```c++
const char *const kParameterScreenClass =
    "screen_class"
```
Current screen class, such as the class name of the UIViewController, logged with screen_view event and added to every event (String).


```c++
let params = [
  AnalyticsParameterScreenClass : "LoginViewController",
  // ...
]
```

<br />

### kParameterScreenName

```c++
const char *const kParameterScreenName =
    "screen_name"
```
Current screen name, such as the name of the UIViewController, logged with screen_view event and added to every event (String).


```c++
let params = [
  AnalyticsParameterScreenName : "LoginView",
  // ...
]
```

<br />

### kParameterSearchTerm

```c++
const char *const kParameterSearchTerm =
    "search_term"
```
The search string/keywords used (String).


```c++
let params = [
  AnalyticsParameterSearchTerm : "periodic table",
  // ...
]
```

<br />

### kParameterShipping

```c++
const char *const kParameterShipping =
    "shipping"
```
Shipping cost associated with a transaction (Double).


```c++
let params = [
  AnalyticsParameterShipping : 5.99,
  AnalyticsParameterCurrency : "USD",  // e.g. $5.99 USD
  // ...
]
```

<br />

### kParameterShippingTier

```c++
const char *const kParameterShippingTier =
    "shipping_tier"
```
The shipping tier (e.g.

Ground, Air, Next-day) selected for delivery of the purchased item (String).

```c++
let params = [
  AnalyticsParameterShippingTier : "Ground",
  // ...
]
```

<br />

### kParameterSource

```c++
const char *const kParameterSource = "source"
```
The origin of your traffic, such as an Ad network (for example, google) or partner (urban airship).

Identify the advertiser, site, publication, etc. that is sending traffic to your property. Highly recommended (String).

```c++
let params = [
  AnalyticsParameterSource : "InMobi",
  // ...
]
```

<br />

### kParameterSourcePlatform

```c++
const char *const kParameterSourcePlatform =
    "source_platform"
```
Source Platform (String).

Used to identify the platform responsible for directing traffic to a given Analytics property (e.g., a buying platform where budgets, targeting criteria, etc. are set, a platform for managing organic traffic data, etc.).

```c++
let params = [
  AnalyticsParameterSourcePlatform : "sa360",
  // ...
]
```

<br />

### kParameterStartDate

```c++
const char *const kParameterStartDate =
    "start_date"
```
The departure date, check-in date or rental start date for the item.

This should be in YYYY-MM-DD format (String).

```c++
let params = [
  AnalyticsParameterStartDate : "2015-09-14",
  // ...
]
```

<br />

### kParameterSubscription

```c++
const char *const kParameterSubscription =
    "subscription"
```
Indicates if the purchase is a subscription.

Specify 1 to indicate true and 0 to indicate false (Int).

```c++
let params = [
  AnalyticsParameterSubscription : 1,
  // ...
]
```

<br />

### kParameterSuccess

```c++
const char *const kParameterSuccess = "success"
```
The result of an operation.

Specify 1 to indicate success and 0 to indicate failure (Int).

```c++
let params = [
  AnalyticsParameterSuccess : 1,
  // ...
]
```

<br />

### kParameterTax

```c++
const char *const kParameterTax = "tax"
```
Tax cost associated with a transaction (Double).


```c++
let params = [
  AnalyticsParameterTax : 2.43,
  AnalyticsParameterCurrency : "USD",  // e.g. $2.43 USD
  // ...
]
```

<br />

### kParameterTerm

```c++
const char *const kParameterTerm = "term"
```
If you're manually tagging keyword campaigns, you should use utm_term to specify the keyword (String).


```c++
let params = [
  AnalyticsParameterTerm : "game",
  // ...
]
```

<br />

### kParameterTransactionID

```c++
const char *const kParameterTransactionID =
    "transaction_id"
```
The unique identifier of a transaction (String).


```c++
let params = [
  AnalyticsParameterTransactionID : "T12345",
  // ...
]
```

<br />

### kParameterTravelClass

```c++
const char *const kParameterTravelClass =
    "travel_class"
```
Travel class (String).


```c++
let params = [
  AnalyticsParameterTravelClass : "business",
  // ...
]
```

<br />

### kParameterValue

```c++
const char *const kParameterValue = "value"
```
A context-specific numeric value which is accumulated automatically for each event type.

This is a general purpose parameter that is useful for accumulating a key metric that pertains to an event. Examples include revenue, distance, time and points. Value should be specified as Int or Double. Notes: Values for pre-defined currency-related events (such as `AnalyticsEventAddToCart`) should be supplied using Double and must be accompanied by a `AnalyticsParameterCurrency` parameter. The valid range of accumulated values is \[-9,223,372,036,854.77, 9,223,372,036,854.77\]. Supplying a non-numeric value, omitting the corresponding `AnalyticsParameterCurrency` parameter, or supplying an invalid [currency code](https://goo.gl/qqX3J2) for conversion events will cause that conversion to be omitted from reporting.

```c++
let params = [
  AnalyticsParameterValue : 3.99,
  AnalyticsParameterCurrency : "USD",  // e.g. $3.99 USD
  // ...
]
```

<br />

### kParameterVirtualCurrencyName

```c++
const char *const kParameterVirtualCurrencyName = "virtual_currency_name"
```
Name of virtual currency type (String).


```c++
let params = [
  AnalyticsParameterVirtualCurrencyName : "virtual_currency_name",
  // ...
]
```

<br />