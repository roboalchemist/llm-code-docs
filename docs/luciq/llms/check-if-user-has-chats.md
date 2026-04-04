# Source: https://docs.luciq.ai/references/in-app-replies/check-if-user-has-chats.md

# Check for Existing Chats

This method returns a boolean variable that depicts whether or not the user has existing chats.

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
Replies.hasChats()
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQReplies hasChats];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Replies.hasChats();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.hasChats()
```

{% endtab %}

{% tab title="RN" %}

```javascript
Replies.hasChats(previousChats=> { 
  if(previousChats) {
    // Has chats
  } else {
    // Doesn't have chats
  }
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
final hasChats = Replies.hasChats();
```

{% endtab %}
{% endtabs %}
