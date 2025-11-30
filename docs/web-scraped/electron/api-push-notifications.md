# Source: https://www.electronjs.org/docs/latest/api/push-notifications

On this page

# pushNotifications

Process: [Main](/docs/latest/glossary#main-process)

> Register for and receive notifications from remote push notification services

For example, when registering for push notifications via Apple push notification services (APNS):

``` 
const  = require('electron')

pushNotifications.registerForAPNSNotifications().then((token) => )

pushNotifications.on('received-apns-notification', (event, userInfo) => )
```

## Events[â€‹](#events "Direct link to Events") 

The `pushNotification` module emits the following events:

#### Event: \'received-apns-notification\' *macOS*[â€‹](#event-received-apns-notification-macos "Direct link to event-received-apns-notification-macos") 

Returns:

- `event` Event
- `userInfo` Record\<String, any\>

Emitted when the app receives a remote notification while running. See: [https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428430-application?language=objc](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428430-application?language=objc)

## Methods[â€‹](#methods "Direct link to Methods") 

The `pushNotification` module has the following methods:

### `pushNotifications.registerForAPNSNotifications()` *macOS*[â€‹](#pushnotificationsregisterforapnsnotifications-macos "Direct link to pushnotificationsregisterforapnsnotifications-macos") 

Returns `Promise<string>`

Registers the app with Apple Push Notification service (APNS) to receive [Badge, Sound, and Alert](https://developer.apple.com/documentation/appkit/nsremotenotificationtype?language=objc) notifications. If registration is successful, the promise will be resolved with the APNS device token. Otherwise, the promise will be rejected with an error message. See: [https://developer.apple.com/documentation/appkit/nsapplication/1428476-registerforremotenotificationtyp?language=objc](https://developer.apple.com/documentation/appkit/nsapplication/1428476-registerforremotenotificationtyp?language=objc)

### `pushNotifications.unregisterForAPNSNotifications()` *macOS*[â€‹](#pushnotificationsunregisterforapnsnotifications-macos "Direct link to pushnotificationsunregisterforapnsnotifications-macos") 

Unregisters the app from notifications received from APNS.

Apps unregistered through this method can always reregister.

See: [https://developer.apple.com/documentation/appkit/nsapplication/1428747-unregisterforremotenotifications?language=objc](https://developer.apple.com/documentation/appkit/nsapplication/1428747-unregisterforremotenotifications?language=objc)

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/push-notifications.md)