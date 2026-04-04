# Source: https://docs.logrocket.com/reference/flutter-custom-events.md

# Track Custom Events

Track custom information or user actions in your Flutter app

Use the Custom Events API to track custom event measurements about your users' in-app behavior.

```dart Flutter
await LogRocket.track(LogRocketCustomEventBuilder('testEvent'));
```

You can then search for sessions containing these events using a **Custom Event** filter in the LogRocket Dashboard:

<Image align="center" width="600px" src="https://files.readme.io/be423402da6b7b408e916d82307c01338ac9fd54692ddd3c2a8cf7b001d0aa52-Screenshot_2025-02-27_at_4.58.37_PM.png" />

You can optionally provide additional properties that will be associated with the event. All supported property types are listed here:

```dart Flutter
var event = LogRocketCustomEventBuilder('testEvent');

event.putRevenue(24.99);
event.putInt("productSku", 488736929);
event.putString("productCategory", "Clothing");
event.putBool("couponApplied", true);
event.putDouble("unitWeight", 1.2);
event.putListString("customerSegments", ["aef34b", "97cb20"]);
event.putListInt("quantities", [1, 8, 12]);
event.putListBool("quantityShipsFree", [false, true, true]);
event.putListDouble("discounts", [1.99, 2.99]);

await LogRocket.track(event);
```

There are a few limits to keep in mind when providing properties to Custom Events:

* Property names must be under 100 characters.
* A maximum of 2000 properties may be uploaded per session. Properties over this limit will not be recorded.

> 📘 'Revenue' Property
>
> The 'revenue' property is a special property that you can use to pass data into our funnels. For more information, see [here](https://docs.logrocket.com/docs/revenue-insights-for-funnels).