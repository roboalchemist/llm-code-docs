# Source: https://firebase.google.com/docs/cloud-messaging/ios/send-image.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/android/send-image.md.txt

The FCM HTTP v1 API and the[Notifications composer](https://console.firebase.google.com/project/_/notification)support sending image links in the payload of a display notification, for image download to the device after delivery. Images for notifications are limited to 1MB in size, and otherwise are restricted by native Android[image support](https://developer.android.com/guide/topics/media/media-formats#image-formats).

## Build the send request

In your notification send request, set the following[AndroidConfig](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#AndroidConfig)option:

- `notification.image`containing the image URL

The following send request sends a common notification title to all platforms, but it also sends an image. Here's an example of the visual effect on a user's device:

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

To learn more, see the[HTTP v1 reference](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)page for more detail on the keys available in platform-specific blocks in the message body.

With`notification`set as shown, this send request enables the receiving client to handle the image delivered in the payload.