# Source: https://firebase.google.com/docs/cloud-messaging/ios/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/doc-revamp/targeting-user-groups/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/cpp/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/unity/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/js/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/flutter/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/android/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/unity/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/js/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/flutter/topic-messaging.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/android/topic-messaging.md.txt

Based on the publish/subscribe model,FCMtopic messaging allows you to send a message to multiple devices that have opted in to a particular topic. You compose topic messages as needed, andFCMhandles routing and delivering the message reliably to the right devices.

For example, users of a local tide forecasting app could opt in to a "tidal currents alerts" topic and receive notifications of optimal saltwater fishing conditions in specified areas. Users of a sports app could subscribe to automatic updates in live game scores for their favorite teams.

Some things to keep in mind about topics:

- Topic messaging is best suited for content such as weather, or other publicly available information.
- Topic messages are**optimized for throughput rather than latency** . For fast, secure delivery to single devices or small groups of devices,[target messages to registration tokens](https://firebase.google.com/docs/cloud-messaging/send-message#send_messages_to_specific_devices), not topics.
- If you need to send messages to multiple devices*per user* , consider[device group messaging](https://firebase.google.com/docs/cloud-messaging/send-message#send_messages_to_device_groups)for those use cases.
- Topic messaging supports unlimited subscriptions for each topic. However,FCMenforces limits in these areas:
  - One app instance can be subscribed to no more than 2000 topics.
  - If you are using[batch import](https://developers.google.com/instance-id/reference/server#manage_relationship_maps_for_multiple_app_instances)to subscribe app instances, each request is limited to 1000 app instances.
  - The frequency of new subscriptions is rate-limited per project. If you send too many subscription requests in a short period of time,FCMservers will respond with a`429 RESOURCE_EXHAUSTED`("quota exceeded") response. Retry with exponential backoff.

## Subscribe the client app to a topic

Client apps can subscribe to any existing topic, or they can create a new topic. When a client app subscribes to a new topic name (one that does not already exist for your Firebase project), a new topic of that name is created inFCMand any client can subsequently subscribe to it.

To subscribe to a topic, the client app callsFirebase Cloud Messaging`subscribeToTopic()`with theFCMtopic name. This method returns a`Task`, which can be used by a completion listener to determine whether the subscription succeeded:  

### Kotlin

```kotlin
Firebase.messaging.subscribeToTopic("weather")
    .addOnCompleteListener { task ->
        var msg = "Subscribed"
        if (!task.isSuccessful) {
            msg = "Subscribe failed"
        }
        Log.d(TAG, msg)
        Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
    }https://github.com/firebase/snippets-android/blob/97ab79d91fc78d648116df9e3eba6a3fdc73f39b/messaging/app/src/main/java/com/google/firebase/example/messaging/kotlin/MainActivity.kt#L76-L84
```

### Java

```java
FirebaseMessaging.getInstance().subscribeToTopic("weather")
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                String msg = "Subscribed";
                if (!task.isSuccessful()) {
                    msg = "Subscribe failed";
                }
                Log.d(TAG, msg);
                Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show();
            }
        });https://github.com/firebase/snippets-android/blob/97ab79d91fc78d648116df9e3eba6a3fdc73f39b/messaging/app/src/main/java/com/google/firebase/example/messaging/MainActivity.java#L77-L88
```

To unsubscribe, the client app callsFirebase Cloud Messaging`unsubscribeFromTopic()`with the topic name.

## Manage topic subscriptions on the server

The[FirebaseAdmin SDK](https://firebase.google.com/docs/admin/setup)allows you to perform basic topic management tasks from the server side. Given their registration token(s), you can subscribe and unsubscribe client app instances in bulk using server logic.

You can subscribe client app instances to any existing topic, or you can create a new topic. When you use the API to subscribe a client app to a new topic (one that does not already exist for your Firebase project), a new topic of that name is created in FCM and any client can subsequently subscribe to it.

You can pass a list of registration tokens to theFirebaseAdmin SDKsubscription method to subscribe the corresponding devices to a topic:  

### Node.js

    // These registration tokens come from the client FCM SDKs.
    const registrationTokens = [
      'YOUR_REGISTRATION_TOKEN_1',
      // ...
      'YOUR_REGISTRATION_TOKEN_n'
    ];

    // Subscribe the devices corresponding to the registration tokens to the
    // topic.
    getMessaging().subscribeToTopic(registrationTokens, topic)
      .then((response) => {
        // See the MessagingTopicManagementResponse reference documentation
        // for the contents of response.
        console.log('Successfully subscribed to topic:', response);
      })
      .catch((error) => {
        console.log('Error subscribing to topic:', error);
      });

### Java

    // These registration tokens come from the client FCM SDKs.
    List<String> registrationTokens = Arrays.asList(
        "YOUR_REGISTRATION_TOKEN_1",
        // ...
        "YOUR_REGISTRATION_TOKEN_n"
    );

    // Subscribe the devices corresponding to the registration tokens to the
    // topic.
    TopicManagementResponse response = FirebaseMessaging.getInstance().subscribeToTopic(
        registrationTokens, topic);
    // See the TopicManagementResponse reference documentation
    // for the contents of response.
    System.out.println(response.getSuccessCount() + " tokens were subscribed successfully");

### Python

    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        # ...
        'YOUR_REGISTRATION_TOKEN_n',
    ]

    # Subscribe the devices corresponding to the registration tokens to the
    # topic.
    response = messaging.subscribe_to_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were subscribed successfully')

### Go

    // These registration tokens come from the client FCM SDKs.
    registrationTokens := []string{
    	"YOUR_REGISTRATION_TOKEN_1",
    	// ...
    	"YOUR_REGISTRATION_TOKEN_n",
    }

    // Subscribe the devices corresponding to the registration tokens to the
    // topic.
    response, err := client.SubscribeToTopic(ctx, registrationTokens, topic)
    if err != nil {
    	log.Fatalln(err)
    }
    // See the TopicManagementResponse reference documentation
    // for the contents of response.
    fmt.Println(response.SuccessCount, "tokens were subscribed successfully")

### C#

    // These registration tokens come from the client FCM SDKs.
    var registrationTokens = new List<string>()
    {
        "YOUR_REGISTRATION_TOKEN_1",
        // ...
        "YOUR_REGISTRATION_TOKEN_n",
    };

    // Subscribe the devices corresponding to the registration tokens to the
    // topic
    var response = await FirebaseMessaging.DefaultInstance.SubscribeToTopicAsync(
        registrationTokens, topic);
    // See the TopicManagementResponse reference documentation
    // for the contents of response.
    Console.WriteLine($"{response.SuccessCount} tokens were subscribed successfully");  
    https://github.com/firebase/firebase-admin-dotnet/blob/edbd92d3b9ec6d1292e3931fa9dd06f0e3f8ab91/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L327-L341

| **Important:** To use the AdminFCMAPI, you must first follow the steps in[Add the Firebase Admin SDK to your Server](https://firebase.google.com/docs/admin/setup)to initialize the SDK.

The AdminFCMAPI also allows you to unsubscribe devices from a topic by passing registration tokens to the appropriate method:  

### Node.js

    // These registration tokens come from the client FCM SDKs.
    const registrationTokens = [
      'YOUR_REGISTRATION_TOKEN_1',
      // ...
      'YOUR_REGISTRATION_TOKEN_n'
    ];

    // Unsubscribe the devices corresponding to the registration tokens from
    // the topic.
    getMessaging().unsubscribeFromTopic(registrationTokens, topic)
      .then((response) => {
        // See the MessagingTopicManagementResponse reference documentation
        // for the contents of response.
        console.log('Successfully unsubscribed from topic:', response);
      })
      .catch((error) => {
        console.log('Error unsubscribing from topic:', error);
      });

### Java

    // These registration tokens come from the client FCM SDKs.
    List<String> registrationTokens = Arrays.asList(
        "YOUR_REGISTRATION_TOKEN_1",
        // ...
        "YOUR_REGISTRATION_TOKEN_n"
    );

    // Unsubscribe the devices corresponding to the registration tokens from
    // the topic.
    TopicManagementResponse response = FirebaseMessaging.getInstance().unsubscribeFromTopic(
        registrationTokens, topic);
    // See the TopicManagementResponse reference documentation
    // for the contents of response.
    System.out.println(response.getSuccessCount() + " tokens were unsubscribed successfully");

### Python

    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        # ...
        'YOUR_REGISTRATION_TOKEN_n',
    ]

    # Unubscribe the devices corresponding to the registration tokens from the
    # topic.
    response = messaging.unsubscribe_from_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were unsubscribed successfully')

### Go

    // These registration tokens come from the client FCM SDKs.
    registrationTokens := []string{
    	"YOUR_REGISTRATION_TOKEN_1",
    	// ...
    	"YOUR_REGISTRATION_TOKEN_n",
    }

    // Unsubscribe the devices corresponding to the registration tokens from
    // the topic.
    response, err := client.UnsubscribeFromTopic(ctx, registrationTokens, topic)
    if err != nil {
    	log.Fatalln(err)
    }
    // See the TopicManagementResponse reference documentation
    // for the contents of response.
    fmt.Println(response.SuccessCount, "tokens were unsubscribed successfully")

### C#

    // These registration tokens come from the client FCM SDKs.
    var registrationTokens = new List<string>()
    {
        "YOUR_REGISTRATION_TOKEN_1",
        // ...
        "YOUR_REGISTRATION_TOKEN_n",
    };

    // Unsubscribe the devices corresponding to the registration tokens from the
    // topic
    var response = await FirebaseMessaging.DefaultInstance.UnsubscribeFromTopicAsync(
        registrationTokens, topic);
    // See the TopicManagementResponse reference documentation
    // for the contents of response.
    Console.WriteLine($"{response.SuccessCount} tokens were unsubscribed successfully");  
    https://github.com/firebase/firebase-admin-dotnet/blob/edbd92d3b9ec6d1292e3931fa9dd06f0e3f8ab91/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L348-L362

| **Note:** You can subscribe or unsubscribe up to 1,000 devices in a single request. If you provide an array with over 1,000 registration tokens, the request will fail with a`messaging/invalid-argument`error.

The`subscribeToTopic()`and`unsubscribeFromTopic()`methods results in an object containing the response fromFCM. The return type has the same format regardless of the number of registration tokens specified in the request.

In case of an error (authentication failures, invalid token or topic etc.) these methods result in an error. For a full list of error codes, including descriptions and resolution steps, see[AdminFCMAPI Errors](https://firebase.google.com/docs/cloud-messaging/send-message#admin_sdk_error_reference).

## Receive and handle topic messages

FCMdelivers topic messages in the same way as other downstream messages.

To receive messages, use a service that extends[`FirebaseMessagingService`](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/FirebaseMessagingService). Your service should override the`onMessageReceived`and`onDeletedMessages`callbacks.

`onMessageReceived`is provided for most message types, with the following exceptions:

<br />

- **Notification messages delivered when your app is in the background**. In this case, the notification is delivered to the device's system tray. A user tap on a notification opens the app launcher by default.

- **Messages with both notification and data payload, when received in the background**. In this case, the notification is delivered to the device's system tray, and the data payload is delivered in the extras of the intent of your launcher Activity.

In summary:

| App state  |    Notification     |        Data         |                           Both                           |
|------------|---------------------|---------------------|----------------------------------------------------------|
| Foreground | `onMessageReceived` | `onMessageReceived` | `onMessageReceived`                                      |
| Background | System tray         | `onMessageReceived` | Notification: system tray Data: in extras of the intent. |

For more information about message types, see[Notifications and data messages](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type).Your service should handle any message within 10 seconds of receipt.

The`onMessageReceived`callback is given timeouts that enable you to simply post a notification but the timers are not designed to allow the app to access the network or to do additional work. As such, if your app does anything more complicated, you need to do additional work to ensure the app can complete its work.

If you expect your app could require close to 10 seconds to handle a message, you should[schedule a WorkManager job](https://firebase.google.com/docs/cloud-messaging/android/message-priority#message-processing)or follow the[WakeLock guidance below](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging#keep-the-device-awake-while-handling-fcm-messages). In some cases, the time window for handling a message may be shorter than 10 seconds depending on delays incurred ahead of calling`onMessageReceived`, including OS delays, app startup time, the main thread being blocked by other operations, or previous`onMessageReceived`calls taking too long. After that timer expires, your app may be subject to[process killing](https://developer.android.com/guide/components/activities/process-lifecycle)or[background execution limits](https://developer.android.com/about/versions/oreo/background). Keep in mind, latencies for network transactions and app startup can be significant, so when in doubt, plan for your message processing to run long if there are any asynchronous dependencies such as network access or intensive data loading requirements.

### Edit the app manifest

To use`FirebaseMessagingService`, you need to add the following in your app manifest:  

```gdscript
<service
    android:name=".java.MyFirebaseMessagingService"
    android:exported="false">
    <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
    </intent-filter>
</service>  
https://github.com/firebase/quickstart-android/blob/729356b9111f97489d2de0a4c68fac450169e010/messaging/app/src/main/AndroidManifest.xml#L50-L56
```

Also, you're recommended to set default values to customize the appearance of notifications. You can specify a custom default icon and a custom default color that are applied whenever equivalent values are not set in the notification payload.

Add these lines inside the`application`tag to set the custom default icon and custom color:  

```transact-sql
<!-- Set custom default icon. This is used when no icon is set for incoming notification messages.
     See README(https://goo.gl/l4GJaQ) for more. -->
<meta-data
    android:name="com.google.firebase.messaging.default_notification_icon"
    android:resource="@drawable/ic_stat_ic_notification" />
<!-- Set color used with incoming notification messages. This is used when no color is set for the incoming
     notification message. See README(https://goo.gl/6BKBk7) for more. -->
<meta-data
    android:name="com.google.firebase.messaging.default_notification_color"
    android:resource="@color/colorAccent" />https://github.com/firebase/quickstart-android/blob/729356b9111f97489d2de0a4c68fac450169e010/messaging/app/src/main/AndroidManifest.xml#L12-L21
```

Android displays the custom default icon for

- All notification messages sent from the[Notifications composer](https://console.firebase.google.com/project/_/notification).
- Any notification message that does not explicitly set the icon in the notification payload.

Android uses the custom default color for

- All notification messages sent from the[Notifications composer](https://console.firebase.google.com/project/_/notification).
- Any notification message that does not explicitly set the color in the notification payload.

If no custom default icon is set and no icon is set in the notification payload, Android displays the application icon rendered in white.

### Override`onMessageReceived`

By overriding the method`FirebaseMessagingService.onMessageReceived`, you can perform actions based on the received[RemoteMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage)object and get the message data:  

### Kotlin

```kotlin
override fun onMessageReceived(remoteMessage: RemoteMessage) {
    // TODO(developer): Handle FCM messages here.
    // Not getting messages here? See why this may be: https://goo.gl/39bRNJ
    Log.d(TAG, "From: ${remoteMessage.from}")

    // Check if message contains a data payload.
    if (remoteMessage.data.isNotEmpty()) {
        Log.d(TAG, "Message data payload: ${remoteMessage.data}")

        // Check if data needs to be processed by long running job
        if (needsToBeScheduled()) {
            // For long-running tasks (10 seconds or more) use WorkManager.
            scheduleJob()
        } else {
            // Handle message within 10 seconds
            handleNow()
        }
    }

    // Check if message contains a notification payload.
    remoteMessage.notification?.let {
        Log.d(TAG, "Message Notification Body: ${it.body}")
    }

    // Also if you intend on generating your own notifications as a result of a received FCM
    // message, here is where that should be initiated. See sendNotification method below.
}https://github.com/firebase/snippets-android/blob/97ab79d91fc78d648116df9e3eba6a3fdc73f39b/messaging/app/src/main/java/com/google/firebase/example/messaging/kotlin/MyFirebaseMessagingService.kt#L23-L49
```

### Java

```java
@Override
public void onMessageReceived(RemoteMessage remoteMessage) {
    // TODO(developer): Handle FCM messages here.
    // Not getting messages here? See why this may be: https://goo.gl/39bRNJ
    Log.d(TAG, "From: " + remoteMessage.getFrom());

    // Check if message contains a data payload.
    if (remoteMessage.getData().size() > 0) {
        Log.d(TAG, "Message data payload: " + remoteMessage.getData());

        if (/* Check if data needs to be processed by long running job */ true) {
            // For long-running tasks (10 seconds or more) use WorkManager.
            scheduleJob();
        } else {
            // Handle message within 10 seconds
            handleNow();
        }

    }

    // Check if message contains a notification payload.
    if (remoteMessage.getNotification() != null) {
        Log.d(TAG, "Message Notification Body: " + remoteMessage.getNotification().getBody());
    }

    // Also if you intend on generating your own notifications as a result of a received FCM
    // message, here is where that should be initiated. See sendNotification method below.
}https://github.com/firebase/snippets-android/blob/97ab79d91fc78d648116df9e3eba6a3fdc73f39b/messaging/app/src/main/java/com/google/firebase/example/messaging/MyFirebaseMessagingService.java#L28-L55
```

### Keep the device awake while handling FCM messages

If your app needs to keep the device awake while processing an FCM message, then it will need to hold a WakeLock during this time or it will need to create a WorkManager job. WakeLocks work well for short processing activities that might exceed the`onMessageReceived`default timeouts. For extended workflows, such as sending multiple serial RPCs to your servers, using a WorkManager job is more appropriate than a WakeLock. In this section we focus on how to use WakeLocks. A WakeLock prevents the device from sleeping while your app is running, which can result in increased battery use, so use of WakeLocks should be reserved for cases where your app should not be paused while handling the message such as:

- Notifications to the user that are time sensitive.
- Interactions with something off device that shouldn't be interrupted (such as network transfers or communications with another device, like a paired watch).

First you'll need to make sure that your app requests the WakeLock permission (the FCM SDK includes this by default, so normally nothing needs to be added).  

```
<uses-permission android:name="android.permission.WAKE_LOCK" />
```

Then your app will need to acquire a WakeLock at the start of the`FirebaseMessagingService.onMessageReceived()`callback and release it at the end of the callback.

App's custom`FirebaseMessagingService`:  

```
@Override
public void onMessageReceived(final RemoteMessage message) {
  // If this is a message that is time sensitive or shouldn't be interrupted
  WakeLock wakeLock = getSystemService(PowerManager.class).newWakeLock(PARTIAL_WAKE_LOCK, "myApp:messageReceived");
  try {
    wakeLock.acquire(TIMEOUT_MS);
    // handle message
    ...
  finally {
    wakeLock.release();
  }
}
```

### Override`onDeletedMessages`

In some situations,FCMmay not deliver a message. This occurs when there are too many messages (\>100) pending for your app on a particular device at the time it connects or if the device hasn't connected toFCMin more than one month. In these cases, you may receive a callback to`FirebaseMessagingService.onDeletedMessages()`When the app instance receives this callback, it should perform a full sync with your app server. If you haven't sent a message to the app on that device within the last 4 weeks,FCMwon't call`onDeletedMessages()`.

### Handle notification messages in a backgrounded app

When your app is in the background, Android directs notification messages to the system tray. A user tap on the notification opens the app launcher by default.

This includes messages that contain both notification and data payload (and all messages sent from the Notifications console). In these cases, the notification is delivered to the device's system tray, and the data payload is delivered in the extras of the intent of your launcher Activity.

For insight into message delivery to your app, see the[FCMreporting dashboard](https://console.firebase.google.com/project/_/notification/reporting), which records the number of messages sent and opened on Apple and Android devices, along with data for "impressions" (notifications seen by users) for Android apps.

## Build send requests

After you have created a topic, either by subscribing client app instances to the topic on the client side or via the[server API](https://firebase.google.com/docs/cloud-messaging/manage-topics), you can send messages to the topic. If this is your first time building send requests forFCM, see the guide to[your server environment andFCM](https://firebase.google.com/docs/cloud-messaging/server)for important background and setup information.

In your sending logic on the backend, specify the desired topic name as shown:  

### Node.js

    // The topic name can be optionally prefixed with "/topics/".
    const topic = 'highScores';

    const message = {
      data: {
        score: '850',
        time: '2:45'
      },
      topic: topic
    };

    // Send a message to devices subscribed to the provided topic.
    getMessaging().send(message)
      .then((response) => {
        // Response is a message ID string.
        console.log('Successfully sent message:', response);
      })
      .catch((error) => {
        console.log('Error sending message:', error);
      });

### Java

    // The topic name can be optionally prefixed with "/topics/".
    String topic = "highScores";

    // See documentation on defining a message payload.
    Message message = Message.builder()
        .putData("score", "850")
        .putData("time", "2:45")
        .setTopic(topic)
        .build();

    // Send a message to the devices subscribed to the provided topic.
    String response = FirebaseMessaging.getInstance().send(message);
    // Response is a message ID string.
    System.out.println("Successfully sent message: " + response);  
    https://github.com/firebase/firebase-admin-java/blob/800298c46df2d77eaa089e0cfcfcf48c1b3b19fa/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L66-L79

### Python

    # The topic name can be optionally prefixed with "/topics/".
    topic = 'highScores'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        topic=topic,
    )

    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)  
    https://github.com/firebase/firebase-admin-python/blob/f85a8de1b5d9a252971827d2a6c075d59d564004/snippets/messaging/cloud_messaging.py#L46-L61

### Go

    // The topic name can be optionally prefixed with "/topics/".
    topic := "highScores"

    // See documentation on defining a message payload.
    message := &messaging.Message{
    	Data: map[string]string{
    		"score": "850",
    		"time":  "2:45",
    	},
    	Topic: topic,
    }

    // Send a message to the devices subscribed to the provided topic.
    response, err := client.Send(ctx, message)
    if err != nil {
    	log.Fatalln(err)
    }
    // Response is a message ID string.
    fmt.Println("Successfully sent message:", response)  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/messaging.go#L61-L79

### C#

    // The topic name can be optionally prefixed with "/topics/".
    var topic = "highScores";

    // See documentation on defining a message payload.
    var message = new Message()
    {
        Data = new Dictionary<string, string>()
        {
            { "score", "850" },
            { "time", "2:45" },
        },
        Topic = topic,
    };

    // Send a message to the devices subscribed to the provided topic.
    string response = await FirebaseMessaging.DefaultInstance.SendAsync(message);
    // Response is a message ID string.
    Console.WriteLine("Successfully sent message: " + response);

### REST

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

    Content-Type: application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA
    {
      "message":{
        "topic" : "foo-bar",
        "notification" : {
          "body" : "This is a Firebase Cloud Messaging Topic Message!",
          "title" : "FCM Message"
          }
       }
    }

cURL command:  

    curl -X POST -H "Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA" -H "Content-Type: application/json" -d '{
      "message": {
        "topic" : "foo-bar",
        "notification": {
          "body": "This is a Firebase Cloud Messaging Topic Message!",
          "title": "FCM Message"
        }
      }
    }' https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

To send a message to a*combination* of topics, specify a*condition* , which is a boolean expression that specifies the target topics. For example, the following condition will send messages to devices that are subscribed to`TopicA`and either`TopicB`or`TopicC`:  

    "'TopicA' in topics && ('TopicB' in topics || 'TopicC' in topics)"

FCMfirst evaluates any conditions in parentheses, and then evaluates the expression from left to right. In the above expression, a user subscribed to any single topic does not receive the message. Likewise, a user who does not subscribe to`TopicA`does not receive the message. These combinations do receive it:

- `TopicA`and`TopicB`
- `TopicA`and`TopicC`

You can include up to five topics in your conditional expression.

**To send to a condition:**  

### Node.js

    // Define a condition which will send to devices which are subscribed
    // to either the Google stock or the tech industry topics.
    const condition = '\'stock-GOOG\' in topics || \'industry-tech\' in topics';

    // See documentation on defining a message payload.
    const message = {
      notification: {
        title: '$FooCorp up 1.43% on the day',
        body: '$FooCorp gained 11.80 points to close at 835.67, up 1.43% on the day.'
      },
      condition: condition
    };

    // Send a message to devices subscribed to the combination of topics
    // specified by the provided condition.
    getMessaging().send(message)
      .then((response) => {
        // Response is a message ID string.
        console.log('Successfully sent message:', response);
      })
      .catch((error) => {
        console.log('Error sending message:', error);
      });

### Java

    // Define a condition which will send to devices which are subscribed
    // to either the Google stock or the tech industry topics.
    String condition = "'stock-GOOG' in topics || 'industry-tech' in topics";

    // See documentation on defining a message payload.
    Message message = Message.builder()
        .setNotification(Notification.builder()
            .setTitle("$GOOG up 1.43% on the day")
            .setBody("$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.")
            .build())
        .setCondition(condition)
        .build();

    // Send a message to devices subscribed to the combination of topics
    // specified by the provided condition.
    String response = FirebaseMessaging.getInstance().send(message);
    // Response is a message ID string.
    System.out.println("Successfully sent message: " + response);  
    https://github.com/firebase/firebase-admin-java/blob/800298c46df2d77eaa089e0cfcfcf48c1b3b19fa/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L85-L102

### Python

    # Define a condition which will send to devices which are subscribed
    # to either the Google stock or the tech industry topics.
    condition = "'stock-GOOG' in topics || 'industry-tech' in topics"

    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title='$GOOG up 1.43% on the day',
            body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
        ),
        condition=condition,
    )

    # Send a message to devices subscribed to the combination of topics
    # specified by the provided condition.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)  
    https://github.com/firebase/firebase-admin-python/blob/f85a8de1b5d9a252971827d2a6c075d59d564004/snippets/messaging/cloud_messaging.py#L67-L84

### Go

    // Define a condition which will send to devices which are subscribed
    // to either the Google stock or the tech industry topics.
    condition := "'stock-GOOG' in topics || 'industry-tech' in topics"

    // See documentation on defining a message payload.
    message := &messaging.Message{
    	Data: map[string]string{
    		"score": "850",
    		"time":  "2:45",
    	},
    	Condition: condition,
    }

    // Send a message to devices subscribed to the combination of topics
    // specified by the provided condition.
    response, err := client.Send(ctx, message)
    if err != nil {
    	log.Fatalln(err)
    }
    // Response is a message ID string.
    fmt.Println("Successfully sent message:", response)  
    https://github.com/firebase/firebase-admin-go/blob/26dec0b7589ef7641eefd6681981024079b8524c/snippets/messaging.go#L85-L105

### C#

    // Define a condition which will send to devices which are subscribed
    // to either the Google stock or the tech industry topics.
    var condition = "'stock-GOOG' in topics || 'industry-tech' in topics";

    // See documentation on defining a message payload.
    var message = new Message()
    {
        Notification = new Notification()
        {
            Title = "$GOOG up 1.43% on the day",
            Body = "$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.",
        },
        Condition = condition,
    };

    // Send a message to devices subscribed to the combination of topics
    // specified by the provided condition.
    string response = await FirebaseMessaging.DefaultInstance.SendAsync(message);
    // Response is a message ID string.
    Console.WriteLine("Successfully sent message: " + response);

### REST

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

    Content-Type: application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA
    {
       "message":{
        "condition": "'dogs' in topics || 'cats' in topics",
        "notification" : {
          "body" : "This is a Firebase Cloud Messaging Topic Message!",
          "title" : "FCM Message",
        }
      }
    }

cURL command:  

    curl -X POST -H "Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA" -H "Content-Type: application/json" -d '{
      "notification": {
        "title": "FCM Message",
        "body": "This is a Firebase Cloud Messaging Topic Message!",
      },
      "condition": "'dogs' in topics || 'cats' in topics"
    }' https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

## Next steps

- Learn more about the other way to send to multiple devices ---[device group messaging](https://firebase.google.com/docs/cloud-messaging/android/device-group)