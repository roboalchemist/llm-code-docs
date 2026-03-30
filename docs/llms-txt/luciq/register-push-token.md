# Source: https://docs.luciq.ai/references/in-app-replies/push-notifications/register-push-token.md

# Register Push Token

In order to receive push notifications, registering your token is necessary. You can use this API to register this token.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Replies.didRegisterForRemoteNotifications(withDeviceToken: deviceToken)
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
    [LCQReplies didRegisterForRemoteNotificationsWithDeviceToken:deviceToken];
}
```

{% endtab %}

{% tab title="And - Java" %}

```java
Replies.setPushNotificationRegistrationToken("PUSH_NOTIFICATION_TOKEN");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Replies.setPushNotificationRegistrationToken("PUSH_NOTIFICATION_TOKEN")
```

{% endtab %}
{% endtabs %}
