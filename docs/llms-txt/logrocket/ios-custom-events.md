# Source: https://docs.logrocket.com/reference/ios-custom-events.md

# Track Custom Events (iOS)

Track custom information or user actions in your iOS app

Use the Custom Events API to track custom event measurements about your users' in-app behavior.

```swift Swift
SDK.track(CustomEventBuilder("Registered"));
```

```objectivec Objective-C
LROCustomEventBuilder *builder = [[LROCustomEventBuilder alloc] init:@"Registered"];
[LROSDK track:builder];
```

You can then search for sessions containing these events using a **Custom Event** filter in the LogRocket Dashboard:

<Image align="center" width="600px" src="https://files.readme.io/be423402da6b7b408e916d82307c01338ac9fd54692ddd3c2a8cf7b001d0aa52-Screenshot_2025-02-27_at_4.58.37_PM.png" />

You can optionally provide additional properties that will be associated with the event:

```swift Swift
let builder = CustomEventBuilder("PurchaseComplete")
builder.put("revenue", 24.99)
builder.put("productCategory", "Clothing")
builder.put("productSku", 488736929)
builder.put("couponApplied", true)
builder.put("customerSegments", ["aef34b", "97cb20"]) // Register multiple values with one call

SDK.track(builder) // Capture the event
```

```objectivec Objective-C
LROCustomEventBuilder *builder = [[LROCustomEventBuilder alloc] init:@"PurchaseComplete"];

[builder putDouble:@"revenue" value:24.99];
[builder putString:@"productCategory" value:@"Clothing"];
[builder putDouble:@"productSku" value:488736929];
[builder putBool:@"couponApplied" value:true];
[builder putStringArray:@"customerSegments" value:[NSArray arrayWithObjects:@"aef34b", @"97cb20",nil]];

[LROSDK track:builder];
```

Properties may be of type boolean, double, or string. Arrays of primitives (boolean, double, or string) are also supported.

There are a few limits to keep in mind when providing properties to Custom Events:

* Property names must be under 100 characters.
* A maximum of 2000 properties may be uploaded per session. Properties over this limit will not be recorded.

> 📘 'Revenue' Property
>
> The 'revenue' property is a special property that you can use to pass data into our funnels. For more information, see [here](https://docs.logrocket.com/docs/revenue-insights-for-funnels).