# Source: https://docs.logrocket.com/reference/capture-custom-pages-ios.md

# Capture Custom Pages (iOS)

iOS Manual Page Tagging

LogRocket automatically captures mobile pages (defined as a View Controller on iOS and an Activity on Android) and tracks this under the Visited URL attribute. These URLs are then referenced in Path Analysis, Heatmaps, and URL filters in the LogRocket dashboard. This API allows you to tag sub pages to enable more granular filtering and metrics.

`tagPage()` can be used to tag a sub page of the currently running view controller. Manually tagging pages can help improve the specificity of metrics in LogRocket. This tagged page will be combined with the most recent view controller currently in scope to form a URL of the form `https://{Bundle ID}/{View Controller Class Name}/{Relative Page Tag}`. These URLs can be referenced in Path Analysis, Heatmaps, and URL filters in the LogRocket dashboard.

```Text Swift
SDK.tagPage("Apparel")

SDK.tagPage('Apparel/Sweaters")

SDK.tagPage("Apparel/Pants")
```

> 🚧
>
> Make sure to only tag pages when the page is visible on screen, as opposed to when it is created. For example, `tagPage()` would be called inside `viewDidAppear` or later in the ViewController’s lifecycle.

> 📘
>
> We recommend tagging pages hierarchically as you would define website URL paths.
>
> The maximum supported relativePage tag length is 500 characters. A warning will be generated if the provided relativePage exceeds this length.
>
> Page tags are url encoded with `addingpercentencoding` using character set urlPathAllowed.

## Tracking mobile pages with page tags only

The view controller tracking system normally updates event URLs when view controllers move in and out of scope. This can be turned off entirely by disabling automatic lifecycle capture. With lifecycle capture off, URLs will be updated exclusively by `tagPage` actions. This may be useful, for example, if path analysis steps are best represented by groups of view controllers, as opposed to a sequence of individual view controllers.  In this case, the grouped view controllers should each call `tagPage` with the same identifier.

> 🚧
>
> Note that if automatic lifecycle capture is disabled, it is important that `tagPage` be called consistently across your app. If new views appear without a call to `tagPage`, subsequent events will inherit their page name from the last tagged page. Additionally, it is recommended to call `tagPage` immediately after initializing a LogRocket session so that user interactions at the start of a session are associated with the proper page.

To opt out of automatic lifecycle capture and rely on manual calls to `tagPage`, initialize LogRocket with the configuration value `enableAutomaticLifecycleCapture` set to `false`. This feature is available on version 1.47.4 and above of the native iOS SDK.