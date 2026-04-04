# Source: https://docs-containers.back4app.com/docs/flutter/graphql/flutter-graphql-project-with-source-code-download.md

---
title: Start from Template
slug: docs/flutter/graphql/flutter-graphql-project-with-source-code-download
description: In this guide you learn how to download and start using a complete (frontend and backend) Flutter App template with GraphQL.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T18:07:29.171Z
updatedAt: 2025-01-16T20:51:21.831Z
---

# Download a Flutter GraphQL project with source code and start using Back4App



## Introduction

In this tutorial, we are going to build an application that would parse data from Back4App backend through GraphQL. As you may know, GraphQL is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data. Back4App is a low code backend as a Service(based on Open Source Parse Platform) which is helping developers to build extensible and scalable mobile and web applications at a rapid pace.

## Goals

The main goal is to build a simple app that is going to show a list of programming languages and their save type format.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/_-4cKpBMuxZgozn0f7GK8_image.png" signedSrc size="50" width="249" height="441" position="center" caption}

At the end of this article we expect that you will be able to:

- **Make an API call on Back4App using GraphQL;**
- **Get the data from GraphQL API;**
- **Fetch data in your Flutter App.**

### Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- An IDE for writing Flutter code like Android Studio or Flutter. However we will be using Android Studio for this tutorial.
- A Back4App account that can be created here: [**Back4App**](https://www.back4app.com/)
- [**GraphQL\_flutter**](https://pub.dev/packages/graphql_flutter)
:::

## 1 -  Clone project from Github to Android Studio

Go to the [**Github repo**](https://github.com/templates-back4app/Flutter-GraphQL), and download the ZIP file, extract it, and open it in your flutter IDE.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/pWqIPMznW1Jcd-AyBCc3C_image.png)

To complete this step, drag the folder inside the zip file into your desktop, open Android Studio and then click on Open existing Android Studio Project. The project directory over would be usually ‘*C:\Users\Username\Desktop\back4App\_GraphQL-starting\_code*’.

But this may be different for different users.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/NPwmVfaQbmfUk6XN_XTkq_image.png)

Open the project and go to the lib\main.dart file. You will see so many errors there, don’t worry, just press all ‘*Get dependencies*’ and all the errors would perish. If doesn’t then just press ‘*Upgrade dependencies*’.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Zot364iTdLBDGfAi7pihY_image.png)

The code in your main.dart should look like this.

```dart
1   import 'package:flutter/material.dart';
2   import 'package:graphql_flutter/graphql_flutter.dart';
3   import 'consonents.dart';
4
5   void main() {
6     runApp(MyApp());
7   }
8
9   class MyApp extends StatelessWidget {
10    @override
11    Widget build(BuildContext context) {
12      return MaterialApp(
13        home: MyHomePage(),
14        ),
15      );
16    }
17  }
18  class MyHomePage extends StatefulWidget {
19    @override
20    _MyHomePageState createState() => _MyHomePageState();
21  }
22
23  class _MyHomePageState extends State<MyHomePage> {
24  
25    @override
26    Widget build(BuildContext context) {
27      return SafeArea(
28        child: Scaffold(
29          appBar: AppBar(
30            title: Text('Parsing data using GraphQL',
31            ),
32          ),
33          body: Container(),
34      ),);
35    }
36  }
```

If you open Run the app now you would only see an empty Screen in your emulator/device with only an AppBar titled *‘Parsing data using GraphQL’*.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/gvYh8hgqNlREnr-l-q-KR_image.png" signedSrc size="50" width="247" height="442" position="center" caption}

We will work on main.dart file and our important values are stored in consonents.dart and we can directly use it from there. We will require the graphql\_flutter dependency to use graphQL in our app.

:::hint{type="info"}
The graphql\_flutter is most popular GraphQL cliet for flutter. It helps us to use *GraphQL* queries directly in our code. It provides us with GraphQLClient, GraphQLProvider and many other useful widgets that helps us to parse data from our database directly with the help of GraphQL without even using StreamBuilder. The package provides us with plenty of features including:

- Subscriptions
- In memory cache
- Offline cache sync
- Optimistic results
- GraphQl file uploads
:::

You can import it by writing the following code in pubspec.yaml file:

:::BlockQuote
dependencies:
&#x20; graphql\_flutter: **^**&#x33;.1.0
:::

:::hint{type="info"}
See more about graphql\_flutter at [**GraphQL Flutter Documentation**](https://pub.dev/packages/graphql_flutter)
:::

All dependencies are already pre-installed and you are good to proceed to the next step now.

## 2 - Creating backend in Back4App

After you have signed up at [**Back4App**](https://www.back4app.com/) website, u can proceed to the next step and create a new app. Click on *‘Build new App’*. Give it the same name as your project name which over here is *‘back4app\_Graphql’*.

Now scroll down to *Server settings* on your left and select *Settings* Manage Parse Server Card, then select the option *‘3.10.0 - Parse Server 3.10.0’* from the list. Now press the save button below and wait until it gets saved.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/IvwhiBtWYUgBFYASsT2z-_image.png)

Now come back to *Core* (on the left), select the *API console*, and select *GraphQL Console* from it.

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/h900ERbA5Rem8OAJb9c8q_image.png)

This is the window where you can write and test your GraphQL queries/mutations code. Let’s proceed to the next step.

## 3 - Creating and getting data through GraphQL

Now, let’s test the GraphQL API on Back4App using the GraphQL API Console. First, paste the following query on the left code-box:

```graphql
1       mutation CreateClass {
2   		    createClass(input:{
3   	    name: "Language"
4    	    schemaFields: {
5   	      addStrings: [{name: "name"}{name: "saveFormat"}]
6   	    }
7   	  }){
8   	    class{
9   	      schemaFields{
10  		name
11   		__typename
12  	      }
13  	    }
14  	  }
15  	}
16
```

The code above will create a class named “Language”. Let’s populate this new class with some rows:

```graphql
1       mutation CreateObject{
2   	  createLanguage(input:{fields: {name: "Python", saveFormat:".py"}}){
3   	    language{
4   	      name,
5   	      saveFormat
6   	    }
7   	  }
8   	}
```

If your operation is successful you’ll see this message on the right code-box on GraphQL PlayGround:

```graphql
1       {
2   	  "data": {
3   	    "createLanguage": {
4    	      "language": {
5    		    "name": "Python",
6   		      "saveFormat": ".py"
7   	      }
8   	    }
9   	  }
10   	}
```

Mutations are used to create or make changes on a class. By running the above mutation, we’ll create a new class named Language with data fields:

- **name: “Python”**
- **saveFormat: “.py”**

Repeat the process and create two more objects in the same Class for:

- **name: “C” and saveFormat: “.c”**
- **name: “java” and saveFormat: “.java”.**

The mutation for this will be such:

```graphql
1       mutation CreateObject{
2   	  createLanguage(input:{fields: {name: "C", saveFormat:".c"}}){
3    	    language{
4    	      name,
5    	      saveFormat
6    	    }
7   	  }
8    	}
```

Java:

```graphql
1       mutation CreateObject{
2   	  createLanguage(input:{fields: {name: "Java", saveFormat:".java"}}){
3   	    language{
4   	      name,
5    	      saveFormat
6    	    }
7   	  }
8   	}
```

Now let’s see all the data in our class *Languages*. For reading data we use*query*. So go ahead and type the below command.

```graphql
1       query FindLanguages{
2   	  languages{
3   	    count,
4   	    edges{
5   	      node{
6   		name,
7    		saveFormat
8   	      }
9   	    }
10  	  }
11  	}
```

In query FindLanguage ‘FindLanguage’ is just a name for your query command and you could even name it anything else. We use the find(className: "") command to find all the elements of the specific Class. count, returns the number of elements in the Class and all the elements are shown inside the result object.

The above query is going to return this:

```graphql
1       {
2   	  "data": {
3   	    "languages": {
4   	      "count": 3,
5   	      "edges": [
6   		{
7   		  "node": {
8   		    "name": "Python",
9   		    "saveFormat": ".py"
10  		  }
11  		},
12  		{
13  		  "node": {
14  		    "name": "C",
15  		    "saveFormat": ".c"
16  		  }
17  		},
18  		{
19  		  "node": {
20  		    "name": "Java",
21  		    "saveFormat": ".java"
22  		  }
23  		}
24  	      ]
25  	    }
26  	  }
27  	}
```

You can see all other queries in the following link:
[**GraphQL queries - Back4App**](https://blog.back4app.com/graphql-on-parse/)

Now, let’s proceed to the next step.

## 4 - Setting up GraphQL in our App

Let’s start coding our app. Before this, you must do few things in your lib\consonents.dart file:

1. Copy graphql link which is next to the history button in the top of GraphQL window, and paste it in as kUrl string datatype.
2. Now move to the bottom of the page and copy the codes from HTTP Headers, copy only the codes on the right of the colon(:) and paste them with their respective names in the lib\consonents.dart file:

![](https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/ysPVIOchEBFZ182itNksQ_image.png)

The file should have following code:

```graphql
1       String kParseApplicationId= "APPLICATION_ID_COPIED_FROM_HEADERS";
2    	String kParseClientKey = "CLIENT_KEY_COPIED_FROM_HEADER";
3   	String kUrl= "URL_COPIED";
4   	// replace "APPLICATION_ID_COPIED_FROM_HEADERS", "CLIENT_KEY_COPIED_FROM_HEADER", "URL_COPIED" with real keys/ids copied 
5   	//from Http Headers tab.
```

Now move to main.dart file and head over to MyApp Stateless Widget and add the following code just above the return MaterialApp():

```graphql
1       final HttpLink httpLink = HttpLink(
2         uri: kUrl,
3         headers: {
4           'X-Parse-Application-Id' : kParseApplicationId,
5           'X-Parse-Client-Key' : kParseClientKey,    
6         },
7       );
```

**HttpLink** is from *flutter\_graphql.dart* and takes the widget HttpLink() with two parameters.The first is the GraphQL API Url on Back4App. The second are the headers necessary to authenticate on Back4App API. After this section you need to include the GraphQL Client Code (explain what is), copy the code below and then paste under the HttpLink section:

```graphql
1       ValueNotifier<GraphQLClient> client = ValueNotifier(
2   	      GraphQLClient(
3   		    cache: OptimisticCache(dataIdFromObject: typenameDataIdFromObject),
4   		    link: httpLink,
5   	      ),
6    	    );
```

Now we’ve provided the link and cache method to our GraphQLClient. We have done this through our ValueNotifier and named it as client. Let’s wrap the MyHomePage() widget which is a child of MaterialApp with GraphQLProvider and pass MyHomePage() as its client. Add an another parameter inside GraphQLProvider namely client and pass client(name of our ValueNotifier) in it. This is how your MyApp class should look now:

```graphql
1   class MyApp extends StatelessWidget {
2     @override
3     Widget build(BuildContext context) {
4       final HttpLink httpLink = HttpLink(
5         uri: kUrl,
6         headers: {
7           'X-Parse-Application-Id' : kParseApplicationId,
8           'X-Parse-Client-Key' : kParseClientKey,        
9           //'X-Parse-REST-API-Key' : kParseRestApiKey,
10        },//getheaders()
11      );
12      ValueNotifier<GraphQLClient> client = ValueNotifier(
13        GraphQLClient(
14          cache: OptimisticCache(dataIdFromObject: typenameDataIdFromObject),
15          link: httpLink,
16        ),
17      );
18      return MaterialApp(
19        home: GraphQLProvider(
20          child: MyHomePage(),
21          client: client,
22        ),
23      );
24    }
25  }
```

Let’s call the API and get the data

## 5 - Making an API call

Now we will work on the MyHomePageState. We’re going to start by initialising a String data type named ‘query’ and assign/pass the query statement for finding all the data from our Language class to it. Since the query is multi-line, we will pass the query in triple quotes. Here’s how it looks like:

```graphql
1   String query='''
2   query FindLanguages{
3   languages{
4     count,
5     edges{
6       node{
7         name,
8         saveFormat
9       }
10    }
11  }
12 }
13  ''';
```

Now go to Query() widget, inside the body parameter of the Scaffold which have two properties:

- ***options***
- ***builder***

And then pass null for both. This is how your build method would look like:

```graphql
1     Widget build(BuildContext context) {
2       return SafeArea(
3         child: Scaffold(
4           appBar: AppBar(
5             title: Text('Parsing data using GraphQL',
6             ),
7           ),
8             body: Query(
9                 options: null,
10                builder: null
11            ),
12      ),);
13    }
```

The Query() widget helps us write queries for GraphQL and will help us read and get data. We will pass the query statement which we have taken as a string in the options and build the widget with the builder parameter.

So pass the QueryOptions() widget in options as follows:

```graphql
1   options: QueryOptions(
2               documentNode: gql(query),
3             ),
4
```

The query is passed through documentNode parameter in QueryOptions. Now let’s build with the help of builder Parameter. The builder method accepts a function with three parameters namely,

- **QueryResult result;**
- **Refetch refetch;**
- **FetchMore fetchmore.**

Right now, we only need to worry about the QueryResult which gives us the result of our query and we can access the data through result.data.
So let’s code the following below:

```graphql
1   builder : (QueryResult result, { Refetch refetch,FetchMore fetchMore,})
2            {
3              if(result.data==null){
4                return Center(child: Text("Loading...",style: TextStyle(fontSize: 20.0),));
5              }else{
6                return Text('SUCCESS');
7              }
8            },
```

In the above code we are accessing the data. If there’s no data we return a text widget reading *‘Loading…’* else we will return a Text() widget reading *‘SUCCESS’*

Here’s how your myHomePage class in main.dart should look like:

```dart
1   class MyHomePage extends StatefulWidget {
2     @override
3     _MyHomePageState createState() => _MyHomePageState();
4   }
5
6   class _MyHomePageState extends State<MyHomePage> {
7     String name;
8     String saveFormat;
9     String objectId;
10   
11    String query = '''
12    query FindLanguages{
13    languages{
14      count,
15      edges{
16        node{
17          name,
18          saveFormat
19        }
20      }
21    }
22  }
23    ''';
24  
25    @override
26    Widget build(BuildContext context) {
27      return SafeArea(
28        child: Scaffold(
29          appBar: AppBar(
30            title: Text(
31              'Parsing data using GraphQL',
32            ),
33          ),
34          body: Query(
35              options: QueryOptions(
36                documentNode: gql(query),
37              ),
38              builder: (
39                  QueryResult result, {
40                    Refetch refetch,
41                    FetchMore fetchMore,
42                  }) {
43                if (result.data == null) {
44                  return Center(
45                    child: Text(
46                      "Loading...",
47                      style: TextStyle(fontSize: 20.0),
48                    ),
49                  );
50                } else{
51                  return Text('SUCCESS');
52                }
53              }
54          ),
55        ),
56      );
57    }
58  }
```

Now, start the App and wait for a few seconds after it restarts. If you see *‘SUCCESS’* on the screen then ***Congrats! You have established your connection and called the API.***

## 6 - Getting and showing Data from API

Instead of returning the Text widget, we will return the *ListView\.builder()* widget with original data. Write the following code instead of return Text('SUCCESS').

```graphql
1   return ListView.builder(
2                       itemBuilder: (BuildContext context, int index){
3                         return ListTile(
4                           title: Text(result.data["languages"]["edges"][index]["node"]['name']),
5                           trailing: Text(result.data["languages"]["edges"][index]["node"]['saveFormat']),
6                         );
7                       },
8                       itemCount: result.data["languages"]["edges"].length,
9                     );
```

Now if you look back to your GraphQL result screen in your API console of Back4App where we typed our find method, the results were such:

```graphql
1   {
2     "data": {
3       "languages": {
4         "count": 3,
5         "edges": [
6           {
7             "node": {
8               "name": "Python",
9               "saveFormat": ".py"
10            }
11          },
12          {
13            "node": {
14              "name": "C",
15              "saveFormat": ".c"
16            }
17          },
18          {
19            "node": {
20              "name": "Java",
21              "saveFormat": ".java"
22            }
23          }
24        ]
25      }
26    }
27  }
```

So from above code the location of “Python” was:

- *“data”->&#x20;*“*languages” -> “count” -> “edges” -> “node” -> “name”*. Also notice name is inside square brackets ‘\[]’ of edges which symbolizes it is the first element of edges list/array.

So we need to enter into this location to get “Python” and same for everything else. When we write result.data, we enter the *“data”* location. So to give the other locations we add \["location\_name"] to it. So the location of “Python” will be result.data\["languages"]\["edges"]\[0]\["node"]\["name"].

When using ListView, it takes two parameters, itemCount, it tells the number of elements in the API call, itemBuilder, it takes a function with parameters (BuildContext context, int index) and returns a list widgets in which we will be showing the data. Here, we will use List of ListTile to show the data:

```dart
1   return ListView.builder(
2                        itemCount: result.data["languages"]["edges"].length,
3                       itemBuilder: (BuildContext context, int index){
4                         return ListTile(
5                           title: Text(result.data["languages"]["edges"][index]["node"]['name']),
6                           trailing: Text(result.data["languages"]["edges"][index]["node"]['saveFormat']),
7                         );
8                       },
9                       
10                    );
```

When we replace Text('SUCCESS') with the above `ListView.builder()` widget, we first pass the itemCount where we pass the number of elements in the results List and so we don’t need to worry about that anymore. In itemBuilder we are returning a list of ListTiles which will have the "name" of the "Languages" class and in "saveFormat" in the trailing. Notice we used index instead of any number after result, this is what itemCount took care of.

This is how your main.dart should look like now:

```dart
1   import 'package:flutter/material.dart';
2   import 'package:graphql_flutter/graphql_flutter.dart';
3   import 'consonents.dart';
4   import 'dart:ui';
5
6   void main() {
7     runApp(MyApp());
8   }
9 
10  class MyApp extends StatelessWidget {
11    @override
12    Widget build(BuildContext context) {
13      final HttpLink httpLink = HttpLink(
14        uri: 'https://parseapi.back4app.com/graphql',
15        headers: {
16          'X-Parse-Application-Id': kParseApplicationId,
17          'X-Parse-Client-Key': kParseClientKey,        
18        }, //getheaders()
19      );
20  
21      ValueNotifier<GraphQLClient> client = ValueNotifier(
22        GraphQLClient(
23          cache: OptimisticCache(dataIdFromObject: typenameDataIdFromObject),
24          link: httpLink,
25        ),
26      );
27 
28      return MaterialApp(
29        home: GraphQLProvider(
30          child: MyHomePage(),
31          client: client,
32        ),
33      );
34    }
35  }
36 
37  class MyHomePage extends StatefulWidget {
38    @override
39    _MyHomePageState createState() => _MyHomePageState();
40  }
41
42  class _MyHomePageState extends State<MyHomePage> {
43    String name;
44    String saveFormat;
45    String objectId;
46  
47    String query = '''
48    query FindLanguages{
49    languages{
50      count,
51      edges{
52        node{
53          name,
54          saveFormat
55        }
56      }
57    }
58  }
59    ''';
60
61    @override
62    Widget build(BuildContext context) {
63      return SafeArea(
64        child: Scaffold(
65          appBar: AppBar(
66            title: Text(
67              'Parsing data using GraphQL',
68            ),
69          ),
70          body: Query(
71            options: QueryOptions(
72              documentNode: gql(query),
73            ),
74            builder: (
75              QueryResult result, {
76              Refetch refetch,
77              FetchMore fetchMore,
78            }) {
79              if (result.data == null) {
80                return Center(
81                    child: Text(
82                  "Loading...",
83                  style: TextStyle(fontSize: 20.0),
84                ));
85              } else {
86                return ListView.builder(
87                  itemBuilder: (BuildContext context, int index) {
88                    return ListTile(
89                      title: Text(result.data["languages"]["edges"][index]["node"]
90                          ['name']),
91                      trailing: Text(result.data["languages"]["edges"][index]
92                          ["node"]['saveFormat']),
93                    );
94                  },
95                  itemCount: result.data["languages"]["edges"].length,
96                );
97              }
98            },
99          ),
100       ),
101     );
102   }
103 }
```

And our final App Screen:

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/4US1H2nsHrXZvtZzrZw3k_image.png" signedSrc size="50" width="249" height="441" position="center" caption}

## Conclusion

Now you have a Flutter App connected to a GraphQL API that can store and retrieve data on Back4App.

We did not require to encode or decode the json data separately which makes our work easier and faster using few lines of codes.

**Have a great day!**
