# Source: https://docs-containers.back4app.com/docs/flutter/graphql/flutter-graphql.md

---
title: Intro to GraphQL
slug: docs/flutter/graphql/flutter-graphql
description: In this tutorial we're going to key concepts of Flutter GraphQL application.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T17:49:58.788Z
updatedAt: 2025-01-17T01:31:50.533Z
---

## Flutter GraphQL on Back4App

## Introduction

Since you are here delving into Back4app docs, you know that Back4app is a flexible low code Backend. It allows you to interact with your backend in several different ways, the way you like it. If you want you can use the REST API, or you can directly use a [**Native SDK**](https://pub.dev/packages/parse_server_sdk) for flutter. In this tutorial series, we are going to explore using the new shiny GraphQL API with Flutter.

This guide was written by Chinmay, a [**Back4App Partner**](https://www.back4app.com/partners/software-development-company) at Hybrowlabs

## Goals

- **Get an overview of GraphQL;**
- **Understand how GraphQL and Flutter fit in together;**
- **Understand Flutter tooling and libraries available for GraphQL;**
- **Understanding the general architecture and key concepts in a Flutter GraphQL application;**

## Prerequisites

:::hint{type="info"}
- We require that the user has some basic understanding of Dart and Flutter;
- Though not necessary, GraphQL cookbook will be useful in understanding the [**Back4App GraphQL spec**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started)
:::

## What is GraphQL

GraphQL is an alternative architecture to the REST API standard. GraphQL was born when the Facebook team was rebuilding their native applications from scratch and they were in heavy need to optimize the data they received from the backend.

While they were refactoring their services as a set of resources, they got frustrated because it was taking them nowhere.

They took a step back and rethought the data as an interconnected graph of objects instead of isolated REST resources. This made a big difference to their application architecture and that’s how GraphQL was born. Since GraphQL was released out in the wild in 2015, it has been getting huge popularity and buzz and has been adopted for use in teams like Twitter, Airbnb, Atlassian, Github.

## Why GraphQL?

At Hybrowlabs, a [**Back4App Partner**](https://www.back4app.com/partners/software-development-company), we build modern, data-intensive web and mobile applications. We adopted Back4app as our backend service of choice because of its ease of use, optimization, and schema definition features that are provided on top of the already awesome databases.

Most of the time the applications in the applications we engineer data that gets displayed or manipulated are not just from a single Back4App class. Rather this data comes from multiple classes. The Back4App-GraphQL combo makes it very easy for us to tackle such scenarios.

All the while it allows us to reduce the network footprint to 2-3 calls per screen load, just bringing the data we want. On the other hand cloud code that we define easily gets documented because of the strongly typed nature of GraphQL. This makes our code maintainable and easy to understand.

**TLDR; here are the advantages of using GraphQL**

1. Network footprint gets minimized
2. Efficient queries and query batching
3. Better code management
4. Strongly typed nature brings predictability.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Vw4PxvzPMzvFcRagwTaOD_image.png)

## Flutter and Back4App GraphQL

It is often very difficult to architect a GraphQL backend solution combining the flexibility of NoSQL databases while preserving structure and organization provided by having a type and schema structure of GraphQL.
Back4app has always had this structured schema-based design and now GraphQL takes it to a whole new level by creating an API knowing semantics of the type system.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/qDVwsETOs-0QgePh1AsEH_image.png)

On the other hand, as we know Dart (which is what Flutter is based on) is a strongly typed language. Yes, Dart is very particular of the type of safety.
With GraphQL we have a schema that can be reused on the client-side. This makes life a lot easier. Also knowing the type-schema that can be fetched in the future really helps as it allows us to implement advanced caching and query invalidation algorithms on this data.

## Flutter toolkit for Back4App GraphQL

For interacting with our GraphQL API we will leverage the awesome [**graphql-flutter**](https://github.com/zino-app/graphql-flutter) library. So let’s understand the features the library provides:

- Support for Queries and Mutations.
- All the schema defined on the Back4App dashboard is directly converted to the Back4app GraphQL endpoints and available either as Queries or Mutations.
- Queries allow us to get nested data from multiple classes in a single API call.
- Queries are mainly done for the purpose of data fetching, and they are cached by
- Back4app GraphQL allows rich query methods, supporting geolocation, time, regex, and full-text search features.
- Mutations allow us to make an API call that can update multiple class entries.
- Mutations consist of mainly creating, editing, deleting data.

Following is a ProgramingLanguage Class that I have created on Back4App:

When navigating into the GraphQL section of the API for Back4App, you will see the previously illustrated console of Back4App. This console will now have all the mutations and queries automatically created!

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cG1rrBLhH48XHFJUWFnZI_image.png)

When i go to the GraphQL section of the API for Back4App, we will see the previously illustrated console of Back4App. This console will now have all the mutations and queries automatically created!

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/847tlfr2XUmWrZQVyqiJo_image.png)

In the above picture I have used Back4App GraphQL for the listing of all my languages from the ProgrammingLanguage class.
Similarly we can create an entry in our ProgrammingLanguage Back4App class by leveraging mutations.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/AaG6rap9yOmL72UdhPMhF_image.png)

### **Query polling**

```graphql
1   Query(
2   Query(  
3   options: QueryOptions(
4       document: GET_ALL_PROGRAMMING_LANGUAGES, // this is the query string you just created
5       pollInterval: 10, //setting up polling
6       ),
7     builder: (QueryResult result) {
8       if (result.errors != null) {
9         return Text(result.errors.toString());
10      }
11
12      if (result.loading) {
13        return Text('Loading');
14      }
15
16      // it can be either Map or List
17      List programmingLanguages = result.data['programmingLanguages'];
18
19      return ListView.builder(
20        itemCount: programmingLanguages.length,
21        itemBuilder: (context, index) {
22          final repository = programmingLanguages[index];
23          return Text(programmingLanguages['name']);
24      });
25    },
26  );
```

- For some use cases, wherein subscriptions might be an overkill. We need to refresh data periodically, we can use the query polling feature of the client.
- This allows us to fetch the latest data in a periodic manner. For example, we can do a background data fetch every 1 minute.

### **In-memory cache**

```graphql
1   static Future<QueryResult> callQuery(
2         {dynamic documentNode, dynamic variables, FetchPolicy fetchPolicy}) {
3       return _singleton._client.query(
4         QueryOptions(
5           context: _singleton.context,
6           documentNode: documentNode,
7           variables: variables,
8           fetchPolicy: fetchPolicy ?? FetchPolicy.cacheAndNetwork,
9         ),
10      );
11    }
```

The Flutter GraphQL client implements various ways of caching the data, they are:

- Cache while Revalidate: Let’s consider a simple example of fetching a list of articles. We want the list data to be cached, when we move from a list to a specific article and then back. Cache while revalidating mechanism implements this method of querying the data, this means that even though an API call is being made to fetch the data, old data is used to display while new data is being fetched, when the new data becomes available, it is then shown.
- Cache-Only: In this method, a network call is only made if there is no data on our device. This is worthwhile when coupled with offline sync facilities for data points that are not going to change. This optimizes the network and saves resources.
- Network-Only: In rare cases when you don’t want to keep the cache of data, then you can use the Network Only mode of the Flutter GraphQL library.

### **Offline cache sync**

Mobile experience expects that it is offline enabled by default. Doing this with Flutter and Rest API is very tedious. You have to store the data into the SQLite database, check if the data is present or not, write SQL queries to fetch the data, and then also do the network calls to update the data.

That is a lot of work, which is totally bypassed with the use of this plugin and offline support for Queries comes baked into our Flutter application.

### **File Storage**

```graphql
1   mutation($files: [Upload!]!) {
2     multipleUpload(files: $files) {
3       id
4       filename
5       mimetype
6       path
7     }
8   }
9
10  import 'package:http/http.dart';
11  
12  // ...
13
14  String filePath = '/aboslute/path/to/file.ext';
15  final file = await multipartFileFrom(File(filePath));
16  
17  final QueryResult r = await graphQLClientClient.mutate(
18    MutationOptions(
19      documentNode: gql(uploadMutation),
20      variables: {
21        'files': [file],
22      },
23    )
24  );gr
```

Many GraphQL server libraries do not support a file upload facility using the GraphQL queries. For uploading a file we have to call a separate REST endpoint. Upload the file, get the URL, then pass it to the GraphQL API in the form of a string. Also, we have to manually maintain the file metadata like filename, etc.

Back4App has support for file upload standards backed into the Back4App GraphQL API. When the file is uploaded, it is uploaded as a FILE type of GraphQL, which corresponds to a Back4app FILE in GraphQL. Automatically, we have stored the file into highly scalable Back4app File storage backed by AWS S3.

### **Optimistic results**

```graphql
1   FlutterWidget(
2     onTap: () {
3       toggleStar(
4         { 'starrableId': repository['id'] },
5         optimisticResult: {
6           'action': {
7             'starrable': {'viewerHasStarred': !starred}
8           }
9         },
10      );
11    },
12  )
```

Users have come to expect a very engaging UI, and instantaneous feedback. Optimistic UI is a UI/UX principle which in essence says that we should not for the action to become over. But instead, we show feedback to the user that we have completed the action!

This is done with the assumption that the action will mostly succeed 99% of the time. If the action unfortunately fails we show a failure message saying we could not complete the action.

Flutter GraphQL comes with baked in support for defining the optimistic mutations which makes it far easier to implement this complex UI interaction system.
Thus with this, we have a very well-optimized base for building modern-day applications.

## Conclusion

In this guide we introduced you to some important advantages of using GraphQL on your Flutter project on Back4App. In the next guide we are going to put our hands on code and start by setting up our Flutter GraphQL Client for using Back4App API.
