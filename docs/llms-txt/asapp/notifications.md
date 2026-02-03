# Source: https://docs.asapp.com/agent-desk/integrations/android-sdk/notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Notifications

ASAPP provides the following notifications:

* [Push Notifications](#push-notifications "Push Notifications")
* [Persistent Notifications](#persistent-notifications "Persistent Notifications")

## Push Notifications

ASAPP's systems may trigger push notifications at certain times, such as when an agent sends a message to an end customer who does not currently have the chat interface open. In such scenarios, ASAPP calls your company's API with data that identifies the recipient's device, which triggers push notifications. ASAPP's servers do not communicate with Firebase directly.

ASAPP provides methods in the SDK to register and deregister the customer's device for push notifications.

For a deeper dive on how ASAPP and your company's API handle push notifications, please see our documentation on [Push Notifications and the Mobile SDKs](../push-notifications-and-the-mobile-sdks "Push Notifications and the Mobile SDKs").

In addition to this section, see Android's documentation about [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) and specifically how to setup [Android Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/android/client).

### Enable Push Notifications

1. Identify which token you will use to send push notifications to the current user. This token is usually either the Firebase instance ID or an identifier that your company's API generates for this purpose.
2. Then, register the push notification token using:

   ```kotlin  theme={null}
   ASAPP.instance.updatePushNotificationsToken(newToken: String)
   ```

   In case you issue a new token to the current user, you also need to update it in the SDK.

### Disable Push Notifications

In case the user logs out of the application or other related scenarios, you can disable push notifications for the current user by calling:

`ASAPP.instance.disablePushNotifications().`

<Note>
  Call this function before you change `ASAPP.instance.user` (or clear the session) to prevent the customer from receiving unintended push notifications.
</Note>

### Handle Push Notifications

You can verify if ASAPP triggered a push notification and passed a data payload into the SDK.

<Note>
  Your application usually won't receive push notifications from ASAPP if the identified user for this device is connected to chat.
</Note>

For a deeper dive on how Android handles push notifications, please see the Firebase docs on [Receiving Messages in Android](https://firebase.google.com/docs/cloud-messaging/android/receive).

#### Background Push Notifications

If your app receives a push notification while in the background or closed, the system displays the OS notification. Once the user taps the notification, the app starts with `Intent` data from that push notification.

To help differentiate notifications from ASAPP and others your app might receive, ASAPP recommends that the push notification has a `click_action` with the value `asapp.intent.action.OPEN_CHAT`. For more information on how to set a click action, please see the [Firebase documentation](https://firebase.google.com/docs/cloud-messaging/http-server-ref#notification-payload-support). With a click action set to the push notification, you will need to add a new intent filter to match it:

```xml  theme={null}
<activity android:name=".HomeActivity">
    <intent-filter>
        <action android:name="asapp.intent.action.OPEN_CHAT" />
        <category android:name="android.intent.category.DEFAULT" />
    </intent-filter>
</activity>
```

Once you create the activity, check if it's an ASAPP notification, and then open chat with the data:

```kotlin  theme={null}
if (ASAPP.instance.shouldOpenChat(intent)) {
    ASAPP.instance.openChat(context = this, androidIntentExtras = intent.extras)
}
```

The helper function [`shouldOpenChat`](https://docs-sdk.asapp.com/api/chatsdk/android/latest/chatsdk/com.asapp.chatsdk/-a-s-a-p-p/should-open-chat.html) simply checks if the intent action matches the recommended one, but its use is optional.

#### Foreground Push Notifications

When you receive Firebase push notifications while your app is in the foreground, it calls `FirebaseMessagingService.onMessageReceived`. Check if that notification is from ASAPP:

```kotlin  theme={null}
class MyFirebaseMessagingService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        super.onMessageReceived(message)
        val wasFromAsapp = ASAPP.instance.onFirebaseMessageReceived(message)
        // ...
    }
}
```

For a good user experience, ASAPP recommends providing UI feedback to indicate there are new messages instead of opening chat right away. For example, update the unread message counter for your app's chat badge. You can retrieve that information from: `ASAPP.instance.conversationStatusHandler`.

## Persistent Notifications

<Frame>
  <img src="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png?fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=8f0e48558beee1803e84ea639bace5fe" data-og-width="866" width="866" data-og-height="1035" height="1035" data-path="image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png?w=280&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=ee372d34b51b8c93ade7c4d3206a8ec1 280w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png?w=560&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=aa1f2d5910e26cdbae9ddcd6b593afa7 560w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png?w=840&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=e510d9bcf460f32aef1d023c233ba385 840w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png?w=1100&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=a83ded2756682bf490de049247af44a1 1100w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png?w=1650&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=0f0db31724cb3bbfd2bc38abfddac1bc 1650w, https://mintcdn.com/asapp/AXwA7-nbwQCJ8xte/image/uuid-e28f9066-d931-3745-9a1b-d2f2ff3703a6.png?w=2500&fit=max&auto=format&n=AXwA7-nbwQCJ8xte&q=85&s=278ef7f96721184a5004e80d80493390 2500w" />
</Frame>

The ASAPP Android SDK automatically surfaces a persistent notification when a user joins a queue or connects to a live agent (starting on v8.4.0). Tapping the notification triggers an intent that takes the user directly into ASAPP Chat. Once the live chat ends or the user leaves the queue, the SDK dismisses the notification.

Persistent notifications are:

* ongoing, not dismissible [notifications](https://developer.android.com/reference/android/app/Notification).
* low priority and do not vibrate or make sounds.
* managed directly by the SDK and do not require integration changes.

ASAPP enables this feature by default. To disable it, please reach out to your ASAPP Implementation Manager.

<Note>
  Persistent notifications are not push notifications, which are created and handled by your application.
</Note>

### Customize Persistent Notifications

#### Notification Title and Icon

<Frame>
  <img src="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png?fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=191ba58513a8529d25035401cdb29f52" data-og-width="1270" width="1270" data-og-height="389" height="389" data-path="image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png?w=280&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=424535d93f6ac64f4b9ca74daec16ee2 280w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png?w=560&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=a60da771f3b6de7835d9bb5083797698 560w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png?w=840&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=6d508ff9ba8964991bf23c7fd4f4cae5 840w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png?w=1100&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3059b6b485e09930ee67108b99558afa 1100w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png?w=1650&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=3b9f0195d95dee09892b59fddb7a337b 1650w, https://mintcdn.com/asapp/NE5s_J_rgoRPqQQt/image/uuid-4796925b-926a-e198-230a-a7aa157a3e21.png?w=2500&fit=max&auto=format&n=NE5s_J_rgoRPqQQt&q=85&s=19515aca5fbdede5049d4d069c4b7c61 2500w" />
</Frame>

To customize the title of persistent notifications, override the following string resource:

```json  theme={null}
<string name="asapp_persistent_notification_title">Chat for Customer Support</string>
```

And to customize the icon, create a new drawable resource with the following identifier (file name):

```json  theme={null}
drawable/asapp_ic_contact_support.xml
```

ASAPP recommends that you do not change the body of persistent notifications.

#### Notification Channel

By default, ASAPP sets the notification to [Notification Channel](https://developer.android.com/reference/android/app/NotificationChannel) `asapp_chat`, but it is possible to customize the channel being used.

To customize the channel used by persistent notifications, override the following string resources:

```json  theme={null}
<string name="asapp_persistent_notification_channel_id">asapp_chat</string>
<string name="asapp_persistent_notification_channel_name">Chat for Customer Support</string>
```
