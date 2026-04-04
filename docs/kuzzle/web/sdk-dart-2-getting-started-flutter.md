# Source: https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter

Title: Kuzzle Documentation

URL Source: https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter

Markdown Content:
Getting Started with Kuzzle and Flutter [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#getting-started-with-kuzzle-and-flutter)
----------------------------------------------------------------------------------------------------------------------------------------------

This section deals with **Kuzzle v2**, the **Dart SDK v2** and **Flutter**. We will create **documents** in Kuzzle and subscribe to [document notifications](https://docs.kuzzle.io/sdk/dart/2/essentials/realtime-notifications#document-messages) to develop a realtime chat.

Requirements [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#requirements)
----------------------------------------------------------------------------------------

*   **Running Kuzzle v2 Stack** ([instructions here](https://docs.kuzzle.io/core/2/guides/getting-started/run-kuzzle))
*   **Setup an editor** ([instructions here](https://flutter.dev/docs/get-started/editor))
*   **Create a new project** ([instructions here](https://flutter.dev/docs/get-started/test-drive?tab=androidstudio#create-app))

Use the Kuzzle SDK in your flutter app [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#use-the-kuzzle-sdk-in-your-flutter-app)
--------------------------------------------------------------------------------------------------------------------------------------------

You can find the kuzzle package on pub.dev. ([https://pub.dev/packages/kuzzle](https://pub.dev/packages/kuzzle))

The `pubspec.yaml` file manages the assets and dependencies for a Flutter app. In `pubspec.yaml`, add kuzzle (2.0.1 or higher) to the dependencies list:

```
dependencies:
  flutter:
    sdk: flutter
  kuzzle: ^2.0.1
```

Then run `flutter pub get` to install the new dependency

`$ flutter pub get`

App entry point [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#app-entry-point)
----------------------------------------------------------------------------------------------

Let's start with the main:

_main.dart:_

```
import 'package:flutter/material.dart';
import 'package:flutter_getting_started/login.dart';
void main() {
  runApp(Login());
}
```

Set a username [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#set-a-username)
--------------------------------------------------------------------------------------------

Here we will ask the user to enter its username. To keep it simple, this does not use the authentication system of Kuzzle but feel free to implement it for a better usage.

_login.dart:_

```
import 'package:flutter/material.dart';
import 'package:flutter_getting_started/chat.dart';
class Login extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Chat app',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: LoginPage(title: 'Chat app'),
    );
  }
}
class LoginPage extends StatefulWidget {
  LoginPage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _LoginPage createState() => _LoginPage();
}
class _LoginPage extends State<LoginPage> {
  final _loginController = TextEditingController();
  @override
  void dispose() {
    _loginController.dispose();
    super.dispose();
  }
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(
      title: Text(widget.title),
    ),
    body: Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: Form(
              child: Column(
                children: <Widget>[
                  Padding(
                    padding: const EdgeInsets.only(left: 8),
                    child: TextField(
                      controller: _loginController,
                      decoration: InputDecoration(
                        hintText: 'Username',
                      ),
                    ),
                  ),
                  RaisedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => Chat(_loginController.text)),
                      );
                    },
                    child: Text('Next'),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    ),
      );
}
```

The chat [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#the-chat)
--------------------------------------------------------------------------------

We have to connect the server so that our client can interact with it (note that the host is the API of an android emulator in this example).

In our _chat.dart_ let's import the sdk:

`import 'package:kuzzle/kuzzle.dart';`

Then we will [establish the connection](https://docs.kuzzle.io/sdk/dart/2/core-classes/kuzzle/connect) to kuzzle and create, if they don't [exist](https://docs.kuzzle.io/sdk/dart/2/controllers/index/exists/), the [index](https://docs.kuzzle.io/sdk/dart/2/controllers/index/create) and [collection](https://docs.kuzzle.io/sdk/dart/2/controllers/collection/create) of our chat. We will also fetch messages sorted by creation date, and subscribe to the same collection to receive new messages in realtime.

### Create index and collection [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#create-index-and-collection)

So first let's write a method which will create the index/collection if it does not exist:

```
void _initData() async {
  // Check if 'chat' index exists
  if (!(await _kuzzle.index.exists('chat'))) {
    // If not, create 'chat' index and 'messages' collection
    await _kuzzle.index.create('chat');
    await _kuzzle.collection.create('chat', 'messages');
}
}
```

### Get existing messages [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#get-existing-messages)

The method _fetchMessage()_ will [search](https://docs.kuzzle.io/sdk/dart/2/controllers/document/search) for the first hundred newest messages. It will then update the state of the widget to store those messages in the `messages` variable.

```
void _fetchMessages() async {
  // Call the search method of the document controller
  final results = await this._kuzzle.document.search(
    'chat', // Name of the index
    'messages', // Name of the collection
    query: {
      'sort': {
        '_kuzzle_info.createdAt': {'order': 'asc'}
      }
    }, // Query => Sort the messages by creation date
    size: 100, // Options => get a maximum of 100 messages
  );
  // Add messages to our array after formating them
  setState(() {
    this._messages = results.hits
      .map((message) => Message.fromJson(message))
      .toList();
  });
}
```

### Receive new messages in realtime [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#receive-new-messages-in-realtime)

And finally the method to subscribe to our collection. It will call the Kuzzle's realtime controller to allow us to receive [real-time notifications](https://docs.kuzzle.io/core/2/api/payloads/notifications) on message creations. New messages received that way will then be added to our list of previously fetched `messages`, and rendered in our list, by updating the state.

```
void _subscribeToNewMessages() async {
  // Call the subscribe method of the realtime controller and receive the roomId
  // Save the id of our subscription (we could need it to unsubscribe)
  _roomId = await _kuzzle.realtime.subscribe(
    'chat', // Name of the index
    'messages', // Name of the collection
    {}, // Filter
    (notification) {
    if (notification.action != 'create') return;
    if (notification.controller != 'document') return;
    setState(() {
      _messages.add(Message.fromJson(notification.result));
    });
  }, subscribeToSelf: true);
}
```

### Call previous written methods [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#call-previous-written-methods)

Then we are going to call all of those methods in the `initState` method of the State of our `StatefulWidget`:

```
@override
void initState() {
  _kuzzle = Kuzzle(WebSocketProtocol(Uri(
    scheme: 'ws',
    host: '10.0.2.2',
    port: 7512,
  )));
  // Etablish the connection
  _kuzzle.connect().then((_) {
    _initData();
    _fetchMessages();
    _subscribeToNewMessages();
  });
  super.initState();
}
```

As you can see we use a model to retrieve each message from the JSON Response to a Dart class.

Here:

```
this._messages = results.hits
  .map((message) => Message.fromJson(message))
  .toList();
```

And here:

`_messages.add(Message.fromJson(notification.result));`

So here is the Dart class used for this model

_message.dart:_

```
class Message {
  final String id;
  final String username;
  final String value;
  final int createdAt;
  Message({this.id, this.username, this.value, this.createdAt});
  factory Message.fromJson(Map<String, dynamic> json) => Message(
    id: json['_id'],
    username: json['_source']['username'],
    value: json['_source']['value'],
    createdAt: json['_source']['_kuzzle_info']['createdAt'],
  );
}
```

### Display everything [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#display-everything)

Finally let's make a view to display everything and add an input to be able to send a message in our `build()` method:

_chat.dart:_

```
@override
Widget build(BuildContext context) => Scaffold(
  appBar: AppBar(
    title: Text(widget.title),
  ),
  body: Center(
    child: Column(
      children: <Widget>[
        Expanded(
          child: Container(
            width: double.infinity,
            child: ChatView(
              messages: _messages,
            ),
          ),
        ),
        Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: Form(
            child: Row(
              children: <Widget>[
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.only(left: 8),
                    child: TextField(
                      controller: _chatController,
                    ),
                  ),
                ),
                FlatButton(
                  onPressed: () async {
                    await _kuzzle.document.create('chat', 'messages', {
                      'username': widget.username,
                      'value': _chatController.text
                    });
                    _chatController.clear();
                  },
                  child: Icon(Icons.send),
                ),
              ],
            ),
          ),
        ),
      ],
    ),
  ),
);
```

And _chat\_view.dart:_

```
import 'package:intl/intl.dart';
import 'package:flutter/material.dart';
import 'package:flutter_getting_started/message.dart';
class ChatView extends StatefulWidget {
  ChatView({Key key, this.title, @required this.messages}) : super(key: key);
  final String title;
  final List<Message> messages;
  @override
  ChatViewState createState() => ChatViewState();
}
class ChatViewState extends State<ChatView> {
  List<Widget> messagesBox = [];
  ScrollController _scrollController = ScrollController();
  @override
  Widget build(BuildContext context) {
    WidgetsBinding.instance.addPostFrameCallback((timeStamp) {
      _scrollController.jumpTo(_scrollController.position.maxScrollExtent);
    });
    return Scaffold(
      body: ListView.builder(
        controller: _scrollController,
        itemCount: widget.messages.length,
        itemBuilder: (context, idx) {
          DateFormat format = DateFormat('yyyy-MM-dd KK:mm a');
          return Card(
            child: Stack(
              children: <Widget>[
                Column(
                  children: <Widget>[
                    ListTile(
                      leading: Icon(Icons.chat),
                      title: Stack(
                        children: <Widget>[
                          Text(
                            widget.messages[idx].username,
                            style: TextStyle(fontWeight: FontWeight.bold),
                          ),
                          Positioned(
                            top: 0,
                            right: 0,
                            child: Text(
                              format.format(
                                DateTime.fromMillisecondsSinceEpoch(
                                  widget.messages[idx].createdAt),
                              ),
                              style: TextStyle(
                                fontSize: 12,
                              ),
                            ),
                          ),
                        ],
                      ),
                      subtitle: Text(widget.messages[idx].value),
                    ),
                  ],
                ),
              ],
            ),
          );
        }),
    );
  }
}
```

### Sending messages [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#sending-messages)

Finally let's see how to send a new message using the Kuzzle sdk:

_chat.dart:_

```
await _kuzzle.document.create('chat', 'messages', {
  'username': widget.username,
  'value': _chatController.text
});
```

For this we simply [create](https://docs.kuzzle.io/sdk/dart/2/controllers/document/create) a document in our `messages` collection with a `username` and a `value`. Once this document is created it will trigger a notification to all clients who subscribed to this collection and receive the message.

Where do we go from here? [#](https://docs.kuzzle.io/sdk/dart/2/getting-started/flutter#where-do-we-go-from-here)
-----------------------------------------------------------------------------------------------------------------

Now that you're more familiar with Kuzzle, dive even deeper to learn how to leverage its full capabilities:

*   discover what this SDK has to offer by browsing other sections of this documentation
*   learn more about Kuzzle [realtime engine](https://docs.kuzzle.io/core/2/guides/main-concepts/realtime-engine)
*   follow our guide to learn how to [manage users, and how to set up fine-grained access control](https://docs.kuzzle.io/core/2/guides/main-concepts/permissions)
*   lean how to use Kuzzle [Admin Console](http://next-console.kuzzle.io/) to manage your users and data
*   learn how to perform a [basic authentication](https://docs.kuzzle.io/sdk/dart/2/controllers/auth/login)
