# Source: https://firebase.google.com/docs/cloud-messaging/doc-revamp/targeting-user-groups/send-topic-messages.md.txt

You can send messages to devices that are subscribed to a particular topic using
the Admin SDK or the FCM v1 HTTP API.

## Prerequisites

- Set up the necessary environment for sending messages using your chosen
  method. See [Set Up Your Server
  Environment](https://firebase.google.com/docs/cloud-messaging/doc-revamp/send-messages/server-environment).

- Client apps must be subscribed to the topic. See [Manage Topic
  Subscriptions](https://firebase.google.com/docs/cloud-messaging/doc-revamp/targeting-user-groups/manage-topic-subscriptions).

## Sending to a Topic

You can send messages to a topic using either the Firebase Admin SDK or the FCM
HTTP v1 API.

### Using the Admin SDK

You can use the Admin SDK to send topic messages from your server. To learn more
about setting up the Admin SDK, see [Send Messages using the Admin
SDK](https://firebase.google.com/docs/cloud-messaging/doc-revamp/send-messages/send/admin-sdk).  

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
    https://github.com/firebase/firebase-admin-java/blob/450fe3cd979d60d067a8d89cbc2530f703ac77a5/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L66-L79

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
    https://github.com/firebase/firebase-admin-python/blob/de713d21da83b1f50c24c5a23132ffc442700448/snippets/messaging/cloud_messaging.py#L46-L61

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

### Using the HTTP v1 API

To send topic messages using the HTTP v1 API, construct a JSON POST request. To
learn more about using the HTTP v1 API, see [Send a Message via FCM v1
API](https://firebase.google.com/docs/cloud-messaging/doc-revamp/send-messages/send/v1-api).  

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

## Sending to Topic Conditions

To send a message to a *combination* of topics, specify a *condition* , which is
a boolean expression that specifies the target topics. For example, the
following condition will send messages to devices that are subscribed to
`TopicA` and either `TopicB` or `TopicC`:

`"'TopicA' in topics && ('TopicB' in topics || 'TopicC' in topics)"`

FCM first evaluates any conditions in parentheses, and then evaluates
the expression from left to right. You can include up to five topics in your
conditional expression.
| **Tip:** If you often send messages to a specific combination of topics, consider creating a new topic for that user group. This is more efficient than using topic conditions. For example, instead of sending messages to subscribers of `TopicA` and `TopicB` using the condition `"'TopicA' in topics && 'TopicB' in topics"`, create a new topic `TopicAandB`, subscribe the relevant users to it, and send messages directly to `TopicAandB`.

### Using the Admin SDK

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
    https://github.com/firebase/firebase-admin-java/blob/450fe3cd979d60d067a8d89cbc2530f703ac77a5/src/test/java/com/google/firebase/snippets/FirebaseMessagingSnippets.java#L85-L102

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
    https://github.com/firebase/firebase-admin-python/blob/de713d21da83b1f50c24c5a23132ffc442700448/snippets/messaging/cloud_messaging.py#L67-L84

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

### Using the HTTP v1 API

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

## Handling Topic Messages in the App

Once you send a message to a topic, FCM delivers it to all subscribed
client app instances.

To learn how to receive and process messages in your Android, iOS, or Web app,
see [Receive
Messages](https://firebase.google.com/docs/cloud-messaging/doc-revamp/send-messages/receive-messages).