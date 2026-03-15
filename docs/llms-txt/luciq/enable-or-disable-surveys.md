# Source: https://docs.luciq.ai/references/in-app-surveys/enable-or-disable-surveys.md

# Enable or Disable Surveys

If you would like to disable the surveys from showing in general, including manual targeting surveys, you can do so using this API.

{% hint style="danger" %}
Disabling Surveys

This API completely disables surveys, meaning surveys will not be shown regardless of the code called.
{% endhint %}

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Surveys.enabled = false;
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQSurveys setEnabled:NO];
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Enable
Surveys.setState(Feature.State.ENABLED);
// Disable
Surveys.setState(Feature.State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Enable
Surveys.setState(Feature.State.ENABLED)
// Disable
Surveys.setState(Feature.State.DISABLED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Surveys.setEnabled(false);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Surveys.setEnabled(false);
```

{% endtab %}
{% endtabs %}
