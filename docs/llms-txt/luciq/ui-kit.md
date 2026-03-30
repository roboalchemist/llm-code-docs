# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-loading/ui-kit.md

# UI Kit

Luciq automatically captures the time it takes for any UI Kit screen to load. This covers the time for any View Controller between `viewDidLoad` and `viewDidAppear`, which includes the following lifecycle methods:

* `viewDidLoad`
* `viewWillAppear`
* `viewWillLayoutSubviews`
* `viewDidLayoutSubviews`
* `viewDidAppear`

### Spans

Luciq will automatically show spans and operations that occurred during the View Controller loading; these include:

* Network Requests
* Database Queries
* UI Kit Lifecycle methods

### End Screen Loading

You can also define custom points in each View Controller to manually inform the SDK that screen loading has ended.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
APM.endScreenLoading(for viewController: self) // self here is a reference to a UIViewController
```

{% endcode %}
{% endtab %}
{% endtabs %}

<br>
