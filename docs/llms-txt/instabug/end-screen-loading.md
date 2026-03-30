# Source: https://docs.instabug.com/references/application-performance-monitoring/enable-or-disable-screen-loading/end-screen-loading.md

# End Screen Loading

You can manually inform the Luciq SDK that screen loading has ended using the following API. You'll simply need to pass the current `View Controller` or `Activity`

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
APM.endScreenLoading(for viewController: self) // self here is a reference to a UIViewController
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQAPM endScreenLoadingForViewController: self]; // self here is a reference to a UIViewController
```

{% endtab %}

{% tab title="And - Java" %}

```java
APM.endScreenLoading(YourActivity.class);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
APM.endScreenLoading(Class<T> activityClass)
```

{% endtab %}

{% tab title="Flutter" %}

```dart
APM.endScreenLoading();
```

{% endtab %}
{% endtabs %}
