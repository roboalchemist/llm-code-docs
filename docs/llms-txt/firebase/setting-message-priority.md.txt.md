# Source: https://firebase.google.com/docs/cloud-messaging/customize-messages/setting-message-priority.md.txt

You have two options for assigning delivery priority to downstream messages:
normal and high priority. Though the behavior differs slightly across
platforms, delivery of normal and high priority messages works
like this:

- **Normal priority**. Normal priority messages are delivered immediately when the app is in the foreground. For backgrounded apps, delivery may be delayed. For less time-sensitive messages, such as notifications of new email, keeping your UI in sync, or syncing app data in the background, choose normal delivery priority.
- **High priority**. FCM attempts to deliver high priority messages immediately even if the device is in Doze mode. High priority messages are for time-sensitive, user visible content.

> [!IMPORTANT]
> **Important:** When sending data messages to Apple devices, the priority **must** be set to 5, or normal priority. Messages sent with high priority are rejected by the FCM backend with the error `INVALID_ARGUMENT`.

Here is an example of a normal priority message sent using the FCM
HTTP v1 protocol to notify a magazine subscriber that new content is available
to download:

    {
      "message":{
        "topic":"subscriber-updates",
        "notification":{
          "body" : "This week's edition is now available.",
          "title" : "NewsMagazine.com",
        },
        "data" : {
          "volume" : "3.21.15",
          "contents" : "http://www.news-magazine.com/world-week/21659772"
        },
        "android":{
          "priority":"normal"
        },
        "apns":{
          "headers":{
            "apns-priority":"5"
          }
        },
        "webpush": {
          "headers": {
            "Urgency": "high"
          }
        }
      }
    }

For more platform-specific detail on setting message priority:

- [Set and manage Android message priority](https://firebase.google.com/docs/cloud-messaging/android-message-priority)
- [APNs documentation](https://developer.apple.com/library/prerelease/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html#//apple_ref/doc/uid/TP40008194-CH11-SW1)
- [Web push message urgency](https://tools.ietf.org/html/rfc8030#section-5.3)

## Life critical use cases

The FCM APIs aren't designed for emergency alerts or other high-risk
activities where the use or failure of the APIs could result in death, personal
injury, or environmental damage, such as the operation of nuclear facilities,
air traffic control, or life support systems. Any such use is expressly
prohibited under [Section 4. a.
7](https://developers.google.com/terms/#a_api_prohibitions) of the Terms of
Service. You are solely responsible for managing your app's compliance with the
Terms, and any damages resulting from your noncompliance. Google provides the
APIs "as is," and reserves the right to discontinue the APIs or any portion or
feature or your access thereto, for any reason and at any time, without
liability or other obligation to you or your users.