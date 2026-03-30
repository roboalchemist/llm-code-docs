# Source: https://docs.logrocket.com/reference/track.md

# Track Custom Events (Web)

Track custom information or user actions in your Web app

Use the Custom Events API to track custom event measurements about your users' in-app behavior.

`LogRocket.track()` accepts a single **String** argument

```javascript Calling track()
LogRocket.track('Registered');
```

You can then search for sessions containing these events using a **Custom Event** filter in the LogRocket Dashboard:

<Image align="center" width="600px" src="https://files.readme.io/be423402da6b7b408e916d82307c01338ac9fd54692ddd3c2a8cf7b001d0aa52-Screenshot_2025-02-27_at_4.58.37_PM.png" />

You can optionally provide a second *Object* argument containing properties that will be associated with the event:

```javascript
LogRocket.track('PurchaseComplete', {
   revenue: 42.99,
   productCategory: 'Clothing',
   productSku: 4887369299,
   couponApplied: true,
   customerSegments: ['aef34b', '97cb20']
});
```

Properties may be of type boolean, integer, float, or string. Arrays of primitives (boolean, integer, float, or string) are also supported.

There are a few limits to keep in mind when providing properties to LogRocket.track():

* Property names must be under 100 characters.
* A maximum of 2000 properties may be uploaded per session. Properties over this limit will not be recorded.

> 📘 'Revenue' property
>
> The 'revenue' property is a special property that you can use to pass data into our funnels.  For more information, see [here](https://docs.logrocket.com/docs/revenue-insights-for-funnels).