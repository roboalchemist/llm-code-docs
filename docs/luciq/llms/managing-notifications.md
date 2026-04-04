# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-in-app-replies/managing-notifications.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-in-app-replies/managing-notifications.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/in-app-replies/managing-notifications.md

# Managing Notifications

### Push Notifications

In order to enable Push Notifications on React Native, please make sure to follow the steps for each platform's individual steps.

{% tabs %}
{% tab title="iOS" %}
In order to enable push notifications on iOS, you will need to follow the steps [here](https://docs.luciq.ai/react-native/setup-luciq-for-react-native/in-app-replies/broken-reference).

{% hint style="warning" %}
Please note that calling `Replies.didReceiveRemoteNotification(notification)` in your `application:didFinishLaunchingWithOptions:` to check whether this is an Luciq notification will not work in iOS due to a known limitation; an alternative solution would be to manually check if the key `LCQHost` exists in the payload, which flags it as an Luciq notification.
{% endhint %}
{% endtab %}

{% tab title="Android" %}
**Start Receiving Push Notifications**

To allow us to send push notifications to your app, you will need to configure your Firebase Cloud Messaging (FCM) Server Key on our Dashboard by navigating to Settings -> Push Notifications and setting the `API_KEY` field.

Once that's done, you can start receiving push notifications by passing the registration token to our SDK:

{% code title="JavaScript" %}

```javascript
Replies.setPushNotificationRegistrationTokenAndroid('TOKEN');
```

{% endcode %}

When a background notification is received, you can pass it to the SDK in order to display the notification:

{% code title="JavaScript" %}

```javascript
Replies.showNotificationAndroid(data);
```

{% endcode %}

**Configure Channels**

You can use channels to group the incoming Luciq notifications into a manageable group. To do this, pass the channel ID to the API below:

{% code title="JavaScript" %}

```javascript
Replies.setPushNotificationChannelIdAndroid('CHANNEL_ID');
```

{% endcode %}

**Change Notification Icon**

The icon that is shown with each push notification can be changed to match your application's icon. Use the API below to change this icon:

{% code title="JavaScript" %}

```javascript
Replies.setNotificationIconAndroid(ICON);
```

{% endcode %}

**Enabling/Disabling Push Notifications**

Push Notifications are enabled by default, but they can be turned on and off via the following API:

{% code title="JavaScript" %}

```javascript
// Enable
Replies.setPushNotificationsEnabled(true);

// Disable
Replies.setPushNotificationsEnabled(false);
```

{% endcode %}
{% endtab %}
{% endtabs %}

### In-App Notifications

By default, a notification will be shown on top of your app's UI when a new message is received.

#### Disabling In-App Notifications

Use the following method to disable notifications that appear in-app.

{% code title="React Native" %}

```javascript
Replies.setInAppNotificationsEnabled(false);
```

{% endcode %}

#### In-App Notification Sound

When your app users receive an in-app notification through Luciq, sound is enabled by default. You can disable it by using the following method.

{% code title="JavaScript" %}

```javascript
Replies.setInAppNotificationSound(false);
```

{% endcode %}

### Get Unread Messages Count

You can use the following method to get the number of messages the user has yet to read.

{% code title="JavaScript" %}

```javascript
const unreadRepliesCount = await Replies.getUnreadRepliesCount();
```

{% endcode %}
