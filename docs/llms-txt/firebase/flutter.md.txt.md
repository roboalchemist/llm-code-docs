# Source: https://firebase.google.com/docs/data-connect/quickstart/flutter.md.txt

In this quickstart, you will create and deploy a small sample database and access it from a
Flutter frontend.

## Prerequisites

To complete this quickstart, you'll need the following:

- An environment with the following tools installed:
  - Node.js with a package manager of your choice. This tutorial assumes `npm`.
  - The [Firebase CLI](https://firebase.google.com/docs/cli):

        npm i -g firebase-tools@latest

  - The [Flutter command line
    tool](https://flutter.dev/docs/get-started/install).
  - The [FlutterFire CLI](https://github.com/FirebaseExtended/flutterfire)

        dart pub global activate flutterfire_cli

- A Google Account.

## Tutorial

| Tutorial ||
|---|---|
| ### 1. Create a new Firebase project Start by creating a new Firebase project in the [Firebase console](https://console.firebase.google.com/). Then, upgrade the project to the Blaze plan. ||
| ### 2. Initialize your project Create a new directory and initialize a Firebase project in it. When prompted, choose the following options: - Choose the project you created in the previous step. - Don't create a schema with Gemini (in this tutorial, you'll use a pre-built example schema). - Create a new Cloud SQL instance. - Create a Flutter template. | mkdir myproj ; cd myproj firebase login --reauth firebase init dataconnect |
| ### 3. Review the example GraphQL definitions In Data Connect, you define all of your database schemas and operations using GraphQL. When you initialized your project, the Firebase CLI created some example definitions to get you started. | **dataconnect/schema/schema.gql (excerpt)** ``` type Movie @table { title: String! imageUrl: String! genre: String } type MovieMetadata @table { movie: Movie! @unique rating: Float releaseYear: Int description: String } ``` **dataconnect/example/queries.gql (excerpt)** ``` query ListMovies @auth(level: PUBLIC) { movies { id title imageUrl genre } } ``` |
| ### 4. Deploy your schemas and operations Whenever you make changes to your database schemas, queries, or mutations, you must deploy them for your changes to take effect on the database. | firebase deploy --only dataconnect |
| ### 5. Seed the database with sample data This seed data will give you something to look at when you test the sample app. Note that in this step you are executing arbitrary GraphQL, which is allowed for administrative tasks. | firebase dataconnect:execute dataconnect/seed_data.gql |
| ### 6. Generate a Dart client SDK This command uses your GraphQL definitions to generate a Dart library specifically for your database. You use this library in your client app to perform all database operations. You can generate libraries for multiple platforms, including Kotlin for Android, Swift for iOS, and JavaScript for web, by adding definitions to `connector.yaml`. | firebase dataconnect:sdk:generate **Auto-generated Dart SDK (excerpt)** ```dart class ExampleConnector { ListMoviesVariablesBuilder listMovies() { return ListMoviesVariablesBuilder(dataConnect); } // ... } ``` |
| ### 7. Set up a Flutter app Run these commands to set up the Flutter app to use your Firebase project. When prompted by the `flutterfire` command, select the Firebase project you created earlier, and choose the platforms you want to target. | cd flutter_app flutter pub add firebase_core firebase_data_connect flutterfire configure |
| ### 8. Write a sample Flutter client Replace the contents of `flutter_app/lib/main.dart` with this simple Flutter app. Notice that the app completes the necessary database access using a function from the generated SDK. | ```dart import 'package:firebase_core/firebase_core.dart'; import 'package:firebase_data_connect/firebase_data_connect.dart'; import 'package:flutter/material.dart'; import 'package:flutter_app/dataconnect_generated/generated.dart'; import 'package:flutter_app/firebase_options.dart'; class MyApp extends StatelessWidget { late final Future<QueryResult<ListMoviesData, void>> _movieListFuture; MyApp({super.key}) { _movieListFuture = ExampleConnector.instance .listMovies() .execute(); } @override Widget build(BuildContext context) { return MaterialApp( home: FutureBuilder( future: _movieListFuture, builder: (context, snapshot) { if (snapshot.connectionState == ConnectionState.done) { return ListView.builder( scrollDirection: Axis.vertical, itemBuilder: (context, index) => Card( child: Text( snapshot.data?.data.movies[index].title ?? "", ), ), itemCount: snapshot.data?.data.movies.length ?? 0, ); } return const CircularProgressIndicator(); }, ), ); } } Future<void> main() async { await Firebase.initializeApp( options: DefaultFirebaseOptions.currentPlatform, ); runApp(MyApp()); } ``` |
| ### 9. Try the app Start the development server to see the example app in action. | flutter run |

## Next steps

### Try the Visual Studio Code extension

When developing with Data Connect, we strongly recommend using the
[Visual Studio
Code extension](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.firebase-dataconnect-vscode). Even if you don't use Visual Studio Code as your primary development
environment, the extension provides several features that make schema and operation
development more convenient:

- A GraphQL language server, providing syntax checking and autocomplete suggestions specific to Data Connect
- CodeLens buttons in line with your code that let you read and write data from your schema definition files and execute queries and mutations from your operation definitions.
- Automatically keep your generated SDKs synchronized with your GraphQL definitions.
- Simplified local emulator setup.
- Simplified deployment to production.

### Use the Data Connect emulator for
local development

Although this tutorial showed you how to deploy Data Connect schemas and operations
directly to production, you will likely not want to make changes to your production database
while you are actively developing your app. Instead, set up the
[Data Connect emulator](https://firebase.google.com/docs/data-connect/data-connect-emulator-suite)
and do your development work against it rather than production. The emulator sets up a local
PGlite instance that behaves similarly to a live Postgres instance on CloudSQL.

### Learn how to write schemas and
operations for your app

When developing apps with Data Connect, the design of your schemas and operations
is one of the first and most important development tasks you will complete.

- [Gemini in the Firebase
  console](https://console.firebase.google.com/project/_/dataconnect/) is an AI tool that can generate Data Connect schemas from a natural language description of your app. This tool can get you started very quickly, especially if you've never worked with relational databases before.
- Alternatively, you can write database schemas, queries, and mutations directly using GraphQL. Start with the [Design Data Connect
  schemas](https://firebase.google.com/docs/data-connect/schemas-guide) page and continue to the follow-up pages to learn how to write operations.