# Source: https://docs.luciq.ai/references/in-app-replies/in-app-notifications/managing-sounds.md

# Managing Sounds

There are different types of sounds that play when different events occur. These sounds can all be disabled or enabled based on need.

**In-App Notification Sound**

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
Replies.setInAppNotificationEnabled(false);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setInAppNotificationEnabled(false)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Replies.setInAppNotificationSound(false);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Replies.setInAppNotificationSound(false);
```

{% endtab %}
{% endtabs %}

**System Notification Sound**

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
Replies.setSystemReplyNotificationSoundEnabled(true);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setSystemReplyNotificationSoundEnabled(true)
```

{% endtab %}
{% endtabs %}

**Conversation Sound**

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
Replies.setShouldPlayConversationSounds(false);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setShouldPlayConversationSounds(false)
```

{% endtab %}
{% endtabs %}
