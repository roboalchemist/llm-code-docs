# Source: https://firebase.google.com/docs/cloud-messaging/ios/first-message.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/flutter/first-message.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/android/first-message.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/js/first-message.md.txt

To get started withFCM, build out the simplest use case: sending a notification message to a specific user when the app is in the background on the device. This page lists all the steps to achieve this, from setup to verification --- it may cover steps you already completed if you have[set up a JavaScript client app](https://firebase.google.com/docs/cloud-messaging/js/client)forFCM.
| **Important:** This guide focuses on the background case. If you want to receive messages when your app is in the foreground as well, see also[Receive Messages in a JavaScript Client](https://firebase.google.com/docs/cloud-messaging/js/receive).

## Set up the SDK

If you haven't already,[add Firebase to your JavaScript project](https://firebase.google.com/docs/web/setup).

## Access the registration token

When you need to retrieve the current registration token for an app instance, first request notification permissions from the user with`Notification.requestPermission()`. When called as shown, this returns a token if permission is granted or rejects the promise if denied:  

```javascript
function requestPermission() {
  console.log('Requesting permission...');
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      console.log('Notification permission granted.');
```

<br />

FCMrequires a`firebase-messaging-sw.js`file. Unless you already have a`firebase-messaging-sw.js`file, create an empty file with that name and place it in the root of your domain before retrieving a token. You can add meaningful content to the file later in the client setup process.

To retrieve the current token:  

### Web

```javascript
import { getMessaging, getToken } from "firebase/messaging";

// Get registration token. Initially this makes a network call, once retrieved
// subsequent calls to getToken will return from cache.
const messaging = getMessaging();
getToken(messaging, { vapidKey: '<YOUR_PUBLIC_VAPID_KEY_HERE>' }).then((currentToken) => {
  if (currentToken) {
    // Send the token to your server and update the UI if necessary
    // ...
  } else {
    // Show permission request UI
    console.log('No registration token available. Request permission to generate one.');
    // ...
  }
}).catch((err) => {
  console.log('An error occurred while retrieving token. ', err);
  // ...
});https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/snippets/messaging-next/index/messaging_get_token.js#L8-L25
```

### Web

```javascript
// Get registration token. Initially this makes a network call, once retrieved
// subsequent calls to getToken will return from cache.
messaging.getToken({ vapidKey: '<YOUR_PUBLIC_VAPID_KEY_HERE>' }).then((currentToken) => {
  if (currentToken) {
    // Send the token to your server and update the UI if necessary
    // ...
  } else {
    // Show permission request UI
    console.log('No registration token available. Request permission to generate one.');
    // ...
  }
}).catch((err) => {
  console.log('An error occurred while retrieving token. ', err);
  // ...
});https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/messaging/index.js#L27-L41
```

After you've obtained the token, send it to your app server and store it using your preferred method.

## Send a test notification message

1. Install and run the app on the target device. On Apple devices, you'll need to accept the request for permission to receive remote notifications.

2. Make sure the app is in the background on the device.

3. In theFirebaseconsole, open the[Messaging page](https://console.firebase.google.com/project/_/messaging/).

4. If this is your first message, select**Create your first campaign**.

   1. Select**Firebase Notification messages** and select**Create**.
5. Otherwise, on the**Campaigns** tab, select**New campaign** and then**Notifications**.

6. Enter the message text. All other fields are optional.

7. Select**Send test message**from the right pane.

8. In the field labeled**Add an FCM registration token**, enter the registration token you obtained in a previous section of this guide.

9. Select**Test**.

After you select**Test**, the targeted client device (with the app in the background) should receive the notification.

## Next steps

### Send messages to foregrounded apps

Once you have successfully sent notification messages while your app is in the background, see[Receive Messages in a JavaScript Client](https://firebase.google.com/docs/cloud-messaging/js/receive)to get started sending to foregrounded apps.

### Go beyond notification messages

To go beyond notification messages and add other, more advanced behavior to your app, see:

- [Receive Messages in a JavaScript Client](https://firebase.google.com/docs/cloud-messaging/js/receive)
- [Send Messages to Multiple Devices](https://firebase.google.com/docs/cloud-messaging/js/send-multiple)