# Source: https://docs.logrocket.com/reference/capture-custom-pages-android.md

# Capture Custom Pages (Android)

Android Manual Page Tagging

LogRocket automatically captures mobile pages (defined as ViewController for iOS and Activity for Android) and tracks this under the Visited URL attribute. These URLs are then referenced in Path Analysis, Heatmaps, and URL filters in the LogRocket dashboard. This API allows you to tag sub pages, for more granular filtering and metrics.

tagPage() can be used to tag a sub page of the currently running Activity. Manually tagging pages can help improve the specificity of metrics in LogRocket. This tagged page will be combined with the running Activity to form a URL of the form `https://{Package Name}/{Activity Class Name}/{Relative Page Tag}`. These URLs can be referenced in Path Analysis, Heatmaps, and URL filters in the LogRocket dashboard.

```java
SDK.tagPage("Apparel")

SDK.tagPage("Apparel/Sweaters")

SDK.tagPage("Apparel/Pants")
```

> 🚧
>
> Make sure to only tag pages when the page is visible on screen, as opposed to when it is created. For example, `tagPage()` would be called inside `setMenuVisibility` instead of `onCreateView`.

> 📘
>
> We recommend tagging pages hierarchically as you would define website URL paths.
>
> The maximum supported relativePage tag length is 500 characters. A warning will be generated if the provided relativePage exceeds this length.
>
> Page tags are URL-encoded according to Uri.encode with ‘/’ remaining unencoded.

## Tracking mobile pages with page tags only

The activity tracking system normally updates event URLs when activities move in and out of scope. This can be turned off entirely by disabling automatic lifecycle capture. With lifecycle capture off, URLs will be updated exclusively by `tagPage` actions. This may be useful, for example, if path analysis steps are best represented by groups of activities, as opposed to a sequence of activities.  In this case, the grouped activities should each call `tagPage` with the same identifier.

> 🚧
>
> Note that if automatic lifecycle capture is disabled, it is important that `tagPage` be called consistently across your app. If new activities appear without a call to `tagPage`, subsequent events will inherit their page name from the last tagged page. Additionally, it is recommended to call `tagPage` immediately after initializing a LogRocket session so that user interactions at the start of a session are associated with the proper page.

To opt out of automatic lifecycle capture and rely on manual calls to `tagPage`, initialize LogRocket with the configuration value `enableAutomaticLifecycleCapture` set to `false`. This feature is available on version 1.47.4 and above of the native Android SDK.