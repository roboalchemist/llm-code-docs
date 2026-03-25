# Source: https://docs-containers.back4app.com/docs/flutter/parse-sdk/users/flutter-query-users.md

---
title: Query Users
slug: docs/flutter/parse-sdk/users/flutter-query-users
description: In this guide you'll learn how to query users in Parse on Flutter
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T15:00:20.690Z
updatedAt: 2025-01-16T20:37:23.859Z
---

# Querying users in Parse on Flutter

## Introduction

Some applications need to directly manage users or be able to view a list of them. Parse has query tools and they can be used to list the users of your application.

In this guide, you will learn how to use ParseQuery to perform user queries in your Flutter application using the **Flutter plugin for Parse Server**.

## Goal

To build a user querying feature using Parse for a Flutter App.

## Prerequisites

**To complete this tutorial, you will need:**

:::hint{type="info"}
- [**Flutter version 2.2.x or later**](https://flutter.dev/docs/get-started/install)
- [**Android Studio&#x20;**](https://developer.android.com/studio)or [**VS Code installed**](https://code.visualstudio.com/) (with [**Plugins**](https://docs.flutter.dev/get-started/editor) Dart and Flutter)
- An app [**created**](https://www.back4app.com/docs/get-started/new-parse-app) on Back4App:
  - **Note:&#x20;**&#x46;ollow the [**New Parse App Tutorial**](https://www.back4app.com/docs/get-started/new-parse-app) to learn how to create a Parse App on Back4App.
- An Flutter app connected to Back4app.
  - **Note:&#x20;**&#x46;ollow the [**Install Parse SDK on Flutter project**](https://www.back4app.com/docs/flutter/parse-sdk/parse-flutter-sdk) to create an Flutter Project connected to Back4App.
- A device (or virtual device) running Android or iOS.
:::

## Understanding the Query Users App

To better understand the Query Users process, we will create an app to query. We won’t explain the Flutter application code once this guide’s primary focus is using the Flutter with Parse.

Following the next steps, you will build a Todo App that will store the tasks at Back4App Database.

## Let’s get started!

Following the next steps you will be able to build a Sign App that will create user Account in Back4App Database.

## 1 - Create Query Users App Template

Open your Flutter project from the previous guide **Flutter plugin for Parse Server**. Go to the main.dart file, clean up all the code, and replace it with:

```dart
1   import 'dart:async';
2
3   import 'package:flutter/material.dart';
4   import 'package:parse_server_sdk_flutter/parse_server_sdk.dart';
5
6   void main() async {
7     WidgetsFlutterBinding.ensureInitialized();
8  
9     final keyApplicationId = 'YOUR_APP_ID_HERE';
10    final keyClientKey = 'YOUR_CLIENT_KEY_HERE';
11    final keyParseServerUrl = 'https://parseapi.back4app.com';
12
13    await Parse().initialize(keyApplicationId, keyParseServerUrl,
14        clientKey: keyClientKey, debug: true);
15  
16    runApp(MaterialApp(
17      home: Home(),
18    ));
19  }
20
21  class Home extends StatefulWidget {
22    @override
23    _HomeState createState() => _HomeState();
24  }
25 
26  class _HomeState extends State<Home> {
27    final _scaffoldKey = GlobalKey<ScaffoldState>();
28  
29    @override
30    Widget build(BuildContext context) {
31      return Scaffold(
32          appBar: AppBar(
33            title: Text("Parse Query Users"),
34            backgroundColor: Colors.blueAccent,
35            centerTitle: true,
36          ),
37          key: _scaffoldKey,
38          body: FutureBuilder<List<ParseObject>>(
39              future: doUserQuery(),
40              builder: (context, snapshot) {
41                switch (snapshot.connectionState) {
42                  case ConnectionState.none:
43                  case ConnectionState.waiting:
44                    return Center(
45                      child: Container(
46                          width: 100,
47                          height: 100,
48                          child: CircularProgressIndicator()),
49                    );
50                  default:
51                    if (snapshot.hasError) {
52                      return Center(
53                        child: Text("Error...: ${snapshot.error.toString()}"),
54                      );
55                    } else {
56                      if (snapshot.data!.isEmpty) {
57                        return Center(
58                          child: Text('None user found'),
59                        );
60                      }
61  
62                      return ListView.builder(
63                          padding: EdgeInsets.only(top: 10.0),
64                          itemCount: snapshot.data!.length,
65                          itemBuilder: (context, index) {
66                            final user = snapshot.data![index] as ParseUser;
67                            final userVerified = user.emailVerified ?? false;
68                            return ListTile(
69                              title: Text(
70                                  'Username: ${user.username} - Verified: ${userVerified.toString()}'),
71                              subtitle: Text(user.createdAt.toString()),
72                            );
73                          });
74                    }
75                }
76              }));
77    }
78
79    Future<List<ParseObject>> doUserQuery() async {
80      return [];
81    }
82  }
83
```

:::hint{type="info"}
When debug parameter in function Parse().initialize is true, allows displaying Parse API calls on the console. This configuration can assist in debugging the code. It is advisable to disable debug in the release version.
:::

## 2 - Connect Template to Back4app Project

Find your Application Id and Client Key credentials navigating to your app Dashboard at [**Back4App Website**](https://www.back4app.com/).

Update your code in main.dart with the values of your project’s ApplicationId and ClientKey in Back4app.

- **keyApplicationId = App Id**
- **keyClientKey = Client Key**

Run the project, and the app will load as shown in the image.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-9q1hAy87h1LFCBqdVRdx_image.png" signedSrc size="50" width="322" height="638" position="center" caption}

## 3 - Code for Query Users

Any Parse query operation uses the ParseQuery object type, which will help you retrieve specific data from your database throughout your app.

A ParseQuery will only resolve after calling a retrieve method, so you can set up a query and chain its several modifiers before submitting the retrieve method.

To create a new ParseQuery, you need to pass as a parameter the desired ParseObject subclass, which is the one that will contain your query results.

You can see a user query example below. Using the code provided, find the doUserQuery function in the file main.dart. Replace the code inside doUserQuery with:

```dart
1       QueryBuilder<ParseUser> queryUsers =
2           QueryBuilder<ParseUser>(ParseUser.forQuery());
3       final ParseResponse apiResponse = await queryUsers.query();
4   
5       if (apiResponse.success && apiResponse.results != null) {
6         return apiResponse.results as List<ParseObject>;
7       } else {
8         return [];
9       }
```

To build this function, follow these steps:

1. Create an instance ofParseQuery class e pass as a parameter to the ParseUser.forQuery
2. Call thequery function that will execute the query against the database.
3. If the operations succeed, will return a list ofParseUser objects. If the operation does not find any objects, the success property will be false, and the results are null.

The complete code should look like this:

```dart
1     Future<List<ParseObject>> doUserQuery() async {
2       QueryBuilder<ParseUser> queryUsers =
3           QueryBuilder<ParseUser>(ParseUser.forQuery());
4       final ParseResponse apiResponse = await queryUsers.query();
5
6       if (apiResponse.success && apiResponse.results != null) {
7         return apiResponse.results as List<ParseObject>;
8       } else {
9         return [];
10      }
11    }
```

You can also try to retrieve a single user using the following structure:

:::BlockQuote
&#x20; user?.get("username");
:::

:::hint{type="info"}
To test it, click on the Run button in Android Studio/VSCode.
:::

After performing this query, your user list on your app should be showing something like this:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/CJFg4YCROokh3Wye9z4LN_image.png" signedSrc size="50" width="322" height="638" position="center" caption}

## It’s done!

At the end of this guide, you learned how to perform queries on Parse users on Flutter.
