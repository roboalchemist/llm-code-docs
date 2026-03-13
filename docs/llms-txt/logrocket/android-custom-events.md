# Source: https://docs.logrocket.com/reference/android-custom-events.md

# Track Custom Events (Android)

Track custom information or user actions in your Android app

Use the Custom Events API to track custom event measurements about your users' in-app behavior..

```java
SDK.track(new CustomEventBuilder("Registered"));
```

You can then search for sessions containing these events using a **Custom Event** filter in the LogRocket Dashboard:

<Image align="center" width="600px" src="https://files.readme.io/be423402da6b7b408e916d82307c01338ac9fd54692ddd3c2a8cf7b001d0aa52-Screenshot_2025-02-27_at_4.58.37_PM.png" />

You can optionally provide additional properties that will be associated with the event:

```java
SDK.track(new CustomEventBuilder("PurchaseComplete") {{
  put("revenue", 24.99);
  put("productCategory", "Clothing");
  put("productSku", 488736929); // Integer values are cast to Double values automatically
  put("couponApplied", true);
  put("customerSegments", "aef34b", "97cb20"); // Multiple values can be added in one call
}});
```

Properties may be of type boolean, double, or string. Arrays of primitives (boolean, double, or string) are also supported.

There are a few limits to keep in mind when providing properties to Custom Events:

* Property names must be under 100 characters.
* A maximum of 2000 properties may be uploaded per session. Properties over this limit will not be recorded.

> 📘 'Revenue' Property
>
> The 'revenue' property is a special property that you can use to pass data into our funnels. For more information, see [here](https://docs.logrocket.com/docs/revenue-insights-for-funnels).