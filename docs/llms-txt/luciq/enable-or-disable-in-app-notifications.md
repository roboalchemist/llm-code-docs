# Source: https://docs.luciq.ai/references/in-app-replies/in-app-notifications/enable-or-disable-in-app-notifications.md

# Enable or Disable In-App Notifications

By default, your users will receive in-app notifications when they receive a new message. This in-app popup notification can be disabled or enabled as required using this API.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Replies.inAppNotificationsEnabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQReplies.inAppNotificationsEnabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Replies.setInAppNotificationEnabled(false);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setReplyNotificationEnabled(false)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Replies.setInAppNotificationsEnabled(false);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Replies.setInAppNotificationsEnabled(false);
```

{% endtab %}
{% endtabs %}
