# Source: https://firebase.google.com/docs/cloud-messaging/ios/send-multiple.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/android/send-multiple.md.txt

# Source: https://firebase.google.com/docs/cloud-messaging/js/send-multiple.md.txt

To target a message to multiple devices, use[Topic messaging](https://firebase.google.com/docs/cloud-messaging/android/topic-messaging). This feature allows you to send a message to multiple devices that have opted in to a particular topic.

This tutorial focuses on sending topic messages from your app server using the[Admin SDK](https://firebase.google.com/docs/admin/setup)or[REST API](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages)forFCM, and receiving and handling them in a web app. We'll cover message handling for both backgrounded and foregrounded apps.

## Set up the SDK

This section may cover steps you already completed if you have[set up a JavaScript client app](https://firebase.google.com/docs/cloud-messaging/js/client)forFCMor worked through the steps to[receive messages](https://firebase.google.com/docs/cloud-messaging/js/receive).

## Add and initialize theFCMSDK

1. If you haven't already,[install the Firebase JS SDK and initialize Firebase](https://firebase.google.com/docs/web/setup#add-sdk-and-initialize).

2. Add theFirebase Cloud MessagingJS SDK and initializeFirebase Cloud Messaging:

### Web

<br />

| [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular web API and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from the namespaced API.

<br />

```javascript
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

<br />

| [Learn more](https://firebase.google.com/docs/web/learn-more#modular-version)about the tree-shakeable modular web API and[upgrade](https://firebase.google.com/docs/web/modular-upgrade)from the namespaced API.

<br />

```javascript
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

## Subscribe the client app to a topic

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

The behavior of messages differs depending on whether the page is in the foreground (has focus), or in the background, hidden behind other tabs, or completely closed. In all cases the page must handle the[`onMessage`](https://firebase.google.com/docs/reference/js/messaging_#onmessage)callback, but in background cases you may also need to handle[`onBackgroundMessage`](https://firebase.google.com/docs/reference/js/messaging_sw#onbackgroundmessage)or configure the display notification to allow the user to bring your web app into the foreground.

|          App state          |                          Notification                           |         Data          |                              Both                               |
|-----------------------------|-----------------------------------------------------------------|-----------------------|-----------------------------------------------------------------|
| Foreground                  | `onMessage`                                                     | `onMessage`           | `onMessage`                                                     |
| Background (service worker) | `onBackgroundMessage`(display notification automatically shown) | `onBackgroundMessage` | `onBackgroundMessage`(display notification automatically shown) |

### Handle messages when your web app is in the foreground

In order to receive the`onMessage`event, your app must define the Firebase messaging service worker in`firebase-messaging-sw.js`. Alternatively, you can provide an existing service worker to the SDK through[`getToken(): Promise<string>`](https://firebase.google.com/docs/reference/js/messaging_#gettoken).  

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
const messaging = getMessaging(firebaseApp);https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/snippets/messaging-next/service-worker/messaging_init_in_sw.js#L8-L27
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
const messaging = firebase.messaging();https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/messaging/service-worker.js#L10-L33
```

When your app is in the foreground (the user is currently viewing your web page), you can receive data and notification payloads directly in the page.  

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
});https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/snippets/messaging-next/index/messaging_receive_message.js#L8-L18
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
});https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/messaging/index.js#L13-L20
```

### Handle messages when your web app is in the background

All messages received while the app is in the background trigger a display notification in the browser. You can specify options for this notification, such as title or click action, either in the send request from your app server, or using service worker logic on the client.
| Click actions support only secure HTTPS URLs.

#### Setting notification options in the send request

For notification messages sent from the app server, theFCMJavaScript API supports the[`fcm_options.link`](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#WebpushFcmOptions)key. Typically this is set to a page in your web app:  

    https://fcm.googleapis.com/v1/projects/<YOUR-PROJECT-ID>/messages:send
    Content-Type: application/json
    Authorization: bearer <YOUR-ACCESS-TOKEN>

    {
      "message": {
        "topic": "matchday",
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

If the link value points to a page that is already open in a browser tab, a click on the notification brings that tab into the foreground. If the page is not already open, a notification click opens the page in a new tab.

Because data messages don't support`fcm_options.link`, you are recommended to add a notification payload to all data messages. Alternatively, you can handle notifications using the service worker.

For an explanation of the difference between notification and data messages, see[Message types](https://firebase.google.com/docs/cloud-messaging/concept-options).
| **Note:** To[send messages to topics](https://firebase.google.com/docs/cloud-messaging/js/topic-messaging), use the Admin SDK to subscribe app instances to topics. To use the AdminFCMAPI, you must first follow the steps in[Add the Firebase Admin SDK to your Server](https://firebase.google.com/docs/admin/setup)to initialize the SDK.

#### Setting notification options in the service worker

For data messages, you can set notification options in the service worker. First, initialize your app in the service worker:  

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
const messaging = getMessaging(firebaseApp);https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/snippets/messaging-next/service-worker/messaging_init_in_sw.js#L8-L27
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
const messaging = firebase.messaging();https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/messaging/service-worker.js#L10-L33
```

To set options, call[`onBackgroundMessage`](https://firebase.google.com/docs/reference/js/messaging_sw#onbackgroundmessage)in`firebase-messaging-sw.js`. In this example, we create a notification with title, body and icon fields.  

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
});https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/snippets/messaging-next/service-worker/messaging_on_background_message.js#L8-L23
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
});https://github.com/firebase/snippets-web/blob/467eaa165dcbd9b3ab15711e76fa52237ba37f8b/messaging/service-worker.js#L41-L54
```
| **Note:** If you want to define customized behavior in the service worker when the notification is clicked, make sure to handle[`notificationclick`](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/notificationclick_event)before you importFCMfunctions or libraries. Otherwise,FCMmay overwrite the custom behavior.

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

## Add web push properties to a notification payload

With the HTTP v1 API you can specify additional notification options as a[JSON object](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#webpushconfig)containing any valid properties from the[Web Notification API](https://developer.mozilla.org/en-US/docs/Web/API/Notification). The`title`and`body`fields in this object, if present, override the equivalent`google.firebase.fcm.v1.Notification.title`and`google.firebase.fcm.v1.Notification.body`fields.

### HTTP POST request

    POST https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send HTTP/1.1

    Content-Type: application/json
    Authorization: Bearer ya29.ElqKBGN2Ri_Uz...PbJ_uNasm

    {
      "message": {
        "token" : <token of destination app>,
        "notification": {
          "title": "FCM Message",
          "body": "This is a message from FCM"
        },
        "webpush": {
          "headers": {
            "Urgency": "high"
          },
          "notification": {
            "body": "This is a message from FCM to web",
            "requireInteraction": "true",
            "badge": "/badge-icon.png"
          }
        }
      }
    }

With this request, targeted web clients (including supported browsers running on Android) receive a high-priority notification message that remains active until the user interacts with it. It contains the fields:

- Title: FCM Message
- Body: This is a message from FCM to web
- RequireInteraction: true
- Badge: /badge-icon.png

Android and Apple native apps (to which the web overrides don't apply) receive a normal-priority notification message with:

- Title: FCM Message
- Body: This is a message from FCM

Note that[`RequireInteraction`](https://developer.mozilla.org/en-US/docs/Web/API/notification/requireInteraction)currently has only partial support among browsers. Developers should check the Web Notification API specification to verify platform and browser support.

### cURL

    curl -X POST -H "Authorization: Bearer ya29.ElqKBGN2Ri_Uz...PbJ_uNasm" -H "Content-Type: application/json" -d '{
      "message": {
        "token": "bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1..."
        "notification": {
          "title": "FCM Message",
          "body": "This is a message from FCM"
        },
        "webpush": {
          "headers": {
            "Urgency": "high"
          },
          "notification": {
            "body": "This is a message from FCM to web",
            "requireInteraction": "true",
            "badge": "/badge-icon.png"
          }
        }
      }
    }' "https://fcm.googleapis.com/v1/projects/myproject-b5ae1/messages:send"

### HTTP response

    {
        "name": "projects/myproject-b5ae1/messages/0:1500415314455276%31bd1c9631bd1c98"
    }

See[Build App Server Send Requests](https://firebase.google.com/docs/cloud-messaging/send-message)to learn more about FCM messages.