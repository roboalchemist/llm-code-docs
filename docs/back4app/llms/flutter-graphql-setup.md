# Source: https://docs-containers.back4app.com/docs/flutter/graphql/flutter-graphql-setup.md

---
title: GraphQL Client Setup
slug: docs/flutter/graphql/flutter-graphql-setup
description: In this tutorial we're going to key concepts of Flutter GraphQL application.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T17:59:04.725Z
updatedAt: 2025-01-16T20:51:16.498Z
---

# Flutter GraphQL Setup



## Introduction

In the last tutorial we understood the benefits of using Back4app GraphQL with Flutter. In this article we are going to setup the basic scaffold for the project and connect to the Back4app Server

## Goals

- **Setup the Flutter Environment**
- **Flutter GraphQL setup anatomy**
- **Flutter GraphQL connection**
- **Flutter GraphQL connection reuse and patterns**

## Prerequisites

:::hint{type="info"}
- We require that the user has some basic understanding of Dart and Flutter;
- Though not necessary, GraphQL cookbook will be useful in understanding the [**GraphQL concepts**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started).
:::

## 0 - Setup the App from Back4app Hub

We would need to create an app, you can follow documentation on: [**https://www.back4app.com/docs/get-started/new-parse-app**](https://www.back4app.com/docs/get-started/new-parse-app)

We would be using Back4app Hub to set up necessary classes for this tutorial.
Please go to: [**https://www.back4app.com/database/chinmay/flutter-graphql**](https://www.back4app.com/database/chinmay/flutter-graphql). Click on connect to API.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/BPEg6W5LOVp_grHWrF541_image.png)

Select the newly created app and then you are done!

## 1 - Setting up Flutter

Setting up flutter is relatively painless. We will follow the setup instructions at the [**official flutter website**](https://flutter.dev/docs/get-started/install).
After this we will create a simple flutter application using the command:

:::BlockQuote
flutter create flutter\_graphql\_setup
:::

Check if everything is OK using the command flutter doctor, by Running the application:

:::BlockQuote
cd flutter\_graphql\_setup&#x20;
flutter run
:::

## 2 - Installing the Flutter GraphQL library

For implementing this client we are going to use the flutter\_graphql library as mentioned in the first article.
We will now add adding this to your packages pubspec.yaml.

:::BlockQuote
dependencies:
graphql\_flutter: ^3.0.0
:::

## 3 - Create a Flutter GraphQL Provider

In GraphQL we do not have to work with multiple endpoints, we only have a single endpoint that is used to query the request data. And we send GraphQL queries to that endpoint. So generally what we do is that we create an instance of the client that is responsible for sending the appropriate headers and format the queries as per our need.
We will be creating a client, for this we need a link (instance of the HttpLink class) and a cache store. We will be using HttpLink as our link and OptimisticCache for our caching. Code would be written in the following manner:

In the [**main.dart**](https://github.com/templates-back4app/Flutter-GraphQL/blob/flutter-graphql-setup/lib/main.dart) we will write the following:

```dart
1   final HttpLink httpLink = HttpLink(
2         uri: 'https://parseapi.back4app.com/graphql',
3         headers: {
4           'X-Parse-Application-Id': kParseApplicationId,
5           'X-Parse-Client-Key': kParseClientKey,
6         }, //getheaders()
7       );
8
9       ValueNotifier<GraphQLClient> client = ValueNotifier(
10        GraphQLClient(
11          cache: OptimisticCache(dataIdFromObject: typenameDataIdFromObject),
12          link: httpLink,
13        ),
14      );
15
```

## 4 - Connect to Back4app using the GraphQL

Go to the Back4app Dashboard in the option “API Console” > “GraphQl Console”:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/-xlGmAHlGt5Y-dUY_Zj3J_image.png)

Note down:

1. **API url**
2. **Parse App ID**
3. **Parse Client ID**

We will create a new file [**constants.dart**](https://github.com/templates-back4app/Flutter-GraphQL/blob/flutter-graphql-setup/lib/constants.dart) in lib folder of our project.

:::BlockQuote
String kParseApplicationId= "";
String kParseClientKey = "";
:::

## 5 - Querying Data

Our component will be wrapped by the GraphQLProvider widget, which would provide necessary details for the widget.
We will need to provide an instance of client that we created in step 2.
We will use GraphQL console, to write our query. You can learn more about GraphQL queries in our [**GraphQL cookbook section.**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started)

```graphql
1   import 'package:graphql_flutter/graphql_flutter.dart';
2   import 'constants.dart';
3
4   class _MyHomePageState extends State<MyHomePage> {
5     String name;
6     String saveFormat;
7     String objectId;
8
9     String query = '''
10    query FindLanguages{
11    languages{
12      count,
13      edges{
14        node{
15          name,
16          saveFormat
17        }
18      }
19    }
20  }
21    ''';
22
23    @override
24    Widget build(BuildContext context) {
25      return SafeArea(
26        child: Scaffold(
27          appBar: AppBar(
28            title: Text(
29              'Parsing data using GraphQL',
30            ),
31          ),
32          body: Query(
33            options: QueryOptions(
34              documentNode: gql(query),
35            ),
36            builder: (
37             QueryResult result, {
38              Refetch refetch,
39              FetchMore fetchMore,
40            }) {
41              if (result.data == null) { //check if data is loading
42                return Center(
43                    child: Text(
44                  "Loading...",
45                  style: TextStyle(fontSize: 20.0),
46                ));
47              }  
48               //to implement rendering logic
49            },
50          ),
51        ),
52      );
53    }
54  }
```

## 6 -  Render the list

We will use the ListView widget to render the list, in the [**main.dart**](https://github.com/templates-back4app/Flutter-GraphQL/blob/flutter-graphql-setup/lib/main.dart)

```dart
1   else {
2                 return ListView.builder(
3                   itemBuilder: (BuildContext context, int index) {
4                     return ListTile(
5                       title: Text(result.data["programmingLanguages"]["edges"][index]["node"]['name']),
6                       trailing: Text(
7                         result.data["programmingLanguages"]["edges"][index]
8                           ["node"]['stronglyTyped'] ? "Strongly Typed":"Weekly Typed"
9                       ),
10                    );
11                  },
12                  itemCount: result.data["programmingLanguages"]["edges"].length,
13                );
14              }
15            
```

We should get the following on our screen:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/6T_PJltnmJwKxobbbkw2Q_image.png" signedSrc size="50" width="396" height="673" position="center" caption}

## Conclusion

We have configured the Flutter GraphQL client and connect to the Back4app GraphQL api.
You can find the code for the same here: [**https://github.com/templates-back4app/Flutter-GraphQL/tree/flutter-graphql-setup.**](https://github.com/templates-back4app/Flutter-GraphQL/tree/flutter-graphql-setup)
