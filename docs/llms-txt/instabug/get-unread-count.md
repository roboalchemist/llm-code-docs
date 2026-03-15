# Source: https://docs.instabug.com/references/in-app-replies/get-unread-count.md

# Get Unread Count

This API returns an integer representing the number unread messages by the user.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
let messageCount = Replies.unreadRepliesCount
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSUInteger messageCount = LCQReplies.unreadRepliesCount;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Replies.getUnreadRepliesCount();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.getUnreadRepliesCount()
```

{% endtab %}

{% tab title="RN" %}

```javascript
Replies.getUnreadMessagesCount((count) => {
  Alert.alert("UnReadMessages", "Messages: " + count);
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
final count = Replies.getUnreadRepliesCount();
```

{% endtab %}
{% endtabs %}
