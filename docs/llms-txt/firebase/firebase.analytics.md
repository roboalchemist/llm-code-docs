# Source: https://firebase.google.com/docs/reference/js/v8/firebase.analytics.md.txt

# analytics | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- analytics

The Analytics SDK does not work in a Node.js environment.

### Callable

- analytics ( app ? : [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App) ) : [Analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics)
- Gets the [`Analytics`](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics) service.

  `firebase.analytics()` can be called with no arguments to access the default
  app's [`Analytics`](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics) service.

  The Analytics SDK does not work in a Node.js environment.

  example
  :

          // Get the Analytics service for the default app
          const defaultAnalytics = firebase.analytics();


  #### Parameters

  -

    ##### Optional app: [App](https://firebase.google.com/docs/reference/js/v8/firebase.app.App)

    The app to create an analytics service for.
    If not passed, uses the default app.

  #### Returns [Analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics)

## Index

### Enumerations

- [EventName](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventName)

### Interfaces

- [Analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Analytics)
- [AnalyticsCallOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.AnalyticsCallOptions)
- [ControlParams](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.ControlParams)
- [CustomParams](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.CustomParams)
- [EventParams](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams)
- [Item](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Item)
- [Promotion](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Promotion)
- [SettingsOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.SettingsOptions)

### Type aliases

- [Currency](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#currency)
- [CustomEventName](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#customeventname)
- [EventNameString](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#eventnamestring)

### Functions

- [isSupported](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#issupported)
- [settings](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#settings)

## Type aliases

### Currency

Currency: string \| number

### CustomEventName

CustomEventName\<T\>: T extends EventNameString ? never : T

#### Type parameters

-

  #### T

### EventNameString

EventNameString: "add_payment_info" \| "add_shipping_info" \| "add_to_cart" \| "add_to_wishlist" \| "begin_checkout" \| "checkout_progress" \| "exception" \| "generate_lead" \| "login" \| "page_view" \| "purchase" \| "refund" \| "remove_from_cart" \| "screen_view" \| "search" \| "select_content" \| "select_item" \| "select_promotion" \| "set_checkout_option" \| "share" \| "sign_up" \| "timing_complete" \| "view_cart" \| "view_item" \| "view_item_list" \| "view_promotion" \| "view_search_results"  
Type for standard gtag.js event names. `logEvent` also accepts any
custom string and interprets it as a custom event name.

## Functions

### isSupported

- isSupported ( ) : Promise \< boolean \>
- An async function that returns true if current browser context supports initialization of analytics module
  (`firebase.analytics()`).

  Returns false otherwise.

  #### Returns Promise\<boolean\>

### settings

- settings ( settings : [SettingsOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.SettingsOptions) ) : void
- Configures Firebase Analytics to use custom `gtag` or `dataLayer` names.
  Intended to be used if `gtag.js` script has been installed on
  this page independently of Firebase Analytics, and is using non-default
  names for either the `gtag` function or for `dataLayer`.
  Must be called before calling `firebase.analytics()` or it won't
  have any effect.

  #### Parameters

  -

    ##### settings: [SettingsOptions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.SettingsOptions)

  #### Returns void