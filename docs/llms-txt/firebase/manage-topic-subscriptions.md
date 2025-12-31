# Source: https://firebase.google.com/docs/cloud-messaging/doc-revamp/targeting-user-groups/manage-topic-subscriptions.md.txt

You can subscribe a client app to a topic from either the server or the client:

- On the server, using the Firebase Admin SDK.

- On the client, using the client-side API within your app.

## Manage topic subscriptions using the Admin SDK

The [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
allows you to perform basic
topic management tasks from the server side. Given their registration
token(s), you can subscribe and unsubscribe client app instances in bulk using
server logic.

You can subscribe client app instances to any existing topic, or
you can create a new topic. When you use the API to subscribe a client app
to a new topic (one that does not already exist for your Firebase project),
a new topic of that name is created in FCM and any client can subsequently
subscribe to it.
| **Important:** To use the Firebase Admin SDK, you must first follow the steps in [Add the Firebase Admin SDK to your Server](https://firebase.google.com/docs/admin/setup) to initialize the SDK.

You can pass a list of registration tokens to the Firebase Admin SDK
subscription method to subscribe the corresponding devices to a topic:  

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
    https://github.com/firebase/firebase-admin-dotnet/blob/543254a6e2058a6eb7e563782a4c3d5ae664f42a/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L327-L341

The Firebase Admin SDK also lets you unsubscribe devices from a topic
by passing registration tokens to the appropriate
method:  

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
    https://github.com/firebase/firebase-admin-dotnet/blob/543254a6e2058a6eb7e563782a4c3d5ae664f42a/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L348-L362

| **Note:** You can subscribe or unsubscribe up to 1,000 devices in a single request. If you provide an array with over 1,000 registration tokens, the request will fail with a `messaging/invalid-argument` error.

The `subscribeToTopic()` and `unsubscribeFromTopic()` methods results in an
object containing the response from FCM. The return type has the same
format regardless of the number of registration tokens specified in the
request.

In case of an error (authentication failures, invalid token or topic etc.)
these methods result in an error.
For a full list of error codes, including descriptions
and resolution steps, see
[Firebase Admin SDK Errors](https://firebase.google.com/docs/cloud-messaging/error-codes#admin-error).

## Manage topic subscriptions from your client app

Client app instances can also be subscribed or unsubscribed to topics directly
from your app through the Firebase SDKs. Note that FCM retries in
case of initial failures to ensure the subscription is successful.

Choose your platform:  

### Android

Client apps can subscribe to any existing topic, or they can create a new
topic. When a client app subscribes to a new topic name (one that does
not already exist for your Firebase project), a new topic of that name is
created in FCM and any client can subsequently subscribe to it.

To subscribe to a topic, the client app calls Firebase Cloud Messaging
`subscribeToTopic()` with the FCM topic name. This method
returns a `Task`, which can be used by a completion listener to determine whether
the subscription succeeded:  

### Kotlin

```kotlin
Firebase.messaging.subscribeToTopic("weather")
    .addOnCompleteListener { task ->
        var msg = "Subscribed"
        if (!task.isSuccessful) {
            msg = "Subscribe failed"
        }
        Log.d(TAG, msg)
        Toast.makeText(baseContext, msg, Toast.LENGTH_SHORT).show()
    }https://github.com/firebase/snippets-android/blob/ed6efb7a660bd9e7b7d92b22de64242799a4577a/messaging/app/src/main/java/com/google/firebase/example/messaging/kotlin/MainActivity.kt#L76-L84
```

### Java

```java
FirebaseMessaging.getInstance().subscribeToTopic("weather")
        .addOnCompleteListener(new OnCompleteListener<Void>() {
            @Override
            public void onComplete(@NonNull Task<Void> task) {
                String msg = "Subscribed";
                if (!task.isSuccessful()) {
                    msg = "Subscribe failed";
                }
                Log.d(TAG, msg);
                Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show();
            }
        });https://github.com/firebase/snippets-android/blob/ed6efb7a660bd9e7b7d92b22de64242799a4577a/messaging/app/src/main/java/com/google/firebase/example/messaging/MainActivity.java#L77-L88
```

To unsubscribe, the client app calls Firebase Cloud Messaging `unsubscribeFromTopic()`
with the topic name.

### iOS

Client apps can subscribe to any existing topic, or they can create a new
topic. When a client app subscribes to a new topic name (one that does
not already exist for your Firebase project), a new topic of that name is
created in FCM and any client can subsequently subscribe to it.

To subscribe to a topic, call the subscription method
from your application's main thread (FCM is not thread-safe).
If the subscription request fails initially, FCM retries automatically.
For cases where the subscription cannot be completed,
the subscription throws an error that you can catch
in a completion handler as shown:  

#### Swift

```text
Messaging.messaging().subscribe(toTopic: "weather") { error in
  print("Subscribed to weather topic")
}https://github.com/firebase/quickstart-ios/blob/f2d5e43f2eaac68c116960d7926d9f6d300d1c11/messaging/MessagingExampleSwift/ViewController.swift#L55-L57
```

#### Objective-C

```objective-c
[[FIRMessaging messaging] subscribeToTopic:@"weather"
                                completion:^(NSError * _Nullable error) {
  NSLog(@"Subscribed to weather topic");
}];https://github.com/firebase/quickstart-ios/blob/f2d5e43f2eaac68c116960d7926d9f6d300d1c11/messaging/MessagingExample/ViewController.m#L54-L57
```

This call makes an
asynchronous request to the FCM backend and subscribes the client to
the given topic. Before calling `subscribeToTopic:topic`, make sure that the
client app instance has already received a registration token via the
callback `didReceiveRegistrationToken`.

Each time the app starts,
FCM makes sure that all requested topics have been subscribed. To
unsubscribe, call `unsubscribeFromTopic:topic`,
and FCM unsubscribes from the topic in the background.

### C++

To subscribe to a topic, call [::firebase::messaging::Subscribe](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#subscribe)
from your application. This makes an asynchronous request to the FCM
backend and subscribes the client to the given topic.  

```c++
::firebase::messaging::Subscribe("example");
```

If the subscription request fails initially, FCM retries until
it can subscribe to the topic successfully. Each time the app starts,
FCM makes sure that all requested topics have been subscribed.

To unsubscribe, call [::firebase::messaging::Unsubscribe](https://firebase.google.com/docs/reference/cpp/namespace/firebase/messaging#unsubscribe),
and FCM unsubscribes from the topic in the background.

### Unity

To subscribe to a topic, call
[Firebase.Messaging.FirebaseMessaging.Subscribe](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#subscribe)
from your application. This makes an asynchronous request to the FCM
backend and subscribes the client to the given topic.  

```c#
Firebase.Messaging.FirebaseMessaging.Subscribe("/topics/example");
```

If the subscription request fails initially, FCM retries until
it can subscribe to the topic successfully. Each time the app starts,
FCM makes sure that all requested topics have been subscribed.

To unsubscribe, call
[Firebase.Messaging.FirebaseMessaging.Unsubscribe](https://firebase.google.com/docs/reference/unity/class/firebase/messaging/firebase-messaging#unsubscribe),
and FCM unsubscribes from the topic in the background.

## Legacy Server-Side Topic Management (Deprecated)

| **Warning:** The legacy Instance ID service consists of REST APIs to manage topic subscriptions, including adding and removing individual tokens, and batch operations. These APIs are deprecated and are no longer recommended for new development.

To understand what Instance IDs are, visit the
[Instance ID page](https://developers.google.com/instance-id). For details on
the deprecated endpoints, see the
[Instance ID API References](https://developers.google.com/instance-id/reference).