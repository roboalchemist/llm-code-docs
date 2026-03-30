# Source: https://docs.instabug.com/references/application-performance-monitoring/enable-or-disable-screen-loading/index.md

# Enable or Disable Screen Loading

Luciq automatically captures data about your screen loading time. You can alter that using the following APIs.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
APM.screenLoadingEnabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQAPM.screenLoadingEnabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
APM.setScreenLoadingEnabled(boolean disabled);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
APM.setScreenLoadingEnabled(boolean disabled)
```

{% endtab %}

{% tab title="Flutter" %}

```dart
APM.setScreenLoadingEnabled(false);
```

{% endtab %}
{% endtabs %}
