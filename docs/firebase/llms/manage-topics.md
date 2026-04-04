# Source: https://firebase.google.com/docs/cloud-messaging/manage-topics.md.txt

<br />

The[FirebaseAdmin SDK](https://firebase.google.com/docs/admin/setup)allows you to perform basic topic management tasks from the server side. Given their registration token(s), you can subscribe and unsubscribe client app instances in bulk using server logic.

You can subscribe client app instances to any existing topic, or you can create a new topic. When you use the API to subscribe a client app to a new topic (one that does not already exist for your Firebase project), a new topic of that name is created in FCM and any client can subsequently subscribe to it.

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
    https://github.com/firebase/firebase-admin-dotnet/blob/6cf4da307eb3803aca69a053023696c111e51426/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L327-L341

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
    https://github.com/firebase/firebase-admin-dotnet/blob/6cf4da307eb3803aca69a053023696c111e51426/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L348-L362

| **Note:** You can subscribe or unsubscribe up to 1,000 devices in a single request. If you provide an array with over 1,000 registration tokens, the request will fail with a`messaging/invalid-argument`error.

The`subscribeToTopic()`and`unsubscribeFromTopic()`methods results in an object containing the response fromFCM. The return type has the same format regardless of the number of registration tokens specified in the request.

In case of an error (authentication failures, invalid token or topic etc.) these methods result in an error. For a full list of error codes, including descriptions and resolution steps, see[AdminFCMAPI Errors](https://firebase.google.com/docs/cloud-messaging/send-message#admin_sdk_error_reference).