# Source: https://docs.luciq.ai/references/application-performance-monitoring/enable-or-disable-apm.md

# Enable or Disable APM

You can enable or disable APM using the following APIs.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
APM.enabled = true
APM.enabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objective-c
LCQAPM.enabled = YES;
LCQAPM.enabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Enable/disable APM
APM.setEnabled(true);
APM.setEnabled(false);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Enable/disable APM
APM.setEnabled(true)
APM.setEnabled(false)
```

{% endtab %}

{% tab title="RN" %}

```javascript
// Enable
APM.setEnabled(true);

// Disable
APM.setEnabled(false);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
// Enable APM
APM.setEnabled(true);

// Disable APM
APM.setEnabled(false);
```

{% endtab %}
{% endtabs %}
