# Source: https://www.courier.com/docs/external-integrations/push/expo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Expo

> Step-by-step guide for integrating Expo push notifications with Courier, including support for single and multiple device tokens, provider overrides, APNs credential troubleshooting, and best practices for tracking and delivery.

## Setup

You will need an [Expo](https://expo.dev/) account with push notifications configured for your project. In Courier, navigate to the [Expo Integration](https://app.courier.com/integrations/catalog/expo) page, enter your Expo access token, then click "Save."

## Profile Requirements

To deliver a push notification to a recipient over Expo, Courier must be provided the recipient's Exponent push token. It should be included in the recipient profile as `expo`.

### Single Token

To push a notification to a single device, you can pass the recipient's push token as a string to `expo.token`.

```json  theme={null}
{
  "message": {
    // Recipient Profile
    "to": {
      "expo": {
        "token": "ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]"
      }
    }
  }
}
```

### Multiple Tokens

If the recipient has multiple devices and you'd like to push to all of them, you can pass the push tokens as an array of strings to `expo.tokens`.

```json  theme={null}
{
  "message": {
    // Recipient Profile
    "to": {
      "expo": {
        "tokens": ["ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]", ...]
      }
    }
  }
}
```

<Note>
  If you pass values to both `token` and `tokens`, Courier will merge the value of `token` into the `tokens` array and dedupe it.
</Note>

## Overrides

You can use a provider override to replace what we send to Expo's API. For example, you can add a ttl value and turn off the sound with your send request:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "expo": {
        "token": "ExponentPushToken[xxxxxxxxxxxxxxxxxxxxxx]"
      }
    },
    "data": {
      "dataForPushMessage": true
    },
    "providers": {
      "expo": {
        "override": {
          "ttl": 10,
          "sound": null
        }
      }
    }
  }
}
```

Everything inside of `providers.expo.override` will replace what we send to Expo's API. Values that are not replaced will still be sent (the title, subtitle, body and data will still be generated and sent in the example above). You can see all the available options by visiting [Expo's website](https://docs.expo.dev/push-notifications/overview/).

## Tracking Events

Courier will include tracking URL information in the `data` attribute on the incoming message payload.

See [Courier push notification tracking](/external-integrations/push/intro-to-push#tracking)

## Troubleshooting

Tips for resolving response errors from Expo

### Could Not Find APNs Credentials

Excerpt from Expo's [Help Forum](https://forums.expo.dev/t/push-notification-error-could-not-find-apns-credentials-for-standalone-app/6955) on how they handle APN tokens:

> Expo push tokens work quite similarly to how Apple's tokens work with APN's, since Expo's server is a relatively thin service that relays notifications to Apple. Expo needs valid APN credentials to send push notifications. And as with APNs in general (not specific to Expo), it doesn't matter what APNs credentials you had at the time an iOS device provided a device token - the APN credentials just need to be valid at the time of sending the notification.

> So, if you revoke your APNs credentials or clear them from Expo, or if your APNs credentials expire (APN p12 certificates expire after one year), Apple will reject all of your push notifications until you provide Expo with valid APN credentials. To be clear, **your Expo push tokens and the underlying iOS device tokens are still valid** and will still work once you provide new, valid APN credentials.

> In this case, the error `Could not find APNs credentials for…` means that Expo does not have any copy of your APNs credentials (currently a p12 certificate). You will need to let Expo recreate the credentials for you (**recommended for most developers:** run `exp build:ios -c` to clear all of them and then run `exp build:ios` to let Expo re-provision them) or upload your own credentials from Apple's developer center (be sure to follow the instructions carefully.

* Your push key should be correctly configured at `https://expo.dev/accounts/[account]/projects/[project]/credentials?platform=ios`
* You've correctly set your bundle identifier in your configuration
* If you are explicitly passing in the `experienceId` in `Notifications.getExpoPushTokenAsync({ experienceId: 'xxxx' })`, make sure it is in the format of `@expo_account/expo_projectname`
