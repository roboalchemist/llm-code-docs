# Source: https://www.courier.com/docs/external-integrations/push/intro-to-push.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Push Notifications

> Overview of Courier’s push notification capabilities, including how to use push channel overrides, attach tracking URLs, and update notification status using the Courier client-side authentication token.

Courier integrates with many different push providers. Each provider may have specific requirements for delivering a message to a recipient, such as device tokens or provider-specific profile fields.

## Available Push Providers

| Provider                                                                               | Description                                                             |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [Apple Push Notifications (APNS)](/external-integrations/push/apple-push-notification) | iOS/macOS push via APNS with P8/P12 auth and Courier Mobile SDK support |
| [Firebase Cloud Messaging (FCM)](/external-integrations/push/firebase-fcm)             | Android/iOS/Web push via Google FCM with Courier Mobile SDK support     |
| [Expo](/external-integrations/push/expo)                                               | Cross-platform push for Expo/React Native apps                          |
| [OneSignal](/external-integrations/push/onesignal-push)                                | Multi-platform push via OneSignal's notification platform               |
| [Airship](/external-integrations/push/airship)                                         | Enterprise push via Airship (formerly Urban Airship)                    |
| [Pusher Beams](/external-integrations/push/pusher-beams)                               | Push via Pusher Beams to users or interest groups                       |
| [Pusher](/external-integrations/push/pusher)                                           | Real-time messaging via Pusher Channels                                 |
| [MagicBell](/external-integrations/push/magicbell)                                     | In-app notifications via MagicBell                                      |
| [Pushbullet](/external-integrations/push/pushbullet)                                   | Cross-device push via Pushbullet                                        |
| [Beamer](/external-integrations/push/beamer)                                           | In-app changelog and push notifications via Beamer                      |
| [NowPush](/external-integrations/push/nowpush)                                         | Cross-platform push via NowPush                                         |

<Tip>
  Can't find a provider? Open up a chat on the Courier site, or email [support@courier.com](mailto:support@courier.com)
</Tip>

## Push Channel Override

Push channel overrides allow you to set the body, clickAction, data, icon, and title of a push notification.

**Data structure for the push channel override:**

```json  theme={null}
{
  "message": {
    "channels": {
      "push": {
        "override": {
          "body": "",
          "clickAction": "",
          "data": "",
          "icon": "",
          "title": ""
        }
      }
    }
    //... rest of message
  }
}
```

## Data Mapping

All push channels have the ability to explicitly turn on data mapping. Data mapping can be useful to help limit how much data is passed to the push provider. For example, you can either pass the entire data payload as

```json  theme={null}
data: request("data")
```

or explicitly choose which values to pass down:

```json  theme={null}
data: {
  "firstName": data("firstName"), // accesses the data object
  "email": profile("email"), // accesses the profile object
  "template": request("template") // accesses the entire request received.
}
```

## Tracking

Courier will attach a trackingUrl for all push requests that allow the state of the push notification to be updated. This is automatically done via the [Courier Mobile SDKs](/sdk-libraries/sdks-overview), but you can control it manually like this:

### Example Message

```json  theme={null}
{
  "message": {
    "data": {
      "trackingUrl": "https://api.courier.com/e/123_channelTrackingId"
      // other data attributes
    }
    // other messages attributes
  }
}
```

### Example Request

```js  theme={null}
fetch("https://api.courier.com/e/123_channelTrackingId", {
  method: "POST",
  headers: {
    "X-Courier-Client-Key": "YOUR_COURIER_CLIENT_KEY",
  },
  body: JSON.stringify({
    event: "DELIVERED", // CLICKED or DELIVERED
  }),
});
```

### Provider-Specific Tracking

Different push providers include the `trackingUrl` in different parts of their payload:

#### Airship

Courier will send `trackingUrl` in `global_attributes` [data bag](https://docs.airship.com/whats-new/2021-08-02-push-api-personalization/) when you receive push notification in your client application.

#### APN (Apple Push Notifications)

`trackingUrl` will be part of `data` attribute in incoming [`payload`](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns/) when you receive push notification in your client application.

#### Firebase

`trackingUrl` will be part of `data` attribute in incoming `message` payload when you receive push notification in your client application.

#### Expo

`trackingUrl` will be part of `data` attribute in incoming `payload` when you receive push notification in your client application.

#### Pusher

`trackingUrl` will be part of `data` attribute in the incoming `payload` when you receive push notification in your client application.
