# Source: https://firebase.google.com/docs/cloud-messaging/web/get-started.md.txt

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/cloud-messaging/ios/get-started) [Android](https://firebase.google.com/docs/cloud-messaging/android/get-started) [Web](https://firebase.google.com/docs/cloud-messaging/web/get-started) [Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started) [Unity](https://firebase.google.com/docs/cloud-messaging/unity/get-started) [C++](https://firebase.google.com/docs/cloud-messaging/cpp/get-started) |

<br />

This guide describes how to get started with Firebase Cloud Messaging in your
Web client apps so that you can reliably send messages.

The FCM JavaScript API lets you receive notification messages in
web apps running in browsers that support the
[Push API](https://www.w3.org/TR/push-api/).
This includes the browser versions listed in this
[support matrix](https://caniuse.com/#feat=push-api) and Chrome extensions
using the Push API.

The FCM SDK is supported only in pages served over HTTPS. This is
due to its use of service workers, which are available only on HTTPS sites. If
you need a provider, [Firebase App Hosting](https://firebase.google.com/docs/hosting/quickstart) is
recommended and provides a no-cost tier for HTTPS hosting on your own domain.

To get started with the FCM JavaScript API, you'll need to add
Firebase to your web app and add logic to access registration tokens.

## Add and initialize the FCM SDK

1. If you haven't already, [install the Firebase JS SDK and initialize Firebase](https://firebase.google.com/docs/web/setup#add-sdk-and-initialize).

2. Add the Firebase Cloud Messaging JS SDK and initialize Firebase Cloud Messaging:

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Firebase Cloud Messaging and get a reference to the service
const messaging = getMessaging(app);
```

### Web


> [!NOTE]
> [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular web API and [upgrade](https://firebase.google.com/docs/web/modular-upgrade) from the namespaced API.

<br />

```
import firebase from "firebase/compat/app";
import "firebase/compat/messaging";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);


// Initialize Firebase Cloud Messaging and get a reference to the service
const messaging = firebase.messaging();
```

If you are using FCM for web and want to upgrade to SDK
6.7.0 or later, you must enable the
[FCM Registration API](https://console.cloud.google.com/apis/library/fcmregistrations.googleapis.com)
for your project in the Google Cloud. When you enable the API, make sure
you are logged in to Cloud Console with the same Google Account you use for
Firebase, and make sure to select the correct project. New projects adding the
FCM SDK have this API enabled by default.

## Configure web credentials with FCM

The FCM Web interface uses Web credentials called Voluntary
Application Server Identification, or VAPID keys, to authorize send requests to
supported web push services. To subscribe your app to push notifications, you
need to associate a pair of keys with your Firebase project. You can either
generate a new key pair or import your existing key pair through the
Firebase console.

### Generate a new key pair

1. Open the [Cloud
   Messaging](https://console.firebase.google.com/project/_/settings/cloudmessaging/) tab of the Firebase console **Settings** pane and go to the **Web configuration** section.
2. In the **Web Push certificates** tab, click **Generate Key Pair**. The console displays a notice that the key pair was generated, and displays the public key string and date added.

### Import an existing key pair

If you have an existing key pair you are already using with your web app, you
can import it to FCM so that you can reach your existing web app
instances through FCM APIs. To import keys, you must have
owner-level access to the Firebase project. Import your existing public and
private key in base64 URL safe encoded form:

1. Open the [Cloud
   Messaging](https://console.firebase.google.com/project/_/settings/cloudmessaging/) tab of the Firebase console **Settings** pane and go to the **Web configuration** section.
2. In the **Web Push certificates** tab, find and select the link text: **import an existing key pair**.
3. In the **Import a key pair** dialog, provide your public and private keys in the corresponding fields and click **Import**. The console displays the public key string and date added.

For instructions on how to add the key to your app, see
[Configure Web credentials in your app](https://firebase.google.com/docs/cloud-messaging/js/client#configure_web_credentials_in_your_app).
For more information about the format of the keys and how to generate them,
see [Application server keys](https://developers.google.com/web/fundamentals/push-notifications/web-push-protocol#application_server_keys).

## Configure Web credentials in your app

The method [`getToken(): Promise<string>`](https://firebase.google.com/docs/reference/js/messaging_#gettoken)
allows FCM to use the VAPID key credential when sending message
requests to different push services. Using the key you generated or imported
according to the instructions in
[Configure Web Credentials with FCM](https://firebase.google.com/docs/cloud-messaging/js/client#configure_web_credentials_with_fcm),
add it in your code after the messaging object is retrieved:

    import { getMessaging, getToken } from "firebase/messaging";

    const messaging = getMessaging();
    // Add the public key generated from the console here.
    getToken(messaging, {vapidKey: "BKagOny0KF_2pCJQ3m....moL0ewzQ8rZu"});

## Access the registration token

When you need to retrieve the current registration token for an app instance, first
request notification permissions from the user with `Notification.requestPermission()`.
When called as shown, this returns a token if permission is granted or rejects the promise
if denied:

```
function requestPermission() {
  console.log('Requesting permission...');
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      console.log('Notification permission granted.');
```

<br />

FCM requires a `firebase-messaging-sw.js` file.
Unless you already have a `firebase-messaging-sw.js` file, create an empty file
with that name and place it in the root of your domain before retrieving a token.
You can add meaningful content to the file later in the client setup process.

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
});
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
});
```

After you've obtained the token, send it to your app server and store
it using your preferred method.

## Send a test notification message

1. Install and run the app on the target device. On Apple devices, you'll need to accept the request for permission to receive remote notifications.
2. Check that the app is in the background on the device.
3. In the Firebase console, open the [Messaging](https://console.firebase.google.com/project/_/notification) page.
4. If this is your first message, select **Create your first campaign** .
   1. Select **Firebase Notification messages** and select **Create**.
5. Otherwise, on the **Campaigns** tab, select **New campaign** and then **Notifications**.
6. Enter the message text.
7. Select **Send test message** from the right pane.
8. In the field labeled **Add an FCM registration token**, enter your registration token.
9. Select **Test**.

After you select **Test**, the targeted client device, with the app in the
background, should receive the notification.

## Next steps

After you have completed the setup steps, here are a few options for moving
forward with FCM for Web (JavaScript):

- [Send messages to devices](https://firebase.google.com/docs/cloud-messaging/server-environment)
- [Receive messages in a JavaScript Client](https://firebase.google.com/docs/cloud-messaging/receive-messages?platform=web)
- [Send messages to topics](https://firebase.google.com/docs/cloud-messaging/topic-messaging)