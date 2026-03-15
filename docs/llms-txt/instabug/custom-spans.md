# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-application-performance-monitoring/custom-spans.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/logs-and-profiling/custom-spans.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/logs-and-profiling/custom-spans.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/custom-settings/logs-and-profiling/custom-spans.md

# Custom Spans

#### Overview

Custom Spans allow you to manually instrument parts of your application and measure how long specific operations take. This helps you track performance for specific spans that are not automatically captured.

Custom spans appear in the Spans timeline alongside automatically collected spans. They will appear inside all APM metrics we already capture such as app launches, screen loading, network logs and Flows. The backend correlates the custom span with its respective metrics based on their timestamps.&#x20;

#### Setup Custom Spans

To log a new custom spans, please use the below API

{% tabs %}
{% tab title="Swift" %}

```swift
let span: CustomSpan? = APM.startCustomSpan(_ name: String)

span?.end()
```

{% endtab %}
{% endtabs %}

To log a completed span, use the below API

{% tabs %}
{% tab title="Swift" %}

```swift
APM.addCompletedCustomSpan(name: String, startDate: Date, endDate: Date)
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
Considerations for creating Custom Spans

1. APM must be enabled to use Custom Spans&#x20;
2. Luciq SDK must be initialized before calling the API
3. Custom span name cannot be empty
4. Maximum **100 spans per session** (older spans may be dropped if the limit is exceeded
5. Minimum SDK version required is 19.5.0
   {% endhint %}
