# Source: https://firebase.google.com/docs/cloud-messaging/web/receive-messages.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/receive-messages) [Android](https://firebase.google.com/docs/cloud-messaging/android/receive-messages) [Web](https://firebase.google.com/docs/cloud-messaging/web/receive-messages) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/receive-messages) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/receive-messages) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/receive-messages) |

<br />

The behavior of messages differs depending on
whether the page is in the foreground (has focus), or in the background, hidden
behind other tabs, or completely closed. In all cases the page must handle the
[`onMessage`](https://firebase.google.com/docs/reference/js/messaging_#onmessage)
callback, but in background cases you may also need to handle
[`onBackgroundMessage`](https://firebase.google.com/docs/reference/js/messaging_sw#onbackgroundmessage)
or configure the display notification to allow the user to bring your
web app into the foreground.

| App state | Notification | Data | Both |
|---|---|---|---|
| Foreground | `onMessage` | `onMessage` | `onMessage` |
| Background (service worker) | `onBackgroundMessage` (display notification automatically shown) | `onBackgroundMessage` | `onBackgroundMessage` (display notification automatically shown) |

The JavaScript [quickstart
sample](https://github.com/firebase/quickstart-js/tree/master/messaging)
demonstrates all code required to receive messages.

> [!IMPORTANT]
> **Important:** This guide mentions initializing Firebase in a service worker. To use the modular SDK in a service worker, you must bundle your service worker file, since ES modules are relatively new and not widely supported (See [ES modules in service workers](https://web.dev/articles/es-modules-in-sw)). If you don't want to bundle your service worker file, you can use the namespaced API provided by the compat packages. To see how you can use module bundlers with Firebase, see [Using module bundlers with Firebase](https://firebase.google.com/docs/web/module-bundling).

## Handle messages when your web app is in the foreground

In order to receive the `onMessage` event, your app must define the
Firebase messaging service worker in `firebase-messaging-sw.js`.
Alternatively, you can provide an existing service worker to the SDK through
[`getToken(): Promise<string>`](https://firebase.google.com/docs/reference/js/messaging_#gettoken).

### Web

```javascript
import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging/sw";

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
const firebaseApp = initializeApp({
  apiKey: 'api-key',
  authDomain: 'project-id.firebaseapp.com',
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: 'project-id',
  storageBucket: 'project-id.appspot.com',
  messagingSenderId: 'sender-id',
  appId: 'app-id',
  measurementId: 'G-measurement-id',
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = getMessaging(firebaseApp);
```

### Web

```javascript
// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here. Other Firebase libraries
// are not available in the service worker.
// Replace 10.13.2 with latest version of the Firebase JS SDK.
importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-messaging-compat.js');

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
  apiKey: 'api-key',
  authDomain: 'project-id.firebaseapp.com',
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: 'project-id',
  storageBucket: 'project-id.appspot.com',
  messagingSenderId: 'sender-id',
  appId: 'app-id',
  measurementId: 'G-measurement-id',
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
```

When your app is in the foreground (the user is viewing your web
page), you can receive data and notification
payloads directly in the page.

### Web

```javascript
// Handle incoming messages. Called when:
// - a message is received while the app has focus
// - the user clicks on an app notification created by a service worker
//   `messaging.onBackgroundMessage` handler.
import { getMessaging, onMessage } from "firebase/messaging";

const messaging = getMessaging();
onMessage(messaging, (payload) => {
  console.log('Message received. ', payload);
  // ...
});
```

### Web

```javascript
// Handle incoming messages. Called when:
// - a message is received while the app has focus
// - the user clicks on an app notification created by a service worker
//   `messaging.onBackgroundMessage` handler.
messaging.onMessage((payload) => {
  console.log('Message received. ', payload);
  // ...
});
```

## Handle messages when your web app is in the background

All messages received while the app is in the background trigger a display
notification in the browser. You can specify options for this notification,
such as title or click action, either in the send request from your app server,
or using service worker logic on the client.

> [!CAUTION]
> **Caution:** Click actions support only secure HTTPS URLs.

### Set notification options in the send request

For notification messages sent from the app server, the FCM
JavaScript API supports the
[`fcm_options.link`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#WebpushFcmOptions)
key. Typically this is set to a page in your web app:

        https://fcm.googleapis.com/v1/projects/<YOUR-PROJECT-ID>/messages:send
        Content-Type: application/json
        Authorization: bearer <YOUR-ACCESS-TOKEN>

        {
          "message": {
            ,
            "notification": {
              "title": "Background Message Title",
              "body": "Background message body"
            },
            "webpush": {
              "fcm_options": {
                "link": "https://dummypage.com"
              }
            }
          }
        }

If the link value points to a page that is already open in a browser tab,
clicking the notification brings that tab into the foreground.
If the page is not already open, a notification click opens the page in a new
tab.

Because data messages don't support `fcm_options.link`, you are recommended to
add a notification payload to all data messages. Alternatively, you can handle
notifications using the service worker.

For an explanation of the difference between notification and data messages, see
[Message types](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type).

> [!NOTE]
> **Note:** To [send messages to topics](https://firebase.google.com/docs/cloud-messaging/js/topic-messaging), use the Admin SDK to subscribe app instances to topics. To use the Admin FCM API, you must first follow the steps in [Add the Firebase Admin SDK to your Server](https://firebase.google.com/docs/admin/setup) to initialize the SDK.

### Set notification options in the service worker

For data messages, you can set notification options in the service worker.
First, initialize your app in the service worker:

### Web

```javascript
import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging/sw";

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
const firebaseApp = initializeApp({
  apiKey: 'api-key',
  authDomain: 'project-id.firebaseapp.com',
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: 'project-id',
  storageBucket: 'project-id.appspot.com',
  messagingSenderId: 'sender-id',
  appId: 'app-id',
  measurementId: 'G-measurement-id',
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = getMessaging(firebaseApp);
```

### Web

```javascript
// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here. Other Firebase libraries
// are not available in the service worker.
// Replace 10.13.2 with latest version of the Firebase JS SDK.
importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.13.2/firebase-messaging-compat.js');

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
  apiKey: 'api-key',
  authDomain: 'project-id.firebaseapp.com',
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: 'project-id',
  storageBucket: 'project-id.appspot.com',
  messagingSenderId: 'sender-id',
  appId: 'app-id',
  measurementId: 'G-measurement-id',
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
```

To set options, call [`onBackgroundMessage`](https://firebase.google.com/docs/reference/js/messaging_sw#onbackgroundmessage)
in `firebase-messaging-sw.js`.
In this example, we create a notification with title, body and icon fields.

### Web

```javascript
import { getMessaging } from "firebase/messaging/sw";
import { onBackgroundMessage } from "firebase/messaging/sw";

const messaging = getMessaging();
onBackgroundMessage(messaging, (payload) => {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  // Customize notification here
  const notificationTitle = 'Background Message Title';
  const notificationOptions = {
    body: 'Background Message body.',
    icon: '/firebase-logo.png'
  };

  self.registration.showNotification(notificationTitle,
    notificationOptions);
});
```

### Web

```javascript
messaging.onBackgroundMessage((payload) => {
  console.log(
    '[firebase-messaging-sw.js] Received background message ',
    payload
  );
  // Customize notification here
  const notificationTitle = 'Background Message Title';
  const notificationOptions = {
    body: 'Background Message body.',
    icon: '/firebase-logo.png'
  };

  self.registration.showNotification(notificationTitle, notificationOptions);
});
```

> [!NOTE]
> **Note:** If you want to define customized behavior in the service worker when the notification is clicked, make sure to handle [`notificationclick`](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/notificationclick_event) before you import FCM functions or libraries. Otherwise, FCM may overwrite the custom behavior.

### Best practices for notifications

For developers sending
notifications through FCM for Web, the most important considerations
are precision and relevance. Here are some specific recommendations for keeping
your notifications precise and relevant:

- Use the icon field to send a meaningful image. For many use cases, this should be a company or app logo that your users immediately recognize. Or, for a chat application, it might be the sending user's profile image.
- Use the title field to express the precise nature of the message. For example, "Jimmy replied" conveys more precise information than "New message." Don't use this valuable space for your company or app name --- use the icon for that purpose.
- Don't use the notification title or body to display your website name or domain; notifications already contain your domain name.
- Add `fcm_options.link`, usually to link the user back to your web app and bring it into focus in the browser. In rare cases where all the information you need to convey can be fit into the notification, you might not need a link.