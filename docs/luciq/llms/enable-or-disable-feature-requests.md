# Source: https://docs.luciq.ai/references/in-app-feature-requests/enable-or-disable-feature-requests.md

# Enable or Disable Feature Requests

You can completely prevent any feature request-related features from displaying by disabling them using the API below.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Enable
FeatureRequests.enabled = true

//Disable
FeatureRequests.enabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Enable
LCQFeatureRequests.enabled = YES;

//Disable
LCQFeatureRequests.enabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Enable
FeatureRequests.setState(Feature.State.ENABLED);

//Disable
FeatureRequests.setState(Feature.State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Enable
FeatureRequests.setState(Feature.State.ENABLED)

//Disable
FeatureRequests.setState(Feature.State.DISABLED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Enable
FeatureRequests.setEnabled(true);

//Disable
FeatureRequests.setEnabled(false);
```

{% endtab %}
{% endtabs %}
