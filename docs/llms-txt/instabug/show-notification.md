# Source: https://docs.instabug.com/references/in-app-replies/push-notifications/show-notification.md

# Show Notification

You can use this API to show a notification when you know that it is Luciq related.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
if let notification = launchOptions?[.remoteNotification] as? [String: AnyObject] {
   let isLuciqNotification = Replies.didReceiveRemoteNotification(notification)
 }
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSDictionary *notificationDictionary = [launchOptions objectForKey:UIApplicationLaunchOptionsRemoteNotificationKey];

BOOL isLuciqNotification = [LCQReplies didReceiveRemoteNotification:notificationDictionary];
```

{% endtab %}

{% tab title="And - Java" %}

```java
if(Replies.isLuciqNotification(data)){
  //Show notification related to Luciq
  Replies.showNotification(data);
}
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
if(Replies.isLuciqNotification(data)){
  //Show notification related to Luciq
  Replies.showNotification(data)
}
```

{% endtab %}
{% endtabs %}
