# Source: https://docs.luciq.ai/references/in-app-replies/enable-or-disable-replies.md

# Enable or Disable Replies

You can completely disable replies to prevent your users from being able to see the replies page as well as disabling in-app notifications.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Replies.enabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQReplies.enabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Replies.setState(Feature.State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setState(Feature.State.DISABLED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Replies.setEnabled(true);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Replies.setEnabled(false);
```

{% endtab %}
{% endtabs %}
