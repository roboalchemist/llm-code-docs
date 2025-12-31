# Source: https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics.md.txt

# Analytics | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics).
- Analytics

The Firebase Analytics service interface.

Do not call this constructor directly. Instead, use
[`firebase.analytics()`](https://firebase.google.com/docs/reference/js/v8/firebase.analytics).

## Index

### Properties

- [app](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics#app)

### Methods

- [logEvent](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics#logevent)
- [setAnalyticsCollectionEnabled](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics#setanalyticscollectionenabled)
- [setCurrentScreen](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics#setcurrentscreen)
- [setUserId](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics#setuserid)
- [setUserProperties](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics#setuserproperties)

## Properties

### app

app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)  
The [app](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) associated with the `Analytics` service
instance.

example
:

        var app = analytics.app;


## Methods

### logEvent

- logEvent ( eventName : "add_payment_info" , eventParams ? : { coupon ?: EventParams \[ "coupon" \] ; currency ?: EventParams \[ "currency" \] ; items ?: EventParams \[ "items" \] ; payment_type ?: EventParams \[ "payment_type" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "add_payment_info"

  -

    ##### Optional eventParams: { coupon?: EventParams\["coupon"\]; currency?: EventParams\["currency"\]; items?: EventParams\["items"\]; payment_type?: EventParams\["payment_type"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional coupon?: EventParams\["coupon"\]

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional payment_type?: EventParams\["payment_type"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "add_shipping_info" , eventParams ? : { coupon ?: EventParams \[ "coupon" \] ; currency ?: EventParams \[ "currency" \] ; items ?: EventParams \[ "items" \] ; shipping_tier ?: EventParams \[ "shipping_tier" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "add_shipping_info"

  -

    ##### Optional eventParams: { coupon?: EventParams\["coupon"\]; currency?: EventParams\["currency"\]; items?: EventParams\["items"\]; shipping_tier?: EventParams\["shipping_tier"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional coupon?: EventParams\["coupon"\]

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional shipping_tier?: EventParams\["shipping_tier"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "add_to_cart" \| "add_to_wishlist" \| "remove_from_cart" , eventParams ? : { currency ?: EventParams \[ "currency" \] ; items ?: EventParams \[ "items" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "add_to_cart" \| "add_to_wishlist" \| "remove_from_cart"

  -

    ##### Optional eventParams: { currency?: EventParams\["currency"\]; items?: EventParams\["items"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "begin_checkout" , eventParams ? : { coupon ?: EventParams \[ "coupon" \] ; currency ?: EventParams \[ "currency" \] ; items ?: EventParams \[ "items" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "begin_checkout"

  -

    ##### Optional eventParams: { coupon?: EventParams\["coupon"\]; currency?: EventParams\["currency"\]; items?: EventParams\["items"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional coupon?: EventParams\["coupon"\]

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "checkout_progress" , eventParams ? : { checkout_option ?: EventParams \[ "checkout_option" \] ; checkout_step ?: EventParams \[ "checkout_step" \] ; coupon ?: EventParams \[ "coupon" \] ; currency ?: EventParams \[ "currency" \] ; items ?: EventParams \[ "items" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "checkout_progress"

  -

    ##### Optional eventParams: { checkout_option?: EventParams\["checkout_option"\]; checkout_step?: EventParams\["checkout_step"\]; coupon?: EventParams\["coupon"\]; currency?: EventParams\["currency"\]; items?: EventParams\["items"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional checkout_option?: EventParams\["checkout_option"\]

    -

      ##### Optional checkout_step?: EventParams\["checkout_step"\]

    -

      ##### Optional coupon?: EventParams\["coupon"\]

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "exception" , eventParams ? : { description ?: EventParams \[ "description" \] ; fatal ?: EventParams \[ "fatal" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  See
  [Measure exceptions](https://developers.google.com/analytics/devguides/collection/ga4/exceptions).

  #### Parameters

  -

    ##### eventName: "exception"

  -

    ##### Optional eventParams: { description?: EventParams\["description"\]; fatal?: EventParams\["fatal"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional description?: EventParams\["description"\]

    -

      ##### Optional fatal?: EventParams\["fatal"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "generate_lead" , eventParams ? : { currency ?: EventParams \[ "currency" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "generate_lead"

  -

    ##### Optional eventParams: { currency?: EventParams\["currency"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "login" , eventParams ? : { method ?: EventParams \[ "method" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "login"

  -

    ##### Optional eventParams: { method?: EventParams\["method"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional method?: EventParams\["method"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "page_view" , eventParams ? : { page_location ?: string ; page_path ?: string ; page_title ?: string } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  See
  [Page views](https://developers.google.com/analytics/devguides/collection/ga4/page-view).

  #### Parameters

  -

    ##### eventName: "page_view"

  -

    ##### Optional eventParams: { page_location?: string; page_path?: string; page_title?: string }

    -

      ##### \[key: string\]: any

    -

      ##### Optional page_location?: string

    -

      ##### Optional page_path?: string

    -

      ##### Optional page_title?: string

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "purchase" \| "refund" , eventParams ? : { affiliation ?: EventParams \[ "affiliation" \] ; coupon ?: EventParams \[ "coupon" \] ; currency ?: EventParams \[ "currency" \] ; items ?: EventParams \[ "items" \] ; shipping ?: EventParams \[ "shipping" \] ; tax ?: EventParams \[ "tax" \] ; transaction_id : EventParams \[ "transaction_id" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "purchase" \| "refund"

  -

    ##### Optional eventParams: { affiliation?: EventParams\["affiliation"\]; coupon?: EventParams\["coupon"\]; currency?: EventParams\["currency"\]; items?: EventParams\["items"\]; shipping?: EventParams\["shipping"\]; tax?: EventParams\["tax"\]; transaction_id: EventParams\["transaction_id"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional affiliation?: EventParams\["affiliation"\]

    -

      ##### Optional coupon?: EventParams\["coupon"\]

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional shipping?: EventParams\["shipping"\]

    -

      ##### Optional tax?: EventParams\["tax"\]

    -

      ##### transaction_id: EventParams\["transaction_id"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "screen_view" , eventParams ? : { firebase_screen : EventParams \[ "firebase_screen" \] ; firebase_screen_class : EventParams \[ "firebase_screen_class" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  See [Track Screenviews](https://firebase.google.com/docs/analytics/screenviews).

  #### Parameters

  -

    ##### eventName: "screen_view"

  -

    ##### Optional eventParams: { firebase_screen: EventParams\["firebase_screen"\]; firebase_screen_class: EventParams\["firebase_screen_class"\] }

    -

      ##### \[key: string\]: any

    -

      ##### firebase_screen: EventParams\["firebase_screen"\]

    -

      ##### firebase_screen_class: EventParams\["firebase_screen_class"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "search" \| "view_search_results" , eventParams ? : { search_term ?: EventParams \[ "search_term" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "search" \| "view_search_results"

  -

    ##### Optional eventParams: { search_term?: EventParams\["search_term"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional search_term?: EventParams\["search_term"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "select_content" , eventParams ? : { content_type ?: EventParams \[ "content_type" \] ; item_id ?: EventParams \[ "item_id" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "select_content"

  -

    ##### Optional eventParams: { content_type?: EventParams\["content_type"\]; item_id?: EventParams\["item_id"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional content_type?: EventParams\["content_type"\]

    -

      ##### Optional item_id?: EventParams\["item_id"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "select_item" , eventParams ? : { item_list_id ?: EventParams \[ "item_list_id" \] ; item_list_name ?: EventParams \[ "item_list_name" \] ; items ?: EventParams \[ "items" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "select_item"

  -

    ##### Optional eventParams: { item_list_id?: EventParams\["item_list_id"\]; item_list_name?: EventParams\["item_list_name"\]; items?: EventParams\["items"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional item_list_id?: EventParams\["item_list_id"\]

    -

      ##### Optional item_list_name?: EventParams\["item_list_name"\]

    -

      ##### Optional items?: EventParams\["items"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "select_promotion" \| "view_promotion" , eventParams ? : { items ?: EventParams \[ "items" \] ; promotion_id ?: EventParams \[ "promotion_id" \] ; promotion_name ?: EventParams \[ "promotion_name" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "select_promotion" \| "view_promotion"

  -

    ##### Optional eventParams: { items?: EventParams\["items"\]; promotion_id?: EventParams\["promotion_id"\]; promotion_name?: EventParams\["promotion_name"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional promotion_id?: EventParams\["promotion_id"\]

    -

      ##### Optional promotion_name?: EventParams\["promotion_name"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "set_checkout_option" , eventParams ? : { checkout_option ?: EventParams \[ "checkout_option" \] ; checkout_step ?: EventParams \[ "checkout_step" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "set_checkout_option"

  -

    ##### Optional eventParams: { checkout_option?: EventParams\["checkout_option"\]; checkout_step?: EventParams\["checkout_step"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional checkout_option?: EventParams\["checkout_option"\]

    -

      ##### Optional checkout_step?: EventParams\["checkout_step"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "share" , eventParams ? : { content_type ?: EventParams \[ "content_type" \] ; item_id ?: EventParams \[ "item_id" \] ; method ?: EventParams \[ "method" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "share"

  -

    ##### Optional eventParams: { content_type?: EventParams\["content_type"\]; item_id?: EventParams\["item_id"\]; method?: EventParams\["method"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional content_type?: EventParams\["content_type"\]

    -

      ##### Optional item_id?: EventParams\["item_id"\]

    -

      ##### Optional method?: EventParams\["method"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "sign_up" , eventParams ? : { method ?: EventParams \[ "method" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "sign_up"

  -

    ##### Optional eventParams: { method?: EventParams\["method"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional method?: EventParams\["method"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "timing_complete" , eventParams ? : { event_category ?: string ; event_label ?: string ; name : string ; value : number } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "timing_complete"

  -

    ##### Optional eventParams: { event_category?: string; event_label?: string; name: string; value: number }

    -

      ##### \[key: string\]: any

    -

      ##### Optional event_category?: string

    -

      ##### Optional event_label?: string

    -

      ##### name: string

    -

      ##### value: number

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "view_cart" \| "view_item" , eventParams ? : { currency ?: EventParams \[ "currency" \] ; items ?: EventParams \[ "items" \] ; value ?: EventParams \[ "value" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "view_cart" \| "view_item"

  -

    ##### Optional eventParams: { currency?: EventParams\["currency"\]; items?: EventParams\["items"\]; value?: EventParams\["value"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional currency?: EventParams\["currency"\]

    -

      ##### Optional items?: EventParams\["items"\]

    -

      ##### Optional value?: EventParams\["value"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent ( eventName : "view_item_list" , eventParams ? : { item_list_id ?: EventParams \[ "item_list_id" \] ; item_list_name ?: EventParams \[ "item_list_name" \] ; items ?: EventParams \[ "items" \] } , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Parameters

  -

    ##### eventName: "view_item_list"

  -

    ##### Optional eventParams: { item_list_id?: EventParams\["item_list_id"\]; item_list_name?: EventParams\["item_list_name"\]; items?: EventParams\["items"\] }

    -

      ##### \[key: string\]: any

    -

      ##### Optional item_list_id?: EventParams\["item_list_id"\]

    -

      ##### Optional item_list_name?: EventParams\["item_list_name"\]

    -

      ##### Optional items?: EventParams\["items"\]

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

- logEvent \< T \> ( eventName : [CustomEventName](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#customeventname) \< T \> , eventParams ? : {} , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Sends analytics event with given `eventParams`. This method
  automatically associates this logged event with this Firebase web
  app instance on this device.
  List of recommended event parameters can be found in
  [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

  #### Type parameters

  -

    #### T: string

  #### Parameters

  -

    ##### eventName: [CustomEventName](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#customeventname)\<T\>

  -

    ##### Optional eventParams: {}

    -

      ##### \[key: string\]: any

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

### setAnalyticsCollectionEnabled

- setAnalyticsCollectionEnabled ( enabled : boolean ) : void
- Sets whether analytics collection is enabled for this app on this device.
  window\['ga-disable-analyticsId'\] = true;

  #### Parameters

  -

    ##### enabled: boolean

  #### Returns void

### setCurrentScreen

- setCurrentScreen ( screenName : string , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
-

  deprecated

  :   Use [logEvent](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics#logevent) with `eventName` as 'screen_view' and add relevant `eventParams`.
      See [Track Screenviews](https://firebase.google.com/docs/analytics/screenviews).

  Use gtag 'config' command to set 'screen_name'.

  #### Parameters

  -

    ##### screenName: string

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

### setUserId

- setUserId ( id : string , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Use gtag 'config' command to set 'user_id'.

  #### Parameters

  -

    ##### id: string

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void

### setUserProperties

- setUserProperties ( properties : [CustomParams](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.CustomParams) , options ? : [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions) ) : void
- Use gtag 'config' command to set all params specified.

  #### Parameters

  -

    ##### properties: [CustomParams](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.CustomParams)

  -

    ##### Optional options: [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)

  #### Returns void