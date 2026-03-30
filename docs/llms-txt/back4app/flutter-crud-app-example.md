# Source: https://docs-containers.back4app.com/docs/flutter/graphql/flutter-crud-app-example.md

---
title: Mutations
slug: docs/flutter/graphql/flutter-crud-app-example
description: In this guide you learn how to download and start using a complete (frontend and backend) Flutter App template with GraphQL.
image: https://www.back4app.com/images/logo-social.png
createdAt: 2024-03-18T18:51:24.936Z
updatedAt: 2025-01-16T20:51:25.761Z
---

# Flutter CRUD app example using GraphQL



## Introduction

On our first Flutter-GraphQL guide, we’ve learned how to set up a Flutter project using GraphQL API to connect and query simple data on Back4App. Also, how we can use the Back4App GraphQL Playground to run queries/mutations to create/populate the App Database.

In this tutorial, we will add a feature with which we will directly create, update, and delete data from our Back4App backend directly from our App using GraphQL mutations.

## Goals

At the end of this article we expect that you will be able to:

- Create data in our Backend using GraphQL API.
- Update data from our Backend using GraphQL API.
- Delete existing data from Backend using GraphQL API.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/kPiedmPCadGXn4Vz8Kz3Q_flutter-createdata.gif" signedSrc size="50" width="270" height="480" position="center" caption}

## Prerequisites

:::hint{type="info"}
**To complete this tutorial, you will need:**

- You’ll need to read our previous guide [**“Flutter GraphQL Project”**](https://www.back4app.com/docs/flutter/graphql/flutter-graphql-project-with-source-code-download) in order to understand our starting point at this guide.
- We’re going to use the previous project if you don’t have it you can [**download here**](https://github.com/templates-back4app/Flutter-GraphQL).
- An IDE for writing Flutter code like Android Studio or VS code.
- A Back4App account that can be [**created here**](https://www.back4app.com/).
- [**Back4App GraphQL\_flutter dependency**](https://pub.dev/packages/graphql_flutter)
:::

:::hint{type="success"}
NOTE: If you want a better understanding of the Back4App GraphQL API take a look at our [**GraphQL Cook Book**](https://www.back4app.com/docs/parse-graphql/graphql-getting-started) and also check our GraphQL Schema on our API Playground.
:::

## 1 - Setting up GUI

Create a new file mutation\_page.dart. Here we will create our GUI for taking input from the user and perform Mutation tasks. Now paste the following code in mutation\_page.dart.

```dart
1   import 'package:back4appgraphqldemo/app_ui.dart';
2   import 'package:back4appgraphqldemo/database_utils.dart';
3   import 'package:flutter/material.dart';
4
5   class MutationPage extends StatelessWidget {
6
7     String langName,saveFormat,objectId;
8     DatabaseUtils utils;
9
10    @override
11    Widget build(BuildContext context) {
12      return AppUI(
13        onChangedName: (text){
14        langName=text;
15        },
16        onChangedSaveFormat: (text){
17                saveFormat=text;
18          },
19        onChangedObjectId: (text){
20        objectId=text;
21        },
22        sendDataButtonPressed: (){
23        },
24        deleteDataButtonPressed: (){
25        },
26        updateButtonPressed: (){
27        },
28      );
29    }
30  }
```

AppUI() widget has already been made for you. So we have created a class named MutationPage and returnded the AppUI widget as its widget. We have also initialsed callback functions for our Text Fields such that Text in first textField will be stored in langName, second one in saveFormat and objectId from the last. Now proceed to main.dart and add a floatingActionButton parameter in Scaffold() widget of MyHomePage class and pass the following code into it:

```dart
1   floatingActionButton: Row(
2             mainAxisAlignment: MainAxisAlignment.end,
3             children: [
4               FloatingActionButton(
5                 heroTag: 'mutation_page',
6                 child: Text('M',
7                 style: TextStyle(
8                   color: Colors.white,
9                 ),
10                ),
11                onPressed: (){
12                  Navigator.pushReplacement(context, MaterialPageRoute(
13                    builder: ((context){
14                      return MutationPage();
15                    })
16                  ));
17                },
18              ),
19            ],
20          ),
```

This will create a Floating Button that will Navigate us to the MutationPage() from our Home page. So now our GUI is set. You can now Hot Restart your App to see the GUI. This is how your main.dart should look like:

```dart
1   import 'package:back4appgraphqldemo/mutation_page.dart';
2   import 'package:flutter/material.dart';
3   import 'package:graphql_flutter/graphql_flutter.dart';
4   import 'consonents.dart';
5   import 'dart:ui';
6
7   void main() {
8     runApp(MyApp());
9   }
10
11  class MyApp extends StatelessWidget {
12    @override
13    Widget build(BuildContext context) {
14      final HttpLink httpLink = HttpLink(
15        uri: 'https://parseapi.back4app.com/graphql',
16        headers: {
17          'X-Parse-Application-Id': kParseApplicationId,
18          'X-Parse-Client-Key': kParseClientKey,
19          'X-Parse-Master-Key': kParseMasterKey,
20          //'X-Parse-REST-API-Key' : kParseRestApiKey,
21        }, //getheaders()
22      );
23
24      ValueNotifier<GraphQLClient> client = ValueNotifier(
25        GraphQLClient(
26          cache: OptimisticCache(dataIdFromObject: typenameDataIdFromObject),
27          link: httpLink,
28        ),
29      );
30  
31      return MaterialApp(
32        home: GraphQLProvider(
33          child: MyHomePage(),
34          client: client,
35        ),
36      );
37    }
38  }
39
40  class MyHomePage extends StatefulWidget {
41    @override
42    _MyHomePageState createState() => _MyHomePageState();
43  }
44
45  class _MyHomePageState extends State<MyHomePage> {
46    String name;
47    String saveFormat;
48    String objectId;
49  
50    String query = '''
51    query FindLanguages{
52    languages{
53      count,
54      edges{
55        node{
56          name,
57          saveFormat
58        }
59      }
60    }
61  }
62    ''';
63  
64    @override
65    Widget build(BuildContext context) {
66      return SafeArea(
67        child: Scaffold(
68          appBar: AppBar(
69            title: Text(
70              'Parsing data using GraphQL',
71            ),
72          ),
73          floatingActionButton: Row(
74            mainAxisAlignment: MainAxisAlignment.end,
75            children: [
76              FloatingActionButton(
77                heroTag: 'mutation_page',
78                child: Text('M',
79                style: TextStyle(
80                  color: Colors.white,
81                ),
82                ),
83                onPressed: (){
84                  Navigator.pushReplacement(context, MaterialPageRoute(
85                    builder: ((context){
86                      return MutationPage();
87                    })
88                  ));
89                },
90              ),
91            ],
92          ),
93          body: Query(
94            options: QueryOptions(
95              documentNode: gql(query),
96            ),
97            builder: (
98              QueryResult result, {
99              Refetch refetch,
100             FetchMore fetchMore,
101           }) {
102             if (result.data == null) {
103               return Center(
104                   child: Text(
105                 "Loading...",
106                 style: TextStyle(fontSize: 20.0),
107               ));
108             } else {
109               return ListView.builder(
110                 itemBuilder: (BuildContext context, int index) {
111                   return ListTile(
112                     title: Text(result.data["languages"]["edges"][index]["node"]
113                         ['name']),
114                     trailing: Text(result.data["languages"]["edges"][index]
115                         ["node"]['saveFormat']),
116 
117                   );
118                 },
119                 itemCount: result.data["languages"]["edges"].length,
120               );
121             }
122           },
123         ),
124       ),
125     );
126   }
127 }
```

## 2 -  Creating/adding data to the database

If you proceed to graphql\_configration.dart you could see that we have already set our GraphQLclient and now we can use it anywhere. Let’s proceed to and create a file database\_utils.dart and perform an operation for **Creating** data. Create a class DatabaseUtils\{} and create a constructor that would receive the data parameters we would work on, here we will require langName,saveFormat, and objectId:

```dart
1   import 'package:back4appgraphqldemo/graphql_configration.dart';
2   import 'package:graphql_flutter/graphql_flutter.dart';
3
4   class DatabaseUtils{
5     final String langName,saveFormat,objectId;
6     DatabaseUtils({this.langName="",this.saveFormat="",this.objectId=""});
7   }
```

Create a functiion addData() which will be an asynchronous function to Create data and initialse our GraphQLClient by initialsing GraphQLConfigration class. Paste the following code into sendData() function:

```dart
1    Future<QueryResult> sendData() async{
2        String addData='''
3         mutation CreateObject(\$input: CreateLanguageFieldsInput){
4           createLanguage(input: {fields: \$input}){
5             language{
6               name,
7               saveFormat
8             }
9           }
10        }
11         ''';
12        final variable ={
13       "input":{
14         "name" : langName,
15         "saveFormat" : saveFormat,
16       }
17     };
18        
19      GraphQlConfiguration configuration = GraphQlConfiguration();
20     GraphQLClient client = configuration.clientToQuery();
21   
22     }
```

Here we have initialized a variable addData and have passed the query to create data and initialized variable that will pass the query Variables. We also initialized the GraphQLClient that will help us to pass queries. We can pass the queries in the manner below:

```dart
1   QueryResult queryResult = await client.query(
2        QueryOptions(documentNode: gql(addData), variables: variable),
3      );
4      return queryResult;
```

We used our GraphQLClient instance to write a query that accepts QueryOptions() that helps us to send a query as you have seen from the last tutorial. The result is stored in queryResult.
This is how your database\_utils.dart should look like:

```dart
1   import 'package:back4appgraphqldemo/graphql_configration.dart';
2   import 'package:graphql_flutter/graphql_flutter.dart';
3
4   class DatabaseUtils{
5     final String langName,saveFormat,objectId;
6     DatabaseUtils({this.langName="",this.saveFormat="",this.objectId=""});
7     Future<QueryResult> sendData() async{
8       String addData='''
9         mutation CreateObject(\$input: CreateLanguageFieldsInput){
10          createLanguage(input: {fields: \$input}){
11            language{
12              name,
13              saveFormat
14            }
15          }
16        }
17        ''';
18      final variable ={
19        "input":{
20          "name" : langName,
21          "saveFormat" : saveFormat,
22         }
23      };
24 
25      GraphQlConfiguration configuration = GraphQlConfiguration();
26      GraphQLClient client = configuration.clientToQuery();
27
28      QueryResult queryResult = await client.query(
29        QueryOptions(documentNode: gql(addData), variables: variable),
30      );
31      return queryResult;
32    }
33  }
```

Now proceed to your UI class mutation\_page.dart. Lets code for send data button which can be coded inside the sendDataButtonPressed: parameter. Since we need the langName and saveFormat first check if it is not empty and then Create an instance of DatabaseUtils and the pass the langName and saveFormat parameter.

```dart
1   if(langName.isNotEmpty && saveFormat.isNotEmpty){
2             utils = DatabaseUtils(
3               langName: langName,
4               saveFormat: saveFormat ,
5             );
6           }
```

After this call the sendData() function from the DatabaseUtils instance.

:::BlockQuote
util&#x73;**.**&#x73;endData();
:::

Now you can **Hot Restart** app, fill the two text fields with their respective data and press the send data button. Now go back to your Query page by pressing the floating action button and you could see one more data is added to our table. This is how your MutationPage class would look like:

```dart
1   import 'package:back4appgraphqldemo/app_ui.dart';
2   import 'package:back4appgraphqldemo/database_utils.dart';
3   import 'package:flutter/material.dart';
4
5   class MutationPage extends StatelessWidget {
6 
7     String langName,saveFormat,objectId;
8     DatabaseUtils utils;
9
10    @override
11    Widget build(BuildContext context) {
12      return AppUI(
13        onChangedName: (text){
14        langName=text;
15        },
16        onChangedSaveFormat: (text){
17                saveFormat=text;
18          },
19        onChangedObjectId: (text){
20        objectId=text;
21        },
22        sendDataButtonPressed: (){
23        if(langName.isNotEmpty && saveFormat.isNotEmpty){
24            utils = DatabaseUtils(
25              langName: langName,
26              saveFormat: saveFormat ,
27            );
28            utils.sendData();
29          }
30        },
31        deleteDataButtonPressed: (){
32        },
33        updateButtonPressed: (){
34        },
35      );
36    }
37  }
```

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/MR8HfB7BOEW99Nko0Jpwz_flutter-createdata-1.gif" signedSrc size="50" width="270" height="480" position="center" caption}

## 3 - Updating Data

In DatabaseUtils create a Future function updateData(). Initialise a String update and pass in the update query and *query variables* in final variables:

```dart
1    Future<QueryResult> updateData() async{
2     String update='''
3     mutation UpdateObject(\$id: ID!,\$input: UpdateLanguageFieldsInput){
4       updateLanguage(input: {id:\$id, fields:\$input}){
5         language{
6           name,
7           id
8         }
9       }
10    }
11    ''';
12     final variable={
13       "id":objectId,
14       "input":{
15         "name" : langName
16       }
17     };
18   }
```

Now initialse our GraphQLClient and send the query through QueryOptions(). This is how your code would look like:

```dart
1   Future<QueryResult> updateData() async{
2 
3      String update='''
4       mutation UpdateObject(\$id: ID!,\$input: UpdateLanguageFieldsInput){
5         updateLanguage(input: {id:\$id, fields:\$input}){
6          language{
7             name,
8             id
9           }
10        }
11      }
12      ''';
13   
14     final variable={
15       "id":objectId,
16       "input":{
17         "name" : langName
18       }
19     };
20  
21     GraphQlConfiguration configuration = GraphQlConfiguration();
22     GraphQLClient client = configuration.clientToQuery();
23  
24     QueryResult queryResult = await client.query(
25       QueryOptions(documentNode: gql(update), variables: variable),
26    );
27     return queryResult;
28   }
```

Now come back to mutaion\_page.dart and code in the updateButtonPressed: parameter. Check if langName, objectId and saveFormat are not empty and then call the updateData() funtion from DatabaseUtils class.

```dart
1    updateButtonPressed: (){
2           if(langName.isNotEmpty && saveFormat.isNotEmpty && objectId.isNotEmpty){
3             utils = DatabaseUtils(
4               langName: langName,
5               saveFormat: saveFormat ,
6               objectId: objectId
7             );
8             utils.updateData();
9           }
10        },
```

Go to Back4App Dashboard and choose a language to update, then copy its objectID. **Hot restart** your app and fill all the 3 text fields: the new **name** of the language you want to insert in first text field and the new **save Format** in second and **objectId** in third . Now press the Update data button and check the updated information on the App by clicking over the Q floating action button on bottom right.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/Dhk13aMGmSxLvzbop-BuN_flutter-updatedata.gif" signedSrc size="50" width="237" height="432" position="center" caption}

## 4 - Deleting data

Create a deleteData() **async** function in DatabaseUtils and initialize String delete and pass the GraphQL query to delete data. Take final variables and pass the query variables into it.

```dart
1   Future<QueryResult> deleteData() async{
2       String delete='''
3     mutation DeleteObject(\$id: ID!){
4       deleteLanguage(input: {id:\$id}){
5         language{
6           name,
7           id
8         }
9       }
10    }
11    ''';
12     final variable={
13       "id":objectId,
14     };
15   }
```

In this, we only require the objectId of the row that needs to be deleted. Initialize the GraphQLClient and send the query through QueryOptions().

```dart
1   Future<QueryResult> deleteData() async{
2        String delete='''
3     mutation DeleteObject(\$id: ID!){
4       deleteLanguage(input: {id:\$id}){
5         language{
6           name,
7           id
8         }
9       }
10    }
11    ''';
12     final variable={
13       "id":objectId,
14     };
15
16     GraphQlConfiguration configuration = GraphQlConfiguration();
17     GraphQLClient client = configuration.clientToQuery();
18  
19     QueryResult queryResult = await client.query(
20       QueryOptions(documentNode: gql(delete), variables: variable),
21     );
22
23     return queryResult;
24   }
```

In MutationPage in the deleteDataButtonPressed: parameter check if objectId is not Empty or null and call the deleteData() function. **Hot Restart** application, enter the **objectId** of the row to be deleted and press the **Delete Data** button. It should delete a specific row from your Language class.

::Image[]{src="https://api.archbee.com/api/optimize/yD3zCY-NNBBIfd0uqcfR5/cFrVVPxzehrwhzb9yosaD_flutter-deletedata.gif" signedSrc size="50" width="270" height="480" position="center" caption}

***SUCCESS*** your app has finally done your mutation operations !!!

main.dart should look like this:

```dart
1   import 'package:back4appgraphqldemo/mutation_page.dart';
2   import 'package:flutter/material.dart';
3   import 'package:graphql_flutter/graphql_flutter.dart';
4   import 'consonents.dart';
5   import 'dart:ui';
6
7   void main() {
8     runApp(MyApp());
9   }
10
11  class MyApp extends StatelessWidget {
12    @override
13    Widget build(BuildContext context) {
14      final HttpLink httpLink = HttpLink(
15        uri: 'https://parseapi.back4app.com/graphql',
16        headers: {
17          'X-Parse-Application-Id': kParseApplicationId,
18          'X-Parse-Client-Key': kParseClientKey,
19          'X-Parse-Master-Key': kParseMasterKey,
20          //'X-Parse-REST-API-Key' : kParseRestApiKey,
21        }, //getheaders()
22      );
23  
24      ValueNotifier<GraphQLClient> client = ValueNotifier(
25        GraphQLClient(
26          cache: OptimisticCache(dataIdFromObject: typenameDataIdFromObject),
27          link: httpLink,
28        ),
29      );
30  
31      return MaterialApp(
32        home: GraphQLProvider(
33          child: MyHomePage(),
34          client: client,
35        ),
36      );
37   }
38  }
39  
40  class MyHomePage extends StatefulWidget {
41    @override
42    _MyHomePageState createState() => _MyHomePageState();
43  }
44 
45  class _MyHomePageState extends State<MyHomePage> {
46    String name;
47    String saveFormat;
48    String objectId;
49
50    String query = '''
51    query FindLanguages{
52    languages{
53      count,
54      edges{
55        node{
56          name,
57          saveFormat
58        }
59      }
60    }
61  }
62    ''';
63  
64    @override
65    Widget build(BuildContext context) {
66      return SafeArea(
67        child: Scaffold(
68          appBar: AppBar(
69            title: Text(
70              'Parsing data using GraphQL',
71            ),
72          ),
73          floatingActionButton: Row(
74            mainAxisAlignment: MainAxisAlignment.end,
75            children: [
76              FloatingActionButton(
77                heroTag: 'mutation_page',
78                child: Text('M',
79                style: TextStyle(
80                  color: Colors.white,
81                ),
82                ),
83                onPressed: (){
84                  Navigator.pushReplacement(context, MaterialPageRoute(
85                    builder: ((context){
86                      return MutationPage();
87                    })
88                  ));
89                },
90              ),
91            ],
92          ),
93          body: Query(
94            options: QueryOptions(
95              documentNode: gql(query),
96            ),
97            builder: (
98              QueryResult result, {
99              Refetch refetch,
100             FetchMore fetchMore,
101           }) {
102             if (result.data == null) {
103               return Center(
104                   child: Text(
105                 "Loading...",
106                 style: TextStyle(fontSize: 20.0),
107               ));
108             } else {
109               return ListView.builder(
110                 itemBuilder: (BuildContext context, int index) {
111                   return ListTile(
112                     title: Text(result.data["languages"]["edges"][index]["node"]
113                         ['name']),
114                     trailing: Text(result.data["languages"]["edges"][index]
115                         ["node"]['saveFormat']),
116 
117                   );
118                 },
119                 itemCount: result.data["languages"]["edges"].length,
120              );
121             }
122           },
123         ),
124       ),
125     );
126   }
127 }
```

database\_utils.dart should like this:

```dart
1   import 'package:back4appgraphqldemo/graphql_configration.dart';
2   import 'package:graphql_flutter/graphql_flutter.dart';
3
4   class DatabaseUtils{
5
6     final String langName,saveFormat,objectId;
7
8     DatabaseUtils({this.langName="",this.saveFormat="",this.objectId=""});
9
10    String delete='''
11    mutation DELETE_LANGUAGES(\$id: ID!){
12      deleteLanguage(input: {id:\$id}){
13        language{
14          name,
15          id
16        }
17      }
18    }
19    ''';
20  
21    String addData='''
22    mutation CREATE_LANGUAGES(\$input: CreateLanguageFieldsInput){
23      createLanguage(input: {fields: \$input}){
24        language{
25          name,
26          saveFormat
27        }
28      }
29    }
30    ''';
31    String update='''
32    mutation UPDATE_LANGUAGES(\$id: ID!,\$input: UpdateLanguageFieldsInput){
33      updateLanguage(input: {id:\$id, fields:\$input}){
34        language{
35          name,
36          id
37        }
38      }
39    }
40    ''';
41
42   Future<QueryResult> sendData() async{
43
44     final variable ={
45       "input":{
46         "name" : langName,
47         "saveFormat" : saveFormat,
48       }
49     };
50     print('sendingData');
51  
52      GraphQlConfiguration configuration = GraphQlConfiguration();
53     GraphQLClient client = configuration.clientToQuery();
54  
55     QueryResult queryResult = await client.query(
56       QueryOptions(documentNode: gql(addData), variables: variable),
57     );
58     return queryResult;
59  
60   }
61   Future<QueryResult> updateData() async{
62     final variable={
63       "id":objectId,
64       "input":{
65         "name" : langName
66       }
67     };
68  
69     GraphQlConfiguration configuration = GraphQlConfiguration();
70     GraphQLClient client = configuration.clientToQuery();
71  
72     QueryResult queryResult = await client.query(
73       QueryOptions(documentNode: gql(update), variables: variable),
74     );
75     return queryResult;
76   }
77
78
79   Future<QueryResult> deleteData() async{
80     final variable={
81       "id":objectId,
82     };
83  
84     GraphQlConfiguration configuration = GraphQlConfiguration();
85     GraphQLClient client = configuration.clientToQuery();
86  
87     QueryResult queryResult = await client.query(
88     QueryOptions(documentNode: gql(delete), variables: variable),
89     );
90  
91     return queryResult;
92   }
93  }
```

mutaion\_page.dart should look like this :

```dart
1   import 'package:back4appgraphqldemo/app_ui.dart';
2   import 'package:back4appgraphqldemo/database_utils.dart';
3   import 'package:flutter/material.dart';
4
5   class MutationPage extends StatelessWidget {
6
7     String langName,saveFormat,objectId;
8     DatabaseUtils utils;
9
10    @override
11    Widget build(BuildContext context) {
12      return AppUI(
13        onChangedName: (text){
14          langName=text;
15        },
16        onChangedSaveFormat: (text){
17          saveFormat=text;
18          },
19        onChangedObjectId: (text){
20          objectId=text;
21        },
22
23        sendDataButtonPressed: (){
24          if(langName.isNotEmpty && saveFormat.isNotEmpty){
25            utils = DatabaseUtils(
26              langName: langName,
27              saveFormat: saveFormat ,
28            );
29            utils.sendData();
30          }
31        },
32        deleteDataButtonPressed: (){
33          if(objectId.isNotEmpty){
34            utils = DatabaseUtils(
35              objectId: objectId,
36            );
37            utils.deleteData();
38          }
39        },
40        updateButtonPressed: (){
41          if(langName.isNotEmpty && saveFormat.isNotEmpty && objectId.isNotEmpty){
42            utils = DatabaseUtils(
43              langName: langName,
44              saveFormat: saveFormat ,
45              objectId: objectId
46            );
47            utils.updateData();
48           }
49        },
50      );
51    }
52  }
```

## Conclusion

In this guide we used GraphQL mutations in the Flutter app to:

- **create new objects on Back4App;**
- **update objects on Back4App;**
- **delete objects on Back4App.**

At this point you have a fully functional Flutter GraphQL CRUD project where you can use at starting point to develop your next App. In the next guide we are going to dive deep into queries showing how to make them to retrieve data from Back4App and show on our Flutter App.

**Have a great day!**
