# Source: https://firebase.google.com/docs/data-connect/flutter-sdk.md.txt

<br />

Firebase Data Connectclient SDKs let you call your server-side queries and mutations directly from a Firebase app. You generate a custom client SDK in parallel as you design the schemas, queries and mutations you deploy to yourData Connectservice. Then, you integrate methods from this SDK into your client logic.

As we've mentioned elsewhere, it's important to note thatData Connectqueries and mutations are not submitted by client code and executed on the server. Instead, when deployed,Data Connectoperations are stored on the server like Cloud Functions. This means you need to deploy corresponding client-side changes to avoid breaking existing users (for example, on older app versions).

That's whyData Connectprovides you with a developer environment and tooling that lets you prototype your server-deployed schemas, queries and mutations. It also generates client-side SDKs automatically, while you prototype.

When you've iterated updates to your service and client apps, both server- and client-side updates are ready to deploy.

## What is the client development workflow?

If you followed the[Get started](https://firebase.google.com/docs/data-connect/quickstart), you were introduced to the overall development flow forData Connect. In this guide, you'll find more detailed information about generating Flutter SDKs from your schema and working with client queries and mutations.

To summarize, to use generated Flutter SDKs in your client apps, you'll follow these prerequisite steps:

1. Add Firebase to your[Flutter](https://firebase.google.com/docs/flutter/setup)app.
2. Install the flutterfire CLI`dart pub global activate flutterfire_cli`.
3. Run`flutterfire configure`.

Then:

1. Develop your app schema.
2. Set up SDK generation:

   - With the**Add SDK to app**button in our Data Connect VS Code extension
   - By[updating your`connector.yaml`](https://firebase.google.com/docs/data-connect/flutter-sdk#generate-flutter).
3. [Initialize your client code and import libraries](https://firebase.google.com/docs/data-connect/flutter-sdk#set-client).

4. [Implement calls to queries](https://firebase.google.com/docs/data-connect/flutter-sdk#using-queries)and[mutations](https://firebase.google.com/docs/data-connect/flutter-sdk#using-mutations).

5. [Set up and use theData Connectemulator](https://firebase.google.com/docs/data-connect/flutter-sdk#prototype-and)and iterate.

## Generate your Flutter SDK

Use theFirebaseCLI to set upData Connectgenerated SDKs in your apps. The`init`command should detect all apps in the current folder and install generated SDKs automatically.  

    firebase init dataconnect:sdk

### Update SDKs while prototyping

If you have Data Connect VS Code extension installed, it will always keep generated SDKs up to date.

If you don't use Data Connect VS Code extension, you can use Firebase CLI to keep generated SDKs up to date.  

    firebase dataconnect:sdk:generate --watch

### Generate SDKs in build pipelines

You can use the Firebase CLI to generate Data Connect SDKs in CI/CD build processes.  

    firebase dataconnect:sdk:generate

## Set up client code

### Initialize yourData Connectapp

First, initialize your app using the[standard Firebase setup instructions](https://firebase.google.com/docs/flutter/setup).

Then, install theData Connectplugin:  

    flutter pub add firebase_data_connect

### Initialize theData ConnectFlutter SDK

Initialize yourData Connectinstance using the information you used to set up Data Connect (all available in theFirebaseconsole Data Connect tab).

#### Import libraries

There are two sets of imports needed to initialize your client code, generalData Connectimports and specific, generated SDK imports.  

    // general imports
    import 'package:firebase_data_connect/firebase_data_connect.dart';

    // generated queries and mutations from SDK
    import 'generated/movies.dart';

## Use queries on the client side

The generated code will already come with predefined Query Refs. All you need to do is import and call`execute`on them.  

    import 'generated/movies.dart';

    await MoviesConnector.instance.listMovies().execute();

### Call SDK query methods

Here's an example using these action shortcut functions:  

    import 'generated/movies.dart';

    function onBtnClick() {
      // This will call the generated Dart from the CLI and then make an HTTP request to the server.
      MoviesConnector.instance.listMovies().execute().then(data => showInUI(data)); // == MoviesConnector.instance.listMovies().ref().execute();
    }

#### Optional fields

Some queries may have optional fields. In these cases, the Flutter SDK exposes a builder method, and will have to be set separately.

For example, the field`rating`is optional when calling`createMovie`, so you need to provide it in the builder function.  

    await MoviesConnector.instance.createMovie({ title: 'Empire Strikes Back', releaseYear: 1980, genre: "Sci-Fi"}).rating(5).execute();

### Subscribe to changes

You can subscribe to changes (which will update any time you execute a query).  

    QueryRef<ListMoviesData, void> listRef = MoviesConnector.instance.listMovies().ref();

    // subscribe will immediately invoke the query if no execute was called on it previously.
    listRef.subscribe().listen((data) {
      updateUIWithMovies(data.movies);
    });

    await MoviesConnector.instance.createMovie({ title: 'Empire Strikes Back', releaseYear: 1980, genre: "Sci-Fi" }).rating(5).execute();
    await listRef.execute(); // will update the subscription above`

### Handle changes to enumeration fields

An app's schema can[contain enumerations](https://firebase.google.com/docs/data-connect/schemas-guide#enumeration-fields), which can be accessed by your[GraphQL queries](https://firebase.google.com/docs/data-connect/queries-guide#query-enumerations).

As an app's design changes, you may add new enum supported values. For example, imagine that later in your application's lifecycle you decide to add a FULLSCREEN value to the`AspectRatio`enum.

In theData Connectworkflow, you can use local development tooling to update your queries and SDKs.

However, before you release an updated version of your clients, older deployed clients may break.

#### Example resilient implementation

The generated SDK forces handling of unknown values. That is, client code must unwrap the`EnumValue`object into either`Known`or`Unknown`.  

    final result = await MoviesConnector.instance.listMovies().execute();

    if (result.data != null && result.data!.isNotEmpty) {
      handleEnumValue(result.data![0].aspectratio);
    }

    void handleEnumValue(EnumValue<AspectRatio> aspectValue) {
      if (aspectValue.value != null) {
        switch(aspectValue.value!) {
          case AspectRatio.ACADEMY:
            print("This movie is in Academy aspect");
            break;
          case AspectRatio.WIDESCREEN:
            print("This movie is in Widescreen aspect");
            break;
          case AspectRatio.ANAMORPHIC:
            print("This movie is in Anamorphic aspect");
            break;
          case AspectRatio.IMAX:
            print("This movie is in IMAX aspect");
        }
      } else {
        print("Unknown aspect ratio detected: ${aspectValue.stringValue}");
      }
    }

## Use mutations on the client side

Mutations are accessible in the same way as queries.  

    await MoviesConnector.instance.createMovie({ title: 'Empire Strikes Back', releaseYear: 1980, genre: "Sci-Fi" }).rating(5).execute();

## Prototype and test your Flutter apps

### Instrument clients to use a local emulator

You can use theData Connectemulator, whether from the Data Connect VS Code extension or from the CLI.

Instrumenting the app to connect to the emulator is the same for both scenarios.  

    import 'package:firebase_data_connect/firebase_data_connect.dart';
    import 'generated/movies.dart';

    MoviesConnector.instance.dataConnect
              .useDataConnectEmulator('127.0.0.1', 9399);

    // Make calls from your app
    QueryRef<ListMoviesData, void> ref = MoviesConnector.instance.listMovies.ref();

To switch to production resources, comment out lines for connecting to the emulator.

## Data types in the Dart SDK

TheData Connectserver represents common GraphQL data types. These are represented in the SDK as follows.

| Data Connect Type |              Dart               |
|-------------------|---------------------------------|
| Timestamp         | firebase_data_connect.Timestamp |
| Int (32-bit)      | int                             |
| Date              | DateTime                        |
| UUID              | string                          |
| Int64             | int                             |
| Float             | double                          |
| Boolean           | bool                            |
| Any               | firebase_data_connect.AnyValue  |