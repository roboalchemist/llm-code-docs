# Source: https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics.md.txt

# Firebase.Analytics.FirebaseAnalytics

## Summary

|                                                                                                                                                                                                                    ### Public static attributes                                                                                                                                                                                                                    ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [EventAdImpression](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaf2085a1d3cb08e9f6db2bcbaab1a26d4)` = "ad_impression"`                                           | `string` Ad Impression event.                                                                                                                                                                                             |
| [EventAddPaymentInfo](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaf528d748fa6ba3697a39e890e20ff5b6)` = "add_payment_info"`                                      | `string` Add Payment Info event.                                                                                                                                                                                          |
| [EventAddShippingInfo](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga38f1b76e1897cf5074c19191ffef0c5f)` = "add_shipping_info"`                                    | `string` Add Shipping Info event.                                                                                                                                                                                         |
| [EventAddToCart](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga780291db2d1875e682a131b0e7822664)` = "add_to_cart"`                                                | `string` E-Commerce Add To Cart event.                                                                                                                                                                                    |
| [EventAddToWishlist](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gab9d7a471d25b43c9701d25877effcccd)` = "add_to_wishlist"`                                        | `string` E-Commerce Add To Wishlist event.                                                                                                                                                                                |
| [EventAppOpen](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaa0116dbd120d6181e3328b726d776312)` = "app_open"`                                                     | `string` App Open event.                                                                                                                                                                                                  |
| [EventBeginCheckout](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga46ed426c3c79cbb8b88b294da64e677d)` = "begin_checkout"`                                         | `string` E-Commerce Begin Checkout event.                                                                                                                                                                                 |
| [EventCampaignDetails](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga13eaeee5a2539f864f07126bce8011f5)` = "campaign_details"`                                     | `string` Campaign Detail event.                                                                                                                                                                                           |
| [EventEarnVirtualCurrency](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gabc9792def19d804d84cb847a837063ab)` = "earn_virtual_currency"`                            | `string` Earn Virtual Currency event.                                                                                                                                                                                     |
| [EventGenerateLead](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gae09776188902a499aee2c2b49c72655b)` = "generate_lead"`                                           | `string` Generate Lead event.                                                                                                                                                                                             |
| [EventInAppPurchase](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga45ba4cdcdad82825840bec002201c1d6)` = "in_app_purchase"`                                        | `string` In-App Purchase event.                                                                                                                                                                                           |
| [EventJoinGroup](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaa7812a4e7c555dc1a3be98b47c77356a)` = "join_group"`                                                 | `string` Join Group event.                                                                                                                                                                                                |
| [EventLevelEnd](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga06d0c36e04e2253ef6efcd1e5087cd52)` = "level_end"`                                                   | `string` Level End event.                                                                                                                                                                                                 |
| [EventLevelStart](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga74f7261b7ce9da5d4eb90421045be246)` = "level_start"`                                               | `string` Level Start event.                                                                                                                                                                                               |
| [EventLevelUp](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gafd7f594b096c2a785ffd791677f6c51d)` = "level_up"`                                                     | `string` Level Up event.                                                                                                                                                                                                  |
| [EventLogin](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga4777f25dec0d444ce981565aac37a5d9)` = "login"`                                                          | `string` Login event.                                                                                                                                                                                                     |
| [EventPostScore](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gae6c7bae26bf168725550d92fde85686b)` = "post_score"`                                                 | `string` Post Score event.                                                                                                                                                                                                |
| [EventPurchase](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga28a024454ff4a4be16fd705a986135e1)` = "purchase"`                                                    | `string` E-Commerce Purchase event.                                                                                                                                                                                       |
| [EventRefund](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gac2ad39117f0d330ebb8f665a13fb0f9b)` = "refund"`                                                        | `string` E-Commerce Refund event.                                                                                                                                                                                         |
| [EventRemoveFromCart](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga7332a67a09a87fd5213053dd81781208)` = "remove_from_cart"`                                      | `string` E-Commerce Remove from Cart event.                                                                                                                                                                               |
| [EventScreenView](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaa0dac3af8c39a1002c07e0a65727c4dc)` = "screen_view"`                                               | `string` Screen View event.                                                                                                                                                                                               |
| [EventSearch](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gadb7a4258a2712c9f28d60b1579421d56)` = "search"`                                                        | `string` Search event.                                                                                                                                                                                                    |
| [EventSelectContent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga53ea47346994ec8c2c13ea8a4396e78e)` = "select_content"`                                         | `string` Select Content event.                                                                                                                                                                                            |
| [EventSelectItem](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gae1ded6912cc85dd90e566f3c698f67dd)` = "select_item"`                                               | `string` Select Item event.                                                                                                                                                                                               |
| [EventSelectPromotion](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gae7f7055b6ef082137e6860ecb9d4b6d7)` = "select_promotion"`                                     | `string` Select promotion event.                                                                                                                                                                                          |
| [EventShare](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaa5873d3d44141caaebb64236effe4260)` = "share"`                                                          | `string` Share event.                                                                                                                                                                                                     |
| [EventSignUp](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga02eab2ba8ebebbdb1e8b78fdfb289a2a)` = "sign_up"`                                                       | `string` Sign Up event.                                                                                                                                                                                                   |
| [EventSpendVirtualCurrency](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gad7ad7c48cb9e4cddefced2165c5df7d3)` = "spend_virtual_currency"`                          | `string` Spend Virtual Currency event.                                                                                                                                                                                    |
| [EventTutorialBegin](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaae32163dc826f78f45c3dbe687d5b495)` = "tutorial_begin"`                                         | `string` Tutorial Begin event.                                                                                                                                                                                            |
| [EventTutorialComplete](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gabf4a2a738c35d247c2833a6106b542d5)` = "tutorial_complete"`                                   | `string` Tutorial End event.                                                                                                                                                                                              |
| [EventUnlockAchievement](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga3bf9935c3379ea13dc5bdf1f5992da08)` = "unlock_achievement"`                                 | `string` Unlock Achievement event.                                                                                                                                                                                        |
| [EventViewCart](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga85e2fdaae405a8d2962195d00f72c9ef)` = "view_cart"`                                                   | `string` E-commerce View Cart event.                                                                                                                                                                                      |
| [EventViewItem](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1ga96f6867734efe261a80c669d260726a2)` = "view_item"`                                                   | `string` View Item event.                                                                                                                                                                                                 |
| [EventViewItemList](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gac2672eae72ea0c741d228c39f676ae20)` = "view_item_list"`                                          | `string` View Item List event.                                                                                                                                                                                            |
| [EventViewPromotion](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaab70fd81164d1a394ee23923ff4cf7de)` = "view_promotion"`                                         | `string` View Promotion event.                                                                                                                                                                                            |
| [EventViewSearchResults](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__event__names_1gaf5304788628f1096bf6818c275ca1daa)` = "view_search_results"`                                | `string` View Search Results event.                                                                                                                                                                                       |
| [ParameterAchievementID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga27e8cb3cb48a1992a7c147755db64fbd)` = "achievement_id"`                                 | `string` Game achievement ID (String).                                                                                                                                                                                    |
| [ParameterAdFormat](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gad1ee55f39670de3db76681e55c37d850)` = "ad_format"`                                           | `string` The ad format (e.g.                                                                                                                                                                                              |
| [ParameterAdNetworkClickID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gaadb818f4cef52b43d84e403624eb34ae)` = "aclid"`                                       | `string` Ad Network Click ID (String).                                                                                                                                                                                    |
| [ParameterAdPlatform](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga737addbe77b5f92387a03b2a15bb59b0)` = "ad_platform"`                                       | `string` The ad platform (e.g.                                                                                                                                                                                            |
| [ParameterAdSource](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga6e3aaaed5e77868b5857b70f0457b5da)` = "ad_source"`                                           | `string` The ad source (e.g.                                                                                                                                                                                              |
| [ParameterAdUnitName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga935624c4e7bee91aa59b74bf8a8ac739)` = "ad_unit_name"`                                      | `string` The ad unit name (e.g.                                                                                                                                                                                           |
| [ParameterAffiliation](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga8308d0256fa1fa5ef5c7140dd10c33be)` = "affiliation"`                                      | `string` A product affiliation to designate a supplying company or brick and mortar store location (String).                                                                                                              |
| [ParameterCP1](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga378d0bb3d9ff4261acc5bb9c57bef762)` = "cp1"`                                                      | `string` Campaign custom parameter (String).                                                                                                                                                                              |
| [ParameterCampaign](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gac58c8d2e923a05b764e4218c8781f0ff)` = "campaign"`                                            | `string` The individual campaign name, slogan, promo code, etc.                                                                                                                                                           |
| [ParameterCampaignID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga13dac1f1a100f479a2a01c44ef25715c)` = "campaign_id"`                                       | `string` Campaign ID (String).                                                                                                                                                                                            |
| [ParameterCharacter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gacf50a02bceb87a582c6fc55c6c0717f2)` = "character"`                                          | `string` Character used in game (String).                                                                                                                                                                                 |
| [ParameterContent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga5f380ff487f66edc790656762ef6d974)` = "content"`                                              | `string` Campaign content (String).                                                                                                                                                                                       |
| [ParameterContentType](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga39a37092cd3fce53ba6ffa53289e1fe9)` = "content_type"`                                     | `string` Type of content selected (String).                                                                                                                                                                               |
| [ParameterCoupon](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga9413a4d3a4fc4fe68c340187abdb751e)` = "coupon"`                                                | `string` Coupon code used for a purchase (String).                                                                                                                                                                        |
| [ParameterCreativeFormat](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga04bd1800c6d7ba7d7ccde63c012bc22e)` = "creative_format"`                               | `string` Creative Format (String).                                                                                                                                                                                        |
| [ParameterCreativeName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga48f69dc8eb17ec5d5dfcc0f0708168d3)` = "creative_name"`                                   | `string` The name of a creative used in a promotional spot (String).                                                                                                                                                      |
| [ParameterCreativeSlot](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga3282cf4abd93c1d65e4daef1a957cff7)` = "creative_slot"`                                   | `string` The name of a creative slot (String).                                                                                                                                                                            |
| [ParameterCurrency](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gae46e9b16a5145af4127990ee02cf2c74)` = "currency"`                                            | `string` Currency of the purchase or items associated with the event, in 3-letter[ISO_4217](http://en.wikipedia.org/wiki/ISO_4217#Active_codes)format (String).                                                           |
| [ParameterDestination](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga67347716dc73e56171dbebbba51febd4)` = "destination"`                                      | `string` Flight or Travel destination (String).                                                                                                                                                                           |
| [ParameterDiscount](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga60dcf4f898f38c73ef988c3b83585355)` = "discount"`                                            | `string` Monetary value of discount associated with a purchase (Double).                                                                                                                                                  |
| [ParameterEndDate](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga3407b387b96a305eca0efd8010dc45bf)` = "end_date"`                                             | `string` The arrival date, check-out date or rental end date for the item.                                                                                                                                                |
| [ParameterExtendSession](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga9e561362e49617a81b330e120dc382ce)` = "extend_session"`                                 | `string` Indicates that the associated event should either extend the current session or start a new session if no session was active when the event was logged.                                                          |
| [ParameterFlightNumber](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gabf078dc5a36b3f19ba9648d27a88a533)` = "flight_number"`                                   | `string` Flight number for travel events (String).                                                                                                                                                                        |
| [ParameterFreeTrial](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga268fd542d2a8201c999fe159ddba6911)` = "free_trial"`                                         | `string` Indicates if the user is on a free trial of a subscription.                                                                                                                                                      |
| [ParameterGroupID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gab0c6c1ae9c737f0a0b4e71099055b234)` = "group_id"`                                             | `string` Group/clan/guild ID (String).                                                                                                                                                                                    |
| [ParameterIndex](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gabe7af91955e082800099f0b9fb93d68e)` = "index"`                                                  | `string` The index of the item in a list (Int).                                                                                                                                                                           |
| [ParameterItemBrand](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga2cb352537be257df46cfc3af1f212c71)` = "item_brand"`                                         | `string` Item brand (String).                                                                                                                                                                                             |
| [ParameterItemCategory](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga6aabf1eea78e6e0b3aa558e2a98667fb)` = "item_category"`                                   | `string` Item category (context-specific) (String).                                                                                                                                                                       |
| [ParameterItemCategory2](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gab69949be997cdc98477844b7cbc863f9)` = "item_category2"`                                 | `string` Item Category (context-specific) (String).                                                                                                                                                                       |
| [ParameterItemCategory3](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gae3ca33c480239ee44c0566f5d636e70e)` = "item_category3"`                                 | `string` Item Category (context-specific) (String).                                                                                                                                                                       |
| [ParameterItemCategory4](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gacdedf0e9e5be48c02bc5de409fd46cbc)` = "item_category4"`                                 | `string` Item Category (context-specific) (String).                                                                                                                                                                       |
| [ParameterItemCategory5](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga223d3b516c655174613807a44ed84283)` = "item_category5"`                                 | `string` Item Category (context-specific) (String).                                                                                                                                                                       |
| [ParameterItemID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga27f2b08585ae5a389fad573a46e29b11)` = "item_id"`                                               | `string` Item ID (context-specific) (String).                                                                                                                                                                             |
| [ParameterItemListID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga69eb93c8a4023aa8c4011677e68f0928)` = "item_list_id"`                                      | `string` The ID of the list in which the item was presented to the user (String).                                                                                                                                         |
| [ParameterItemListName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga2782e3f15edab0abd297393751da2659)` = "item_list_name"`                                  | `string` The name of the list in which the item was presented to the user (String).                                                                                                                                       |
| [ParameterItemName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga52aa7d69ba549c8c5bd83aa04f980f94)` = "item_name"`                                           | `string` Item Name (context-specific) (String).                                                                                                                                                                           |
| [ParameterItemVariant](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga20df71ec9c0a472accdd66319fa5bfe5)` = "item_variant"`                                     | `string` Item variant (String).                                                                                                                                                                                           |
| [ParameterItems](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga2784d1f012538493c6bb0829b986ae9a)` = "items"`                                                  | `string` The list of items involved in the transaction expressed as`[[String: Any]]`.                                                                                                                                     |
| [ParameterLevel](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga3e747288c7aca047097073062398d5df)` = "level"`                                                  | `string` Level in game (Int).                                                                                                                                                                                             |
| [ParameterLevelName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga748a5109b769d62cacfcb274facf27db)` = "level_name"`                                         | `string` The name of a level in a game (String).                                                                                                                                                                          |
| [ParameterLocation](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga49d8df43f333dbb464eb8be9bca18bd4)` = "location"`                                            | `string` Location (String).                                                                                                                                                                                               |
| [ParameterLocationID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gac24c5a521cf32506bc1e58c952e89b71)` = "location_id"`                                       | `string` The location associated with the event.                                                                                                                                                                          |
| [ParameterMarketingTactic](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga8d19f9a0a68d3cf102b93b0e61e8d64b)` = "marketing_tactic"`                             | `string` Marketing Tactic (String).                                                                                                                                                                                       |
| [ParameterMedium](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gad75f5232098329cc85e68c0ca3425b02)` = "medium"`                                                | `string` The advertising or marParameter(keting, cpc, banner, email), push.                                                                                                                                               |
| [ParameterMethod](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga7368101eb1614cb80ccf885cff34012b)` = "method"`                                                | `string` A particular approach used in an operation; for example, "facebook" or "email" in the context of a sign_up or login event.                                                                                       |
| [ParameterNumberOfNights](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga9a79b5a4b19b5c897a5afad6a6db0411)` = "number_of_nights"`                              | `string` Number of nights staying at hotel (Int).                                                                                                                                                                         |
| [ParameterNumberOfPassengers](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gae8f3f74b880f9e5aa67c9523ac3bc889)` = "number_of_passengers"`                      | `string` Number of passengers traveling (Int).                                                                                                                                                                            |
| [ParameterNumberOfRooms](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gac4871d9ec8656a192e4409cc5e9f197a)` = "number_of_rooms"`                                | `string` Number of rooms for travel events (Int).                                                                                                                                                                         |
| [ParameterOrigin](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga643498f873a73095ec48541b55caf9d1)` = "origin"`                                                | `string` Flight or Travel origin (String).                                                                                                                                                                                |
| [ParameterPaymentType](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga425351ec1386e9e84db6e631a5fed28e)` = "payment_type"`                                     | `string` The chosen method of payment (String).                                                                                                                                                                           |
| [ParameterPrice](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga526644fcd239ef7fc8be6b661088d08c)` = "price"`                                                  | `string` Purchase price (Double).                                                                                                                                                                                         |
| [ParameterPriceIsDiscounted](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gab12d820e5ca5df29c9ae9e469991f08b)` = "price_is_discounted"`                        | `string` Indicates if an item's price is discounted.                                                                                                                                                                      |
| [ParameterProductID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gaf2b38edb5bcb2b7fcfc7eb0fa3bfca5d)` = "product_id"`                                         | `string` The ID of a product (String).                                                                                                                                                                                    |
| [ParameterProductName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga83821382a7842647ba26d65cd14f91ef)` = "product_name"`                                     | `string` The name of a product (String).                                                                                                                                                                                  |
| [ParameterPromotionID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga3efc940851d03f70fec63b201f30fc20)` = "promotion_id"`                                     | `string` The ID of a product promotion (String).                                                                                                                                                                          |
| [ParameterPromotionName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga80cc63dd506975317c0cbd5fa2a82f35)` = "promotion_name"`                                 | `string` The name of a product promotion (String).                                                                                                                                                                        |
| [ParameterQuantity](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga83a1ca15d25d99aabe755d413e1b7d83)` = "quantity"`                                            | `string` Purchase quantity (Int).                                                                                                                                                                                         |
| [ParameterScore](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gac69aa0a217496876f0e5a9aedf98b853)` = "score"`                                                  | `string` Score in game (Int).                                                                                                                                                                                             |
| [ParameterScreenClass](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga99bbe1ef7dad9befa36fab7551aa074b)` = "screen_class"`                                     | `string` Current screen class, such as the class name of the UIViewController, logged with screen_view event and added to every event (String).                                                                           |
| [ParameterScreenName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga0b76faae50343c0c636059a999badbf3)` = "screen_name"`                                       | `string` Current screen name, such as the name of the UIViewController, logged with screen_view event and added to every event (String).                                                                                  |
| [ParameterSearchTerm](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gabb8d52a65f2846418d75a17fe8c3eb6a)` = "search_term"`                                       | `string` The search string/keywords used (String).                                                                                                                                                                        |
| [ParameterShipping](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gafc75615508fc899e136c27721725bb53)` = "shipping"`                                            | `string` Shipping cost associated with a transaction (Double).                                                                                                                                                            |
| [ParameterShippingTier](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga7c18898fd2500cf4ca14ed6e7bd837eb)` = "shipping_tier"`                                   | `string` The shipping tier (e.g.                                                                                                                                                                                          |
| [ParameterSource](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga70b1519770f25692f7602d39785018d9)` = "source"`                                                | `string` The origin of your traffic, such as an Ad network (for example, google) or partner (urban airship).                                                                                                              |
| [ParameterSourcePlatform](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga695127fdfc935c8b86340c19e5aeb70e)` = "source_platform"`                               | `string` Source Platform (String).                                                                                                                                                                                        |
| [ParameterStartDate](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gabbdcdd99c8cda186d418a2390160196d)` = "start_date"`                                         | `string` The departure date, check-in date or rental start date for the item.                                                                                                                                             |
| [ParameterSubscription](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga7c50342f527ce01a8146c67834b35d4d)` = "subscription"`                                    | `string` Indicates if the purchase is a subscription.                                                                                                                                                                     |
| [ParameterSuccess](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gaa4eed7e18b679bbc0e2101533b9b18ce)` = "success"`                                              | `string` The result of an operation.                                                                                                                                                                                      |
| [ParameterTax](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga3b635b513c5ff886d4276607f01879dd)` = "tax"`                                                      | `string` Tax cost associated with a transaction (Double).                                                                                                                                                                 |
| [ParameterTerm](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga1404b8d46c6a333ab46c5e01332694ef)` = "term"`                                                    | `string` If you're manually tagging keyword campaigns, you should use utm_term to specify the keyword (String).                                                                                                           |
| [ParameterTransactionID](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1gaffb421d1795f302632bb0b3369632acf)` = "transaction_id"`                                 | `string` The unique identifier of a transaction (String).                                                                                                                                                                 |
| [ParameterTravelClass](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga393eb888a19ee130d69c60912da8266f)` = "travel_class"`                                     | `string` Travel class (String).                                                                                                                                                                                           |
| [ParameterValue](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga9c83240ada0e8620e326bbbee48f6855)` = "value"`                                                  | `string` A context-specific numeric value which is accumulated automatically for each event type.                                                                                                                         |
| [ParameterVirtualCurrencyName](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__parameter__names_1ga87a99fdfc2233237c854c42855dd2550)` = "virtual_currency_name"`                    | `string` Name of virtual currency type (String).                                                                                                                                                                          |
| [UserPropertyAllowAdPersonalizationSignals](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__user__property__names_1gae84a687de309c83dabf27ca65dd18b0e)` = "allow_personalized_ads"` | `string` Indicates whether events logged by Google[Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics)can be used to personalize ads for the user. |
| [UserPropertySignUpMethod](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#group__user__property__names_1ga58850cee496acc02fbf1cc788b45df32)` = "sign_up_method"`                          | `string` The method used to sign in.                                                                                                                                                                                      |

|                                                                                                                                                                                                                                                                                                                                                ### Public static functions                                                                                                                                                                                                                                                                                                                                                 ||
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [GetAnalyticsInstanceIdAsync](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a20cef56e55293abf0bfd4b545caec4ef)`()`                                                                                                                                                                                                                                                                                                                                                                                  | `System.Threading.Tasks.Task< string >` Get the instance ID from the analytics service.                           |
| [GetSessionIdAsync](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a7e232a75c51db971b935f0d66ecd4e1c)`()`                                                                                                                                                                                                                                                                                                                                                                                            | `System.Threading.Tasks.Task< long >` Asynchronously retrieves the identifier of the current app session.         |
| [InitiateOnDeviceConversionMeasurementWithEmailAddress](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1aabd79448352789908d077d4f8af3af30)`(string emailAddress)`                                                                                                                                                                                                                                                                                                                                     | `void` Initiates on-device conversion measurement given a user email address on iOS and tvOS (no-op on Android).  |
| [InitiateOnDeviceConversionMeasurementWithHashedEmailAddress](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a76a2a2bb4bda47385c0b296d8bf2aed5)`(byte[] hashedEmailAddress)`                                                                                                                                                                                                                                                                                                                         | `void` Initiates on-device conversion measurement given a sha256-hashed user email address.                       |
| [InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1ad31660d9ef79ddcdc925ef8ca99e2da5)`(byte[] hashedPhoneNumber)`                                                                                                                                                                                                                                                                                                                           | `void` Initiates on-device conversion measurement given a sha256-hashed phone number in E.164 format.             |
| [InitiateOnDeviceConversionMeasurementWithPhoneNumber](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a0c984fbd75c1abc3a4bc9a35817efd1f)`(string phoneNumber)`                                                                                                                                                                                                                                                                                                                                       | `void` Initiates on-device conversion measurement given a phone number in E.164 format on iOS (no-op on Android). |
| [LogEvent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a0a56fc71e4138209ff3c81b4716d8faf)`(string name, string parameterName, string parameterValue)`                                                                                                                                                                                                                                                                                                                                             | `void` Log an event with one string parameter.                                                                    |
| [LogEvent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a3561def7e017f1fed2c9c747eff781e5)`(string name, string parameterName, double parameterValue)`                                                                                                                                                                                                                                                                                                                                             | `void` Log an event with one float parameter.                                                                     |
| [LogEvent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1ad9ade4984381301a87912aaba4b32680)`(string name, string parameterName, long parameterValue)`                                                                                                                                                                                                                                                                                                                                               | `void` Log an event with one 64-bit integer parameter.                                                            |
| [LogEvent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a4cbf4e24bb4b90bc7c123c47713a02ab)`(string name, string parameterName, int parameterValue)`                                                                                                                                                                                                                                                                                                                                                | `void` Log an event with one integer parameter (stored as a 64-bit integer).                                      |
| [LogEvent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a8599e5f2ac3b75c93e1fa4490236b555)`(string name)`                                                                                                                                                                                                                                                                                                                                                                                          | `void` Log an event with no parameters.                                                                           |
| [LogEvent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1ab1d49ef22ab1be81f616146696bf49e5)`(string name, params `[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)`[] parameters)`                                                                                                                                                                                                                       | `void` Log an event with associated parameters.                                                                   |
| [LogEvent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1afc449e973887b91f651532fb266b7cef)`(string name, IEnumerable< `[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)` > parameters)`                                                                                                                                                                                                                 | `void` Log an event with associated parameters.                                                                   |
| [ResetAnalyticsData](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a4c6ea81854fc1cf332c1054c7a7b87c0)`()`                                                                                                                                                                                                                                                                                                                                                                                           | `void` Clears all analytics data for this app from the device and resets the app instance id.                     |
| [SetAnalyticsCollectionEnabled](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a140e587eacd12dd0c30d145053688a29)`(bool enabled)`                                                                                                                                                                                                                                                                                                                                                                    | `void` Sets whether analytics collection is enabled for this app on this device.                                  |
| [SetConsent](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a01a3b193af036f0f00e1561bbf0d5f83)`(System.Collections.Generic.IDictionary< `[ConsentType](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics_1a9bbaa83c33ea86aec075f5f666fa5935)`, `[ConsentStatus](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics_1ab87c55ec1a8727fd7a14850f2ad86e8b)` > consentSettings)` | `void` Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device.     |
| [SetDefaultEventParameters](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1accd5f69a2ea73521b9be85226ada4dc0)`(params `[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)`[] parameters)`                                                                                                                                                                                                                   | `void` Adds parameters that will be set on every event logged from the SDK.                                       |
| [SetDefaultEventParameters](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1aa2155908ff2d54cfd5fac79dec3a07e7)`(IEnumerable< `[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)` > parameters)`                                                                                                                                                                                                             | `void` Adds parameters that will be set on every event logged from the SDK.                                       |
| [SetSessionTimeoutDuration](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a5be7037651745c1dec7774080927d335)`(System.TimeSpan timeSpan)`                                                                                                                                                                                                                                                                                                                                                            | `void` Sets the duration of inactivity that terminates the current session.                                       |
| [SetUserId](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1adfddde01572b799475c679786201cd54)`(string userId)`                                                                                                                                                                                                                                                                                                                                                                                       | `void` Sets the user ID property.                                                                                 |
| [SetUserProperty](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics_1a20ff41eabdec58b25ea76fd2b6dcfbbe)`(string name, string property)`                                                                                                                                                                                                                                                                                                                                                                  | `void` Set a user property to the given value.                                                                    |

## Public static attributes

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

### UserPropertyAllowAdPersonalizationSignals

```c#
string UserPropertyAllowAdPersonalizationSignals = "allow_personalized_ads"
```  
Indicates whether events logged by Google[Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics)can be used to personalize ads for the user.

Set to "YES" to enable, or "NO" to disable. Default is enabled. See the[documentation](https://firebase.google.com/support/guides/disable-analytics)for more details and information about related settings.

<br />

```c#
Analytics.setUserProperty("NO", forName: AnalyticsUserPropertyAllowAdPersonalizationSignals)
```

<br />

### UserPropertySignUpMethod

```c#
string UserPropertySignUpMethod = "sign_up_method"
```  
The method used to sign in.

For example, "google", "facebook" or "twitter".

## Public static functions

### GetAnalyticsInstanceIdAsync

```c#
System.Threading.Tasks.Task< string > GetAnalyticsInstanceIdAsync()
```  
Get the instance ID from the analytics service.

<br />

|                                                                               Details                                                                               ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A Task with the[Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics)instance ID. |

### GetSessionIdAsync

```c#
System.Threading.Tasks.Task< long > GetSessionIdAsync()
```  
Asynchronously retrieves the identifier of the current app session.

The session ID retrieval could fail due to[Analytics](https://firebase.google.com/docs/reference/unity/namespace/firebase/analytics#namespace_firebase_1_1_analytics)collection disabled, or if the app session was expired.

<br />

|                               Details                               ||
|-------------|--------------------------------------------------------|
| **Returns** | A Task with the identifier of the current app session. |

### InitiateOnDeviceConversionMeasurementWithEmailAddress

```c#
void InitiateOnDeviceConversionMeasurementWithEmailAddress(
  string emailAddress
)
```  
Initiates on-device conversion measurement given a user email address on iOS and tvOS (no-op on Android).

On iOS and tvOS, this method requires the dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise the invocation results in a no-op.

<br />

|                                                                                                                             Details                                                                                                                             ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------|------------------------------------------------------------------------------------------------------| | `emailAddress` | User email address. Include a domain name for all email addresses (e.g. gmail.com or hotmail.co.jp). | |

### InitiateOnDeviceConversionMeasurementWithHashedEmailAddress

```c#
void InitiateOnDeviceConversionMeasurementWithHashedEmailAddress(
  byte[] hashedEmailAddress
)
```  
Initiates on-device conversion measurement given a sha256-hashed user email address.

Requires dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise it is a no-op.

<br />

|                                                                                                                                                                                                                   Details                                                                                                                                                                                                                   ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `hashedEmailAddress` | User email address as a UTF8-encoded string normalized and hashed according to the instructions at<https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3>. | |

### InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber

```c#
void InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber(
  byte[] hashedPhoneNumber
)
```  
Initiates on-device conversion measurement given a sha256-hashed phone number in E.164 format.

Requires dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise it is a no-op.

<br />

|                                                                                                                                                                                                               Details                                                                                                                                                                                                               ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `hashedPhoneNumber` | UTF8-encoded user phone number in E.164 format and then hashed according to the instructions at<https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3>. | |

### InitiateOnDeviceConversionMeasurementWithPhoneNumber

```c#
void InitiateOnDeviceConversionMeasurementWithPhoneNumber(
  string phoneNumber
)
```  
Initiates on-device conversion measurement given a phone number in E.164 format on iOS (no-op on Android).

On iOS, requires dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise it is a no-op.

<br />

|                                                                                                                                                                                                                             Details                                                                                                                                                                                                                             ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `phoneNumber` | User phone number. Must be in E.164 format, which means it must be limited to a maximum of 15 digits and must include a plus sign (+) prefix and country code with no dashes, parentheses, or spaces. | |

### LogEvent

```c#
void LogEvent(
  string name,
  string parameterName,
  string parameterValue
)
```  
Log an event with one string parameter.

**See also:**LogEvent(string, Parameter\[\])

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`           | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See the FirebaseAnalytics.Event properties for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameterName`  | Name of the parameter to log. For more information, see[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter).                                                                                                                                                                                                                                                            | | `parameterValue` | Value of the parameter to log.                                                                                                                                                                                                                                                                                                                                                                                                                                 | |

### LogEvent

```c#
void LogEvent(
  string name,
  string parameterName,
  double parameterValue
)
```  
Log an event with one float parameter.

**See also:**LogEvent(string, Parameter\[\])

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`           | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See the FirebaseAnalytics.Event properties for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameterName`  | Name of the parameter to log. For more information, see[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter).                                                                                                                                                                                                                                                            | | `parameterValue` | Value of the parameter to log.                                                                                                                                                                                                                                                                                                                                                                                                                                 | |

### LogEvent

```c#
void LogEvent(
  string name,
  string parameterName,
  long parameterValue
)
```  
Log an event with one 64-bit integer parameter.

**See also:**LogEvent(string, Parameter\[\])

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`           | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See the FirebaseAnalytics.Event properties for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameterName`  | Name of the parameter to log. For more information, see[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter).                                                                                                                                                                                                                                                            | | `parameterValue` | Value of the parameter to log.                                                                                                                                                                                                                                                                                                                                                                                                                                 | |

### LogEvent

```c#
void LogEvent(
  string name,
  string parameterName,
  int parameterValue
)
```  
Log an event with one integer parameter (stored as a 64-bit integer).

**See also:**LogEvent(string, Parameter\[\])

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`           | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See the FirebaseAnalytics.Event properties for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameterName`  | Name of the parameter to log. For more information, see[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter).                                                                                                                                                                                                                                                            | | `parameterValue` | Value of the parameter to log.                                                                                                                                                                                                                                                                                                                                                                                                                                 | |

### LogEvent

```c#
void LogEvent(
  string name
)
```  
Log an event with no parameters.

**See also:**LogEvent(string, Parameter\[\])

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See the FirebaseAnalytics.Event properties for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | |

### LogEvent

```c#
void LogEvent(
  string name,
  params Parameter[] parameters
)
```  
Log an event with associated parameters.

An Event is an important occurrence in your app that you want to measure. You can report up to 500 different types of events per app and you can associate up to 25 unique parameters with each Event type.

Some common events are in the reference guide via the FirebaseAnalytics.Event\* constants, but you may also choose to specify custom event types that are associated with your specific app.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`       | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See the FirebaseAnalytics.Event properties for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameters` | A parameter array of[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)instances.                                                                                                                                                                                                                                                                                      | |

### LogEvent

```c#
void LogEvent(
  string name,
  IEnumerable< Parameter > parameters
)
```  
Log an event with associated parameters.

An Event is an important occurrence in your app that you want to measure. You can report up to 500 different types of events per app and you can associate up to 25 unique parameters with each Event type.

Some common events are in the reference guide via the FirebaseAnalytics.Event\* constants, but you may also choose to specify custom event types that are associated with your specific app.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`       | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See the FirebaseAnalytics.Event properties for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameters` | An enumerable list of[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)instances.                                                                                                                                                                                                                                                                                     | |

### ResetAnalyticsData

```c#
void ResetAnalyticsData()
```  
Clears all analytics data for this app from the device and resets the app instance id.  

### SetAnalyticsCollectionEnabled

```c#
void SetAnalyticsCollectionEnabled(
  bool enabled
)
```  
Sets whether analytics collection is enabled for this app on this device.

This setting is persisted across app sessions. By default it is enabled.

<br />

|                                                                          Details                                                                          ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |-----------|--------------------------------------------------------| | `enabled` | true to enable analytics collection, false to disable. | |

### SetConsent

```c#
void SetConsent(
  System.Collections.Generic.IDictionary< ConsentType, ConsentStatus > consentSettings
)
```  
Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device.

Use the consent map to specify individual consent type values. Settings are persisted across app sessions. By default consent types are set to "granted".  

### SetDefaultEventParameters

```c#
void SetDefaultEventParameters(
  params Parameter[] parameters
)
```  
Adds parameters that will be set on every event logged from the SDK.

Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters bundle will be added to the map of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.

<br />

|                                                                                                                                                                                                Details                                                                                                                                                                                                ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `parameters` | A parameter array of[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)instances. | |

### SetDefaultEventParameters

```c#
void SetDefaultEventParameters(
  IEnumerable< Parameter > parameters
)
```  
Adds parameters that will be set on every event logged from the SDK.

Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters bundle will be added to the map of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.

<br />

|                                                                                                                                                                                                 Details                                                                                                                                                                                                 ||
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `parameters` | An enumerable list of[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter)instances. | |

### SetSessionTimeoutDuration

```c#
void SetSessionTimeoutDuration(
  System.TimeSpan timeSpan
)
```  
Sets the duration of inactivity that terminates the current session.

<br />

| **Note:**The default value is 30 minutes.

<br />

|                                                                                    Details                                                                                    ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------------------------| | `timeSpan` | The duration of inactivity that terminates the current session. | |

### SetUserId

```c#
void SetUserId(
  string userId
)
```  
Sets the user ID property.

This feature must be used in accordance with[Google's Privacy Policy](https://www.google.com/policies/privacy)

<br />

|                                                                                                                                                                                                   Details                                                                                                                                                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `userId` | The user ID associated with the user of this app on this device. The user ID must be non-empty and no more than 256 characters long. Setting userId to null removes the user ID. | |

### SetUserProperty

```c#
void SetUserProperty(
  string name,
  string property
)
```  
Set a user property to the given value.

Properties associated with a user allow a developer to segment users into groups that are useful to their application. Up to 25 properties can be associated with a user.

Suggested property names are listed[Analytics User Properties](https://firebase.google.com/docs/reference/unity/group/user-property-names#group__user__property__names)(user_property_names.h) but you're not limited to this set. For example, the "gamertype" property could be used to store the type of player where a range of values could be "casual", "mid_core", or "core".

<br />

|                                                                                                                                                                                                                                                                                                                                                    Details                                                                                                                                                                                                                                                                                                                                                     ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `name`     | Name of the user property to set. This must be a combination of letters and digits (matching the regular expression \[a-zA-Z0-9\] between 1 and 40 characters long starting with a letter \[a-zA-Z\] character. | | `property` | Value to set the user property to. Set this argument to NULL or nullptr to remove the user property. The value can be between 1 to 100 characters long.                                                         | |