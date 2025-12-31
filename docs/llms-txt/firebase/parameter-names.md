# Source: https://firebase.google.com/docs/reference/cpp/group/parameter-names.md.txt

# Source: https://firebase.google.com/docs/reference/unity/group/parameter-names.md.txt

# Analytics Parameters

Predefined event parameter names.

## Summary

Params supply information that contextualize Events. You can associate up to 25 unique Params with each Event type. Some Params are suggested below for certain common Events, but you are not limited to these. You may supply extra Params for suggested Events or custom Params for Custom events. Param names can be up to 40 characters long, may only contain alphanumeric characters and underscores ("_"), and must start with an alphabetic character. Param values can be up to 100 characters long for standard Google[Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics)properties and up to 500 characters long for Google[Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics)360 properties. The "firebase_", "google_", and "ga_" prefixes are reserved and should not be used.

|                                                                                                                                                                          ### Variables                                                                                                                                                                           ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ParameterAchievementID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga27e8cb3cb48a1992a7c147755db64fbd)` = "achievement_id"`              | `string` Game achievement ID (String).                                                                                                                           |
| [ParameterAdFormat](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gad1ee55f39670de3db76681e55c37d850)` = "ad_format"`                        | `string` The ad format (e.g.                                                                                                                                     |
| [ParameterAdNetworkClickID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gaadb818f4cef52b43d84e403624eb34ae)` = "aclid"`                    | `string` Ad Network Click ID (String).                                                                                                                           |
| [ParameterAdPlatform](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga737addbe77b5f92387a03b2a15bb59b0)` = "ad_platform"`                    | `string` The ad platform (e.g.                                                                                                                                   |
| [ParameterAdSource](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga6e3aaaed5e77868b5857b70f0457b5da)` = "ad_source"`                        | `string` The ad source (e.g.                                                                                                                                     |
| [ParameterAdUnitName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga935624c4e7bee91aa59b74bf8a8ac739)` = "ad_unit_name"`                   | `string` The ad unit name (e.g.                                                                                                                                  |
| [ParameterAffiliation](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga8308d0256fa1fa5ef5c7140dd10c33be)` = "affiliation"`                   | `string` A product affiliation to designate a supplying company or brick and mortar store location (String).                                                     |
| [ParameterCP1](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga378d0bb3d9ff4261acc5bb9c57bef762)` = "cp1"`                                   | `string` Campaign custom parameter (String).                                                                                                                     |
| [ParameterCampaign](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gac58c8d2e923a05b764e4218c8781f0ff)` = "campaign"`                         | `string` The individual campaign name, slogan, promo code, etc.                                                                                                  |
| [ParameterCampaignID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga13dac1f1a100f479a2a01c44ef25715c)` = "campaign_id"`                    | `string` Campaign ID (String).                                                                                                                                   |
| [ParameterCharacter](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gacf50a02bceb87a582c6fc55c6c0717f2)` = "character"`                       | `string` Character used in game (String).                                                                                                                        |
| [ParameterContent](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga5f380ff487f66edc790656762ef6d974)` = "content"`                           | `string` Campaign content (String).                                                                                                                              |
| [ParameterContentType](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga39a37092cd3fce53ba6ffa53289e1fe9)` = "content_type"`                  | `string` Type of content selected (String).                                                                                                                      |
| [ParameterCoupon](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga9413a4d3a4fc4fe68c340187abdb751e)` = "coupon"`                             | `string` Coupon code used for a purchase (String).                                                                                                               |
| [ParameterCreativeFormat](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga04bd1800c6d7ba7d7ccde63c012bc22e)` = "creative_format"`            | `string` Creative Format (String).                                                                                                                               |
| [ParameterCreativeName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga48f69dc8eb17ec5d5dfcc0f0708168d3)` = "creative_name"`                | `string` The name of a creative used in a promotional spot (String).                                                                                             |
| [ParameterCreativeSlot](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga3282cf4abd93c1d65e4daef1a957cff7)` = "creative_slot"`                | `string` The name of a creative slot (String).                                                                                                                   |
| [ParameterCurrency](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gae46e9b16a5145af4127990ee02cf2c74)` = "currency"`                         | `string` Currency of the purchase or items associated with the event, in 3-letter[ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes)format (String).  |
| [ParameterDestination](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga67347716dc73e56171dbebbba51febd4)` = "destination"`                   | `string` Flight or Travel destination (String).                                                                                                                  |
| [ParameterDiscount](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga60dcf4f898f38c73ef988c3b83585355)` = "discount"`                         | `string` Monetary value of discount associated with a purchase (Double).                                                                                         |
| [ParameterEndDate](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga3407b387b96a305eca0efd8010dc45bf)` = "end_date"`                          | `string` The arrival date, check-out date or rental end date for the item.                                                                                       |
| [ParameterExtendSession](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga9e561362e49617a81b330e120dc382ce)` = "extend_session"`              | `string` Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged. |
| [ParameterFlightNumber](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gabf078dc5a36b3f19ba9648d27a88a533)` = "flight_number"`                | `string` Flight number for travel events (String).                                                                                                               |
| [ParameterFreeTrial](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga268fd542d2a8201c999fe159ddba6911)` = "free_trial"`                      | `string` Indicates if the user is on a free trial of a subscription.                                                                                             |
| [ParameterGroupID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gab0c6c1ae9c737f0a0b4e71099055b234)` = "group_id"`                          | `string` Group/clan/guild ID (String).                                                                                                                           |
| [ParameterIndex](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gabe7af91955e082800099f0b9fb93d68e)` = "index"`                               | `string` The index of the item in a list (Int).                                                                                                                  |
| [ParameterItemBrand](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga2cb352537be257df46cfc3af1f212c71)` = "item_brand"`                      | `string` Item brand (String).                                                                                                                                    |
| [ParameterItemCategory](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga6aabf1eea78e6e0b3aa558e2a98667fb)` = "item_category"`                | `string` Item category (context-specific) (String).                                                                                                              |
| [ParameterItemCategory2](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gab69949be997cdc98477844b7cbc863f9)` = "item_category2"`              | `string` Item Category (context-specific) (String).                                                                                                              |
| [ParameterItemCategory3](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gae3ca33c480239ee44c0566f5d636e70e)` = "item_category3"`              | `string` Item Category (context-specific) (String).                                                                                                              |
| [ParameterItemCategory4](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gacdedf0e9e5be48c02bc5de409fd46cbc)` = "item_category4"`              | `string` Item Category (context-specific) (String).                                                                                                              |
| [ParameterItemCategory5](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga223d3b516c655174613807a44ed84283)` = "item_category5"`              | `string` Item Category (context-specific) (String).                                                                                                              |
| [ParameterItemID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga27f2b08585ae5a389fad573a46e29b11)` = "item_id"`                            | `string` Item ID (context-specific) (String).                                                                                                                    |
| [ParameterItemListID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga69eb93c8a4023aa8c4011677e68f0928)` = "item_list_id"`                   | `string` The ID of the list in which the item was presented to the user (String).                                                                                |
| [ParameterItemListName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga2782e3f15edab0abd297393751da2659)` = "item_list_name"`               | `string` The name of the list in which the item was presented to the user (String).                                                                              |
| [ParameterItemName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga52aa7d69ba549c8c5bd83aa04f980f94)` = "item_name"`                        | `string` Item Name (context-specific) (String).                                                                                                                  |
| [ParameterItemVariant](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga20df71ec9c0a472accdd66319fa5bfe5)` = "item_variant"`                  | `string` Item variant (String).                                                                                                                                  |
| [ParameterItems](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga2784d1f012538493c6bb0829b986ae9a)` = "items"`                               | `string` The list of items involved in the transaction expressed as`[[String: Any]]`.                                                                            |
| [ParameterLevel](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga3e747288c7aca047097073062398d5df)` = "level"`                               | `string` Level in game (Int).                                                                                                                                    |
| [ParameterLevelName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga748a5109b769d62cacfcb274facf27db)` = "level_name"`                      | `string` The name of a level in a game (String).                                                                                                                 |
| [ParameterLocation](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga49d8df43f333dbb464eb8be9bca18bd4)` = "location"`                         | `string` Location (String).                                                                                                                                      |
| [ParameterLocationID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gac24c5a521cf32506bc1e58c952e89b71)` = "location_id"`                    | `string` The location associated with the event.                                                                                                                 |
| [ParameterMarketingTactic](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga8d19f9a0a68d3cf102b93b0e61e8d64b)` = "marketing_tactic"`          | `string` Marketing Tactic (String).                                                                                                                              |
| [ParameterMedium](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gad75f5232098329cc85e68c0ca3425b02)` = "medium"`                             | `string` The advertising or marParameter(keting, cpc, banner, email), push.                                                                                      |
| [ParameterMethod](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga7368101eb1614cb80ccf885cff34012b)` = "method"`                             | `string` A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event.                              |
| [ParameterNumberOfNights](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga9a79b5a4b19b5c897a5afad6a6db0411)` = "number_of_nights"`           | `string` Number of nights staying at hotel (Int).                                                                                                                |
| [ParameterNumberOfPassengers](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gae8f3f74b880f9e5aa67c9523ac3bc889)` = "number_of_passengers"`   | `string` Number of passengers traveling (Int).                                                                                                                   |
| [ParameterNumberOfRooms](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gac4871d9ec8656a192e4409cc5e9f197a)` = "number_of_rooms"`             | `string` Number of rooms for travel events (Int).                                                                                                                |
| [ParameterOrigin](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga643498f873a73095ec48541b55caf9d1)` = "origin"`                             | `string` Flight or Travel origin (String).                                                                                                                       |
| [ParameterPaymentType](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga425351ec1386e9e84db6e631a5fed28e)` = "payment_type"`                  | `string` The chosen method of payment (String).                                                                                                                  |
| [ParameterPrice](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga526644fcd239ef7fc8be6b661088d08c)` = "price"`                               | `string` Purchase price (Double).                                                                                                                                |
| [ParameterPriceIsDiscounted](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gab12d820e5ca5df29c9ae9e469991f08b)` = "price_is_discounted"`     | `string` Indicates if an item's price is discounted.                                                                                                             |
| [ParameterProductID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gaf2b38edb5bcb2b7fcfc7eb0fa3bfca5d)` = "product_id"`                      | `string` The ID of a product (String).                                                                                                                           |
| [ParameterProductName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga83821382a7842647ba26d65cd14f91ef)` = "product_name"`                  | `string` The name of a product (String).                                                                                                                         |
| [ParameterPromotionID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga3efc940851d03f70fec63b201f30fc20)` = "promotion_id"`                  | `string` The ID of a product promotion (String).                                                                                                                 |
| [ParameterPromotionName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga80cc63dd506975317c0cbd5fa2a82f35)` = "promotion_name"`              | `string` The name of a product promotion (String).                                                                                                               |
| [ParameterQuantity](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga83a1ca15d25d99aabe755d413e1b7d83)` = "quantity"`                         | `string` Purchase quantity (Int).                                                                                                                                |
| [ParameterScore](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gac69aa0a217496876f0e5a9aedf98b853)` = "score"`                               | `string` Score in game (Int).                                                                                                                                    |
| [ParameterScreenClass](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga99bbe1ef7dad9befa36fab7551aa074b)` = "screen_class"`                  | `string` Current screen class, such as the class name of the UIViewController, logged with screen_view event and added to every event (String).                  |
| [ParameterScreenName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga0b76faae50343c0c636059a999badbf3)` = "screen_name"`                    | `string` Current screen name, such as the name of the UIViewController, logged with screen_view event and added to every event (String).                         |
| [ParameterSearchTerm](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gabb8d52a65f2846418d75a17fe8c3eb6a)` = "search_term"`                    | `string` The search string/keywords used (String).                                                                                                               |
| [ParameterShipping](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gafc75615508fc899e136c27721725bb53)` = "shipping"`                         | `string` Shipping cost associated with a transaction (Double).                                                                                                   |
| [ParameterShippingTier](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga7c18898fd2500cf4ca14ed6e7bd837eb)` = "shipping_tier"`                | `string` The shipping tier (e.g.                                                                                                                                 |
| [ParameterSource](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga70b1519770f25692f7602d39785018d9)` = "source"`                             | `string` The origin of your traffic, such as an Ad network (for example, google) or partner (urban airship).                                                     |
| [ParameterSourcePlatform](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga695127fdfc935c8b86340c19e5aeb70e)` = "source_platform"`            | `string` Source Platform (String).                                                                                                                               |
| [ParameterStartDate](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gabbdcdd99c8cda186d418a2390160196d)` = "start_date"`                      | `string` The departure date, check-in date or rental start date for the item.                                                                                    |
| [ParameterSubscription](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga7c50342f527ce01a8146c67834b35d4d)` = "subscription"`                 | `string` Indicates if the purchase is a subscription.                                                                                                            |
| [ParameterSuccess](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gaa4eed7e18b679bbc0e2101533b9b18ce)` = "success"`                           | `string` The result of an operation.                                                                                                                             |
| [ParameterTax](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga3b635b513c5ff886d4276607f01879dd)` = "tax"`                                   | `string` Tax cost associated with a transaction (Double).                                                                                                        |
| [ParameterTerm](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga1404b8d46c6a333ab46c5e01332694ef)` = "term"`                                 | `string` If you're manually tagging keyword campaigns, you should use utm_term to specify the keyword (String).                                                  |
| [ParameterTransactionID](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gaffb421d1795f302632bb0b3369632acf)` = "transaction_id"`              | `string` The unique identifier of a transaction (String).                                                                                                        |
| [ParameterTravelClass](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga393eb888a19ee130d69c60912da8266f)` = "travel_class"`                  | `string` Travel class (String).                                                                                                                                  |
| [ParameterValue](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga9c83240ada0e8620e326bbbee48f6855)` = "value"`                               | `string` A context-specific numeric value which is accumulated automatically for each event type.                                                                |
| [ParameterVirtualCurrencyName](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1ga87a99fdfc2233237c854c42855dd2550)` = "virtual_currency_name"` | `string` Name of virtual currency type (String).                                                                                                                 |

## Variables

### ParameterAchievementID

```c#
string ParameterAchievementID =
    "achievement_id"
```  
Game achievement ID (String).

<br />

```c#
let params = [
  AnalyticsParameterAchievementID : "10_matches_won",
  // ...
]
```

<br />

### ParameterAdFormat

```c#
string ParameterAdFormat =
    "ad_format"
```  
The ad format (e.g.

Banner, Interstitial, Rewarded, Native, Rewarded Interstitial, Instream). (String).  

```c#
let params = [
  AnalyticsParameterAdFormat : "Banner",
  // ...
]
```

<br />

### ParameterAdNetworkClickID

```c#
string ParameterAdNetworkClickID = "aclid"
```  
Ad Network Click ID (String).

Used for network-specific click IDs which vary in format.  

```c#
let params = [
  AnalyticsParameterAdNetworParameter(kClickID, "1234567"),
  // ...
]
```

<br />

### ParameterAdPlatform

```c#
string ParameterAdPlatform =
    "ad_platform"
```  
The ad platform (e.g.

MoPub, IronSource) (String).  

```c#
let params = [
  AnalyticsParameterAdPlatform : "MoPub",
  // ...
]
```

<br />

### ParameterAdSource

```c#
string ParameterAdSource =
    "ad_source"
```  
The ad source (e.g.

AdColony) (String).  

```c#
let params = [
  AnalyticsParameterAdSource : "AdColony",
  // ...
]
```

<br />

### ParameterAdUnitName

```c#
string ParameterAdUnitName =
    "ad_unit_name"
```  
The ad unit name (e.g.

Banner_03) (String).  

```c#
let params = [
  AnalyticsParameterAdUnitName : "Banner_03",
  // ...
]
```

<br />

### ParameterAffiliation

```c#
string ParameterAffiliation =
    "affiliation"
```  
A product affiliation to designate a supplying company or brick and mortar store location (String).

<br />

```c#
let params = [
  AnalyticsParameterAffiliation : "Google Store",
  // ...
]
```

<br />

### ParameterCP1

```c#
string ParameterCP1 = "cp1"
```  
Campaign custom parameter (String).

Used as a method of capturing custom data in a campaign. Use varies by network.  

```c#
let params = [
  AnalyticsParameterCP1 : "custom_data",
  // ...
]
```

<br />

### ParameterCampaign

```c#
string ParameterCampaign =
    "campaign"
```  
The individual campaign name, slogan, promo code, etc.

Some networks have pre-defined macro to capture campaign information, otherwise can be populated by developer. Highly Recommended (String).  

```c#
let params = [
  AnalyticsParameterCampaign : "winter_promotion",
  // ...
]
```

<br />

### ParameterCampaignID

```c#
string ParameterCampaignID =
    "campaign_id"
```  
Campaign ID (String).

Used for keyword analysis to identify a specific product promotion or strategic campaign. This is a required key for GA4 data import.  

```c#
let params = [
  AnalyticsParameterCampaignID : "7877652710",
  // ...
]
```

<br />

### ParameterCharacter

```c#
string ParameterCharacter =
    "character"
```  
Character used in game (String).

<br />

```c#
let params = [
  AnalyticsParameterCharacter : "beat_boss",
  // ...
]
```

<br />

### ParameterContent

```c#
string ParameterContent = "content"
```  
Campaign content (String).  

### ParameterContentType

```c#
string ParameterContentType =
    "content_type"
```  
Type of content selected (String).

<br />

```c#
let params = [
  AnalyticsParameterContentType : "news article",
  // ...
]
```

<br />

### ParameterCoupon

```c#
string ParameterCoupon = "coupon"
```  
Coupon code used for a purchase (String).

<br />

```c#
let params = [
  AnalyticsParameterCoupon : "SUMMER_FUN",
  // ...
]
```

<br />

### ParameterCreativeFormat

```c#
string ParameterCreativeFormat =
    "creative_format"
```  
Creative Format (String).

Used to identify the high-level classification of the type of ad served by a specific campaign.  

```c#
let params = [
  AnalyticsParameterCreativeFormat : "display",
  // ...
]
```

<br />

### ParameterCreativeName

```c#
string ParameterCreativeName =
    "creative_name"
```  
The name of a creative used in a promotional spot (String).

<br />

```c#
let params = [
  AnalyticsParameterCreativeName : "Summer Sale",
  // ...
]
```

<br />

### ParameterCreativeSlot

```c#
string ParameterCreativeSlot =
    "creative_slot"
```  
The name of a creative slot (String).

<br />

```c#
let params = [
  AnalyticsParameterCreativeSlot : "summer_banner2",
  // ...
]
```

<br />

### ParameterCurrency

```c#
string ParameterCurrency =
    "currency"
```  
Currency of the purchase or items associated with the event, in 3-letter[ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes)format (String).

<br />

```c#
let params = [
  AnalyticsParameterCurrency : "USD",
  // ...
]
```

<br />

### ParameterDestination

```c#
string ParameterDestination =
    "destination"
```  
Flight or Travel destination (String).

<br />

```c#
let params = [
  AnalyticsParameterDestination : "Mountain View, CA",
  // ...
]
```

<br />

### ParameterDiscount

```c#
string ParameterDiscount =
    "discount"
```  
Monetary value of discount associated with a purchase (Double).

<br />

```c#
let params = [
  AnalyticsParameterDiscount : 2.0,
  AnalyticsParameterCurrency : "USD",  // e.g. $2.00 USD
  // ...
]
```

<br />

### ParameterEndDate

```c#
string ParameterEndDate = "end_date"
```  
The arrival date, check-out date or rental end date for the item.

This should be in YYYY-MM-DD format (String).  

```c#
let params = [
  AnalyticsParameterEndDate : "2015-09-14",
  // ...
]
```

<br />

### ParameterExtendSession

```c#
string ParameterExtendSession =
    "extend_session"
```  
Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged.

Specify 1 to extend the current session or to start a new session; any other value will not extend or start a session.  

```c#
let params = [
  AnalyticsParameterExtendSession : 1,
  // ...
]
```

<br />

### ParameterFlightNumber

```c#
string ParameterFlightNumber =
    "flight_number"
```  
Flight number for travel events (String).

<br />

```c#
let params = [
  AnalyticsParameterFlightNumber : "ZZ800",
  // ...
]
```

<br />

### ParameterFreeTrial

```c#
string ParameterFreeTrial =
    "free_trial"
```  
Indicates if the user is on a free trial of a subscription.

Specify 1 to indicate true and 0 to indicate false (Int).  

```c#
let params = [
  AnalyticsParameterFreeTrial : 1,
  // ...
]
```

<br />

### ParameterGroupID

```c#
string ParameterGroupID = "group_id"
```  
Group/clan/guild ID (String).

<br />

```c#
let params = [
  AnalyticsParameterGroupID : "g1",
  // ...
]
```

<br />

### ParameterIndex

```c#
string ParameterIndex = "index"
```  
The index of the item in a list (Int).

<br />

```c#
let params = [
  AnalyticsParameterIndex : 5,
  // ...
]
```

<br />

### ParameterItemBrand

```c#
string ParameterItemBrand =
    "item_brand"
```  
Item brand (String).

<br />

```c#
let params = [
  AnalyticsParameterItemBrand : "Google",
  // ...
]
```

<br />

### ParameterItemCategory

```c#
string ParameterItemCategory =
    "item_category"
```  
Item category (context-specific) (String).

<br />

```c#
let params = [
  AnalyticsParameterItemCategory : "pants",
  // ...
]
```

<br />

### ParameterItemCategory2

```c#
string ParameterItemCategory2 =
    "item_category2"
```  
Item Category (context-specific) (String).

<br />

```c#
let params = [
  AnalyticsParameterItemCategory2 : "pants",
  // ...
]
```

<br />

### ParameterItemCategory3

```c#
string ParameterItemCategory3 =
    "item_category3"
```  
Item Category (context-specific) (String).

<br />

```c#
let params = [
  AnalyticsParameterItemCategory3 : "pants",
  // ...
]
```

<br />

### ParameterItemCategory4

```c#
string ParameterItemCategory4 =
    "item_category4"
```  
Item Category (context-specific) (String).

<br />

```c#
let params = [
  AnalyticsParameterItemCategory4 : "pants",
  // ...
]
```

<br />

### ParameterItemCategory5

```c#
string ParameterItemCategory5 =
    "item_category5"
```  
Item Category (context-specific) (String).

<br />

```c#
let params = [
  AnalyticsParameterItemCategory5 : "pants",
  // ...
]
```

<br />

### ParameterItemID

```c#
string ParameterItemID = "item_id"
```  
Item ID (context-specific) (String).

<br />

```c#
let params = [
  AnalyticsParameterItemID : "SKU_12345",
  // ...
]
```

<br />

### ParameterItemListID

```c#
string ParameterItemListID =
    "item_list_id"
```  
The ID of the list in which the item was presented to the user (String).

<br />

```c#
let params = [
  AnalyticsParameterItemListID : "ABC123",
  // ...
]
```

<br />

### ParameterItemListName

```c#
string ParameterItemListName =
    "item_list_name"
```  
The name of the list in which the item was presented to the user (String).

<br />

```c#
let params = [
  AnalyticsParameterItemListName : "Related products",
  // ...
]
```

<br />

### ParameterItemName

```c#
string ParameterItemName =
    "item_name"
```  
Item Name (context-specific) (String).

<br />

```c#
let params = [
  AnalyticsParameterItemName : "jeggings",
  // ...
]
```

<br />

### ParameterItemVariant

```c#
string ParameterItemVariant =
    "item_variant"
```  
Item variant (String).

<br />

```c#
let params = [
  AnalyticsParameterItemVariant : "Black",
  // ...
]
```

<br />

### ParameterItems

```c#
string ParameterItems = "items"
```  
The list of items involved in the transaction expressed as`[[String: Any]]`.

<br />

```c#
let params = [
  AnalyticsParameterItems : [
    [AnalyticsParameterItemName : "jeggings", AnalyticsParameterItemCategory : "pants"],
    [AnalyticsParameterItemName : "boots", AnalyticsParameterItemCategory : "shoes"],
  ],
]
```

<br />

### ParameterLevel

```c#
string ParameterLevel = "level"
```  
Level in game (Int).

<br />

```c#
let params = [
  AnalyticsParameterLevel : 42,
  // ...
]
```

<br />

### ParameterLevelName

```c#
string ParameterLevelName =
    "level_name"
```  
The name of a level in a game (String).

<br />

```c#
let params = [
  AnalyticsParameterLevelName : "room_1",
  // ...
]
```

<br />

### ParameterLocation

```c#
string ParameterLocation =
    "location"
```  
Location (String).

The Google[Place ID](https://developers.google.com/places/place-id)that corresponds to the associated event. Alternatively, you can supply your own custom Location ID.  

```c#
let params = [
  AnalyticsParameterLocation : "ChIJiyj437sx3YAR9kUWC8QkLzQ",
  // ...
]
```

<br />

### ParameterLocationID

```c#
string ParameterLocationID =
    "location_id"
```  
The location associated with the event.

Preferred to be the Google[Place ID](https://developers.google.com/places/place-id)that corresponds to the associated item but could be overridden to a custom location ID string.(String).  

```c#
let params = [
  AnalyticsParameterLocationID : "ChIJiyj437sx3YAR9kUWC8QkLzQ",
  // ...
]
```

<br />

### ParameterMarketingTactic

```c#
string ParameterMarketingTactic = "marketing_tactic"
```  
Marketing Tactic (String).

Used to identify the targeting criteria applied to a specific campaign.  

```c#
let params = [
  AnalyticsParameterMarParameter(ketingTactic, "Remarketing"),
  // ...
]
```

<br />

### ParameterMedium

```c#
string ParameterMedium = "medium"
```  
The advertising or marParameter(keting, cpc, banner, email), push.

Highly recommended (String).  

```c#
let params = [
  AnalyticsParameterMedium : "email",
  // ...
]
```

<br />

### ParameterMethod

```c#
string ParameterMethod = "method"
```  
A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event.

(String).  

```c#
let params = [
  AnalyticsParameterMethod : "google",
  // ...
]
```

<br />

### ParameterNumberOfNights

```c#
string ParameterNumberOfNights = "number_of_nights"
```  
Number of nights staying at hotel (Int).

<br />

```c#
let params = [
  AnalyticsParameterNumberOfNights : 3,
  // ...
]
```

<br />

### ParameterNumberOfPassengers

```c#
string ParameterNumberOfPassengers = "number_of_passengers"
```  
Number of passengers traveling (Int).

<br />

```c#
let params = [
  AnalyticsParameterNumberOfPassengers : 11,
  // ...
]
```

<br />

### ParameterNumberOfRooms

```c#
string ParameterNumberOfRooms =
    "number_of_rooms"
```  
Number of rooms for travel events (Int).

<br />

```c#
let params = [
  AnalyticsParameterNumberOfRooms : 2,
  // ...
]
```

<br />

### ParameterOrigin

```c#
string ParameterOrigin = "origin"
```  
Flight or Travel origin (String).

<br />

```c#
let params = [
  AnalyticsParameterOrigin : "Mountain View, CA",
  // ...
]
```

<br />

### ParameterPaymentType

```c#
string ParameterPaymentType =
    "payment_type"
```  
The chosen method of payment (String).

<br />

```c#
let params = [
  AnalyticsParameterPaymentType : "Visa",
  // ...
]
```

<br />

### ParameterPrice

```c#
string ParameterPrice = "price"
```  
Purchase price (Double).

<br />

```c#
let params = [
  AnalyticsParameterPrice : 1.0,
  AnalyticsParameterCurrency : "USD",  // e.g. $1.00 USD
  // ...
]
```

<br />

### ParameterPriceIsDiscounted

```c#
string ParameterPriceIsDiscounted = "price_is_discounted"
```  
Indicates if an item's price is discounted.

Specify 1 to indicate true and 0 to indicate false (Int).  

```c#
let params = [
  AnalyticsParameterPriceIsDiscounted : 1,
  // ...
]
```

<br />

### ParameterProductID

```c#
string ParameterProductID =
    "product_id"
```  
The ID of a product (String).

<br />

```c#
let params = [
  AnalyticsParameterProductID : "PROD_12345",
  // ...
]
```

<br />

### ParameterProductName

```c#
string ParameterProductName =
    "product_name"
```  
The name of a product (String).

<br />

```c#
let params = [
  AnalyticsParameterProductName : "My Awesome Product",
  // ...
]
```

<br />

### ParameterPromotionID

```c#
string ParameterPromotionID =
    "promotion_id"
```  
The ID of a product promotion (String).

<br />

```c#
let params = [
  AnalyticsParameterPromotionID : "ABC123",
  // ...
]
```

<br />

### ParameterPromotionName

```c#
string ParameterPromotionName =
    "promotion_name"
```  
The name of a product promotion (String).

<br />

```c#
let params = [
  AnalyticsParameterPromotionName : "Summer Sale",
  // ...
]
```

<br />

### ParameterQuantity

```c#
string ParameterQuantity =
    "quantity"
```  
Purchase quantity (Int).

<br />

```c#
let params = [
  AnalyticsParameterQuantity : 1,
  // ...
]
```

<br />

### ParameterScore

```c#
string ParameterScore = "score"
```  
Score in game (Int).

<br />

```c#
let params = [
  AnalyticsParameterScore : 4200,
  // ...
]
```

<br />

### ParameterScreenClass

```c#
string ParameterScreenClass =
    "screen_class"
```  
Current screen class, such as the class name of the UIViewController, logged with screen_view event and added to every event (String).

<br />

```c#
let params = [
  AnalyticsParameterScreenClass : "LoginViewController",
  // ...
]
```

<br />

### ParameterScreenName

```c#
string ParameterScreenName =
    "screen_name"
```  
Current screen name, such as the name of the UIViewController, logged with screen_view event and added to every event (String).

<br />

```c#
let params = [
  AnalyticsParameterScreenName : "LoginView",
  // ...
]
```

<br />

### ParameterSearchTerm

```c#
string ParameterSearchTerm =
    "search_term"
```  
The search string/keywords used (String).

<br />

```c#
let params = [
  AnalyticsParameterSearchTerm : "periodic table",
  // ...
]
```

<br />

### ParameterShipping

```c#
string ParameterShipping =
    "shipping"
```  
Shipping cost associated with a transaction (Double).

<br />

```c#
let params = [
  AnalyticsParameterShipping : 5.99,
  AnalyticsParameterCurrency : "USD",  // e.g. $5.99 USD
  // ...
]
```

<br />

### ParameterShippingTier

```c#
string ParameterShippingTier =
    "shipping_tier"
```  
The shipping tier (e.g.

Ground, Air, Next-day) selected for delivery of the purchased item (String).  

```c#
let params = [
  AnalyticsParameterShippingTier : "Ground",
  // ...
]
```

<br />

### ParameterSource

```c#
string ParameterSource = "source"
```  
The origin of your traffic, such as an Ad network (for example, google) or partner (urban airship).

Identify the advertiser, site, publication, etc. that is sending traffic to your property. Highly recommended (String).  

```c#
let params = [
  AnalyticsParameterSource : "InMobi",
  // ...
]
```

<br />

### ParameterSourcePlatform

```c#
string ParameterSourcePlatform =
    "source_platform"
```  
Source Platform (String).

Used to identify the platform responsible for directing traffic to a given[Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics)property (e.g., a buying platform where budgets, targeting criteria, etc. are set, a platform for managing organic traffic data, etc.).  

```c#
let params = [
  AnalyticsParameterSourcePlatform : "sa360",
  // ...
]
```

<br />

### ParameterStartDate

```c#
string ParameterStartDate =
    "start_date"
```  
The departure date, check-in date or rental start date for the item.

This should be in YYYY-MM-DD format (String).  

```c#
let params = [
  AnalyticsParameterStartDate : "2015-09-14",
  // ...
]
```

<br />

### ParameterSubscription

```c#
string ParameterSubscription =
    "subscription"
```  
Indicates if the purchase is a subscription.

Specify 1 to indicate true and 0 to indicate false (Int).  

```c#
let params = [
  AnalyticsParameterSubscription : 1,
  // ...
]
```

<br />

### ParameterSuccess

```c#
string ParameterSuccess = "success"
```  
The result of an operation.

Specify 1 to indicate success and 0 to indicate failure (Int).  

```c#
let params = [
  AnalyticsParameterSuccess : 1,
  // ...
]
```

<br />

### ParameterTax

```c#
string ParameterTax = "tax"
```  
Tax cost associated with a transaction (Double).

<br />

```c#
let params = [
  AnalyticsParameterTax : 2.43,
  AnalyticsParameterCurrency : "USD",  // e.g. $2.43 USD
  // ...
]
```

<br />

### ParameterTerm

```c#
string ParameterTerm = "term"
```  
If you're manually tagging keyword campaigns, you should use utm_term to specify the keyword (String).

<br />

```c#
let params = [
  AnalyticsParameterTerm : "game",
  // ...
]
```

<br />

### ParameterTransactionID

```c#
string ParameterTransactionID =
    "transaction_id"
```  
The unique identifier of a transaction (String).

<br />

```c#
let params = [
  AnalyticsParameterTransactionID : "T12345",
  // ...
]
```

<br />

### ParameterTravelClass

```c#
string ParameterTravelClass =
    "travel_class"
```  
Travel class (String).

<br />

```c#
let params = [
  AnalyticsParameterTravelClass : "business",
  // ...
]
```

<br />

### ParameterValue

```c#
string ParameterValue = "value"
```  
A context-specific numeric value which is accumulated automatically for each event type.

This is a general purpose parameter that is useful for accumulating a key metric that pertains to an event. Examples include revenue, distance, time and points. Value should be specified as Int or Double. Notes: Values for pre-defined currency-related events (such as`AnalyticsEventAddToCart`) should be supplied using Double and must be accompanied by a`AnalyticsParameterCurrency`parameter. The valid range of accumulated values is \[-9,223,372,036,854.77, 9,223,372,036,854.77\]. Supplying a non-numeric value, omitting the corresponding`AnalyticsParameterCurrency`parameter, or supplying an invalid[currency code](https://goo.gl/qqX3J2)for conversion events will cause that conversion to be omitted from reporting.  

```c#
let params = [
  AnalyticsParameterValue : 3.99,
  AnalyticsParameterCurrency : "USD",  // e.g. $3.99 USD
  // ...
]
```

<br />

### ParameterVirtualCurrencyName

```c#
string ParameterVirtualCurrencyName = "virtual_currency_name"
```  
Name of virtual currency type (String).

<br />

```c#
let params = [
  AnalyticsParameterVirtualCurrencyName : "virtual_currency_name",
  // ...
]
```

<br />