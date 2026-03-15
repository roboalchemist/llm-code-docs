# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings/private-views.md

# Private Views

You can use this API to set any particular view as private so that it is always hidden in screenshots.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
view.Luciq_privateView = true
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
view.Luciq_privateView = YES;
```

{% endcode %}
{% endtab %}
{% endtabs %}
