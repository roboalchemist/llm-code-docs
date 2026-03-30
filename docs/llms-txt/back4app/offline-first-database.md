# Source: https://docs-containers.back4app.com/docs/flutter/graphql/offline-first-database.md

---
title: Offline Database
slug: docs/flutter/graphql/offline-first-database
description: In this tutorial we're going to key concepts of Flutter GraphQL application.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T19:44:48.070Z
updatedAt: 2025-01-16T20:51:33.253Z
---

# Implementing the offline first database using the GraphQL API



## Introduction

Since you are here, you must have gone through the rest of the tutorials and are familiar with executing GraphQL queries and mutations to fetch and mutate the data. In this docs, we are going to explore how to implement an offline first user interface with Flutter and GraphQL.

## Goals

- Understand internal architecture of the flutter graphql offline client
- Allowing application to run graphql queries even though application is offline
- Implement Offline data persistence

## Prerequisites

:::hint{type="info"}
- We require that the user has some basic understanding of Dart and Flutter.
- Though not necessary, the GraphQL cookbook will be useful in understanding some of the [**GraphQL concepts**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started).
- We require that you have completed the prerequisite topic [**Flutter Graphql Setup**](https://www.back4app.com/docs/flutter/graphql/flutter-graphql-setup) and have previous code setup and back4app backend implemented.
:::

## 1 - Setting up offline cache

Flutter GraphQl client supports “offline queries” by default, that is it will not throw errors if we query some GraphQL data when offline and would fetch the data from cache.

We have to note that this is different from persisting the cache across app sessions and specifically the flutter graphql client does not have cache persistence to disk. So if the app closed from the system tray and reopened the data would still need to be fetched.

To enable the same we have to enable the offline cache:

Go to [**main.dart**](https://github.com/templates-back4app/Flutter-GraphQL/blob/772c058c74d870798af1cce7a29a5046f9dda456/lib/main.dart#L32):

```dart
1   return MaterialApp(
2     home: GraphQLProvider(
3       child: CacheProvider(   // cache provider widget that provides the offline queries support.
4         child: MyHomePage(),
5       ),
6       client: client,
7     ),
8   );
```

## 2: Setting up stored preferences

One caveat while using the flutter-graphql client is that it does not store any cache of its own when the application is closed, nor does it hydrate the cache when the application is opened again.

For implementing the same we would be leveraging the flutter shared\_prefrencces library. It wraps platform-specific persistent storage for simple data (NSUserDefaults on iOS and macOS, SharedPreferences on Android, etc.), essentially allowing to store data offline in a very simple manner.

For installing the library please add in the [**pubspec.yml**](https://github.com/templates-back4app/Flutter-GraphQL/blob/772c058c74d870798af1cce7a29a5046f9dda456/pubspec.yaml#L34) file

:::BlockQuote
&#x20;shared\_preferences: **^**&#x30;.5.1&#x32;**+**&#x34;
:::

In [**main.dart**](https://github.com/templates-back4app/Flutter-GraphQL/blob/772c058c74d870798af1cce7a29a5046f9dda456/lib/main.dart#L142) add the following:

```dart
1   import 'package:shared_preferences/shared_preferences.dart';
2
3   class SharedPreferencesHelper {
4     static final String _offline_cache_key = 'programmingLanguageListResponse';
5
6     static Future<ProgrammingLanguageList> getCache() async {
7       final SharedPreferences prefs = await SharedPreferences.getInstance();
8       final cache = prefs.getString(_offline_cache_key);
9       final offlineData =
10          cache != null ? programmingLanguageListFromJson(cache) : null;
11
12      return offlineData;
13    }
14  
15    static Future<bool> setCache(dynamic value) async {
16      final SharedPreferences prefs = await SharedPreferences.getInstance();
17  
18      return prefs.setString(_offline_cache_key, jsonEncode(value));
19    }
20  }
```

Shared Preferences library stores data in a key-value form where value gets stringified into a JSON string. We will need to parse this data to our data model.

## 3 - Parsing the locally stored data

We will create a new file called programing\_languages\_model.dart. Which will store the parsing logic. We will generate this logic by pasting our graphql response in the JSON to dart model converter at [**https://app.quicktype.io/**](https://app.quicktype.io/)

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/BFcGNKTus1yY8fHPQUau8_image.png)

We will copy the generated code and create a file programing\_languages\_model.dart [**https://github.com/templates-back4app/Flutter-GraphQL/blob/flutter-graphql-offline/lib/programing\_languages\_model.dart**](https://github.com/templates-back4app/Flutter-GraphQL/blob/flutter-graphql-offline/lib/programing_languages_model.dart)

## 4 - Integrating Offline Storage logic

If the data does not exist we would be using the data from shared preferences. If the data is also not in the shared preferences we would simply show a loading icon.

We will now implement changes to integrate all the changes together, in the build method of our \_MyHomePageState we would change our build method. We would use the FutureBuilder widget to consume data from the SharedPreferencesHelper class.

```dart
1   return FutureBuilder<ProgrammingLanguageList>(
2     future: SharedPreferencesHelper.getCache(),
3     builder: (prefs, snapshot) {
4       final offlineData = snapshot.data;
5       if (!snapshot.hasError) {
6         return SafeArea(
7           ….
```

Using the FutureBuilder widget allows us to write code without having to use state. It is a relatively quick process to get the data from shared preferences. We could also show a loader while we are initialising the shared preferences and are getting data from an offline store.

We now use this offline data object and render while data from GraphQL is not available. We will also refactor the code a little bit. Following will be our code for the Query[**https://github.com/templates-back4app/Flutter-GraphQL/blob/flutter-graphql-offline/lib/main.dart**](https://github.com/templates-back4app/Flutter-GraphQL/blob/flutter-graphql-offline/lib/main.dart) widget.

```dart
1   body: Query(
2       options: QueryOptions(
3         documentNode: gql(query),
4       ),
5       builder: (
6         QueryResult result, {
7           Refetch refetch,
8           FetchMore fetchMore,
9         }) {
10          final data = result.data == null
11          ? offlineData
12          : programmingLanguageListFromJson(
13            jsonEncode(result.data));
14            if (data == null) {
15              return Center(
16                child: Text(
17                  "Loading...",
18                  style: TextStyle(fontSize: 20.0),
19                ));
20              } else {
21                SharedPreferencesHelper.setCache(data);
22                return ListView.builder(
23                  itemBuilder: (BuildContext context, int index) {
24                    if (index == 0) {
25                      return Center(
26                        child: RaisedButton(
27                          onPressed: refetch,
28                          child: result.loading == true
29                          ? Text("Loading...")
30                          : Text("Refetch"),
31                        ),
32                      );
33                    }
34                    return ListTile(
35                      title: Text(data.programmingLanguages
36                      .edges[index - 1].node.name),
37                      trailing: Text(data.programmingLanguages
38                      .edges[index - 1].node.stronglyTyped
39                      ? "Strongly Typed"
40                      : "Weekly Typed"),
41                    );
42                  },
43                  itemCount: data.programmingLanguages.edges.length + 1,
44                );
45                }
46              },
47    ),
48          ),
```

We should get the following:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ZqmUgda8xfGDIT05CbTra_flutter-graphql-offline.gif" signedSrc size="50" width="240" height="506" position="center" caption}

## Conclusion

We are now able to ensure a very good mobile experience by storing the data offline and revalidating the data when the application gets connected to the internet. Also, one important aspect that is enhancing the user experience is that the flutter-graphql client caches the old response and while sending a new request automatically. Because of which we don’t have to keep showing clumsy loading screens, while re-fetching data.

The code for the article is available at: [**https://github.com/templates-back4app/Flutter-GraphQL/tree/flutter-graphql-offline**](https://github.com/templates-back4app/Flutter-GraphQL/tree/flutter-graphql-offline)
