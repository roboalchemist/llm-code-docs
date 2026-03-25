# Source: https://docs.instabug.com/references/in-app-replies/push-notifications/enable-or-disable-push-notifications.md

# Enable or Disable Push Notifications

If you would like to disable or enable push notifications at runtime, this method would do the trick.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

<pre class="language-swift"><code class="lang-swift"><strong>Replies.pushNotificationsEnabled = false
</strong></code></pre>

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQReplies setPushNotificationsEnabled:NO];
```

{% endtab %}

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
Replies.setPushNotificationsEnabled(false);
```

{% endtab %}
{% endtabs %}
