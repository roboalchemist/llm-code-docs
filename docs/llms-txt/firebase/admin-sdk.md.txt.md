# Source: https://firebase.google.com/docs/cloud-messaging/send/admin-sdk.md.txt

If you haven't set up Firebase Admin SDK already,
follow the [guide](https://firebase.google.com/docs/admin/setup)
to set up Firebase Admin SDK on your server.

## Enable the FCM HTTP v1 API

Enable the Cloud Messaging API in the
[Cloud Messaging settings page](https://console.firebase.google.com/project/_/settings/cloudmessaging)
for your project.

## Send messages to specific devices

To send to a single, specific device, pass the device's registration token as
shown.

### Node.js

    // This registration token comes from the client FCM SDKs.
    const registrationToken = 'YOUR_REGISTRATION_TOKEN';

    const message = {
      data: {
        score: '850',
        time: '2:45'
      },
      token: registrationToken
    };

    // Send a message to the device corresponding to the provided
    // registration token.
    getMessaging().send(message)
      .then((response) => {
        // Response is a message ID string.
        console.log('Successfully sent message:', response);
      })
      .catch((error) => {
        console.log('Error sending message:', error);
      });

### Java

    // This registration token comes from the client FCM SDKs.
    String registrationToken = "YOUR_REGISTRATION_TOKEN";

    // See documentation on defining a message payload.
    Message message = Message.builder()
        .putData("score", "850")
        .putData("time", "2:45")
        .setToken(registrationToken)
        .build();

    // Send a message to the device corresponding to the provided
    // registration token.
    String response = FirebaseMessaging.getInstance().send(message);
    // Response is a message ID string.
    System.out.println("Successfully sent message: " + response);https://github.com/firebase/firebase-admin-java/blob/d69dcbd9604ca2eb49c32d27067df4b70a126c87/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L46-L60

### Python

    # This registration token comes from the client FCM SDKs.
    registration_token = 'YOUR_REGISTRATION_TOKEN'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)https://github.com/firebase/firebase-admin-python/blob/581ef26c3ea0964d44bbd77dfbae1940985c1300/snippets/messaging/cloud_messaging.py#L24-L40

### Go

    // Obtain a messaging.Client from the App.
    ctx := context.Background()
    client, err := app.Messaging(ctx)
    if err != nil {
    	log.Fatalf("error getting Messaging client: %v\n", err)
    }

    // This registration token comes from the client FCM SDKs.
    registrationToken := "YOUR_REGISTRATION_TOKEN"

    // See documentation on defining a message payload.
    message := &messaging.Message{
    	Data: map[string]string{
    		"score": "850",
    		"time":  "2:45",
    	},
    	Token: registrationToken,
    }

    // Send a message to the device corresponding to the provided
    // registration token.
    response, err := client.Send(ctx, message)
    if err != nil {
    	log.Fatalln(err)
    }
    // Response is a message ID string.
    fmt.Println("Successfully sent message:", response)https://github.com/firebase/firebase-admin-go/blob/4f7026f0837678ceb33ab2d2c145a0d18d9952fd/snippets/messaging.go#L29-L55

### C#

    // This registration token comes from the client FCM SDKs.
    var registrationToken = "YOUR_REGISTRATION_TOKEN";

    // See documentation on defining a message payload.
    var message = new Message()
    {
        Data = new Dictionary<string, string>()
        {
            { "score", "850" },
            { "time", "2:45" },
        },
        Token = registrationToken,
    };

    // Send a message to the device corresponding to the provided
    // registration token.
    string response = await FirebaseMessaging.DefaultInstance.SendAsync(message);
    // Response is a message ID string.
    Console.WriteLine("Successfully sent message: " + response);

On success, each send method returns a message ID. The Firebase Admin SDK returns
the ID string in the format `projects/{project_id}/messages/{message_id}`.

## Send one message to multiple devices

The Admin FCM SDKs allow you to multicast a message to a list of
device registration tokens. You can use this feature when you need to send the
same message to a large number of devices. You can specify up to 500 device
registration tokens per invocation.

The return value includes a list of tokens that corresponds to the order of the
input tokens. This is useful when you want to check which tokens resulted in
errors and then [handle them appropriately](https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode).

### Node.js

    // These registration tokens come from the client FCM SDKs.
    const registrationTokens = [
      'YOUR_REGISTRATION_TOKEN_1',
      // ...
      'YOUR_REGISTRATION_TOKEN_N',
    ];

    const message = {
      data: {score: '850', time: '2:45'},
      tokens: registrationTokens,
    };

    getMessaging().sendEachForMulticast(message)
      .then((response) => {
        if (response.failureCount > 0) {
          const failedTokens = [];
          response.responses.forEach((resp, idx) => {
            if (!resp.success) {
              failedTokens.push(registrationTokens[idx]);
            }
          });
          console.log('List of tokens that caused failures: ' + failedTokens);
        }
      });

### Java

    // These registration tokens come from the client FCM SDKs.
    List<String> registrationTokens = Arrays.asList(
        "YOUR_REGISTRATION_TOKEN_1",
        // ...
        "YOUR_REGISTRATION_TOKEN_n"
    );

    MulticastMessage message = MulticastMessage.builder()
        .putData("score", "850")
        .putData("time", "2:45")
        .addAllTokens(registrationTokens)
        .build();
    BatchResponse response = FirebaseMessaging.getInstance().sendEachForMulticast(message);
    if (response.getFailureCount() > 0) {
      List<SendResponse> responses = response.getResponses();
      List<String> failedTokens = new ArrayList<>();
      for (int i = 0; i < responses.size(); i++) {
        if (!responses.get(i).isSuccessful()) {
          // The order of responses corresponds to the order of the registration tokens.
          failedTokens.add(registrationTokens.get(i));
        }
      }

      System.out.println("List of tokens that caused failures: " + failedTokens);
    }https://github.com/firebase/firebase-admin-java/blob/d69dcbd9604ca2eb49c32d27067df4b70a126c87/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L236-L260

### Python

    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        'YOUR_REGISTRATION_TOKEN_1',
        # ...
        'YOUR_REGISTRATION_TOKEN_N',
    ]

    message = messaging.MulticastMessage(
        data={'score': '850', 'time': '2:45'},
        tokens=registration_tokens,
    )
    response = messaging.send_each_for_multicast(message)
    if response.failure_count > 0:
        responses = response.responses
        failed_tokens = []
        for idx, resp in enumerate(responses):
            if not resp.success:
                # The order of responses corresponds to the order of the registration tokens.
                failed_tokens.append(registration_tokens[idx])
        print(f'List of tokens that caused failures: {failed_tokens}')https://github.com/firebase/firebase-admin-python/blob/581ef26c3ea0964d44bbd77dfbae1940985c1300/snippets/messaging/cloud_messaging.py#L249-L268

### Go

    // Create a list containing up to 500 registration tokens.
    // This registration tokens come from the client FCM SDKs.
    registrationTokens := []string{
    	"YOUR_REGISTRATION_TOKEN_1",
    	// ...
    	"YOUR_REGISTRATION_TOKEN_n",
    }
    message := &messaging.MulticastMessage{
    	Data: map[string]string{
    		"score": "850",
    		"time":  "2:45",
    	},
    	Tokens: registrationTokens,
    }

    br, err := client.SendEachForMulticast(context.Background(), message)
    if err != nil {
    	log.Fatalln(err)
    }

    if br.FailureCount > 0 {
    	var failedTokens []string
    	for idx, resp := range br.Responses {
    		if !resp.Success {
    			// The order of responses corresponds to the order of the registration tokens.
    			failedTokens = append(failedTokens, registrationTokens[idx])
    		}
    	}

    	fmt.Printf("List of tokens that caused failures: %v\n", failedTokens)
    }https://github.com/firebase/firebase-admin-go/blob/128f8f425f0a72725e2f39832de6189a92a649db/snippets/messaging.go#L241-L271

### C#

    // These registration tokens come from the client FCM SDKs.
    var registrationTokens = new List<string>()
    {
        "YOUR_REGISTRATION_TOKEN_1",
        // ...
        "YOUR_REGISTRATION_TOKEN_n",
    };
    var message = new MulticastMessage()
    {
        Tokens = registrationTokens,
        Data = new Dictionary<string, string>()
        {
            { "score", "850" },
            { "time", "2:45" },
        },
    };

    var response = await FirebaseMessaging.DefaultInstance.SendEachForMulticastAsync(message);
    if (response.FailureCount > 0)
    {
        var failedTokens = new List<string>();
        for (var i = 0; i < response.Responses.Count; i++)
        {
            if (!response.Responses[i].IsSuccess)
            {
                // The order of responses corresponds to the order of the registration tokens.
                failedTokens.Add(registrationTokens[i]);
            }
        }

        Console.WriteLine($"List of tokens that caused failures: {failedTokens}");
    }
    https://github.com/firebase/firebase-admin-dotnet/blob/9d71ceb37ed2deaf22aed643d1dcfed759df9f9d/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L185-L217

## Send a list of messages

The Admin SDKs support sending a list of up to 500 messages. This feature can be
used to build a customized set of messages and send them to different
recipients, including topics or specific device registration tokens. For
example, you can use this feature when you need to send different audiences
slightly differentiated messages.

### Node.js

    // Create a list containing up to 500 messages.
    const messages = [];
    messages.push({
      notification: { title: 'Price drop', body: '5% off all electronics' },
      token: registrationToken,
    });
    messages.push({
      notification: { title: 'Price drop', body: '2% off all books' },
      topic: 'readers-club',
    });

    getMessaging().sendEach(messages)
      .then((response) => {
        console.log(response.successCount + ' messages were sent successfully');
      });

### Java

    // Create a list containing up to 500 messages.
    List<Message> messages = Arrays.asList(
        Message.builder()
            .setNotification(Notification.builder()
                .setTitle("Price drop")
                .setBody("5% off all electronics")
                .build())
            .setToken(registrationToken)
            .build(),
        // ...
        Message.builder()
            .setNotification(Notification.builder()
                .setTitle("Price drop")
                .setBody("2% off all books")
                .build())
            .setTopic("readers-club")
            .build()
    );

    BatchResponse response = FirebaseMessaging.getInstance().sendEach(messages);
    // See the BatchResponse reference documentation
    // for the contents of response.
    System.out.println(response.getSuccessCount() + " messages were sent successfully");https://github.com/firebase/firebase-admin-java/blob/d69dcbd9604ca2eb49c32d27067df4b70a126c87/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L156-L178

### Python

    # Create a list containing up to 500 messages.
    messages = [
        messaging.Message(
            notification=messaging.Notification('Price drop', '5% off all electronics'),
            token=registration_token,
        ),
        # ...
        messaging.Message(
            notification=messaging.Notification('Price drop', '2% off all books'),
            topic='readers-club',
        ),
    ]

    response = messaging.send_each(messages)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print(f'{response.success_count} messages were sent successfully')https://github.com/firebase/firebase-admin-python/blob/581ef26c3ea0964d44bbd77dfbae1940985c1300/snippets/messaging/cloud_messaging.py#L228-L244

### Go

    // Create a list containing up to 500 messages.
    messages := []*messaging.Message{
    	{
    		Notification: &messaging.Notification{
    			Title: "Price drop",
    			Body:  "5% off all electronics",
    		},
    		Token: registrationToken,
    	},
    	{
    		Notification: &messaging.Notification{
    			Title: "Price drop",
    			Body:  "2% off all books",
    		},
    		Topic: "readers-club",
    	},
    }

    br, err := client.SendEach(context.Background(), messages)
    if err != nil {
    	log.Fatalln(err)
    }

    // See the BatchResponse reference documentation
    // for the contents of response.
    fmt.Printf("%d messages were sent successfully\n", br.SuccessCount)https://github.com/firebase/firebase-admin-go/blob/128f8f425f0a72725e2f39832de6189a92a649db/snippets/messaging.go#L148-L173

### C#

    // Create a list containing up to 500 messages.
    var messages = new List<Message>()
    {
        new Message()
        {
            Notification = new Notification()
            {
                Title = "Price drop",
                Body = "5% off all electronics",
            },
            Token = registrationToken,
        },
        new Message()
        {
            Notification = new Notification()
            {
                Title = "Price drop",
                Body = "2% off all books",
            },
            Topic = "readers-club",
        },
    };

    var response = await FirebaseMessaging.DefaultInstance.SendEachAsync(messages);
    // See the BatchResponse reference documentation
    // for the contents of response.
    Console.WriteLine($"{response.SuccessCount} messages were sent successfully");https://github.com/firebase/firebase-admin-dotnet/blob/9d71ceb37ed2deaf22aed643d1dcfed759df9f9d/FirebaseAdmin/FirebaseAdmin.Snippets/FirebaseMessagingSnippets.cs#L124-L150