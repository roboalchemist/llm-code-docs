# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/application-performance-monitoring/screen-loading.md

# Screen Loading

{% hint style="info" %}
📘 The way Luciq captures the loading time of your screens depends on whether they are built using [UI Kit](https://docs.luciq.ai/docs/ios-apm-screen-loading#ui-kit) or [SwiftUI](https://docs.luciq.ai/docs/ios-apm-screen-loading#swiftui).
{% endhint %}

### UI Kit

Luciq automatically captures the time it takes for any UI Kit screen to load. This covers the time for any View Controller between `viewDidLoad` and `viewDidAppear`, which includes the following lifecycle methods:

* `viewDidLoad`
* `viewWillAppear`
* `viewWillLayoutSubviews`
* `viewDidLayoutSubviews`
* `viewDidAppear`

#### Spans

Luciq will automatically show spans and operations that occurred during the View Controller loading; these include:

* Network Requests
* Database Queries
* UI Kit Lifecycle methods

#### End Screen Loading

You can also define custom points in each View Controller to manually inform the SDK that screen loading has ended.

***

### SwiftUI

{% hint style="warning" %}

#### 🚧 **Minimum Required SDK Version**

SwiftUI Screen Loading is supported starting iOS SDK v14.0.0
{% endhint %}

To be able to measure the loading time of your SwiftUI views, you need to [instrument your views](https://docs.luciq.ai/docs/ios-swiftui-integration#define-screen-names) by wrapping them in our `LuciqTracedView` component:

#### Spans

Luciq will automatically show spans and operations that occurred during the SwiftUI view loading; these include:

* Network Requests
* Database Queries
* The `body` span, which represents how long the body object took to load

***

### Screen Loading Apdex

Luciq calculates an Apdex score for your app traces as a way of measuring their performance. An Apdex score ranges between 0 and 1; the higher the value, the better:

* Apdex score ≥ 0.94 equates to **Excellent** performance.
* Apdex score ≥ 0.85 and < 0.94 equates to **Good** performance.
* Apdex score ≥ 0.7 and < 0.85 equates to **Fair** performance.
* Apdex score ≥ 0.5 and < 0.7 equates to **Poor** performance.
* Apdex score < 0.5 is considered **Unacceptable**.

#### How Is the Screen Loading Apdex Calculated?

When an app trace occurrence is collected, it is flagged based on a pre-defined target (T). An app trace occurrence is considered:

* **Satisfying**: if its duration ≤ T
* **Tolerable**: if its duration > T and ≤ 4T
* **Frustrating**: if its duration > 4T

Then, based on the bucketing explained above, the Apdex score is calculated as follows:

* Total occurrences = Satisfying occurrences + Tolerable occurrences + Frustrating occurrences
* Apdex score = (Satisfying occurrences + 0.5 \* Tolerable occurrences) / Total occurrences

#### How Can You Control a Specific Screen's Target?

By default, the target is set to **0.1 seconds**; however, you can easily change this number from your dashboard by clicking on your current threshold in the Apdex section.
