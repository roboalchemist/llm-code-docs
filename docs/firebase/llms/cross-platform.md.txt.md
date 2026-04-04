# Source: https://firebase.google.com/docs/cloud-messaging/customize-messages/cross-platform.md.txt

The [Firebase Admin SDK](https://firebase.google.com/docs/cloud-messaging/send/admin-sdk) and the [FCM v1
HTTP API](https://firebase.google.com/docs/cloud-messaging/send/v1-api) lets your message requests to set
all fields available in the
[`message`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Message) object. This
includes:

- a common set of fields to be interpreted by **all** app instances that receive the message.
- platform-specific sets of fields, such as `AndroidConfig` and `WebpushConfig`, interpreted only by app instances running on the specified platform.

Platform-specific blocks give you flexibility to customize messages for
different platforms to ensure that they are handled correctly when received. The
FCM backend will take all specified parameters into account and customize the
message for each platform.

## When to use common fields

Use common fields when you're:

- Send fields to any platform
- Send messages to topics

All app instances, regardless of platform, can interpret the following common
fields:

- [`message.notification.title`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Notification.FIELDS.title)
- [`message.notification.body`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Notification.FIELDS.body)
- [`message.data`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#Message.FIELDS.data)

## When to use platform-specific fields

Use platform-specific fields when you want to:

- Send fields only to particular platforms
- Send platform-specific fields *in addition to* the common fields

Whenever you want to send values only to particular platforms, use
platform-specific fields. For example, to send a notification only to Apple and
Web platforms but not to Android, you must use two separate sets of fields, one
for Apple and one for Web.

When you are sending messages with specific delivery options, use
platform-specific fields to set them. You can specify different values per
platform if you want. However, even when you want to set essentially the same
value across platforms, you must use platform-specific fields. This is because
each platform may interpret the value slightly differently---for example,
time to live is set on Android as an expiration time in seconds, while on Apple
it is set as an expiration *date*.

## Notification message with platform-specific delivery options

The following HTTP v1 API send request sends a common notification title and
content to all platforms, but also sends some platform-specific overrides.
Specifically, the request:

- sets a long time to live for Android and Web platforms, while setting the APNs (Apple platforms) message priority to a low setting
- sets the appropriate keys to define the result of a user tap on the notification on Android and Apple --- `click_action`, and `category`, respectively.

    {
      "message":{
         "token":"bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
         "notification":{
           "title":"Match update",
           "body":"Arsenal goal in added time, score is now 3-0"
         },
         "android":{
           "ttl":"86400s",
           "notification"{
             "click_action":"OPEN_ACTIVITY_1"
           }
         },
         "apns": {
           "headers": {
             "apns-priority": "5",
           },
           "payload": {
             "aps": {
               "category": "NEW_MESSAGE_CATEGORY"
             }
           }
         },
         "webpush":{
           "headers":{
             "TTL":"86400"
           }
         }
       }
     }

To learn more, see the [HTTP v1
reference](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages) page for more detail
on the keys available in platform-specific blocks in the message body. For more
information about building send requests that contain the message body, see
[Send a message using FCM HTTP v1 API](https://firebase.google.com/docs/cloud-messaging/send/v1-api).

## Notification message with color and icon options

In the following example, the send request sends a common notification title and
content to all platforms, but it also sends some platform-specific overrides to
Android devices.

For Android, the request sets a special icon and color to display on Android
devices. As noted in the reference for
[AndroidNotification](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidnotification),
the color is specified in #rrggbb format, and the image must be a drawable icon
resource local to the Android app.

Here's an example of the visual effect on a user's device:

![Simple drawing of two devices, with one displaying a custom icon and color](https://firebase.google.com/static/docs/cloud-messaging/images/Icon_Notification_v2.png)

### Node.js

    const topicName = 'industry-tech';

    const message = {
      notification: {
        title: '`$FooCorp` up 1.43% on the day',
        body: 'FooCorp gained 11.80 points to close at 835.67, up 1.43% on the day.'
      },
      android: {
        notification: {
          icon: 'stock_ticker_update',
          color: '#7e55c3'
        }
      },
      topic: topicName,
    };

    getMessaging().send(message)
      .then((response) => {
        // Response is a message ID string.
        console.log('Successfully sent message:', response);
      })
      .catch((error) => {
        console.log('Error sending message:', error);
      });

### Java

    Message message = Message.builder()
        .setNotification(Notification.builder()
            .setTitle("$GOOG up 1.43% on the day")
            .setBody("$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.")
            .build())
        .setAndroidConfig(AndroidConfig.builder()
            .setTtl(3600 * 1000)
            .setNotification(AndroidNotification.builder()
                .setIcon("stock_ticker_update")
                .setColor("#f45342")
                .build())
            .build())
        .setApnsConfig(ApnsConfig.builder()
            .setAps(Aps.builder()
                .setBadge(42)
                .build())
            .build())
        .setTopic("industry-tech")
        .build();https://github.com/firebase/firebase-admin-java/blob/d69dcbd9604ca2eb49c32d27067df4b70a126c87/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L320-L338

### Python

    message = messaging.Message(
        notification=messaging.Notification(
            title='$GOOG up 1.43% on the day',
            body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
        ),
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='normal',
            notification=messaging.AndroidNotification(
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        apns=messaging.APNSConfig(
            payload=messaging.APNSPayload(
                aps=messaging.Aps(badge=42),
            ),
        ),
        topic='industry-tech',
    )https://github.com/firebase/firebase-admin-python/blob/581ef26c3ea0964d44bbd77dfbae1940985c1300/snippets/messaging/cloud_messaging.py#L163-L182

### Go

    oneHour := time.Duration(1) * time.Hour
    badge := 42
    message := &messaging.Message{
    	Notification: &messaging.Notification{
    		Title: "$GOOG up 1.43% on the day",
    		Body:  "$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.",
    	},
    	Android: &messaging.AndroidConfig{
    		TTL: &oneHour,
    		Notification: &messaging.AndroidNotification{
    			Icon:  "stock_ticker_update",
    			Color: "#f45342",
    		},
    	},
    	APNS: &messaging.APNSConfig{
    		Payload: &messaging.APNSPayload{
    			Aps: &messaging.Aps{
    				Badge: &badge,
    			},
    		},
    	},
    	Topic: "industry-tech",
    }https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/messaging.go#L357-L379

### C#

    var message = new Message
    {
        Notification = new Notification()
        {
            Title = "$GOOG up 1.43% on the day",
            Body = "$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.",
        },
        Android = new AndroidConfig()
        {
            TimeToLive = TimeSpan.FromHours(1),
            Notification = new AndroidNotification()
            {
                Icon = "stock_ticker_update",
                Color = "#f45342",
            },
        },
        Apns = new ApnsConfig()
        {
            Aps = new Aps()
            {
                Badge = 42,
            },
        },
        Topic = "industry-tech",
    };https://github.com/firebase/firebase-admin-dotnet/blob/9d71ceb37ed2deaf22aed643d1dcfed759df9f9d/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L295-L319

### REST

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

    Content-Type: application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA
    {
      "message":{
         "topic":"industry-tech",
         "notification":{
           "title": "`$FooCorp` up 1.43% on the day",
           "body": "FooCorp gained 11.80 points to close at 835.67, up 1.43% on the day."
         },
         "android":{
           "notification":{
             "icon":"stock_ticker_update",
             "color":"#7e55c3"
           }
         }
       }
     }

To learn more, see the [HTTP v1
reference](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)
page for more detail on the keys available in platform-specific blocks in the
message body.

## Notification message with a custom image

Keep in mind:

- Images for notifications are limited to 1MB in size, and otherwise are restricted by built-in Android [image
  support](https://developer.android.com/guide/topics/media/media-formats#image-formats).
- To be able to receive and handle notification images in an Apple app, you must add a [Notification Service
  Extension](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension). The notification service extension allows your app to handle the image delivered in the FCM payload before displaying the notification to the end user, see [Set up the notification service
  extension](https://firebase.google.com/docs/cloud-messaging/get-started?platform=ios#set-up-notification-service-extension) for code sample.
- Images uploaded using the Notifications composer are limited to 300KB in size.
- Images stored or served from Cloud Storage are subject to standard [quota limits](https://firebase.google.com/pricing).

In your notification send request, set the following options to enable the
receiving client to handle the image delivered in the payload:

- For Android, set the following [AndroidConfig](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidConfig) option:
  - `notification.image` containing the image URL
- For iOS, set the following [ApnsConfig](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#ApnsConfig) options:
  - `fcm_options.image` containing the image URL. Apple requires that the image URL includes a valid file extension to correctly identify the resource type.
  - `headers({ "mutable-content": 1})`

The following send request sends a common notification title to all platforms,
but it also sends an image. Here's an example of the visual effect on a user's
device:

![Simple drawing of an image in a display notification](https://firebase.google.com/static/docs/cloud-messaging/images/Image_Notification_v2.png)

### Node.js

    const topicName = 'industry-tech';

    const message = {
      notification: {
        title: 'Sparky says hello!'
      },
      android: {
        notification: {
          imageUrl: 'https://foo.bar.pizza-monster.png'
        }
      },
      apns: {
        payload: {
          aps: {
            'mutable-content': 1
          }
        },
        fcm_options: {
          image: 'https://foo.bar.pizza-monster.png'
        }
      },
      webpush: {
        headers: {
          image: 'https://foo.bar.pizza-monster.png'
        }
      },
      topic: topicName,
    };

    getMessaging().send(message)
      .then((response) => {
        // Response is a message ID string.
        console.log('Successfully sent message:', response);
      })
      .catch((error) => {
        console.log('Error sending message:', error);
      });

### REST

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

    Content-Type: application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...HnS_uNreA
    {
      "message":{
         "topic":"industry-tech",
         "notification":{
           "title":"Sparky says hello!",
         },
         "android":{
           "notification":{
             "image":"https://foo.bar/pizza-monster.png"
           }
         },
         "apns":{
           "payload":{
             "aps":{
               "mutable-content":1
             }
           },
           "fcm_options": {
               "image":"https://foo.bar/pizza-monster.png"
           }
         },
         "webpush":{
           "headers":{
             "image":"https://foo.bar/pizza-monster.png"
           }
         }
       }
     }

To learn more, see the [HTTP v1
reference](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)
page for more detail on the keys available in platform-specific blocks in the
message body.

## Notification message with an associated click action

The following send request sends a common notification title to all platforms,
but it also sends an action for the app to perform in response to the user
interacting with the notification. Here's an example of the visual effect
on a user's device:

![Simple drawing of a user tap opening a web page](https://firebase.google.com/static/docs/cloud-messaging/images/Click_Action_v2.png)

### Node.js

    const topicName = 'industry-tech';

    const message = {
      notification: {
        title: 'Breaking News....'
      },
      android: {
        notification: {
          clickAction: 'news_intent'
        }
      },
      apns: {
        payload: {
          aps: {
            'category': 'INVITE_CATEGORY'
          }
        }
      },
      webpush: {
        fcmOptions: {
          link: 'breakingnews.html'
        }
      },
      topic: topicName,
    };

    getMessaging().send(message)
      .then((response) => {
        // Response is a message ID string.
        console.log('Successfully sent message:', response);
      })
      .catch((error) => {
        console.log('Error sending message:', error);
      });

### REST

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1