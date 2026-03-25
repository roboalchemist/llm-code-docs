# Source: https://docs.instabug.com/references/in-app-replies/push-notifications/set-notification-icon.md

# Set Notification Icon

Use this API to set the icon you'd like to show for Luciq related notifications. This method takes `@DrawableRes int` parameter.

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
Replies.setNotificationIcon(@DrawableRes int notificationIcon);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setNotificationIcon(@DrawableRes int notificationIcon)
```

{% endtab %}
{% endtabs %}
